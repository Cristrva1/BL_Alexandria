# REPO_MENU — Menú portable de la biblioteca de repositorios

> Generado: 2026-06-25 · 186 repos curados · Documento 100% para IA.
> COPIA esta carpeta (`menu_portable/`) a la raíz de tu proyecto y
> referencia este archivo desde tu AGENTS.md / system prompt.

---

## INSTRUCCIONES PARA EL AGENTE (léeme entero, soy corto)

Eres un agente que debe elegir qué repositorios instalar/usar para un
proyecto concreto. Tienes un menú curado de **186 repos** de IA y
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

### 1. Automatización, Mensajería & CRM (16)
Detalle: `REPO_MENU_cats/01-automatizaci-n-mensajer-a-crm.md`

- `activepieces` [R|hyb|M|~] — href="https://activepieces.com".
- `appsmith` [P|loc|M|~] — Organizations build custom applications like dashboards, admin panels, customer 360, IT automation, and servic
- `browser-use` [P|loc|M|~] — 🌤️ Want to skip the setup? Use our cloud for faster, scalable, stealth-enabled browser automation!.
- `budibase` [P|loc|M|~] — AI Agents that run your operations Budibase is an open-source operations platform that saves engineers 100s of
- `chatwoot` [L|hyb|M|~] — The modern customer support platform, an open-source alternative to Intercom, Zendesk, Salesforce Service Clou
- `evolution-api` [A|hyb|M|~] — Open-source REST API for WhatsApp and multi-channel messaging — part of the Evolution Foundation ecosystem.
- `huginn` [D|hyb|M|+] — Huginn is a system for building agents that perform automated tasks for you online. They can read the web, wat
- `listmonk` [D|hyb|M|+] — listmonk is a standalone, self-hosted, newsletter and mailing list manager. It is fast, feature-rich, and pack
- `mautic` [P|loc|M|~] — Open Source Marketing Automation Software.
- `n8n` [P|loc|M|~] — n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-
- `n8n-io` [P|loc|M|~] — n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-
- `n8n-mcp` [P|loc|M|~] — A Model Context Protocol (MCP) server that provides AI assistants with comprehensive access to n8n node docume
- `novu` [L|hyb|M|~] — The open-source communication infrastructure for agents and products.
- `openevolve` [L|loc|M|~] — 🧬 The most advanced open-source evolutionary coding agent**.
- `twenty-main` [R|loc|M|~] — Twenty gives technical teams the building blocks for a custom CRM that meets complex business needs and quickl
- `whatsapp-agentkit` [D|cld|M|+] — Construye tu propio agente de WhatsApp con inteligencia artificial en menos de 30 minutos. No necesitas saber 

### 2. Skills, Prompts & Guías de Agente (27)
Detalle: `REPO_MENU_cats/02-skills-prompts-gu-as-de-agente.md`

- `agent-toolkit` [S|loc|M|+] — Opinionated skills shared by @leonardocouy for improving daily work efficiency with Claude Code. Skills are pa
- `andrej-karpathy-skills` [S|hyb|M|+] — Check out my new project Multica — an open-source platform for running and managing coding agents with reusabl
- `antigravity-awesome-skills` [S|loc|E|+] — 🌌 Antigravity Awesome Skills: 1,682+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More.
- `autoresearch` [P|loc|H|~] — One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun,
- `awesome-agent-skills` [S|cld|H|+] — Hand-picked, not AI-slop generated.
- `browser-harness` [S|loc|M|+] — Browser Harness ♞.
- `context-engineering` [R|loc|M|~] — Context Engineering.
- `geo-seo-claude` [S|hyb|M|+] — (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) while maintaining traditional SEO foundations.
- `guia` [S|hyb|H|+] — Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, eleg
- `hermes-agent` [S|loc|M|+] — The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it c
- `humanizer` [S|loc|M|+] — A skill for Claude Code and OpenCode that removes signs of AI-generated writing from text, making it sound mor
- `last30days-skill` [S|hyb|M|+] — An AI agent-led search engine scored by upvotes, likes, and real money - not editors.**.
- `llm-council` [P|cld|M|+] — The idea of this repo is that instead of asking a question to your favorite LLM provider (e.g. OpenAI GPT 5.1,
- `marketingskills` [S|cld|H|+] — A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who wan
- `multica` [S|loc|M|+] — Your next 10 hires won't be human.**.
- `nanogpt` [L|cld|H|~] — Update Nov 2025** nanoGPT has a new and improved cousin called nanochat. It is very likely you meant to use/fi
- `notebooklm-py` [S|hyb|M|+] — A Comprehensive NotebookLM Skill & Unofficial Python API.** Full programmatic access to NotebookLM's features—
- `open-generative-ai` [S|hyb|H|+] — The free, open-source alternative to AI Video Platforms.** Generate AI images and videos using 200+ state-of-t
- `openmontage` [S|loc|H|+] — Turn your AI coding assistant into a full video production studio. Describe what you want in plain language — 
- `playwright-cli` [S|loc|E|+] — Playwright CLI with SKILLS.
- `prompt-master` [S|hyb|H|+] — A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context a
- `skills-remotion` [S|loc|M|+] — This is an internal package and has no documentation.
- `skillspector` [S|loc|M|+] — Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before 
- `stitch-sdk` [S|hyb|M|+] — Generate UI screens from text prompts and extract their HTML and screenshots programmatically.
- `stop-slop` [S|hyb|M|+] — A skill for removing AI tells from prose.
- `superpowers` [S|loc|M|+] — Superpowers is a complete software development methodology for your coding agents, built on top of a set of co
- `ui-ux-pro-max-skill` [S|loc|M|+] — An AI skill that provides design intelligence for building professional UI/UX across multiple platforms and fr

### 3. Frameworks & Orquestación de Agentes (34)
Detalle: `REPO_MENU_cats/03-frameworks-orquestaci-n-de-agentes.md`

- `ag2` [P|hyb|M|~] — AG2 was evolved from AutoGen. Fully open-sourced. We invite collaborators from all organizations to contribute
- `agents-towards-production` [S|hyb|H|+] — Agents Towards Production.
- `autogen` [R|loc|M|~] — AutoGen ![Maintenance Mode](https://github.com/microsoft/agent-framework).
- `awesome-claude-code` [S|cld|M|+] — The old ways have come and gone. It's time to embrace the next phase. The previous Table of Contents was no lo
- `awesome-dataviz` [D|loc|M|+] — A curated list of awesome **open-source** data visualizations frameworks, libraries and software. Inspired by 
- `awesome-langgraph` [D|loc|M|+] — 🦜🕸️ Awesome LangGraph & LangChain Ecosystem !Awesome !Last Updated.
- `awesome-mcp-servers` [D|loc|H|+] — A curated list of awesome Model Context Protocol (MCP) servers.
- `codebase-memory-mcp` [R|hyb|M|~] — The fastest and most efficient code intelligence engine for AI coding agents.** Full-indexes an average reposi
- `crewai` [R|hyb|M|~] — Fast and Flexible Multi-Agent Automation Framework.
- `dash` [P|loc|M|~] — Dash is the most downloaded, trusted Python framework for building ML & data science web apps*.
- `deer-flow` [S|hyb|M|+] — English | 中文 | 日本語 | Français | Русский.
- `defending-code-reference-harness` [L|hyb|M|~] — A reference implementation for autonomous vulnerability discovery and remediation with Claude, based on our le
- `dify` [P|hyb|M|~] — alt="chat on Discord"> alt="join Reddit"> alt="follow on X(Twitter)"> alt="follow on LinkedIn"> .
- `ecc` [A|hyb|M|~] — Official sources only.** Install ECC only from verified channels: the GitHub repository github.com/affaan-m/EC
- `flowise` [P|loc|M|~] — English | 繁體中文 | 简体中文 | 日本語 | 한국어.
- `gpt-researcher` [S|hyb|M|+] — 🔎 GPT Researcher.
- `guardrails` [P|loc|M|~] — LATEST RELEASE / DEVELOPMENT VERSION**: The develop branch tracks the latest top of tree development. The late
- `headroom` [P|loc|M|~] — ██╗ ██╗███████╗ █████╗ ██████╗ ██████╗ ██████╗ ██████╗ ███╗ ███╗ ██║ ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══
- `hyperframes` [S|hyb|M|+] — HyperFrames is an open-source framework for turning HTML, CSS, media, and seekable animations into determinist
- `langchain` [R|loc|M|~] — LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interop
- `langflow` [P|hyb|M|~] — ✨ Highlight features.
- `langfuse` [P|loc|M|~] — alt="chat on Discord"> alt="follow on X(Twitter)"> alt="follow on LinkedIn"> .
- `mcp-use` [P|hyb|M|~] — to build MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.
- `nemo-agent-toolkit` [D|loc|M|+] — SPDX-License-Identifier: Apache-2.0.
- `openhands` [P|hyb|M|~] — Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backend
- `openscreen` [P|hyb|M|~] — This started as a side project that blew up; not production grade and you'll hit bugs, but hopefully it covers
- `playwright` [R|hyb|E|~] — Playwright is a framework for web automation and testing. It drives Chromium, Firefox, and WebKit with a singl
- `ponytail` [L|hyb|M|~] — You know him. Long ponytail. Oval glasses. Has been at the company longer than the version control. You show h
- `repomix` [L|loc|E|~] — Need discussion? Join us on Discord ! .
- `ruflo` [R|loc|M|~] — An agent meta-harness for Claude Code and Codex.**.
- `sandbox` [L|hyb|M|~] — AIO Sandbox - All-in-One Agent Sandbox Environment
- `scrapling` [L|hyb|M|~] — Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale 
- `tooljet` [A|hyb|M|~] — :star: If you find ToolJet useful, please consider giving us a star on GitHub! Your support helps us continue 
- `turbovec` [D|loc|H|+] — A 10 million document corpus takes 31 GB of RAM as float32. turbovec fits it in 4 GB - and searches it faster 

### 4. Scraping, Búsqueda & Research Web (15)
Detalle: `REPO_MENU_cats/04-scraping-b-squeda-research-web.md`

- `archivebox` [P|hyb|M|~] — ▶️ Quickstart | Demo | GitHub | Documentation | Info & Motivation | Communi.
- `crawl4ai` [A|hyb|M|~] — 🚀 Crawl4AI Cloud API — Closed Beta (Launching Soon) Reliable, large-scale web extraction, now built to be _**d
- `crawlee` [R|hyb|M|~] — Crawlee covers your crawling and scraping end-to-end and **helps you build reliable scrapers. Fast.**.
- `crawlee-python` [L|hyb|M|~] — Crawlee covers your crawling and scraping end-to-end and **helps you build reliable scrapers. Fast.**.
- `firecrawl` [L|loc|M|~] — src="https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/firecrawl_logo.png".
- `how-to-train-your-gpt` [R|loc|M|~] — A guide to building a world-class language model from absolute scratch. Taught like you're five. Built like yo
- `instaloader` [L|loc|M|~] — .. |pypi| image:: https://img.shields.io/pypi/v/instaloader.svg :alt: Instaloader PyPI Project Page :target: h
- `llm-scraper` [P|cld|E|+] — LLM Scraper is a TypeScript library that allows you to extract structured data from **any** webpage using LLMs
- `motion` [R|hyb|H|~] — An open source animation library for JavaScript, React and Vue.
- `normalize.css` [L|loc|E|~] — src="https://necolas.github.io/normalize.css/logo.svg" alt="Normalize Logo" width="80" height="80" align="righ
- `odysseus` [S|hyb|H|+] — A self-hosted AI workspace for chat, agents, research, documents, email, notes, calendar, and local model work
- `scrapegraph-ai` [P|hyb|M|~] — 🕷️ ScrapeGraphAI: You Only Scrape Once.
- `scrapely` [L|hyb|E|~] — .. image:: https://api.travis-ci.org/scrapy/scrapely.svg?branch=master :target: https://travis-ci.org/scrapy/s
- `scrapy` [L|loc|M|~] — :target: https://scrapy.org.
- `snscrape` [D|loc|M|+] — snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or

### 5. MCP & Conectividad (12)
Detalle: `REPO_MENU_cats/05-mcp-conectividad.md`

- `awesome-mcp-clients` [D|hyb|M|+] — A curated list of awesome Model Context Protocol (MCP) clients.
- `claude-plugins-official` [P|cld|M|+] — A curated directory of high-quality plugins for Claude Code.
- `github-mcp-server` [P|loc|M|~] — The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and c
- `graphify` [L|loc|H|~] — 🇺🇸 English | 🇨🇳 简体中文 | 🇯🇵 日本語 | 🇰🇷 한국어 | 🇩🇪 Deutsch | 🇫🇷 Français | 🇪🇸 Español | 🇮🇳 <a href="docs/translatio.
- `mcp` [D|hyb|M|+] — This repository contains a list of Google's official Model Context Protocol (MCP) servers, guidance on how to 
- `mcp-neo4j` [D|loc|M|+] — These MCP servers are a part of the Neo4j Labs program. They are developed and maintained by the Neo4j Field G
- `metabase` [P|loc|M|~] — The easiest way to get started with Metabase is to sign up for a free trial of Metabase Cloud.
- `n8n-skills` [S|hyb|M|+] — Expert Claude Code skills for building flawless n8n workflows using the n8n-mcp MCP server**.
- `notebooklm-mcp-cli` [P|hyb|M|~] — Programmatic access to Google NotebookLM** — via command-line interface (CLI) or Model Context Protocol (MCP) 
- `opencut` [P|hyb|M|~] — OpenCut is being rewritten from the ground up.** What's coming:.
- `public-apis` [D|hyb|M|+] — The Public APIs repository is manually curated by community members like you and folks working at APILayer. It
- `servers` [D|loc|M|+] — This repository is a collection of *reference implementations* for the Model Context Protocol (MCP), as well a

### 6. Memoria, LLM Ops & Observabilidad (4)
Detalle: `REPO_MENU_cats/06-memoria-llm-ops-observabilidad.md`

- `agentmemory` [R|hyb|M|~] — Your coding agent remembers everything. No more re-explaining. Built on iii engine Persistent memory for Claud
- `loguru` [P|loc|M|~] — ______________________________________________________________________.
- `mem0` [L|hyb|M|~] — New Memory Algorithm (April 2026).
- `mempalace` [D|hyb|M|+] — Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.

### 7. Inteligencia de Código, Datos & Entrenamiento (8)
Detalle: `REPO_MENU_cats/07-inteligencia-de-c-digo-datos-entrenamiento.md`

- `awesome-bigdata` [D|loc|M|+] — A curated list of awesome big data frameworks, resources and other awesomeness. Inspired by awesome-php, aweso
- `codegraph` [L|loc|M|~] — Already installed? Run `codegraph upgrade` to update in place.
- `data-science-ipython-notebooks` [L|loc|M|~] — data-science-ipython-notebooks.
- `deepseek-coder` [L|loc|H|~] — 1. Introduction of DeepSeek Coder.
- `echarts` [L|loc|E|~] — Apache ECharts is a free, powerful charting and visualization library offering easy ways to add intuitive, int
- `gitnexus` [R|hyb|E|~] — ⚠️ Important Notice:** GitNexus has NO official cryptocurrency, token, or coin. Any token/coin using the GitNe
- `llm.c` [A|cld|H|+] — LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython. Current focus is on pretrai
- `openai-python` [P|hyb|M|~] — The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.9+ application. 

### 8. Workspaces de IA Local & Notebooks (1)
Detalle: `REPO_MENU_cats/08-workspaces-de-ia-local-notebooks.md`

- `open-notebook` [P|hyb|M|~] — An open source, privacy-focused alternative to Google's Notebook LM!.

### 9. Diseño, UI & Frontend (33)
Detalle: `REPO_MENU_cats/09-dise-o-ui-frontend.md`

- `agency-agents` [S|loc|H|+] — A complete AI agency at your fingertips** - From frontend wizards to Reddit community ninjas, from whimsy inje
- `daily-stock-analysis` [L|hyb|M|~] — 🤖 基于 AI 大模型的 A股/港股/美股/日股/韩股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/Discord/Slack/邮箱.
- `design.md` [D|loc|M|+] — A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent,
- `gradio` [S|hyb|M|+] — | [Documentation](https://gradio.app/docs/)
- `graphrag` [L|loc|H|~] — 👉 Microsoft Research Blog Post 👉 Read the docs 👉 GraphRAG Arxiv.
- `gsap` [R|loc|M|~] — GSAP is a **framework-agnostic** JavaScript animation library that turns developers into animation superheroes
- `heroui` [L|loc|M|~] — packages/react/README.md
- `impeccable` [S|hyb|E|+] — Design guidance for AI coding agents. 1 skill, 23 commands, live browser iteration, and 44 deterministic detec
- `llmfit` [A|loc|H|~] — New: Community Leaderboard** — Browse real-world performance data from actual users. Press `b` to see measured
- `magicui` [R|hyb|M|~] — UI Library for Design Engineers.
- `mirofish` [R|hyb|M|~] — 简洁通用的群体智能引擎，预测万物.
- `nanochat` [A|loc|H|~] — nanochat is the simplest experimental harness for training LLMs. It is designed to run on a single GPU node, t
- `nemotron` [A|hyb|H|~] — Open and efficient models for agentic AI.** Training recipes, deployment guides, and use-case examples for the
- `open-design` [R|loc|M|~] — 🔥 **Open Design 0.10.0 is here: the all-in-one Agentic design workspace.** The whole craft now lives in one wi
- `openwa` [P|hyb|M|~] — OpenWA** is a free, open-source WhatsApp API Gateway designed for developers who need full control over their 
- `pdfcraft` [P|loc|M|~] — Merge, split, compress, convert, and edit PDF files online without uploading to servers.
- `penpot` [P|loc|M|~] — Penpot is the open-source design platform for teams that build digital products at scale.
- `plasmic` [L|loc|M|~] — The open-source visual builder for your codebase. Build beautiful apps and websites incredibly fast. Drag and 
- `posthog` [S|loc|M|+] — PostHog is an all-in-one, open source platform for building successful products.
- `react-three-fiber` [L|loc|M|~] — react-three-fiber is a React renderer for threejs.
- `real-esrgan` [L|loc|H|~] — 👀**Demos** **|** 🚩**Updates** **|** ⚡**Usage** **|** 🏰**Model Zoo** **|** 🔧Install **|** 💻Train **|** ❓FAQ **|
- `remotion` [R|hyb|M|~] — Remotion is a framework for **creating videos programmatically using React.**.
- `skills` [S|loc|M|+] — Skills For Real Engineers.
- `skills-emil` [S|loc|M|+] — For designers and engineers to help them build better user interfaces.
- `stitch-skills` [S|loc|M|+] — A collection of agent skills and plugins for Google Stitch, following the Agent Skills open standard. Compatib
- `swr` [L|loc|M|~] — SWR is a React Hooks library for data fetching.
- `tailwindcss` [P|hyb|M|~] — A utility-first CSS framework for rapidly building custom user interfaces.
- `taste-skill` [S|loc|M|+] — Portable **Agent Skills** that upgrade AI-built interfaces: stronger layout, typography, motion, and spacing i
- `three.js` [L|loc|H|~] — JavaScript 3D library.
- `ui` [P|loc|M|~] — A set of beautifully designed components that you can customize, extend, and build on. Start here then make it
- `ui-shadcn` [-|-|-|?] — colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de in — alt: heroui
- `vllm` [L|loc|M|~] — Easy, fast, and cheap LLM serving for everyone.
- `youtube2webpage` [L|loc|M|~] — Youtube-to-Webpage is a Perl script to create a webpage from a Youtube video with a transcript generated from 

### 10. Analítica & Visualización (2)
Detalle: `REPO_MENU_cats/10-anal-tica-visualizaci-n.md`

- `streamlit` [P|loc|E|~] — Welcome to Streamlit 👋.
- `uplot` [L|hyb|M|~] — A small (~50 KB min), fast chart for time series, lines, areas, ohlc & bars _(MIT Licensed)_.

### 11. Generación de Imagen & Visión (17)
Detalle: `REPO_MENU_cats/11-generaci-n-de-imagen-visi-n.md`

- `comfyui` [R|hyb|H|~] — The most powerful and modular AI engine for content creation.**.
- `comfyui-ipadapter-plus` [L|loc|H|~] — The IPAdapter are very powerful models for image-to-image conditioning. The subject or even just the style of 
- `controlnet` [L|loc|H|~] — News: A nightly version of ControlNet 1.1 is released!
- `cosmos` [R|loc|M|~] — Table of Contents.
- `deep-live-cam` [A|hyb|M|~] — Real-time face swap and video deepfake with a single click and only a single image.
- `diffusers` [L|loc|M|~] — Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance
- `face-recognition` [L|loc|M|~] — _You can also read a translated version of this file in Chinese 简体中文版 or in Korean 한국어 or in Japanese 日本語._.
- `fooocus` [S|loc|H|+] — Fooocus is an image generating software (based on Gradio ).
- `gfpgan` [L|loc|M|~] — 1. :boom: **Updated** online demo: ![Replicate](https://replicate.com/tencentarc/gfpgan). Here is the backup. 
- `invokeai` [R|loc|M|~] — Invoke - Professional Creative AI Tools for Visual Media.
- `litellm` [P|hyb|M|~] — LiteLLM is an open source AI Gateway that gives you a single, unified interface to call 100+ LLM providers — O
- `liveportrait` [L|loc|H|~] — `2025/06/01`**: 🌍 Over the past year, **LivePortrait** has 🚀 become an efficient portrait-animation (humans, c
- `luxtts` [D|loc|H|+] — LuxTTS is an lightweight zipvoice based text-to-speech model designed for high quality voice cloning and reali
- `nemo` [R|loc|M|~] — Checkout our HuggingFace🤗 collection for the latest open weight checkpoints and demos!.
- `sd-webui-controlnet` [L|loc|M|~] — The WebUI extension for ControlNet and other injection-based SD controls.
- `stable-diffusion-webui` [S|loc|M|+] — A web interface for Stable Diffusion, implemented using Gradio library.
- `tts` [L|loc|H|~] — 📣 ⓍTTSv2 is here with 16 languages and better performance across the board. 📣 ⓍTTS fine-tuning code is out. Ch

### 12. Audio, Voz & Video (13)
Detalle: `REPO_MENU_cats/12-audio-voz-video.md`

- `faster-whisper` [R|cld|H|+] — faster-whisper** is a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference 
- `ffmpeg` [D|loc|M|+] — FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles an
- `fluxer` [P|hyb|M|~] — As of this writing (15 June 2026), we are working to finalise the API and self-hosting documentation over the 
- `lossless-cut` [A|loc|M|~] — The swiss army knife of lossless video/audio editing.
- `moviepy` [L|loc|M|~] — MoviePy recently upgraded to v2.0, introducing major breaking changes. You can consult the last v1 docs here b
- `omnivoice-studio` [P|hyb|H|~] — OmniVoice Studio is in active beta.** Things may break between releases. For the latest features and fixes, cl
- `supertonic` [L|hyb|H|~] — Supertonic** is a lightning-fast, on-device multilingual text-to-speech system designed for local inference wi
- `vibevoice` [D|hyb|M|+] — 🎙️ VibeVoice: Open-Source Frontier Voice AI.
- `video-use` [S|hyb|M|+] — Introducing **video-use** — edit videos with Claude Code. 100% open source.
- `videofy-minimal` [P|hyb|M|~] — Videofy Minimal is a local tool for turning news articles into short videos for digital signage screens.
- `voxcpm` [L|hyb|H|~] — 👋 Join our community for discussion and support!.
- `whisper` [L|cld|H|~] — Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and i
- `whisperx` [L|hyb|H|~] — Recall.ai - Meeting Transcription API.

### 13. Documentos & Presentaciones (3)
Detalle: `REPO_MENU_cats/13-documentos-presentaciones.md`

- `markitdown` [D|loc|E|+] — MarkItDown performs I/O with the privileges of the current process. Like open() or requests.get(), it will acc
- `ppt-master` [L|hyb|H|~] — PPT Master — AI generates natively editable PPTX from any document
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
