"""Candidatos a retiro: propuesta para revisión humana. No modifica ``data/retired.json``.

Un repo es candidato solo si cumple las tres condiciones aprobadas:

1. Puntuación de calidad < umbral (45 por defecto).
2. Sin commits en 365 días (en repos derivados, commits propios) o archivado.
3. Sin caso de uso único: pertenece a un grupo de similares, no es el recomendado y no está marcado
   como ``caso_unico`` en ``curation/grupos.yaml``. Un repo sin grupo se considera único.

Si falta un dato (sin métricas o sin puntuación), el repo no es candidato: falta evidencia.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from repo_intelligence.quality import metrics as mx

UMBRAL = 45.0


def _load(path: Path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def evaluate(root: Path, *, threshold: float = UMBRAL, today: str | None = None) -> dict:
    today = today or date.today().isoformat()
    compact = _load(root / "INDICE_IA.json", {"repos": []})
    scores = _load(root / "data" / "metricas" / "puntuaciones.json", {"repos": {}})["repos"]
    groups = _load(root / "data" / "grupos.json", {"grupos": []})["grupos"]
    retired = {r.get("id") for r in _load(root / "data" / "retired.json", {"repos": []}).get("repos", [])}
    row_of: dict[str, tuple[dict, dict]] = {}
    for g in groups:
        for row in g.get("ranking", []):
            row_of[row["id"]] = (g, row)
    names = {r["id"]: r.get("name") or r["id"] for r in compact["repos"]}
    candidates, near, missing = [], [], []
    for repo in compact["repos"]:
        rid = repo["id"]
        if repo.get("alias_of") or int(repo.get("cat") or 0) <= 0 or rid in retired:
            continue
        s = scores.get(rid)
        m = mx.load_cache(root, rid) or {}
        if not s or not m or m.get("error") or m.get("commits_365d") is None:
            why = ("sin repositorio de GitHub" if not repo.get("gh") else
                   f"alojado en {repo['repository_host']}" if repo.get("repository_host") not in (None, "github", "github.com") else
                   f"error de métricas: {m['error']}" if m.get("error") else "sin métricas en caché")
            missing.append({"id": rid, "motivo": why})
            continue
        low = s["puntuacion"] < threshold
        archived = bool(m.get("archivado"))
        inactive = archived or int(m.get("commits_365d") or 0) == 0
        g, row = row_of.get(rid, (None, None))
        unique_reason = None
        if g is None:
            unique_reason = "sin grupo de similares"
        elif row["papel"] == "recomendado":
            unique_reason = "es el recomendado de su grupo"
        elif row.get("caso_unico"):
            unique_reason = "marcado como caso único en curation/grupos.yaml"
        evidence = {
            "id": rid, "nombre": names.get(rid, rid), "gh": repo.get("gh") or m.get("full_name"), "cat": repo.get("cat"),
            "sub": repo.get("sub"), "puntuacion": s["puntuacion"], "ejes": s["ejes"], "licencia": (s.get("licencia") or {}).get("clase"),
            "commits_365d": m.get("commits_365d"), "commits_90d": m.get("commits_90d"), "ultimo_push": m.get("ultimo_push"),
            "archivado": archived, "estrellas": m.get("estrellas"), "fork_de": m.get("fork_de"),
            "grupo": ({"id": g["id"], "titulo": g["titulo"], "posicion": row["posicion"], "total": len(g["ranking"]),
                       "papel": row["papel"], "cuando": row.get("cuando"), "cuando_origen": row.get("cuando_origen"),
                       "recomendado": g["recomendado"], "puntuacion_recomendado": next(
                           (x["puntuacion"] for x in g["ranking"] if x["id"] == g["recomendado"]), None)} if g else None),
            "condiciones": {"puntuacion_baja": low, "sin_actividad": inactive, "sin_caso_unico": unique_reason is None},
        }
        if unique_reason:
            evidence["caso_unico_motivo"] = unique_reason
        met = sum(evidence["condiciones"].values())
        if met == 3:
            candidates.append(evidence)
        elif met == 2:
            near.append(evidence)
    for e in candidates:
        e["estado"] = "pendiente de revisión"
    # candidatos de un informe anterior con la misma fecha que ya se retiraron: se conservan con su estado
    previous = _load(root / "reports" / f"candidatos-retiro-{today}.json", {"candidatos": []})["candidatos"]
    ledger = {r.get("id"): r for r in _load(root / "data" / "retired.json", {"repos": []}).get("repos", [])}
    for e in previous:
        if e["id"] in ledger and e["id"] not in {x["id"] for x in candidates}:
            candidates.append({**e, "estado": "retirado", "retirado_el": ledger[e["id"]].get("retired_at"),
                               "motivo_retiro": ledger[e["id"]].get("reason")})
    key = lambda e: (e["puntuacion"], e["id"])  # noqa: E731
    retired_now = [e["id"] for e in candidates if e.get("estado") == "retirado"]
    nota = ("Propuesta para revisión. El informe no retira nada; los retiros los decide el propietario y se registran en data/retired.json."
            + (f" Retirados tras la revisión: {', '.join(retired_now)}." if retired_now else ""))
    return {"fecha": today, "umbral": threshold, "nota": nota,
            "criterios": ["puntuación < umbral", "sin commits en 365 días (propios en derivados) o archivado",
                          "sin caso de uso único: en un grupo, no recomendado y sin marca caso_unico"],
            "evaluados": sum(1 for r in compact["repos"] if not r.get("alias_of") and int(r.get("cat") or 0) > 0 and r["id"] not in retired),
            "sin_datos": sorted(missing, key=lambda x: x["id"]), "candidatos": sorted(candidates, key=key), "cerca": sorted(near, key=key)}


def _state(e: dict) -> str:
    if e.get("estado") == "retirado":
        return f"retirado el {e.get('retirado_el')} ({e.get('motivo_retiro')}) — en data/retired.json"
    return e.get("estado") or "pendiente de revisión"


def _fails(e: dict) -> str:
    labels = {"puntuacion_baja": "puntuación ≥ umbral", "sin_actividad": "con commits en 365 días", "sin_caso_unico": "caso único"}
    return next(labels[k] for k, v in e["condiciones"].items() if not v)


def render_md(data: dict) -> str:
    cands = data["candidatos"]
    lines = [f"# Candidatos a retiro — {data['fecha']}", "", data["nota"], "",
             "Un repo aparece aquí solo si cumple las tres condiciones:", ""]
    lines += [f"{i}. {c}" for i, c in enumerate(data["criterios"], 1)]
    lines += ["", f"Umbral de puntuación: {data['umbral']:g}. Repos evaluados: {data['evaluados']}. "
              f"Sin datos suficientes (no evaluables): {len(data['sin_datos'])}.", "",
              "«Commits 365 d» cuenta commits en la rama principal (propios en repos derivados). «Último push» incluye "
              "cualquier rama, por eso puede ser reciente aunque no haya commits en la principal.", "",
              f"## Candidatos ({len(cands)})", ""]
    if not cands:
        lines += ["Ningún repo cumple las tres condiciones.", ""]
    else:
        lines += ["| Repo | Puntuación | Commits 365 d | Último push | Grupo (posición) | Alternativa recomendada | Estado |",
                  "|---|---:|---:|---|---|---|---|"]
        for e in cands:
            g = e["grupo"]
            arch = " · archivado" if e["archivado"] else ""
            lines.append(f"| `{e['id']}` ({e['gh']}) | {e['puntuacion']:.1f} | {e['commits_365d']}{arch} | {e['ultimo_push'] or '—'} | "
                         f"{g['titulo']} ({g['posicion']}/{g['total']}) | `{g['recomendado']}` ({g['puntuacion_recomendado']:.0f}) | {_state(e)} |")
        lines += ["", "### Evidencia por repo", ""]
        for e in cands:
            g, ax = e["grupo"], e["ejes"]
            lines += [f"#### {e['nombre']} (`{e['id']}`)", "", f"- Estado: {_state(e)}.",
                      f"- Puntuación {e['puntuacion']:.1f}: adopción {ax['adopcion']:.1f}/25, mantenimiento {ax['mantenimiento']:.1f}/25, "
                      f"licencia {ax['licencia']:.1f}/15 ({e['licencia']}), madurez {ax['madurez']:.1f}/10, respaldo {ax['respaldo']:.1f}/10, "
                      f"encaje {ax['encaje']:.1f}/10, seguridad {ax['seguridad']:.1f}/5.",
                      f"- Actividad: {e['commits_365d']} commits en 365 días, último push {e['ultimo_push'] or '—'}"
                      + (", archivado" if e["archivado"] else "") + (f", derivado de {e['fork_de']}" if e.get("fork_de") else "") + ".",
                      f"- Grupo «{g['titulo']}»: posición {g['posicion']} de {g['total']}; recomendado `{g['recomendado']}`.",
                      f"- Cuándo elegirlo hoy: {g['cuando'] or '—'}" + (" (texto de plantilla)" if g.get("cuando_origen") != "curado" else ""), ""]
    near = data["cerca"]
    lines += [f"## Cerca del umbral: cumplen dos de tres ({len(near)})", "",
              "No son candidatos. Se listan para revisar el criterio.", "",
              "| Repo | Puntuación | Commits 365 d | Grupo | Condición que no cumple |", "|---|---:|---:|---|---|"]
    for e in near:
        g = e["grupo"]
        lines.append(f"| `{e['id']}` | {e['puntuacion']:.1f} | {e['commits_365d']} | {g['titulo'] if g else '—'} | {_fails(e)} |")
    if data["sin_datos"]:
        lines += ["", f"## Sin datos suficientes ({len(data['sin_datos'])})", "", "No se pueden evaluar; no son candidatos.", ""]
        lines += [f"- `{x['id']}`: {x['motivo']}" for x in data["sin_datos"]]
    return "\n".join(lines) + "\n"


def write_report(root: Path, data: dict) -> list[Path]:
    out = root / "reports"
    out.mkdir(parents=True, exist_ok=True)
    js = out / f"candidatos-retiro-{data['fecha']}.json"
    md = out / f"candidatos-retiro-{data['fecha']}.md"
    js.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md.write_text(render_md(data), encoding="utf-8")
    return [md, js]
