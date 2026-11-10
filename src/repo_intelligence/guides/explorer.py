"""Interactive, self-contained explorer of the library (docs/index.html).

The page embeds the catalog as JSON and filters it client-side: search, category
and subcategory, role, setup, "only picks", local/new, and sorting by stars,
name or recent activity. It works offline (double-click the file), on GitHub
Pages (Settings → Pages → branch main, folder /docs) and as a preview artifact.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from repo_intelligence.core.catalog import Catalog, fmt_stars, slug

TITLE = "Explorador BL_Alexandria"


def explorer_data(cat: Catalog) -> dict[str, Any]:
    repo_url = (cat.meta.get("repo_url") or "").rstrip("/")
    categories = []
    for c in cat.public_categories():
        num = int(c["num"])
        categories.append(
            {
                "num": num,
                "title": c["title"],
                "emoji": c.get("emoji", ""),
                "desc": c.get("desc", ""),
                "subs": [{"key": s["key"], "title": s["title"]} for s in c.get("subs", [])],
            }
        )
    repos = []
    for repo in cat.repos:
        if repo.get("alias_of") or int(repo.get("cat") or 0) == 0:
            continue
        ficha = f"human/fichas/{slug(repo['id'])}.md"
        repos.append(
            {
                "id": repo["id"],
                "name": repo.get("name") or repo["id"],
                "emoji": repo.get("emoji") or "",
                "cat": int(repo.get("cat") or 0),
                "sub": repo.get("sub") or "",
                "role": repo.get("role") or "",
                "exec": repo.get("exec") or "",
                "setup": repo.get("setup") or "",
                "mcp": bool(repo.get("mcp")),
                "stars": repo.get("stars") if isinstance(repo.get("stars"), int) else None,
                "lib": bool(repo.get("lib")),
                "pick": bool(repo.get("pick")),
                "status": repo.get("status") or "",
                "one": repo.get("one") or "",
                "desc": repo.get("desc") or "",
                "why": repo.get("why") or "",
                "install": repo.get("install") or "",
                "cases": repo.get("cases") or [],
                "choose": repo.get("choose_if") or "",
                "avoid": repo.get("avoid_if") or "",
                "limits": repo.get("limits") or "",
                "stack": repo.get("stack") or "",
                "models": repo.get("models") or "",
                "tags": repo.get("tags") or [],
                "combines": [c for c in repo.get("combines_with", []) if cat.get(c)],
                "alts": [a for a in repo.get("alternatives", []) if cat.get(a)],
                "url": repo.get("repo_url") or "",
                "home": repo.get("homepage") or "",
                "license": repo.get("license") or "",
                "lang": repo.get("lang") or "",
                "updated": repo.get("updated") or "",
                "ficha": f"{repo_url}/blob/HEAD/{ficha}" if repo_url else f"../{ficha}",
            }
        )
    recipes = [
        {
            "id": rc["id"],
            "title": rc["title"],
            "emoji": rc.get("emoji", ""),
            "goal": rc.get("goal", ""),
            "repos": [r for r in rc.get("repos", []) if cat.get(r)],
            "page": f"{repo_url}/blob/HEAD/human/playbooks/{slug(rc['id'])}.md" if repo_url else f"../human/playbooks/{slug(rc['id'])}.md",
        }
        for rc in cat.recipes
    ]
    total_stars = sum(r["stars"] or 0 for r in repos)
    return {
        "checked": cat.checked_at,
        "total_stars": fmt_stars(total_stars),
        "categories": categories,
        "recipes": recipes,
        "repos": repos,
    }


def explorer_fragment(cat: Catalog) -> str:
    """Page content without <html>/<head>/<body> (used for artifact previews)."""
    data = json.dumps(explorer_data(cat), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return _TEMPLATE.replace("__TITLE__", TITLE).replace("__DATA__", data)


def explorer_document(cat: Catalog) -> str:
    fragment = explorer_fragment(cat)
    return (
        "<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        "<meta name=\"description\" content=\"Explorador interactivo de la biblioteca curada de repos de IA y automatización BL_Alexandria.\">\n"
        "</head>\n<body>\n"
        f"{fragment}\n</body>\n</html>\n"
    )


def render_explorer(project_root: Path, cat: Catalog) -> Path:
    path = Path(project_root) / "docs" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    text = explorer_document(cat)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")
    return path


_TEMPLATE = r"""<title>__TITLE__</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
/* Layout: fichero de biblioteca — cabecera con buscador, índice de categorías a la izquierda,
   rejilla de fichas con signatura (categoría.subcategoría) y estrellas; en móvil, todo en una columna. */
:root {
  --bg: #f3f5f8;
  --surface: #ffffff;
  --surface-2: #e9edf3;
  --ink: #131a27;
  --muted: #586378;
  --line: #d7dde6;
  --accent: #2a47ad;
  --accent-soft: #e3e8f8;
  --accent-ink: #ffffff;
  --gold: #9a610e;
  --new: #1b7356;
  --new-soft: #ddf1e8;
  --warn: #9c4317;
  --warn-soft: #f8e6dc;
  --shadow: 0 1px 2px rgba(19, 26, 39, .06), 0 4px 14px rgba(19, 26, 39, .05);
  --font-display: "Bricolage Grotesque", "Avenir Next", "Segoe UI", system-ui, sans-serif;
  --font-body: "IBM Plex Sans", "Segoe UI", system-ui, -apple-system, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  --radius: 10px;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0c1018; --surface: #141a25; --surface-2: #1b2331; --ink: #e6eaf2; --muted: #9ba6b9;
    --line: #283244; --accent: #8fa7ff; --accent-soft: #1d2848; --accent-ink: #0c1018; --gold: #e2ad57;
    --new: #5fcca3; --new-soft: #12302a; --warn: #f19a70; --warn-soft: #3a2218;
    --shadow: 0 1px 2px rgba(0, 0, 0, .4), 0 6px 18px rgba(0, 0, 0, .25);
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #0c1018; --surface: #141a25; --surface-2: #1b2331; --ink: #e6eaf2; --muted: #9ba6b9;
  --line: #283244; --accent: #8fa7ff; --accent-soft: #1d2848; --accent-ink: #0c1018; --gold: #e2ad57;
  --new: #5fcca3; --new-soft: #12302a; --warn: #f19a70; --warn-soft: #3a2218;
  --shadow: 0 1px 2px rgba(0, 0, 0, .4), 0 6px 18px rgba(0, 0, 0, .25);
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0; background: var(--bg); color: var(--ink); font: 15px/1.5 var(--font-body);
}
a { color: var(--accent); }
button, input, select { font: inherit; color: inherit; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.wrap {
  max-width: 1320px; margin: 0 auto;
  padding-left: max(16px, env(safe-area-inset-left, 0px));
  padding-right: max(16px, env(safe-area-inset-right, 0px));
}
header.top { padding-block: 28px 18px; border-bottom: 1px solid var(--line); background: var(--surface); }
.brand { display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px 14px; }
.brand h1 { font: 700 clamp(1.6rem, 1.2rem + 1.8vw, 2.4rem)/1.1 var(--font-display); margin: 0; letter-spacing: -.01em; text-wrap: balance; }
.brand .sig { font: 500 .78rem/1 var(--font-mono); color: var(--muted); letter-spacing: .06em; text-transform: uppercase; }
.lede { margin: 8px 0 18px; color: var(--muted); max-width: 70ch; }
.stats { display: flex; flex-wrap: wrap; gap: 8px 22px; margin: 0 0 18px; padding: 0; list-style: none; font-variant-numeric: tabular-nums; }
.stats b { font: 600 1.15rem/1 var(--font-display); color: var(--ink); margin-right: 4px; }
.stats li { color: var(--muted); font-size: .9rem; }
.searchbar { display: flex; gap: 10px; flex-wrap: wrap; }
.searchbar input[type=search] {
  flex: 1 1 320px; min-width: 0; padding: 12px 14px; border-radius: var(--radius);
  border: 1px solid var(--line); background: var(--bg); font-size: 1rem;
}
.tabs { display: flex; gap: 4px; background: var(--surface-2); padding: 4px; border-radius: var(--radius); }
.tabs a { text-decoration: none; color: var(--muted); padding: 8px 14px; border-radius: 7px; font-weight: 500; }
.tabs a[aria-current="page"] { background: var(--surface); color: var(--ink); box-shadow: var(--shadow); }
main { padding-block: 22px 48px; }
.layout { display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 26px; align-items: start; }
nav.cats { position: sticky; top: calc(env(safe-area-inset-top, 0px) + 12px); display: grid; gap: 2px; }
nav.cats h2, .filters h2 { font: 500 .72rem/1 var(--font-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 0 0 8px; }
.cat-btn {
  display: grid; grid-template-columns: 1.6em minmax(0, 1fr) auto; gap: 6px; align-items: center; text-align: left;
  border: 0; background: none; padding: 7px 8px; border-radius: 8px; cursor: pointer; color: var(--ink);
}
.cat-btn:hover { background: var(--surface-2); }
.cat-btn[aria-pressed="true"] { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
.cat-btn .n { font: 400 .8rem var(--font-mono); color: var(--muted); font-variant-numeric: tabular-nums; }
.filters { display: flex; flex-wrap: wrap; gap: 10px 16px; align-items: center; margin-bottom: 14px; }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip {
  border: 1px solid var(--line); background: var(--surface); padding: 5px 11px; border-radius: 999px; cursor: pointer;
  font-size: .85rem; color: var(--ink);
}
.chip[aria-pressed="true"] { border-color: var(--accent); background: var(--accent-soft); color: var(--accent); font-weight: 600; }
.ctl { display: flex; align-items: center; gap: 6px; color: var(--muted); font-size: .85rem; }
.ctl select { padding: 6px 8px; border-radius: 8px; border: 1px solid var(--line); background: var(--surface); }
.ctl input { accent-color: var(--accent); }
.subchips { margin: -4px 0 16px; }
.catintro { margin: 0 0 14px; color: var(--muted); max-width: 80ch; }
.catintro strong { color: var(--ink); font: 600 1.05rem var(--font-display); margin-right: 6px; }
.count { font: 400 .85rem var(--font-mono); color: var(--muted); margin: 0 0 12px; font-variant-numeric: tabular-nums; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(285px, 1fr)); gap: 14px; }
.card {
  display: flex; flex-direction: column; gap: 10px; min-width: 0; background: var(--surface);
  border: 1px solid var(--line); border-radius: var(--radius); padding: 14px 15px 12px; box-shadow: var(--shadow);
}
.meta { display: flex; justify-content: space-between; gap: 8px; font: 400 .74rem/1.2 var(--font-mono); color: var(--muted); letter-spacing: .02em; }
.meta .callno { min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.dlg-head .meta { padding-right: 40px; }
.stars { color: var(--gold); font: 500 .8rem var(--font-mono); white-space: nowrap; font-variant-numeric: tabular-nums; }
.card h3 { margin: 0; font: 600 1.12rem/1.25 var(--font-display); overflow-wrap: anywhere; }
.card h3 button { all: unset; cursor: pointer; }
.card h3 button:hover { text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }
.card h3 button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px; }
.card p.one { margin: 0; color: var(--ink); font-size: .92rem; }
.badges { display: flex; flex-wrap: wrap; gap: 5px; }
.badge { font-size: .74rem; padding: 2px 8px; border-radius: 999px; background: var(--surface-2); color: var(--muted); white-space: nowrap; }
.badge.pick { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
.badge.new { background: var(--new-soft); color: var(--new); font-weight: 600; }
.badge.warn { background: var(--warn-soft); color: var(--warn); font-weight: 600; }
.cmd { display: flex; align-items: center; gap: 6px; background: var(--bg); border: 1px solid var(--line); border-radius: 8px; padding: 6px 6px 6px 10px; min-width: 0; }
.cmd code { font: 400 .78rem/1.4 var(--font-mono); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0; flex: 1; }
.copy { border: 0; background: var(--surface-2); border-radius: 6px; padding: 3px 8px; cursor: pointer; font-size: .74rem; color: var(--muted); flex: none; }
.copy:hover { color: var(--accent); }
.card .links { display: flex; gap: 14px; font-size: .84rem; margin-top: auto; padding-top: 2px; }
.empty { padding: 40px 18px; text-align: center; color: var(--muted); border: 1px dashed var(--line); border-radius: var(--radius); }
.empty button { margin-top: 10px; }
.btn { border: 1px solid var(--accent); background: var(--accent); color: var(--accent-ink); padding: 8px 14px; border-radius: 8px; cursor: pointer; font-weight: 600; }
.recipes { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 14px; }
.recipe { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); padding: 16px; display: grid; gap: 10px; min-width: 0; }
.recipe h3 { margin: 0; font: 600 1.15rem/1.25 var(--font-display); }
.recipe p { margin: 0; color: var(--muted); }
.stack { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.stack .arrow { color: var(--muted); font-size: .8rem; }
dialog {
  width: min(720px, calc(100vw - 24px)); max-height: min(88vh, 900px); border: 1px solid var(--line); border-radius: 14px;
  padding: 0; background: var(--surface); color: var(--ink); box-shadow: 0 20px 60px rgba(0, 0, 0, .3);
}
dialog::backdrop { background: rgba(10, 14, 22, .45); }
.dlg-head { position: sticky; top: 0; background: var(--surface); padding: 18px 20px 12px; border-bottom: 1px solid var(--line); display: grid; gap: 6px; }
.dlg-head h2 { margin: 0; font: 700 1.5rem/1.15 var(--font-display); padding-right: 40px; overflow-wrap: anywhere; }
.dlg-close { position: absolute; top: 14px; right: 14px; border: 0; background: var(--surface-2); width: 32px; height: 32px; border-radius: 50%; cursor: pointer; font-size: 1.1rem; color: var(--ink); }
.dlg-body { padding: 16px 20px 22px; display: grid; gap: 14px; }
.dlg-body h4 { margin: 0 0 4px; font: 500 .74rem/1 var(--font-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }
.dlg-body p { margin: 0; max-width: 68ch; }
.dlg-body ul { margin: 0; padding-left: 1.1em; }
.fit { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.fit > div { background: var(--bg); border: 1px solid var(--line); border-radius: 8px; padding: 10px 12px; min-width: 0; }
.related { display: flex; flex-wrap: wrap; gap: 6px; }
.related button { border: 1px solid var(--line); background: var(--bg); border-radius: 999px; padding: 4px 10px; cursor: pointer; font-size: .84rem; color: var(--ink); }
.related button:hover { border-color: var(--accent); color: var(--accent); }
.facts { display: grid; grid-template-columns: max-content minmax(0, 1fr); gap: 4px 14px; font-size: .9rem; margin: 0; }
.facts dt { color: var(--muted); }
.facts dd { margin: 0; overflow-wrap: anywhere; }
footer { padding-block: 20px 36px; color: var(--muted); font-size: .82rem; border-top: 1px solid var(--line); }
@media (max-width: 860px) {
  .layout { grid-template-columns: minmax(0, 1fr); }
  nav.cats { position: static; display: flex; overflow-x: auto; gap: 6px; padding-bottom: 6px; }
  nav.cats h2 { display: none; }
  .cat-btn { grid-template-columns: auto auto auto; white-space: nowrap; border: 1px solid var(--line); background: var(--surface); }
  .fit { grid-template-columns: minmax(0, 1fr); }
}
@media (prefers-reduced-motion: no-preference) {
  .card { transition: border-color .15s ease, transform .15s ease; }
  .card:hover { border-color: var(--accent); transform: translateY(-1px); }
}
</style>

<header class="top">
  <div class="wrap">
    <div class="brand">
      <h1>Explorador BL_Alexandria</h1>
      <span class="sig" id="sig"></span>
    </div>
    <p class="lede">Busca entre los repos de IA y automatización de la biblioteca: qué hace cada uno, cuándo elegirlo, cómo instalarlo y con qué combinarlo. Cada ficha lleva su signatura (categoría.subcategoría) y sus estrellas de GitHub.</p>
    <ul class="stats" id="stats"></ul>
    <div class="searchbar">
      <input type="search" id="q" placeholder="Busca por nombre, función o etiqueta: whatsapp, rag, tts, mcp…" aria-label="Buscar repos" autocomplete="off">
      <nav class="tabs" aria-label="Vistas">
        <a href="#repos" id="tab-repos">Repos</a>
        <a href="#recetas" id="tab-recetas">Recetas</a>
      </nav>
    </div>
  </div>
</header>

<main class="wrap">
  <section id="view-repos" class="layout">
    <nav class="cats" id="cats" aria-label="Categorías"></nav>
    <div>
      <div class="filters">
        <div class="chips" role="group" aria-label="Biblioteca">
          <button class="chip" id="f-all" aria-pressed="true" type="button">Todos</button>
          <button class="chip" id="f-lib" aria-pressed="false" type="button">📦 En mi biblioteca</button>
          <button class="chip" id="f-new" aria-pressed="false" type="button">🆕 Sugeridos</button>
        </div>
        <label class="ctl"><input type="checkbox" id="f-pick"> Solo imprescindibles</label>
        <label class="ctl">Setup
          <select id="f-setup"><option value="">todos</option><option value="easy">🟢 fácil</option><option value="medium">🟡 medio</option><option value="heavy">🔴 pesado</option></select>
        </label>
        <label class="ctl">Rol
          <select id="f-role"><option value="">todos</option><option value="platform">⚙️ plataforma</option><option value="runtime">🧩 motor</option><option value="library">📚 librería</option><option value="skill">🎨 skill</option><option value="directory">📂 catálogo</option><option value="app">🖥️ app</option></select>
        </label>
        <label class="ctl">Orden
          <select id="f-sort"><option value="stars">⭐ estrellas</option><option value="name">nombre</option><option value="recent">actividad reciente</option></select>
        </label>
      </div>
      <p class="catintro" id="catintro" hidden></p>
      <div class="chips subchips" id="subs" role="group" aria-label="Subcategorías" hidden></div>
      <p class="count" id="count" aria-live="polite"></p>
      <div class="grid" id="grid"></div>
      <div class="empty" id="empty" hidden>
        <p id="empty-text">No hay repos que coincidan con esos filtros.</p>
        <button class="btn" id="reset" type="button">Quitar filtros</button>
      </div>
    </div>
  </section>
  <section id="view-recetas" hidden>
    <p class="catintro">Stacks end-to-end ya pensados. Pulsa un repo para ver su ficha.</p>
    <div class="recipes" id="recipes"></div>
  </section>
</main>

<footer>
  <div class="wrap" id="foot"></div>
</footer>

<dialog id="dlg" aria-labelledby="dlg-title">
  <div class="dlg-head">
    <button class="dlg-close" id="dlg-close" type="button" aria-label="Cerrar">×</button>
    <div class="card-meta meta" id="dlg-meta"></div>
    <h2 id="dlg-title"></h2>
    <div class="badges" id="dlg-badges"></div>
  </div>
  <div class="dlg-body" id="dlg-body"></div>
</dialog>

<script type="application/json" id="data">__DATA__</script>
<script>
(function () {
  "use strict";
  var DATA = JSON.parse(document.getElementById("data").textContent);
  var REPOS = DATA.repos, CATS = DATA.categories;
  var byId = {}; REPOS.forEach(function (r) { byId[r.id] = r; });
  var catByNum = {}; CATS.forEach(function (c) { catByNum[c.num] = c; });
  var ROLE = { platform: "⚙️ plataforma", runtime: "🧩 motor", library: "📚 librería", skill: "🎨 skill", directory: "📂 catálogo", app: "🖥️ app" };
  var SETUP = { easy: "🟢 fácil", medium: "🟡 medio", heavy: "🔴 pesado" };
  var EXEC = { local: "🏠 local", cloud: "☁️ cloud/API", hybrid: "🔀 híbrido" };
  var state = { q: "", cat: 0, sub: "", lib: "all", pick: false, setup: "", role: "", sort: "stars" };
  try { var saved = JSON.parse(localStorage.getItem("blx-filters") || "null"); if (saved && typeof saved === "object") { state.sort = saved.sort || state.sort; } } catch (e) {}

  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function fmt(n) { if (n == null) return "—"; if (n >= 1e6) return (n / 1e6).toFixed(1).replace(".0", "") + "M"; if (n >= 1e5) return Math.round(n / 1e3) + "k"; if (n >= 1e3) return (n / 1e3).toFixed(1).replace(".0", "") + "k"; return String(n); }
  function norm(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function subIndex(r) { var c = catByNum[r.cat]; if (!c) return 0; for (var i = 0; i < c.subs.length; i++) { if (c.subs[i].key === r.sub) return i + 1; } return 0; }
  function subTitle(r) { var c = catByNum[r.cat]; if (!c) return ""; for (var i = 0; i < c.subs.length; i++) { if (c.subs[i].key === r.sub) return c.subs[i].title; } return ""; }
  function firstCommand(t) { var m = /`([^`]+)`/.exec(t || ""); return m ? m[1] : ""; }
  function inlineCode(t) { return esc(t).replace(/`([^`]+)`/g, "<code>$1</code>"); }
  REPOS.forEach(function (r) { r._hay = norm([r.name, r.id, r.one, r.desc, r.tags.join(" "), r.stack, subTitle(r)].join(" ")); });

  // Header numbers
  var local = REPOS.filter(function (r) { return r.lib; }).length;
  $("sig").textContent = "Signatura " + CATS.length + " secciones · " + (DATA.checked ? "datos al " + DATA.checked : "");
  $("stats").innerHTML = [
    ["" + REPOS.length, "repos curados"], ["" + CATS.length, "categorías"], ["" + local, "en tu biblioteca"],
    ["" + (REPOS.length - local), "sugeridos nuevos"], [DATA.total_stars, "estrellas en total"], ["" + DATA.recipes.length, "recetas"]
  ].map(function (s) { return "<li><b>" + esc(s[0]) + "</b>" + esc(s[1]) + "</li>"; }).join("");
  $("foot").innerHTML = "Generado desde <code>INDICE_IA.json</code> con <code>uv run repo-intelligence guide build</code>." + (DATA.checked ? " Estrellas y actividad de GitHub al " + esc(DATA.checked) + "." : "");

  // Category nav
  function renderCats() {
    var counts = {}; REPOS.forEach(function (r) { counts[r.cat] = (counts[r.cat] || 0) + 1; });
    var html = "<h2>Categorías</h2>" + btn(0, "📚", "Todas", REPOS.length);
    CATS.forEach(function (c) { html += btn(c.num, c.emoji, c.num + ". " + c.title, counts[c.num] || 0); });
    $("cats").innerHTML = html;
    function btn(num, emoji, title, n) {
      return '<button class="cat-btn" type="button" data-cat="' + num + '" aria-pressed="' + (state.cat === num) + '"><span>' + esc(emoji) + "</span><span>" + esc(title) + '</span><span class="n">' + n + "</span></button>";
    }
  }

  function renderSubs() {
    var box = $("subs"), intro = $("catintro");
    if (!state.cat) { box.hidden = true; intro.hidden = true; return; }
    var c = catByNum[state.cat];
    intro.hidden = false;
    intro.innerHTML = "<strong>" + esc(c.emoji + " " + c.title) + "</strong>" + esc(c.desc);
    var counts = {}; REPOS.forEach(function (r) { if (r.cat === state.cat) counts[r.sub] = (counts[r.sub] || 0) + 1; });
    var html = '<button class="chip" type="button" data-sub="" aria-pressed="' + (state.sub === "") + '">Todas</button>';
    c.subs.forEach(function (s, i) {
      if (!counts[s.key]) return;
      html += '<button class="chip" type="button" data-sub="' + esc(s.key) + '" aria-pressed="' + (state.sub === s.key) + '">' + state.cat + "." + (i + 1) + " " + esc(s.title) + " · " + counts[s.key] + "</button>";
    });
    box.innerHTML = html; box.hidden = false;
  }

  function matches(r) {
    if (state.cat && r.cat !== state.cat) return false;
    if (state.sub && r.sub !== state.sub) return false;
    if (state.lib === "lib" && !r.lib) return false;
    if (state.lib === "new" && r.lib) return false;
    if (state.pick && !r.pick) return false;
    if (state.setup && r.setup !== state.setup) return false;
    if (state.role && r.role !== state.role) return false;
    if (state.q) {
      var terms = norm(state.q).split(/\s+/).filter(Boolean);
      for (var i = 0; i < terms.length; i++) { if (r._hay.indexOf(terms[i]) === -1) return false; }
    }
    return true;
  }

  function sorted(list) {
    var key = state.sort;
    return list.slice().sort(function (a, b) {
      if (key === "name") return a.name.localeCompare(b.name, "es");
      if (key === "recent") return String(b.updated).localeCompare(String(a.updated)) || (b.stars || 0) - (a.stars || 0);
      return (b.stars || 0) - (a.stars || 0);
    });
  }

  function badges(r) {
    var b = [];
    if (r.pick) b.push('<span class="badge pick">⭐ imprescindible</span>');
    if (!r.lib) b.push('<span class="badge new">🆕 sugerido</span>');
    if (r.status === "archived") b.push('<span class="badge warn">archivado</span>');
    if (r.status === "missing") b.push('<span class="badge warn">ya no está en GitHub</span>');
    if (ROLE[r.role]) b.push('<span class="badge">' + ROLE[r.role] + "</span>");
    if (SETUP[r.setup]) b.push('<span class="badge">' + SETUP[r.setup] + "</span>");
    if (EXEC[r.exec]) b.push('<span class="badge">' + EXEC[r.exec] + "</span>");
    if (r.mcp) b.push('<span class="badge">🔌 MCP</span>');
    return b.join("");
  }

  function card(r) {
    var cmd = firstCommand(r.install);
    var cmdHtml = cmd ? '<div class="cmd"><code title="' + esc(cmd) + '">' + esc(cmd) + '</code><button class="copy" type="button" data-copy="' + esc(cmd) + '">Copiar</button></div>' : "";
    return '<article class="card">' +
      '<div class="meta"><span class="callno">Sig. ' + r.cat + "." + subIndex(r) + " · " + esc(subTitle(r)) + '</span><span class="stars">★ ' + fmt(r.stars) + "</span></div>" +
      '<h3><button type="button" data-open="' + esc(r.id) + '">' + (r.emoji ? esc(r.emoji) + " " : "") + esc(r.name) + "</button></h3>" +
      '<p class="one">' + esc(r.one) + "</p>" +
      '<div class="badges">' + badges(r) + "</div>" + cmdHtml +
      '<div class="links"><a href="#repos" data-open="' + esc(r.id) + '">Ver detalle</a>' +
      (r.url ? '<a href="' + esc(r.url) + '" target="_blank" rel="noopener">GitHub</a>' : "") +
      '<a href="' + esc(r.ficha) + '" target="_blank" rel="noopener">Ficha</a></div>' +
      "</article>";
  }

  function render() {
    var list = sorted(REPOS.filter(matches));
    $("grid").innerHTML = list.map(card).join("");
    $("count").textContent = list.length + (list.length === 1 ? " repo" : " repos") + (state.q ? " para «" + state.q + "»" : "");
    $("empty").hidden = list.length > 0;
    if (!list.length) $("empty-text").textContent = state.q ? "Ningún repo coincide con «" + state.q + "» con estos filtros." : "No hay repos con esta combinación de filtros.";
    try { localStorage.setItem("blx-filters", JSON.stringify({ sort: state.sort })); } catch (e) {}
  }

  function renderRecipes() {
    $("recipes").innerHTML = DATA.recipes.map(function (rc) {
      var stack = rc.repos.map(function (id, i) {
        var r = byId[id]; return (i ? '<span class="arrow">→</span>' : "") + (r ? '<button class="chip" type="button" data-open="' + esc(id) + '">' + esc(r.name) + "</button>" : "");
      }).join("");
      return '<article class="recipe"><h3>' + esc(rc.emoji + " " + rc.title) + "</h3><p>" + esc(rc.goal) + '</p><div class="stack">' + stack + '</div><a href="' + esc(rc.page) + '" target="_blank" rel="noopener">Ver receta completa</a></article>';
    }).join("");
  }

  function relatedButtons(ids) {
    return ids.map(function (id) { var r = byId[id]; return r ? '<button type="button" data-open="' + esc(id) + '">' + esc(r.name) + " · ★ " + fmt(r.stars) + "</button>" : ""; }).join("");
  }

  function openRepo(id) {
    var r = byId[id]; if (!r) return;
    $("dlg-meta").innerHTML = '<span class="callno">Sig. ' + r.cat + "." + subIndex(r) + " · " + esc(catByNum[r.cat].title) + " › " + esc(subTitle(r)) + '</span><span class="stars">★ ' + fmt(r.stars) + "</span>";
    $("dlg-title").textContent = (r.emoji ? r.emoji + " " : "") + r.name;
    $("dlg-badges").innerHTML = badges(r);
    var html = '<p><strong>' + esc(r.one) + "</strong></p>";
    if (r.desc) html += "<div><h4>Qué es</h4><p>" + inlineCode(r.desc) + "</p></div>";
    if (r.why) html += "<div><h4>Por qué destaca</h4><p>" + inlineCode(r.why) + "</p></div>";
    if (r.install) html += "<div><h4>Instalación</h4><p>" + inlineCode(r.install) + "</p></div>";
    if (r.cases.length) html += "<div><h4>Casos de uso</h4><ul>" + r.cases.map(function (c) { return "<li>" + esc(c) + "</li>"; }).join("") + "</ul></div>";
    if (r.choose || r.avoid) html += '<div class="fit"><div><h4>✅ Elígelo si…</h4><p>' + inlineCode(r.choose) + '</p></div><div><h4>⛔ Evítalo si…</h4><p>' + inlineCode(r.avoid) + "</p></div></div>";
    if (r.limits) html += "<div><h4>Limitaciones</h4><p>" + inlineCode(r.limits) + "</p></div>";
    if (r.combines.length) html += '<div><h4>Combina con</h4><div class="related">' + relatedButtons(r.combines) + "</div></div>";
    if (r.alts.length) html += '<div><h4>Alternativas (elige una)</h4><div class="related">' + relatedButtons(r.alts) + "</div></div>";
    html += '<dl class="facts">' +
      (r.stack ? "<dt>Stack</dt><dd>" + esc(r.stack) + "</dd>" : "") +
      (r.models ? "<dt>Modelos / API</dt><dd>" + esc(r.models) + "</dd>" : "") +
      (r.license ? "<dt>Licencia</dt><dd>" + esc(r.license) + "</dd>" : "") +
      (r.lang ? "<dt>Lenguaje</dt><dd>" + esc(r.lang) + "</dd>" : "") +
      (r.updated ? "<dt>Última actividad</dt><dd>" + esc(r.updated) + "</dd>" : "") +
      (r.tags.length ? "<dt>Etiquetas</dt><dd>" + r.tags.map(esc).join(", ") + "</dd>" : "") +
      "</dl>";
    html += '<p class="links" style="display:flex;gap:16px;flex-wrap:wrap">' +
      (r.url ? '<a href="' + esc(r.url) + '" target="_blank" rel="noopener">Abrir en GitHub</a>' : "") +
      (r.home ? '<a href="' + esc(r.home) + '" target="_blank" rel="noopener">Sitio web</a>' : "") +
      '<a href="' + esc(r.ficha) + '" target="_blank" rel="noopener">Ficha completa</a></p>';
    $("dlg-body").innerHTML = html;
    var dlg = $("dlg");
    if (typeof dlg.showModal === "function") { if (!dlg.open) dlg.showModal(); } else { dlg.setAttribute("open", ""); }
    $("dlg-body").scrollTop = 0;
  }

  function copyText(button, text) {
    function done(ok) { button.textContent = ok ? "Copiado" : "Selecciona y copia"; setTimeout(function () { button.textContent = "Copiar"; }, 1600); }
    try {
      navigator.clipboard.writeText(text).then(function () { done(true); }, function () { selectFallback(); done(false); });
    } catch (e) { selectFallback(); done(false); }
    function selectFallback() { var code = button.parentNode.querySelector("code"); if (!code) return; var range = document.createRange(); range.selectNodeContents(code); var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range); }
  }

  function setView() {
    var recetas = location.hash === "#recetas";
    $("view-repos").hidden = recetas; $("view-recetas").hidden = !recetas;
    $("tab-repos").setAttribute("aria-current", recetas ? "false" : "page");
    $("tab-recetas").setAttribute("aria-current", recetas ? "page" : "false");
  }

  document.addEventListener("click", function (ev) {
    var t = ev.target.closest("[data-open],[data-cat],[data-sub],[data-copy]");
    if (!t) return;
    if (t.hasAttribute("data-copy")) { copyText(t, t.getAttribute("data-copy")); return; }
    if (t.hasAttribute("data-open")) { ev.preventDefault(); openRepo(t.getAttribute("data-open")); return; }
    if (t.hasAttribute("data-cat")) { state.cat = Number(t.getAttribute("data-cat")); state.sub = ""; renderCats(); renderSubs(); render(); return; }
    if (t.hasAttribute("data-sub")) { state.sub = t.getAttribute("data-sub"); renderSubs(); render(); }
  });
  var timer;
  $("q").addEventListener("input", function (ev) { clearTimeout(timer); timer = setTimeout(function () { state.q = ev.target.value.trim(); render(); }, 120); });
  ["all", "lib", "new"].forEach(function (k) {
    $("f-" + k).addEventListener("click", function () { state.lib = k; ["all", "lib", "new"].forEach(function (o) { $("f-" + o).setAttribute("aria-pressed", String(o === k)); }); render(); });
  });
  $("f-pick").addEventListener("change", function (ev) { state.pick = ev.target.checked; render(); });
  $("f-setup").addEventListener("change", function (ev) { state.setup = ev.target.value; render(); });
  $("f-role").addEventListener("change", function (ev) { state.role = ev.target.value; render(); });
  $("f-sort").value = state.sort;
  $("f-sort").addEventListener("change", function (ev) { state.sort = ev.target.value; render(); });
  $("reset").addEventListener("click", function () {
    state = { q: "", cat: 0, sub: "", lib: "all", pick: false, setup: "", role: "", sort: state.sort };
    $("q").value = ""; $("f-pick").checked = false; $("f-setup").value = ""; $("f-role").value = "";
    ["all", "lib", "new"].forEach(function (o) { $("f-" + o).setAttribute("aria-pressed", String(o === "all")); });
    renderCats(); renderSubs(); render();
  });
  $("dlg-close").addEventListener("click", function () { $("dlg").close ? $("dlg").close() : $("dlg").removeAttribute("open"); });
  $("dlg").addEventListener("click", function (ev) { if (ev.target === $("dlg")) $("dlg").close(); });
  window.addEventListener("hashchange", setView);

  renderCats(); renderSubs(); render(); renderRecipes(); setView();
})();
</script>
"""
