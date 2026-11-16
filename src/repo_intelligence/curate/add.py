"""Alta de repos en el catálogo: ``repo-intelligence add``.

Reúne en un solo paso lo que antes hacían los scripts fechados de altas
(``catalog_expansion_20261116.py`` + ``apply_descripciones_4s.py`` +
``reciprocar_combinaciones.py``):

1. Lee la identidad del repo con la API de GitHub (``gh api``): id numérico, estrellas,
   licencia, último push, archivado, temas, web, rama por defecto, README y árbol raíz.
2. Rechaza repos archivados, privados o ya catalogados (por id numérico, ``owner/repo``,
   URL o id del catálogo). Un repo de ``data/retired.json`` se rechaza salvo ``--force``.
3. Escribe la entrada compacta (``INDICE_IA.json``) y la ficha (``INDICE_IA.detalle.json``)
   con los campos de acceso, inicio, revisión editorial y las 4 secciones. Sin texto propio,
   deja marcadores ``PENDIENTE`` que los tests impiden publicar.
4. Valida y aplica ``combina_con``. La reciprocidad se completa sola dentro del límite de 6
   (misma política que ``analysis/combina_policy.py``). Con ``--ligero`` las combinaciones
   son opcionales (0 a 6) y la entrada queda exenta de la simetría.
5. Opcionalmente sugiere combinaciones (grupos ``alt``, subcategoría, áreas y hubs).

No instala ni ejecuta ningún proyecto catalogado.
"""
from __future__ import annotations

import base64
import glob
import importlib
import json
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date as _date, datetime, timezone
from pathlib import Path
from typing import Any, Callable

from repo_intelligence.analysis.combina_policy import HUB_THRESHOLD, MAX_COMBOS, MIN_COMBOS, classify, combo_map, inbound
from repo_intelligence.core.access import access_routes

PENDING = "PENDIENTE"
LIGERO = "ligero"
ROLE = {"skill": "skill", "reference": "directory", "library": "library", "app": "app", "server": "platform", "model": "runtime",
        "mcp": "runtime", "agent": "app", "framework": "library", "engine": "runtime", "template": "library", "plugin": "library"}
AVOID = {"library": "buscas una aplicación lista y no quieres preparar un proyecto de código",
         "framework": "buscas una aplicación lista y no quieres preparar un proyecto de código",
         "mcp": "necesitas un producto autónomo y esta pieza requiere un cliente MCP",
         "reference": "necesitas una aplicación lista para ejecutar en lugar de material de consulta",
         "model": "no tienes el hardware o no aceptas la licencia de los pesos",
         "engine": "no quieres preparar modelos, dependencias y hardware propios",
         "server": "no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones",
         "agent": "necesitas una herramienta estable y auditada para datos sensibles",
         "app": "necesitas una instalación sin cuentas ni dependencias adicionales",
         "skill": "no usas un agente compatible con skills",
         "plugin": "no usas el anfitrión para el que se publica el plugin",
         "template": "buscas una aplicación lista y no quieres preparar un proyecto de código"}
MANIFESTS = {"pyproject.toml", "package.json", "Cargo.toml", "go.mod", "CMakeLists.txt", "pom.xml", "build.gradle", "composer.json",
             "Gemfile", "requirements.txt", "Dockerfile", "docker-compose.yml", "compose.yaml", "mix.exs", "setup.py", "Makefile"}
AI_GROUPS = ("local", "local_choice", "optional", "required", "depends")
STALE_DAYS = 365


class AddError(RuntimeError):
    """Error de alta que detiene el lote completo (no se escribe nada)."""


GhFn = Callable[[str], dict]


def gh_api(path: str) -> dict:
    """``gh api <path>`` autenticado. Lanza ``AddError`` si falla."""
    result = subprocess.run(["gh", "api", path], capture_output=True, text=True, encoding="utf-8", timeout=60)
    if result.returncode:
        raise AddError(f"gh api {path}: {result.stderr.strip() or result.stdout.strip()}")
    return json.loads(result.stdout)


def today() -> str:
    return _date.today().isoformat()


# --------------------------------------------------------------------------------------------
# Lectura de GitHub
# --------------------------------------------------------------------------------------------

def fetch_identity(full_name: str, gh: GhFn = gh_api) -> dict:
    """Metadatos, README, árbol raíz, temas y última release de ``owner/repo``."""
    meta = gh(f"repos/{full_name}")
    out: dict[str, Any] = {"metadata": meta}
    try:
        out["readme"] = gh(f"repos/{meta['full_name']}/readme")
    except AddError as error:
        out["readme_error"] = str(error)
    try:
        out["tree"] = gh(f"repos/{meta['full_name']}/git/trees/{meta.get('default_branch') or 'HEAD'}")
    except AddError:
        out["tree"] = {"sha": None, "tree": []}
    try:
        rel = gh(f"repos/{meta['full_name']}/releases/latest")
        if rel.get("tag_name"):
            out["release"] = f"{rel['tag_name']} ({(rel.get('published_at') or '')[:10]})"
    except AddError:
        pass
    return out


def summary(meta: dict) -> dict:
    """Ficha breve de identidad (lo que se imprime y se guarda en el informe)."""
    return {"full_name": meta.get("full_name"), "github_id": meta.get("id"), "stars": meta.get("stargazers_count"),
            "license": (meta.get("license") or {}).get("spdx_id"), "pushed_at": (meta.get("pushed_at") or "")[:10],
            "archived": bool(meta.get("archived")), "topics": list(meta.get("topics") or []), "homepage": meta.get("homepage") or None,
            "default_branch": meta.get("default_branch"), "language": meta.get("language"), "description": meta.get("description")}


# --------------------------------------------------------------------------------------------
# Comprobaciones
# --------------------------------------------------------------------------------------------

def _norm_url(value: str | None) -> str:
    return (value or "").lower().rstrip("/").removesuffix(".git").replace("http://", "https://").replace("://www.", "://")


def check_identity(meta: dict, rid: str, compact: dict, retired: dict, *, force: bool = False, now: str | None = None) -> tuple[list[str], list[str]]:
    """Devuelve (errores, avisos). Un error impide el alta."""
    errors: list[str] = []
    warnings: list[str] = []
    full = (meta.get("full_name") or "").lower()
    url = _norm_url(meta.get("html_url") or f"https://github.com/{full}")
    if meta.get("private"):
        errors.append(f"{full}: repositorio privado")
    if meta.get("archived"):
        errors.append(f"{full}: archivado en GitHub")
    for repo in compact.get("repos", []):
        if repo.get("alias_of"):
            continue
        same_id = meta.get("id") and repo.get("github_id") == meta.get("id")
        same_name = (repo.get("gh") or "").lower() == full
        same_url = _norm_url(f"https://github.com/{repo.get('gh')}") == url if repo.get("gh") else False
        if same_id or same_name or same_url:
            errors.append(f"{full}: ya está en el catálogo como «{repo['id']}»")
        elif repo.get("id") == rid:
            errors.append(f"{full}: el id «{rid}» ya lo usa {repo.get('gh')}")
    for gone in retired.get("repos", []):
        if (meta.get("id") and gone.get("github_id") == meta.get("id")) or (gone.get("gh") or "").lower() == full:
            text = f"{full}: retirado en data/retired.json (motivo «{gone.get('reason')}»)"
            (warnings if force else errors).append(text + (" — se añade por --force" if force else "; usa --force para reincorporarlo"))
    pushed = (meta.get("pushed_at") or "")[:10]
    if pushed:
        ref = datetime.fromisoformat(now or today())
        age = (ref - datetime.fromisoformat(pushed)).days
        if age > STALE_DAYS:
            warnings.append(f"{full}: sin push desde {pushed} ({age} días)")
    return errors, warnings


# --------------------------------------------------------------------------------------------
# Construcción de entradas
# --------------------------------------------------------------------------------------------

def _curation_base(root: Path, date: str):
    """Helpers de acceso e inicio compartidos con las migraciones fechadas (scripts/)."""
    scripts = str(root / "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    base = importlib.import_module("document_curation_20261114")
    base.DATE = date
    return base


def default_spec(full_name: str, meta: dict, *, cat: int, sub: str, kind: str = "app", rid: str | None = None,
                 name: str | None = None, one: str | None = None) -> dict:
    """Spec mínima para un alta individual: lo no aportado queda como ``PENDIENTE``."""
    rid = rid or slug_id(meta.get("name") or full_name.split("/")[-1])
    gh_desc = (meta.get("description") or "").strip()
    pending_one = one or f"{PENDIENTE_TXT} descripción en español (GitHub: {gh_desc[:90]})"
    return {"gh": meta.get("full_name") or full_name, "id": rid, "name": name or meta.get("name") or rid, "cat": cat, "sub": sub,
            "kind": kind, "one": pending_one, "how": f"{PENDIENTE_TXT} cómo funciona.",
            "examples": [f"{PENDIENTE_TXT} ejemplo 1", f"{PENDIENTE_TXT} ejemplo 2"],
            "try": [f"{PENDIENTE_TXT} primera prueba", f"{PENDIENTE_TXT} resultado esperado"],
            "tags": list(meta.get("topics") or [])[:5],
            "que_es": f"{PENDIENTE_TXT} ¿Qué es?", "que_hace": f"{PENDIENTE_TXT} ¿Qué hace?", "como_lo_hace": f"{PENDIENTE_TXT} ¿Cómo lo hace?",
            "fuentes": [meta.get("html_url") or f"https://github.com/{full_name}"], "borrador": True}


PENDIENTE_TXT = PENDING + ":"


def slug_id(value: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


def validate_spec(spec: dict, compact: dict, *, batch_ids: set[str]) -> list[str]:
    errors = []
    rid = spec.get("id") or "?"
    for key in ("gh", "id", "cat", "sub", "kind", "one"):
        if not spec.get(key) and spec.get(key) != 0:
            errors.append(f"{rid}: falta «{key}»")
    if spec.get("kind") and spec["kind"] not in ROLE:
        errors.append(f"{rid}: tipo «{spec['kind']}» desconocido ({', '.join(sorted(ROLE))})")
    if not spec.get("borrador"):
        if not 60 <= len(spec.get("one") or "") <= 175:
            errors.append(f"{rid}: «one» debe tener 60-175 caracteres (tiene {len(spec.get('one') or '')})")
        if len(spec.get("examples") or []) != 2 or len(spec.get("try") or []) != 2:
            errors.append(f"{rid}: hacen falta 2 «examples» y «try» = [acción, resultado]")
        for f in ("que_es", "que_hace", "como_lo_hace", "how"):
            if not (spec.get(f) or "").strip():
                errors.append(f"{rid}: falta «{f}»")
        if not spec.get("fuentes"):
            errors.append(f"{rid}: faltan «fuentes»")
    cats = {int(c["num"]): {s["key"] for s in c.get("subs", [])} for c in compact.get("categories", [])}
    if spec.get("cat") is not None and int(spec["cat"]) not in cats:
        errors.append(f"{rid}: la categoría {spec['cat']} no existe")
    elif spec.get("sub") and spec["sub"] not in cats.get(int(spec["cat"]), set()):
        errors.append(f"{rid}: la subcategoría «{spec['sub']}» no existe en la categoría {spec['cat']}")
    ids = {r["id"] for r in compact.get("repos", []) if not r.get("alias_of")} | batch_ids
    combos = spec.get("combina_con") or []
    ligero = bool(spec.get("ligero"))
    lo = 0 if ligero or spec.get("borrador") else MIN_COMBOS
    if not lo <= len(combos) <= MAX_COMBOS:
        errors.append(f"{rid}: combina_con debe tener {lo}-{MAX_COMBOS} elementos (tiene {len(combos)}); usa --ligero para 0-{MAX_COMBOS}")
    seen = set()
    for combo in combos:
        cid = combo.get("id")
        if cid not in ids:
            errors.append(f"{rid}: combina_con apunta a «{cid}», que no existe")
        if cid == rid or cid in seen:
            errors.append(f"{rid}: combina_con repetido o autorreferente ({cid})")
        if cid in set(spec.get("alt") or []):
            errors.append(f"{rid}: «{cid}» es alternativa, no combinación")
        if not (combo.get("motivo") or "").strip():
            errors.append(f"{rid}: «{cid}» sin motivo")
        seen.add(cid)
    return errors


def build_entries(spec: dict, fetched: dict, root: Path, date: str, lote: str) -> tuple[dict, dict]:
    """Entrada compacta + ficha de detalle a partir de la spec y la identidad leída."""
    base = _curation_base(root, date)
    meta = fetched["metadata"]
    readme = fetched.get("readme") or {"html_url": meta.get("html_url"), "sha": None, "content": ""}
    text = base64.b64decode(readme.get("content") or "").decode("utf8", errors="replace")
    rid = spec["id"]
    entry = {"id": rid, "kind": spec["kind"], "cat": int(spec["cat"]), "sub": spec["sub"], "one": spec["one"]}
    groups = {"local": base.LOCAL, "local_choice": base.LOCAL_CHOICE, "optional": base.OPTIONAL, "required": base.REQUIRED,
              "depends": base.PROVIDER}
    for key, group in groups.items():
        (group.add if spec.get("ai") == key else group.discard)(rid)
    (base.READY.add if spec.get("ready") else base.READY.discard)(rid)
    if spec.get("cmd"):
        base.ENTRY_COMMANDS[rid] = spec["cmd"]
    else:
        base.ENTRY_COMMANDS.pop(rid, None)
    access = base.access_profile(entry, readme, text)
    access["antigravity"] = "not_documented"
    access.update(spec.get("access") or {})
    start = base.starting(entry, readme, text, access, meta)
    if spec.get("url"):
        start["entry_url"] = spec["url"]
    if spec.get("steps"):
        start["steps"] = list(spec["steps"])
    lic = spec.get("license") or (meta.get("license") or {}).get("spdx_id")
    ligero = bool(spec.get("ligero"))
    repo = {"id": rid, "name": spec.get("name") or rid, "cat": int(spec["cat"]), "sub": spec["sub"], "role": ROLE[spec["kind"]],
            "exec": "hybrid" if access.get("api") in {"optional", "required", "depends"} else "local",
            "setup": spec.get("setup", "medium"), "mcp": spec["kind"] == "mcp" or bool(spec.get("mcp")),
            "prov": list(spec.get("prov") or []), "tags": list(spec.get("tags") or []), "stars": meta.get("stargazers_count", 0),
            "gh": meta["full_name"], "lib": False, "pick": False, "one": spec["one"], "alt": [], "doc": f"human/fichas/{rid}.md",
            "github_id": meta["id"], "lang": meta.get("language"), "license": lic, "added_at": date, "github_checked": date,
            "goals": list(spec.get("goals") or []), "source_archived": False}
    if ligero:
        repo["nivel"] = LIGERO
    if spec.get("borrador"):
        repo["borrador"] = True
    repo["routes"] = access_routes({"access": access})
    files = [i["path"] for i in (fetched.get("tree") or {}).get("tree", []) if i.get("type") == "blob"]
    manifests = [p for p in files if p in MANIFESTS]
    limits = "Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada."
    if int(spec["cat"]) == 16:
        limits += " Las pruebas activas requieren un alcance autorizado y un entorno adecuado."
    if spec.get("caveat"):
        limits += " " + spec["caveat"].strip()
    scenarios = list(spec.get("examples") or [])
    action, success = (list(spec.get("try") or []) + ["", ""])[:2]
    detail = {
        "name": repo["name"], "cat": repo["cat"], "sub": repo["sub"], "desc": spec["one"], "how": spec.get("how") or "",
        "install": "Sigue la instalación y el ejemplo mínimo en " + (readme.get("html_url") or meta.get("html_url")),
        "cases": scenarios or [spec["one"]], "stack": ", ".join([v for v in [meta.get("language"), *manifests] if v]),
        "choose_if": "Tu objetivo encaja con estos ejemplos: " + "; ".join(scenarios), "avoid_if": spec.get("avoid") or AVOID[spec["kind"]],
        "limits": limits, "combines_with": [], "alternatives": [], "repo": meta.get("html_url"), "homepage": meta.get("homepage") or None,
        "license": lic, "lang": meta.get("language"), "updated": date, "doc": f"human/fichas/{rid}.md",
        "access": access, "getting_started": start, "first_step": start["steps"][0],
        "sources": {"readme_blob_sha": readme.get("sha"), "root_tree_sha": (fetched.get("tree") or {}).get("sha"),
                    "readme_url": readme.get("html_url"), "github_checked": date, "collection": f"altas-{lote}"},
        "why": "Usos propuestos: " + "; ".join(scenarios) + ".", "models": spec.get("models") or "No usa LLM ni API de IA",
        "source_archived": False,
        "practical_examples": [{"scenario": s, "status": "illustrative"} for s in scenarios],
        "first_try": {"action": action, "success": success, "execution": "proposed_not_executed"},
        "editorial_review": {"status": "draft" if spec.get("borrador") else "source_reviewed", "checked_at": date,
                             "source": readme.get("html_url"), "source_blob_sha": readme.get("sha"),
                             "previous_category": [repo["cat"], repo["sub"]], "category_verdict": "confirmed",
                             "note": spec.get("note") or access.get("api_note", ""),
                             "checks": ["identity", "category", "examples", "installation_source", "api_costs", "claude_code", "codex",
                                        "antigravity", "local_model"], "installation_tested": False},
    }
    if ligero:
        detail["nivel"] = LIGERO
    if spec.get("cmd") and spec["cmd"] not in text:
        detail.setdefault("_avisos", []).append(f"el comando de entrada «{spec['cmd']}» no aparece en el README")
    apply_four_sections(detail, spec, fetched, date, lote)
    return repo, detail


def four_section_record(spec: dict, fetched: dict, date: str) -> dict:
    meta = fetched["metadata"]
    github = {"name_with_owner": meta["full_name"], "archived": bool(meta.get("archived")), "pushed_at": (meta.get("pushed_at") or "")[:10],
              "license": (meta.get("license") or {}).get("spdx_id"), "primary_language": meta.get("language"), "checked_at": date}
    if fetched.get("release"):
        github["latest_release"] = fetched["release"]
    record = {k: spec[k] for k in ("que_es", "que_hace", "como_lo_hace") if spec.get(k)}
    record["combina_con"] = [dict(c) for c in spec.get("combina_con") or []]
    if spec.get("notas"):
        record["notas"] = spec["notas"]
    record["fuentes"] = list(spec.get("fuentes") or [])
    record["github"] = github
    return record


def apply_four_sections(detail: dict, spec: dict, fetched: dict, date: str, lote: str) -> None:
    rec = four_section_record(spec, fetched, date)
    for f in ("que_es", "que_hace", "como_lo_hace"):
        detail[f] = (rec.get(f) or "").strip()
    detail["combina_con"] = [{k: v for k, v in {"id": c["id"], "motivo": (c.get("motivo") or "").strip(),
                                                 "orden_instalacion": (c.get("orden_instalacion") or "").strip()}.items() if v}
                             for c in rec["combina_con"]]
    detail["combines_with"] = [c["id"] for c in detail["combina_con"]]
    if rec.get("notas"):
        detail["descripcion_notas"] = rec["notas"].strip()
    detail["descripcion_fuentes"] = rec["fuentes"]
    detail["descripcion_revision"] = {"batch": f"altas-{lote}", "checked_at": date,
                                      "status": "draft" if spec.get("borrador") else "source_reviewed", "installation_tested": False}
    detail["descripcion_github"] = rec["github"]


# --------------------------------------------------------------------------------------------
# Combinaciones
# --------------------------------------------------------------------------------------------

def ligero_ids(compact: dict) -> set[str]:
    return {r["id"] for r in compact.get("repos", []) if r.get("nivel") == LIGERO}


def suggest_combos(rid: str, compact: dict, detail: dict, limit: int = MAX_COMBOS) -> list[dict]:
    """Combinaciones candidatas para ``rid`` con su razón. No escribe nada.

    Señales (de más a menos peso): lo que ya combinan sus alternativas (3), repos del mismo
    tema práctico en otra subcategoría (2), hubs de su categoría (1) y repos de su categoría
    en otra subcategoría (0,5). Los repos de su misma subcategoría suelen competir con él, así
    que solo cuentan si los combina una alternativa.
    Nunca propone alternativas, retirados, alias ni combinaciones ya presentes.
    """
    repos = {r["id"]: r for r in compact.get("repos", []) if not r.get("alias_of") and int(r.get("cat") or 0) > 0}
    me = repos.get(rid)
    if not me:
        raise AddError(f"«{rid}» no está en el catálogo")
    alts = set(me.get("alt") or [])
    own = {c["id"] for c in (detail.get(rid) or {}).get("combina_con") or []}
    combos = combo_map(detail)
    hub_counts = Counter(t for ts in combos.values() for t in ts)
    score: dict[str, float] = Counter()
    why: dict[str, list[str]] = {}

    def vote(cid: str, pts: float, reason: str) -> None:
        if cid == rid or cid in alts or cid in own or cid not in repos:
            return
        score[cid] += pts
        why.setdefault(cid, [])
        if reason not in why[cid]:
            why[cid].append(reason)

    for alt in alts:
        for cid in combos.get(alt, []):
            vote(cid, 3, f"lo combina {repos.get(alt, {}).get('name', alt)}, alternativa de este repo")
    for cid, n in hub_counts.items():
        if n >= HUB_THRESHOLD and cid in repos and repos[cid]["cat"] == me["cat"]:
            vote(cid, 1, f"hub de la categoría {me['cat']} ({n} repos lo combinan)")
    for area in (compact.get("discovery") or {}).get("areas", []):
        for topic in area.get("topics", []):
            members = set(topic.get("repos") or [])
            for sel in topic.get("selectors") or []:
                members |= {r["id"] for r in repos.values() if r["cat"] == sel.get("cat") and r["sub"] in (sel.get("subs") or [])}
            if rid in members:
                for cid in members:
                    if repos.get(cid, {}).get("sub") != me["sub"]:
                        vote(cid, 2, f"misma área práctica ({area.get('title')} › {topic.get('title')})")
    for cid, r in repos.items():
        if r["cat"] == me["cat"] and r["sub"] != me["sub"]:
            vote(cid, 0.5, f"misma categoría, otra subcategoría ({r['sub']})")
    ranked = sorted(score, key=lambda c: (-score[c], -(repos[c].get("stars") or 0), c))[:limit]
    return [{"id": c, "puntos": score[c], "razon": "; ".join(why[c]),
             "motivo": f"Sugerida por {why[c][0]}. Revisa que la integración tenga sentido antes de publicarla.",
             "orden_instalacion": f"Instala primero {repos[rid]['name']} y después {repos[c]['name']}; comprueba cada pieza por separado."}
            for c in ranked]


def reciprocate(detail: dict, names: dict[str, str], *, exempt: set[str], only_sources: set[str] | None = None) -> dict[str, list[dict]]:
    """Añade la combinación recíproca B→A cuando A→B no la cumple la política y B tiene hueco (< 6).

    Igual que ``scripts/reciprocar_combinaciones.py``: no inventa integraciones, cita el motivo de A.
    Devuelve las altas por destino. Los repos exentos (``ligero``) no reciben recíprocas.
    """
    additions: dict[str, list[dict]] = {}
    for a, b in classify(combo_map(detail), exempt=exempt)["violation"]:
        if only_sources is not None and a not in only_sources and b not in only_sources:
            continue
        if len(detail[b].get("combina_con") or []) + len(additions.get(b, [])) >= MAX_COMBOS:
            continue
        src = next(c for c in detail[a]["combina_con"] if c["id"] == b)
        motivo = src["motivo"].strip().rstrip(".")
        additions.setdefault(b, []).append({
            "id": a, "motivo": f"Combinación recíproca: {names.get(a, a)} lo enlaza como «{motivo}».",
            "orden_instalacion": f"Orden indicado desde {names.get(a, a)}: {(src.get('orden_instalacion') or 'sin orden específico').strip()}",
            "reciproca_de": a})
    for b, new in additions.items():
        detail[b]["combina_con"] = list(detail[b].get("combina_con") or []) + new
        detail[b]["combines_with"] = [c["id"] for c in detail[b]["combina_con"]]
    return additions


def sync_four_files(root: Path, additions: dict[str, list[dict]], extra: dict[str, dict] | None = None) -> dict[str, dict]:
    """Copia las recíprocas al lote de ``curation/descripciones-4s`` que define cada destino."""
    last: dict[str, str] = {}
    for f in sorted(glob.glob(str(root / "curation/descripciones-4s/*.json"))):
        for rid, e in (json.loads(Path(f).read_text(encoding="utf8")).get("repos") or {}).items():
            if isinstance(e, dict) and e.get("combina_con"):
                last[rid] = f
    files: dict[str, dict] = dict(extra or {})
    for b, new in additions.items():
        f = last.get(b)
        if extra:
            f = next((k for k, doc in extra.items() if b in doc.get("repos", {})), f)
        if not f:
            continue
        doc = files.setdefault(f, json.loads(Path(f).read_text(encoding="utf8")))
        entry = doc["repos"][b]
        have = {c["id"] for c in entry.get("combina_con") or []}
        entry["combina_con"] = list(entry.get("combina_con") or []) + [dict(n) for n in new if n["id"] not in have]
    return files


# --------------------------------------------------------------------------------------------
# Lote completo
# --------------------------------------------------------------------------------------------

@dataclass
class AddResult:
    added: list[dict] = field(default_factory=list)
    skipped: list[dict] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    reciprocal: dict[str, list[str]] = field(default_factory=dict)
    new_subs: list[str] = field(default_factory=list)
    written: list[str] = field(default_factory=list)


def load_batch(path: Path) -> dict:
    text = path.read_text(encoding="utf8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        import yaml
        return yaml.safe_load(text)
    return json.loads(text)


def _declare_subs(compact: dict, subs: list[dict], result: AddResult) -> None:
    for s in subs or []:
        cat = next((c for c in compact["categories"] if int(c["num"]) == int(s["cat"])), None)
        if cat is None:
            raise AddError(f"subcategoría nueva {s}: la categoría no existe")
        if s["key"] in {x["key"] for x in cat.get("subs", [])}:
            continue
        cat.setdefault("subs", []).append({"key": s["key"], "title": s["title"]})
        result.new_subs.append(f"{s['cat']}/{s['key']}")


def recount(compact: dict, date: str) -> None:
    for cat in compact["categories"]:
        cat["count"] = sum(int(r["cat"]) == int(cat["num"]) and not r.get("alias_of") for r in compact["repos"])
    for goal in (compact.get("discovery") or {}).get("goals", []):
        members = [r for r in compact["repos"] if goal["id"] in r.get("goals", []) or r["id"] in goal.get("starters", []) + goal.get("guided", [])]
        goal["categories"] = sorted({r["cat"] for r in members})
    total = sum(not r.get("alias_of") for r in compact["repos"])
    compact["meta"]["updated"] = date
    compact["meta"]["title"] = f"Índice IA — {total} repos curados de IA, automatización y herramientas"


def run_add(root: Path, batch: dict, *, gh: GhFn = gh_api, force: bool = False, ligero: bool = False, simulate: bool = False,
            date: str | None = None, fetched_cache: dict[str, dict] | None = None) -> AddResult:
    """Da de alta un lote. Si cualquier repo falla la validación, no escribe nada."""
    date = date or batch.get("fecha") or today()
    lote = batch.get("lote") or f"manual-{date}"
    compact = json.loads((root / "INDICE_IA.json").read_text(encoding="utf8"))
    detail_doc = json.loads((root / "INDICE_IA.detalle.json").read_text(encoding="utf8"))
    detail = detail_doc["repos"]
    retired = json.loads((root / "data/retired.json").read_text(encoding="utf8")) if (root / "data/retired.json").exists() else {"repos": []}
    result = AddResult()
    _declare_subs(compact, batch.get("subcategorias_nuevas") or [], result)
    specs = [dict(s) for s in batch.get("repos") or []]
    for s in specs:
        if ligero:
            s.setdefault("ligero", True)
    skipped_ids: set[str] = set()
    errors: list[str] = []
    built: list[tuple[dict, dict, dict, dict]] = []
    for spec in specs:
        full = spec.get("gh") or ""
        try:
            fetched = (fetched_cache or {}).get(full.lower()) or fetch_identity(full, gh)
        except AddError as error:
            result.skipped.append({"gh": full, "motivo": str(error)})
            skipped_ids.add(spec.get("id"))
            continue
        meta = fetched["metadata"]
        if meta.get("full_name", "").lower() != full.lower():
            result.warnings.append(f"{full}: el nombre canónico es {meta.get('full_name')}; se usa ese")
            spec["gh"] = meta["full_name"]
        errs, warns = check_identity(meta, spec.get("id") or "", compact, retired, force=force, now=date)
        result.warnings += warns
        if errs:
            result.skipped.append({"gh": full, "motivo": "; ".join(errs), **summary(meta)})
            skipped_ids.add(spec.get("id"))
            continue
        built.append((spec, fetched, meta, {}))
    # validación con los ids del lote que sí pasan
    kept_ids = {s["id"] for s, *_ in built}
    for spec, *_ in built:
        dropped = [c["id"] for c in spec.get("combina_con") or [] if c.get("id") in skipped_ids]
        if dropped:
            result.warnings.append(f"{spec['id']}: se quitan combinaciones con repos omitidos del lote ({', '.join(dropped)})")
        spec["combina_con"] = [c for c in spec.get("combina_con") or [] if c.get("id") not in skipped_ids]
        spec["alt"] = [a for a in spec.get("alt") or [] if a not in skipped_ids]
        errors += validate_spec(spec, compact, batch_ids=kept_ids)
    if errors:
        raise AddError("Lote no válido:\n- " + "\n- ".join(errors))
    four_doc = {"batch": f"altas-{lote}", "checked_at": date,
                "method": batch.get("metodo") or ("Lectura del README y la documentación oficial enlazada; estado del repositorio leído con la "
                                                 "API de GitHub autenticada. No se instaló ni ejecutó ningún proyecto."), "repos": {}}
    by_id = {r["id"]: r for r in compact["repos"]}
    for spec, fetched, meta, _ in built:
        repo, d = build_entries(spec, fetched, root, date, lote)
        for warning in d.pop("_avisos", []):
            result.warnings.append(f"{spec['id']}: {warning}")
        compact["repos"].append(repo)
        detail[spec["id"]] = d
        by_id[spec["id"]] = repo
        four_doc["repos"][spec["id"]] = four_section_record(spec, fetched, date)
        result.added.append({"id": spec["id"], "nivel": LIGERO if spec.get("ligero") else "completo",
                             "borrador": bool(spec.get("borrador")), **summary(meta)})
    # alternativas: grupos del lote + "alt" por repo (simétricas)
    groups = [list(g) for g in batch.get("alt_groups") or []]
    for spec, *_ in built:
        for other in spec.get("alt") or []:
            groups.append([spec["id"], other])
    for group in groups:
        for left in group:
            for right in group:
                if left == right or left not in by_id or right not in by_id:
                    continue
                alts = by_id[left].setdefault("alt", [])
                if right not in alts:
                    alts.append(right)
                detail[left]["alternatives"] = list(alts)
                if right in detail[left].get("combines_with", []):
                    raise AddError(f"{left}: «{right}» es alternativa y combinación a la vez")
    # reciprocidad automática dentro del límite de 6
    names = {r["id"]: r.get("name") or r["id"] for r in compact["repos"]}
    adds = reciprocate(detail, names, exempt=ligero_ids(compact), only_sources=set(kept_ids))
    result.reciprocal = {b: [c["id"] for c in v] for b, v in adds.items()}
    remaining = classify(combo_map(detail), exempt=ligero_ids(compact))["violation"]
    if remaining:
        raise AddError(f"Quedan combinaciones sin reciprocidad posible: {remaining[:10]}")
    recount(compact, date)
    if simulate or not built:
        return result
    four_path = root / f"curation/descripciones-4s/48-altas-{lote}.json"
    files = sync_four_files(root, adds, {str(four_path): four_doc})
    (root / "INDICE_IA.json").write_text(json.dumps(compact, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    (root / "INDICE_IA.detalle.json").write_text(json.dumps(detail_doc, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    result.written += ["INDICE_IA.json", "INDICE_IA.detalle.json"]
    for f, doc in files.items():
        Path(f).parent.mkdir(parents=True, exist_ok=True)
        Path(f).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        result.written.append(str(Path(f).relative_to(root)))
    spec_path = root / f"curation/altas/{lote}.json"
    spec_path.parent.mkdir(parents=True, exist_ok=True)
    stored = {k: v for k, v in batch.items() if k != "repos"}
    stored.update(lote=lote, fecha=date, repos=[{k: v for k, v in s.items() if k not in {"que_es", "que_hace", "como_lo_hace", "combina_con",
                                                                                         "notas", "fuentes"}} for s, *_ in built])
    spec_path.write_text(json.dumps(stored, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    report = root / "reports/altas" / f"{lote}.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps({"lote": lote, "checked_at": date, "added": result.added, "skipped": result.skipped,
                                  "warnings": result.warnings, "reciprocal": result.reciprocal, "new_subs": result.new_subs,
                                  "notes": ["No se instaló ni se ejecutó ningún proyecto del catálogo.",
                                            "Identidades verificadas con la API de GitHub (id numérico, propietario, licencia, archivado)."]},
                                 ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    result.written += [str(spec_path.relative_to(root)), str(report.relative_to(root))]
    return result


def apply_suggested(root: Path, rid: str, picks: list[dict], date: str | None = None) -> dict[str, list[str]]:
    """Escribe combinaciones sugeridas en ``rid`` (hasta 6) y completa la reciprocidad."""
    compact = json.loads((root / "INDICE_IA.json").read_text(encoding="utf8"))
    doc = json.loads((root / "INDICE_IA.detalle.json").read_text(encoding="utf8"))
    detail = doc["repos"]
    current = list(detail[rid].get("combina_con") or [])
    room = MAX_COMBOS - len(current)
    new = [{"id": p["id"], "motivo": p["motivo"], "orden_instalacion": p["orden_instalacion"]} for p in picks[:max(room, 0)]]
    detail[rid]["combina_con"] = current + new
    detail[rid]["combines_with"] = [c["id"] for c in detail[rid]["combina_con"]]
    names = {r["id"]: r.get("name") or r["id"] for r in compact["repos"]}
    adds = reciprocate(detail, names, exempt=ligero_ids(compact), only_sources={rid})
    last = None
    for f in sorted(glob.glob(str(root / "curation/descripciones-4s/*.json"))):
        if rid in (json.loads(Path(f).read_text(encoding="utf8")).get("repos") or {}):
            last = f
    files = sync_four_files(root, adds)
    if last:
        d = files.setdefault(last, json.loads(Path(last).read_text(encoding="utf8")))
        have = {c["id"] for c in d["repos"][rid].get("combina_con") or []}
        d["repos"][rid]["combina_con"] = list(d["repos"][rid].get("combina_con") or []) + [c for c in new if c["id"] not in have]
    (root / "INDICE_IA.detalle.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    for f, d in files.items():
        Path(f).write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    return {"añadidas": [c["id"] for c in new], **{f"recíproca en {b}": [c["id"] for c in v] for b, v in adds.items()}}
