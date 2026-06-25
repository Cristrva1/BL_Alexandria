# REPO_MENU — Menú portable de la biblioteca de repositorios

> Generado: 2026-06-25 · 177 repos curados · Documento 100% para IA.
> COPIA esta carpeta (`menu_portable/`) a la raíz de tu proyecto y
> referencia este archivo desde tu AGENTS.md / system prompt.

---

## INSTRUCCIONES PARA EL AGENTE (léeme entero, soy corto)

Eres un agente que debe elegir qué repositorios instalar/usar para un
proyecto concreto. Tienes un menú curado de **177 repos** de IA y
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
| claude-code | `claude-plugins-official`, `awesome-claude-code`, `superpowers`, `skills`, `agent-toolkit`, `n8n-skills`, `geo-seo-claude`, `agency-agents` |
| antigravity | `antigravity-awesome-skills`, `awesome-agent-skills`, `prompt-master` |
| codex | `antigravity-awesome-skills`, `awesome-agent-skills`, `marketingskills`, `taste-skill` |
| grok | Sin repos específicos; úsalo como proveedor LLM en runtime. |
| deepseek | `deepseek-coder` |

## Recetas (stacks end-to-end listos)

Si el proyecto es un PRODUCTO (no una pieza suelta), parte de una
receta y ajusta. Cada receta lista los repos en orden de uso.

### Bot de WhatsApp con IA
**Meta:** atención/ventas automatizada por WhatsApp con un agente LLM.  
**Stack:** `evolution-api` → `n8n` → `n8n-mcp` → `n8n-skills` → `chatwoot` → `novu`
**Cómo:** evolution-api recibe/envía mensajes vía webhook; n8n enruta y llama al LLM; chatwoot centraliza cuando entra un agente humano.

### Pipeline de Reels / video corto
**Meta:** convertir contenido en video corto con voz y subtítulos.  
**Stack:** `whisperx` → `supertonic` → `tts` → `comfyui` → `fooocus` → `real-esrgan` → `moviepy` → `remotion` → `lossless-cut`
**Cómo:** [videofy_minimal](#-videofy_minimal) puede orquestar el flujo simple; remotion/moviepy escalan a variantes programáticas.

### Agente de research profundo
**Meta:** investigación citada y estructurada a partir de la web.  
**Stack:** `gpt-researcher` → `deer-flow` → `firecrawl` → `crawl4ai` → `browser-use` → `markitdown` → `langfuse`

### Workspace privado local soberano
**Meta:** asistente todo-en-uno sin fuga de datos.  
**Stack:** `odysseus` → `open-notebook` → `ecc` → `mem0`

### Análisis de repos grandes
**Meta:** que un asistente entienda una base de código enorme barato.  
**Stack:** `codegraph` → `graphify` → `graphrag` → `gitnexus`

### Marketing de agencia
**Meta:** operar campañas y contenido a escala.  
**Stack:** `marketingskills` → `agency-agents` → `mautic` → `listmonk` → `posthog` → `metabase` → `open-generative-ai`

### Web app moderna con IA
**Meta:** construir frontend pulido rápido.  
**Stack:** `open-design` → `plasmic` → `tailwindcss` → `heroui` → `gsap` → `motion` → `threejs` → `swr` → `echarts` → `uplot`

### Construir una app/servidor MCP
**Meta:** exponer datos o herramientas propias a asistentes.  
**Stack:** `mcp-use` → `mcp` → `servers` → `awesome-mcp-servers`

### Documentos → presentaciones
**Meta:** pasar texto/informes a slides editables.  
**Stack:** `markitdown` → `ppt-master` → `revealjs`

---

## ÍNDICE COMPACTO (1 línea por repo)

Formato: `id` [role|exec|setup|inst] — descripción — alt:…

### Sin categoría

- `tools` [L|loc|M|?] — (ver ficha de tools)

### 1. Automatización, Mensajería & CRM (14)
Detalle: `REPO_MENU_cats/01-automatizaci-n-mensajer-a-crm.md`

- `activepieces` [P|hyb|M|~] — plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flu
- `appsmith` [P|loc|M|~] — Organizations build custom applications like dashboards, admin panels, customer 360, IT automation, and servic
- `budibase` [P|loc|M|~] — AI Agents that run your operations Budibase is an open-source operations platform that saves engineers 100s of
- `chatwoot` [P|loc|H|~] — plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, e
- `evolution-api` [P|loc|H|~] — API REST robusta que actúa como middleware para automatizar WhatsApp y mensajería multicanal, exponiendo el en
- `huginn` [P|loc|M|~] — sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como u
- `listmonk` [P|loc|M|?] — gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depe — alt: mautic
- `mautic` [P|loc|H|?] — plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites com — alt: listmonk
- `n8n` [P|loc|M|~] — plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un
- `n8n-io` [P|loc|M|~] — copia local del repositorio oficial de n8n (mismo proyecto que [n8n](#-n8n)), mantenida como referencia o espe — alt: n8n
- `novu` [P|hyb|M|~] — infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y ch — alt: listmonk
- `openwa` [L|loc|E|~] — gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraes
- `twenty-main` [P|hyb|H|~] — CRM open-source orientado a desarrolladores, alternativa moderna y personalizable a Salesforce/HubSpot que mod
- `whatsapp-agentkit` [S|hyb|E|+] — plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de pr

### 2. Skills, Prompts & Guías de Agente (22)
Detalle: `REPO_MENU_cats/02-skills-prompts-gu-as-de-agente.md`

- `agency-agents` [S|cld|M|+] — conjunto de playbooks y agentes especializados (incluye un Digital Marketing Pro) diseñados para operar una ag
- `agent-toolkit` [S|cld|E|+] — conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documen — alt: superpowers
- `agents-towards-production` [D|cld|M|+] — playbook open-source con tutoriales end-to-end para llevar agentes GenAI de prototipo a producto real, cubrien
- `andrej-karpathy-skills` [S|cld|E|+] — guía de 4 principios (inspirada en las ideas de Andrej Karpathy sobre asistentes de código) que define cómo de
- `antigravity-awesome-skills` [D|cld|E|+] — catálogo masivo con más de 1.678 habilidades (`SKILL.md`) categorizadas por dominio (desarrollo, QA, DevOps, s — alt: awesome-agent-skills
- `awesome-agent-skills` [D|cld|E|+] — colección curada de habilidades oficiales y comunitarias publicadas por marcas líderes (Anthropic, Google, Str
- `awesome-claude-code` [D|cld|E|+] — lista "awesome" curada de scripts, agentes, hooks, slash commands y extensiones específicos del ecosistema de 
- `claude-plugins-official` [D|cld|E|+] — plugins y extensiones oficiales para Claude, distribuidos junto al repositorio de Claude Code de Anthropic.
- `context-engineering` [D|cld|E|+] — guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la informaci
- `geo-seo-claude` [S|cld|E|+] — skill GEO-first con soporte SEO clásico para optimizar la visibilidad de sitios ante motores de búsqueda con I
- `guia` [S|hyb|H|+] — Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, eleg
- `humanizer` [S|cld|E|+] — skill para Claude Code/OpenCode que elimina las señales típicas ("tells") de la escritura generada por IA para
- `marketingskills` [S|cld|E|+] — colección de skills de marketing que cubren conversión, copywriting, SEO, analítica y growth para usar con age
- `n8n-skills` [S|cld|E|+] — conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando 
- `prompt-master` [S|cld|E|+] — skill que ayuda a redactar prompts precisos para cualquier herramienta de IA, buscando el mejor resultado sin 
- `skills` [D|cld|E|+] — colección de skills de referencia mantenida por el proyecto aihero.dev / Total TypeScript, pensada como ejempl
- `skills-emil` [S|cld|E|+] — colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrolla
- `skillspector` [S|cld|E|+] — herramienta para auditar la seguridad de skills y detectar patrones potencialmente riesgosos antes de instalar
- `stop-slop` [S|cld|E|+] — skill que enseña al modelo a eliminar patrones y "tells" de la prosa generada por IA, mejorando ritmo y estilo — alt: humanizer
- `superpowers` [S|cld|E|+] — metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseg
- `taste-skill` [S|cld|E|+] — skills "anti-slop" para producir frontends premium (layout, tipografía, motion) más skills de generación de im
- `ui-ux-pro-max-skill` [S|cld|E|+] — habilidades que dotan al asistente de inteligencia de diseño UI/UX y estilos avanzados para producir interface

### 3. Frameworks & Orquestación de Agentes (23)
Detalle: `REPO_MENU_cats/03-frameworks-orquestaci-n-de-agentes.md`

- `ag2` [L|cld|M|~] — framework maduro para sistemas multiagente con patrones de colaboración (heredero de AutoGen). Modela conversa
- `autogen` [R|loc|M|~] — AutoGen ![Maintenance Mode](https://github.com/microsoft/agent-framework).
- `autoresearch` [P|hyb|M|~] — enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. Proy — alt: gpt-researcher
- `awesome-langgraph` [D|cld|E|+] — repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. Es una lista curada, no
- `crewai` [L|cld|E|~] — framework para orquestar "crews" de agentes con roles y tareas. Cada agente recibe un rol y objetivo, y el equ
- `deer-flow` [P|hyb|M|~] — super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. Coordina tareas
- `defending-code-reference-harness` [L|hyb|M|~] — A reference implementation for autonomous vulnerability discovery and remediation with Claude, based on our le
- `dify` [P|hyb|M|~] — plataforma integral para construir apps de IA con backend y UI listos. Combina orquestación de prompts, RAG, a
- `flowise` [A|hyb|E|~] — builder visual drag-and-drop para pipelines LLM. Permite montar chatflows y agentes conectando nodos y exponer — alt: dify
- `gpt-researcher` [P|hyb|M|~] — agente autónomo que investiga en línea y consolida reportes citados y estructurados. Planifica sub-preguntas, 
- `guardrails` [P|loc|M|~] — LATEST RELEASE / DEVELOPMENT VERSION**: The [develop](https://github.com/NVIDIA-NeMo/Guardrails/tree/develop) 
- `hermes-agent` [A|loc|M|~] — entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. Ofrece un panel de control de e
- `langchain` [L|cld|M|~] — framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). Ofrece abstraccione
- `langflow` [A|hyb|M|~] — constructor visual de flujos LLM/agentes construido sobre LangChain. Permite arrastrar y conectar componentes 
- `llm-council` [P|hyb|M|~] — "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. Cada modelo aporta una respuesta y
- `mirofish` [P|hyb|H|~] — motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar 
- `multica` [P|hyb|M|?] — plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas")
- `nemo-agent-toolkit` [L|hyb|H|~] — toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). Aporta componentes para conectar, eva
- `openevolve` [R|cld|H|+] — agente de codificación evolutivo que optimiza algoritmos por simulación genética. Genera, evalúa y muta candid
- `openhands` [P|hyb|M|~] — plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). El agente puede l
- `repomix` [L|loc|E|~] — Need discussion? Join us on <a href="https://discord.gg/wNYzTwZFku">Discord</a>!<br>.
- `ruflo` [P|hyb|H|?] — harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude
- `tooljet` [A|hyb|M|~] — :star: If you find ToolJet useful, please consider giving us a star on GitHub! Your support helps us continue 

### 4. Scraping, Búsqueda & Research Web (16)
Detalle: `REPO_MENU_cats/04-scraping-b-squeda-research-web.md`

- `archivebox` [P|hyb|M|~] — ▶️ <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Quickstart">Quickstart</a> | <a href="https://demo.a
- `browser-use` [L|hyb|M|~] — biblioteca que da a los LLMs la capacidad de usar navegadores reales con interfaz para modelos de visión, deja — alt: playwright
- `crawl4ai` [L|loc|M|~] — librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pen — alt: firecrawl
- `crawlee` [L|loc|M|~] — framework moderno de crawling para Node.js con antibloqueo integrado, unifico scraping de HTTP y de navegador  — alt: crawlee-python
- `crawlee-python` [L|loc|M|~] — versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosist
- `firecrawl` [P|cld|M|+] — plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio
- `instaloader` [L|loc|E|~] — herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles,  — alt: snscrape
- `llm-scraper` [L|hyb|E|~] — librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el — alt: scrapegraph-ai
- `normalize.css` [L|loc|E|~] — src="https://necolas.github.io/normalize.css/logo.svg" alt="Normalize Logo" width="80" height="80" align="righ
- `playwright` [L|hyb|M|~] — framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola A — alt: browser-use
- `playwright-cli` [S|hyb|E|+] — interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador 
- `scrapegraph-ai` [L|hyb|M|~] — framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué e — alt: llm-scraper
- `scrapely` [L|loc|E|~] — librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mis
- `scrapling` [L|loc|M|~] — librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica 
- `scrapy` [L|loc|M|~] — framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesam
- `snscrape` [L|loc|E|~] — scraper de redes sociales (Twitter/X, Reddit, Telegram, etc.) que recolecta posts y perfiles sin necesidad de  — alt: instaloader

### 5. MCP & Conectividad (9)
Detalle: `REPO_MENU_cats/05-mcp-conectividad.md`

- `awesome-mcp-clients` [D|hyb|M|+] — A curated list of awesome Model Context Protocol (MCP) clients.
- `awesome-mcp-servers` [D|hyb|E|+] — directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos 
- `github-mcp-server` [P|loc|M|~] — The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and c
- `mcp` [L|hyb|M|~] — núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA intero — alt: mcp-use
- `mcp-neo4j` [R|hyb|M|~] — conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con sopo
- `mcp-use` [L|hyb|M|~] — framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de
- `n8n-mcp` [R|hyb|M|~] — servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n para ayudar a
- `public-apis` [D|cld|E|+] — directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyect
- `servers` [D|hyb|M|+] — colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enl

### 6. Memoria, LLM Ops & Observabilidad (10)
Detalle: `REPO_MENU_cats/06-memoria-llm-ops-observabilidad.md`

- `agentmemory` [L|hyb|E|?] — memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini, Codex…), construida sobr
- `headroom` [L|hyb|E|~] — utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder 
- `langfuse` [P|hyb|M|~] — plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llama
- `litellm` [L|hyb|E|~] — gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato d
- `llmfit` [L|hyb|E|~] — herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar mod
- `loguru` [L|loc|E|~] — librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin 
- `mem0` [L|hyb|E|~] — capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y — alt: mempalace
- `mempalace` [L|loc|E|~] — memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin envia
- `sandbox` [P|hyb|M|~] — entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un m
- `turbovec` [L|loc|E|~] — librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación 

### 7. Inteligencia de Código, Datos & Entrenamiento (14)
Detalle: `REPO_MENU_cats/07-inteligencia-de-c-digo-datos-entrenamiento.md`

- `awesome-bigdata` [D|cld|E|+] — directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para des
- `codegraph` [R|loc|E|~] — CLI que indexa tu código y da a los asistentes de IA inteligencia semántica 100% local, permitiéndoles entende
- `cosmos` [R|hyb|H|~] — plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos
- `data-science-ipython-notebooks` [D|loc|E|+] — gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep l
- `deepseek-coder` [R|hyb|H|~] — familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para 
- `gitnexus` [A|hyb|E|?] — herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar  — alt: codegraph
- `graphify` [R|hyb|M|~] — generador de grafos de conocimiento para proyectos locales que mapea código, PDFs, imágenes y video en diagram — alt: codegraph
- `graphrag` [L|hyb|M|~] — sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lu
- `how-to-train-your-gpt` [D|loc|E|+] — guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librerí — alt: nanogpt
- `llm.c` [A|cld|H|+] — LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython. Current focus is on pretrai
- `llmc` [L|loc|H|?] — implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados,  — alt: nanogpt
- `nanochat` [L|loc|M|~] — pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde e — alt: nanogpt
- `nanogpt` [L|loc|M|~] — implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quep
- `openai-python` [L|cld|E|~] — SDK oficial de OpenAI para Python, que expone de forma tipada y cómoda la API (chat, embeddings, imágenes, aud — alt: litellm

### 8. Workspaces de IA Local & Notebooks (5)
Detalle: `REPO_MENU_cats/08-workspaces-de-ia-local-notebooks.md`

- `ecc` [P|loc|H|~] — sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendim
- `notebooklm-mcp-cli` [R|cld|E|+] — CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde termi — alt: notebooklm-py
- `notebooklm-py` [L|cld|E|~] — API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuen — alt: open-notebook
- `odysseus` [P|loc|H|~] — workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por age
- `open-notebook` [A|loc|M|~] — clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y ge — alt: notebooklm-py

### 9. Diseño, UI & Frontend (20)
Detalle: `REPO_MENU_cats/09-dise-o-ui-frontend.md`

- `design.md` [D|loc|M|+] — A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent,
- `designmd` [S|cld|E|+] — especificación de formato para describir una identidad visual a agentes de código (tokens YAML + prosa), de mo
- `gradio` [S|hyb|M|+] — English | [中文](readme_files/zh-cn#readme).
- `gsap` [L|loc|M|~] — librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincro — alt: motion
- `heroui` [L|loc|E|~] — librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, da
- `impeccable` [S|cld|E|+] — guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" d
- `magicui` [L|loc|E|~] — librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces mod — alt: heroui
- `motion` [L|loc|E|~] — librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteraccio — alt: gsap
- `nemotron` [A|hyb|H|~] — Open and efficient models for agentic AI.** Training recipes, deployment guides, and use-case examples for the
- `normalizecss` [L|loc|E|?] — hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme.
- `open-design` [A|hyb|M|~] — editor/workspace de diseño colaborativo asistido por IA que genera, maqueta y anima interfaces a partir de ins — alt: plasmic
- `penpot` [A|loc|H|~] — plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que qui — alt: open-design
- `plasmic` [A|hyb|M|~] — builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin per — alt: open-design
- `react-three-fiber` [L|loc|M|~] — renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos. — alt: threejs
- `swr` [L|loc|E|~] — librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los reva
- `tailwindcss` [L|loc|E|~] — framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directame
- `three.js` [L|loc|H|~] — JavaScript 3D library.
- `threejs` [L|loc|M|~] — motor 3D (WebGL) para renderizar gráficos y escenas interactivas directamente en el navegador.
- `ui` [P|loc|M|~] — A set of beautifully designed components that you can customize, extend, and build on. Start here then make it
- `ui-shadcn` [L|loc|E|~] — colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de in — alt: heroui

### 10. Analítica & Visualización (7)
Detalle: `REPO_MENU_cats/10-anal-tica-visualizaci-n.md`

- `awesome-dataviz` [D|cld|E|+] — directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad
- `dash` [L|loc|M|~] — framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con compone — alt: streamlit
- `echarts` [L|loc|M|~] — librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gr — alt: uplot
- `metabase` [P|hyb|M|?] — herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos  — alt: posthog
- `posthog` [P|hyb|H|~] — plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session re — alt: metabase
- `streamlit` [L|loc|E|~] — framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin t — alt: dash
- `uplot` [L|loc|E|~] — librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penaliz — alt: echarts

### 11. Generación de Imagen & Visión (16)
Detalle: `REPO_MENU_cats/11-generaci-n-de-imagen-visi-n.md`

- `comfyui` [R|loc|H|~] — motor local modular para crear pipelines visuales de generación con IA mediante un grafo de nodos, donde cada  — alt: fooocus
- `comfyui-ipadapter-plus` [R|loc|H|~] — conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una imagen 
- `controlnet` [R|loc|H|~] — método y modelos para condicionar la generación text-to-image con señales externas como poses, bordes, profund — alt: sd-webui-controlnet
- `deep-live-cam` [R|loc|H|~] — herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video con
- `diffusers` [L|loc|H|~] — librería de Hugging Face para construir y ejecutar pipelines de modelos de difusión (imagen, video, audio) des — alt: fooocus
- `face-recognition` [L|loc|M|~] — librería de Python sencilla para detección y reconocimiento facial, con una API de alto nivel para localizar, 
- `fluxer` [P|hyb|M|?] — plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop;
- `fooocus` [A|loc|M|~] — herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, oc — alt: comfyui
- `gfpgan` [R|loc|M|~] — algoritmo de restauración facial que reconstruye rostros degradados o de baja calidad usando priors generativo — alt: real-esrgan
- `invokeai` [A|loc|H|~] — suite profesional y unificada para Stable Diffusion que combina una UI pulida con canvas, capas, inpainting y  — alt: fooocus
- `liveportrait` [R|loc|H|~] — sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia — alt: deep-live-cam
- `nemo` [R|loc|M|~] — Checkout our [HuggingFace🤗 collection](https://huggingface.co/collections/nvidia/nemotron-speech) for the late
- `open-generative-ai` [P|hyb|M|~] — plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos acc — alt: comfyui
- `real-esrgan` [R|loc|M|~] — herramienta de superresolución y restauración para imágenes reales que reescala y limpia material de baja cali — alt: gfpgan
- `sd-webui-controlnet` [R|loc|H|~] — extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI, con preproc
- `stable-diffusion-webui` [A|loc|H|~] — interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpaintin — alt: invokeai

### 12. Audio, Voz & Video (15)
Detalle: `REPO_MENU_cats/12-audio-voz-video.md`

- `faster-whisper` [R|loc|M|~] — reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria,  — alt: whisperx
- `hyperframes` [L|loc|M|~] — framework npm para generar animaciones frame a frame de forma programática desde código. — alt: remotion
- `lossless-cut` [A|loc|E|~] — aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la cal — alt: moviepy
- `moviepy` [L|loc|E|~] — librería Python para edición de video programática: cortar, concatenar, superponer texto, subtítulos y audio,  — alt: remotion
- `omnivoice-studio` [A|loc|M|~] — suite de voz de escritorio open-source planteada como alternativa a ElevenLabs, con dictado en tiempo real, cl — alt: tts
- `opencut` [A|hyb|M|?] — editor de video open-source con UI moderna, planteado como alternativa libre tipo CapCut, usable en web o escr — alt: moviepy
- `openscreen` [A|hyb|E|?] — herramienta ligera de grabación de pantalla para screencasts y demos; el proyecto original está archivado y co
- `remotion` [L|loc|M|~] — framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a — alt: moviepy
- `supertonic` [R|loc|M|~] — motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en e — alt: voxcpm
- `tts` [L|loc|M|~] — toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y  — alt: supertonic
- `videofy-minimal` [A|loc|E|~] — herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pi — alt: remotion
- `voxcpm` [R|loc|H|~] — sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y  — alt: supertonic
- `whisper` [R|loc|M|~] — modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que tran — alt: faster-whisper
- `whisperx` [R|loc|M|~] — extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para s — alt: whisper
- `youtube2webpage` [L|loc|E|?] — script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripció

### 13. Documentos & Presentaciones (5)
Detalle: `REPO_MENU_cats/13-documentos-presentaciones.md`

- `markitdown` [L|loc|E|~] — utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, a
- `pdfcraft` [A|loc|E|?] — conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y co — alt: markitdown
- `ppt-master` [R|hyb|E|~] — generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas pa — alt: revealjs
- `reveal.js` [R|hyb|M|~] — reveal.js is an open source HTML presentation framework. It enables anyone with a web browser to create beauti
- `revealjs` [L|loc|E|~] — framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orad — alt: ppt-master

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
