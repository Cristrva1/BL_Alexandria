"""Retired repos stay out of the catalog, keep provenance and point to live replacements."""
import json
from pathlib import Path

from repo_intelligence.core.catalog import load_catalog
from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]
LEDGER = json.loads((ROOT / "data/retired.json").read_text(encoding="utf-8"))


def test_retired_ledger_is_consistent_with_the_catalog():
    catalog = load_catalog(ROOT)
    entries = LEDGER["repos"]
    ids = [e["id"] for e in entries]
    assert len(ids) == len(set(ids))
    assert len({e["github_id"] for e in entries}) == len(entries)
    for entry in entries:
        assert catalog.get(entry["id"]) is None, entry["id"]
        assert entry["reason"] in LEDGER["reasons"]
        assert entry["gh"] and isinstance(entry["github_id"], int)
        assert entry["evidence"] and entry["retired_at"]
        for replacement in entry["replaced_by"]:
            assert catalog.get(replacement) is not None, (entry["id"], replacement)
            assert replacement not in ids
    live = {r.get("github_id") for r in catalog.repos}
    assert not live & {e["github_id"] for e in entries}


def test_no_card_or_navigation_points_to_a_retired_repo():
    retired = {e["id"] for e in LEDGER["repos"]}
    catalog = build_catalog(ROOT)
    for repo in catalog["repos"]:
        for key in ("alt", "alternatives", "combines_with"):
            assert not set(repo.get(key) or []) & retired, (repo["id"], key)
    for area in catalog["discovery"]["areas"]:
        assert not set(area.get("starters") or []) & retired
        for topic in area["topics"]:
            assert not set(topic["repo_ids"]) & retired, topic["id"]
    for goal in catalog["discovery"]["goals"]:
        assert not set(goal.get("starters") or []) & retired
        assert not set(goal.get("guided") or []) & retired
    for recipe in catalog["recipes"]:
        assert not set(json.dumps(recipe, ensure_ascii=False).split('"')) & retired, recipe["id"]
