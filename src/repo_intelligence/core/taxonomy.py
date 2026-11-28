"""Compile practical areas and subtopics without duplicating repository records.

The canonical selectors live in INDICE_IA.json / discovery.areas. A project can
belong to several practical collections while keeping its stable technical cat/sub.
Unknown selectors fail the build instead of silently creating an incomplete shelf.
"""
from copy import deepcopy
from repo_intelligence.core.access import SUPPORTED_CLIENT


def goal_memberships(compact: dict) -> dict[str, list[str]]:
    """Combine direct editorial goals, guided starters and the minimum recipe steps."""
    memberships = {r["id"]: list(r.get("goals", [])) for r in compact.get("repos", [])}
    recipes = {r["id"]: r for r in compact.get("recipes", [])}
    for goal in compact.get("discovery", {}).get("goals", []):
        members = set(goal.get("guided", [])) | set(goal.get("starters", []))
        for recipe_id in goal.get("recipe_ids", []):
            members.update(recipes.get(recipe_id, {}).get("plan", {}).get("minimum", []))
        for rid in members & memberships.keys():
            if goal["id"] not in memberships[rid]:
                memberships[rid].append(goal["id"])
    return memberships


def build_areas(compact: dict, repos: list[dict]) -> list[dict]:
    sources = compact.get("discovery", {}).get("areas", [])
    if not sources:
        return []
    by_id = {r["id"]: r for r in repos}
    categories = {c["num"]: c for c in compact.get("categories", [])}
    area_ids, topic_ids, areas = set(), set(), []
    for source in sources:
        area = deepcopy(source)
        aid = area["id"]
        if aid in area_ids:
            raise ValueError(f"Duplicate area: {aid}")
        area_ids.add(aid)
        members = set()
        for topic in area["topics"]:
            tid = topic["id"]
            if tid in topic_ids:
                raise ValueError(f"Duplicate topic: {tid}")
            topic_ids.add(tid)
            selected = set(topic.get("repos", [])) | set(topic.get("reference_repos", []))
            unknown = selected - by_id.keys()
            if unknown:
                raise ValueError(f"{tid}: unknown repositories {sorted(unknown)}")
            for selector in topic.get("selectors", []):
                category = categories.get(selector["cat"])
                if not category:
                    raise ValueError(f"{tid}: unknown category {selector['cat']}")
                subs = selector.get("subs", [])
                if set(subs) - {s["key"] for s in category.get("subs", [])}:
                    raise ValueError(f"{tid}: unknown sections {subs}")
                selected.update(r["id"] for r in repos if r["cat"] == selector["cat"] and (not subs or r.get("sub") in subs))
            selected.difference_update(topic.get("exclude", []))
            if not selected:
                raise ValueError(f"Empty practical topic: {tid}")
            starters = topic.get("guided_starters", [])
            if len(starters) > 3 or len(starters) != len(set(starters)) or set(starters) - selected:
                raise ValueError(f"{tid}: invalid guided starters {starters}")
            if topic.get("reference_only") and starters:
                raise ValueError(f"{tid}: a reference topic cannot have guided starters")
            topic["repo_ids"] = sorted(selected)
            topic["count"] = len(selected)
            members.update(selected)
        area["repo_ids"] = sorted(members)
        area["count"] = len(members)
        references = {rid for t in area["topics"] for rid in t.get("reference_repos", [])}
        if area.get("client") in {"claude_code", "codex", "antigravity"}:
            for rid in members - references:
                if by_id[rid].get("access", {}).get(area["client"]) not in SUPPORTED_CLIENT:
                    raise ValueError(f"{aid}: no documented client support for {rid}")
        evidence = {e["repo_id"] for e in area.get("evidence", [])}
        if references - evidence or (area.get("client") == "antigravity" and members - evidence):
            raise ValueError(f"{aid}: missing source evidence for setup references")
        for rid in area.get("starters", []):
            if rid not in members:
                raise ValueError(f"{aid}: starter {rid} is outside its topics")
        areas.append(area)
    uncovered = set(by_id) - {rid for area in areas if area.get("kind") == "work" for rid in area["repo_ids"]}
    if uncovered:
        raise ValueError(f"Repositories without a practical work area: {sorted(uncovered)}")
    return areas


def attach_areas(repos: list[dict], areas: list[dict]) -> None:
    """Add derived facets and vocabulary for deterministic browser search."""
    by_id = {r["id"]: r for r in repos}
    for repo in repos:
        repo.update(areas=[], topics=[], discovery_text="")
    for area in areas:
        for rid in area["repo_ids"]:
            repo = by_id[rid]
            repo["areas"].append(area["id"])
            repo["discovery_text"] += " " + " ".join([area["title"], *area.get("keywords", [])])
        for topic in area["topics"]:
            for rid in topic["repo_ids"]:
                repo = by_id[rid]
                repo["topics"].append(topic["id"])
                repo["discovery_text"] += " " + " ".join([topic["title"], *topic.get("keywords", [])])
