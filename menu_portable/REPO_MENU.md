# REPO_MENU — Menú portable de la biblioteca de repositorios

> Generado: 2026-08-24 · 212 repos curados · Documento 100% para IA.
> COPIA esta carpeta (`menu_portable/`) a la raíz de tu proyecto y
> referencia este archivo desde tu AGENTS.md / system prompt.

---

## INSTRUCCIONES PARA EL AGENTE (léeme entero, soy corto)

Eres un agente que debe elegir qué repositorios instalar/usar para un
proyecto concreto. Tienes un menú curado de **212 repos** de IA y
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

- `cli` [A|loc|E|~] — gh es la CLI oficial de GitHub. No es un agente; es la herramienta de git/GitHub que el resto del flujo asume 
- `tools` [L|loc|M|?] — Carpeta de herramientas auxiliares del hub, no un repositorio de producto. Sirve como referencia interna, no c

### 1. Automatización, Mensajería & CRM (17)
Detalle: `REPO_MENU_cats/01-automatizaci-n-mensajer-a-crm.md`

- `activepieces` [R|hyb|M|~] — Activepieces es un reemplazo open source de Zapier: orquestas automatizaciones con piezas auto-hospedables y u — alt: n8n
- `appsmith` [P|loc|M|~] — Organizations build custom applications like dashboards, admin panels, customer 360, IT automation, and servic
- `browser-use` [P|loc|M|~] — 🌤️ Want to skip the setup? Use our cloud for faster, scalable, stealth-enabled browser automation!.
- `budibase` [P|loc|M|~] — AI Agents that run your operations Budibase is an open-source operations platform that saves engineers 100s of
- `chatwoot` [L|hyb|M|~] — The modern customer support platform, an open-source alternative to Intercom, Zendesk, Salesforce Service Clou
- `evolution-api` [A|hyb|M|~] — Open-source REST API for WhatsApp and multi-channel messaging — part of the Evolution Foundation ecosystem.
- `huginn` [D|hyb|M|+] — Huginn is a system for building agents that perform automated tasks for you online. They can read the web, wat
- `listmonk` [D|hyb|M|+] — listmonk is a standalone, self-hosted, newsletter and mailing list manager. It is fast, feature-rich, and pack
- `mautic` [P|loc|M|~] — Open Source Marketing Automation Software.
- `n8n` [P|loc|M|~] — n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no- — alt: activepieces,huginn
- `n8n-io` [P|loc|M|~] — n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-
- `n8n-mcp` [P|loc|M|~] — A Model Context Protocol (MCP) server that provides AI assistants with comprehensive access to n8n node docume
- `novu` [L|hyb|M|~] — The open-source communication infrastructure for agents and products.
- `openevolve` [L|loc|M|~] — 🧬 The most advanced open-source evolutionary coding agent.
- `openwa` [P|hyb|M|~] — OpenWA is a free, open-source WhatsApp API Gateway designed for developers who need full control over their me
- `twenty-main` [R|loc|M|~] — Twenty gives technical teams the building blocks for a custom CRM that meets complex business needs and quickl
- `whatsapp-agentkit` [D|cld|M|+] — Construye tu propio agente de WhatsApp con inteligencia artificial en menos de 30 minutos. No necesitas saber 

### 2. Skills, Prompts & Guías de Agente (30)
Detalle: `REPO_MENU_cats/02-skills-prompts-gu-as-de-agente.md`

- `agent-toolkit` [S|loc|M|+] — Opinionated skills shared by @leonardocouy for improving daily work efficiency with Claude Code. Skills are pa
- `andrej-karpathy-skills` [S|hyb|M|+] — > Check out my new project Multica — an open-source platform for running and managing coding agents with reusa
- `antigravity-awesome-skills` [S|loc|E|+] — 🌌 Antigravity Awesome Skills: 1,682+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More.
- `arcads-claude-code` [S|loc|M|+] — Plugin de skills que conecta un coding agent con Arcads para piezas creativas (video e imagen). Requiere cuent
- `autoresearch` [P|loc|H|~] — One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun,
- `awesome-agent-skills` [S|cld|H|+] — Directorio de agent skills revisado a mano. Úsalo para elegir piezas concretas; no instales el catálogo entero
- `browser-harness` [S|loc|M|+] — Connect an LLM directly to your real browser with a thin, editable CDP harness. For browser tasks where you ne
- `context-engineering` [R|loc|M|~] — > "Context engineering is the delicate art and science of filling the context window with just the right infor
- `geo-seo-claude` [S|hyb|M|+] — (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) while maintaining traditional SEO foundations.
- `guia` [S|hyb|H|+] — Catálogo operativo de los 156 repositorios locales del workspace, diseñado para entender, comparar, elegir y c
- `hermes-agent` [S|loc|M|+] — The self-improving AI agent built by Nous Research. It's the only agent with a built-in learning loop — it cre
- `humanizer` [S|loc|M|+] — A skill for Claude Code and OpenCode that removes signs of AI-generated writing from text, making it sound mor
- `last30days-skill` [S|hyb|M|+] — An AI agent-led search engine scored by upvotes, likes, and real money - not editors..
- `llm-council` [P|cld|M|+] — The idea of this repo is that instead of asking a question to your favorite LLM provider (e.g. OpenAI GPT 5.1,
- `marketingskills` [S|cld|H|+] — A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who wan
- `multica` [S|loc|M|+] — The open-source managed agents platform.
- `n8n-skills` [S|hyb|M|+] — Paquete de skills para construir flujos n8n con un agente. Combínalo con n8n y n8n-mcp; no sustituye la instan
- `nanogpt` [L|cld|H|~] — Update Nov 2025 nanoGPT has a new and improved cousin called nanochat. It is very likely you meant to use/find
- `notebooklm-py` [S|hyb|M|+] — A Comprehensive NotebookLM Skill & Unofficial Python API. Full programmatic access to NotebookLM's features—in
- `open-generative-ai` [S|hyb|H|+] — The free, open-source alternative to AI Video Platforms. Generate AI images and videos using 200+ state-of-the
- `openmontage` [S|loc|H|+] — Turn your AI coding assistant into a full video production studio. Describe what you want in plain language — 
- `playwright-cli` [S|loc|E|+] — Playwright CLI empaquetado con skills de agente: permite manejar Chromium/Firefox/WebKit en scripts y en flujo
- `prompt-master` [S|hyb|H|+] — A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context a
- `skills-remotion` [S|loc|M|+] — This is an internal package and has no documentation.
- `skillspector` [S|loc|M|+] — Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks before in
- `stitch-sdk` [S|hyb|M|+] — Generate UI screens from text prompts and extract their HTML and screenshots programmatically.
- `stop-slop` [S|hyb|M|+] — A skill for removing AI tells from prose.
- `superpowers` [S|loc|M|+] — Superpowers is a complete software development methodology for your coding agents, built on top of a set of co
- `taste-skill` [S|loc|M|+] — taste-skill corrige interfaces generadas por agentes: jerarquía visual, tipo, movimiento y espacio. No es un k
- `ui-ux-pro-max-skill` [S|loc|M|+] — An AI skill that provides design intelligence for building professional UI/UX across multiple platforms and fr

### 3. Frameworks & Orquestación de Agentes (47)
Detalle: `REPO_MENU_cats/03-frameworks-orquestaci-n-de-agentes.md`

- `ag2` [P|hyb|M|~] — AG2 was evolved from AutoGen. Fully open-sourced. We invite collaborators from all organizations to contribute
- `agent-protocol` [D|hyb|M|+] — Agent Protocol intenta estandarizar cómo se expone un agente (run, I/O, estado) sin atarse a un framework. Es 
- `agent-reach` [R|hyb|M|~] — Agent-Reach estabiliza cómo un agente se conecta a proveedores LLM. La idea es que el canal de acceso pueda ca
- `agents-towards-production` [S|hyb|H|+] — The open-source playbook for turning AI agents into real-world products.
- `autogen` [R|loc|M|~] — AutoGen orquesta conversaciones entre agentes LLM. Está en mantenimiento; para trabajo nuevo revisa el sucesor
- `awesome-claude-code` [S|cld|M|+] — The old ways have come and gone. It's time to embrace the next phase. The previous Table of Contents was no lo
- `awesome-dataviz` [D|loc|M|+] — A curated list of awesome open-source data visualizations frameworks, libraries and software. Inspired by awes
- `awesome-langgraph` [D|loc|M|+] — 🦜🕸️ Awesome LangGraph & LangChain Ecosystem !Awesome !Last Updated.
- `awesome-mcp-servers` [D|loc|H|+] — A curated list of awesome Model Context Protocol (MCP) servers.
- `codebase-memory-mcp` [R|hyb|M|~] — The fastest and most efficient code intelligence engine for AI coding agents. Full-indexes an average reposito
- `computer-use-preview` [L|cld|M|~] — Preview de Gemini Computer Use: el modelo ve la pantalla y opera UI. Requiere API de Google y no es un agente 
- `crewai` [R|hyb|M|~] — Fast and Flexible Multi-Agent Automation Framework.
- `dash` [P|loc|M|~] — Dash is the most downloaded, trusted Python framework for building ML & data science web apps*.
- `deepagents` [L|loc|M|~] — Deep Agents is an open source agent harness — an opinionated agent that runs out of the box. Extend, override,
- `deeptutor` [A|hyb|M|~] — DeepTutor es un sistema de tutoría con agentes para aprendizaje continuo. Encaja como producto educativo, no c
- `deer-flow` [S|hyb|M|+] — > On February 28th, 2026, DeerFlow claimed the 🏆 #1 spot on GitHub Trending following the launch of version 2.
- `defending-code-reference-harness` [L|hyb|M|~] — A reference implementation for autonomous vulnerability discovery and remediation with Claude, based on our le
- `dify` [P|hyb|M|~] — Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipelin
- `ecc` [A|hyb|M|~] — Official sources only. Install ECC only from verified channels: the GitHub repository github.com/affaan-m/ECC,
- `flowise` [P|loc|M|~] — Flowise es un constructor visual de cadenas y agentes LLM. Encaja si quieres prototipar orquestación con nodos
- `gpt-researcher` [S|hyb|M|+] — GPT Researcher the first open deep research agent designed for both web and local research on any given task.
- `guardrails` [P|loc|M|~] — > LATEST RELEASE / DEVELOPMENT VERSION: The develop branch tracks the latest top of tree development. The late
- `headroom` [P|loc|M|~] — 60–95% fewer tokens · library · proxy · MCP · 6 algorithms · local-first · reversible.
- `hyperframes` [S|hyb|M|+] — HyperFrames is an open-source framework for turning HTML, CSS, media, and seekable animations into determinist
- `langchain` [R|loc|M|~] — LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interop
- `langflow` [P|hyb|M|~] — Langflow is a powerful platform for building and deploying AI-powered agents and workflows. It provides develo
- `langfuse` [P|loc|M|~] — Langfuse uses GitHub Discussions for Support and Feature Requests.
- `langgraph-supervisor-py` [R|loc|M|~] — > Note: We now recommend using the supervisor pattern directly via tools rather than this library for most use
- `langgraphjs` [R|loc|M|~] — Implementación TypeScript de LangGraph. Sirve para construir, gestionar y desplegar agentes de larga duración 
- `loop-engineering` [S|loc|M|+] — > Stop prompting. Design the loop. Get a score.
- `mcp-use` [P|hyb|M|~] — to build MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.
- `mercury-agent` [S|loc|M|+] — Remembers what matters. Asks before it acts. Runs 24/7 from CLI, Telegram, or Web. 31 built-in tools, Kanban b
- `nemo-agent-toolkit` [D|loc|M|+] — NVIDIA NeMo Agent Toolkit adds intelligence to AI agents across any framework—enhancing speed, accuracy, and d
- `nemoclaw` [S|loc|M|+] — NVIDIA NemoClaw is an open source reference stack for running supported AI agents more safely inside NVIDIA Op
- `open-swe` [P|loc|M|~] — Elite engineering orgs like Stripe, Ramp, and Coinbase are building their own internal coding agents — Slackbo
- `openclaw` [L|loc|M|~] — OpenClaw is a personal AI assistant that runs on your devices and meets you in the channels you already use. I
- `openhands` [P|hyb|M|~] — Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backend
- `openscreen` [P|hyb|M|~] — This started as a side project that blew up; not production grade and you'll hit bugs, but hopefully it covers
- `playwright` [R|hyb|E|~] — Playwright is a framework for web automation and testing. It drives Chromium, Firefox, and WebKit with a singl
- `ponytail` [L|hyb|M|~] — You know him. Long ponytail. Oval glasses. Has been at the company longer than the version control. You show h
- `repomix` [L|loc|E|~] — Warp, built for coding with multiple AI agents Available for MacOS, Linux, & Windows.
- `ruflo` [R|loc|M|~] — An agent meta-harness for Claude Code and Codex..
- `sandbox` [L|hyb|M|~] — AIO Sandbox concentra herramientas de ejecución aislada para agentes: filesystem, red y procesos sin dejarlos 
- `scrapling` [L|hyb|M|~] — Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale 
- `t3code` [A|cld|M|+] — T3 Code orquesta los agentes que ya corren en el host desde una UI (iOS, Android, web, Electron). No sustituye
- `tooljet` [A|hyb|M|~] — :star: If you find ToolJet useful, please consider giving us a star on GitHub! Your support helps us continue 
- `turbovec` [D|loc|H|+] — A 10 million document corpus takes 31 GB of RAM as float32. turbovec fits it in 4 GB - and searches it faster 

### 4. Scraping, Búsqueda & Research Web (13)
Detalle: `REPO_MENU_cats/04-scraping-b-squeda-research-web.md`

- `archivebox` [P|hyb|M|~] — ArchiveBox is a self-hosted app that lets you preserve content from websites in a variety of formats.
- `crawl4ai` [A|hyb|M|~] — 🚀 Crawl4AI Cloud API — Closed Beta (Launching Soon) Reliable, large-scale web extraction, now built to be _dra
- `crawlee` [R|hyb|M|~] — Crawlee covers your crawling and scraping end-to-end and helps you build reliable scrapers. Fast..
- `crawlee-python` [L|hyb|M|~] — Crawlee covers your crawling and scraping end-to-end and helps you build reliable scrapers. Fast..
- `firecrawl` [L|loc|M|~] — The API to search, scrape, and interact with the web at scale. 🔥 The web context API to find sources, extract 
- `how-to-train-your-gpt` [R|loc|M|~] — A guide to building a world-class language model from absolute scratch. Taught like you're five. Built like yo
- `instaloader` [L|loc|M|~] — Instaloader es un scraper de Instagram orientado a archivo personal o datasets. No es un navegador agentizado;
- `llm-scraper` [P|cld|E|+] — LLM Scraper is a TypeScript library that allows you to extract structured data from any webpage using LLMs.
- `odysseus` [S|hyb|H|+] — A self-hosted AI workspace for chat, agents, research, documents, email, notes, calendar, and local model work
- `scrapegraph-ai` [P|hyb|M|~] — ScrapeGraphAI convierte una instrucción en un grafo de extracción web. Encaja cuando el HTML es irregular y un
- `scrapely` [L|hyb|E|~] — some example web pages and the data to be extracted, scrapely constructs a parser for all similar pages.
- `scrapy` [L|loc|M|~] — Scrapy es el estándar de crawling en Python: spiders, pipelines y export. Úsalo para extracciones masivas, no 
- `snscrape` [D|loc|M|+] — snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or

### 5. MCP & Conectividad (14)
Detalle: `REPO_MENU_cats/05-mcp-conectividad.md`

- `awesome-mcp-clients` [D|hyb|M|+] — A curated list of awesome Model Context Protocol (MCP) clients.
- `claude-plugins-official` [P|cld|M|+] — A curated directory of high-quality plugins for Claude Code.
- `context7` [R|loc|E|~] — Context7 evita que el modelo alucine APIs viejas: trae docs versionadas al contexto. Instálalo como servidor M
- `davinci-resolve-mcp` [R|hyb|M|~] — DaVinci Resolve MCP expone edición, media pool, render, color y Fusion a asistentes compatibles con Model Cont
- `github-mcp-server` [P|loc|M|~] — The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and c
- `graphify` [L|loc|H|~] — Type /graphify in your AI coding assistant and it maps your entire project — code, docs, PDFs, images, videos 
- `langchain-mcp-adapters` [L|hyb|E|~] — Puente ligero entre servidores MCP y el ecosistema LangChain/LangGraph. Librería, no un servidor MCP en sí.
- `mcp` [D|hyb|M|+] — This repository contains a list of Google's official Model Context Protocol (MCP) servers, guidance on how to 
- `mcp-neo4j` [D|loc|M|+] — These MCP servers are a part of the Neo4j Labs program. They are developed and maintained by the Neo4j Field G
- `metabase` [P|loc|M|~] — The easiest way to get started with Metabase is to sign up for a free trial of Metabase Cloud.
- `notebooklm-mcp-cli` [P|hyb|M|~] — Programmatic access to Google NotebookLM — via command-line interface (CLI) or Model Context Protocol (MCP) se
- `opencut` [P|hyb|M|~] — OpenCut is being rewritten from the ground up. What's coming:.
- `public-apis` [D|hyb|M|+] — The Public APIs repository is manually curated by community members like you and folks working at APILayer. It
- `servers` [D|loc|M|+] — This repository is a collection of *reference implementations* for the Model Context Protocol (MCP), as well a

### 6. Memoria, LLM Ops & Observabilidad (5)
Detalle: `REPO_MENU_cats/06-memoria-llm-ops-observabilidad.md`

- `agentmemory` [R|hyb|M|~] — Your coding agent remembers everything. No more re-explaining. Built on iii engine Persistent memory for Claud
- `engram` [R|hyb|M|~] — Engram da a cualquier agente compatible con MCP una memoria local (o cloud) en un solo binario, sin dependenci
- `loguru` [P|loc|M|~] — Did you ever feel lazy about configuring a logger and used print() instead?... I did, yet logging is fundament
- `mem0` [L|hyb|M|~] — mem0 guarda y recupera hechos de usuario entre sesiones. Úsalo cuando el agente necesita memoria a largo plazo
- `mempalace` [D|hyb|M|+] — Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.

### 7. Inteligencia de Código, Datos & Entrenamiento (10)
Detalle: `REPO_MENU_cats/07-inteligencia-de-c-digo-datos-entrenamiento.md`

- `awesome-bigdata` [D|loc|M|+] — A curated list of awesome big data frameworks, resources and other awesomeness. Inspired by awesome-php, aweso
- `codegraph` [L|loc|M|~] — CodeGraph construye un grafo del codebase para que un agente navegue símbolos y dependencias sin leer el repo 
- `data-science-ipython-notebooks` [D|loc|M|+] — Directorio de notebooks educativos de data science. Es material de referencia, no una librería para importar e
- `deepseek-coder` [L|loc|H|~] — DeepSeek Coder is composed of a series of code language models, each trained from scratch on 2T tokens, with a
- `echarts` [L|loc|E|~] — Apache ECharts is a free, powerful charting and visualization library offering easy ways to add intuitive, int
- `gitnexus` [R|hyb|E|~] — ⚠️ Important Notice: GitNexus has NO official cryptocurrency, token, or coin. Any token/coin using the GitNexu
- `llm.c` [A|cld|H|+] — LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython. Current focus is on pretrai
- `openai-python` [P|hyb|M|~] — The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.9+ application. 
- `swe-bench` [L|loc|M|~] — SWE-bench is a benchmark for evaluating large language models on real world software issues collected from Git
- `timesfm` [L|loc|M|~] — TimesFM predice series temporales con un decoder-only pretrained. Es un modelo de investigación/producción de 

### 8. Workspaces de IA Local & Notebooks (2)
Detalle: `REPO_MENU_cats/08-workspaces-de-ia-local-notebooks.md`

- `hermes-desktop` [A|loc|M|~] — Hermes Desktop envuelve el agente Hermes en una UI nativa. Úsalo si quieres Hermes como aplicación, no solo co
- `open-notebook` [P|hyb|M|~] — An open source, privacy-focused alternative to Google's Notebook LM!.

### 9. Diseño, UI & Frontend (30)
Detalle: `REPO_MENU_cats/09-dise-o-ui-frontend.md`

- `agency-agents` [S|loc|H|+] — A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy inject
- `daily-stock-analysis` [L|hyb|M|~] — 🤖 基于 AI 大模型的 A股/港股/美股/日股/韩股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/Discord/Slack/邮箱.
- `design.md` [D|loc|M|+] — A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent,
- `gradio` [S|hyb|M|+] — Gradio is an open-source Python package that allows you to quickly build a demo or web application for your ma
- `graphrag` [L|loc|H|~] — 👉 Microsoft Research Blog Post 👉 Read the docs 👉 GraphRAG Arxiv.
- `gsap` [R|loc|M|~] — GSAP is a framework-agnostic JavaScript animation library that turns developers into animation superheroes. Bu
- `heroui` [L|loc|M|~] — HeroUI (antes NextUI) entrega componentes React con tema. Elige esto si quieres una lib con actualizaciones; e
- `impeccable` [S|hyb|E|+] — Design guidance for AI coding agents. 1 skill, 23 commands, live browser iteration, and 44 deterministic detec
- `llmfit` [A|loc|H|~] — New: Community Leaderboard — Browse real-world performance data from actual users. Press `b` to see measured t
- `magicui` [R|hyb|M|~] — Visit https://magicui.design/docs to view the documentation.
- `mirofish` [R|hyb|M|~] — A Simple and Universal Swarm Intelligence Engine, Predicting Anything.
- `motion` [L|hyb|H|~] — Motion (antes Framer Motion) anima interfaces web con una API declarativa. Úsala en el frontend, no como motor
- `nanochat` [A|loc|H|~] — nanochat is the simplest experimental harness for training LLMs. It is designed to run on a single GPU node, t
- `nemotron` [A|hyb|H|~] — Open and efficient models for agentic AI. Training recipes, deployment guides, and use-case examples for the N
- `normalize.css` [L|loc|E|~] — normalize.css alinea el render de elementos HTML entre navegadores. Es una base de CSS, no un sistema de diseñ
- `open-design` [R|loc|M|~] — 🔥 Open Design 0.10.0 is here: the all-in-one Agentic design workspace. The whole craft now lives in one window
- `penpot` [P|loc|M|~] — Penpot is the open-source design platform for teams that build digital products at scale.
- `plasmic` [L|loc|M|~] — The open-source visual builder for your codebase. Build beautiful apps and websites incredibly fast. Drag and 
- `posthog` [S|loc|M|+] — PostHog is an all-in-one, open source platform for building successful products.
- `react-three-fiber` [L|loc|M|~] — react-three-fiber is a React renderer for threejs.
- `real-esrgan` [L|loc|H|~] — 🔥 RealESRGANx4plusanime6B for anime images (动漫插图模型). Please see [animemodel].
- `skills` [S|loc|M|+] — My agent skills that I use every day to do real engineering - not vibe coding.
- `skills-emil` [S|loc|M|+] — For designers and engineers to help them build better user interfaces.
- `stitch-skills` [S|loc|M|+] — A collection of agent skills and plugins for Google Stitch, following the Agent Skills open standard. Compatib
- `swr` [L|loc|M|~] — SWR is a React Hooks library for data fetching.
- `tailwindcss` [P|hyb|M|~] — A utility-first CSS framework for rapidly building custom user interfaces.
- `three.js` [L|loc|H|~] — The aim of the project is to create an easy-to-use, lightweight, cross-browser, general-purpose 3D library. Th
- `ui` [P|loc|M|~] — colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de in — alt: heroui
- `vllm` [L|loc|M|~] — Easy, fast, and cheap LLM serving for everyone.
- `youtube2webpage` [L|loc|M|~] — Youtube-to-Webpage is a Perl script to create a webpage from a Youtube video with a transcript generated from 

### 10. Analítica & Visualización (2)
Detalle: `REPO_MENU_cats/10-anal-tica-visualizaci-n.md`

- `streamlit` [P|loc|E|~] — A faster way to build and share data apps.
- `uplot` [L|hyb|M|~] — A small (~50 KB min), fast chart for time series, lines, areas, ohlc & bars _(MIT Licensed)_.

### 11. Generación de Imagen & Visión (18)
Detalle: `REPO_MENU_cats/11-generaci-n-de-imagen-visi-n.md`

- `comfyui` [R|hyb|H|~] — The most powerful and modular AI engine for content creation..
- `comfyui-ipadapter-plus` [L|loc|H|~] — The IPAdapter are very powerful models for image-to-image conditioning. The subject or even just the style of 
- `controlnet` [L|loc|H|~] — ControlNet 1.1 is released. Those new models will be merged to this repo after we make sure that everything is
- `cosmos` [R|loc|H|~] — Colección NVIDIA Cosmos para modelos de mundo y video. Setup pesado: GPU y checkpoints. No es un editor de ima
- `deep-live-cam` [A|hyb|M|~] — Real-time face swap and video deepfake with a single click and only a single image.
- `diffusers` [L|loc|M|~] — Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance
- `face-recognition` [L|loc|M|~] — Recognize and manipulate faces from Python or from the command line with the world's simplest face recognition
- `fooocus` [S|loc|H|+] — Fooocus is an image generating software (based on Gradio ).
- `gfpgan` [L|loc|M|~] — 1. :boom: Updated online demo: . Here is the backup. 1. :boom: Updated online demo: 1. .
- `invokeai` [R|loc|M|~] — Invoke - Professional Creative AI Tools for Visual Media.
- `litellm` [P|hyb|M|~] — LiteLLM is an open source AI Gateway that gives you a single, unified interface to call 100+ LLM providers — O
- `liveportrait` [L|loc|H|~] — `2025/06/01`: 🌍 Over the past year, LivePortrait has 🚀 become an efficient portrait-animation (humans, cats an
- `luxtts` [D|loc|H|+] — LuxTTS is an lightweight zipvoice based text-to-speech model designed for high quality voice cloning and reali
- `nemo` [R|loc|M|~] — Checkout our HuggingFace🤗 collection for the latest open weight checkpoints and demos!.
- `sd-webui-controlnet` [L|loc|M|~] — The WebUI extension for ControlNet and other injection-based SD controls.
- `stable-diffusion-webui` [S|loc|M|+] — A web interface for Stable Diffusion, implemented using Gradio library.
- `tts` [L|loc|H|~] — 📣 ⓍTTSv2 is here with 16 languages and better performance across the board. 📣 ⓍTTS fine-tuning code is out. Ch
- `unlimited-ocr` [L|hyb|H|~] — Unlimited OCR apunta a extracción de texto y estructura en documentos largos. Setup de visión; no es un editor

### 12. Audio, Voz & Video (16)
Detalle: `REPO_MENU_cats/12-audio-voz-video.md`

- `faster-whisper` [R|cld|H|+] — faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference en
- `ffmpeg` [D|loc|M|+] — FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles an
- `fluxer` [P|hyb|M|~] — As of this writing (15 June 2026), we are working to finalise the API and self-hosting documentation over the 
- `lossless-cut` [A|loc|M|~] — The swiss army knife of lossless video/audio editing.
- `moviepy` [L|loc|M|~] — MoviePy recently upgraded to v2.0, introducing major breaking changes. You can consult the last v1 docs here b
- `omnivoice-studio` [A|hyb|H|~] — OmniVoice Studio concentra clonación y síntesis de voz en un studio local. Está en beta; espera roturas entre 
- `remotion` [L|hyb|M|~] — Remotion renderiza video desde componentes React. Úsalo para piezas generadas por código (intros, datos, motio
- `remotion-superpowers` [P|cld|H|+] — A free, open-source Claude Code plugin that turns Remotion into a full video production studio — by Dojo Codin
- `supertonic` [L|hyb|H|~] — Supertonic is a lightning-fast, on-device multilingual text-to-speech system designed for local inference with
- `vibevoice` [D|hyb|M|+] — 🎙️ VibeVoice: Open-Source Frontier Voice AI.
- `video-use` [S|hyb|M|+] — Introducing video-use — edit videos with Claude Code. 100% open source.
- `videofy-minimal` [P|hyb|M|~] — Videofy Minimal is a local tool for turning news articles into short videos for digital signage screens.
- `voxcpm` [L|hyb|H|~] — 👋 Join our community for discussion and support!.
- `wan2gp` [P|loc|H|~] — WanGP is a one-stop super app for the best open source generative models across video, image, audio, and text-
- `whisper` [L|cld|H|~] — Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and i
- `whisperx` [L|hyb|H|~] — If you’re looking for a transcription API for meetings, consider checking out Recall.ai's Meeting Transcriptio

### 13. Documentos & Presentaciones (6)
Detalle: `REPO_MENU_cats/13-documentos-presentaciones.md`

- `markitdown` [D|loc|E|+] — MarkItDown performs I/O with the privileges of the current process. Like open() or requests.get(), it will acc
- `pdf-inspector` [L|hyb|M|~] — PDF Inspector detecta si un PDF es texto o escaneado y extrae contenido con coordenadas. Encaja en pipelines d
- `pdfcraft` [A|loc|M|~] — PDFCraft procesa PDFs en el cliente. Encaja para utilidades locales de documentos, no para un pipeline de conv
- `pdfding` [A|loc|M|~] — PdfDing es un manager de PDFs que hosteas tú. Alternativa ligera a suites documentales pesadas.
- `ppt-master` [L|hyb|H|~] — This project is kept free and open source with the support of PackyCode , APIKEY.FUN , RunAPI , YouYun ZhiSuan
- `reveal.js` [R|hyb|M|~] — reveal.js is an open source HTML presentation framework. It enables anyone with a web browser to create beauti

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
