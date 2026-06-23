from pathlib import Path

from repo_intelligence.git.discover import discover_repos


def test_discover_empty_base(tmp_path: Path) -> None:
    assert discover_repos(tmp_path) == []
