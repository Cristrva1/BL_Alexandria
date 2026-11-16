"""Nivel de complejidad 1-4 por repo: señales objetivas del catálogo + corrección manual.

Niveles: 1 Básico · 2 Intermedio · 3 Avanzado · 4 Experto.

Señales (todas del catálogo, sin instalar nada):

* ``setup`` (easy/medium/heavy/hard) como base.
* ``getting_started.audience``: ``ready_app`` (instalador o app lista), ``reading`` (material de
  consulta), ``agent`` (skill o plugin dentro de un agente), ``developer`` (hay que programar).
* GPU obligatoria (``access.hardware == gpu`` o la nota de hardware la exige), Kubernetes/Helm,
  ``docker compose``, API obligatoria y subcategorías de dominio experto (explotación/C2, AD,
  reversing, depuración, forense, entrenamiento).

La corrección manual vive en ``curation/complejidad.yaml`` (``id: {nivel, motivo}``) y siempre gana.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import yaml

NAMES = {1: "Básico", 2: "Intermedio", 3: "Avanzado", 4: "Experto"}
EXPERT_SUBS = {(16, "explotacion-c2"), (16, "ad-interno"), (16, "reversing"), (16, "depuracion"), (16, "ir-forense"),
               (24, "entrenamiento")}
SETUP_BASE = {"easy": 1, "medium": 2, "heavy": 3, "hard": 4}
GPU_RE = re.compile(r"\b(gpu|cuda|vram|rocm)\b", re.I)
GPU_SOFT = re.compile(r"(según|opcional|optional|sin gpu|cpu o gpu|cpu/gpu|cpu y gpu|o gpu|si (tienes|hay)|recomendad)", re.I)
K8S_RE = re.compile(r"\b(kubectl|helm|kubernetes|k8s)\b", re.I)
COMPOSE_RE = re.compile(r"docker[ -]compose|compose\.ya?ml", re.I)


def compute(entry: dict, detail: dict) -> tuple[int, list[str]]:
    """Nivel automático y motivos legibles."""
    gs = detail.get("getting_started") or {}
    access = detail.get("access") or {}
    audience = gs.get("audience")
    setup = entry.get("setup") or "medium"
    text = " ".join([gs.get("command") or "", detail.get("install") or "", " ".join(str(p) for p in gs.get("prerequisites") or [])])
    hw_note = access.get("hardware_note") or ""
    reasons: list[str] = []

    if audience == "reading" or access.get("mode") == "reference" or entry.get("role") == "directory":
        return 1, ["material de consulta: se lee, no se instala"]

    level = SETUP_BASE.get(setup, 2)
    reasons.append(f"preparación {({'easy': 'sencilla', 'medium': 'media', 'heavy': 'pesada', 'hard': 'difícil'}).get(setup, setup)}")

    if audience == "ready_app":
        level = min(level, 2)
        reasons.append("app o instalador listo para usar")
    if audience == "agent" or access.get("mode") == "agent_extension":
        level = min(level, 2)
        reasons.append("se instala dentro de un agente (skill, plugin o MCP)")
    if audience == "developer" or entry.get("role") == "library":
        level = max(level, 2)
        reasons.append("requiere programar con él")
    gpu_hard = access.get("hardware") == "gpu" or (GPU_RE.search(hw_note) and not GPU_SOFT.search(hw_note))
    if gpu_hard:
        level = max(level, 3)
        reasons.append("necesita GPU")
    if K8S_RE.search(text):
        level = max(level, 3)
        reasons.append("despliegue con Kubernetes/Helm")
    if COMPOSE_RE.search(text):
        level = max(level, 2)
        reasons.append("varios servicios con Docker Compose")
    if access.get("api") == "required":
        level = max(level, 2)
        reasons.append("requiere clave de API")
    if (entry.get("cat"), entry.get("sub")) in EXPERT_SUBS:
        level = max(level, 3)
        if setup in ("heavy", "hard"):
            level = 4
        reasons.append("dominio especializado")
    return max(1, min(level, 4)), reasons


def load_overrides(root: Path) -> dict[str, dict]:
    path = root / "curation" / "complejidad.yaml"
    if not path.exists():
        return {}
    return (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("correcciones") or {}


def resolve(rid: str, entry: dict, detail: dict, overrides: dict[str, dict]) -> dict:
    auto, reasons = compute(entry, detail)
    manual = overrides.get(rid)
    if manual:
        n = int(manual["nivel"])
        return {"nivel": n, "nombre": NAMES[n], "motivos": [manual["motivo"]], "origen": "manual", "auto": auto, "motivos_auto": reasons}
    return {"nivel": auto, "nombre": NAMES[auto], "motivos": reasons, "origen": "auto", "auto": auto}


def apply_all(root: Path) -> Counter:
    """Calcula ``complejidad`` para todo el catálogo y la escribe en los dos índices
    (``complejidad`` = nivel en INDICE_IA.json; ``complejidad_detalle`` = nivel, nombre, motivos y origen en la ficha)."""
    cpath, dpath = root / "INDICE_IA.json", root / "INDICE_IA.detalle.json"
    compact = json.loads(cpath.read_text(encoding="utf-8"))
    detail = json.loads(dpath.read_text(encoding="utf-8"))
    overrides = load_overrides(root)
    dist: Counter = Counter()
    for r in compact["repos"]:
        if r.get("alias_of") or int(r.get("cat") or 0) == 0:
            continue
        d = detail["repos"].get(r["id"])
        if d is None:
            continue
        res = resolve(r["id"], r, d, overrides)
        r["complejidad"] = res["nivel"]
        d.pop("complejidad", None)
        d["complejidad_detalle"] = res
        dist[res["nivel"]] += 1
    cpath.write_text(json.dumps(compact, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    dpath.write_text(json.dumps(detail, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return dist
