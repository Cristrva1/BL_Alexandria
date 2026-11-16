"""Subcategorías de ciberseguridad (categoría 16) y reubicaciones del 2026-11-16."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"nmap": "reconocimiento", "subfinder": "reconocimiento", "metasploit": "explotacion-c2",
            "bloodhound": "ad-interno", "wazuh": "deteccion", "crowdsec": "deteccion", "trivy": "nube-contenedores"}


def test_security_subcategories_and_moves():
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    cat = next(c for c in compact["categories"] if c["num"] == 16)
    keys = {s["key"] for s in cat["subs"]}
    assert {"reconocimiento", "explotacion-c2", "ad-interno", "deteccion", "nube-contenedores"} <= keys
    repos = {r["id"]: r for r in compact["repos"]}
    for rid, sub in EXPECTED.items():
        assert repos[rid]["sub"] == sub and detail[rid]["sub"] == sub, rid
    area = next(a for a in compact["discovery"]["areas"] if a["id"] == "ciberseguridad")
    selected = {s for t in area["topics"] for sel in t["selectors"] if sel["cat"] == 16 for s in sel["subs"]}
    assert keys <= selected  # toda subcategoría de seguridad aparece en el área práctica
