from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ProjectPaths:
    project_root: Path
    repo_library: Path
    registry_file: Path
    scan_index: Path
    detail_index: Path
    winners_index: Path
    router_index: Path
    snapshots_dir: Path
    extracted_dir: Path
    packed_dir: Path

    @classmethod
    def load(cls, project_root: Path | None = None) -> "ProjectPaths":
        root = project_root or Path.cwd()
        config_file = root / "config" / "paths.yaml"
        raw: dict[str, Any] = {}
        if config_file.exists():
            raw = yaml.safe_load(config_file.read_text(encoding="utf-8")) or {}

        configured_root = Path(raw.get("project_root") or root).expanduser()
        if not configured_root.is_absolute():
            configured_root = (root / configured_root).resolve()
        repo_library = Path(raw.get("repo_library") or configured_root).expanduser()
        if not repo_library.is_absolute():
            repo_library = (configured_root / repo_library).resolve()
        return cls(
            project_root=configured_root,
            repo_library=repo_library,
            registry_file=_resolve(configured_root, raw.get("registry_file", "registry/repos.yaml")),
            scan_index=_resolve(configured_root, raw.get("scan_index", "ai_index/REPOS.scan.json")),
            detail_index=_resolve(configured_root, raw.get("detail_index", "ai_index/REPOS.detail.json")),
            winners_index=_resolve(configured_root, raw.get("winners_index", "ai_index/WINNERS.json")),
            router_index=_resolve(configured_root, raw.get("router_index", "ai_index/ROUTER.json")),
            snapshots_dir=_resolve(configured_root, raw.get("snapshots_dir", "data/snapshots")),
            extracted_dir=_resolve(configured_root, raw.get("extracted_dir", "data/extracted")),
            packed_dir=_resolve(configured_root, raw.get("packed_dir", "data/packed")),
        )


def _resolve(root: Path, value: str | Path) -> Path:
    path = Path(value).expanduser()
    return path if path.is_absolute() else root / path
