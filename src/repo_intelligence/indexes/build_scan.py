from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from repo_intelligence.core.io import read_json, write_json
from repo_intelligence.core.models import RepoRecord, ScanRepo
from repo_intelligence.extract.readme import short_summary


def build_scan_index(project_root: Path, output: Path, records: list[RepoRecord]) -> Path:
    compact_index = read_json(project_root / "INDICE_IA.json", {})
    indexed = _index_library(compact_index.get("repos", []))

    scan_repos: list[dict[str, Any]] = []
    for record in records:
        key = _match_key(record, indexed)
        meta = indexed.get(key or "", {})
        one = meta.get("one") or short_summary(Path(record.readme) if record.readme else None)
        scan = ScanRepo(
            id=meta.get("id") or record.id,
            name=meta.get("name") or record.name,
            role=meta.get("role"),
            exec=meta.get("exec"),
            setup=meta.get("setup"),
            tags=meta.get("tags", []),
            one=one,
            install_mode=_install_mode(meta),
            decision=_decision(meta),
            alt=meta.get("alt", []),
            path=record.path,
        )
        scan_repos.append(scan.model_dump())

    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "registry/repos.yaml + INDICE_IA.json",
        "repos": scan_repos,
    }
    write_json(output, data)
    return output


def _index_library(repos: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for repo in repos:
        for value in {repo.get("id", ""), repo.get("name", "")}:
            if value:
                indexed[_norm(value)] = repo
    return indexed


def _match_key(record: RepoRecord, indexed: dict[str, dict[str, Any]]) -> str | None:
    for value in (record.id, record.name):
        key = _norm(value)
        if key in indexed:
            return key
    return None


def _norm(value: str) -> str:
    return value.lower().replace("_", "-").replace(".", "-")


def _install_mode(meta: dict[str, Any]) -> str:
    repo_id = meta.get("id", "")
    role = meta.get("role")
    if repo_id in {"repomix", "gitnexus"}:
        return "global"
    if repo_id in {"markitdown", "crawl4ai"}:
        return "local_project"
    if role in {"skill", "directory"}:
        return "reference_only"
    if meta.get("setup") == "heavy":
        return "deferred"
    return "reference_only"


def _decision(meta: dict[str, Any]) -> str:
    install_mode = _install_mode(meta)
    if install_mode in {"global", "local_project"}:
        return "use_now"
    if install_mode == "deferred":
        return "defer"
    return "reference"
