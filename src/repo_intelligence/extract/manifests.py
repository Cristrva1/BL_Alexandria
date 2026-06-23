from __future__ import annotations

from pathlib import Path


MANIFEST_NAMES = (
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "setup.py",
    "uv.lock",
    "pnpm-lock.yaml",
    "package-lock.json",
    "docker-compose.yml",
    "docker-compose.yaml",
    "Dockerfile",
)


def detect_manifests(repo: Path) -> list[Path]:
    found: list[Path] = []
    for name in MANIFEST_NAMES:
        candidate = repo / name
        if candidate.exists():
            found.append(candidate)
    return found
