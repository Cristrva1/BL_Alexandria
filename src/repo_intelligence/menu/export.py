"""Portable AI menu exporter.

Generates a self-contained, token-optimized "menu" of the curated repository
library that can be copied into the root of a NEW project so an AI agent reads
it and decides which repos to install/use — without visiting the web or the
local READMEs.

Output package (default: ``menu_portable/``)::

    menu_portable/
        REPO_MENU.md            <- ENTRY POINT. AI reads this first.
        REPO_MENU_cats/         <- per-category detail (load only finalists)
            01-*.md ... 13-*.md
        REPO_MENU_DATA.json     <- machine-readable mirror (optional, for agents that prefer JSON)

The compact index lists every repo as one line. Detail files add full desc,
stack, derived install command (with confidence), choose_if/avoid_if,
combines_with and alternatives.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Install command derivation
# ---------------------------------------------------------------------------

# Confidence symbols rendered in the menu.
_OK = "ok"        # high confidence
_MAYBE = "verify"  # medium: name/command may need adjustment
_LOW = "clone"    # low: only clone is safe; check README

# PyPI / npm name normalization: suffixes that are not part of the package name.
_PKG_SUFFIXES = (
    "-python", "-js", "-ts", "-core", "-sdk", "-cli", "-server", "-api",
    "-lib", "-wrapper",
)


def _norm_pkg(name: str) -> str:
    n = name.lower()
    for suf in _PKG_SUFFIXES:
        if n.endswith(suf) and len(n) > len(suf):
            n = n[: -len(suf)]
    return n


def _has(stack: str, *needles: str) -> bool:
    s = stack.lower()
    return any(n in s for n in needles)


def derive_install(repo: dict) -> tuple[str, str, str]:
    """Return (command, confidence, note) for a repo record.

    ``repo`` is the merged view: compact fields (role/exec/setup) + detail
    fields (stack/repo). Missing fields are tolerated.
    """
    role = (repo.get("role") or "").lower()
    exec_ = (repo.get("exec") or "").lower()
    stack = repo.get("stack") or ""
    repo_url = repo.get("repo") or ""
    name = repo.get("name") or repo.get("id") or ""
    slug = repo_url.rstrip("/").split("/")[-1] if repo_url else name
    if slug.endswith(".git"):
        slug = slug[:-4]
    clone = f"git clone {repo_url}" if repo_url else f"git clone <{name}>"

    # --- Cloud / SaaS: no local install, just credentials -------------------
    if exec_ == "cloud" and role in ("platform", "app", "runtime"):
        return ("Crear cuenta / API key en el proveedor (no self-host).", _OK,
                "Servicio gestionado; no se clona.")

    # --- Skills / directories / catalogs: copy as reference -----------------
    if role in ("skill", "directory"):
        return (f"Copiar la skill a la carpeta de skills de tu agente "
                f"(p.ej. .claude/skills/{name}/). Si necesitas el código: {clone}",
                _OK, "Material de referencia/playbook; no es una dependencia runtime.")

    # --- Platforms / runtimes / apps: usually clone + run -------------------
    if role in ("platform", "runtime", "app"):
        if _has(stack, "docker"):
            return (f"{clone} && cd {slug} && docker compose up -d", _MAYBE,
                    "Requiere Docker; el compose puede variar — revisa docker-compose.yml.")
        if _has(stack, "python"):
            return (f"{clone} && cd {slug} && (uv sync || pip install -r requirements.txt)", _MAYBE,
                    "Proyecto Python; usa uv si hay pyproject.toml/uv.lock.")
        if _has(stack, "node", "typescript", "javascript", "fastify", "nest"):
            return (f"{clone} && cd {slug} && (pnpm install || npm install)", _MAYBE,
                    "Proyecto Node; usa pnpm si hay pnpm-lock.yaml.")
        return (f"{clone} (verificar README para build/run)", _LOW,
                "Stack no claro; revisa el README tras clonar.")

    # --- Libraries: prefer package manager ----------------------------------
    if role == "library":
        if _has(stack, "python"):
            pkg = _norm_pkg(name)
            return (f"pip install {pkg}   (o: uv add {pkg})", _MAYBE,
                    f"Nombre PyPI puede diferir de '{name}'; verifica en pypi.org.")
        if _has(stack, "node", "typescript", "javascript"):
            pkg = _norm_pkg(name)
            return (f"npm install {pkg}   (o: pnpm add {pkg})", _MAYBE,
                    f"Nombre npm puede diferir de '{name}'; verifica en npmjs.com.")
        return (f"{clone} (verificar README para install)", _LOW,
                "Stack no claro; revisa el README tras clonar.")

    # --- Fallback -----------------------------------------------------------
    return (f"{clone} (verificar README)", _LOW, "Tipo no reconocido.")


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

_ROLE_ICON = {
    "platform": "P", "runtime": "R", "library": "L",
    "skill": "S", "directory": "D", "app": "A",
}
_EXEC_ICON = {"local": "loc", "cloud": "cld", "hybrid": "hyb"}
_SETUP_ICON = {"easy": "E", "medium": "M", "heavy": "H"}
_CONF_ICON = {"ok": "+", "verify": "~", "clone": "?"}


def _icon(map_: dict, value: str | None) -> str:
    return map_.get((value or "").lower(), "-")


def _oneline(text: str, limit: int = 120) -> str:
    text = (text or "").strip().replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text[:limit]


def _best_desc(r: dict) -> str:
    """Pick the most meaningful short description available.

    Prefer the curated `desc` when it reads like a real sentence; fall back to
    `one`. Auto-drafted repos sometimes have junk `one` (just the name or '---').
    """
    desc = (r.get("desc") or "").strip()
    one = (r.get("one") or "").strip()
    name = (r.get("name") or r.get("id") or "").strip()

    def meaningful(t: str) -> bool:
        t = t.strip().strip("-").strip()
        if len(t) < 25:
            return False
        if t.lower() == name.lower():
            return False
        # README blobs usually start with the project name + "is a"/"is an".
        return True

    # `desc` is often longer/richer; prefer it when meaningful.
    if meaningful(desc):
        return desc
    if meaningful(one):
        return one
    # Whatever is longer between the two, else a placeholder.
    return desc or one or f"(ver ficha de {name})"


def _clean_field(text: str | None, name: str) -> str:
    """Return the field if meaningful, else a dash.

    Auto-drafted repos produce junk like 'quieres ---' or 'quieres <name>'.
    """
    t = (text or "").strip()
    if not t or t.strip("-").strip() == "":
        return "—"
    low = t.lower()
    # Auto-draft templates: 'quieres ---', 'quieres <name>', 'ya tienes una
    # herramienta equivalente...', 'no encaja con tu stack actual'
    if low.startswith("quieres ") and low.removeprefix("quieres ").strip("-").strip() in ("", name.lower()):
        return "—"
    if low.startswith("ya tienes una herramienta equivalente"):
        return "—"
    if low in (name.lower(), f"quieres {name.lower()}"):
        return "—"
    return t


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "cat"


def export_menu(project_root: Path, output_dir: Path | None = None) -> dict:
    """Build the portable menu package. Returns stats dict."""
    scan_path = project_root / "INDICE_IA.json"
    detail_path = project_root / "INDICE_IA.detalle.json"
    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    detail = json.loads(detail_path.read_text(encoding="utf-8"))
    detail_repos = detail.get("repos", {})

    categories = scan.get("categories", [])
    recipes = scan.get("recipes", [])
    model_guidance = scan.get("model_guidance", {})
    compact_repos = scan.get("repos", [])

    # Merge compact + detail into a unified view keyed by id.
    merged: dict[str, dict] = {}
    for r in compact_repos:
        rid = r.get("id") or r.get("name")
        merged[rid] = dict(r)
    for rid, d in detail_repos.items():
        if rid in merged:
            merged[rid].update({k: v for k, v in d.items() if v})
        else:
            merged[rid] = dict(d)
            merged[rid]["id"] = rid

    # Attach derived install.
    for rid, r in merged.items():
        cmd, conf, note = derive_install(r)
        r["_install"] = cmd
        r["_install_conf"] = conf
        r["_install_note"] = note

    out = output_dir or (project_root / "menu_portable")
    cats_dir = out / "REPO_MENU_cats"
    if out.exists():
        # Clear previous cats but keep the dir.
        for f in cats_dir.glob("*.md"):
            f.unlink()
    out.mkdir(parents=True, exist_ok=True)
    cats_dir.mkdir(parents=True, exist_ok=True)

    # Group repos by category number. cat=0 means uncategorized.
    by_cat: dict[int, list[dict]] = {}
    for rid, r in merged.items():
        by_cat.setdefault(int(r.get("cat") or 0), []).append(r)
    for c in by_cat.values():
        c.sort(key=lambda r: (r.get("id") or ""))

    cat_meta = {c["num"]: c for c in categories}

    _write_entry(out, scan, merged, by_cat, cat_meta, recipes, model_guidance)
    _write_category_files(cats_dir, by_cat, cat_meta)
    _write_json_mirror(out, scan, merged, by_cat, cat_meta, recipes, model_guidance)

    return {
        "output_dir": str(out),
        "repos": len(merged),
        "categories": len([c for c in by_cat if c != 0]),
        "files": 1 + len([c for c in by_cat if c != 0]) + 1,
    }


# ---------------------------------------------------------------------------
# Entry point file
# ---------------------------------------------------------------------------

def _write_entry(out: Path, scan: dict, merged: dict, by_cat: dict,
                 cat_meta: dict, recipes: list, model_guidance: dict) -> None:
    lines: list[str] = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    n = len(merged)

    lines.append("# REPO_MENU — Menú portable de la biblioteca de repositorios")
    lines.append("")
    lines.append(f"> Generado: {now} · {n} repos curados · Documento 100% para IA.")
    lines.append("> COPIA esta carpeta (`menu_portable/`) a la raíz de tu proyecto y")
    lines.append("> referencia este archivo desde tu AGENTS.md / system prompt.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## INSTRUCCIONES PARA EL AGENTE (léeme entero, soy corto)")
    lines.append("")
    lines.append("Eres un agente que debe elegir qué repositorios instalar/usar para un")
    lines.append("proyecto concreto. Tienes un menú curado de **%d repos** de IA y" % n)
    lines.append("automatización. Objeto: gastar MÍNIMOS tokens y NO visitar la web.")
    lines.append("")
    lines.append("PROTOCOLO (en orden):")
    lines.append("")
    lines.append("1. **No leas todo.** Este archivo basta para preseleccionar.")
    lines.append("2. **Filtra** candidatos por categoría, `role`, `exec`, `setup` y la")
    lines.append("   descripción `one` de cada línea del índice de abajo.")
    lines.append("3. **Desempata** con `alt`/alternativas: si ya elegiste un repo,")
    lines.append("   DESCARTA sus alternativas (cumplen la misma función, no dos).")
    lines.append("4. **Combina** con `recipes` si el proyecto es un flujo end-to-end.")
    lines.append("5. **Solo para finalistas (<8):** abre el archivo de su categoría en")
    lines.append("   `REPO_MENU_cats/NN-*.md` para ver desc completa, `choose_if`,")
    lines.append("   `avoid_if`, `combines_with` y el **comando de instalación** derivado.")
    lines.append("6. **Instalación:** cada repo trae un comando derivado marcado con")
    lines.append("   confianza: `+` seguro · `~` verificar nombre · `?` solo clone + README.")
    lines.append("")
    lines.append("REGLA CLAVE — herramienta de código ≠ modelo en ejecución:")
    lines.append("- El AGENTE/IDE con que CONSTRUYES (Claude Code, Antigravity, Codex…)")
    lines.append("  solo importa para repos `role=skill/directory` (catálogos de skills).")
    lines.append("- El LLM que tu APP llama EN EJECUCIÓN se configura por env vars;")
    lines.append("  la mayoría de repos runtime son AGNÓSTICOS al agente de código.")
    lines.append("")
    lines.append("LEYENDA de columnas del índice:")
    lines.append("`role`: P=plataforma R=runtime L=librería S=skill D=catálogo A=app")
    lines.append("`exec`: loc=local cld=cloud hyb=híbrido · `setup`: E=easy M=medium H=heavy")
    lines.append("`inst`: +=comando seguro ~=verificar ?=solo clone")
    lines.append("")
    lines.append("---")
    lines.append("")
    # Model guidance table
    tools = model_guidance.get("tools", {})
    if tools:
        lines.append("## Repos específicos por herramienta de código")
        lines.append("")
        lines.append("| Herramienta | Repos que le sirven |")
        lines.append("|---|---|")
        for tool, info in tools.items():
            repos = info.get("best_fit_repos", [])
            note = info.get("note", "")
            cell = ", ".join(f"`{r}`" for r in repos) if repos else (note or "—")
            lines.append(f"| {tool} | {cell} |")
        lines.append("")

    # Recipes
    if recipes:
        lines.append("## Recetas (stacks end-to-end listos)")
        lines.append("")
        lines.append("Si el proyecto es un PRODUCTO (no una pieza suelta), parte de una")
        lines.append("receta y ajusta. Cada receta lista los repos en orden de uso.")
        lines.append("")
        for rc in recipes:
            lines.append(f"### {rc.get('title','')}")
            lines.append(f"**Meta:** {rc.get('goal','')}  ")
            repos = rc.get("repos", [])
            lines.append("**Stack:** " + " → ".join(f"`{r}`" for r in repos))
            how = rc.get("how")
            if how:
                lines.append(f"**Cómo:** {how}")
            lines.append("")
        lines.append("---")
        lines.append("")

    # Compact index grouped by category
    lines.append("## ÍNDICE COMPACTO (1 línea por repo)")
    lines.append("")
    lines.append("Formato: `id` [role|exec|setup|inst] — descripción — alt:…")
    lines.append("")

    # Uncategorized first if any
    if 0 in by_cat and by_cat[0]:
        lines.append("### Sin categoría")
        lines.append("")
        for r in by_cat[0]:
            lines.append(_compact_line(r))
        lines.append("")

    for num in sorted(c for c in by_cat if c != 0):
        meta = cat_meta.get(num, {})
        title = meta.get("title", f"Categoría {num}")
        count = len(by_cat[num])
        slug = _slugify(title)
        lines.append(f"### {num}. {title} ({count})")
        lines.append(f"Detalle: `REPO_MENU_cats/{num:02d}-{slug}.md`")
        lines.append("")
        for r in by_cat[num]:
            lines.append(_compact_line(r))
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Cómo instalar (resumen de la lógica de derivación)")
    lines.append("")
    lines.append("- `role=skill/directory` → copiar a la carpeta de skills de tu agente.")
    lines.append("- `role=platform/runtime/app` + Docker → `git clone && docker compose up`.")
    lines.append("- `role=library` Python → `pip install <pkg>` / `uv add <pkg>` (verifica nombre).")
    lines.append("- `role=library` Node → `npm install <pkg>` (verifica nombre).")
    lines.append("- `exec=cloud` → servicio gestionado: API key, no se clona.")
    lines.append("- Marca `?` → solo `git clone` es seguro; revisa el README del repo.")
    lines.append("")
    lines.append("> Si un comando marcado `~` falla, busca el nombre real del paquete en")
    lines.append("> pypi.org / npmjs.com o clona el repo y lee su manifest.")
    lines.append("")

    (out / "REPO_MENU.md").write_text("\n".join(lines), encoding="utf-8")


def _compact_line(r: dict) -> str:
    rid = r.get("id") or r.get("name") or "?"
    role = _icon(_ROLE_ICON, r.get("role"))
    exec_ = _icon(_EXEC_ICON, r.get("exec"))
    setup = _icon(_SETUP_ICON, r.get("setup"))
    conf = _CONF_ICON.get(r.get("_install_conf", "clone"), "?")
    one = _oneline(_best_desc(r), 110)
    alt = r.get("alt") or r.get("alternatives") or []
    alt_s = f" — alt: {','.join(alt)}" if alt else ""
    return f"- `{rid}` [{role}|{exec_}|{setup}|{conf}] — {one}{alt_s}"


# ---------------------------------------------------------------------------
# Per-category detail files
# ---------------------------------------------------------------------------

def _write_category_files(cats_dir: Path, by_cat: dict, cat_meta: dict) -> None:
    for num in sorted(c for c in by_cat if c != 0):
        meta = cat_meta.get(num, {})
        title = meta.get("title", f"Categoría {num}")
        slug = _slugify(title)
        repos = by_cat[num]
        lines: list[str] = []
        lines.append(f"# {num}. {title} — detalle de repos")
        lines.append("")
        lines.append("> Abre este archivo SOLO si tienes finalistas en esta categoría.")
        lines.append("> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.")
        lines.append("")
        for r in repos:
            lines.append(_detail_block(r))
            lines.append("")
        (cats_dir / f"{num:02d}-{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def _detail_block(r: dict) -> str:
    rid = r.get("id") or r.get("name") or "?"
    role = r.get("role") or "?"
    exec_ = r.get("exec") or "?"
    setup = r.get("setup") or "?"
    conf = r.get("_install_conf", "clone")
    conf_icon = _CONF_ICON.get(conf, "?")
    desc = _oneline(_best_desc(r), 400)
    stack = r.get("stack") or "—"
    repo_url = r.get("repo") or "—"
    install = r.get("_install", "")
    note = r.get("_install_note", "")
    choose = _clean_field(r.get("choose_if"), rid)
    avoid = _clean_field(r.get("avoid_if"), rid)
    combines = r.get("combines_with") or []
    alt = r.get("alt") or r.get("alternatives") or []
    mcp = r.get("mcp")
    prov = r.get("prov") or []

    b: list[str] = []
    b.append(f"## `{rid}`")
    b.append(f"role={role} · exec={exec_} · setup={setup} · mcp={mcp} · prov={prov or '—'}")
    b.append("")
    b.append(f"**Qué es:** {desc}")
    b.append(f"**Stack:** {stack}")
    b.append(f"**Repo:** {repo_url}")
    b.append("")
    b.append(f"**Instalación** [{conf_icon}]: `{install}`")
    if note:
        b.append(f"_{note}_")
    b.append("")
    b.append(f"**Elige si:** {choose}")
    b.append(f"**Evita si:** {avoid}")
    if combines:
        b.append("**Combina con:** " + ", ".join(f"`{c}`" for c in combines))
    if alt:
        b.append("**Alternativas (elige una):** " + ", ".join(f"`{a}`" for a in alt))
    return "\n".join(b)


# ---------------------------------------------------------------------------
# JSON mirror (optional, for JSON-preferring agents)
# ---------------------------------------------------------------------------

def _write_json_mirror(out: Path, scan: dict, merged: dict, by_cat: dict,
                       cat_meta: dict, recipes: list, model_guidance: dict) -> None:
    data = {
        "purpose": "Menú portable de repos para que un agente elija sin visitar la web.",
        "how_to_use": [
            "Filtra por cat/role/exec/setup/one.",
            "Desempata con alt (descarta alternativas del repo elegido).",
            "Combina con recipes si es un flujo end-to-end.",
            "Solo finalistas: lee el bloque completo aquí o en REPO_MENU_cats/.",
            "Instalación: campo install + install_conf (ok/verify/clone).",
        ],
        "categories": [
            {"num": c["num"], "title": c["title"], "count": len(by_cat.get(c["num"], []))}
            for c in scan.get("categories", [])
        ],
        "recipes": recipes,
        "model_guidance": model_guidance,
        "repos": [
            {
                "id": r.get("id") or r.get("name"),
                "name": r.get("name"),
                "cat": r.get("cat"),
                "role": r.get("role"),
                "exec": r.get("exec"),
                "setup": r.get("setup"),
                "mcp": r.get("mcp"),
                "prov": r.get("prov") or [],
                "one": _oneline(_best_desc(r), 160),
                "desc": _oneline(_best_desc(r), 400),
                "stack": r.get("stack") or "",
                "repo": r.get("repo") or "",
                "install": r.get("_install"),
                "install_conf": r.get("_install_conf"),
                "install_note": r.get("_install_note"),
                "choose_if": _clean_field(r.get("choose_if"), r.get("id") or r.get("name") or ""),
                "avoid_if": _clean_field(r.get("avoid_if"), r.get("id") or r.get("name") or ""),
                "combines_with": r.get("combines_with") or [],
                "alt": r.get("alt") or r.get("alternatives") or [],
            }
            for r in sorted(merged.values(), key=lambda x: (x.get("cat") or 0, x.get("id") or ""))
        ],
    }
    (out / "REPO_MENU_DATA.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
