"""Aplica lotes de descripciones en 4 secciones a INDICE_IA.detalle.json.

Uso:
    uv run python scripts/apply_descripciones_4s.py curation/descripciones-4s/piloto-2026-11-15.json          # valida (dry-run)
    uv run python scripts/apply_descripciones_4s.py curation/descripciones-4s/piloto-2026-11-15.json --apply  # escribe

Cada lote es la fuente editable; INDICE_IA.detalle.json sigue siendo la fuente de verdad que leen
los generadores (`guide build`, `menu export`, `web build`). El script:
- añade `que_es`, `que_hace`, `como_lo_hace`, `combina_con`, `descripcion_notas`,
  `descripcion_fuentes`, `descripcion_revision` y `descripcion_github` (estado leído de la API de GitHub:
  archivado, renombrado, último push, licencia) sin tocar los demás campos;
- sincroniza `combines_with` con los ids de `combina_con` (misma lista, mismo orden),
  porque recomendador, decisiones y menú portable siguen leyendo `combines_with`;
- rechaza ids inexistentes, autorreferencias, alternativas listadas como combinación y textos vacíos.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DETAIL = ROOT / "INDICE_IA.detalle.json"
COMPACT = ROOT / "INDICE_IA.json"
TEXT_FIELDS = ("que_es", "que_hace", "como_lo_hace")


def validate(batch: dict, compact: dict, detail: dict, min_combos: int = 1) -> list[str]:
    ids = {r["id"] for r in compact["repos"] if not r.get("alias_of")}
    alts = {r["id"]: set(r.get("alt") or []) for r in compact["repos"]}
    errors: list[str] = []
    for rid, entry in batch["repos"].items():
        if rid not in ids or rid not in detail["repos"]:
            errors.append(f"{rid}: no existe en el índice")
            continue
        for field in TEXT_FIELDS:
            if not (entry.get(field) or "").strip():
                errors.append(f"{rid}: falta {field}")
        combos = entry.get("combina_con") or []
        if not min_combos <= len(combos) <= 6:
            errors.append(f"{rid}: combina_con debe tener {min_combos}-6 elementos (tiene {len(combos)})")
        seen = set()
        for combo in combos:
            cid = combo.get("id")
            if cid not in ids:
                errors.append(f"{rid}: combina_con apunta a {cid}, que no existe")
            if cid == rid or cid in seen:
                errors.append(f"{rid}: combina_con repetido o autorreferente ({cid})")
            if cid in alts.get(rid, set()):
                errors.append(f"{rid}: {cid} es alternativa, no combinación")
            if not (combo.get("motivo") or "").strip():
                errors.append(f"{rid}: {cid} sin motivo")
            seen.add(cid)
        if not entry.get("fuentes"):
            errors.append(f"{rid}: sin fuentes")
    return errors


def apply(batch: dict, detail: dict) -> list[str]:
    changes = []
    for rid, entry in batch["repos"].items():
        target = detail["repos"][rid]
        before = list(target.get("combines_with") or [])
        for field in TEXT_FIELDS:
            target[field] = entry[field].strip()
        target["combina_con"] = [
            {k: v for k, v in {"id": c["id"], "motivo": c["motivo"].strip(), "orden_instalacion": (c.get("orden_instalacion") or "").strip()}.items() if v}
            for c in entry["combina_con"]
        ]
        if entry.get("notas"):
            target["descripcion_notas"] = entry["notas"].strip()
        else:
            target.pop("descripcion_notas", None)
        target["descripcion_fuentes"] = list(entry["fuentes"])
        target["descripcion_revision"] = {
            "batch": batch.get("batch"),
            "checked_at": batch.get("checked_at"),
            "status": "source_reviewed",
            "installation_tested": False,
        }
        if entry.get("github"):
            target["descripcion_github"] = dict(entry["github"])
        target["combines_with"] = [c["id"] for c in entry["combina_con"]]
        removed = [c for c in before if c not in target["combines_with"]]
        added = [c for c in target["combines_with"] if c not in before]
        changes.append(f"{rid}: +{added} -{removed}")
    return changes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--min-combos", type=int, default=1, help="Mínimo de combinaciones por repo (los lotes completos usan 3).")
    args = parser.parse_args()
    batch = json.loads(args.batch.read_text(encoding="utf8"))
    compact = json.loads(COMPACT.read_text(encoding="utf8"))
    detail = json.loads(DETAIL.read_text(encoding="utf8"))
    errors = validate(batch, compact, detail, args.min_combos)
    if errors:
        print("\n".join(errors))
        return 1
    changes = apply(batch, detail)
    print("\n".join(changes))
    if args.apply:
        DETAIL.write_text(json.dumps(detail, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        print(f"Escrito {DETAIL.name}: {len(changes)} repos.")
    else:
        print("Dry-run: usa --apply para escribir.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
