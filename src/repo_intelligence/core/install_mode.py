from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

_DEFAULTS = {
    "global": ["repomix", "gitnexus"],
    "local_project": ["markitdown", "crawl4ai", "litellm"],
    "docker_local": [
        "n8n",
        "langfuse",
        "evolution-api",
        "chatwoot",
        "novu",
        "mautic",
        "listmonk",
        "posthog",
        "metabase",
    ],
}


def _project_root() -> Path:
    # core/install_mode.py -> core -> repo_intelligence -> src -> project root
    return Path(__file__).resolve().parents[3]


@lru_cache(maxsize=1)
def _mode_sets() -> dict[str, set[str]]:
    path = _project_root() / "config" / "repo_policy.yaml"
    raw: dict[str, Any] = {}
    if path.exists():
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    block = raw.get("repo_install_modes") or _DEFAULTS
    return {
        "global": set(block.get("global") or _DEFAULTS["global"]),
        "local_project": set(block.get("local_project") or _DEFAULTS["local_project"]),
        "docker_local": set(block.get("docker_local") or _DEFAULTS["docker_local"]),
    }


def install_mode(repo: dict[str, Any] | None) -> str:
    repo = repo or {}
    repo_id = repo.get("id") or ""
    role = repo.get("role")
    modes = _mode_sets()
    if repo_id in modes["global"]:
        return "global"
    if repo_id in modes["local_project"]:
        return "local_project"
    if repo_id in modes["docker_local"]:
        return "docker_local"
    if role in {"skill", "directory"}:
        return "reference_only"
    if repo.get("setup") == "heavy":
        return "deferred"
    return repo.get("install_mode") or "reference_only"


def decision(repo: dict[str, Any] | None) -> str:
    mode = install_mode(repo)
    if mode in {"global", "local_project", "docker_local"}:
        return "use_now"
    if mode == "deferred":
        return "defer"
    return "reference"
