from __future__ import annotations

import re
from pathlib import Path
from typing import Any


README_NAMES = (
    "README.md", "README.MD", "readme.md", "README.txt", "README-first.md",
    "README.rst", "readme.rst", "README.markdown", "README.html",
)


def find_readme(repo: Path) -> Path | None:
    for name in README_NAMES:
        candidate = repo / name
        if candidate.exists():
            return candidate
    # Case-insensitive fallback for any file starting with "readme"
    if repo.is_dir():
        for f in repo.iterdir():
            if f.is_file() and f.name.lower().startswith("readme"):
                return f
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


def read_readme_text(readme: Path | None, max_chars: int = 50000) -> str:
    if not readme or not readme.exists():
        return ""
    try:
        text = readme.read_text(encoding="utf-8", errors="ignore")
        return text[:max_chars]
    except OSError:
        return ""


def extract_intro_and_desc(readme_text: str, max_desc: int = 420) -> dict[str, str]:
    """Return first meaningful title + a solid paragraph description."""
    lines = [l.strip() for l in readme_text.splitlines()]
    title = ""
    desc_lines: list[str] = []
    in_desc = False

    for i, line in enumerate(lines[:80]):  # look near top
        if not title and line.startswith("#") and len(line) > 2:
            title = line.lstrip("#").strip()
            continue
        if not title and i < 3 and len(line) > 10 and not line.startswith(("[", "!", "|", "- ", "* ")):
            title = line.strip()
            continue

        clean = line.lstrip("#*>- ").strip()
        if not clean:
            if in_desc and desc_lines:
                break
            continue
        if clean.startswith(("http", "!", "[", "<", "```", "|")):
            continue
        if len(clean) > 15:
            if not in_desc:
                in_desc = True
            desc_lines.append(clean)
            if len(" ".join(desc_lines)) > max_desc:
                break
    desc = " ".join(desc_lines)[:max_desc]
    if desc and not desc.endswith("."):
        desc += "."
    return {
        "title": title[:120] if title else "",
        "desc": desc or ""
    }


def extract_features(readme_text: str, max_items: int = 6) -> list[str]:
    features: list[str] = []
    lines = readme_text.splitlines()
    in_features = False
    for line in lines:
        l = line.strip()
        if re.match(r"^#{1,3}\s*(features?|caracter[ií]sticas|what|por qu[eé]|ventajas)", l, re.I):
            in_features = True
            continue
        if in_features:
            if l.startswith(("- ", "* ", "+ ")):
                item = l[2:].strip()
                if len(item) > 8 and len(item) < 120:
                    features.append(item)
            elif l.startswith("#") or (l and not l.startswith(("-", "*", "+")) and len(features) > 0):
                break
        if len(features) >= max_items:
            break
    return features[:max_items]


def guess_tech_stack(readme_text: str, manifests: list[str]) -> list[str]:
    stack: list[str] = []
    text = (readme_text + " " + " ".join(manifests)).lower()

    lang_map = {
        "python": ["python", "pyproject", "requirements", ".py"],
        "typescript": ["typescript", "ts", "next", "nest"],
        "javascript": ["javascript", "node", "npm", "package.json"],
        "react": ["react", "next.js", "vite"],
        "docker": ["docker", "docker-compose"],
        "postgres": ["postgres", "postgresql", "pg"],
        "fastapi": ["fastapi"],
        "langchain": ["langchain"],
        "whisper": ["whisper"],
        "comfy": ["comfy"],
    }
    for tech, kws in lang_map.items():
        if any(kw in text for kw in kws):
            stack.append(tech)

    # from manifests direct
    if any("pyproject" in m or "requirements" in m for m in manifests):
        if "python" not in stack:
            stack.append("python")
    if any("package.json" in m for m in manifests):
        if "javascript" not in stack and "typescript" not in stack:
            stack.append("javascript")
    if any("docker" in m.lower() for m in manifests):
        if "docker" not in stack:
            stack.append("docker")

    return list(dict.fromkeys(stack))  # dedup preserve order


def extract_install_hints(readme_text: str) -> list[str]:
    hints: list[str] = []
    for line in readme_text.splitlines():
        l = line.strip()
        if re.search(r"(pip install|npm i |pnpm add |uv (add|pip)|docker (run|compose)|git clone)", l, re.I):
            hints.append(l[:140])
        if len(hints) >= 3:
            break
    return hints
