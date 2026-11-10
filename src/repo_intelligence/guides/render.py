"""Render every human-facing output of the library from the curated JSON.

Single source of truth: `INDICE_IA.json` + `INDICE_IA.detalle.json` (read via
`core.catalog`). Outputs are deterministic (no wall-clock timestamps) so a
rebuild without data changes produces no diff.

Outputs:
    Catalogo.md                      flat catalog grouped by category/subcategory
    Guia.md                          full guide in one document
    human/README.md                  human home: "¿qué quieres construir?", map, top
    human/catalogo.md                pointer to Catalogo.md
    human/categorias/NN-*.md         one page per category
    human/fichas/<id>.md             one card per repo
    human/comparativas/*.md          pairwise comparisons from `alt`
    human/playbooks/*.md             end-to-end recipes (with Mermaid flow)
    human/novedades.md               repos suggested but not cloned locally yet
    human/usar-ahora.md, diferir.md, descartar.md   install-mode views
    docs/index.html                  interactive explorer (see guides/explorer.py)
    ai_index/REPOS.detail.json       machine detail index used by `recommend`
    README.md / AGENTS.md            only the blocks between <!-- BL:* --> markers
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from repo_intelligence.core.catalog import (
    DECISION_LABELS,
    EXEC_LABELS,
    ROLE_LABELS,
    SETUP_LABELS,
    STATUS_LABELS,
    Catalog,
    category_filename,
    fmt_stars,
    gh_anchor,
    load_catalog,
    md_cell,
    slug,
)
from repo_intelligence.core.io import read_yaml, write_json
from repo_intelligence.guides.explorer import render_explorer

INSTALL_MODE_LABELS = {
    "global": ("🌍", "Global", "instálalo una vez en tu máquina"),
    "local_project": ("📦", "Dependencia del proyecto", "instálalo dentro de cada proyecto que lo use"),
    "docker_local": ("🐳", "Servicio Docker", "levántalo con Docker cuando el proyecto lo necesite"),
    "reference_only": ("📖", "Referencia", "léelo o clónalo; no lo instales de entrada"),
    "deferred": ("⏳", "Diferir", "pesado: solo si llega a finalista"),
}
MARKER_RE = r"<!-- BL:{name} -->.*?<!-- /BL:{name} -->"
FOOTER_SOURCE = "Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano."


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def render_all(project_root: Path) -> dict[str, int]:
    project_root = Path(project_root)
    cat = load_catalog(project_root)
    registry = read_yaml(project_root / "registry" / "repos.yaml", {"repos": []})
    local_ids = _local_ids(registry.get("repos", []))

    _render_detail_index(project_root, cat, local_ids)
    _render_fichas(project_root, cat, local_ids)
    _render_categories(project_root, cat)
    comparisons = _render_comparisons(project_root, cat)
    _render_playbooks(project_root, cat)
    _render_install_views(project_root, cat)
    _render_novedades(project_root, cat)
    _render_catalog(project_root, cat, local_ids)
    _render_guide(project_root, cat)
    _render_human_home(project_root, cat)
    render_explorer(project_root, cat)
    _update_root_docs(project_root, cat)

    return {
        "repos": len(cat.repos),
        "categories": len(cat.public_categories()),
        "cards": len(cat.repos),
        "comparisons": comparisons,
        "playbooks": len(cat.recipes),
    }


# ---------------------------------------------------------------------------
# Link helpers (relative paths depend on where the page lives)
# ---------------------------------------------------------------------------

_PREFIX = {
    "root": "human/",
    "human": "",
    "fichas": "../",
    "categorias": "../",
    "playbooks": "../",
    "comparativas": "../",
}


def ficha_path(repo_id: str, base: str) -> str:
    if base == "fichas":
        return f"{slug(repo_id)}.md"
    return f"{_PREFIX[base]}fichas/{slug(repo_id)}.md"


def category_path(cat: Catalog, num: int, base: str) -> str:
    filename = cat.category_file(num)
    if base == "categorias":
        return filename
    return f"{_PREFIX[base]}categorias/{filename}"


def playbook_path(recipe_id: str, base: str) -> str:
    if base == "playbooks":
        return f"{slug(recipe_id)}.md"
    return f"{_PREFIX[base]}playbooks/{slug(recipe_id)}.md"


def repo_link(cat: Catalog, repo_id: str, base: str, label: str | None = None) -> str:
    repo = cat.get(repo_id)
    if not repo:
        return f"`{repo_id}`"
    return f"[{label or repo.get('name') or repo_id}]({ficha_path(repo['id'], base)})"


def category_label(cat: Catalog, num: int) -> str:
    c = cat.category(num)
    return f"{c.get('emoji', '📁')} {c.get('title', '')}".strip()


# ---------------------------------------------------------------------------
# Badges / small formatters
# ---------------------------------------------------------------------------

def _label(table: dict[str, tuple[str, str]], value: str | None) -> str:
    icon, text = table.get(value or "", ("", value or "—"))
    return f"{icon} {text}".strip()


def _icon(table: dict[str, tuple[str, str]], value: str | None) -> str:
    return table.get(value or "", ("—", ""))[0]


def _local_flag(repo: dict[str, Any], local_ids: set[str] | None = None) -> str:
    if repo.get("status") in {"local", "alias"}:
        return "🧰"
    if local_ids is not None and local_ids:
        return "📦" if repo["id"].lower() in local_ids else "🆕"
    return "📦" if repo.get("lib") else "🆕"


def _install_mode_text(mode: str) -> str:
    icon, title, hint = INSTALL_MODE_LABELS.get(mode, ("📖", mode, ""))
    return f"{icon} **{title}** — {hint}" if hint else f"{icon} **{title}**"


def _status_note(repo: dict[str, Any]) -> str:
    status = repo.get("status")
    if not status:
        return ""
    note = STATUS_LABELS.get(status, "")
    if status == "alias" and repo.get("alias_of"):
        note = f"🔁 Alias local de `{repo['alias_of']}`; usa esa ficha."
    return note


def _name_with_pick(repo: dict[str, Any], link: str) -> str:
    return f"⭐ {link}" if repo.get("pick") else link


def _strip_period(text: str) -> str:
    return (text or "").strip().rstrip(".")


def _footer(cat: Catalog) -> str:
    checked = f" Datos de GitHub verificados el {cat.checked_at}." if cat.checked_at else ""
    return f"---\n\n<sub>{FOOTER_SOURCE}{checked}</sub>\n"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


def _clean_dir(directory: Path, keep: set[str]) -> None:
    if not directory.exists():
        return
    for path in directory.glob("*.md"):
        if path.name not in keep:
            path.unlink()


def _local_ids(registry_repos: list[dict[str, Any]]) -> set[str]:
    ids: set[str] = set()
    for repo in registry_repos:
        for key in ("id", "name"):
            value = (repo.get(key) or "").lower()
            if value:
                ids.add(value)
    return ids


# ---------------------------------------------------------------------------
# ai_index/REPOS.detail.json (consumed by `recommend`)
# ---------------------------------------------------------------------------

def _render_detail_index(project_root: Path, cat: Catalog, local_ids: set[str]) -> None:
    rows = []
    for repo in sorted(cat.repos, key=lambda r: r["id"]):
        rows.append(
            {
                "id": repo["id"],
                "name": repo.get("name"),
                "cat": repo.get("cat"),
                "sub": repo.get("sub"),
                "role": repo.get("role"),
                "exec": repo.get("exec"),
                "setup": repo.get("setup"),
                "tags": repo.get("tags", []),
                "stars": repo.get("stars"),
                "one": repo.get("one"),
                "desc": repo.get("desc") or repo.get("one", ""),
                "stack": repo.get("stack"),
                "install": repo.get("install"),
                "choose_if": repo.get("choose_if"),
                "avoid_if": repo.get("avoid_if"),
                "combines_with": repo.get("combines_with", []),
                "alternatives": repo.get("alternatives", []),
                "install_mode": repo.get("install_mode"),
                "decision": repo.get("decision"),
                "local": (repo["id"].lower() in local_ids) if local_ids else bool(repo.get("lib")),
                "repo_url": repo.get("repo_url"),
                "doc": repo.get("doc"),
            }
        )
    write_json(project_root / "ai_index" / "REPOS.detail.json", {"generated_from": "INDICE_IA.json + INDICE_IA.detalle.json", "repos": rows})


# ---------------------------------------------------------------------------
# human/fichas/<id>.md
# ---------------------------------------------------------------------------

def _render_fichas(project_root: Path, cat: Catalog, local_ids: set[str]) -> None:
    out = project_root / "human" / "fichas"
    keep: set[str] = set()
    for repo in cat.repos:
        filename = f"{slug(repo['id'])}.md"
        keep.add(filename)
        _write(out / filename, _ficha(cat, repo, local_ids))
    _clean_dir(out, keep)


def _ficha(cat: Catalog, repo: dict[str, Any], local_ids: set[str]) -> str:
    num = int(repo.get("cat") or 0)
    c = cat.category(num)
    crumbs = ["[🏠 Inicio](../README.md)"]
    if num > 0:
        crumbs.append(f"[{category_label(cat, num)}]({category_path(cat, num, 'fichas')})")
        crumbs.append(cat.sub_title(num, repo.get("sub")))
    lines = [" › ".join(crumbs), "", f"# {repo.get('emoji') or _icon(ROLE_LABELS, repo.get('role'))} {repo.get('name') or repo['id']}", ""]
    if repo.get("one"):
        lines += [f"> {repo['one']}", ""]

    local = _local_flag(repo, local_ids)
    local_text = {"📦": "📦 Sí", "🆕": "🆕 Aún no (sugerido)", "🧰": "🧰 Interna"}[local]
    lines += [
        "| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |",
        "|---|---|---|---|---|",
        f"| {fmt_stars(repo.get('stars'))} | {md_cell(repo.get('license') or '—')} | {md_cell(repo.get('lang') or '—')} | {md_cell(repo.get('updated') or '—')} | {local_text} |",
        "",
        " · ".join(
            part
            for part in [
                f"**Ejecución** {_label(EXEC_LABELS, repo.get('exec'))}",
                f"**Rol** {_label(ROLE_LABELS, repo.get('role'))}",
                f"**Setup** {_label(SETUP_LABELS, repo.get('setup'))}",
                "**MCP** 🔌 sí" if repo.get("mcp") else "",
            ]
            if part
        ),
        "",
    ]
    status = _status_note(repo)
    if status:
        lines += [f"> {status}", ""]

    def section(title: str, body: str | None) -> None:
        if body:
            lines.extend([f"## {title}", "", body.strip(), ""])

    section("Qué es", repo.get("desc"))
    section("Por qué destaca", repo.get("why"))
    section("Cómo funciona", repo.get("how"))
    section("Instalación rápida", repo.get("install"))
    if repo.get("cases"):
        lines += ["## Casos de uso", ""] + [f"- {case}" for case in repo["cases"]] + [""]
    if repo.get("choose_if") or repo.get("avoid_if"):
        lines += [
            "## ¿Es para ti?",
            "",
            "| ✅ Elígelo si… | ⛔ Evítalo si… |",
            "|---|---|",
            f"| {md_cell(repo.get('choose_if') or '—')} | {md_cell(repo.get('avoid_if') or '—')} |",
            "",
        ]
    if repo.get("limits"):
        lines += [f"**Limitaciones:** {repo['limits']}", ""]

    facts = []
    if repo.get("stack"):
        facts.append(f"- **Stack:** {repo['stack']}")
    if repo.get("models"):
        facts.append(f"- **Modelos / API:** {repo['models']}")
    if repo.get("tags"):
        facts.append("- **Etiquetas:** " + " ".join(f"`{tag}`" for tag in repo["tags"]))
    facts.append(f"- **Modo de instalación sugerido:** {_install_mode_text(repo.get('install_mode', 'reference_only'))}")
    lines += ["## Stack y modelos", ""] + facts + [""]

    lines += _repo_table_section(cat, "Combina con", repo.get("combines_with", []), "fichas")
    lines += _repo_table_section(cat, "Alternativas (elige una)", repo.get("alternatives", []), "fichas")

    links = []
    if repo.get("repo_url"):
        label = repo.get("gh") or repo["repo_url"].replace("https://github.com/", "")
        links.append(f"- 🐙 GitHub: [{label}]({repo['repo_url']})")
    if repo.get("homepage"):
        links.append(f"- 🌐 Web: <{repo['homepage']}>")
    for recipe in cat.recipes_using(repo["id"]):
        links.append(f"- 🧪 Receta: [{recipe.get('title')}]({playbook_path(recipe['id'], 'fichas')})")
    if links:
        lines += ["## Enlaces", ""] + links + [""]
    lines.append(_footer(cat))
    return "\n".join(lines)


def _repo_table_section(cat: Catalog, title: str, ids: list[str], base: str) -> list[str]:
    rows = []
    for other_id in ids:
        other = cat.get(other_id)
        if not other:
            continue
        rows.append(f"| {repo_link(cat, other['id'], base)} | {fmt_stars(other.get('stars'))} | {md_cell(other.get('one'))} |")
    if not rows:
        return []
    return [f"## {title}", "", "| Repo | ⭐ | Qué hace |", "|---|---:|---|", *rows, ""]


# ---------------------------------------------------------------------------
# human/categorias/NN-*.md
# ---------------------------------------------------------------------------

def _render_categories(project_root: Path, cat: Catalog) -> None:
    out = project_root / "human" / "categorias"
    cats = cat.public_categories()
    keep: set[str] = set()
    for index, c in enumerate(cats):
        num = int(c["num"])
        filename = cat.category_file(num)
        keep.add(filename)
        prev_c = cats[index - 1] if index > 0 else None
        next_c = cats[index + 1] if index + 1 < len(cats) else None
        _write(out / filename, _category_page(cat, c, prev_c, next_c))
    _clean_dir(out, keep)


def _category_page(cat: Catalog, c: dict[str, Any], prev_c: dict[str, Any] | None, next_c: dict[str, Any] | None) -> str:
    num = int(c["num"])
    repos = cat.in_category(num, include_aliases=False)
    nav = ["[🏠 Inicio](../README.md)", "[📚 Catálogo](../../Catalogo.md)"]
    if prev_c:
        nav.append(f"[⬅️ {prev_c['num']}. {prev_c['title']}]({cat.category_file(int(prev_c['num']))})")
    if next_c:
        nav.append(f"[{next_c['num']}. {next_c['title']} ➡️]({cat.category_file(int(next_c['num']))})")
    new_count = sum(1 for r in repos if not r.get("lib") and r.get("status") not in {"local"})
    groups = cat.grouped(num, include_aliases=False)
    lines = [
        " · ".join(nav),
        "",
        f"# {c.get('emoji', '')} {num}. {c['title']}".replace("  ", " "),
        "",
        f"> {c.get('desc', '')}",
        "",
        f"**{len(repos)} repos** · {len(groups)} subcategorías · ⭐ {fmt_stars(sum(r.get('stars') or 0 for r in repos))} estrellas en total"
        + (f" · 🆕 {new_count} sugeridos nuevos" if new_count else ""),
        "",
    ]
    picks = cat.picks(num)
    if picks:
        lines += [
            "## ⭐ Imprescindibles",
            "",
            "Si solo vas a mirar unos pocos, empieza por estos:",
            "",
            "| Repo | ⭐ | Qué hace | Instalación |",
            "|---|---:|---|---|",
        ]
        for repo in picks:
            lines.append(
                f"| {repo_link(cat, repo['id'], 'categorias')} | {fmt_stars(repo.get('stars'))} | {md_cell(repo.get('one'))} | {md_cell(_short_install(repo.get('install')))} |"
            )
        lines.append("")

    lines += ["## 🧭 Subcategorías", ""]
    for key, members in groups:
        title = cat.sub_title(num, key)
        lines.append(f"- [{title}](#{gh_anchor(title)}) — {len(members)} repos")
    lines.append("")

    for key, members in groups:
        title = cat.sub_title(num, key)
        lines += [f"## {title}", "", "| Repo | ⭐ | Qué hace | Ideal si… | Setup |", "|---|---:|---|---|:---:|"]
        for repo in members:
            name = _name_with_pick(repo, repo_link(cat, repo["id"], "categorias"))
            if not repo.get("lib") and repo.get("status") != "local":
                name += " 🆕"
            lines.append(
                f"| {name} | {fmt_stars(repo.get('stars'))} | {md_cell(repo.get('one'))} | {md_cell(_strip_period(repo.get('choose_if')))} | {_icon(SETUP_LABELS, repo.get('setup'))} |"
            )
        lines.append("")

    choices = _choice_groups(cat, num)
    if choices:
        lines += ["## ⚖️ ¿Cuál elegir?", "", "Repos que cumplen la misma función: elige uno por grupo.", ""]
        for members in choices:
            names = ", ".join(m.get("name") or m["id"] for m in members)
            lines += [f"### {names}", "", "| Repo | ⭐ | Elígelo si… | Evítalo si… |", "|---|---:|---|---|"]
            for repo in members:
                lines.append(
                    f"| {repo_link(cat, repo['id'], 'categorias')} | {fmt_stars(repo.get('stars'))} | {md_cell(_strip_period(repo.get('choose_if')))} | {md_cell(_strip_period(repo.get('avoid_if')))} |"
                )
            lines.append("")

    related = [rc for rc in cat.recipes if any((cat.get(r) or {}).get("cat") == num for r in rc.get("repos", []))]
    if related:
        lines += ["## 🧪 Recetas que usan esta categoría", ""]
        lines += [f"- [{rc.get('emoji', '')} {rc['title']}]({playbook_path(rc['id'], 'categorias')}) — {rc.get('goal', '')}".replace("[ ", "[") for rc in related]
        lines.append("")
    lines += [
        "## 🏷️ Leyenda",
        "",
        "⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).",
        "",
        _footer(cat),
    ]
    return "\n".join(lines)


_COMMAND_STARTS = (
    "npm", "npx", "pnpm", "yarn", "bun", "pip", "pipx", "uv", "uvx", "python", "docker", "git ", "brew",
    "go ", "cargo", "curl", "wget", "/plugin", "ollama", "winget", "apt", "conda", "make", "helm", "deno",
    "gem", "composer", "irm", "iwr", "claude ", "gh ", "dotnet", "mvn", "gradle", "flatpak", "snap",
)


def _looks_like_command(snippet: str) -> bool:
    """True si el fragmento entre comillas invertidas es un comando, no una ruta o un nombre."""
    s = snippet.strip()
    return s.startswith(_COMMAND_STARTS) and " " in s


def _public_count(repos: list[dict[str, Any]]) -> int:
    """Repos de las 13 categorías públicas (sin las utilidades internas del hub)."""
    return sum(1 for r in repos if int(r.get("cat") or 0) > 0)


def _short_install(text: str | None) -> str:
    if not text:
        return "—"
    for snippet in re.findall(r"`([^`]+)`", text):
        if _looks_like_command(snippet):
            return f"`{snippet}`"
    return text if len(text) <= 90 else text[:87].rstrip() + "…"


def _choice_groups(cat: Catalog, num: int) -> list[list[dict[str, Any]]]:
    members = {r["id"]: r for r in cat.in_category(num, include_aliases=False)}
    adjacency: dict[str, set[str]] = defaultdict(set)
    for repo_id, repo in members.items():
        for alt in repo.get("alternatives", []):
            other = cat.get(alt)
            if other and other["id"] in members and other["id"] != repo_id:
                adjacency[repo_id].add(other["id"])
                adjacency[other["id"]].add(repo_id)
    seen: set[str] = set()
    groups: list[list[dict[str, Any]]] = []
    order = [r["id"] for r in cat.in_category(num, include_aliases=False)]
    for start in order:
        if start in seen or start not in adjacency:
            continue
        stack, component = [start], []
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            component.append(node)
            stack.extend(adjacency[node] - seen)
        if len(component) >= 2:
            ranked = sorted((members[i] for i in component), key=lambda r: (0 if r.get("pick") else 1, -(r.get("stars") or 0)))
            groups.append(ranked[:7])
    return groups


# ---------------------------------------------------------------------------
# human/comparativas/*.md
# ---------------------------------------------------------------------------

def _render_comparisons(project_root: Path, cat: Catalog) -> int:
    out = project_root / "human" / "comparativas"
    # Solo "la recomendada vs su rival principal": cada repo marcado como pick se
    # compara con su primera alternativa de la misma categoría. Así hay una
    # comparativa útil por decisión, no una por cada pareja posible.
    pairs: set[tuple[str, str]] = set()
    for repo in cat.repos:
        if not repo.get("pick") or repo.get("alias_of"):
            continue
        for alt in repo.get("alternatives", []):
            other = cat.get(alt)
            if not other or other["id"] == repo["id"] or other.get("alias_of"):
                continue
            if other.get("cat") != repo.get("cat"):
                continue
            pairs.add(tuple(sorted((repo["id"], other["id"]))))  # type: ignore[arg-type]
            break
    keep: set[str] = {"README.md"}
    by_cat: dict[int, list[tuple[str, str, str]]] = defaultdict(list)
    for left_id, right_id in sorted(pairs):
        left, right = cat.get(left_id), cat.get(right_id)
        assert left and right
        filename = f"{slug(left_id)}-vs-{slug(right_id)}.md"
        keep.add(filename)
        _write(out / filename, _comparison(cat, left, right))
        by_cat[int(left.get("cat") or 0)].append((filename, left.get("name") or left_id, right.get("name") or right_id))

    lines = ["[🏠 Inicio](../README.md)", "", "# ⚖️ Comparativas", "", f"{len(pairs)} comparaciones directas: la opción recomendada de cada subcategoría frente a su rival principal.", ""]
    for num in sorted(by_cat):
        lines += [f"## {category_label(cat, num)}", ""]
        lines += [f"- [{a} vs {b}]({fname})" for fname, a, b in by_cat[num]]
        lines.append("")
    lines.append(_footer(cat))
    _write(out / "README.md", "\n".join(lines))
    _clean_dir(out, keep)
    return len(pairs)


def _comparison(cat: Catalog, left: dict[str, Any], right: dict[str, Any]) -> str:
    def row(label: str, key: str, fmt=None) -> str:
        lv, rv = left.get(key), right.get(key)
        if fmt:
            lv, rv = fmt(lv), fmt(rv)
        return f"| {label} | {md_cell(lv or '—')} | {md_cell(rv or '—')} |"

    lname, rname = left.get("name") or left["id"], right.get("name") or right["id"]
    lines = [
        "[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)",
        "",
        f"# {lname} vs {rname}",
        "",
        f"| | {repo_link(cat, left['id'], 'comparativas')} | {repo_link(cat, right['id'], 'comparativas')} |",
        "|---|---|---|",
        row("Qué hace", "one"),
        row("⭐ Estrellas", "stars", fmt_stars),
        row("Elígelo si…", "choose_if"),
        row("Evítalo si…", "avoid_if"),
        row("Ejecución", "exec", lambda v: _label(EXEC_LABELS, v)),
        row("Setup", "setup", lambda v: _label(SETUP_LABELS, v)),
        row("Licencia", "license"),
        row("Instalación", "install", _short_install),
        "",
        "## Regla práctica",
        "",
    ]
    if left.get("choose_if") and right.get("choose_if"):
        lines += [
            f"- Elige **{lname}** si {_strip_period(left['choose_if'])}.",
            f"- Elige **{rname}** si {_strip_period(right['choose_if'])}.",
            "- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.",
        ]
    else:
        lines.append(f"Elige uno según el caso de uso; deja el otro como alternativa.")
    lines += ["", _footer(cat)]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# human/playbooks/*.md
# ---------------------------------------------------------------------------

def _render_playbooks(project_root: Path, cat: Catalog) -> None:
    out = project_root / "human" / "playbooks"
    keep: set[str] = {"README.md"}
    for recipe in cat.recipes:
        filename = f"{slug(recipe['id'])}.md"
        keep.add(filename)
        _write(out / filename, _playbook(cat, recipe))
    lines = ["[🏠 Inicio](../README.md)", "", "# 🧪 Recetas end-to-end", "", "Stacks completos ya pensados: parte de una receta cuando tu proyecto es un producto y no una pieza suelta.", ""]
    lines += ["| Receta | Objetivo | Piezas |", "|---|---|---:|"]
    for recipe in cat.recipes:
        lines.append(f"| [{recipe.get('emoji', '')} {recipe['title']}]({slug(recipe['id'])}.md) | {md_cell(recipe.get('goal'))} | {len(recipe.get('repos', []))} |".replace("[ ", "["))
    lines += ["", _footer(cat)]
    _write(out / "README.md", "\n".join(lines))
    _clean_dir(out, keep)


def _mermaid_node(cat: Catalog, value: str) -> str:
    node_id = re.sub(r"\W", "_", value)
    repo = cat.get(value)
    label = (repo.get("name") if repo else value).replace('"', "'")
    return f'{node_id}["{label}"]'


def _playbook(cat: Catalog, recipe: dict[str, Any]) -> str:
    lines = [
        "[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)",
        "",
        f"# {recipe.get('emoji', '🧪')} {recipe['title']}",
        "",
        f"> **Objetivo:** {recipe.get('goal', '')}",
        "",
    ]
    flow = recipe.get("flow") or []
    if not flow and len(recipe.get("repos", [])) > 1:
        ids = recipe["repos"]
        flow = [[ids[i], ids[i + 1]] for i in range(len(ids) - 1)]
    if flow:
        lines += ["## 🗺️ Cómo fluye", "", "```mermaid", "flowchart LR"]
        for edge in flow:
            src, dst = _mermaid_node(cat, edge[0]), _mermaid_node(cat, edge[1])
            label = f"|{edge[2]}|" if len(edge) > 2 and edge[2] else ""
            lines.append(f"  {src} -->{label} {dst}")
        lines += ["```", ""]

    steps = recipe.get("steps") or [{"id": rid, "role": ""} for rid in recipe.get("repos", [])]
    lines += ["## 🧩 Piezas", "", "| # | Repo | Papel en la receta | ⭐ | Instalación |", "|---:|---|---|---:|---|"]
    for index, step in enumerate(steps, start=1):
        repo = cat.get(step["id"]) or {}
        role = step.get("role") or repo.get("one") or ""
        lines.append(
            f"| {index} | {repo_link(cat, step['id'], 'playbooks')} | {md_cell(role)} | {fmt_stars(repo.get('stars'))} | {md_cell(_short_install(repo.get('install')))} |"
        )
    lines.append("")
    if recipe.get("how"):
        lines += ["## 🔌 Cómo se conecta", "", recipe["how"], ""]
    if recipe.get("when_not"):
        lines += ["## 🚫 Cuándo NO usar esta receta", "", recipe["when_not"], ""]
    variants = []
    for step in steps:
        repo = cat.get(step["id"]) or {}
        alts = [a for a in repo.get("alternatives", []) if cat.get(a)]
        if alts:
            variants.append(f"- En lugar de {repo_link(cat, step['id'], 'playbooks')}: " + ", ".join(repo_link(cat, a, "playbooks") for a in alts[:3]))
    if variants:
        lines += ["## 🔁 Variantes", "", *variants, ""]
    lines.append(_footer(cat))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# human/usar-ahora.md, diferir.md, descartar.md
# ---------------------------------------------------------------------------

def _render_install_views(project_root: Path, cat: Catalog) -> None:
    human = project_root / "human"
    use_now = [r for r in cat.repos if r.get("decision") == "use_now"]
    defer = [r for r in cat.repos if r.get("decision") == "defer"]
    _write(
        human / "usar-ahora.md",
        _install_view(
            cat,
            "✅ Usar ahora",
            "Piezas que la política del hub (`config/repo_policy.yaml`) marca para instalar de entrada: herramientas globales, dependencias de proyecto y servicios Docker.",
            use_now,
        ),
    )
    _write(
        human / "diferir.md",
        _install_view(cat, "⏳ Diferir", "Herramientas valiosas pero pesadas (GPU, varios servicios o mucha configuración): instálalas solo cuando sean finalistas claros.", defer),
    )
    alternatives = [r for r in cat.repos if r.get("alternatives") and not r.get("alias_of")]
    lines = [
        "[🏠 Inicio](../README.md)",
        "",
        "# 🔀 Alternativas y descartes",
        "",
        "Nada se borra: cuando dos repos cumplen la misma función se marcan como alternativas. Elige uno por función y deja el otro como plan B.",
        "",
        "| Repo | Alternativas declaradas |",
        "|---|---|",
    ]
    for repo in sorted(alternatives, key=lambda r: (int(r.get("cat") or 0), (r.get("name") or "").lower())):
        alts = ", ".join(repo_link(cat, a, "human") for a in repo["alternatives"] if cat.get(a))
        lines.append(f"| {repo_link(cat, repo['id'], 'human')} | {alts} |")
    lines += ["", f"Ver también [⚖️ Comparativas](comparativas/README.md).", "", _footer(cat)]
    _write(human / "descartar.md", "\n".join(lines))


def _install_view(cat: Catalog, title: str, intro: str, repos: list[dict[str, Any]]) -> str:
    lines = ["[🏠 Inicio](../README.md)", "", f"# {title}", "", intro, "", f"**{len(repos)} repos.**", ""]
    by_mode: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for repo in repos:
        by_mode[repo.get("install_mode") or "reference_only"].append(repo)
    for mode in ["global", "local_project", "docker_local", "deferred", "reference_only"]:
        members = by_mode.get(mode)
        if not members:
            continue
        icon, label, hint = INSTALL_MODE_LABELS[mode]
        lines += [f"## {icon} {label}", "", f"_{hint.capitalize()}._", "", "| Repo | Categoría | Qué hace |", "|---|---|---|"]
        for repo in sorted(members, key=lambda r: (int(r.get("cat") or 0), -(r.get("stars") or 0))):
            lines.append(f"| {repo_link(cat, repo['id'], 'human')} | {category_label(cat, int(repo.get('cat') or 0))} | {md_cell(repo.get('one'))} |")
        lines.append("")
    lines.append(_footer(cat))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# human/novedades.md
# ---------------------------------------------------------------------------

def _render_novedades(project_root: Path, cat: Catalog) -> None:
    new = [r for r in cat.repos if not r.get("lib") and r.get("status") not in {"local", "alias"}]
    lines = [
        "[🏠 Inicio](../README.md)",
        "",
        "# 🆕 Repos sugeridos (aún no clonados)",
        "",
        f"**{len(new)} repos** curados con ficha completa que todavía no están en tu biblioteca local (`../Repositorios_Prueba`). "
        "Se eligieron por popularidad (estrellas) y porque cubren huecos de cada sección.",
        "",
        "## Cómo traerlos a tu biblioteca",
        "",
        "Previsualiza qué se clonaría (por categoría o por id) y luego ejecútalo con `--run`:",
        "",
        "```bash",
        "uv run repo-intelligence clone --cat 8",
        "uv run repo-intelligence clone --id ollama --id open-webui --run",
        "```",
        "",
        "Después: `uv run repo-intelligence discover` y `uv run repo-intelligence guide build`. Sus fichas ya están curadas, así que no hace falta `enrich`.",
        "",
    ]
    by_cat: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for repo in new:
        by_cat[int(repo.get("cat") or 0)].append(repo)
    for num in sorted(by_cat):
        members = sorted(by_cat[num], key=lambda r: -(r.get("stars") or 0))
        lines += [f"## {category_label(cat, num)} ({len(members)})", "", "| Repo | ⭐ | Qué hace |", "|---|---:|---|"]
        for repo in members:
            lines.append(f"| {repo_link(cat, repo['id'], 'human')} | {fmt_stars(repo.get('stars'))} | {md_cell(repo.get('one'))} |")
        lines.append("")
    lines.append(_footer(cat))
    _write(project_root / "human" / "novedades.md", "\n".join(lines))


# ---------------------------------------------------------------------------
# Catalogo.md (root) + human/catalogo.md (pointer)
# ---------------------------------------------------------------------------

def _render_catalog(project_root: Path, cat: Catalog, local_ids: set[str]) -> None:
    repos = [r for r in cat.repos if not r.get("alias_of")]
    lines = [
        "# 📚 Catálogo de BL_Alexandria",
        "",
        f"**{_public_count(repos)} repos** de IA y automatización en **{len(cat.public_categories())} categorías**, con una línea por repo."
        + (f" Estrellas de GitHub al {cat.checked_at}." if cat.checked_at else ""),
        "",
        "[🗺️ Guía humana](human/README.md) · [🔎 Explorador interactivo](docs/index.html) · [🧪 Recetas](human/playbooks/README.md) · [🆕 Novedades](human/novedades.md) · [🤖 Para agentes](AGENTS.md)",
        "",
        "> **Leyenda:** ⭐ imprescindible de su sección · 📦 ya está en tu biblioteca local · 🆕 sugerido (aún no clonado) · Rol: ⚙️ plataforma · 🧩 motor · 📚 librería · 🎨 skill · 📂 catálogo · 🖥️ app · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado",
        "",
        "## Índice",
        "",
    ]
    for c in cat.public_categories():
        title = f"{c.get('emoji', '')} {c['num']}. {c['title']}"
        count = len(cat.in_category(int(c["num"]), include_aliases=False))
        lines.append(f"{c['num']}. [{c.get('emoji', '')} {c['title']}](#{gh_anchor(title)}) — {count}")
    lines += ["", "## 🔥 Top 30 por estrellas", "", "| # | Repo | ⭐ | Categoría | Qué hace |", "|---:|---|---:|---|---|"]
    top = sorted((r for r in repos if isinstance(r.get("stars"), int) and int(r.get("cat") or 0) > 0), key=lambda r: -r["stars"])[:30]
    for index, repo in enumerate(top, start=1):
        lines.append(
            f"| {index} | {repo_link(cat, repo['id'], 'root')} | {fmt_stars(repo['stars'])} | {category_label(cat, int(repo['cat']))} | {md_cell(repo.get('one'))} |"
        )
    lines.append("")
    for c in cat.public_categories():
        num = int(c["num"])
        lines += [f"## {c.get('emoji', '')} {num}. {c['title']}", "", f"_{c.get('desc', '')}_ → [página de la categoría]({category_path(cat, num, 'root')})", ""]
        for key, members in cat.grouped(num, include_aliases=False):
            lines += [f"### {cat.sub_title(num, key)}", "", "| Repo | ⭐ | Qué hace | Rol | Setup | |", "|---|---:|---|:---:|:---:|:---:|"]
            for repo in members:
                lines.append(
                    f"| {_name_with_pick(repo, repo_link(cat, repo['id'], 'root'))} | {fmt_stars(repo.get('stars'))} | {md_cell(repo.get('one'))} | {_icon(ROLE_LABELS, repo.get('role'))} | {_icon(SETUP_LABELS, repo.get('setup'))} | {_local_flag(repo, local_ids)} |"
                )
            lines.append("")
    internal = [r for r in cat.repos if int(r.get("cat") or 0) == 0]
    if internal:
        lines += ["## 🧰 Utilidades internas del hub", "", "| Carpeta | Qué es |", "|---|---|"]
        lines += [f"| {repo_link(cat, r['id'], 'root')} | {md_cell(r.get('one'))} |" for r in internal]
        lines.append("")
    lines.append(_footer(cat))
    _write(project_root / "Catalogo.md", "\n".join(lines))
    _write(
        project_root / "human" / "catalogo.md",
        "[🏠 Inicio](README.md)\n\n# 📚 Catálogo\n\nEl catálogo completo vive en la raíz: **[Catalogo.md](../Catalogo.md)** (una línea por repo, agrupado por categoría y subcategoría, con estrellas).\n",
    )


# ---------------------------------------------------------------------------
# Guia.md — the whole library in one document
# ---------------------------------------------------------------------------

def _render_guide(project_root: Path, cat: Catalog) -> None:
    repos = [r for r in cat.repos if not r.get("alias_of")]
    lines = [
        "# 🌌 Guía completa de BL_Alexandria",
        "",
        f"Las **{_public_count(repos)} fichas** de la biblioteca en un solo documento, agrupadas por categoría y subcategoría. "
        "Úsala para leer de corrido o buscar con Ctrl+F; para navegar por partes usa la [guía humana](human/README.md) "
        "o el [explorador interactivo](docs/index.html).",
        "",
        "## 🧭 Cómo leer cada ficha",
        "",
        "- **Etiquetas:** Ejecución 🏠 local · ☁️ cloud/API · 🔀 híbrido — Rol ⚙️ plataforma · 🧩 motor · 📚 librería · 🎨 skill · 📂 catálogo · 🖥️ app — Setup 🟢 fácil · 🟡 medio · 🔴 pesado — 🔌 MCP.",
        "- **⭐** junto al nombre: imprescindible de su subcategoría. El número de estrellas viene de GitHub.",
        "- **Elige si / Evita si** te dicen en una línea si encaja; **Combina con** lleva a sus complementos.",
        "",
        "## 📂 Mapa de categorías",
        "",
        "| # | Categoría | Repos | Para qué |",
        "|---:|---|---:|---|",
    ]
    for c in cat.public_categories():
        title = f"{c.get('emoji', '')} {c['num']}. {c['title']}"
        lines.append(f"| {c['num']} | [{c.get('emoji', '')} {c['title']}](#{gh_anchor(title)}) | {len(cat.in_category(int(c['num']), include_aliases=False))} | {md_cell(c.get('desc'))} |")
    lines += ["", "## 🧪 Recetas de integración", ""]
    for recipe in cat.recipes:
        names = " → ".join(repo_link(cat, rid, "root") for rid in recipe.get("repos", []))
        lines.append(f"- **[{recipe.get('emoji', '')} {recipe['title']}]({playbook_path(recipe['id'], 'root')})** — {recipe.get('goal', '')} {names}".replace("[ ", "["))
    lines.append("")
    for c in cat.public_categories():
        num = int(c["num"])
        lines += ["---", "", f"## {c.get('emoji', '')} {num}. {c['title']}", "", c.get("desc", ""), ""]
        for members in _choice_groups(cat, num):
            names = ", ".join(m.get("name") or m["id"] for m in members)
            lines += [f"**⚖️ ¿Cuál elegir? — {names}**", "", "| Repo | Elígelo si… | Evítalo si… |", "|---|---|---|"]
            for repo in members:
                lines.append(f"| {repo_link(cat, repo['id'], 'root')} | {md_cell(_strip_period(repo.get('choose_if')))} | {md_cell(_strip_period(repo.get('avoid_if')))} |")
            lines.append("")
        for key, members in cat.grouped(num, include_aliases=False):
            lines += [f"### {cat.sub_title(num, key)}", ""]
            for repo in members:
                lines += _guide_card(cat, repo)
    lines.append(_footer(cat))
    _write(project_root / "Guia.md", "\n".join(lines))


def _guide_card(cat: Catalog, repo: dict[str, Any]) -> list[str]:
    star = " ⭐" if repo.get("pick") else ""
    tags = [
        f"Ejecución {_label(EXEC_LABELS, repo.get('exec'))}",
        "MCP 🔌" if repo.get("mcp") else "",
        f"Rol {_label(ROLE_LABELS, repo.get('role'))}",
        f"Setup {_label(SETUP_LABELS, repo.get('setup'))}",
        f"⭐ {fmt_stars(repo.get('stars'))}" if repo.get("stars") else "",
    ]
    lines = [f"#### {repo.get('emoji') or _icon(ROLE_LABELS, repo.get('role'))} {repo.get('name') or repo['id']}{star}", f"**Etiquetas:** {' · '.join(t for t in tags if t)}  "]
    status = _status_note(repo)
    if status:
        lines.append(f"**Aviso:** {status}  ")
    if repo.get("desc"):
        lines.append(f"**Qué es:** {repo['desc']}  ")
    if repo.get("install"):
        lines.append(f"**Instalación:** {repo['install']}  ")
    if repo.get("choose_if") or repo.get("avoid_if"):
        lines.append(f"**Elige si:** {_strip_period(repo.get('choose_if')) or '—'} — **Evita si:** {_strip_period(repo.get('avoid_if')) or '—'}  ")
    combos = [repo_link(cat, c, "root") for c in repo.get("combines_with", []) if cat.get(c)]
    if combos:
        lines.append(f"**Combina con:** {' · '.join(combos)}  ")
    link_parts = [f"[ficha completa]({ficha_path(repo['id'], 'root')})"]
    if repo.get("repo_url"):
        link_parts.append(f"[GitHub]({repo['repo_url']})")
    lines += [f"**Más:** {' · '.join(link_parts)}", ""]
    return lines


# ---------------------------------------------------------------------------
# human/README.md
# ---------------------------------------------------------------------------

def _render_human_home(project_root: Path, cat: Catalog) -> None:
    repos = [r for r in cat.repos if not r.get("alias_of") and int(r.get("cat") or 0) > 0]
    new_count = sum(1 for r in repos if not r.get("lib") and r.get("status") != "local")
    lines = [
        "# 🗺️ Guía humana de BL_Alexandria",
        "",
        f"> {len(repos)} repos de IA y automatización explicados en español: qué hace cada uno, cuándo usarlo, cómo instalarlo y con qué combinarlo.",
        "",
        "[📚 Catálogo](../Catalogo.md) · [🔎 Explorador interactivo](../docs/index.html) · [🧪 Recetas](playbooks/README.md) · [⚖️ Comparativas](comparativas/README.md) · "
        f"[🆕 Novedades ({new_count})](novedades.md) · [📖 Guía completa](../Guia.md)",
        "",
        "## 🚀 ¿Qué quieres construir?",
        "",
        _start_here_table(cat, "human"),
        "",
        "## 📂 Categorías",
        "",
        _categories_table(cat, "human"),
        "",
        "## 🔥 Los 20 más populares",
        "",
        _top_table(cat, "human", 20),
        "",
        "## 🏷️ Cómo leer una ficha",
        "",
        "Cada [ficha](fichas/) responde, en este orden: **qué es**, **por qué destaca**, **cómo funciona**, **cómo se instala**, **casos de uso**, **¿es para ti?** (elígelo si / evítalo si), **con qué se combina** y **qué alternativas tiene**.",
        "",
        "- Ejecución: 🏠 local · ☁️ cloud/API · 🔀 híbrido",
        "- Rol: ⚙️ plataforma · 🧩 motor/runtime · 📚 librería/SDK · 🎨 skill/prompt · 📂 catálogo/recurso · 🖥️ app",
        "- Setup: 🟢 fácil (un comando) · 🟡 medio (servicios o credenciales) · 🔴 pesado (GPU o varios servicios)",
        "- ⭐ imprescindible de su sección · 📦 ya clonado en tu biblioteca · 🆕 sugerido nuevo",
        "",
        "## 📦 Decisiones de instalación",
        "",
        "- [✅ Usar ahora](usar-ahora.md): lo que la política del hub instala de entrada.",
        "- [⏳ Diferir](diferir.md): potente pero pesado; solo si es finalista.",
        "- [🔀 Alternativas y descartes](descartar.md): parejas que cumplen la misma función.",
        "",
        _footer(cat),
    ]
    _write(project_root / "human" / "README.md", "\n".join(lines))


def _start_here_table(cat: Catalog, base: str) -> str:
    rows = ["| Quiero… | Empieza por | Repos clave |", "|---|---|---|"]
    for item in cat.meta.get("start_here", []):
        if item.get("recipe"):
            recipe = next((rc for rc in cat.recipes if rc["id"] == item["recipe"]), None)
            target = f"[🧪 {recipe['title']}]({playbook_path(recipe['id'], base)})" if recipe else item["recipe"]
        else:
            num = int(item.get("cat") or 0)
            label = category_label(cat, num)
            path = category_path(cat, num, base)
            if item.get("sub"):
                sub_title = cat.sub_title(num, item["sub"])
                target = f"[{label} › {sub_title}]({path}#{gh_anchor(sub_title)})"
            else:
                target = f"[{label}]({path})"
        keys = ", ".join(repo_link(cat, rid, base) for rid in item.get("repos", []) if cat.get(rid))
        rows.append(f"| {md_cell(item.get('want'))} | {target} | {keys} |")
    return "\n".join(rows)


def _categories_table(cat: Catalog, base: str) -> str:
    rows = ["| # | Categoría | Repos | Imprescindibles |", "|---:|---|---:|---|"]
    for c in cat.public_categories():
        num = int(c["num"])
        picks = ", ".join(repo_link(cat, r["id"], base) for r in cat.picks(num)[:5])
        rows.append(f"| {num} | [{c.get('emoji', '')} {c['title']}]({category_path(cat, num, base)}) | {len(cat.in_category(num, include_aliases=False))} | {picks} |")
    return "\n".join(rows)


def _top_table(cat: Catalog, base: str, limit: int) -> str:
    repos = sorted(
        (r for r in cat.repos if isinstance(r.get("stars"), int) and int(r.get("cat") or 0) > 0 and not r.get("alias_of")),
        key=lambda r: -r["stars"],
    )[:limit]
    rows = ["| # | Repo | ⭐ | Categoría | Qué hace |", "|---:|---|---:|---|---|"]
    for index, repo in enumerate(repos, start=1):
        rows.append(f"| {index} | {repo_link(cat, repo['id'], base)} | {fmt_stars(repo['stars'])} | {category_label(cat, int(repo['cat']))} | {md_cell(repo.get('one'))} |")
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# README.md / AGENTS.md generated blocks
# ---------------------------------------------------------------------------

def _update_root_docs(project_root: Path, cat: Catalog) -> None:
    repos = [r for r in cat.repos if not r.get("alias_of")]
    local = sum(1 for r in repos if r.get("lib") and r.get("status") != "local")
    new = sum(1 for r in repos if not r.get("lib") and r.get("status") != "local")
    stats = (
        f"**{len(repos)} repos curados** · **{len(cat.public_categories())} categorías** · **{len(cat.recipes)} recetas** · "
        f"{local} ya en tu biblioteca local + {new} sugeridos nuevos"
        + (f" · estrellas de GitHub al {cat.checked_at}" if cat.checked_at else "")
    )
    recipes = "\n".join(
        f"- [{rc.get('emoji', '')} {rc['title']}]({playbook_path(rc['id'], 'root')}) — " + ", ".join(f"`{rid}`" for rid in rc.get("repos", []))
        for rc in cat.recipes
    ).replace("[ ", "[")
    blocks = {
        "STATS": stats,
        "START": _start_here_table(cat, "root"),
        "CATEGORIES": _categories_table(cat, "root"),
        "TOP": _top_table(cat, "root", 15),
        "RECIPES": recipes,
        "AGENT_CATEGORIES": _agent_categories_table(cat),
        "AGENT_TOOLS": _agent_tools_table(cat),
    }
    for name in ("README.md", "AGENTS.md"):
        path = project_root / name
        if path.exists():
            text = path.read_text(encoding="utf-8")
            updated = replace_blocks(text, blocks)
            if updated != text:
                path.write_text(updated, encoding="utf-8")


def replace_blocks(text: str, blocks: dict[str, str]) -> str:
    for name, body in blocks.items():
        pattern = re.compile(MARKER_RE.format(name=re.escape(name)), re.DOTALL)
        text = pattern.sub(lambda _m, n=name, b=body: f"<!-- BL:{n} -->\n{b}\n<!-- /BL:{n} -->", text)
    return text


def _agent_categories_table(cat: Catalog) -> str:
    rows = ["| # | Categoría | Repos | Subcategorías | Archivo |", "|---:|---|---:|---|---|"]
    for c in cat.public_categories():
        num = int(c["num"])
        subs = ", ".join(sub["title"] for sub in c.get("subs", []))
        rows.append(f"| {num} | {c.get('emoji', '')} {c['title']} | {len(cat.in_category(num, include_aliases=False))} | {md_cell(subs)} | `human/categorias/{category_filename(num, c['title'])}` |")
    return "\n".join(rows)


def _agent_tools_table(cat: Catalog) -> str:
    rows = ["| Herramienta | Repos específicos que le sirven |", "|---|---|"]
    for tool, info in cat.model_guidance.get("tools", {}).items():
        repos = info.get("best_fit_repos") or []
        cell = ", ".join(f"`{r}`" for r in repos) if repos else info.get("note", "—")
        if repos and info.get("note"):
            cell += f" — {info['note']}"
        rows.append(f"| **{info.get('label', tool)}** | {md_cell(cell)} |")
    return "\n".join(rows)


def counts_by_category(cat: Catalog) -> Counter[int]:
    return Counter(int(r.get("cat") or 0) for r in cat.repos if not r.get("alias_of"))
