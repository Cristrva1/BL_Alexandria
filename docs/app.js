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
    ["inicio", "Inicio"], ["empezar", "Guíame"], ["explorar", "Buscar"], ["rutas", "Por objetivo"],
    ["acceso", "Acceso y costes"], ["guias", "Guías"], ["salas", "Categorías"],
    ["recetas", "Recetas"], ["comparar", "Comparar"], ["novedades", "Novedades"],
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
    const status = item.status === "archived" ? "Archivado" : item.status === "unverified" ? "Referencia sin verificar" : "";
    return `<article class="repo-row">
      <div class="repo-summary"><p class="meta">${esc(catName(item.cat))}${status ? ` · <strong>${esc(status)}</strong>` : ""}</p>
      <h2><a href="#/repo/${encodeURIComponent(item.id)}">${esc(item.name)}</a></h2>
      <p>${esc(item.lead)}</p></div>
      <div class="repo-access"><span class="badge">${esc(label("api", item.access.api))}</span>
      <p class="meta">${esc(label("cost", item.access.cost))} · ${esc(preparation(item))}</p>
      <a href="#/repo/${encodeURIComponent(item.id)}">Ver uso e instalación<span class="sr-only"> de ${esc(item.name)}</span></a></div>
    </article>`;
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
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (_error) { /* Session remains usable without persistent storage. */ }
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
    return AlexandriaSearch.search(catalog.repos, catalog.categories, catalog.discovery.goals, params);
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
      return `<a class="${cls}" href="#/${id}"${id===active?' aria-current="page"':""}>${esc(text)}</a>`;
    }).join("");
    return `<a class="skip" href="#contenido">Saltar al contenido</a>
      <div class="shell">
        <nav class="nav" aria-label="Secciones">
          <a class="brand" href="#/inicio">
            <span class="seal" aria-hidden="true">A</span>
            <span><small>Biblioteca</small><strong>Alexandría</strong></span>
          </a>
          <div class="nav-items">${items}</div>
          <p class="nav-foot">${catalog.counts.repos} repos · ${catalog.counts.categories} salas · ${catalog.counts.recipes} recetas</p>
        </nav>
        <main id="contenido" class="main" tabindex="-1"><div class="wrap">${main}</div></main>
      </div>`;
  }

  function goalLinks(goals) {
    return `<ul class="goal-list">${goals.map(goal => `<li><a href="#/explorar?goal=${esc(goal.id)}"><strong>${esc(goal.title)}</strong><span>${esc(goal.description)}</span></a></li>`).join("")}</ul>`;
  }

  function renderHome() {
    return `<header class="library-intro"><h1>Encuentra lo que necesitas.<br>Entiende cómo usarlo.</h1>
      <p class="lede">${catalog.counts.repos} repositorios de IA y automatización, explicados por su función, su acceso y sus requisitos.</p>
      <search><form id="home-search" class="home-search" action="#/explorar" method="get">
      <label for="home-query">¿Qué quieres hacer?</label><p id="search-help" class="meta">Puedes escribir una tarea o un nombre: transcribir audio, crear presentaciones, n8n…</p>
      <div class="search-line"><input id="home-query" name="q" type="search" aria-describedby="search-help" placeholder="Describe lo que buscas" autocapitalize="none" autocorrect="off" spellcheck="false" enterkeyhint="search"><button class="btn" type="submit">Buscar</button></div></form></search>
      <p class="guided-entry"><a class="btn ghost" href="#/empezar">No sé por dónde empezar: guíame</a><span>Elige una tarea y recibe hasta tres opciones, con su primer paso.</span></p>
    </header>
    <section class="section"><div class="command-row"><h2>Empieza por un resultado</h2><a href="#/rutas">Ver las ${catalog.discovery.goals.length} rutas</a></div>
      ${goalLinks(catalog.discovery.goals.slice(0, 8))}</section>
    <section class="section"><h2>O parte de lo que ya tienes</h2><p>Elige cómo quieres usar la IA y después filtra por tu objetivo.</p>
      <ul class="access-links">${["claude","codex","local_model","no_api"].map(route => `<li><a href="#/explorar?route=${route}">${esc(label("route", route))}</a></li>`).join("")}</ul>
      <p class="meta">Una interfaz local puede usar un modelo remoto. Una suscripción puede admitir unas rutas y no otras. <a href="#/acceso">Entiende acceso y costes</a>.</p></section>
    <section class="section reading-start"><h2>Una biblioteca que te orienta</h2><p>Abre una ficha para entender qué hace, con qué acceso funciona y cómo empezar. Compara hasta tres alternativas; utiliza una receta cuando necesites varias piezas.</p><p><a href="#/guias">Leer las guías</a> · <a href="#/salas">Explorar categorías</a> · <a href="#/novedades">Ver incorporaciones</a></p></section>`;
  }

  function renderGoals() {
    return `<h1>¿Qué quieres conseguir?</h1><p class="lede">No hace falta conocer el nombre del repo. Elige una tarea y compara unos pocos puntos de partida.</p>${goalLinks(catalog.discovery.goals)}`;
  }

  function preparation(item) {
    return catalog.labels.audience[item.getting_started?.audience] || "Consulta los requisitos";
  }

  function renderGuided(params) {
    const goal=catalog.discovery.goals.find(item=>item.id===params.get("goal"));
    const route=params.get("route")||"";
    const picks=AlexandriaSearch.guided(catalog.repos,catalog.categories,catalog.discovery.goals,params);
    const selection=new URLSearchParams();if(goal)selection.set("goal",goal.id);if(route)selection.set("route",route);
    const choices=[["","Todavía no sé: enséñame opciones"],["claude","Ya uso Claude Code"],["codex","Ya uso Codex"],["local_model","Quiero un modelo en mi equipo"],["no_api","Quiero una ruta sin API de IA"],["api","Puedo configurar una API de IA"]];
    return `<h1>Encuentra tu punto de partida</h1><p class="lede">No necesitas saber programar para elegir. Responde dos preguntas y revisa unas pocas opciones antes de instalar.</p>
      <form id="guided-start" class="guided-form" action="#/empezar" method="get">
      <div class="filter-field"><label for="guided-goal">1. ¿Qué quieres conseguir?</label><select id="guided-goal" name="goal" required><option value="">Elige una tarea</option>${catalog.discovery.goals.map(item=>`<option value="${esc(item.id)}"${goal?.id===item.id?" selected":""}>${esc(item.title)}</option>`).join("")}</select></div>
      <div class="filter-field"><label for="guided-route">2. ¿Con qué quieres empezar?</label><select id="guided-route" name="route" aria-describedby="guided-access-help">${choices.map(([value,text])=>`<option value="${value}"${value===route?" selected":""}>${esc(text)}</option>`).join("")}</select><p id="guided-access-help" class="meta">El filtro de Claude Code o Codex muestra rutas documentadas con ese agente. Los servicios conectados pueden tener costes adicionales.</p></div>
      <button class="btn" type="submit">Mostrar mis opciones</button></form>
      ${goal?`<section id="guided-results" class="section" tabindex="-1" aria-labelledby="guided-result-title"><h2 id="guided-result-title">${picks.length?"Hasta tres opciones para comparar":"No hay una ruta documentada con esta combinación"}</h2><p>${esc(goal.description)}</p>
      ${picks.length?`<p class="meta">Se priorizan interfaces, instrucciones para agentes y puntos de partida editoriales. El orden no es una garantía de instalación sencilla.</p><ol class="guided-picks">${picks.map(item=>`<li><article><h3><a href="#/repo/${encodeURIComponent(item.id)}">${esc(item.name)}</a></h3><p>${esc(item.lead)}</p><p><strong>Preparación:</strong> ${esc(preparation(item))}.</p><p><strong>Acceso:</strong> ${esc(label("api",item.access.api))}. ${esc(label("cost",item.access.cost))}.</p><p><strong>Primer paso:</strong> ${esc(item.getting_started?.steps?.[0]||"Abre la ficha y revisa los requisitos.")}</p><a href="#/repo/${encodeURIComponent(item.id)}">Ver pasos y pedir ayuda con ${esc(item.name)}</a></article></li>`).join("")}</ol>`:`<p>Prueba «Todavía no sé» para ver otras formas de acceso o <a href="#/acceso">lee cómo funcionan las cuentas y las APIs</a>.</p>`}<p><a href="${exploreHref(selection)}">Ver todas las coincidencias y sus filtros</a></p></section>`:""}
      <section class="section reading-start"><h2>¿Y después de elegir?</h2><ol><li>Abre la ficha y comprueba acceso, coste y requisitos de equipo.</li><li>Lee «Cómo empezar». Una librería o un servicio puede necesitar ayuda técnica.</li><li>Usa el encargo que trae la ficha para pedir pasos guiados a tu asistente y haz una prueba pequeña.</li></ol><p><a href="#/guia/vocabulario">Entender las palabras: repo, API, skill, MCP…</a></p></section>`;
  }

  function renderReading(id) {
    if (!id) return `<h1>Guías para elegir y empezar</h1><p class="lede">Una entrada sencilla y el detalle técnico cuando lo necesitas.</p><ul class="guide-list">${catalog.reading.map(guide => `<li><h2><a href="#/guia/${esc(guide.id)}">${esc(guide.title)}</a></h2><p>${esc(guide.intro)}</p></li>`).join("")}</ul><p><a href="#/curso">Leer las lecciones de la biblioteca</a> · <a href="#/laboratorio">Practicar comparando alternativas</a></p>`;
    const guide = catalog.reading.find(item => item.id === id);
    if (!guide) return missing("Esa guía no está disponible.", "#/guias");
    return `<article class="reading"><p><a href="#/guias">Todas las guías</a></p><h1>${esc(guide.title)}</h1><p class="lede">${esc(guide.intro)}</p>
      <nav class="reading-toc" aria-label="En esta guía"><h2>En esta guía</h2><ol>${guide.sections.map((section,index) => `<li><a href="#/guia/${esc(id)}?section=${index}">${esc(section.title)}</a></li>`).join("")}</ol></nav>
      ${guide.sections.map((section,index) => `<section id="reading-section-${index}" class="reading-section"><h2>${esc(section.title)}</h2><p>${esc(section.text)}</p></section>`).join("")}
      ${guide.sources ? `<section><h2>Fuentes y fecha</h2><p>Consultadas el ${esc(catalog.access_checked)}. Las condiciones pueden cambiar.</p><ul>${guide.sources.map(source => `<li><a href="${esc(safeUrl(source.url))}" target="_blank" rel="noreferrer">${esc(source.title)}</a></li>`).join("")}</ul></section>` : ""}
      <p><a class="btn" href="#/explorar">Buscar una herramienta</a></p></article>`;
  }

  function renderNew() {
    const items = filtered(new URLSearchParams("sort=new"));
    const dates = Array.from(new Set(items.map(item => item.added_at))).sort().reverse();
    return `<h1>Incorporaciones a Alexandria</h1><p class="lede">Cuándo se añadió cada herramienta a esta biblioteca. Esta fecha no indica cuándo se lanzó el proyecto ni si ya lo descargaste.</p>
      ${dates.map(date => { const rows = items.filter(item => item.added_at === date); return `<section class="section"><h2>${esc(date || "Fecha por confirmar")} <span class="meta">${rows.length} repos</span></h2>${rows.slice(0,12).map(repoCard).join("")}${rows.length>12 ? `<p><a href="#/explorar?sort=new">Ver todas las incorporaciones</a></p>`:""}</section>`; }).join("")}`;
  }

  function renderCourse() {
    const cards = catalog.lessons.map((lesson, index) => `<a class="lesson-link" href="#/curso/${esc(lesson.id)}">
      <span class="meta">${esc(lesson.kicker)} · ${lesson.minutes} min</span>
      <h3>${index + 1}. ${esc(lesson.title)}</h3>
      <p>${esc((lesson.blocks.find((block) => block.type === "p") || {}).text || "")}</p>
    </a>`).join("");
    return `
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
    return `
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
    const rooms = catalog.categories.filter(cat => cat.num > 0).map(cat => `<li><h2><a href="#/explorar?cat=${cat.num}">${esc(cat.title)}</a></h2><p>${esc(cat.description || cat.blurb)}</p><p class="meta">${cat.count} repos · ${(cat.subs || []).length} secciones</p></li>`).join("");
    return `<h1>Explora por tema</h1><p class="lede">Cada repo tiene una categoría principal. Puedes encontrarlo también desde sus objetivos, sus etiquetas o su forma de acceso.</p><ul class="shelf-list">${rooms}</ul>`;
  }

  function selectField(name, title, choices, current) {
    return `<div class="filter-field"><label for="filter-${name}">${esc(title)}</label><select id="filter-${name}" name="${name}">${choices.map(([value,text]) => `<option value="${esc(value)}"${value===current?" selected":""}>${esc(text)}</option>`).join("")}</select></div>`;
  }

  function resultsMarkup(items, params) {
    const size=24, pages=Math.max(1,Math.ceil(items.length/size));
    const page=Math.min(pages,Math.max(1,Math.floor(Number(params.get("page"))||1)));
    const start=(page-1)*size;
    if (!items.length) return `<div class="empty"><h2>No hay coincidencias con estos filtros</h2><p>Prueba una tarea más corta o retira un filtro. <a href="#/explorar">Limpiar filtros</a> · <a href="#/rutas">Buscar por objetivo</a></p></div>`;
    const pageLink = (next,text) => { const query=new URLSearchParams(params);query.set("page",String(next));return `<a class="btn ghost" href="${exploreHref(query)}">${text}</a>`; };
    return `${items.slice(start,start+size).map(repoCard).join("")}<nav class="pagination" aria-label="Páginas de resultados">${page>1?pageLink(page-1,"Anterior"):""}<span>${start+1}–${Math.min(start+size,items.length)} de ${items.length}</span>${page<pages?pageLink(page+1,"Siguiente"):""}</nav>`;
  }

  function renderExplore(params) {
    const items=filtered(params);
    const goal=catalog.discovery.goals.find(item=>item.id===params.get("goal"));
    const category=catByNum[params.get("cat")];
    const chips=[];
    const addChip=(key,text)=>{const next=new URLSearchParams(params);next.delete(key);next.delete("page");if(key==="cat")next.delete("sub");chips.push(`<a class="chip" href="${exploreHref(next)}">${esc(text)} <span aria-hidden="true">×</span><span class="sr-only">: quitar filtro</span></a>`);};
    for(const [key,value] of params){if(key==="q"||key==="page"||key==="sort"||!value)continue;const text=key==="cat"?catName(value):key==="goal"?(goal?.title||value):key==="route"?label("route",value):value;addChip(key,text);}
    const groups=catalog.labels;
    return `<h1>${goal?esc(goal.title):"Busca una herramienta"}</h1><p class="lede">${goal?esc(goal.description):"Busca una tarea, un nombre o una tecnología. Después filtra por acceso y requisitos."}</p>
      <search><form class="library-filters" id="filters" action="#/explorar" method="get">
        <div class="query-field"><label for="q">Buscar en la biblioteca</label><input id="q" type="search" name="q" placeholder="Por ejemplo: transcribir audio" value="${esc(params.get("q")||"")}" autocapitalize="none" autocorrect="off" spellcheck="false" enterkeyhint="search"></div>
        <div class="filter-grid">
        ${selectField("goal","Objetivo",[["","Cualquier objetivo"],...catalog.discovery.goals.map(item=>[item.id,item.title])],params.get("goal")||"")}
        ${selectField("route","Forma de uso",[["","Cualquier acceso"],...Object.entries(groups.route)],params.get("route")||"")}
        ${selectField("cat","Categoría",[["","Todas las categorías"],...catalog.categories.filter(cat=>cat.num>0).map(cat=>[String(cat.num),cat.title])],params.get("cat")||"")}
        ${selectField("sub","Sección",[["","Todas las secciones"],...(category?.subs||[]).map(sub=>[sub.key,sub.title])],params.get("sub")||"")}
        </div>
        <details class="advanced-filters"${["role","setup","status"].some(key=>params.has(key))?" open":""}><summary>Más filtros: tipo, dificultad y estado</summary><div class="filter-grid">
        ${selectField("role","Tipo de herramienta",[["","Cualquier tipo"],...Object.entries(groups.role)],params.get("role")||"")}
        ${selectField("setup","Preparación",[["","Cualquier dificultad"],...Object.entries(groups.setup)],params.get("setup")||"")}
        ${selectField("status","Estado",[["","Todos los estados"],["active","Sin alerta de archivo"],["archived","Archivados"],["unverified","Referencias sin verificar"]],params.get("status")||"")}
        ${selectField("sort","Orden",[["relevance","Adecuación a la búsqueda"],["new","Incorporación reciente"],["name","Nombre"],["stars","Popularidad en GitHub"]],params.get("sort")||"relevance")}
        </div></details><button class="btn filter-submit" type="submit">Aplicar filtros</button>
      </form></search>
      <div class="filters">${chips.join("")}${chips.length?'<a href="#/explorar">Limpiar todo</a>':""}</div>
      <p class="live" id="count" role="status">${items.length} resultados. Las estrellas no determinan la adecuación.</p>
      <div id="results" class="repo-list">${resultsMarkup(items,params)}</div>`;
  }

  function accessSection(item) {
    const a=item.access;
    const rows=[["API de IA",label("api",a.api),a.api_note],["Claude Code",label("client",a.claude_code),""],["Codex",label("client",a.codex),""],["Modelos locales",label("local_model",a.local_model),a.local_note],["Coste",label("cost",a.cost),a.cost_note],["Equipo",label("hardware",a.hardware),a.hardware_note]];
    if(a.other_access)rows.push(["Otras rutas",a.other_access,""]);
    return `<section id="repo-access" class="section" aria-labelledby="access-heading"><h2 id="access-heading">Acceso, coste y equipo</h2><p>${esc(a.scope)}</p><dl class="access-facts">${rows.map(([title,value,note])=>`<div><dt>${esc(title)}</dt><dd><strong>${esc(value)}</strong>${note?`<p>${esc(note)}</p>`:""}</dd></div>`).join("")}</dl><p class="access-explanation">${esc(a.subscription_note)} <a href="#/acceso">Cómo interpretar estas rutas</a>.</p></section>`;
  }

  function startSection(item) {
    const g=item.getting_started||{};
    const source=safeUrl(g.source||item.repo_url);
    const prompt=[`Quiero usar ${item.name} y necesito pasos guiados para una persona sin experiencia técnica.`, `Fuente original: ${source}.`, `La ficha de Alexandría indica: ${preparation(item)}; API de IA: ${label("api",item.access.api)}; Claude Code: ${label("client",item.access.claude_code)}; Codex: ${label("client",item.access.codex)}; modelo local: ${label("local_model",item.access.local_model)}.`, "Lee la documentación actual antes de dar comandos. Pregunta mi sistema operativo y qué resultado busco. Explica si conviene una aplicación lista, una skill o configurar un proyecto. Distingue tu ayuda para instalar de la cuenta o el modelo que usará la herramienta. Comprueba dependencias, costes y límites de la ruta elegida. Guíame una acción a la vez hasta una primera prueba pequeña y verifica el resultado. No inventes paquetes o comandos ni pidas que pegue contraseñas en el chat."].join("\n\n");
    return `<section id="repo-start" class="section"><h2>Cómo empezar</h2><p class="meta">${esc(preparation(item))}. <a href="#/guia/vocabulario">Entender los términos</a>.</p>${g.prerequisites?.length?`<p><strong>Antes de empezar</strong></p><ul>${g.prerequisites.map(text=>`<li>${esc(text)}</li>`).join("")}</ul>`:""}
      ${safeUrl(g.entry_url)?`<p><a class="btn" href="${esc(safeUrl(g.entry_url))}" target="_blank" rel="noreferrer">Abrir la web o descarga indicada por el autor</a></p>`:""}
      ${g.steps?.length?`<ol class="start-steps">${g.steps.map(text=>`<li>${esc(text)}</li>`).join("")}</ol>`:"<p>Consulta la ruta de instalación en la documentación original.</p>"}
      ${g.command&&g.command_status==="documented"?`<p id="command-title"><strong>Comando de entrada documentado</strong></p><pre class="command" role="region" aria-labelledby="command-title" tabindex="0"><code>${esc(g.command)}</code></pre><button class="btn small" type="button" data-action="copy" data-text="${esc(g.command)}">Copiar comando</button><p class="meta">${esc(g.note)}</p>`:""}
      ${source?`<p><a href="${esc(source)}" target="_blank" rel="noreferrer">Abrir instrucciones originales</a></p>`:""}
      <details class="guided-help"><summary>Necesito ayuda paso a paso con esta herramienta</summary><p>Copia este encargo en Claude Code, Codex o tu asistente. Que te ayude a instalar no significa que la aplicación use su suscripción.</p><label for="help-prompt">Encargo para tu asistente</label><textarea id="help-prompt" rows="9" readonly>${esc(prompt)}</textarea><button class="btn small" type="button" data-action="copy" data-text="${esc(prompt)}">Copiar encargo</button><p class="copy-status" role="status"></p></details></section>`;
  }

  function renderRepo(id) {
    const item = repo(id);
    if (!item) return missing("Ese repo no está en la biblioteca.", "#/explorar");
    const compared = compareList().includes(item.id);
    const sameOpening=item.body && item.lead && item.body.toLowerCase().startsWith(item.lead.toLowerCase());
    const bodyText=sameOpening?item.body.slice(item.lead.length).trim():item.body;
    const body=bodyText?paragraphs(bodyText):"";
    const dek=item.lead?`<p class="dek">${esc(item.lead)}</p>`:"";
    const skill = item.role === "skill" || item.role === "directory"
      ? `<p class="aside">${esc(catalog.copy.skill_note)}</p>` : "";
    const prov = item.prov.length
      ? item.prov.map((name) => `<span class="badge">${esc(name)}</span>`).join("")
      : "<span class='meta'>Consulta la ruta de acceso y las fuentes; una lista vacía no confirma ausencia de coste.</span>";
    const tags = (item.tags || []).slice(0, 12).map((tag) => `<a class="badge" href="#/explorar?q=${encodeURIComponent(tag)}">${esc(tag)}</a>`).join("");
    const sourceUrl = safeUrl(item.repo_url);
    const source = sourceUrl
      ? `<a href="${esc(sourceUrl)}" target="_blank" rel="noreferrer">Abrir el repositorio</a>`
      : "<span class='meta'>Sin URL de origen.</span>";
    const confidence = label("confidence", item.install.confidence);
    return `
      <h1>${esc(item.name)}</h1>
      ${dek}
      ${badges(item)}
      <nav class="repo-toc" aria-label="En esta ficha"><a href="#/repo/${encodeURIComponent(item.id)}?section=access">Ver acceso y costes</a><a href="#/repo/${encodeURIComponent(item.id)}?section=start">Ir a los primeros pasos</a></nav>
      ${accessSection(item)}
      ${body?`<div class="section">${body}</div>`:""}
      ${item.how ? `<section class="section"><h2>Cómo funciona</h2><p>${esc(item.how)}</p></section>` : ""}
      ${skill}
      <section class="split">
        <article class="callout yes"><h3>Elige si</h3><p>${item.choose_if ? rich(item.choose_if) : "La ficha todavía no declara este criterio."}</p></article>
        <article class="callout no"><h3>Evítalo si</h3><p>${item.avoid_if ? rich(item.avoid_if) : "La ficha todavía no declara este límite."}</p></article>
      </section>
      ${startSection(item)}
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
      <section class="section"><h2>Fuentes y límites</h2><p>${esc(item.limits || "Revisa los límites de la variante y del proveedor que elijas.")}</p><p class="meta">Acceso revisado el ${esc(item.access.checked_at || "fecha por confirmar")}. Lectura de documentación; no prueba de ejecución.</p><ul>${(item.access.sources||[]).map((url,index)=>`<li><a href="${esc(safeUrl(url))}" target="_blank" rel="noreferrer">Fuente ${index+1}</a></li>`).join("")}</ul></section>
      <details class="section technical-details"><summary>Ampliar ficha técnica y etiquetas</summary>
        <p><strong>Papel.</strong> ${esc(label("role", item.role))}. ${esc(catalog.role_why[item.role] || "")}</p>
        <p><strong>Ejecución.</strong> ${esc(label("exec", item.exec))}.</p>
        <p><strong>Arranque.</strong> ${esc(label("setup", item.setup))}.</p>
        <p><strong>Stack.</strong> ${item.stack ? esc(item.stack) : "No declarado."}</p>
        <p><strong>Proveedor.</strong> ${prov}</p>
        ${tags ? `<p><strong>Etiquetas.</strong></p><div class="badges">${tags}</div>` : ""}
        <p>${source}${item.doc ? ` · En esta biblioteca: <code>${esc(item.doc)}</code>` : ""}</p>
      </details><p><button class="btn small" type="button" data-action="compare" data-id="${esc(item.id)}">${compared ? "Quitar de comparar" : "Añadir a comparar"}</button> <a href="#/comparar">Abrir comparación</a></p>`;
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
    return `
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
    return `
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
    return `
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
      <label for="compare-repo">Añadir una herramienta a la comparación</label>
      <select id="compare-repo" name="repo_id">
        <option value="">Añadir un repo…</option>
        ${catalog.repos.map((item) => `<option value="${esc(item.id)}">${esc(item.name)}</option>`).join("")}
      </select>
      <button class="btn small" type="submit">Añadir</button>
    </form>`;
    if (!ids.length) {
      return `<h1>Pon hasta tres fichas juntas</h1>
        <p class="lede">Sirve para desempatar, no para sumar. Si dos repos son alternativas, quédate con uno.</p>
        ${picker}<p class="empty">Todavía no hay repos en la mesa. Ábrelos desde una ficha o elige uno aquí.</p>`;
    }
    const rows = [
      ["Oficio", (item) => esc(item.lead)],
      ["Papel", (item) => esc(label("role", item.role))],
      ["Ejecución", (item) => esc(label("exec", item.exec))],
      ["Arranque", (item) => esc(label("setup", item.setup))],
      ["API de IA", item => esc(label("api", item.access.api))],
      ["Claude Code", item => esc(label("client", item.access.claude_code))],
      ["Codex", item => esc(label("client", item.access.codex))],
      ["Modelo local", item => esc(label("local_model", item.access.local_model))],
      ["Coste", item => esc(item.access.cost_note)],
      ["Equipo", item => esc(item.access.hardware_note)],
      ["Elige si", (item) => item.choose_if ? rich(item.choose_if) : "—"],
      ["Evítalo si", (item) => item.avoid_if ? rich(item.avoid_if) : "—"],
      ["Stack", (item) => esc(item.stack || "—")],
    ];
    const head = ids.map((id) => `<th scope="col"><a href="#/repo/${encodeURIComponent(id)}">${esc(repo(id).name)}</a><br><button class="btn small ghost" type="button" data-action="compare" data-id="${esc(id)}">Quitar</button></th>`).join("");
    const body = rows.map(([name, cell]) => `<tr><th scope="row">${name}</th>${ids.map((id) => `<td>${cell(repo(id))}</td>`).join("")}</tr>`).join("");
    return `
      <h1>Míralos en la misma mesa</h1>
      <p class="lede">Si comparten oficio, no los instales juntos. Lee «Evítalo si» antes de quedarte con los dos.</p>
      ${picker}
      <p class="mobile-hint meta">Si no ves todas las columnas, desliza la tabla hacia los lados.</p><div class="table-wrap" role="region" aria-label="Tabla de comparación desplazable" tabindex="0"><table class="compare"><caption>Comparación de función, acceso y requisitos</caption><thead><tr><th scope="col">Criterio</th>${head}</tr></thead><tbody>${body}</tbody></table></div>`;
  }

  function missing(text, href) {
    return `<h1>No está en el estante</h1><p class="lede">${esc(text)}</p><p><a href="${href}">Volver</a></p>`;
  }

  function activeOf(parts) {
    const head = parts[0] || "inicio";
    if (head === "repo") return "explorar";
    if (["curso","guia","laboratorio"].includes(head)) return "guias";
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
    return nav ? nav[1] : "Alexandría";
  }

  function view(route) {
    const [head, second] = route.parts;
    if (!head || head === "inicio") return renderHome();
    if (head === "curso") return second ? renderLesson(second) : renderCourse();
    if (head === "rutas") return renderGoals();
    if (head === "empezar") return renderGuided(route.params);
    if (head === "guias") return renderReading();
    if (head === "guia") return renderReading(second);
    if (head === "acceso") return renderReading("acceso");
    if (head === "novedades") return renderNew();
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
    const items=filtered(params), results=document.getElementById("results"), count=document.getElementById("count");
    if (!results||!count) return;
    results.innerHTML=resultsMarkup(items,params);
    count.textContent=`${items.length} resultados. Las estrellas no determinan la adecuación.`;
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

  let lastPath=null;
  function draw() {
    clearTimeout(searchTimer);
    const route = parseHash();
    document.getElementById("app").innerHTML = layout(activeOf(route.parts), view(route));
    document.title = `${titleOf(route.parts)} — Alexandría`;
    const path=route.parts.join("/");
    if(path!==lastPath){
      const heading=document.querySelector("main h1");
      if(heading){heading.tabIndex=-1;if(lastPath!==null)heading.focus({preventScroll:true});}
      window.scrollTo({top:0,behavior:"instant"});
    }
    lastPath=path;
    const section=route.params.get("section");
    if(section!==null){const target=document.getElementById(route.parts[0]==="repo"?`repo-${section}`:`reading-section-${section}`);if(target){target.tabIndex=-1;target.focus({preventScroll:true});target.scrollIntoView();}}
    const q = document.getElementById("q");
    if (q && route.parts[0] === "explorar" && window.__focusSearch) {
      q.focus();
      window.__focusSearch = false;
    }
  }

  let searchTimer;
  document.getElementById("app").addEventListener("input", (event) => {
    if(event.target.id!=="q" || event.isComposing)return;
    clearTimeout(searchTimer);
    searchTimer=setTimeout(()=>{
      const params=currentParamsFromForm();paintExplore(params);
      const href=exploreHref(params);if(location.hash!==href)history.replaceState(null,"",href);
    },220);
  });

  document.getElementById("app").addEventListener("submit", (event) => {
    if(event.target.id === "guided-start") {
      event.preventDefault();const params=new URLSearchParams(new FormData(event.target));
      if(!params.get("route"))params.delete("route");
      history.pushState(null,"",`#/empezar?${params.toString()}`);draw();
      const results=document.getElementById("guided-results");if(results){results.focus({preventScroll:true});results.scrollIntoView({block:"start"});}
    }
    if (event.target.id === "compare-add") {
      event.preventDefault();
      const id = new FormData(event.target).get("repo_id");
      if (!id) return;
      const list = compareList().filter((item) => item !== id);
      list.push(String(id));
      storageSet("alexandria-compare", list.slice(-3));
      draw();
    }
    if (event.target.id === "home-search") {
      event.preventDefault();
      const params=new URLSearchParams(); const q=new FormData(event.target).get("q");
      if(q)params.set("q",String(q));location.hash=exploreHref(params).slice(1);
    }
    if (event.target.id === "filters") {
      event.preventDefault();const params=currentParamsFromForm();params.delete("page");
      const cat=catByNum[params.get("cat")];if(!cat?.subs.some(sub=>sub.key===params.get("sub")))params.delete("sub");
      history.pushState(null,"",exploreHref(params));
      document.activeElement?.blur();draw();
      const count=document.getElementById("count");if(count){count.tabIndex=-1;count.focus();}
    }
  });

  document.getElementById("app").addEventListener("click", async (event) => {
    if(event.target.closest("a.skip")){event.preventDefault();document.getElementById("contenido").focus();return;}

    const button = event.target.closest("[data-action]");
    if (!button) return;
    const action = button.dataset.action;
    if (action === "copy") {
      const text = button.dataset.text || "";
      try {
        await navigator.clipboard.writeText(text);
        button.textContent = "Copiado";
      } catch (_error) {
        button.textContent = "Selecciona y copia el texto";
      }
      const status=button.parentElement.querySelector(".copy-status");if(status)status.textContent=button.textContent==="Copiado"?"Encargo copiado. Ya puedes pegarlo en tu asistente.":"Selecciona el texto del encargo y cópialo manualmente.";
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
    if(event.target.name === "cat") {
      const sub=document.getElementById("filter-sub"),cat=catByNum[event.target.value];
      if(sub)sub.innerHTML='<option value="">Todas las secciones</option>'+(cat?.subs||[]).map(item=>`<option value="${esc(item.key)}">${esc(item.title)}</option>`).join("");
    }
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
