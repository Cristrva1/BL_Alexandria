"""Avisos de licencia visibles para repos source-available u open-core."""
import json
from pathlib import Path

from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"caido": "no es open source", "vault": "Business Source License 1.1", "wpscan": "licencia de pago",
            "opencti": "Open-core", "prowler": "Open-core"}


def test_license_notes_are_in_detail_ficha_and_web():
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    web = {r["id"]: r for r in build_catalog(ROOT)["repos"]}
    for rid, needle in EXPECTED.items():
        assert needle in detail[rid]["licencia_nota"], rid
        assert web[rid]["licencia_nota"] == detail[rid]["licencia_nota"], rid
        ficha = (ROOT / "human" / "fichas" / f"{rid}.md").read_text(encoding="utf8")
        assert "**Licencia y costes:**" in ficha, rid
    assert "OpenBao" in detail["vault"]["licencia_nota"]
