/* Reading, search and copy only. These guides never execute their commands. */
(function(root){
  const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const fold=value=>String(value||'').toLowerCase().normalize('NFD').replace(/\p{M}/gu,'');
  const topics={empezar:'Elegir y empezar',programar:'Construir y revisar',mejorar:'Mejorar el agente',movil:'Teléfonos',operar:'Publicar y operar'};
  const names={configurar:'Configurar IA',servicios:'Servicios y despliegue'};
  const get=catalog=>catalog.handbook||{groups:[],resources:[],prompts:[],paths:[]};
  function external(url,label){
    try{if(new URL(url).protocol!=='https:')return esc(label);}catch{return esc(label);}
    return `<a href="${esc(url)}" target="_blank" rel="noreferrer">${esc(label)}</a>`;
  }
  const href=id=>`#/manual/${encodeURIComponent(id)}`;
  const list=(items,ordered=false)=>`<${ordered?'ol':'ul'}>${items.map(text=>`<li>${esc(text)}</li>`).join('')}</${ordered?'ol':'ul'}>`;
  function matches(item,query){
    const hay=fold([item.id,item.name,item.title,item.kind,item.summary,item.when,...(item.aliases||[]),...(item.prepare||[]),...(item.improve||[])].join(' '));
    return fold(query).trim().split(/\s+/).filter(Boolean).every(token=>hay.includes(token));
  }
  function selectResources(catalog,section,group='',query=''){
    const h=get(catalog),groups=new Set(h.groups.filter(g=>g.section===section&&(!group||g.id===group)).map(g=>g.id));
    return h.resources.filter(r=>groups.has(r.group)&&matches(r,query));
  }
  function groupLink(section,id,text){return `<a href="#/${section}?group=${esc(id)}">${esc(text)}</a>`;}
  function row(resource){return `<li><article class="handbook-row"><div><p class="meta">${esc(resource.kind)}</p><h3><a href="${href(resource.id)}">${esc(resource.name)}</a></h3></div><div><p>${esc(resource.summary)}</p><a href="${href(resource.id)}">Requisitos, cuenta, costes y primera prueba</a></div></article></li>`;}
  function index(catalog,section,params){
    const h=get(catalog),groups=h.groups.filter(g=>g.section===section),query=(params.get('q')||'').trim().slice(0,300);
    const group=groups.some(g=>g.id===params.get('group'))?params.get('group'):'';
    const results=selectResources(catalog,section,group,query),overview=!group&&!query;
    const paths=h.paths.filter(p=>p.section===section);
    const intro=section==='configurar'?'Elige qué pieza necesitas: un agente para trabajar, un modelo para responder, un motor local o una forma de automatizar el teléfono. Empieza por una prueba pequeña; después añade mejoras.':'Código, alojamiento, datos y acceso remoto cumplen funciones diferentes. Encuentra la pieza que falta en tu proyecto antes de contratar o instalar otro servicio.';
    const directories=groups.map(g=>{
      const items=results.filter(r=>r.group===g.id);if(!items.length)return '';
      return `<section class="handbook-group"><div class="command-row"><h2>${esc(g.title)}</h2>${overview?groupLink(section,g.id,`Ver las ${items.length} guías`):''}</div><p>${esc(g.description)}</p><ul class="handbook-directory">${(overview?items.slice(0,3):items).map(row).join('')}</ul></section>`;
    }).join('');
    return `<h1>${names[section]}</h1><p class="lede">${intro}</p><p class="meta">Orientación revisada el ${esc(h.updated_at)}. Las condiciones y versiones pueden cambiar. Las guías complementan las fichas de repos; no suman proyectos al catálogo.</p>
      <nav class="handbook-jump" aria-label="Grupos de ${names[section]}">${groups.map(g=>groupLink(section,g.id,g.title)).join('')}</nav>
      <search><form id="handbook-filter" class="decision-form handbook-filter" method="get" action="#/${section}"><div><label for="handbook-query">Buscar en estas guías</label><input id="handbook-query" name="q" type="search" maxlength="300" value="${esc(query)}" placeholder="Nombre, función o tecnología"></div><div><label for="handbook-group">Grupo</label><select id="handbook-group" name="group"><option value="">Todos los grupos</option>${groups.map(g=>`<option value="${esc(g.id)}"${group===g.id?' selected':''}>${esc(g.title)}</option>`).join('')}</select></div><button class="btn" type="submit">Buscar guías</button></form></search>
      <p id="handbook-count" class="meta" tabindex="-1" role="status">${results.length} ${results.length===1?'guía':'guías'}${overview?' en este directorio. Se muestran tres entradas por grupo; abre un grupo para ver todas.':'.'} ${group||query?`<a href="#/${section}">Quitar filtros</a>`:''}</p>
      ${overview?`<section class="handbook-paths"><h2>Recorridos para empezar</h2><ul>${paths.map(p=>`<li><a href="${href(p.id)}">${esc(p.title)}</a><span>${esc(p.goal)}</span></li>`).join('')}</ul></section>`:''}
      ${directories||`<section class="section"><h2>No encontramos una guía con esos filtros</h2><p>Prueba un nombre más corto o cambia el grupo. También puedes <a href="#/explorar">buscar en los repositorios</a>.</p></section>`}
      <p class="section"><a href="#/prompts">Usar una plantilla o consultar comandos documentados</a> · <a href="#/empezar">Pedir una recomendación por proyecto</a></p>`;
  }
  function commandBlock(command,id){
    return `<article class="handbook-command"><h3>${esc(command.title)}</h3><p><strong>Dónde:</strong> ${esc(command.where)}</p><pre><code>${esc(command.text)}</code></pre><p>${esc(command.effect)}</p><div class="decision-actions"><button type="button" class="btn small" data-action="copy" data-text="${esc(command.text)}">Copiar comando</button>${external(command.source,'Ver fuente del comando')}<span class="copy-status meta" role="status"></span></div></article>`;
  }
  function pathDetail(catalog,path){
    const h=get(catalog),byId=Object.fromEntries(h.resources.map(r=>[r.id,r]));
    return `<article class="reading"><p><a href="#/${path.section}">${names[path.section]}</a> / Recorrido sugerido</p><h1>${esc(path.title)}</h1><p class="lede">${esc(path.goal)}</p><p>Propuesta de orientación para una primera prueba. Las alternativas indicadas permiten elegir una ruta; no necesitas instalar todas.</p><ol class="handbook-path-steps">${path.steps.map(step=>`<li><h2><a href="${href(step.resource)}">${esc(byId[step.resource].name)}</a></h2><p>${esc(step.text)}</p><a href="${href(step.resource)}">Abrir los requisitos y primeros pasos</a></li>`).join('')}</ol><p><strong>Qué comprobar:</strong> ${esc(path.verify)}</p><p>${esc(path.limit)}</p><p class="meta">Recorrido editorial; no ejecutado por Alexandría. Cada guía enlaza las fuentes del proyecto correspondiente.</p><p><a href="#/prompts?topic=empezar">Plantillas para elegir e instalar con ayuda</a></p></article>`;
  }
  function detail(catalog,id){
    const h=get(catalog),path=h.paths.find(p=>p.id===id);if(path)return pathDetail(catalog,path);
    const r=h.resources.find(r=>r.id===id);if(!r)return '<h1>Esta guía no está disponible</h1><p><a href="#/configurar">Volver a Configurar IA</a></p>';
    const group=h.groups.find(g=>g.id===r.group),byId=Object.fromEntries(catalog.repos.map(r=>[r.id,r]));
    return `<article class="reading handbook-detail"><nav class="breadcrumbs" aria-label="Ubicación"><a href="#/${group.section}">${names[group.section]}</a> / ${groupLink(group.section,group.id,group.title)}</nav><p class="kicker">${esc(r.kind)}</p><h1>${esc(r.name)}</h1><p class="lede">${esc(r.summary)}</p><p>${external(r.sources[0].url,'Abrir guía original')}</p>
      <dl class="handbook-facts"><div><dt>Cuenta y compatibilidad</dt><dd>${esc(r.access)}</dd></div><div><dt>Acceso y coste</dt><dd>${esc(r.cost)}</dd></div></dl>
      <nav class="handbook-jump" aria-label="En esta guía"><a href="${href(id)}?section=start">Primera prueba</a><a href="${href(id)}?section=improve">Mejoras</a>${r.commands.length?`<a href="${href(id)}?section=commands">Comandos</a>`:''}<a href="${href(id)}?section=sources">Fuentes</a></nav>
      <section id="manual-start" class="reading-section"><h2>Prepara lo necesario</h2>${list(r.prepare)}<h2>Tu primera prueba</h2>${list(r.steps,true)}<p><strong>Qué comprobar:</strong> ${esc(r.verify)}</p></section>
      <section id="manual-improve" class="reading-section"><h2>Mejoras después de la primera prueba</h2>${list(r.improve)}<h2>Límites que cambian la decisión</h2>${list(r.limits)}</section>
      ${r.commands.length?`<section id="manual-commands" class="reading-section"><h2>Comandos documentados</h2><p>Lee dónde se ejecuta y qué modifica cada uno antes de copiarlo. Alexandría solo muestra y copia el texto.</p>${r.commands.map((c,i)=>commandBlock(c,`${id}-${i}`)).join('')}</section>`:''}
      ${r.repo_ids.length?`<section class="reading-section"><h2>Fichas relacionadas del catálogo</h2><ul>${r.repo_ids.map(id=>byId[id]?`<li><a href="#/repo/${esc(id)}">${esc(byId[id].name)}</a></li>`:'').join('')}</ul></section>`:''}
      <section id="manual-sources" class="reading-section"><h2>Fuentes y fecha</h2><ul>${r.sources.map(s=>`<li>${external(s.url,s.title)} · ${esc(s.checked_at)}</li>`).join('')}</ul><p class="meta">Guía documental y prueba propuesta; no equivale a una instalación o medición de rendimiento realizada por Alexandría.</p></section><p><a href="#/prompts?topic=${group.id==='movil'?'movil':group.section==='servicios'?'operar':'empezar'}">Pedir acompañamiento con una plantilla</a></p></article>`;
  }
  function prompts(catalog,params){
    const h=get(catalog),commands=params.get('type')==='commands',query=(params.get('q')||'').trim().slice(0,300);
    const topic=Object.hasOwn(topics,params.get('topic'))?params.get('topic'):'';
    const templates=h.prompts.filter(p=>(!topic||p.topic===topic)&&matches(p,query));
    const commandResources=h.resources.filter(r=>r.commands.length&&matches(r,query));
    const commandCount=commandResources.reduce((n,r)=>n+r.commands.length,0);
    return `<h1>Prompts y comandos para trabajar con criterio</h1><p class="lede">Una plantilla explica lo que quieres conseguir. Un comando actúa en una herramienta concreta. Elige el contexto, completa los datos que faltan y comprueba el resultado.</p><nav class="handbook-jump" aria-label="Tipo de recurso"><a href="#/prompts"${!commands?' aria-current="page"':''}>Plantillas (${h.prompts.length})</a><a href="#/prompts?type=commands"${commands?' aria-current="page"':''}>Comandos documentados (${h.resources.reduce((n,r)=>n+r.commands.length,0)})</a></nav>
      <search><form id="handbook-filter" class="decision-form handbook-filter" method="get" action="#/prompts">${commands?'<input type="hidden" name="type" value="commands">':''}<div><label for="handbook-query">${commands?'Buscar por herramienta':'Buscar una plantilla'}</label><input id="handbook-query" type="search" name="q" maxlength="300" value="${esc(query)}"></div>${!commands?`<div><label for="handbook-topic">Para qué la necesitas</label><select id="handbook-topic" name="topic"><option value="">Todos los temas</option>${Object.entries(topics).map(([id,title])=>`<option value="${id}"${id===topic?' selected':''}>${esc(title)}</option>`).join('')}</select></div>`:''}<button type="submit" class="btn">Buscar</button></form></search>
      <p class="meta" id="handbook-count" role="status" tabindex="-1">${commands?`${commandCount} ${commandCount===1?'comando encontrado':'comandos encontrados'}`:`${templates.length} ${templates.length===1?'plantilla encontrada':'plantillas encontradas'}`}. ${query||topic?`<a href="#/prompts${commands?'?type=commands':''}">Quitar filtros</a>`:''}</p>
      ${commands?`<p>Necesitas tener instalada la herramienta y comprobar la versión. Algunos comandos descargan paquetes, instalan software o arrancan un servidor; su efecto se indica en cada entrada.</p>${commandResources.map(r=>`<section class="handbook-group"><h2><a href="${href(r.id)}">${esc(r.name)}</a></h2>${r.commands.map((c,i)=>commandBlock(c,`${r.id}-${i}`)).join('')}</section>`).join('')||'<p>No hay comandos documentados para esta búsqueda. Prueba otro nombre o abre su guía.</p>'}`:
      `<p>Plantillas originales de Alexandría. Sustituye los campos entre corchetes y añade solo los datos necesarios, sin claves. La plantilla orienta el trabajo; no instala herramientas ni cambia los permisos del cliente.</p><ul class="handbook-prompts">${templates.map(p=>`<li><article><p class="meta">${esc(topics[p.topic])}</p><h2>${esc(p.title)}</h2><p>${esc(p.when)}</p><p><strong>Ten a mano:</strong> ${esc(p.inputs.join(' · '))}.</p><details class="reading-details"><summary>Leer y copiar la plantilla: ${esc(p.title)}</summary><label for="prompt-${esc(p.id)}">Texto de la plantilla</label><textarea id="prompt-${esc(p.id)}" rows="12" readonly>${esc(p.body)}</textarea><button class="btn small" type="button" data-action="copy" data-text="${esc(p.body)}">Copiar plantilla</button><p class="copy-status meta" role="status"></p></details><p><strong>Qué esperar:</strong> ${esc(p.expect)}</p></article></li>`).join('')}</ul>${!templates.length?'<p>No encontramos una plantilla con esos filtros. Prueba otro tema o un nombre más corto.</p>':''}`}`;
  }
  function lookup(catalog,id){const h=get(catalog);return h.resources.find(r=>r.id===id)||h.paths.find(p=>p.id===id);}
  function sectionOf(catalog,id){const h=get(catalog),item=lookup(catalog,id);return item?.section||h.groups.find(g=>g.id===item?.group)?.section||'configurar';}
  const api={index,detail,prompts,selectResources,lookup,sectionOf};
  if(typeof module==='object'&&module.exports)module.exports=api;else root.AlexandriaHandbook=api;
})(typeof globalThis!=='undefined'?globalThis:this);
