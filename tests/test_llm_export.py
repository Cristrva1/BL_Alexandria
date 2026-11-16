"""Markdown para agentes por categoría y subcategoría (docs/llm/) y su descarga desde el explorador."""
import json
import re
import subprocess
from pathlib import Path

import pytest
from typer.testing import CliRunner

from repo_intelligence.cli import app
from repo_intelligence.llm.export import MAX_TOKENS, estimate_tokens, export_llm, web_manifest
from repo_intelligence.web.build import build_site

ROOT = Path(__file__).resolve().parents[1]
COMPACT = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
DETAIL = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
PUBLIC = [r for r in COMPACT["repos"] if not r.get("alias_of") and int(r.get("cat") or 0) > 0]


@pytest.fixture(scope="module")
def exported(tmp_path_factory):
    out = tmp_path_factory.mktemp("llm")
    return out, export_llm(ROOT, out)


def _text(out, name):
    return (out / name).read_text(encoding="utf8")


def test_one_file_per_category_and_subcategory_under_the_token_limit(exported):
    out, stats = exported
    names = {f["archivo"] for f in stats["manifest"]["archivos"]}
    pairs = {(int(r["cat"]), r["sub"]) for r in PUBLIC}
    assert {f"categoria-{c}.md" for c, _ in pairs} <= names
    assert {f"categoria-{c}-{s}.md" for c, s in pairs} <= names
    assert names == {p.name for p in out.glob("*.md")}
    for f in stats["manifest"]["archivos"]:
        text = _text(out, f["archivo"])
        assert estimate_tokens(text) == f["tokens_estimados"] <= MAX_TOKENS, f["archivo"]
    assert json.loads(_text(out, "index.json"))["archivos"] == stats["manifest"]["archivos"]


def test_every_public_repo_has_one_ficha_per_subcategory_file(exported):
    out, _ = exported
    for r in PUBLIC:
        text = _text(out, f"categoria-{r['cat']}-{r['sub']}.md")
        assert text.count(f"(`{r['id']}`)\n") == 1, r["id"]
        assert f"| `{r['id']}` |" in text, r["id"]


def test_agent_instructions_table_and_snippet(exported):
    out, _ = exported
    text = _text(out, "categoria-16-deteccion.md")
    for needle in ("## Instrucciones para el agente", "Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita",
                   "## Tabla de decisión", "| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |", "## Fichas",
                   "## Cómo referenciarlo desde AGENTS.md o CLAUDE.md", "docs/alexandria/categoria-16-deteccion.md",
                   "@docs/alexandria/categoria-16-deteccion.md"):
        assert needle in text, needle


def test_install_commands_only_from_catalog(exported):
    out, _ = exported
    for r in PUBLIC:
        gs = DETAIL[r["id"]].get("getting_started") or {}
        text = _text(out, f"categoria-{r['cat']}-{r['sub']}.md")
        block = text.split(f"(`{r['id']}`)\n", 1)[1].split("\n### ", 1)[0]
        if gs.get("command_status") == "documented" and gs.get("command"):
            assert "documentada en la fuente; no ejecutada" in block, r["id"]
            assert gs["command"].strip().splitlines()[0] in block, r["id"]
        else:
            assert "sin comando en el catálogo; ver README oficial" in block, r["id"]


def test_dual_use_and_licence_flags(exported):
    out, _ = exported
    assert "Herramienta ofensiva: solo con autorización escrita" in _text(out, "categoria-16-explotacion-c2.md")
    assert "Uso dual: solo contra sistemas propios" in _text(out, "categoria-16-reconocimiento.md")
    vault = next(r for r in PUBLIC if r["id"] == "vault")
    assert "BSL (source-available)" in _text(out, f"categoria-{vault['cat']}-{vault['sub']}.md")
    assert "Elastic License 2.0" in _text(out, "categoria-16-deteccion.md")


def test_large_categories_are_split_into_parts(exported):
    out, stats = exported
    index = next(f for f in stats["manifest"]["archivos"] if f["archivo"] == "categoria-16.md")
    assert len(index["partes"]) >= 2
    text = _text(out, "categoria-16.md")
    assert "## Partes" in text and "## Fichas" not in text
    ids = [r["id"] for r in PUBLIC if int(r["cat"]) == 16]
    joined = "".join(_text(out, p) for p in index["partes"])
    for rid in ids:
        assert joined.count(f"(`{rid}`)\n") == 1, rid
        assert f"| `{rid}` |" in text, rid


def test_published_docs_llm_matches_a_fresh_export(exported):
    out, _ = exported
    published = ROOT / "docs" / "llm"
    assert {p.name for p in published.iterdir()} == {p.name for p in out.iterdir()}
    for p in out.iterdir():
        assert (published / p.name).read_text(encoding="utf8") == p.read_text(encoding="utf8"), p.name


def test_web_build_ships_files_and_manifest(tmp_path):
    build_site(ROOT, tmp_path)
    catalog = json.loads((tmp_path / "catalog.json").read_text(encoding="utf8"))
    entry = catalog["llm"]["16/deteccion"]
    assert entry["file"] == "llm/categoria-16-deteccion.md" and (tmp_path / entry["file"]).is_file()
    assert catalog["llm"]["16"]["parts"] and all((tmp_path / p).is_file() for p in catalog["llm"]["16"]["parts"])
    for cat in catalog["categories"]:
        if cat["num"] > 0 and cat.get("count"):
            assert str(cat["num"]) in catalog["llm"], cat["num"]
    assert "llmDownload(category" in (tmp_path / "app.js").read_text(encoding="utf8")


def test_download_button_markup_in_browser_logic():
    app_js = (ROOT / "src/repo_intelligence/web/assets/app.js").read_text(encoding="utf8")
    fn = re.search(r"  function llmDownload\(category, subKey\) \{.*?\n  \}\n", app_js, re.S).group(0)
    script = r'''
const assert=require('node:assert/strict');
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c]);
const catalog={llm:{"16":{file:"llm/categoria-16.md",tokens:5200,parts:["llm/categoria-16-parte-1.md","llm/categoria-16-parte-2.md"]},
  "16/deteccion":{file:"llm/categoria-16-deteccion.md",tokens:4800,parts:[]}}};
''' + fn + r'''
const cat={num:16,title:"Seguridad",subs:[{key:"deteccion",title:"Detección"},{key:"otra",title:"Otra"}]};
const sub=llmDownload(cat,"deteccion");
assert.match(sub,/href="llm\/categoria-16-deteccion.md" download/);
assert.match(sub,/Detección · ~5k tokens/);
const whole=llmDownload(cat,null);
assert.match(whole,/href="llm\/categoria-16.md" download/);
assert.match(whole,/categoria-16-parte-2.md/);
assert.equal(llmDownload(cat,"otra"),"");
assert.equal(llmDownload(null,null),"");
'''
    result = subprocess.run(["node", "-e", script], capture_output=True, text=True, encoding="utf8")
    assert result.returncode == 0, result.stderr


def test_cli_llm_export(tmp_path, monkeypatch):
    monkeypatch.chdir(ROOT)
    result = CliRunner().invoke(app, ["llm", "export", "-o", str(tmp_path)])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "categoria-1.md").is_file() and "archivos" in result.output
    assert web_manifest(json.loads((tmp_path / "index.json").read_text(encoding="utf8")))["1"]["file"] == "llm/categoria-1.md"
