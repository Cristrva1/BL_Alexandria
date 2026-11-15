import json
import re
import threading
import urllib.request
from pathlib import Path

from repo_intelligence.web.build import build_site, make_server
from repo_intelligence.web.catalog import build_catalog
from repo_intelligence.web.lessons import CATEGORY_LESSONS, RECIPE_LESSONS


def _write_indices(root: Path, *, one: str = "n8n is a workflow automation platform.", desc: str = "Orquesta flujos con nodos y puede llamar a un modelo.") -> None:
    compact = {
        "categories": [
            {"num": 1, "title": "Automatización", "count": 1},
            {"num": 9, "title": "Diseño", "count": 1},
        ],
        "recipes": [
            {
                "id": "bot-de-whatsapp-con-ia",
                "title": "Bot de WhatsApp con IA",
                "goal": "atención por WhatsApp",
                "repos": ["n8n"],
                "how": "n8n enruta y llama al LLM",
            },
            {
                "id": "web-app-moderna-con-ia",
                "title": "Web app moderna con IA",
                "goal": "construir frontend",
                "repos": ["threejs"],
                "how": None,
            },
        ],
        "model_guidance": {
            "key_distinction": "Separa el agente con el que programas del modelo que llama la app.",
            "tools": {"grok": {"best_fit_repos": [], "note": "Proveedor en runtime."}},
        },
        "repos": [
            {
                "id": "n8n",
                "name": "n8n",
                "cat": 1,
                "role": "library",
                "exec": "local",
                "setup": "easy",
                "mcp": False,
                "prov": ["openai"],
                "tags": ["automation"],
                "one": one,
                "alt": ["activepieces"],
                "doc": "human/fichas/n8n.md",
            },
            {
                "id": "three.js",
                "name": "three.js",
                "cat": 9,
                "role": "library",
                "exec": "local",
                "setup": "medium",
                "mcp": False,
                "prov": [],
                "tags": [],
                "one": "Biblioteca 3D para la web, para escenas y no para animar botones.",
                "alt": [],
            },
        ],
    }
    detalle = {
        "repos": {
            "n8n": {
                "desc": desc,
                "stack": "python",
                "repo": "https://github.com/n8n-io/n8n",
                "choose_if": "quieres orquestar flujos en self-host",
                "avoid_if": "no quieres operar un servicio",
                "combines_with": ["chatwoot"],
            },
            "three.js": {
                "desc": "three.js dibuja escenas 3D en el navegador.",
                "stack": "javascript",
                "repo": "https://github.com/mrdoob/three.js",
                "choose_if": "la pantalla necesita una escena 3D",
                "avoid_if": "solo vas a animar interfaz plana",
                "combines_with": [],
            },
        }
    }
    (root / "INDICE_IA.json").write_text(json.dumps(compact), encoding="utf-8")
    (root / "INDICE_IA.detalle.json").write_text(json.dumps(detalle), encoding="utf-8")


def test_catalog_merges_detail_install_and_aliases(tmp_path: Path) -> None:
    _write_indices(tmp_path)
    catalog = build_catalog(tmp_path)

    n8n = next(repo for repo in catalog["repos"] if repo["id"] == "n8n")
    assert "instalación original" in n8n["install"]["command"]
    assert "pip install" not in n8n["install"]["command"]
    assert n8n["choose_if"].startswith("quieres orquestar")
    assert n8n["lead"].startswith("n8n is a workflow")

    web = next(recipe for recipe in catalog["recipes"] if recipe["id"] == "web-app-moderna-con-ia")
    assert web["steps"][0]["id"] == "three.js"
    assert web["steps"][0]["missing"] is False
    assert "escena" in web["steps"][0]["why"]

    whatsapp = next(recipe for recipe in catalog["recipes"] if recipe["id"] == "bot-de-whatsapp-con-ia")
    assert whatsapp["steps"][0]["why"].startswith("El flujo")
    assert catalog["counts"]["categories"] == 2


def test_junk_readme_falls_back_to_curated_criterion(tmp_path: Path) -> None:
    _write_indices(
        tmp_path,
        one="Important Notice: this project has no official cryptocurrency or token.",
        desc="⚠️ Important Notice: any token on pump.fun is not affiliated with this project.",
    )
    catalog = build_catalog(tmp_path)
    n8n = next(repo for repo in catalog["repos"] if repo["id"] == "n8n")
    assert n8n["body"] == ""
    assert "orquestar flujos" in n8n["lead"]


def test_site_inlines_catalog_and_escapes_script(tmp_path: Path) -> None:
    _write_indices(tmp_path, desc="</script><script>alert(1)</script>")
    out = tmp_path / "web"
    stats = build_site(tmp_path, out)

    html = (out / "index.html").read_text(encoding="utf-8")
    assert stats["repos"] == 2
    assert "<script>alert" not in html
    assert "\\u003c/script\\u003e" in html
    match = re.search(
        r'<script id="catalog-data" type="application/json">(.*?)</script>',
        html,
        re.DOTALL,
    )
    assert match is not None
    data = json.loads(match.group(1))
    n8n = next(repo for repo in data["repos"] if repo["id"] == "n8n")
    assert n8n["desc"] == "</script><script>alert(1)</script>"
    assert (out / "app.js").exists()
    assert (out / "styles.css").exists()


def test_site_ships_binarias_labs_brand(tmp_path: Path) -> None:
    _write_indices(tmp_path)
    out = tmp_path / "web"
    build_site(tmp_path, out)

    html = (out / "index.html").read_text(encoding="utf-8")
    app = (out / "app.js").read_text(encoding="utf-8")
    assert 'href="marca/favicon.png"' in html
    assert 'href="marca/apple-touch-icon.png"' in html
    for name in ("binarias-labs.png", "binarias-labs-dark.png", "bl-mark-dark.png", "favicon.png", "apple-touch-icon.png"):
        path = out / "marca" / name
        assert path.read_bytes().startswith(b"\x89PNG"), name
        assert f"marca/{name}" in html + app or name in ("favicon.png", "apple-touch-icon.png")
    assert 'alt="Binarias Labs"' in app


def test_server_serves_the_site(tmp_path: Path) -> None:
    _write_indices(tmp_path)
    out = tmp_path / "web"
    build_site(tmp_path, out)
    httpd, url = make_server(out, 0)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            assert response.status == 200
            assert "Alejandría" in body
            assert "n8n" in body
        with urllib.request.urlopen(url + "app.js") as response:
            assert response.status == 200
            assert "Explorar" in response.read().decode("utf-8")
        with urllib.request.urlopen(url + "styles.css") as response:
            assert response.status == 200
    finally:
        httpd.shutdown()
        httpd.server_close()


def test_real_library_catalog_resolves_every_recipe_step() -> None:
    root = Path(__file__).resolve().parents[1]
    if not (root / "INDICE_IA.json").exists():
        return
    catalog = build_catalog(root)
    ids = {repo["id"] for repo in catalog["repos"]}
    assert catalog["counts"]["repos"] == len(ids)
    public_categories = [cat for cat in catalog["categories"] if cat["num"] > 0]
    assert catalog["counts"]["categories"] == len(public_categories)
    for category in public_categories:
        assert category["description"]
    import json

    source_recipes = json.loads((root / "INDICE_IA.json").read_text(encoding="utf-8"))["recipes"]
    sources = {recipe["id"]: recipe for recipe in source_recipes}
    assert {recipe["id"] for recipe in catalog["recipes"]} == set(sources)
    for recipe in catalog["recipes"]:
        assert recipe["lesson"]
        assert recipe["steps"]
        assert [step["id"] for step in recipe["steps"]] == sources[recipe["id"]]["repos"]
        for step in recipe["steps"]:
            assert step["id"] in ids
            assert step["missing"] is False
            assert step["why"]
    pairs = {tuple(sorted((lab["a"], lab["b"]))) for lab in catalog["labs"]}
    assert ("heroui", "ui") in pairs
    assert ("comfyui", "fooocus") in pairs
    assert ("ppt-master", "reveal.js") in pairs
    assert len(pairs) >= 10
