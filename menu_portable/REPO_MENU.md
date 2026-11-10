# REPO_MENU — Menú portable de la biblioteca de repositorios

> Generado: 2026-11-10 · 414 repos curados · Documento 100% para IA.
> COPIA esta carpeta (`menu_portable/`) a la raíz de tu proyecto y
> referencia este archivo desde tu AGENTS.md / system prompt.

---

## INSTRUCCIONES PARA EL AGENTE (léeme entero, soy corto)

Eres un agente que debe elegir qué repositorios instalar/usar para un
proyecto concreto. Tienes un menú curado de **414 repos** de IA y
automatización. Objeto: gastar MÍNIMOS tokens y NO visitar la web.

PROTOCOLO (en orden):

1. **No leas todo.** Este archivo basta para preseleccionar.
2. **Filtra** candidatos por categoría, `role`, `exec`, `setup` y la
   descripción `one` de cada línea del índice de abajo.
3. **Desempata** con `alt`/alternativas: si ya elegiste un repo,
   DESCARTA sus alternativas (cumplen la misma función, no dos).
4. **Combina** con `recipes` si el proyecto es un flujo end-to-end.
5. **Solo para finalistas (<8):** abre el archivo de su categoría en
   `REPO_MENU_cats/NN-*.md` para ver desc completa, `choose_if`,
   `avoid_if`, `combines_with` y el **comando de instalación** derivado.
6. **Instalación:** cada repo trae un comando derivado marcado con
   confianza: `+` seguro · `~` verificar nombre · `?` solo clone + README.

REGLA CLAVE — herramienta de código ≠ modelo en ejecución:
- El AGENTE/IDE con que CONSTRUYES (Claude Code, Antigravity, Codex…)
  solo importa para repos `role=skill/directory` (catálogos de skills).
- El LLM que tu APP llama EN EJECUCIÓN se configura por env vars;
  la mayoría de repos runtime son AGNÓSTICOS al agente de código.

LEYENDA de columnas del índice:
`role`: P=plataforma R=runtime L=librería S=skill D=catálogo A=app
`exec`: loc=local cld=cloud hyb=híbrido · `setup`: E=easy M=medium H=heavy
`inst`: +=comando seguro ~=verificar ?=solo clone

---

## Repos específicos por herramienta de código

| Herramienta | Repos que le sirven |
|---|---|
| claude-code | `claude-code`, `anthropic-skills`, `claude-plugins-official`, `superpowers`, `awesome-claude-code`, `awesome-claude-skills`, `claude-mem`, `n8n-skills`, `geo-seo-claude`, `agency-agents` |
| codex | `codex`, `agent-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`, `spec-kit`, `marketingskills`, `taste-skill` |
| antigravity | `antigravity-awesome-skills`, `awesome-agent-skills`, `prompt-master`, `stitch-skills` |
| gemini-cli | `gemini-cli`, `awesome-agent-skills`, `antigravity-awesome-skills`, `stitch-skills` |
| opencode | `opencode`, `awesome-agent-skills`, `antigravity-awesome-skills`, `prompt-master` |
| grok | Sin repos específicos: úsalo como proveedor LLM en runtime (los repos agnósticos lo aceptan vía API compatible con OpenAI). |
| deepseek | `deepseek-coder` |

## Recetas (stacks end-to-end listos)

Si el proyecto es un PRODUCTO (no una pieza suelta), parte de una
receta y ajusta. Cada receta lista los repos en orden de uso.

### Bot de WhatsApp con IA
**Meta:** Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.  
**Stack:** `evolution-api` → `n8n` → `n8n-mcp` → `n8n-skills` → `chatwoot` → `novu`
**Cómo:** Evolution API mantiene la sesión de WhatsApp y reenvía cada mensaje a un webhook de n8n. El workflow de n8n arma el contexto, llama al LLM, guarda el lead y, si detecta una intención de compra o un problema, abre la conversación en Chatwoot para que responda una persona. Novu avisa al equipo. Con n8n-mcp y n8n-skills, tu agente de código construye y corrige esos workflows por ti.

### Pipeline de Reels / video corto
**Meta:** Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.  
**Stack:** `whisperx` → `chatterbox` → `comfyui` → `real-esrgan` → `remotion` → `ffmpeg` → `moneyprinterturbo`
**Cómo:** WhisperX saca los subtítulos con marcas de tiempo por palabra; Chatterbox genera la locución; ComfyUI produce los visuales y Real-ESRGAN los mejora. Remotion arma el clip con una plantilla reutilizable y FFmpeg exporta el formato final. Si quieres algo inmediato sin montar piezas, MoneyPrinterTurbo hace el recorrido completo desde un tema.

### Agente de research profundo
**Meta:** Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.  
**Stack:** `gpt-researcher` → `searxng` → `crawl4ai` → `browser-use` → `markitdown` → `langfuse`
**Cómo:** GPT Researcher divide la pregunta en sub-preguntas, busca con SearXNG y pasa las URLs a Crawl4AI, que devuelve Markdown listo para el modelo. Browser Use cubre las páginas que necesitan clics o sesión, y MarkItDown suma tus documentos. Langfuse registra cada llamada para revisar costos y errores. DeerFlow es la alternativa si prefieres un harness con sandbox y más autonomía.

### Workspace privado local soberano
**Meta:** Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.  
**Stack:** `ollama` → `odysseus` → `open-notebook` → `mem0` → `searxng`
**Cómo:** Ollama sirve los modelos en tu equipo con una API local. Odysseus centraliza chat, documentos y tareas; Open Notebook indexa tus fuentes para preguntarles como en NotebookLM; mem0 recuerda preferencias y hechos entre sesiones; SearXNG añade búsqueda web sin rastreo.

### Análisis de repos grandes
**Meta:** Que un agente de código entienda una base de código enorme sin gastar todo su contexto.  
**Stack:** `repomix` → `codegraph` → `gitnexus` → `graphify` → `deepwiki-open` → `claude-code`
**Cómo:** CodeGraph y graphify construyen índices estructurales que el agente consulta en lugar de leer archivos completos; GitNexus ayuda a recorrer dependencias; Repomix empaqueta solo la parte relevante cuando necesitas pasar código a un chat. DeepWiki Open produce documentación para humanos. Claude Code (o Codex) usa todo eso como contexto barato.

### Marketing de agencia
**Meta:** Operar campañas, contenido y email a escala con agentes y herramientas propias.  
**Stack:** `marketingskills` → `agency-agents` → `mautic` → `listmonk` → `posthog` → `open-generative-ai`
**Cómo:** Las skills y los roles guían a tu agente de código en cada canal; Mautic segmenta y nutre leads; listmonk envía newsletters; PostHog mide conversión y retención; Open Generative AI produce piezas visuales. Metabase o Superset sirven si necesitas reportes para clientes.

### Web app moderna con IA
**Meta:** Construir un frontend pulido con chat o funciones de IA integradas.  
**Stack:** `ui` → `tailwindcss` → `vercel-ai` → `assistant-ui` → `motion` → `recharts` → `swr`
**Cómo:** shadcn/ui y Tailwind dan la base visual; el AI SDK de Vercel resuelve streaming, tool calling y proveedores; assistant-ui aporta la interfaz de chat; Motion anima y Recharts dibuja datos; SWR gestiona el fetching. Para diseñar antes de codificar, prueba Open Design o Penpot.

### Construir una app o servidor MCP
**Meta:** Exponer tus datos o herramientas a Claude, ChatGPT, Cursor y otros agentes con Model Context Protocol.  
**Stack:** `awesome-mcp-servers` → `fastmcp` → `mcp-typescript-sdk` → `mcp-inspector` → `servers` → `mcp-use`
**Cómo:** Busca en awesome-mcp-servers antes de construir. Si no existe, FastMCP (Python) o el SDK oficial de TypeScript te dan el servidor con poco código; los servidores de referencia muestran cómo modelar tools, recursos y prompts. MCP Inspector valida el servidor antes de conectarlo a Claude Code, Codex o Cursor. mcp-use sirve cuando quieres una app MCP con interfaz propia.

### Documentos → presentaciones
**Meta:** Pasar informes, PDFs o notas a presentaciones editables o slides web.  
**Stack:** `markitdown` → `docling` → `ppt-master` → `slidev` → `marp`
**Cómo:** MarkItDown (o Docling si el PDF tiene tablas y columnas) normaliza todo a Markdown. Desde ahí, PPT Master genera un PowerPoint nativo editable, Slidev produce slides web con código y componentes, y Marp exporta a PDF o PPTX con estilos simples.

### ChatGPT privado con modelos locales
**Meta:** Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.  
**Stack:** `ollama` → `open-webui` → `searxng` → `litellm`
**Cómo:** Ollama corre los modelos y expone una API compatible con OpenAI; Open WebUI se conecta a ella y añade cuentas de usuario, subida de documentos, búsqueda web vía SearXNG y herramientas. Si algunos usuarios necesitan modelos comerciales, LiteLLM unifica el acceso con control de costos.

### RAG sobre tus documentos
**Meta:** Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.  
**Stack:** `docling` → `llama-index` → `qdrant` → `litellm` → `ragas` → `langfuse`
**Cómo:** Docling convierte los documentos en Markdown estructurado; LlamaIndex los fragmenta, genera embeddings y los guarda en Qdrant; en cada pregunta recupera los fragmentos relevantes y llama al modelo vía LiteLLM. Ragas mide si la respuesta usa bien el contexto y Langfuse registra cada consulta. Si prefieres una plataforma con UI, RAGFlow o AnythingLLM cubren el flujo completo.

### Agente de código potenciado
**Meta:** Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.  
**Stack:** `claude-code` → `superpowers` → `context7` → `serena` → `claude-mem` → `skillspector`
**Cómo:** Superpowers obliga al agente a planificar, escribir pruebas y revisar; Context7 le pasa la documentación vigente de cada librería; Serena le da navegación semántica del código en lugar de leer archivos enteros; claude-mem conserva decisiones entre sesiones. SkillSpector revisa cualquier skill nueva antes de instalarla.

### Agente de voz en tiempo real
**Meta:** Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.  
**Stack:** `pipecat` → `faster-whisper` → `litellm` → `kokoro` → `livekit-agents`
**Cómo:** Pipecat encadena transporte de audio, detección de voz, STT, LLM y TTS con manejo de interrupciones. faster-whisper transcribe, el LLM (vía LiteLLM) decide qué decir y Kokoro lo sintetiza. LiveKit Agents es la alternativa si quieres WebRTC y telefonía SIP resueltos de serie.

### Analítica de producto con IA
**Meta:** Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.  
**Stack:** `posthog` → `duckdb` → `wrenai` → `superset` → `umami`
**Cómo:** PostHog captura eventos y embudos; exportas a Parquet y analizas con DuckDB sin montar un warehouse; WrenAI traduce preguntas a SQL sobre tu esquema; Superset publica los dashboards. Si solo necesitas visitas y fuentes de tráfico, Umami o Plausible bastan.

---

## ÍNDICE COMPACTO (1 línea por repo)

Formato: `id` [role|exec|setup|inst] — descripción — alt:…

### Sin categoría

- `guia` [D|loc|E|+] — El texto escrito a mano de la guía anterior se incorporó a las fichas; `Guia.md` ahora se genera desde el índi
- `tools` [D|loc|E|+] — Contiene utilidades de apoyo de la biblioteca. Sirve como referencia interna, no como dependencia de un proyec

### 1. Automatización, Mensajería & CRM (33)
Detalle: `REPO_MENU_cats/01-automatizaci-n-mensajer-a-crm.md`

- `activepieces` [P|hyb|M|~] — Orquesta tus apps con flujos visuales sin código y conserva el control al alojarlo en tu servidor. — alt: n8n
- `appsmith` [P|loc|M|~] — Arrastra widgets, conéctalos a más de 25 bases de datos o cualquier API y añade lógica en JavaScript. Pensada  — alt: tooljet,budibase,nocodb
- `awesome-n8n-templates` [D|loc|E|+] — Reúne workflows de n8n ordenados por tema (Gmail, Telegram, WhatsApp, Notion, OpenAI y más). Sirve para arranc
- `baileys` [L|loc|E|~] — Implementa el protocolo de WhatsApp Web directamente, así que consume muy pocos recursos. Es la base de muchas — alt: whatsapp-web-js,waha
- `botpress` [P|hyb|M|~] — Combina un estudio visual con código para crear agentes que usan bases de conocimiento, herramientas y canales — alt: typebot,rasa
- `budibase` [P|loc|M|~] — Genera apps CRUD, formularios y flujos a partir de bases existentes y ahora añade agentes de IA agnósticos de  — alt: appsmith,tooljet,nocodb
- `chatwoot` [P|loc|H|~] — Reúne WhatsApp, email, web chat y redes en una sola bandeja, con paso a un humano cuando el bot no basta. Alte
- `erpnext` [P|loc|H|~] — Cubre la operación completa de una empresa sin licencias de pago. Muy usado por pymes y en manufactura y distr — alt: odoo
- `evolution-api` [P|loc|H|~] — Conecta WhatsApp a tu stack mediante una API REST propia, sin quedar atado a un proveedor cerrado. — alt: whatsapp-web-js,waha
- `fluxer` [P|hyb|M|?] — Apunta a unificar varios modelos generativos tras un cliente único.
- `huginn` [P|loc|M|?] — Vigila webs, feeds y APIs y dispara acciones cuando algo cambia, todo alojado por ti y sin depender de tercero — alt: n8n,node-red
- `kestra` [P|loc|M|~] — Define flujos en YAML con un editor web, cientos de plugins y disparadores por calendario o eventos. Pensado p — alt: windmill,trigger-dev
- `listmonk` [P|loc|M|?] — Envía newsletters y campañas a miles de suscriptores desde un solo binario ligero que consume muy pocos recurs
- `mautic` [P|loc|H|?] — Nutre leads por email con reglas y segmentos automáticos, sin ceder los datos de tus clientes a un SaaS.
- `n8n` [P|loc|M|~] — Conecta cualquier app con cualquier otra en tu propio servidor, sin pagar una suscripción mensual por cada flu — alt: activepieces,huginn,windmill,node-red
- `n8n-io` [P|loc|M|~] — No aporta nada distinto a la ficha principal.
- `n8n-mcp` [R|hyb|M|~] — Resuelve el problema de que un LLM invente parámetros de nodos que no existen y genere workflows rotos.
- `n8n-skills` [S|cld|E|+] — Enseña a tu agente de código a escribir flujos de n8n en JSON que funcionan a la primera, con menos idas y vue
- `nocodb` [P|loc|E|~] — Ofrece vistas de tabla, kanban, galería y formularios sobre PostgreSQL, MySQL o SQLite, con API REST automátic — alt: appsmith,budibase
- `node-red` [P|loc|E|~] — Conecta dispositivos, APIs y servicios arrastrando nodos en el navegador. Es muy usado en IoT, domótica e indu — alt: n8n,huginn
- `novu` [P|hyb|M|~] — Envía notificaciones por email, SMS, push y chat desde una sola API, sin integrar y mantener cada proveedor po
- `odoo` [P|loc|H|~] — Integra CRM, ventas, facturación, inventario, RR. HH. y sitio web en una sola plataforma modular. La usan pyme — alt: erpnext
- `openwa` [L|loc|E|~] — Envía y recibe mensajes de WhatsApp desde tu propio script con una API sencilla y expresiva.
- `rasa` [R|loc|H|~] — Permite crear asistentes de texto y voz con control total del diálogo y de los datos. Muy usado en empresas qu — alt: botpress
- `self-hosted-ai-starter-kit` [P|loc|M|~] — Kit oficial de n8n que levanta un entorno de IA privado: n8n para orquestar, Ollama para modelos, Qdrant como 
- `tooljet` [P|loc|M|~] — Construye apps internas arrastrando componentes y conectando bases y APIs, o genéralas describiéndolas con IA. — alt: appsmith,budibase
- `trigger-dev` [P|hyb|M|~] — Escribe tareas largas o con reintentos en TypeScript dentro de tu app y Trigger.dev las ejecuta, reintenta y m — alt: windmill,kestra
- `twenty-main` [P|hyb|H|~] — La premisa es tratar el CRM como una pieza más de tu stack: lo construyes, lo despliegas y lo versionas igual 
- `typebot` [P|loc|M|~] — Diseña conversaciones con bloques arrastrables (preguntas, condiciones, integraciones, IA) y publícalas en web — alt: botpress
- `waha` [P|loc|E|~] — Expone WhatsApp como API HTTP con webhooks, lista para conectar a n8n o a tu backend. Ofrece motores basados e — alt: evolution-api,whatsapp-web-js,baileys
- `whatsapp-agentkit` [S|hyb|E|+] — Arranca un bot de WhatsApp con IA sin escribir código, a partir de una plantilla guiada.
- `whatsapp-web-js` [L|loc|E|~] — Permite enviar y recibir mensajes, medios y grupos desde código usando una sesión de WhatsApp Web. Muy usada p — alt: baileys,waha,evolution-api
- `windmill` [P|loc|M|~] — Convierte scripts de Python, TypeScript, Go o SQL en workflows, endpoints y apps con UI generada. Sirve a equi — alt: n8n,kestra,trigger-dev

### 2. Skills, Prompts & Guías de Agente (38)
Detalle: `REPO_MENU_cats/02-skills-prompts-gu-as-de-agente.md`

- `12-factor-agents` [D|hyb|E|+] — Ensayo de Dex Horthy (HumanLayer) que resume lo aprendido construyendo agentes para clientes reales: los produ
- `agency-agents` [S|hyb|E|+] — Plantillas de subagente en Markdown agrupadas por divisiones, como una agencia completa: ingeniería, diseño, p — alt: wshobson-agents
- `agent-skills` [S|loc|E|+] — Skills listas para Claude Code, Codex y otros agentes que cubren pruebas, rendimiento, accesibilidad, revisión — alt: superpowers
- `agent-toolkit` [S|cld|E|+] — Te da skills listas para tareas comunes, para que tu agente sea productivo desde el primer día.
- `agents-towards-production` [D|cld|M|+] — Playbook de Nir Diamant (DiamantAI) con un tutorial por carpeta, en notebooks o scripts listos para ejecutar, 
- `ai-agents-for-beginners` [D|cld|M|+] — Recorre desde qué es un agente hasta producción: frameworks, patrones de diseño (uso de herramientas, planific
- `andrej-karpathy-skills` [S|cld|E|+] — Ajusta el comportamiento de tu asistente con principios claros, sin atarte a una herramienta concreta.
- `anthropic-skills` [S|cld|E|+] — Repositorio de Anthropic con skills listas para Claude Code, Claude.ai y la API: creativas, técnicas (pruebas 
- `antigravity-awesome-skills` [S|hyb|E|+] — Antes llamada Antigravity Awesome Skills, reúne miles de skills por dominio (desarrollo, seguridad, DevOps, da — alt: awesome-agent-skills,awesome-claude-skills,wshobson-agents
- `arcads-claude-code` [S|cld|M|+] — Repo de trabajo que convierte Claude Code o Cursor en un estudio de anuncios: genera videos UGC, presentacione
- `awesome-agent-skills` [D|hyb|E|+] — Índice mantenido por VoltAgent que enlaza skills publicadas por los equipos de cada producto (Anthropic, Googl — alt: antigravity-awesome-skills,awesome-claude-skills
- `awesome-claude-code` [D|cld|E|+] — Índice comunitario del ecosistema de Claude Code organizado por temas: guías de inicio, recursos oficiales de  — alt: awesome-claude-skills
- `awesome-claude-skills` [D|cld|E|+] — Recopilación de skills por áreas (documentos, desarrollo, datos, marketing, escritura, multimedia, productivid — alt: awesome-agent-skills,antigravity-awesome-skills,awesome-claude-code
- `awesome-copilot` [S|cld|E|+] — Repositorio de la organización GitHub que reúne personalizaciones de Copilot aportadas por la comunidad: agent
- `awesome-llm-apps` [D|hyb|M|+] — Repositorio de Shubham Saboo con plantillas de código abierto ordenadas por tipo: agentes simples de un solo a — alt: openai-cookbook,claude-cookbooks
- `bmad-method` [S|loc|E|+] — Organiza el trabajo con IA en roles y documentos (brief, PRD, arquitectura, historias) que el agente de código — alt: spec-kit
- `claude-cookbooks` [D|cld|E|+] — Notebooks y guías de Anthropic con código copiable para construir con Claude: clasificación, resumen, RAG (con — alt: openai-cookbook,awesome-llm-apps
- `claude-plugins-official` [S|cld|E|+] — Directorio curado desde el que Claude Code instala plugins de forma nativa. En `/plugins` están los que mantie — alt: wshobson-agents
- `context-engineering` [D|cld|E|+] — Enseña de forma sistemática qué meter en el prompt y qué dejar fuera para que el modelo responda mejor.
- `ecc` [P|loc|H|~] — Actúa como capa intermedia entre el modelo y tu sistema, de modo que las acciones del agente pasan por un escu
- `fabric` [A|hyb|E|?] — Organiza prompts reutilizables (patterns) para tareas como resumir videos, extraer ideas o analizar textos. Se — alt: prompts-chat
- `generative-ai-for-beginners` [D|cld|E|+] — Recorre desde qué es un LLM hasta prompts, RAG, agentes, seguridad y fine-tuning, con código en Python y TypeS — alt: llm-course
- `geo-seo-claude` [S|cld|E|+] — Añade a Claude Code comandos `/geo` que auditan un sitio para buscadores con IA (ChatGPT, Claude, Perplexity, 
- `humanizer` [S|hyb|E|+] — Detecta 26 patrones típicos de la prosa de LLM (contrastes tipo 'no es X, es Y', cierres dramáticos, tríadas f — alt: stop-slop
- `loop-engineering` [S|loc|E|+] — Propone dejar de escribir prompts aislados y diseñar ciclos con objetivo, verificación y puntuación para que e
- `marketingskills` [S|hyb|E|+] — Skills de Corey Haines para marketers técnicos y founders que trabajan con agentes de código: conversión, copy
- `openai-cookbook` [D|cld|E|+] — Reúne recetas sobre embeddings, function calling, RAG, evaluación, agentes y voz. Sirve como referencia prácti — alt: claude-cookbooks,awesome-llm-apps
- `ponytail` [S|loc|E|+] — Empuja al agente a reutilizar, borrar y simplificar antes de añadir código nuevo. Reduce soluciones infladas y
- `prompt-eng-tutorial` [D|cld|E|+] — Nueve capítulos con ejercicios sobre claridad, roles, ejemplos, razonamiento paso a paso y cómo evitar alucina — alt: prompt-engineering-guide
- `prompt-engineering-guide` [D|cld|E|+] — Explica técnicas de prompting, riesgos y aplicaciones con ejemplos y referencias a papers. Disponible en vario — alt: prompt-eng-tutorial
- `prompt-master` [S|cld|E|+] — Te ayuda a escribir mejores prompts con meta-prompting reutilizable, como una capa por encima de cualquier IA.
- `prompts-chat` [D|loc|E|+] — Reúne miles de prompts de rol y tarea para ChatGPT, Claude y otros, con buscador web. Puedes desplegar tu prop — alt: fabric
- `skills` [D|cld|E|+] — Muestra cómo se escribe una buena skill para agentes, con pocos ejemplos pero de alta calidad para usarlos com
- `skillspector` [S|cld|E|+] — Resuelve el riesgo de ejecutar skills de terceros sin revisión.
- `spec-kit` [S|loc|E|+] — Te guía para escribir especificación, plan y tareas antes de que el agente programe. Funciona con Copilot, Cla — alt: bmad-method
- `stop-slop` [S|hyb|E|+] — Un SKILL.md con tres archivos de referencia (frases a eliminar, estructuras a evitar y ejemplos antes/después) — alt: humanizer
- `superpowers` [S|cld|E|+] — Le da a tu agente de código un método de trabajo completo y coherente (planear, probar, revisar), no piezas su — alt: agent-skills
- `wshobson-agents` [S|hyb|E|+] — Colección de Seth Hobson que agrupa subagentes especialistas, skills y comandos en plugins por área: desarroll — alt: claude-plugins-official,antigravity-awesome-skills,agency-agents

### 3. Frameworks & Orquestación de Agentes (59)
Detalle: `REPO_MENU_cats/03-frameworks-orquestaci-n-de-agentes.md`

- `adk-python` [L|hyb|E|~] — Define agentes y sistemas multiagente con herramientas, memoria y evaluación, con interfaz web de pruebas incl — alt: langgraph,openai-agents-python
- `ag2` [L|cld|M|~] — Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo. — alt: autogen
- `agent-framework` [R|hyb|M|~] — Une la simplicidad de AutoGen con las capacidades empresariales de Semantic Kernel: workflows con estado, obse — alt: autogen,semantic-kernel
- `agent-protocol` [D|loc|E|+] — Define cómo se ejecuta un agente, cómo recibe entradas y cómo guarda su estado, sin atarse a un framework. Es 
- `agno` [R|hyb|E|~] — Construye agentes con memoria, RAG y herramientas, y sírvelos como API con su plataforma. Antes se llamaba Phi — alt: crewai
- `aider` [R|hyb|E|~] — Le pides cambios en lenguaje natural y Aider edita los archivos y confirma cada cambio en Git. Funciona con ca — alt: opencode,cline,continue
- `autogen` [R|hyb|M|~] — Popularizó los sistemas multiagente que conversan para resolver tareas. Microsoft recomienda usar Agent Framew — alt: agent-framework,ag2,crewai
- `autogpt` [P|hyb|H|~] — El famoso proyecto de agentes autónomos evolucionó a una plataforma con editor de bloques, marketplace y servi — alt: sim,langflow,flowise
- `autoresearch` [P|hyb|M|~] — Proyecto pequeño y exploratorio de Karpathy, más que una herramienta pulida.
- `awesome-langgraph` [D|cld|E|+] — Es una lista curada, no una herramienta ejecutable.
- `claude-code` [R|cld|E|+] — Lee y edita archivos, ejecuta comandos, hace commits y abre PRs a partir de instrucciones en lenguaje natural. — alt: codex,gemini-cli,opencode,goose
- `cline` [R|hyb|E|~] — Planifica, edita archivos, ejecuta comandos y usa el navegador pidiendo aprobación en cada paso. Admite MCP y  — alt: continue,aider
- `codex` [R|cld|E|+] — Lee tu repositorio, propone y aplica cambios y ejecuta comandos dentro de un sandbox. Usa AGENTS.md para el co — alt: claude-code,gemini-cli,opencode
- `composio` [P|cld|E|+] — Da a cualquier agente herramientas listas para Gmail, Slack, GitHub, Notion y cientos más, gestionando OAuth p
- `computer-use-preview` [R|cld|M|+] — Muestra cómo un modelo Gemini con computer use controla un navegador para completar tareas. Es una vista previ — alt: browser-use,skyvern
- `continue` [R|hyb|E|~] — Integra chat, edición y autocompletado en el IDE con cualquier modelo, y permite ejecutar comprobaciones de IA — alt: cline,aider
- `crewai` [L|cld|E|~] — Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárq — alt: autogen,langgraph,agno
- `deepagents` [R|hyb|E|~] — Da a cualquier modelo las capacidades de los agentes profundos (planificar, delegar, usar archivos) sin constr — alt: openai-agents-python
- `deeptutor` [A|hyb|M|~] — Resuelve dudas, genera ejercicios y guía el estudio con RAG sobre tu material y memoria del alumno. Es un prod — alt: open-notebook
- `deer-flow` [P|hyb|M|~] — Coordina tareas complejas delegando en agentes especializados.
- `dify` [P|hyb|M|~] — Combina orquestación de prompts, RAG, agentes, workflows y observabilidad en un mismo producto autoalojable. — alt: sim,ragflow
- `dspy` [L|hyb|M|~] — Defines módulos con firmas de entrada y salida y DSPy optimiza automáticamente los prompts y ejemplos con tus  — alt: promptfoo
- `e2b` [P|cld|E|+] — Arranca microVMs aisladas en milisegundos donde el agente puede ejecutar código, instalar paquetes o usar un e — alt: sandbox
- `flowise` [A|hyb|E|~] — Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible. — alt: sim,autogpt
- `gemini-cli` [R|cld|E|+] — Programa, investiga y automatiza tareas desde la terminal con contexto de millones de tokens y búsqueda de Goo — alt: claude-code,codex,opencode
- `goose` [R|hyb|E|~] — Funciona como app de escritorio o CLI y va más allá del código: automatiza tareas de desarrollo y de sistema c — alt: opencode,claude-code,open-interpreter
- `gpt-researcher` [P|hyb|M|~] — Planifica sub-preguntas, busca fuentes y redacta un informe con referencias. — alt: storm,vane
- `haystack` [L|hyb|M|~] — Compone pipelines modulares de recuperación, generación y agentes con componentes intercambiables. Muy usado e — alt: llama-index,langchain
- `hermes-agent` [A|loc|M|~] — Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local. — alt: openclaw,mercury-agent
- `langchain` [L|cld|M|~] — Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos. — alt: llama-index,haystack,semantic-kernel
- `langflow` [A|hyb|M|~] — Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código Python. — alt: sim,autogpt
- `langgraph` [R|hyb|M|~] — Modela agentes y flujos multiagente como grafos de nodos con estado compartido y checkpoints. Pensado para age — alt: crewai,openai-agents-python,pydantic-ai,langgraph-supervisor-py,adk-python
- `langgraph-supervisor-py` [L|hyb|E|~] — Facilitaba el patrón supervisor en sistemas multiagente. LangChain ahora recomienda implementar ese patrón dir — alt: langgraph
- `langgraphjs` [R|hyb|M|~] — Lleva el modelo de grafos con estado, checkpoints y human-in-the-loop de LangGraph al ecosistema JavaScript. — alt: mastra,vercel-ai
- `llama-index` [L|hyb|E|~] — Ofrece cargadores para cientos de fuentes, índices, motores de consulta y agentes centrados en documentos. Su  — alt: haystack,langchain
- `llm-council` [P|hyb|M|~] — Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.
- `mastra` [L|hyb|E|~] — Reúne en un solo paquete agentes con memoria, workflows con estado, RAG, evals y un playground local. Pensado  — alt: langgraphjs,vercel-ai
- `mercury-agent` [A|hyb|E|~] — Recuerda lo importante, pide permiso antes de actuar y trae 31 herramientas, tableros kanban y skills extensib — alt: openclaw,hermes-agent
- `mirofish` [P|hyb|H|~] — Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.
- `multica` [P|hyb|M|~] — Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.
- `nemo-agent-toolkit` [L|hyb|H|~] — Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.
- `nemoclaw` [P|hyb|H|~] — Ejecuta agentes populares dentro de los sandboxes de NVIDIA OpenShell con inferencia gestionada y políticas de — alt: sandbox
- `open-interpreter` [R|loc|E|~] — Ejecuta código y comandos en tu máquina para cumplir tareas descritas en lenguaje natural. Su versión actual s — alt: goose
- `open-swe` [R|cld|M|+] — Trabaja en segundo plano a partir de issues o mensajes, planifica, programa en un sandbox y abre PRs. Inspirad — alt: openhands,swe-agent
- `openai-agents-python` [L|hyb|E|~] — Define agentes con instrucciones y herramientas, pasa el control entre ellos y añade validaciones. Funciona co — alt: pydantic-ai,langgraph,smolagents,deepagents,adk-python
- `openclaw` [A|hyb|M|~] — Un solo operador, muchas superficies: el asistente vive en tu equipo, tiene memoria, ejecuta tareas reales y r — alt: hermes-agent,mercury-agent
- `opencode` [R|hyb|E|~] — Ofrece una TUI cuidada, modo cliente-servidor, LSP y agentes configurables. Sirve si quieres un agente libre d — alt: claude-code,codex,goose,gemini-cli,aider
- `openevolve` [R|cld|H|+] — Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.
- `openhands` [P|hyb|M|~] — El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox. — alt: open-swe,swe-agent
- `pydantic-ai` [L|hyb|E|~] — Construye agentes con salidas validadas, herramientas tipadas e inyección de dependencias, al estilo FastAPI.  — alt: openai-agents-python,smolagents,langgraph
- `ruflo` [P|hyb|H|?] — Orquesta swarms de agentes especializados a escala.
- `sandbox` [P|hyb|M|~] — Resuelve el riesgo de dejar que un agente toque tu host: todo corre contenido en un contenedor reproducible. — alt: nemoclaw,e2b
- `semantic-kernel` [L|hyb|M|~] — Pensado para empresas que ya usan .NET o Java y quieren añadir IA con patrones conocidos. Su evolución para ag — alt: agent-framework,langchain
- `sim` [P|hyb|M|~] — Diseña agentes conectando bloques en un canvas, prueba en vivo y despliega como API o chat. Open source y auto — alt: flowise,langflow,dify,autogpt
- `smolagents` [L|hyb|E|~] — Sus agentes expresan las acciones como código en vez de JSON, lo que reduce pasos y errores. El núcleo cabe en — alt: pydantic-ai,openai-agents-python
- `storm` [R|hyb|M|~] — Simula conversaciones entre perspectivas para hacer preguntas, busca fuentes y redacta un artículo estructurad — alt: gpt-researcher
- `swe-agent` [R|hyb|M|~] — Resuelve issues reales con el modelo que elijas y sirve como base de investigación en agentes de software. Tam — alt: openhands,open-swe
- `t3code` [A|loc|E|~] — No sustituye al agente: orquesta Claude Code, Codex y otros desde una UI cómoda, también en el móvil. Útil par
- `vercel-ai` [L|hyb|E|~] — Unifica la llamada a decenas de proveedores con una API común y trae hooks de React para chat con streaming. E — alt: langgraphjs,mastra

### 4. Scraping, Búsqueda & Research Web (29)
Detalle: `REPO_MENU_cats/04-scraping-b-squeda-research-web.md`

- `agent-reach` [A|loc|E|~] — Un solo comando para que el agente lea y busque en redes y plataformas populares, incluidas chinas como Bilibi — alt: snscrape
- `archivebox` [A|loc|E|~] — Le das URLs, marcadores o historial y guarda copias completas para siempre. Útil para investigación y preserva
- `browser-harness` [R|loc|E|~] — Conecta el agente a tu navegador por CDP con un arnés pequeño y editable. Útil cuando necesitas libertad total — alt: playwright-mcp,chrome-devtools-mcp
- `browser-use` [L|hyb|M|~] — Resuelve la fragilidad del scraping basado en CSS: el agente "ve" la página como un humano y decide la siguien — alt: computer-use-preview,stagehand,skyvern,playwright-mcp
- `changedetection` [A|loc|E|~] — Vigila precios, stock, documentación o cualquier texto de una página y te avisa cuando cambia. Admite navegado
- `crawl4ai` [L|loc|M|~] — Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pen — alt: jina-reader
- `crawlee` [L|loc|M|~] — Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navega
- `crawlee-python` [L|loc|M|~] — Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosist
- `firecrawl` [P|cld|M|+] — Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio — alt: jina-reader
- `instaloader` [L|loc|E|~] — Resuelve el archivado masivo de Instagram sin recurrir a APIs oficiales de pago ni herramientas manuales.
- `jina-reader` [P|cld|E|+] — Pega `https://r.jina.ai/` delante de una URL y obtienes su contenido limpio. También busca en la web con `s.ji — alt: firecrawl,crawl4ai
- `last30days-skill` [S|cld|E|+] — Busca lo que la gente está diciendo ahora sobre un tema y lo resume con fuentes. Prioriza señales reales como 
- `lightpanda` [R|loc|E|?] — Ejecuta JavaScript y es compatible con Puppeteer y Playwright por CDP, usando una fracción de memoria. Ideal p
- `llm-scraper` [L|hyb|E|~] — Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el — alt: maxun
- `maxun` [P|loc|M|~] — Grabas lo que quieres extraer haciendo clic en la página y Maxun crea un robot que lo repite, con paginación y — alt: scrapegraph-ai,llm-scraper
- `playwright` [L|hyb|M|~] — Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola A — alt: puppeteer,selenium
- `playwright-cli` [S|hyb|E|+] — Resuelve el problema de los árboles de accesibilidad y los JSON de herramientas que inflan el prompt en cada t
- `puppeteer` [L|loc|E|~] — Automatiza navegación, capturas, PDFs y pruebas. Es la base de muchas herramientas de scraping. — alt: playwright,selenium
- `scrapegraph-ai` [L|hyb|M|~] — Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué e — alt: maxun
- `scrapely` [L|loc|E|~] — Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mis
- `scrapling` [L|loc|M|~] — Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica 
- `scrapy` [L|loc|M|~] — Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesam
- `searxng` [P|loc|E|~] — Combina resultados de más de 70 servicios sin rastrearte. Muchos agentes de investigación lo usan como API de 
- `selenium` [L|loc|M|~] — Estándar W3C WebDriver, muy usado en pruebas empresariales con Selenium Grid para paralelizar. — alt: playwright,puppeteer
- `skyvern` [P|hyb|M|~] — Completa formularios, compras o descargas en sitios que nunca vio, entendiendo la página con visión. Incluye U — alt: browser-use,stagehand,computer-use-preview
- `snscrape` [L|loc|E|~] — Resuelve la recolección histórica de datos sociales cuando las APIs de pago no son viables o no existen. — alt: agent-reach
- `stagehand` [L|hyb|E|~] — Usa `act`, `extract` y `observe` para que la IA haga lo difícil y tu código lo predecible. Basado en Playwrigh — alt: browser-use,skyvern
- `vane` [A|loc|E|~] — Busca en la web con SearXNG y responde con citas usando modelos locales o en la nube. Incluye modos de enfoque — alt: gpt-researcher
- `yt-dlp` [A|loc|E|~] — Descarga videos, audios, subtítulos y metadatos de YouTube y miles de plataformas. Base de muchos pipelines de

### 5. MCP & Conectividad (20)
Detalle: `REPO_MENU_cats/05-mcp-conectividad.md`

- `awesome-mcp-clients` [D|loc|E|+] — Ayuda a elegir dónde usar tus servidores MCP: chats de escritorio, editores, CLIs y plataformas.
- `awesome-mcp-servers` [D|hyb|E|+] — Resuelve el "¿ya existe un servidor para X?" antes de que construyas el tuyo desde cero.
- `blender-mcp` [R|loc|E|~] — Crea y modifica escenas, objetos y materiales hablando con tu asistente. Útil para prototipos 3D rápidos.
- `chrome-devtools-mcp` [R|loc|E|~] — Tu agente de código puede abrir páginas, leer errores de consola, inspeccionar peticiones y medir rendimiento  — alt: playwright-mcp,browser-harness
- `context7` [R|cld|E|+] — Evita que el modelo invente APIs viejas: busca la documentación vigente de la librería que estás usando y la i — alt: deepwiki-open
- `fastmcp` [L|loc|E|~] — Convierte funciones Python en herramientas MCP con un decorador y añade autenticación, composición de servidor — alt: mcp-python-sdk
- `figma-context-mcp` [R|hyb|E|~] — Simplifica la respuesta de la API de Figma y da al agente solo lo relevante (estructura, estilos, medidas) par
- `github-mcp-server` [R|hyb|E|~] — Conecta asistentes y agentes con la plataforma GitHub: repositorios, issues, pull requests, Actions y segurida
- `langchain-mcp-adapters` [L|loc|E|~] — Permite que tus agentes de LangGraph usen cualquier servidor MCP sin escribir adaptadores. El repo está archiv — alt: mcp-use
- `mcp` [L|hyb|M|~] — Resuelve la fragmentación: cada integración de IA dejaba de ser ad-hoc y pasa a hablar un protocolo común.
- `mcp-for-beginners` [D|loc|E|+] — Explica los fundamentos del Model Context Protocol, seguridad y despliegue con ejercicios por lenguaje. Dispon
- `mcp-inspector` [A|loc|E|~] — Conéctate a cualquier servidor MCP, lista sus herramientas y recursos y lánzalos a mano para ver respuestas y 
- `mcp-neo4j` [R|hyb|M|~] — Resuelve el acceso natural a grafos desde un LLM: el asistente consulta y escribe Cypher sin que tú escribas e
- `mcp-python-sdk` [L|loc|E|~] — Implementación de referencia del protocolo en Python, con la API FastMCP integrada para servidores sencillos. — alt: fastmcp
- `mcp-typescript-sdk` [L|loc|E|~] — Base de la mayoría de servidores MCP en Node.js, con transportes stdio y HTTP. — alt: mcp-use
- `mcp-use` [L|hyb|M|~] — Resuelve el salto del SDK base (verboso) a algo productivo: registro de tools, inspector y despliegue incluido — alt: langchain-mcp-adapters,mcp-typescript-sdk
- `playwright-mcp` [R|loc|E|~] — Da a tu agente un navegador real controlado por el árbol de accesibilidad, sin depender de capturas. Ideal par — alt: chrome-devtools-mcp,browser-use,browser-harness
- `public-apis` [D|cld|E|+] — Resuelve el descubrimiento: en un solo lugar tienes URLs, autenticación y HTTPS de cada API en lugar de buscar
- `serena` [R|loc|E|~] — En vez de leer archivos enteros, el agente busca símbolos, referencias y edita a nivel de función usando servi — alt: codegraph,gitnexus
- `servers` [D|hyb|M|+] — Resuelve la falta de ejemplos canónicos: muestra cómo se construye un servidor MCP correcto, paso a paso.

### 6. Memoria, RAG & LLM Ops (32)
Detalle: `REPO_MENU_cats/06-memoria-rag-llm-ops.md`

- `agentmemory` [L|hyb|E|?] — Resuelve el "re-explica todo" al cambiar de asistente: la memoria vive fuera del cliente. — alt: engram,supermemory,claude-mem
- `chroma` [R|loc|E|~] — Se usa embebida en tu script Python o como servidor, con embeddings automáticos. Perfecta para prototipos de R — alt: qdrant,pgvector,milvus,faiss
- `claude-mem` [S|loc|E|+] — Registra lo que hace el agente en cada sesión, lo resume y vuelve a inyectar lo relevante al empezar la siguie — alt: engram,agentmemory
- `cognee` [L|hyb|E|~] — Convierte documentos y conversaciones en un grafo de conocimiento consultable para dar memoria de largo plazo  — alt: graphiti,mem0,graphrag,letta
- `deepeval` [L|hyb|E|~] — Escribe pruebas para tus apps de LLM con métricas como fidelidad, relevancia o alucinación, e intégralas en tu — alt: ragas,promptfoo
- `engram` [R|loc|E|?] — Da a cualquier agente compatible con MCP una memoria local de decisiones y aprendizajes, sin dependencias pesa — alt: claude-mem,agentmemory
- `faiss` [L|loc|M|~] — Base de muchas bases vectoriales; ideal para investigación o cuando quieres índices en memoria sin servidor. — alt: qdrant,chroma
- `graphiti` [L|hyb|M|~] — Actualiza el grafo con cada nuevo dato sin recalcular todo y guarda cuándo era válido cada hecho. Ideal para m — alt: cognee,graphrag
- `graphrag` [L|hyb|M|~] — Resuelve las preguntas que requieren conectar entidades dispersas en muchos documentos, donde el RAG clásico f — alt: graphiti,cognee,lightrag
- `guardrails` [L|hyb|M|~] — Controla de qué puede hablar tu bot, bloquea jailbreaks y valida entradas y salidas con reglas en el lenguaje 
- `headroom` [L|hyb|E|~] — Resuelve el dolor habitual de los agentes: quedarse sin ventana de contexto a mitad de una tarea larga.
- `langfuse` [P|hyb|M|~] — Resuelve la opacidad: ves qué prompt, qué modelo, qué coste y qué salida tuvo cada paso de tu pipeline. — alt: phoenix,opik,mlflow
- `letta` [P|hyb|M|~] — Crea agentes que gestionan su propia memoria en bloques editables y archivos, y persisten entre conversaciones — alt: mem0,cognee
- `lightrag` [L|hyb|M|~] — Construye un grafo de entidades a partir de tus documentos y consulta en modo local, global o híbrido. Más bar — alt: graphrag,ragflow,pageindex
- `litellm` [L|hyb|E|~] — Resuelve el lock-in: cambias de proveedor o añades fallback sin reescribir el código de tu app.
- `loguru` [L|loc|E|~] — Resuelve la fricción del módulo `logging` stdlib, que exige boilerplate para algo tan básico como imprimir log
- `mem0` [L|hyb|E|~] — Resuelve el "amnesia" del LLM: el agente conserva preferencias y hechos entre sesiones sin reenviar todo el hi — alt: letta,cognee,supermemory
- `mempalace` [L|loc|E|~] — Resuelve la memoria privada: cero llamadas a API, tus textos no salen de tu máquina.
- `milvus` [R|loc|H|?] — Pensada para producción con grandes volúmenes, alta disponibilidad y varios tipos de índices. Tiene una versió — alt: qdrant,chroma
- `mlflow` [P|loc|E|~] — Registra experimentos, versiona modelos y, para LLM, ofrece trazas, evaluación y gestión de prompts. — alt: langfuse
- `opik` [P|loc|M|~] — Traza llamadas, ejecuta evaluaciones automáticas y monitorea producción con paneles. Incluye optimizador de pr — alt: langfuse,phoenix
- `pageindex` [L|cld|E|~] — Genera un árbol tipo índice del documento y deja que el LLM navegue por él como un experto. Funciona bien con  — alt: lightrag
- `pgvector` [L|loc|E|?] — Guarda embeddings en una columna y búscalos con SQL, con índices HNSW o IVFFlat. Evita añadir otra base de dat — alt: qdrant,chroma
- `phoenix` [P|loc|E|~] — Visualiza trazas de agentes y RAG, ejecuta evaluaciones y gestiona datasets y experimentos. Corre en local o e — alt: langfuse,opik
- `promptfoo` [A|loc|E|~] — Defines casos de prueba en YAML y comparas salidas de varios modelos con aserciones. También escanea vulnerabi — alt: deepeval,ragas,dspy
- `qdrant` [R|loc|E|~] — Guarda embeddings con metadatos y los busca con filtros rápidos, a escala. Muy usada como memoria de RAG y age — alt: milvus,chroma,pgvector,faiss
- `ragas` [L|hyb|E|~] — Mide fidelidad, relevancia del contexto y calidad de respuestas, y genera conjuntos de prueba a partir de tus  — alt: deepeval,promptfoo
- `ragflow` [P|loc|H|~] — Procesa PDFs, tablas e imágenes con parsing visual, crea bases de conocimiento con citas trazables y añade age — alt: dify,lightrag
- `sglang` [R|loc|H|~] — Compite con vLLM en velocidad, con caché de prefijos RadixAttention y buen soporte de salidas estructuradas. M — alt: vllm
- `supermemory` [P|hyb|E|~] — Guarda y recupera lo que importa de documentos, conversaciones y webs para dar contexto a tus modelos. Ofrece  — alt: mem0,agentmemory
- `turbovec` [L|loc|E|~] — Resuelve el coste de memoria y cómputo de la búsqueda vectorial cuando una vector DB completa es demasiado par
- `vllm` [R|loc|H|~] — Sirve modelos abiertos a muchos usuarios con una API compatible con OpenAI, gracias a PagedAttention y batchin — alt: sglang

### 7. Inteligencia de Código, Datos & Entrenamiento (34)
Detalle: `REPO_MENU_cats/07-inteligencia-de-c-digo-datos-entrenamiento.md`

- `ast-grep` [A|loc|E|?] — Busca y reemplaza código por su estructura (AST), no por texto. Útil para refactors masivos y reglas de lint p — alt: semgrep
- `awesome-bigdata` [D|cld|E|+] — Resuelve el "qué uso para X a escala": un panorama del stack de datos grandes en un solo vistazo.
- `cli` [A|cld|E|+] — No es un agente: es la herramienta que los agentes de código usan para abrir PRs, revisar issues o lanzar work
- `codebase-memory-mcp` [R|loc|E|?] — Indexa repos en milisegundos y da al agente herramientas MCP para entender arquitectura, dependencias y cambio — alt: codegraph,gitnexus
- `codegraph` [R|loc|E|~] — Resuelve el coste de contexto de los agentes en repos grandes. — alt: codebase-memory-mcp,serena
- `cosmos` [R|hyb|H|~] — Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.
- `data-science-ipython-notebooks` [D|loc|E|+] — Resuelve el "aprender DS con ejemplos reales" sin tener que montarlos tú desde cero.
- `deepseek-coder` [R|hyb|H|~] — Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia in
- `deepwiki-open` [A|hyb|M|~] — Analiza un repositorio y crea documentación navegable con diagramas y un chat para preguntar sobre el código. — alt: context7
- `defending-code-reference-harness` [S|cld|M|+] — Implementación de referencia para descubrir y corregir vulnerabilidades de forma autónoma con Claude, basada e
- `duckdb` [L|loc|E|?] — El "SQLite de la analítica": sin servidor, embebida en Python, R o Node, y capaz de procesar millones de filas — alt: polars
- `gitnexus` [A|hyb|E|~] — Resuelve el "llegar a un proyecto ajeno y no saber por dónde empezar": lo navegas y lo discutes en vez de leer — alt: repomix,codebase-memory-mcp,serena
- `graphify` [R|hyb|M|~] — Resuelve el onboarding visual: un índice textual no basta cuando hay relaciones entre archivos.
- `how-to-train-your-gpt` [D|loc|E|+] — Resuelve el "quiero entenderlo con explicación narrada" frente al código desnudo de nanoGPT.
- `llama-factory` [A|loc|M|~] — Soporta LoRA, QLoRA, ajuste completo, DPO y más desde una UI o CLI. Muy usado en investigación e industria. — alt: unsloth
- `llm-course` [D|loc|E|+] — Tres rutas: fundamentos, científico de LLM (entrenar y afinar) e ingeniero de LLM (apps y despliegue), con rec — alt: llms-from-scratch,generative-ai-for-beginners
- `llm.c` [L|loc|H|?] — Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framewo
- `llms-from-scratch` [D|loc|M|+] — Construyes atención, GPT, preentrenamiento y fine-tuning desde cero, entendiendo cada pieza. Ideal para aprend — alt: llm-course,nanogpt
- `marimo` [A|loc|E|~] — Al cambiar una celda se recalculan las dependientes, evitando estados ocultos. Incluye SQL, gráficos interacti
- `nanochat` [L|loc|M|~] — Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.
- `nanogpt` [L|loc|M|~] — Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción. — alt: llms-from-scratch
- `nemotron` [D|loc|H|+] — Reúne guías de entrenamiento, despliegue y casos de uso de los modelos Nemotron, pensados para IA agéntica efi
- `openai-python` [L|cld|E|~] — Resuelve el glue HTTP: no escribes peticiones a mano, usas clientes tipados con streaming.
- `peft` [L|loc|M|~] — Adapta modelos grandes entrenando solo una pequeña parte de los parámetros, ahorrando memoria y tiempo.
- `polars` [L|loc|E|~] — API expresiva con ejecución perezosa y paralela para procesar datos grandes en un solo equipo. — alt: duckdb
- `pytorch` [L|loc|M|~] — Base de la mayoría de investigación y modelos abiertos actuales.
- `repomix` [A|loc|E|~] — Genera un archivo XML, Markdown o texto con la estructura y el código del repo, respetando .gitignore y contan — alt: gitnexus
- `semgrep` [A|loc|E|~] — Encuentra bugs y vulnerabilidades con miles de reglas comunitarias o propias. Muy usado en CI de seguridad. — alt: ast-grep
- `swe-bench` [D|loc|H|+] — Da al modelo un repositorio y un issue y comprueba si su parche pasa las pruebas. Es la referencia para medir 
- `timesfm` [L|loc|M|~] — Predice ventas, demanda o tráfico a partir del histórico sin entrenar un modelo propio (zero-shot).
- `transformers` [L|loc|E|~] — Da acceso a cientos de miles de modelos con una API común para inferencia y entrenamiento. Es la base del ecos
- `tree-sitter` [L|loc|M|?] — Genera parsers rápidos que actualizan el árbol sintáctico mientras editas. Lo usan editores, Aider, ast-grep y
- `trl` [L|loc|M|~] — Ofrece entrenadores listos para ajuste supervisado y por preferencias, usados para alinear modelos.
- `unsloth` [A|loc|M|~] — Afina modelos como Qwen, Llama o Gemma en una sola GPU y expórtalos a GGUF u Ollama. Ofrece notebooks gratuito — alt: llama-factory

### 8. IA Local: Modelos, Chats & Workspaces (21)
Detalle: `REPO_MENU_cats/08-ia-local-modelos-chats-workspaces.md`

- `anything-llm` [A|loc|E|~] — Organiza documentos en espacios de trabajo, crea RAG sin configurar nada y añade agentes con herramientas. Esc — alt: open-webui,khoj,private-gpt
- `cherry-studio` [A|hyb|E|~] — Chatea con decenas de proveedores y modelos locales, usa asistentes predefinidos, MCP y base de conocimiento d — alt: jan,lobehub
- `exo` [R|loc|M|~] — Une Macs, PCs o teléfonos en un clúster que comparte la carga de un modelo que no cabría en uno solo.
- `hermes-desktop` [A|loc|E|~] — Para quien quiere usar Hermes Agent como aplicación y no solo desde la terminal.
- `jan` [A|loc|E|~] — Descarga modelos y chatea en local con privacidad total, o conecta APIs en la nube si quieres. Incluye servido — alt: cherry-studio,textgen
- `khoj` [A|hyb|M|~] — Busca en tus documentos y en internet, crea agentes personalizados, programa resúmenes y hace investigación pr — alt: anything-llm,surfsense
- `librechat` [A|hyb|M|~] — Une OpenAI, Anthropic, Google, Azure, OpenRouter y modelos locales con agentes, artifacts, búsqueda y control  — alt: open-webui,lobehub
- `llama-cpp` [R|loc|M|?] — Base de Ollama, LM Studio y muchas apps. Incluye un servidor compatible con OpenAI y herramientas para cuantiz — alt: ollama,llamafile,localai
- `llamafile` [R|loc|E|?] — Empaqueta modelo y motor en un ejecutable que funciona en Windows, macOS y Linux sin instalar nada. Proyecto d — alt: ollama,llama-cpp
- `llmfit` [L|hyb|E|~] — Resuelve la elección subjetiva de modelo: la conviertes en un flujo objetivo y reproducible con métricas.
- `lobehub` [A|hyb|E|~] — Antes LobeChat: chat elegante con agentes, plugins, base de conocimiento y despliegue en un clic. Ahora añade  — alt: open-webui,librechat,cherry-studio
- `localai` [R|loc|M|~] — Sustituye la API de OpenAI por una propia que corre modelos abiertos de muchos tipos. Útil para apps que ya ha — alt: ollama,llama-cpp
- `notebooklm-mcp-cli` [R|cld|E|+] — Convierte NotebookLM en una herramienta invocable por asistentes.
- `notebooklm-py` [L|cld|E|~] — Cubre el vacío de automatización que la interfaz web oficial no ofrece.
- `odysseus` [P|loc|H|~] — Sustituye la dispersión entre varios SaaS por un único panel que tú controlas.
- `ollama` [R|loc|E|?] — Un comando para bajar y ejecutar modelos como Qwen, Gemma, DeepSeek o gpt-oss. Casi todas las apps de IA local — alt: llama-cpp,localai,llamafile
- `open-notebook` [A|loc|M|~] — Resuelve el envío de documentos sensibles a la nube que implica el NotebookLM oficial. — alt: deeptutor,surfsense
- `open-webui` [A|loc|E|~] — Da a tu equipo un chat privado con usuarios, documentos, búsqueda web, herramientas y modelos locales o en la  — alt: librechat,lobehub,anything-llm,textgen
- `private-gpt` [P|loc|M|~] — Ofrece una API lista para construir apps de IA sin que los datos salgan de tu entorno. Funciona con cualquier  — alt: anything-llm
- `surfsense` [A|hyb|M|~] — Conecta tus fuentes (archivos, Slack, Notion, GitHub, web) y conversa con ellas con citas, genera podcasts y r — alt: open-notebook,khoj
- `textgen` [A|loc|M|~] — La clásica "oobabooga": carga modelos en muchos formatos y backends, con chat, modo notebook y entrenamiento L — alt: jan,open-webui

### 9. Diseño, UI & Frontend (34)
Detalle: `REPO_MENU_cats/09-dise-o-ui-frontend.md`

- `animejs` [L|loc|E|~] — API simple y potente para líneas de tiempo, scroll y animaciones complejas. — alt: gsap,motion
- `ant-design` [L|loc|E|~] — Componentes muy completos para apps de negocio: tablas, formularios, fechas y layouts de backoffice. — alt: mui,ui
- `assistant-ui` [L|loc|E|~] — Componentes componibles de chat con streaming, adjuntos, markdown y herramientas, compatibles con AI SDK y Lan — alt: copilotkit
- `copilotkit` [L|hyb|E|~] — Añade copilotos, chat y agentes que actúan sobre tu app, con estado compartido entre agente y UI. Se integra c — alt: assistant-ui
- `daisyui` [L|loc|E|~] — Añade clases como `btn` o `card` sobre Tailwind para escribir menos HTML, sin JavaScript. — alt: ui
- `design.md` [S|cld|E|+] — Resuelve la inconsistencia de marca cuando varias personas o agentes tocan la UI.
- `excalidraw` [A|loc|E|~] — Dibuja diagramas rápidos que parecen bocetos, colabora en tiempo real y embébela en tus apps como componente R — alt: tldraw,mermaid
- `gsap` [L|loc|M|~] — Es la herramienta de referencia del motion web profesional. — alt: animejs
- `heroui` [L|loc|E|~] — Resuelve la accesibilidad seria sin renunciar a un estilado moderno. — alt: mui
- `impeccable` [S|cld|E|+] — Ataca el patrón repetitivo de interfaces que "huelen" a IA.
- `lucide` [L|loc|E|~] — Iconos limpios y uniformes, usados por shadcn/ui y muchas apps.
- `magicui` [L|loc|E|~] — Apunta al impacto visual más que a la accesibilidad estricta. — alt: react-bits
- `motion` [L|loc|E|~] — Hizo accesible la animación en el ecosistema React. — alt: animejs
- `mui` [L|loc|E|~] — Cientos de componentes accesibles y personalizables para apps React, con temas y sistema de estilos propio. — alt: ant-design,ui,heroui
- `normalize.css` [L|loc|E|?] — Resuelve las inconsistencias de margen, tipografía y formularios entre Chrome, Firefox y Safari.
- `onlook` [A|loc|E|~] — Edita tu app en un lienzo visual o pide cambios a la IA, y Onlook escribe el código en tu proyecto. — alt: open-design
- `open-design` [A|hyb|M|~] — Resuelve el ir y venir entre prompt, preview y código exportable. — alt: onlook
- `openui` [L|hyb|E|~] — Permite que el modelo devuelva componentes interactivos (tablas, formularios, gráficos) que tu app renderiza.
- `penpot` [A|loc|H|~] — Es la alternativa abierta a Figma más conocida.
- `plasmic` [A|hyb|M|~] — Cubre el hueco entre no-code y desarrollo a medida.
- `radix-primitives` [L|loc|E|~] — Resuelven accesibilidad, foco y teclado en diálogos, menús o tooltips, dejándote el estilo. Son la base de sha
- `react-bits` [L|loc|E|~] — Fondos, textos animados y efectos listos para copiar en proyectos React y Next.js. — alt: magicui
- `react-three-fiber` [L|loc|M|~] — Lleva la mentalidad componible de React al 3D sin abandonar three.js por debajo.
- `screenshot-to-code` [A|cld|E|+] — Sube una imagen o graba un video de una web y obtén código funcional que puedes iterar. — alt: stitch-sdk
- `skills-emil` [S|cld|E|+] — Resuelve el handoff diseño↔código, no solo la estética final.
- `stitch-sdk` [L|cld|E|~] — Automatiza Stitch, el generador de interfaces de Google, para integrarlo en tus flujos y agentes. — alt: screenshot-to-code
- `stitch-skills` [S|cld|E|+] — Skills en el estándar abierto Agent Skills que enseñan a Claude Code, Codex o Gemini CLI a diseñar con Stitch.
- `swr` [L|loc|E|~] — Cubre el caso de consumir APIs en frontend sin manejar caché a mano.
- `tailwindcss` [L|loc|E|~] — Elimina el contexto de estilos disperso entre hojas y componentes.
- `taste-skill` [S|cld|E|+] — Ataca el acabado "de plantilla" que delata a las UIs generadas por IA.
- `three.js` [L|loc|M|~] — Abstrae la complejidad de WebGL en escenas, cámaras, luces y mallas.
- `tldraw` [L|loc|E|~] — Base de muchas herramientas de pizarra y de UI generativa con IA. Ofrece colaboración y personalización comple — alt: excalidraw
- `ui` [L|loc|E|~] — El código fuente pasa a ser tuyo y lo editas a voluntad. — alt: mui,ant-design,daisyui
- `ui-ux-pro-max-skill` [S|cld|E|+] — Resuelve el punto débil habitual del código asistido por IA: la jerarquía visual y el acabado.

### 10. Analítica & Visualización (20)
Detalle: `REPO_MENU_cats/10-anal-tica-visualizaci-n.md`

- `awesome-dataviz` [D|cld|E|+] — Punto de partida para descubrir opciones de dataviz sin búsquedas dispersas.
- `chart-js` [L|loc|E|~] — Ocho tipos de gráfico listos, responsivos y animados con muy poco código. Ideal para dashboards web simples. — alt: echarts,recharts
- `d3` [L|loc|M|~] — Da control total sobre cada elemento visual. Base de muchas librerías de gráficos y del periodismo de datos. — alt: echarts
- `daily-stock-analysis` [A|cld|M|+] — Combina datos de mercado, noticias en tiempo real y análisis con LLM para generar reportes automáticos por Tel
- `dash` [L|loc|M|~] — Cubre el caso de dashboards productivos en Python sin salir del lenguaje.
- `echarts` [L|loc|M|~] — Cubre casi cualquier tipo de chart en el navegador. — alt: d3,chart-js,recharts
- `gradio` [L|loc|E|~] — Envuelve una función Python en una interfaz web con entradas y salidas de texto, imagen, audio o chat. Base de — alt: streamlit
- `grafana` [P|loc|E|~] — Crea dashboards y alertas sobre Prometheus, Loki, bases SQL y decenas de fuentes. Estándar en monitoreo.
- `matomo` [P|loc|M|?] — Analítica web completa con embudos, mapas de calor y comercio electrónico, auto-hospedada. — alt: umami,plausible
- `metabase` [P|hyb|M|?] — Apunta a perfiles no técnicos que necesitan reporting propio. — alt: superset,redash
- `pandas-ai` [L|hyb|E|~] — Haces preguntas en lenguaje natural y genera el código de análisis o gráficos. Útil para analistas y apps de d — alt: wrenai
- `plausible` [P|hyb|M|?] — Un panel de una sola página con lo esencial: visitas, fuentes, páginas y objetivos. — alt: umami,matomo
- `posthog` [P|hyb|H|~] — Cubre todo el ciclo de medición de producto sin integrar varias herramientas.
- `recharts` [L|loc|E|~] — Construye gráficos con componentes de React. Muy usada en dashboards de apps React y en shadcn/ui. — alt: chart-js,echarts
- `redash` [P|loc|M|~] — Pensada para analistas que escriben SQL y quieren compartir resultados rápido con el equipo. — alt: metabase,superset
- `streamlit` [L|loc|E|~] — Convierte un script de datos en una app web interactiva casi al instante. — alt: gradio
- `superset` [P|loc|M|~] — Conecta tus bases SQL, crea gráficos y dashboards sin código o con SQL Lab, con control de acceso. — alt: metabase,redash
- `umami` [P|loc|E|~] — Mide visitas, campañas, eventos, conversiones e ingresos en un panel simple, cumpliendo GDPR. — alt: plausible,matomo
- `uplot` [L|loc|E|~] — Apuesta por hacer una sola cosa (líneas/áreas temporales) mejor que ninguna.
- `wrenai` [P|hyb|M|~] — Define tu modelo de datos una vez y los usuarios (o agentes) preguntan en lenguaje natural para obtener SQL, g — alt: pandas-ai

### 11. Generación de Imagen & Visión (27)
Detalle: `REPO_MENU_cats/11-generaci-n-de-imagen-visi-n.md`

- `codeformer` [L|loc|M|~] — Recupera detalles de caras en fotos de baja calidad con buena fidelidad. — alt: gfpgan
- `comfyui` [R|loc|H|~] — Resuelve la composición de flujos de difusión complejos que una UI fija no permite. — alt: wan2gp,sd-webui-forge
- `comfyui-ipadapter-plus` [R|loc|H|~] — Funciona como un "LoRA de una sola imagen": le das un referente y la salida hereda su look.
- `controlnet` [R|loc|H|~] — Resuelve el problema de que el texto por sí solo no controla la composición de la imagen.
- `deep-live-cam` [R|loc|H|~] — Convierte un cambio de rostro, que normalmente requiere pipeline complejo, en un flujo de "un clic". — alt: facefusion
- `diffusers` [L|loc|H|~] — Es la capa de abstracción que unifica el zoo de modelos de difusión bajo una misma interfaz Python.
- `face-recognition` [L|loc|M|~] — Envuelve dlib para que el reconocimiento facial sea trivial desde un script. — alt: insightface
- `facefusion` [A|loc|M|~] — Herramienta líder para face swap, mejora facial y sincronía labial, con controles de uso responsable. — alt: deep-live-cam
- `flux` [R|loc|H|~] — Modelos de texto a imagen de alta calidad, con variantes para edición, relleno y control. — alt: stable-diffusion-webui
- `fooocus` [A|loc|M|~] — Es la opción más sencilla para empezar con difusión local.
- `gfpgan` [R|loc|M|~] — Resuelve el problema concreto de las caras "fundidas" que aparecen al reescalar o comprimir fotos. — alt: codeformer
- `insightface` [L|loc|M|~] — Base de muchas herramientas faciales; ofrece modelos de reconocimiento de última generación. — alt: face-recognition
- `invokeai` [A|loc|H|~] — Resuelve la fragmentación de herramientas SD reuniendo generación, edición y control en una sola app self-host — alt: krita-ai-diffusion
- `krita-ai-diffusion` [A|loc|M|~] — Pinta, selecciona y genera dentro de tu editor de imágenes favorito; usa ComfyUI por debajo. — alt: invokeai
- `label-studio` [P|loc|E|~] — Crea datasets para entrenar o evaluar modelos con interfaces de anotación configurables y preetiquetado con IA
- `liveportrait` [R|loc|H|~] — Convierte una foto en un avatar que sigue las expresiones de un "conductor".
- `open-generative-ai` [P|hyb|M|~] — Centraliza la generación visual sin filtros restrictivos ni suscripción.
- `opencv` [L|loc|E|~] — Procesamiento de imagen y video, detección, calibración de cámaras y más, en C++ y Python.
- `real-esrgan` [R|loc|M|~] — A diferencia de los upscalers bicúbicos, infiere detalle plausible al ampliar.
- `rembg` [L|loc|E|~] — Elimina fondos de fotos de producto o retratos con modelos como U2Net o BiRefNet.
- `sam2` [L|loc|M|~] — Marca un objeto en un fotograma y SAM 2 lo sigue en todo el video. Más rápido que SAM en imágenes. — alt: segment-anything
- `sd-webui-controlnet` [R|loc|H|~] — Lleva el control composicional al flujo de trabajo habitual de la WebUI sin tocar código.
- `sd-webui-forge` [A|loc|M|~] — Mantiene la interfaz de AUTOMATIC1111 con mejoras de rendimiento y soporte de modelos nuevos como FLUX. — alt: stable-diffusion-webui,comfyui
- `segment-anything` [L|loc|M|~] — Genera máscaras precisas sin entrenamiento para el objeto que indiques. Su sucesor SAM 2 añade video. — alt: sam2
- `stable-diffusion-webui` [A|loc|H|~] — Es la UI que popularizó la difusión local. — alt: sd-webui-forge,flux
- `supervision` [L|loc|E|~] — Se conecta a cualquier detector y te da utilidades para dibujar, contar en zonas, seguir objetos y evaluar.
- `ultralytics` [L|loc|E|~] — Entrena un detector con tus datos en pocas líneas y expórtalo a ONNX, TensorRT o móvil.

### 12. Audio, Voz & Video (42)
Detalle: `REPO_MENU_cats/12-audio-voz-video.md`

- `audiocraft` [L|loc|M|~] — AudioCraft reúne el código de inferencia y entrenamiento de los modelos de audio generativo de Meta: MusicGen 
- `chatterbox` [L|loc|E|~] — Clona una voz con unos segundos de audio y ajusta la expresividad. Multilingüe y con marca de agua. — alt: fish-speech,gpt-sovits,kokoro,luxtts
- `cosyvoice` [L|loc|M|~] — Síntesis de voz natural con clonación y control de estilo, también en streaming. — alt: fish-speech,index-tts
- `davinci-resolve-mcp` [R|loc|M|~] — Expone la API oficial de scripting de DaVinci Resolve como herramientas MCP para Claude, Cursor, Codex y otros
- `faster-whisper` [R|loc|M|~] — Es el mismo modelo de OpenAI, pero con un runtime de inferencia optimizado. — alt: whisper-cpp
- `ffmpeg` [A|loc|E|?] — FFmpeg es la base multimedia sobre la que se apoyan casi todos los editores, reproductores y pipelines de vide
- `fish-speech` [L|loc|M|~] — Clona voces con pocos segundos de audio y genera habla natural en muchos idiomas. — alt: chatterbox,cosyvoice,gpt-sovits
- `gpt-sovits` [A|loc|M|~] — Entrena una voz con muy pocos datos y sintetiza en varios idiomas. Muy popular entre creadores. — alt: chatterbox,fish-speech
- `hunyuanvideo` [R|loc|H|~] — HunyuanVideo publica los pesos, la definición en PyTorch y el código de inferencia de un modelo de texto a vid — alt: wan2-2,ltx-video
- `hyperframes` [R|loc|E|~] — HyperFrames define cada video como un archivo HTML con atributos de tiempo y pistas, animado con GSAP, CSS, Lo — alt: remotion,moviepy
- `index-tts` [L|loc|M|~] — Clona voces sin entrenar y permite controlar la duración exacta, útil para doblaje. — alt: cosyvoice
- `kokoro` [L|loc|E|~] — Voces naturales en varios idiomas, incluido el español, rápido incluso en CPU. — alt: chatterbox,tts,luxtts
- `livekit-agents` [R|hyb|M|~] — Construye agentes que hablan, escuchan y ven, con detección de turnos y telefonía, desplegables a escala. — alt: pipecat
- `lossless-cut` [A|loc|E|~] — LosslessCut es una interfaz gráfica sobre FFmpeg para recortar y fusionar archivos de video y audio sin recomp
- `ltx-video` [R|loc|H|~] — LTX-Video es el repositorio de los modelos v0.9.x de Lightricks, un transformer de difusión (DiT) para texto a — alt: wan2-2,hunyuanvideo
- `luxtts` [L|loc|E|~] — Basado en ZipVoice, pensado para clonación rápida y realista con pocos recursos. — alt: kokoro,chatterbox
- `manim` [L|loc|M|~] — Manim permite describir en código Python escenas con fórmulas LaTeX, gráficas, geometría y transformaciones an
- `moneyprinterturbo` [A|hyb|M|~] — MoneyPrinterTurbo automatiza la producción de shorts: das un tema o palabras clave y escribe el guion con un L — alt: openmontage,videofy-minimal
- `moviepy` [L|loc|E|~] — MoviePy convierte la edición de video en código Python: abres clips, los recortas, superpones texto o imágenes — alt: remotion,hyperframes
- `nemo` [L|loc|H|~] — Incluye modelos de ASR como Parakeet y Canary, que lideran rankings de transcripción, y herramientas para afin — alt: whisperx
- `obs-studio` [A|loc|E|?] — OBS Studio captura, compone, codifica, graba y transmite video en Windows, macOS y Linux. Combinas en escenas  — alt: openscreen
- `omnivoice-studio` [A|loc|M|~] — Reúne STT, TTS y dubbing en una sola app sin claves de API. — alt: videolingo
- `opencut` [A|hyb|M|~] — OpenCut es un editor de video pensado como alternativa abierta a CapCut: privado (los videos no salen de tu di
- `openmontage` [S|loc|M|+] — Describes el video y el agente investiga, escribe el guion, genera recursos y monta el resultado. — alt: remotion-superpowers,moneyprinterturbo
- `openscreen` [A|loc|E|~] — OpenScreen graba una ventana o la pantalla completa con micrófono y audio del sistema, y después te deja pulir — alt: obs-studio
- `pipecat` [R|hyb|M|~] — Encadena STT, LLM y TTS con interrupciones y baja latencia, y conecta con teléfono, WebRTC o WhatsApp. — alt: livekit-agents
- `remotion` [L|loc|M|~] — Convierte el video en un artefacto versionable y parametrizable desde tu código frontend. — alt: moviepy,hyperframes
- `remotion-superpowers` [S|loc|E|+] — Añade locución con IA, música, footage de stock e imágenes para producir videos en código. — alt: openmontage,video-use
- `rvc` [A|loc|M|~] — Cambia la voz de una grabación manteniendo entonación. Muy usado para covers y doblaje.
- `skills-remotion` [S|loc|E|+] — Enseñan al agente las buenas prácticas de Remotion: composiciones, animaciones, audio y render.
- `supertonic` [R|loc|M|~] — Apunta a latencia mínima con privacidad total, sin nube ni llamadas de API.
- `tts` [L|loc|M|~] — Reúne en una sola librería modelos como Tacotron, VITS y XTTS, con CLI y API Python. — alt: kokoro
- `vibevoice` [L|loc|H|~] — Genera conversaciones de hasta 90 minutos con cuatro voces distintas, y tiene variantes de baja latencia.
- `video-use` [S|loc|E|+] — El agente corta, une, subtitula y ajusta videos a partir de instrucciones en lenguaje natural. — alt: remotion-superpowers
- `videofy-minimal` [A|loc|E|~] — Encadena TTS/STT y montaje en un solo flujo para pasar de texto a reel con lo mínimo. — alt: moneyprinterturbo
- `videolingo` [A|hyb|M|~] — VideoLingo reúne en una interfaz Streamlit el trabajo de un equipo de subtitulado: descarga el video con yt-dl — alt: omnivoice-studio
- `voxcpm` [R|loc|H|~] — Pertenece a la familia CPM de modelos generativos de OpenBMB.
- `wan2-2` [R|loc|H|~] — Wan2.2 publica pesos y código de inferencia de varios modelos de video: texto a video e imagen a video de 14B  — alt: hunyuanvideo,ltx-video
- `wan2gp` [A|loc|H|~] — WanGP, antes Wan2GP, es una interfaz web para ejecutar en tu GPU decenas de modelos generativos abiertos: vide — alt: comfyui
- `whisper` [R|loc|M|~] — Cubre también identificación de idioma y traducción al inglés en la misma red. — alt: whisper-cpp
- `whisper-cpp` [R|loc|E|?] — Transcribe voz a texto en local sin Python ni GPU obligatoria, incluso en tiempo real. Base de muchas apps de  — alt: faster-whisper,whisper
- `whisperx` [R|loc|M|~] — Convierte la salida "por segmento" de Whisper en timings palabra a palabra con etiqueta de speaker. — alt: nemo

### 13. Documentos & Presentaciones (23)
Detalle: `REPO_MENU_cats/13-documentos-presentaciones.md`

- `docling` [L|loc|E|~] — Entiende la estructura del documento (tablas, layout, fórmulas, orden de lectura) y la exporta para RAG y agen — alt: marker,mineru,unstructured,olmocr
- `marker` [L|loc|E|~] — Pensado para libros y papers, con opción de mejorar el resultado usando un LLM. — alt: docling,mineru
- `markitdown` [L|loc|E|~] — Es la puerta de entrada habitual para ingesta de documentos en pipelines RAG.
- `marp` [A|loc|E|~] — Escribes Markdown con separadores y obtienes slides limpias; tiene extensión de VS Code. — alt: slidev,reveal.js
- `mermaid` [L|loc|E|~] — GitHub, Notion y muchos editores lo renderizan de forma nativa; los LLM lo escriben muy bien. — alt: excalidraw
- `mineru` [A|loc|M|~] — Muy bueno con papers científicos, tablas y fórmulas; ofrece CLI, API y app de escritorio. — alt: docling,marker
- `ocrmypdf` [A|loc|E|~] — Convierte escaneos en PDF/A buscables manteniendo la imagen original.
- `olmocr` [A|loc|H|~] — Pensado para crear datasets de entrenamiento a partir de millones de PDFs, con orden de lectura correcto. — alt: paddleocr,docling,unlimited-ocr
- `paddleocr` [L|loc|M|~] — Reconoce texto en más de 80 idiomas y analiza documentos con tablas y layout. Incluye modelos pequeños para di — alt: tesseract,olmocr,unlimited-ocr
- `pandoc` [A|loc|E|?] — La navaja suiza de la conversión de textos: genera Word o PDF desde Markdown y al revés.
- `pdf-inspector` [L|loc|E|?] — Detecta si un PDF necesita OCR para enrutarlo al proceso correcto, y extrae texto rápido cuando no hace falta.
- `pdfcraft` [A|loc|E|?] — Apunta a ser la alternativa local y sin nube a los servicios online de PDF. — alt: stirling-pdf
- `pdfding` [A|loc|E|~] — Organiza y lee tus PDFs desde cualquier dispositivo. El desarrollo se trasladó a Codeberg.
- `pdfmathtranslate` [A|hyb|E|~] — Ideal para leer artículos científicos en tu idioma sin perder el layout. Admite Google, DeepL, OpenAI, Ollama 
- `ppt-master` [R|hyb|E|~] — Sustituye el maquetado manual de slides por un borrador estructurado por un LLM. — alt: presenton
- `presenton` [A|hyb|E|~] — Crea presentaciones editables a partir de un prompt o documento, con tus plantillas, y exporta a PPTX o PDF. — alt: ppt-master
- `reveal.js` [L|loc|E|~] — Convierte las diapositivas en una página web versionable y reproducible por código. — alt: slidev,marp
- `slidev` [A|loc|E|~] — Escribe tus slides en Markdown y obtén resaltado de código, diagramas, animaciones y exportación a PDF. Los ag — alt: marp,reveal.js
- `stirling-pdf` [A|loc|E|~] — Más de 50 herramientas de PDF en el navegador sin enviar archivos a terceros. — alt: pdfcraft
- `tesseract` [A|loc|E|?] — Base de muchas herramientas de OCR, ligero y sin GPU. — alt: paddleocr
- `unlimited-ocr` [L|loc|H|~] — Extrae texto y estructura de documentos de muchas páginas sin dividirlos, pensado para contexto largo. — alt: olmocr,paddleocr
- `unstructured` [L|hyb|M|~] — Particiona más de 25 tipos de archivo en elementos (títulos, tablas, texto) y los prepara para bases vectorial — alt: docling
- `youtube2webpage` [L|loc|E|?] — Convierte una charla en un artículo navegable con contexto visual.

---

## Cómo instalar (resumen de la lógica de derivación)

- `role=skill/directory` → copiar a la carpeta de skills de tu agente.
- `role=platform/runtime/app` + Docker → `git clone && docker compose up`.
- `role=library` Python → `pip install <pkg>` / `uv add <pkg>` (verifica nombre).
- `role=library` Node → `npm install <pkg>` (verifica nombre).
- `exec=cloud` → servicio gestionado: API key, no se clona.
- Marca `?` → solo `git clone` es seguro; revisa el README del repo.

> Si un comando marcado `~` falla, busca el nombre real del paquete en
> pypi.org / npmjs.com o clona el repo y lee su manifest.
