/* Local selection from practical topics or curated goal cohorts. */
(function (root) {
  const decisions=typeof module==='object'&&module.exports?require('./decisions.js'):root.AlexandriaDecisions;
  const clients={claude:'claude_code',codex:'codex',antigravity:'antigravity'};
  const supported=new Set(['native','host','connector','project_integration']);
  const fold=value=>String(value||'').toLowerCase().normalize('NFD').replace(/\p{M}/gu,'');
  const clean=value=>fold(value).replace(/[^a-z0-9]+/g,' ').trim();
  const oneOf=(value,allowed,fallback)=>allowed.includes(value)?value:fallback;
  const clientNames={claude:'Claude Code',codex:'Codex',antigravity:'Antigravity',web:'chat web'};
  const labels={
    experience:{unknown:'No sé qué nivel tengo',beginner:'Estoy empezando',intermediate:'Instalo y configuro herramientas',developer:'Programo y uso la terminal'},
    os:{unknown:'Sistema por confirmar',windows:'Windows',mac_arm:'macOS con Apple Silicon',mac_intel:'macOS con Intel',linux:'Linux',browser:'Solo navegador o tableta'},
    ram:{unknown:'RAM por confirmar',small:'Hasta 8 GB de RAM',medium:'16 GB de RAM',large:'32 GB de RAM o más'},
    gpu:{unknown:'GPU por confirmar',no:'Sin GPU dedicada',yes:'Con GPU dedicada'},
    mode:{any:'Sin preferencia de ejecución',existing:'Solo integraciones con mis agentes',api:'Puedo configurar una API de IA',local:'Prefiero modelos locales',no_api:'Evitar una clave nueva de API de IA'}
  };
  function normalize(input={}) {
    return {
      project:String(input.project||'').trim().slice(0,800),goal:String(input.goal||''),topic:String(input.topic||''),group:String(input.group||''),
      experience:oneOf(input.experience,Object.keys(labels.experience),'unknown'),
      os:oneOf(input.os,Object.keys(labels.os),'unknown'),ram:oneOf(input.ram,Object.keys(labels.ram),'unknown'),
      gpu:oneOf(input.gpu,Object.keys(labels.gpu),'unknown'),mode:oneOf(input.mode,Object.keys(labels.mode),'any'),
      clients:[...new Set((Array.isArray(input.clients)?input.clients:[]).filter(id=>Object.hasOwn(clientNames,id)))]
    };
  }
  const vague=new Set(['clientes','ventas','mensajes','fuentes','local','offline','sin api','codex','claude code','aplicacion','ejemplos','codigo','conocimiento','audio','voz']);
  const aliases={web:['sitio web','pagina web','tienda online'],voz:['transcribir','transcripciones','subtitulos','audio a texto'],narrar:['texto a voz','narracion','narrar'],documentos:['preguntar a documentos','mis pdf','mis archivos','consultar documentos'],programar:['agente de codigo','ayuda para programar'],notas:['organizar notas','obsidian'],local:['ia local','modelo local','modelos locales','ollama','chat privado']};
  function inferGoal(project,goals,explicit='') {
    const chosen=goals.find(g=>g.id===explicit);
    if(chosen)return {kind:'explicit',goal:chosen,suggestions:[]};
    const text=' '+clean(project)+' ';
    let ranked=goals.map(goal=>{
      const phrases=[...new Set([...(goal.keywords||[]).filter(k=>!vague.has(clean(k))),...(aliases[goal.id]||[])])];
      const hits=phrases.filter(phrase=>{
        const term=clean(phrase);
        return term && (text.includes(' '+term+' ') || (term.length>5&&term.endsWith('s')&&text.includes(' '+term.slice(0,-1)+' ')));
      });
      // Use the most specific phrase, not repeated synonyms as fake certainty.
      return {goal,score:Math.max(0,...hits.map(h=>Math.min(8,2+clean(h).length/3)))};
    }).filter(item=>item.score>0).sort((a,b)=>b.score-a.score);
    // A local execution preference must not obscure a concrete output such as images.
    if(ranked.some(item=>item.goal.id!=='local'&&item.score>=4))ranked=ranked.filter(item=>item.goal.id!=='local');
    if(!ranked.length)return {kind:'unrecognized',goal:null,suggestions:[]};
    if(ranked.length>1 && ranked[0].score-ranked[1].score<1.5)return {kind:'ambiguous',goal:null,suggestions:ranked.slice(0,3).map(x=>x.goal)};
    return {kind:'detected',goal:ranked[0].goal,suggestions:[]};
  }
  const stop=new Set('quiero necesito crear hacer con para que una unos unas este esta desde tengo usar como por mis del los las un el la de en y o ia'.split(' '));
  function tokens(project) { return [...new Set(clean(project).split(' ').filter(w=>w.length>2&&!stop.has(w)))]; }
  function matchedClients(item,profile) { return profile.clients.filter(id=>clients[id]&&supported.has(item.access?.[clients[id]])); }
  function taskMatches(item,goal,project) {
    const task=fold(project),purpose=fold(item.lead);
    if(goal.id==='imagenes'){
      if(/(?:quitar|eliminar|recortar).{0,25}fondo/.test(task))return /fondo/.test(purpose);
      if(/(?:generar|crear).{0,35}(?:imagen|foto)/.test(task))return /genera|difusion|diffusion/.test(purpose);
    }
    if(goal.id==='video'&&/grabar (?:mi |la )?pantalla|capturar pantalla/.test(task))return /grabar|grabacion|captura/.test(purpose);
    return true;
  }
  function webProject(catalog, profile) {
    const rules=catalog.web_project_rules;
    const text=clean(profile.project);
    if(!rules||!text||new RegExp(rules.exclusions).test(text))return null;
    const request=text.replace(new RegExp(rules.negations,'g'),'');
    for(const id of ['ia','cms','panel']){
      const route=catalog.web_projects.find(item=>item.id===id);
      if(!route||!new RegExp(route.match).test(request))continue;
      const variant=Object.values(route.variants||{}).find(item=>new RegExp(item.match).test(request));
      return {...route,...variant};
    }
    return new RegExp(rules.context).test(text)?catalog.web_projects.find(item=>item.id==='informativa'):null;
  }
  function recommend(catalog,input) {
    const profile=normalize(input);
    const editorialGroups=new Map((catalog.guided_groups||[]).map(group=>[group.id,group]));
    const selectedGroup=editorialGroups.get(profile.group);
    const area=(catalog.discovery.areas||[]).find(item=>item.topics.some(topic=>topic.id===profile.topic));
    const topic=area?.topics.find(item=>item.id===profile.topic);
    const webIntent=!profile.goal&&!topic&&!selectedGroup&&catalog.web_project_rules&&new RegExp(catalog.web_project_rules.context).test(clean(profile.project))&&webProject(catalog,profile);
    const intent=selectedGroup
      ? {kind:'group',goal:{id:selectedGroup.id,title:selectedGroup.title,starters:[],guided:selectedGroup.members},suggestions:[]}
      : topic
      ? {kind:'topic',goal:{id:topic.id,title:topic.title,starters:topic.guided_starters||[],guided:topic.repo_ids},area:area.id,suggestions:[]}
      : webIntent ? {...inferGoal(profile.project,catalog.discovery.goals,'web'),kind:'detected'} : inferGoal(profile.project,catalog.discovery.goals,profile.goal);
    if(!intent.goal)return {profile,intent,picks:[],excluded:{},notices:[]};
    const goal=intent.goal,eligible=new Set(goal.guided||goal.starters),excluded={access:0,device:0,preparation:0,function:0};
    const wantsLocal=profile.mode==='local',terms=tokens(profile.project),notices=[];
    if(selectedGroup?.reference_only||topic?.reference_only){
      return {profile,intent,picks:[],excluded,notices,referenceOnly:true};
    }
    if(!selectedGroup&&!topic){
      const groups=new Set(catalog.repos.filter(item=>eligible.has(item.id)&&item.guided_editorial).map(item=>item.guided_editorial.group));
      for(const item of catalog.repos){
        if(groups.has(item.guided_editorial?.group)&&item.goals?.includes(goal.id))eligible.add(item.id);
      }
    }
    if(profile.clients.includes('web'))notices.push('Un chat web no acredita acceso a Claude Code, Codex o Antigravity. Marca esos clientes solo si ya puedes utilizarlos.');
    if(profile.mode==='existing'&&!profile.clients.some(id=>clients[id]))notices.push('Para aprovechar una suscripción como agente, indica un cliente de código disponible. Un chat web no se convierte automáticamente en esa integración.');
    if(wantsLocal)notices.push('Una ruta con modelos locales puede cubrir solo una etapa. Comprueba embeddings, herramientas y conexiones; no se garantiza un flujo offline.');
    const audienceScores={beginner:{ready_app:55,agent:25,reading:30,setup:0,developer:-30},intermediate:{ready_app:25,agent:25,reading:10,setup:20,developer:5},developer:{ready_app:5,agent:20,reading:5,setup:25,developer:45},unknown:{ready_app:30,agent:20,reading:15,setup:5,developer:0}};
    const ranked=catalog.repos.filter(item=>eligible.has(item.id)&&!item.status).flatMap(item=>{
      const editorial=item.guided_editorial;
      if(item.audit_guidance?.reference_only){excluded.function++;return [];}
      if(editorial&&(editorialGroups.get(editorial.group)?.reference_only||!['principal','alternative'].includes(editorial.role))){
        excluded.function++;return [];
      }
      if(!taskMatches(item,goal,profile.project)){excluded.function++;return [];}
      const a=item.access||{},g=item.getting_started||{},matched=matchedClients(item,profile),reading=g.audience==='reading';
      const needsAgent=(a.mode==='agent_extension'||a.cost==='host_plan')&&!reading;
      if((needsAgent&&!matched.length)||(profile.mode==='existing'&&(!matched.length||a.api==='required'))
        ||(profile.mode==='no_api'&&!['not_required','optional'].includes(a.api))
        ||(wantsLocal&&(!(a.local_model==='supported'||(a.local_model==='not_applicable'&&a.api==='not_required'))||a.api==='required'))){excluded.access++;return [];}
      const useBrowser=!!g.browser_url&&profile.mode!=='existing';
      if(profile.os==='browser'&&!useBrowser&&!reading){excluded.device++;return [];}
      const constrained=profile.ram==='small'||profile.gpu==='no';
      const requirements=g.local_requirements||{},cpuRoute=profile.gpu==='no'&&requirements.cpu_only_os?.includes(profile.os);
      const knownRamCeiling={small:8,medium:16}[profile.ram];
      if(wantsLocal&&!useBrowser&&cpuRoute&&knownRamCeiling&&requirements.cpu_only_min_ram_gb>knownRamCeiling){excluded.preparation++;return [];}
      if(wantsLocal&&profile.experience==='beginner'&&constrained&&item.setup==='heavy'&&!useBrowser){excluded.preparation++;return [];}
      const audienceFit=audienceScores[profile.experience][g.audience]||0;
      let score=audienceFit+(goal.starters.includes(item.id)?18-goal.starters.indexOf(item.id):0);
      if(matched.length)score+=25;
      if(item.setup==='easy')score+=10;
      if(item.setup==='heavy')score-=profile.experience==='developer'?0:20;
      if(constrained&&a.local_model==='supported'&&profile.mode!=='api'&&!useBrowser)score-=item.setup==='heavy'?30:8;
      if(useBrowser&&(profile.experience==='beginner'||profile.os==='browser'))score+=35;
      const hay=clean([item.name,item.lead,editorial?.note,...(item.tags||[]),...(item.practical_examples||[]).map(e=>e.scenario)].join(' '));
      const taskWords=new Set(hay.split(' '));
      const matchedTerms=terms.filter(term=>taskWords.has(term));
      score+=Math.min(25,matchedTerms.length*5);
      const installation=fold([a.hardware_note,g.command,...(g.prerequisites||[])].join(' '));
      const osHint={windows:/windows|winget|powershell/,mac_arm:/macos|apple silicon|metal|mlx/,mac_intel:/macos|mac os/,linux:/linux|apt install/}[profile.os];
      const osFit=!!osHint?.test(installation);
      if(osFit)score+=5; // A source hint, never a compatibility certificate.
      const reasons=[],warnings=[];
      if(matchedTerms.length)reasons.push(`Su ficha menciona ${matchedTerms.slice(0,3).join(', ')}.`);
      if(useBrowser)reasons.push('Hay una aplicación web enlazada por su fuente oficial.');
      else if(profile.experience==='beginner'&&g.audience==='ready_app')reasons.push('Dispone de una ruta de aplicación, preferible a integrar una librería al empezar.');
      else if(profile.experience==='developer'&&g.audience==='developer')reasons.push('Es una pieza de código que puedes integrar en tu proyecto.');
      if(matched.length&&!useBrowser)reasons.push(`La ficha documenta una ruta con ${matched.map(id=>clientNames[id]).join(' o ')}.`);
      if(a.local_model==='not_applicable')reasons.push('La función básica no necesita un modelo de lenguaje.');
      if(item.setup==='heavy'&&!useBrowser)warnings.push('La preparación está marcada como pesada. Revisa infraestructura y requisitos del modelo antes de descargarlo.');
      if(a.local_model==='supported'&&!useBrowser&&(profile.mode==='local'||profile.mode==='no_api'))warnings.push('Tu RAM y GPU ayudan a priorizar; no confirman que un modelo concreto quepa o funcione en tu equipo.');
      if(wantsLocal&&!useBrowser&&cpuRoute&&requirements.note)warnings.push(requirements.note);
      if(useBrowser)warnings.push('La web alojada puede tener cuenta, límites o plan propios. No hereda automáticamente la licencia o el precio del software local.');
      if(['required','unconfirmed','depends'].includes(a.api))warnings.push('Revisa la cuenta y el proveedor de la aplicación: tu suscripción del agente no los incluye automáticamente.');
      if(topic?.guided_starters?.includes(item.id))reasons.push("La revisión de este tema lo propone como punto de partida.");
      if(!reasons.length)reasons.push(`El catálogo lo incluye en «${goal.title}».`);
      return [{item,score,reasons:reasons.slice(0,3),warnings,matched,useBrowser,audienceFit,osFit,taskFit:matchedTerms.length}];
    }).sort((a,b)=>b.score-a.score||a.item.name.localeCompare(b.item.name,'es'));

    let primary=ranked[0];
    const editorialGroup=primary?.item.guided_editorial?.group;
    const group=primary?.item.similares?.grupo;
    if(editorialGroup){
      const preferred=ranked.find(pick=>pick.item.guided_editorial?.group===editorialGroup&&pick.item.guided_editorial.role==='principal');
      if(preferred&&primary.taskFit<=preferred.taskFit&&primary.matched.length<=preferred.matched.length
        &&(profile.experience==='unknown'||primary.audienceFit<=preferred.audienceFit)
        &&(!primary.osFit||preferred.osFit)){
        primary=preferred;
        primary.reasons.unshift('Es la opción principal de la revisión editorial para esta tarea.');
      }
    }else if(group){
      // Compare quality only within a documented group and at the same fit.
      const tied=ranked.filter(pick=>pick.score===primary.score && pick.item.similares?.grupo===group);
      if(tied.length>1 && tied.every(pick=>Number.isFinite(pick.item.calidad?.puntuacion))){
        tied.sort((a,b)=>b.item.calidad.puntuacion-a.item.calidad.puntuacion);
        if(tied[0].item.calidad.puntuacion>tied[1].item.calidad.puntuacion){
          primary=tied[0];
          primary.reasons.push('La puntuación de calidad de su grupo desempató entre opciones con el mismo encaje.');
        }
      }
    }
    const alternatives=[],otherOptions=[];
    for(const pick of ranked){
      if(pick===primary)continue;
      const relation=decisions.relationship(primary.item,pick.item);
      const similar=relation==='undocumented'&&group&&pick.item.similares?.grupo===group;
      const approved=editorialGroup&&pick.item.guided_editorial?.group===editorialGroup;
      if(approved||(!editorialGroup&&(relation==='alternative'||similar)))alternatives.push(pick);
      else otherOptions.push(pick);
    }
    const ordered=[...alternatives,...otherOptions];
    const picks=primary?[primary,...ordered.slice(0,2)]:[];
    return {profile,intent,picks,excluded,notices,extra:selectedGroup?ordered.slice(2):[]};
  }
  function firstTry(pick) {
    return (pick.useBrowser&&pick.item.getting_started?.browser_first_try)||pick.item.first_try||{};
  }
  function startSteps(pick,input) {
    const p=normalize(input),item=pick.item,g=item.getting_started||{},a=item.access||{};
    const needs=(g.prerequisites||[]).join('; ');
    const first=pick.useBrowser
      ? {text:'Abre la aplicación web oficial y crea un archivo o proyecto de prueba. Comprueba sus condiciones de cuenta y uso.',href:g.browser_url,label:'Abrir aplicación web'}
      : {text:`Abre la guía original${p.os!=='unknown'&&p.os!=='browser'?` y comprueba la ruta para ${labels.os[p.os]}`:''}. Prepara: ${needs||'las dependencias indicadas por el autor'}.`,href:g.source||item.repo_url,label:'Abrir guía original'};
    let setup;
    if(pick.matched.length&&!pick.useBrowser)setup=`Sigue la integración documentada con ${pick.matched.map(id=>clientNames[id]).join(' o ')}. Comprueba qué cuenta o modelo usará la herramienta; no basta con que el agente pueda instalarla.`;
    else if(p.mode==='local'&&a.local_model==='supported')setup='Elige el backend y un modelo local que la fuente admita. Revisa memoria, pesos y configuración de cada etapa antes de usar tus propios datos.';
    else if(a.local_model==='not_applicable'&&a.api==='not_required')setup='Empieza por la función básica del programa. Mantén desactivadas las integraciones que todavía no necesites y revisa licencia y servicios opcionales.';
    else setup='Elige una sola ruta de ejecución de la ficha. Configura su cuenta, modelo o proveedor según la guía y revisa los posibles costes antes de continuar.';
    return [first,{text:setup},{text:firstTry(pick).action||'Ejecuta una prueba mínima de la documentación original.'}];
  }
  const api={normalize,inferGoal,recommend,startSteps,firstTry,matchedClients,webProject,labels,clientNames};
  if(typeof module==='object'&&module.exports)module.exports=api;else root.AlexandriaGuide=api;
})(typeof globalThis!=='undefined'?globalThis:this);
