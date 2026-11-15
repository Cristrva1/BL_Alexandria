"""Pruebas del índice curado y de las guías generadas a partir de él."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import pytest

from repo_intelligence.analysis.recommend import recommend
from repo_intelligence.core.catalog import load_catalog, slug
from repo_intelligence.guides.render import _looks_like_command, _short_install, render_all

ROOT = Path(__file__).resolve().parents[1]
ROLES = {"platform", "runtime", "library", "skill", "directory", "app"}


@pytest.fixture(scope="module")
def catalog():
    return load_catalog(ROOT)


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    """Genera las guías en una copia temporal para no tocar el repo."""
    root = tmp_path_factory.mktemp("hub")
    for name in ("INDICE_IA.json", "INDICE_IA.detalle.json", "README.md", "AGENTS.md"):
        shutil.copy(ROOT / name, root / name)
    stats = render_all(root)
    return root, stats


def test_every_repo_has_core_fields(catalog):
    for repo in catalog.repos:
        if repo.get("alias_of") or int(repo.get("cat") or 0) == 0:
            continue
        assert repo.get("name"), repo["id"]
        assert repo.get("role") in ROLES, repo["id"]
        assert 40 <= len(repo.get("one") or "") <= 200, repo["id"]
        assert repo.get("desc"), repo["id"]


def test_ids_are_unique_and_references_resolve(catalog):
    ids = [r["id"] for r in catalog.repos]
    assert len(ids) == len(set(ids))
    for repo in catalog.repos:
        for ref in list(repo.get("alternatives", [])) + list(repo.get("combines_with") or []):
            assert catalog.get(ref), f"{repo['id']} apunta a {ref}, que no existe"


def test_alternatives_are_symmetric(catalog):
    for repo in catalog.repos:
        for alt in repo.get("alternatives", []):
            other = catalog.get(alt)
            assert repo["id"] in other.get("alternatives", []), f"{repo['id']} ↔ {alt}"


def test_every_category_has_a_pick(catalog):
    for c in catalog.public_categories():
        assert catalog.picks(int(c["num"])), c.get("title")


def test_guide_build_writes_navigable_pages(built):
    root, stats = built
    assert stats["categories"] == 13
    assert (root / "human" / "README.md").exists()
    assert (root / "Catalogo.md").exists()
    assert (root / "Guia.md").exists()
    assert (root / "docs" / "index.html").exists()
    assert len(list((root / "human" / "fichas").glob("*.md"))) >= stats["cards"] - 1


def test_comparisons_stay_focused(built):
    root, stats = built
    # Una comparativa por decisión (opción recomendada vs. rival), no una por pareja posible.
    assert 0 < stats["comparisons"] <= 100
    assert len(list((root / "human" / "comparativas").glob("*-vs-*.md"))) == stats["comparisons"]


def test_generated_markdown_has_no_broken_relative_links(built):
    root, _ = built
    broken = []
    pages = list((root / "human").rglob("*.md")) + [root / "Catalogo.md", root / "Guia.md"]
    for page in pages:
        for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", page.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (page.parent / target).resolve().exists():
                broken.append(f"{page.relative_to(root)} → {target}")
    assert not broken, broken[:10]


def test_ficha_file_names_match_slugs(built, catalog):
    root, _ = built
    for repo in catalog.repos[:50]:
        if not repo.get("alias_of"):
            assert (root / "human" / "fichas" / f"{slug(repo['id'])}.md").exists()


def test_short_install_prefers_real_commands():
    assert _short_install("Usa `docker compose up -d` tras clonar") == "`docker compose up -d`"
    text = "Copia las carpetas a `.claude/skills/` o instálalas como plugin."
    assert _short_install(text).startswith("Copia las carpetas")
    assert _looks_like_command("npx skills add foo/bar")
    assert not _looks_like_command("00-course-setup")


def test_recommend_works_from_curated_index_without_local_scan(tmp_path):
    for name in ("INDICE_IA.json", "INDICE_IA.detalle.json"):
        shutil.copy(ROOT / name, tmp_path / name)
    result = recommend(tmp_path, "bot de WhatsApp con IA para responder clientes y guardar leads", max_repos=5)
    ids = [item["id"] for item in result["recommended_repos"]]
    assert ids, "sin escaneo local también debe recomendar desde el índice curado"
    assert "evolution-api" in ids or "whatsapp-web-js" in ids
