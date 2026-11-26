"""Puntuación de calidad (0-100) con la rúbrica aprobada en ``config/calidad.yaml``.

Las métricas numéricas se convierten en percentiles (rango medio, robusto a valores extremos
como cierres masivos de issues antiguas) y cada percentil es la media de dos comparaciones:

* frente a la categoría técnica (o el catálogo entero si la categoría tiene pocos datos), y
* frente al grupo de similares (``data/grupos.json``) o, si no hay grupo, la subcategoría.

Así el último de un grupo pequeño no queda en 0 automáticamente. Madurez, licencia, respaldo,
seguridad y encaje con el stack usan escalas absolutas.
"""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

import yaml

PERMISSIVE = {"MIT", "APACHE-2.0", "BSD-2-CLAUSE", "BSD-3-CLAUSE", "ISC", "UNLICENSE", "0BSD", "ZLIB", "CC0-1.0", "CC-BY-4.0",
              "BSL-1.0", "PSF-2.0", "PYTHON-2.0", "MIT-0", "WTFPL", "ARTISTIC-2.0", "UPL-1.0", "NCSA", "POSTGRESQL", "X11"}
COPYLEFT = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-2.1", "LGPL-3.0", "MPL-2.0", "EPL-1.0", "EPL-2.0", "GPL-2.0-ONLY",
            "GPL-3.0-ONLY", "GPL-3.0-OR-LATER", "GPL-2.0-OR-LATER", "AGPL-3.0-ONLY", "AGPL-3.0-OR-LATER", "LGPL-2.1-ONLY",
            "LGPL-3.0-ONLY", "EUPL-1.2", "CC-BY-SA-4.0", "OSL-3.0", "CDDL-1.0", "MS-PL", "MS-RL"}
SOURCE_AVAILABLE = {"BUSL-1.1", "ELASTIC-2.0", "SSPL-1.0", "CC-BY-NC-4.0", "CC-BY-NC-SA-4.0", "CC-BY-NC-ND-4.0", "COMMONS-CLAUSE"}
STACK_LANGS = {"Python", "TypeScript", "JavaScript", "Go"}
NAMES = {"adopcion": "Adopción", "mantenimiento": "Mantenimiento", "licencia": "Licencia", "madurez": "Madurez",
         "respaldo": "Respaldo", "encaje": "Encaje con tu stack", "seguridad": "Seguridad"}


def load_config(root: Path) -> dict:
    path = root / "config" / "calidad.yaml"
    if not path.exists():  # copia sin config/ (pruebas): rúbrica del código fuente
        path = Path(__file__).resolve().parents[3] / "config" / "calidad.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def percentile_ranks(values: dict[str, float]) -> dict[str, float]:
    """Percentil de rango medio en [0, 1]: (menores + 0.5·iguales) / n."""
    vals = sorted(values.values())
    n = len(vals)
    out = {}
    for k, v in values.items():
        lo = sum(1 for x in vals if x < v)
        eq = sum(1 for x in vals if x == v)
        out[k] = (lo + 0.5 * eq) / n if n else 0.5
    return out


def licence_class(rid: str, spdx: str | None, detail: dict, config: dict, auto: tuple[str, str] | None = None) -> tuple[str, str]:
    manual = (config.get("licencias") or {}).get(rid)
    if manual:
        return manual["clase"], manual.get("nota") or spdx or ""
    s = (spdx or "").upper()
    if auto and auto[0] and s in ("", "NOASSERTION", "OTHER"):
        return auto[0], f"{spdx or 'sin SPDX'}: {auto[1]}"
    if detail.get("licencia_nota"):
        return ("open_core" if s in {x.upper() for x in PERMISSIVE | COPYLEFT} else "source_available"), detail["licencia_nota"][:120]
    if s in PERMISSIVE:
        return "osi_permisiva", spdx or ""
    if s in COPYLEFT:
        return "osi_copyleft", spdx or ""
    if s in SOURCE_AVAILABLE:
        return "source_available", spdx or ""
    return "desconocida", spdx or "sin licencia detectada"


def backer_class(m: dict, config: dict) -> str:
    owner = (m.get("propietario") or "").lower()
    if owner in {f.lower() for f in config.get("fundaciones") or []}:
        return "fundacion"
    return "organizacion" if m.get("propietario_tipo") == "Organization" else "individual"


def effective_downloads(m: dict) -> float | None:
    vals = [m.get("pypi_mes"), m.get("npm_mes")]
    if m.get("docker_pulls"):
        vals.append(m["docker_pulls"] / max(m.get("edad_dias", 30) / 30.4, 1))  # media mensual aproximada
    vals = [v for v in vals if v]
    return max(vals) if vals else None


def has_docker(rid: str, compact_entry: dict, detail: dict, m: dict) -> bool:
    gs = detail.get("getting_started") or {}
    blob = " ".join([gs.get("command") or "", detail.get("install") or "", " ".join(compact_entry.get("tags") or [])]).lower()
    return bool(m.get("docker_pulls")) or "docker" in blob


def stack_fit(rid: str, compact_entry: dict, detail: dict, m: dict) -> tuple[float, list[str]]:
    pts, why = 0.0, []
    lang = m.get("lenguaje") or compact_entry.get("lang")
    if lang in STACK_LANGS:
        pts += 3
        why.append(f"lenguaje {lang}")
    if has_docker(rid, compact_entry, detail, m):
        pts += 3
        why.append("Docker disponible")
    if compact_entry.get("exec") == "local":
        pts += 2
        why.append("se ejecuta en local")
    if "local_model" in (compact_entry.get("routes") or []):
        pts += 2
        why.append("admite modelos locales/Ollama")
    return min(pts, 10.0), why


METRICS = {  # métrica -> (eje, mayor_es_mejor)
    "estrellas_anio": ("adopcion", True),
    "descargas_mes": ("adopcion", True),
    "estrellas": ("adopcion", True),
    "commits_90d": ("mantenimiento", True),
    "releases_365d": ("mantenimiento", True),
    "primera_respuesta_dias": ("mantenimiento", False),
    "ratio_cerradas": ("mantenimiento", True),
    "bus_factor": ("mantenimiento", True),
}


def metric_value(name: str, m: dict) -> float | None:
    if m.get("error"):
        return None
    if name == "descargas_mes":
        return effective_downloads(m)
    if name == "bus_factor":
        return None if m.get("cuota_principal") is None else 1 - m["cuota_principal"]
    if name in ("commits_90d", "releases_365d") and m.get("archivado"):
        return 0.0
    return m.get(name)


def score_all(metrics: dict[str, dict], compact: dict, detail: dict, config: dict, groups: dict[str, str] | None = None,
              *, today: str | None = None) -> dict[str, dict]:
    """Devuelve ``{id: {puntuacion, ejes, metricas, notas, ...}}`` para los repos con métricas."""
    today = today or date.today().isoformat()
    entries = {r["id"]: r for r in compact["repos"] if not r.get("alias_of")}
    ids = [i for i in metrics if i in entries and not metrics[i].get("error")]
    groups = groups or {}
    norm = config.get("normalizacion") or {}
    w_cat, w_grp = float(norm.get("peso_categoria", 0.5)), float(norm.get("peso_grupo", 0.5))
    min_cat = int(norm.get("minimo_categoria", 8))

    pct: dict[str, dict[str, float]] = defaultdict(dict)
    for name, (_axis, higher) in METRICS.items():
        vals = {i: v for i in ids if (v := metric_value(name, metrics[i])) is not None}
        if not vals:
            continue
        signed = {i: (v if higher else -v) for i, v in vals.items()}
        global_p = percentile_ranks(signed)
        by_cat: dict[Any, dict] = defaultdict(dict)
        by_grp: dict[Any, dict] = defaultdict(dict)
        for i, v in signed.items():
            e = entries[i]
            by_cat[e["cat"]][i] = v
            by_grp[groups.get(i) or (e["cat"], e["sub"])][i] = v
        cat_p: dict[str, float] = {}
        for members in by_cat.values():
            ranks = percentile_ranks(members) if len(members) >= min_cat else {i: global_p[i] for i in members}
            cat_p.update(ranks)
        grp_p: dict[str, float] = {}
        for members in by_grp.values():
            if len(members) >= 2:
                grp_p.update(percentile_ranks(members))
        for i in signed:
            pct[i][name] = (w_cat * cat_p[i] + w_grp * grp_p[i]) / (w_cat + w_grp) if i in grp_p else cat_p[i]

    W = config["pesos"]
    sub = config["subpesos"]
    lic_pts = config["licencia_puntos"]
    back_pts = config["respaldo_puntos"]
    out: dict[str, dict] = {}
    for i in ids:
        m, e, d = metrics[i], entries[i], detail.get(i, {})
        notes: list[str] = []
        axes: dict[str, float] = {}
        for axis in ("adopcion", "mantenimiento"):
            parts = {k: w for k, w in sub[axis].items() if k in pct[i]}
            missing = [k for k in sub[axis] if k not in pct[i]]
            if parts:
                total_w = sum(parts.values())
                axes[axis] = W[axis] * sum(pct[i][k] * w for k, w in parts.items()) / total_w
            else:
                axes[axis] = W[axis] * 0.5
            if missing:
                notes.append(f"{NAMES[axis]}: sin dato de {', '.join(missing)} (se reparte el peso)")
        if m.get("archivado"):
            axes["mantenimiento"] = 0.0
            notes.append("Repositorio archivado: mantenimiento 0")
        # Madurez
        age = min(m.get("edad_dias", 0) / 1095, 1.0)
        major = m.get("semver_mayor")
        continuous = (m.get("releases_365d") or 0) >= 12 and m.get("edad_dias", 0) >= 1095
        if (major is not None and major >= 1) or continuous:
            sem = 1.0
        elif major == 0:
            sem = 1 / 3
        else:
            sem = 0.5
        home = m.get("homepage") or ""
        docs = 1.0 if home and "github.com/" + (e.get("gh") or "").lower() not in home.lower() else 0.0
        sm = sub["madurez"]
        axes["madurez"] = age * sm["edad"] + sem * sm["semver"] + docs * sm["docs"]
        # Licencia, respaldo, seguridad, encaje
        lclass, lnote = licence_class(i, m.get("licencia_spdx"), d, config, (m.get("licencia_clase_auto"), m.get("licencia_motivo_auto") or ""))
        axes["licencia"] = float(lic_pts[lclass])
        bclass = backer_class(m, config)
        axes["respaldo"] = float(back_pts[bclass])
        sc = m.get("scorecard")
        axes["seguridad"] = W["seguridad"] * sc / 10 if sc is not None else W["seguridad"] / 2
        if sc is None:
            notes.append("Sin OpenSSF Scorecard publicado: seguridad neutral")
        fit, why = stack_fit(i, e, d, m)
        axes["encaje"] = fit
        if m.get("derivado_de"):
            notes.append(f"Derivado de {m['derivado_de']}: commits y contribuidores sin el historial del upstream")
        total = round(sum(axes.values()), 1)
        out[i] = {
            "puntuacion": total,
            "ejes": {k: round(v, 1) for k, v in axes.items()},
            "percentiles": {k: round(v, 3) for k, v in pct[i].items()},
            "licencia": {"clase": lclass, "detalle": lnote},
            "respaldo": bclass,
            "encaje": why,
            "notas": notes,
            "fecha_metricas": m.get("fecha"),
            "fecha_puntuacion": today,
        }
    return out


def load_groups(root: Path) -> dict[str, str]:
    path = root / "data" / "grupos.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {rid: g["id"] for g in data.get("grupos", []) for rid in g.get("miembros", [])}


def write_scores(root: Path, scores: dict[str, dict], config: dict, today: str) -> Path:
    out = root / "data" / "metricas" / "puntuaciones.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {"fecha": today, "rubrica": {"pesos": config["pesos"], "subpesos": config["subpesos"],
                                          "normalizacion": config.get("normalizacion")},
               "repos": dict(sorted(scores.items()))}
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return out


def sync_indices(root: Path, scores: dict[str, dict]) -> int:
    """Escribe ``puntuacion`` en INDICE_IA.json y ``calidad`` en INDICE_IA.detalle.json."""
    cpath, dpath = root / "INDICE_IA.json", root / "INDICE_IA.detalle.json"
    compact = json.loads(cpath.read_text(encoding="utf-8"))
    detail = json.loads(dpath.read_text(encoding="utf-8"))
    n = 0
    for r in compact["repos"]:
        s = scores.get(r["id"])
        if s is None or r.get("alias_of"):
            continue
        r["puntuacion"] = round(s["puntuacion"])
        d = detail["repos"].get(r["id"])
        if d is not None:
            d["calidad"] = {"puntuacion": s["puntuacion"], "ejes": s["ejes"], "licencia": s["licencia"]["clase"],
                            "notas": s["notas"], "fecha": s["fecha_metricas"]}
        n += 1
    cpath.write_text(json.dumps(compact, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    dpath.write_text(json.dumps(detail, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return n
