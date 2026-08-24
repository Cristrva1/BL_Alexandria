# 3. Frameworks & Orquestación de Agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ag2`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** AG2 was evolved from AutoGen. Fully open-sourced. We invite collaborators from all organizations to contribute.
**Stack:** python, typescript, react, docker
**Repo:** https://github.com/ag2ai/ag2.git

**Instalación** [~]: `git clone https://github.com/ag2ai/ag2.git && cd ag2 && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** construyes multiagente serio en Python
**Evita si:** te basta un agente único o quieres orquestación visual.
**Combina con:** `langchain`, `langfuse`

## `agents-towards-production`
role=skill · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Agents Towards Production.
**Stack:** python, typescript, docker, fastapi, langchain
**Repo:** https://github.com/NirDiamant/agents-towards-production.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/agents-towards-production/). Si necesitas el código: git clone https://github.com/NirDiamant/agents-towards-production.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** vas a producción con agentes y necesitas el ciclo completo
**Evita si:** solo experimentas localmente o buscas skills, no tutoriales.
**Combina con:** `langfuse`, `ag2`

## `autogen`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** AutoGen ![Maintenance Mode](https://github.com/microsoft/agent-framework).
**Stack:** python, typescript, javascript, postgres
**Repo:** https://github.com/microsoft/autogen.git

**Instalación** [~]: `git clone https://github.com/microsoft/autogen.git && cd autogen && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres autogen [![maintenance mode](https://img.shields.io/badge/status-maintenance%20m
**Evita si:** —
**Combina con:** `awesome-claude-code`, `agents-towards-production`, `ag2`

## `awesome-claude-code`
role=skill · exec=cloud · setup=medium · mcp=False · prov=—

**Qué es:** The old ways have come and gone. It's time to embrace the next phase. The previous Table of Contents was no longer fit for purpose, so a new organizational system is being prepared. Thanks to everyone who has contributed to and supported this repo, be ye human or machine.
**Stack:** python, typescript
**Repo:** https://github.com/hesreallyhim/awesome-claude-code.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-claude-code/). Si necesitas el código: git clone https://github.com/hesreallyhim/awesome-claude-code.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** vives en Claude Code y quieres exprimirlo
**Evita si:** usas otro asistente (no aplica).
**Combina con:** `claude-plugins-official`, `superpowers`

## `awesome-dataviz`
role=directory · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** A curated list of awesome **open-source** data visualizations frameworks, libraries and software. Inspired by awesome-python and originally created by fasouto.
**Stack:** python, typescript, javascript, react, postgres
**Repo:** https://github.com/hal9ai/awesome-dataviz.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-dataviz/). Si necesitas el código: git clone https://github.com/hal9ai/awesome-dataviz.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas opciones de visualización y aún no has elegido
**Evita si:** ya elegiste tu librería y solo necesitas usarla.
**Combina con:** `echarts`, `awesome-bigdata`

## `awesome-langgraph`
role=directory · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** 🦜🕸️ Awesome LangGraph & LangChain Ecosystem !Awesome !Last Updated.
**Stack:** javascript/typescript, python, typescript, javascript, react, docker, postgres, fastapi, langchain
**Repo:** https://github.com/vonzosten/awesome-LangGraph.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-LangGraph/). Si necesitas el código: git clone https://github.com/vonzosten/awesome-LangGraph.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** construyes con LangGraph y quieres patrones de referencia
**Evita si:** no usas ese ecosistema.
**Combina con:** `langchain`

## `awesome-mcp-servers`
role=directory · exec=local · setup=heavy · mcp=True · prov=—

**Qué es:** A curated list of awesome Model Context Protocol (MCP) servers.
**Stack:** python, typescript, javascript, react, docker, postgres, fastapi, langchain, whisper, comfy
**Repo:** https://github.com/punkpeye/awesome-mcp-servers.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-mcp-servers/). Si necesitas el código: git clone https://github.com/punkpeye/awesome-mcp-servers.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas antes de construir
**Evita si:** ya sabes que necesitas uno a medida y no te vale ninguno listado.
**Combina con:** `mcp-use`, `servers`

## `codebase-memory-mcp`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** The fastest and most efficient code intelligence engine for AI coding agents.** Full-indexes an average repository in milliseconds, the Linux kernel (28M LOC, 75K files) in 3 minutes. Answers structural queries in under 1ms. Ships as a single static binary for macOS, Linux, and Windows — download, run `install`, done.
**Stack:** python, typescript, javascript, docker
**Repo:** https://github.com/DeusData/codebase-memory-mcp.git

**Instalación** [~]: `git clone https://github.com/DeusData/codebase-memory-mcp.git && cd codebase-memory-mcp && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** —
**Combina con:** `awesome-claude-code`, `agents-towards-production`, `ag2`

## `crewai`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Fast and Flexible Multi-Agent Automation Framework.
**Stack:** python, typescript, postgres, langchain
**Repo:** https://github.com/crewAIInc/crewAI.git

**Instalación** [~]: `git clone https://github.com/crewAIInc/crewAI.git && cd crewAI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres velocidad y un modelo mental simple de "equipo"
**Evita si:** necesitas control de bajo nivel o orquestación muy custom.
**Combina con:** `langchain`, `mem0`

## `dash`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Dash is the most downloaded, trusted Python framework for building ML & data science web apps*.
**Stack:** python, typescript, javascript, react, postgres
**Repo:** https://github.com/plotly/dash.git

**Instalación** [~]: `git clone https://github.com/plotly/dash.git && cd dash && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres dashboards productivos en Python con control del frontend
**Evita si:** prefieres prototipos ultrarrápidos ([streamlit](#-streamlit)).
**Combina con:** `streamlit`, `echarts`

## `deer-flow`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** English | 中文 | 日本語 | Français | Русский.
**Stack:** python, typescript, javascript, docker, langchain
**Repo:** https://github.com/bytedance/deer-flow.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/deer-flow/). Si necesitas el código: git clone https://github.com/bytedance/deer-flow.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres un orquestador completo y extensible
**Evita si:** buscas algo minimalista o sin Docker.
**Combina con:** `gpt-researcher`, `firecrawl`

## `defending-code-reference-harness`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** A reference implementation for autonomous vulnerability discovery and remediation with Claude, based on our learnings from partnering with security teams at several organizations since launching Claude Mythos Preview. For a write up of these learnings along with best practices, see the accompanying blog post (also avail.
**Stack:** python, typescript, docker
**Repo:** https://github.com/anthropics/defending-code-reference-harness.git

**Instalación** [~]: `pip install defending-code-reference-harness   (o: uv add defending-code-reference-harness)`
_Nombre PyPI puede diferir de 'defending-code-reference-harness'; verifica en pypi.org._

**Elige si:** quieres defending code reference harness
**Evita si:** —
**Combina con:** `awesome-claude-code`, `agents-towards-production`, `ag2`

## `dify`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** alt="chat on Discord"> alt="join Reddit"> alt="follow on X(Twitter)"> alt="follow on LinkedIn"> .
**Stack:** javascript/typescript, python, typescript, javascript, react, docker, postgres
**Repo:** https://github.com/langgenius/dify.git

**Instalación** [~]: `git clone https://github.com/langgenius/dify.git && cd dify && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres una app IA completa autoalojada
**Evita si:** solo necesitas una librería o un prototipo puntual.
**Combina con:** `langflow`, `flowise`

## `ecc`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Official sources only.** Install ECC only from verified channels: the GitHub repository github.com/affaan-m/ECC, the npm packages `ecc-universal` and `ecc-agentshield`, the GitHub App, the plugin slug `ecc@ecc`, and the project website [ecc.tools](http.
**Stack:** python, typescript, javascript, react, docker, postgres, fastapi
**Repo:** https://github.com/affaan-m/ECC.git

**Instalación** [~]: `git clone https://github.com/affaan-m/ECC.git && cd ECC && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** ejecutas agentes con acceso real a tu máquina y necesitas contención
**Evita si:** solo haces prompts de chat sin ejecución de código.
**Combina con:** `openhands`, `sandbox`, `hermes-agent`

## `flowise`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** English | 繁體中文 | 简体中文 | 日本語 | 한국어.
**Stack:** javascript/typescript, typescript, javascript, react, docker
**Repo:** https://github.com/FlowiseAI/Flowise.git

**Instalación** [~]: `git clone https://github.com/FlowiseAI/Flowise.git && cd Flowise && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un prototipo visual ya, en stack JS
**Evita si:** necesitas plataforma completa con RAG/observabilidad ([dify](#-dify)).
**Combina con:** `dify`, `langflow`

## `gpt-researcher`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** 🔎 GPT Researcher.
**Stack:** python, typescript, javascript, react, docker, fastapi, langchain
**Repo:** https://github.com/assafelovic/gpt-researcher.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/gpt-researcher/). Si necesitas el código: git clone https://github.com/assafelovic/gpt-researcher.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas research profundo citado
**Evita si:** solo quieres una respuesta corta o un chat simple.
**Combina con:** `firecrawl`, `browser-use`, `research profundo`

## `guardrails`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** LATEST RELEASE / DEVELOPMENT VERSION**: The develop branch tracks the latest top of tree development. The latest released version is 0.21.0.
**Stack:** python, typescript, javascript, react, docker, langchain
**Repo:** https://github.com/NVIDIA-NeMo/Guardrails.git

**Instalación** [~]: `git clone https://github.com/NVIDIA-NeMo/Guardrails.git && cd Guardrails && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres nvidia nemo guardrails library
**Evita si:** —
**Combina con:** `awesome-claude-code`, `agents-towards-production`, `ag2`

## `headroom`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** ██╗ ██╗███████╗ █████╗ ██████╗ ██████╗ ██████╗ ██████╗ ███╗ ███╗ ██║ ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║ ███████║█████╗ ███████║██║ ██║██████╔╝██║ ██║██║ ██║██╔████╔██║ ██╔══██║██╔══╝ ██╔══██║██║ ██║██╔══██╗██║ ██║██║ ██║██║╚██╔╝██║ ██║ ██║███████╗██║ ██║██████╔╝██║ ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║ ╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝╚═════╝ ╚═╝ ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═╝ .
**Stack:** python, typescript, javascript, docker, postgres, langchain
**Repo:** https://github.com/headroomlabs-ai/headroom.git

**Instalación** [~]: `git clone https://github.com/headroomlabs-ai/headroom.git && cd headroom && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** te quedas sin contexto en sesiones largas
**Evita si:** tus prompts ya caben holgados o la pérdida de detalle por resumen es inaceptable.
**Combina con:** `context-engineering`, `codegraph`

## `hyperframes`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** HyperFrames is an open-source framework for turning HTML, CSS, media, and seekable animations into deterministic MP4 videos. Use it locally with the CLI, from AI coding agents with skills, or as the rendering core behind hosted authoring workflows.
**Stack:** javascript/typescript, python, typescript, javascript, react, docker
**Repo:** https://github.com/heygen-com/hyperframes.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/hyperframes/). Si necesitas el código: git clone https://github.com/heygen-com/hyperframes.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** generas animación por frames con control por código
**Evita si:** prefieres video en React con reloj integrado ([remotion](#-remotion)) o edición visual.
**Combina con:** `remotion`

## `langchain`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves.
**Stack:** python, typescript, langchain
**Repo:** https://github.com/langchain-ai/langchain.git

**Instalación** [~]: `git clone https://github.com/langchain-ai/langchain.git && cd langchain && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres la base estándar con máximas integraciones
**Evita si:** prefieres mínima abstracción o un solo proveedor sin cambiar.
**Combina con:** `langflow`, `langfuse`, `litellm`

## `langflow`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** ✨ Highlight features.
**Stack:** python, typescript, javascript, docker
**Repo:** https://github.com/langflow-ai/langflow.git

**Instalación** [~]: `git clone https://github.com/langflow-ai/langflow.git && cd langflow && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** prefieres construir en visual sobre LangChain
**Evita si:** quieres todo en código o no usas LangChain.
**Combina con:** `langchain`, `dify`

## `langfuse`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** alt="chat on Discord"> alt="follow on X(Twitter)"> alt="follow on LinkedIn"> .
**Stack:** javascript/typescript, python, typescript, javascript, react, docker, fastapi, langchain
**Repo:** https://github.com/langfuse/langfuse.git

**Instalación** [~]: `git clone https://github.com/langfuse/langfuse.git && cd langfuse && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** operas agentes en serio y necesitas trazas/costes/eval
**Evita si:** haces prototipos triviales o no quieres operar el backend.
**Combina con:** `langchain`, `litellm`, `ag2`

## `mcp-use`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** to build MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.
**Stack:** python, typescript, javascript, react, langchain
**Repo:** https://github.com/mcp-use/mcp-use.git

**Instalación** [~]: `git clone https://github.com/mcp-use/mcp-use.git && cd mcp-use && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** construyes un servidor MCP propio y quieres productividad
**Evita si:** solo buscas usar uno ya hecho ([awesome-mcp-servers](#-awesome-mcp-servers)) o necesitas control a nivel spec.
**Combina con:** `mcp`, `awesome-mcp-servers`, `app mcp`

## `nemo-agent-toolkit`
role=directory · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** SPDX-License-Identifier: Apache-2.0.
**Stack:** python, typescript, javascript, react, fastapi, langchain
**Repo:** https://github.com/NVIDIA/NeMo-Agent-Toolkit.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/NeMo-Agent-Toolkit/). Si necesitas el código: git clone https://github.com/NVIDIA/NeMo-Agent-Toolkit.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** trabajas con infra NVIDIA o necesitas guardrails/eval empresarial
**Evita si:** quieres algo ligero y agnóstico.
**Combina con:** `langchain`

## `openhands`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends.
**Stack:** python, typescript, javascript, docker
**Repo:** https://github.com/OpenHands/OpenHands.git

**Instalación** [~]: `git clone https://github.com/OpenHands/OpenHands.git && cd OpenHands && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un agente que "haga", no solo hable
**Evita si:** solo necesitas chat/RAG o no puedes correr Docker.
**Combina con:** `ecc`, `sandbox`

## `openscreen`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** This started as a side project that blew up; not production grade and you'll hit bugs, but hopefully it covers what you need. **This project will soon be archived.**.
**Stack:** javascript/typescript, typescript, javascript, postgres
**Repo:** https://github.com/siddharthvaddem/openscreen.git

**Instalación** [~]: `git clone https://github.com/siddharthvaddem/openscreen.git && cd openscreen && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** necesitas screencast simple desde el navegador
**Evita si:** quieres algo mantenido y estable (el original está archivado) o grabación fuera del navegador.
**Combina con:** `opencut`

## `playwright`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Playwright is a framework for web automation and testing. It drives Chromium, Firefox, and WebKit with a single API — in your tests, in your scripts, and as a tool for AI agents.
**Stack:** javascript/typescript, python, typescript, javascript, postgres
**Repo:** https://github.com/microsoft/playwright.git

**Instalación** [~]: `git clone https://github.com/microsoft/playwright.git && cd playwright && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas control preciso y reproducible del browser
**Evita si:** quieres que el agente navegue por visión ([browser-use](#-browser-use)) o no necesitas un navegador real.
**Combina con:** `browser-use`, `crawlee`

## `ponytail`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** You know him. Long ponytail. Oval glasses. Has been at the company longer than the version control. You show him fifty lines; he looks at them, says nothing, and replaces them with one.
**Stack:** javascript/typescript, python, typescript, javascript, react, fastapi
**Repo:** https://github.com/DietrichGebert/ponytail.git

**Instalación** [~]: `pip install ponytail   (o: uv add ponytail)`
_Nombre PyPI puede diferir de 'ponytail'; verifica en pypi.org._

**Elige si:** —
**Evita si:** —
**Combina con:** `awesome-claude-code`, `agents-towards-production`, `ag2`

## `repomix`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Need discussion? Join us on Discord ! .
**Stack:** javascript/typescript, python, typescript, javascript, react, docker, postgres
**Repo:** https://github.com/yamadashy/repomix.git

**Instalación** [~]: `pip install repomix   (o: uv add repomix)`
_Nombre PyPI puede diferir de 'repomix'; verifica en pypi.org._

**Elige si:** quieres need discussion? join us on <a href="https://discord.gg/wnyztwzfku">discord</a>!
**Evita si:** —
**Combina con:** `awesome-claude-code`, `agents-towards-production`, `ag2`

## `ruflo`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** An agent meta-harness for Claude Code and Codex.**.
**Stack:** javascript/typescript, typescript, javascript, react, docker, postgres
**Repo:** https://github.com/ruvnet/ruflo.git

**Instalación** [~]: `git clone https://github.com/ruvnet/ruflo.git && cd ruflo && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** orquestas muchos agentes a escala y quieres rendimiento
**Evita si:** solo necesitas 1-2 agentes o no usas Claude Code/Codex.
**Combina con:** `mem0`, `ecc`

## `sandbox`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** AIO Sandbox - All-in-One Agent Sandbox Environment
**Stack:** javascript/typescript, python, typescript, javascript, react, docker, langchain
**Repo:** https://github.com/agent-infra/sandbox.git

**Instalación** [~]: `pip install sandbox   (o: uv add sandbox)`
_Nombre PyPI puede diferir de 'sandbox'; verifica en pypi.org._

**Elige si:** quieres aislar la ejecución de agentes y reproducibilidad
**Evita si:** te basta correr local sin sandbox o no puedes asumir el overhead de Docker.
**Combina con:** `openhands`, `ecc`

## `scrapling`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl.
**Stack:** python, typescript, javascript, docker, postgres
**Repo:** https://github.com/D4Vinci/Scrapling.git

**Instalación** [~]: `pip install scrapling   (o: uv add scrapling)`
_Nombre PyPI puede diferir de 'Scrapling'; verifica en pypi.org._

**Elige si:** los sitios cambian o te bloquean a menudo
**Evita si:** el target es estable y simple, o no necesitas stealth.
**Combina con:** `scrapy`

## `tooljet`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** :star: If you find ToolJet useful, please consider giving us a star on GitHub! Your support helps us continue to innovate and deliver exciting features.
**Stack:** javascript/typescript, python, typescript, javascript, docker, postgres
**Repo:** https://github.com/ToolJet/ToolJet.git

**Instalación** [~]: `git clone https://github.com/ToolJet/ToolJet.git && cd ToolJet && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres tooljet is the open-source foundation of tooljet ai - the ai-native platform for building
**Evita si:** —
**Combina con:** `awesome-claude-code`, `agents-towards-production`, `ag2`

## `turbovec`
role=directory · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** A 10 million document corpus takes 31 GB of RAM as float32. turbovec fits it in 4 GB - and searches it faster than FAISS.**.
**Stack:** python, typescript, langchain
**Repo:** https://github.com/RyanCodrai/turbovec.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/turbovec/). Si necesitas el código: git clone https://github.com/RyanCodrai/turbovec.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas vector search veloz y embebido sin desplegar una DB
**Evita si:** ya usas una vector DB completa con persistencia y escalado horizontal.
**Combina con:** `mem0`, `graphrag`
