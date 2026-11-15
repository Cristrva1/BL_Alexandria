import json
from pathlib import Path

from repo_intelligence.menu.export import export_menu


def _write_indices(root: Path) -> None:
    compact = {
        "categories": [
            {
                "num": 1,
                "title": "Automatización, Mensajería & CRM",
                "file": "human/categorias/01.md",
                "count": 1,
            }
        ],
        "recipes": [
            {
                "id": "bot-whatsapp",
                "title": "Bot de WhatsApp con IA",
                "goal": "atención por WhatsApp",
                "repos": ["n8n"],
                "how": "n8n enruta y llama al LLM",
            }
        ],
        "model_guidance": {
            "key_distinction": (
                "Separa el AGENTE/IDE con el que CONSTRUYES del LLM que tu APP llama EN EJECUCIÓN."
            ),
            "tools": {
                "claude-code": {"best_fit_repos": ["n8n-skills"]},
                "grok": {
                    "best_fit_repos": [],
                    "note": "Sin repos específicos; úsalo como proveedor LLM en runtime.",
                },
            },
        },
        "repos": [
            {
                "id": "n8n",
                "name": "n8n",
                "cat": 1,
                "role": "platform",
                "exec": "local",
                "setup": "medium",
                "mcp": False,
                "prov": ["openai"],
                "tags": ["automation", "docker"],
                "one": "n8n is a workflow automation platform.",
                "alt": ["activepieces"],
                "agent_tools": ["claude-code"],
            }
        ],
    }
    detalle = {
        "repos": {
            "n8n": {
                "desc": "This is a much longer README blob that should not appear in the compact index line.",
                "stack": "Node, Docker",
                "repo": "https://github.com/n8n-io/n8n",
                "choose_if": "quieres automatizar flujos",
                "avoid_if": "no quieres self-host",
                "combines_with": ["chatwoot"],
            }
        }
    }
    (root / "INDICE_IA.json").write_text(json.dumps(compact), encoding="utf-8")
    (root / "INDICE_IA.detalle.json").write_text(json.dumps(detalle), encoding="utf-8")


def test_export_menu_mirrors_agents_protocol(tmp_path: Path) -> None:
    _write_indices(tmp_path)
    out = tmp_path / "menu_portable"
    stats = export_menu(tmp_path, out)

    assert stats["repos"] == 1
    menu = (out / "REPO_MENU.md").read_text(encoding="utf-8")
    protocol = menu.split("## Recetas")[0]

    assert "`tags`" in protocol
    assert "`prov`" in protocol
    assert "`agent_tools`" in protocol
    assert "Considera la herramienta" in protocol
    assert "Claude Code" in protocol

    n8n_line = next(line for line in menu.splitlines() if line.startswith("- `n8n`"))
    assert "n8n is a workflow automation platform." in n8n_line
    assert "README blob" not in n8n_line
    assert "tags: automation,docker" in n8n_line
    assert "prov: openai" in n8n_line
    assert "tools: claude-code" in n8n_line
    assert "alt: activepieces" in n8n_line


def test_export_menu_json_and_category_include_scan_fields(tmp_path: Path) -> None:
    _write_indices(tmp_path)
    out = tmp_path / "menu_portable"
    export_menu(tmp_path, out)

    data = json.loads((out / "REPO_MENU_DATA.json").read_text(encoding="utf-8"))
    repo = data["repos"][0]
    assert repo["id"] == "n8n"
    assert repo["tags"] == ["automation", "docker"]
    assert repo["prov"] == ["openai"]
    assert repo["agent_tools"] == ["claude-code"]
    assert "Filtra por cat/tags/role/exec/setup/prov/one." in data["how_to_use"]

    cat = (out / "REPO_MENU_cats" / "01-automatizaci-n-mensajer-a-crm.md").read_text(
        encoding="utf-8"
    )
    assert "tags=['automation', 'docker']" in cat or "tags=automation,docker" in cat
    assert "claude-code" in cat
    assert "openai" in cat
