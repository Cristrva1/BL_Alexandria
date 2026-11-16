"""Remaining n8n ecosystem retired and taxonomy cleaned (2026-11-16)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GONE = {"awesome-n8n-templates", "self-hosted-ai-starter-kit"}
GENERATED = ["README.md", "Guia.md", "Catalogo.md", "human/README.md", "human/areas.md", "human/areas/automatizacion.md",
             "human/categorias/01-automatizaci-n-mensajer-a-crm.md", "menu_portable/REPO_MENU.md", "menu_portable/REPO_AREAS.md",
             "menu_portable/REPO_MENU_cats/01-automatizar-procesos-y-crear-herramientas-internas.md", "human/MANUAL_IA.md"]


def test_n8n_ecosystem_is_retired_and_purged():
    ledger = {r["id"]: r for r in json.loads((ROOT / "data/retired.json").read_text(encoding="utf8"))["repos"]}
    assert GONE <= set(ledger) and all(ledger[i]["reason"] == "editorial" for i in GONE)
    index = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    assert not GONE & {r["id"] for r in index["repos"]} and not GONE & set(detail)
    assert "self-hosted-ai-starter-kit" not in json.dumps(index["discovery"])
    for entry in detail.values():
        assert not GONE & set(entry.get("combines_with") or [])


def test_n8n_subcategory_topic_and_wording_are_gone():
    index = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    cat1 = next(c for c in index["categories"] if c["num"] == 1)
    assert [s["key"] for s in cat1["subs"]] == ["motores", "internas"]
    assert "n8n" not in json.dumps(cat1, ensure_ascii=False).lower() and "Activepieces" in cat1["desc"]
    topics = {t["id"] for a in index["discovery"]["areas"] for t in a["topics"]}
    assert "negocio-n8n" not in topics
    assert all(r.get("sub") != "n8n" for r in index["repos"])
    for rel in GENERATED:
        assert "n8n" not in (ROOT / rel).read_text(encoding="utf8").lower(), rel
    handbook = {r["id"]: r for r in json.loads((ROOT / "data/handbook.json").read_text(encoding="utf8"))["resources"]}
    assert "n8n-servicio" not in handbook and handbook["activepieces-servicio"]["repo_ids"] == ["activepieces"]
