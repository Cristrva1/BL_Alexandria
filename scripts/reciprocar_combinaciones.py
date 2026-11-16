"""Completa la simetría de `combina_con` según `analysis/combina_policy.py`.

Para cada enlace A→B que la política no acepta (B no es hub ni está saturado), añade en B la
combinación recíproca citando el motivo y el orden de A, en el detalle y en el lote de
`curation/descripciones-4s` que define a B. No inventa integraciones: reutiliza el texto de A.

Uso: uv run python scripts/reciprocar_combinaciones.py [--apply]
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from repo_intelligence.analysis.combina_policy import MAX_COMBOS, classify, combo_map  # noqa: E402


def main() -> int:
    detail_path = ROOT / "INDICE_IA.detalle.json"
    detail = json.loads(detail_path.read_text(encoding="utf8"))
    repos = detail["repos"]
    names = {r["id"]: r.get("name") or r["id"] for r in json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))["repos"]}
    violations = classify(combo_map(repos))["violation"]
    additions: dict[str, list[dict]] = {}
    for a, b in violations:
        if len(repos[b]["combina_con"]) + len(additions.get(b, [])) >= MAX_COMBOS:
            continue
        src = next(c for c in repos[a]["combina_con"] if c["id"] == b)
        motivo = src["motivo"].strip().rstrip(".")
        additions.setdefault(b, []).append({
            "id": a, "motivo": f"Combinación recíproca: {names.get(a, a)} lo enlaza como «{motivo}».",
            "orden_instalacion": f"Orden indicado desde {names.get(a, a)}: {(src.get('orden_instalacion') or 'sin orden específico').strip()}",
            "reciproca_de": a})
    for b, new in additions.items():
        repos[b]["combina_con"] += new
        repos[b]["combines_with"] = [c["id"] for c in repos[b]["combina_con"]]
    last = {}
    for f in sorted(glob.glob(str(ROOT / "curation/descripciones-4s/*.json"))):
        for rid, e in (json.loads(Path(f).read_text(encoding="utf8")).get("repos") or {}).items():
            if isinstance(e, dict) and e.get("combina_con"):
                last[rid] = f
    files: dict[str, dict] = {}
    for b, new in additions.items():
        f = last.get(b)
        if not f:
            continue
        doc = files.setdefault(f, json.loads(Path(f).read_text(encoding="utf8")))
        have = {c["id"] for c in doc["repos"][b]["combina_con"]}
        doc["repos"][b]["combina_con"] += [dict(n) for n in new if n["id"] not in have]
    remaining = classify(combo_map(repos))["violation"]
    print({"added": sum(map(len, additions.values())), "targets": len(additions), "remaining_violations": remaining})
    if "--apply" in sys.argv:
        detail_path.write_text(json.dumps(detail, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        for f, doc in files.items():
            Path(f).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
