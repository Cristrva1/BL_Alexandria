# 🤖 AGENTS.md — Punto de entrada para agentes de IA

Esta biblioteca es un menú curado de repos de IA y automatización, con datos completos para cada uno. Este archivo te dice cómo elegir los repos correctos **gastando el mínimo de tokens**. Es corto, así que léelo entero y luego abre solo lo que necesites.

<!-- BL:STATS -->
**411 repos curados** · **13 categorías** · **14 recetas** · 209 ya en tu biblioteca local + 202 sugeridos nuevos · estrellas de GitHub al 2026-11-05
<!-- /BL:STATS -->

---

## ⚡ Protocolo de selección (en orden)

0. **Si el usuario describió un proyecto concreto**, genera primero su superguía:
   `uv run repo-intelligence recommend --project "<descripción, con la herramienta si la nombra>" --max-repos 7`
   (o `--project-file proyecto.md` para briefs largos). Después lee `ai_index/CONTEXT_PACKS/latest.md`: ya trae finalistas, orden e instalación.
1. **Lee `INDICE_IA.json`**, el índice compacto con una entrada por repo. Es la única lectura obligatoria.
2. **Filtra** por `cat`/`sub` (categoría y subcategoría), `tags`, `role`, `exec`, `setup`, `prov` y el resumen `one`. `pick: true` marca la opción recomendada de su subcategoría.
3. **Desempata** con `alt`: si ya elegiste un repo, **descarta sus `alt`**, porque cumplen la misma función.
4. **Parte de una receta** (`recipes`) si el usuario quiere un producto completo y no una pieza suelta.
5. **Solo para finalistas (menos de 8)**, abre su entrada en `INDICE_IA.detalle.json` por `id`: `desc`, `why`, `how`, `install`, `choose_if`, `avoid_if`, `limits`, `combines_with`. La ficha humana equivalente está en `human/fichas/<id>.md`.

> Coste: los pasos 1 a 4 son un solo archivo. No leas `Guia.md` ni `Catalogo.md` enteros; son para humanos.

---

## 🗺️ Archivos

| Archivo | Para qué | Cuándo |
|---|---|---|
| **`AGENTS.md`** (este) | Cómo navegar | Siempre, primero |
| **`INDICE_IA.json`** | Índice compacto: id, cat, sub, role, exec, setup, mcp, prov, tags, stars, pick, one, alt | Para preseleccionar |
| **`INDICE_IA.detalle.json`** | Ficha completa por `id` | Solo finalistas |
| `ai_index/CONTEXT_PACKS/latest.md` | Última superguía generada por `recommend` | Si ya hay un proyecto descrito |
| `menu_portable/REPO_MENU.md` | Menú autocontenido para copiar a otro proyecto | Al trabajar fuera de este repo |
| `human/categorias/NN-*.md` | Categoría completa en formato humano | Lectura humana |

---

## 🧠 Regla clave: herramienta de código ≠ modelo en ejecución

- **El agente o IDE con el que se CONSTRUYE** (Claude Code, Codex, Antigravity, OpenCode…) solo importa para los repos `role = skill` o `directory` (skills, plugins, catálogos).
- **El LLM que la APP llama EN EJECUCIÓN** está en `prov` (`openai`, `anthropic`, `google`, `local`, `mcp`). La mayoría de repos runtime son agnósticos: el proveedor se configura con variables de entorno. `prov: []` significa "no declarado", no "incompatible".

<!-- BL:AGENT_TOOLS -->
| Herramienta | Repos específicos que le sirven |
|---|---|
| **Claude Code** | `claude-code`, `anthropic-skills`, `claude-plugins-official`, `superpowers`, `awesome-claude-code`, `awesome-claude-skills`, `claude-mem`, `n8n-skills`, `geo-seo-claude`, `agency-agents` — Skills en .claude/skills y plugins con /plugin marketplace. |
| **Codex** | `codex`, `agent-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`, `spec-kit`, `marketingskills`, `taste-skill` — Lee AGENTS.md y skills portables (formato Agent Skills). |
| **Antigravity** | `antigravity-awesome-skills`, `awesome-agent-skills`, `prompt-master`, `stitch-skills` |
| **Gemini CLI** | `gemini-cli`, `awesome-agent-skills`, `antigravity-awesome-skills`, `stitch-skills` |
| **OpenCode** | `opencode`, `awesome-agent-skills`, `antigravity-awesome-skills`, `prompt-master` |
| **Grok** | Sin repos específicos: úsalo como proveedor LLM en runtime (los repos agnósticos lo aceptan vía API compatible con OpenAI). |
| **DeepSeek** | `deepseek-coder` — Es el modelo; el resto es agnóstico vía proveedor compatible con OpenAI. |
<!-- /BL:AGENT_TOOLS -->

---

## 📂 Categorías

<!-- BL:AGENT_CATEGORIES -->
| # | Categoría | Repos | Subcategorías | Archivo |
|---:|---|---:|---|---|
| 1 | 🤖 Automatización, Mensajería & CRM | 32 | Motores de workflow y automatización, Ecosistema n8n, WhatsApp y mensajería, Chatbots y asistentes conversacionales, CRM, ERP y soporte al cliente, Email, marketing y notificaciones, Apps internas y bases de datos no-code | `human/categorias/01-automatizaci-n-mensajer-a-crm.md` |
| 2 | 🧠 Skills, Prompts & Guías de Agente | 38 | Catálogos y marketplaces de skills, Metodologías y harness para agentes de código, Escritura y calidad de texto, Skills de dominio: marketing, SEO y negocio, Prompts y prompt engineering, Guías, cursos y cookbooks | `human/categorias/02-skills-prompts-gu-as-de-agente.md` |
| 3 | 🕸️ Frameworks & Orquestación de Agentes | 59 | Agentes de código (terminal e IDE), Frameworks de agentes en Python, Frameworks en TypeScript y multi-lenguaje, Builders visuales y plataformas de agentes, Asistentes autónomos y equipos de agentes, Agentes de research autónomo, Infraestructura: sandboxes, herramientas y protocolos, Simulación, evolución y debate entre modelos | `human/categorias/03-frameworks-orquestaci-n-de-agentes.md` |
| 4 | 🕷️ Scraping, Búsqueda & Research Web | 29 | Crawlers y extracción para IA, Scraping guiado por LLM, Navegadores y automatización web, Búsqueda, monitoreo y research web, Redes sociales y descarga de medios | `human/categorias/04-scraping-b-squeda-research-web.md` |
| 5 | 🔌 MCP & Conectividad | 20 | SDKs y frameworks para crear MCP, Servidores MCP destacados, Directorios, clientes y aprendizaje | `human/categorias/05-mcp-conectividad.md` |
| 6 | 🧬 Memoria, RAG & LLM Ops | 32 | Memoria persistente para agentes, RAG y motores de conocimiento, Bases vectoriales y búsqueda semántica, Serving y gateways de LLM, Ahorro de contexto y tokens, Observabilidad, evaluación y guardrails | `human/categorias/06-memoria-rag-llm-ops.md` |
| 7 | 🧑‍💻 Inteligencia de Código, Datos & Entrenamiento | 34 | Entender y empaquetar código para agentes, Calidad, seguridad y benchmarks de código, Entrenar y afinar modelos, Aprender LLMs desde cero, Modelos abiertos y fundacionales, CLIs y SDKs de desarrollo, Datos y notebooks | `human/categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md` |
| 8 | 🏠 IA Local: Modelos, Chats & Workspaces | 21 | Motores para correr modelos en local, Interfaces de chat auto-hospedadas, Workspaces privados y segundos cerebros, NotebookLM: alternativas y clientes | `human/categorias/08-ia-local-modelos-chats-workspaces.md` |
| 9 | 🎨 Diseño, UI & Frontend | 34 | Componentes, iconos y sistemas de diseño, CSS y estilos, Animación y 3D, Diseño visual, canvas y builders, UI generada con IA y frontends para agentes, Skills de diseño para agentes | `human/categorias/09-dise-o-ui-frontend.md` |
| 10 | 📊 Analítica & Visualización | 20 | Analítica web y de producto, BI, dashboards y chat con datos, Librerías de gráficos, Apps de datos en Python, Recursos y casos de uso | `human/categorias/10-anal-tica-visualizaci-n.md` |
| 11 | 🖼️ Generación de Imagen & Visión | 27 | Interfaces para generar imágenes, Modelos, librerías y control, Restauración, upscaling y edición, Rostros y retratos animados, Visión por computador, Suites generativas todo-en-uno | `human/categorias/11-generaci-n-de-imagen-visi-n.md` |
| 12 | 🎬 Audio, Voz & Video | 42 | Transcripción (voz a texto), Síntesis y clonación de voz, Agentes de voz en tiempo real, Edición, grabación y subtítulos, Video programático y con agentes, Video generativo y pipelines automáticos, Música y audio generativo | `human/categorias/12-audio-voz-video.md` |
| 13 | 📄 Documentos & Presentaciones | 23 | Conversión de documentos para IA, OCR, Herramientas PDF, Presentaciones, Diagramas y documentación | `human/categorias/13-documentos-presentaciones.md` |
<!-- /BL:AGENT_CATEGORIES -->

## 🔗 Recetas

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

---

## 🏷️ Leyenda de campos

- **`role`**: `platform` (plataforma) · `runtime` (motor) · `library` (librería/SDK) · `skill` (skill/prompt) · `directory` (catálogo) · `app` (app/UI)
- **`exec`**: `local` 🏠 · `cloud` ☁️ · `hybrid` 🔀
- **`setup`**: `easy` 🟢 · `medium` 🟡 · `heavy` 🔴 (GPU o varios servicios)
- **`mcp`**: `true` si expone o consume Model Context Protocol
- **`lib`**: `true` si el repo ya está clonado en la biblioteca local; `false` = sugerido nuevo
- **`alt`**: sustitutos (elige uno) · **`combines_with`** (en detalle): complementarios (úsalos juntos)

---

## 🔧 Mantenimiento

La fuente de verdad son `INDICE_IA.json` + `INDICE_IA.detalle.json`. `Catalogo.md`, `Guia.md`, `human/`, `docs/index.html`, `menu_portable/` y los bloques `<!-- BL:* -->` de este archivo y del README se regeneran con:

```powershell
uv run repo-intelligence guide build
uv run repo-intelligence menu export
uv run pytest
```

Para agregar repos con datos completos: `discover` → `analyze --new` → `enrich --new --auto-merge` (borradores revisables en `data/drafts/`) → `guide build`. La lógica de inferencia está en `src/repo_intelligence/analysis/curation.py`.

Al editar a mano una entrada, mantén: `one` de 60 a 175 caracteres en español claro; `alt` simétrico (si A lista a B, B lista a A) y como máximo 5; ids de `alt` y `combines_with` que existan en el índice. Las pruebas lo comprueban.
