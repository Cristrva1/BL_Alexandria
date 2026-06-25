from pathlib import Path

from repo_intelligence.analysis.recommend import _effective_max_repos, _infer_required_capabilities, recommend
from repo_intelligence.core.io import write_json


def test_recommend_infers_claude_code_and_filters_generic_code(tmp_path: Path) -> None:
    ai_index = tmp_path / "ai_index"
    ai_index.mkdir()
    write_json(
        ai_index / "REPOS.scan.json",
        {
            "repos": [
                _repo("superpowers", role="skill", tags=["skills", "agents"]),
                _repo("agent-toolkit", role="skill", tags=["skills", "agents"]),
                _repo("claude-plugins-official", role="directory", tags=["skills"]),
                _repo("awesome-claude-code", role="directory", tags=["skills", "agents"]),
                _repo("skillspector", role="skill", tags=["skills"]),
                _repo("context-engineering", role="directory", tags=["skills", "context"]),
                _repo("prompt-master", role="skill", tags=["skills"]),
                _repo("awesome-bigdata", role="directory", tags=["code"]),
                _repo("data-science-ipython-notebooks", role="directory", tags=["code"]),
            ]
        },
    )
    write_json(
        ai_index / "REPOS.detail.json",
        {
            "repos": [
                {"id": "superpowers", "desc": "metodologia completa para agentes y Claude Code"},
                {"id": "agent-toolkit", "desc": "skills diarias para Claude Code"},
                {"id": "claude-plugins-official", "desc": "plugins oficiales para Claude Code"},
                {"id": "awesome-claude-code", "desc": "catalogo Claude Code"},
                {"id": "skillspector", "desc": "auditoria de skills"},
                {"id": "context-engineering", "desc": "ingenieria de contexto"},
                {"id": "prompt-master", "desc": "mejora prompts"},
                {"id": "awesome-bigdata", "desc": "catalogo de big data y codigo"},
                {"id": "data-science-ipython-notebooks", "desc": "notebooks de data science y codigo"},
            ]
        },
    )
    write_json(ai_index / "WINNERS.json", {})

    result = recommend(
        tmp_path,
        "Quiero optimizar y ultralizar Claude Code para uso diario",
        max_repos=7,
        build_tool="auto",
    )

    ids = [repo["id"] for repo in result["recommended_repos"]]
    assert result["requested_tool"] == "auto"
    assert result["build_tool"] == "claude-code"
    assert ids == [
        "superpowers",
        "agent-toolkit",
        "claude-plugins-official",
        "awesome-claude-code",
        "skillspector",
        "context-engineering",
        "prompt-master",
    ]
    superguide = tmp_path / result["superguide_file"]
    latest = tmp_path / result["latest_superguide_file"]
    assert superguide.exists()
    assert latest.exists()
    text = superguide.read_text(encoding="utf-8")
    assert "# Super Guia Practica Del Proyecto" in text
    assert "Quiero optimizar y ultralizar Claude Code para uso diario" in text
    assert "Prompt Para El Agente Instalador" in text


def test_recommend_accepts_claude_alias_from_tool_hint(tmp_path: Path) -> None:
    ai_index = tmp_path / "ai_index"
    ai_index.mkdir()
    write_json(ai_index / "REPOS.scan.json", {"repos": [_repo("superpowers", role="skill", tags=["skills", "agents"])]})
    write_json(ai_index / "REPOS.detail.json", {"repos": [{"id": "superpowers", "desc": "metodologia para agentes"}]})
    write_json(ai_index / "WINNERS.json", {})

    result = recommend(tmp_path, "Optimizar mi flujo diario", max_repos=1, build_tool="claude")

    assert result["build_tool"] == "claude-code"


def test_infer_required_capabilities_detects_product_needs() -> None:
    caps = _infer_required_capabilities(
        """
        Bot de whatsapp para leads con seguimiento desde CRM,
        documentos para RAG y dashboard web con metricas y analitica.
        """
    )
    assert caps["whatsapp"] > 0
    assert caps["automation"] > 0
    assert caps["docs"] > 0
    assert caps["dataviz"] > 0
    assert caps["ui"] > 0


def test_effective_max_repos_scales_for_complex_projects() -> None:
    caps = _infer_required_capabilities(
        "whatsapp crm dashboard web analitica mcp agentes docs rag"
    )
    assert _effective_max_repos(5, caps) >= 6


def test_superguide_uses_public_folder_names_not_absolute_paths(tmp_path: Path) -> None:
    ai_index = tmp_path / "ai_index"
    ai_index.mkdir()
    write_json(
        ai_index / "REPOS.scan.json",
        {
            "repos": [
                {
                    **_repo("superpowers", role="skill", tags=["skills", "agents"]),
                    "local_path": r"C:\\Users\\someone\\Repos\\superpowers",
                }
            ]
        },
    )
    write_json(ai_index / "REPOS.detail.json", {"repos": [{"id": "superpowers", "desc": "metodologia para agentes"}]})
    write_json(ai_index / "WINNERS.json", {})

    result = recommend(tmp_path, "Optimizar Claude Code", max_repos=1, build_tool="auto")
    text = (tmp_path / result["superguide_file"]).read_text(encoding="utf-8")

    assert "C:\\Users\\" not in text
    assert "superpowers" in text


def _repo(repo_id: str, role: str, tags: list[str]) -> dict[str, object]:
    return {
        "id": repo_id,
        "name": repo_id,
        "cat": 2,
        "role": role,
        "exec": "cloud",
        "setup": "easy",
        "tags": tags,
        "one": "",
        "mcp": False,
    }
