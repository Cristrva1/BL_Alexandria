"""Extract complete READMEs from all cloned repos into data/extracted/.

Unlike ensure_analyzed (which truncates at 8000 chars and only ran for 21 repos),
this script copies the FULL README content for every repo in the library.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from repo_intelligence.core.paths import ProjectPaths
from repo_intelligence.core.io import read_yaml
from repo_intelligence.extract.readme import find_readme


def normalize_id(name: str) -> str:
    return name.lower().replace(" ", "-").replace("_", "-")


def build_id_map(paths: ProjectPaths) -> dict[str, str]:
    """Map folder names to canonical IDs from the registry."""
    registry = read_yaml(paths.registry_file, {"repos": []})
    mapping = {}
    for rec in registry.get("repos", []):
        folder = Path(rec.get("path", "")).name
        rid = rec.get("id", normalize_id(folder))
        mapping[folder] = rid
    return mapping


def try_markitdown(source: Path, dest: Path) -> bool:
    """Try converting with markitdown. Returns True on success."""
    try:
        result = subprocess.run(
            ["markitdown", str(source)],
            capture_output=True, text=True, timeout=60, check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            dest.write_text(result.stdout, encoding="utf-8")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        pass
    return False


def main() -> int:
    paths = ProjectPaths.load()
    lib = paths.repo_library
    extracted_dir = paths.extracted_dir
    extracted_dir.mkdir(parents=True, exist_ok=True)

    if not lib.exists():
        print(f"ERROR: repo library not found at {lib}", file=sys.stderr)
        return 1

    id_map = build_id_map(paths)
    print(f"Loaded {len(id_map)} canonical IDs from registry")

    repos = sorted([p for p in lib.iterdir() if p.is_dir() and not p.name.startswith(".")])
    print(f"Found {len(repos)} repos in {lib}")

    manifest: list[dict] = []
    ok = 0
    no_readme = 0
    converted = 0
    copied = 0

    for repo_path in repos:
        rid = id_map.get(repo_path.name, normalize_id(repo_path.name))
        out_dir = extracted_dir / rid
        out_dir.mkdir(parents=True, exist_ok=True)

        readme = find_readme(repo_path)
        entry: dict = {
            "id": rid,
            "name": repo_path.name,
            "source_path": str(readme) if readme else None,
            "source_format": readme.suffix.lower() if readme else None,
            "chars": 0,
            "extracted_chars": 0,
            "truncated": False,
            "no_readme": False,
            "method": None,
        }

        if not readme:
            (out_dir / "NO_README.txt").write_text(
                f"No README found in {repo_path.name}\n", encoding="utf-8"
            )
            entry["no_readme"] = True
            no_readme += 1
            manifest.append(entry)
            print(f"  [NO README] {rid}")
            continue

        try:
            raw_text = readme.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            entry["no_readme"] = True
            no_readme += 1
            manifest.append(entry)
            print(f"  [READ ERROR] {rid}")
            continue

        entry["chars"] = len(raw_text)
        out_file = out_dir / "readme.md"

        # For .md files, copy directly (full content, no truncation)
        if readme.suffix.lower() in (".md", ".markdown", ".txt"):
            out_file.write_text(raw_text, encoding="utf-8")
            entry["method"] = "copy"
            copied += 1
        else:
            # For .rst, .html, etc. try markitdown; fallback to raw copy
            if try_markitdown(readme, out_file):
                entry["method"] = "markitdown"
                converted += 1
            else:
                out_file.write_text(raw_text, encoding="utf-8")
                entry["method"] = "copy_raw"
                copied += 1

        entry["extracted_chars"] = out_file.stat().st_size
        ok += 1
        manifest.append(entry)

        if ok % 20 == 0:
            print(f"  ... {ok} extracted")

    # Write manifest
    manifest_path = extracted_dir / "MANIFEST.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print()
    print(f"=== Summary ===")
    print(f"Total repos:     {len(repos)}")
    print(f"With README:     {ok}")
    print(f"No README:       {no_readme}")
    print(f"Copied (.md):    {copied}")
    print(f"Converted:       {converted}")
    print(f"Manifest:        {manifest_path}")

    # Stats on truncation
    truncated = [m for m in manifest if m["chars"] > 8000]
    print(f"Previously truncated (>8000 chars): {len(truncated)}")
    big = [m for m in manifest if m["chars"] > 50000]
    print(f"Very large (>50000 chars): {len(big)}")

    return 0 if ok + no_readme == len(repos) else 1


if __name__ == "__main__":
    sys.exit(main())
