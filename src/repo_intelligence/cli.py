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
from repo_intelligence.menu.export import export_menu

# New integral curation pipeline (submodule)
import repo_intelligence.analysis.curation as curation_mod

app = typer.Typer(help="Local intelligence for the BL_Alexandria repository library.")
guide_app = typer.Typer(help="Human guide commands.")
context_app = typer.Typer(help="Context pack commands.")
report_app = typer.Typer(help="Report commands.")
menu_app = typer.Typer(help="Portable AI menu commands.")
app.add_typer(guide_app, name="guide")
app.add_typer(context_app, name="context")
app.add_typer(report_app, name="report")
app.add_typer(menu_app, name="menu")
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
    project: Annotated[str, typer.Option("--project", "-p", help="Describe the project you want to build.")] = "",
    project_file: Annotated[Path | None, typer.Option("--project-file", help="Markdown/text file with a long project brief.")] = None,
    tool: Annotated[str, typer.Option("--tool", help="Tool hint: auto, codex, claude-code, claude, antigravity, grok-build, open-code.")] = "auto",
    max_repos: Annotated[int, typer.Option("--max-repos", help="Maximum repositories to recommend.")] = 5,
) -> None:
    """Recommend repositories and install modes for a concrete project."""
    paths = ProjectPaths.load()
    project_text = _load_project_text(project, project_file)
    result = recommend(paths.project_root, project_text, max_repos=max_repos, build_tool=tool)
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


@menu_app.command("export")
def menu_export(
    output: Annotated[Path | None, typer.Option("--output", "-o", help="Output directory (default: menu_portable/ in project root).")] = None,
) -> None:
    """Export a portable, AI-optimized menu of all curated repos.

    Produces a self-contained folder (REPO_MENU.md + per-category detail files
    + JSON mirror) that you can copy into the root of a NEW project so an AI
    agent reads it and picks repos to install without visiting the web.
    """
    paths = ProjectPaths.load()
    out_dir = output or (paths.project_root / "menu_portable")
    stats = export_menu(paths.project_root, out_dir)
    console.print(
        f"Portable menu exported to {stats['output_dir']}: "
        f"{stats['repos']} repos, {stats['categories']} categories, "
        f"{stats['files']} files."
    )
    console.print("Copy that folder to your new project root and point your agent at REPO_MENU.md.")


@context_app.command("build")
def context_build(
    query: Annotated[str, typer.Option("--query")] = "",
    project_file: Annotated[Path | None, typer.Option("--project-file")] = None,
    tool: Annotated[str, typer.Option("--tool")] = "auto",
    max_repos: Annotated[int, typer.Option("--max-repos")] = 3,
) -> None:
    """Create a portable AI context pack for a project/query."""
    paths = ProjectPaths.load()
    project_text = _load_project_text(query, project_file) if (query or project_file) else "general repository intelligence project"
    result = recommend(paths.project_root, project_text, max_repos=max_repos, build_tool=tool)
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


@app.command()
def analyze(
    new: Annotated[bool, typer.Option("--new", help="Only newly discovered repos (not yet in INDICE_IA)")] = True,
    ids: Annotated[list[str], typer.Option("--id", help="Specific repo ids to analyze")] = None,
    force: Annotated[bool, typer.Option("--force", help="Re-run heavy tools even if artifacts exist")] = False,
) -> None:
    """Run deep analysis (repomix, markitdown, gitnexus) on repos and store artifacts.

    This is the first step for integral incorporation of new repositories.
    Artifacts go to data/packed/ and data/extracted/.
    """
    paths = ProjectPaths.load()
    registry = read_yaml(paths.registry_file, {"repos": []})
    recs = {r["id"]: r for r in registry.get("repos", [])}

    targets = curation_mod.get_new_repo_ids(paths.project_root) if new else list(recs.keys())
    if ids:
        targets = [i for i in ids if i in recs]

    table = Table(title="Analysis")
    table.add_column("Repo")
    table.add_column("Artifacts")
    table.add_column("Tools run")

    for rid in targets:
        rec = recs.get(rid)
        if not rec:
            continue
        res = curation_mod.ensure_analyzed(paths, rid, Path(rec["path"]), force=force)
        table.add_row(rid, str(res.get("packed", "")), ", ".join(res.get("ran", [])))
    console.print(table)
    console.print("Analysis artifacts written. Use `enrich` next.")


@app.command()
def enrich(
    new: Annotated[bool, typer.Option("--new", help="Only new (not yet curated) repos")] = True,
    ids: Annotated[list[str], typer.Option("--id")] = None,
    auto_merge: Annotated[bool, typer.Option("--auto-merge", help="Immediately merge drafts into INDICE_IA*.json so they become curated")] = False,
    force: Annotated[bool, typer.Option("--force", help="Force re-analysis")] = False,
) -> None:
    """Produce high-quality drafts (and optionally merge) with technical + theoretical ficha data.

    This is the key command that makes adding a repo *integral*:
    - infers category, role, tags, stack from content + manifests
    - generates desc, choose_if, avoid_if, combines etc.
    - writes data/drafts/<id>.json for review
    - with --auto-merge updates the source indices so guide build produces full fichas.
    """
    paths = ProjectPaths.load()
    res = curation_mod.run_enrich_for_new(
        paths.project_root,
        only_new=new,
        auto_merge=auto_merge,
        force_analyze=force,
    )
    console.print(f"Analyzed: {len(res['analyzed'])}  Drafted: {len(res['drafted'])}  Merged: {len(res.get('merged', []))}")
    if res["drafted"]:
        console.print("Drafts saved under data/drafts/")
        for d in res["drafted"][:5]:
            console.print(f"  - {d['id']}: {d['draft']}")
    if auto_merge:
        console.print("Merged into INDICE files. Run `guide build` to refresh all catalogs and human guides.")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _first_line(value: str, limit: int = 100) -> str:
    line = value.splitlines()[0] if value else ""
    return line[:limit]


def _load_project_text(project: str, project_file: Path | None) -> str:
    chunks: list[str] = []
    if project:
        chunks.append(project.strip())
    if project_file:
        if not project_file.exists():
            raise typer.BadParameter(f"No existe el archivo: {project_file}")
        if not project_file.is_file():
            raise typer.BadParameter(f"No es un archivo: {project_file}")
        chunks.append(project_file.read_text(encoding="utf-8").strip())
    text = "\n\n".join(chunk for chunk in chunks if chunk)
    if not text:
        raise typer.BadParameter("Escribe --project o usa --project-file proyecto.md")
    return text
