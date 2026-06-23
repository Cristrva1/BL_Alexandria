from pathlib import Path

from repo_intelligence.guides.render import _update_rich_root_guide


def test_rich_root_guide_is_not_replaced_when_repos_are_known(tmp_path: Path) -> None:
    guide = tmp_path / "Guia.md"
    original = (
        "# 🌌 Catálogo de Repositorios de IA & Automatización\n\n"
        "Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, elegir y combinar** repos rápido.\n\n"
        "## 📂 Mapa de categorías\n\n"
        "### 🧬 evolution-api\n"
        "### n8n\n"
    )
    guide.write_text(original, encoding="utf-8")

    _update_rich_root_guide(
        tmp_path,
        "# Guia de la biblioteca\n\nversion simple\n",
        [{"id": "evolution-api", "name": "evolution-api"}, {"id": "n8n", "name": "n8n"}],
        {"evolution-api": {}, "n8n": {}},
        "2026-06-23T00:00:00+00:00",
    )

    text = guide.read_text(encoding="utf-8")
    assert "version simple" not in text
    assert "2 repositorios" in text
    assert "2 repos curados" in text
    assert "🧬 evolution-api" in text


def test_rich_root_guide_appends_only_new_repos(tmp_path: Path) -> None:
    guide = tmp_path / "Guia.md"
    guide.write_text("# 🌌 Catálogo de Repositorios de IA & Automatización\n\n### n8n\n", encoding="utf-8")

    _update_rich_root_guide(
        tmp_path,
        "# Guia de la biblioteca\n\nversion simple\n",
        [{"id": "n8n", "name": "n8n"}, {"id": "new-repo", "name": "New Repo", "cat": 99}],
        {"new-repo": {"desc": "Repo nuevo detectado."}},
        "2026-06-23T00:00:00+00:00",
    )

    text = guide.read_text(encoding="utf-8")
    assert "version simple" not in text
    assert "Repos detectados pendientes de curaduría" in text
    assert "new-repo" in text


def test_rich_root_guide_updates_total_count_without_rewriting_body(tmp_path: Path) -> None:
    guide = tmp_path / "Guia.md"
    guide.write_text(
        "# 🌌 Catálogo de Repositorios de IA & Automatización\n\n"
        "Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, elegir y combinar** repos rápido.\n\n"
        "## 📂 Mapa de categorías\n\n"
        "### n8n\n",
        encoding="utf-8",
    )

    _update_rich_root_guide(
        tmp_path,
        "# Guia de la biblioteca\n\nversion simple\n",
        [{"id": "n8n", "name": "n8n"}, {"id": "new-repo", "name": "New Repo", "cat": 99}],
        {"n8n": {}},
        "2026-06-23T00:00:00+00:00",
    )

    text = guide.read_text(encoding="utf-8")
    assert "Catálogo operativo de los **2 repositorios** locales del workspace" in text
    assert "1 repos curados" in text
    assert "version simple" not in text


def test_mentions_do_not_count_as_curated_entries(tmp_path: Path) -> None:
    guide = tmp_path / "Guia.md"
    guide.write_text(
        "# 🌌 Catálogo de Repositorios de IA & Automatización\n\n"
        "Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, elegir y combinar** repos rápido.\n\n"
        "## 📂 Mapa de categorías\n\n"
        "### ag2\n"
        "AG2 es heredero de AutoGen.\n",
        encoding="utf-8",
    )

    _update_rich_root_guide(
        tmp_path,
        "# Guia de la biblioteca\n\nversion simple\n",
        [{"id": "ag2", "name": "ag2"}, {"id": "autogen", "name": "autogen", "cat": 3}],
        {"ag2": {}},
        "2026-06-23T00:00:00+00:00",
    )

    text = guide.read_text(encoding="utf-8")
    assert "autogen" in text
    assert "Repos detectados pendientes de curaduría" in text


def test_internal_links_do_not_count_as_curated_entries(tmp_path: Path) -> None:
    guide = tmp_path / "Guia.md"
    guide.write_text(
        "# 🌌 Catálogo de Repositorios de IA & Automatización\n\n"
        "Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, elegir y combinar** repos rápido.\n\n"
        "## 📂 Mapa de categorías\n\n"
        "[repomix](#-repomix) aparece en una receta, pero no tiene ficha propia.\n",
        encoding="utf-8",
    )

    _update_rich_root_guide(
        tmp_path,
        "# Guia de la biblioteca\n\nversion simple\n",
        [{"id": "repomix", "name": "repomix", "cat": 7}],
        {},
        "2026-06-23T00:00:00+00:00",
    )

    text = guide.read_text(encoding="utf-8")
    assert "repomix" in text
    assert "Repos detectados pendientes de curaduría" in text
