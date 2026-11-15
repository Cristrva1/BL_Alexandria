"""The dated stars snapshot must resolve to stable, distinct catalog identities."""

import json
from pathlib import Path

from repo_intelligence.core.catalog import load_catalog
from repo_intelligence.guides.render import _local_ids

ROOT = Path(__file__).resolve().parents[1]


def test_verified_stars_resolve_to_their_github_identity():
    snapshot_path = sorted((ROOT / "reports").glob("github-stars-*.json"))[-1]
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    catalog = load_catalog(ROOT)
    assert len(snapshot["stars"]) == snapshot["count"]
    assert len({star["github_id"] for star in snapshot["stars"]}) == snapshot["count"]
    for star in snapshot["stars"]:
        repo = catalog.get(star["catalog_id"])
        assert repo is not None, star["full_name"]
        assert repo["github_id"] == star["github_id"]
        assert repo["gh"].lower() == star["full_name"].lower()
        assert repo["starred_by"] == snapshot["user"]


def test_catalog_does_not_duplicate_or_conflate_github_repositories():
    catalog = load_catalog(ROOT)
    github = [repo for repo in catalog.repos if repo.get("gh") and not repo.get("alias_of")]
    assert len({repo["gh"].lower() for repo in github}) == len(github)
    assert len({repo["github_id"] for repo in github}) == len(github)
    assert catalog.get("manim")["github_id"] != catalog.get("manim-community")["github_id"]
    assert catalog.get("opencode")["github_id"] != catalog.get("opencode-legacy")["github_id"]


def test_new_star_cards_keep_verifiable_source_provenance():
    snapshot_path = sorted((ROOT / "reports").glob("github-stars-*.json"))[-1]
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    catalog = load_catalog(ROOT)
    for repo_id in snapshot["added_ids"]:
        repo = catalog.get(repo_id)
        assert repo["sources"]["readme_blob_sha"]
        assert repo["sources"]["root_tree_sha"]
        assert repo["how"] and repo["install"] and repo["limits"]
        assert repo["lib"] is False


def test_local_inventory_skips_missing_registered_directories(tmp_path):
    present = tmp_path / "present"
    present.mkdir()
    assert _local_ids([
        {"id": "present", "name": "Present", "path": str(present)},
        {"id": "gone", "name": "Gone", "path": str(tmp_path / "gone")},
    ]) == {"present"}
