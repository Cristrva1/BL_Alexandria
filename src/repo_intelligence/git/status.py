from __future__ import annotations

import subprocess
from pathlib import Path


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def is_git_repo(path: Path) -> bool:
    return (path / ".git").exists()


def head(repo: Path) -> str | None:
    value = git(repo, "rev-parse", "HEAD")
    return value or None


def branch(repo: Path) -> str | None:
    value = git(repo, "branch", "--show-current")
    return value or None


def dirty(repo: Path) -> bool:
    return bool(git(repo, "status", "--porcelain"))


def remotes(repo: Path) -> list[str]:
    raw = git(repo, "remote", "-v")
    urls: list[str] = []
    for line in raw.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[1] not in urls:
            urls.append(parts[1])
    return urls
