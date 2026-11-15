"""Portable AI menu exporter.

Generates a self-contained, token-optimized "menu" of the curated repository
library that can be copied into the root of a NEW project so an AI agent reads
it and decides which repos to install/use — without visiting the web or the
local READMEs.

Output package (default: ``menu_portable/``)::

    menu_portable/
        REPO_MENU.md            <- ENTRY POINT. AI reads this first.
        REPO_MENU_cats/         <- per-category detail (load only finalists)
            NN-*.md
        REPO_MENU_DATA.json     <- machine-readable mirror (optional, for agents that prefer JSON)

The compact index lists every repo as one line. Detail files add full desc,
stack, sourced entry command (when documented), choose_if/avoid_if,
combines_with and alternatives.
"""
from __future__ import annotations

import json
import re
from repo_intelligence.core.access import access_facts, access_routes, access_rows
from repo_intelligence.core.taxonomy import build_areas
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Documented entry commands
# ---------------------------------------------------------------------------

# Confidence symbols rendered in the menu.
_OK = "ok"        # command selected from the reviewed source
_LOW = "clone"    # legacy key retained for exports: consult the original guide


def derive_install(repo: dict) -> tuple[str, str, str]:
    """Return (command, confidence, note) for a repo record.

    ``repo`` is the merged view: compact fields (role/exec/setup) + detail
    fields (stack/repo). Missing fields are tolerated.
    """
    getting = repo.get("getting_started") or {}
    command = getting.get("command") or ""
    if command and getting.get("command_status") == "documented":
        return command, _OK, "Comando documentado en la fuente revisada; no equivale a una prueba de instalación."
    if getting.get("kind") == "reference" or repo.get("role") == "directory":
        return "Consultar el material original; elegir un ejemplo antes de instalar.", _LOW, "Una referencia no se instala como un servicio único."
    source = getting.get("source") or repo.get("repo") or repo.get("repo_url") or "el README original"
    return "Seguir la instalación original: " + source, _LOW, "No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo."


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
_TOOL_LABEL = {
    "claude-code": "Claude Code",
    "antigravity": "Antigravity",
    "codex": "Codex",
    "grok": "Grok",
    "deepseek": "Deepseek",
}


def _icon(map_: dict, value: str | None) -> str:
    return map_.get((value or "").lower(), "-")


def _oneline(text: str, limit: int = 120) -> str:
    text = (text or "").strip().replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text[:limit]


def _is_meaningful(text: str, name: str) -> bool:
    t = (text or "").strip().strip("-").strip()
    if len(t) < 25:
        return False
    return t.lower() != name.lower()


def _best_desc(r: dict) -> str:
    """Pick the most meaningful short description available.

    Prefer the curated `desc` when it reads like a real sentence; fall back to
    `one`. Auto-drafted repos sometimes have junk `one` (just the name or '---').
    """
    desc = (r.get("desc") or "").strip()
    one = (r.get("one") or "").strip()
    name = (r.get("name") or r.get("id") or "").strip()
    if _is_meaningful(desc, name):
        return desc
    if _is_meaningful(one, name):
        return one
    return desc or one or f"(ver ficha de {name})"


def _compact_desc(r: dict) -> str:
    """One-liner for the compact index: prefer scan `one`, matching AGENTS.md."""
    one = (r.get("one") or "").strip()
    name = (r.get("name") or r.get("id") or "").strip()
    if _is_meaningful(one, name):
        return one
    return _best_desc(r)


def _csv(values, limit: int | None = None) -> str:
    items = [str(v) for v in (values or []) if v]
    if limit is not None:
        items = items[:limit]
    return ",".join(items)


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
    areas=build_areas(scan,[r for r in merged.values() if int(r.get("cat") or 0)>0 and not r.get("alias_of")])
    if areas:
        lines=["# Categorías y subcategorías prácticas", "", "Mapa portable por tareas. Cada id conserva su ficha en REPO_MENU_DATA.json y su sección técnica en REPO_MENU_cats/.", "", "Los recuentos por área pueden solaparse: no equivalen a proyectos distintos.", ""]
        for area in areas:
            lines += ["## "+area["title"], "", area["description"], ""]
            for topic in area["topics"]:
                lines += ["### "+topic["title"], "", topic["description"], "", ", ".join("`"+rid+"`" for rid in topic["repo_ids"]), ""]
        (out/"REPO_AREAS.md").write_text("\n".join(lines),encoding="utf8")
        entry=out/"REPO_MENU.md"
        entry.write_text(entry.read_text(encoding="utf8").replace("\n", "\n\n[Explorar por áreas prácticas y configuración de asistentes](REPO_AREAS.md).\n",1),encoding="utf8")

    return {
        "output_dir": str(out),
        "repos": len(merged),
        "categories": len([c for c in by_cat if c != 0]),
        "files": 1 + len([c for c in by_cat if c != 0]) + 1 + bool(areas),
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
    lines.append("0. **Si el usuario ya describió un proyecto concreto**, parte de las")
    lines.append("   `recipes` que coincidan con el producto; no empieces por repos sueltos.")
    lines.append("1. **No leas todo.** Este archivo basta para preseleccionar.")
    lines.append("2. **Filtra** candidatos por `cat`, `tags`, `role`, `exec`, `setup`, `prov`")
    lines.append("   y palabras de `one` (resumen de una línea).")
    lines.append("3. **Desempata** con `alt`: si ya elegiste un repo, **descarta sus `alt`**")
    lines.append("   (cumplen la misma función, no necesitas dos).")
    lines.append("4. **Combina** con `recipes` si el proyecto es un flujo end-to-end.")
    lines.append("5. **Considera la herramienta** del usuario (Claude Code, Antigravity,")
    lines.append("   Codex, Grok, Deepseek) con la tabla de abajo y el campo opcional")
    lines.append("   `agent_tools`. Solo importa para repos `role=skill/directory`.")
    lines.append("6. **Solo para finalistas (<8):** abre `REPO_MENU_cats/NN-*.md` para")
    lines.append("   desc, `choose_if`, `avoid_if`, `combines_with` y el comando de")
    lines.append("   entrada documentada y la primera prueba propuesta.")
    lines.append("7. **Instalación:** comando marcado `+` documentado en la fuente · `~` por revisar ·")
    lines.append("   `?` solo clone + README.")
    lines.append("")
    lines.append("REGLA CLAVE — herramienta de código ≠ modelo en ejecución:")
    lines.append("- El AGENTE/IDE con que CONSTRUYES (Claude Code, Antigravity, Codex…)")
    lines.append("  solo importa para repos `role=skill/directory` (catálogos de skills).")
    lines.append("- El LLM que tu APP llama EN EJECUCIÓN es el campo `prov`; se configura")
    lines.append("  por env vars. La mayoría de repos runtime son AGNÓSTICOS al agente.")
    lines.append("")
    lines.append("LEYENDA de columnas del índice:")
    lines.append("`role`: P=plataforma R=runtime L=librería S=skill D=catálogo A=app")
    lines.append("`exec`: loc=local cld=cloud hyb=híbrido · `setup`: E=easy M=medium H=heavy")
    lines.append("`inst`: +=documentado ~=revisar ?=consultar fuente")
    lines.append("`tags` / `prov` / `tools` (`agent_tools`): solo si el repo los declara")
    lines.append("`alt`: repos sustitutos (elige uno)")
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
            label = _TOOL_LABEL.get(tool, tool)
            lines.append(f"| {label} | {cell} |")
        lines.append("")

    # Recipes
    if recipes:
        lines.append("## Recetas: flujos propuestos")
        lines.append("")
        lines.append("Si el proyecto es un PRODUCTO (no una pieza suelta), parte de una")
        lines.append("receta y ajusta. Empieza por su propuesta inicial; el recorrido completo incluye ampliaciones y otras rutas.")
        lines.append("")
        for rc in recipes:
            lines.append(f"### {rc.get('title','')}")
            lines.append(f"**Meta:** {rc.get('goal','')}")
            repos = rc.get("repos", [])
            lines.append("**Recursos del recorrido completo:** " + ", ".join(f"`{r}`" for r in repos))
            if rc.get('plan'):
                plan=rc['plan']
                lines += ['**Empieza con:** '+', '.join('`'+rid+'`' for rid in plan['minimum']),
                          '**Prepara:** '+plan['inputs'], '**Primera prueba propuesta:** '+plan['first_try']['action'],
                          '**Qué comprobar:** '+plan['first_try']['success'], plan['note']]
            how = rc.get("how")
            if how:
                lines.append(f"**Cómo:** {how}")
            lines.append("")
        lines.append("---")
        lines.append("")

    # Compact index grouped by category
    lines.append("## ÍNDICE COMPACTO (1 línea por repo)")
    lines.append("")
    lines.append("Formato: `id` [role|exec|setup|inst] — one — tags:… — prov:… — tools:… — alt:…")
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
    lines.append("## Cómo interpretar la instalación")
    lines.append("")
    lines.append("- Usa la entrada seleccionada del README o la guía original de cada ficha; no deduzcas paquetes por el nombre del repo.")
    lines.append("- Un bloque puede ser un comando de terminal, configuración, código o una instrucción dentro del agente: conserva su contexto.")
    lines.append("- Para skills y MCP sigue el método documentado para tu cliente; no copies la misma configuración a todos los agentes.")
    lines.append("- Revisa cuenta, API, servicios, licencia y modelos locales como decisiones separadas.")
    lines.append("- Marca `?` → revisa la instalación original; clonar no equivale a instalar.")
    lines.append("")
    lines.append("> La revisión es documental. Ni el comando ni la primera prueba se ejecutaron en los proyectos de terceros.")
    lines.append("")

    (out / "REPO_MENU.md").write_text("\n".join(lines), encoding="utf-8")


def _compact_line(r: dict) -> str:
    rid = r.get("id") or r.get("name") or "?"
    role = _icon(_ROLE_ICON, r.get("role"))
    exec_ = _icon(_EXEC_ICON, r.get("exec"))
    setup = _icon(_SETUP_ICON, r.get("setup"))
    conf = _CONF_ICON.get(r.get("_install_conf", "clone"), "?")
    one = _oneline(_compact_desc(r), 110)
    extras: list[str] = []
    tags = _csv(r.get("tags") or [], 8)
    if tags:
        extras.append(f"tags: {tags}")
    prov = _csv(r.get("prov") or [])
    if prov:
        extras.append(f"prov: {prov}")
    tools = _csv(r.get("agent_tools") or [])
    if tools:
        extras.append(f"tools: {tools}")
    alt = r.get("alt") or r.get("alternatives") or []
    if alt:
        extras.append("alt: " + ",".join(alt))
    extra_s = (" — " + " — ".join(extras)) if extras else ""
    return f"- `{rid}` [{role}|{exec_}|{setup}|{conf}] — {one}{extra_s}"


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
    tags = _csv(r.get("tags") or [])
    tools = _csv(r.get("agent_tools") or [])

    meta = f"role={role} · exec={exec_} · setup={setup} · mcp={mcp} · prov={_csv(prov) or '—'}"
    if tags:
        meta += f" · tags={tags}"
    if tools:
        meta += f" · tools={tools}"

    b: list[str] = []
    b.append(f"## `{rid}`")
    b.append(meta)
    b.append("")
    b.append(f"**Qué es:** {desc}")
    b.append(f"**Stack:** {stack}")
    b.append("**Acceso y costes:**")
    b.extend(f"- {title}: {body}" for title, body in access_rows(r))
    b.append(f"**Repo:** {repo_url}")
    b.append("")
    b.append(f"**Instalación** [{conf_icon}]:")
    if install:
        fence='`' * max(3,max((len(run) for run in re.findall(r'`+',install)),default=0)+1)
        b.extend(['',fence,'\n'.join(line if line.strip() else '' for line in install.splitlines()),fence,''])
    if note:
        b.append(f"_{note}_")
    b.append("")
    b.append(f"**Elige si:** {choose}")
    b.append(f"**Evita si:** {avoid}")
    if r.get('first_try'):
        b.append('**Primera prueba propuesta:** '+r['first_try']['action'])
        b.append('**Qué comprobar:** '+r['first_try']['success'])
        b.append('Revisión documental individual; instalación no ejecutada por Alexandría.')
    if combines:
        b.append("**Combina con:** " + ", ".join(f"`{c}`" for c in combines))
    if alt:
        b.append("**Alternativas (elige una):** " + ", ".join(f"`{a}`" for a in alt))
    return "\n".join(b)


# ---------------------------------------------------------------------------
# JSON mirror (optional, for JSON-preferring agents)
# ---------------------------------------------------------------------------

def _json_repo(r: dict) -> dict:
    item = {
        "id": r.get("id") or r.get("name"),
        "name": r.get("name"),
        "cat": r.get("cat"),
        "role": r.get("role"),
        "exec": r.get("exec"),
        "setup": r.get("setup"),
        "mcp": r.get("mcp"),
        "prov": r.get("prov") or [],
        "tags": r.get("tags") or [],
        "routes": access_routes(r),
        "access": access_facts(r),
        "getting_started": r.get("getting_started") or {},
        "first_try": r.get("first_try") or {},
        "practical_examples": r.get("practical_examples") or [],
        "editorial_review": r.get("editorial_review") or {},
        "one": _oneline(_compact_desc(r), 160),
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
    tools = r.get("agent_tools") or []
    if tools:
        item["agent_tools"] = tools
    return item


def _write_json_mirror(out: Path, scan: dict, merged: dict, by_cat: dict,
                       cat_meta: dict, recipes: list, model_guidance: dict) -> None:
    data = {
        "purpose": "Menú portable de repos para que un agente elija sin visitar la web.",
        "how_to_use": [
            "Filtra por cat/tags/role/exec/setup/prov/one.",
            "Desempata con alt (descarta alternativas del repo elegido).",
            "Combina con recipes si es un flujo end-to-end.",
            "Considera la herramienta del usuario con model_guidance y agent_tools (solo skill/directory).",
            "Solo finalistas: lee el bloque completo aquí o en REPO_MENU_cats/.",
            "Instalación: campo install + install_conf (ok/verify/clone).",
        ],
        "categories": [
            {"num": c["num"], "title": c["title"], "count": len(by_cat.get(c["num"], []))}
            for c in scan.get("categories", [])
        ],
        "recipes": recipes,
        "areas": build_areas(scan,[r for r in merged.values() if int(r.get("cat") or 0)>0 and not r.get("alias_of")]),
        "model_guidance": model_guidance,
        "repos": [
            _json_repo(r)
            for r in sorted(merged.values(), key=lambda x: (x.get("cat") or 0, x.get("id") or ""))
        ],
    }
    (out / "REPO_MENU_DATA.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
