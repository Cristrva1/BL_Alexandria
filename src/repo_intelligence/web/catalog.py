"""Arma el catálogo que consume el sitio educativo."""

from __future__ import annotations

from repo_intelligence.analysis.combina_policy import combo_map, used_by

import re
from pathlib import Path
from repo_intelligence.core.taxonomy import attach_areas, build_areas
from repo_intelligence.core.access import access_facts, access_routes, API_LABELS, CLIENT_LABELS, LOCAL_LABELS, COST_LABELS, HARDWARE_LABELS, ROUTE_LABELS
from repo_intelligence.core.reading import GUIDES
from repo_intelligence.core.handbook import load_handbook
from repo_intelligence.core.techniques import load_techniques
from repo_intelligence.core.access import AUDIENCE_LABELS

from repo_intelligence.menu.export import derive_install
from repo_intelligence.web.lessons import (
    CATEGORY_LESSONS,
    COPY,
    GLOSSARY,
    JOURNEYS,
    LABELS,
    LESSONS,
    RECIPE_LESSONS,
    ROLE_WHY,
    TOOL_NOTES,
)

_SETUP_RANK = {"easy": 0, "medium": 1, "heavy": 2}
_ROLE_RANK = {
    "platform": 0,
    "runtime": 1,
    "app": 2,
    "library": 3,
    "skill": 4,
    "directory": 5,
}
_JUNK_PREFIXES = (
    ">",
    "thanks to",
    "this project is kept",
    "important notice",
    "request a trial",
    "the easiest way to get started",
    "official sources only",
    "dev is the default branch",
)


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (value or "").lower())


def _build_index(repo_ids: list[str]) -> dict[str, str]:
    """Map exact ids and unambiguous punctuation-insensitive aliases."""
    index: dict[str, str] = {}
    folded_owner: dict[str, str] = {}
    ambiguous: set[str] = set()
    for repo_id in repo_ids:
        index[repo_id] = repo_id
        key = _norm(repo_id)
        previous = folded_owner.get(key)
        if previous is not None and previous != repo_id:
            ambiguous.add(key)
        else:
            folded_owner[key] = repo_id
    for key, repo_id in folded_owner.items():
        if key in ambiguous:
            continue
        index.setdefault(key, repo_id)
    return index


def _resolve(token: str, index: dict[str, str]) -> str | None:
    if not token:
        return None
    if token in index:
        return index[token]
    return index.get(_norm(token))


def _is_junk(text: str, name: str) -> bool:
    raw = (text or "").strip()
    folded = raw.lower().lstrip(">").strip()
    if len(folded) < 25:
        return True
    if folded == (name or "").strip().lower():
        return True
    if raw.lower().startswith(_JUNK_PREFIXES) or folded.startswith(_JUNK_PREFIXES):
        return True
    if any(marker in folded for marker in ("cryptocurrency", "pump.fun", "important notice", "not affiliated")):
        return True
    if len(folded) < 240 and any(marker in folded for marker in ("read the docs", "blog post", "arxiv")):
        return True
    return False


def _prose(text: str, limit: int | None = None) -> str:
    cleaned = re.sub(r"\s+", " ", (text or "").replace("👉", " ").strip())
    if limit is not None and len(cleaned) > limit:
        cut = cleaned[:limit].rsplit(" ", 1)[0].rstrip(".,;:")
        return f"{cut}…"
    return cleaned


def _lead(repo: dict) -> tuple[str, str]:
    """Return (card lead, ficha body). Body is empty when no clean prose exists."""
    name = repo.get("name") or repo.get("id") or ""
    one = repo.get("one") or ""
    desc = repo.get("desc") or ""
    choose = _prose(repo.get("choose_if") or "")
    body = ""
    if not _is_junk(desc, name):
        body = desc.strip()
    elif not _is_junk(one, name):
        body = one.strip()
    if not _is_junk(one, name):
        lead = _prose(one, 220)
    elif body:
        lead = _prose(body, 220)
    elif choose:
        lead = _prose(choose, 220)
    else:
        lead = f"Ficha curada de {name}."
    return lead, body


def _starters(members: list[dict], limit: int = 3) -> list[str]:
    ordered = sorted(
        members,
        key=lambda repo: (
            _SETUP_RANK.get(repo.get("setup") or "", 9),
            _ROLE_RANK.get(repo.get("role") or "", 9),
            (repo.get("name") or "").lower(),
        ),
    )
    return [repo["id"] for repo in ordered[:limit]]


def _refs(values: list, index: dict[str, str]) -> list[dict[str, str | None]]:
    refs: list[dict[str, str | None]] = []
    seen: set[str] = set()
    for value in values or []:
        text = str(value).strip()
        if not text:
            continue
        hit = _resolve(text, index)
        key = hit or text.lower()
        if key in seen:
            continue
        seen.add(key)
        refs.append({"id": hit, "label": text})
    return refs


def _add_pair(labs: list[dict[str, str]], seen: set[tuple[str, str]], left: str | None, right: str | None) -> None:
    if not left or not right or left == right:
        return
    key = tuple(sorted((left, right)))
    if key in seen:
        return
    seen.add(key)
    labs.append({"a": key[0], "b": key[1]})


def _load_json(path: Path) -> dict:
    import json

    return json.loads(path.read_text(encoding="utf-8"))


def build_catalog(project_root: Path) -> dict:
    """Merge the compact index, the detail index and the teaching layer."""
    root = Path(project_root)
    compact = _load_json(root / "INDICE_IA.json")
    detalle = _load_json(root / "INDICE_IA.detalle.json")
    raw_details = detalle.get("repos") or {}
    if isinstance(raw_details, list):
        details = {item.get("id") or item.get("name"): item for item in raw_details}
    else:
        details = raw_details

    draft: list[dict] = []
    for source in compact.get("repos") or []:
        repo_id = source.get("id")
        if not repo_id or source.get("alias_of") or int(source.get("cat") or 0) == 0:
            continue
        detail = details.get(repo_id) or {}
        alt = source.get("alt") or detail.get("alternatives") or []
        merged = {
            "id": repo_id,
            "name": source.get("name") or detail.get("name") or repo_id,
            "cat": source.get("cat") if source.get("cat") is not None else detail.get("cat") or 0,
            "role": source.get("role") or "",
            "exec": source.get("exec") or "",
            "setup": source.get("setup") or "",
            "mcp": bool(source.get("mcp")),
            "prov": list(source.get("prov") or []),
            "tags": list(source.get("tags") or []),
            "one": source.get("one") or "",
            "desc": detail.get("desc") or "",
            "choose_if": detail.get("choose_if") or "",
            "avoid_if": detail.get("avoid_if") or "",
            "combines_with": list(detail.get("combines_with") or []),
            "alt": list(alt),
            "stack": detail.get("stack") or "",
            "repo_url": detail.get("repo") or "",
            "doc": source.get("doc") or detail.get("doc") or "",
            "agent_tools": list(source.get("agent_tools") or []),
            "sub": source.get("sub") or "",
            "how": detail.get("how") or "",
            "why": detail.get("why") or "",
            "cases": detail.get("cases") or [],
            "gh": source.get("gh") or "",
            "limits": detail.get("limits") or "",
            "getting_started": detail.get("getting_started") or {},
            "first_try": detail.get("first_try") or {},
            "practical_examples": detail.get("practical_examples") or [],
            "editorial_review": detail.get("editorial_review") or {},
            "access": access_facts(detail),
            "routes": access_routes(detail),
            "goals": source.get("goals") or [],
            "added_at": source.get("added_at") or "",
            "status": source.get("status") or "",
            "pick": bool(source.get("pick")),
            "stars": source.get("stars"),
            "license": detail.get("license") or "",
            "homepage": detail.get("homepage") or "",
        }
        # 4-section description: only emitted when curated, to keep catalog.json small.
        combos = [dict(item) for item in detail.get("combina_con") or [] if isinstance(item, dict) and item.get("id")]
        if combos:
            merged["combina_con"] = combos
        if source.get("nivel"):
            merged["nivel"] = source["nivel"]  # alta ligera: combinaciones opcionales
        quality = detail.get("calidad") or {}
        if quality.get("puntuacion") is not None:
            merged["calidad"] = {"puntuacion": quality["puntuacion"], "fecha": quality.get("fecha")}
        if detail.get("complejidad_detalle"):
            cx = detail["complejidad_detalle"]
            merged["complejidad"] = {"nivel": cx["nivel"], "nombre": cx["nombre"], "motivos": cx.get("motivos") or [], "origen": cx.get("origen")}
        if detail.get("similares"):
            merged["similares"] = detail["similares"]
        for field in ("que_es", "que_hace", "como_lo_hace", "licencia_nota", "descripcion_notas", "descripcion_fuentes", "descripcion_revision", "descripcion_github", "descripcion_origen"):
            if detail.get(field):
                merged[field] = detail[field]
        command, confidence, note = derive_install({**merged, "repo": merged["repo_url"]})
        lead, body = _lead(merged)
        merged["lead"] = lead
        merged["body"] = body
        merged["install"] = {
            "command": command,
            "confidence": confidence,
            "note": note,
        }
        draft.append(merged)

    index = _build_index([repo["id"] for repo in draft])
    repos: list[dict] = []
    for repo in draft:
        repo["alt_refs"] = _refs(repo["alt"], index)
        repo["combine_refs"] = _refs(repo["combines_with"], index)
        for combo in repo.get("combina_con", []):
            combo["id"] = _resolve(str(combo["id"]), index) or combo["id"]
        repos.append(repo)
    repos.sort(key=lambda repo: (repo["cat"], (repo["name"] or "").lower(), repo["id"]))
    inbound_free = used_by(combo_map(repos))
    names = {repo["id"]: (repo["name"] or repo["id"]).lower() for repo in repos}
    for repo in repos:
        users = [rid for rid in inbound_free.get(repo["id"], []) if rid in names]
        if users:
            repo["used_by"] = sorted(users, key=lambda rid: names[rid])

    areas = build_areas(compact, repos)
    attach_areas(repos, areas)

    by_cat: dict[int, list[dict]] = {}
    for repo in repos:
        by_cat.setdefault(int(repo["cat"]), []).append(repo)

    categories: list[dict] = []
    seen_nums: set[int] = set()
    for source in compact.get("categories") or []:
        number = int(source["num"])
        seen_nums.add(number)
        lesson = CATEGORY_LESSONS.get(number, {})
        members = by_cat.get(number, [])
        categories.append(
            {
                "num": number,
                "title": source.get("title") or f"Sala {number}",
                "question": source.get("question") or lesson.get("question", ""),
                "blurb": source.get("desc") or lesson.get("blurb", ""),
                "description": source.get("desc") or lesson.get("blurb", ""),
                "subs": source.get("subs") or [],
                "count": len(members),
                "starters": _starters(members),
            }
        )
    for number in sorted(num for num in by_cat if num not in seen_nums):
        lesson = CATEGORY_LESSONS.get(number, {})
        members = by_cat[number]
        categories.append(
            {
                "num": number,
                "title": lesson.get("title") or ("Taller local" if number == 0 else f"Sala {number}"),
                "question": lesson.get("question", ""),
                "blurb": lesson.get("blurb", ""),
                "count": len(members),
                "starters": _starters(members),
            }
        )
    categories.sort(key=lambda cat: cat["num"])

    recipes: list[dict] = []
    for source in compact.get("recipes") or []:
        recipe_id = source.get("id") or ""
        notes = RECIPE_LESSONS.get(recipe_id, {})
        step_notes = dict(notes.get("steps") or {})
        # The curated recipe owns its current steps; teaching notes add context.
        for step in source.get("steps") or []:
            if step.get("id") and step.get("role"):
                step_notes[step["id"]] = step["role"]
        resolved_groups: list[list[str]] = []
        exclusive: dict[str, list[str]] = {}
        for group in notes.get("pick_one") or []:
            resolved = []
            for token in group:
                hit = _resolve(str(token), index)
                if hit and hit not in resolved:
                    resolved.append(hit)
            if len(resolved) < 2:
                continue
            resolved_groups.append(resolved)
            for item in resolved:
                exclusive[item] = [other for other in resolved if other != item]
        steps = []
        for token in source.get("repos") or []:
            hit = _resolve(str(token), index)
            if hit is None:
                steps.append(
                    {
                        "id": None,
                        "label": str(token),
                        "missing": True,
                        "why": "Este nombre no está en el índice.",
                        "exclusive_with": [],
                    }
                )
                continue
            matched = next(repo for repo in repos if repo["id"] == hit)
            why = step_notes.get(hit) or ROLE_WHY.get(matched["role"]) or "Forma parte de esta receta."
            steps.append(
                {
                    "id": hit,
                    "label": matched["name"],
                    "missing": False,
                    "why": why,
                    "exclusive_with": exclusive.get(hit, []),
                }
            )
        recipes.append(
            {
                "id": recipe_id,
                "title": source.get("title") or recipe_id,
                "goal": source.get("goal") or "",
                "how": source.get("how") or "",
                "lesson": notes.get("lesson") or source.get("how") or source.get("goal") or "",
                "pick_one": resolved_groups,
                "steps": steps,
                "plan": source.get("plan") or {},
                "when_not": source.get("when_not") or "",
            }
        )

    labs: list[dict[str, str]] = []
    seen_pairs: set[tuple[str, str]] = set()
    for repo in repos:
        for ref in repo["alt_refs"]:
            _add_pair(labs, seen_pairs, repo["id"], ref["id"])
    for recipe in recipes:
        for group in recipe["pick_one"]:
            for left, right in zip(group, group[1:]):
                _add_pair(labs, seen_pairs, left, right)
            if len(group) > 2:
                _add_pair(labs, seen_pairs, group[0], group[-1])
    labs.sort(key=lambda pair: (pair["a"], pair["b"]))

    guidance = compact.get("model_guidance") or {}
    tools = []
    for tool_id, payload in (guidance.get("tools") or {}).items():
        best = []
        for token in payload.get("best_fit_repos") or []:
            hit = _resolve(str(token), index)
            if hit and hit not in best:
                best.append(hit)
        tools.append(
            {
                "id": tool_id,
                "note": TOOL_NOTES.get(tool_id) or payload.get("note") or "",
                "source_note": payload.get("note") or "",
                "repos": best,
            }
        )

    return {
        "generated_at": (compact.get("meta") or {}).get("updated") or (compact.get("meta") or {}).get("stars_checked") or "",
        "title": (compact.get("meta") or {}).get("title") or "Alejandría",
        "counts": {
            "repos": len(repos),
            "categories": len([cat for cat in categories if cat["num"] >= 1]),
            "areas": len(areas),
            "work_areas": sum(area.get("kind") == "work" for area in areas),
            "tool_collections": sum(area.get("kind") == "tool" for area in areas),
            "topics": sum(len(area["topics"]) for area in areas),
            "technical_subs": sum(len(cat.get("subs", [])) for cat in categories if cat["num"] >= 1),
            "recipes": len(recipes),
            "mcp": sum(1 for repo in repos if repo["mcp"]),
            "labs": len(labs),
        },
        "labels": {**LABELS, "api": API_LABELS, "client": CLIENT_LABELS, "local_model": LOCAL_LABELS, "cost": COST_LABELS, "hardware": HARDWARE_LABELS, "route": ROUTE_LABELS, "audience": AUDIENCE_LABELS},
        "reading": GUIDES,
        "handbook": load_handbook(project_root, {repo['id'] for repo in repos}),
        "techniques": load_techniques(project_root, {repo["gh"]: repo["id"] for repo in repos if repo.get("gh")}),
        "discovery": {**(compact.get("discovery") or {"goals": []}), "areas": areas},
        "access_checked": (compact.get("meta") or {}).get("access_checked") or "",
        "copy": COPY,
        "glossary": GLOSSARY,
        "lessons": LESSONS,
        "journeys": JOURNEYS,
        "role_why": ROLE_WHY,
        "model_guidance": {
            "key_distinction": guidance.get("key_distinction") or "",
            "rule_of_thumb": guidance.get("rule_of_thumb") or "",
            "tools": tools,
        },
        "categories": categories,
        "recipes": recipes,
        "labs": labs,
        "repos": repos,
    }
