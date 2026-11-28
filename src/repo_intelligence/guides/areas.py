"""Human navigation for practical areas, generated from the same web facets."""
from pathlib import Path

from repo_intelligence.core.access import API_LABELS, access_facts
from repo_intelligence.core.catalog import Catalog, md_cell, slug
from repo_intelligence.core.taxonomy import build_areas


def practical_table(areas: list[dict]) -> str:
    lines = ["| Área | Subcategorías | Repos únicos |", "|---|---|---:|"]
    for area in areas:
        names = ", ".join(t["title"] for t in area["topics"])
        lines.append(f'| [{area["title"]}](areas/{area["id"]}.md) | {md_cell(names)} | {area["count"]} |')
    return "\n".join(lines)


def render_area_guides(root: Path, catalog: Catalog) -> list[dict]:
    public = [r for r in catalog.repos if r["cat"] > 0 and not r.get("alias_of")]
    areas = build_areas(catalog.compact, public)
    if not areas:
        return []
    by_id = {r["id"]: r for r in public}
    folder = root / "human/areas"
    folder.mkdir(parents=True, exist_ok=True)
    work = [a for a in areas if a["kind"] == "work"]
    tools = [a for a in areas if a["kind"] == "tool"]
    lines = ["[Inicio](README.md) · [Explorador](../docs/index.html#/salas)", "", "# Categorías y subcategorías prácticas", "",
        f'{len(work)} áreas de trabajo y {len(tools)} colecciones de configuración, con {sum(len(a["topics"]) for a in areas)} subcategorías prácticas. '
        f'Es una capa de navegación distinta del índice técnico ({len(catalog.public_categories())} categorías y '
        f'{sum(len(c.get("subs", [])) for c in catalog.public_categories())} subcategorías técnicas); por eso los recuentos no coinciden.', "",
        "Elige un área, después una tarea y por último una ficha. Un repositorio puede servir en varias áreas; conserva una sola identidad y ficha. Los recuentos por área no se suman para obtener el total de proyectos.", "",
        "## Áreas de trabajo", "", practical_table(work), "", "## Configuración de asistentes", "", practical_table(tools), "",
        "Estas colecciones reúnen recursos para preparar el cliente. No convierten su suscripción en una API para cualquier aplicación.", "",
        "## Índice técnico", "", f"Las {len(catalog.public_categories())} secciones técnicas y sus rutas históricas se conservan al final del [mapa general](README.md). Las rutas por objetivo reúnen piezas cuando una tarea abarca varias áreas.", ""]
    (root / "human/areas.md").write_text("\n".join(lines), encoding="utf8")
    for area in areas:
        lines = ['[Áreas](../areas.md) · [Inicio](../README.md)', '', '# '+area['title'], '', area['description'], '',
            f'{area["count"]} repos únicos · {len(area["topics"])} subcategorías. [Ver en el explorador](../../docs/index.html#/area/{area["id"]}).', '']
        if area.get("guide"):
            lines += ['## Primera configuración, paso a paso', '']
            for n, step in enumerate(area['guide'], 1):
                lines += [f'{n}. **{step["title"]}.** {step["text"]}']
                if link := step.get("link"):
                    lines[-1] += f' [{link["label"]}]({link["url"]}).'
            lines += ['', f'[Fuente oficial del cliente]({area["official_url"]})', '', area['scope'], '']
        if area["id"] == "frontend":
            lines += ['## Qué usar para tu web', '', '[Elige una combinación para una página informativa, un panel o un chat con IA](../elegir-web.md).', '']
        else:
            lines += ['## Opciones para empezar', '', ', '.join(f'[{by_id[rid]["name"]}](../fichas/{slug(rid)}.md)' for rid in area['starters']), '',
                      'Son opciones para comparar. No es necesario instalar todas.', '']
        lines += ['## Subcategorías', '']
        for topic in area['topics']:
            lines += ['### '+topic['title'], '', topic['description'], '',
                f'[Explorar {topic["count"]} repos](../../docs/index.html#/explorar?area={area["id"]}&topic={topic["id"]})', '',
                '| Repositorio | Para qué sirve | API de IA |', '|---|---|---|']
            for rid in sorted(topic['repo_ids'], key=lambda rid:by_id[rid]['name'].lower()):
                repo = by_id[rid]
                lines.append(f'| [{md_cell(repo["name"])}](../fichas/{slug(rid)}.md) | {md_cell(repo["one"])} | {API_LABELS[access_facts(repo)["api"]]} |')
            lines += ['']
        if area.get('evidence'):
            lines += ['## Fuentes de compatibilidad', '']
            lines += [f'- [{by_id[e["repo_id"]]["name"]}]({e["source"]}), revisado el {e["checked_at"]}.' for e in area['evidence']]
            lines += ['']
        lines += ['La revisión de documentación no equivale a una instalación probada. Consulta cada ficha para acceso, coste, equipo y pasos de arranque.', '']
        (folder / (area['id']+'.md')).write_text('\n'.join(lines), encoding='utf8')
    return areas
