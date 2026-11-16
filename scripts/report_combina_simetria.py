"""Informe de simetría de `combina_con` según la política de `analysis/combina_policy.py`.

Cada enlace A→B entre repos descritos es recíproco, apunta a un hub (B recibe al menos
HUB_THRESHOLD enlaces) o apunta a un repo saturado (B ya tiene MAX_COMBOS combinaciones).
Cualquier otro caso es una infracción: añade la combinación inversa con fundamento o elimina el enlace.

Uso: uv run python scripts/report_combina_simetria.py [--json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from repo_intelligence.analysis.combina_policy import HUB_THRESHOLD, MAX_COMBOS, classify, combo_map, hubs  # noqa: E402


def asymmetries(detail: dict) -> list[tuple[str, str]]:
    """Enlaces unidireccionales (aceptados o no)."""
    groups = classify(combo_map(detail.get("repos", {})))
    return sorted(groups["hub"] + groups["saturated"] + groups["violation"])


def coverage(detail: dict, compact: dict) -> tuple[int, int]:
    public = [r["id"] for r in compact["repos"] if not r.get("alias_of") and int(r.get("cat") or 0) > 0]
    done = [rid for rid in public if detail["repos"].get(rid, {}).get("combina_con")]
    return len(done), len(public)


def main() -> int:
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    combos = combo_map(detail["repos"])
    groups = classify(combos)
    done, total = coverage(detail, compact)
    if "--json" in sys.argv:
        print(json.dumps({"coverage": [done, total], "hub_threshold": HUB_THRESHOLD, "hubs": sorted(hubs(combos)),
                          **{k: sorted(v) for k, v in groups.items()}}, ensure_ascii=False, indent=1))
        return 0
    print(f"Cobertura 4 secciones: {done}/{total}")
    print(f"Umbral de hub: {HUB_THRESHOLD} enlaces entrantes ({len(hubs(combos))} hubs); máximo por repo: {MAX_COMBOS}")
    print(f"Recíprocas: {len(groups['reciprocal'])} enlaces")
    print(f"Unidireccionales aceptadas hacia hubs: {len(groups['hub'])}")
    print(f"Unidireccionales aceptadas hacia repos saturados: {len(groups['saturated'])}")
    print(f"Infracciones: {len(groups['violation'])}")
    for a, b in groups["violation"]:
        print(f"  {a} → {b} (falta {b} → {a} o eliminar el enlace)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
