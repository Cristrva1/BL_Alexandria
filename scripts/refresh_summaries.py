"""Rewrite compact `one` and detalle `desc` from READMEs when the current text is junk or cut off.

Does not touch choose_if / avoid_if / combines_with.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from repo_intelligence.core.paths import ProjectPaths
from repo_intelligence.extract.readme import (
    clip_sentence,
    find_readme,
    is_bad_summary,
    read_readme_text,
    summarize_readme,
)


def _readme_for(rid: str, paths: ProjectPaths, repo_path: Path | None) -> str:
    extracted = paths.extracted_dir / rid / "readme.md"
    if extracted.exists():
        try:
            return extracted.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            pass
    if repo_path:
        return read_readme_text(find_readme(repo_path))
    return ""


def recount(compact: dict) -> None:
    counts = Counter(r.get("cat") for r in compact.get("repos", []))
    for cat in compact.get("categories", []):
        cat["count"] = counts.get(cat["num"], 0)
    n = len(compact.get("repos", []))
    compact.setdefault("meta", {})["title"] = f"Índice IA — {n} repos curados de IA y Automatización"


def main() -> int:
    root = Path.cwd()
    paths = ProjectPaths.load(root)
    compact_path = root / "INDICE_IA.json"
    detalle_path = root / "INDICE_IA.detalle.json"
    compact = json.loads(compact_path.read_text(encoding="utf-8"))
    detalle = json.loads(detalle_path.read_text(encoding="utf-8"))
    det_repos = detalle.setdefault("repos", {})

    from repo_intelligence.core.io import read_yaml

    registry = read_yaml(paths.registry_file, {"repos": []})
    path_by_id = {r["id"]: Path(r["path"]) for r in registry.get("repos", []) if r.get("id")}

    one_n = desc_n = 0
    for repo in compact.get("repos", []):
        rid = repo["id"]
        text = _readme_for(rid, paths, path_by_id.get(rid))
        if not text:
            continue
        one = summarize_readme(text, max_chars=220)
        desc = summarize_readme(text, max_chars=400)
        if one and one != (repo.get("one") or ""):
            repo["one"] = one
            one_n += 1
        current_desc = (det_repos.get(rid) or {}).get("desc") or ""
        if desc and (is_bad_summary(current_desc) or not current_desc):
            entry = det_repos.setdefault(rid, {"name": repo.get("name", rid), "cat": repo.get("cat")})
            entry["desc"] = clip_sentence(desc, 400)
            desc_n += 1

    recount(compact)
    compact_path.write_text(json.dumps(compact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    detalle_path.write_text(json.dumps(detalle, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"updated one={one_n} desc={desc_n} compact={len(compact['repos'])} detalle={len(det_repos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
