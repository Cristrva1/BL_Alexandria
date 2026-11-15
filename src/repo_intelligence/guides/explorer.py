"""Publish the same library interface to docs/ and web/.

The canonical explorer and the educational site deliberately share their data,
assets, filters and reading guides. This prevents two conflicting libraries.
"""
from pathlib import Path
from repo_intelligence.core.catalog import Catalog


def render_explorer(project_root: Path, cat: Catalog) -> Path:
    from repo_intelligence.web.build import build_site

    root = Path(project_root)
    build_site(root, root / "docs")
    from repo_intelligence.core.handbook import render_handbook
    render_handbook(root)
    return root / "docs" / "index.html"
