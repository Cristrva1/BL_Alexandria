"""Migración fechada: subcategorías de ciberseguridad en la categoría 16 (2026-11-16).

Crea cinco subcategorías con repos ya catalogados y reubica solo los que pertenecen claramente.
`ir-forense` e `inteligencia-amenazas` se crean con sus primeras altas (una subcategoría no puede
quedar vacía). Idempotente: ejecutarlo dos veces no cambia nada.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_SUBS = [
    ("reconocimiento", "Reconocimiento y superficie de ataque"),
    ("explotacion-c2", "Explotación, C2 y post-explotación"),
    ("ad-interno", "Active Directory y red interna"),
    ("deteccion", "Detección, SIEM e IDS"),
    ("nube-contenedores", "Nube, contenedores e IaC"),
]
MOVES = {
    "nmap": ("pruebas", "reconocimiento"),
    "subfinder": ("pruebas", "reconocimiento"),
    "metasploit": ("pruebas", "explotacion-c2"),
    "bloodhound": ("pruebas", "ad-interno"),
    "wazuh": ("defensa", "deteccion"),
    "crowdsec": ("defensa", "deteccion"),
    "trivy": ("defensa", "nube-contenedores"),
}
CAT_DESC = ("Depuradores, descompiladores, análisis de binarios, pruebas de intrusión, detección y seguridad "
            "de nube. Trabaja sobre sistemas propios o con autorización escrita y separa análisis, pruebas activas y defensa.")
TOPICS = [
    {"id": "seguridad-ofensiva", "title": "Pruebas de intrusión autorizadas",
     "description": "Reconocimiento, explotación y Active Directory dentro de un alcance firmado.",
     "selectors": [{"cat": 16, "subs": ["reconocimiento", "explotacion-c2", "ad-interno"]}],
     "repos": [], "keywords": ["pentesting", "red team", "c2"], "reference_repos": []},
    {"id": "seguridad-deteccion", "title": "Detección y respuesta",
     "description": "SIEM, IDS y bloqueo de ataques en sistemas propios.",
     "selectors": [{"cat": 16, "subs": ["deteccion"]}],
     "repos": [], "keywords": ["siem", "ids", "blue team"], "reference_repos": []},
    {"id": "seguridad-nube", "title": "Nube, contenedores e IaC",
     "description": "Revisar imágenes, clústeres y cuentas de nube antes de publicar.",
     "selectors": [{"cat": 16, "subs": ["nube-contenedores"]}],
     "repos": [], "keywords": ["cloud security", "kubernetes", "iac"], "reference_repos": []},
]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf8"))


def save(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf8")


def main() -> None:
    compact_path, detail_path = ROOT / "INDICE_IA.json", ROOT / "INDICE_IA.detalle.json"
    compact, detail_doc = load(compact_path), load(detail_path)
    cat = next(c for c in compact["categories"] if c["num"] == 16)
    keys = [s["key"] for s in cat["subs"]]
    at = keys.index("pruebas") + 1
    for key, title in reversed(NEW_SUBS):
        if key not in keys:
            cat["subs"].insert(at, {"key": key, "title": title})
    cat["desc"] = CAT_DESC
    for repo in compact["repos"]:
        if repo["id"] in MOVES and repo["cat"] == 16:
            repo["sub"] = MOVES[repo["id"]][1]
    for rid, (_, new) in MOVES.items():
        detail_doc["repos"][rid]["sub"] = new
    area = next(a for a in compact["discovery"]["areas"] if a["id"] == "ciberseguridad")
    existing = {t["id"] for t in area["topics"]}
    pruebas = next(t for t in area["topics"] if t["id"] == "seguridad-pruebas")
    pruebas["title"], pruebas["description"] = "Tráfico, pruebas y protección", "Revisar tráfico, aplicaciones web, contraseñas, rendimiento y endurecimiento."
    at = [t["id"] for t in area["topics"]].index("seguridad-pruebas") + 1
    for topic in reversed(TOPICS):
        if topic["id"] not in existing:
            area["topics"].insert(at, topic)
    save(compact_path, compact)
    save(detail_path, detail_doc)
    spec_path = ROOT / "curation/expansion-2026-11-16/p05.json"
    spec = load(spec_path)
    for item in spec["repos"]:
        if item["id"] in MOVES:
            item["sub"] = MOVES[item["id"]][1]
    save(spec_path, spec)
    print("subcategorías:", [s["key"] for s in cat["subs"]])
    print("reubicados:", {k: f"{a} → {b}" for k, (a, b) in MOVES.items()})


if __name__ == "__main__":
    main()
