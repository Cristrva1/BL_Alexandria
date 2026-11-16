"""Decisiones del 2026-11-15: grupos de alternativas mutuas y pdfding con forja canónica en Codeberg."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = [
    ["no-ai-slop", "humanizer", "stop-slop"],
    ["claude-seo", "geo-seo-claude"],
    ["ui-ux-pro-max-skill", "taste-skill", "impeccable", "hallmark"],
    ["superclaude-framework", "superpowers", "ecc", "gstack"],
]


def _load():
    compact = {r["id"]: r for r in json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf-8"))["repos"]}
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf-8"))["repos"]
    return compact, detail


def test_alternative_groups_are_symmetric_and_never_combined():
    compact, detail = _load()
    for group in GROUPS:
        for rid in group:
            others = set(group) - {rid}
            assert others <= set(compact[rid]["alt"]), rid
            assert others <= set(detail[rid]["alternatives"]), rid
            assert not others & set(compact[rid].get("combines_with") or []), rid
            assert not others & set(detail[rid].get("combines_with") or []), rid
            assert not others & {c["id"] for c in detail[rid].get("combina_con") or []}, rid


def test_pdfding_points_to_codeberg_and_keeps_github_identity():
    compact, detail = _load()
    repo, card = compact["pdfding"], detail["pdfding"]
    assert repo["repository_host"] == "codeberg" and repo["source_repo"] == "mrmn/PdfDing"
    assert repo["github_archived"] is True and repo["gh"] == "mrmn2/PdfDing" and repo["github_id"]
    assert card["repo"] == "https://codeberg.org/mrmn/PdfDing"
    assert card["editorial_review"]["source"].startswith("https://codeberg.org/mrmn/PdfDing/")
    assert card["editorial_review"]["previous_source"].startswith("https://github.com/mrmn2/PdfDing/")
    assert card["descripcion_origen"]["host"] == "codeberg" and card["descripcion_origen"]["archived"] is False
    assert card["descripcion_github"]["archived"] is True
