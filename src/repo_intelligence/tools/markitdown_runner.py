from __future__ import annotations

import subprocess
from pathlib import Path


def convert_to_markdown(input_path: Path, output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(["markitdown", str(input_path), "-o", str(output_path)], check=False)
    return result.returncode
