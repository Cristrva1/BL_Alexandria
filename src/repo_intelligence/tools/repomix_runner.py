from __future__ import annotations

import subprocess
from pathlib import Path


def pack_repo(repo: Path, output: Path) -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(["repomix", "--output", str(output)], cwd=repo, check=False)
    return result.returncode
