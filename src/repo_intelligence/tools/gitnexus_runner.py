from __future__ import annotations

import subprocess
from pathlib import Path


def analyze_repo(repo: Path, force: bool = False) -> int:
    args = ["gitnexus", "analyze"]
    if force:
        args.append("--force")
    args.append(".")
    result = subprocess.run(args, cwd=repo, check=False)
    return result.returncode
