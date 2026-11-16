"""Calidad al dar de alta: puntuación, complejidad y aviso de grupo de similares para repos nuevos.

Lo usa ``repo-intelligence add`` justo después de escribir (o simular) el alta:

1. Obtiene las métricas públicas de los repos nuevos (en simulación, en una caché temporal).
2. Puntúa todo el catálogo con la caché existente + los nuevos (misma rúbrica y percentiles).
3. Calcula la complejidad 1-4 con sus motivos.
4. Busca el grupo de similares más parecido y dice en qué posición quedaría por puntuación.
   No modifica ``curation/grupos.yaml``: la incorporación al grupo es una decisión editorial.
"""
from __future__ import annotations

import json
import tempfile
from datetime import date
from pathlib import Path
from typing import Callable

from repo_intelligence.quality import complexity as cx
from repo_intelligence.quality import metrics as mx
from repo_intelligence.quality import score as sx
from repo_intelligence.quality import similar as gx


def evaluate(root: Path, ids: list[str], compact: dict, detail: dict, *, simulate: bool = False, fetch: bool = True,
             collect_fn: Callable | None = None, today: str | None = None) -> dict[str, dict]:
    """Devuelve ``{id: {puntuacion, ejes, complejidad, grupo, avisos}}``. Si no es simulación, escribe
    puntuaciones, complejidad y grupos en los índices (el alta ya está escrita)."""
    today = today or date.today().isoformat()
    collect_fn = collect_fn or mx.collect
    config = sx.load_config(root)
    targets = [t for t in mx.catalog_targets(compact, detail) if t["id"] in ids]
    metrics = {t["id"]: m for t in mx.catalog_targets(compact, detail) if (m := mx.load_cache(root, t["id"]))}
    notes: dict[str, list[str]] = {i: [] for i in ids}
    if fetch and targets:
        if simulate:
            with tempfile.TemporaryDirectory() as tmp:
                metrics.update(collect_fn(Path(tmp), targets, config=config, refresh=True))
        else:
            metrics.update(collect_fn(root, targets, config=config, refresh=True))
    elif not fetch:
        for i in ids:
            notes[i].append("sin métricas (--sin-metricas): ejecuta `repo-intelligence score --id " + i + "` más tarde")
    scores = sx.score_all(metrics, compact, detail, config, sx.load_groups(root), today=today)
    groups_doc = root / "data" / "grupos.json"
    groups = json.loads(groups_doc.read_text(encoding="utf-8"))["grupos"] if groups_doc.exists() else []
    model = gx.SimilarityModel(compact, detail)
    overrides = cx.load_overrides(root)
    out: dict[str, dict] = {}
    for rid in ids:
        entry = next((r for r in compact["repos"] if r["id"] == rid), None)
        if entry is None:
            continue
        level = cx.resolve(rid, entry, detail.get(rid, {}), overrides)
        s = scores.get(rid)
        info = {"puntuacion": s["puntuacion"] if s else None, "ejes": s["ejes"] if s else None,
                "complejidad": level, "grupo": None, "avisos": list(notes.get(rid, []))}
        if rid in metrics and metrics[rid].get("error"):
            info["avisos"].append(f"métricas no disponibles: {metrics[rid]['error']}")
        g, sim = gx.best_group_for(model, rid, groups) if rid in model.entries else (None, 0.0)
        by_sub = False
        if not g:  # borradores sin textos: misma categoría/subcategoría que la mayoría de un grupo
            g, by_sub = _group_by_sub(entry, groups, compact), True
        if g:
            ranked = sorted([(scores.get(m, {}).get("puntuacion") or 0, m) for m in g["miembros"] if m != rid]
                            + [((s or {}).get("puntuacion") or 0, rid)], reverse=True)
            pos = [m for _p, m in ranked].index(rid) + 1
            info["grupo"] = {"id": g["id"], "titulo": g["titulo"], "similitud": sim, "posicion": pos, "total": len(ranked),
                             "recomendado_actual": g["recomendado"]}
            why = "comparte subcategoría con el grupo" if by_sub else "se parece al grupo"
            how = "" if by_sub else f" (similitud {sim:.2f})"
            info["grupo"]["criterio"] = "subcategoria" if by_sub else "similitud"
            info["avisos"].append(
                f"{why} «{g['titulo']}»{how}: quedaría en la posición {pos} de {len(ranked)} "
                f"por puntuación (recomendado actual: {g['recomendado']}). Si es equivalente, añádelo a curation/grupos.yaml "
                "y ejecuta `repo-intelligence grupos`.")
        out[rid] = info
    if not simulate:
        sx.write_scores(root, scores, config, today)
        sx.sync_indices(root, scores)
        cx.apply_all(root)
        if (root / "curation" / "grupos.yaml").exists():
            gx.rebuild(root, today)
    return out


def _group_by_sub(entry: dict, groups: list[dict], compact: dict) -> dict | None:
    where = {r["id"]: (int(r.get("cat") or 0), r.get("sub")) for r in compact["repos"]}
    key = (int(entry.get("cat") or 0), entry.get("sub"))
    best, best_n = None, 1
    for g in groups:
        n = sum(where.get(m) == key for m in g["miembros"])
        if n > best_n and n * 2 >= len(g["miembros"]):
            best, best_n = g, n
    return best
