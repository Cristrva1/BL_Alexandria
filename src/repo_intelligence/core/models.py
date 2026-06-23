from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field


class RepoRecord(BaseModel):
    id: str
    name: str
    path: str
    is_git: bool = False
    head: str | None = None
    branch: str | None = None
    dirty: bool = False
    remotes: list[str] = Field(default_factory=list)
    readme: str | None = None
    manifests: list[str] = Field(default_factory=list)
    install_mode: str = "reference_only"

    @property
    def local_path(self) -> Path:
        return Path(self.path)


class ScanRepo(BaseModel):
    id: str
    name: str
    role: str | None = None
    exec: str | None = None
    setup: str | None = None
    tags: list[str] = Field(default_factory=list)
    one: str = ""
    install_mode: str = "reference_only"
    decision: str = "reference"
    alt: list[str] = Field(default_factory=list)
    path: str
