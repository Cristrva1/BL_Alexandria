from __future__ import annotations

import re
from pathlib import Path
from typing import Any


README_NAMES = (
    "README.md", "README.MD", "readme.md", "README.txt", "README-first.md",
    "README.rst", "readme.rst", "README.markdown", "README.html",
)


def find_readme(repo: Path) -> Path | None:
    try:
        for name in README_NAMES:
            candidate = repo / name
            if candidate.exists():
                return candidate
        if repo.is_dir():
            for f in repo.iterdir():
                if f.is_file() and f.name.lower().startswith("readme"):
                    return f
    except OSError:
        return None
    return None


_BOX_DRAWING = re.compile(r"[█░▓▒▄▀■□▪▫┌┐└┘├┤┬┴┼─│━┃═╔╗╚╝╠╣╦╩╬]")
_BADGE_OR_HTML = re.compile(
    r"img\.shields\.io|badge\.svg|alt\s*=|src\s*=|href\s*=|target\s*=|<img|<a |</a>|align\s*=",
    re.I,
)
_LANG_SWITCH = re.compile(
    r"\benglish\s*(\||/|·)\s*|language:\s*|简体|繁體|日本語|한국어|portugu",
    re.I,
)
_SKIP_PREFIXES = (
    "!",
    "[",
    "<",
    "|",
    "---",
    "***",
    "http://",
    "https://",
    "src=",
    "href=",
    "alt=",
    "target=",
    "spdx-",
    "copyright",
    "table of contents",
    "latest release",
    "need discussion",
    "check out my new",
    "join our",
    "join us",
    "documentation",
    ".. image::",
    ":target:",
)


def _strip_markup(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</(p|div|h[1-6]|li|tr)>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`]+", "", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.M)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    return text


def is_junk_line(line: str) -> bool:
    s = (line or "").strip()
    if not s:
        return True
    sl = s.lower()
    if sl.startswith(_SKIP_PREFIXES):
        return True
    if _BADGE_OR_HTML.search(s) or _BOX_DRAWING.search(s):
        return True
    if _LANG_SWITCH.search(s) and len(s) < 240:
        return True
    if s.count("|") >= 3:
        return True
    if re.fullmatch(r"[\W_#*~`·▶️]+", s):
        return True
    letters = sum(ch.isalpha() for ch in s)
    return letters < 12


def is_bad_summary(text: str) -> bool:
    t = (text or "").strip()
    if len(t) < 40:
        return True
    if is_junk_line(t):
        return True
    if t.endswith("...") or t.endswith("…"):
        return True
    if any(token in t.lower() for token in ("target=", "href=", "alt=", "img.shields", "spdx-", "<a ", "<img")):
        return True
    if t[-1].isalnum() and len(t) >= 180:
        return True
    if t.endswith((" y", " de", " the", " a", " for", " with", " and", " an", " to", ",", "**")):
        return True
    return False


def clip_sentence(text: str, max_chars: int) -> str:
    cleaned = re.sub(r"\s+", " ", (text or "").strip())
    cleaned = cleaned.strip(" -•")
    if not cleaned:
        return ""
    if len(cleaned) <= max_chars:
        if cleaned[-1] not in ".!?":
            cleaned += "."
        return cleaned
    window = cleaned[: max_chars + 1]
    ends = [window.rfind(ch) for ch in ".!?"]
    cut = max(ends)
    if cut >= int(max_chars * 0.45):
        return window[: cut + 1].strip()
    sp = window.rfind(" ")
    if sp > 40:
        return window[:sp].rstrip(" ,;:-") + "."
    return window[:max_chars].rstrip() + "."


def summarize_readme(readme_text: str, max_chars: int = 240) -> str:
    intro = extract_intro_and_desc(readme_text, max_desc=max_chars + 120)
    desc = intro.get("desc") or ""
    title = intro.get("title") or ""
    if desc and not is_junk_line(desc):
        return clip_sentence(desc, max_chars)
    if title and not is_junk_line(title) and len(title) > 20:
        return clip_sentence(title, max_chars)
    return clip_sentence(desc or title, max_chars)


def short_summary(readme: Path | None, max_chars: int = 260) -> str:
    text = read_readme_text(readme)
    return summarize_readme(text, max_chars=max_chars) if text else ""


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
    plain = _strip_markup(readme_text or "")
    lines = [ln.strip() for ln in plain.splitlines()]
    title = ""
    desc_lines: list[str] = []

    for line in lines[:120]:
        if is_junk_line(line):
            if desc_lines:
                break
            continue
        clean = re.sub(r"\s+", " ", line).strip()
        if not title and 8 < len(clean) < 160:
            title = clean
            continue
        if clean == title:
            continue
        if len(clean) < 20:
            continue
        desc_lines.append(clean)
        if len(" ".join(desc_lines)) >= max_desc:
            break
        if len(desc_lines) >= 3:
            break

    desc = clip_sentence(" ".join(desc_lines), max_desc) if desc_lines else ""
    if not desc and title:
        desc = clip_sentence(title, max_desc)
    return {
        "title": title[:120] if title else "",
        "desc": desc or "",
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
