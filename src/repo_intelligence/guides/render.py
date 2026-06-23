from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from repo_intelligence.core.io import read_json, read_yaml, write_json


def render_all(project_root: Path) -> dict[str, int]:
    compact = read_json(project_root / "INDICE_IA.json", {})
    detail = read_json(project_root / "INDICE_IA.detalle.json", {})
    scan = read_json(project_root / "ai_index" / "REPOS.scan.json", {"repos": []})
    registry = read_yaml(project_root / "registry" / "repos.yaml", {"repos": []})

    repos = compact.get("repos", [])
    detail_repos: dict[str, dict[str, Any]] = detail.get("repos", {})
    local_by_id = _local_index(scan.get("repos", []), registry.get("repos", []))
    categories = compact.get("categories", [])
    recipes = compact.get("recipes", [])

    generated_at = datetime.now(timezone.utc).isoformat()
    _render_detail_index(project_root, generated_at, repos, detail_repos, local_by_id)
    _render_human_home(project_root, generated_at, repos, categories, recipes)
    _render_catalog(project_root, generated_at, repos, detail_repos, local_by_id)
    _render_sections(project_root, generated_at, repos, detail_repos)
    _render_categories(project_root, generated_at, repos, detail_repos, categories)
    _render_cards(project_root, generated_at, repos, detail_repos, local_by_id)
    comparisons = _render_comparisons(project_root, generated_at, repos, detail_repos)
    _render_playbooks(project_root, generated_at, recipes, detail_repos)

    return {
        "repos": len(repos),
        "categories": len(categories),
        "cards": len(detail_repos),
        "comparisons": comparisons,
        "playbooks": len(recipes),
    }


def _render_detail_index(
    project_root: Path,
    generated_at: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
    local_by_id: dict[str, dict[str, Any]],
) -> None:
    compact_by_id = {repo["id"]: repo for repo in repos}
    enriched: list[dict[str, Any]] = []
    for repo_id, detail in sorted(detail_repos.items()):
        compact = compact_by_id.get(repo_id, {})
        local = local_by_id.get(_norm(repo_id), {})
        enriched.append(
            {
                "id": repo_id,
                "name": detail.get("name") or compact.get("name") or repo_id,
                "cat": detail.get("cat") or compact.get("cat"),
                "role": compact.get("role"),
                "exec": compact.get("exec"),
                "setup": compact.get("setup"),
                "tags": compact.get("tags", []),
                "desc": detail.get("desc") or compact.get("one", ""),
                "stack": detail.get("stack"),
                "choose_if": detail.get("choose_if"),
                "avoid_if": detail.get("avoid_if"),
                "combines_with": detail.get("combines_with", []),
                "alternatives": detail.get("alternatives") or compact.get("alt", []),
                "install_mode": _install_mode(compact),
                "decision": _decision(compact),
                "local_path": local.get("path"),
                "repo_url": detail.get("repo"),
                "doc": detail.get("doc") or compact.get("doc"),
            }
        )
    write_json(
        project_root / "ai_index" / "REPOS.detail.json",
        {"generated_at": generated_at, "repos": enriched},
    )


def _render_human_home(
    project_root: Path,
    generated_at: str,
    repos: list[dict[str, Any]],
    categories: list[dict[str, Any]],
    recipes: list[dict[str, Any]],
) -> None:
    lines = [
        "# Guia humana",
        "",
        f"Generado: {generated_at}",
        "",
        "Esta carpeta contiene salidas navegables para entender la biblioteca sin abrir GitHub ni leer repos completos.",
        "",
        "## Archivos principales",
        "",
        "- [catalogo.md](catalogo.md): tabla humana de todos los repos del indice.",
        "- [usar-ahora.md](usar-ahora.md): piezas que sostienen este proyecto.",
        "- [diferir.md](diferir.md): herramientas potentes que no entran en la V1.",
        "- [descartar.md](descartar.md): duplicados o alternativas desplazadas.",
        "- [categorias/](categorias/): vista por categoria.",
        "- [fichas/](fichas/): una ficha por repo documentado.",
        "- [comparativas/](comparativas/): comparaciones directas entre alternativas.",
        "- [playbooks/](playbooks/): recetas end-to-end.",
        "",
        "## Resumen",
        "",
        f"- Repos documentados en indice: {len(repos)}",
        f"- Categorias: {len(categories)}",
        f"- Playbooks/recetas: {len(recipes)}",
        "",
        "## Lectura recomendada para Codex",
        "",
        "1. `ai_index/WINNERS.json`",
        "2. `ai_index/ROUTER.json`",
        "3. `ai_index/REPOS.scan.json`",
        "4. `ai_index/REPOS.detail.json` solo para finalistas",
    ]
    _write_text(project_root / "human" / "README.md", "\n".join(lines) + "\n")


def _render_catalog(
    project_root: Path,
    generated_at: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
    local_by_id: dict[str, dict[str, Any]],
) -> None:
    lines = [
        "# Catalogo generado",
        "",
        f"Generado: {generated_at}",
        "",
        "| Repo | Categoria | Rol | Instalacion | Decision | Resumen | Local |",
        "|---|---:|---|---|---|---|---|",
    ]
    for repo in repos:
        repo_id = repo["id"]
        detail = detail_repos.get(repo_id, {})
        local = "si" if _norm(repo_id) in local_by_id else "no"
        lines.append(
            "| {name} | {cat} | {role} | {install} | {decision} | {one} | {local} |".format(
                name=_esc(repo.get("name") or repo_id),
                cat=repo.get("cat", ""),
                role=repo.get("role", ""),
                install=_install_mode(repo),
                decision=_decision(repo),
                one=_esc(detail.get("desc") or repo.get("one") or ""),
                local=local,
            )
        )
    text = "\n".join(lines) + "\n"
    _write_text(project_root / "human" / "catalogo.md", text)
    _write_text(project_root / "Catalogo.md", text)


def _render_sections(
    project_root: Path,
    generated_at: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
) -> None:
    use_now = [repo for repo in repos if _decision(repo) == "use_now"]
    defer = [repo for repo in repos if _decision(repo) == "defer"]
    reference = [repo for repo in repos if _decision(repo) == "reference"]
    alternatives = [repo for repo in repos if repo.get("alt")]

    _write_repo_list(project_root / "human" / "usar-ahora.md", "Usar ahora", generated_at, use_now, detail_repos)
    _write_repo_list(project_root / "human" / "diferir.md", "Diferir", generated_at, defer, detail_repos)

    lines = [
        "# Descartar o dejar como alternativa",
        "",
        f"Generado: {generated_at}",
        "",
        "No se descartan por borrado. Se marcan como alternativas cuando duplican funcion con otro repo.",
        "",
    ]
    for repo in alternatives:
        lines.append(f"## {repo.get('name') or repo['id']}")
        lines.append("")
        lines.append(f"Alternativas declaradas: {', '.join(repo.get('alt', []))}.")
        lines.append("")
    lines.append("## Referencia solamente")
    lines.append("")
    for repo in reference[:80]:
        lines.append(f"- `{repo.get('id')}`: {_install_mode(repo)}")
    _write_text(project_root / "human" / "descartar.md", "\n".join(lines) + "\n")


def _render_categories(
    project_root: Path,
    generated_at: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
    categories: list[dict[str, Any]],
) -> None:
    by_cat: dict[int, list[dict[str, Any]]] = {}
    for repo in repos:
        by_cat.setdefault(int(repo.get("cat") or 0), []).append(repo)

    for category in categories:
        num = int(category["num"])
        title = category["title"]
        lines = [
            f"# {title}",
            "",
            f"Generado: {generated_at}",
            "",
            "| Repo | Rol | Instalacion | Decision | Uso real |",
            "|---|---|---|---|---|",
        ]
        for repo in by_cat.get(num, []):
            detail = detail_repos.get(repo["id"], {})
            lines.append(
                "| {name} | {role} | {install} | {decision} | {desc} |".format(
                    name=_esc(repo.get("name") or repo["id"]),
                    role=repo.get("role", ""),
                    install=_install_mode(repo),
                    decision=_decision(repo),
                    desc=_esc(detail.get("desc") or repo.get("one") or ""),
                )
            )
        filename = f"{num:02d}-{_slug(title)}.md"
        _write_text(project_root / "human" / "categorias" / filename, "\n".join(lines) + "\n")


def _render_cards(
    project_root: Path,
    generated_at: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
    local_by_id: dict[str, dict[str, Any]],
) -> None:
    compact_by_id = {repo["id"]: repo for repo in repos}
    for repo_id, detail in detail_repos.items():
        compact = compact_by_id.get(repo_id, {})
        local = local_by_id.get(_norm(repo_id), {})
        lines = [
            f"# {detail.get('name') or compact.get('name') or repo_id}",
            "",
            f"Generado: {generated_at}",
            "",
            "## Decision",
            "",
            _human_decision(compact),
            "",
            "## Para que sirve realmente",
            "",
            detail.get("desc") or compact.get("one") or "Sin descripcion en el indice.",
            "",
            "## Que problema resuelve",
            "",
            detail.get("choose_if") or "Pendiente de especificar con una decision de proyecto concreta.",
            "",
            "## Por que tiene valor",
            "",
            _value_line(compact, detail),
            "",
            "## Cuando usarlo",
            "",
            detail.get("choose_if") or "Cuando encaje con la funcion indicada por su categoria.",
            "",
            "## Cuando NO usarlo",
            "",
            detail.get("avoid_if") or "Cuando duplique una herramienta ya elegida o aumente complejidad sin ahorrar tokens.",
            "",
            "## Tipo de instalacion",
            "",
            _install_mode(compact),
            "",
            "## Instalacion detectada",
            "",
            "Repo local detectado: " + ("si" if local else "no"),
            "",
            "## Con que se combina",
            "",
            _bullet_list(detail.get("combines_with", [])),
            "",
            "## Contra que compite",
            "",
            _bullet_list(detail.get("alternatives") or compact.get("alt", [])),
            "",
            "## Riesgos",
            "",
            _risk_line(compact),
            "",
            "## Ideas profesionales",
            "",
            _ideas_line(compact, detail),
            "",
            "## Veredicto",
            "",
            _verdict(compact, detail),
            "",
        ]
        _write_text(project_root / "human" / "fichas" / f"{_slug(repo_id)}.md", "\n".join(lines))


def _render_comparisons(
    project_root: Path,
    generated_at: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
) -> int:
    compact_by_id = {repo["id"]: repo for repo in repos}
    compact_by_norm = {_norm(repo["id"]): repo for repo in repos}
    count = 0
    seen: set[tuple[str, str]] = set()
    for repo in repos:
        repo_id = repo["id"]
        for alt in repo.get("alt", []):
            pair = tuple(sorted((_norm(repo_id), _norm(alt))))
            if pair in seen:
                continue
            seen.add(pair)
            left = detail_repos.get(repo_id, {})
            right_repo = compact_by_id.get(alt) or compact_by_norm.get(_norm(alt), {})
            right = detail_repos.get(alt, {})
            lines = [
                f"# {repo_id} vs {alt}",
                "",
                f"Generado: {generated_at}",
                "",
                f"| Criterio | {_esc(left.get('name') or repo.get('name') or repo_id)} | {_esc(right.get('name') or right_repo.get('name') or alt)} |",
                "|---|---|---|",
                f"| Uso real | {_esc(left.get('desc') or repo.get('one') or '')} | {_esc(right.get('desc') or right_repo.get('one') or '')} |",
                f"| Elegir si | {_esc(left.get('choose_if') or '')} | {_esc(right.get('choose_if') or '')} |",
                f"| Evitar si | {_esc(left.get('avoid_if') or '')} | {_esc(right.get('avoid_if') or '')} |",
                f"| Instalacion | {_install_mode(repo)} | {_install_mode(right_repo)} |",
                "",
                "## Regla practica",
                "",
                f"Elige `{repo_id}` si su caso de uso encaja mejor ahora. Deja `{alt}` como alternativa, salvo que el proyecto necesite explicitamente ambos.",
            ]
            _write_text(project_root / "human" / "comparativas" / f"{_slug(repo_id)}-vs-{_slug(alt)}.md", "\n".join(lines) + "\n")
            count += 1
    return count


def _render_playbooks(
    project_root: Path,
    generated_at: str,
    recipes: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
) -> None:
    for recipe in recipes:
        lines = [
            f"# {recipe['title']}",
            "",
            f"Generado: {generated_at}",
            "",
            "## Objetivo",
            "",
            recipe.get("goal") or "",
            "",
            "## Stack sugerido",
            "",
        ]
        for repo_id in recipe.get("repos", []):
            detail = detail_repos.get(repo_id, {})
            lines.append(f"- `{repo_id}`: {detail.get('desc', 'Sin ficha detallada.')}")
        lines.extend(["", "## Como se conecta", "", recipe.get("how") or "Pendiente de especificar en el proyecto concreto.", ""])
        _write_text(project_root / "human" / "playbooks" / f"{_slug(recipe['id'])}.md", "\n".join(lines))


def _write_repo_list(path: Path, title: str, generated_at: str, repos: list[dict[str, Any]], detail_repos: dict[str, dict[str, Any]]) -> None:
    lines = ["# " + title, "", f"Generado: {generated_at}", ""]
    for repo in repos:
        detail = detail_repos.get(repo["id"], {})
        lines.append(f"## {repo.get('name') or repo['id']}")
        lines.append("")
        lines.append(f"Tipo: `{_install_mode(repo)}`")
        lines.append("")
        lines.append(detail.get("desc") or repo.get("one") or "")
        lines.append("")
    _write_text(path, "\n".join(lines) + "\n")


def _local_index(scan_repos: list[dict[str, Any]], registry_repos: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    local: dict[str, dict[str, Any]] = {}
    for repo in registry_repos:
        local[_norm(repo.get("id", ""))] = repo
        local[_norm(repo.get("name", ""))] = repo
    for repo in scan_repos:
        local.setdefault(_norm(repo.get("id", "")), repo)
        local.setdefault(_norm(repo.get("name", "")), repo)
    return {key: value for key, value in local.items() if key}


def _install_mode(repo: dict[str, Any]) -> str:
    repo_id = repo.get("id", "")
    role = repo.get("role")
    if repo_id in {"repomix", "gitnexus"}:
        return "global"
    if repo_id in {"markitdown", "crawl4ai"}:
        return "local_project"
    if role in {"skill", "directory"}:
        return "reference_only"
    if repo.get("setup") == "heavy":
        return "deferred"
    return "reference_only"


def _decision(repo: dict[str, Any]) -> str:
    mode = _install_mode(repo)
    if mode in {"global", "local_project"}:
        return "use_now"
    if mode == "deferred":
        return "defer"
    return "reference"


def _human_decision(repo: dict[str, Any]) -> str:
    return {
        "use_now": "USAR AHORA",
        "defer": "DIFERIR",
        "reference": "REFERENCIA",
    }.get(_decision(repo), "REFERENCIA")


def _risk_line(repo: dict[str, Any]) -> str:
    if repo.get("setup") == "heavy":
        return "Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro."
    if repo.get("role") in {"skill", "directory"}:
        return "Riesgo de ruido: leer y seleccionar, no instalar catalogos completos."
    return "Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta."


def _value_line(repo: dict[str, Any], detail: dict[str, Any]) -> str:
    tags = ", ".join(repo.get("tags", [])) or "sin tags"
    return f"Aporta valor en `{repo.get('role', 'repo')}` para {tags}. Stack declarado: {detail.get('stack') or 'no especificado'}."


def _ideas_line(repo: dict[str, Any], detail: dict[str, Any]) -> str:
    combines = detail.get("combines_with", [])
    if combines:
        return f"Combinar con {', '.join(combines)} cuando el flujo necesite mas de una pieza."
    return "Usarlo como finalista solo despues de comparar contra alternativas del mismo caso de uso."


def _verdict(repo: dict[str, Any], detail: dict[str, Any]) -> str:
    decision = _human_decision(repo).lower()
    reason = detail.get("choose_if") or repo.get("one") or "encaja con la categoria documentada"
    return f"Veredicto: {decision}. Tiene sentido si {reason}. No debe instalarse por inercia."


def _bullet_list(values: list[str]) -> str:
    if not values:
        return "- Ninguno declarado."
    return "\n".join(f"- `{value}`" for value in values)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _esc(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug or "item"


def _norm(value: str) -> str:
    return value.lower().replace("_", "-").replace(".", "-")
