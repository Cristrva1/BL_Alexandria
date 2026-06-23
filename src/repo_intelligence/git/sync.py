from __future__ import annotations

import subprocess
from pathlib import Path

from repo_intelligence.git.status import dirty, is_git_repo


def safe_pull(repo: Path) -> tuple[str, str]:
    if not is_git_repo(repo):
        return "skipped", "not a git repo"
    if dirty(repo):
        return "skipped", "dirty working tree"
    result = subprocess.run(
        ["git", "pull", "--ff-only"],
        cwd=repo,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output = (result.stdout + "\n" + result.stderr).strip()
    return ("updated" if result.returncode == 0 else "failed", output)
