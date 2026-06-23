from __future__ import annotations

from pathlib import Path

from repo_intelligence.core.models import RepoRecord
from repo_intelligence.extract.manifests import detect_manifests
from repo_intelligence.extract.readme import find_readme
from repo_intelligence.git import status


def discover_repos(base: Path) -> list[RepoRecord]:
    if not base.exists():
        raise FileNotFoundError(f"Repo library does not exist: {base}")

    records: list[RepoRecord] = []
    for child in sorted(base.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir():
            continue
        is_git = status.is_git_repo(child)
        readme = find_readme(child)
        records.append(
            RepoRecord(
                id=_slug(child.name),
                name=child.name,
                path=str(child),
                is_git=is_git,
                head=status.head(child) if is_git else None,
                branch=status.branch(child) if is_git else None,
                dirty=status.dirty(child) if is_git else False,
                remotes=status.remotes(child) if is_git else [],
                readme=str(readme) if readme else None,
                manifests=[str(path.relative_to(child)) for path in detect_manifests(child)],
                install_mode="reference_only",
            )
        )
    return records


def _slug(name: str) -> str:
    return name.strip().lower().replace(" ", "-").replace("_", "-")
