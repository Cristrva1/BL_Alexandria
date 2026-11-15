# REPO_MENU — Menú portable de la biblioteca de repositorios

> Generado: 2026-11-15 · 501 repos curados · Documento 100% para IA.
> COPIA esta carpeta (`menu_portable/`) a la raíz de tu proyecto y
> referencia este archivo desde tu AGENTS.md / system prompt.

---

## INSTRUCCIONES PARA EL AGENTE (léeme entero, soy corto)

Eres un agente que debe elegir qué repositorios instalar/usar para un
proyecto concreto. Tienes un menú curado de **501 repos** de IA y
automatización. Objeto: gastar MÍNIMOS tokens y NO visitar la web.

PROTOCOLO (en orden):

0. **Si el usuario ya describió un proyecto concreto**, parte de las
   `recipes` que coincidan con el producto; no empieces por repos sueltos.
1. **No leas todo.** Este archivo basta para preseleccionar.
2. **Filtra** candidatos por `cat`, `tags`, `role`, `exec`, `setup`, `prov`
   y palabras de `one` (resumen de una línea).
3. **Desempata** con `alt`: si ya elegiste un repo, **descarta sus `alt`**
   (cumplen la misma función, no necesitas dos).
4. **Combina** con `recipes` si el proyecto es un flujo end-to-end.
5. **Considera la herramienta** del usuario (Claude Code, Antigravity,
   Codex, Grok, Deepseek) con la tabla de abajo y el campo opcional
   `agent_tools`. Solo importa para repos `role=skill/directory`.
6. **Solo para finalistas (<8):** abre `REPO_MENU_cats/NN-*.md` para
   desc, `choose_if`, `avoid_if`, `combines_with` y el comando de
   instalación derivado.
7. **Instalación:** comando marcado `+` seguro · `~` verificar nombre ·
   `?` solo clone + README.

REGLA CLAVE — herramienta de código ≠ modelo en ejecución:
- El AGENTE/IDE con que CONSTRUYES (Claude Code, Antigravity, Codex…)
  solo importa para repos `role=skill/directory` (catálogos de skills).
- El LLM que tu APP llama EN EJECUCIÓN es el campo `prov`; se configura
  por env vars. La mayoría de repos runtime son AGNÓSTICOS al agente.

LEYENDA de columnas del índice:
`role`: P=plataforma R=runtime L=librería S=skill D=catálogo A=app
`exec`: loc=local cld=cloud hyb=híbrido · `setup`: E=easy M=medium H=heavy
`inst`: +=comando seguro ~=verificar ?=solo clone
`tags` / `prov` / `tools` (`agent_tools`): solo si el repo los declara
`alt`: repos sustitutos (elige uno)

---

## Repos específicos por herramienta de código

| Herramienta | Repos que le sirven |
|---|---|
| Claude Code | `claude-code`, `anthropic-skills`, `claude-plugins-official`, `superpowers`, `awesome-claude-code`, `awesome-claude-skills`, `claude-mem`, `n8n-skills`, `geo-seo-claude`, `agency-agents` |
| Codex | `codex`, `agent-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`, `spec-kit`, `marketingskills`, `taste-skill` |
| Antigravity | `antigravity-awesome-skills`, `awesome-agent-skills`, `prompt-master`, `stitch-skills` |
| gemini-cli | `gemini-cli`, `awesome-agent-skills`, `antigravity-awesome-skills`, `stitch-skills` |
| opencode | `opencode`, `awesome-agent-skills`, `antigravity-awesome-skills`, `prompt-master` |
| Grok | Sin repos específicos: úsalo como proveedor LLM en runtime (los repos agnósticos lo aceptan vía API compatible con OpenAI). |
| Deepseek | `deepseek-coder` |

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

Formato: `id` [role|exec|setup|inst] — one — tags:… — prov:… — tools:… — alt:…

### Sin categoría

- `guia` [D|loc|E|+] — Guía editorial original de la biblioteca, hoy integrada en las fichas de cada repo. — tags: learning
- `tools` [D|loc|E|+] — Carpeta interna de herramientas auxiliares del hub; no es un producto para instalar. — tags: skills

### 1. Automatización, Mensajería & CRM (36)
Detalle: `REPO_MENU_cats/01-automatizaci-n-mensajer-a-crm.md`

- `activepieces` [P|hyb|M|~] — Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flu — tags: automation,typescript,docker — alt: n8n
- `appsmith` [P|loc|M|~] — Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. — tags: ui,automation,typescript,docker — alt: tooljet,budibase,nocodb
- `awesome-n8n-templates` [D|loc|E|+] — Colección de más de 280 plantillas gratuitas de n8n listas para importar, con IA y apps populares. — tags: automation,prompts
- `baileys` [L|loc|E|~] — Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. — tags: whatsapp,chatbot,typescript — alt: whatsapp-web-js,waha
- `botpress` [P|hyb|M|~] — Plataforma para construir y desplegar agentes conversacionales con LLM en web, WhatsApp y más. — tags: chatbot,agents,typescript — alt: typebot,rasa
- `budibase` [P|loc|M|~] — Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. — tags: automation,agents,docker — alt: appsmith,tooljet,nocodb
- `cal.diy` [P|hyb|H|~] — Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia. — tags: motores,next-auth,nextjs,open-source,postgresql,prisma,t3-stack,tailwindcss
- `chatwoot` [P|loc|H|~] — Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, e — tags: automation,crm,ruby,docker
- `compai-crm` [P|cld|H|+] — CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia. — tags: crm,typescript
- `erpnext` [P|loc|H|~] — ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura. — tags: crm,python — alt: odoo
- `evolution-api` [P|loc|H|~] — API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. — tags: automation,whatsapp,typescript,docker — alt: whatsapp-web-js,waha
- `fluxer` [P|hyb|M|?] — Plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop; — tags: whatsapp,chatbot,typescript
- `huginn` [P|loc|M|?] — Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como u — tags: automation,ruby,docker — alt: n8n,node-red
- `kestra` [P|loc|M|~] — Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. — tags: automation,data,java,docker — alt: windmill,trigger-dev
- `listmonk` [P|loc|M|?] — Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depe — tags: automation,email,go,docker
- `mautic` [P|loc|H|?] — Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites com — tags: automation,email,php
- `n8n` [P|loc|M|~] — Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un — tags: automation,typescript,docker — alt: activepieces,huginn,windmill,node-red
- `n8n-io` [P|loc|M|~] — Copia local del repositorio oficial de n8n (mismo proyecto que n8n), mantenida como referencia o espejo del có — tags: automation,typescript,docker
- `n8n-mcp` [R|hyb|M|~] — Servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n (816 core + 1 — tags: automation,mcp,typescript
- `n8n-skills` [S|cld|E|+] — Conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando  — tags: skills,automation
- `nocodb` [P|loc|E|~] — Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. — tags: data,automation,docker — alt: appsmith,budibase
- `node-red` [P|loc|E|~] — Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. — tags: automation,javascript,docker — alt: n8n,huginn
- `novu` [P|hyb|M|~] — Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y ch — tags: automation,email,typescript
- `odoo` [P|loc|H|~] — Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. — tags: crm,python,postgres — alt: erpnext
- `openwa` [L|loc|E|~] — Gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraes — tags: whatsapp,chatbot,typescript
- `rasa` [R|loc|H|~] — Framework Python para asistentes conversacionales con NLU y gestión de diálogo, desplegables en local. — tags: chatbot,agents,python — alt: botpress
- `self-hosted-ai-starter-kit` [P|loc|M|~] — Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos. — tags: automation,local,rag,docker
- `tooljet` [P|loc|M|~] — Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. — tags: ui,automation,docker — alt: appsmith,budibase
- `trigger-dev` [P|hyb|M|~] — Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. — tags: automation,agents,typescript — alt: windmill,kestra
- `twenty-main` [P|hyb|H|~] — CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modela — tags: automation,crm,typescript,docker
- `typebot` [P|loc|M|~] — Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. — tags: chatbot,automation,typescript — alt: botpress
- `waha` [P|loc|E|~] — API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. — tags: whatsapp,automation,docker — alt: evolution-api,whatsapp-web-js,baileys
- `whatsapp-agentkit` [S|hyb|E|+] — Plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de pr — tags: agents,automation,python
- `whatsapp-web-js` [L|loc|E|~] — Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. — tags: whatsapp,chatbot,javascript — alt: baileys,waha,evolution-api
- `whatsmeow` [L|hyb|M|?] — Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web. — tags: whatsapp,go,golang,whatsapp-web
- `windmill` [P|loc|M|~] — Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. — tags: automation,agents,rust,docker — alt: n8n,kestra,trigger-dev

### 2. Skills, Prompts & Guías de Agente (54)
Detalle: `REPO_MENU_cats/02-skills-prompts-gu-as-de-agente.md`

- `12-factor-agents` [D|hyb|E|+] — Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12  — tags: agents,learning,prompts,typescript
- `500-ai-agents-projects` [D|hyb|E|+] — Colección de ideas, casos de uso y ejemplos de agentes de IA para distintos sectores y tareas. — tags: guias,ai-agents,genai,python
- `agency-agents` [S|hyb|E|+] — Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Co — tags: agents,prompts,skills,coding-agent — alt: wshobson-agents
- `agent-skills` [S|loc|E|+] — Colección de skills de ingeniería de producción para agentes de código, de Addy Osmani. — tags: skills,coding-agent — alt: superpowers
- `agent-toolkit` [S|cld|E|+] — Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documen — tags: agents,skills,python
- `agents-towards-production` [D|cld|M|+] — Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad,  — tags: agents,learning,notebooks,python — prov: openai,local
- `ai-agents-for-beginners` [D|cld|M|+] — Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, tra — tags: agents,learning,notebooks,python — prov: openai,local
- `ai-engineering-hub` [D|hyb|E|+] — Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificia — tags: guias,agents,ai,llms,machine-learning,mcp,rag,jupyter notebook
- `andrej-karpathy-skills` [S|cld|E|+] — Guía de 4 principios inspirada en Andrej Karpathy para que tu agente de código responda útil y sin relleno. — tags: skills,coding-agent
- `anthropic-skills` [S|cld|E|+] — Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especific — tags: skills,docs,pdf,coding-agent,python — prov: anthropic
- `antigravity-awesome-skills` [S|hyb|E|+] — Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con insta — tags: skills,coding-agent,mcp,javascript — alt: awesome-agent-skills,awesome-claude-skills,wshobson-agents
- `arcads-claude-code` [S|cld|M|+] — Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, S — tags: video,image,skills,python
- `autoskills` [A|loc|E|~] — CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia. — tags: catalogos,ruby
- `awesome-agent-skills` [D|hyb|E|+] — Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comu — tags: skills,coding-agent,agents — alt: antigravity-awesome-skills,awesome-claude-skills
- `awesome-agents` [D|hyb|E|+] — Directorio de herramientas y proyectos abiertos para construir y operar agentes de inteligencia artificial. — tags: catalogos
- `awesome-claude-code` [D|cld|E|+] — Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alter — tags: coding-agent,skills,agents — prov: anthropic — alt: awesome-claude-skills
- `awesome-claude-skills` [D|cld|E|+] — Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para con — tags: skills,automation,coding-agent — prov: anthropic — alt: awesome-agent-skills,antigravity-awesome-skills,awesome-claude-code
- `awesome-copilot` [S|cld|E|+] — Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub C — tags: skills,coding-agent,prompts,mcp
- `awesome-llm-apps` [D|hyb|M|+] — Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y sk — tags: agents,rag,learning,python — prov: openai,anthropic,google,local — alt: openai-cookbook,claude-cookbooks
- `bmad-method` [S|loc|E|+] — Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. — tags: coding-agent,skills,agents — alt: spec-kit
- `chatgpt-dan` [D|cld|E|+] — Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT. — tags: prompts,chatgpt,gpt-3-5,gpt-4,jailbreak,openai,prompt
- `chatgpt-system-prompt` [D|hyb|E|+] — Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts. — tags: prompts,gpt,prompt,prompt-engineering,html
- `claude-cookbooks` [D|cld|E|+] — Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, ca — tags: learning,notebooks,rag,python — prov: anthropic — alt: openai-cookbook,awesome-llm-apps
- `claude-plugins-official` [S|cld|E|+] — Marketplace oficial de Anthropic con plugins para Claude Code, propios y de socios: comandos, agentes, skills  — tags: skills,coding-agent,mcp — prov: anthropic — alt: wshobson-agents
- `claude-quickstarts` [D|cld|M|+] — Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora. — tags: guias,python — prov: anthropic
- `claude-token-efficient` [S|loc|E|+] — Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto. — tags: metodologia,python — tools: claude-code
- `codex-plugin-cc` [S|cld|E|+] — Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas. — tags: metodologia,javascript — prov: openai — tools: claude-code
- `context-engineering` [D|cld|E|+] — Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la informaci — tags: learning,python
- `ecc` [P|loc|H|~] — Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendim — tags: automation,skills,javascript
- `fabric` [A|hyb|E|?] — CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. — tags: prompts,automation,go — prov: openai,anthropic,local — alt: prompts-chat
- `financial-services` [S|cld|M|+] — Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros. — tags: dominio,python — prov: anthropic
- `gemini-skills` [S|hyb|E|+] — Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini. — tags: catalogos,gemini,gemini-api,skills,python — prov: google
- `generative-ai-for-beginners` [D|cld|E|+] — Curso gratuito de Microsoft con 21 lecciones para empezar a construir aplicaciones con IA generativa. — tags: learning,prompts,python — alt: llm-course
- `geo-seo-claude` [S|cld|E|+] — Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms — tags: skills,search,pdf,python — prov: anthropic
- `grok-plugin-claude-code` [S|cld|E|+] — Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar. — tags: metodologia,ai-agents,claude-code,grok,grok-cli,plugin,xai,javascript — prov: xai — tools: claude-code
- `humanizer` [S|hyb|E|+] — Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales  — tags: skills,prompts,docs — alt: stop-slop
- `loop-engineering` [S|loc|E|+] — Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos. — tags: coding-agent,skills,typescript
- `marketingskills` [S|hyb|E|+] — Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code,  — tags: skills,analytics,email,search
- `openai-cookbook` [D|cld|E|+] — Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. — tags: learning,notebooks,python — alt: claude-cookbooks,awesome-llm-apps
- `ponytail` [S|loc|E|+] — Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribe — tags: skills,coding-agent
- `prompt-eng-tutorial` [D|cld|E|+] — Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios. — tags: learning,prompts,notebooks — prov: anthropic — alt: prompt-engineering-guide
- `prompt-engineering-guide` [D|cld|E|+] — Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. — tags: learning,prompts,rag — alt: prompt-eng-tutorial
- `prompt-master` [S|cld|E|+] — Skill que ayuda a redactar prompts precisos para cualquier herramienta de IA, buscando el mejor resultado sin  — tags: skills,prompts
- `prompts-chat` [D|loc|E|+] — La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. — tags: prompts,chatbot — alt: fabric
- `security-audit-skill` [S|hyb|M|+] — Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estru — tags: metodologia,javascript
- `skills` [D|cld|E|+] — Colección de skills de referencia mantenida por el proyecto aihero.dev / Total TypeScript, pensada como ejempl — tags: skills,coding-agent
- `skillspector` [S|cld|E|+] — Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. — tags: skills,coding-agent,python
- `social-media-research-skills` [S|cld|M|+] — Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. — tags: dominio,agent-skills,ai-agents,claude-code,claude-skills,competitor-analysis,content-marketing,cursor — tools: claude-code,codex — alt: last30days-skill
- `spec-kit` [S|loc|E|+] — Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. — tags: coding-agent,skills,python — alt: bmad-method
- `stop-slop` [S|hyb|E|+] — Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbric — tags: skills,prompts,docs — alt: humanizer
- `superclaude-framework` [S|hyb|M|+] — Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code. — tags: metodologia,python — tools: claude-code
- `superpowers` [S|cld|E|+] — Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseg — tags: skills,coding-agent — alt: agent-skills
- `system-prompts-and-models-of-ai-tools` [D|hyb|E|+] — Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño. — tags: prompts,ai,bolt,cluely,copilot,cursor,cursorai,devin
- `wshobson-agents` [S|hyb|E|+] — Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor — tags: skills,coding-agent,agents,python — alt: claude-plugins-official,antigravity-awesome-skills,agency-agents

### 3. Frameworks & Orquestación de Agentes (73)
Detalle: `REPO_MENU_cats/03-frameworks-orquestaci-n-de-agentes.md`

- `adk-python` [L|hyb|E|~] — Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. — tags: agents,python — prov: google,openai,anthropic — alt: langgraph,openai-agents-python
- `ag2` [L|cld|M|~] — Framework maduro para sistemas multiagente con patrones de colaboración (heredero directo de AutoGen). — tags: automation,agents,python — alt: autogen
- `agent-desktop` [A|loc|M|?] — CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. — tags: infra,accessibility,accessibility-api,ai-agents,automation,cli,computer-use,computer-use-agent
- `agent-framework` [R|hyb|M|~] — Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Ke — tags: agents,python — prov: openai,anthropic — alt: autogen,semantic-kernel
- `agent-protocol` [D|loc|E|+] — Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado. — tags: agents,python
- `agno` [R|hyb|E|~] — Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. — tags: agents,memory,python — prov: openai,anthropic,google,local — alt: crewai
- `aider` [R|hyb|E|~] — Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. — tags: coding-agent,python — prov: openai,anthropic,local — alt: opencode,cline,continue
- `autogen` [R|hyb|M|~] — Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento. — tags: agents,python — prov: openai,anthropic,local — alt: agent-framework,ag2,crewai
- `autogpt` [P|hyb|H|~] — Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. — tags: agents,automation,python — prov: openai,anthropic — alt: sim,langflow,flowise
- `autoresearch` [P|hyb|M|~] — Enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. — tags: research,agents,python
- `awesome-langgraph` [D|cld|E|+] — Repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. — tags: automation,agents,javascript
- `claude-code` [R|cld|E|+] — Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. — tags: coding-agent,agents,mcp,typescript — prov: anthropic,mcp — alt: codex,gemini-cli,opencode,goose
- `cline` [R|hyb|E|~] — Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. — tags: coding-agent,agents,typescript — prov: openai,anthropic,google,local — alt: continue,aider
- `codex` [R|cld|E|+] — Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. — tags: coding-agent,agents,rust — prov: openai,mcp — alt: claude-code,gemini-cli,opencode
- `codex-chatgpt-web` [A|cld|M|+] — Integración de terceros que conecta una sesión de ChatGPT Web con el selector de modelos y herramientas de Cod — tags: infra,chatgpt,chatgpt-pro,codex,free-ai,mcp,openai,playwright
- `composio` [P|cld|E|+] — Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps real — tags: agents,mcp,automation,typescript — prov: openai,anthropic,mcp
- `computer-use-preview` [R|cld|M|+] — Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. — tags: browser,agents,python — prov: google — alt: browser-use,skyvern
- `continue` [R|hyb|E|~] — Agente de código open source para VS Code, JetBrains y CI, con chat, autocompletado y revisiones. — tags: coding-agent,typescript — prov: openai,anthropic,local — alt: cline,aider
- `crewai` [L|cld|E|~] — Framework para orquestar "crews" de agentes con roles y tareas. — tags: automation,agents,python — alt: autogen,langgraph,agno,metagpt
- `deepagents` [R|hyb|E|~] — Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. — tags: agents,python — prov: anthropic,openai — alt: openai-agents-python
- `deeptutor` [A|hyb|M|~] — Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. — tags: learning,agents,rag,python — prov: openai,local — alt: open-notebook
- `deer-flow` [P|hyb|M|~] — Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. — tags: automation,research,python,docker
- `dify` [P|hyb|M|~] — Plataforma integral para construir apps de IA con backend y UI listos. — tags: automation,agents,python,docker — alt: sim,ragflow
- `dspy` [L|hyb|M|~] — Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. — tags: prompts,evaluation,python — prov: openai,anthropic,local — alt: promptfoo
- `e2b` [P|cld|E|+] — Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. — tags: agents,security,python — alt: sandbox
- `flowise` [A|hyb|E|~] — Builder visual drag-and-drop para pipelines LLM. — tags: automation,agents,typescript,docker — alt: sim,autogpt
- `gemini-cli` [R|cld|E|+] — Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. — tags: coding-agent,agents,typescript — prov: google,mcp — alt: claude-code,codex,opencode
- `goose` [R|hyb|E|~] — Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. — tags: coding-agent,agents,mcp,rust — prov: openai,anthropic,google,local — alt: opencode,claude-code,open-interpreter
- `gpt-researcher` [P|hyb|M|~] — Agente autónomo que investiga en línea y consolida reportes citados y estructurados. — tags: automation,research,python,docker — alt: storm,vane,open-deep-research
- `haystack` [L|hyb|M|~] — Framework de deepset para pipelines de RAG y agentes listos para producción. — tags: rag,agents,python — prov: openai,anthropic,local — alt: llama-index,langchain
- `hermes-agent` [A|loc|M|~] — Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. — tags: agents,python — alt: openclaw,mercury-agent
- `hermes-agent-self-evolution` [L|cld|M|~] — Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GE — tags: experimentos,python
- `langchain` [L|cld|M|~] — Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). — tags: agents,automation,python — alt: llama-index,haystack,semantic-kernel
- `langchain4j` [L|hyb|M|?] — Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la — tags: ts,anthropic,chatgpt,chroma,embeddings,gemini,gpt,huggingface
- `langflow` [A|hyb|M|~] — Constructor visual de flujos LLM/agentes construido sobre LangChain. — tags: automation,agents,python,docker — alt: sim,autogpt
- `langgraph` [R|hyb|M|~] — Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. — tags: agents,python — prov: openai,anthropic,google,local — alt: crewai,openai-agents-python,pydantic-ai,langgraph-supervisor-py,adk-python
- `langgraph-supervisor-py` [L|hyb|E|~] — Librería archivada para crear un agente supervisor que coordina a otros agentes en LangGraph. — tags: agents,python — alt: langgraph
- `langgraphjs` [R|hyb|M|~] — Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. — tags: agents,typescript — alt: mastra,vercel-ai
- `llama-index` [L|hyb|E|~] — Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. — tags: rag,agents,python — prov: openai,anthropic,local — alt: haystack,langchain
- `llm-council` [P|hyb|M|~] — "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. — tags: agents,python
- `local-deep-research` [P|hyb|M|~] — Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes  — tags: research,academia,anthropic,arxiv,brave,deep-research,encryption,home-automation — alt: open-deep-research
- `mastra` [L|hyb|E|~] — Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. — tags: agents,rag,typescript — prov: openai,anthropic,google,local — alt: langgraphjs,vercel-ai
- `mercury-agent` [A|hyb|E|~] — Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. — tags: agents,chatbot,typescript — alt: openclaw,hermes-agent
- `metagpt` [R|cld|M|+] — Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. — tags: py,agent,gpt,llm,metagpt,multi-agent,python — alt: crewai
- `mimo-code` [A|hyb|M|~] — Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria pers — tags: coding,ai,ai-agents,cli,mimo,mimo-code,typescript
- `mirofish` [P|hyb|H|~] — Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar  — tags: agents,python
- `multica` [P|hyb|M|~] — Plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas") — tags: agents,go
- `nemo-agent-toolkit` [L|hyb|H|~] — Toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). — tags: automation,agents,python
- `nemoclaw` [P|hyb|H|~] — Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. — tags: agents,security,typescript — alt: sandbox
- `nodeterm` [A|loc|M|~] — Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. — tags: infra,adhd,agent-orchestration,ai-agents,canvas,claude-code,codex,coding-agents
- `open-deep-research` [R|hyb|M|~] — Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servi — tags: research,python — alt: local-deep-research,gpt-researcher
- `open-interpreter` [R|loc|E|~] — Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos. — tags: coding-agent,local,rust — prov: openai,local — alt: goose
- `open-swe` [R|cld|M|+] — Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería. — tags: coding-agent,agents,python — prov: anthropic,openai — alt: openhands,swe-agent
- `openai-agents-python` [L|hyb|E|~] — SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. — tags: agents,python — prov: openai — alt: pydantic-ai,langgraph,smolagents,deepagents,adk-python
- `openclaude` [A|hyb|M|~] — Agente de código abierto para terminal que conecta proveedores remotos y modelos locales con herramientas y MC — tags: coding,ai,ai-agent,ai-tools,cli,typescript
- `openclaw` [A|hyb|M|~] — Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. — tags: agents,chatbot,typescript — prov: anthropic,openai,local — alt: hermes-agent,mercury-agent
- `opencode` [R|hyb|E|~] — Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. — tags: coding-agent,agents,typescript — prov: openai,anthropic,google,local — alt: claude-code,codex,goose,gemini-cli,aider
- `opencode-legacy` [A|hyb|M|?] — Agente de código en Go del antiguo proyecto opencode-ai, archivado y continuado bajo el nombre Crush. — tags: coding,ai,claude,code,llm,openai,go
- `opencursor` [A|hyb|M|~] — Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos. — tags: coding,agent,ai,code,coder,cursor,extension,ide
- `openevolve` [R|cld|H|+] — Agente de codificación evolutivo que optimiza algoritmos por simulación genética. — tags: automation,agents,python
- `openhands` [P|hyb|M|~] — Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). — tags: agents,automation,typescript,docker — alt: open-swe,swe-agent
- `paperclip` [P|hyb|H|~] — Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. — tags: asistentes,acpx,agent-orchestration,agent-skills,agentic-ai,ai-agents,ai-engineering,ai-governance
- `pydantic-ai` [L|hyb|E|~] — Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. — tags: agents,python — prov: openai,anthropic,google,local — alt: openai-agents-python,smolagents,langgraph
- `ruflo` [P|hyb|H|?] — Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude — tags: automation,agents,typescript
- `sandbox` [P|hyb|M|~] — Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un m — tags: agents,automation,python,docker — alt: nemoclaw,e2b
- `semantic-kernel` [L|hyb|M|~] — SDK de Microsoft para integrar LLM en apps de C#, Python y Java con plugins y planificación. — tags: agents,python — prov: openai — alt: agent-framework,langchain
- `sim` [P|hyb|M|~] — Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. — tags: agents,automation,typescript — prov: openai,anthropic,local — alt: flowise,langflow,dify,autogpt
- `smolagents` [L|hyb|E|~] — Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. — tags: agents,python — prov: openai,local — alt: pydantic-ai,openai-agents-python
- `social-media-agent` [R|cld|M|+] — Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de pu — tags: asistentes,typescript
- `storm` [R|hyb|M|~] — Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. — tags: research,agents,python — prov: openai — alt: gpt-researcher
- `swe-agent` [R|hyb|M|~] — Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo. — tags: coding-agent,evaluation,python — prov: openai,anthropic — alt: openhands,open-swe
- `t3code` [A|loc|E|~] — Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. — tags: coding-agent,ui,typescript
- `vercel-ai` [L|hyb|E|~] — Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. — tags: agents,ui,typescript,react — prov: openai,anthropic,google,local — alt: langgraphjs,mastra

### 4. Scraping, Búsqueda & Research Web (34)
Detalle: `REPO_MENU_cats/04-scraping-b-squeda-research-web.md`

- `agent-browser` [A|loc|E|~] — CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. — tags: navegador,rust — alt: playwright-cli
- `agent-reach` [A|loc|E|~] — CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. — tags: scraping,research,python — alt: snscrape
- `archivebox` [A|loc|E|~] — Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios. — tags: scraping,data,python,docker
- `awesome-chrome-devtools` [D|loc|E|+] — Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol. — tags: navegador,awesome,awesome-list
- `awesome-web-scraping` [D|hyb|E|+] — Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos. — tags: crawlers,captcha-bypass,captcha-recaptcha,crawler,crawling,crawling-framework,crawling-python,crawling-tool
- `browser-harness` [R|loc|E|~] — Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. — tags: browser,coding-agent,python — alt: playwright-mcp,chrome-devtools-mcp
- `browser-use` [L|hyb|M|~] — Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. — tags: automation,browser,python — alt: computer-use-preview,stagehand,skyvern,playwright-mcp
- `camofox-browser` [R|hyb|M|~] — Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes. — tags: navegador,ai-agent,anti-bot,antidetect-browser,automation,bot-detection,browser-automation,cloudflare-bypass
- `changedetection` [A|loc|E|~] — Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más. — tags: scraping,notifications,python,docker
- `crawl4ai` [L|loc|M|~] — Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pen — tags: scraping,python — alt: jina-reader
- `crawlee` [L|loc|M|~] — Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navega — tags: scraping,typescript
- `crawlee-python` [L|loc|M|~] — Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosist — tags: scraping,python
- `firecrawl` [P|cld|M|+] — Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio — tags: scraping,typescript,docker — alt: jina-reader
- `instaloader` [L|loc|E|~] — Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles,  — tags: vision,scraping,python
- `jina-reader` [P|cld|E|+] — Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. — tags: scraping,rag,typescript — alt: firecrawl,crawl4ai
- `last30days-skill` [S|cld|E|+] — Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días — tags: research,skills,python — alt: social-media-research-skills
- `lightpanda` [R|loc|E|?] — Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome. — tags: browser,scraping
- `llm-scraper` [L|hyb|E|~] — Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el — tags: scraping,typescript — alt: maxun
- `maxun` [P|loc|M|~] — Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. — tags: scraping,automation,typescript — alt: scrapegraph-ai,llm-scraper
- `playwright` [L|hyb|M|~] — Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola A — tags: automation,browser,typescript — alt: puppeteer,selenium
- `playwright-cli` [S|hyb|E|+] — Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador  — tags: browser,typescript — alt: agent-browser
- `puppeteer` [L|loc|E|~] — Librería de Google para controlar Chrome y Firefox desde Node.js. — tags: browser,scraping,typescript — alt: playwright,selenium
- `scrapegraph-ai` [L|hyb|M|~] — Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué e — tags: scraping,python — alt: maxun
- `scrapely` [L|loc|E|~] — Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mis — tags: scraping
- `scrapling` [L|loc|M|~] — Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica  — tags: automation,scraping,python
- `scrapy` [L|loc|M|~] — Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesam — tags: scraping,python
- `scrapydweb` [P|loc|M|~] — Panel web para administrar clústeres de Scrapyd y consultar trabajos, logs y estadísticas de Scrapy. — tags: crawlers,dashboard,log-analysis,log-parsing,scrapy,scrapy-log-analysis,scrapy-visualization,scrapyd
- `searxng` [P|loc|E|~] — Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. — tags: search,research,python,docker
- `selenium` [L|loc|M|~] — Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. — tags: browser,java,python — alt: playwright,puppeteer
- `skyvern` [P|hyb|M|~] — Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. — tags: browser,automation,python — prov: openai,anthropic — alt: browser-use,stagehand,computer-use-preview
- `snscrape` [L|loc|E|~] — Scraper de redes sociales (Twitter/X, Reddit, Telegram, Instagram, etc.) que recolecta posts y perfiles sin ne — tags: scraping,python — alt: agent-reach
- `stagehand` [L|hyb|E|~] — SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. — tags: browser,agents,typescript — prov: openai,anthropic — alt: browser-use,skyvern
- `vane` [A|loc|E|~] — Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). — tags: search,research,local,typescript — prov: openai,local — alt: gpt-researcher
- `yt-dlp` [A|loc|E|~] — Descargador de audio y video por línea de comandos compatible con miles de sitios. — tags: video,audio,scraping,python

### 5. MCP & Conectividad (24)
Detalle: `REPO_MENU_cats/05-mcp-conectividad.md`

- `annas-mcp` [R|hyb|M|?] — Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos. — tags: servidores,annas-archive,cli,mcp-server,go
- `awesome-mcp-clients` [D|loc|E|+] — Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y agentes. — tags: mcp
- `awesome-mcp-servers` [D|hyb|E|+] — Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos  — tags: automation,mcp
- `blender-mcp` [R|loc|E|~] — Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP. — tags: mcp,design,python — prov: mcp
- `chrome-devtools-mcp` [R|loc|E|~] — Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. — tags: mcp,browser,typescript — prov: mcp — alt: playwright-mcp,browser-harness
- `context7` [R|cld|E|+] — Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. — tags: mcp,docs,typescript — prov: mcp — alt: deepwiki-open
- `fastmcp` [L|loc|E|~] — La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. — tags: mcp,python — prov: mcp — alt: mcp-python-sdk
- `figma-context-mcp` [R|hyb|E|~] — Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos. — tags: mcp,design,ui,typescript — prov: mcp
- `free-for-dev` [D|cld|E|+] — Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. — tags: recursos,awesome-list,free-for-developers,html
- `freedomain` [D|cld|E|+] — Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. — tags: recursos,digitalplat,dns,dns-tutorial,documentation,domain,domain-platform,domain-registration
- `github-mcp-server` [R|hyb|E|~] — Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. — tags: mcp,code,go — prov: mcp
- `langchain-mcp-adapters` [L|loc|E|~] — Puente que convierte herramientas de servidores MCP en herramientas de LangChain y LangGraph. — tags: mcp,agents,python — prov: mcp — alt: mcp-use
- `masterdnsvpn` [A|hyb|M|?] — Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. — tags: redes,dns,dns-client,dns-proxy,dns-server,dns-tunnel,dns-tunneling,dnstt
- `mcp` [L|hyb|M|~] — Núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA intero — tags: mcp
- `mcp-for-beginners` [D|loc|E|+] — Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python. — tags: mcp,learning
- `mcp-inspector` [A|loc|E|~] — Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. — tags: mcp,evaluation,typescript
- `mcp-neo4j` [R|hyb|M|~] — Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con sopo — tags: mcp,python
- `mcp-python-sdk` [L|loc|E|~] — SDK oficial de Python para crear servidores y clientes del Model Context Protocol. — tags: mcp,python — prov: mcp — alt: fastmcp
- `mcp-typescript-sdk` [L|loc|E|~] — SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. — tags: mcp,typescript — prov: mcp — alt: mcp-use
- `mcp-use` [L|hyb|M|~] — Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de — tags: automation,mcp,typescript — alt: langchain-mcp-adapters,mcp-typescript-sdk
- `playwright-mcp` [R|loc|E|~] — Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. — tags: mcp,browser,typescript — prov: mcp — alt: chrome-devtools-mcp,browser-use,browser-harness
- `public-apis` [D|cld|E|+] — Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyect — tags: mcp,python
- `serena` [R|loc|E|~] — Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. — tags: mcp,coding-agent,code,python — prov: mcp — alt: codegraph,gitnexus
- `servers` [D|hyb|M|+] — Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enl — tags: mcp,typescript

### 6. Memoria, RAG & LLM Ops (35)
Detalle: `REPO_MENU_cats/06-memoria-rag-llm-ops.md`

- `agentmemory` [L|hyb|E|?] — Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida  — tags: agents,memory,typescript — alt: engram,supermemory,claude-mem
- `backdoor` [R|hyb|M|~] — Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. — tags: serving,ai,anthropic,claude,claude-code,deepseek,llm,ollama
- `chroma` [R|loc|E|~] — Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. — tags: vector-db,rag,rust — alt: qdrant,pgvector,milvus,faiss
- `claude-mem` [S|loc|E|+] — Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. — tags: memory,coding-agent,mcp,typescript — prov: anthropic,mcp — alt: engram,agentmemory
- `cognee` [L|hyb|E|~] — Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. — tags: memory,rag,python — prov: openai,local — alt: graphiti,mem0,graphrag,letta
- `deepeval` [L|hyb|E|~] — Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. — tags: evaluation,python — prov: openai — alt: ragas,promptfoo
- `engram` [R|loc|E|?] — Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. — tags: memory,mcp,coding-agent,go — prov: mcp — alt: claude-mem,agentmemory
- `faiss` [L|loc|M|~] — Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. — tags: vector-db,python,cpp — alt: qdrant,chroma
- `graphiti` [L|hyb|M|~] — Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. — tags: memory,rag,python — prov: openai,anthropic — alt: cognee,graphrag
- `graphrag` [L|hyb|M|~] — Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lu — tags: rag,python — alt: graphiti,cognee,lightrag
- `guardrails` [L|hyb|M|~] — Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM. — tags: security,chatbot,python
- `headroom` [L|hyb|E|~] — Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder  — tags: automation,llmops,python — alt: rtk
- `langfuse` [P|hyb|M|~] — Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llama — tags: automation,observability,typescript,docker — alt: phoenix,opik,mlflow
- `letta` [P|hyb|M|~] — Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). — tags: memory,agents,python — prov: openai,anthropic,local — alt: mem0,cognee
- `lightrag` [L|hyb|M|~] — RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. — tags: rag,python — prov: openai,local — alt: graphrag,ragflow,pageindex
- `litellm` [L|hyb|E|~] — Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato d — tags: inference,llmops,python,docker
- `loguru` [L|loc|E|~] — Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin  — tags: observability,evaluation,python
- `mem0` [L|hyb|E|~] — Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y — tags: memory,python — alt: letta,cognee,supermemory
- `mempalace` [L|loc|E|~] — Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin envia — tags: memory,python
- `milvus` [R|loc|H|?] — Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. — tags: vector-db,rag,go,docker — alt: qdrant,chroma
- `mlflow` [P|loc|E|~] — Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. — tags: observability,training,evaluation,python — alt: langfuse
- `opik` [P|loc|M|~] — Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. — tags: observability,evaluation,python — alt: langfuse,phoenix
- `pageindex` [L|cld|E|~] — Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. — tags: rag,docs,python — prov: openai — alt: lightrag
- `pgvector` [L|loc|E|?] — Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. — tags: vector-db,postgres,rag — alt: qdrant,chroma
- `phoenix` [P|loc|E|~] — Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. — tags: observability,evaluation,python — alt: langfuse,opik
- `promptfoo` [A|loc|E|~] — CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. — tags: evaluation,security,typescript — prov: openai,anthropic,google,local — alt: deepeval,ragas,dspy
- `qdrant` [R|loc|E|~] — Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. — tags: vector-db,rag,rust,docker — alt: milvus,chroma,pgvector,faiss
- `ragas` [L|hyb|E|~] — Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. — tags: evaluation,rag,python — prov: openai — alt: deepeval,promptfoo
- `ragflow` [P|loc|H|~] — Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. — tags: rag,docs,agents,docker — prov: openai,local — alt: dify,lightrag
- `rtk` [A|loc|E|?] — Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código — tags: tokens,agentic-coding,ai-coding,anthropic,claude-code,cli,command-line-tool,cost-reduction — alt: headroom
- `sglang` [R|loc|H|~] — Framework de servicio de alto rendimiento para LLM y modelos multimodales. — tags: inference,python — prov: local — alt: vllm
- `supermemory` [P|hyb|E|~] — Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. — tags: memory,rag,typescript — alt: mem0,agentmemory
- `tensorrt-llm` [L|loc|H|~] — Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes esp — tags: serving,blackwell,cuda,llm-serving,moe,pytorch,python
- `turbovec` [L|loc|E|~] — Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación  — tags: automation,vector-db,rust
- `vllm` [R|loc|H|~] — Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. — tags: inference,python — prov: local — alt: sglang

### 7. Inteligencia de Código, Datos & Entrenamiento (44)
Detalle: `REPO_MENU_cats/07-inteligencia-de-c-digo-datos-entrenamiento.md`

- `ast-grep` [A|loc|E|?] — CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. — tags: code,security,rust — alt: semgrep
- `awesome-bigdata` [D|cld|E|+] — Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para des — tags: data
- `awesome-machine-learning` [D|hyb|E|+] — Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema. — tags: aprender,python
- `bigdata` [D|loc|H|+] — Colección educativa de proyectos de datos con ejercicios de Hive, HDFS, Spark, HBase y sistemas de recomendaci — tags: datos,java
- `bionemo-recipes` [D|loc|H|+] — Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. — tags: entrenamiento,drug-discovery,gpu,machine-learning,pytorch,python
- `cli` [A|cld|E|+] — CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. — tags: code,go
- `codebase-memory-mcp` [R|loc|E|?] — Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para  — tags: code,mcp,memory — prov: mcp — alt: codegraph,gitnexus
- `codegraph` [R|loc|E|~] — CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada arc — tags: code,typescript — alt: codebase-memory-mcp,serena
- `cosmos` [R|hyb|H|~] — Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos — tags: inference
- `data-science-ipython-notebooks` [D|loc|E|+] — Gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep l — tags: data,python
- `deepseek-coder` [R|hyb|H|~] — Familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para  — tags: inference,python
- `deepwiki-open` [A|hyb|M|~] — Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki. — tags: code,docs,python — prov: openai,google,local — alt: context7
- `defending-code-reference-harness` [S|cld|M|+] — Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilid — tags: security,skills,coding-agent — prov: anthropic
- `duckdb` [L|loc|E|?] — Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. — tags: data,analytics,cpp — alt: polars
- `gitnexus` [A|hyb|E|~] — Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar  — tags: code,typescript — alt: repomix,codebase-memory-mcp,serena
- `globalbuildingatlas` [D|loc|H|+] — Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. — tags: datos,python
- `graphify` [R|hyb|M|~] — Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos. — tags: code,python
- `how-to-train-your-gpt` [D|loc|E|+] — Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librerí — tags: learning
- `hudi` [P|hyb|H|~] — Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. — tags: datos,apacheflink,apachehudi,apachespark,bigdata,data-integration,datalake,hudi
- `llama-factory` [A|loc|M|~] — Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. — tags: training,python — prov: local — alt: unsloth
- `llm-course` [D|loc|E|+] — Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. — tags: learning,training,notebooks — alt: llms-from-scratch,generative-ai-for-beginners
- `llm.c` [L|loc|H|?] — Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados,  — tags: learning
- `llms-from-scratch` [D|loc|M|+] — Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. — tags: learning,training,python — alt: llm-course,nanogpt
- `machinelearning` [D|loc|M|+] — Ejemplos educativos de algoritmos de machine learning y redes neuronales con Python. — tags: aprender,python
- `marimo` [A|loc|E|~] — Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. — tags: notebooks,data,python
- `nanochat` [L|loc|M|~] — Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde e — tags: learning,python
- `nanogpt` [L|loc|M|~] — Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quep — tags: learning,python — alt: llms-from-scratch
- `nemotron` [D|loc|H|+] — Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. — tags: training,inference — prov: local
- `openai-python` [L|cld|E|~] — SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. — tags: code,python
- `peft` [L|loc|M|~] — Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. — tags: training,python
- `polars` [L|loc|E|~] — Librería de DataFrames escrita en Rust, mucho más rápida que pandas. — tags: data,python,rust — alt: duckdb
- `python-machine-learning-book` [D|loc|M|+] — Código de la primera edición del libro Python Machine Learning, con ejemplos de algoritmos y evaluación. — tags: aprender,data-mining,data-science,logistic-regression,machine-learning,machine-learning-algorithms,neural-network,python
- `pytorch` [L|loc|M|~] — Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. — tags: training,python
- `repomix` [A|loc|E|~] — Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. — tags: code,coding-agent,typescript — alt: gitnexus
- `semgrep` [A|loc|E|~] — Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. — tags: security,code — alt: ast-grep
- `swe-bench` [D|loc|H|+] — Benchmark para evaluar si los modelos resuelven issues reales de GitHub. — tags: evaluation,coding-agent,python
- `tensorflow` [L|loc|H|?] — Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entor — tags: entrenamiento,deep-learning,deep-neural-networks,distributed,machine-learning,ml,neural-network,python
- `timesfm` [L|loc|M|~] — Modelo fundacional de Google Research para pronosticar series de tiempo sin entrenamiento previo. — tags: data,analytics,python
- `train-llm-from-scratch` [D|loc|H|+] — Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generaci — tags: aprender,gemini,large-language-models,llm,openai,training,transformers,python
- `transformers` [L|loc|E|~] — Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. — tags: training,inference,python
- `tree-sitter` [L|loc|M|?] — Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. — tags: code,rust
- `trl` [L|loc|M|~] — Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. — tags: training,python
- `unsloth` [A|loc|M|~] — Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI. — tags: training,local,python — prov: local — alt: llama-factory
- `warp` [L|loc|H|~] — Framework de NVIDIA que compila funciones de Python en kernels para simulación física y cálculo en CPU o GPU. — tags: entrenamiento,cuda,differentiable-programming,gpu,gpu-acceleration,nvidia,nvidia-warp,python

### 8. IA Local: Modelos, Chats & Workspaces (25)
Detalle: `REPO_MENU_cats/08-ia-local-modelos-chats-workspaces.md`

- `anything-llm` [A|loc|E|~] — App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. — tags: rag,agents,local,javascript — prov: openai,anthropic,local — alt: open-webui,khoj,private-gpt
- `chatbox` [A|hyb|E|~] — Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz comú — tags: chats,assistant,chatbot,chatgpt,claude,claude-code,copilot,deepseek — alt: jan
- `cherry-studio` [A|hyb|E|~] — App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. — tags: chatbot,agents,typescript — prov: openai,anthropic,google,local — alt: jan,lobehub
- `exo` [R|loc|M|~] — Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina. — tags: inference,local,python — prov: local
- `hermes-desktop` [A|loc|E|~] — App de escritorio que envuelve al agente Hermes en una interfaz nativa. — tags: agents,ui,typescript
- `jan` [A|loc|E|~] — App de escritorio open source, alternativa a ChatGPT que corre 100 % sin conexión. — tags: chatbot,local,rust — prov: local,openai — alt: cherry-studio,textgen,chatbox
- `khoj` [A|hyb|M|~] — Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. — tags: research,rag,agents,python — prov: openai,anthropic,local — alt: anything-llm,surfsense
- `librechat` [A|hyb|M|~] — Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. — tags: chatbot,agents,typescript,docker — prov: openai,anthropic,google,local — alt: open-webui,lobehub
- `llama-cpp` [R|loc|M|?] — Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. — tags: inference,local,cpp — prov: local — alt: ollama,llamafile,localai
- `llamafile` [R|loc|E|?] — Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. — tags: inference,local,cpp — prov: local — alt: ollama,llama-cpp
- `llmfit` [L|hyb|E|~] — Herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar mod — tags: inference,local,rust
- `lobehub` [A|hyb|E|~] — Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. — tags: chatbot,agents,typescript — prov: openai,anthropic,google,local — alt: open-webui,librechat,cherry-studio
- `localai` [R|loc|M|~] — Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. — tags: inference,local,go,docker — prov: local — alt: ollama,llama-cpp
- `muse-spark` [A|hyb|H|~] — Proyecto de terceros que se presenta como un estudio de IA de escritorio; su afiliación y funciones no están v — tags: workspaces,download-muse-ai,download-muse-spark,muse,muse-ai,muse-spark,muse-spark-1-1,muse-spark-1-2
- `nextcloud-server` [P|hyb|H|~] — Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia. — tags: workspaces,cloud,collaboration,decentralized,design,distributed,enterprise,federation
- `notebooklm-mcp-cli` [R|cld|E|+] — CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde termi — tags: mcp,notebooks,python
- `notebooklm-py` [L|cld|E|~] — API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuen — tags: notebooks,research,python
- `odysseus` [P|loc|H|~] — Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por age — tags: agents,local,python,docker
- `ollama` [R|loc|E|?] — La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. — tags: inference,local,go — prov: local — alt: llama-cpp,localai,llamafile
- `open-notebook` [A|loc|M|~] — Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y ge — tags: notebooks,research,typescript,docker — alt: deeptutor,surfsense
- `open-webui` [A|loc|E|~] — Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. — tags: chatbot,local,rag,docker — prov: openai,local — alt: librechat,lobehub,anything-llm,textgen
- `private-gpt` [P|loc|M|~] — Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. — tags: rag,local,python — prov: local,openai — alt: anything-llm
- `surfsense` [A|hyb|M|~] — Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. — tags: research,rag,notebooks,python — prov: openai,local — alt: open-notebook,khoj
- `textgen` [A|loc|M|~] — App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. — tags: chatbot,local,inference,python — prov: local — alt: jan,open-webui
- `transformers.js` [L|loc|M|~] — Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript. — tags: motores,browser,javascript,transformers,webml

### 9. Diseño, UI & Frontend (35)
Detalle: `REPO_MENU_cats/09-dise-o-ui-frontend.md`

- `animejs` [L|loc|E|~] — Motor de animación JavaScript ligero para CSS, SVG, DOM y objetos. — tags: ui,design,javascript — alt: gsap,motion
- `ant-design` [L|loc|E|~] — Lenguaje de diseño empresarial y librería de componentes React de Ant Group. — tags: ui,react,typescript — alt: mui,ui
- `assistant-ui` [L|loc|E|~] — Librería React y TypeScript para interfaces de chat con IA de calidad producción. — tags: ui,chatbot,react,typescript — alt: copilotkit
- `copilotkit` [L|hyb|E|~] — Stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI. — tags: ui,agents,react,typescript — prov: openai,anthropic — alt: assistant-ui
- `daisyui` [L|loc|E|~] — La librería de componentes más popular para Tailwind CSS, con clases semánticas y temas. — tags: ui,design,javascript — alt: ui
- `design.md` [S|cld|E|+] — Formato para describir una identidad visual a agentes de código con tokens YAML y prosa. — tags: skills,design,typescript
- `excalidraw` [A|loc|E|~] — Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa. — tags: design,docs,typescript — alt: tldraw,mermaid
- `front-end-checklist` [D|loc|E|+] — Checklist y recursos para revisar aspectos de calidad de un frontend antes de entregarlo. — tags: skills,ai-agent,ai-agents,checklist,css,front-end-developer-tool,front-end-development,frontend
- `gsap` [L|loc|M|~] — Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincro — tags: ui,design,javascript — alt: animejs
- `heroui` [L|loc|E|~] — Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, da — tags: ui,typescript — alt: mui
- `impeccable` [S|cld|E|+] — Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" d — tags: skills,design,rust
- `lucide` [L|loc|E|~] — Librería de más de 1500 iconos SVG consistentes, con paquetes para React, Vue y más. — tags: ui,design,typescript
- `magicui` [L|loc|E|~] — Librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces mod — tags: ui — alt: react-bits
- `motion` [L|loc|E|~] — Librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteraccio — tags: ui,design,typescript — alt: animejs
- `mui` [L|loc|E|~] — Librería de componentes React completa que implementa Material Design de Google. — tags: ui,react,javascript — alt: ant-design,ui,heroui
- `normalize.css` [L|loc|E|?] — Hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme. — tags: ui,design
- `onlook` [A|loc|E|~] — Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma. — tags: design,ui,coding-agent,typescript — prov: anthropic — alt: open-design
- `open-design` [A|hyb|M|~] — Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural. — tags: agents,design,typescript — alt: onlook
- `openui` [L|hyb|E|~] — Estándar abierto de Thesys para UI generativa: el LLM responde con interfaces, no solo texto. — tags: ui,agents,typescript
- `penpot` [A|loc|H|~] — Plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que qui — tags: design,docker
- `plasmic` [A|hyb|M|~] — Builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin per — tags: design,typescript
- `radix-primitives` [L|loc|E|~] — Componentes React sin estilos y accesibles para construir sistemas de diseño propios. — tags: ui,react,typescript
- `react-bits` [L|loc|E|~] — La mayor colección open source de componentes React animados e interactivos para webs llamativas. — tags: ui,react,javascript — alt: magicui
- `react-three-fiber` [L|loc|M|~] — Renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos. — tags: ui,design,typescript
- `screenshot-to-code` [A|cld|E|+] — Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue. — tags: ui,vision,code,python — prov: openai,anthropic,google — alt: stitch-sdk
- `skills-emil` [S|cld|E|+] — Colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrolla — tags: skills,design
- `stitch-sdk` [L|cld|E|~] — SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código. — tags: ui,design,typescript — prov: google — alt: screenshot-to-code
- `stitch-skills` [S|cld|E|+] — Colección de skills de agente para trabajar con el servidor MCP de Google Stitch. — tags: skills,design,ui
- `swr` [L|loc|E|~] — Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los reva — tags: ui,typescript
- `tailwindcss` [L|loc|E|~] — Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directame — tags: ui,design,typescript
- `taste-skill` [S|cld|E|+] — Skills "anti-slop" para producir frontends premium (layout, tipografía, motion y espaciado) más skills de gene — tags: skills,design,javascript
- `three.js` [L|loc|M|~] — Motor 3D (WebGL) para renderizar gráficos y escenas interactivas directamente en el navegador. — tags: ui,design,javascript
- `tldraw` [L|loc|E|~] — SDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas. — tags: design,ui,react,typescript — alt: excalidraw
- `ui` [L|loc|E|~] — Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de in — tags: ui,typescript — alt: mui,ant-design,daisyui
- `ui-ux-pro-max-skill` [S|cld|E|+] — Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para  — tags: skills,design,python

### 10. Analítica & Visualización (37)
Detalle: `REPO_MENU_cats/10-anal-tica-visualizaci-n.md`

- `autohedge` [R|cld|H|+] — Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado. — tags: finanzas,ai,blackrock,finance,goldmansachs,hedgefund,jpmorgan,ml
- `awesome-dataviz` [D|cld|E|+] — Directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad — tags: automation,dataviz,javascript
- `binance-trader` [A|cld|M|+] — Bot experimental de Python para estudiar estrategias y automatización con la API de Binance. — tags: finanzas,arbitrage,binance,bitcoin,btc,cryptocurrency,trade,python
- `chart-js` [L|loc|E|~] — Librería JavaScript sencilla para gráficos HTML5 en canvas. — tags: dataviz,javascript — alt: echarts,recharts
- `chartanalyst` [L|loc|M|~] — Experimento de aprendizaje profundo que usa redes convolucionales para reconocer patrones en gráficos bursátil — tags: finanzas,python
- `crypto-trader` [L|cld|M|~] — Biblioteca de Python con bindings de la API de Gemini y un ejemplo de estrategia de criptomonedas. — tags: finanzas,algorithm,bitcoin,bot,coinbase,exchange-api,gemini,market
- `d3` [L|loc|M|~] — Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y HTML. — tags: dataviz,javascript — alt: echarts
- `daily-stock-analysis` [A|cld|M|+] — Sistema que analiza acciones de varios mercados con LLM y envía un tablero de decisiones diario. — tags: analytics,agents,python — prov: openai,google
- `dash` [L|loc|M|~] — Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con compone — tags: automation,ui,python
- `data-analyst-roadmap` [D|loc|E|+] — Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y orientación de carrera. — tags: recursos,blogs,businessintelligence,courses,data,dataanalysis,dataanalyst,excel
- `dataanalystportfolioprojects` [D|loc|M|+] — Portafolio de ejemplos de análisis de datos con SQL, Python, Tableau, Excel y Hive. — tags: recursos,analytics,dashboard,data-visualization,excel,hadoop,hiveq,portfolio
- `dexter` [A|cld|M|+] — Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis. — tags: finanzas,typescript
- `echarts` [L|loc|M|~] — Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gr — tags: dataviz,typescript — alt: d3,chart-js,recharts
- `finceptterminal` [A|hyb|H|~] — Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes. — tags: finanzas,ai-agents,algorithmic-trading,bloomberg-terminal,cpp,finance,financial-markets,fintech
- `gradio` [L|loc|E|~] — Librería Python para crear y compartir apps web de modelos de ML en minutos. — tags: ui,python — alt: streamlit
- `grafana` [P|loc|E|~] — Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes. — tags: observability,dataviz,typescript,docker
- `intellitrader` [A|hyb|M|?] — Bot configurable de criptomonedas con componentes de simulación, señales y conexión a exchanges. — tags: finanzas,binance,bitcoin,bot,crypto,cryptocurrencies,cryptocurrency,trading-bot
- `machine-learning-for-trading` [D|hyb|H|+] — Material y código de Machine Learning for Trading para estudiar datos, modelos y evaluación de estrategias. — tags: finanzas,algorithmic-trading,artificial-intelligence,backtesting,data-science,deep-learning,finance,investment
- `matomo` [P|loc|M|?] — Alternativa open source a Google Analytics con control total de los datos. — tags: analytics,php — alt: umami,plausible
- `metabase` [P|hyb|M|?] — Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos  — tags: analytics,dataviz,docker — alt: superset,redash
- `open-sol-bot` [P|hyb|H|~] — Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado. — tags: finanzas,blockchain,solana,telegram-bot,trader,transaction,python
- `osiris` [A|hyb|M|~] — Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. — tags: osint,typescript
- `pandas-ai` [L|hyb|E|~] — Librería para conversar con tus datos (SQL, CSV, Parquet) usando LLM. — tags: analytics,data,python — prov: openai,local — alt: wrenai
- `plausible` [P|hyb|M|?] — Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. — tags: analytics,docker — alt: umami,matomo
- `posthog` [P|hyb|H|~] — Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session re — tags: analytics,python,docker
- `pythia` [P|loc|H|~] — Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción. — tags: osint,typescript
- `qlib` [P|loc|H|~] — Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias. — tags: finanzas,algorithmic-trading,auto-quant,deep-learning,finance,fintech,investment,machine-learning
- `quantharness` [R|cld|M|+] — Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de t — tags: finanzas,agentic-ai,large-language-models,html
- `recharts` [L|loc|E|~] — Librería de gráficos para React construida con D3, declarativa y componible. — tags: dataviz,react,typescript — alt: chart-js,echarts
- `redash` [P|loc|M|~] — Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. — tags: analytics,dataviz,typescript — alt: metabase,superset
- `stocks-analyst` [D|hyb|M|+] — Scripts para recopilar recomendaciones de analistas bursátiles y preparar datos para su evaluación histórica. — tags: finanzas,jupyter notebook
- `streamlit` [L|loc|E|~] — Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin t — tags: ui,dataviz,python — alt: gradio
- `superset` [P|loc|M|~] — Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. — tags: analytics,dataviz,python,docker — alt: metabase,redash
- `tradingagents` [R|cld|M|+] — Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de tradi — tags: finanzas,agent,finance,llm,multiagent,trading,python
- `umami` [P|loc|E|~] — Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. — tags: analytics,typescript,docker — alt: plausible,matomo
- `uplot` [L|loc|E|~] — Librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penaliz — tags: dataviz,javascript
- `wrenai` [P|hyb|M|~] — BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. — tags: analytics,data,agents,python — prov: openai,local — alt: pandas-ai

### 11. Generación de Imagen & Visión (28)
Detalle: `REPO_MENU_cats/11-generaci-n-de-imagen-visi-n.md`

- `codeformer` [L|loc|M|~] — Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. — tags: image,vision,python — alt: gfpgan
- `comfyui` [R|loc|H|~] — Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. — tags: image,python — alt: wan2gp,sd-webui-forge
- `comfyui-ipadapter-plus` [R|loc|H|~] — Conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una o varia — tags: image,python
- `controlnet` [R|loc|H|~] — Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. — tags: image,python
- `deep-live-cam` [R|loc|H|~] — Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. — tags: vision,image,python — alt: facefusion
- `diffusers` [L|loc|H|~] — Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. — tags: image,python
- `face-recognition` [L|loc|M|~] — Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas  — tags: image,vision,python — alt: insightface
- `facefusion` [A|loc|M|~] — Plataforma para intercambio y mejora de rostros en imágenes y video. — tags: image,video,vision,python — alt: deep-live-cam
- `flux` [R|loc|H|~] — Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes. — tags: image,python — prov: local — alt: stable-diffusion-webui
- `fooocus` [A|loc|M|~] — Herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, oc — tags: image,python
- `gfpgan` [R|loc|M|~] — Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando pr — tags: image,python — alt: codeformer
- `insightface` [L|loc|M|~] — Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. — tags: vision,image,python — alt: face-recognition
- `invokeai` [A|loc|H|~] — Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpain — tags: image,typescript — alt: krita-ai-diffusion
- `krita-ai-diffusion` [A|loc|M|~] — Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. — tags: image,design,python — prov: local — alt: invokeai
- `label-studio` [P|loc|E|~] — Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. — tags: data,vision,training,docker
- `liveportrait` [R|loc|H|~] — Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia — tags: image,vision,python
- `open-generative-ai` [P|hyb|M|~] — Plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos acc — tags: image,video,javascript
- `opencv` [L|loc|E|~] — La librería de visión por computadora de referencia, con miles de algoritmos. — tags: vision,image,cpp,python
- `real-esrgan` [R|loc|M|~] — Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de b — tags: image,python
- `rembg` [L|loc|E|~] — Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. — tags: image,python
- `ruview` [P|loc|H|?] — Proyecto de detección espacial que experimenta con señales WiFi para estimar presencia y movimiento. — tags: sensores,claude,claude-code,esp32,firmware,home-assistant,home-automation,iot
- `sam2` [L|loc|M|~] — Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. — tags: vision,video,python — alt: segment-anything
- `sd-webui-controlnet` [R|loc|H|~] — Extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI (AUTOMATIC11 — tags: vision,image,python
- `sd-webui-forge` [A|loc|M|~] — Versión optimizada de la WebUI de Stable Diffusion, más rápida y con menos memoria. — tags: image,local,python — prov: local — alt: stable-diffusion-webui,comfyui
- `segment-anything` [L|loc|M|~] — Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja. — tags: vision,image,python — alt: sam2
- `stable-diffusion-webui` [A|loc|H|~] — Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpaintin — tags: vision,image,python — alt: sd-webui-forge,flux
- `supervision` [L|loc|E|~] — Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. — tags: vision,python
- `ultralytics` [L|loc|E|~] — Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. — tags: vision,training,python

### 12. Audio, Voz & Video (50)
Detalle: `REPO_MENU_cats/12-audio-voz-video.md`

- `ace-step-1.5` [P|loc|H|~] — Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tam — tags: musica,text2music,python
- `ai-youtube-shorts-generator` [A|hyb|M|~] — Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de mome — tags: generativo,2short-ai-alternative,ai-clip-generator,ai-clipping,auto-clip,auto-crop,highlight-detection,klap-alternative
- `audiocraft` [L|loc|M|~] — Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códe — tags: audio,inference,training,python — prov: local
- `chatterbox` [L|loc|E|~] — Modelo de texto a voz open source de Resemble AI con clonación de voz y control de emoción. — tags: tts,audio,python — prov: local — alt: fish-speech,gpt-sovits,kokoro,luxtts
- `cosyvoice` [L|loc|M|~] — Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. — tags: tts,audio,python — prov: local — alt: fish-speech,index-tts
- `davinci-resolve-mcp` [R|loc|M|~] — Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render — tags: video,mcp,agents,python — prov: mcp
- `edge-tts` [L|cld|E|~] — Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. — tags: tts,speech-synthesis,text-to-speech,python — alt: kokoro
- `faster-whisper` [R|loc|M|~] — Reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria,  — tags: stt,audio,python — alt: whisper-cpp
- `ffmpeg` [A|loc|E|?] — Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier forma — tags: video,audio,automation,cpp
- `fish-speech` [L|loc|M|~] — Sistema de texto a voz open source de alta calidad con clonación de voz multilingüe. — tags: tts,audio,python — prov: local — alt: chatterbox,cosyvoice,gpt-sovits
- `gpt-sovits` [A|loc|M|~] — Clonación de voz y TTS con solo un minuto de audio, con interfaz web para entrenar. — tags: tts,audio,python — prov: local — alt: chatterbox,fish-speech
- `hunyuanvideo` [R|loc|H|~] — Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de infere — tags: video,inference,local,python — prov: local — alt: wan2-2,ltx-video
- `hyperframes` [R|loc|E|~] — Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo use — tags: video,agents,skills,typescript — prov: mcp — alt: remotion,moviepy
- `index-tts` [L|loc|M|~] — Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. — tags: tts,audio,python — prov: local — alt: cosyvoice
- `kokoro` [L|loc|E|~] — Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. — tags: tts,audio,local — prov: local — alt: chatterbox,tts,luxtts,edge-tts
- `livekit-agents` [R|hyb|M|~] — Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. — tags: audio,agents,video,python — prov: openai,anthropic,google — alt: pipecat
- `lossless-cut` [A|loc|E|~] — App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. — tags: video,audio,ui,typescript
- `ltx-video` [R|loc|H|~] — Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; ho — tags: video,inference,local,python — prov: local — alt: wan2-2,hunyuanvideo
- `luxtts` [L|loc|E|~] — Modelo de TTS ligero con clonación de voz que genera audio hasta 150 veces más rápido que tiempo real. — tags: tts,audio,python — prov: local — alt: kokoro,chatterbox
- `manim` [L|loc|M|~] — Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenG — tags: video,dataviz,learning,python — alt: manim-community
- `manim-community` [L|loc|M|~] — Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. — tags: programatico,animations,hacktoberfest,manim,math,python — alt: manim
- `moneyprinterturbo` [A|hyb|M|~] — App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música e — tags: video,automation,tts,python — prov: openai,anthropic,google,local — alt: openmontage,videofy-minimal
- `moviepy` [L|loc|E|~] — Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efecto — tags: video,audio,automation,python — alt: remotion,hyperframes
- `music-megathread` [D|hyb|E|+] — Directorio de reproductores, herramientas, servicios y otros recursos relacionados con música. — tags: musica
- `nemo` [L|loc|H|~] — Framework de NVIDIA para entrenar y usar modelos de voz: reconocimiento, síntesis y más. — tags: stt,tts,audio,python — alt: whisperx
- `obs-studio` [A|loc|E|?] — App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio e — tags: video,audio,ui,cpp — alt: openscreen
- `omnivoice-studio` [A|loc|M|~] — Alternativa local y open source a ElevenLabs: clonación, diseño y conversión de voz en una app. — tags: tts,audio,python — alt: videolingo
- `opencut` [A|hyb|M|~] — Editor de video libre con línea de tiempo, alternativa a CapCut, que funciona en el navegador y procesa en tu  — tags: video,ui,typescript,rust
- `openmontage` [S|loc|M|+] — Convierte tu agente de código en un estudio de producción de video completo. — tags: video,coding-agent,skills — alt: remotion-superpowers,moneyprinterturbo
- `openscreen` [A|loc|E|~] — App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a  — tags: video,ui,typescript — alt: obs-studio
- `palmier-pro` [A|loc|M|?] — Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios  — tags: edicion,ai-video,claude,macos,mcp,seedance2,swift,video-editor
- `pipecat` [R|hyb|M|~] — Framework open source para agentes de voz y apps multimodales en tiempo real. — tags: audio,agents,stt,tts,python — prov: openai,anthropic,google — alt: livekit-agents
- `rea-video` [S|hyb|M|+] — Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO — tags: programatico,agent-skills,ai-video,aigc-detection,claude-code,codex,ffmpeg,prompt-engineering
- `remotion` [L|loc|M|~] — Framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a — tags: video,typescript — alt: moviepy,hyperframes
- `remotion-superpowers` [S|loc|E|+] — Plugin que convierte Remotion en un estudio de video para Claude Code, Codex o Gemini CLI. — tags: video,skills,coding-agent — alt: openmontage,video-use
- `rvc` [A|loc|M|~] — Conversión de voz: entrena un modelo con menos de 10 minutos de audio y transforma una voz en otra. — tags: audio,tts,python — prov: local
- `short-video-factory` [A|hyb|M|~] — Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. — tags: generativo,ai,automatic,automation,clipping,cross-platform,desktop,linux
- `skills-remotion` [S|loc|E|+] — Skills oficiales de Remotion para que tu agente de código cree videos con React. — tags: video,skills
- `supertonic` [R|loc|M|~] — Motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en e — tags: tts,audio
- `tts` [L|loc|M|~] — Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y  — tags: tts,audio,python — alt: kokoro
- `vibevoice` [L|loc|H|~] — Modelos de voz de frontera de Microsoft para podcasts largos con varios hablantes y tiempo real. — tags: tts,audio,python — prov: local
- `video-use` [S|loc|E|+] — Herramienta para editar videos con agentes de código como Claude Code, de los creadores de browser-use. — tags: video,coding-agent,skills,python — alt: remotion-superpowers
- `videofy-minimal` [A|loc|E|~] — Herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pi — tags: video,typescript — alt: moneyprinterturbo
- `videolingo` [A|hyb|M|~] — App que subtitula, traduce y dobla videos de forma automática: ASR con timestamps por palabra, traducción con  — tags: video,stt,tts,python — prov: openai — alt: omnivoice-studio
- `voxcpm` [R|loc|H|~] — Modelo de texto a voz sin tokenizador que clona voces con naturalidad y expresividad alta. — tags: tts,audio,python
- `wan2-2` [R|loc|H|~] — Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y li — tags: video,inference,local,python — prov: local — alt: hunyuanvideo,ltx-video
- `wan2gp` [A|loc|H|~] — App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modes — tags: video,image,tts,local,python — prov: local,mcp — alt: comfyui
- `whisper` [R|loc|M|~] — Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que tran — tags: stt,audio,python — alt: whisper-cpp
- `whisper-cpp` [R|loc|E|?] — Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. — tags: stt,audio,local,cpp — prov: local — alt: faster-whisper,whisper
- `whisperx` [R|loc|M|~] — Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para s — tags: stt,audio,python — alt: nemo

### 13. Documentos & Presentaciones (24)
Detalle: `REPO_MENU_cats/13-documentos-presentaciones.md`

- `archify` [S|loc|E|+] — Skill para convertir ideas, planes y bases de código en diagramas y visualizaciones HTML interactivas. — tags: diagramas,agent-skills,ai-agents,architecture-diagram,claude-code,claude-skills,codex,coding-agents — tools: claude-code,codex
- `docling` [L|loc|E|~] — Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. — tags: docs,pdf,ocr,python — alt: marker,mineru,unstructured,olmocr
- `marker` [L|loc|E|~] — Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. — tags: docs,pdf,python — alt: docling,mineru
- `markitdown` [L|loc|E|~] — Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, a — tags: docs,python
- `marp` [A|loc|E|~] — Ecosistema para crear presentaciones con Markdown simple y exportarlas a PDF, PPTX o HTML. — tags: slides,typescript — alt: slidev,reveal.js
- `mermaid` [L|loc|E|~] — Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown. — tags: docs,dataviz,typescript — alt: excalidraw
- `mineru` [A|loc|M|~] — Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. — tags: docs,pdf,ocr,python — alt: docling,marker
- `ocrmypdf` [A|loc|E|~] — Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. — tags: ocr,pdf,python
- `olmocr` [A|loc|H|~] — Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. — tags: ocr,pdf,python — prov: local — alt: paddleocr,docling,unlimited-ocr
- `paddleocr` [L|loc|M|~] — Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. — tags: ocr,docs,python — alt: tesseract,olmocr,unlimited-ocr
- `pandoc` [A|loc|E|?] — Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos. — tags: docs
- `pdf-inspector` [L|loc|E|?] — Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas. — tags: pdf,docs,rust
- `pdfcraft` [A|loc|E|?] — Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y co — tags: pdf,typescript — alt: stirling-pdf
- `pdfding` [A|loc|E|~] — Gestor y visor de PDFs auto-hospedado, ligero, con etiquetas y progreso de lectura. — tags: pdf,docker
- `pdfmathtranslate` [A|hyb|E|~] — Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe. — tags: pdf,docs,python — prov: openai,google,local
- `ppt-master` [R|hyb|E|~] — Generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas pa — tags: slides,python — alt: presenton
- `presenton` [A|hyb|E|~] — Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. — tags: slides,agents,typescript — prov: openai,google,local — alt: ppt-master
- `reveal.js` [L|loc|E|~] — Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orad — tags: slides,javascript — alt: slidev,marp
- `slidev` [A|loc|E|~] — Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. — tags: slides,typescript — alt: marp,reveal.js
- `stirling-pdf` [A|loc|E|~] — Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. — tags: pdf,docker — alt: pdfcraft
- `tesseract` [A|loc|E|?] — Motor de OCR open source clásico, con más de 100 idiomas. — tags: ocr,cpp — alt: paddleocr
- `unlimited-ocr` [L|loc|H|~] — Modelo de Baidu para parsear documentos largos de una sola pasada con visión. — tags: ocr,docs,python — alt: olmocr,paddleocr
- `unstructured` [L|hyb|M|~] — ETL open source que transforma documentos complejos en datos estructurados para LLM. — tags: docs,data,python — alt: docling
- `youtube2webpage` [L|loc|E|?] — Script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripció — tags: docs,javascript

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
