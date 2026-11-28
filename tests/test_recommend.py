import shutil
from pathlib import Path

from repo_intelligence.analysis.recommend import _infer_required_capabilities, recommend
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


def test_complex_projects_respect_limit_and_alternatives(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    for name in ("INDICE_IA.json", "INDICE_IA.detalle.json"):
        shutil.copy(root / name, tmp_path / name)
    query = "whatsapp crm dashboard web analitica mcp agentes docs rag"
    for limit in (1, 2, 7):
        result = recommend(tmp_path, query, max_repos=limit)
        rows = result["recommended_repos"]
        assert 0 < len(rows) <= limit
        ids = {repo["id"] for repo in rows}
        assert all(not ids.intersection(repo["alt"]) for repo in rows)


def test_web_projects_start_with_the_pieces_the_first_version_needs(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    for name in ("INDICE_IA.json", "INDICE_IA.detalle.json"):
        shutil.copy(root / name, tmp_path / name)
    scenarios = [
        ("Quiero hacer una página web", "HTML + CSS", []),
        ("Quiero una landing page con Codex", "HTML + CSS", []),
        ("Quiero hacer un panel web con login", "Next.js + Tailwind CSS + shadcn/ui", ["tailwindcss", "ui"]),
        ("Quiero crear una web app con chat con IA", "Next.js + AI SDK", ["vercel-ai"]),
        ("Quiero hacer una página web sin chat con IA", "HTML + CSS", []),
        ("Quiero crear un sitio web corporativo con CMS y borradores", "Astro + Strapi 5", []),
        ("Quiero un panel web para consultar métricas", "Metabase", ["metabase", "superset"]),
        ("Quiero un panel web para editar registros", "ToolJet", ["tooljet", "appsmith"]),
        ("Quiero una aplicación web con IA que genere cotizaciones", "Next.js + AI SDK con salida estructurada", ["vercel-ai"]),
        ("Quiero una web con IA", "Next.js + AI SDK", ["vercel-ai"]),
    ]
    for query, stack, ids in scenarios:
        result = recommend(tmp_path, query, max_repos=7)
        assert result["web_project"]["stack"] == stack
        assert [repo["id"] for repo in result["recommended_repos"]] == ids
        guide = (tmp_path / result["latest_superguide_file"]).read_text(encoding="utf-8")
        assert stack in guide
        assert "Primera prueba" in guide
        assert "Qué combinar y qué elegir" in guide

    research = recommend(tmp_path, "Quiero extraer datos de una página web")
    assert "web_project" not in research


def test_recommend_excludes_retired_repos_from_an_older_scan(tmp_path: Path) -> None:
    archived = [
        _repo("old", role="app", tags=["whatsapp"]),
        {**_repo("old-alias", role="app", tags=["whatsapp"]), "github_id": 123},
        {**_repo("renamed", role="app", tags=["whatsapp"]), "gh": "Example/Old"},
    ]
    active = _repo("active", role="app", tags=["whatsapp"])
    write_json(tmp_path / "ai_index" / "REPOS.scan.json", {"repos": [*archived, active]})
    write_json(tmp_path / "data" / "retired.json", {"repos": [{"id": "old", "github_id": 123, "gh": "example/old"}]})

    result = recommend(tmp_path, "Quiero un bot de WhatsApp", max_repos=7)

    assert [repo["id"] for repo in result["recommended_repos"]] == ["active"]


def test_auto_without_tool_phrase_does_not_assume_codex(tmp_path: Path) -> None:
    ai_index = tmp_path / "ai_index"
    ai_index.mkdir()
    write_json(
        ai_index / "REPOS.scan.json",
        {
            "repos": [
                _repo("evolution-api", role="app", tags=["whatsapp", "automation"]),
                _repo("n8n", role="platform", tags=["automation"]),
                _repo("awesome-agent-skills", role="directory", tags=["skills"]),
            ]
        },
    )
    write_json(
        ai_index / "REPOS.detail.json",
        {
            "repos": [
                {"id": "evolution-api", "desc": "api de whatsapp"},
                {"id": "n8n", "desc": "automatizacion de flujos"},
                {"id": "awesome-agent-skills", "desc": "catalogo de skills"},
            ]
        },
    )
    write_json(ai_index / "WINNERS.json", {})

    result = recommend(
        tmp_path,
        "bot de WhatsApp con IA para responder clientes y guardar leads",
        max_repos=5,
        build_tool="auto",
    )
    ids = [repo["id"] for repo in result["recommended_repos"]]
    assert result["requested_tool"] == "auto"
    assert result["build_tool"] == "auto"
    assert "awesome-agent-skills" not in ids
    assert "evolution-api" in ids


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
