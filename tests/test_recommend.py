from pathlib import Path

from repo_intelligence.analysis.recommend import recommend
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
        build_tool="codex",
    )

    ids = [repo["id"] for repo in result["recommended_repos"]]
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
