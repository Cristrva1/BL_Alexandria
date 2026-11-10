# 📚 BL_Alexandria

**La biblioteca de repos de IA de Binarias Labs, explicada en español.** Para cada repo te dice qué hace, cuándo elegirlo, cuándo evitarlo, cómo instalarlo y con qué combinarlo. Así decides qué usar en un proyecto sin leer cientos de READMEs.

<!-- BL:STATS -->
**411 repos curados** · **13 categorías** · **14 recetas** · 209 ya en tu biblioteca local + 202 sugeridos nuevos · estrellas de GitHub al 2026-11-05
<!-- /BL:STATS -->

> **Atajo:** abre el [🔎 explorador interactivo](docs/index.html) (búsqueda y filtros) o la [🗺️ guía humana](human/README.md). Si eres una IA, empieza por [AGENTS.md](AGENTS.md).

---

## 🧭 Tres formas de usarla

| Si quieres… | Haz esto | Tiempo |
|---|---|---|
| **Curiosear** qué existe para un tema | Abre una [categoría](#-categorías) o busca en el [explorador](docs/index.html) | 2 min |
| **Montar algo concreto** (un bot, un RAG, un pipeline de video…) | Sigue la [receta](#-recetas-listas) que más se parezca | 10 min |
| **Que el sistema te recomiende** repos para tu idea | Ejecuta `recommend` con la descripción del proyecto ([ver abajo](#-recomendación-para-tu-proyecto)) | 1 min |

## 🚀 ¿Qué quieres construir?

<!-- BL:START -->
| Quiero… | Empieza por | Repos clave |
|---|---|---|
| Un bot de WhatsApp que atienda, venda y pase a humano | [🧪 Bot de WhatsApp con IA](human/playbooks/bot-de-whatsapp-con-ia.md) | [evolution-api](human/fichas/evolution-api.md), [n8n](human/fichas/n8n.md), [chatwoot](human/fichas/chatwoot.md) |
| Un ChatGPT privado con modelos en mi máquina | [🧪 ChatGPT privado con modelos locales](human/playbooks/chatgpt-privado-local.md) | [Ollama](human/fichas/ollama.md), [Open WebUI](human/fichas/open-webui.md), [Jan](human/fichas/jan.md) |
| Preguntarle a mis documentos (RAG) | [🧪 RAG sobre tus documentos](human/playbooks/rag-sobre-documentos.md) | [Docling](human/fichas/docling.md), [LlamaIndex](human/fichas/llama-index.md), [Qdrant](human/fichas/qdrant.md) |
| Programar más rápido con un agente de código | [🧪 Agente de código potenciado](human/playbooks/agente-de-codigo-potenciado.md) | [Claude Code](human/fichas/claude-code.md), [Codex CLI](human/fichas/codex.md), [OpenCode](human/fichas/opencode.md), [superpowers](human/fichas/superpowers.md) |
| Un agente que investigue en la web y cite fuentes | [🧪 Agente de research profundo](human/playbooks/agente-de-research-profundo.md) | [gpt-researcher](human/fichas/gpt-researcher.md), [firecrawl](human/fichas/firecrawl.md), [SearXNG](human/fichas/searxng.md) |
| Automatizar procesos entre mis apps | [🤖 Automatización, Mensajería & CRM › Motores de workflow y automatización](human/categorias/01-automatizaci-n-mensajer-a-crm.md#motores-de-workflow-y-automatización) | [n8n](human/fichas/n8n.md), [activepieces](human/fichas/activepieces.md), [Windmill](human/fichas/windmill.md) |
| Crear o conectar herramientas por MCP | [🧪 Construir una app o servidor MCP](human/playbooks/construir-una-appservidor-mcp.md) | [FastMCP](human/fichas/fastmcp.md), [Playwright MCP](human/fichas/playwright-mcp.md), [GitHub MCP Server](human/fichas/github-mcp-server.md) |
| Un agente de voz para web o teléfono | [🧪 Agente de voz en tiempo real](human/playbooks/agente-de-voz.md) | [Pipecat](human/fichas/pipecat.md), [LiveKit Agents](human/fichas/livekit-agents.md), [Kokoro](human/fichas/kokoro.md) |
| Videos cortos con voz y subtítulos | [🧪 Pipeline de Reels / video corto](human/playbooks/pipeline-de-reels-video-corto.md) | [whisperX](human/fichas/whisperx.md), [remotion](human/fichas/remotion.md), [MoneyPrinterTurbo](human/fichas/moneyprinterturbo.md) |
| Generar o editar imágenes con IA | [🖼️ Generación de Imagen & Visión](human/categorias/11-generaci-n-de-imagen-visi-n.md) | [ComfyUI](human/fichas/comfyui.md), [FLUX](human/fichas/flux.md), [rembg](human/fichas/rembg.md) |
| Una web app moderna con IA integrada | [🧪 Web app moderna con IA](human/playbooks/web-app-moderna-con-ia.md) | [ui](human/fichas/ui.md), [tailwindcss](human/fichas/tailwindcss.md), [AI SDK (Vercel)](human/fichas/vercel-ai.md) |
| Dashboards y analítica de producto | [🧪 Analítica de producto con IA](human/playbooks/analitica-con-ia.md) | [posthog](human/fichas/posthog.md), [Apache Superset](human/fichas/superset.md), [metabase](human/fichas/metabase.md) |
| Convertir PDFs y documentos para IA | [📄 Documentos & Presentaciones › Conversión de documentos para IA](human/categorias/13-documentos-presentaciones.md#conversión-de-documentos-para-ia) | [markitdown](human/fichas/markitdown.md), [Docling](human/fichas/docling.md), [MinerU](human/fichas/mineru.md) |
| Entrenar o afinar un modelo | [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento › Entrenar y afinar modelos](human/categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md#entrenar-y-afinar-modelos) | [Unsloth](human/fichas/unsloth.md), [LLaMA-Factory](human/fichas/llama-factory.md), [Transformers](human/fichas/transformers.md) |
<!-- /BL:START -->

## 📂 Categorías

<!-- BL:CATEGORIES -->
| # | Categoría | Repos | Imprescindibles |
|---:|---|---:|---|
| 1 | [🤖 Automatización, Mensajería & CRM](human/categorias/01-automatizaci-n-mensajer-a-crm.md) | 32 | [n8n](human/fichas/n8n.md), [Self-hosted AI Starter Kit](human/fichas/self-hosted-ai-starter-kit.md), [whatsapp-web.js](human/fichas/whatsapp-web-js.md), [Typebot](human/fichas/typebot.md), [Odoo](human/fichas/odoo.md) |
| 2 | [🧠 Skills, Prompts & Guías de Agente](human/categorias/02-skills-prompts-gu-as-de-agente.md) | 38 | [Anthropic Skills](human/fichas/anthropic-skills.md), [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md), [Agent Skills (Addy Osmani)](human/fichas/agent-skills.md), [Humanizer](human/fichas/humanizer.md), [Marketing Skills](human/fichas/marketingskills.md) |
| 3 | [🕸️ Frameworks & Orquestación de Agentes](human/categorias/03-frameworks-orquestaci-n-de-agentes.md) | 59 | [OpenCode](human/fichas/opencode.md), [Claude Code](human/fichas/claude-code.md), [LangGraph](human/fichas/langgraph.md), [Mastra](human/fichas/mastra.md), [Sim](human/fichas/sim.md) |
| 4 | [🕷️ Scraping, Búsqueda & Research Web](human/categorias/04-scraping-b-squeda-research-web.md) | 29 | [firecrawl](human/fichas/firecrawl.md), [Scrapegraph-ai](human/fichas/scrapegraph-ai.md), [Stagehand](human/fichas/stagehand.md), [SearXNG](human/fichas/searxng.md), [yt-dlp](human/fichas/yt-dlp.md) |
| 5 | [🔌 MCP & Conectividad](human/categorias/05-mcp-conectividad.md) | 20 | [FastMCP](human/fichas/fastmcp.md), [MCP TypeScript SDK](human/fichas/mcp-typescript-sdk.md), [Context7](human/fichas/context7.md), [Playwright MCP](human/fichas/playwright-mcp.md), [MCP for Beginners](human/fichas/mcp-for-beginners.md) |
| 6 | [🧬 Memoria, RAG & LLM Ops](human/categorias/06-memoria-rag-llm-ops.md) | 32 | [claude-mem](human/fichas/claude-mem.md), [RAGFlow](human/fichas/ragflow.md), [Qdrant](human/fichas/qdrant.md), [vLLM](human/fichas/vllm.md), [headroom](human/fichas/headroom.md) |
| 7 | [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](human/categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) | 34 | [Repomix](human/fichas/repomix.md), [Semgrep](human/fichas/semgrep.md), [Unsloth](human/fichas/unsloth.md), [LLM Course](human/fichas/llm-course.md), [TimesFM](human/fichas/timesfm.md) |
| 8 | [🏠 IA Local: Modelos, Chats & Workspaces](human/categorias/08-ia-local-modelos-chats-workspaces.md) | 21 | [Ollama](human/fichas/ollama.md), [Open WebUI](human/fichas/open-webui.md), [Jan](human/fichas/jan.md), [AnythingLLM](human/fichas/anything-llm.md), [SurfSense](human/fichas/surfsense.md) |
| 9 | [🎨 Diseño, UI & Frontend](human/categorias/09-dise-o-ui-frontend.md) | 34 | [ui](human/fichas/ui.md), [daisyUI](human/fichas/daisyui.md), [three.js](human/fichas/three-js.md), [Excalidraw](human/fichas/excalidraw.md), [CopilotKit](human/fichas/copilotkit.md) |
| 10 | [📊 Analítica & Visualización](human/categorias/10-anal-tica-visualizaci-n.md) | 20 | [Umami](human/fichas/umami.md), [Apache Superset](human/fichas/superset.md), [WrenAI](human/fichas/wrenai.md), [Recharts](human/fichas/recharts.md), [Gradio](human/fichas/gradio.md) |
| 11 | [🖼️ Generación de Imagen & Visión](human/categorias/11-generaci-n-de-imagen-visi-n.md) | 27 | [stable-diffusion-webui](human/fichas/stable-diffusion-webui.md), [FLUX](human/fichas/flux.md), [rembg](human/fichas/rembg.md), [Deep-Live-Cam](human/fichas/deep-live-cam.md), [Ultralytics YOLO](human/fichas/ultralytics.md) |
| 12 | [🎬 Audio, Voz & Video](human/categorias/12-audio-voz-video.md) | 42 | [whisper.cpp](human/fichas/whisper-cpp.md), [Kokoro](human/fichas/kokoro.md), [Pipecat](human/fichas/pipecat.md), [FFmpeg](human/fichas/ffmpeg.md), [MoviePy](human/fichas/moviepy.md) |
| 13 | [📄 Documentos & Presentaciones](human/categorias/13-documentos-presentaciones.md) | 23 | [Docling](human/fichas/docling.md), [PaddleOCR](human/fichas/paddleocr.md), [OCRmyPDF](human/fichas/ocrmypdf.md), [Stirling-PDF](human/fichas/stirling-pdf.md), [Slidev](human/fichas/slidev.md) |
<!-- /BL:CATEGORIES -->

## 🔥 Los más populares

<!-- BL:TOP -->
| # | Repo | ⭐ | Categoría | Qué hace |
|---:|---|---:|---|---|
| 1 | [public-apis](human/fichas/public-apis.md) | 498k | 🔌 MCP & Conectividad | Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos. |
| 2 | [OpenClaw](human/fichas/openclaw.md) | 394k | 🕸️ Frameworks & Orquestación de Agentes | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| 3 | [skills](human/fichas/skills.md) | 320k | 🧠 Skills, Prompts & Guías de Agente | Colección de skills de referencia mantenida por el proyecto aihero.dev / Total TypeScript, pensada como ejemplos limpios y bien construidos. |
| 4 | [superpowers](human/fichas/superpowers.md) | 315k | 🧠 Skills, Prompts & Guías de Agente | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |
| 5 | [ECC](human/fichas/ecc.md) | 300k | 🧠 Skills, Prompts & Guías de Agente | Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. |
| 6 | [hermes-agent](human/fichas/hermes-agent.md) | 262k | 🕸️ Frameworks & Orquestación de Agentes | Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. |
| 7 | [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md) | 232k | 🧠 Skills, Prompts & Guías de Agente | Guía de 4 principios inspirada en Andrej Karpathy para que tu agente de código responda útil y sin relleno. |
| 8 | [OpenCode](human/fichas/opencode.md) | 226k | 🕸️ Frameworks & Orquestación de Agentes | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| 9 | [n8n](human/fichas/n8n.md) | 210k | 🤖 Automatización, Mensajería & CRM | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| 10 | [yt-dlp](human/fichas/yt-dlp.md) | 207k | 🕷️ Scraping, Búsqueda & Research Web | Descargador de audio y video por línea de comandos compatible con miles de sitios. |
| 11 | [firecrawl](human/fichas/firecrawl.md) | 200k | 🕷️ Scraping, Búsqueda & Research Web | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |
| 12 | [markitdown](human/fichas/markitdown.md) | 195k | 📄 Documentos & Presentaciones | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. |
| 13 | [Anthropic Skills](human/fichas/anthropic-skills.md) | 192k | 🧠 Skills, Prompts & Guías de Agente | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. |
| 14 | [Ponytail](human/fichas/ponytail.md) | 188k | 🧠 Skills, Prompts & Guías de Agente | Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribes. |
| 15 | [AutoGPT](human/fichas/autogpt.md) | 188k | 🕸️ Frameworks & Orquestación de Agentes | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. |
<!-- /BL:TOP -->

Lista completa en el [📚 Catálogo](Catalogo.md) (una línea por repo) o en la [📖 Guía completa](Guia.md) (todas las fichas en un solo documento).

## 🧪 Recetas listas

Stacks completos, paso a paso, para productos habituales:

<!-- BL:RECIPES -->
- [💬 Bot de WhatsApp con IA](human/playbooks/bot-de-whatsapp-con-ia.md) — `evolution-api`, `n8n`, `n8n-mcp`, `n8n-skills`, `chatwoot`, `novu`
- [🎬 Pipeline de Reels / video corto](human/playbooks/pipeline-de-reels-video-corto.md) — `whisperx`, `chatterbox`, `comfyui`, `real-esrgan`, `remotion`, `ffmpeg`, `moneyprinterturbo`
- [🔎 Agente de research profundo](human/playbooks/agente-de-research-profundo.md) — `gpt-researcher`, `searxng`, `crawl4ai`, `browser-use`, `markitdown`, `langfuse`
- [🏠 Workspace privado local soberano](human/playbooks/workspace-privado-local-soberano.md) — `ollama`, `odysseus`, `open-notebook`, `mem0`, `searxng`
- [🧠 Análisis de repos grandes](human/playbooks/analisis-de-repos-grandes.md) — `repomix`, `codegraph`, `gitnexus`, `graphify`, `deepwiki-open`, `claude-code`
- [📈 Marketing de agencia](human/playbooks/marketing-de-agencia.md) — `marketingskills`, `agency-agents`, `mautic`, `listmonk`, `posthog`, `open-generative-ai`
- [🌐 Web app moderna con IA](human/playbooks/web-app-moderna-con-ia.md) — `ui`, `tailwindcss`, `vercel-ai`, `assistant-ui`, `motion`, `recharts`, `swr`
- [🔌 Construir una app o servidor MCP](human/playbooks/construir-una-appservidor-mcp.md) — `awesome-mcp-servers`, `fastmcp`, `mcp-typescript-sdk`, `mcp-inspector`, `servers`, `mcp-use`
- [📊 Documentos → presentaciones](human/playbooks/documentos-presentaciones.md) — `markitdown`, `docling`, `ppt-master`, `slidev`, `marp`
- [🦙 ChatGPT privado con modelos locales](human/playbooks/chatgpt-privado-local.md) — `ollama`, `open-webui`, `searxng`, `litellm`
- [📎 RAG sobre tus documentos](human/playbooks/rag-sobre-documentos.md) — `docling`, `llama-index`, `qdrant`, `litellm`, `ragas`, `langfuse`
- [🛠️ Agente de código potenciado](human/playbooks/agente-de-codigo-potenciado.md) — `claude-code`, `superpowers`, `context7`, `serena`, `claude-mem`, `skillspector`
- [📞 Agente de voz en tiempo real](human/playbooks/agente-de-voz.md) — `pipecat`, `faster-whisper`, `litellm`, `kokoro`, `livekit-agents`
- [📊 Analítica de producto con IA](human/playbooks/analitica-con-ia.md) — `posthog`, `duckdb`, `wrenai`, `superset`, `umami`
<!-- /BL:RECIPES -->

## 🧩 Cómo leer una ficha

Cada repo tiene su ficha en [`human/fichas/`](human/fichas/) con la misma estructura:

| Sección | Te responde |
|---|---|
| **Qué es / Por qué destaca** | Qué problema resuelve y por qué es relevante |
| **Cómo funciona** | La idea técnica en dos o tres frases |
| **Instalación rápida** | El comando o los pasos para probarlo |
| **¿Es para ti?** | ✅ Elígelo si… / ⛔ Evítalo si… |
| **Combina con / Alternativas** | Qué usar junto a él y qué otros repos cumplen la misma función (elige uno) |

Etiquetas que verás: **Ejecución** 🏠 local · ☁️ nube · 🔀 híbrido. **Setup** 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios). **⭐ Imprescindible** marca la opción recomendada de su subcategoría. **🆕** marca los repos sugeridos que aún no están clonados en tu biblioteca local.

Cuando dos repos compiten por lo mismo, las [⚖️ comparativas](human/comparativas/README.md) ponen la opción recomendada frente a su rival principal, lado a lado.

---

## 🎯 Recomendación para tu proyecto

Describe tu idea (mientras más concreta, mejor) y, si quieres, con qué herramienta la vas a construir:

```powershell
uv run repo-intelligence recommend --project "bot de WhatsApp con IA para responder clientes y guardar leads. Lo voy a construir con Codex." --max-repos 7
```

Para un brief largo, escríbelo en `proyecto.md` y usa `--project-file proyecto.md`.

El resultado sale en la terminal y además genera una **superguía** del proyecto en `ai_index/SUPERGUIAS/<proyecto>.md` (con copia en `ai_index/CONTEXT_PACKS/latest.md`). Trae los finalistas, por qué entra cada uno, el orden de instalación y cómo instalar cada pieza:

| Modo | Qué significa |
|---|---|
| 🌍 `global` | Instálalo una vez en tu máquina |
| 📦 `local_project` | Instálalo dentro del proyecto |
| 🐳 `docker_local` | Levántalo con Docker cuando haga falta |
| 📖 `reference_only` | Léelo o copia ideas; no lo instales de entrada |
| ⏳ `deferred` | Pesado: solo si llega a finalista |

Dale la superguía a tu agente con algo como: *"Lee `ai_index/CONTEXT_PACKS/latest.md`, instala solo los finalistas en el orden indicado y no leas repos completos."*

`recommend` funciona solo con el índice curado. Si además tienes los repos clonados y escaneados, usa también esos datos.

## 📦 Menú portable para otro proyecto

`menu export` crea un paquete pequeño que puedes copiar a la raíz de cualquier proyecto nuevo. Una IA lo lee y elige qué instalar sin navegar por internet:

```powershell
uv run repo-intelligence menu export -o ../mi_proyecto/menu_portable
```

El punto de entrada es `menu_portable/REPO_MENU.md`. El detalle por categoría está en `REPO_MENU_cats/`.

---

## ⚙️ Instalación

Requisitos: Git, [uv](https://docs.astral.sh/uv/) y Python 3.13. Docker, Node y pnpm solo hacen falta para los repos que los pidan.

```powershell
git clone https://github.com/Cristrva1/BL_Alexandria.git
cd BL_Alexandria
uv sync --python 3.13
uv run repo-intelligence doctor
```

Rutas: el sistema espera los clones de la biblioteca en una carpeta hermana, `../Repositorios_Prueba`. Cámbiala en `config/paths.yaml` si usas otra. **No es obligatoria**: guías, explorador, `recommend` y `menu export` funcionan sin clones.

<details>
<summary>Herramientas opcionales para el análisis profundo (Windows)</summary>

```powershell
winget install -e --id Git.Git
winget install -e --id GitHub.cli
winget install -e --id OpenJS.NodeJS.LTS
winget install -e --id Docker.DockerDesktop
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
npm install -g pnpm repomix gitnexus
uv tool install "markitdown[all]"
```

Sin `uv`: `python -m venv .venv`, activa el entorno y luego `pip install -r requirements.txt` y `pip install -e .`.
</details>

## 🔧 Mantener la biblioteca

La **fuente de verdad** son dos archivos:

- `INDICE_IA.json`: índice compacto, una entrada por repo.
- `INDICE_IA.detalle.json`: la ficha completa de cada repo.

Todo lo demás se genera a partir de ellos: `Catalogo.md`, `Guia.md`, `human/`, `docs/index.html`, los bloques marcados de este README y `menu_portable/`. No edites a mano lo generado.

```powershell
uv run repo-intelligence guide build   # regenera guías, fichas, catálogo y explorador
uv run repo-intelligence menu export   # regenera el menú portable
uv run pytest                          # comprueba datos, enlaces y guías
```

Para agregar repos nuevos con datos completos:

```powershell
uv run repo-intelligence discover
uv run repo-intelligence analyze --new
uv run repo-intelligence enrich --new --auto-merge   # borradores en data/drafts/, revísalos
uv run repo-intelligence guide build
```

Para mantener los clones locales: `pull --safe` (usa red), `snapshot`, `scan --changed-only`, `score`, `conflicts` y `report daily`. El modo de instalación de cada repo se decide en `src/repo_intelligence/core/install_mode.py` con las reglas de `config/repo_policy.yaml`.

**Red y APIs:** ningún comando llama a modelos de IA. Solo `pull --safe` contacta con los remotos Git.

## 📏 Reglas de la casa

- No instales todos los repos ni catálogos completos de skills: elige finalistas.
- Si dos repos son alternativas, quédate con uno.
- No uses un framework multiagente si el problema se resuelve con un script.
- Difiere lo pesado (GPU, varios servicios) hasta que el proyecto lo justifique.
- No leas repos completos ni pases Repomix por toda la biblioteca: solo por los finalistas.
