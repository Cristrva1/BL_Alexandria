from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from repo_intelligence.analysis.recommend import recommend
from repo_intelligence.core.io import read_yaml, write_json, write_yaml
from repo_intelligence.core.paths import ProjectPaths
from repo_intelligence.git.discover import discover_repos
from repo_intelligence.git.snapshots import write_snapshot
from repo_intelligence.git.sync import safe_pull
from repo_intelligence.guides.render import render_all
from repo_intelligence.indexes.build_scan import build_scan_index

app = typer.Typer(help="Local intelligence for the BL_Alexandria repository library.")
guide_app = typer.Typer(help="Human guide commands.")
context_app = typer.Typer(help="Context pack commands.")
report_app = typer.Typer(help="Report commands.")
app.add_typer(guide_app, name="guide")
app.add_typer(context_app, name="context")
app.add_typer(report_app, name="report")
console = Console()


@app.command()
def doctor() -> None:
    """Check paths and external tools."""
    paths = ProjectPaths.load()
    table = Table(title="Repo Intelligence Doctor")
    table.add_column("Check")
    table.add_column("Status")
    table.add_column("Detail")

    table.add_row("project_root", "OK" if paths.project_root.exists() else "MISSING", str(paths.project_root))
    table.add_row("repo_library", "OK" if paths.repo_library.exists() else "MISSING", str(paths.repo_library))
    for tool in ["git", "gh", "node", "npm", "pnpm", "uv", "docker", "repomix", "gitnexus", "markitdown"]:
        found = shutil.which(tool)
        table.add_row(tool, "OK" if found else "MISSING", found or "")
    console.print(table)


@app.command()
def discover(
    base: Annotated[Path | None, typer.Option(help="Override repo library path.")] = None,
) -> None:
    """Discover cloned repositories and rebuild the compact scan index."""
    paths = ProjectPaths.load()
    repo_base = base or paths.repo_library
    records = discover_repos(repo_base)
    write_yaml(paths.registry_file, {"generated_at": _now(), "base": str(repo_base), "repos": [r.model_dump() for r in records]})
    build_scan_index(paths.project_root, paths.scan_index, records)
    console.print(f"Discovered {len(records)} repos")
    console.print(f"Wrote {paths.registry_file}")
    console.print(f"Wrote {paths.scan_index}")


@app.command()
def snapshot() -> None:
    """Write a Git snapshot for every discovered repository."""
    paths = ProjectPaths.load()
    records = discover_repos(paths.repo_library)
    output = write_snapshot(paths.snapshots_dir, records)
    console.print(f"Wrote {output}")


@app.command()
def pull(safe: Annotated[bool, typer.Option("--safe", help="Skip dirty repos and use fast-forward only.")] = True) -> None:
    """Pull local repositories safely."""
    if not safe:
        raise typer.BadParameter("Only safe pulls are supported in V1.")
    paths = ProjectPaths.load()
    records = discover_repos(paths.repo_library)
    table = Table(title="Safe pull")
    table.add_column("Repo")
    table.add_column("Result")
    table.add_column("Message")
    for record in records:
        result, message = safe_pull(Path(record.path))
        table.add_row(record.name, result, _first_line(message))
    console.print(table)


@app.command()
def scan(changed_only: Annotated[bool, typer.Option("--changed-only")] = False) -> None:
    """Rebuild the compact AI scan index."""
    paths = ProjectPaths.load()
    registry = read_yaml(paths.registry_file, {"repos": []})
    if not registry.get("repos"):
        records = discover_repos(paths.repo_library)
    else:
        from repo_intelligence.core.models import RepoRecord

        records = [RepoRecord(**item) for item in registry["repos"]]
    output = build_scan_index(paths.project_root, paths.scan_index, records)
    suffix = " (changed-only flag accepted; V1 rebuilds compact scan)" if changed_only else ""
    console.print(f"Wrote {output}{suffix}")


@app.command()
def score() -> None:
    """Create an initial score report placeholder from deterministic rules."""
    paths = ProjectPaths.load()
    output = paths.project_root / "data" / "reports" / "score.json"
    write_json(output, {"generated_at": _now(), "status": "v1_placeholder", "rule_file": "config/scoring_rules.yaml"})
    console.print(f"Wrote {output}")


@app.command()
def conflicts() -> None:
    """Write initial known conflicts."""
    paths = ProjectPaths.load()
    output = paths.project_root / "ai_index" / "CONFLICTS.json"
    write_json(
        output,
        {
            "generated_at": _now(),
            "conflicts": [
                {
                    "repo_a": "n8n",
                    "repo_b": "activepieces",
                    "type": "functional_overlap",
                    "severity": "medium",
                    "reason": "Ambos son plataformas visuales de automatizacion.",
                    "recommendation": "Elegir n8n como estandar y dejar Activepieces como alternativa.",
                }
            ],
        },
    )
    console.print(f"Wrote {output}")


@app.command()
def decide(project_type: Annotated[str, typer.Option("--project-type")] = "repo_library_management") -> None:
    """Write a compact decision file for a project type."""
    paths = ProjectPaths.load()
    output = paths.project_root / "data" / "decisions" / f"{project_type}.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "# Decision\n\n"
        f"Project type: `{project_type}`\n\n"
        "Winner: `scripts_propios`\n\n"
        "Support tools: `repomix`, `gitnexus`, `markitdown`, `crawl4ai`.\n\n"
        "Avoid now: `graphrag`, `crewai`, `dify`, `flowise`.\n",
        encoding="utf-8",
    )
    console.print(f"Wrote {output}")


@app.command("recommend")
def recommend_project(
    project: Annotated[str, typer.Option("--project", "-p", help="Describe the project you want to build.")],
    tool: Annotated[str, typer.Option("--tool", help="Tool used to build it: codex, claude-code, antigravity, grok-build, open-code.")] = "codex",
    max_repos: Annotated[int, typer.Option("--max-repos", help="Maximum repositories to recommend.")] = 5,
) -> None:
    """Recommend repositories and install modes for a concrete project."""
    paths = ProjectPaths.load()
    result = recommend(paths.project_root, project, max_repos=max_repos, build_tool=tool)
    table = Table(title="Recommended Repositories")
    table.add_column("Repo")
    table.add_column("Score")
    table.add_column("Install")
    table.add_column("Reason")
    for repo in result["recommended_repos"]:
        reason = repo.get("expert_reason") or ", ".join(repo.get("reasons", []))
        table.add_row(repo["id"], str(repo["score"]), repo["install_mode"], _first_line(reason, 110))
    console.print(table)
    console.print(f"Wrote {paths.project_root / result['superguide_file']}")
    console.print(f"Updated {paths.project_root / result['latest_superguide_file']}")


@guide_app.command("build")
def guide_build(changed_only: Annotated[bool, typer.Option("--changed-only")] = False) -> None:
    """Rebuild human guides, cards, comparisons, playbooks, and detail index."""
    paths = ProjectPaths.load()
    stats = render_all(paths.project_root)
    console.print(
        "Generated guides: "
        f"{stats['repos']} repos, {stats['categories']} categories, "
        f"{stats['cards']} cards, {stats['comparisons']} comparisons, "
        f"{stats['playbooks']} playbooks"
    )
    if changed_only:
        console.print("changed-only accepted; V1 regenerates deterministic guide outputs.")


@context_app.command("build")
def context_build(
    query: Annotated[str, typer.Option("--query")] = "",
    tool: Annotated[str, typer.Option("--tool")] = "codex",
    max_repos: Annotated[int, typer.Option("--max-repos")] = 3,
) -> None:
    """Create a portable AI context pack for a project/query."""
    paths = ProjectPaths.load()
    result = recommend(paths.project_root, query or "general repository intelligence project", max_repos=max_repos, build_tool=tool)
    console.print(f"Wrote {paths.project_root / result['superguide_file']}")
    console.print(f"Updated {paths.project_root / result['latest_superguide_file']}")
    console.print(f"Recommended {len(result['recommended_repos'])} repos")


@report_app.command("daily")
def report_daily() -> None:
    """Create a tiny daily report."""
    paths = ProjectPaths.load()
    output = paths.project_root / "data" / "reports" / "daily.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(f"# Daily report\n\nGenerated: {_now()}\n", encoding="utf-8")
    console.print(f"Wrote {output}")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _first_line(value: str, limit: int = 100) -> str:
    line = value.splitlines()[0] if value else ""
    return line[:limit]
