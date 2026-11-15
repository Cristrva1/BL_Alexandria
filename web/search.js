(function (root) {
  "use strict";
  const fold = value => String(value || "").toLowerCase().normalize("NFD").replace(/\p{M}/gu, "");
  const stop = new Set("quiero necesito para como hacer con de del la el los las mi mis un una unos unas y o en por me que puedo usar crear repo repos repositorio repositorios sirve sirva herramienta".split(" "));
  const groups = [
    ["voz", "tts", "narracion", "speech", "sintesis"],
    ["transcribir", "transcribe", "transcripcion", "whisper", "stt", "subtitulos", "transcription"],
    ["presentacion", "presentaciones", "powerpoint", "ppt", "slides", "diapositivas"],
    ["imagenes", "imagen", "image", "fotos", "restauracion"],
    ["video", "videos", "reels", "shorts", "montaje"],
    ["datos", "data", "analitica", "analytics"],
    ["dashboard", "dashboards", "tablero", "tableros", "bi"],
    ["investigar", "investigacion", "research", "fuentes"],
    ["automatizar", "automatizacion", "workflow", "workflows", "flujos"],
    ["local", "offline", "ollama"],
    ["programar", "coding", "codigo", "desarrollo"],
    ["finanzas", "financiero", "trading", "mercados", "bolsa"],
  ];
  function terms(query) {
    return fold(query).split(/[^a-z0-9.+-]+/).filter(term => term && !stop.has(term));
  }
  function alternatives(term) {
    const group = groups.find(items => items.includes(term));
    return group || [term];
  }
  function search(repos, categories, goals, params) {
    const q = fold(params.get("q") || "").trim();
    const setup=q.match(/\b(?:configurar|configuracion|configura|preparar|setup|optimizar)\s+(?:de\s+)?(claude code|codex|antigravity)\b/);
    const setupArea=setup ? `configurar-${setup[1].replace(/\s+/g,"-")}` : "";
    const implicitRoutes=[];
    let task=q;
    if(/\bsin\s+(?:una?\s+)?(?:api|clave)/.test(task)) { implicitRoutes.push("no_api");task=task.replace(/\bsin\s+(?:una?\s+)?(?:api|clave)(?:\s+de\s+ia)?/g,""); }
    if(/\b(?:modelo[s]?\s+local(?:es)?|offline|sin conexion)\b/.test(task)) { implicitRoutes.push("local_model");task=task.replace(/\b(?:modelo[s]?\s+local(?:es)?|offline|sin conexion)\b/g,""); }
    if(/\b(?:con|suscripcion(?: de)?)\s+(?:mi\s+)?codex\b/.test(task)) { implicitRoutes.push("codex");task=task.replace(/\b(?:con|suscripcion(?: de)?)\s+(?:mi\s+)?codex\b/g,""); }
    if(/\b(?:con|suscripcion(?: de)?)\s+(?:mi\s+)?claude(?: code)?\b/.test(task)) { implicitRoutes.push("claude");task=task.replace(/\b(?:con|suscripcion(?: de)?)\s+(?:mi\s+)?claude(?: code)?\b/g,""); }
    const tokens = terms(task);
    const goal = goals.find(item => item.id === params.get("goal"));
    const cats = Object.fromEntries(categories.map(cat => [cat.num, cat]));
    const selected = repos.filter(item => {
      if (setupArea && !(item.areas || []).includes(setupArea)) return false;
      if (params.get("area") && !(item.areas || []).includes(params.get("area"))) return false;
      if (params.get("topic") && !(item.topics || []).includes(params.get("topic"))) return false;
      if (params.get("cat") && String(item.cat) !== params.get("cat")) return false;
      if (params.get("sub") && item.sub !== params.get("sub")) return false;
      if (params.get("route") && !(item.routes || []).includes(params.get("route"))) return false;
      if (implicitRoutes.some(route=>!(item.routes||[]).includes(route))) return false;
      if (goal && !(item.goals || []).includes(goal.id) && !goal.starters.includes(item.id)) return false;
      for (const field of ["role", "exec", "setup"]) if (params.get(field) && item[field] !== params.get(field)) return false;
      if (params.get("mcp") === "1" && !item.mcp) return false;
      if (params.get("status") === "active" && item.status) return false;
      if (params.get("status") && params.get("status") !== "active" && item.status !== params.get("status")) return false;
      if (params.get("prov") && !item.prov.includes(params.get("prov"))) return false;
      const clientSupport = ["native","host","connector","project_integration"];
      const supported = [clientSupport.includes(item.access?.claude_code) ? "claude code" : "", clientSupport.includes(item.access?.codex) ? "codex" : ""];
      const hay = fold([item.name, item.id, item.one, item.lead, item.desc, item.choose_if, item.stack, item.discovery_text, cats[item.cat]?.title, ...(item.tags || []), ...supported].join(" "));
      return tokens.every(term => alternatives(term).some(alias => hay.includes(alias)));
    });
    const score = item => (fold(item.id) === q || fold(item.name) === q ? 1000 : 0)
      + (q && fold(item.name).includes(q) ? 300 : 0)
      + tokens.filter(term => alternatives(term).some(alias=>fold(item.name+" "+item.one).includes(alias))).length * 35
      + (goal && goal.starters.includes(item.id) ? 100 - goal.starters.indexOf(item.id) : 0)
      + (item.pick ? 5 : 0) - (item.status ? 10 : 0);
    const sort = params.get("sort") || "relevance";
    return selected.sort((a, b) => {
      if (sort === "new") return String(b.added_at || "").localeCompare(String(a.added_at || "")) || a.name.localeCompare(b.name);
      if (sort === "name") return a.name.localeCompare(b.name);
      if (sort === "stars") return (b.stars || 0) - (a.stars || 0) || a.name.localeCompare(b.name);
      return score(b) - score(a) || a.name.localeCompare(b.name);
    });
  }
  function guided(repos, categories, goals, params) {
    const goal = goals.find(item => item.id === params.get("goal"));
    if (!goal) return [];
    const query = new URLSearchParams({goal:goal.id,status:"active"});
    if (params.get("route")) query.set("route",params.get("route"));
    const eligible = new Set(goal.guided || goal.starters);
    const candidates = search(repos,categories,goals,query).filter(item=>eligible.has(item.id));
    const readiness = {ready_app:50,agent:35,reading:30,setup:10,developer:0};
    const score = item => (readiness[item.getting_started?.audience] || 0)
      + (goal.starters.includes(item.id) ? 35-goal.starters.indexOf(item.id) : 0)
      + (item.setup === "easy" ? 10 : item.setup === "heavy" ? -15 : 0);
    return candidates.sort((a,b)=>score(b)-score(a) || a.name.localeCompare(b.name)).slice(0,3);
  }
  const api = { fold, terms, search, guided };
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.AlexandriaSearch = api;
})(typeof globalThis !== "undefined" ? globalThis : this);
