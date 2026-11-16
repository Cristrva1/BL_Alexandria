"""Informe de simetría de `combina_con` (solo avisa; no falla).

Una combinación A→B es asimétrica cuando B ya tiene descripción en 4 secciones y no menciona a A.
No toda combinación debe ser simétrica (p. ej., una skill que depende de una plataforma),
pero cada caso merece revisión editorial cuando la cobertura esté completa.

Uso: uv run python scripts/report_combina_simetria.py [--json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def asymmetries(detail: dict) -> list[tuple[str, str]]:
    repos = detail.get("repos", {})
    curated = {rid: [c["id"] for c in entry.get("combina_con") or []] for rid, entry in repos.items() if entry.get("combina_con")}
    pairs = []
    for rid, ids in curated.items():
        for other in ids:
            if other in curated and rid not in curated[other]:
                pairs.append((rid, other))
    return sorted(pairs)


def coverage(detail: dict, compact: dict) -> tuple[int, int]:
    public = [r["id"] for r in compact["repos"] if not r.get("alias_of") and int(r.get("cat") or 0) > 0]
    done = [rid for rid in public if detail["repos"].get(rid, {}).get("combina_con")]
    return len(done), len(public)


def main() -> int:
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    pairs = asymmetries(detail)
    done, total = coverage(detail, compact)
    if "--json" in sys.argv:
        print(json.dumps({"coverage": [done, total], "asymmetric": pairs}, ensure_ascii=False, indent=1))
        return 0
    print(f"Cobertura 4 secciones: {done}/{total}")
    print(f"Combinaciones asimétricas entre repos ya descritos: {len(pairs)}")
    for a, b in pairs:
        print(f"  {a} → {b} (falta {b} → {a})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
