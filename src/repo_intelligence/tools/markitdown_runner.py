from __future__ import annotations

import subprocess
from pathlib import Path


def convert_to_markdown(input_path: Path, output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(["markitdown", str(input_path), "-o", str(output_path)], check=False, capture_output=True, text=True)
        if result.returncode != 0:
            # fallback: just copy the raw readme as markdown
            try:
                content = input_path.read_text(encoding="utf-8", errors="replace")
                output_path.write_text(content, encoding="utf-8")
                return 0
            except Exception:
                pass
        return result.returncode
    except Exception:
        # ultimate fallback
        try:
            content = input_path.read_text(encoding="utf-8", errors="replace")
            output_path.write_text(content, encoding="utf-8")
            return 0
        except Exception:
            return 1
