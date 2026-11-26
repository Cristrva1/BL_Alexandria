from __future__ import annotations

import hashlib
import json
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import yaml
from filelock import FileLock


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_yaml(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return yaml.safe_load(path.read_text(encoding="utf-8")) or default


def write_yaml(path: Path, data: Any) -> None:
    ensure_parent(path)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


@contextmanager
def catalog_update(root: Path):
    """Serialize catalog writers and finish any previously prepared batch."""
    root = root.resolve()
    key = hashlib.sha256(os.path.normcase(str(root)).encode()).hexdigest()
    lock = FileLock(Path(tempfile.gettempdir()) / f"alexandria-{key}.lock", is_singleton=True)
    with lock:
        pending = root / "data" / ".alta-pendiente"
        if pending.exists():
            _finish_batch(root, pending)
        yield


def _finish_batch(root: Path, pending: Path) -> None:
    # A missing staged file has already been replaced. Retry the remaining files.
    manifest = pending / "archivos.json"
    if manifest.exists():
        for i, name in enumerate(json.loads(manifest.read_text(encoding="utf8"))):
            target = (root / name).resolve()
            target.relative_to(root)
            staged = pending / str(i)
            if staged.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                staged.replace(target)
        manifest.unlink()
    pending.rmdir()


def write_catalog_batch(root: Path, documents: dict[Path, dict]) -> None:
    """Stage a validated batch together on the same filesystem before replacing files."""
    root = root.resolve()
    directory = root / "data"
    directory.mkdir(exist_ok=True)
    pending = directory / ".alta-pendiente"
    with tempfile.TemporaryDirectory(prefix=".alta-", dir=directory) as temporary:
        stage = Path(temporary)
        names = []
        for i, (path, document) in enumerate(documents.items()):
            target = path.resolve()
            names.append(target.relative_to(root).as_posix())
            if target.exists() and not target.is_file():
                raise ValueError(f"El destino del lote debe ser un archivo: {target}")
            indent = 2 if names[-1].startswith("reports/") else 1
            (stage / str(i)).write_text(json.dumps(document, ensure_ascii=False, indent=indent) + "\n", encoding="utf8")
        (stage / "archivos.json").write_text(json.dumps(names), encoding="utf8")
        stage.rename(pending)
    _finish_batch(root, pending)
