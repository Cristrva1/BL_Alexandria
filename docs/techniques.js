/* Techniques, ideas and recommendations. Reading, filtering and copy only: commands are never executed. */
(function(root){
  const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const fold=value=>String(value||'').toLowerCase().normalize('NFD').replace(/\p{M}/gu,'');
  const LEVELS={inicial:'Inicial',intermedio:'Intermedio',avanzado:'Avanzado'};
  const get=catalog=>catalog.techniques||{areas:[],items:[],sites:[],site_groups:[],rules:[]};
  const tone=h=>Number.isFinite(Number(h))?` style="--h:${Number(h)}"`:'';
  function external(url,label){
    try{if(new URL(url).protocol!=='https:')return esc(label);}catch{return esc(label);}
    return `<a href="${esc(url)}" target="_blank" rel="noreferrer">${esc(label)}</a>`;
  }
  function matches(item,query){
    const hay=fold([item.id,item.title,item.summary,item.why,item.caution,item.kind,...(item.steps||[]),...(item.tools||[])].join(' '));
    return fold(query).trim().split(/\s+/).filter(Boolean).every(token=>hay.includes(token));
  }
  function select(catalog,params){
    const t=get(catalog),area=t.areas.some(a=>a.id===params.get('area'))?params.get('area'):'';
    const level=Object.hasOwn(LEVELS,params.get('level'))?params.get('level'):'';
    const query=(params.get('q')||'').trim().slice(0,300);
    const items=t.items.filter(i=>(!area||i.area===area)&&(!level||i.level===level)&&matches(i,query));
    return {area,level,query,items};
  }
  function href(params){const q=params.toString();return `#/tecnicas${q?`?${q}`:''}`;}
  function card(t,item,index){
    const area=t.areas.find(a=>a.id===item.area)||{};
    return `<li class="rise" style="--i:${index%9}"><a class="tech-card"${tone(area.h)} href="#/tecnica/${esc(item.id)}"><span class="badges"><span class="badge tone">${esc(area.icon||'')} ${esc(area.title||item.area)}</span><span class="badge">${esc(item.kind)}</span><span class="badge ${item.level==='inicial'?'green':item.level==='avanzado'?'terra':'gold'}">${esc(LEVELS[item.level]||item.level)}</span></span><h3>${esc(item.title)}</h3><p>${esc(item.summary)}</p><span class="foot"><span>${item.steps.length} pasos${item.commands.length?` · ${item.commands.length} ${item.commands.length===1?'comando':'comandos'}`:''}</span><b>Ver técnica →</b></span></a></li>`;
  }
  function index(catalog,params){
    const t=get(catalog),{area,level,query,items}=select(catalog,params),overview=!area&&!level&&!query;
    const counts=Object.fromEntries(t.areas.map(a=>[a.id,t.items.filter(i=>i.area===a.id).length]));
    const pill=(key,value,text,count)=>{const next=new URLSearchParams(params);if(value)next.set(key,value);else next.delete(key);next.delete('q');const current=(params.get(key)||'')===value;return `<a class="pill" href="${href(next)}"${current?' aria-current="true"':''}>${text}${count!==undefined?` <span class="count">${count}</span>`:''}</a>`;};
    const grid=list=>`<ul class="tech-grid" role="list">${list.map((item,i)=>card(t,item,i)).join('')}</ul>`;
    const groups=overview?t.areas.filter(a=>counts[a.id]).map(a=>`<section class="section reveal"${tone(a.h)}><div class="section-head"><div><h2><span aria-hidden="true">${esc(a.icon)}</span> ${esc(a.title)}</h2><p>${esc(a.description)}</p></div><a class="more" href="${href(new URLSearchParams({area:a.id}))}">Ver las ${counts[a.id]} →</a></div>${grid(items.filter(i=>i.area===a.id).slice(0,6))}</section>`).join(''):'';
    const sites=overview&&t.sites.length?`<section class="section reveal" id="tech-sitios"><div class="section-head"><div><h2>Sitios y servicios útiles</h2><p>Recursos web para inspirarte, aprender o probar herramientas. Revisa sus condiciones de uso y privacidad antes de subir datos.</p></div></div>${(t.site_groups||[]).filter(a=>t.sites.some(s=>s.area===a.id)).map(a=>`<h3 class="compact-title">${esc(a.icon)} ${esc(a.title)}</h3><ul class="site-list">${t.sites.filter(s=>s.area===a.id).map(s=>`<li>${external(s.url,s.name)}<p>${esc(s.purpose)}</p></li>`).join('')}</ul>`).join('')}</section>`:'';
    return `<header class="page-head"><p class="eyebrow">Técnicas, ideas y recomendaciones</p><h1>Trabaja mejor con IA</h1><p class="lede">Formas concretas de trabajar con agentes, cuidar el contexto, diseñar, lanzar y producir contenido. Cada técnica explica cómo aplicarla, por qué ayuda y qué límite tiene.</p><p class="meta">Selección revisada el ${esc(t.updated_at)} a partir de publicaciones y documentación de la comunidad. Los textos son propios de Alexandría y enlazan su fuente; las cifras citadas por terceros no se verificaron. Ninguna técnica se ejecutó aquí.</p></header>
      ${overview&&t.rules.length?`<section class="section" aria-labelledby="rules-title"><div class="section-head"><div><h2 id="rules-title">Diez reglas para empezar con buen pie</h2><p>Lo que conviene hacer siempre, uses la herramienta que uses.</p></div></div><ol class="rules-list">${t.rules.map(r=>`<li><strong>${esc(r.title)}</strong><p>${esc(r.text)}</p></li>`).join('')}</ol></section>`:''}
      <nav class="chip-row" aria-label="Filtrar por área">${pill('area','','Todas',t.items.length)}${t.areas.filter(a=>counts[a.id]).map(a=>pill('area',a.id,`${esc(a.icon)} ${esc(a.title)}`,counts[a.id])).join('')}</nav>
      <nav class="chip-row" aria-label="Filtrar por nivel">${pill('level','','Cualquier nivel')}${Object.entries(LEVELS).map(([id,text])=>pill('level',id,esc(text))).join('')}</nav>
      <search><form id="techniques-filter" class="decision-form" method="get" action="#/tecnicas">${area?`<input type="hidden" name="area" value="${esc(area)}">`:''}${level?`<input type="hidden" name="level" value="${esc(level)}">`:''}<div><label for="tech-query">Buscar una técnica</label><input id="tech-query" name="q" type="search" maxlength="300" value="${esc(query)}" placeholder="Por ejemplo: hooks, tokens, animaciones, SEO"></div><button class="btn" type="submit">Buscar</button></form></search>
      <p id="tech-count" class="meta" role="status" tabindex="-1">${items.length} ${items.length===1?'técnica':'técnicas'}${overview?' en total. Se muestran hasta seis por área.':'.'} ${!overview?`<a href="#/tecnicas">Quitar filtros</a>`:''}</p>
      ${overview?groups:items.length?grid(items):`<div class="empty"><h2>No encontramos una técnica con esos filtros</h2><p>Prueba una palabra más corta o cambia de área. También puedes <a href="#/prompts">ver las plantillas de prompts</a>.</p></div>`}
      ${sites}
      <p class="section"><a href="#/prompts">Plantillas de prompts listas para copiar</a> · <a href="#/prompts?type=commands">Comandos documentados</a> · <a href="#/configurar">Configurar agentes y modelos</a></p>`;
  }
  function lookup(catalog,id){return get(catalog).items.find(i=>i.id===id);}
  function detail(catalog,id){
    const t=get(catalog),item=lookup(catalog,id);
    if(!item)return '<h1>Esta técnica no está disponible</h1><p><a href="#/tecnicas">Volver a Técnicas e ideas</a></p>';
    const area=t.areas.find(a=>a.id===item.area)||{},repos=Object.fromEntries((catalog.repos||[]).map(r=>[r.id,r]));
    const related=t.items.filter(i=>i.area===item.area&&i.id!==item.id).slice(0,3);
    const commands=item.commands.map((c,i)=>`<article class="tech-command"><h3>${esc(c.title)}</h3><p><strong>Dónde:</strong> ${esc(c.where)}</p><pre><code>${esc(c.text)}</code></pre><p>${esc(c.effect)}</p><div class="decision-actions"><button type="button" class="btn small" data-action="copy" data-text="${esc(c.text)}">Copiar comando</button>${external(c.source,'Ver fuente del comando')}<span class="copy-status meta" role="status"></span></div></article>`).join('');
    return `<article class="tech-detail"${tone(area.h)}><nav class="breadcrumbs" aria-label="Ubicación"><a href="#/tecnicas">Técnicas e ideas</a> / <a href="#/tecnicas?area=${esc(item.area)}">${esc(area.title||item.area)}</a></nav>
      <header class="page-head tone"><div class="title-row"><span class="icon-tile big" aria-hidden="true">${esc(area.icon||'💡')}</span><h1>${esc(item.title)}</h1></div><p class="lede">${esc(item.summary)}</p><div class="badges"><span class="badge tone">${esc(item.kind)}</span><span class="badge tone">Nivel ${esc((LEVELS[item.level]||item.level).toLowerCase())}</span>${(item.tools||[]).slice(0,6).map(tool=>`<a class="badge" href="#/explorar?q=${encodeURIComponent(tool)}">${esc(tool)}</a>`).join('')}</div></header>
      <nav class="handbook-jump" aria-label="En esta técnica"><a href="#/tecnica/${esc(id)}?section=pasos">Cómo aplicarla</a>${item.commands.length?`<a href="#/tecnica/${esc(id)}?section=comandos">Comandos</a>`:''}<a href="#/tecnica/${esc(id)}?section=fuentes">Fuentes</a></nav>
      <section id="tech-pasos" class="section"><h2>Cómo aplicarla</h2><ol class="steps">${item.steps.map(s=>`<li>${esc(s)}</li>`).join('')}</ol></section>
      <div class="why-caution"><div class="callout yes"><h3>Por qué ayuda</h3><p>${esc(item.why)}</p></div><div class="callout no"><h3>Antes de usarla</h3><p>${esc(item.caution)}</p></div></div>
      ${commands?`<section id="tech-comandos" class="section"><h2>Comandos documentados</h2><p>Lee dónde se ejecuta y qué modifica cada comando antes de copiarlo. Comprueba la versión actual en la fuente y, si instala código de terceros, revisa antes su repositorio. Alexandría solo muestra el texto.</p>${commands}</section>`:''}
      ${item.repo_ids?.length?`<section class="section"><h2>Fichas relacionadas del catálogo</h2><ul class="starter-list">${item.repo_ids.filter(r=>repos[r]).map(r=>`<li><a href="#/repo/${esc(r)}"><strong>${esc(repos[r].name)}</strong></a><p>${esc(repos[r].lead)}</p></li>`).join('')}</ul></section>`:''}
      <section id="tech-fuentes" class="section"><h2>Fuentes</h2><ul>${item.sources.map(s=>`<li>${external(s.url,s.title)}</li>`).join('')}</ul><p class="meta">Texto propio de Alexandría a partir de la fuente indicada, revisada el ${esc(t.updated_at)}. No equivale a una prueba ejecutada ni a una medición de rendimiento.</p></section>
      ${related.length?`<section class="section"><h2>Más técnicas de ${esc(area.title||'esta área')}</h2><ul class="tech-grid" role="list">${related.map((r,i)=>card(t,r,i)).join('')}</ul></section>`:''}
      <p><a class="btn ghost" href="#/tecnicas">← Volver a todas las técnicas</a></p></article>`;
  }
  const api={index,detail,lookup,select};
  if(typeof module==='object'&&module.exports)module.exports=api;else root.AlexandriaTechniques=api;
})(typeof globalThis!=='undefined'?globalThis:this);
