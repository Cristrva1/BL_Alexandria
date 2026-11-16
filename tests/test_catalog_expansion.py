"""Ampliación aprobada el 2026-11-16: cada alta por lotes está completa y verificada."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECS = sorted((ROOT / "curation/expansion-2026-11-16").glob("p*.json"))


def _load():
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    return {r["id"]: r for r in compact["repos"]}, detail


def test_every_batch_entry_is_catalogued_with_four_sections_and_sources():
    repos, detail = _load()
    retired = {r["github_id"] for r in json.loads((ROOT / "data/retired.json").read_text(encoding="utf8"))["repos"]}
    seen = set()
    for spec_file in SPECS:
        spec = json.loads(spec_file.read_text(encoding="utf8"))
        for s in spec["repos"]:
            rid = s["id"]
            assert rid not in seen, rid
            seen.add(rid)
            repo, d = repos[rid], detail[rid]
            assert repo["gh"].lower() == s["gh"].lower() and repo["github_id"] not in retired, rid
            assert (repo["cat"], repo["sub"]) == (s["cat"], s["sub"]), rid
            for field in ("que_es", "que_hace", "como_lo_hace", "descripcion_fuentes", "editorial_review", "practical_examples", "first_try"):
                assert d.get(field), (rid, field)
            assert 3 <= len(d["combina_con"]) <= 6, rid
            assert d["descripcion_revision"]["installation_tested"] is False, rid
            assert d["descripcion_github"]["archived"] is False, rid
            assert d["sources"]["collection"] == "catalog-expansion-2026-11-16", rid
            if s.get("caveat"):
                assert s["caveat"] in d["limits"], rid


def test_alternative_groups_are_symmetric_and_not_combined():
    repos, detail = _load()
    for spec_file in SPECS:
        for group in json.loads(spec_file.read_text(encoding="utf8")).get("alt_groups", []):
            for left in group:
                for right in group:
                    if left != right:
                        assert right in repos[left]["alt"], (left, right)
                        assert right not in {c["id"] for c in detail[left]["combina_con"]}, (left, right)
