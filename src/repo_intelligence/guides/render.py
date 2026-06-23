from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from repo_intelligence.core.io import read_json, read_yaml, write_json


ROOT_GUIDE_APPEND_START = "<!-- BL_ALEXANDRIA_AUTO_APPEND_START -->"
ROOT_GUIDE_APPEND_END = "<!-- BL_ALEXANDRIA_AUTO_APPEND_END -->"
SCAN_ALIASES = {"ui": "ui-shadcn"}
ROOT_GUIDE_CROSS_NOTE = '> Cada repo vive en **una** categoría; los cruces se resuelven con "Combina con". Excluidos por ser propios: `Binarias_Labs_C21`, `Binarias_Labs_Pruebas`.'


def render_all(project_root: Path) -> dict[str, int]:
    compact = read_json(project_root / "INDICE_IA.json", {})
    detail = read_json(project_root / "INDICE_IA.detalle.json", {})
    scan = read_json(project_root / "ai_index" / "REPOS.scan.json", {"repos": []})
    registry = read_yaml(project_root / "registry" / "repos.yaml", {"repos": []})

    repos = compact.get("repos", [])
    detail_repos: dict[str, dict[str, Any]] = detail.get("repos", {})
    scan_repos = scan.get("repos", [])
    guide_repos = _merge_scan_repos(repos, scan_repos)
    detected_repo_count = len(scan_repos) or len(guide_repos)
    local_by_id = _local_index(scan.get("repos", []), registry.get("repos", []))
    categories = compact.get("categories", [])
    recipes = compact.get("recipes", [])

    generated_at = datetime.now(timezone.utc).isoformat()
    _render_detail_index(project_root, generated_at, repos, detail_repos, local_by_id)
    _render_human_home(project_root, generated_at, repos, categories, recipes)
    _render_catalog(project_root, generated_at, repos, detail_repos, local_by_id)
    _render_root_guide(project_root, generated_at, guide_repos, detail_repos, categories, recipes, detected_repo_count)
    _render_sections(project_root, generated_at, repos, detail_repos)
    _render_categories(project_root, generated_at, repos, detail_repos, categories)
    _render_cards(project_root, generated_at, repos, detail_repos, local_by_id)
    comparisons = _render_comparisons(project_root, generated_at, repos, detail_repos)
    _render_playbooks(project_root, generated_at, recipes, detail_repos)

    return {
        "repos": detected_repo_count,
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


def _render_root_guide(
    project_root: Path,
    generated_at: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
    categories: list[dict[str, Any]],
    recipes: list[dict[str, Any]],
    detected_repo_count: int | None = None,
) -> None:
    by_cat: dict[int, list[dict[str, Any]]] = {}
    for repo in repos:
        by_cat.setdefault(int(repo.get("cat") or 0), []).append(repo)

    lines = [
        "# Guia de la biblioteca",
        "",
        f"Generado: {generated_at}",
        "",
        "Esta guia se regenera con `uv run repo-intelligence guide build`.",
        "",
        "## Lectura rapida",
        "",
        "- [Catalogo.md](Catalogo.md): tabla plana de repos.",
        "- [human/README.md](human/README.md): guia humana navegable.",
        "- [human/fichas/](human/fichas/): ficha individual por repo.",
        "- [human/comparativas/](human/comparativas/): alternativas y solapamientos.",
        "- [human/playbooks/](human/playbooks/): recetas end-to-end.",
        "- [ai_index/REPOS.scan.json](ai_index/REPOS.scan.json): indice compacto para IA.",
        "",
        "## Como usar esta guia",
        "",
        "1. Empieza por una categoria o playbook.",
        "2. Elige como maximo 3 repos finalistas por funcion.",
        "3. Abre solo las fichas de esos finalistas.",
        "4. Instala solo lo marcado como global, local del proyecto o Docker local.",
        "5. Deja los catalogos de skills como referencia salvo que una ficha indique lo contrario.",
        "",
        "## Playbooks",
        "",
    ]

    for recipe in recipes:
        lines.append(f"- [{recipe['title']}](human/playbooks/{_slug(recipe['id'])}.md): {recipe.get('goal') or ''}")

    lines.extend(["", "## Categorias", ""])
    for category in categories:
        num = int(category["num"])
        title = category["title"]
        category_file = f"human/categorias/{num:02d}-{_slug(title)}.md"
        category_repos = by_cat.get(num, [])
        lines.extend(
            [
                f"### {num}. [{title}]({category_file})",
                "",
                "| Repo | Decision | Instalacion | Resumen |",
                "|---|---|---|---|",
            ]
        )
        for repo in category_repos:
            repo_id = repo["id"]
            detail = detail_repos.get(repo_id, {})
            ficha = f"human/fichas/{_slug(repo_id)}.md"
            lines.append(
                "| [{name}]({ficha}) | {decision} | {install} | {desc} |".format(
                    name=_esc(repo.get("name") or repo_id),
                    ficha=ficha,
                    decision=_decision(repo),
                    install=_install_mode(repo),
                    desc=_esc(detail.get("desc") or repo.get("one") or ""),
                )
            )
        lines.append("")

    generated_text = "\n".join(lines) + "\n"
    _write_text(project_root / "human" / "guia-generada.md", generated_text)
    _update_rich_root_guide(project_root, generated_text, repos, detail_repos, generated_at, detected_repo_count=detected_repo_count)


def _update_rich_root_guide(
    project_root: Path,
    fallback_text: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
    generated_at: str,
    detected_repo_count: int | None = None,
) -> None:
    guide_path = project_root / "Guia.md"
    if not guide_path.exists():
        _write_text(guide_path, fallback_text)
        return

    current = guide_path.read_text(encoding="utf-8")
    if "# 🌌 Catálogo de Repositorios de IA & Automatización" not in current:
        _write_text(guide_path, fallback_text)
        return

    current = _strip_root_guide_appendix(current)
    current = _update_rich_guide_counts(current, repos, detail_repos, detected_repo_count=detected_repo_count)
    missing = _repos_missing_from_rich_guide(current, repos)
    if not missing:
        if current != guide_path.read_text(encoding="utf-8"):
            _write_text(guide_path, current)
        return

    appendix = _render_new_repo_appendix(missing, detail_repos, generated_at)
    if ROOT_GUIDE_APPEND_START in current and ROOT_GUIDE_APPEND_END in current:
        before = current.split(ROOT_GUIDE_APPEND_START, 1)[0].rstrip()
        after = current.split(ROOT_GUIDE_APPEND_END, 1)[1].lstrip()
        updated = f"{before}\n\n{appendix}\n\n{after}"
    else:
        base = re.sub(r"\n---\s*$", "", current.rstrip()).rstrip()
        updated = f"{base}\n\n---\n\n{appendix}\n"
    _write_text(guide_path, updated)


def _merge_scan_repos(compact_repos: list[dict[str, Any]], scan_repos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged = list(compact_repos)
    seen = {_norm(repo.get("id", "")) for repo in compact_repos}
    for repo in scan_repos:
        repo_id = _norm(repo.get("id", ""))
        if not repo_id or repo_id in seen:
            continue
        alias = SCAN_ALIASES.get(repo_id)
        if alias and _norm(alias) in seen:
            continue
        merged.append(
            {
                "id": repo.get("id"),
                "name": repo.get("name") or repo.get("id"),
                "cat": repo.get("cat") or 0,
                "role": repo.get("role") or "unknown",
                "exec": repo.get("exec") or "unknown",
                "setup": repo.get("setup") or "unknown",
                "tags": repo.get("tags", []),
                "one": repo.get("one") or "Repo detectado localmente, pendiente de ficha curada.",
                "install_mode": repo.get("install_mode") or "reference_only",
                "decision": repo.get("decision") or "reference",
                "alt": repo.get("alt", []),
            }
        )
        seen.add(repo_id)
    return merged


def _strip_root_guide_appendix(current: str) -> str:
    if ROOT_GUIDE_APPEND_START not in current or ROOT_GUIDE_APPEND_END not in current:
        return current
    before = current.split(ROOT_GUIDE_APPEND_START, 1)[0].rstrip()
    before = re.sub(r"\n---\s*$", "", before).rstrip()
    after = current.split(ROOT_GUIDE_APPEND_END, 1)[1].lstrip()
    if after:
        return f"{before}\n\n{after}"
    return before + "\n"


def _update_rich_guide_counts(
    current: str,
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
    detected_repo_count: int | None = None,
) -> str:
    total = detected_repo_count or len(repos)
    curated = len(detail_repos)
    current = re.sub(
        r"Catálogo operativo de los \*\*\d+ repositorios\*\* locales del workspace",
        f"Catálogo operativo de los **{total} repositorios** locales del workspace",
        current,
        count=1,
    )
    note = (
        f"> Estado actual: **{total} repos detectados** en la biblioteca local; "
        f"**{curated} repos curados** con ficha completa en esta guía. "
        "Los repos nuevos sin ficha curada se agregan al apéndice automático sin reescribir el cuerpo editorial."
    )
    marker = "<!-- BL_ALEXANDRIA_STATUS -->"
    status_block = f"{marker}\n{note}\n<!-- /BL_ALEXANDRIA_STATUS -->"
    if marker in current and "<!-- /BL_ALEXANDRIA_STATUS -->" in current:
        before = current.split(marker, 1)[0].rstrip()
        after = current.split("<!-- /BL_ALEXANDRIA_STATUS -->", 1)[1].lstrip()
        current = f"{before}\n\n{status_block}\n\n{after}"
    else:
        current = current.replace("## 📂 Mapa de categorías", f"{status_block}\n\n## 📂 Mapa de categorías", 1)
    return _ensure_root_guide_cross_note(current)


def _ensure_root_guide_cross_note(current: str) -> str:
    if ROOT_GUIDE_CROSS_NOTE in current:
        return current
    marker = "\n---\n\n## 🔗 Recetas de integración"
    if marker not in current:
        return current
    return current.replace(marker, f"\n{ROOT_GUIDE_CROSS_NOTE}\n{marker}", 1)


def _repos_missing_from_rich_guide(current: str, repos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    haystack = current.lower()
    missing: list[dict[str, Any]] = []
    for repo in repos:
        if not _repo_has_rich_entry(haystack, repo):
            missing.append(repo)
    return missing


def _repo_has_rich_entry(haystack: str, repo: dict[str, Any]) -> bool:
    repo_id = repo["id"]
    repo_name = repo.get("name") or repo_id
    headings = [line for line in haystack.splitlines() if line.startswith("### ")]
    slugs = {
        _slug(repo_id),
        _slug(repo_name),
        _slug(repo_id).replace("-", "_"),
        _slug(repo_name).replace("-", "_"),
    }
    for slug in slugs:
        if not slug:
            continue
        if f"human/fichas/{slug}.md" in haystack:
            return True
    candidates = {
        _norm(repo_id),
        _norm(str(repo_name)),
        _slug(repo_id),
        _slug(str(repo_name)),
    }
    for heading in headings:
        normalized = {_norm(heading).strip("# "), _slug(heading)}
        if any(candidate and any(value == candidate or value.endswith(f"-{candidate}") for value in normalized) for candidate in candidates):
            return True
    return False


def _render_new_repo_appendix(
    repos: list[dict[str, Any]],
    detail_repos: dict[str, dict[str, Any]],
    generated_at: str,
) -> str:
    lines = [
        ROOT_GUIDE_APPEND_START,
        "## 🆕 Repos detectados pendientes de curaduría",
        "",
        f"Generado: {generated_at}",
        "",
        "Esta sección se actualiza automáticamente para no destruir la guía curada. Integra manualmente estas fichas al cuerpo principal cuando quieras dejar la guía completamente editorial.",
        "",
        "| Repo | Categoria | Instalacion | Resumen |",
        "|---|---:|---|---|",
    ]
    for repo in repos:
        repo_id = repo["id"]
        detail = detail_repos.get(repo_id, {})
        lines.append(
            "| [{name}](human/fichas/{ficha}.md) | {cat} | {install} | {desc} |".format(
                name=_esc(repo.get("name") or repo_id),
                ficha=_slug(repo_id),
                cat=repo.get("cat", ""),
                install=_install_mode(repo),
                desc=_esc(detail.get("desc") or repo.get("one") or ""),
            )
        )
    lines.append(ROOT_GUIDE_APPEND_END)
    return "\n".join(lines)


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
