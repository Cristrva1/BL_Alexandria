from __future__ import annotations

from pathlib import Path


README_NAMES = ("README.md", "README.MD", "readme.md", "README.txt", "README-first.md")


def find_readme(repo: Path) -> Path | None:
    for name in README_NAMES:
        candidate = repo / name
        if candidate.exists():
            return candidate
    return None


def short_summary(readme: Path | None, max_chars: int = 260) -> str:
    if not readme or not readme.exists():
        return ""
    try:
        text = readme.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    for raw in text.splitlines():
        line = raw.strip().lstrip("#").strip()
        if line and not line.startswith(("!", "[", "<")):
            return (line[: max_chars - 1] + "...") if len(line) > max_chars else line
    return ""
