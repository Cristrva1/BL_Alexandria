"""Destacados de 14/aprender, 7/calidad y 32/motores-web (2026-11-16)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PICKS = {"machine-learning-for-trading": (14, "aprender"), "ast-grep": (7, "calidad"), "lightpanda": (32, "motores-web")}


def test_subcategory_picks():
    repos = {r["id"]: r for r in json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))["repos"]}
    for rid, (cat, sub) in PICKS.items():
        assert repos[rid]["pick"] is True and (repos[rid]["cat"], repos[rid]["sub"]) == (cat, sub), rid
    assert repos["swe-bench"]["pick"] is False
    report = json.loads((ROOT / "reports/destacados-subcategorias-2026-11-16.json").read_text(encoding="utf8"))
    assert {p["id"] for p in report["picks"]} == set(PICKS) and all(p["reason"] for p in report["picks"])
