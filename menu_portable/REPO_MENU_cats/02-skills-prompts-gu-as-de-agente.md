# 2. Skills, Prompts & Guías de Agente — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agent-toolkit`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Opinionated skills shared by @leonardocouy for improving daily work efficiency with Claude Code. Skills are packaged instructions and scripts that extend agent capabilities across development, documentation, planning, and professional workflows.
**Stack:** python, typescript, react
**Repo:** https://github.com/softaworks/agent-toolkit.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/agent-toolkit/). Si necesitas el código: git clone https://github.com/softaworks/agent-toolkit.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres productividad inmediata con tareas comunes
**Evita si:** buscas un método integral ([superpowers](#-superpowers)).
**Combina con:** `superpowers`

## `andrej-karpathy-skills`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Check out my new project Multica — an open-source platform for running and managing coding agents with reusable skills.
**Stack:** typescript
**Repo:** https://github.com/multica-ai/andrej-karpathy-skills.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/andrej-karpathy-skills/). Si necesitas el código: git clone https://github.com/multica-ai/andrej-karpathy-skills.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres respuestas más útiles ya, sin curar prompts largos
**Evita si:** buscas skills ejecutables con scripts concretos.
**Combina con:** `awesome-claude-code`, `context-engineering`

## `antigravity-awesome-skills`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** 🌌 Antigravity Awesome Skills: 1,682+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More.
**Stack:** javascript/typescript, python, typescript, javascript, react, postgres
**Repo:** https://github.com/sickn33/antigravity-awesome-skills.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/antigravity-awesome-skills/). Si necesitas el código: git clone https://github.com/sickn33/antigravity-awesome-skills.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres opciones por cantidad y dominio
**Evita si:** prefieres curaduría oficial y respaldo de marca ([awesome-agent-skills](#-awesome-agent-skills)).
**Combina con:** `skillspector`, `awesome-agent-skills`

## `autoresearch`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of "group meeting". That era is long gone. Research is now entirely the domain of autonomous swarms of AI agents running across compute cluster megastructures in the skies. The agents claim that we are now in th
**Stack:** python, typescript
**Repo:** https://github.com/karpathy/autoresearch.git

**Instalación** [~]: `git clone https://github.com/karpathy/autoresearch.git && cd autoresearch && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** experimentas con research iterativo o quieres un punto de partida
**Evita si:** quieres salida pulida y lista ([gpt-researcher](#-gpt-researcher)).
**Combina con:** `gpt-researcher`, `crawl4ai`

## `awesome-agent-skills`
role=skill · exec=cloud · setup=heavy · mcp=False · prov=—

**Qué es:** Hand-picked, not AI-slop generated.
**Stack:** python, typescript, javascript, react, docker, postgres, fastapi, langchain, whisper
**Repo:** https://github.com/VoltAgent/awesome-agent-skills.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-agent-skills/). Si necesitas el código: git clone https://github.com/VoltAgent/awesome-agent-skills.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** valoras respaldo de marca y curaduría
**Evita si:** necesitas máxima cantidad o variedad ([antigravity-awesome-skills](#-antigravity-awesome-skills)).
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `superpowers`

## `browser-harness`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Browser Harness ♞.
**Stack:** python, typescript, postgres
**Repo:** https://github.com/browser-use/browser-harness.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/browser-harness/). Si necesitas el código: git clone https://github.com/browser-use/browser-harness.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres <img src="https://raw.githubusercontent.com/browser-use/media/main/browser-harness/banner-
**Evita si:** —
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `context-engineering`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Context Engineering.
**Stack:** python, typescript, react, postgres
**Repo:** https://github.com/jasontang-ai/Context-Engineering.git

**Instalación** [~]: `git clone https://github.com/jasontang-ai/Context-Engineering.git && cd Context-Engineering && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres profundizar en contexto y RAG
**Evita si:** buscas skills ejecutables listas para copiar.
**Combina con:** `andrej-karpathy-skills`, `headroom`

## `geo-seo-claude`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) while maintaining traditional SEO foundations.
**Stack:** python, typescript
**Repo:** https://github.com/zubair-trabzada/geo-seo-claude.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/geo-seo-claude/). Si necesitas el código: git clone https://github.com/zubair-trabzada/geo-seo-claude.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** te importa el descubrimiento por IA, no solo Google
**Evita si:** solo haces SEO clásico sin objetivo generativo.
**Combina con:** `marketingskills`, `agency-agents`

## `guia`
role=skill · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, elegir y combinar** repos rápido.
**Stack:** typescript, whisper, comfy
**Repo:** —

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/guia/). Si necesitas el código: git clone <guia>`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres 🌌 catálogo de repositorios de ia & automatización
**Evita si:** —
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `hermes-agent`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing w.
**Stack:** python, typescript, javascript, docker, postgres
**Repo:** https://github.com/NousResearch/hermes-agent.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/hermes-agent/). Si necesitas el código: git clone https://github.com/NousResearch/hermes-agent.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres agentes locales con UI y memoria persistente
**Evita si:** prefieres orquestación en nube o no quieres compilar Tauri.
**Combina con:** `ecc`, `odysseus`

## `humanizer`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** A skill for Claude Code and OpenCode that removes signs of AI-generated writing from text, making it sound more natural and human.
**Stack:** typescript
**Repo:** https://github.com/blader/humanizer.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/humanizer/). Si necesitas el código: git clone https://github.com/blader/humanizer.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** publicas prosa generada por IA y quieres evitar el "tono IA"
**Evita si:** escribes a mano o el registro formal no es problema.
**Combina con:** `stop-slop`

## `last30days-skill`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** An AI agent-led search engine scored by upvotes, likes, and real money - not editors.**.
**Stack:** python, typescript, javascript, react
**Repo:** https://github.com/mvanhorn/last30days-skill.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/last30days-skill/). Si necesitas el código: git clone https://github.com/mvanhorn/last30days-skill.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres /last30days
**Evita si:** —
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `llm-council`
role=platform · exec=cloud · setup=medium · mcp=False · prov=—

**Qué es:** The idea of this repo is that instead of asking a question to your favorite LLM provider (e.g. OpenAI GPT 5.1, Google Gemini 3.0 Pro, Anthropic Claude Sonnet 4.5, xAI Grok 4, eg.c), you can group them into your "LLM Council". This repo is a simple, local web app that essentially looks like ChatGPT except it uses OpenRouter to send your query to multiple LLMs, it then asks them to review and rank e
**Stack:** python, typescript, javascript, react, postgres, fastapi
**Repo:** https://github.com/karpathy/llm-council.git

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres consenso entre modelos o comparar proveedores
**Evita si:** te basta un único LLM o el coste multi-modelo no es asumible.
**Combina con:** `litellm`

## `marketingskills`
role=skill · exec=cloud · setup=heavy · mcp=False · prov=—

**Qué es:** A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who want AI coding agents to help with conversion optimization, copywriting, SEO, analytics, and growth engineering. Works with Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent that supports the Agent Skills spec.
**Stack:** typescript, postgres
**Repo:** https://github.com/coreyhaines31/marketingskills.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/marketingskills/). Si necesitas el código: git clone https://github.com/coreyhaines31/marketingskills.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** automatizas marketing con agentes y quieres playbooks
**Evita si:** necesitas ejecución (no skills) o no haces marketing.
**Combina con:** `agency-agents`, `mautic`, `marketing de agencia`

## `multica`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Your next 10 hires won't be human.**.
**Stack:** javascript/typescript, typescript, javascript, react, docker, postgres
**Repo:** https://github.com/multica-ai/multica.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/multica/). Si necesitas el código: git clone https://github.com/multica-ai/multica.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** mezclas trabajo humano y agentes en un mismo flujo
**Evita si:** quieres automatización 100% headless o un producto maduro.
**Combina con:** `ruflo`, `chatwoot`

## `nanogpt`
role=library · exec=cloud · setup=heavy · mcp=False · prov=—

**Qué es:** Update Nov 2025** nanoGPT has a new and improved cousin called nanochat. It is very likely you meant to use/find nanochat instead. nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity.
**Stack:** python, typescript, javascript, postgres
**Repo:** https://github.com/karpathy/nanoGPT.git

**Instalación** [~]: `pip install nanogpt   (o: uv add nanogpt)`
_Nombre PyPI puede diferir de 'nanoGPT'; verifica en pypi.org._

**Elige si:** quieres entender el entrenamiento de un GPT desde cero
**Evita si:** solo consumes modelos vía API o necesitas un pipeline de chat completo ([nanochat](#-nanochat)).
**Combina con:** `nanochat`, `llm.c`

## `notebooklm-py`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** A Comprehensive NotebookLM Skill & Unofficial Python API.** Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.
**Stack:** python, typescript, javascript, postgres, fastapi
**Repo:** https://github.com/teng-lin/notebooklm-py.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/notebooklm-py/). Si necesitas el código: git clone https://github.com/teng-lin/notebooklm-py.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** automatizas el NotebookLM real y aceptas el riesgo de API no oficial
**Evita si:** quieres todo local ([open-notebook](#-open-notebook)).
**Combina con:** `notebooklm-mcp-cli`

## `open-generative-ai`
role=skill · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** The free, open-source alternative to AI Video Platforms.** Generate AI images and videos using 200+ state-of-the-art models — no content filters, no closed ecosystem, no subscription fees.
**Stack:** javascript/typescript, python, typescript, javascript, react, docker, comfy
**Repo:** https://github.com/Anil-matcha/Open-Generative-AI.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Open-Generative-AI/). Si necesitas el código: git clone https://github.com/Anil-matcha/Open-Generative-AI.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres un hub de generación multi-modal sin atarte a un SaaS
**Evita si:** ya tienes tu pipeline local ([ComfyUI](#-comfyui)) o necesitas control fino por nodo.
**Combina con:** `remotion`, `marketing de agencia`

## `openmontage`
role=skill · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Turn your AI coding assistant into a full video production studio. Describe what you want in plain language — your agent handles research, scripting, asset generation, editing, and final composition.
**Stack:** python, typescript, javascript, react, postgres, whisper
**Repo:** https://github.com/calesthio/OpenMontage.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/OpenMontage/). Si necesitas el código: git clone https://github.com/calesthio/OpenMontage.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** —
**Evita si:** —
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `playwright-cli`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Playwright CLI with SKILLS.
**Stack:** javascript/typescript, python, typescript, javascript
**Repo:** https://github.com/microsoft/playwright-cli.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/playwright-cli/). Si necesitas el código: git clone https://github.com/microsoft/playwright-cli.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** tu agente vive en CLI y el contexto es un recurso caro
**Evita si:** necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP).
**Combina con:** `playwright`, `browser-use`

## `prompt-master`
role=skill · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention. No re-prompting your way to an answer you should have gotten on attempt one.
**Stack:** python, typescript, javascript, react, postgres, comfy
**Repo:** https://github.com/nidhinjs/prompt-master.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/prompt-master/). Si necesitas el código: git clone https://github.com/nidhinjs/prompt-master.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres dejar de re-promptear y acertar antes
**Evita si:** ya tienes prompts afinados y estables.
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `skills-remotion`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** This is an internal package and has no documentation.
**Stack:** javascript/typescript, javascript
**Repo:** https://github.com/remotion-dev/skills.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/skills_remotion/). Si necesitas el código: git clone https://github.com/remotion-dev/skills.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres @remotion/skills
**Evita si:** —
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `skillspector`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before installing agent skills.
**Stack:** python, typescript, javascript, docker
**Repo:** https://github.com/NVIDIA/SkillSpector.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/SkillSpector/). Si necesitas el código: git clone https://github.com/NVIDIA/SkillSpector.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** instalas skills externas o curas catálogos
**Evita si:** solo usas skills propias de confianza.
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `stitch-sdk`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Generate UI screens from text prompts and extract their HTML and screenshots programmatically.
**Stack:** javascript/typescript, typescript, javascript
**Repo:** https://github.com/google-labs-code/stitch-sdk.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/stitch-sdk/). Si necesitas el código: git clone https://github.com/google-labs-code/stitch-sdk.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres @google/stitch-sdk
**Evita si:** —
**Combina con:** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`

## `stop-slop`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** A skill for removing AI tells from prose.
**Stack:** typescript
**Repo:** https://github.com/hardikpandya/stop-slop.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/stop-slop/). Si necesitas el código: git clone https://github.com/hardikpandya/stop-slop.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres prosa más natural y te molesta el tono IA
**Evita si:** ya usas [humanizer](#-humanizer) (solapan) o escribes a mano.
**Combina con:** `humanizer`

## `superpowers`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them.
**Stack:** javascript/typescript, typescript, javascript
**Repo:** https://github.com/obra/superpowers.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/superpowers/). Si necesitas el código: git clone https://github.com/obra/superpowers.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres método, no fragmentos sueltos
**Evita si:** solo necesitas una skill aislada puntual.
**Combina con:** `awesome-claude-code`, `agent-toolkit`

## `ui-ux-pro-max-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** An AI skill that provides design intelligence for building professional UI/UX across multiple platforms and frameworks.
**Stack:** python, typescript, javascript, react
**Repo:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/ui-ux-pro-max-skill/). Si necesitas el código: git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** generas UI con IA y el resultado se ve genérico o despulido
**Evita si:** no trabajas frontend o ya tienes un sistema de diseño impuesto.
**Combina con:** `taste-skill`, `impeccable`, `tailwindcss`
