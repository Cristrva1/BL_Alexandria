"""Incorporate newly discovered repos into INDICE without running repomix.

Copies README -> data/extracted, drafts compact+detalle, merges into indices.
"""
from __future__ import annotations

import sys
from pathlib import Path

from repo_intelligence.analysis.curation import (
    _load_existing_indices,
    build_draft_entries,
    build_profile,
    merge_into_indices,
    resolve_enrich_targets,
    save_draft,
)
from repo_intelligence.core.io import read_json, read_yaml
from repo_intelligence.core.paths import ProjectPaths
from repo_intelligence.extract.readme import find_readme


def main() -> int:
    root = Path.cwd()
    paths = ProjectPaths.load(root)
    registry = read_yaml(paths.registry_file, {"repos": []})
    records = {r["id"]: r for r in registry.get("repos", []) if r.get("id")}
    compact = read_json(root / "INDICE_IA.json", {})
    curated = {r["id"] for r in compact.get("repos", [])}
    targets = resolve_enrich_targets(list(records.keys()), curated, only_new=True, ids=None)
    print(f"new targets: {len(targets)}")
    for rid in targets:
        rec = dict(records[rid])
        repo_path = Path(rec["path"])
        rm = find_readme(repo_path)
        dest = paths.extracted_dir / rid / "readme.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if rm and rm.exists():
            dest.write_text(rm.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
            rec["readme"] = str(rm)
            print(f"  extracted {rid}")
        else:
            dest.write_text("", encoding="utf-8")
            print(f"  NO_README {rid}")
        compact_idx, det_idx = _load_existing_indices(root)
        profile = build_profile(rec, paths)
        c_entry, d_entry = build_draft_entries(profile, compact_idx, det_idx.get("repos", {}))
        save_draft(root, rid, c_entry, d_entry, profile)
        merge_into_indices(root, rid, c_entry, d_entry)
        print(f"  merged {rid} cat={c_entry.get('cat')} role={c_entry.get('role')}")
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
