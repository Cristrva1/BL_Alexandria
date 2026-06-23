from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from repo_intelligence.core.io import write_json
from repo_intelligence.core.models import RepoRecord


def write_snapshot(snapshots_dir: Path, records: list[RepoRecord]) -> Path:
    snapshots_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = snapshots_dir / f"snapshot_{now}.json"
    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repos": [record.model_dump() for record in records],
    }
    write_json(path, data)
    return path
