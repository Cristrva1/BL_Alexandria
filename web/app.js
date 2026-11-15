(function () {
  const raw = document.getElementById("catalog-data").textContent;
  const catalog = JSON.parse(raw);
  const byId = Object.fromEntries(catalog.repos.map((repo) => [repo.id, repo]));
  const catByNum = Object.fromEntries(catalog.categories.map((cat) => [String(cat.num), cat]));
  const folded = new Map();
  for (const repo of catalog.repos) {
    folded.set(norm(repo.id), repo.id);
  }

  const NAV = [
    ["inicio", "Inicio"],
    ["curso", "Curso"],
    ["salas", "Salas"],
    ["explorar", "Explorar"],
    ["recetas", "Recetas"],
    ["laboratorio", "Laboratorio"],
    ["comparar", "Comparar"],
  ];

  const ROLE_COLORS = ["#c24d2c", "#1e5c52", "#8d6a2f", "#3f382f", "#8e341c", "#6d6458"];

  function norm(value) {
    return (value || "").toLowerCase().replace(/[^a-z0-9]/g, "");
  }

  function fold(value) {
    return (value || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/\p{M}/gu, "");
  }

  function safeUrl(value) {
    try {
      const parsed = new URL(value);
      if (parsed.protocol === "http:" || parsed.protocol === "https:") return parsed.href;
    } catch (_error) {
      return "";
    }
    return "";
  }

  function esc(value) {
    return String(value ?? "").replace(/[&<>"']/g, (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;",
    }[char]));
  }

  function resolveLoose(slug) {
    const direct = byId[slug] ? slug : null;
    if (direct) return direct;
    const lower = (slug || "").toLowerCase();
    const found = catalog.repos.find((repo) => repo.id.toLowerCase() === lower);
    return found ? found.id : folded.get(norm(slug)) || null;
  }

  function rich(text) {
    const escaped = esc(text || "");
    return escaped
      .replace(/\[([^\]]+)\]\(#-([^)\s]+)\)/g, (_, label, slug) => {
        const id = resolveLoose(slug);
        if (!id) return label;
        return `<a href="#/repo/${encodeURIComponent(id)}">${label}</a>`;
      })
      .replace(/`([^`]+)`/g, "<code>$1</code>");
  }

  function paragraphs(text) {
    if (!text) return "";
    return String(text)
      .split(/\n{2,}/)
      .map((part) => `<p>${rich(part).replace(/\n/g, "<br>")}</p>`)
      .join("");
  }

  function label(group, key) {
    return (catalog.labels[group] && catalog.labels[group][key]) || key || "—";
  }

  function catName(num) {
    const cat = catByNum[String(num)];
    return cat ? cat.title : (num === 0 ? "Taller local" : "Sin sala");
  }

  function repo(id) {
    return byId[id] || null;
  }

  function badges(item) {
    const bits = [
      `<span class="badge">${esc(label("role", item.role))}</span>`,
      `<span class="badge">${esc(label("exec", item.exec))}</span>`,
      `<span class="badge ${item.setup === "heavy" ? "terra" : item.setup === "easy" ? "green" : "gold"}">${esc(label("setup", item.setup))}</span>`,
    ];
    if (item.mcp) bits.push('<span class="badge green">MCP</span>');
    return `<div class="badges">${bits.join("")}</div>`;
  }

  function repoCard(item) {
    return `<a class="card" href="#/repo/${encodeURIComponent(item.id)}">
      <span class="meta">${esc(catName(item.cat))}</span>
      <h3>${esc(item.name)}</h3>
      <p>${esc(item.lead)}</p>
      ${badges(item)}
    </a>`;
  }

  function refLinks(refs) {
    if (!refs || !refs.length) return "<p class='meta'>Ninguna declarada.</p>";
    return `<div class="badges">${refs.map((ref) => {
      if (ref.id && repo(ref.id)) {
        const name = repo(ref.id).name;
        return `<a class="badge" href="#/repo/${encodeURIComponent(ref.id)}">${esc(name)}</a>`;
      }
      return `<span class="badge">${esc(ref.label || ref.id || "")}</span>`;
    }).join("")}</div>`;
  }

  function parseHash() {
    const rawHash = (location.hash || "#/inicio").replace(/^#/, "");
    const [path, query = ""] = rawHash.split("?");
    const parts = path.split("/").filter(Boolean);
    return { parts, params: new URLSearchParams(query) };
  }

  function exploreHref(params) {
    const search = params.toString();
    return `#/explorar${search ? `?${search}` : ""}`;
  }

  function storageGet(key, fallback) {
    try {
      const value = localStorage.getItem(key);
      return value ? JSON.parse(value) : fallback;
    } catch (_error) {
      return fallback;
    }
  }

  function storageSet(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
  }

  function compareList() {
    return storageGet("alexandria-compare", []).filter((id) => repo(id));
  }

  function recipeDone(id) {
    return new Set(storageGet(`alexandria-recipe:${id}`, []));
  }

  function resume() {
    for (const recipe of catalog.recipes) {
      const done = recipeDone(recipe.id);
      const total = recipe.steps.filter((step) => step.id).length;
      if (done.size > 0 && done.size < total) {
        return { recipe, done: done.size, total };
      }
    }
    return null;
  }

  function filtered(params) {
    const q = fold(params.get("q") || "");
    const cat = params.get("cat") || "";
    const role = params.get("role") || "";
    const exec = params.get("exec") || "";
    const setup = params.get("setup") || "";
    const mcp = params.get("mcp") || "";
    const prov = params.get("prov") || "";
    return catalog.repos.filter((item) => {
      if (cat && String(item.cat) !== cat) return false;
      if (role && item.role !== role) return false;
      if (exec && item.exec !== exec) return false;
      if (setup && item.setup !== setup) return false;
      if (mcp === "1" && !item.mcp) return false;
      if (mcp === "0" && item.mcp) return false;
      if (prov === "none" && item.prov.length) return false;
      if (prov && prov !== "none" && !item.prov.includes(prov)) return false;
      if (!q) return true;
      const hay = fold([
        item.name, item.id, item.lead, item.body, item.one, item.desc,
        item.choose_if, item.avoid_if, item.stack, catName(item.cat),
        ...(item.tags || []), ...(item.prov || []),
      ].join(" "));
      return hay.includes(q);
    });
  }

  function options(group, current, allLabel) {
    const entries = Object.entries(catalog.labels[group] || {});
    const opts = [`<option value="">${esc(allLabel)}</option>`]
      .concat(entries.map(([key, text]) => `<option value="${esc(key)}"${key === current ? " selected" : ""}>${esc(text)}</option>`));
    return opts.join("");
  }

  function layout(active, main) {
    const items = NAV.map(([id, text]) => {
      const cls = id === active ? "item active" : "item";
      return `<a class="${cls}" href="#/${id}">${esc(text)}</a>`;
    }).join("");
    return `<a class="skip" href="#contenido">Saltar al contenido</a>
      <div class="shell">
        <nav class="nav" aria-label="Secciones">
          <a class="brand" href="#/inicio">
            <span class="seal" aria-hidden="true">A</span>
            <span><small>Biblioteca</small><strong>Alejandría</strong></span>
          </a>
          ${items}
          <p class="nav-foot">${catalog.counts.repos} repos · ${catalog.counts.categories} salas · ${catalog.counts.recipes} recetas</p>
        </nav>
        <main id="contenido" class="main"><div class="wrap">${main}</div></main>
      </div>`;
  }

  function renderHome() {
    const counts = catalog.counts;
    const principles = catalog.copy.principles.map((item) => `<article class="card"><h3>${esc(item.title)}</h3><p>${esc(item.text)}</p></article>`).join("");
    const roles = {};
    catalog.repos.forEach((item) => { roles[item.role] = (roles[item.role] || 0) + 1; });
    const roleKeys = Object.keys(roles);
    const bar = roleKeys.map((key, index) => {
      const width = (roles[key] / counts.repos) * 100;
      return `<span style="width:${width}%;background:${ROLE_COLORS[index % ROLE_COLORS.length]}" title="${esc(label("role", key))}"></span>`;
    }).join("");
    const legend = roleKeys.map((key, index) => `<span><i class="swatch" style="background:${ROLE_COLORS[index % ROLE_COLORS.length]}"></i>${esc(label("role", key))} ${roles[key]}</span>`).join("");
    const recipes = catalog.recipes.slice(0, 3).map(recipeCard).join("");
    const progress = resume();
    const resumeHtml = progress
      ? `<p class="aside">Sigues en ${esc(progress.recipe.title)}: ${progress.done} de ${progress.total} piezas. <a href="#/receta/${esc(progress.recipe.id)}">Continuar</a></p>`
      : `<p class="aside">Empieza por la lección 1. Dura unos minutos y evita que instales de más.</p>`;
    return `<header class="hero">
        <div>
          <p class="kicker">Biblioteca curada</p>
          <h1>Elige pocos repos y entiende por qué.</h1>
          <p class="lede">${counts.repos} repositorios de IA y automatización, leídos para decidir qué instalar y qué dejar fuera.</p>
          <div class="actions">
            <a class="btn" href="#/curso">Empezar el curso</a>
            <a class="btn ghost" href="#/explorar">Explorar los repos</a>
          </div>
        </div>
        <div class="stamp-card">
          <strong>${counts.repos}</strong>
          <span>repos en ${counts.categories} salas</span>
          <p class="meta">${counts.recipes} recetas de producto · ${counts.mcp} con MCP · ${counts.labs} pares para practicar</p>
        </div>
      </header>
      <p class="principle">${esc(catalog.copy.principle)}</p>
      ${resumeHtml}
      <section class="section grid-3">${principles}</section>
      <section class="section">
        <h2>De qué está hecha</h2>
        <div class="bar" aria-hidden="true">${bar}</div>
        <div class="legend">${legend}</div>
      </section>
      <section class="section">
        <div class="command-row">
          <h2>Tres recetas para entrar</h2>
          <a href="#/recetas">Ver las ${counts.recipes}</a>
        </div>
        <div class="grid-3">${recipes}</div>
      </section>`;
  }

  function renderCourse() {
    const cards = catalog.lessons.map((lesson, index) => `<a class="lesson-link" href="#/curso/${esc(lesson.id)}">
      <span class="meta">${esc(lesson.kicker)} · ${lesson.minutes} min</span>
      <h3>${index + 1}. ${esc(lesson.title)}</h3>
      <p>${esc((lesson.blocks.find((block) => block.type === "p") || {}).text || "")}</p>
    </a>`).join("");
    return `<p class="kicker">Curso</p>
      <h1>Aprende a usar la biblioteca</h1>
      <p class="lede">Cuatro lecciones cortas. Después, el laboratorio te hace elegir entre alternativas reales.</p>
      <div class="section cards">${cards}</div>
      <p><a class="btn" href="#/laboratorio">Practicar en el laboratorio</a></p>`;
  }

  function renderLesson(id) {
    const lesson = catalog.lessons.find((item) => item.id === id);
    if (!lesson) return missing("Esa lección no está en el curso.", "#/curso");
    const index = catalog.lessons.findIndex((item) => item.id === id);
    const blocks = lesson.blocks.map((block) => {
      if (block.type === "points") {
        return `<ul class="points">${block.items.map((item) => `<li>${esc(item)}</li>`).join("")}</ul>`;
      }
      if (block.type === "aside") return `<p class="aside">${esc(block.text)}</p>`;
      return `<p>${esc(block.text)}</p>`;
    }).join("");
    const glossary = id === "glosario"
      ? `<dl class="glossary section">${catalog.glossary.map((entry) => `<dt>${esc(entry.term)}</dt><dd>${esc(entry.text)}</dd>`).join("")}</dl>`
      : "";
    const tools = id === "dos-decisiones" ? renderTools() : "";
    const prev = catalog.lessons[index - 1];
    const next = catalog.lessons[index + 1];
    return `<p class="kicker">${esc(lesson.kicker)} · ${lesson.minutes} min</p>
      <h1>${esc(lesson.title)}</h1>
      ${blocks}
      ${tools}
      ${glossary}
      <div class="pager">
        ${prev ? `<a href="#/curso/${esc(prev.id)}">← ${esc(prev.title)}</a>` : "<span></span>"}
        ${next ? `<a href="#/curso/${esc(next.id)}">${esc(next.title)} →</a>` : `<a href="#/laboratorio">Ir al laboratorio →</a>`}
      </div>`;
  }

  function renderTools() {
    const tools = catalog.model_guidance.tools.map((tool) => {
      const names = tool.repos.map((id) => repo(id) ? `<a href="#/repo/${encodeURIComponent(id)}">${esc(repo(id).name)}</a>` : esc(id)).join(", ");
      return `<article class="card"><h3>${esc(tool.id)}</h3><p>${esc(tool.note)}</p>${names ? `<p class="meta">Repos: ${names}</p>` : ""}</article>`;
    }).join("");
    return `<section class="section">
      <h2>Según la herramienta con la que programas</h2>
      <p>${esc(catalog.model_guidance.key_distinction || "")}</p>
      <div class="cards">${tools}</div>
    </section>`;
  }

  function renderRooms() {
    const rooms = catalog.categories.filter((cat) => cat.num >= 1).map((cat) => `<a class="room" href="#/explorar?cat=${cat.num}">
      <span class="room-num">${String(cat.num).padStart(2, "0")}</span>
      <h3>${esc(cat.title)}</h3>
      <p>${esc(cat.blurb)}</p>
      <span class="meta">${cat.count} repos</span>
    </a>`).join("");
    const journeys = catalog.journeys.map((journey) => {
      const links = journey.rooms.map((num) => {
        const cat = catByNum[String(num)];
        return cat ? `<a href="#/explorar?cat=${num}">${esc(cat.title)}</a>` : "";
      }).filter(Boolean).join(" · ");
      return `<article class="card"><h3>${esc(journey.title)}</h3><p>${esc(journey.text)}</p><p class="meta">${links}</p></article>`;
    }).join("");
    const local = catByNum["0"];
    const footnote = local
      ? `<p class="meta">Además hay ${local.count} ${local.count === 1 ? "pieza" : "piezas"} de taller local, fuera de las salas. <a href="#/explorar?cat=0">Ver</a></p>`
      : "";
    return `<p class="kicker">Mapa</p>
      <h1>Trece salas, un oficio cada una</h1>
      <p class="lede">${esc(catalog.copy.journey_note)}</p>
      <section class="section grid-3">${journeys}</section>
      <div class="rooms">${rooms}</div>
      ${footnote}`;
  }

  function renderExplore(params) {
    const items = filtered(params);
    const cats = [`<option value="">Todas las salas</option>`]
      .concat(catalog.categories.map((cat) => {
        const short = cat.title.split(/[,&]/)[0].trim();
        const selected = String(cat.num) === (params.get("cat") || "") ? " selected" : "";
        return `<option value="${cat.num}"${selected}>${esc(short)}</option>`;
      }))
      .join("");
    const providers = Array.from(new Set(catalog.repos.flatMap((item) => item.prov))).sort();
    const provOpts = [`<option value="">Proveedor</option>`, `<option value="none"${params.get("prov") === "none" ? " selected" : ""}>Sin declarar</option>`]
      .concat(providers.map((item) => `<option value="${esc(item)}"${params.get("prov") === item ? " selected" : ""}>${esc(item)}</option>`))
      .join("");
    const chips = [];
    const addChip = (key, text) => {
      const next = new URLSearchParams(params);
      next.delete(key);
      chips.push(`<a class="chip" href="${exploreHref(next)}">${esc(text)} ×</a>`);
    };
    if (params.get("q")) addChip("q", `“${params.get("q")}”`);
    if (params.get("cat")) addChip("cat", catName(params.get("cat")));
    if (params.get("role")) addChip("role", label("role", params.get("role")));
    if (params.get("exec")) addChip("exec", label("exec", params.get("exec")));
    if (params.get("setup")) addChip("setup", label("setup", params.get("setup")));
    if (params.get("mcp")) addChip("mcp", params.get("mcp") === "1" ? "Con MCP" : "Sin MCP");
    if (params.get("prov")) addChip("prov", params.get("prov") === "none" ? "Sin proveedor" : params.get("prov"));
    const list = items.length
      ? `<div class="cards" id="results">${items.map(repoCard).join("")}</div>`
      : `<div id="results"><p class="empty">${esc(catalog.copy.empty_search)}</p></div>`;
    return `<p class="kicker">Explorador</p>
      <h1>Busca por oficio, no por moda</h1>
      <form class="toolbar" id="filters">
        <input id="q" type="search" name="q" placeholder="Buscar: whatsapp, memoria, voz…" value="${esc(params.get("q") || "")}" autocomplete="off">
        <select name="cat" aria-label="Sala">${cats}</select>
        <select name="role" aria-label="Papel">${options("role", params.get("role") || "", "Papel")}</select>
        <select name="exec" aria-label="Ejecución">${options("exec", params.get("exec") || "", "Ejecución")}</select>
        <select name="setup" aria-label="Arranque">${options("setup", params.get("setup") || "", "Arranque")}</select>
        <select name="mcp" aria-label="MCP">
          <option value="">MCP</option>
          <option value="1"${params.get("mcp") === "1" ? " selected" : ""}>Con MCP</option>
          <option value="0"${params.get("mcp") === "0" ? " selected" : ""}>Sin MCP</option>
        </select>
        <select name="prov" aria-label="Proveedor">${provOpts}</select>
      </form>
      <div class="filters">${chips.join("")}${chips.length ? `<a class="chip" href="#/explorar">Limpiar</a>` : ""}</div>
      <p class="live" id="count" aria-live="polite">${items.length} ${items.length === 1 ? "repo" : "repos"}</p>
      ${list}`;
  }

  function renderRepo(id) {
    const item = repo(id);
    if (!item) return missing("Ese repo no está en la biblioteca.", "#/explorar");
    const compared = compareList().includes(item.id);
    const body = item.body
      ? paragraphs(item.body)
      : `<p>${esc(catalog.copy.junk_note)}</p>`;
    const sameOpening = item.body && item.lead
      && item.body.toLowerCase().startsWith(item.lead.toLowerCase().slice(0, 48));
    const dek = item.lead && !sameOpening ? `<p class="dek">${esc(item.lead)}</p>` : "";
    const skill = item.role === "skill" || item.role === "directory"
      ? `<p class="aside">${esc(catalog.copy.skill_note)}</p>` : "";
    const prov = item.prov.length
      ? item.prov.map((name) => `<span class="badge">${esc(name)}</span>`).join("")
      : "<span class='meta'>No declara proveedor. Casi siempre se configura con una variable de entorno.</span>";
    const tags = (item.tags || []).slice(0, 12).map((tag) => `<a class="badge" href="#/explorar?q=${encodeURIComponent(tag)}">${esc(tag)}</a>`).join("");
    const sourceUrl = safeUrl(item.repo_url);
    const source = sourceUrl
      ? `<a href="${esc(sourceUrl)}" target="_blank" rel="noreferrer">Abrir el repositorio</a>`
      : "<span class='meta'>Sin URL de origen.</span>";
    const confidence = label("confidence", item.install.confidence);
    return `<p class="kicker"><a href="#/explorar?cat=${item.cat}">${esc(catName(item.cat))}</a></p>
      <h1>${esc(item.name)}</h1>
      ${dek}
      ${badges(item)}
      <div class="section">${body}</div>
      ${skill}
      <section class="split">
        <article class="callout yes"><h3>Elige si</h3><p>${item.choose_if ? rich(item.choose_if) : "La ficha todavía no declara este criterio."}</p></article>
        <article class="callout no"><h3>Evítalo si</h3><p>${item.avoid_if ? rich(item.avoid_if) : "La ficha todavía no declara este límite."}</p></article>
      </section>
      <section class="section">
        <div class="command-row">
          <h2>Cómo entra en un proyecto</h2>
          <span class="badge ${item.install.confidence === "ok" ? "green" : item.install.confidence === "verify" ? "gold" : "terra"}">${esc(confidence)}</span>
        </div>
        <pre class="command" id="install-command">${esc(item.install.command)}</pre>
        <button class="btn small" type="button" data-action="copy" data-text="${esc(item.install.command)}">Copiar comando</button>
        <p class="meta">${esc(item.install.note)} ${esc(catalog.copy.install_note)}</p>
      </section>
      <section class="section grid-2">
        <div>
          <h2>Combina con</h2>
          <p class="meta">${esc(catalog.copy.combine_note)}</p>
          ${refLinks(item.combine_refs)}
        </div>
        <div>
          <h2>Alternativas</h2>
          <p class="meta">${esc(catalog.copy.alt_note)}</p>
          ${refLinks(item.alt_refs)}
        </div>
      </section>
      <section class="section callout">
        <h2>Ficha técnica</h2>
        <p><strong>Papel.</strong> ${esc(label("role", item.role))}. ${esc(catalog.role_why[item.role] || "")}</p>
        <p><strong>Ejecución.</strong> ${esc(label("exec", item.exec))}.</p>
        <p><strong>Arranque.</strong> ${esc(label("setup", item.setup))}.</p>
        <p><strong>Stack.</strong> ${item.stack ? esc(item.stack) : "No declarado."}</p>
        <p><strong>Proveedor.</strong> ${prov}</p>
        ${tags ? `<p><strong>Etiquetas.</strong></p><div class="badges">${tags}</div>` : ""}
        <p>${source}${item.doc ? ` · En esta biblioteca: <code>${esc(item.doc)}</code>` : ""}</p>
        <button class="btn small" type="button" data-action="compare" data-id="${esc(item.id)}">${compared ? "Quitar de comparar" : "Añadir a comparar"}</button>
      </section>`;
  }

  function recipeCard(recipe) {
    const layers = recipe.pick_one.length ? `${recipe.pick_one.length} ${recipe.pick_one.length === 1 ? "capa con alternativa" : "capas con alternativa"}` : "piezas que se suman";
    return `<a class="recipe-link" href="#/receta/${esc(recipe.id)}">
      <span class="meta">${recipe.steps.length} piezas · ${layers}</span>
      <h3>${esc(recipe.title)}</h3>
      <p>${esc(recipe.goal)}</p>
    </a>`;
  }

  function renderRecipes() {
    return `<p class="kicker">Recetas</p>
      <h1>Un producto, pocas piezas</h1>
      <p class="lede">Cada receta es un recorrido. El orden es el orden del flujo. Si un paso dice que comparte capa con otro, eliges uno.</p>
      <div class="section cards">${catalog.recipes.map(recipeCard).join("")}</div>`;
  }

  function renderRecipe(id) {
    const recipe = catalog.recipes.find((item) => item.id === id);
    if (!recipe) return missing("Esa receta no está.", "#/recetas");
    const done = recipeDone(recipe.id);
    const realSteps = recipe.steps.filter((step) => step.id);
    const items = recipe.steps.map((step, index) => {
      if (!step.id) {
        return `<li><span class="step-no">${index + 1}</span><article><h3>${esc(step.label)}</h3><p>${esc(step.why)}</p></article></li>`;
      }
      const item = repo(step.id);
      const exclusive = (step.exclusive_with || []).map((other) => repo(other) ? repo(other).name : other).join(" o ");
      const note = exclusive ? `<p class="meta">Misma capa que ${esc(exclusive)}. Empieza por una.</p>` : "";
      return `<li>
        <span class="step-no">${index + 1}</span>
        <article>
          <div class="step-head">
            <div>
              <h3><a href="#/repo/${encodeURIComponent(step.id)}">${esc(item ? item.name : step.label)}</a></h3>
              <p>${esc(step.why)}</p>
              ${note}
            </div>
            <label class="check"><input type="checkbox" data-action="step" data-recipe="${esc(recipe.id)}" data-id="${esc(step.id)}"${done.has(step.id) ? " checked" : ""}> Ya lo entendí</label>
          </div>
        </article>
      </li>`;
    }).join("");
    return `<p class="kicker">Receta · ${realSteps.length} piezas</p>
      <h1>${esc(recipe.title)}</h1>
      <p class="lede">${esc(recipe.goal)}</p>
      ${recipe.lesson ? `<p>${esc(recipe.lesson)}</p>` : ""}
      ${recipe.how ? `<p class="meta">${rich(recipe.how)}</p>` : ""}
      <p class="live" id="recipe-progress">${done.size} de ${realSteps.length} piezas marcadas. Es un recordatorio local, no un requisito.</p>
      <ol class="timeline">${items}</ol>
      <p><a href="#/recetas">Volver a las recetas</a></p>`;
  }

  function renderLab(params) {
    const labs = catalog.labs;
    if (!labs.length) return `<h1>Laboratorio</h1><p class="empty">Esta biblioteca todavía no declara alternativas para practicar.</p>`;
    const requested = Number(params.get("n") || "0");
    const index = ((requested % labs.length) + labs.length) % labs.length;
    const pair = labs[index];
    const left = repo(pair.a);
    const right = repo(pair.b);
    const choice = sessionStorage.getItem(`alexandria-lab:${pair.a}:${pair.b}`);
    const next = (index + 1) % labs.length;
    const verdict = choice && repo(choice) ? renderVerdict(repo(choice), choice === pair.a ? right : left) : "";
    return `<p class="kicker">Laboratorio · ${index + 1} de ${labs.length}</p>
      <h1>Quédate con una.</h1>
      <p class="lede">${esc(catalog.copy.lab_intro)}</p>
      <div class="versus">
        ${choiceCard(left, choice)}
        <span class="or">o</span>
        ${choiceCard(right, choice)}
      </div>
      ${verdict}
      <div class="pager">
        <a href="#/laboratorio?n=${(index - 1 + labs.length) % labs.length}">← Par anterior</a>
        <a href="#/laboratorio?n=${next}">Otro par →</a>
      </div>`;
  }

  function choiceCard(item, choice) {
    const chosen = choice === item.id ? " chosen" : "";
    return `<button class="choice${chosen}" type="button" data-action="choose-lab" data-id="${esc(item.id)}">
      <span class="meta">${esc(catName(item.cat))}</span>
      <h3>${esc(item.name)}</h3>
      <p>${esc(item.lead)}</p>
      ${badges(item)}
    </button>`;
  }

  function renderVerdict(chosen, other) {
    return `<section class="verdict callout yes">
      <h2>Te quedas con ${esc(chosen.name)}.</h2>
      <p>${chosen.choose_if ? `Tiene sentido cuando ${rich(String(chosen.choose_if).replace(/[.\s]+$/, ""))}.` : esc(chosen.lead)}</p>
      <p>Dejas fuera a <a href="#/repo/${encodeURIComponent(other.id)}">${esc(other.name)}</a>, porque cubre el mismo hueco.</p>
      <h3>Con qué sí se combina</h3>
      ${refLinks(chosen.combine_refs)}
      <p><a href="#/repo/${encodeURIComponent(chosen.id)}">Abrir la ficha completa</a></p>
    </section>`;
  }

  function renderCompare() {
    const ids = compareList();
    const picker = `<form class="toolbar" id="compare-add">
      <select name="id" aria-label="Añadir repo">
        <option value="">Añadir un repo…</option>
        ${catalog.repos.map((item) => `<option value="${esc(item.id)}">${esc(item.name)}</option>`).join("")}
      </select>
      <button class="btn small" type="submit">Añadir</button>
    </form>`;
    if (!ids.length) {
      return `<p class="kicker">Comparar</p><h1>Pon hasta tres fichas juntas</h1>
        <p class="lede">Sirve para desempatar, no para sumar. Si dos repos son alternativas, quédate con uno.</p>
        ${picker}<p class="empty">Todavía no hay repos en la mesa. Ábrelos desde una ficha o elige uno aquí.</p>`;
    }
    const rows = [
      ["Oficio", (item) => esc(item.lead)],
      ["Papel", (item) => esc(label("role", item.role))],
      ["Ejecución", (item) => esc(label("exec", item.exec))],
      ["Arranque", (item) => esc(label("setup", item.setup))],
      ["Elige si", (item) => item.choose_if ? rich(item.choose_if) : "—"],
      ["Evítalo si", (item) => item.avoid_if ? rich(item.avoid_if) : "—"],
      ["Stack", (item) => esc(item.stack || "—")],
    ];
    const head = ids.map((id) => `<th><a href="#/repo/${encodeURIComponent(id)}">${esc(repo(id).name)}</a><br><button class="btn small ghost" type="button" data-action="compare" data-id="${esc(id)}">Quitar</button></th>`).join("");
    const body = rows.map(([name, cell]) => `<tr><th>${name}</th>${ids.map((id) => `<td>${cell(repo(id))}</td>`).join("")}</tr>`).join("");
    return `<p class="kicker">Comparar · ${ids.length} de 3</p>
      <h1>Míralos en la misma mesa</h1>
      <p class="lede">Si comparten oficio, no los instales juntos. Lee «Evítalo si» antes de quedarte con los dos.</p>
      ${picker}
      <div class="table-wrap"><table class="compare"><thead><tr><th></th>${head}</tr></thead><tbody>${body}</tbody></table></div>`;
  }

  function missing(text, href) {
    return `<h1>No está en el estante</h1><p class="lede">${esc(text)}</p><p><a href="${href}">Volver</a></p>`;
  }

  function activeOf(parts) {
    const head = parts[0] || "inicio";
    if (head === "repo") return "explorar";
    if (head === "receta") return "recetas";
    if (head === "sala") return "salas";
    return NAV.some(([id]) => id === head) ? head : "inicio";
  }

  function titleOf(parts) {
    const head = parts[0] || "inicio";
    if (head === "repo" && repo(decodeURIComponent(parts[1] || ""))) return repo(decodeURIComponent(parts[1])).name;
    if (head === "receta") {
      const recipe = catalog.recipes.find((item) => item.id === parts[1]);
      return recipe ? recipe.title : "Receta";
    }
    if (head === "curso" && parts[1]) {
      const lesson = catalog.lessons.find((item) => item.id === parts[1]);
      return lesson ? lesson.title : "Curso";
    }
    const nav = NAV.find(([id]) => id === head);
    return nav ? nav[1] : "Alejandría";
  }

  function view(route) {
    const [head, second] = route.parts;
    if (!head || head === "inicio") return renderHome();
    if (head === "curso") return second ? renderLesson(second) : renderCourse();
    if (head === "salas" || head === "sala") return renderRooms();
    if (head === "explorar") return renderExplore(route.params);
    if (head === "repo") return renderRepo(decodeURIComponent(second || ""));
    if (head === "recetas") return renderRecipes();
    if (head === "receta") return renderRecipe(second || "");
    if (head === "laboratorio") return renderLab(route.params);
    if (head === "comparar") return renderCompare();
    return missing("Esa sección no existe.", "#/inicio");
  }

  function paintExplore(params) {
    const items = filtered(params);
    const results = document.getElementById("results");
    const count = document.getElementById("count");
    if (!results || !count) return;
    results.className = items.length ? "cards" : "";
    results.innerHTML = items.length
      ? items.map(repoCard).join("")
      : `<p class="empty">${esc(catalog.copy.empty_search)}</p>`;
    count.textContent = `${items.length} ${items.length === 1 ? "repo" : "repos"}`;
  }

  function currentParamsFromForm() {
    const form = document.getElementById("filters");
    const params = new URLSearchParams();
    if (!form) return params;
    new FormData(form).forEach((value, key) => {
      if (String(value).trim()) params.set(key, String(value).trim());
    });
    return params;
  }

  function draw() {
    const route = parseHash();
    const typing = document.activeElement && document.activeElement.id === "q" && (route.parts[0] || "inicio") === "explorar";
    if (typing && document.getElementById("filters")) {
      paintExplore(currentParamsFromForm());
      return;
    }
    document.getElementById("app").innerHTML = layout(activeOf(route.parts), view(route));
    document.title = `${titleOf(route.parts)} — Alejandría`;
    const q = document.getElementById("q");
    if (q && route.parts[0] === "explorar" && window.__focusSearch) {
      q.focus();
      window.__focusSearch = false;
    }
  }

  document.getElementById("app").addEventListener("input", (event) => {
    if (event.target.id !== "q") return;
    const params = currentParamsFromForm();
    paintExplore(params);
    const href = exploreHref(params);
    if (location.hash !== href) history.replaceState(null, "", href);
  });

  document.getElementById("app").addEventListener("change", (event) => {
    const form = event.target.form;
    if (!form) return;
    if (form.id === "filters") {
      location.hash = exploreHref(currentParamsFromForm()).slice(1);
    }
  });

  document.getElementById("app").addEventListener("submit", (event) => {
    if (event.target.id === "compare-add") {
      event.preventDefault();
      const id = new FormData(event.target).get("id");
      if (!id) return;
      const list = compareList().filter((item) => item !== id);
      list.push(String(id));
      storageSet("alexandria-compare", list.slice(-3));
      draw();
    }
    if (event.target.id === "filters") event.preventDefault();
  });

  document.getElementById("app").addEventListener("click", async (event) => {
    const button = event.target.closest("[data-action]");
    if (!button) return;
    const action = button.dataset.action;
    if (action === "copy") {
      const text = button.dataset.text || "";
      try {
        await navigator.clipboard.writeText(text);
        button.textContent = "Copiado";
      } catch (_error) {
        button.textContent = "Selecciona el comando";
      }
    }
    if (action === "compare") {
      const id = button.dataset.id;
      const list = compareList();
      const next = list.includes(id) ? list.filter((item) => item !== id) : list.concat(id).slice(-3);
      storageSet("alexandria-compare", next);
      draw();
    }
    if (action === "choose-lab") {
      const route = parseHash();
      const index = Number(route.params.get("n") || "0");
      const pair = catalog.labs[((index % catalog.labs.length) + catalog.labs.length) % catalog.labs.length];
      sessionStorage.setItem(`alexandria-lab:${pair.a}:${pair.b}`, button.dataset.id);
      draw();
    }
  });

  document.getElementById("app").addEventListener("change", (event) => {
    if (event.target.dataset.action !== "step") return;
    const recipeId = event.target.dataset.recipe;
    const done = recipeDone(recipeId);
    if (event.target.checked) done.add(event.target.dataset.id);
    else done.delete(event.target.dataset.id);
    storageSet(`alexandria-recipe:${recipeId}`, Array.from(done));
    const progress = document.getElementById("recipe-progress");
    const recipe = catalog.recipes.find((item) => item.id === recipeId);
    if (progress && recipe) {
      const total = recipe.steps.filter((step) => step.id).length;
      progress.textContent = `${done.size} de ${total} piezas marcadas. Es un recordatorio local, no un requisito.`;
    }
  });

  document.addEventListener("keydown", (event) => {
    const tag = event.target.tagName;
    if (event.key === "/" && tag !== "INPUT" && tag !== "TEXTAREA" && tag !== "SELECT") {
      event.preventDefault();
      window.__focusSearch = true;
      if ((location.hash || "").startsWith("#/explorar")) {
        const field = document.getElementById("q");
        if (field) field.focus();
        window.__focusSearch = false;
      } else {
        location.hash = "#/explorar";
      }
    }
  });

  window.addEventListener("hashchange", draw);
  if (!location.hash) history.replaceState(null, "", "#/inicio");
  draw();
})();
