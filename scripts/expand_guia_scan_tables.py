"""Expande las columnas 'Qué es' y 'Elige si…' de las tablas de escaneo en guias/*.md.

Usa el texto de las fichas editoriales (más rico) y lo comprime a una línea de tabla.
Luego hay que correr `python tools_check/mirror_to_guia.py` para reconstruir Guia.md.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from repo_intelligence.extract.readme import clip_sentence

ROOT = Path(__file__).resolve().parents[1]
GUIDES = [ROOT / "guias" / f"guia{i}.md" for i in range(1, 6)]


def _norm(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load_fichas() -> dict[str, dict[str, str]]:
    fichas: dict[str, dict[str, str]] = {}
    blob = "\n".join(p.read_text(encoding="utf-8") for p in GUIDES)
    parts = re.split(r"(?=^### )", blob, flags=re.M)
    for part in parts:
        heading = re.match(r"^###\s+\S+\s+(.+)\n", part)
        if not heading or "**Qué es:**" not in part:
            continue
        name = heading.group(1).strip()
        que = re.search(r"\*\*Qué es:\*\*\s*(.+)", part)
        elige = re.search(
            r"\*\*Elige si:\*\*\s*(.+?)(?:\s+[—-]\s+\*\*Evita si:|\n)",
            part,
        )
        payload = {
            "que": que.group(1).strip() if que else "",
            "elige": elige.group(1).strip() if elige else "",
        }
        fichas[_norm(name)] = payload
        fichas[name.lower()] = payload
    return fichas


def one_line(text: str, max_chars: int) -> str:
    t = (text or "").replace("|", " / ").replace("\n", " ")
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = t.replace("**", "")
    return clip_sentence(t, max_chars)


def expand_que(ficha_que: str, current: str) -> str:
    source = ficha_que or current
    if not source:
        return current
    sentences = re.split(r"(?<=[.!?])\s+", source)
    chunk = sentences[0] if sentences else source
    if len(chunk) < 55 and len(sentences) > 1:
        chunk = sentences[0] + " " + sentences[1]
    t = one_line(chunk, 220)
    if t and t[0].islower():
        t = t[0].upper() + t[1:]
    words = t.rstrip(".!?").split()
    if words and len(words[-1]) <= 3 and len(words) > 4:
        t = " ".join(words[:-1]).rstrip(" ,;:") + "."
    if t.count('"') % 2 == 1 or t.count("«") != t.count("»"):
        comma = t.rfind(",")
        if comma > 60:
            t = t[:comma].rstrip() + "."
    return t


def expand_elige(ficha_elige: str, current: str) -> str:
    raw = (ficha_elige or "").strip()
    if (not raw) or raw in {"—", "-", "–"} or raw.startswith("—") or "Evita si" in raw:
        if current and "Evita si" not in current and current not in {"—", "-", "🟢", "🟡", "🔴"}:
            return current
        return "Es el mismo proyecto que n8n; usa esa ficha." if "n8n" in current.lower() or not raw else current
    t = raw
    if t[0].islower():
        t = t[0].upper() + t[1:]
    return one_line(t, 120)


def rewrite_file(path: Path, fichas: dict[str, dict[str, str]]) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    in_table = False
    cols: list[str] = []
    changed = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("| Repo |") and "Qué es" in line:
            in_table = True
            cols = [c.strip() for c in line.strip("|").split("|")]
            out.append(line)
            i += 1
            continue
        if in_table:
            if not line.startswith("|"):
                in_table = False
                out.append(line)
                i += 1
                continue
            if line.startswith("|---"):
                out.append(line)
                i += 1
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) != len(cols):
                out.append(line)
                i += 1
                continue
            repo_cell = cells[0]
            m = re.search(r"\[([^\]]+)\]", repo_cell)
            name = m.group(1) if m else ""
            key = _norm(name)
            ficha = fichas.get(key) or fichas.get(name.lower()) or {}
            try:
                que_i = next(idx for idx, h in enumerate(cols) if h.startswith("Qué es"))
                elige_i = next(idx for idx, h in enumerate(cols) if h.startswith("Elige"))
            except StopIteration:
                out.append(line)
                i += 1
                continue
            new_que = expand_que(ficha.get("que", ""), cells[que_i])
            new_elige = expand_elige(ficha.get("elige", ""), cells[elige_i])
            if new_que:
                cells[que_i] = new_que
            if new_elige:
                cells[elige_i] = new_elige
            new_line = "| " + " | ".join(cells) + " |"
            if new_line != line:
                changed += 1
            out.append(new_line)
            i += 1
            continue
        out.append(line)
        i += 1
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    fichas = load_fichas()
    print(f"fichas={len(fichas)}")
    total = 0
    for path in GUIDES:
        n = rewrite_file(path, fichas)
        print(f"{path.name}: {n} filas")
        total += n
    print(f"total={total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
