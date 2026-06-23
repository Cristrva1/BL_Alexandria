from pathlib import Path

from repo_intelligence.guides.render import _update_rich_root_guide


def test_rich_root_guide_is_not_replaced_when_repos_are_known(tmp_path: Path) -> None:
    guide = tmp_path / "Guia.md"
    original = (
        "# 🌌 Catálogo de Repositorios de IA & Automatización\n\n"
        "### 🧬 evolution-api\n"
        "### n8n\n"
    )
    guide.write_text(original, encoding="utf-8")

    _update_rich_root_guide(
        tmp_path,
        "# Guia de la biblioteca\n\nversion simple\n",
        [{"id": "evolution-api", "name": "evolution-api"}, {"id": "n8n", "name": "n8n"}],
        {},
        "2026-06-23T00:00:00+00:00",
    )

    assert guide.read_text(encoding="utf-8") == original


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
    assert "Repos detectados después de la guía curada" in text
    assert "new-repo" in text
