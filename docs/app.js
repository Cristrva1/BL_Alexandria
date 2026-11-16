(function () {
  const raw = document.getElementById("catalog-data").textContent;
  const catalog = JSON.parse(raw);
  const byId = Object.fromEntries(catalog.repos.map((repo) => [repo.id, repo]));
  const catByNum = Object.fromEntries(catalog.categories.map((cat) => [String(cat.num), cat]));
  const areas = catalog.discovery.areas || [];
  const areaById = Object.fromEntries(areas.map(area => [area.id, area]));
  const topicById = Object.fromEntries(areas.flatMap(area => area.topics.map(topic => [topic.id, {...topic,area:area.id}])));
  const folded = new Map();
  for (const repo of catalog.repos) {
    folded.set(norm(repo.id), repo.id);
  }

  const NAV = [
    ["inicio", "Inicio"], ["empezar", "Guíame"], ["explorar", "Buscar"], ["rutas", "Por objetivo"],
    ["acceso", "Acceso y costes"], ["guias", "Guías"], ["configurar", "Configurar IA"],
    ["prompts", "Prompts y comandos"], ["tecnicas", "Técnicas e ideas"], ["servicios", "Servicios y despliegue"], ["salas", "Categorías"],
    ["recetas", "Recetas"], ["comparar", "Comparar"], ["novedades", "Novedades"],
  ];
  const NAV_GROUPS = [
    ["Empieza", ["inicio", "empezar", "rutas", "acceso"]],
    ["Explora", ["explorar", "salas", "recetas", "comparar", "novedades"]],
    ["Aprende y trabaja", ["guias", "tecnicas", "prompts"]],
    ["Configura", ["configurar", "servicios"]],
  ];
  const NAV_ICONS = {inicio:"🏛️",empezar:"🧭",explorar:"🔎",rutas:"🎯",acceso:"🔑",guias:"📖",configurar:"🛠️",prompts:"💬",tecnicas:"💡",servicios:"🚀",salas:"🗂️",recetas:"🧪",comparar:"⚖️",novedades:"✨"};
  // Visual identity per practical area: an icon and an OKLCH hue (lightness comes from the theme).
  const AREA_STYLE = {
    frontend:["🎨",295], ciberseguridad:["🛡️",25], audiovisual:["🎬",345], trading:["📈",150], automatizacion:["⚙️",65],
    agentes:["🤖",255], "ia-local":["🏠",190], documentos:["📄",48], datos:["📊",225], productividad:["🗂️",115],
    desarrollo:["🧑‍💻",275], vision:["👁️",30], aprender:["🧠",85],
    "configurar-claude-code":["✳️",38], "configurar-codex":["◎",205], "configurar-antigravity":["🪐",310],
  };
  const GOAL_ICONS = {programar:"💻",automatizar:"⚙️",whatsapp:"💬",documentos:"📎",investigar:"🔎",local:"🦙",web:"🌐",video:"🎬",voz:"🎙️",narrar:"🗣️",imagenes:"🖼️",presentaciones:"📽️",diagramas:"🧭",datos:"📈",mcp:"🔌",skills:"🧩",aprender:"📚",finanzas:"💹",notas:"🗒️",servicios:"🖥️",seguridad:"🛡️","3d":"🧊"};
  const RECIPE_STYLE = {"bot-de-whatsapp-con-ia":["💬",150],"pipeline-de-reels-video-corto":["🎬",345],"agente-de-research-profundo":["🔎",255],"workspace-privado-local-soberano":["🏠",190],"analisis-de-repos-grandes":["🧠",275],"marketing-de-agencia":["📣",25],"web-app-moderna-con-ia":["🌐",295],"construir-una-appservidor-mcp":["🔌",205],"documentos-presentaciones":["📽️",48],"chatgpt-privado-local":["🦙",170],"rag-sobre-documentos":["📎",85],"agente-de-codigo-potenciado":["🛠️",38],"agente-de-voz":["📞",320],"analitica-con-ia":["📊",225]};
  const EXAMPLES = [
    {icon:"💬",h:150,title:"Atender clientes por WhatsApp",text:"Un asistente responde preguntas frecuentes, guarda los datos de contacto y pasa la conversación a una persona cuando hace falta.",goal:"whatsapp",recipe:"bot-de-whatsapp-con-ia"},
    {icon:"📽️",h:48,title:"Convertir un PDF en presentación",text:"Extrae el texto de un informe largo y genera diapositivas editables que puedes revisar antes de presentarlas.",goal:"presentaciones",recipe:"documentos-presentaciones"},
    {icon:"🎬",h:345,title:"Subtitular y recortar videos cortos",text:"Transcribe el audio, añade subtítulos y prepara versiones verticales para Reels o TikTok.",goal:"video",recipe:"pipeline-de-reels-video-corto"},
    {icon:"🦙",h:170,title:"Un ChatGPT privado en tu computadora",text:"Conversa con modelos que se ejecutan en tu equipo, sin enviar tus documentos a un servicio externo.",goal:"local",recipe:"chatgpt-privado-local"},
    {icon:"📎",h:85,title:"Preguntar a tus manuales y contratos",text:"Carga documentos propios y obtén respuestas que citan el fragmento de donde salen.",goal:"documentos",recipe:"rag-sobre-documentos"},
    {icon:"🔎",h:255,title:"Investigar un tema con fuentes",text:"Un agente busca en la web, lee varias páginas y redacta un informe con enlaces para comprobarlo.",goal:"investigar",recipe:"agente-de-research-profundo"},
  ];
  function toneStyle(h) { return h===undefined?"":` style="--h:${Number(h)}"`; }
  function areaIcon(id) { return (AREA_STYLE[id]||["📚"])[0]; }
  function areaTone(id) { return toneStyle((AREA_STYLE[id]||[])[1]); }

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
    const area = (item.areas || []).find(id => areaById[id]?.kind === "work") || (item.areas || [])[0];
    return `<article class="repo-row"${areaTone(area)}>
      <div class="repo-summary"><p class="meta">${area && areaById[area] ? `${areaIcon(area)} ${esc(areaById[area].title)}` : esc(catName(item.cat))}${status ? ` · <strong>${esc(status)}</strong>` : ""}</p>
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

  const sessionData = {};
  function storageGet(key, fallback) {
    try {
      const value = localStorage.getItem(key);
      return value ? JSON.parse(value) : sessionData[key] ?? fallback;
    } catch (_error) {
      return sessionData[key] ?? fallback;
    }
  }

  function storageSet(key, value) {
    sessionData[key] = value;
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (_error) { /* Session remains usable without persistent storage. */ }
  }

  function compareList() {
    const route=parseHash();
    return AlexandriaDecisions.ids(route.parts[0]==="comparar" && route.params.has("ids") ? route.params.get("ids") : storageGet("alexandria-compare", []),byId);
  }

  function recipeDone(id) {
    const saved=storageGet(`alexandria-recipe:${id}`, []);
    return new Set(Array.isArray(saved)?saved:[]);
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
    const navText = Object.fromEntries(NAV);
    const item = (id) => `<li><a class="${id === active ? "item active" : "item"}" href="#/${id}"${id===active?' aria-current="page"':""}><span class="ico" aria-hidden="true">${NAV_ICONS[id]||"•"}</span>${esc(navText[id])}</a></li>`;
    const groups = NAV_GROUPS.map(([title, ids]) => `<section class="nav-group"><h2>${esc(title)}</h2><ul>${ids.map(item).join("")}</ul></section>`).join("");
    const extras = (catalog.handbook?.prompts?.length || 0);
    const techniques = (catalog.techniques?.items?.length || 0);
    return `<a class="skip" href="#contenido">Saltar al contenido</a>
      <div class="shell">
        <nav class="nav" aria-label="Secciones">
          <a class="brand" href="#/inicio">
            <img class="brand-mark" src="marca/bl-mark-dark.png" alt="" width="61" height="44">
            <span><small>Binarias Labs</small><strong>Alexandría</strong></span>
          </a>
          <button class="nav-toggle" type="button" data-action="nav-toggle" aria-expanded="false" aria-controls="nav-items"><span class="bars" aria-hidden="true"><i></i><i></i><i></i></span>Menú</button>
          <div class="nav-items" id="nav-items">${groups}</div>
          <p class="nav-foot">${catalog.counts.repos} repos · ${areas.length || catalog.counts.categories} áreas${areas.length ? ` · ${catalog.counts.topics} subcategorías` : ""}<br>${extras} prompts · ${techniques} técnicas</p>
        </nav>
        <main id="contenido" class="main" tabindex="-1"><div class="wrap">${main}<p id="app-feedback" class="meta" role="status"></p>${siteFooter()}</div></main>
      </div>`;
  }

  function siteFooter() {
    return `<footer class="site-foot"><div><h2>Biblioteca de Alexandría</h2><p>Un menú curado de ${catalog.counts.repos} repositorios de IA y automatización, explicado para personas que empiezan. Cada ficha separa qué hace, qué acceso necesita y cómo hacer una primera prueba.</p><p class="meta">Revisión documental: las instalaciones y los rendimientos no se ejecutaron en Alexandría. Comprueba siempre la fuente original.</p></div>
      <div><h2>Empieza</h2><ul><li><a href="#/empezar">Guíame paso a paso</a></li><li><a href="#/guia/vocabulario">Vocabulario básico</a></li><li><a href="#/acceso">Acceso y costes</a></li><li><a href="#/recetas">Recetas completas</a></li></ul></div>
      <div><h2>Trabaja mejor</h2><ul><li><a href="#/tecnicas">Técnicas e ideas</a></li><li><a href="#/prompts">Plantillas de prompts</a></li><li><a href="#/prompts?type=commands">Comandos documentados</a></li><li><a href="https://github.com/Cristrva1/BL_Alexandria" target="_blank" rel="noreferrer">Código en GitHub</a></li></ul></div>
      <div class="foot-brand"><picture><source srcset="marca/binarias-labs-dark.png" media="(prefers-color-scheme: dark)"><img src="marca/binarias-labs.png" alt="Binarias Labs" width="198" height="50" loading="lazy" decoding="async"></picture><p>Un proyecto de <strong>Binarias Labs</strong>. Tecnología que integra posibilidades.</p></div></footer>`;
  }

  function goalLinks(goals) {
    return `<ul class="goal-list">${goals.map(goal => `<li><a href="#/rutas?goal=${esc(goal.id)}"><strong>${esc(goal.title)}</strong><span>${esc(goal.description)}</span></a></li>`).join("")}</ul>`;
  }

  function areaCard(area, index=0) {
    const topics = area.topics.slice(0, 3).map(topic => `<span>${esc(topic.title)}</span>`).join("");
    return `<li class="rise" style="--i:${index}"><a class="area-card"${areaTone(area.id)} href="#/area/${esc(area.id)}"><span class="head"><span class="icon-tile" aria-hidden="true">${areaIcon(area.id)}</span><h3>${esc(area.title)}</h3></span><p>${esc(area.description)}</p><span class="topics">${topics}</span><span class="foot"><span>${area.topics.length} subcategorías</span><b>${area.count} repos →</b></span></a></li>`;
  }

  function recipeTile(recipe, index=0) {
    const [icon, hue] = RECIPE_STYLE[recipe.id] || ["🧪", 40];
    const pieces = (recipe.plan?.minimum?.length ? recipe.plan.minimum : recipe.steps.filter(s => s.id).map(s => s.id)).slice(0, 4);
    return `<li class="rise" style="--i:${index}"><a class="recipe-card"${toneStyle(hue)} href="#/receta/${esc(recipe.id)}"><span class="head"><span class="icon-tile" aria-hidden="true">${icon}</span><h3>${esc(recipe.title)}</h3></span><p>${esc(recipe.goal)}</p><span class="pieces">${pieces.map(id => `<span>${esc(repo(id)?.name || id)}</span>`).join("")}</span><span class="foot">${pieces.length} piezas para empezar · ${recipe.steps.length} en el recorrido completo</span></a></li>`;
  }

  function promptPreview(prompt) {
    return `<li><a href="#/prompts?topic=${esc(prompt.topic)}">${esc(prompt.title)}</a><p>${esc(prompt.when)}</p><div class="decision-actions" style="margin-block:.5rem 0"><button class="btn small ghost" type="button" data-action="copy" data-text="${esc(prompt.body)}">Copiar plantilla</button><span class="copy-status meta" role="status"></span></div></li>`;
  }

  function renderHome() {
    const work = areas.filter(area => area.kind === "work");
    const tools = areas.filter(area => area.kind === "tool");
    const techniques = catalog.techniques?.items || [];
    const featuredTech = (techniques.filter(t => t.featured).length ? techniques.filter(t => t.featured) : techniques).slice(0, 4);
    const prompts = catalog.handbook?.prompts || [];
    const featuredPrompts = (prompts.filter(p => p.featured).length ? prompts.filter(p => p.featured) : prompts).slice(0, 3);
    const groups = catalog.discovery.goal_groups || [];
    const goalById = Object.fromEntries(catalog.discovery.goals.map(g => [g.id, g]));
    const queries = ["transcribir audio", "bot de WhatsApp", "presentación desde PDF", "modelo local", "automatizar flujos", "subtítulos"];
    const stats = [
      [catalog.counts.repos, "repos curados", "#/explorar"], [catalog.counts.work_areas || areas.length, "áreas de trabajo", "#/salas"],
      [catalog.counts.topics, "subcategorías", "#/salas"], [catalog.counts.recipes, "recetas completas", "#/recetas"],
      [prompts.length, "plantillas de prompts", "#/prompts"], [techniques.length, "técnicas e ideas", "#/tecnicas"],
    ];
    const paths = [
      {h:150,icon:"🌱",title:"Nunca he usado estas herramientas",text:"Te explicamos los términos, qué cuesta cada pieza y te proponemos una primera prueba pequeña.",links:[["#/empezar","Guíame con mi proyecto"],["#/guia/vocabulario","Entender el vocabulario"],["#/acceso","Qué es una API, una suscripción o un modelo local"]]},
      {h:40,icon:"🛠️",title:"Quiero crear algo concreto",text:"Parte del resultado que buscas y combina pocas piezas con un propósito claro.",links:[["#/rutas","Elegir por objetivo"],["#/recetas","Seguir una receta completa"],["#/comparar","Comparar alternativas"]]},
      {h:255,icon:"🤖",title:"Ya trabajo con un agente",text:"Mejora Claude Code, Codex o Antigravity con técnicas, plantillas y comandos documentados.",links:[["#/tecnicas","Técnicas e ideas"],["#/prompts","Plantillas de prompts"],["#/configurar","Configurar agentes y modelos"]]},
    ];
    return `<header class="hero">
      <div class="library-intro rise">
        <p class="eyebrow">Biblioteca de Alexandría · catálogo educativo de IA</p>
        <h1>Encuentra lo que necesitas.<br><span class="ink-gradient">Entiende cómo usarlo.</span></h1>
        <p class="lede">${catalog.counts.repos} repositorios de IA y automatización, explicados por su función, su acceso y sus requisitos. Con recetas, técnicas y plantillas para pasar de la idea a una primera prueba.</p>
        <search><form id="home-search" class="home-search" action="#/explorar" method="get">
          <label for="home-query">¿Qué quieres hacer?</label><p id="search-help" class="meta">Escribe una tarea o un nombre. Pulsa <kbd>/</kbd> en cualquier página para buscar.</p>
          <div class="search-line"><input id="home-query" name="q" type="search" aria-describedby="search-help" placeholder="Por ejemplo: transcribir una reunión" autocapitalize="none" autocorrect="off" spellcheck="false" enterkeyhint="search"><button class="btn" type="submit">Buscar <span class="arrow" aria-hidden="true">→</span></button></div></form></search>
        <p class="quick-queries"><span>Prueba:</span>${queries.map(q => `<a class="chip" href="#/explorar?q=${encodeURIComponent(q)}">${esc(q)}</a>`).join("")}</p>
        <div class="hero-ctas"><a class="btn" href="#/empezar">No sé por dónde empezar: guíame <span class="arrow" aria-hidden="true">→</span></a><a class="btn ghost" href="#/recetas">Ver recetas completas</a></div>
      </div>
      <aside class="hero-panel rise" style="--i:3" aria-labelledby="stats-title"><h2 id="stats-title">La biblioteca en cifras</h2><ul class="stats">${stats.map(([n, text, href]) => `<li><a href="${href}"><strong>${esc(n)}</strong><span>${esc(text)}</span></a></li>`).join("")}</ul>
        ${catalog.discovery.editorial_review?`<p class="meta">${catalog.discovery.editorial_review.reviewed} fichas revisadas una a una en fuentes de sus autores · ${esc(catalog.discovery.editorial_review.date)}. Instalaciones no ejecutadas.</p>`:""}</aside>
    </header>

    <section class="section reveal" aria-labelledby="paths-title"><div class="section-head"><div><h2 id="paths-title">Elige cómo empezar</h2><p>Tres entradas según tu experiencia. Puedes cambiar de camino cuando quieras.</p></div></div>
      <div class="path-grid">${paths.map((path, i) => `<article class="path-card rise" style="--h:${path.h};--i:${i}"><span class="icon-tile big" aria-hidden="true">${path.icon}</span><h3>${esc(path.title)}</h3><p>${esc(path.text)}</p><ul>${path.links.map(([href, text]) => `<li><a href="${href}">${esc(text)}</a></li>`).join("")}</ul></article>`).join("")}</div></section>

    ${work.length ? `<section class="section reveal" aria-labelledby="areas-title"><div class="section-head"><div><h2 id="areas-title">Explora un área de trabajo</h2><p>Cada área se divide en subcategorías con tareas concretas. Un repo puede aparecer en varias.</p></div><a class="more" href="#/salas">Ver categorías y subcategorías →</a></div>
      <ul class="area-grid" role="list">${work.map(areaCard).join("")}</ul></section>` : ""}

    <section class="section reveal" aria-labelledby="examples-title"><div class="section-head"><div><h2 id="examples-title">Ideas para tu primer proyecto</h2><p>Ejemplos reales de lo que puedes construir. Cada uno enlaza su receta y una recomendación guiada.</p></div></div>
      <ul class="example-grid" role="list">${EXAMPLES.filter(e => catalog.recipes.some(r => r.id === e.recipe)).map((e, i) => `<li class="rise" style="--i:${i}"><article class="example-card"${toneStyle(e.h)}><span class="head"><span class="icon-tile" aria-hidden="true">${e.icon}</span><h3>${esc(e.title)}</h3></span><p>${esc(e.text)}</p><span class="links"><a href="#/receta/${esc(e.recipe)}">Ver la receta</a>${goalById[e.goal] ? `<a href="#/empezar?goal=${esc(e.goal)}">Pedir recomendación</a>` : ""}</span></article></li>`).join("")}</ul></section>

    <section class="section reveal" aria-labelledby="recipes-title"><div class="section-head"><div><h2 id="recipes-title">Recetas: varias piezas, un propósito</h2><p>Qué hace cada herramienta, con cuáles empezar y qué comprobar en la primera prueba.</p></div><a class="more" href="#/recetas">Ver las ${catalog.recipes.length} recetas →</a></div>
      <ul class="recipe-grid" role="list">${catalog.recipes.slice(0, 6).map(recipeTile).join("")}</ul></section>

    <section class="section reveal" aria-labelledby="craft-title"><div class="section-head"><div><h2 id="craft-title">Técnicas, prompts y comandos</h2><p>Formas de trabajar con agentes que ahorran tiempo y tokens, reescritas con fuente y advertencias.</p></div></div>
      <div class="duo">
        <article class="panel"><h3><span class="icon-tile" style="--h:85" aria-hidden="true">💡</span>Técnicas e ideas</h3><ul class="mini-list">${featuredTech.map(t => `<li><a href="#/tecnica/${esc(t.id)}">${esc(t.title)}</a><p>${esc(t.summary)}</p></li>`).join("") || "<li><p>Próximamente.</p></li>"}</ul><a class="btn small" href="#/tecnicas">Ver todas las técnicas <span class="arrow" aria-hidden="true">→</span></a></article>
        <article class="panel"><h3><span class="icon-tile" style="--h:255" aria-hidden="true">💬</span>Plantillas listas para copiar</h3><ul class="mini-list">${featuredPrompts.map(promptPreview).join("")}</ul><a class="btn small" href="#/prompts">Ver las ${prompts.length} plantillas <span class="arrow" aria-hidden="true">→</span></a> <a href="#/prompts?type=commands" style="margin-left:.6rem">Comandos documentados</a></article>
      </div></section>

    ${tools.length ? `<section class="section reveal" aria-labelledby="tools-title"><div class="section-head"><div><h2 id="tools-title">Configura tu asistente</h2><p>Colecciones para ampliar Claude Code, Codex o Antigravity, y guías para elegir agentes, modelos, IA local y teléfonos.</p></div><a class="more" href="#/configurar">Abrir Configurar IA →</a></div>
      <ul class="area-grid" role="list">${tools.map(areaCard).join("")}</ul></section>` : ""}

    ${groups.length ? `<section class="section reveal" aria-labelledby="goals-title"><div class="section-head"><div><h2 id="goals-title">Empieza por un resultado</h2><p>${catalog.discovery.goals.length} objetivos agrupados por lo que quieres conseguir.</p></div><a class="more" href="#/rutas">Ver todas las rutas →</a></div>
      <div class="goal-columns">${groups.map(group => `<div><h3>${esc(group.title)}</h3><ul>${group.goals.map(id => goalById[id]).filter(Boolean).map(g => `<li><a href="#/rutas?goal=${esc(g.id)}"><span class="ico" aria-hidden="true">${GOAL_ICONS[g.id] || "•"}</span>${esc(g.title)}</a></li>`).join("")}</ul></div>`).join("")}</div></section>` : `<section class="section"><h2>Empieza por un resultado</h2>${goalLinks(catalog.discovery.goals.slice(0, 8))}</section>`}

    <section class="section reveal" aria-labelledby="access-title"><div class="section-head"><div><h2 id="access-title">O parte de lo que ya tienes</h2><p>Elige cómo quieres usar la IA y después filtra por tu objetivo.</p></div><a class="more" href="#/acceso">Entender acceso y costes →</a></div>
      <ul class="access-links">${[["claude","✳️"],["codex","◎"],["antigravity","🪐"],["local_model","🏠"],["no_api","🔓"]].map(([route, icon]) => `<li><a href="#/explorar?route=${route}"><span aria-hidden="true">${icon}</span>${esc(label("route", route))}</a></li>`).join("")}</ul>
      <p class="meta">Una interfaz local puede usar un modelo remoto. Una suscripción puede admitir unas rutas y no otras.</p></section>`;
  }

  const accessChoices = [["","Sin preferencia de acceso"],["claude","Con Claude Code"],["codex","Con Codex"],["antigravity","Con Antigravity"],["local_model","Con modelos locales"],["no_api","Sin clave propia de API de IA"],["api","Con API de IA"]];
  function routeOptions(current,empty=true) { return accessChoices.filter(([id])=>empty||id).map(([id,text])=>`<option value="${id}"${id===current?" selected":""}>${esc(text)}</option>`).join(""); }
  function goalOptions(current,empty="Todos los objetivos") { return `<option value="">${empty}</option>`+catalog.discovery.goals.map(g=>`<option value="${esc(g.id)}"${g.id===current?" selected":""}>${esc(g.title)}</option>`).join(""); }
  function comparisonHref(ids) { return AlexandriaDecisions.href(ids,byId); }
  function pickList(items) {
    return `<ol class="decision-picks">${items.map(item=>`<li><article><h3><a href="#/repo/${esc(item.id)}">${esc(item.name)}</a></h3><p>${esc(item.lead)}</p><p class="meta">${esc(preparation(item))} · ${esc(label("cost",item.access.cost))}</p><p><strong>Primera prueba:</strong> ${esc(item.first_try?.action||"Revisa el ejemplo de la documentación original.")}</p><a href="#/repo/${esc(item.id)}?section=start">Revisar requisitos y primeros pasos</a></article></li>`).join("")}</ol>`;
  }
  function renderGoals(params) {
    const goal=catalog.discovery.goals.find(g=>g.id===params.get("goal"));
    const route=accessChoices.some(([id])=>id===params.get("route"))?params.get("route"):"";
    const context=new URLSearchParams();if(route)context.set("route",route);
    const filters=`<form id="goal-context" class="decision-form"><div><label for="objective-goal">Qué quieres conseguir</label><select id="objective-goal" name="goal">${goalOptions(goal?.id,"Elige un objetivo")}</select></div><div><label for="objective-route">Cómo quieres usarlo</label><select id="objective-route" name="route">${routeOptions(route)}</select></div><button class="btn" type="submit">Ver mi ruta</button></form>`;
    if(goal){
      context.set("goal",goal.id);
      const picks=AlexandriaSearch.guided(catalog.repos,catalog.categories,catalog.discovery.goals,context);
      const related=catalog.recipes.filter(r=>(goal.recipe_ids||[]).includes(r.id));
      return `<p class="breadcrumbs"><a href="#/rutas${route?`?route=${esc(route)}`:""}">Todos los objetivos</a></p><h1><span aria-hidden="true">${GOAL_ICONS[goal.id]||""}</span> ${esc(goal.title)}</h1><p class="lede">${esc(goal.description)}</p>${filters}
        <section class="decision-brief"><h2>Antes de elegir una herramienta</h2><dl><div><dt>Resultado buscado</dt><dd>${esc(goal.outcome||goal.description)}</dd></div><div><dt>Qué preparar</dt><dd>${esc(goal.bring||"Una tarea y datos de prueba")}</dd></div><div><dt>La decisión importante</dt><dd>${esc(goal.decision||"¿Qué parte de tu tarea necesita resolver esta herramienta?")}</dd></div></dl></section>
        <section class="section"><h2>${picks.length?"Pocos puntos de partida, con funciones distintas":"No hay un punto de partida documentado con este acceso"}</h2><p class="meta">Selección editorial de hasta tres opciones. Revisa sus funciones: no todas son sustitutas ni tienen la misma preparación.</p>${picks.length?pickList(picks):`<p>Cambia la forma de acceso para explorar otras rutas. La ausencia de una coincidencia no demuestra incompatibilidad.</p>`}<div class="decision-actions">${picks.length>1?`<a class="btn" href="${comparisonHref(picks.map(p=>p.id))}">Comparar funciones de estas opciones</a>`:""}<a href="${exploreHref(context)}">Ver todas las herramientas para este objetivo</a></div></section>
        ${related.length?`<section class="section"><h2>Si necesitas un flujo completo</h2><ul class="related-recipes">${related.map(r=>`<li><a href="#/receta/${esc(r.id)}">${esc(r.title)}</a><p>${esc(r.goal)}</p></li>`).join("")}</ul></section>`:""}`;
    }
    const groups=[...(catalog.discovery.goal_groups||[])];
    const grouped=new Set(groups.flatMap(g=>g.goals)),other=catalog.discovery.goals.filter(g=>!grouped.has(g.id)).map(g=>g.id);
    if(other.length)groups.push({id:"otros",title:"Otros objetivos",goals:other});
    return `<h1>Empieza por el resultado</h1><p class="lede">Elige qué quieres conseguir. Te ayudaremos a preparar una primera prueba y a comparar unas pocas herramientas.</p>${filters}<nav class="area-jump" aria-label="Grupos de objetivos">${groups.map(g=>`<a href="#/rutas?group=${esc(g.id)}${route?`&route=${esc(route)}`:""}">${esc(g.title)}</a>`).join("")}${params.get("group")?`<a href="#/rutas${route?`?route=${esc(route)}`:""}">Ver todos</a>`:""}</nav>
      ${groups.filter(g=>!params.get("group")||g.id===params.get("group")||!groups.some(x=>x.id===params.get("group"))).map(group=>`<section class="section"><h2>${esc(group.title)}</h2><ul class="objective-directory">${group.goals.map(id=>catalog.discovery.goals.find(g=>g.id===id)).filter(Boolean).map(g=>`<li><a href="#/rutas?goal=${esc(g.id)}${route?`&route=${esc(route)}`:""}"><h3><span aria-hidden="true">${GOAL_ICONS[g.id]||"•"}</span>${esc(g.title)}</h3><p>${esc(g.outcome||g.description)}</p><span>Ver opciones y primera prueba</span></a></li>`).join("")}</ul></section>`).join("")}`;
  }

  const accessAdvice={
    claude:{title:"Usar Claude Code",use:"Skills e instrucciones dentro del agente, herramientas MCP o una integración que el proyecto documente.",pay:"El acceso del agente y las tarifas de los servicios conectados se revisan por separado.",check:"Distingue las instrucciones para el agente de la cuenta que usará la aplicación en ejecución."},
    codex:{title:"Usar Codex",use:"Skills compatibles, herramientas MCP y las rutas de integración indicadas en cada ficha.",pay:"Tener acceso a Codex no incluye automáticamente las APIs que utilice un proyecto.",check:"Comprueba el método de autenticación y si la ruta está documentada para tu cliente."},
    antigravity:{title:"Usar Antigravity",use:"Recursos compatibles con ese cliente, con su propio método de instalación o conexión.",pay:"El acceso al agente no elimina los costes de servicios, medios o proveedores externos.",check:"No copies una configuración de otro cliente sin revisar el recorrido de Antigravity."},
    local_model:{title:"Ejecutar un modelo en tu equipo",use:"Un motor o una aplicación con una ruta local documentada.",pay:"Equipo, energía y almacenamiento; también puede haber licencias o servicios externos.",check:"Verifica pesos, memoria, embeddings y herramientas: una etapa local no acredita un flujo íntegramente offline."},
    no_api:{title:"Empezar sin clave propia de API de IA",use:"Software sin modelo, recursos para un agente o una ruta que permite prescindir de esa clave.",pay:"Puede seguir usando una suscripción o un servicio online. Sin clave no significa gratis.",check:"Lee qué cuenta, conexión y servicios exige la ruta básica."},
    api:{title:"Configurar una API de IA",use:"Una aplicación que admite o necesita un proveedor de modelos configurado por ti.",pay:"Cuotas, créditos o consumo según proveedor y plan; alojamiento y otros servicios van aparte.",check:"Comprueba qué servicio recibe los datos y configura límites de gasto en el proveedor cuando estén disponibles."}
  };
  function renderAccess(params) {
    if(params.has("section"))return renderReading("acceso");
    const route=Object.hasOwn(accessAdvice,params.get("route"))?params.get("route"):"";
    const goal=catalog.discovery.goals.find(g=>g.id===params.get("goal"));
    const query=new URLSearchParams();if(route)query.set("route",route);if(goal)query.set("goal",goal.id);
    const count=route?filtered(query).length:0,advice=accessAdvice[route];
    const picks=route&&goal?AlexandriaSearch.guided(catalog.repos,catalog.categories,catalog.discovery.goals,query):[];
    return `<h1>Elige tu acceso. Entiende el coste.</h1><p class="lede">Una suscripción, una API y un modelo local son formas distintas de usar IA. Empieza por tu caso y comprueba qué puede cobrar cada pieza.</p>
      <form id="access-plan" class="decision-form"><div><label for="access-route">Con qué quieres trabajar</label><select id="access-route" name="route" required><option value="">Elige una forma de acceso</option>${routeOptions(route,false)}</select></div><div><label for="access-goal">Para qué lo necesitas</label><select id="access-goal" name="goal">${goalOptions(goal?.id,"Cualquier objetivo")}</select></div><button class="btn" type="submit">Entender mi ruta</button></form>
      ${advice?`<section class="decision-brief" id="access-result" tabindex="-1"><h2>${esc(advice.title)}</h2><dl><div><dt>Cómo se usa</dt><dd>${esc(advice.use)}</dd></div><div><dt>Qué puede cobrar</dt><dd>${esc(advice.pay)}</dd></div><div><dt>Antes de empezar</dt><dd>${esc(advice.check)}</dd></div></dl><p><a class="btn" href="${exploreHref(query)}">${count?`Explorar ${count} herramientas con esta ruta`:"Revisar esta combinación en el catálogo"}</a></p>${goal?`<p>${picks.length?"Puntos de partida para tu objetivo:":"No hay una recomendación inicial documentada con esta combinación. Puedes cambiar el acceso sin perder tu objetivo."}</p>${picks.length?pickList(picks):""}`:""}</section>`:`<section class="section"><h2>¿Qué tienes ahora?</h2><ul class="access-directory">${Object.entries(accessAdvice).map(([id,item])=>`<li><h3><a href="#/acceso?route=${id}">${esc(item.title)}</a></h3><p>${esc(item.use)}</p></li>`).join("")}</ul></section>`}
      <section class="section"><h2>Un presupuesto tiene varias partes</h2><p>Revisa estas capas antes de instalar. No se suman como una tarifa fija: dependen de la ruta, el volumen y la licencia.</p><dl class="cost-layers"><div><dt>Acceso al agente</dt><dd>La cuenta con la que trabajas en Claude Code, Codex o Antigravity y sus límites.</dd></div><div><dt>Modelo que usa la aplicación</dt><dd>API, créditos o modelo local. Puede ser diferente del que te ayuda a construirla.</dd></div><div><dt>Servicios y contenido</dt><dd>Hosting, búsqueda, telefonía, correo, datos, generación de medios y licencias.</dd></div><div><dt>Equipo y operación</dt><dd>RAM, GPU, espacio, energía, copias de seguridad y mantenimiento.</dd></div></dl></section>
      <section class="section"><h2>Lee las etiquetas con cuidado</h2><ul class="reading-notes"><li><strong>Integración documentada:</strong> la fuente describe una ruta; no significa que Alexandría la haya ejecutado.</li><li><strong>Referencia:</strong> material para aprender, sin una conexión confirmada al cliente.</li><li><strong>Por confirmar:</strong> falta evidencia. No equivale a gratuito, compatible o imposible.</li></ul><p><a href="#/guia/acceso">Leer la guía completa, fuentes y fecha</a> · <a href="#/explorar?route=review">Ver requisitos que siguen por confirmar</a></p></section>`;
  }

  function preparation(item) {
    return catalog.labels.audience[item.getting_started?.audience] || "Consulta los requisitos";
  }

  let guidedSession=null;
  function guidedState(params) {
    const goal=catalog.discovery.goals.find(g=>g.id===params.get("goal")),route=params.get("route");
    // A new goal link (for example from the home page ideas) starts a fresh draft.
    if(guidedSession&&!(goal&&goal.id!==guidedSession.fromGoal))return guidedSession;
    const modes={claude:'existing',codex:'existing',antigravity:'existing',local_model:'local',no_api:'no_api',api:'api'};
    const draft=AlexandriaGuide.normalize({project:goal?.title||'',goal:goal?.id||'',mode:modes[route]||'any',clients:['claude','codex','antigravity'].includes(route)?[route]:[]});
    return guidedSession={draft,submitted:goal?draft:null,fromGoal:goal?.id||""};
  }
  function profileSelect(group,id,name,value) {
    return `<select id="${id}" name="${name}">${Object.entries(AlexandriaGuide.labels[group]).map(([key,title])=>`<option value="${key}"${value===key?' selected':''}>${esc(title)}</option>`).join('')}</select>`;
  }
  function guidedPrompt(pick,profile) {
    const item=pick.item,l=AlexandriaGuide.labels,trial=AlexandriaGuide.firstTry(pick);
    return [`Quiero crear: ${profile.project}`,`Objetivo: ${catalog.discovery.goals.find(g=>g.id===profile.goal)?.title||'confirmar al empezar'}.`,
      `Mi experiencia: ${l.experience[profile.experience]}. Mi equipo: ${l.os[profile.os]}, ${l.ram[profile.ram]}, ${l.gpu[profile.gpu]}.`,
      `Acceso declarado: ${profile.clients.map(id=>AlexandriaGuide.clientNames[id]).join(', ')||'ninguno confirmado'}. Preferencia: ${l.mode[profile.mode]}.`,
      `Estoy considerando ${item.name}. Fuente: ${item.getting_started?.source||item.repo_url}.`,
      `Primera prueba propuesta: ${trial.action||'elegir una prueba pequeña'}. Qué comprobar: ${trial.success||'definir un resultado observable'}.`,
      'Lee la documentación actual y comprueba sistema, dependencias, licencia y costes antes de dar comandos. Si falta un dato de equipo, pregúntalo. Separa tu ayuda para instalar del modelo que ejecuta la aplicación y no asumas que mi suscripción paga sus APIs. Guíame una acción a la vez y verifica el resultado. No inventes paquetes ni solicites claves en el chat.'
    ].join('\n\n');
  }
  function guidedResults(profile) {
    const result=AlexandriaGuide.recommend(catalog,profile),{intent,picks,notices,excluded}=result,l=AlexandriaGuide.labels;
    const summary=`<dl class="guided-summary"><div><dt>Experiencia</dt><dd>${esc(l.experience[profile.experience])}</dd></div><div><dt>Equipo</dt><dd>${esc([l.os[profile.os],l.ram[profile.ram],l.gpu[profile.gpu]].join(' · '))}</dd></div><div><dt>Acceso</dt><dd>${esc(profile.clients.map(id=>AlexandriaGuide.clientNames[id]).join(', ')||'Ningún agente confirmado')} · ${esc(l.mode[profile.mode])}</dd></div></dl>`;
    let body;
    if(!intent.goal){
      body=`<p>${intent.kind==='ambiguous'?'Tu descripción encaja en varios objetivos. Elige cuál quieres resolver primero en «Tipo de resultado».':'No hemos identificado un objetivo con suficiente claridad. Elige «Tipo de resultado» o añade qué entrada tendrás y qué salida necesitas.'}</p>${intent.suggestions.length?`<ul>${intent.suggestions.map(g=>`<li>${esc(g.title)}</li>`).join('')}</ul>`:''}<button class="btn ghost" type="button" data-action="guided-objective">Elegir el objetivo</button>`;
    }else if(!picks.length){
      body=`<p>No encontramos un punto de partida documentado con estas condiciones. Conservamos tus respuestas; puedes ajustar el perfil.</p><ul>${excluded.device?'<li>Solo navegador: no hay una aplicación web verificada en estos puntos de partida.</li>':''}${excluded.access?'<li>Revisa el acceso: una integración con tu agente, un modelo local y una API son rutas diferentes.</li>':''}${excluded.preparation?'<li>Se han apartado opciones con preparación pesada o requisitos documentados que superan el equipo indicado. Puedes revisar sus fichas si vas a usar otro entorno.</li>':''}</ul><button class="btn ghost" type="button" data-action="guided-edit">Ajustar mis respuestas</button>`;
    }else{
      body=`<p>Son puntos de partida para explorar, con funciones y requisitos distintos. Elige una primera prueba; no necesitas instalar todas las opciones.</p><ol class="guided-recommendations">${picks.map(pick=>{
        const item=pick.item,trial=AlexandriaGuide.firstTry(pick),steps=AlexandriaGuide.startSteps(pick,profile),prompt=guidedPrompt(pick,{...profile,goal:intent.goal.id});
        return `<li><article><h3><a href="#/repo/${esc(item.id)}">${esc(item.name)}</a></h3><p>${esc(item.lead)}</p><p class="meta">${esc(pick.useBrowser?'Aplicación web oficial':preparation(item))} · ${esc(label('cost',item.access.cost))}</p><h4>Por qué aparece para ti</h4><ul>${pick.reasons.map(text=>`<li>${esc(text)}</li>`).join('')}</ul>${pick.warnings.length?`<p class="guided-caution"><strong>Antes de empezar:</strong> ${esc(pick.warnings.join(' '))}</p>`:''}<h4>Tus primeros pasos</h4><ol class="guided-start-steps">${steps.map(step=>`<li>${esc(step.text)}${safeUrl(step.href)?` <a href="${esc(safeUrl(step.href))}" target="_blank" rel="noreferrer">${esc(step.label)}</a>`:''}</li>`).join('')}</ol><p><strong>Qué comprobar:</strong> ${esc(trial.success||'El resultado indicado por la documentación.')}</p><p><strong>Costes a revisar:</strong> ${esc(item.access.cost_note)}</p><p class="meta">Ficha revisada el ${esc(item.access.checked_at)}. Prueba propuesta; no ejecutada por Alexandría.</p><details class="reading-details"><summary>Pedir ayuda a mi asistente con estos datos</summary><label for="guided-prompt-${esc(item.id)}">Encargo para empezar con ${esc(item.name)}</label><textarea id="guided-prompt-${esc(item.id)}" rows="7" readonly>${esc(prompt)}</textarea><button class="btn small" type="button" data-action="copy" data-text="${esc(prompt)}">Copiar encargo personalizado</button><p class="copy-status meta" role="status"></p></details><p><a href="#/repo/${esc(item.id)}?section=start">Abrir la ficha, requisitos y fuentes</a></p></article></li>`;
      }).join('')}</ol><div class="decision-actions">${picks.length>1?`<a class="btn" href="${comparisonHref(picks.map(p=>p.item.id))}">Comparar funciones de estas opciones</a>`:''}<button class="btn ghost" type="button" data-action="guided-edit">Cambiar mis respuestas</button><a href="#/rutas?goal=${esc(intent.goal.id)}">Explorar este objetivo</a></div>`;
    }
    return `<section id="guided-results" class="section" aria-labelledby="guided-result-title"><h2 id="guided-result-title" tabindex="-1">${!intent.goal?'Aclaremos el resultado que buscas':picks.length?`${picks.length} ${picks.length===1?'punto de partida':'puntos de partida'} para tu proyecto`:'Revisemos las condiciones para empezar'}</h2><p class="guided-project"><strong>Quieres crear:</strong> ${esc(profile.project)}</p>${intent.goal?`<p><strong>${intent.kind==='detected'?'Objetivo interpretado':'Objetivo elegido'}:</strong> ${esc(intent.goal.title)}. Puedes corregirlo en el formulario.</p>`:''}${summary}${notices.length?`<ul class="reading-notes">${notices.map(text=>`<li>${esc(text)}</li>`).join('')}</ul>`:''}<p class="meta">Selección orientativa basada en el catálogo y tus respuestas. No certifica compatibilidad de hardware ni mide rendimiento.</p>${body}</section>`;
  }
  function renderGuided(params) {
    const state=guidedState(params),p=state.draft;
    return `<h1>Cuéntanos qué quieres crear</h1><p class="lede">Tu proyecto, tu experiencia y lo que ya tienes. Recibirás hasta tres repos con motivos para elegirlos y pasos para una primera prueba.</p><p class="meta">Todas las preguntas están aquí. Tus respuestas se procesan en esta pestaña: no se envían a una API ni se guardan al recargar.</p>
      <form id="guided-start" class="guided-profile-form" action="#/empezar" method="post" aria-label="Tu proyecto y condiciones para empezar">
      <fieldset><legend>Qué quieres crear</legend><div class="guided-project-fields"><div><label for="guided-project">Describe tu proyecto (obligatorio)</label><textarea id="guided-project" name="project" rows="3" minlength="12" maxlength="800" required aria-describedby="guided-project-help guided-validation">${esc(p.project)}</textarea><p id="guided-project-help" class="meta">Por ejemplo: «Quiero crear una presentación a partir de un PDF». Entre 12 y 800 caracteres.</p></div><div><label for="guided-goal">Tipo de resultado</label><select id="guided-goal" name="goal">${goalOptions(p.goal,'Detectar por la descripción')}</select><p class="meta">Si el objetivo no se interpreta bien, elígelo aquí.</p></div></div></fieldset>
      <fieldset><legend>Tu experiencia</legend><div class="guided-radio-options">${Object.entries(AlexandriaGuide.labels.experience).map(([key,text])=>`<label><input type="radio" name="experience" value="${key}"${p.experience===key?' checked':''}> <span>${esc(text)}</span></label>`).join('')}</div><p class="meta">Al empezar se priorizan interfaces y rutas de aplicación; si programas, también piezas para integrar en código.</p></fieldset>
      <fieldset><legend>Tu equipo</legend><div class="guided-equipment"><div><label for="guided-os">Sistema o dispositivo</label>${profileSelect('os','guided-os','os',p.os)}</div><div><label for="guided-ram">Memoria RAM</label>${profileSelect('ram','guided-ram','ram',p.ram)}</div><div><label for="guided-gpu">GPU dedicada</label>${profileSelect('gpu','guided-gpu','gpu',p.gpu)}</div></div><p class="meta">Puedes dejar «por confirmar». RAM y GPU sirven para priorizar; los requisitos dependen del modelo y del flujo que elijas.</p></fieldset>
      <fieldset><legend>Tu acceso a IA</legend><p class="field-help">Marca lo que ya puedes utilizar. Si no tienes ninguno, deja las opciones sin marcar.</p><div class="guided-client-options">${Object.entries(AlexandriaGuide.clientNames).map(([key,text])=>`<label><input type="checkbox" name="clients" value="${key}"${p.clients.includes(key)?' checked':''}> <span>${esc(key==='web'?'Solo un chat web: ChatGPT, Claude, Gemini…':text)}</span></label>`).join('')}</div><div class="guided-mode"><label for="guided-mode">Qué ruta prefieres para ejecutar la herramienta</label>${profileSelect('mode','guided-mode','mode',p.mode)}</div><p class="meta">Usar un agente para instalar no implica que su suscripción pague la IA de la aplicación. No necesitas introducir claves ni datos de tu cuenta.</p></fieldset>
      <p id="guided-validation" class="guided-validation" role="status"></p><div class="decision-actions"><button class="btn" type="submit">Recomendar hasta 3 repos</button><button class="btn ghost" type="button" data-action="guided-clear">Borrar respuestas</button></div></form>
      ${state.submitted?guidedResults(state.submitted):''}<p class="meta"><a href="#/guia/vocabulario">Entender los términos</a> · <a href="#/acceso">Entender acceso y costes</a></p>`;
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

  function quickAreas(items) {
    return `<ul class="area-quick-list" role="list">${items.map(area=>`<li><a href="#/area/${esc(area.id)}"><strong>${esc(area.title)}</strong><span>${area.topics.length} subcategorías · ${area.count} repos</span></a></li>`).join("")}</ul>`;
  }

  function repoCount(count) {
    return `${count} ${count===1?"repo":"repos"}`;
  }

  function topicHref(area, topic) {
    return exploreHref(new URLSearchParams({area:area.id,topic:topic.id}));
  }

  function areaDirectory(items, query) {
    return `<ul class="area-directory" role="list">${items.map(area=>{
      const areaMatch=fold([area.title,...area.keywords].join(" ")).includes(query);
      const matches=area.topics.filter(topic=>areaMatch||fold([topic.title,topic.description,...topic.keywords].join(" ")).includes(query));
      const preview = !query && area.id==="audiovisual" ? ["av-video-edicion","av-voz","av-audio","av-imagen"].map(id=>topicById[id]) : matches.slice(0,4);
      return `<li class="area-entry"${areaTone(area.id)}><div class="head"><span class="icon-tile" aria-hidden="true">${areaIcon(area.id)}</span><h3><a href="#/area/${esc(area.id)}">${esc(area.title)}</a></h3></div><p>${esc(area.description)}</p>
        <ul class="topic-preview" role="list">${preview.map(topic=>`<li><a href="${topicHref(area,topic)}">${esc(topic.title)}</a></li>`).join("")}</ul>
        <a class="area-more" href="#/area/${esc(area.id)}">Explorar ${area.topics.length} subcategorías<span class="sr-only"> de ${esc(area.title)}</span></a><span class="meta"> · ${area.count} repos</span></li>`;
    }).join("")}</ul>`;
  }

  function technicalRooms() {
    return `<ul class="technical-index" role="list">${catalog.categories.filter(cat=>cat.num>0).map(cat=>`<li><a href="#/explorar?cat=${cat.num}">${esc(cat.title)}</a><span class="meta"> · ${cat.count}</span></li>`).join("")}</ul>`;
  }

  function renderRooms(params) {
    if (!areas.length) return `<h1>Explora por tema</h1>${technicalRooms()}`;
    const query=fold(params.get("q")||"").trim();
    const matches=areas.filter(area=>fold([area.title,...area.keywords,...area.topics.flatMap(topic=>[topic.title,topic.description,...topic.keywords])].join(" ")).includes(query));
    return `<h1>Explora por áreas</h1><p class="lede">Elige tu campo de trabajo y después una tarea concreta. También puedes preparar Claude Code, Codex o Antigravity en sus colecciones de configuración.</p>
      <search><form id="areas-search" class="home-search" action="#/salas" method="get"><label for="area-query">Buscar una categoría o subcategoría</label><p class="meta" id="area-help">Por ejemplo: frontend, ciberseguridad, voz, trading o configurar Codex.</p><div class="search-line"><input id="area-query" name="q" type="search" value="${esc(params.get("q")||"")}" aria-describedby="area-help" placeholder="¿Qué tema quieres explorar?"><button class="btn" type="submit">Buscar tema</button></div></form></search>
      <p id="area-results-count" role="status">${matches.length} ${matches.length===1?"área":"áreas"}${query?(matches.length===1?" coincide con tu búsqueda":" coinciden con tu búsqueda"):` · ${catalog.counts.topics} subcategorías`}. Un repo puede aparecer en varios temas; su ficha es la misma.</p>
      ${matches.some(a=>a.kind==="work")?`<section class="section"><h2>Áreas de trabajo</h2>${areaDirectory(matches.filter(a=>a.kind==="work"),query)}</section>`:""}
      ${matches.some(a=>a.kind==="tool")?`<section class="section"><h2>Configuración de asistentes</h2>${areaDirectory(matches.filter(a=>a.kind==="tool"),query)}</section>`:""}
      ${!matches.length?`<div class="empty"><h2>No encontramos ese tema</h2><p>Prueba un nombre más general o <a href="${exploreHref(new URLSearchParams({q:params.get("q")||""}))}">busca ese término en los repositorios</a>.</p><a href="#/salas">Ver todas las áreas</a></div>`:""}
      <details class="technical-map"><summary>Ver el índice técnico de ${catalog.counts.categories} secciones</summary><p class="meta">Clasificación original por tipo de herramienta. Los enlaces anteriores siguen funcionando.</p>${technicalRooms()}</details>`;
  }

  function renderArea(id) {
    const area=areaById[id];
    if(!area)return missing("No encontramos esa categoría.","#/salas");
    const topics=area.topics.map(topic=>`<li><a class="topic-row" href="${topicHref(area,topic)}" aria-labelledby="topic-name-${esc(topic.id)} topic-count-${esc(topic.id)}" aria-describedby="topic-desc-${esc(topic.id)}"><div><h3 id="topic-name-${esc(topic.id)}">${esc(topic.title)}</h3><p id="topic-desc-${esc(topic.id)}">${esc(topic.description)}</p></div><span class="topic-count" id="topic-count-${esc(topic.id)}">${repoCount(topic.count)}</span></a></li>`).join("");
    const guide=area.guide?`<section class="section setup-guide"><h2>Primera configuración, paso a paso</h2><ol>${area.guide.map(step=>`<li><h3>${esc(step.title)}</h3><p>${esc(step.text)}</p></li>`).join("")}</ol><p><a href="${esc(safeUrl(area.official_url))}" target="_blank" rel="noreferrer">Abrir la fuente oficial de ${esc(area.title.replace("Configuración de ",""))}</a></p><p class="meta">${esc(area.scope)}</p></section>`:"";
    return `<div${areaTone(id)}><nav class="breadcrumbs" aria-label="Ubicación"><a href="#/salas">Categorías</a><span aria-hidden="true"> / </span><span aria-current="page">${esc(area.title)}</span></nav><header class="page-head tone"><div class="title-row"><span class="icon-tile big" aria-hidden="true">${areaIcon(id)}</span><h1>${esc(area.title)}</h1></div><p class="lede">${esc(area.description)}</p><div class="badges"><span class="badge tone">${area.count} repos únicos</span><span class="badge tone">${area.topics.length} subcategorías</span>${area.kind==="tool"?'<span class="badge tone">Colección de configuración</span>':'<span class="badge tone">Área de trabajo</span>'}</div></header>
      <nav class="area-jump" aria-label="En esta categoría"><a href="#/area/${esc(id)}?section=topics">Elegir subcategoría</a>${area.guide?`<a href="#/area/${esc(id)}?section=setup">Primeros pasos</a>`:""}<a href="${exploreHref(new URLSearchParams({area:id}))}">Ver todos los repos de esta área</a></nav>
      <section class="section" id="area-topics"><h2>¿Qué necesitas hacer?</h2><ul class="topic-directory" role="list">${topics}</ul></section>
      ${guide.replace('class="section setup-guide"','class="section setup-guide" id="area-setup"')}
      <section class="section"><h2>Opciones para empezar</h2><p>Compara estas fichas antes de instalar. No necesitas usar todas.</p>${quickRepos(area.starters)}</section>
      ${area.evidence?.length?`<details class="technical-map"><summary>Fuentes de compatibilidad de esta colección</summary><ul>${area.evidence.map(e=>`<li><a href="${esc(safeUrl(e.source))}" target="_blank" rel="noreferrer">${esc(repo(e.repo_id)?.name||e.repo_id)}</a> · revisado el ${esc(e.checked_at)}</li>`).join("")}</ul></details>`:""}</div>`;
  }

  function quickRepos(ids) {
    return `<ul class="starter-list" role="list">${ids.map(id=>repo(id)).filter(Boolean).map(item=>`<li><a href="#/repo/${esc(item.id)}"><strong>${esc(item.name)}</strong></a><p>${esc(item.lead)}</p><p class="meta">${esc(label("api",item.access.api))} · ${esc(preparation(item))}</p></li>`).join("")}</ul>`;
  }

  function selectField(name, title, choices, current, disabled=false) {
    return `<div class="filter-field"><label for="filter-${name}">${esc(title)}</label><select id="filter-${name}" name="${name}"${disabled?" disabled":""}>${choices.map(([value,text]) => `<option value="${esc(value)}"${value===current?" selected":""}>${esc(text)}</option>`).join("")}</select></div>`;
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
    const area=areaById[params.get("area")],topic=topicById[params.get("topic")];
    const chips=[];
    const addChip=(key,text)=>{const next=new URLSearchParams(params);next.delete(key);next.delete("page");if(key==="cat")next.delete("sub");if(key==="area")next.delete("topic");chips.push(`<a class="chip" href="${exploreHref(next)}">${esc(text)} <span aria-hidden="true">×</span><span class="sr-only">: quitar filtro</span></a>`);};
    for(const [key,value] of params){if(key==="q"||key==="page"||key==="sort"||!value)continue;const text=key==="area"?(area?.title||value):key==="topic"?(topic?.title||value):key==="cat"?catName(value):key==="sub"?(category?.subs.find(s=>s.key===value)?.title||value):key==="goal"?(goal?.title||value):key==="route"?label("route",value):value;addChip(key,text);}
    const groups=catalog.labels;
    return `${area?`<nav class="breadcrumbs" aria-label="Ubicación"><a href="#/salas">Categorías</a> / <a href="#/area/${esc(area.id)}">${esc(area.title)}</a>${topic?` / <span aria-current="page">${esc(topic.title)}</span>`:""}</nav>`:""}<header class="page-head${area?" tone":""}"${area?areaTone(area.id):""}><div class="title-row">${area?`<span class="icon-tile big" aria-hidden="true">${areaIcon(area.id)}</span>`:""}<h1>${esc(topic?.title||area?.title||goal?.title||"Busca una herramienta")}</h1></div><p class="lede">${esc(topic?.description||area?.description||goal?.description||"Busca una tarea, un nombre o una tecnología. Después filtra por área, acceso y requisitos.")}</p>${area&&!topic?`<div class="chip-row">${area.topics.map(t=>`<a class="chip" href="${topicHref(area,t)}">${esc(t.title)} <span class="meta">${t.count}</span></a>`).join("")}</div>`:""}</header>
      <search><form class="library-filters" id="filters" action="#/explorar" method="get">
        <div class="query-field"><label for="q">Buscar en la biblioteca</label><input id="q" type="search" name="q" placeholder="Por ejemplo: transcribir audio" value="${esc(params.get("q")||"")}" autocapitalize="none" autocorrect="off" spellcheck="false" enterkeyhint="search"></div>
        <div class="filter-grid">
        ${areas.length?selectField("area","Área de trabajo o asistente",[["","Todas las áreas"],...areas.map(item=>[item.id,item.title])],params.get("area")||""):""}
        ${areas.length?selectField("topic","Subcategoría",[["",area?"Todas las subcategorías":"Elige primero un área"],...(area?.topics||[]).map(t=>[t.id,t.title])],params.get("topic")||"",!area):""}
        ${selectField("goal","Objetivo",[["","Cualquier objetivo"],...catalog.discovery.goals.map(item=>[item.id,item.title])],params.get("goal")||"")}
        ${selectField("route","Forma de uso",[["","Cualquier acceso"],...Object.entries(groups.route)],params.get("route")||"")}
        </div>
        <details class="advanced-filters"${["role","setup","status","cat","sub"].some(key=>params.has(key))?" open":""}><summary>Más filtros: sección técnica, tipo y preparación</summary><div class="filter-grid">
        ${selectField("cat","Sección técnica",[["","Todas las secciones técnicas"],...catalog.categories.filter(cat=>cat.num>0).map(cat=>[String(cat.num),cat.title])],params.get("cat")||"")}
        ${selectField("sub","Especialidad técnica",[["","Todas las especialidades"],...(category?.subs||[]).map(sub=>[sub.key,sub.title])],params.get("sub")||"")}
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
    const rows=[["API de IA",label("api",a.api),a.api_note===a.cost_note?"":a.api_note],["Claude Code",label("client",a.claude_code),""],["Codex",label("client",a.codex),""],["Antigravity",label("client",a.antigravity),""],["Modelos locales",label("local_model",a.local_model),a.local_note===item.how?"":a.local_note],["Coste",label("cost",a.cost),a.cost_note],["Equipo",label("hardware",a.hardware),a.hardware_note]];
    if(a.other_access)rows.push(["Otras rutas",a.other_access,""]);
    const subscription=a.subscription_note===item.how?"Conectar un agente no incluye automáticamente su suscripción ni los servicios externos. Revisa la ruta documentada.":a.subscription_note;
    return `<section id="repo-access" class="section" aria-labelledby="access-heading"><h2 id="access-heading">Acceso, coste y equipo</h2><p>${esc(a.scope)}</p><dl class="access-facts">${rows.map(([title,value,note])=>`<div><dt>${esc(title)}</dt><dd><strong>${esc(value)}</strong>${note?`<p>${esc(note)}</p>`:""}</dd></div>`).join("")}</dl><p class="access-explanation">${esc(subscription)} <a href="#/acceso">Cómo interpretar estas rutas</a>.</p></section>`;
  }

  function startSection(item) {
    const g=item.getting_started||{};
    const source=safeUrl(g.source||item.repo_url);
    const prompt=[`Quiero usar ${item.name} y necesito pasos guiados para una persona sin experiencia técnica.`, `Fuente original: ${source}.`, `La ficha de Alexandría indica: ${preparation(item)}; API de IA: ${label("api",item.access.api)}; Claude Code: ${label("client",item.access.claude_code)}; Codex: ${label("client",item.access.codex)}; Antigravity: ${label("client",item.access.antigravity)}; modelo local: ${label("local_model",item.access.local_model)}.`,item.first_try?.action?`Primera prueba propuesta: ${item.first_try.action}. Resultado que comprobar: ${item.first_try.success}.`:"", "Lee la documentación actual antes de dar comandos. Pregunta mi sistema operativo y qué resultado busco. Explica si conviene una aplicación lista, una skill o configurar un proyecto. Distingue tu ayuda para instalar de la cuenta o el modelo que usará la herramienta. Comprueba dependencias, costes y límites de la ruta elegida. Guíame una acción a la vez hasta una primera prueba pequeña y verifica el resultado. No inventes paquetes o comandos ni pidas que pegue contraseñas en el chat."].filter(Boolean).join("\n\n");
    return `<section id="repo-start" class="section"><h2>Cómo empezar</h2><p class="meta">${esc(preparation(item))}. <a href="#/guia/vocabulario">Entender los términos</a>.</p>${g.prerequisites?.length?`<p><strong>Antes de empezar</strong></p><ul>${g.prerequisites.map(text=>`<li>${esc(text)}</li>`).join("")}</ul>`:""}
      ${safeUrl(g.entry_url)?`<p><a class="btn" href="${esc(safeUrl(g.entry_url))}" target="_blank" rel="noreferrer">Abrir la web o descarga indicada por el autor</a></p>`:""}
      ${g.steps?.length?`<ol class="start-steps">${g.steps.map(text=>`<li>${esc(text)}</li>`).join("")}</ol>`:"<p>Consulta la ruta de instalación en la documentación original.</p>"}
      ${g.command&&g.command_status==="documented"?`<p id="command-title"><strong>Entrada documentada · ${esc(g.command_language||"consulta la sintaxis original")}</strong></p><pre class="command" role="region" aria-labelledby="command-title" tabindex="0"><code>${esc(g.command)}</code></pre><button class="btn small" type="button" data-action="copy" data-text="${esc(g.command)}">Copiar comando</button>`:""}
      ${g.note?`<p class="meta">${esc(g.note)}</p>`:""}
      ${item.first_try?.action?`<div class="callout"><h3>Tu primera prueba</h3><p>${esc(item.first_try.action)}.</p><p><strong>Qué comprobar:</strong> ${esc(item.first_try.success)}.</p><p class="meta">Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.</p></div>`:""}
      ${source?`<p><a href="${esc(source)}" target="_blank" rel="noreferrer">Abrir instrucciones originales</a></p>`:""}
      <details class="guided-help"><summary>Necesito ayuda paso a paso con esta herramienta</summary><p>Copia este encargo en Claude Code, Codex o tu asistente. Que te ayude a instalar no significa que la aplicación use su suscripción.</p><label for="help-prompt">Encargo para tu asistente</label><textarea id="help-prompt" rows="9" readonly>${esc(prompt)}</textarea><button class="btn small" type="button" data-action="copy" data-text="${esc(prompt)}">Copiar encargo</button><p class="copy-status" role="status"></p></details></section>`;
  }

  function hasFour(item) {
    return Boolean(item.que_es && item.que_hace && item.como_lo_hace && ((item.combina_con || []).length || item.nivel === 'ligero'));
  }

  function usedBy(item) {
    const users = (item.used_by || []).filter((id) => repo(id));
    if (!users.length) return "";
    const links = users.map((id) => `<a href="#/repo/${encodeURIComponent(id)}">${esc(repo(id).name)}</a>`).join(" · ");
    const body = `<p class="meta">Repos que lo citan en sus combinaciones sin que figuren arriba. Lista generada automáticamente; el motivo está en la ficha de cada uno.</p><p>${links}</p>`;
    return users.length > 12
      ? `<details class="used-by"><summary><h2>Usado por (${users.length})</h2></summary>${body}</details>`
      : `<h2>Usado por (${users.length})</h2>${body}`;
  }

  function fourSections(item) {
    if (!hasFour(item)) return "";
    const combos = item.combina_con.filter((combo) => repo(combo.id)).map((combo) => `<li><a href="#/repo/${encodeURIComponent(combo.id)}"><strong>${esc(repo(combo.id).name)}</strong></a>: ${esc(combo.motivo || "")}${combo.orden_instalacion ? `<br><span class="meta">Orden y cuidados: ${esc(combo.orden_instalacion)}</span>` : ""}</li>`).join("");
    const sources = (item.descripcion_fuentes || []).map((url, index) => `<a href="${esc(safeUrl(url))}" target="_blank" rel="noreferrer">Fuente ${index + 1}</a>`).join(" · ");
    const checked = (item.descripcion_revision || {}).checked_at || "fecha por confirmar";
    const gh = item.descripcion_github || {};
    const og = item.descripcion_origen || {};
    const ogHost = ({codeberg:"Codeberg",gitlab:"GitLab",huggingface:"Hugging Face"})[og.host] || og.host || "la forja original";
    const ogLine = og.checked_at ? `<p class="meta">Estado en ${esc(ogHost)}: ${og.archived ? "⚠️ archivado (solo lectura)" : "activo"}${og.pushed_at ? ` · última actividad ${esc(og.pushed_at)}` : ""}${og.latest_release ? ` · última versión ${esc(og.latest_release)}` : ""}${og.license ? ` · licencia ${esc(og.license)}` : ""} (consultado el ${esc(og.checked_at)}).</p>` : "";
    const ghLine = gh.checked_at ? `<p class="meta">${og.checked_at ? "Copia antigua en GitHub" : "Estado en GitHub"}: ${gh.archived ? "⚠️ archivado (solo lectura)" : "activo"}${gh.renamed_to ? ` · renombrado a ${esc(gh.renamed_to)}` : ""}${gh.pushed_at ? ` · último push ${esc(gh.pushed_at)}` : ""}${gh.latest_release ? ` · última versión ${esc(gh.latest_release)}` : ""}${gh.license ? ` · licencia ${esc(gh.license)}` : ""} (consultado el ${esc(gh.checked_at)}).</p>` : "";
    return `<section id="repo-four" class="section">
        <h2>¿Qué es?</h2><p>${esc(item.que_es)}</p>
        <h2>¿Qué hace?</h2><p>${esc(item.que_hace)}</p>
        <h2>¿Cómo lo hace?</h2><p>${esc(item.como_lo_hace)}</p>
        <h2>¿Con qué otros repos se combina?</h2><ul>${combos}</ul>
        ${usedBy(item)}
        ${item.descripcion_notas ? `<p><strong>Notas.</strong> ${esc(item.descripcion_notas)}</p>` : ""}
        ${ogLine}${ghLine}
        <p class="meta">Descripción redactada a partir de la documentación del autor (revisada el ${esc(checked)}); no se instaló ni ejecutó.${sources ? ` ${sources}` : ""}</p>
      </section>`;
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
      <nav class="repo-toc" aria-label="En esta ficha"><a href="#/repo/${encodeURIComponent(item.id)}?section=examples">Ver ejemplos</a><a href="#/repo/${encodeURIComponent(item.id)}?section=access">Ver acceso y costes</a><a href="#/repo/${encodeURIComponent(item.id)}?section=start">Ir a los primeros pasos</a></nav>
      ${fourSections(item)}
      ${item.practical_examples?.length?`<section id="repo-examples" class="section"><h2>Para qué puedes usarlo</h2><ul>${item.practical_examples.map(example=>`<li>${esc(example.scenario)}</li>`).join("")}</ul><p class="meta">Ejemplos de uso propuestos para orientar tu elección.</p></section>`:""}
      ${accessSection(item)}
      ${body&&!hasFour(item)?`<div class="section">${body}</div>`:""}
      ${item.how&&!hasFour(item) ? `<section class="section"><h2>Qué conviene saber</h2><p>${esc(item.how)}</p></section>` : ""}
      ${skill}
      ${startSection(item)}
      ${item.areas?.length?`<section class="section"><h2>Encuéntralo por tema</h2><ul class="access-links" role="list">${item.areas.map(id=>areaById[id]).filter(Boolean).map(area=>`<li><a href="#/area/${esc(area.id)}">${esc(area.title)}</a></li>`).join("")}</ul></section>`:""}
      <section class="section grid-2">
        <div>
          <h2>Combina con</h2>
          <p class="meta">${esc(hasFour(item) ? "Detalle y orden de instalación en «¿Con qué otros repos se combina?»." : catalog.copy.combine_note)}</p>
          ${refLinks(item.combine_refs)}
        </div>
        <div>
          <h2>Alternativas</h2>
          <p class="meta">${esc(catalog.copy.alt_note)}</p>
          ${refLinks(item.alt_refs)}
        </div>
      </section>
      <section class="section"><h2>Fuentes y límites</h2>${item.limits&&item.limits!==item.how?`<p>${esc(item.limits)}</p>`:""}<p class="meta">Acceso revisado el ${esc(item.access.checked_at || "fecha por confirmar")}. Lectura de documentación; no prueba de ejecución.</p><ul>${(item.access.sources||[]).map((url,index)=>`<li><a href="${esc(safeUrl(url))}" target="_blank" rel="noreferrer">Fuente ${index+1}</a></li>`).join("")}</ul></section>
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
    const parts=AlexandriaDecisions.recipeParts(recipe);
    const [icon,hue]=RECIPE_STYLE[recipe.id]||["🧪",40];
    return `<article class="recipe-overview"${toneStyle(hue)}><span class="icon-tile big" aria-hidden="true">${icon}</span><div><h2><a href="#/receta/${esc(recipe.id)}">${esc(recipe.title)}</a></h2><p>${esc(recipe.goal)}</p><p class="meta">${parts.minimum.length?`Propuesta inicial: ${parts.minimum.length} ${parts.minimum.length===1?"pieza":"piezas"}`:"Recorrido por revisar"} · ${recipe.steps.length} recursos en el recorrido completo</p></div><div><p><strong>Prepara:</strong> ${esc(recipe.plan?.inputs||"Una tarea acotada y datos de prueba")}</p><a href="#/receta/${esc(recipe.id)}">Ver cómo empezar y qué comprobar</a></div></article>`;
  }

  function renderRecipes(params) {
    const goal=catalog.discovery.goals.find(g=>g.id===params.get("goal"));
    const recipes=goal?catalog.recipes.filter(r=>(goal.recipe_ids||[]).includes(r.id)):catalog.recipes;
    return `<h1>Combina herramientas con un propósito</h1><p class="lede">Una receta explica qué hace cada pieza y con cuáles empezar. Primero una prueba pequeña; después, las ampliaciones que necesites.</p>
      <form id="recipe-filter" class="decision-form"><div><label for="recipe-goal">Filtrar por lo que quieres conseguir</label><select id="recipe-goal" name="goal">${goalOptions(goal?.id)}</select></div><button class="btn" type="submit">Ver recetas</button></form>
      <p class="meta">${recipes.length} ${recipes.length===1?"receta":"recetas"} para explorar. Son propuestas de combinación basadas en las fichas, sin una prueba de integración del conjunto.</p>
      ${recipes.length?`<div class="recipe-directory">${recipes.map(recipeCard).join("")}</div>`:`<p class="empty">Todavía no hay una receta para este objetivo. <a href="#/rutas?goal=${esc(goal.id)}">Explora sus herramientas y primera prueba</a> o <a href="#/recetas">vuelve a todas las recetas</a>.</p>`}`;
  }

  function renderRecipe(id,params) {
    const recipe = catalog.recipes.find((item) => item.id === id);
    if (!recipe) return missing("Esa receta no está.", "#/recetas");
    const done = recipeDone(recipe.id);
    const parts=AlexandriaDecisions.recipeParts(recipe),plan=recipe.plan||{};
    const showAll=params.get("view")==="all"||!parts.minimum.length;
    const visibleIds=showAll?recipe.steps.filter(s=>s.id).map(s=>s.id):parts.minimum;
    const realSteps=visibleIds.map(rid=>recipe.steps.find(s=>s.id===rid));
    const doneCount=visibleIds.filter(rid=>done.has(rid)).length;
    const items = realSteps.map((step, index) => {
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
              <p class="meta">${parts.instead.includes(step.id)?"Otra ruta; no la sumes automáticamente al inicio.":parts.minimum.includes(step.id)?"Pieza de la propuesta inicial.":"Ampliación opcional del recorrido."}</p>
              <dl class="piece-facts"><div><dt>Preparación</dt><dd>${esc(preparation(item))}</dd></div><div><dt>API de IA</dt><dd>${esc(label("api",item.access.api))}</dd></div><div><dt>Coste</dt><dd>${esc(item.access.cost_note)}</dd></div></dl>
              <a href="#/repo/${esc(step.id)}?section=start">Abrir sus requisitos y arranque</a>
            </div>
            <label class="check"><input type="checkbox" data-action="step" data-recipe="${esc(recipe.id)}" data-id="${esc(step.id)}"${done.has(step.id) ? " checked" : ""}> Ya revisé esta pieza<span class="sr-only">: ${esc(item.name)}</span></label>
          </div>
        </article>
      </li>`;
    }).join("");
    return `
      <p class="breadcrumbs"><a href="#/recetas">Todas las recetas</a></p><header class="page-head tone"${toneStyle((RECIPE_STYLE[recipe.id]||[])[1])}><div class="title-row"><span class="icon-tile big" aria-hidden="true">${(RECIPE_STYLE[recipe.id]||["🧪"])[0]}</span><h1>${esc(recipe.title)}</h1></div>
      <p class="lede">${esc(recipe.goal)}</p></header>
      ${recipe.lesson ? `<p>${esc(recipe.lesson)}</p>` : ""}
      <p class="meta">Ruta propuesta por Alexandría; integración del conjunto no ejecutada. Una lista de piezas no sustituye sus dependencias, modelos ni cuentas.</p>
      ${plan.inputs?`<section class="decision-brief"><h2>Tu primera versión</h2><dl><div><dt>Qué preparar</dt><dd>${esc(plan.inputs)}</dd></div><div><dt>Primera prueba propuesta</dt><dd>${esc(plan.first_try.action)}</dd></div><div><dt>Qué comprobar</dt><dd>${esc(plan.first_try.success)}</dd></div></dl><p>${esc(plan.note)}</p></section>`:""}
      <section class="section"><h2>${showAll?"Todas las piezas y sus rutas":"Empieza con estas piezas"}</h2><p>${showAll?"Este inventario incluye ampliaciones y alternativas. No necesitas instalar todas para empezar.":"Propuesta inicial para acotar la prueba. Abre cada ficha y revisa su configuración antes de conectar las piezas."}</p><div class="decision-actions"><a class="${showAll?"":"selected-link"}" href="#/receta/${esc(id)}">Propuesta inicial</a><a class="${showAll?"selected-link":""}" href="#/receta/${esc(id)}?view=all">Recorrido completo (${recipe.steps.length} recursos)</a></div>
      <p class="live meta" id="recipe-progress" role="status" data-step-ids="${esc(JSON.stringify(visibleIds))}">${doneCount} de ${realSteps.length} piezas visibles revisadas. Recordatorio guardado en este navegador; no acredita instalación.</p>
      <ol class="timeline">${items}</ol>
      </section>
      ${parts.extra.length&&!showAll?`<section class="section"><h2>Añade solo lo que te falte</h2><ul class="recipe-additions">${parts.extra.map(rid=>`<li><a href="#/repo/${esc(rid)}">${esc(repo(rid).name)}</a><p>${esc(recipe.steps.find(s=>s.id===rid).why)}</p></li>`).join("")}</ul></section>`:""}
      ${parts.instead.length?`<section class="section"><h2>Otras rutas que puedes elegir</h2><p>Revisan otra forma de resolver una capa o el flujo. No son instalaciones adicionales obligatorias.</p><ul>${parts.instead.map(rid=>`<li><a href="#/repo/${esc(rid)}">${esc(repo(rid).name)}</a> — ${esc(repo(rid).lead)}</li>`).join("")}</ul></section>`:""}
      <section class="section"><h2>Antes de ampliar el flujo</h2><p>Comprueba por pieza el proveedor del modelo, la licencia, el alojamiento y los servicios conectados. No hay un precio único ni una suscripción que incluya automáticamente todo el recorrido.</p><p><a href="#/acceso">Preparar el acceso y revisar los costes</a></p>${recipe.when_not?`<h3>Cuándo simplificar o elegir otra ruta</h3><p>${esc(recipe.when_not)}</p>`:""}</section>
      ${recipe.how?`<details class="reading-details"><summary>Entender cómo se conectan las piezas</summary>${paragraphs(recipe.how)}</details>`:""}<p><a href="#/recetas">Volver a las recetas</a></p>`;
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

  function comparePicker(params,ids) {
    const query=params.get("q")||"",goal=catalog.discovery.goals.some(g=>g.id===params.get("goal"))?params.get("goal"):"";
    const suggested=[...new Set(ids.flatMap(id=>repo(id).alt_refs.map(ref=>ref.id)).filter(Boolean))];
    const starters=catalog.discovery.goals.find(g=>g.id===goal)?.starters||[];
    const found=AlexandriaDecisions.candidates(catalog.repos,query,ids,goal,[...suggested,...starters]);
    return `<search><form id="compare-search" class="decision-form"><div><label for="compare-query">Buscar por nombre o tecnología</label><input id="compare-query" name="q" type="search" value="${esc(query)}" placeholder="Por ejemplo: activepieces, whisper o react" aria-describedby="compare-search-help"></div><div><label for="compare-goal">Acotar por objetivo</label><select id="compare-goal" name="goal">${goalOptions(goal)}</select></div><button class="btn" type="submit">Buscar herramientas</button></form></search><p id="compare-search-help" class="meta">Selecciona hasta tres. Cada resultado muestra su identidad para distinguir repos con el mismo nombre.</p>
      <section aria-labelledby="compare-candidates-title"><h2 id="compare-candidates-title" class="compact-title">${query||goal?"Resultados para añadir":suggested.length?"Alternativas documentadas para seguir comparando":"Busca una herramienta o empieza con una comparación"}</h2><div id="compare-candidates" aria-live="polite">${found.length?`<p class="meta">${found.length} ${found.length===1?"coincidencia":"coincidencias"}${found.length>6?"; se muestran seis. Afina la búsqueda para ver otras.":"."}</p><ul class="compare-candidates">${found.slice(0,6).map(item=>`<li><div><strong>${esc(item.name)}</strong><span class="meta">${esc(item.gh||item.id)}</span><p>${esc(item.lead)}</p></div><button class="btn small ghost" type="button" data-action="compare" data-id="${esc(item.id)}" aria-label="Añadir ${esc(item.name)} (${esc(item.gh||item.id)}) a comparar"${ids.length===3?" disabled":""}>Añadir</button></li>`).join("")}</ul>`:query||goal?`<p>No hay coincidencias para esta búsqueda. Prueba un nombre más corto o cambia el objetivo.</p>`:""}</div></section>`;
  }
  function comparisonTable(group,items,differences) {
    const rows=group.rows.filter(row=>!differences||AlexandriaDecisions.different(row,items));
    const table=rows.length?`<div class="comparison-table-wrap" role="region" tabindex="0" aria-labelledby="comparison-${group.id}-caption"><table class="compare decision-table"><caption id="comparison-${group.id}-caption">${esc(group.title)} · ${items.length} ${items.length===1?"herramienta":"herramientas"}</caption><thead><tr><th scope="col">Criterio</th>${items.map(item=>`<th scope="col"><a href="#/repo/${esc(item.id)}">${esc(item.name)}</a></th>`).join("")}</tr></thead><tbody>${rows.map(row=>`<tr><th scope="row">${esc(row.title)}</th>${items.map(item=>`<td data-label="${esc(item.name)}">${row.render?row.render(item):esc(row.value(item)||"No documentado")}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`:`<p class="meta">No hay diferencias en los criterios de esta sección. Desactiva el filtro para verlos.</p>`;
    return group.id==="functions"?`<section class="section comparison-section"><h2>${esc(group.title)}</h2>${table}</section>`:`<details id="compare-details-${group.id}" class="comparison-section comparison-details"><summary>${esc(group.title)} · ${rows.length} criterios${differences?" con diferencias":""}</summary>${table}</details>`;
  }
  function renderCompare(params) {
    const ids=compareList(),items=ids.map(repo),differences=params.get("diff")==="1"&&items.length>1;
    const row=(title,value,render)=>({title,value,render});
    const groups=[
      {id:"functions",title:"Funciones y diferencias técnicas",rows:[
        row("Qué hace",i=>i.lead),row("Usos concretos",i=>i.practical_examples.map(e=>e.scenario).join("; ")),
        row("Tipo de pieza",i=>label("role",i.role)),row("Dónde se ejecuta el software",i=>label("exec",i.exec)),
        row("Herramientas y dependencias",i=>i.stack),row("MCP",i=>i.mcp?"MCP indicado en la ficha":"No indicado en la ficha"),
        row("Qué conviene saber",i=>i.how||i.limits)]},
      {id:"start",title:"Preparación y primera prueba",rows:[row("Preparación",i=>preparation(i)),row("Equipo y requisitos",i=>i.access.hardware_note),row("Primera prueba propuesta",i=>i.first_try?.action),row("Qué comprobar",i=>i.first_try?.success)]},
      {id:"access",title:"Acceso y costes",rows:[row("API de IA",i=>label("api",i.access.api)),row("Claude Code",i=>label("client",i.access.claude_code)),row("Codex",i=>label("client",i.access.codex)),row("Antigravity",i=>label("client",i.access.antigravity)),row("Modelo local",i=>label("local_model",i.access.local_model)),row("Tipo de coste",i=>label("cost",i.access.cost)),row("Qué puede cobrar",i=>i.access.cost_note)]},
      {id:"sources",title:"Fuentes y alcance de revisión",rows:[row("Revisión de la ficha",i=>i.access.checked_at),row("Estado del proyecto",i=>i.status==="archived"?"Archivado":i.status==="unverified"?"Identidad por verificar":"Sin alerta de archivo; no acredita mantenimiento reciente"),row("Documentación",i=>i.access.sources.join("; "),i=>`<ul class="comparison-sources">${i.access.sources.slice(0,3).map((url,n)=>`<li><a href="${esc(safeUrl(url))}" target="_blank" rel="noreferrer">Fuente ${n+1}<span class="sr-only"> de ${esc(i.name)}</span></a></li>`).join("")}</ul>`)]}
    ];
    const pairs=items.flatMap((a,index)=>items.slice(index+1).map(b=>({a,b,kind:AlexandriaDecisions.relationship(a,b)})));
    const presets=catalog.discovery.compare_presets||[];
    const selected=`<section class="section" aria-labelledby="selected-title"><div class="command-row"><h2 id="selected-title">Tu selección (${ids.length}/3)</h2>${ids.length?`<button class="btn small ghost" type="button" data-action="compare-clear">Vaciar comparación</button>`:""}</div>${items.length?`<ul class="compare-selection">${items.map(i=>`<li><div><a href="#/repo/${esc(i.id)}"><strong>${esc(i.name)}</strong></a><span class="meta">${esc(i.gh||i.id)}</span></div><button class="btn small ghost" type="button" data-action="compare" data-id="${esc(i.id)}" aria-label="Quitar ${esc(i.name)} de la comparación">Quitar</button></li>`).join("")}</ul>`:`<p>Busca por nombre, acota por objetivo o abre uno de los ejemplos de abajo. Las fichas también tienen un botón para añadirlas aquí.</p>`}${ids.length===3?`<p class="meta">Ya hay tres herramientas. Quita una antes de añadir otra; ninguna se reemplaza automáticamente.</p>`:""}</section>`;
    return `<h1>Compara funciones antes de elegir</h1><p class="lede">Pon hasta tres herramientas frente a frente. Primero sus funciones y diferencias técnicas; después, preparación, acceso y costes.</p>${selected}${items.length>1?`<details class="reading-details compare-edit" id="compare-editor"><summary>Buscar otra herramienta para la comparación</summary>${comparePicker(params,ids)}</details>`:comparePicker(params,ids)}
      ${items.length?`<section class="section"><div class="comparison-controls"><label class="check"><input id="compare-differences" type="checkbox"${differences?" checked":""}${items.length<2?" disabled":""}> Mostrar solo diferencias</label><button class="btn small ghost" type="button" data-action="copy" data-copy-kind="link" data-text="${esc('https://cristrva1.github.io/BL_Alexandria/'+comparisonHref(ids))}">Copiar enlace público</button><span class="copy-status meta" role="status"></span></div>${items.length<2?`<p class="meta">Añade una segunda herramienta para contrastar sus funciones.</p>`:`<h2 class="compact-title">Cómo se relacionan estas piezas</h2><ul class="comparison-relations">${pairs.map(({a,b,kind})=>`<li><strong>${esc(a.name)} y ${esc(b.name)}:</strong> ${kind==="alternative"?"figuran como alternativas en las fichas. Contrasta sus funciones para elegir.":kind==="complement"?"figuran como complementarias. Pueden cubrir etapas distintas; no necesitas descartar una por compararlas.":"su relación no está documentada como alternativa ni complemento. Revisa qué tarea resuelve cada una."}</li>`).join("")}</ul>`}</section>${groups.map(g=>comparisonTable(g,items,differences)).join("")}<p class="meta">Revisión documental; no son pruebas de rendimiento ni una evaluación de cuál es mejor. No documentado no significa incompatible.</p>`:presets.length?`<section class="section"><h2>Empieza con una comparación concreta</h2><ul class="comparison-presets">${presets.map(p=>`<li><a href="${comparisonHref(p.repos)}"><strong>${esc(p.title)}</strong><span>${p.repos.map(id=>esc(repo(id)?.name||id)).join(" · ")}</span></a></li>`).join("")}</ul></section>`:""}`;
  }

  function missing(text, href) {
    return `<h1>No está en el estante</h1><p class="lede">${esc(text)}</p><p><a href="${href}">Volver</a></p>`;
  }

  function activeOf(parts) {
    const head = parts[0] || "inicio";
    if (head === 'manual') return AlexandriaHandbook.sectionOf(catalog,parts[1]);
    if (head === "repo") return "explorar";
    if (["curso","guia","laboratorio"].includes(head)) return "guias";
    if (head === "receta") return "recetas";
    if (head === "tecnica") return "tecnicas";
    if (head === "sala" || head === "area") return "salas";
    return NAV.some(([id]) => id === head) ? head : "inicio";
  }

  function titleOf(parts, params) {
    const head = parts[0] || "inicio";
    if (head === 'manual') return AlexandriaHandbook.lookup(catalog,parts[1])?.name || AlexandriaHandbook.lookup(catalog,parts[1])?.title || 'Guía';
    if (head === "area") return areaById[parts[1]]?.title || "Categoría";
    if (head === "tecnica") return AlexandriaTechniques.lookup(catalog,decodeURIComponent(parts[1]||''))?.title || "Técnica";
    if (head === "explorar") return topicById[params.get("topic")]?.title || areaById[params.get("area")]?.title || "Buscar";
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
    if (head === "rutas") return renderGoals(route.params);
    if (head === "empezar") return renderGuided(route.params);
    if (head === 'configurar' || head === 'servicios') return AlexandriaHandbook.index(catalog,head,route.params);
    if (head === 'manual') return AlexandriaHandbook.detail(catalog,second);
    if (head === 'prompts') return AlexandriaHandbook.prompts(catalog,route.params);
    if (head === 'tecnicas') return AlexandriaTechniques.index(catalog,route.params);
    if (head === 'tecnica') return AlexandriaTechniques.detail(catalog,decodeURIComponent(second||''));
    if (head === "guias") return renderReading();
    if (head === "guia") return renderReading(second);
    if (head === "acceso") return renderAccess(route.params);
    if (head === "novedades") return renderNew();
    if (head === "salas" || head === "sala") return renderRooms(route.params);
    if (head === "area") return renderArea(second || "");
    if (head === "explorar") return renderExplore(route.params);
    if (head === "repo") return renderRepo(decodeURIComponent(second || ""));
    if (head === "recetas") return renderRecipes(route.params);
    if (head === "receta") return renderRecipe(second || "",route.params);
    if (head === "laboratorio") return renderLab(route.params);
    if (head === "comparar") return renderCompare(route.params);
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
    const openComparisons=route.parts[0]==="comparar"?[...document.querySelectorAll('.comparison-details[open], .compare-edit[open]')].map(node=>node.id):[];
    if(route.parts[0]==="comparar"&&route.params.has("ids"))storageSet("alexandria-compare",compareList());
    document.getElementById("app").innerHTML = layout(activeOf(route.parts), view(route));
    openComparisons.forEach(id=>{const node=document.getElementById(id);if(node)node.open=true;});
    document.title = `${titleOf(route.parts,route.params)} — Alexandría`;
    const path=route.parts.join("/")+(["rutas","acceso"].includes(route.parts[0])?`:${route.params.get("goal")||""}:${route.params.get("route")||""}`:"");
    if(path!==lastPath){
      const heading=document.querySelector("main h1");
      if(heading){heading.tabIndex=-1;if(lastPath!==null)heading.focus({preventScroll:true});}
      window.scrollTo({top:0,behavior:"instant"});
    }
    lastPath=path;
    const section=route.params.get("section");
    if(section!==null){const target=document.getElementById(route.parts[0]==="repo"?`repo-${section}`:route.parts[0]==="area"?`area-${section}`:route.parts[0]==='manual'?`manual-${section}`:route.parts[0]==='tecnica'?`tech-${section}`:`reading-section-${section}`);if(target){target.tabIndex=-1;target.focus({preventScroll:true});target.scrollIntoView();}}
    const q = document.getElementById("q");
    if (q && route.parts[0] === "explorar" && window.__focusSearch) {
      q.focus();
      window.__focusSearch = false;
    }
  }

  let searchTimer;
  function readGuidedForm(form) {
    const data=new FormData(form),profile=Object.fromEntries(data);
    profile.clients=data.getAll('clients');
    return AlexandriaGuide.normalize(profile);
  }
  function updateGuidedDraft(form,changedField) {
    const state=guidedState(parseHash().params);
    state.draft=readGuidedForm(form);state.submitted=null;
    const results=document.getElementById('guided-results');if(results)results.hidden=true;
    if(changedField==='project'){
      const project=document.getElementById('guided-project');project.setCustomValidity('');project.removeAttribute('aria-invalid');
      document.getElementById('guided-validation').textContent='';
    }
  }
  document.getElementById("app").addEventListener("input", (event) => {
    if(event.target.closest('#guided-start')){updateGuidedDraft(event.target.closest('form'),event.target.name);return;}
    if(event.target.id==="compare-query"&&!event.isComposing){
      clearTimeout(searchTimer);searchTimer=setTimeout(()=>{
        const params=parseHash().params,form=document.getElementById("compare-search");
        for(const key of ["q","goal"]){const value=String(new FormData(form).get(key)||"").trim();if(value)params.set(key,value);else params.delete(key);}
        params.set("ids",compareList().join(","));
        history.replaceState(null,"",`#/comparar?${params}`);
        const template=document.createElement("template");template.innerHTML=comparePicker(params,compareList());
        document.getElementById("compare-candidates").innerHTML=template.content.querySelector("#compare-candidates").innerHTML;
        document.getElementById("compare-candidates-title").textContent=template.content.querySelector("#compare-candidates-title").textContent;
      },220);return;
    }
    if(event.target.id!=="q" || event.isComposing)return;
    clearTimeout(searchTimer);
    searchTimer=setTimeout(()=>{
      const params=currentParamsFromForm();paintExplore(params);
      const href=exploreHref(params);if(location.hash!==href)history.replaceState(null,"",href);
    },220);
  });

  document.getElementById("app").addEventListener("submit", (event) => {
    if(event.target.id==='techniques-filter'){
      event.preventDefault();const params=new URLSearchParams();
      new FormData(event.target).forEach((value,key)=>{if(String(value).trim())params.set(key,String(value).trim());});
      history.pushState(null,'',`#/tecnicas${params.size?`?${params}`:''}`);draw();
      document.getElementById('tech-count')?.focus();return;
    }
    if(event.target.id==='handbook-filter'){
      event.preventDefault();const params=new URLSearchParams();
      new FormData(event.target).forEach((value,key)=>{if(String(value).trim())params.set(key,String(value).trim());});
      const section=parseHash().parts[0];history.pushState(null,'',`#/${section}${params.size?`?${params}`:''}`);draw();
      document.getElementById('handbook-count')?.focus();return;
    }
    const destination={"goal-context":"rutas","access-plan":"acceso","recipe-filter":"recetas","compare-search":"comparar"}[event.target.id];
    if(destination){
      event.preventDefault();const params=new URLSearchParams();
      new FormData(event.target).forEach((value,key)=>{if(String(value).trim())params.set(key,String(value).trim());});
      if(destination==="comparar"){params.set("ids",compareList().join(","));if(parseHash().params.get("diff")==="1")params.set("diff","1");}
      history.pushState(null,"",`#/${destination}${params.size?`?${params}`:""}`);draw();
      const target=document.getElementById(destination==="acceso"?"access-result":destination==="comparar"?"compare-candidates-title":"contenido");
      if(target){target.tabIndex=-1;target.focus();}return;
    }
    if(event.target.id === "areas-search") {
      event.preventDefault();const params=new URLSearchParams(new FormData(event.target));
      if(!params.get("q"))params.delete("q");
      history.pushState(null,"",`#/salas${params.size?`?${params}`:""}`);draw();
      const count=document.getElementById("area-results-count");if(count){count.tabIndex=-1;count.focus();}
    }
    if(event.target.id === "guided-start") {
      event.preventDefault();const profile=readGuidedForm(event.target),field=document.getElementById('guided-project');
      if(profile.project.length<12){
        const message='Describe qué quieres crear con al menos 12 caracteres, además de espacios.';
        field.setCustomValidity(message);field.setAttribute('aria-invalid','true');
        document.getElementById('guided-validation').textContent=message;field.reportValidity();field.focus();return;
      }
      guidedSession={draft:profile,submitted:AlexandriaGuide.normalize(profile)};
      // Profile and free-text project never enter the URL or persistent storage.
      history.replaceState(null,'','#/empezar');draw();
      document.getElementById('guided-result-title')?.focus();
      return;
    }
    if (event.target.id === "home-search") {
      event.preventDefault();
      const params=new URLSearchParams(); const q=new FormData(event.target).get("q");
      if(q)params.set("q",String(q));location.hash=exploreHref(params).slice(1);
    }
    if (event.target.id === "filters") {
      event.preventDefault();const params=currentParamsFromForm();params.delete("page");
      const cat=catByNum[params.get("cat")];if(!cat?.subs.some(sub=>sub.key===params.get("sub")))params.delete("sub");
      const area=areaById[params.get("area")];if(!area?.topics.some(topic=>topic.id===params.get("topic")))params.delete("topic");
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
    if(action==='nav-toggle'){
      const nav=button.closest('.nav'),open=!nav.classList.contains('open');
      nav.classList.toggle('open',open);button.setAttribute('aria-expanded',String(open));button.lastChild.textContent=open?'Cerrar':'Menú';return;
    }
    if(action==='guided-clear'){
      guidedSession={draft:AlexandriaGuide.normalize(),submitted:null};
      history.replaceState(null,'','#/empezar');draw();document.getElementById('guided-project').focus();return;
    }
    if(action==='guided-edit'||action==='guided-objective'){
      document.getElementById(action==='guided-objective'?'guided-goal':'guided-project')?.focus();return;
    }
    if (action === "copy") {
      const text = button.dataset.text || "";
      try {
        await navigator.clipboard.writeText(text);
        button.textContent = "Copiado";
      } catch (_error) {
        button.textContent = "Selecciona y copia el texto";
      }
      const status=button.parentElement.querySelector(".copy-status");if(status)status.textContent=button.textContent==="Copiado"?(button.dataset.copyKind==="link"?"Enlace público copiado con las herramientas seleccionadas.":"Contenido copiado. Ya puedes pegarlo donde lo necesites."):"No se pudo acceder al portapapeles. Selecciona el contenido y cópialo manualmente.";
    }
    if(action==="compare-clear"){
      storageSet("alexandria-compare",[]);const params=parseHash().params;params.set("ids","");params.delete("diff");
      history.pushState(null,"",`#/comparar?${params}`);draw();document.getElementById("compare-query")?.focus();
    }
    if (action === "compare") {
      const id = button.dataset.id;
      if(!repo(id))return;
      const list = compareList();
      if(!list.includes(id)&&list.length===3){document.getElementById("app-feedback").textContent="Ya hay tres herramientas seleccionadas. Quita una desde Comparar antes de añadir otra.";return;}
      const next = list.includes(id) ? list.filter((item) => item !== id) : list.concat(id);
      storageSet("alexandria-compare", next);
      const route=parseHash();if(route.parts[0]==="comparar"){route.params.set("ids",next.join(","));history.pushState(null,"",`#/comparar?${route.params}`);}
      draw();
      const target=parseHash().parts[0]==="comparar"?document.getElementById("selected-title"):[...document.querySelectorAll('[data-action="compare"]')].find(node=>node.dataset.id===id);
      if(target){target.tabIndex=target.tagName==="BUTTON"?0:-1;target.focus();}
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
    if(event.target.closest('#guided-start')){updateGuidedDraft(event.target.closest('form'),event.target.name);return;}
    if(event.target.id==="compare-differences"){
      const params=parseHash().params;params.set("ids",compareList().join(","));if(event.target.checked)params.set("diff","1");else params.delete("diff");
      history.replaceState(null,"",`#/comparar?${params}`);draw();document.getElementById("compare-differences").focus();return;
    }
    if(event.target.name === "area") {
      const select=document.getElementById("filter-topic"),area=areaById[event.target.value];
      if(select){select.disabled=!area;select.innerHTML=`<option value="">${area?"Todas las subcategorías":"Elige primero un área"}</option>`+(area?.topics||[]).map(topic=>`<option value="${esc(topic.id)}">${esc(topic.title)}</option>`).join("");}
    }
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
      const visible=JSON.parse(progress.dataset.stepIds||"[]");
      progress.textContent = `${visible.filter(id=>done.has(id)).length} de ${visible.length} piezas visibles revisadas. Recordatorio guardado en este navegador; no acredita instalación.`;
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

  // Link navigation animates between views; programmatic redraws stay synchronous.
  function navigate() {
    if (!document.startViewTransition || matchMedia("(prefers-reduced-motion: reduce)").matches) { draw(); return; }
    const transition = document.startViewTransition(draw);
    // A quick second navigation skips the running animation; that is expected, not an error.
    transition.ready.catch(() => {});
    transition.finished.then(() => { const heading=document.querySelector("main h1"); if(heading && document.activeElement===document.body) heading.focus({preventScroll:true}); }).catch(() => {});
  }
  window.addEventListener("hashchange", navigate);
  if (!location.hash) history.replaceState(null, "", "#/inicio");
  draw();
})();
