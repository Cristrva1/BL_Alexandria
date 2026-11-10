# 🌌 Guía completa de BL_Alexandria

Las **411 fichas** de la biblioteca en un solo documento, agrupadas por categoría y subcategoría. Úsala para leer de corrido o buscar con Ctrl+F; para navegar por partes usa la [guía humana](human/README.md) o el [explorador interactivo](docs/index.html).

## 🧭 Cómo leer cada ficha

- **Etiquetas:** Ejecución 🏠 local · ☁️ cloud/API · 🔀 híbrido — Rol ⚙️ plataforma · 🧩 motor · 📚 librería · 🎨 skill · 📂 catálogo · 🖥️ app — Setup 🟢 fácil · 🟡 medio · 🔴 pesado — 🔌 MCP.
- **⭐** junto al nombre: imprescindible de su subcategoría. El número de estrellas viene de GitHub.
- **Elige si / Evita si** te dicen en una línea si encaja; **Combina con** lleva a sus complementos.

## 📂 Mapa de categorías

| # | Categoría | Repos | Para qué |
|---:|---|---:|---|
| 1 | [🤖 Automatización, Mensajería & CRM](#-1-automatización-mensajería--crm) | 32 | Motores de workflow, ecosistema n8n, WhatsApp y chat, chatbots, CRM/ERP, email y apps internas. |
| 2 | [🧠 Skills, Prompts & Guías de Agente](#-2-skills-prompts--guías-de-agente) | 38 | Catálogos de skills, metodologías para agentes de código, escritura sin 'slop', prompts, cursos y cookbooks. |
| 3 | [🕸️ Frameworks & Orquestación de Agentes](#️-3-frameworks--orquestación-de-agentes) | 59 | Agentes de código, frameworks multiagente en Python y TypeScript, builders visuales, asistentes autónomos, research e infraestructura. |
| 4 | [🕷️ Scraping, Búsqueda & Research Web](#️-4-scraping-búsqueda--research-web) | 29 | Crawlers que entregan Markdown para IA, scraping guiado por LLM, navegadores automatizados, buscadores y redes sociales. |
| 5 | [🔌 MCP & Conectividad](#-5-mcp--conectividad) | 20 | SDKs para crear servidores MCP, servidores destacados (navegador, GitHub, diseño, 3D), directorios y APIs públicas. |
| 6 | [🧬 Memoria, RAG & LLM Ops](#-6-memoria-rag--llm-ops) | 32 | Memoria persistente para agentes, RAG, bases vectoriales, serving y gateways de LLM, ahorro de tokens y observabilidad. |
| 7 | [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](#-7-inteligencia-de-código-datos--entrenamiento) | 34 | Entender y empaquetar codebases para agentes, calidad de código, entrenar y afinar modelos, modelos abiertos y herramientas de datos. |
| 8 | [🏠 IA Local: Modelos, Chats & Workspaces](#-8-ia-local-modelos-chats--workspaces) | 21 | Correr LLMs en tu máquina, interfaces tipo ChatGPT auto-hospedadas, workspaces privados y alternativas a NotebookLM. |
| 9 | [🎨 Diseño, UI & Frontend](#-9-diseño-ui--frontend) | 34 | Componentes y sistemas de diseño, CSS, animación y 3D, canvas y builders, UI generada con IA y skills de diseño para agentes. |
| 10 | [📊 Analítica & Visualización](#-10-analítica--visualización) | 20 | Analítica web y de producto, BI y dashboards, chat con tus datos, librerías de gráficos y apps de datos en Python. |
| 11 | [🖼️ Generación de Imagen & Visión](#️-11-generación-de-imagen--visión) | 27 | Interfaces de difusión, modelos y control, restauración y upscaling, rostros y visión por computador. |
| 12 | [🎬 Audio, Voz & Video](#-12-audio-voz--video) | 42 | Transcripción, síntesis y clonación de voz, agentes de voz, edición y subtítulos, video programático, video generativo y música. |
| 13 | [📄 Documentos & Presentaciones](#-13-documentos--presentaciones) | 23 | Convertir documentos a Markdown/JSON para IA, OCR, herramientas PDF, presentaciones y diagramas. |

## 🧪 Recetas de integración

- **[💬 Bot de WhatsApp con IA](human/playbooks/bot-de-whatsapp-con-ia.md)** — Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta. [evolution-api](human/fichas/evolution-api.md) → [n8n](human/fichas/n8n.md) → [n8n-mcp](human/fichas/n8n-mcp.md) → [n8n-skills](human/fichas/n8n-skills.md) → [chatwoot](human/fichas/chatwoot.md) → [novu](human/fichas/novu.md)
- **[🎬 Pipeline de Reels / video corto](human/playbooks/pipeline-de-reels-video-corto.md)** — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados. [whisperX](human/fichas/whisperx.md) → [Chatterbox](human/fichas/chatterbox.md) → [ComfyUI](human/fichas/comfyui.md) → [Real-ESRGAN](human/fichas/real-esrgan.md) → [remotion](human/fichas/remotion.md) → [FFmpeg](human/fichas/ffmpeg.md) → [MoneyPrinterTurbo](human/fichas/moneyprinterturbo.md)
- **[🔎 Agente de research profundo](human/playbooks/agente-de-research-profundo.md)** — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas. [gpt-researcher](human/fichas/gpt-researcher.md) → [SearXNG](human/fichas/searxng.md) → [crawl4ai](human/fichas/crawl4ai.md) → [browser-use](human/fichas/browser-use.md) → [markitdown](human/fichas/markitdown.md) → [langfuse](human/fichas/langfuse.md)
- **[🏠 Workspace privado local soberano](human/playbooks/workspace-privado-local-soberano.md)** — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros. [Ollama](human/fichas/ollama.md) → [odysseus](human/fichas/odysseus.md) → [open-notebook](human/fichas/open-notebook.md) → [mem0](human/fichas/mem0.md) → [SearXNG](human/fichas/searxng.md)
- **[🧠 Análisis de repos grandes](human/playbooks/analisis-de-repos-grandes.md)** — Que un agente de código entienda una base de código enorme sin gastar todo su contexto. [Repomix](human/fichas/repomix.md) → [codegraph](human/fichas/codegraph.md) → [GitNexus](human/fichas/gitnexus.md) → [graphify](human/fichas/graphify.md) → [DeepWiki Open](human/fichas/deepwiki-open.md) → [Claude Code](human/fichas/claude-code.md)
- **[📈 Marketing de agencia](human/playbooks/marketing-de-agencia.md)** — Operar campañas, contenido y email a escala con agentes y herramientas propias. [Marketing Skills](human/fichas/marketingskills.md) → [The Agency (agency-agents)](human/fichas/agency-agents.md) → [mautic](human/fichas/mautic.md) → [listmonk](human/fichas/listmonk.md) → [posthog](human/fichas/posthog.md) → [Open-Generative-AI](human/fichas/open-generative-ai.md)
- **[🌐 Web app moderna con IA](human/playbooks/web-app-moderna-con-ia.md)** — Construir un frontend pulido con chat o funciones de IA integradas. [ui](human/fichas/ui.md) → [tailwindcss](human/fichas/tailwindcss.md) → [AI SDK (Vercel)](human/fichas/vercel-ai.md) → [assistant-ui](human/fichas/assistant-ui.md) → [motion](human/fichas/motion.md) → [Recharts](human/fichas/recharts.md) → [swr](human/fichas/swr.md)
- **[🔌 Construir una app o servidor MCP](human/playbooks/construir-una-appservidor-mcp.md)** — Exponer tus datos o herramientas a Claude, ChatGPT, Cursor y otros agentes con Model Context Protocol. [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md) → [FastMCP](human/fichas/fastmcp.md) → [MCP TypeScript SDK](human/fichas/mcp-typescript-sdk.md) → [MCP Inspector](human/fichas/mcp-inspector.md) → [servers](human/fichas/servers.md) → [mcp-use](human/fichas/mcp-use.md)
- **[📊 Documentos → presentaciones](human/playbooks/documentos-presentaciones.md)** — Pasar informes, PDFs o notas a presentaciones editables o slides web. [markitdown](human/fichas/markitdown.md) → [Docling](human/fichas/docling.md) → [ppt-master](human/fichas/ppt-master.md) → [Slidev](human/fichas/slidev.md) → [Marp](human/fichas/marp.md)
- **[🦙 ChatGPT privado con modelos locales](human/playbooks/chatgpt-privado-local.md)** — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor. [Ollama](human/fichas/ollama.md) → [Open WebUI](human/fichas/open-webui.md) → [SearXNG](human/fichas/searxng.md) → [litellm](human/fichas/litellm.md)
- **[📎 RAG sobre tus documentos](human/playbooks/rag-sobre-documentos.md)** — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas. [Docling](human/fichas/docling.md) → [LlamaIndex](human/fichas/llama-index.md) → [Qdrant](human/fichas/qdrant.md) → [litellm](human/fichas/litellm.md) → [Ragas](human/fichas/ragas.md) → [langfuse](human/fichas/langfuse.md)
- **[🛠️ Agente de código potenciado](human/playbooks/agente-de-codigo-potenciado.md)** — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria. [Claude Code](human/fichas/claude-code.md) → [superpowers](human/fichas/superpowers.md) → [Context7](human/fichas/context7.md) → [Serena](human/fichas/serena.md) → [claude-mem](human/fichas/claude-mem.md) → [SkillSpector](human/fichas/skillspector.md)
- **[📞 Agente de voz en tiempo real](human/playbooks/agente-de-voz.md)** — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono. [Pipecat](human/fichas/pipecat.md) → [faster-whisper](human/fichas/faster-whisper.md) → [litellm](human/fichas/litellm.md) → [Kokoro](human/fichas/kokoro.md) → [LiveKit Agents](human/fichas/livekit-agents.md)
- **[📊 Analítica de producto con IA](human/playbooks/analitica-con-ia.md)** — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural. [posthog](human/fichas/posthog.md) → [DuckDB](human/fichas/duckdb.md) → [WrenAI](human/fichas/wrenai.md) → [Apache Superset](human/fichas/superset.md) → [Umami](human/fichas/umami.md)

---

## 🤖 1. Automatización, Mensajería & CRM

Motores de workflow, ecosistema n8n, WhatsApp y chat, chatbots, CRM/ERP, email y apps internas.

**⚖️ ¿Cuál elegir? — n8n, huginn, Kestra, activepieces, Node-RED, Windmill, Trigger.dev**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [n8n](human/fichas/n8n.md) | quieres el motor central de automatización con máximo catálogo | buscas algo minimalista o sin self-host |
| [huginn](human/fichas/huginn.md) | automatizas tareas orientadas a eventos y valoras la privacidad | quieres editor visual moderno o IA nativa (n8n) |
| [Kestra](human/fichas/kestra.md) | quieres workflows declarativos en YAML con UI y control de versiones | buscas automatizaciones de negocio con nodos visuales; mira `n8n` |
| [activepieces](human/fichas/activepieces.md) | quieres reemplazar Zapier con piezas propias en TypeScript | ya dominas n8n y su ecosistema te basta |
| [Node-RED](human/fichas/node-red.md) | trabajas con IoT o eventos y quieres algo ligero y probado | necesitas integraciones SaaS y nodos de IA listos; mira `n8n` |
| [Windmill](human/fichas/windmill.md) | tu equipo programa y quiere workflows versionados en código | prefieres arrastrar nodos sin escribir código; mira `n8n` |
| [Trigger.dev](human/fichas/trigger-dev.md) | tu app es TypeScript y necesitas tareas largas confiables sin montar colas | quieres un editor visual para no programadores; mira `n8n` |

**⚖️ ¿Cuál elegir? — whatsapp-web.js, Baileys, evolution-api, WAHA**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [whatsapp-web.js](human/fichas/whatsapp-web-js.md) | quieres programar un bot de WhatsApp en Node rápido | necesitas una API REST multi-sesión lista; mira `evolution-api` o `waha` |
| [Baileys](human/fichas/baileys.md) | necesitas WhatsApp en código con bajo consumo de recursos | prefieres una API REST lista; mira `evolution-api` |
| [evolution-api](human/fichas/evolution-api.md) | operas WhatsApp en producción con varias instancias | solo necesitas un bot de prueba o un único script (OpenWA basta) |
| [WAHA](human/fichas/waha.md) | quieres una API REST de WhatsApp lista en minutos | necesitas multi-instancia avanzada gratis; mira `evolution-api` |

**⚖️ ¿Cuál elegir? — Typebot, Rasa, Botpress**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Typebot](human/fichas/typebot.md) | quieres un chatbot guiado sin programar, con buena UX | necesitas un agente abierto con razonamiento libre; mira `botpress` |
| [Rasa](human/fichas/rasa.md) | necesitas un asistente on-premise con diálogo muy controlado | quieres algo rápido con LLM y sin entrenar; mira `botpress` o `typebot` |
| [Botpress](human/fichas/botpress.md) | quieres un agente conversacional multicanal con poco código | necesitas todo self-host y sin nube; mira `rasa` o `typebot` |

**⚖️ ¿Cuál elegir? — Odoo, ERPNext**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Odoo](human/fichas/odoo.md) | necesitas un ERP completo con CRM integrado | solo quieres un CRM ligero; mira `twenty-main` |
| [ERPNext](human/fichas/erpnext.md) | quieres un ERP completo y totalmente libre | buscas el mayor ecosistema de módulos; mira `odoo` |

**⚖️ ¿Cuál elegir? — NocoDB, ToolJet, Appsmith, Budibase**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [NocoDB](human/fichas/nocodb.md) | quieres un Airtable propio sobre tu base de datos | necesitas apps internas con lógica compleja; mira `appsmith` |
| [ToolJet](human/fichas/tooljet.md) | quieres herramientas internas con IA para generarlas | prefieres un proyecto con licencia más permisiva; mira `appsmith` |
| [Appsmith](human/fichas/appsmith.md) | necesitas herramientas internas con lógica y muchas fuentes de datos | solo quieres hojas colaborativas; mira `nocodb` |
| [Budibase](human/fichas/budibase.md) | quieres apps internas y agentes en una sola plataforma self-host | buscas el editor más flexible para backoffices; mira `appsmith` |

### Motores de workflow y automatización

#### 🔁 n8n ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 210k  
**Qué es:** Conecta cualquier app con cualquier otra en tu propio servidor, sin pagar una suscripción mensual por cada flujo.  
**Instalación:** Vía `docker compose` o imagen Docker oficial; también `npx n8n` para una prueba rápida local. Requiere una base de datos (SQLite por defecto, PostgreSQL para producción).  
**Elige si:** quieres el motor central de automatización con máximo catálogo — **Evita si:** buscas algo minimalista o sin self-host  
**Combina con:** [n8n-mcp](human/fichas/n8n-mcp.md) · [n8n-skills](human/fichas/n8n-skills.md) · [evolution-api](human/fichas/evolution-api.md)  
**Más:** [ficha completa](human/fichas/n8n.md) · [GitHub](https://github.com/n8n-io/n8n)

#### 🤖 huginn
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 50.5k  
**Qué es:** Vigila webs, feeds y APIs y dispara acciones cuando algo cambia, todo alojado por ti y sin depender de terceros.  
**Instalación:** Vía `docker` (imagen oficial) o desplegando la app Rails manualmente; requiere MySQL/PostgreSQL y un entorno Ruby.  
**Elige si:** automatizas tareas orientadas a eventos y valoras la privacidad — **Evita si:** quieres editor visual moderno o IA nativa (n8n)  
**Combina con:** [novu](human/fichas/novu.md)  
**Más:** [ficha completa](human/fichas/huginn.md) · [GitHub](https://github.com/huginn/huginn)

#### 🔁 Kestra
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.2k  
**Qué es:** Define flujos en YAML con un editor web, cientos de plugins y disparadores por calendario o eventos. Pensado para equipos de datos y plataforma que quieren orquestación como código.  
**Instalación:** `docker run --pull=always -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock kestra/kestra:latest server local`.  
**Elige si:** quieres workflows declarativos en YAML con UI y control de versiones — **Evita si:** buscas automatizaciones de negocio con nodos visuales; mira `n8n`  
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [Apache Superset](human/fichas/superset.md)  
**Más:** [ficha completa](human/fichas/kestra.md) · [GitHub](https://github.com/kestra-io/kestra)

#### 🧩 activepieces
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 25.5k  
**Qué es:** Orquesta tus apps con flujos visuales sin código y conserva el control al alojarlo en tu servidor.  
**Instalación:** Vía `docker compose` para self-host, o usando su versión cloud si prefieres no operar la infra; requiere Node.js y una base de datos para el modo local.  
**Elige si:** quieres reemplazar Zapier con piezas propias en TypeScript — **Evita si:** ya dominas n8n y su ecosistema te basta  
**Combina con:** [novu](human/fichas/novu.md)  
**Más:** [ficha completa](human/fichas/activepieces.md) · [GitHub](https://github.com/activepieces/activepieces)

#### 🔁 Node-RED
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 23.8k  
**Qué es:** Conecta dispositivos, APIs y servicios arrastrando nodos en el navegador. Es muy usado en IoT, domótica e industria por su ligereza y su enorme biblioteca de nodos de la comunidad.  
**Instalación:** `npm install -g --unsafe-perm node-red` y luego `node-red`, o `docker run -it -p 1880:1880 nodered/node-red`.  
**Elige si:** trabajas con IoT o eventos y quieres algo ligero y probado — **Evita si:** necesitas integraciones SaaS y nodos de IA listos; mira `n8n`  
**Más:** [ficha completa](human/fichas/node-red.md) · [GitHub](https://github.com/node-red/node-red)

#### 🔁 Windmill
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.5k  
**Qué es:** Convierte scripts de Python, TypeScript, Go o SQL en workflows, endpoints y apps con UI generada. Sirve a equipos técnicos que quieren la flexibilidad del código con la comodidad de un orquestador visual.  
**Instalación:** `docker compose up -d` con el `docker-compose.yml` del repo (incluye PostgreSQL); abre `http://localhost`.  
**Elige si:** tu equipo programa y quiere workflows versionados en código — **Evita si:** prefieres arrastrar nodos sin escribir código; mira `n8n`  
**Combina con:** [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/windmill.md) · [GitHub](https://github.com/windmill-labs/windmill)

#### 🔁 Trigger.dev
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 16.7k  
**Qué es:** Escribe tareas largas o con reintentos en TypeScript dentro de tu app y Trigger.dev las ejecuta, reintenta y monitorea. Ideal para equipos de producto con Next.js o Node que no quieren operar colas.  
**Instalación:** `npx trigger.dev@latest init` dentro de tu proyecto; se usa con su cloud o en self-host con Docker.  
**Elige si:** tu app es TypeScript y necesitas tareas largas confiables sin montar colas — **Evita si:** quieres un editor visual para no programadores; mira `n8n`  
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md) · [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/trigger-dev.md) · [GitHub](https://github.com/triggerdotdev/trigger.dev)

### Ecosistema n8n

#### 🔁 Self-hosted AI Starter Kit ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 15.3k  
**Qué es:** Kit oficial de n8n que levanta un entorno de IA privado: n8n para orquestar, Ollama para modelos, Qdrant como base vectorial y PostgreSQL. Útil para prototipar agentes y RAG sin enviar datos fuera.  
**Instalación:** `git clone https://github.com/n8n-io/self-hosted-ai-starter-kit` y `docker compose --profile cpu up` (o `gpu-nvidia`).  
**Elige si:** quieres un stack de IA local funcionando hoy con n8n — **Evita si:** vas a producción con alta carga; arma tu propio despliegue  
**Combina con:** [n8n](human/fichas/n8n.md) · [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md)  
**Más:** [ficha completa](human/fichas/self-hosted-ai-starter-kit.md) · [GitHub](https://github.com/n8n-io/self-hosted-ai-starter-kit)

#### 🔁 Awesome n8n Templates
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 26.3k  
**Qué es:** Reúne workflows de n8n ordenados por tema (Gmail, Telegram, WhatsApp, Notion, OpenAI y más). Sirve para arrancar rápido y aprender patrones de automatización.  
**Instalación:** No se instala: abre el repo, descarga el JSON y usa Import from File en n8n.  
**Elige si:** usas n8n y quieres partir de flujos hechos — **Evita si:** no usas n8n  
**Combina con:** [n8n](human/fichas/n8n.md) · [n8n-mcp](human/fichas/n8n-mcp.md) · [n8n-skills](human/fichas/n8n-skills.md)  
**Más:** [ficha completa](human/fichas/awesome-n8n-templates.md) · [GitHub](https://github.com/enescingoz/awesome-n8n-templates)

#### 🔌 n8n-mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 23.2k  
**Qué es:** Resuelve el problema de que un LLM invente parámetros de nodos que no existen y genere workflows rotos.  
**Instalación:** `npx n8n-mcp` y añadirlo a la config del cliente MCP (p. ej. Claude Desktop). Requiere Node.js y, para flujos reales, una instancia n8n accesible.  
**Elige si:** generas flujos n8n con IA y quieres menos alucinaciones de parámetros — **Evita si:** no usas n8n o construyes los flujos a mano  
**Combina con:** [n8n](human/fichas/n8n.md) · [n8n-skills](human/fichas/n8n-skills.md)  
**Más:** [ficha completa](human/fichas/n8n-mcp.md) · [GitHub](https://github.com/czlonkowski/n8n-mcp)

#### 🛠️ n8n-skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 6.6k  
**Qué es:** Enseña a tu agente de código a escribir flujos de n8n en JSON que funcionan a la primera, con menos idas y vueltas de errores.  
**Instalación:** Clona el repo y copia las skills (`SKILL.md`) a tu directorio de skills de Claude Code u otro asistente compatible; sin dependencias.  
**Elige si:** generas workflows n8n con IA y te cansan los fallos de JSON — **Evita si:** no usas n8n  
**Combina con:** [n8n](human/fichas/n8n.md) · [n8n-mcp](human/fichas/n8n-mcp.md)  
**Más:** [ficha completa](human/fichas/n8n-skills.md) · [GitHub](https://github.com/czlonkowski/n8n-skills)

### WhatsApp y mensajería

#### 💬 whatsapp-web.js ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 22.9k  
**Qué es:** Permite enviar y recibir mensajes, medios y grupos desde código usando una sesión de WhatsApp Web. Muy usada para bots y prototipos.  
**Instalación:** `npm i whatsapp-web.js` y escanea el QR que muestra al arrancar.  
**Elige si:** quieres programar un bot de WhatsApp en Node rápido — **Evita si:** necesitas una API REST multi-sesión lista; mira `evolution-api` o `waha`  
**Combina con:** [n8n](human/fichas/n8n.md) · [chatwoot](human/fichas/chatwoot.md)  
**Más:** [ficha completa](human/fichas/whatsapp-web-js.md) · [GitHub](https://github.com/wwebjs/whatsapp-web.js)

#### 🌐 OpenWA
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 16.7k  
**Qué es:** Envía y recibe mensajes de WhatsApp desde tu propio script con una API sencilla y expresiva.  
**Instalación:** Vía `npm i @open-wa/wa-automate` en proyectos Node.js (o el paquete equivalente para Python); requiere un entorno con navegador headless para la sesión.  
**Elige si:** desarrollas scripts o bots individuales y quieres arrancar rápido — **Evita si:** necesitas infra multi-instancia o alta disponibilidad (evolution-api)  
**Combina con:** [n8n](human/fichas/n8n.md) · [evolution-api](human/fichas/evolution-api.md)  
**Más:** [ficha completa](human/fichas/openwa.md) · [GitHub](https://github.com/rmyndharis/OpenWA)

#### 💬 Baileys
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 11.6k  
**Qué es:** Implementa el protocolo de WhatsApp Web directamente, así que consume muy pocos recursos. Es la base de muchas APIs de WhatsApp, incluida Evolution API.  
**Instalación:** `npm i baileys` y vincula la sesión con QR o código de emparejamiento.  
**Elige si:** necesitas WhatsApp en código con bajo consumo de recursos — **Evita si:** prefieres una API REST lista; mira `evolution-api`  
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/baileys.md) · [GitHub](https://github.com/WhiskeySockets/Baileys)

#### 🌐 fluxer
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 10.8k  
**Qué es:** Apunta a unificar varios modelos generativos tras un cliente único.  
**Instalación:** Descargar el cliente Canary (web/desktop) o `git clone` del repo y compilar con el toolchain de Node/TS; self-host sujeto a cambios. No hay paquete estable publicado.  
**Elige si:** quieres probar algo nuevo y seguir su evolución — **Evita si:** necesitas estabilidad de producción (API aún en finalización)  
**Combina con:** [Open-Generative-AI](human/fichas/open-generative-ai.md)  
**Más:** [ficha completa](human/fichas/fluxer.md) · [GitHub](https://github.com/fluxerapp/fluxer)

#### 🧬 evolution-api
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 10.1k  
**Qué es:** Conecta WhatsApp a tu stack mediante una API REST propia, sin quedar atado a un proveedor cerrado.  
**Instalación:** Despliegue habitual con `docker compose` usando la imagen oficial, configurando variables de entorno y Redis; requiere mantener las sesiones de WhatsApp activas.  
**Elige si:** operas WhatsApp en producción con varias instancias — **Evita si:** solo necesitas un bot de prueba o un único script (OpenWA basta)  
**Combina con:** [n8n](human/fichas/n8n.md) · [chatwoot](human/fichas/chatwoot.md)  
**Más:** [ficha completa](human/fichas/evolution-api.md) · [GitHub](https://github.com/evolution-foundation/evolution-api)

#### 💬 WAHA
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 7.8k  
**Qué es:** Expone WhatsApp como API HTTP con webhooks, lista para conectar a n8n o a tu backend. Ofrece motores basados en navegador o en WebSocket.  
**Instalación:** `docker run -it -p 3000:3000 devlikeapro/waha` y abre `http://localhost:3000`.  
**Elige si:** quieres una API REST de WhatsApp lista en minutos — **Evita si:** necesitas multi-instancia avanzada gratis; mira `evolution-api`  
**Combina con:** [n8n](human/fichas/n8n.md) · [chatwoot](human/fichas/chatwoot.md)  
**Más:** [ficha completa](human/fichas/waha.md) · [GitHub](https://github.com/devlikeapro/waha)

#### 🤖 whatsapp-agentkit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 554  
**Qué es:** Arranca un bot de WhatsApp con IA sin escribir código, a partir de una plantilla guiada.  
**Instalación:** `git clone` del repo y seguir el asistente con Claude Code; requiere una clave API de Anthropic y una cuenta/instancia de WhatsApp para el webhook.  
**Elige si:** quieres arrancar sin partir de cero y te vale con lo que Claude Code genere — **Evita si:** necesitas control fino del stack o ya tienes el bot hecho  
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [n8n-mcp](human/fichas/n8n-mcp.md)  
**Más:** [ficha completa](human/fichas/whatsapp-agentkit.md) · [GitHub](https://github.com/Hainrixz/whatsapp-agentkit)

### Chatbots y asistentes conversacionales

#### 🤖 Typebot ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 10.6k  
**Qué es:** Diseña conversaciones con bloques arrastrables (preguntas, condiciones, integraciones, IA) y publícalas en web o WhatsApp. Pensado para captar leads y formularios conversacionales.  
**Instalación:** Self-host con Docker Compose siguiendo la guía del repo (requiere PostgreSQL y SMTP), o usa su cloud.  
**Elige si:** quieres un chatbot guiado sin programar, con buena UX — **Evita si:** necesitas un agente abierto con razonamiento libre; mira `botpress`  
**Combina con:** [n8n](human/fichas/n8n.md) · [evolution-api](human/fichas/evolution-api.md)  
**Más:** [ficha completa](human/fichas/typebot.md) · [GitHub](https://github.com/baptisteArno/typebot.io)

#### 🤖 Rasa
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 21.4k  
**Qué es:** Permite crear asistentes de texto y voz con control total del diálogo y de los datos. Muy usado en empresas que necesitan bots on-premise y predecibles.  
**Instalación:** `pip install rasa` y `rasa init`; las versiones nuevas (Rasa Pro) requieren licencia.  
**Elige si:** necesitas un asistente on-premise con diálogo muy controlado — **Evita si:** quieres algo rápido con LLM y sin entrenar; mira `botpress` o `typebot`  
**Combina con:** [chatwoot](human/fichas/chatwoot.md)  
**Más:** [ficha completa](human/fichas/rasa.md) · [GitHub](https://github.com/RasaHQ/rasa)

#### 🤖 Botpress
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 15k  
**Qué es:** Combina un estudio visual con código para crear agentes que usan bases de conocimiento, herramientas y canales. Su producto principal hoy es cloud; el repo contiene SDK, integraciones y CLI.  
**Instalación:** `npm i -g @botpress/cli` y despliega con `bp deploy`; el Studio se usa en su cloud.  
**Elige si:** quieres un agente conversacional multicanal con poco código — **Evita si:** necesitas todo self-host y sin nube; mira `rasa` o `typebot`  
**Combina con:** [chatwoot](human/fichas/chatwoot.md) · [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/botpress.md) · [GitHub](https://github.com/botpress/botpress)

### CRM, ERP y soporte al cliente

#### 👥 Odoo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 55.7k  
**Qué es:** Integra CRM, ventas, facturación, inventario, RR. HH. y sitio web en una sola plataforma modular. La usan pymes y grandes empresas en todo el mundo.  
**Instalación:** `docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:16` y `docker run -p 8069:8069 --link db:db odoo`.  
**Elige si:** necesitas un ERP completo con CRM integrado — **Evita si:** solo quieres un CRM ligero; mira `twenty-main`  
**Combina con:** [n8n](human/fichas/n8n.md) · [metabase](human/fichas/metabase.md)  
**Más:** [ficha completa](human/fichas/odoo.md) · [GitHub](https://github.com/odoo/odoo)

#### 👥 twenty-main
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 60.7k  
**Qué es:** La premisa es tratar el CRM como una pieza más de tu stack: lo construyes, lo despliegas y lo versionas igual que el código.  
**Instalación:** La vía soportada es `docker compose` con la imagen oficial (levanta app, base de datos y worker); también puedes clonar el repo y arrancar los servicios con el stack Node/PostgreSQL para desarrollo. Requiere PostgreSQL y recursos no triviales (de ahí el setup 🔴).  
**Elige si:** quieres un CRM que se adapte 1:1 a tu negocio y vivir en self-host — **Evita si:** buscas algo plug-and-play gestionado o no quieres operar PostgreSQL y Docker  
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/twenty-main.md) · [GitHub](https://github.com/twentyhq/twenty)

#### 👥 ERPNext
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 41.1k  
**Qué es:** Cubre la operación completa de una empresa sin licencias de pago. Muy usado por pymes y en manufactura y distribución.  
**Instalación:** `git clone https://github.com/frappe/frappe_docker` y `docker compose -f pwd.yml up -d` para una prueba.  
**Elige si:** quieres un ERP completo y totalmente libre — **Evita si:** buscas el mayor ecosistema de módulos; mira `odoo`  
**Combina con:** [n8n](human/fichas/n8n.md) · [metabase](human/fichas/metabase.md)  
**Más:** [ficha completa](human/fichas/erpnext.md) · [GitHub](https://github.com/frappe/erpnext)

#### 💬 chatwoot
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 39.5k  
**Qué es:** Reúne WhatsApp, email, web chat y redes en una sola bandeja, con paso a un humano cuando el bot no basta. Alternativa abierta a Intercom o Zendesk.  
**Instalación:** Vía `docker compose` con la imagen oficial, o instalación manual del stack Rails; requiere PostgreSQL y Redis.  
**Elige si:** das soporte por varios canales y necesitas handoff humano — **Evita si:** solo necesitas enviar mensajes salientes (evolution-api)  
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [novu](human/fichas/novu.md)  
**Más:** [ficha completa](human/fichas/chatwoot.md) · [GitHub](https://github.com/chatwoot/chatwoot)

### Email, marketing y notificaciones

#### 🔔 novu ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 40.3k  
**Qué es:** Envía notificaciones por email, SMS, push y chat desde una sola API, sin integrar y mantener cada proveedor por separado.  
**Instalación:** Vía `docker compose` para self-host, o usando su plataforma cloud; el modo local requiere MongoDB/PostgreSQL y Redis.  
**Elige si:** envías notificaciones por varios canales y quieres un único backend — **Evita si:** solo necesitas email (listmonk)  
**Combina con:** [chatwoot](human/fichas/chatwoot.md) · [activepieces](human/fichas/activepieces.md)  
**Más:** [ficha completa](human/fichas/novu.md) · [GitHub](https://github.com/novuhq/novu)

#### 📬 listmonk
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 24.2k  
**Qué es:** Envía newsletters y campañas a miles de suscriptores desde un solo binario ligero que consume muy pocos recursos.  
**Instalación:** Vía `docker compose` o descargando el binario único de Go y apuntándolo a PostgreSQL; requiere un servidor SMTP (o servicio como SES) para los envíos.  
**Elige si:** quieres email marketing simple, rápido y propio — **Evita si:** necesitas nurturing avanzado o scoring de leads (mautic)  
**Combina con:** [mautic](human/fichas/mautic.md) · [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/listmonk.md) · [GitHub](https://github.com/knadh/listmonk)

#### 📣 mautic
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 11k  
**Qué es:** Nutre leads por email con reglas y segmentos automáticos, sin ceder los datos de tus clientes a un SaaS.  
**Instalación:** Vía `docker compose` o instalación PHP/MySQL tradicional sobre un servidor web; requiere MySQL y un MTA o servicio SMTP para los envíos.  
**Elige si:** necesitas automatización de marketing seria y soberana — **Evita si:** te basta una newsletter simple (listmonk)  
**Combina con:** [listmonk](human/fichas/listmonk.md) · [Marketing Skills](human/fichas/marketingskills.md)  
**Más:** [ficha completa](human/fichas/mautic.md) · [GitHub](https://github.com/mautic/mautic)

### Apps internas y bases de datos no-code

#### 🧱 NocoDB ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 65.5k  
**Qué es:** Ofrece vistas de tabla, kanban, galería y formularios sobre PostgreSQL, MySQL o SQLite, con API REST automática. Útil como backoffice rápido para equipos no técnicos.  
**Instalación:** `docker run -d -p 8080:8080 nocodb/nocodb:latest`.  
**Elige si:** quieres un Airtable propio sobre tu base de datos — **Evita si:** necesitas apps internas con lógica compleja; mira `appsmith`  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/nocodb.md) · [GitHub](https://github.com/nocodb/nocodb)

#### 🧱 ToolJet
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 41.2k  
**Qué es:** Construye apps internas arrastrando componentes y conectando bases y APIs, o genéralas describiéndolas con IA. Pensada para equipos de operaciones y TI.  
**Instalación:** `docker run -p 80:80 tooljet/try:ee-lts-latest` para probar; para producción usa su Docker Compose.  
**Elige si:** quieres herramientas internas con IA para generarlas — **Evita si:** prefieres un proyecto con licencia más permisiva; mira `appsmith`  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/tooljet.md) · [GitHub](https://github.com/ToolJet/ToolJet)

#### 🧱 Appsmith
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 41.2k  
**Qué es:** Arrastra widgets, conéctalos a más de 25 bases de datos o cualquier API y añade lógica en JavaScript. Pensada para equipos que construyen backoffices rápido.  
**Instalación:** `docker run -d --name appsmith -p 80:80 -v "$PWD/stacks:/appsmith-stacks" appsmith/appsmith-ce`.  
**Elige si:** necesitas herramientas internas con lógica y muchas fuentes de datos — **Evita si:** solo quieres hojas colaborativas; mira `nocodb`  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/appsmith.md) · [GitHub](https://github.com/appsmithorg/appsmith)

#### 🧱 Budibase
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 28.4k  
**Qué es:** Genera apps CRUD, formularios y flujos a partir de bases existentes y ahora añade agentes de IA agnósticos de modelo. Pensada para equipos de operaciones.  
**Instalación:** `docker run -d -p 10000:80 budibase/budibase:latest`.  
**Elige si:** quieres apps internas y agentes en una sola plataforma self-host — **Evita si:** buscas el editor más flexible para backoffices; mira `appsmith`  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/budibase.md) · [GitHub](https://github.com/Budibase/budibase)

---

## 🧠 2. Skills, Prompts & Guías de Agente

Catálogos de skills, metodologías para agentes de código, escritura sin 'slop', prompts, cursos y cookbooks.

**⚖️ ¿Cuál elegir? — Claude Code Plugins Directory, The Agency (agency-agents), Awesome Claude Skills, Awesome Claude Code, Agentic Awesome Skills, wshobson/agents, Awesome Agent Skills**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) | usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando | buscas recursos comunitarios o trabajas con otro agente; mira `awesome-claude-code` o `wshobson-agents` |
| [The Agency (agency-agents)](human/fichas/agency-agents.md) | quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código | solo necesitas skills de marketing y growth; mira `marketingskills` |
| [Awesome Claude Skills](human/fichas/awesome-claude-skills.md) | usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo | solo quieres skills de procedencia oficial; mira `anthropic-skills` o `awesome-agent-skills` |
| [Awesome Claude Code](human/fichas/awesome-claude-code.md) | usas Claude Code a diario y quieres descubrir herramientas y flujos probados por la comunidad | trabajas con otro agente o solo quieres plugins oficiales; mira `claude-plugins-official` o `awesome-agent-skills` |
| [Agentic Awesome Skills](human/fichas/antigravity-awesome-skills.md) | quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código | prefieres pocas skills oficiales y revisadas; mira `anthropic-skills` o `awesome-agent-skills` |
| [wshobson/agents](human/fichas/wshobson-agents.md) | quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin | solo quieres plugins oficiales de Anthropic y socios; mira `claude-plugins-official` |
| [Awesome Agent Skills](human/fichas/awesome-agent-skills.md) | quieres skills con procedencia clara, publicadas por el equipo que mantiene cada herramienta | prefieres instalar un lote grande con un solo comando; mira `antigravity-awesome-skills` |

**⚖️ ¿Cuál elegir? — Agent Skills (Addy Osmani), superpowers**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Agent Skills (Addy Osmani)](human/fichas/agent-skills.md) | quieres skills de ingeniería web de calidad para tu agente | buscas un catálogo enorme de skills de todo tipo; mira `antigravity-awesome-skills` |
| [superpowers](human/fichas/superpowers.md) | quieres método, no fragmentos sueltos | solo necesitas una skill aislada puntual |

**⚖️ ¿Cuál elegir? — Spec Kit, BMAD Method**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Spec Kit](human/fichas/spec-kit.md) | quieres que el agente siga una especificación antes de programar | buscas roles completos de equipo ágil; mira `bmad-method` |
| [BMAD Method](human/fichas/bmad-method.md) | quieres un proceso completo de producto a código con agentes | prefieres algo ligero centrado en especificaciones; mira `spec-kit` |

**⚖️ ¿Cuál elegir? — Humanizer, Stop Slop**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Humanizer](human/fichas/humanizer.md) | publicas textos redactados con IA y quieres que se lean como escritos por una persona | quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop` |
| [Stop Slop](human/fichas/stop-slop.md) | quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt | prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer` |

**⚖️ ¿Cuál elegir? — Prompt Engineering Guide, Anthropic's Prompt Engineering Tutorial**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Prompt Engineering Guide](human/fichas/prompt-engineering-guide.md) | quieres una referencia amplia de técnicas de prompting | prefieres ejercicios prácticos con corrección; mira `prompt-eng-tutorial` |
| [Anthropic's Prompt Engineering Tutorial](human/fichas/prompt-eng-tutorial.md) | quieres aprender prompts con práctica guiada | buscas una guía amplia multi-modelo; mira `prompt-engineering-guide` |

**⚖️ ¿Cuál elegir? — Fabric, prompts.chat**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Fabric](human/fichas/fabric.md) | quieres prompts reutilizables desde la terminal | buscas solo una lista de prompts para copiar; mira `prompts-chat` |
| [prompts.chat](human/fichas/prompts-chat.md) | buscas prompts listos para copiar | quieres ejecutarlos como comandos encadenables; mira `fabric` |

**⚖️ ¿Cuál elegir? — Awesome LLM Apps, OpenAI Cookbook, Claude Cookbooks**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Awesome LLM Apps](human/fichas/awesome-llm-apps.md) | quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto | buscas un curso estructurado con lecciones en orden; mira `ai-agents-for-beginners` o `generative-ai-for-beginners` |
| [OpenAI Cookbook](human/fichas/openai-cookbook.md) | construyes sobre la API de OpenAI y quieres ejemplos oficiales | usas Claude como modelo principal; mira `claude-cookbooks` |
| [Claude Cookbooks](human/fichas/claude-cookbooks.md) | construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar | tu app usa la API de OpenAI; mira `openai-cookbook` |

### Catálogos y marketplaces de skills

#### 🗂️ Anthropic Skills ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 192k  
**Qué es:** Repositorio de Anthropic con skills listas para Claude Code, Claude.ai y la API: creativas, técnicas (pruebas de apps web, creación de servidores MCP) y empresariales, más las skills de docx, pptx, xlsx y PDF que Claude usa para generar archivos. Incluye la especificación del estándar Agent Skills y una plantilla para crear las tuyas.  
**Instalación:** En Claude Code: `/plugin marketplace add anthropics/skills` y luego `/plugin install document-skills@anthropic-agent-skills` (o `example-skills@anthropic-agent-skills`).  
**Elige si:** quieres skills oficiales de Anthropic o un ejemplo de referencia para escribir las tuyas — **Evita si:** buscas volumen o skills de comunidad para varios agentes; mira `awesome-agent-skills` o `antigravity-awesome-skills`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) · [superpowers](human/fichas/superpowers.md)  
**Más:** [ficha completa](human/fichas/anthropic-skills.md) · [GitHub](https://github.com/anthropics/skills)

#### 🔌 Claude Code Plugins Directory ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 46.7k  
**Qué es:** Directorio curado desde el que Claude Code instala plugins de forma nativa. En `/plugins` están los que mantiene Anthropic (revisión de código y PR, desarrollo de features, diseño frontend, hooks, gestión de CLAUDE.md, skill-creator) y en `/external_plugins` los de socios y comunidad que pasan su revisión (Figma, Atlassian, Cloudflare, Firebase, Context7, Superpowers y cientos más).  
**Instalación:** En Claude Code: `/plugin install <plugin>@claude-plugins-official`, o explora el catálogo en `/plugin` > Discover.  
**Elige si:** usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando — **Evita si:** buscas recursos comunitarios o trabajas con otro agente; mira `awesome-claude-code` o `wshobson-agents`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [Awesome Claude Code](human/fichas/awesome-claude-code.md)  
**Más:** [ficha completa](human/fichas/claude-plugins-official.md) · [GitHub](https://github.com/anthropics/claude-plugins-official)

#### 🗂️ Awesome Claude Skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 79.2k  
**Qué es:** Recopilación de skills por áreas (documentos, desarrollo, datos, marketing, escritura, multimedia, productividad, seguridad) que enlaza skills oficiales de Anthropic y de la comunidad, y aloja algunas propias. Incluye el plugin connect-apps, que usa Composio para que Claude envíe correos, cree issues o publique en Slack.  
**Instalación:** No se instala entero: copia la carpeta de la skill que quieras a `~/.claude/skills/`. Para el plugin de apps: `claude --plugin-dir ./connect-apps-plugin` y luego `/connect-apps:setup` con tu API key de Composio.  
**Elige si:** usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo — **Evita si:** solo quieres skills de procedencia oficial; mira `anthropic-skills` o `awesome-agent-skills`  
**Combina con:** [Composio](human/fichas/composio.md) · [Claude Code](human/fichas/claude-code.md) · [SkillSpector](human/fichas/skillspector.md)  
**Más:** [ficha completa](human/fichas/awesome-claude-skills.md) · [GitHub](https://github.com/ComposioHQ/awesome-claude-skills)

#### ⭐ Awesome Claude Code
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 57.7k  
**Qué es:** Índice comunitario del ecosistema de Claude Code organizado por temas: guías de inicio, recursos oficiales de Anthropic, skills, orquestación de agentes, memoria, observabilidad y coste, seguridad, status lines y configuración. Cada entrada incluye una breve valoración del mantenedor.  
**Instalación:** No se instala: abre el repo y sigue el enlace del recurso que te interese.  
**Elige si:** usas Claude Code a diario y quieres descubrir herramientas y flujos probados por la comunidad — **Evita si:** trabajas con otro agente o solo quieres plugins oficiales; mira `claude-plugins-official` o `awesome-agent-skills`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) · [superpowers](human/fichas/superpowers.md)  
**Más:** [ficha completa](human/fichas/awesome-claude-code.md) · [GitHub](https://github.com/hesreallyhim/awesome-claude-code)

#### 🗂️ Agentic Awesome Skills
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 49.5k  
**Qué es:** Antes llamada Antigravity Awesome Skills, reúne miles de skills por dominio (desarrollo, seguridad, DevOps, datos, marketing) instalables en Claude Code, Codex, Cursor, Gemini CLI, Kiro, OpenCode y otros agentes. Incluye bundles por rol, plugins temáticos y AAS Core, un MCP local para que el agente busque en el catálogo y elija skills antes de instalarlas.  
**Instalación:** `npx agentic-awesome-skills --claude` (o `--codex`, `--cursor`, `--gemini`, `--path ./mis-skills`); añade `--skills <ids> --dry-run` para previsualizar. En Claude Code también: `/plugin marketplace add sickn33/agentic-awesome-skills`.  
**Elige si:** quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código — **Evita si:** prefieres pocas skills oficiales y revisadas; mira `anthropic-skills` o `awesome-agent-skills`  
**Combina con:** [SkillSpector](human/fichas/skillspector.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)  
**Más:** [ficha completa](human/fichas/antigravity-awesome-skills.md) · [GitHub](https://github.com/sickn33/agentic-awesome-skills)

#### 🗂️ wshobson/agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 42.4k  
**Qué es:** Colección de Seth Hobson que agrupa subagentes especialistas, skills y comandos en plugins por área: desarrollo Python y JavaScript, revisión de código, testing, infraestructura, seguridad y más. Se escribe una sola vez en formato de plugin de Claude Code y unos adaptadores generan las versiones para Codex, Cursor, OpenCode, Antigravity CLI, GitHub Copilot y Pi.  
**Instalación:** En Claude Code: `/plugin marketplace add wshobson/agents` y `/plugin install python-development@claude-code-workflows`. Solo una skill: `npx skills add wshobson/agents --skill <skill>`.  
**Elige si:** quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin — **Evita si:** solo quieres plugins oficiales de Anthropic y socios; mira `claude-plugins-official`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [SkillSpector](human/fichas/skillspector.md)  
**Más:** [ficha completa](human/fichas/wshobson-agents.md) · [GitHub](https://github.com/wshobson/agents)

#### 🗂️ Awesome GitHub Copilot
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 41k  
**Qué es:** Repositorio de la organización GitHub que reúne personalizaciones de Copilot aportadas por la comunidad: agentes especializados (algunos conectados a servidores MCP), instrucciones que se aplican por tipo de archivo, skills, plugins y un cookbook de recetas para las APIs de Copilot. Tiene web con búsqueda, un Learning Hub y un llms.txt para agentes.  
**Instalación:** `copilot plugin install <plugin>@awesome-copilot`; si tu versión no conoce el marketplace, ejecuta antes `copilot plugin marketplace add github/awesome-copilot`.  
**Elige si:** tu equipo trabaja con GitHub Copilot en VS Code o Copilot CLI y quiere personalizarlo — **Evita si:** usas Claude Code u otro agente; mira `claude-plugins-official` o `antigravity-awesome-skills`  
**Combina con:** [GitHub MCP Server](human/fichas/github-mcp-server.md) · [Spec Kit](human/fichas/spec-kit.md) · [GitHub CLI](human/fichas/cli.md)  
**Más:** [ficha completa](human/fichas/awesome-copilot.md) · [GitHub](https://github.com/github/awesome-copilot)

#### 🏅 Awesome Agent Skills
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 37k  
**Qué es:** Índice mantenido por VoltAgent que enlaza skills publicadas por los equipos de cada producto (Anthropic, Google, Vercel, Stripe, Cloudflare, Supabase, Hugging Face, Trail of Bits...) y una sección de comunidad revisada a mano. Incluye la tabla de carpetas de skills por agente (Claude Code, Codex, Cursor, Gemini CLI, Copilot, OpenCode, Windsurf) y normas de calidad para escribir skills.  
**Instalación:** No se instala: abre el repo, elige la skill y cópiala a la carpeta de skills de tu agente (por ejemplo `~/.claude/skills/`) o usa el comando que indique su fuente.  
**Elige si:** quieres skills con procedencia clara, publicadas por el equipo que mantiene cada herramienta — **Evita si:** prefieres instalar un lote grande con un solo comando; mira `antigravity-awesome-skills`  
**Combina con:** [SkillSpector](human/fichas/skillspector.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)  
**Más:** [ficha completa](human/fichas/awesome-agent-skills.md) · [GitHub](https://github.com/VoltAgent/awesome-agent-skills)

### Metodologías y harness para agentes de código

#### 🧭 Agent Skills (Addy Osmani) ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 115k  
**Qué es:** Skills listas para Claude Code, Codex y otros agentes que cubren pruebas, rendimiento, accesibilidad, revisión de código y buenas prácticas web. Pensadas para que el agente trabaje como un ingeniero senior.  
**Instalación:** Copia las carpetas a `.claude/skills/` (o la carpeta de skills de tu agente) o instálalas como plugin.  
**Elige si:** quieres skills de ingeniería web de calidad para tu agente — **Evita si:** buscas un catálogo enorme de skills de todo tipo; mira `antigravity-awesome-skills`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)  
**Más:** [ficha completa](human/fichas/agent-skills.md) · [GitHub](https://github.com/addyosmani/agent-skills)

#### 📦 skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 320k  
**Qué es:** Muestra cómo se escribe una buena skill para agentes, con pocos ejemplos pero de alta calidad para usarlos como plantilla.  
**Instalación:** Clona el repo y copia las skills elegidas a tu directorio de skills, o úsalas como referencia para crear las tuyas; las que tengan scripts TS requieren Node.  
**Elige si:** buscas referencias limpias y didácticas — **Evita si:** quieres un catálogo masivo (antigravity-awesome-skills)  
**Combina con:** [Awesome Agent Skills](human/fichas/awesome-agent-skills.md)  
**Más:** [ficha completa](human/fichas/skills.md) · [GitHub](https://github.com/mattpocock/skills)

#### 💪 superpowers
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 315k  
**Qué es:** Le da a tu agente de código un método de trabajo completo y coherente (planear, probar, revisar), no piezas sueltas.  
**Instalación:** Clona el repo y copia las skills e instrucciones a tu directorio de skills del asistente (p. ej. `~/.claude/skills`); sin dependencias.  
**Elige si:** quieres método, no fragmentos sueltos — **Evita si:** solo necesitas una skill aislada puntual  
**Combina con:** [Awesome Claude Code](human/fichas/awesome-claude-code.md) · [agent-toolkit](human/fichas/agent-toolkit.md)  
**Más:** [ficha completa](human/fichas/superpowers.md) · [GitHub](https://github.com/obra/superpowers)

#### 🌌 ECC
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 300k  
**Qué es:** Actúa como capa intermedia entre el modelo y tu sistema, de modo que las acciones del agente pasan por un escudo antes de tocar el filesystem o la shell.  
**Instalación:** `git clone` del repo y compilación del core en Rust más dependencias en TS/Python/Go. Requiere toolchain de Rust y permisos para instalar hooks a nivel de sistema.  
**Elige si:** ejecutas agentes con acceso real a tu máquina y necesitas contención — **Evita si:** solo haces prompts de chat sin ejecución de código  
**Combina con:** [OpenHands](human/fichas/openhands.md) · [sandbox](human/fichas/sandbox.md) · [hermes-agent](human/fichas/hermes-agent.md)  
**Más:** [ficha completa](human/fichas/ecc.md) · [GitHub](https://github.com/affaan-m/ECC)

#### 🧠 andrej-karpathy-skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 232k  
**Qué es:** Ajusta el comportamiento de tu asistente con principios claros, sin atarte a una herramienta concreta.  
**Instalación:** Clona el repo y copia el `CLAUDE.md` (o su contenido) en tu proyecto o en el directorio de configuración del asistente; no requiere dependencias ni claves.  
**Elige si:** quieres respuestas más útiles ya, sin curar prompts largos — **Evita si:** buscas skills ejecutables con scripts concretos  
**Combina con:** [Awesome Claude Code](human/fichas/awesome-claude-code.md) · [Context-Engineering](human/fichas/context-engineering.md)  
**Más:** [ficha completa](human/fichas/andrej-karpathy-skills.md) · [GitHub](https://github.com/multica-ai/andrej-karpathy-skills)

#### 🧭 Ponytail
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 188k  
**Qué es:** Empuja al agente a reutilizar, borrar y simplificar antes de añadir código nuevo. Reduce soluciones infladas y cambios innecesarios.  
**Instalación:** Copia la skill a la carpeta de skills de tu agente siguiendo el README.  
**Elige si:** tu agente tiende a sobrecomplicar las soluciones — **Evita si:** necesitas una metodología completa de proyecto; mira `bmad-method`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [superpowers](human/fichas/superpowers.md) · [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md)  
**Más:** [ficha completa](human/fichas/ponytail.md) · [GitHub](https://github.com/DietrichGebert/ponytail)

#### 🧭 Spec Kit
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 149k  
**Qué es:** Te guía para escribir especificación, plan y tareas antes de que el agente programe. Funciona con Copilot, Claude Code, Gemini CLI y otros.  
**Instalación:** `uvx --from git+https://github.com/github/spec-kit.git specify init mi-proyecto`.  
**Elige si:** quieres que el agente siga una especificación antes de programar — **Evita si:** buscas roles completos de equipo ágil; mira `bmad-method`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [Gemini CLI](human/fichas/gemini-cli.md)  
**Más:** [ficha completa](human/fichas/spec-kit.md) · [GitHub](https://github.com/github/spec-kit)

#### 🧭 BMAD Method
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 55.2k  
**Qué es:** Organiza el trabajo con IA en roles y documentos (brief, PRD, arquitectura, historias) que el agente de código sigue paso a paso. Útil para proyectos medianos donde los prompts sueltos se pierden.  
**Instalación:** `npx bmad-method install` en la raíz de tu proyecto.  
**Elige si:** quieres un proceso completo de producto a código con agentes — **Evita si:** prefieres algo ligero centrado en especificaciones; mira `spec-kit`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)  
**Más:** [ficha completa](human/fichas/bmad-method.md) · [GitHub](https://github.com/bmad-code-org/BMAD-METHOD)

#### 🛡️ SkillSpector
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 25.2k  
**Qué es:** Resuelve el riesgo de ejecutar skills de terceros sin revisión.  
**Instalación:** Clona el repo e instala sus dependencias (Python/Node) según el README; ejecútalo apuntando al directorio de skills que quieras auditar. Requiere Python y/o Node según el modo de escaneo.  
**Elige si:** instalas skills externas o curas catálogos — **Evita si:** solo usas skills propias de confianza  
**Combina con:** [Agentic Awesome Skills](human/fichas/antigravity-awesome-skills.md)  
**Más:** [ficha completa](human/fichas/skillspector.md) · [GitHub](https://github.com/NVIDIA/SkillSpector)

#### 🧰 agent-toolkit
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 2.7k  
**Qué es:** Te da skills listas para tareas comunes, para que tu agente sea productivo desde el primer día.  
**Instalación:** Clona el repo y copia las carpetas de skill a tu directorio de skills de Claude Code; sin dependencias pesadas.  
**Elige si:** quieres productividad inmediata con tareas comunes — **Evita si:** buscas un método integral (superpowers)  
**Combina con:** [superpowers](human/fichas/superpowers.md)  
**Más:** [ficha completa](human/fichas/agent-toolkit.md) · [GitHub](https://github.com/softaworks/agent-toolkit)

### Escritura y calidad de texto

#### 🧑 Humanizer ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 67.4k  
**Qué es:** Detecta 26 patrones típicos de la prosa de LLM (contrastes tipo 'no es X, es Y', cierres dramáticos, tríadas forzadas, frases de falsa profundidad, importancia inflada) y reescribe el texto sin cambiar lo que dice. Puede imitar tu estilo si le das una muestra y, sobre un archivo, solo toca la prosa: no el código, los datos ni el frontmatter.  
**Instalación:** En Claude Code: `/plugin marketplace add blader/humanizer` y `/plugin install humanizer@humanizer`; en otros agentes: `npx skills add blader/humanizer --global --agent '*'`.  
**Elige si:** publicas textos redactados con IA y quieres que se lean como escritos por una persona — **Evita si:** quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop`  
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)  
**Más:** [ficha completa](human/fichas/humanizer.md) · [GitHub](https://github.com/blader/humanizer)

#### 🧹 Stop Slop
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 18.8k  
**Qué es:** Un SKILL.md con tres archivos de referencia (frases a eliminar, estructuras a evitar y ejemplos antes/después) que enseña a Claude o a cualquier LLM a quitar muletillas, contrastes binarios, fragmentos dramáticos, voz pasiva y otros patrones predecibles. Cierra con una rúbrica de cinco dimensiones para decidir si el texto necesita otra vuelta.  
**Instalación:** `git clone https://github.com/hardikpandya/stop-slop ~/.claude/skills/stop-slop`; en otros entornos, pega el contenido de `SKILL.md` en tus instrucciones o en el system prompt.  
**Elige si:** quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt — **Evita si:** prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer`  
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [Claude Code](human/fichas/claude-code.md)  
**Más:** [ficha completa](human/fichas/stop-slop.md) · [GitHub](https://github.com/hardikpandya/stop-slop)

### Skills de dominio: marketing, SEO y negocio

#### 📈 Marketing Skills ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 59.5k  
**Qué es:** Skills de Corey Haines para marketers técnicos y founders que trabajan con agentes de código: conversión, copywriting, SEO y SEO para IA, anuncios, emails, analítica y atribución, pricing, lanzamientos, retención y ventas. La skill product-marketing guarda el contexto de tu producto y las demás la consultan antes de actuar.  
**Instalación:** `npx skills add coreyhaines31/marketingskills` (o solo algunas con `--skill cro copywriting`); en Claude Code también `/plugin marketplace add coreyhaines31/marketingskills` y `/plugin install marketing-skills`.  
**Elige si:** eres founder o marketer técnico y quieres que tu agente de código haga trabajo de growth con marcos probados — **Evita si:** necesitas una herramienta que envíe campañas o mida resultados; mira `mautic`, `listmonk` o `posthog`  
**Combina con:** [The Agency (agency-agents)](human/fichas/agency-agents.md) · [GEO-SEO Claude](human/fichas/geo-seo-claude.md) · [mautic](human/fichas/mautic.md) · [posthog](human/fichas/posthog.md)  
**Más:** [ficha completa](human/fichas/marketingskills.md) · [GitHub](https://github.com/coreyhaines31/marketingskills)

#### 🏢 The Agency (agency-agents)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 168k  
**Qué es:** Plantillas de subagente en Markdown agrupadas por divisiones, como una agencia completa: ingeniería, diseño, paid media, ventas, marketing, producto, testing, seguridad, soporte, finanzas, videojuegos y más. Cada agente define identidad, misión, flujo de trabajo, entregables con ejemplos y métricas de éxito, y hay runbooks que arman equipos para escenarios como un MVP o una campaña.  
**Instalación:** `git clone https://github.com/msitarzewski/agency-agents && cd agency-agents && ./scripts/install.sh --tool claude-code --division engineering,marketing`, o la app de escritorio (`brew install --cask msitarzewski/agency-agents/agency-agents`).  
**Elige si:** quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código — **Evita si:** solo necesitas skills de marketing y growth; mira `marketingskills`  
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [GEO-SEO Claude](human/fichas/geo-seo-claude.md) · [Claude Code](human/fichas/claude-code.md)  
**Más:** [ficha completa](human/fichas/agency-agents.md) · [GitHub](https://github.com/msitarzewski/agency-agents)

#### 🌍 GEO-SEO Claude
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 11.6k  
**Qué es:** Añade a Claude Code comandos `/geo` que auditan un sitio para buscadores con IA (ChatGPT, Claude, Perplexity, Gemini, AI Overviews) sin dejar el SEO técnico: citabilidad del contenido, acceso de crawlers de IA en robots.txt, menciones de marca, datos estructurados y llms.txt. Genera informes para clientes en Markdown o PDF y lleva un pequeño CRM de prospectos.  
**Instalación:** `curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install.sh | bash` (requiere Python 3.10+ y Claude Code); después, `/geo audit <url>`.  
**Elige si:** quieres medir y mejorar cómo te citan los buscadores con IA, no solo tu posición en Google — **Evita si:** solo haces SEO clásico o no usas Claude Code; mira `marketingskills`  
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [The Agency (agency-agents)](human/fichas/agency-agents.md) · [playwright](human/fichas/playwright.md)  
**Más:** [ficha completa](human/fichas/geo-seo-claude.md) · [GitHub](https://github.com/zubair-trabzada/geo-seo-claude)

#### 📈 Arcads AI Video Skill Pack
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio  
**Aviso:** ⚠️ El repositorio original ya no está disponible en GitHub; se conserva el clon local.  
**Qué es:** Repo de trabajo que convierte Claude Code o Cursor en un estudio de anuncios: genera videos UGC, presentaciones de producto, lookbooks y miniaturas de YouTube con los modelos de Arcads, y anuncios estáticos para Meta con 37 plantillas. Incluye pipelines multipaso (estilo Pixar o plastilina con ffmpeg), subtitulado con Whisper y HyperFrames, y publicación como anuncios pausados en Meta.  
**Instalación:** `git clone https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial && cd arcads-claude-code-mrpaidsocial && ./scripts/setup.sh` (pide tu API key de Arcads); luego abre la carpeta en Claude Code o Cursor.  
**Elige si:** ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor — **Evita si:** quieres generar video con modelos abiertos sin servicio de pago; mira `comfyui` u `openmontage`  
**Combina con:** [HyperFrames](human/fichas/hyperframes.md) · [whisper](human/fichas/whisper.md) · [FFmpeg](human/fichas/ffmpeg.md) · [Marketing Skills](human/fichas/marketingskills.md)  
**Más:** [ficha completa](human/fichas/arcads-claude-code.md) · [GitHub](https://github.com/krusemediallc/arcads-claude-code)

### Prompts y prompt engineering

#### 💡 Prompt Engineering Guide ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 80k  
**Qué es:** Explica técnicas de prompting, riesgos y aplicaciones con ejemplos y referencias a papers. Disponible en varios idiomas, incluido el español.  
**Instalación:** No se instala: léela en promptingguide.ai o en el repo.  
**Elige si:** quieres una referencia amplia de técnicas de prompting — **Evita si:** prefieres ejercicios prácticos con corrección; mira `prompt-eng-tutorial`  
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md)  
**Más:** [ficha completa](human/fichas/prompt-engineering-guide.md) · [GitHub](https://github.com/dair-ai/Prompt-Engineering-Guide)

#### 💡 Fabric ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 44.6k  
**Qué es:** Organiza prompts reutilizables (patterns) para tareas como resumir videos, extraer ideas o analizar textos. Se encadena con pipes en la terminal.  
**Instalación:** `go install github.com/danielmiessler/fabric/cmd/fabric@latest` y luego `fabric --setup`.  
**Elige si:** quieres prompts reutilizables desde la terminal — **Evita si:** buscas solo una lista de prompts para copiar; mira `prompts-chat`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [yt-dlp](human/fichas/yt-dlp.md)  
**Más:** [ficha completa](human/fichas/fabric.md) · [GitHub](https://github.com/danielmiessler/Fabric)

#### 💡 prompts.chat
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 177k  
**Qué es:** Reúne miles de prompts de rol y tarea para ChatGPT, Claude y otros, con buscador web. Puedes desplegar tu propia copia para tu organización.  
**Instalación:** No se instala para usarlo: abre prompts.chat; para self-host clona el repo y sigue su guía.  
**Elige si:** buscas prompts listos para copiar — **Evita si:** quieres ejecutarlos como comandos encadenables; mira `fabric`  
**Más:** [ficha completa](human/fichas/prompts-chat.md) · [GitHub](https://github.com/f/prompts.chat)

#### 💡 Anthropic's Prompt Engineering Tutorial
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 39.2k  
**Qué es:** Nueve capítulos con ejercicios sobre claridad, roles, ejemplos, razonamiento paso a paso y cómo evitar alucinaciones. Cada lección se practica contra la API de Claude.  
**Instalación:** No se instala: abre los notebooks y configura tu clave de API de Anthropic.  
**Elige si:** quieres aprender prompts con práctica guiada — **Evita si:** buscas una guía amplia multi-modelo; mira `prompt-engineering-guide`  
**Combina con:** [Claude Cookbooks](human/fichas/claude-cookbooks.md)  
**Más:** [ficha completa](human/fichas/prompt-eng-tutorial.md) · [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial)

#### 🎯 prompt-master
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 15.8k  
**Qué es:** Te ayuda a escribir mejores prompts con meta-prompting reutilizable, como una capa por encima de cualquier IA.  
**Instalación:** Clona el repo y copia el `SKILL.md` a tu directorio de skills, o pega su contenido como instrucción en la IA que uses; sin dependencias.  
**Elige si:** quieres dejar de re-promptear y acertar antes — **Evita si:** ya tienes prompts afinados y estables  
**Combina con:** [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md)  
**Más:** [ficha completa](human/fichas/prompt-master.md) · [GitHub](https://github.com/nidhinjs/prompt-master)

### Guías, cursos y cookbooks

#### 🎓 Generative AI for Beginners ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 123k  
**Qué es:** Recorre desde qué es un LLM hasta prompts, RAG, agentes, seguridad y fine-tuning, con código en Python y TypeScript. Está traducido a muchos idiomas, incluido el español.  
**Instalación:** No se instala: abre el repo o haz fork y sigue las lecciones en Codespaces.  
**Elige si:** quieres un curso estructurado y gratuito para empezar — **Evita si:** ya construyes con LLM y buscas recetas concretas; mira `openai-cookbook`  
**Combina con:** [AI Agents for Beginners](human/fichas/ai-agents-for-beginners.md) · [MCP for Beginners](human/fichas/mcp-for-beginners.md)  
**Más:** [ficha completa](human/fichas/generative-ai-for-beginners.md) · [GitHub](https://github.com/microsoft/generative-ai-for-beginners)

#### 🎓 AI Agents for Beginners ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 79.3k  
**Qué es:** Recorre desde qué es un agente hasta producción: frameworks, patrones de diseño (uso de herramientas, planificación, multiagente, metacognición), RAG agéntico, protocolos MCP, A2A y NLWeb, context engineering, memoria, agentes que usan el navegador, despliegue, agentes locales y seguridad. Cada lección trae README, video corto y ejemplos en Python.  
**Instalación:** Lee las lecciones en GitHub; para ejecutar el código, clona el repo (el README explica cómo omitir las traducciones) y sigue `00-course-setup`, que pide una cuenta de Azure con Microsoft Foundry.  
**Elige si:** estás empezando con agentes y quieres un curso guiado, gratuito y disponible en español — **Evita si:** no quieres depender de Azure o ya llevas agentes a producción; mira `agents-towards-production` o `12-factor-agents`  
**Combina con:** [Generative AI for Beginners](human/fichas/generative-ai-for-beginners.md) · [Microsoft Agent Framework](human/fichas/agent-framework.md) · [MCP for Beginners](human/fichas/mcp-for-beginners.md)  
**Más:** [ficha completa](human/fichas/ai-agents-for-beginners.md) · [GitHub](https://github.com/microsoft/ai-agents-for-beginners)

#### 🎓 Awesome LLM Apps
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 144k  
**Qué es:** Repositorio de Shubham Saboo con plantillas de código abierto ordenadas por tipo: agentes simples de un solo archivo, agentes avanzados con herramientas y memoria, equipos multiagente, agentes de voz, agentes con MCP, RAG, chat con documentos y webs, fine-tuning y cursos rápidos de Google ADK y OpenAI Agents SDK. Según la app usa OpenAI, Anthropic, Google, xAI, DeepSeek o modelos abiertos.  
**Instalación:** `git clone https://github.com/Shubhamsaboo/awesome-llm-apps`, entra en la carpeta de la app, `pip install -r requirements.txt` y ejecuta su script (p. ej. `streamlit run travel_agent.py`) con la API key del modelo que use.  
**Elige si:** quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto — **Evita si:** buscas un curso estructurado con lecciones en orden; mira `ai-agents-for-beginners` o `generative-ai-for-beginners`  
**Combina con:** [streamlit](human/fichas/streamlit.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md) · [Agent Development Kit (ADK)](human/fichas/adk-python.md) · [firecrawl](human/fichas/firecrawl.md)  
**Más:** [ficha completa](human/fichas/awesome-llm-apps.md) · [GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps)

#### 🎓 OpenAI Cookbook
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 77k  
**Qué es:** Reúne recetas sobre embeddings, function calling, RAG, evaluación, agentes y voz. Sirve como referencia práctica al construir con la API de OpenAI.  
**Instalación:** No se instala: abre los notebooks en GitHub o en cookbook.openai.com.  
**Elige si:** construyes sobre la API de OpenAI y quieres ejemplos oficiales — **Evita si:** usas Claude como modelo principal; mira `claude-cookbooks`  
**Combina con:** [openai-python](human/fichas/openai-python.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md)  
**Más:** [ficha completa](human/fichas/openai-cookbook.md) · [GitHub](https://github.com/openai/openai-cookbook)

#### 🎓 Claude Cookbooks
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 54.5k  
**Qué es:** Notebooks y guías de Anthropic con código copiable para construir con Claude: clasificación, resumen, RAG (con Pinecone o embeddings de Voyage AI), tool use y un agente de atención al cliente, visión y extracción de formularios, subagentes, PDFs, salida JSON consistente, moderación, prompt caching y checklists de coste y latencia.  
**Instalación:** `git clone https://github.com/anthropics/claude-cookbooks && cd claude-cookbooks && uv sync` y abre los notebooks en Jupyter con tu `ANTHROPIC_API_KEY`.  
**Elige si:** construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar — **Evita si:** tu app usa la API de OpenAI; mira `openai-cookbook`  
**Combina con:** [Anthropic's Prompt Engineering Tutorial](human/fichas/prompt-eng-tutorial.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [promptfoo](human/fichas/promptfoo.md)  
**Más:** [ficha completa](human/fichas/claude-cookbooks.md) · [GitHub](https://github.com/anthropics/claude-cookbooks)

#### 🎓 12-Factor Agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 27.1k  
**Qué es:** Ensayo de Dex Horthy (HumanLayer) que resume lo aprendido construyendo agentes para clientes reales: los productos que funcionan son sobre todo software determinista con pasos de LLM bien colocados. Cada factor (controlar tus prompts, tu ventana de contexto y tu flujo de control, pausar y reanudar, contactar a humanos con tool calls, agentes pequeños) tiene su capítulo con diagramas y ejemplos.  
**Instalación:** No se instala: abre el repo y lee los factores en orden (empieza por el factor 3 si te interesa el context engineering).  
**Elige si:** vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework — **Evita si:** buscas tutoriales con código ejecutable paso a paso; mira `agents-towards-production` o `ai-agents-for-beginners`  
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md) · [LangGraph](human/fichas/langgraph.md) · [AI SDK (Vercel)](human/fichas/vercel-ai.md)  
**Más:** [ficha completa](human/fichas/12-factor-agents.md) · [GitHub](https://github.com/humanlayer/12-factor-agents)

#### 🎓 Agents Towards Production
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 21.9k  
**Qué es:** Playbook de Nir Diamant (DiamantAI) con un tutorial por carpeta, en notebooks o scripts listos para ejecutar, sobre cada pieza del stack de un agente: tool calling seguro, datos web, RAG, memoria (Redis, Mem0, Cognee), Docker, FastAPI, GPU, MCP, A2A, LangGraph, seguridad, fine-tuning, trazas y evaluación. Muchos tutoriales los aportan empresas patrocinadoras.  
**Instalación:** `git clone https://github.com/NirDiamant/agents-towards-production` y, dentro del tutorial elegido, `pip install -r requirements.txt` y `jupyter notebook`; cada uno indica las API keys que necesita.  
**Elige si:** ya tienes un prototipo de agente y necesitas resolver memoria, despliegue, seguridad u observabilidad — **Evita si:** estás empezando con agentes desde cero; mira `ai-agents-for-beginners`  
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [mem0](human/fichas/mem0.md) · [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/agents-towards-production.md) · [GitHub](https://github.com/NirDiamant/agents-towards-production)

#### 🎓 Loop Engineering
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 11.7k  
**Qué es:** Propone dejar de escribir prompts aislados y diseñar ciclos con objetivo, verificación y puntuación para que el agente itere solo. Incluye starters y herramientas de línea de comandos.  
**Instalación:** `git clone https://github.com/cobusgreyling/loop-engineering` y copia el starter que necesites a tu proyecto.  
**Elige si:** quieres que tu agente de código itere solo con criterios medibles — **Evita si:** solo necesitas una lista de skills; mira `awesome-agent-skills`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [superpowers](human/fichas/superpowers.md)  
**Más:** [ficha completa](human/fichas/loop-engineering.md) · [GitHub](https://github.com/cobusgreyling/loop-engineering)

#### 🧩 Context-Engineering
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 9.3k  
**Qué es:** Enseña de forma sistemática qué meter en el prompt y qué dejar fuera para que el modelo responda mejor.  
**Instalación:** Clona el repo y abre los notebooks/Markdown localmente; no requiere instalación más allá de un entorno de notebooks (Jupyter) y claves de API para los ejemplos.  
**Elige si:** quieres profundizar en contexto y RAG — **Evita si:** buscas skills ejecutables listas para copiar  
**Combina con:** [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md) · [headroom](human/fichas/headroom.md)  
**Más:** [ficha completa](human/fichas/context-engineering.md) · [GitHub](https://github.com/jasontang-ai/Context-Engineering)

---

## 🕸️ 3. Frameworks & Orquestación de Agentes

Agentes de código, frameworks multiagente en Python y TypeScript, builders visuales, asistentes autónomos, research e infraestructura.

**⚖️ ¿Cuál elegir? — OpenCode, Claude Code, Codex CLI, Gemini CLI, Cline, Open Interpreter, goose**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OpenCode](human/fichas/opencode.md) | quieres un agente de código abierto y multi-modelo | prefieres la experiencia oficial de un proveedor; mira `claude-code` o `codex` |
| [Claude Code](human/fichas/claude-code.md) | quieres el agente de código más capaz para tareas largas en tu repo | necesitas un agente totalmente abierto y multi-modelo; mira `opencode` |
| [Codex CLI](human/fichas/codex.md) | usas ChatGPT u OpenAI y quieres un agente abierto en terminal | trabajas con Claude como modelo principal; mira `claude-code` |
| [Gemini CLI](human/fichas/gemini-cli.md) | quieres un agente de terminal potente con cuota gratuita | buscas el agente con mejor desempeño en tareas largas; mira `claude-code` |
| [Cline](human/fichas/cline.md) | quieres un agente dentro de VS Code con control de cada paso | trabajas solo en terminal; mira `opencode` |
| [Open Interpreter](human/fichas/open-interpreter.md) | quieres un agente que ejecute código usando modelos abiertos | buscas un agente maduro para repos grandes; mira `opencode` |
| [goose](human/fichas/goose.md) | quieres un agente abierto con app de escritorio y MCP | solo programas en terminal y quieres el más usado; mira `opencode` |

**⚖️ ¿Cuál elegir? — OpenHands, SWE-agent, Open SWE**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OpenHands](human/fichas/openhands.md) | quieres un agente que "haga", no solo hable | solo necesitas chat/RAG o no puedes correr Docker |
| [SWE-agent](human/fichas/swe-agent.md) | investigas o automatizas la resolución de issues | quieres un asistente diario en tu terminal; mira `claude-code` |
| [Open SWE](human/fichas/open-swe.md) | quieres construir el agente de código interno de tu empresa | solo quieres un agente para tu terminal; mira `claude-code` |

**⚖️ ¿Cuál elegir? — LangGraph, langchain, AutoGen, crewAI, LlamaIndex, Agno, Deep Agents**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [LangGraph](human/fichas/langgraph.md) | necesitas agentes con estado, control fino y persistencia | quieres algo mínimo para un agente simple; mira `smolagents` |
| [langchain](human/fichas/langchain.md) | quieres la base estándar con máximas integraciones | prefieres mínima abstracción o un solo proveedor sin cambiar |
| [AutoGen](human/fichas/autogen.md) | mantienes un proyecto que ya usa AutoGen | empiezas algo nuevo; mira `agent-framework` |
| [crewAI](human/fichas/crewai.md) | quieres velocidad y un modelo mental simple de "equipo" | necesitas control de bajo nivel o orquestación muy custom |
| [LlamaIndex](human/fichas/llama-index.md) | tu proyecto gira alrededor de RAG sobre tus documentos | necesitas orquestación general de agentes; mira `langgraph` |
| [Agno](human/fichas/agno.md) | quieres un framework de agentes con memoria y API lista | necesitas grafos explícitos y controlables; mira `langgraph` |
| [Deep Agents](human/fichas/deepagents.md) | quieres un agente potente sin diseñar el bucle desde cero | necesitas control total del grafo; usa `langgraph` directamente |

**⚖️ ¿Cuál elegir? — Mastra, AI SDK (Vercel), LangGraph.js**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Mastra](human/fichas/mastra.md) | tu equipo trabaja en TypeScript y quiere agentes completos | trabajas en Python; mira `langgraph` o `pydantic-ai` |
| [AI SDK (Vercel)](human/fichas/vercel-ai.md) | construyes una app web con IA en TypeScript | necesitas agentes complejos con memoria y workflows; mira `mastra` |
| [LangGraph.js](human/fichas/langgraphjs.md) | quieres el modelo de LangGraph en TypeScript | buscas una experiencia TS más integrada; mira `mastra` |

**⚖️ ¿Cuál elegir? — Sim, AutoGPT, dify, langflow, Flowise**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Sim](human/fichas/sim.md) | quieres un constructor visual de agentes moderno y abierto | prefieres automatización general con cientos de apps; mira `n8n` |
| [AutoGPT](human/fichas/autogpt.md) | quieres agentes continuos con un editor visual propio | buscas algo ligero y fácil de operar; mira `sim` o `flowise` |
| [dify](human/fichas/dify.md) | quieres una app IA completa autoalojada | solo necesitas una librería o un prototipo puntual |
| [langflow](human/fichas/langflow.md) | prefieres construir en visual sobre LangChain | quieres todo en código o no usas LangChain |
| [Flowise](human/fichas/flowise.md) | quieres un prototipo visual ya, en stack JS | necesitas plataforma completa con RAG/observabilidad (dify) |

**⚖️ ¿Cuál elegir? — OpenClaw, hermes-agent, Mercury Agent**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OpenClaw](human/fichas/openclaw.md) | quieres un asistente personal que actúe por tus canales de chat | necesitas un agente para tu empresa con varios usuarios; mira `hermes-agent` |
| [hermes-agent](human/fichas/hermes-agent.md) | quieres agentes locales con UI y memoria persistente | prefieres orquestación en nube o no quieres compilar Tauri |
| [Mercury Agent](human/fichas/mercury-agent.md) | quieres un asistente personal ligero con permisos claros | buscas el ecosistema más grande; mira `openclaw` |

**⚖️ ¿Cuál elegir? — STORM, gpt-researcher**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [STORM](human/fichas/storm.md) | necesitas informes largos y citados sobre un tema | quieres respuestas cortas con fuentes; mira `gpt-researcher` |
| [gpt-researcher](human/fichas/gpt-researcher.md) | necesitas research profundo citado | solo quieres una respuesta corta o un chat simple |

**⚖️ ¿Cuál elegir? — E2B, NemoClaw, sandbox**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [E2B](human/fichas/e2b.md) | tu agente ejecuta código y necesitas aislarlo | solo necesitas ejecutar código localmente de confianza |
| [NemoClaw](human/fichas/nemoclaw.md) | quieres correr agentes potentes con aislamiento corporativo | solo necesitas un sandbox para ejecutar código; mira `e2b` |
| [sandbox](human/fichas/sandbox.md) | quieres aislar la ejecución de agentes y reproducibilidad | te basta correr local sin sandbox o no puedes asumir el overhead de Docker |

### Agentes de código (terminal e IDE)

#### 👨‍💻 OpenCode ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 226k  
**Qué es:** Ofrece una TUI cuidada, modo cliente-servidor, LSP y agentes configurables. Sirve si quieres un agente libre de proveedor.  
**Instalación:** `curl -fsSL https://opencode.ai/install | bash` o `npm i -g opencode-ai`.  
**Elige si:** quieres un agente de código abierto y multi-modelo — **Evita si:** prefieres la experiencia oficial de un proveedor; mira `claude-code` o `codex`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md) · [Awesome Agent Skills](human/fichas/awesome-agent-skills.md)  
**Más:** [ficha completa](human/fichas/opencode.md) · [GitHub](https://github.com/anomalyco/opencode)

#### 👨‍💻 Claude Code ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 155k  
**Qué es:** Lee y edita archivos, ejecuta comandos, hace commits y abre PRs a partir de instrucciones en lenguaje natural. Se extiende con skills, plugins, subagentes, hooks y servidores MCP.  
**Instalación:** `curl -fsSL https://claude.ai/install.sh | bash` (o `npm install -g @anthropic-ai/claude-code`) y ejecuta `claude` en tu proyecto.  
**Elige si:** quieres el agente de código más capaz para tareas largas en tu repo — **Evita si:** necesitas un agente totalmente abierto y multi-modelo; mira `opencode`  
**Combina con:** [superpowers](human/fichas/superpowers.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [claude-mem](human/fichas/claude-mem.md) · [Context7](human/fichas/context7.md)  
**Más:** [ficha completa](human/fichas/claude-code.md) · [GitHub](https://github.com/anthropics/claude-code)

#### 👨‍💻 Codex CLI
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 135k  
**Qué es:** Lee tu repositorio, propone y aplica cambios y ejecuta comandos dentro de un sandbox. Usa AGENTS.md para el contexto del proyecto y admite MCP.  
**Instalación:** `npm i -g @openai/codex` (o `brew install --cask codex`) y ejecuta `codex`.  
**Elige si:** usas ChatGPT u OpenAI y quieres un agente abierto en terminal — **Evita si:** trabajas con Claude como modelo principal; mira `claude-code`  
**Combina con:** [Agent Skills (Addy Osmani)](human/fichas/agent-skills.md) · [Spec Kit](human/fichas/spec-kit.md) · [Context7](human/fichas/context7.md)  
**Más:** [ficha completa](human/fichas/codex.md) · [GitHub](https://github.com/openai/codex)

#### 👨‍💻 Gemini CLI
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 109k  
**Qué es:** Programa, investiga y automatiza tareas desde la terminal con contexto de millones de tokens y búsqueda de Google integrada. Admite MCP y extensiones.  
**Instalación:** `npx @google/gemini-cli` o `npm install -g @google/gemini-cli` y ejecuta `gemini`.  
**Elige si:** quieres un agente de terminal potente con cuota gratuita — **Evita si:** buscas el agente con mejor desempeño en tareas largas; mira `claude-code`  
**Combina con:** [Stitch Skills](human/fichas/stitch-skills.md) · [Context7](human/fichas/context7.md)  
**Más:** [ficha completa](human/fichas/gemini-cli.md) · [GitHub](https://github.com/google-gemini/gemini-cli)

#### 🙌 OpenHands
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 93.1k  
**Qué es:** El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.  
**Instalación:** `docker run` de la imagen oficial (o `pip install openhands-ai` para el modo CLI). Requiere Docker y una clave de proveedor de LLM.  
**Elige si:** quieres un agente que "haga", no solo hable — **Evita si:** solo necesitas chat/RAG o no puedes correr Docker  
**Combina con:** [ECC](human/fichas/ecc.md) · [sandbox](human/fichas/sandbox.md)  
**Más:** [ficha completa](human/fichas/openhands.md) · [GitHub](https://github.com/OpenHands/OpenHands)

#### 👨‍💻 Cline
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 71.5k  
**Qué es:** Planifica, edita archivos, ejecuta comandos y usa el navegador pidiendo aprobación en cada paso. Admite MCP y casi cualquier proveedor.  
**Instalación:** Instala la extensión "Cline" desde el marketplace de VS Code y configura tu proveedor.  
**Elige si:** quieres un agente dentro de VS Code con control de cada paso — **Evita si:** trabajas solo en terminal; mira `opencode`  
**Combina con:** [Context7](human/fichas/context7.md) · [Playwright MCP](human/fichas/playwright-mcp.md)  
**Más:** [ficha completa](human/fichas/cline.md) · [GitHub](https://github.com/cline/cline)

#### 👨‍💻 Open Interpreter
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 68.9k  
**Qué es:** Ejecuta código y comandos en tu máquina para cumplir tareas descritas en lenguaje natural. Su versión actual se enfoca en modelos abiertos.  
**Instalación:** Sigue la instalación del README (binario de releases o instalador del proyecto).  
**Elige si:** quieres un agente que ejecute código usando modelos abiertos — **Evita si:** buscas un agente maduro para repos grandes; mira `opencode`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [E2B](human/fichas/e2b.md)  
**Más:** [ficha completa](human/fichas/open-interpreter.md) · [GitHub](https://github.com/openinterpreter/openinterpreter)

#### 👨‍💻 goose
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 56.4k  
**Qué es:** Funciona como app de escritorio o CLI y va más allá del código: automatiza tareas de desarrollo y de sistema con extensiones MCP. Nacido en Block.  
**Instalación:** Descarga la app desde los releases o `curl -fsSL https://github.com/block/goose/releases/download/stable/download_cli.sh | bash`.  
**Elige si:** quieres un agente abierto con app de escritorio y MCP — **Evita si:** solo programas en terminal y quieres el más usado; mira `opencode`  
**Combina con:** [Playwright MCP](human/fichas/playwright-mcp.md) · [GitHub MCP Server](human/fichas/github-mcp-server.md)  
**Más:** [ficha completa](human/fichas/goose.md) · [GitHub](https://github.com/aaif-goose/goose)

#### 👨‍💻 T3 Code
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 55k  
**Qué es:** No sustituye al agente: orquesta Claude Code, Codex y otros desde una UI cómoda, también en el móvil. Útil para lanzar y revisar sesiones a distancia.  
**Instalación:** Descarga la app desde los releases o sigue el README para levantar el servidor local.  
**Elige si:** usas varios agentes de código y quieres controlarlos desde una UI — **Evita si:** solo usas un agente en la terminal  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [OpenCode](human/fichas/opencode.md)  
**Más:** [ficha completa](human/fichas/t3code.md) · [GitHub](https://github.com/pingdotgg/t3code)

#### 👨‍💻 Aider
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 50k  
**Qué es:** Le pides cambios en lenguaje natural y Aider edita los archivos y confirma cada cambio en Git. Funciona con casi cualquier modelo.  
**Instalación:** `python -m pip install aider-install && aider-install` y luego `aider` en tu repo.  
**Elige si:** quieres un agente sencillo que trabaje con Git paso a paso — **Evita si:** necesitas autonomía en tareas largas; mira `claude-code`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/aider.md) · [GitHub](https://github.com/Aider-AI/aider)

#### 👨‍💻 Continue
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 36.5k  
**Qué es:** Integra chat, edición y autocompletado en el IDE con cualquier modelo, y permite ejecutar comprobaciones de IA en los PRs.  
**Instalación:** Instala la extensión "Continue" en VS Code o JetBrains; el CLI con `npm i -g @continuedev/cli`.  
**Elige si:** quieres autocompletado y chat en el IDE con modelos a elección — **Evita si:** buscas un agente autónomo para tareas largas; mira `cline`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/continue.md) · [GitHub](https://github.com/continuedev/continue)

#### 👨‍💻 SWE-agent
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 20.8k  
**Qué es:** Resuelve issues reales con el modelo que elijas y sirve como base de investigación en agentes de software. También tiene usos en ciberseguridad y retos de programación.  
**Instalación:** `pip install sweagent` (requiere Docker) y ejecuta `sweagent run` con la URL del issue.  
**Elige si:** investigas o automatizas la resolución de issues — **Evita si:** quieres un asistente diario en tu terminal; mira `claude-code`  
**Combina con:** [SWE-bench](human/fichas/swe-bench.md) · [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/swe-agent.md) · [GitHub](https://github.com/SWE-agent/SWE-agent)

#### 👨‍💻 Open SWE
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 11.2k  
**Qué es:** Trabaja en segundo plano a partir de issues o mensajes, planifica, programa en un sandbox y abre PRs. Inspirado en los agentes internos de empresas como Stripe o Ramp.  
**Instalación:** Clona el repo y sigue la guía de despliegue en LangGraph Platform con tus claves.  
**Elige si:** quieres construir el agente de código interno de tu empresa — **Evita si:** solo quieres un agente para tu terminal; mira `claude-code`  
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [E2B](human/fichas/e2b.md)  
**Más:** [ficha completa](human/fichas/open-swe.md) · [GitHub](https://github.com/langchain-ai/open-swe)

### Frameworks de agentes en Python

#### 🐍 LangGraph ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 44.7k  
**Qué es:** Modela agentes y flujos multiagente como grafos de nodos con estado compartido y checkpoints. Pensado para agentes de producción que deben ser controlables y recuperables.  
**Instalación:** `pip install -U langgraph`.  
**Elige si:** necesitas agentes con estado, control fino y persistencia — **Evita si:** quieres algo mínimo para un agente simple; mira `smolagents`  
**Combina con:** [langchain](human/fichas/langchain.md) · [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/langgraph.md) · [GitHub](https://github.com/langchain-ai/langgraph)

#### 🦜 langchain
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 149k  
**Qué es:** Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.  
**Instalación:** `pip install langchain` o `npm install langchain`. Requiere la clave del proveedor de LLM que vayas a usar (OpenAI, Anthropic, etc.).  
**Elige si:** quieres la base estándar con máximas integraciones — **Evita si:** prefieres mínima abstracción o un solo proveedor sin cambiar  
**Combina con:** [langflow](human/fichas/langflow.md) · [langfuse](human/fichas/langfuse.md) · [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/langchain.md) · [GitHub](https://github.com/langchain-ai/langchain)

#### 🐍 AutoGen
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 61.8k  
**Qué es:** Popularizó los sistemas multiagente que conversan para resolver tareas. Microsoft recomienda usar Agent Framework para proyectos nuevos.  
**Instalación:** `pip install -U "autogen-agentchat" "autogen-ext[openai]"`.  
**Elige si:** mantienes un proyecto que ya usa AutoGen — **Evita si:** empiezas algo nuevo; mira `agent-framework`  
**Combina con:** [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/autogen.md) · [GitHub](https://github.com/microsoft/autogen)

#### 👥 crewAI
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 60.7k  
**Qué es:** Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.  
**Instalación:** `pip install crewai` (o `crewai[tools]` para el set de herramientas integradas). Requiere una clave de API de LLM por entorno.  
**Elige si:** quieres velocidad y un modelo mental simple de "equipo" — **Evita si:** necesitas control de bajo nivel o orquestación muy custom  
**Combina con:** [langchain](human/fichas/langchain.md) · [mem0](human/fichas/mem0.md)  
**Más:** [ficha completa](human/fichas/crewai.md) · [GitHub](https://github.com/crewAIInc/crewAI)

#### 🐍 LlamaIndex
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 52.9k  
**Qué es:** Ofrece cargadores para cientos de fuentes, índices, motores de consulta y agentes centrados en documentos. Su plataforma LlamaParse procesa PDFs complejos.  
**Instalación:** `pip install llama-index`.  
**Elige si:** tu proyecto gira alrededor de RAG sobre tus documentos — **Evita si:** necesitas orquestación general de agentes; mira `langgraph`  
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [Docling](human/fichas/docling.md) · [Ragas](human/fichas/ragas.md)  
**Más:** [ficha completa](human/fichas/llama-index.md) · [GitHub](https://github.com/run-llama/llama_index)

#### 🐍 Agno
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 43.1k  
**Qué es:** Construye agentes con memoria, RAG y herramientas, y sírvelos como API con su plataforma. Antes se llamaba Phidata.  
**Instalación:** `pip install -U agno`.  
**Elige si:** quieres un framework de agentes con memoria y API lista — **Evita si:** necesitas grafos explícitos y controlables; mira `langgraph`  
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [mem0](human/fichas/mem0.md)  
**Más:** [ficha completa](human/fichas/agno.md) · [GitHub](https://github.com/agno-agi/agno)

#### 🐍 DSPy
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 39k  
**Qué es:** Defines módulos con firmas de entrada y salida y DSPy optimiza automáticamente los prompts y ejemplos con tus métricas. Útil para pipelines que deben mejorar con datos.  
**Instalación:** `pip install dspy`.  
**Elige si:** quieres optimizar prompts de forma sistemática con datos — **Evita si:** solo necesitas una llamada simple al modelo  
**Combina con:** [Ragas](human/fichas/ragas.md) · [MLflow](human/fichas/mlflow.md)  
**Más:** [ficha completa](human/fichas/dspy.md) · [GitHub](https://github.com/stanfordnlp/dspy)

#### 🐍 Deep Agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 31.2k  
**Qué es:** Da a cualquier modelo las capacidades de los agentes profundos (planificar, delegar, usar archivos) sin construirlas tú. Cada pieza se puede extender o reemplazar.  
**Instalación:** `pip install deepagents`.  
**Elige si:** quieres un agente potente sin diseñar el bucle desde cero — **Evita si:** necesitas control total del grafo; usa `langgraph` directamente  
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/deepagents.md) · [GitHub](https://github.com/langchain-ai/deepagents)

#### 🐍 OpenAI Agents SDK
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.6k  
**Qué es:** Define agentes con instrucciones y herramientas, pasa el control entre ellos y añade validaciones. Funciona con modelos de OpenAI y otros compatibles.  
**Instalación:** `pip install openai-agents`.  
**Elige si:** usas OpenAI y quieres agentes multiagente con poco código — **Evita si:** necesitas control de estado avanzado; mira `langgraph`  
**Combina con:** [openai-python](human/fichas/openai-python.md) · [FastMCP](human/fichas/fastmcp.md)  
**Más:** [ficha completa](human/fichas/openai-agents-python.md) · [GitHub](https://github.com/openai/openai-agents-python)

#### 🐍 smolagents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.3k  
**Qué es:** Sus agentes expresan las acciones como código en vez de JSON, lo que reduce pasos y errores. El núcleo cabe en unas mil líneas.  
**Instalación:** `pip install smolagents`.  
**Elige si:** quieres un agente simple y transparente en Python — **Evita si:** necesitas flujos con estado y aprobación humana; mira `langgraph`  
**Combina con:** [E2B](human/fichas/e2b.md) · [Transformers](human/fichas/transformers.md)  
**Más:** [ficha completa](human/fichas/smolagents.md) · [GitHub](https://github.com/huggingface/smolagents)

#### 🐍 Haystack
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 27k  
**Qué es:** Compone pipelines modulares de recuperación, generación y agentes con componentes intercambiables. Muy usado en búsqueda empresarial.  
**Instalación:** `pip install haystack-ai`.  
**Elige si:** quieres pipelines de RAG explícitos y listos para producción — **Evita si:** buscas el ecosistema más grande de integraciones; mira `llama-index`  
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [Docling](human/fichas/docling.md)  
**Más:** [ficha completa](human/fichas/haystack.md) · [GitHub](https://github.com/deepset-ai/haystack)

#### 🐍 Agent Development Kit (ADK)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 22.2k  
**Qué es:** Define agentes y sistemas multiagente con herramientas, memoria y evaluación, con interfaz web de pruebas incluida. Se despliega fácil en Google Cloud.  
**Instalación:** `pip install google-adk` y prueba con `adk web`.  
**Elige si:** trabajas con Gemini o Google Cloud — **Evita si:** tu stack es OpenAI; mira `openai-agents-python`  
**Combina con:** [Gemini CLI](human/fichas/gemini-cli.md) · [FastMCP](human/fichas/fastmcp.md)  
**Más:** [ficha completa](human/fichas/adk-python.md) · [GitHub](https://github.com/google/adk-python)

#### 🐍 Pydantic AI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 21.1k  
**Qué es:** Construye agentes con salidas validadas, herramientas tipadas e inyección de dependencias, al estilo FastAPI. Incluye evaluación y observabilidad con Logfire.  
**Instalación:** `pip install pydantic-ai`.  
**Elige si:** quieres agentes tipados y validados en Python — **Evita si:** necesitas grafos complejos con persistencia; mira `langgraph`  
**Combina con:** [langfuse](human/fichas/langfuse.md) · [FastMCP](human/fichas/fastmcp.md)  
**Más:** [ficha completa](human/fichas/pydantic-ai.md) · [GitHub](https://github.com/pydantic/pydantic-ai)

#### 🤝 ag2
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 5.1k  
**Qué es:** Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo.  
**Instalación:** `pip install ag2` (o `pyautogen` para el nombre legacy). Requiere una clave de API de LLM (OpenAI, Anthropic u otro) configurada por entorno.  
**Elige si:** construyes multiagente serio en Python — **Evita si:** te basta un agente único o quieres orquestación visual  
**Combina con:** [langchain](human/fichas/langchain.md) · [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/ag2.md) · [GitHub](https://github.com/ag2ai/ag2)

#### 🕸️ awesome-LangGraph
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 2k  
**Qué es:** Es una lista curada, no una herramienta ejecutable.  
**Instalación:** No requiere instalación; se consulta el repo (o `git clone` para uso offline).  
**Elige si:** construyes con LangGraph y quieres patrones de referencia — **Evita si:** no usas ese ecosistema  
**Combina con:** [langchain](human/fichas/langchain.md)  
**Más:** [ficha completa](human/fichas/awesome-langgraph.md) · [GitHub](https://github.com/vonzosten/awesome-LangGraph)

#### 🐍 LangGraph Supervisor
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.7k  
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.  
**Qué es:** Facilitaba el patrón supervisor en sistemas multiagente. LangChain ahora recomienda implementar ese patrón directamente con herramientas.  
**Instalación:** `pip install langgraph-supervisor` (solo para proyectos existentes).  
**Elige si:** mantienes código que ya la usa — **Evita si:** empiezas un proyecto nuevo; usa el patrón con herramientas en `langgraph`  
**Más:** [ficha completa](human/fichas/langgraph-supervisor-py.md) · [GitHub](https://github.com/langchain-ai/langgraph-supervisor-py)

### Frameworks en TypeScript y multi-lenguaje

#### 🟦 Mastra ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 29.4k  
**Qué es:** Reúne en un solo paquete agentes con memoria, workflows con estado, RAG, evals y un playground local. Pensado para equipos web que trabajan en TypeScript.  
**Instalación:** `npm create mastra@latest`.  
**Elige si:** tu equipo trabaja en TypeScript y quiere agentes completos — **Evita si:** trabajas en Python; mira `langgraph` o `pydantic-ai`  
**Combina con:** [CopilotKit](human/fichas/copilotkit.md) · [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/mastra.md) · [GitHub](https://github.com/mastra-ai/mastra)

#### 🟦 Semantic Kernel
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 28.8k  
**Qué es:** Pensado para empresas que ya usan .NET o Java y quieren añadir IA con patrones conocidos. Su evolución para agentes es Microsoft Agent Framework.  
**Instalación:** `dotnet add package Microsoft.SemanticKernel` o `pip install semantic-kernel`.  
**Elige si:** tu app es .NET o Java y quieres IA integrada — **Evita si:** empiezas un sistema de agentes nuevo; mira `agent-framework`  
**Más:** [ficha completa](human/fichas/semantic-kernel.md) · [GitHub](https://github.com/microsoft/semantic-kernel)

#### 🟦 AI SDK (Vercel)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 27.9k  
**Qué es:** Unifica la llamada a decenas de proveedores con una API común y trae hooks de React para chat con streaming. Es la base de muchos frameworks de agentes en TS.  
**Instalación:** `npm i ai` más el proveedor, p. ej. `npm i @ai-sdk/openai`.  
**Elige si:** construyes una app web con IA en TypeScript — **Evita si:** necesitas agentes complejos con memoria y workflows; mira `mastra`  
**Combina con:** [ui](human/fichas/ui.md) · [assistant-ui](human/fichas/assistant-ui.md)  
**Más:** [ficha completa](human/fichas/vercel-ai.md) · [GitHub](https://github.com/vercel/ai)

#### 🟦 Microsoft Agent Framework
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 14.6k  
**Qué es:** Une la simplicidad de AutoGen con las capacidades empresariales de Semantic Kernel: workflows con estado, observabilidad y despliegue en Azure.  
**Instalación:** `pip install agent-framework --pre` o el paquete NuGet `Microsoft.Agents.AI` para .NET.  
**Elige si:** trabajas en el ecosistema Microsoft o .NET — **Evita si:** quieres el ecosistema open source más grande; mira `langgraph`  
**Más:** [ficha completa](human/fichas/agent-framework.md) · [GitHub](https://github.com/microsoft/agent-framework)

#### 🟦 LangGraph.js
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 3.4k  
**Qué es:** Lleva el modelo de grafos con estado, checkpoints y human-in-the-loop de LangGraph al ecosistema JavaScript.  
**Instalación:** `npm install @langchain/langgraph @langchain/core`.  
**Elige si:** quieres el modelo de LangGraph en TypeScript — **Evita si:** buscas una experiencia TS más integrada; mira `mastra`  
**Combina con:** [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/langgraphjs.md) · [GitHub](https://github.com/langchain-ai/langgraphjs)

### Builders visuales y plataformas de agentes

#### 🧩 Sim ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.1k  
**Qué es:** Diseña agentes conectando bloques en un canvas, prueba en vivo y despliega como API o chat. Open source y auto-hospedable.  
**Instalación:** `npx simstudio` para probar en local, o Docker Compose para self-host.  
**Elige si:** quieres un constructor visual de agentes moderno y abierto — **Evita si:** prefieres automatización general con cientos de apps; mira `n8n`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/sim.md) · [GitHub](https://github.com/simstudioai/sim)

#### 🧩 AutoGPT
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 188k  
**Qué es:** El famoso proyecto de agentes autónomos evolucionó a una plataforma con editor de bloques, marketplace y servidor para agentes que corren en segundo plano.  
**Instalación:** Self-host con Docker Compose siguiendo la guía del repo (requiere Supabase y varios servicios).  
**Elige si:** quieres agentes continuos con un editor visual propio — **Evita si:** buscas algo ligero y fácil de operar; mira `sim` o `flowise`  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/autogpt.md) · [GitHub](https://github.com/Significant-Gravitas/AutoGPT)

#### 🧱 dify
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 161k  
**Qué es:** Combina orquestación de prompts, RAG, agentes, workflows y observabilidad en un mismo producto autoalojable.  
**Instalación:** `docker compose up` desde el repo (o cloud gestionado de Dify). Requiere Docker y al menos una clave de proveedor de LLM.  
**Elige si:** quieres una app IA completa autoalojada — **Evita si:** solo necesitas una librería o un prototipo puntual  
**Combina con:** [langflow](human/fichas/langflow.md) · [Flowise](human/fichas/flowise.md)  
**Más:** [ficha completa](human/fichas/dify.md) · [GitHub](https://github.com/langgenius/dify)

#### 🔗 langflow
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 157k  
**Qué es:** Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código Python.  
**Instalación:** `pip install langflow` o vía Docker. Requiere un proveedor de LLM configurado por entorno para los componentes que lo usen.  
**Elige si:** prefieres construir en visual sobre LangChain — **Evita si:** quieres todo en código o no usas LangChain  
**Combina con:** [langchain](human/fichas/langchain.md) · [dify](human/fichas/dify.md)  
**Más:** [ficha completa](human/fichas/langflow.md) · [GitHub](https://github.com/langflow-ai/langflow)

#### 🌊 Flowise
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 55.6k  
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.  
**Qué es:** Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible.  
**Instalación:** `npm install -g flowise && npx flowise start` o vía Docker. Requiere Node.js y las claves de los proveedores de LLM que uses.  
**Elige si:** quieres un prototipo visual ya, en stack JS — **Evita si:** necesitas plataforma completa con RAG/observabilidad (dify)  
**Combina con:** [dify](human/fichas/dify.md) · [langflow](human/fichas/langflow.md)  
**Más:** [ficha completa](human/fichas/flowise.md) · [GitHub](https://github.com/FlowiseAI/Flowise)

### Asistentes autónomos y equipos de agentes

#### 🦾 OpenClaw ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 394k  
**Qué es:** Un solo operador, muchas superficies: el asistente vive en tu equipo, tiene memoria, ejecuta tareas reales y responde por los canales que ya usas. Es uno de los proyectos de IA más populares de GitHub.  
**Instalación:** `npm install -g openclaw@latest` y `openclaw onboard` para configurar canales y modelo.  
**Elige si:** quieres un asistente personal que actúe por tus canales de chat — **Evita si:** necesitas un agente para tu empresa con varios usuarios; mira `hermes-agent`  
**Combina con:** [NemoClaw](human/fichas/nemoclaw.md) · [claude-mem](human/fichas/claude-mem.md)  
**Más:** [ficha completa](human/fichas/openclaw.md) · [GitHub](https://github.com/openclaw/openclaw)

#### ☤ hermes-agent
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 262k  
**Qué es:** Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.  
**Instalación:** `git clone` y build con Tauri/Cargo (más dependencias Python). Para modo local puro necesitas pesos de Hermes y una GPU razonable; sin GPU puede usar APIs comerciales.  
**Elige si:** quieres agentes locales con UI y memoria persistente — **Evita si:** prefieres orquestación en nube o no quieres compilar Tauri  
**Combina con:** [ECC](human/fichas/ecc.md) · [odysseus](human/fichas/odysseus.md)  
**Más:** [ficha completa](human/fichas/hermes-agent.md) · [GitHub](https://github.com/NousResearch/hermes-agent)

#### 🐝 ruflo
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 81.4k  
**Qué es:** Orquesta swarms de agentes especializados a escala.  
**Instalación:** `cargo install` o build desde fuente con `git clone` (consulta el README). Requiere tener instalados los CLIs de agentes (Claude Code/Codex) y sus claves.  
**Elige si:** orquestas muchos agentes a escala y quieres rendimiento — **Evita si:** solo necesitas 1-2 agentes o no usas Claude Code/Codex  
**Combina con:** [mem0](human/fichas/mem0.md) · [ECC](human/fichas/ecc.md)  
**Más:** [ficha completa](human/fichas/ruflo.md) · [GitHub](https://github.com/ruvnet/ruflo)

#### 🦾 DeepTutor
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 57.8k  
**Qué es:** Resuelve dudas, genera ejercicios y guía el estudio con RAG sobre tu material y memoria del alumno. Es un producto educativo, no un orquestador genérico.  
**Instalación:** Clona el repo y sigue la guía (Docker o instalación Python) con tus claves de modelo.  
**Elige si:** quieres un tutor con IA sobre tu propio material — **Evita si:** buscas un framework para construir agentes; mira `langgraph`  
**Combina con:** [Docling](human/fichas/docling.md)  
**Más:** [ficha completa](human/fichas/deeptutor.md) · [GitHub](https://github.com/HKUDS/DeepTutor)

#### 🧑‍🤝‍🧑 multica
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 55.5k  
**Qué es:** Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.  
**Instalación:** Consulta el README del repo (`git clone` / instalación web). Requiere claves de proveedor de LLM para los agentes.  
**Elige si:** mezclas trabajo humano y agentes en un mismo flujo — **Evita si:** quieres automatización 100% headless o un producto maduro  
**Combina con:** [ruflo](human/fichas/ruflo.md) · [chatwoot](human/fichas/chatwoot.md)  
**Más:** [ficha completa](human/fichas/multica.md) · [GitHub](https://github.com/multica-ai/multica)

#### 🦾 Mercury Agent
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 3.9k  
**Qué es:** Recuerda lo importante, pide permiso antes de actuar y trae 31 herramientas, tableros kanban y skills extensibles, con datos en SQLite.  
**Instalación:** Sigue el README: clona el repo, configura tu clave de modelo y arranca el agente.  
**Elige si:** quieres un asistente personal ligero con permisos claros — **Evita si:** buscas el ecosistema más grande; mira `openclaw`  
**Combina con:** [claude-mem](human/fichas/claude-mem.md)  
**Más:** [ficha completa](human/fichas/mercury-agent.md) · [GitHub](https://github.com/cosmicstack-labs/mercury-agent)

### Agentes de research autónomo

#### 🔬 autoresearch ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 99.7k  
**Qué es:** Proyecto pequeño y exploratorio de Karpathy, más que una herramienta pulida.  
**Instalación:** `git clone` del repo y ejecución de sus scripts en Python (consulta el README). Requiere una clave de LLM y acceso a búsqueda web.  
**Elige si:** experimentas con research iterativo o quieres un punto de partida — **Evita si:** quieres salida pulida y lista (gpt-researcher)  
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [crawl4ai](human/fichas/crawl4ai.md)  
**Más:** [ficha completa](human/fichas/autoresearch.md) · [GitHub](https://github.com/karpathy/autoresearch)

#### 🦌 deer-flow
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 85.2k  
**Qué es:** Coordina tareas complejas delegando en agentes especializados.  
**Instalación:** `git clone` del repo y arranque con sus scripts (o Docker). Requiere claves de proveedor de LLM y, para el sandbox, Docker.  
**Elige si:** quieres un orquestador completo y extensible — **Evita si:** buscas algo minimalista o sin Docker  
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [firecrawl](human/fichas/firecrawl.md)  
**Más:** [ficha completa](human/fichas/deer-flow.md) · [GitHub](https://github.com/bytedance/deer-flow)

#### 🔎 STORM
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 31.8k  
**Qué es:** Simula conversaciones entre perspectivas para hacer preguntas, busca fuentes y redacta un artículo estructurado y citado. Útil para informes de fondo.  
**Instalación:** `pip install knowledge-storm` y configura un buscador (p. ej. Bing o You.com) y tu modelo.  
**Elige si:** necesitas informes largos y citados sobre un tema — **Evita si:** quieres respuestas cortas con fuentes; mira `gpt-researcher`  
**Combina con:** [SearXNG](human/fichas/searxng.md) · [firecrawl](human/fichas/firecrawl.md)  
**Más:** [ficha completa](human/fichas/storm.md) · [GitHub](https://github.com/stanford-oval/storm)

#### 🔍 gpt-researcher
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.6k  
**Qué es:** Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.  
**Instalación:** `pip install gpt-researcher` o vía Docker. Requiere una clave de LLM y, según configuración, una clave de búsqueda web (Tavily).  
**Elige si:** necesitas research profundo citado — **Evita si:** solo quieres una respuesta corta o un chat simple  
**Combina con:** [firecrawl](human/fichas/firecrawl.md) · [browser-use](human/fichas/browser-use.md)  
**Más:** [ficha completa](human/fichas/gpt-researcher.md) · [GitHub](https://github.com/assafelovic/gpt-researcher)

### Infraestructura: sandboxes, herramientas y protocolos

#### 🛠️ Composio ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 31k  
**Qué es:** Da a cualquier agente herramientas listas para Gmail, Slack, GitHub, Notion y cientos más, gestionando OAuth por ti. Funciona con los principales frameworks y por MCP.  
**Instalación:** `pip install composio` o `npm i @composio/core` y configura tu clave de API.  
**Elige si:** tu agente necesita actuar en muchas apps SaaS — **Evita si:** quieres todo auto-hospedado sin servicio externo  
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md) · [Mastra](human/fichas/mastra.md)  
**Más:** [ficha completa](human/fichas/composio.md) · [GitHub](https://github.com/ComposioHQ/composio)

#### 🛠️ E2B ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 14.8k  
**Qué es:** Arranca microVMs aisladas en milisegundos donde el agente puede ejecutar código, instalar paquetes o usar un escritorio. Muy usado para intérpretes de código y agentes de datos.  
**Instalación:** `pip install e2b-code-interpreter` o `npm i @e2b/code-interpreter` con tu clave de API.  
**Elige si:** tu agente ejecuta código y necesitas aislarlo — **Evita si:** solo necesitas ejecutar código localmente de confianza  
**Combina con:** [smolagents](human/fichas/smolagents.md) · [Open SWE](human/fichas/open-swe.md)  
**Más:** [ficha completa](human/fichas/e2b.md) · [GitHub](https://github.com/e2b-dev/E2B)

#### 🛠️ NemoClaw
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 23k  
**Qué es:** Ejecuta agentes populares dentro de los sandboxes de NVIDIA OpenShell con inferencia gestionada y políticas de seguridad. Pensado para empresas.  
**Instalación:** Sigue la guía del repo (requiere el entorno de NVIDIA OpenShell).  
**Elige si:** quieres correr agentes potentes con aislamiento corporativo — **Evita si:** solo necesitas un sandbox para ejecutar código; mira `e2b`  
**Combina con:** [OpenClaw](human/fichas/openclaw.md) · [hermes-agent](human/fichas/hermes-agent.md) · [Nemotron (NVIDIA)](human/fichas/nemotron.md)  
**Más:** [ficha completa](human/fichas/nemoclaw.md) · [GitHub](https://github.com/NVIDIA/NemoClaw)

#### 📦 sandbox
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 6.3k  
**Qué es:** Resuelve el riesgo de dejar que un agente toque tu host: todo corre contenido en un contenedor reproducible.  
**Instalación:** `docker run` de la imagen del proyecto; requiere Docker y recursos suficientes para correr navegador + servicios en paralelo.  
**Elige si:** quieres aislar la ejecución de agentes y reproducibilidad — **Evita si:** te basta correr local sin sandbox o no puedes asumir el overhead de Docker  
**Combina con:** [OpenHands](human/fichas/openhands.md) · [ECC](human/fichas/ecc.md)  
**Más:** [ficha completa](human/fichas/sandbox.md) · [GitHub](https://github.com/agent-infra/sandbox)

#### 🛠️ Gemini Computer Use (preview)
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 3.3k  
**Qué es:** Muestra cómo un modelo Gemini con computer use controla un navegador para completar tareas. Es una vista previa, no un agente de propósito general.  
**Instalación:** Clona el repo, `pip install -r requirements.txt` y configura tu clave de Gemini.  
**Elige si:** quieres probar computer use con Gemini — **Evita si:** buscas automatización web robusta; mira `browser-use` o `stagehand`  
**Combina con:** [playwright](human/fichas/playwright.md)  
**Más:** [ficha completa](human/fichas/computer-use-preview.md) · [GitHub](https://github.com/google-gemini/computer-use-preview)

#### 🟩 NeMo-Agent-Toolkit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 2.7k  
**Qué es:** Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.  
**Instalación:** `pip install nvidia-nat` (o `git clone` del repo). Para sacar provecho real necesitas acceso a NIM/NGC o GPUs NVIDIA; de ahí el setup 🔴.  
**Elige si:** trabajas con infra NVIDIA o necesitas guardrails/eval empresarial — **Evita si:** quieres algo ligero y agnóstico  
**Combina con:** [langchain](human/fichas/langchain.md)  
**Más:** [ficha completa](human/fichas/nemo-agent-toolkit.md) · [GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

#### 🛠️ Agent Protocol
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 697  
**Qué es:** Define cómo se ejecuta un agente, cómo recibe entradas y cómo guarda su estado, sin atarse a un framework. Es una especificación, no un runtime.  
**Instalación:** No se instala: lee la especificación OpenAPI e impleméntala en tu servidor.  
**Elige si:** diseñas una plataforma que sirve agentes de distintos frameworks — **Evita si:** solo necesitas construir un agente  
**Combina con:** [LangGraph](human/fichas/langgraph.md)  
**Más:** [ficha completa](human/fichas/agent-protocol.md) · [GitHub](https://github.com/langchain-ai/agent-protocol)

### Simulación, evolución y debate entre modelos

#### 🐟 MiroFish ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 85.1k  
**Qué es:** Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.  
**Instalación:** Consulta el README del repo (`git clone` y ejecución en Python). Requiere claves de LLM para los agentes y cómputo no trivial para simulaciones grandes (de ahí el setup 🔴).  
**Elige si:** simulas futuros/escenarios con muchos actores — **Evita si:** necesitas tareas deterministas o resultados reproducibles  
**Combina con:** [openevolve](human/fichas/openevolve.md)  
**Más:** [ficha completa](human/fichas/mirofish.md) · [GitHub](https://github.com/666ghj/MiroFish)

#### 🏛️ llm-council
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 26.4k  
**Qué es:** Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.  
**Instalación:** `git clone` del repo y ejecución según su README. Requiere claves de varios proveedores de LLM (OpenAI, Anthropic, Google, xAI) para que el consejo tenga variedad.  
**Elige si:** quieres consenso entre modelos o comparar proveedores — **Evita si:** te basta un único LLM o el coste multi-modelo no es asumible  
**Combina con:** [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/llm-council.md) · [GitHub](https://github.com/karpathy/llm-council)

#### 🧬 openevolve
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 7.8k  
**Qué es:** Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.  
**Instalación:** `pip install openevolve` (o `git clone` del repo). Requiere un proveedor de LLM de frontera (Claude/GPT-4o) y, según el problema, cómputo no trivial para evaluar muchas generaciones.  
**Elige si:** optimizas problemas algorítmicos donde cabe explorar muchas variantes — **Evita si:** haces tareas de texto comunes o buscas respuesta inmediata  
**Combina con:** [llm-council](human/fichas/llm-council.md)  
**Más:** [ficha completa](human/fichas/openevolve.md) · [GitHub](https://github.com/algorithmicsuperintelligence/openevolve)

---

## 🕷️ 4. Scraping, Búsqueda & Research Web

Crawlers que entregan Markdown para IA, scraping guiado por LLM, navegadores automatizados, buscadores y redes sociales.

**⚖️ ¿Cuál elegir? — firecrawl, crawl4ai, Jina Reader**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [firecrawl](human/fichas/firecrawl.md) | alimentas agentes/RAG con web y quieres salida limpia | solo quieres HTML crudo o el presupuesto de API no encaja |
| [crawl4ai](human/fichas/crawl4ai.md) | necesitas volumen barato y self-host | quieres una API hosted simple sin operar navegadores (firecrawl) |
| [Jina Reader](human/fichas/jina-reader.md) | necesitas leer páginas como Markdown al instante | vas a rastrear sitios completos; mira `crawl4ai` o `firecrawl` |

**⚖️ ¿Cuál elegir? — Scrapegraph-ai, Maxun, llm-scraper**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Scrapegraph-ai](human/fichas/scrapegraph-ai.md) | quieres estructura semántica "by prompt" en Python | te basta un esquema simple (llm-scraper) o el coste de LLM por página es alto |
| [Maxun](human/fichas/maxun.md) | quieres extraer datos web sin programar | programas y prefieres librerías; mira `crawl4ai` o `scrapy` |
| [llm-scraper](human/fichas/llm-scraper.md) | quieres salida tipada y validada en stack TS | prefieres extracción semántica por grafos (Scrapegraph-ai) o trabajas en Python |

**⚖️ ¿Cuál elegir? — Stagehand, browser-use, Skyvern**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Stagehand](human/fichas/stagehand.md) | quieres automatización web robusta con un toque de IA en TS | quieres que un agente navegue solo; mira `browser-use` |
| [browser-use](human/fichas/browser-use.md) | quieres navegación como humano y tolerancia a cambios de UI | necesitas scripts deterministas y baratos (playwright) o no quieres depender de un LLM por paso |
| [Skyvern](human/fichas/skyvern.md) | automatizas portales web que cambian a menudo | necesitas scraping masivo y barato; mira `crawl4ai` |

**⚖️ ¿Cuál elegir? — playwright, Puppeteer, Selenium**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [playwright](human/fichas/playwright.md) | necesitas control preciso y reproducible del browser | quieres que el agente navegue por visión (browser-use) o no necesitas un navegador real |
| [Puppeteer](human/fichas/puppeteer.md) | trabajas en Node y quieres controlar Chrome | necesitas varios navegadores y pruebas E2E; mira `playwright` |
| [Selenium](human/fichas/selenium.md) | tu equipo ya usa Selenium o necesitas muchos lenguajes | empiezas de cero; mira `playwright` |

**⚖️ ¿Cuál elegir? — Agent-Reach, snscrape**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Agent-Reach](human/fichas/agent-reach.md) | tu agente necesita leer redes sociales sin APIs de pago | necesitas datos con garantías de términos de servicio |
| [snscrape](human/fichas/snscrape.md) | recolectas varias redes y no te sirve una API oficial | solo necesitas Instagram (instaloader) o la plataforma ya bloqueó el acceso no oficial |

### Crawlers y extracción para IA

#### 🔥 firecrawl ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 200k  
**Qué es:** Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. Se ha vuelto la opción de referencia para alimentar pipelines RAG y agentes con web limpia; muy adoptada y con integración MCP de primera clase.  
**Instalación:** API hosted con clave (`npm i @mendable/firecrawl-js` o `pip install firecrawl-py`); también self-host con Docker. Requiere una clave de API (gratuita con límite, de pago a escala) o infra para self-host.  
**Elige si:** alimentas agentes/RAG con web y quieres salida limpia — **Evita si:** solo quieres HTML crudo o el presupuesto de API no encaja  
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [crawl4ai](human/fichas/crawl4ai.md)  
**Más:** [ficha completa](human/fichas/firecrawl.md) · [GitHub](https://github.com/firecrawl/firecrawl)

#### 🩹 Scrapling
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 101k  
**Qué es:** Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. Proyecto en alza por su enfoque "auto-reparable" de selectores, que evita reescribir scrapers cada vez que el sitio se actualiza.  
**Instalación:** `pip install scrapling` (con `scrapling install` para los navegadores del modo sigiloso). Requiere Python y, para el modo stealth, los binarios de navegador que instala el subcomando.  
**Elige si:** los sitios cambian o te bloquean a menudo — **Evita si:** el target es estable y simple, o no necesitas stealth  
**Combina con:** [scrapy](human/fichas/scrapy.md)  
**Más:** [ficha completa](human/fichas/scrapling.md) · [GitHub](https://github.com/D4Vinci/Scrapling)

#### 🕷️ crawl4ai
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 87.2k  
**Qué es:** Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. Una de las alternativas open-source más populares a las APIs de pago; gratuita, self-host y muy activa en la comunidad de scraping para LLMs.  
**Instalación:** `pip install crawl4ai` seguido de `crawl4ai-setup` para instalar los navegadores de Playwright. Requiere Chromium (lo instala el setup) y, para LLM-extraction, una clave de proveedor.  
**Elige si:** necesitas volumen barato y self-host — **Evita si:** quieres una API hosted simple sin operar navegadores (firecrawl)  
**Combina con:** [firecrawl](human/fichas/firecrawl.md) · [gpt-researcher](human/fichas/gpt-researcher.md)  
**Más:** [ficha completa](human/fichas/crawl4ai.md) · [GitHub](https://github.com/unclecode/crawl4ai)

#### 🐍 scrapy
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 65.3k  
**Qué es:** Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. Estándar de facto del scraping en Python desde hace más de una década, con enorme ecosistema de extensiones y base instalada masiva.  
**Instalación:** `pip install scrapy`; el comando `scrapy startproject` genera el andamiaje del proyecto. Requiere Python y, según el target, rotación de proxies/headers para evitar bloqueos.  
**Elige si:** quieres un crawler sólido y configurable a escala — **Evita si:** buscas salida lista para LLM o algo puntual sin curva de framework  
**Combina con:** [scrapely](human/fichas/scrapely.md) · [crawlee-python](human/fichas/crawlee-python.md)  
**Más:** [ficha completa](human/fichas/scrapy.md) · [GitHub](https://github.com/scrapy/scrapy)

#### 🦗 crawlee
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 26.4k  
**Qué es:** Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. Mantenido por Apify, es la referencia de crawling en el ecosistema JavaScript y trae evasión de bloqueos lista de fábrica.  
**Instalación:** `npm i crawlee` o, para empezar, `npx crawlee create`. Requiere Node.js y, para el modo navegador, los binarios de Playwright/Puppeteer.  
**Elige si:** scrapeas con Node y necesitas antibloqueo — **Evita si:** trabajas en Python (crawlee-python) o no necesitas evasión  
**Combina con:** [playwright](human/fichas/playwright.md)  
**Más:** [ficha completa](human/fichas/crawlee.md) · [GitHub](https://github.com/apify/crawlee)

#### 🕷️ Jina Reader
**Etiquetas:** Ejecución ☁️ cloud/API · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 12.2k  
**Qué es:** Pega `https://r.jina.ai/` delante de una URL y obtienes su contenido limpio. También busca en la web con `s.jina.ai`.  
**Instalación:** No se instala: usa `curl https://r.jina.ai/https://ejemplo.com`; con clave de API tienes más cuota.  
**Elige si:** necesitas leer páginas como Markdown al instante — **Evita si:** vas a rastrear sitios completos; mira `crawl4ai` o `firecrawl`  
**Combina con:** [n8n](human/fichas/n8n.md) · [LlamaIndex](human/fichas/llama-index.md)  
**Más:** [ficha completa](human/fichas/jina-reader.md) · [GitHub](https://github.com/jina-ai/reader)

#### 🦗 crawlee-python
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 9.7k  
**Qué es:** Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. Acerca las ventajas del Crawlee de Node a quienes ya viven en Python, con respaldo oficial de Apify y adopción en crecimiento.  
**Instalación:** `pip install crawlee` (extras como `crawlee[playwright]` para el modo navegador). Requiere Python y, para el modo navegador, los binarios de Playwright.  
**Elige si:** quieres Crawlee en Python con antibloqueo — **Evita si:** ya usas scrapy y te basta, o no necesitas evasión  
**Combina con:** [scrapy](human/fichas/scrapy.md) · [playwright](human/fichas/playwright.md)  
**Más:** [ficha completa](human/fichas/crawlee-python.md) · [GitHub](https://github.com/apify/crawlee-python)

#### 📐 scrapely
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.9k  
**Qué es:** Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales. Pieza histórica del ecosistema Scrapy; nicho y poco activa hoy, pero útil cuando se quiere extraer "por demostración" en lugar de programar selectores.  
**Instalación:** `pip install scrapely`. Requiere Python; sin dependencias pesadas.  
**Elige si:** prefieres enseñar por ejemplos y el sitio es homogéneo — **Evita si:** necesitas un crawler completo o el proyecto exige mantenimiento activo  
**Combina con:** [scrapy](human/fichas/scrapy.md)  
**Más:** [ficha completa](human/fichas/scrapely.md) · [GitHub](https://github.com/scrapy/scrapely)

### Scraping guiado por LLM

#### 🕸️ Scrapegraph-ai ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 32.7k  
**Qué es:** Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. Muy popular por permitir scraping "by prompt", combinando extracción con razonamiento del modelo y soporte para múltiples proveedores.  
**Instalación:** `pip install scrapegraphai` más `playwright install` para el render dinámico. Requiere una clave de proveedor de LLM y los binarios de Playwright.  
**Elige si:** quieres estructura semántica "by prompt" en Python — **Evita si:** te basta un esquema simple (llm-scraper) o el coste de LLM por página es alto  
**Combina con:** [crawl4ai](human/fichas/crawl4ai.md) · [graphrag](human/fichas/graphrag.md)  
**Más:** [ficha completa](human/fichas/scrapegraph-ai.md) · [GitHub](https://github.com/ScrapeGraphAI/Scrapegraph-ai)

#### 🧠 Maxun
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.2k  
**Qué es:** Grabas lo que quieres extraer haciendo clic en la página y Maxun crea un robot que lo repite, con paginación y programación. Ideal para equipos sin programadores.  
**Instalación:** Self-host con `docker compose up -d` siguiendo el README.  
**Elige si:** quieres extraer datos web sin programar — **Evita si:** programas y prefieres librerías; mira `crawl4ai` o `scrapy`  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/maxun.md) · [GitHub](https://github.com/getmaxun/maxun)

#### 🧾 llm-scraper
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 7k  
**Qué es:** Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. Popular por su simplicidad: salida tipada y validada sin escribir parsers, integrándose directamente con Playwright y los SDKs de LLM.  
**Instalación:** `npm i llm-scraper playwright` y la SDK del proveedor de LLM elegido. Requiere Node.js, los binarios de Playwright y una clave de API de LLM.  
**Elige si:** quieres salida tipada y validada en stack TS — **Evita si:** prefieres extracción semántica por grafos (Scrapegraph-ai) o trabajas en Python  
**Combina con:** [playwright](human/fichas/playwright.md) · [firecrawl](human/fichas/firecrawl.md)  
**Más:** [ficha completa](human/fichas/llm-scraper.md) · [GitHub](https://github.com/mishushakov/llm-scraper)

### Navegadores y automatización web

#### 🌐 Stagehand ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 26k  
**Qué es:** Usa `act`, `extract` y `observe` para que la IA haga lo difícil y tu código lo predecible. Basado en Playwright.  
**Instalación:** `npx create-browser-app` o `npm i @browserbasehq/stagehand`.  
**Elige si:** quieres automatización web robusta con un toque de IA en TS — **Evita si:** quieres que un agente navegue solo; mira `browser-use`  
**Combina con:** [Mastra](human/fichas/mastra.md) · [playwright](human/fichas/playwright.md)  
**Más:** [ficha completa](human/fichas/stagehand.md) · [GitHub](https://github.com/browserbase/stagehand)

#### 🌐 browser-use
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 121k  
**Qué es:** Resuelve la fragilidad del scraping basado en CSS: el agente "ve" la página como un humano y decide la siguiente acción.  
**Instalación:** `pip install browser-use` y `playwright install`; requiere clave de un LLM con visión (OpenAI, Anthropic o Google). Para escala/stealth existe cloud gestionado.  
**Elige si:** quieres navegación como humano y tolerancia a cambios de UI — **Evita si:** necesitas scripts deterministas y baratos (playwright) o no quieres depender de un LLM por paso  
**Combina con:** [playwright](human/fichas/playwright.md) · [gpt-researcher](human/fichas/gpt-researcher.md)  
**Más:** [ficha completa](human/fichas/browser-use.md) · [GitHub](https://github.com/browser-use/browser-use)

#### 🎭 playwright
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 99.7k  
**Qué es:** Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. Se ha convertido en el estándar moderno de automatización de browser, desplazando a Selenium/Puppeteer por su fiabilidad y su auto-espera de elementos.  
**Instalación:** `npm i playwright` o `pip install playwright`, seguido de `playwright install` para los navegadores. Requiere descargar los binarios de Chromium/Firefox/WebKit (~varios cientos de MB).  
**Elige si:** necesitas control preciso y reproducible del browser — **Evita si:** quieres que el agente navegue por visión (browser-use) o no necesitas un navegador real  
**Combina con:** [browser-use](human/fichas/browser-use.md) · [crawlee](human/fichas/crawlee.md)  
**Más:** [ficha completa](human/fichas/playwright.md) · [GitHub](https://github.com/microsoft/playwright)

#### 🌐 Puppeteer
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 95.8k  
**Qué es:** Automatiza navegación, capturas, PDFs y pruebas. Es la base de muchas herramientas de scraping.  
**Instalación:** `npm i puppeteer` (descarga Chrome automáticamente).  
**Elige si:** trabajas en Node y quieres controlar Chrome — **Evita si:** necesitas varios navegadores y pruebas E2E; mira `playwright`  
**Combina con:** [Lightpanda](human/fichas/lightpanda.md)  
**Más:** [ficha completa](human/fichas/puppeteer.md) · [GitHub](https://github.com/puppeteer/puppeteer)

#### 🌐 Lightpanda
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 41.8k  
**Qué es:** Ejecuta JavaScript y es compatible con Puppeteer y Playwright por CDP, usando una fracción de memoria. Ideal para scraping masivo.  
**Instalación:** Descarga el binario de releases o `docker run -d -p 9222:9222 lightpanda/browser:nightly`.  
**Elige si:** necesitas muchos navegadores headless con poca memoria — **Evita si:** necesitas compatibilidad total con sitios complejos; usa Chrome con `playwright`  
**Combina con:** [Puppeteer](human/fichas/puppeteer.md) · [playwright](human/fichas/playwright.md)  
**Más:** [ficha completa](human/fichas/lightpanda.md) · [GitHub](https://github.com/lightpanda-io/browser)

#### 🌐 Selenium
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 34.6k  
**Qué es:** Estándar W3C WebDriver, muy usado en pruebas empresariales con Selenium Grid para paralelizar.  
**Instalación:** `pip install selenium` (o el paquete de tu lenguaje).  
**Elige si:** tu equipo ya usa Selenium o necesitas muchos lenguajes — **Evita si:** empiezas de cero; mira `playwright`  
**Más:** [ficha completa](human/fichas/selenium.md) · [GitHub](https://github.com/SeleniumHQ/selenium)

#### 🌐 Skyvern
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 23.4k  
**Qué es:** Completa formularios, compras o descargas en sitios que nunca vio, entendiendo la página con visión. Incluye UI, API y workflows.  
**Instalación:** `pip install skyvern` y `skyvern quickstart`, o Docker Compose.  
**Elige si:** automatizas portales web que cambian a menudo — **Evita si:** necesitas scraping masivo y barato; mira `crawl4ai`  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/skyvern.md) · [GitHub](https://github.com/Skyvern-AI/skyvern)

#### 🌐 Browser Harness
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 19k  
**Qué es:** Conecta el agente a tu navegador por CDP con un arnés pequeño y editable. Útil cuando necesitas libertad total y tus cuentas ya abiertas.  
**Instalación:** Sigue el README: pide a tu agente que lo instale con el prompt indicado.  
**Elige si:** tu agente debe usar tu navegador real con sesión — **Evita si:** necesitas aislamiento; mira `playwright-mcp`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)  
**Más:** [ficha completa](human/fichas/browser-harness.md) · [GitHub](https://github.com/browser-use/browser-harness)

#### 🎭 playwright-cli
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 15.1k  
**Qué es:** Resuelve el problema de los árboles de accesibilidad y los JSON de herramientas que inflan el prompt en cada turno.  
**Instalación:** Parte del ecosistema Playwright; se usa vía `npx playwright`/`npm` dentro del agente de código. Requiere Node.js y los binarios de navegador (`npx playwright install`).  
**Elige si:** tu agente vive en CLI y el contexto es un recurso caro — **Evita si:** necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP)  
**Combina con:** [playwright](human/fichas/playwright.md) · [browser-use](human/fichas/browser-use.md)  
**Más:** [ficha completa](human/fichas/playwright-cli.md) · [GitHub](https://github.com/microsoft/playwright-cli)

### Búsqueda, monitoreo y research web

#### 🔍 SearXNG ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 39.4k  
**Qué es:** Combina resultados de más de 70 servicios sin rastrearte. Muchos agentes de investigación lo usan como API de búsqueda gratuita y propia.  
**Instalación:** `docker run -d -p 8080:8080 searxng/searxng` y habilita el formato JSON en `settings.yml`.  
**Elige si:** tus agentes necesitan buscar en la web sin coste por consulta — **Evita si:** necesitas resultados con SLA comercial  
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [Open WebUI](human/fichas/open-webui.md) · [Vane](human/fichas/vane.md)  
**Más:** [ficha completa](human/fichas/searxng.md) · [GitHub](https://github.com/searxng/searxng)

#### 🔍 Agent-Reach
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 111k  
**Qué es:** Un solo comando para que el agente lea y busque en redes y plataformas populares, incluidas chinas como Bilibili y XiaoHongShu.  
**Instalación:** Sigue el README: `pip install` del paquete y configura cookies si alguna plataforma lo pide.  
**Elige si:** tu agente necesita leer redes sociales sin APIs de pago — **Evita si:** necesitas datos con garantías de términos de servicio  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [last30days](human/fichas/last30days-skill.md)  
**Más:** [ficha completa](human/fichas/agent-reach.md) · [GitHub](https://github.com/Panniantong/Agent-Reach)

#### 🔍 last30days
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 67.2k  
**Qué es:** Busca lo que la gente está diciendo ahora sobre un tema y lo resume con fuentes. Prioriza señales reales como votos, likes y apuestas.  
**Instalación:** Instálala como skill en Claude Code siguiendo el README (copia a `.claude/skills/`).  
**Elige si:** quieres saber qué se dice ahora sobre un tema — **Evita si:** necesitas un informe académico; mira `storm`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Agent-Reach](human/fichas/agent-reach.md)  
**Más:** [ficha completa](human/fichas/last30days-skill.md) · [GitHub](https://github.com/mvanhorn/last30days-skill)

#### 🔍 Vane
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 38.1k  
**Qué es:** Busca en la web con SearXNG y responde con citas usando modelos locales o en la nube. Incluye modos de enfoque para académico, YouTube o Reddit.  
**Instalación:** `docker run -d -p 3000:3000 itzcrazykns1337/vane:latest` (incluye SearXNG).  
**Elige si:** quieres un buscador con respuestas citadas auto-hospedado — **Evita si:** necesitas informes largos; mira `gpt-researcher`  
**Combina con:** [SearXNG](human/fichas/searxng.md) · [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/vane.md) · [GitHub](https://github.com/ItzCrazyKns/Vane)

#### 🔍 changedetection.io
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 35.7k  
**Qué es:** Vigila precios, stock, documentación o cualquier texto de una página y te avisa cuando cambia. Admite navegador real para sitios con JavaScript.  
**Instalación:** `docker run -d -p 5000:5000 -v datastore:/datastore dgtlmoon/changedetection.io`.  
**Elige si:** quieres alertas cuando cambia una página — **Evita si:** necesitas extraer datos estructurados; mira `maxun`  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/changedetection.md) · [GitHub](https://github.com/dgtlmoon/changedetection.io)

#### 🔍 ArchiveBox
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 29k  
**Qué es:** Le das URLs, marcadores o historial y guarda copias completas para siempre. Útil para investigación y preservación de fuentes.  
**Instalación:** `docker run -it -v $PWD:/data archivebox/archivebox init --setup`.  
**Elige si:** quieres conservar copias fieles de páginas web — **Evita si:** solo necesitas el texto para un LLM; mira `jina-reader`  
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md)  
**Más:** [ficha completa](human/fichas/archivebox.md) · [GitHub](https://github.com/ArchiveBox/ArchiveBox)

### Redes sociales y descarga de medios

#### 📱 yt-dlp ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 207k  
**Qué es:** Descarga videos, audios, subtítulos y metadatos de YouTube y miles de plataformas. Base de muchos pipelines de transcripción.  
**Instalación:** `pip install yt-dlp` o `brew install yt-dlp`.  
**Elige si:** necesitas bajar audio o video de la web — **Evita si:** solo necesitas metadatos sociales; mira `instaloader`  
**Combina con:** [whisperX](human/fichas/whisperx.md) · [FFmpeg](human/fichas/ffmpeg.md) · [Fabric](human/fichas/fabric.md)  
**Más:** [ficha completa](human/fichas/yt-dlp.md) · [GitHub](https://github.com/yt-dlp/yt-dlp)

#### 📸 instaloader
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13.8k  
**Qué es:** Resuelve el archivado masivo de Instagram sin recurrir a APIs oficiales de pago ni herramientas manuales.  
**Instalación:** `pip install instaloader`; se usa como CLI (`instaloader perfil`) o importando el módulo. Para contenido privado o límites altos hace falta iniciar sesión con una cuenta de Instagram.  
**Elige si:** necesitas datos de Instagram de forma fiable — **Evita si:** quieres varias redes a la vez (snscrape) o el contenido requiere API oficial por ToS  
**Combina con:** [snscrape](human/fichas/snscrape.md)  
**Más:** [ficha completa](human/fichas/instaloader.md) · [GitHub](https://github.com/instaloader/instaloader)

#### 🐦 snscrape
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 5.5k  
**Qué es:** Resuelve la recolección histórica de datos sociales cuando las APIs de pago no son viables o no existen.  
**Instalación:** `pip install snscrape` (o desde el repo para la versión de desarrollo, que suele ir por delante de PyPI). Algunas redes requieren sesión o cookies para funcionar.  
**Elige si:** recolectas varias redes y no te sirve una API oficial — **Evita si:** solo necesitas Instagram (instaloader) o la plataforma ya bloqueó el acceso no oficial  
**Combina con:** [instaloader](human/fichas/instaloader.md)  
**Más:** [ficha completa](human/fichas/snscrape.md) · [GitHub](https://github.com/JustAnotherArchivist/snscrape)

---

## 🔌 5. MCP & Conectividad

SDKs para crear servidores MCP, servidores destacados (navegador, GitHub, diseño, 3D), directorios y APIs públicas.

**⚖️ ¿Cuál elegir? — FastMCP, MCP Python SDK**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [FastMCP](human/fichas/fastmcp.md) | quieres crear un servidor MCP en Python rápido | trabajas en TypeScript; mira `mcp-typescript-sdk` |
| [MCP Python SDK](human/fichas/mcp-python-sdk.md) | quieres el SDK oficial con mínima dependencia | quieres funciones extra como auth y composición; mira `fastmcp` |

**⚖️ ¿Cuál elegir? — MCP TypeScript SDK, mcp-use, LangChain MCP Adapters**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [MCP TypeScript SDK](human/fichas/mcp-typescript-sdk.md) | creas servidores MCP en TypeScript | trabajas en Python; mira `fastmcp` |
| [mcp-use](human/fichas/mcp-use.md) | construyes un servidor MCP propio y quieres productividad | solo buscas usar uno ya hecho (awesome-mcp-servers) o necesitas control a nivel spec |
| [LangChain MCP Adapters](human/fichas/langchain-mcp-adapters.md) | usas LangGraph y quieres herramientas MCP | no usas LangChain |

**⚖️ ¿Cuál elegir? — Playwright MCP, Chrome DevTools MCP**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Playwright MCP](human/fichas/playwright-mcp.md) | quieres que tu agente use un navegador real | necesitas depurar rendimiento y consola; mira `chrome-devtools-mcp` |
| [Chrome DevTools MCP](human/fichas/chrome-devtools-mcp.md) | tu agente necesita depurar una web como lo harías en DevTools | solo quieres automatizar navegación; mira `playwright-mcp` |

### SDKs y frameworks para crear MCP

#### 🧰 FastMCP ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 28.4k  
**Qué es:** Convierte funciones Python en herramientas MCP con un decorador y añade autenticación, composición de servidores y cliente de pruebas. Su versión 1 se integró en el SDK oficial.  
**Instalación:** `pip install fastmcp` (o `uv add fastmcp`).  
**Elige si:** quieres crear un servidor MCP en Python rápido — **Evita si:** trabajas en TypeScript; mira `mcp-typescript-sdk`  
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md) · [Claude Code](human/fichas/claude-code.md)  
**Más:** [ficha completa](human/fichas/fastmcp.md) · [GitHub](https://github.com/PrefectHQ/fastmcp)

#### 🧰 MCP TypeScript SDK ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13.7k  
**Qué es:** Base de la mayoría de servidores MCP en Node.js, con transportes stdio y HTTP.  
**Instalación:** `npm install @modelcontextprotocol/sdk`.  
**Elige si:** creas servidores MCP en TypeScript — **Evita si:** trabajas en Python; mira `fastmcp`  
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md)  
**Más:** [ficha completa](human/fichas/mcp-typescript-sdk.md) · [GitHub](https://github.com/modelcontextprotocol/typescript-sdk)

#### 🧰 MCP Python SDK
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 24.8k  
**Qué es:** Implementación de referencia del protocolo en Python, con la API FastMCP integrada para servidores sencillos.  
**Instalación:** `pip install "mcp[cli]"`.  
**Elige si:** quieres el SDK oficial con mínima dependencia — **Evita si:** quieres funciones extra como auth y composición; mira `fastmcp`  
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md)  
**Más:** [ficha completa](human/fichas/mcp-python-sdk.md) · [GitHub](https://github.com/modelcontextprotocol/python-sdk)

#### 🧰 MCP Inspector
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 11.3k  
**Qué es:** Conéctate a cualquier servidor MCP, lista sus herramientas y recursos y lánzalos a mano para ver respuestas y errores.  
**Instalación:** `npx @modelcontextprotocol/inspector` y apunta a tu servidor.  
**Elige si:** desarrollas un servidor MCP — **Evita si:** solo usas servidores ya hechos  
**Combina con:** [FastMCP](human/fichas/fastmcp.md) · [MCP TypeScript SDK](human/fichas/mcp-typescript-sdk.md)  
**Más:** [ficha completa](human/fichas/mcp-inspector.md) · [GitHub](https://github.com/modelcontextprotocol/inspector)

#### 🛠️ mcp-use
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 10.9k  
**Qué es:** Resuelve el salto del SDK base (verboso) a algo productivo: registro de tools, inspector y despliegue incluidos.  
**Instalación:** `npm install mcp-use` o `pip install mcp-use` según el stack; requiere un cliente MCP para probar el resultado.  
**Elige si:** construyes un servidor MCP propio y quieres productividad — **Evita si:** solo buscas usar uno ya hecho (awesome-mcp-servers) o necesitas control a nivel spec  
**Combina con:** [mcp](human/fichas/mcp.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)  
**Más:** [ficha completa](human/fichas/mcp-use.md) · [GitHub](https://github.com/mcp-use/mcp-use)

#### 🧰 LangChain MCP Adapters
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 3.6k  
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.  
**Qué es:** Permite que tus agentes de LangGraph usen cualquier servidor MCP sin escribir adaptadores. El repo está archivado y su función se integró en LangChain.  
**Instalación:** `pip install langchain-mcp-adapters`.  
**Elige si:** usas LangGraph y quieres herramientas MCP — **Evita si:** no usas LangChain  
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [langchain](human/fichas/langchain.md)  
**Más:** [ficha completa](human/fichas/langchain-mcp-adapters.md) · [GitHub](https://github.com/langchain-ai/langchain-mcp-adapters)

### Servidores MCP destacados

#### 🔌 Context7 ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 64.5k  
**Qué es:** Evita que el modelo invente APIs viejas: busca la documentación vigente de la librería que estás usando y la inyecta en el prompt.  
**Instalación:** Añade a tu cliente MCP: `npx -y @upstash/context7-mcp` (o el servidor remoto con clave).  
**Elige si:** tu agente de código usa librerías que cambian a menudo — **Evita si:** trabajas sin conexión a internet  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Cline](human/fichas/cline.md) · [OpenCode](human/fichas/opencode.md)  
**Más:** [ficha completa](human/fichas/context7.md) · [GitHub](https://github.com/upstash/context7)

#### 🔌 Playwright MCP ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 39.4k  
**Qué es:** Da a tu agente un navegador real controlado por el árbol de accesibilidad, sin depender de capturas. Ideal para pruebas y automatización web.  
**Instalación:** Añade a tu cliente MCP: `npx @playwright/mcp@latest`.  
**Elige si:** quieres que tu agente use un navegador real — **Evita si:** necesitas depurar rendimiento y consola; mira `chrome-devtools-mcp`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [playwright](human/fichas/playwright.md)  
**Más:** [ficha completa](human/fichas/playwright-mcp.md) · [GitHub](https://github.com/microsoft/playwright-mcp)

#### 📚 servers
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 91.9k  
**Qué es:** Resuelve la falta de ejemplos canónicos: muestra cómo se construye un servidor MCP correcto, paso a paso.  
**Instalación:** Ejecutar un servidor del repo con `npx` (p. ej. `npx -y @modelcontextprotocol/server-filesystem /ruta`) y añadirlo a la config del cliente MCP. Requiere Node.js para los servers TS.  
**Elige si:** quieres ejemplos canónicos y plantillas fiables — **Evita si:** buscas soluciones listas para producción (son demos educativas, no hardening)  
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)  
**Más:** [ficha completa](human/fichas/servers.md) · [GitHub](https://github.com/modelcontextprotocol/servers)

#### 🔌 Chrome DevTools MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 55.1k  
**Qué es:** Tu agente de código puede abrir páginas, leer errores de consola, inspeccionar peticiones y medir rendimiento para depurar de verdad.  
**Instalación:** Añade a tu cliente MCP: `npx chrome-devtools-mcp@latest`.  
**Elige si:** tu agente necesita depurar una web como lo harías en DevTools — **Evita si:** solo quieres automatizar navegación; mira `playwright-mcp`  
**Combina con:** [Claude Code](human/fichas/claude-code.md)  
**Más:** [ficha completa](human/fichas/chrome-devtools-mcp.md) · [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)

#### 🔌 GitHub MCP Server
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 34.4k  
**Qué es:** Conecta asistentes y agentes con la plataforma GitHub: repositorios, issues, pull requests, Actions y seguridad.  
**Instalación:** Usa el servidor remoto `https://api.githubcopilot.com/mcp/` o `docker run -i ghcr.io/github/github-mcp-server` con tu token.  
**Elige si:** tu agente trabaja con GitHub — **Evita si:** usas otra forja como GitLab  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)  
**Más:** [ficha completa](human/fichas/github-mcp-server.md) · [GitHub](https://github.com/github/github-mcp-server)

#### 🔌 Blender MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 33.9k  
**Qué es:** Crea y modifica escenas, objetos y materiales hablando con tu asistente. Útil para prototipos 3D rápidos.  
**Instalación:** Instala el addon en Blender y añade a tu cliente MCP: `uvx blender-mcp`.  
**Elige si:** quieres manejar Blender con tu agente — **Evita si:** no trabajas en 3D  
**Combina con:** [Claude Code](human/fichas/claude-code.md)  
**Más:** [ficha completa](human/fichas/blender-mcp.md) · [GitHub](https://github.com/ahujasid/mcp-for-blender)

#### 🔌 Serena
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 31.3k  
**Qué es:** En vez de leer archivos enteros, el agente busca símbolos, referencias y edita a nivel de función usando servidores de lenguaje. Ahorra tokens en repos grandes.  
**Instalación:** Añade a tu cliente MCP: `uvx --from git+https://github.com/oraios/serena serena start-mcp-server`.  
**Elige si:** tu agente trabaja en un repo grande y gasta muchos tokens leyendo — **Evita si:** tu proyecto es pequeño  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)  
**Más:** [ficha completa](human/fichas/serena.md) · [GitHub](https://github.com/oraios/serena)

#### 🔌 Figma Context MCP
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 16.2k  
**Qué es:** Simplifica la respuesta de la API de Figma y da al agente solo lo relevante (estructura, estilos, medidas) para convertir un diseño en código.  
**Instalación:** Añade a tu cliente MCP: `npx -y figma-developer-mcp --figma-api-key=TU_TOKEN --stdio`.  
**Elige si:** implementas diseños de Figma con un agente de código — **Evita si:** no usas Figma  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [ui](human/fichas/ui.md) · [tailwindcss](human/fichas/tailwindcss.md)  
**Más:** [ficha completa](human/fichas/figma-context-mcp.md) · [GitHub](https://github.com/GLips/Figma-Context-MCP)

#### 🕸️ mcp-neo4j
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 989  
**Qué es:** Resuelve el acceso natural a grafos desde un LLM: el asistente consulta y escribe Cypher sin que tú escribas el glue a mano.  
**Instalación:** `pip install mcp-neo4j-cypher` (o imagen Docker) y registrar el servidor en la config del cliente MCP. Requiere una instancia Neo4j accesible (local o Aura cloud) con credenciales.  
**Elige si:** usas Neo4j con IA y quieres que el asistente hable Cypher — **Evita si:** no trabajas con grafos o tu base es relacional pura  
**Combina con:** [graphrag](human/fichas/graphrag.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)  
**Más:** [ficha completa](human/fichas/mcp-neo4j.md) · [GitHub](https://github.com/neo4j-contrib/mcp-neo4j)

### Directorios, clientes y aprendizaje

#### 📚 MCP for Beginners ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 17.6k  
**Qué es:** Explica los fundamentos del Model Context Protocol, seguridad y despliegue con ejercicios por lenguaje. Disponible en varios idiomas.  
**Instalación:** No se instala: abre el repo y sigue las lecciones.  
**Elige si:** quieres aprender MCP de forma estructurada — **Evita si:** ya construyes servidores MCP; ve directo a `fastmcp`  
**Combina con:** [FastMCP](human/fichas/fastmcp.md) · [MCP Inspector](human/fichas/mcp-inspector.md)  
**Más:** [ficha completa](human/fichas/mcp-for-beginners.md) · [GitHub](https://github.com/microsoft/mcp-for-beginners)

#### 🌍 public-apis
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 498k  
**Qué es:** Resuelve el descubrimiento: en un solo lugar tienes URLs, autenticación y HTTPS de cada API en lugar de buscarlas una a una.  
**Instalación:** Sin instalación; se navega el README (o su versión web) y se consume cada API según su propia documentación y claves.  
**Elige si:** buscas datos externos y no sabes qué API usar — **Evita si:** ya tienes tus fuentes definidas o necesitas SLA empresarial (son APIs públicas, sin garantías)  
**Combina con:** [n8n](human/fichas/n8n.md) · [firecrawl](human/fichas/firecrawl.md)  
**Más:** [ficha completa](human/fichas/public-apis.md) · [GitHub](https://github.com/public-apis/public-apis)

#### 🗂️ awesome-mcp-servers
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 97.6k  
**Qué es:** Resuelve el "¿ya existe un servidor para X?" antes de que construyas el tuyo desde cero.  
**Instalación:** Sin instalación propia; se consulta el README y luego se instala el servidor elegido (normalmente vía `npx` o `pip`) y se registra en el cliente MCP.  
**Elige si:** buscas antes de construir — **Evita si:** ya sabes que necesitas uno a medida y no te vale ninguno listado  
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [servers](human/fichas/servers.md)  
**Más:** [ficha completa](human/fichas/awesome-mcp-servers.md) · [GitHub](https://github.com/punkpeye/awesome-mcp-servers)

#### 📚 Awesome MCP Clients
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 6.6k  
**Qué es:** Ayuda a elegir dónde usar tus servidores MCP: chats de escritorio, editores, CLIs y plataformas.  
**Instalación:** No se instala: abre el repo y consulta la lista.  
**Elige si:** buscas un cliente para tus servidores MCP — **Evita si:** buscas servidores; mira `awesome-mcp-servers`  
**Combina con:** [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)  
**Más:** [ficha completa](human/fichas/awesome-mcp-clients.md) · [GitHub](https://github.com/punkpeye/awesome-mcp-clients)

#### 🧩 mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 4.7k  
**Qué es:** Resuelve la fragmentación: cada integración de IA dejaba de ser ad-hoc y pasa a hablar un protocolo común.  
**Instalación:** `npm install @modelcontextprotocol/sdk` o `pip install mcp` según el lenguaje; requiere un cliente MCP (Claude Desktop, Cursor, etc.) para conectar.  
**Elige si:** programas MCP a bajo nivel o necesitas conformidad estricta con la spec — **Evita si:** prefieres un framework de alto nivel que abstraiga el protocolo (mcp-use)  
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [servers](human/fichas/servers.md)  
**Más:** [ficha completa](human/fichas/mcp.md) · [GitHub](https://github.com/google/mcp)

---

## 🧬 6. Memoria, RAG & LLM Ops

Memoria persistente para agentes, RAG, bases vectoriales, serving y gateways de LLM, ahorro de tokens y observabilidad.

**⚖️ ¿Cuál elegir? — claude-mem, RAGFlow, mem0, LightRAG, PageIndex, graphrag, cognee**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [claude-mem](human/fichas/claude-mem.md) | usas Claude Code a diario y repites contexto entre sesiones | necesitas memoria para una app propia; mira `mem0` |
| [RAGFlow](human/fichas/ragflow.md) | tus documentos son complejos y necesitas citas fiables | quieres algo ligero en un portátil; mira `anything-llm` |
| [mem0](human/fichas/mem0.md) | quieres memoria estándar lista con integraciones amplias | necesitas todo local sin llamadas a API (mempalace) o control total del almacenamiento |
| [LightRAG](human/fichas/lightrag.md) | quieres RAG con grafo sin el coste de GraphRAG | no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index` |
| [PageIndex](human/fichas/pageindex.md) | tus documentos son largos y con estructura clara | tienes miles de documentos cortos; usa búsqueda vectorial |
| [graphrag](human/fichas/graphrag.md) | tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto | un RAG simple basta o el coste de indexado con LLM es prohibitivo |
| [cognee](human/fichas/cognee.md) | quieres memoria basada en grafo con poco esfuerzo | necesitas un grafo temporal en tiempo real; mira `graphiti` |

**⚖️ ¿Cuál elegir? — Qdrant, Milvus, Faiss, Chroma, pgvector**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Qdrant](human/fichas/qdrant.md) | quieres una base vectorial dedicada y rápida | ya tienes PostgreSQL y poco volumen; mira `pgvector` |
| [Milvus](human/fichas/milvus.md) | esperas volúmenes muy grandes de vectores | tu proyecto es pequeño; mira `chroma` o `qdrant` |
| [Faiss](human/fichas/faiss.md) | necesitas índices vectoriales en memoria y máximo control | quieres persistencia y API listas; mira `qdrant` |
| [Chroma](human/fichas/chroma.md) | empiezas con RAG y quieres lo más simple | necesitas gran escala y filtros complejos; mira `qdrant` o `milvus` |
| [pgvector](human/fichas/pgvector.md) | ya usas PostgreSQL y quieres vectores | tienes volúmenes muy grandes; mira `milvus` |

**⚖️ ¿Cuál elegir? — vLLM, SGLang**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [vLLM](human/fichas/vllm.md) | necesitas servir LLM abiertos a muchos usuarios en GPU | solo los usas tú en un portátil; mira `ollama` |
| [SGLang](human/fichas/sglang.md) | buscas el máximo rendimiento en servicio de LLM | quieres la opción más documentada; mira `vllm` |

**⚖️ ¿Cuál elegir? — promptfoo, DeepEval, Ragas**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [promptfoo](human/fichas/promptfoo.md) | quieres pruebas automáticas de prompts y seguridad | necesitas observabilidad en producción; mira `langfuse` |
| [DeepEval](human/fichas/deepeval.md) | quieres tests de LLM en Python como pytest | prefieres configurar en YAML y comparar modelos; mira `promptfoo` |
| [Ragas](human/fichas/ragas.md) | evalúas un sistema RAG | necesitas red teaming de seguridad; mira `promptfoo` |

**⚖️ ¿Cuál elegir? — langfuse, MLflow, Opik, Phoenix**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [langfuse](human/fichas/langfuse.md) | operas agentes en serio y necesitas trazas/costes/eval | haces prototipos triviales o no quieres operar el backend |
| [MLflow](human/fichas/mlflow.md) | tu equipo hace ML clásico y LLM y quiere una sola plataforma | solo trazas LLM y quieres algo más ligero; mira `langfuse` |
| [Opik](human/fichas/opik.md) | quieres observabilidad y evaluación en un solo producto abierto | prefieres la opción más extendida; mira `langfuse` |
| [Phoenix](human/fichas/phoenix.md) | quieres observabilidad basada en OpenTelemetry | buscas la plataforma más usada; mira `langfuse` |

### Memoria persistente para agentes

#### 🧠 claude-mem ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 116k  
**Qué es:** Registra lo que hace el agente en cada sesión, lo resume y vuelve a inyectar lo relevante al empezar la siguiente. Evita repetir contexto en proyectos largos.  
**Instalación:** En Claude Code: `/plugin marketplace add thedotmack/claude-mem` y `/plugin install claude-mem`.  
**Elige si:** usas Claude Code a diario y repites contexto entre sesiones — **Evita si:** necesitas memoria para una app propia; mira `mem0`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [superpowers](human/fichas/superpowers.md)  
**Más:** [ficha completa](human/fichas/claude-mem.md) · [GitHub](https://github.com/thedotmack/claude-mem)

#### 🧠 mem0
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 68.7k  
**Qué es:** Resuelve el "amnesia" del LLM: el agente conserva preferencias y hechos entre sesiones sin reenviar todo el historial.  
**Instalación:** `pip install mem0ai` (también SDK en npm) o servicio gestionado; requiere un LLM y una vector DB configurados (o los defaults del cloud).  
**Elige si:** quieres memoria estándar lista con integraciones amplias — **Evita si:** necesitas todo local sin llamadas a API (mempalace) o control total del almacenamiento  
**Combina con:** [crewAI](human/fichas/crewai.md) · [langchain](human/fichas/langchain.md) · [agentmemory](human/fichas/agentmemory.md)  
**Más:** [ficha completa](human/fichas/mem0.md) · [GitHub](https://github.com/mem0ai/mem0)

#### 🏛️ mempalace
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 60.5k  
**Qué es:** Resuelve la memoria privada: cero llamadas a API, tus textos no salen de tu máquina.  
**Instalación:** `pip install` desde PyPI; se configura el backend de búsqueda local según el repo. No requiere claves de API ni servicios externos.  
**Elige si:** la privacidad es prioridad y no quieres llamadas a API — **Evita si:** quieres un SaaS gestionado con escalado automático o integraciones de framework ya hechas (mem0)  
**Combina con:** [open-notebook](human/fichas/open-notebook.md) · [odysseus](human/fichas/odysseus.md)  
**Más:** [ficha completa](human/fichas/mempalace.md) · [GitHub](https://github.com/MemPalace/mempalace)

#### 🧠 cognee
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 33.2k  
**Qué es:** Convierte documentos y conversaciones en un grafo de conocimiento consultable para dar memoria de largo plazo a tus agentes.  
**Instalación:** `pip install cognee`.  
**Elige si:** quieres memoria basada en grafo con poco esfuerzo — **Evita si:** necesitas un grafo temporal en tiempo real; mira `graphiti`  
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [mcp-neo4j](human/fichas/mcp-neo4j.md)  
**Más:** [ficha completa](human/fichas/cognee.md) · [GitHub](https://github.com/topoteretes/cognee)

#### 🧠 Graphiti
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 32.7k  
**Qué es:** Actualiza el grafo con cada nuevo dato sin recalcular todo y guarda cuándo era válido cada hecho. Ideal para memoria de agentes que cambia.  
**Instalación:** `pip install graphiti-core` (requiere Neo4j o FalkorDB).  
**Elige si:** necesitas memoria que cambie con el tiempo y se pueda consultar — **Evita si:** solo quieres RAG sobre documentos estáticos; mira `lightrag`  
**Combina con:** [mcp-neo4j](human/fichas/mcp-neo4j.md)  
**Más:** [ficha completa](human/fichas/graphiti.md) · [GitHub](https://github.com/getzep/graphiti)

#### 🧠 supermemory
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 31.6k  
**Qué es:** Guarda y recupera lo que importa de documentos, conversaciones y webs para dar contexto a tus modelos. Ofrece API, SDK y una app de usuario.  
**Instalación:** `npm i supermemory` para su API, o sigue el README para self-host.  
**Elige si:** quieres una API de memoria lista para tu app — **Evita si:** prefieres librería en Python; mira `mem0`  
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md)  
**Más:** [ficha completa](human/fichas/supermemory.md) · [GitHub](https://github.com/supermemoryai/supermemory)

#### 💾 agentmemory
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.3k  
**Qué es:** Resuelve el "re-explica todo" al cambiar de asistente: la memoria vive fuera del cliente.  
**Instalación:** Instalación del servidor MCP según el repo y configuración en cada cliente compatible (Claude Code, Cursor, etc.); requiere el motor iii como backend.  
**Elige si:** cambias de asistente y quieres una memoria común entre ellos — **Evita si:** te basta la memoria nativa de un único cliente o no usas MCP  
**Combina con:** [mem0](human/fichas/mem0.md) · [ruflo](human/fichas/ruflo.md)  
**Más:** [ficha completa](human/fichas/agentmemory.md) · [GitHub](https://github.com/rohitg00/agentmemory)

#### 🧠 Letta
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 25.4k  
**Qué es:** Crea agentes que gestionan su propia memoria en bloques editables y archivos, y persisten entre conversaciones. Incluye servidor, API y entorno de desarrollo.  
**Instalación:** `docker run -p 8283:8283 letta/letta:latest` o `pip install letta-client` para su cloud.  
**Elige si:** quieres agentes con memoria de largo plazo gestionada — **Evita si:** solo necesitas una capa de memoria para tu app; mira `mem0`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/letta.md) · [GitHub](https://github.com/letta-ai/letta)

#### 🧠 Engram
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 7.9k  
**Qué es:** Da a cualquier agente compatible con MCP una memoria local de decisiones y aprendizajes, sin dependencias pesadas.  
**Instalación:** `brew install gentleman-programming/tap/engram` o binario de releases; luego añádelo como servidor MCP.  
**Elige si:** quieres memoria local simple para cualquier agente — **Evita si:** solo usas Claude Code y quieres algo automático; mira `claude-mem`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [OpenCode](human/fichas/opencode.md)  
**Más:** [ficha completa](human/fichas/engram.md) · [GitHub](https://github.com/Gentleman-Programming/engram)

### RAG y motores de conocimiento

#### 📎 RAGFlow ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 94k  
**Qué es:** Procesa PDFs, tablas e imágenes con parsing visual, crea bases de conocimiento con citas trazables y añade agentes y workflows.  
**Instalación:** `git clone https://github.com/infiniflow/ragflow && cd ragflow/docker && docker compose up -d`.  
**Elige si:** tus documentos son complejos y necesitas citas fiables — **Evita si:** quieres algo ligero en un portátil; mira `anything-llm`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [Docling](human/fichas/docling.md)  
**Más:** [ficha completa](human/fichas/ragflow.md) · [GitHub](https://github.com/infiniflow/ragflow)

#### 📎 LightRAG
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 40.6k  
**Qué es:** Construye un grafo de entidades a partir de tus documentos y consulta en modo local, global o híbrido. Más barato que GraphRAG.  
**Instalación:** `pip install lightrag-hku` (incluye servidor con UI: `lightrag-server`).  
**Elige si:** quieres RAG con grafo sin el coste de GraphRAG — **Evita si:** no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md)  
**Más:** [ficha completa](human/fichas/lightrag.md) · [GitHub](https://github.com/HKUDS/LightRAG)

#### 📎 PageIndex
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.3k  
**Qué es:** Genera un árbol tipo índice del documento y deja que el LLM navegue por él como un experto. Funciona bien con informes largos y estructurados.  
**Instalación:** `pip install pageindex` o clona el repo y usa su script con tu clave de OpenAI.  
**Elige si:** tus documentos son largos y con estructura clara — **Evita si:** tienes miles de documentos cortos; usa búsqueda vectorial  
**Combina con:** [Docling](human/fichas/docling.md)  
**Más:** [ficha completa](human/fichas/pageindex.md) · [GitHub](https://github.com/VectifyAI/PageIndex)

#### 🔗 graphrag
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 36.6k  
**Qué es:** Resuelve las preguntas que requieren conectar entidades dispersas en muchos documentos, donde el RAG clásico falla.  
**Instalación:** `pip install graphrag` y luego `graphrag index` / `graphrag query` sobre tu corpus. Requiere claves de un LLM y embeddings; el indexado consume bastantes llamadas.  
**Elige si:** tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto — **Evita si:** un RAG simple basta o el coste de indexado con LLM es prohibitivo  
**Combina con:** [graphify](human/fichas/graphify.md) · [mcp-neo4j](human/fichas/mcp-neo4j.md) · [turbovec](human/fichas/turbovec.md)  
**Más:** [ficha completa](human/fichas/graphrag.md) · [GitHub](https://github.com/microsoft/graphrag)

### Bases vectoriales y búsqueda semántica

#### 🧮 Qdrant ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 35.5k  
**Qué es:** Guarda embeddings con metadatos y los busca con filtros rápidos, a escala. Muy usada como memoria de RAG y agentes.  
**Instalación:** `docker run -p 6333:6333 qdrant/qdrant` y `pip install qdrant-client`.  
**Elige si:** quieres una base vectorial dedicada y rápida — **Evita si:** ya tienes PostgreSQL y poco volumen; mira `pgvector`  
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [langchain](human/fichas/langchain.md) · [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/qdrant.md) · [GitHub](https://github.com/qdrant/qdrant)

#### 🧮 Milvus
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 46.6k  
**Qué es:** Pensada para producción con grandes volúmenes, alta disponibilidad y varios tipos de índices. Tiene una versión ligera para empezar.  
**Instalación:** `pip install pymilvus` (incluye Milvus Lite) o Docker Compose para el modo standalone.  
**Elige si:** esperas volúmenes muy grandes de vectores — **Evita si:** tu proyecto es pequeño; mira `chroma` o `qdrant`  
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)  
**Más:** [ficha completa](human/fichas/milvus.md) · [GitHub](https://github.com/milvus-io/milvus)

#### 🧮 Faiss
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 41.3k  
**Qué es:** Base de muchas bases vectoriales; ideal para investigación o cuando quieres índices en memoria sin servidor.  
**Instalación:** `pip install faiss-cpu` (o `faiss-gpu`).  
**Elige si:** necesitas índices vectoriales en memoria y máximo control — **Evita si:** quieres persistencia y API listas; mira `qdrant`  
**Combina con:** [Transformers](human/fichas/transformers.md)  
**Más:** [ficha completa](human/fichas/faiss.md) · [GitHub](https://github.com/facebookresearch/faiss)

#### 🧮 Chroma
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 29.7k  
**Qué es:** Se usa embebida en tu script Python o como servidor, con embeddings automáticos. Perfecta para prototipos de RAG.  
**Instalación:** `pip install chromadb`.  
**Elige si:** empiezas con RAG y quieres lo más simple — **Evita si:** necesitas gran escala y filtros complejos; mira `qdrant` o `milvus`  
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [langchain](human/fichas/langchain.md)  
**Más:** [ficha completa](human/fichas/chroma.md) · [GitHub](https://github.com/chroma-core/chroma)

#### 🧮 pgvector
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.6k  
**Qué es:** Guarda embeddings en una columna y búscalos con SQL, con índices HNSW o IVFFlat. Evita añadir otra base de datos.  
**Instalación:** `CREATE EXTENSION vector;` (incluida en muchos servicios; o `docker run pgvector/pgvector:pg17`).  
**Elige si:** ya usas PostgreSQL y quieres vectores — **Evita si:** tienes volúmenes muy grandes; mira `milvus`  
**Combina con:** [n8n](human/fichas/n8n.md) · [LlamaIndex](human/fichas/llama-index.md)  
**Más:** [ficha completa](human/fichas/pgvector.md) · [GitHub](https://github.com/pgvector/pgvector)

#### ⚡ turbovec
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 17.5k  
**Qué es:** Resuelve el coste de memoria y cómputo de la búsqueda vectorial cuando una vector DB completa es demasiado para tu escala.  
**Instalación:** `pip install` (Python) o crate de Rust según el repo; sin servicios externos ni GPU obligatoria para inferencia.  
**Elige si:** necesitas vector search veloz y embebido sin desplegar una DB — **Evita si:** ya usas una vector DB completa con persistencia y escalado horizontal  
**Combina con:** [mem0](human/fichas/mem0.md) · [graphrag](human/fichas/graphrag.md)  
**Más:** [ficha completa](human/fichas/turbovec.md) · [GitHub](https://github.com/RyanCodrai/turbovec)

### Serving y gateways de LLM

#### 🚀 vLLM ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 96.7k  
**Qué es:** Sirve modelos abiertos a muchos usuarios con una API compatible con OpenAI, gracias a PagedAttention y batching continuo.  
**Instalación:** `pip install vllm` y `vllm serve Qwen/Qwen3-8B` (requiere GPU NVIDIA o AMD).  
**Elige si:** necesitas servir LLM abiertos a muchos usuarios en GPU — **Evita si:** solo los usas tú en un portátil; mira `ollama`  
**Combina con:** [litellm](human/fichas/litellm.md) · [Open WebUI](human/fichas/open-webui.md)  
**Más:** [ficha completa](human/fichas/vllm.md) · [GitHub](https://github.com/vllm-project/vllm)

#### 🔀 litellm
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 63k  
**Qué es:** Resuelve el lock-in: cambias de proveedor o añades fallback sin reescribir el código de tu app.  
**Instalación:** `pip install litellm` (o despliegue del proxy vía Docker); requiere las claves de los proveedores que uses vía variables de entorno.  
**Elige si:** trabajas con múltiples modelos o quieres fallback/control de costos — **Evita si:** usas un único proveedor fijo y no necesitas abstracción  
**Combina con:** [langchain](human/fichas/langchain.md) · [langfuse](human/fichas/langfuse.md) · [llm-council](human/fichas/llm-council.md)  
**Más:** [ficha completa](human/fichas/litellm.md) · [GitHub](https://github.com/BerriAI/litellm)

#### 🚀 SGLang
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 38.7k  
**Qué es:** Compite con vLLM en velocidad, con caché de prefijos RadixAttention y buen soporte de salidas estructuradas. Muy usado para modelos grandes como DeepSeek.  
**Instalación:** `pip install "sglang[all]"` y `python -m sglang.launch_server --model-path Qwen/Qwen3-8B`.  
**Elige si:** buscas el máximo rendimiento en servicio de LLM — **Evita si:** quieres la opción más documentada; mira `vllm`  
**Combina con:** [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/sglang.md) · [GitHub](https://github.com/sgl-project/sglang)

### Ahorro de contexto y tokens

#### 🗜️ headroom ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 79.3k  
**Qué es:** Resuelve el dolor habitual de los agentes: quedarse sin ventana de contexto a mitad de una tarea larga.  
**Instalación:** Instalación según el repo (`pip`/`npm`); requiere un LLM para la condensación (o modo local si lo soporta).  
**Elige si:** te quedas sin contexto en sesiones largas — **Evita si:** tus prompts ya caben holgados o la pérdida de detalle por resumen es inaceptable  
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md) · [codegraph](human/fichas/codegraph.md)  
**Más:** [ficha completa](human/fichas/headroom.md) · [GitHub](https://github.com/headroomlabs-ai/headroom)

### Observabilidad, evaluación y guardrails

#### 📡 promptfoo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 27k  
**Qué es:** Defines casos de prueba en YAML y comparas salidas de varios modelos con aserciones. También escanea vulnerabilidades como inyección de prompts.  
**Instalación:** `npx promptfoo@latest init`.  
**Elige si:** quieres pruebas automáticas de prompts y seguridad — **Evita si:** necesitas observabilidad en producción; mira `langfuse`  
**Combina con:** [langfuse](human/fichas/langfuse.md) · [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/promptfoo.md) · [GitHub](https://github.com/promptfoo/promptfoo)

#### 📡 langfuse
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 37.3k  
**Qué es:** Resuelve la opacidad: ves qué prompt, qué modelo, qué coste y qué salida tuvo cada paso de tu pipeline.  
**Instalación:** Docker Compose para self-host (Postgres + backend + frontend) o cuenta cloud; SDKs vía `pip`/`npm`. El self-host requiere mantener PostgreSQL.  
**Elige si:** operas agentes en serio y necesitas trazas/costes/eval — **Evita si:** haces prototipos triviales o no quieres operar el backend  
**Combina con:** [langchain](human/fichas/langchain.md) · [litellm](human/fichas/litellm.md) · [ag2](human/fichas/ag2.md)  
**Más:** [ficha completa](human/fichas/langfuse.md) · [GitHub](https://github.com/langfuse/langfuse)

#### 📡 MLflow
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 28.7k  
**Qué es:** Registra experimentos, versiona modelos y, para LLM, ofrece trazas, evaluación y gestión de prompts.  
**Instalación:** `pip install mlflow` y `mlflow ui`.  
**Elige si:** tu equipo hace ML clásico y LLM y quiere una sola plataforma — **Evita si:** solo trazas LLM y quieres algo más ligero; mira `langfuse`  
**Combina con:** [Transformers](human/fichas/transformers.md) · [DSPy](human/fichas/dspy.md)  
**Más:** [ficha completa](human/fichas/mlflow.md) · [GitHub](https://github.com/mlflow/mlflow)

#### 📝 loguru
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 24.2k  
**Qué es:** Resuelve la fricción del módulo `logging` stdlib, que exige boilerplate para algo tan básico como imprimir logs legibles.  
**Instalación:** `pip install loguru`; sin configuración previa, `from loguru import logger` y a usar.  
**Elige si:** quieres logging fácil y legible en Python sin pelear con stdlib — **Evita si:** ya usas el stdlib `logging` configurado o tienes un stack de observabilidad corporativo  
**Combina con:** [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/loguru.md) · [GitHub](https://github.com/Delgan/loguru)

#### 📡 Opik
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 23.3k  
**Qué es:** Traza llamadas, ejecuta evaluaciones automáticas y monitorea producción con paneles. Incluye optimizador de prompts.  
**Instalación:** Clona el repo y ejecuta `./opik.sh` (Docker), o usa su cloud; `pip install opik`.  
**Elige si:** quieres observabilidad y evaluación en un solo producto abierto — **Evita si:** prefieres la opción más extendida; mira `langfuse`  
**Combina con:** [LangGraph](human/fichas/langgraph.md)  
**Más:** [ficha completa](human/fichas/opik.md) · [GitHub](https://github.com/comet-ml/opik)

#### 📡 DeepEval
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 19.4k  
**Qué es:** Escribe pruebas para tus apps de LLM con métricas como fidelidad, relevancia o alucinación, e intégralas en tu CI.  
**Instalación:** `pip install -U deepeval`.  
**Elige si:** quieres tests de LLM en Python como pytest — **Evita si:** prefieres configurar en YAML y comparar modelos; mira `promptfoo`  
**Combina con:** [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/deepeval.md) · [GitHub](https://github.com/confident-ai/deepeval)

#### 📡 Ragas
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 16.3k  
**Qué es:** Mide fidelidad, relevancia del contexto y calidad de respuestas, y genera conjuntos de prueba a partir de tus documentos.  
**Instalación:** `pip install ragas`.  
**Elige si:** evalúas un sistema RAG — **Evita si:** necesitas red teaming de seguridad; mira `promptfoo`  
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/ragas.md) · [GitHub](https://github.com/vibrantlabsai/ragas)

#### 📡 Phoenix
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 12.2k  
**Qué es:** Visualiza trazas de agentes y RAG, ejecuta evaluaciones y gestiona datasets y experimentos. Corre en local o en tu servidor.  
**Instalación:** `pip install arize-phoenix` y `phoenix serve`, o `docker run -p 6006:6006 arizephoenix/phoenix`.  
**Elige si:** quieres observabilidad basada en OpenTelemetry — **Evita si:** buscas la plataforma más usada; mira `langfuse`  
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [LangGraph](human/fichas/langgraph.md)  
**Más:** [ficha completa](human/fichas/phoenix.md) · [GitHub](https://github.com/Arize-ai/phoenix)

#### 📡 NeMo Guardrails
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 7.5k  
**Qué es:** Controla de qué puede hablar tu bot, bloquea jailbreaks y valida entradas y salidas con reglas en el lenguaje Colang.  
**Instalación:** `pip install nemoguardrails`.  
**Elige si:** necesitas políticas de seguridad en un chatbot — **Evita si:** solo quieres probar vulnerabilidades; mira `promptfoo`  
**Combina con:** [langchain](human/fichas/langchain.md)  
**Más:** [ficha completa](human/fichas/guardrails.md) · [GitHub](https://github.com/NVIDIA-NeMo/Guardrails)

---

## 🧑‍💻 7. Inteligencia de Código, Datos & Entrenamiento

Entender y empaquetar codebases para agentes, calidad de código, entrenar y afinar modelos, modelos abiertos y herramientas de datos.

**⚖️ ¿Cuál elegir? — Repomix, codegraph, codebase-memory-mcp, GitNexus**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Repomix](human/fichas/repomix.md) | quieres dar tu repo completo a un LLM | el repo es enorme; mira `codebase-memory-mcp` o `serena` |
| [codegraph](human/fichas/codegraph.md) | trabajas repos grandes y el contexto del agente es caro | tu base de código es pequeña y no justifica mantener un índice |
| [codebase-memory-mcp](human/fichas/codebase-memory-mcp.md) | tu agente trabaja en repos grandes | tu repo es pequeño; usa `repomix` |
| [GitNexus](human/fichas/gitnexus.md) | quieres entender un repo puntual de forma visual | necesitas indexar muchos repos a escala (codegraph) o no quieres front web |

**⚖️ ¿Cuál elegir? — Semgrep, ast-grep**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Semgrep](human/fichas/semgrep.md) | quieres análisis de seguridad en CI | solo quieres refactors estructurales; mira `ast-grep` |
| [ast-grep](human/fichas/ast-grep.md) | necesitas buscar o reescribir código por estructura | buscas análisis de seguridad con reglas existentes; mira `semgrep` |

**⚖️ ¿Cuál elegir? — Unsloth, LLaMA-Factory**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Unsloth](human/fichas/unsloth.md) | quieres afinar un LLM con pocos recursos | necesitas muchas técnicas y una UI de entrenamiento; mira `llama-factory` |
| [LLaMA-Factory](human/fichas/llama-factory.md) | quieres muchas técnicas de fine-tuning con UI | buscas la opción más eficiente en memoria; mira `unsloth` |

**⚖️ ¿Cuál elegir? — LLM Course, LLMs from Scratch, nanoGPT**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [LLM Course](human/fichas/llm-course.md) | quieres una ruta completa para aprender LLM | buscas un curso introductorio de apps; mira `generative-ai-for-beginners` |
| [LLMs from Scratch](human/fichas/llms-from-scratch.md) | quieres entender los LLM implementándolos | solo quieres usar modelos existentes |
| [nanoGPT](human/fichas/nanogpt.md) | quieres entender el entrenamiento de un GPT desde cero | solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat) |

**⚖️ ¿Cuál elegir? — DuckDB, Polars**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [DuckDB](human/fichas/duckdb.md) | quieres SQL analítico rápido sin montar servidores | necesitas una base transaccional multiusuario; usa PostgreSQL |
| [Polars](human/fichas/polars.md) | tu análisis con pandas es lento | prefieres SQL; mira `duckdb` |

### Entender y empaquetar código para agentes

#### 🧬 Repomix ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 29.2k  
**Qué es:** Genera un archivo XML, Markdown o texto con la estructura y el código del repo, respetando .gitignore y contando tokens. También funciona como servidor MCP.  
**Instalación:** `npx repomix` en la carpeta del repo (o `npm i -g repomix`).  
**Elige si:** quieres dar tu repo completo a un LLM — **Evita si:** el repo es enorme; mira `codebase-memory-mcp` o `serena`  
**Combina con:** [Claude Code](human/fichas/claude-code.md)  
**Más:** [ficha completa](human/fichas/repomix.md) · [GitHub](https://github.com/yamadashy/repomix)

#### 🕸️ graphify
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 145k  
**Qué es:** Resuelve el onboarding visual: un índice textual no basta cuando hay relaciones entre archivos.  
**Instalación:** `pipx install graphify` o `uv tool install graphify`, luego `/graphify .` sobre el proyecto. Requiere Python 3.10+; el enriquecimiento con LLM necesita claves de API.  
**Elige si:** quieres ver conexiones visualmente o auditar un sistema — **Evita si:** solo necesitas índice textual barato (codegraph) o tu proyecto es trivial  
**Combina con:** [codegraph](human/fichas/codegraph.md) · [graphrag](human/fichas/graphrag.md)  
**Más:** [ficha completa](human/fichas/graphify.md) · [GitHub](https://github.com/Graphify-Labs/graphify)

#### 📊 codegraph
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 77.3k  
**Qué es:** Resuelve el coste de contexto de los agentes en repos grandes.  
**Instalación:** `npm install -g codegraph` (binario autónomo de Node.js) y luego `codegraph index .`. Requiere Node.js; el índice se regenera al cambiar el código.  
**Elige si:** trabajas repos grandes y el contexto del agente es caro — **Evita si:** tu base de código es pequeña y no justifica mantener un índice  
**Combina con:** [graphify](human/fichas/graphify.md) · [headroom](human/fichas/headroom.md)  
**Más:** [ficha completa](human/fichas/codegraph.md) · [GitHub](https://github.com/colbymchenry/codegraph)

#### 🧬 codebase-memory-mcp
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 48.4k  
**Qué es:** Indexa repos en milisegundos y da al agente herramientas MCP para entender arquitectura, dependencias y cambios sin leer archivo por archivo.  
**Instalación:** Descarga el binario de releases y añádelo como servidor MCP a tu agente.  
**Elige si:** tu agente trabaja en repos grandes — **Evita si:** tu repo es pequeño; usa `repomix`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Serena](human/fichas/serena.md)  
**Más:** [ficha completa](human/fichas/codebase-memory-mcp.md) · [GitHub](https://github.com/DeusData/codebase-memory-mcp)

#### 🧭 GitNexus
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 48.4k  
**Qué es:** Resuelve el "llegar a un proyecto ajeno y no saber por dónde empezar": lo navegas y lo discutes en vez de leer ficheros sueltos.  
**Instalación:** `git clone https://github.com/abhigyanpatwari/GitNexus` y arranque del front web según el README; requiere Node.js y una clave de LLM para las preguntas.  
**Elige si:** quieres entender un repo puntual de forma visual — **Evita si:** necesitas indexar muchos repos a escala (codegraph) o no quieres front web  
**Combina con:** [codegraph](human/fichas/codegraph.md)  
**Más:** [ficha completa](human/fichas/gitnexus.md) · [GitHub](https://github.com/abhigyanpatwari/GitNexus)

#### 🧬 tree-sitter
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 27.4k  
**Qué es:** Genera parsers rápidos que actualizan el árbol sintáctico mientras editas. Lo usan editores, Aider, ast-grep y muchas herramientas de código con IA.  
**Instalación:** `npm i -g tree-sitter-cli` o los bindings de tu lenguaje (`pip install tree-sitter`).  
**Elige si:** construyes herramientas que entienden código — **Evita si:** solo necesitas buscar patrones; mira `ast-grep`  
**Combina con:** [ast-grep](human/fichas/ast-grep.md) · [Aider](human/fichas/aider.md)  
**Más:** [ficha completa](human/fichas/tree-sitter.md) · [GitHub](https://github.com/tree-sitter/tree-sitter)

#### 🧬 DeepWiki Open
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 18.4k  
**Qué es:** Analiza un repositorio y crea documentación navegable con diagramas y un chat para preguntar sobre el código.  
**Instalación:** `docker compose up` con tus claves de API en `.env`.  
**Elige si:** quieres documentación automática de un repositorio — **Evita si:** necesitas contexto de librerías externas; mira `context7`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/deepwiki-open.md) · [GitHub](https://github.com/AsyncFuncAI/deepwiki-open)

### Calidad, seguridad y benchmarks de código

#### 🛡️ Semgrep ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 17.6k  
**Qué es:** Encuentra bugs y vulnerabilidades con miles de reglas comunitarias o propias. Muy usado en CI de seguridad.  
**Instalación:** `pip install semgrep` o `brew install semgrep`; luego `semgrep scan`.  
**Elige si:** quieres análisis de seguridad en CI — **Evita si:** solo quieres refactors estructurales; mira `ast-grep`  
**Combina con:** [Defending Code Reference Harness](human/fichas/defending-code-reference-harness.md)  
**Más:** [ficha completa](human/fichas/semgrep.md) · [GitHub](https://github.com/semgrep/semgrep)

#### 🛡️ ast-grep
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 16.5k  
**Qué es:** Busca y reemplaza código por su estructura (AST), no por texto. Útil para refactors masivos y reglas de lint propias.  
**Instalación:** `npm i -g @ast-grep/cli` o `brew install ast-grep`.  
**Elige si:** necesitas buscar o reescribir código por estructura — **Evita si:** buscas análisis de seguridad con reglas existentes; mira `semgrep`  
**Combina con:** [tree-sitter](human/fichas/tree-sitter.md) · [Claude Code](human/fichas/claude-code.md)  
**Más:** [ficha completa](human/fichas/ast-grep.md) · [GitHub](https://github.com/ast-grep/ast-grep)

#### 🛡️ Defending Code Reference Harness
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 7.7k  
**Qué es:** Implementación de referencia para descubrir y corregir vulnerabilidades de forma autónoma con Claude, basada en experiencia con equipos de seguridad.  
**Instalación:** Clona el repo y usa las skills en Claude Code siguiendo el README.  
**Elige si:** quieres un flujo de seguridad con agentes probado — **Evita si:** solo necesitas un escáner estático; mira `semgrep`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Semgrep](human/fichas/semgrep.md)  
**Más:** [ficha completa](human/fichas/defending-code-reference-harness.md) · [GitHub](https://github.com/anthropics/defending-code-reference-harness)

#### 🛡️ SWE-bench
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 6.2k  
**Qué es:** Da al modelo un repositorio y un issue y comprueba si su parche pasa las pruebas. Es la referencia para medir agentes de código.  
**Instalación:** `pip install swebench` (requiere Docker y mucho espacio en disco).  
**Elige si:** necesitas medir agentes de código con un estándar — **Evita si:** solo quieres usar un agente  
**Combina con:** [SWE-agent](human/fichas/swe-agent.md)  
**Más:** [ficha completa](human/fichas/swe-bench.md) · [GitHub](https://github.com/SWE-bench/SWE-bench)

### Entrenar y afinar modelos

#### 🏋️ Unsloth ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 79.3k  
**Qué es:** Afina modelos como Qwen, Llama o Gemma en una sola GPU y expórtalos a GGUF u Ollama. Ofrece notebooks gratuitos y una interfaz local.  
**Instalación:** `pip install unsloth` o usa sus notebooks de Colab.  
**Elige si:** quieres afinar un LLM con pocos recursos — **Evita si:** necesitas muchas técnicas y una UI de entrenamiento; mira `llama-factory`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [TRL](human/fichas/trl.md)  
**Más:** [ficha completa](human/fichas/unsloth.md) · [GitHub](https://github.com/unslothai/unsloth)

#### 🏋️ Transformers
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 169k  
**Qué es:** Da acceso a cientos de miles de modelos con una API común para inferencia y entrenamiento. Es la base del ecosistema de modelos abiertos.  
**Instalación:** `pip install transformers`.  
**Elige si:** trabajas con modelos abiertos en Python — **Evita si:** solo quieres chatear con un modelo local; mira `ollama`  
**Combina con:** [PEFT](human/fichas/peft.md) · [TRL](human/fichas/trl.md) · [PyTorch](human/fichas/pytorch.md)  
**Más:** [ficha completa](human/fichas/transformers.md) · [GitHub](https://github.com/huggingface/transformers)

#### 🏋️ PyTorch
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 105k  
**Qué es:** Base de la mayoría de investigación y modelos abiertos actuales.  
**Instalación:** `pip install torch` (elige la variante de tu GPU en pytorch.org).  
**Elige si:** entrenas o investigas modelos — **Evita si:** solo consumes APIs de LLM  
**Combina con:** [Transformers](human/fichas/transformers.md)  
**Más:** [ficha completa](human/fichas/pytorch.md) · [GitHub](https://github.com/pytorch/pytorch)

#### 🏋️ LLaMA-Factory
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 76k  
**Qué es:** Soporta LoRA, QLoRA, ajuste completo, DPO y más desde una UI o CLI. Muy usado en investigación e industria.  
**Instalación:** `git clone https://github.com/hiyouga/LlamaFactory && pip install -e ".[torch,metrics]"` y `llamafactory-cli webui`.  
**Elige si:** quieres muchas técnicas de fine-tuning con UI — **Evita si:** buscas la opción más eficiente en memoria; mira `unsloth`  
**Combina con:** [PEFT](human/fichas/peft.md) · [Transformers](human/fichas/transformers.md)  
**Más:** [ficha completa](human/fichas/llama-factory.md) · [GitHub](https://github.com/hiyouga/LlamaFactory)

#### 🏋️ PEFT
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 21.9k  
**Qué es:** Adapta modelos grandes entrenando solo una pequeña parte de los parámetros, ahorrando memoria y tiempo.  
**Instalación:** `pip install peft`.  
**Elige si:** afinas modelos con código propio — **Evita si:** prefieres una herramienta lista; mira `unsloth`  
**Combina con:** [Transformers](human/fichas/transformers.md) · [TRL](human/fichas/trl.md)  
**Más:** [ficha completa](human/fichas/peft.md) · [GitHub](https://github.com/huggingface/peft)

#### 🏋️ TRL
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 19.7k  
**Qué es:** Ofrece entrenadores listos para ajuste supervisado y por preferencias, usados para alinear modelos.  
**Instalación:** `pip install trl`.  
**Elige si:** necesitas SFT o RL sobre modelos abiertos — **Evita si:** quieres algo sin código; mira `llama-factory`  
**Combina con:** [Transformers](human/fichas/transformers.md) · [PEFT](human/fichas/peft.md) · [Unsloth](human/fichas/unsloth.md)  
**Más:** [ficha completa](human/fichas/trl.md) · [GitHub](https://github.com/huggingface/trl)

### Aprender LLMs desde cero

#### 📘 LLM Course ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 85k  
**Qué es:** Tres rutas: fundamentos, científico de LLM (entrenar y afinar) e ingeniero de LLM (apps y despliegue), con recursos y notebooks ejecutables.  
**Instalación:** No se instala: abre el repo y sigue la ruta que te interese.  
**Elige si:** quieres una ruta completa para aprender LLM — **Evita si:** buscas un curso introductorio de apps; mira `generative-ai-for-beginners`  
**Combina con:** [Unsloth](human/fichas/unsloth.md) · [LLaMA-Factory](human/fichas/llama-factory.md)  
**Más:** [ficha completa](human/fichas/llm-course.md) · [GitHub](https://github.com/mlabonne/llm-course)

#### 📘 LLMs from Scratch
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 108k  
**Qué es:** Construyes atención, GPT, preentrenamiento y fine-tuning desde cero, entendiendo cada pieza. Ideal para aprender cómo funcionan por dentro.  
**Instalación:** `git clone https://github.com/rasbt/LLMs-from-scratch` y `pip install -r requirements.txt`.  
**Elige si:** quieres entender los LLM implementándolos — **Evita si:** solo quieres usar modelos existentes  
**Combina con:** [PyTorch](human/fichas/pytorch.md)  
**Más:** [ficha completa](human/fichas/llms-from-scratch.md) · [GitHub](https://github.com/rasbt/LLMs-from-scratch)

#### 🔬 nanoGPT
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 64.6k  
**Qué es:** Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción.  
**Instalación:** `git clone https://github.com/karpathy/nanoGPT` y `pip install torch numpy transformers datasets tiktoken`. Requiere GPU para entrenar (CPU solo sirve para pruebas triviales).  
**Elige si:** quieres entender el entrenamiento de un GPT desde cero — **Evita si:** solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat)  
**Combina con:** [nanochat](human/fichas/nanochat.md)  
**Más:** [ficha completa](human/fichas/nanogpt.md) · [GitHub](https://github.com/karpathy/nanoGPT)

#### 💬 nanochat
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 60.4k  
**Qué es:** Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.  
**Instalación:** `git clone https://github.com/karpathy/nanochat` y seguir el script de entrenamiento del README (entorno PyTorch con GPU). Requiere GPU seria para entrenar y datos de preentrenamiento.  
**Elige si:** quieres el pipeline completo de un chat end-to-end — **Evita si:** solo necesitas el core del modelo (nanoGPT) o un modelo listo para usar  
**Combina con:** [nanoGPT](human/fichas/nanogpt.md)  
**Más:** [ficha completa](human/fichas/nanochat.md) · [GitHub](https://github.com/karpathy/nanochat)

#### ⚙️ llm.c
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 31.4k  
**Qué es:** Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framework.  
**Instalación:** `git clone https://github.com/karpathy/llm.c`, instalar CUDA toolkit y compilar con `make`. Requiere una GPU NVIDIA con CUDA; sin él no tiene sentido.  
**Elige si:** quieres bajo nivel sin abstracciones y tienes GPU CUDA — **Evita si:** prefieres PyTorch (nanoGPT) o no tienes CUDA  
**Combina con:** [nanoGPT](human/fichas/nanogpt.md)  
**Más:** [ficha completa](human/fichas/llm-c.md) · [GitHub](https://github.com/karpathy/llm.c)

#### 📘 how-to-train-your-gpt
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 4.2k  
**Qué es:** Resuelve el "quiero entenderlo con explicación narrada" frente al código desnudo de nanoGPT.  
**Instalación:** `git clone https://github.com/raiyanyahya/how-to-train-your-gpt` y seguir las instrucciones del repositorio; requiere Python y PyTorch (GPU recomendada para entrenar).  
**Elige si:** quieres una guía explicada y narrada — **Evita si:** prefieres solo el código limpio (nanoGPT) o buscas algo productivo  
**Combina con:** [nanoGPT](human/fichas/nanogpt.md) · [nanochat](human/fichas/nanochat.md)  
**Más:** [ficha completa](human/fichas/how-to-train-your-gpt.md) · [GitHub](https://github.com/raiyanyahya/how-to-train-your-gpt)

### Modelos abiertos y fundacionales

#### 🧠 TimesFM ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 35.4k  
**Qué es:** Predice ventas, demanda o tráfico a partir del histórico sin entrenar un modelo propio (zero-shot).  
**Instalación:** `pip install timesfm`.  
**Elige si:** necesitas pronósticos rápidos sin entrenar modelos — **Evita si:** necesitas explicabilidad estadística clásica  
**Combina con:** [Polars](human/fichas/polars.md) · [DuckDB](human/fichas/duckdb.md)  
**Más:** [ficha completa](human/fichas/timesfm.md) · [GitHub](https://github.com/google-research/timesfm)

#### 🧩 DeepSeek-Coder
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 24.4k  
**Qué es:** Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia infraestructura.  
**Instalación:** `pip install transformers torch` y descarga de pesos desde Hugging Face, o uso vía API de DeepSeek. El despliegue local requiere GPU con VRAM generosa según el tamaño del modelo.  
**Elige si:** quieres un modelo de código abierto y desplegable on-prem — **Evita si:** prefieres APIs comerciales gestionadas o no tienes GPU para servirlo  
**Combina con:** [litellm](human/fichas/litellm.md) · [codegraph](human/fichas/codegraph.md)  
**Más:** [ficha completa](human/fichas/deepseek-coder.md) · [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder)

#### 🌌 cosmos
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 12.3k  
**Qué es:** Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.  
**Instalación:** `git clone https://github.com/NVIDIA/Cosmos`, instalar dependencias del repo y descargar pesos Cosmos desde Hugging Face. Requiere GPU potente (NVIDIA, CUDA) para inferencia y generación.  
**Elige si:** trabajas IA física/robótica y necesitas datos sintéticos — **Evita si:** haces tareas de texto/UI o no tienes GPU para servirlo  
**Combina con:** [diffusers](human/fichas/diffusers.md)  
**Más:** [ficha completa](human/fichas/cosmos.md) · [GitHub](https://github.com/NVIDIA/cosmos)

#### 🧠 Nemotron (NVIDIA)
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 2.3k  
**Qué es:** Reúne guías de entrenamiento, despliegue y casos de uso de los modelos Nemotron, pensados para IA agéntica eficiente.  
**Instalación:** No se instala: sigue las guías del repo para el modelo que necesites.  
**Elige si:** usas GPUs NVIDIA y quieres modelos abiertos optimizados — **Evita si:** buscas la forma más simple de correr modelos; mira `ollama`  
**Combina con:** [vLLM](human/fichas/vllm.md) · [NemoClaw](human/fichas/nemoclaw.md)  
**Más:** [ficha completa](human/fichas/nemotron.md) · [GitHub](https://github.com/NVIDIA-NeMo/Nemotron)

### CLIs y SDKs de desarrollo

#### 🧰 GitHub CLI ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 46.9k  
**Qué es:** No es un agente: es la herramienta que los agentes de código usan para abrir PRs, revisar issues o lanzar workflows.  
**Instalación:** `brew install gh` (o el instalador de tu sistema) y `gh auth login`.  
**Elige si:** trabajas con GitHub desde la terminal o con agentes — **Evita si:** usas GitLab u otra forja  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [GitHub MCP Server](human/fichas/github-mcp-server.md)  
**Más:** [ficha completa](human/fichas/cli.md) · [GitHub](https://github.com/cli/cli)

#### 🐍 openai-python
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 32.1k  
**Qué es:** Resuelve el glue HTTP: no escribes peticiones a mano, usas clientes tipados con streaming.  
**Instalación:** `pip install openai` y configurar `OPENAI_API_KEY` (variable de entorno). Requiere una cuenta OpenAI con clave válida y saldo.  
**Elige si:** usas modelos de OpenAI desde Python y quieres el cliente oficial — **Evita si:** quieres abstracción multi-proveedor (litellm) o no usas OpenAI  
**Combina con:** [litellm](human/fichas/litellm.md) · [langchain](human/fichas/langchain.md)  
**Más:** [ficha completa](human/fichas/openai-python.md) · [GitHub](https://github.com/openai/openai-python)

### Datos y notebooks

#### 🗃️ DuckDB ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 43k  
**Qué es:** El "SQLite de la analítica": sin servidor, embebida en Python, R o Node, y capaz de procesar millones de filas en segundos.  
**Instalación:** `pip install duckdb` o `brew install duckdb`.  
**Elige si:** quieres SQL analítico rápido sin montar servidores — **Evita si:** necesitas una base transaccional multiusuario; usa PostgreSQL  
**Combina con:** [marimo](human/fichas/marimo.md) · [Apache Superset](human/fichas/superset.md)  
**Más:** [ficha completa](human/fichas/duckdb.md) · [GitHub](https://github.com/duckdb/duckdb)

#### 🗃️ marimo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 23.5k  
**Qué es:** Al cambiar una celda se recalculan las dependientes, evitando estados ocultos. Incluye SQL, gráficos interactivos y asistente de IA.  
**Instalación:** `pip install marimo` y `marimo edit`.  
**Elige si:** quieres notebooks reproducibles y versionables — **Evita si:** dependes de extensiones de Jupyter  
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [Polars](human/fichas/polars.md)  
**Más:** [ficha completa](human/fichas/marimo.md) · [GitHub](https://github.com/marimo-team/marimo)

#### 🗃️ Polars
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.3k  
**Qué es:** API expresiva con ejecución perezosa y paralela para procesar datos grandes en un solo equipo.  
**Instalación:** `pip install polars`.  
**Elige si:** tu análisis con pandas es lento — **Evita si:** prefieres SQL; mira `duckdb`  
**Combina con:** [marimo](human/fichas/marimo.md)  
**Más:** [ficha completa](human/fichas/polars.md) · [GitHub](https://github.com/pola-rs/polars)

#### 📓 data-science-ipython-notebooks
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 29.4k  
**Qué es:** Resuelve el "aprender DS con ejemplos reales" sin tener que montarlos tú desde cero.  
**Instalación:** `git clone https://github.com/donnemartin/data-science-ipython-notebooks` y abrir los notebooks con `jupyter lab` (o `jupyter notebook`). Requiere Python y las librerías de cada notebook.  
**Elige si:** estudias/consultas DS con ejemplos ejecutables — **Evita si:** buscas una librería, no ejemplos, o necesitas material actualizado a las versiones más recientes  
**Combina con:** [dash](human/fichas/dash.md) · [streamlit](human/fichas/streamlit.md)  
**Más:** [ficha completa](human/fichas/data-science-ipython-notebooks.md) · [GitHub](https://github.com/donnemartin/data-science-ipython-notebooks)

#### 🗄️ awesome-bigdata
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 14.7k  
**Qué es:** Resuelve el "qué uso para X a escala": un panorama del stack de datos grandes en un solo vistazo.  
**Instalación:** No requiere instalación; se navega online en el repositorio de GitHub y se elige la herramienta según tu caso.  
**Elige si:** diseñas pipelines de datos grandes y necesitas descubrir el ecosistema — **Evita si:** tu proyecto es pequeño y no justifica herramientas de big data  
**Combina con:** [awesome-dataviz](human/fichas/awesome-dataviz.md)  
**Más:** [ficha completa](human/fichas/awesome-bigdata.md) · [GitHub](https://github.com/oxnr/awesome-bigdata)

---

## 🏠 8. IA Local: Modelos, Chats & Workspaces

Correr LLMs en tu máquina, interfaces tipo ChatGPT auto-hospedadas, workspaces privados y alternativas a NotebookLM.

**⚖️ ¿Cuál elegir? — Ollama, llama.cpp, LocalAI, llamafile**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Ollama](human/fichas/ollama.md) | quieres modelos locales funcionando en minutos | necesitas servir a muchos usuarios con GPU; mira `vllm` |
| [llama.cpp](human/fichas/llama-cpp.md) | quieres el máximo control y rendimiento local | prefieres simplicidad; mira `ollama` |
| [LocalAI](human/fichas/localai.md) | quieres una API tipo OpenAI local para varias modalidades | solo necesitas chat local simple; mira `ollama` |
| [llamafile](human/fichas/llamafile.md) | quieres repartir un modelo que funcione con doble clic | vas a cambiar de modelos a menudo; mira `ollama` |

**⚖️ ¿Cuál elegir? — Open WebUI, AnythingLLM, Jan, SurfSense, LobeHub, PrivateGPT, Cherry Studio**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Open WebUI](human/fichas/open-webui.md) | necesitas un ChatGPT privado para tu equipo | solo quieres una app de escritorio individual; mira `jan` |
| [AnythingLLM](human/fichas/anything-llm.md) | quieres RAG privado sin programar | necesitas un pipeline de RAG a medida; mira `llama-index` |
| [Jan](human/fichas/jan.md) | quieres un ChatGPT local en tu escritorio | necesitas multiusuario; mira `open-webui` |
| [SurfSense](human/fichas/surfsense.md) | quieres un NotebookLM propio y con más fuentes | solo quieres el NotebookLM de Google por código; mira `notebooklm-py` |
| [LobeHub](human/fichas/lobehub.md) | quieres un chat bonito y extensible con agentes | necesitas el máximo control empresarial; mira `librechat` |
| [PrivateGPT](human/fichas/private-gpt.md) | construyes un producto de IA que no puede enviar datos fuera | quieres una app lista para usuarios finales; mira `anything-llm` |
| [Cherry Studio](human/fichas/cherry-studio.md) | quieres una app de escritorio multi-proveedor completa | solo quieres modelos locales simples; mira `jan` |

### Motores para correr modelos en local

#### 🦙 Ollama ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 187k  
**Qué es:** Un comando para bajar y ejecutar modelos como Qwen, Gemma, DeepSeek o gpt-oss. Casi todas las apps de IA local lo soportan.  
**Instalación:** `curl -fsSL https://ollama.com/install.sh | sh` (o el instalador de macOS/Windows) y `ollama run qwen3`.  
**Elige si:** quieres modelos locales funcionando en minutos — **Evita si:** necesitas servir a muchos usuarios con GPU; mira `vllm`  
**Combina con:** [Open WebUI](human/fichas/open-webui.md) · [n8n](human/fichas/n8n.md) · [AnythingLLM](human/fichas/anything-llm.md)  
**Más:** [ficha completa](human/fichas/ollama.md) · [GitHub](https://github.com/ollama/ollama)

#### 🦙 llama.cpp
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 134k  
**Qué es:** Base de Ollama, LM Studio y muchas apps. Incluye un servidor compatible con OpenAI y herramientas para cuantizar modelos GGUF.  
**Instalación:** `brew install llama.cpp` o binarios de releases; luego `llama-server -hf ggml-org/gemma-3-1b-it-GGUF`.  
**Elige si:** quieres el máximo control y rendimiento local — **Evita si:** prefieres simplicidad; mira `ollama`  
**Combina con:** [Open WebUI](human/fichas/open-webui.md)  
**Más:** [ficha completa](human/fichas/llama-cpp.md) · [GitHub](https://github.com/ggml-org/llama.cpp)

#### 🦙 LocalAI
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 50.3k  
**Qué es:** Sustituye la API de OpenAI por una propia que corre modelos abiertos de muchos tipos. Útil para apps que ya hablan con OpenAI.  
**Instalación:** `docker run -p 8080:8080 --name local-ai -ti localai/localai:latest`.  
**Elige si:** quieres una API tipo OpenAI local para varias modalidades — **Evita si:** solo necesitas chat local simple; mira `ollama`  
**Combina con:** [AnythingLLM](human/fichas/anything-llm.md)  
**Más:** [ficha completa](human/fichas/localai.md) · [GitHub](https://github.com/mudler/LocalAI)

#### 🦙 exo
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 48.3k  
**Qué es:** Une Macs, PCs o teléfonos en un clúster que comparte la carga de un modelo que no cabría en uno solo.  
**Instalación:** Sigue el README (instalación con `uv` o la app de macOS).  
**Elige si:** tienes varios equipos y quieres correr un modelo grande — **Evita si:** un solo equipo te basta; mira `ollama`  
**Combina con:** [Open WebUI](human/fichas/open-webui.md)  
**Más:** [ficha completa](human/fichas/exo.md) · [GitHub](https://github.com/exo-explore/exo)

#### 📏 llmfit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 38.9k  
**Qué es:** Resuelve la elección subjetiva de modelo: la conviertes en un flujo objetivo y reproducible con métricas.  
**Instalación:** Instalación según el repo (binario Go o paquete Python); requiere claves de los modelos a comparar y un dataset de evaluación.  
**Elige si:** necesitas elegir modelo con datos y reproducibilidad — **Evita si:** ya tienes el modelo decidido o tu caso no justifica un harness de evaluación  
**Combina con:** [litellm](human/fichas/litellm.md) · [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/llmfit.md) · [GitHub](https://github.com/AlexsJones/llmfit)

#### 🦙 llamafile
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 26.6k  
**Qué es:** Empaqueta modelo y motor en un ejecutable que funciona en Windows, macOS y Linux sin instalar nada. Proyecto de Mozilla.  
**Instalación:** Descarga un `.llamafile`, dale permiso de ejecución y ábrelo.  
**Elige si:** quieres repartir un modelo que funcione con doble clic — **Evita si:** vas a cambiar de modelos a menudo; mira `ollama`  
**Más:** [ficha completa](human/fichas/llamafile.md) · [GitHub](https://github.com/mozilla-ai/llamafile)

### Interfaces de chat auto-hospedadas

#### 💬 Open WebUI ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 158k  
**Qué es:** Da a tu equipo un chat privado con usuarios, documentos, búsqueda web, herramientas y modelos locales o en la nube.  
**Instalación:** `docker run -d -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main`.  
**Elige si:** necesitas un ChatGPT privado para tu equipo — **Evita si:** solo quieres una app de escritorio individual; mira `jan`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [SearXNG](human/fichas/searxng.md) · [litellm](human/fichas/litellm.md)  
**Más:** [ficha completa](human/fichas/open-webui.md) · [GitHub](https://github.com/open-webui/open-webui)

#### 💬 Jan ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 45.6k  
**Qué es:** Descarga modelos y chatea en local con privacidad total, o conecta APIs en la nube si quieres. Incluye servidor local compatible con OpenAI.  
**Instalación:** Descarga el instalador desde jan.ai o los releases.  
**Elige si:** quieres un ChatGPT local en tu escritorio — **Evita si:** necesitas multiusuario; mira `open-webui`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/jan.md) · [GitHub](https://github.com/janhq/jan)

#### 💬 LobeHub
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 84.7k  
**Qué es:** Antes LobeChat: chat elegante con agentes, plugins, base de conocimiento y despliegue en un clic. Ahora añade agentes que trabajan en tus chats de equipo.  
**Instalación:** `docker run -d -p 3210:3210 lobehub/lobehub` o despliegue en Vercel.  
**Elige si:** quieres un chat bonito y extensible con agentes — **Evita si:** necesitas el máximo control empresarial; mira `librechat`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/lobehub.md) · [GitHub](https://github.com/lobehub/lobehub)

#### 💬 Cherry Studio
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 53.4k  
**Qué es:** Chatea con decenas de proveedores y modelos locales, usa asistentes predefinidos, MCP y base de conocimiento desde una sola app.  
**Instalación:** Descarga el instalador desde los releases.  
**Elige si:** quieres una app de escritorio multi-proveedor completa — **Evita si:** solo quieres modelos locales simples; mira `jan`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/cherry-studio.md) · [GitHub](https://github.com/CherryHQ/cherry-studio)

#### 💬 Text Generation WebUI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 47.7k  
**Qué es:** La clásica "oobabooga": carga modelos en muchos formatos y backends, con chat, modo notebook y entrenamiento LoRA.  
**Instalación:** Descarga el paquete portable de releases o usa el script `start_*` del repo.  
**Elige si:** quieres experimentar con muchos backends locales — **Evita si:** quieres algo sencillo; mira `jan` u `ollama`  
**Más:** [ficha completa](human/fichas/textgen.md) · [GitHub](https://github.com/oobabooga/textgen)

#### 💬 LibreChat
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 46.9k  
**Qué es:** Une OpenAI, Anthropic, Google, Azure, OpenRouter y modelos locales con agentes, artifacts, búsqueda y control de usuarios.  
**Instalación:** `git clone https://github.com/danny-avila/LibreChat && cd LibreChat && docker compose up -d`.  
**Elige si:** quieres todos los proveedores en un chat con SSO — **Evita si:** usas sobre todo modelos locales; mira `open-webui`  
**Combina con:** [litellm](human/fichas/litellm.md) · [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/librechat.md) · [GitHub](https://github.com/LibreChat-AI/LibreChat)

### Workspaces privados y segundos cerebros

#### 🏠 AnythingLLM ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 68.1k  
**Qué es:** Organiza documentos en espacios de trabajo, crea RAG sin configurar nada y añade agentes con herramientas. Escritorio o Docker multiusuario.  
**Instalación:** Descarga la app de escritorio o `docker pull mintplexlabs/anythingllm`.  
**Elige si:** quieres RAG privado sin programar — **Evita si:** necesitas un pipeline de RAG a medida; mira `llama-index`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/anything-llm.md) · [GitHub](https://github.com/Mintplex-Labs/anything-llm)

#### ⛺ odysseus
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 95.5k  
**Qué es:** Sustituye la dispersión entre varios SaaS por un único panel que tú controlas.  
**Instalación:** `docker compose` para levantar backend, base de datos y frontend, o despliegue manual con Python y Node. Requiere PostgreSQL y un endpoint de modelo (Ollama local o API key comercial).  
**Elige si:** quieres operación privada todo-en-uno y aceptas operar la infra — **Evita si:** prefieres SaaS gestionado sin mantenimiento  
**Combina con:** [open-notebook](human/fichas/open-notebook.md) · [ECC](human/fichas/ecc.md) · [mem0](human/fichas/mem0.md)  
**Más:** [ficha completa](human/fichas/odysseus.md) · [GitHub](https://github.com/odysseus-dev/odysseus)

#### 🏠 PrivateGPT
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 57.6k  
**Qué es:** Ofrece una API lista para construir apps de IA sin que los datos salgan de tu entorno. Funciona con cualquier motor compatible con OpenAI.  
**Instalación:** Clona el repo y sigue la guía de instalación con `poetry` o Docker.  
**Elige si:** construyes un producto de IA que no puede enviar datos fuera — **Evita si:** quieres una app lista para usuarios finales; mira `anything-llm`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md)  
**Más:** [ficha completa](human/fichas/private-gpt.md) · [GitHub](https://github.com/zylon-ai/private-gpt)

#### 🏠 Khoj
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 38.1k  
**Qué es:** Busca en tus documentos y en internet, crea agentes personalizados, programa resúmenes y hace investigación profunda. Accesible desde web, Obsidian, Emacs o WhatsApp.  
**Instalación:** `pip install khoj` y `khoj --anonymous-mode`, o Docker Compose.  
**Elige si:** quieres un asistente sobre tus notas personales — **Evita si:** necesitas una plataforma de equipo; mira `anything-llm`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/khoj.md) · [GitHub](https://github.com/khoj-ai/khoj)

#### 🏠 Hermes Desktop
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 14.6k  
**Qué es:** Para quien quiere usar Hermes Agent como aplicación y no solo desde la terminal.  
**Instalación:** Descarga el instalador desde los releases.  
**Elige si:** usas Hermes Agent y prefieres una app de escritorio — **Evita si:** no usas Hermes  
**Combina con:** [hermes-agent](human/fichas/hermes-agent.md)  
**Más:** [ficha completa](human/fichas/hermes-desktop.md) · [GitHub](https://github.com/fathah/hermes-desktop)

### NotebookLM: alternativas y clientes

#### 📓 SurfSense ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 16.8k  
**Qué es:** Conecta tus fuentes (archivos, Slack, Notion, GitHub, web) y conversa con ellas con citas, genera podcasts y reportes. Puede funcionar sin conexión.  
**Instalación:** Self-host con Docker Compose siguiendo la guía del repo.  
**Elige si:** quieres un NotebookLM propio y con más fuentes — **Evita si:** solo quieres el NotebookLM de Google por código; mira `notebooklm-py`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/surfsense.md) · [GitHub](https://github.com/MODSetter/SurfSense)

#### 📓 open-notebook
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 41.8k  
**Qué es:** Resuelve el envío de documentos sensibles a la nube que implica el NotebookLM oficial.  
**Instalación:** `docker` (imagen oficial) o `pip` más Ollama para los modelos locales. Requiere Ollama instalado y al menos un modelo descargado (p. ej. Llama 3) para el modo 100% local.  
**Elige si:** quieres NotebookLM privado y sin cuotas — **Evita si:** prefieres el NotebookLM real automatizado (notebooklm-py)  
**Combina con:** [odysseus](human/fichas/odysseus.md) · [markitdown](human/fichas/markitdown.md)  
**Más:** [ficha completa](human/fichas/open-notebook.md) · [GitHub](https://github.com/lfnovo/open-notebook)

#### 🎙️ notebooklm-py
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 20.2k  
**Qué es:** Cubre el vacío de automatización que la interfaz web oficial no ofrece.  
**Instalación:** `pip install` de la librería más configuración de credenciales de Google (cookies de sesión o auth no oficial).  
**Elige si:** automatizas el NotebookLM real y aceptas el riesgo de API no oficial — **Evita si:** quieres todo local (open-notebook)  
**Combina con:** [notebooklm-mcp-cli](human/fichas/notebooklm-mcp-cli.md)  
**Más:** [ficha completa](human/fichas/notebooklm-py.md) · [GitHub](https://github.com/teng-lin/notebooklm-py)

#### 🎚️ notebooklm-mcp-cli
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 6.5k  
**Qué es:** Convierte NotebookLM en una herramienta invocable por asistentes.  
**Instalación:** `pip install` o `git clone` y registro del servidor MCP en tu cliente (Claude Desktop, etc.). Requiere credenciales de Google válidas.  
**Elige si:** integras NotebookLM con tu asistente MCP — **Evita si:** prefieres la API directa en scripts (notebooklm-py)  
**Combina con:** [notebooklm-py](human/fichas/notebooklm-py.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)  
**Más:** [ficha completa](human/fichas/notebooklm-mcp-cli.md) · [GitHub](https://github.com/jacob-bd/gemini-notebook-mcp-cli)

---

## 🎨 9. Diseño, UI & Frontend

Componentes y sistemas de diseño, CSS, animación y 3D, canvas y builders, UI generada con IA y skills de diseño para agentes.

**⚖️ ¿Cuál elegir? — ui, daisyUI, Ant Design, Material UI, heroui**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [ui](human/fichas/ui.md) | quieres ser dueño del código de UI | prefieres una lib "llave en mano" con updates automáticos (heroui) |
| [daisyUI](human/fichas/daisyui.md) | usas Tailwind y quieres componentes sin JavaScript | usas React y quieres control total; mira `ui` |
| [Ant Design](human/fichas/ant-design.md) | construyes apps empresariales con muchos datos | quieres un estilo más personalizado; mira `ui` |
| [Material UI](human/fichas/mui.md) | quieres una librería React completa y probada | prefieres copiar componentes y estilarlos con Tailwind; mira `ui` |
| [heroui](human/fichas/heroui.md) | quieres calidad + accesibilidad listas | quieres control copy-paste del código (ui) |

**⚖️ ¿Cuál elegir? — React Bits, magicui**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [React Bits](human/fichas/react-bits.md) | quieres efectos visuales llamativos en React | necesitas componentes de formulario y datos; mira `ui` |
| [magicui](human/fichas/magicui.md) | priorizas estética y velocidad | necesitas accesibilidad estricta (heroui) |

**⚖️ ¿Cuál elegir? — Anime.js, motion, GSAP**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Anime.js](human/fichas/animejs.md) | quieres animaciones potentes sin framework | usas React y quieres animaciones declarativas; mira `motion` |
| [motion](human/fichas/motion.md) | animas componentes React con API declarativa | necesitas timelines complejos no ligados a React (GSAP) |
| [GSAP](human/fichas/gsap.md) | necesitas animación avanzada y control fino de timelines | te basta animar componentes React con API declarativa (motion) |

**⚖️ ¿Cuál elegir? — Excalidraw, tldraw**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Excalidraw](human/fichas/excalidraw.md) | quieres diagramas rápidos con estilo boceto | prefieres diagramas como texto; mira `mermaid` |
| [tldraw](human/fichas/tldraw.md) | construyes una app con lienzo infinito | solo necesitas una pizarra lista; usa `excalidraw` |

**⚖️ ¿Cuál elegir? — open-design, Onlook**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [open-design](human/fichas/open-design.md) | generas UI desde texto y quieres edición visual | prefieres editar visualmente sobre tu código existente (plasmic) |
| [Onlook](human/fichas/onlook.md) | quieres editar tu app React visualmente con ayuda de IA | necesitas diseño desde cero en vectores; mira `penpot` |

**⚖️ ¿Cuál elegir? — CopilotKit, assistant-ui**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [CopilotKit](human/fichas/copilotkit.md) | quieres agentes que interactúen con la UI de tu app | solo necesitas una ventana de chat; mira `assistant-ui` |
| [assistant-ui](human/fichas/assistant-ui.md) | necesitas una UI de chat pulida en React | quieres agentes que manipulen tu app; mira `copilotkit` |

**⚖️ ¿Cuál elegir? — screenshot-to-code, Stitch SDK**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [screenshot-to-code](human/fichas/screenshot-to-code.md) | quieres pasar imágenes de diseño a código | trabajas desde Figma; mira `figma-context-mcp` |
| [Stitch SDK](human/fichas/stitch-sdk.md) | quieres automatizar Stitch | prefieres herramientas locales; mira `screenshot-to-code` |

### Componentes, iconos y sistemas de diseño

#### 🧱 ui ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 128k  
**Qué es:** El código fuente pasa a ser tuyo y lo editas a voluntad.  
**Instalación:** `npx shadcn@latest init` y luego `npx shadcn add <componente>`. Requiere React + Tailwind configurados.  
**Elige si:** quieres ser dueño del código de UI — **Evita si:** prefieres una lib "llave en mano" con updates automáticos (heroui)  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [plasmic](human/fichas/plasmic.md)  
**Más:** [ficha completa](human/fichas/ui.md) · [GitHub](https://github.com/shadcn-ui/ui)

#### 🧱 Ant Design
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 100k  
**Qué es:** Componentes muy completos para apps de negocio: tablas, formularios, fechas y layouts de backoffice.  
**Instalación:** `npm i antd`.  
**Elige si:** construyes apps empresariales con muchos datos — **Evita si:** quieres un estilo más personalizado; mira `ui`  
**Combina con:** [echarts](human/fichas/echarts.md)  
**Más:** [ficha completa](human/fichas/ant-design.md) · [GitHub](https://github.com/ant-design/ant-design)

#### 🧱 Material UI
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 99.3k  
**Qué es:** Cientos de componentes accesibles y personalizables para apps React, con temas y sistema de estilos propio.  
**Instalación:** `npm i @mui/material @emotion/react @emotion/styled`.  
**Elige si:** quieres una librería React completa y probada — **Evita si:** prefieres copiar componentes y estilarlos con Tailwind; mira `ui`  
**Combina con:** [Recharts](human/fichas/recharts.md)  
**Más:** [ficha completa](human/fichas/mui.md) · [GitHub](https://github.com/mui/material-ui)

#### 🧱 React Bits
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 51.6k  
**Qué es:** Fondos, textos animados y efectos listos para copiar en proyectos React y Next.js.  
**Instalación:** Copia el componente desde la web o usa `npx shadcn@latest add` con su registro.  
**Elige si:** quieres efectos visuales llamativos en React — **Evita si:** necesitas componentes de formulario y datos; mira `ui`  
**Combina con:** [ui](human/fichas/ui.md) · [motion](human/fichas/motion.md)  
**Más:** [ficha completa](human/fichas/react-bits.md) · [GitHub](https://github.com/DavidHDev/react-bits)

#### 🔄 swr
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 32.5k  
**Qué es:** Cubre el caso de consumir APIs en frontend sin manejar caché a mano.  
**Instalación:** `npm i swr`. Solo necesita un fetcher (una función async) por clave; funciona con cualquier API REST/GraphQL.  
**Elige si:** manejas datos remotos en React y quieres caché simple — **Evita si:** prefieres React Query con su modelo de caché global más rico  
**Combina con:** [heroui](human/fichas/heroui.md)  
**Más:** [ficha completa](human/fichas/swr.md) · [GitHub](https://github.com/vercel/swr)

#### 🦸 heroui
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 31.2k  
**Qué es:** Resuelve la accesibilidad seria sin renunciar a un estilado moderno.  
**Instalación:** `npm i @heroui/react` y configurar el plugin de Tailwind. Requiere React 18+ y Tailwind.  
**Elige si:** quieres calidad + accesibilidad listas — **Evita si:** quieres control copy-paste del código (ui)  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [swr](human/fichas/swr.md)  
**Más:** [ficha completa](human/fichas/heroui.md) · [GitHub](https://github.com/heroui-inc/heroui)

#### 🧱 Lucide
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 25.7k  
**Qué es:** Iconos limpios y uniformes, usados por shadcn/ui y muchas apps.  
**Instalación:** `npm i lucide-react`.  
**Elige si:** necesitas iconos consistentes — **Evita si:** buscas ilustraciones, no iconos  
**Combina con:** [ui](human/fichas/ui.md)  
**Más:** [ficha completa](human/fichas/lucide.md) · [GitHub](https://github.com/lucide-icons/lucide)

#### ✨ magicui
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.2k  
**Qué es:** Apunta al impacto visual más que a la accesibilidad estricta.  
**Instalación:** `npx shadcn add` apuntando al registro de Magic UI, o copiar el componente directamente. Requiere Tailwind y motion instalados.  
**Elige si:** priorizas estética y velocidad — **Evita si:** necesitas accesibilidad estricta (heroui)  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [motion](human/fichas/motion.md)  
**Más:** [ficha completa](human/fichas/magicui.md) · [GitHub](https://github.com/magicuidesign/magicui)

#### 🧱 Radix Primitives
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 19.5k  
**Qué es:** Resuelven accesibilidad, foco y teclado en diálogos, menús o tooltips, dejándote el estilo. Son la base de shadcn/ui.  
**Instalación:** `npm i radix-ui`.  
**Elige si:** construyes tu propio sistema de diseño — **Evita si:** quieres componentes ya estilados; mira `ui`  
**Combina con:** [ui](human/fichas/ui.md) · [tailwindcss](human/fichas/tailwindcss.md)  
**Más:** [ficha completa](human/fichas/radix-primitives.md) · [GitHub](https://github.com/radix-ui/primitives)

### CSS y estilos

#### 🎨 daisyUI ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 42.8k  
**Qué es:** Añade clases como `btn` o `card` sobre Tailwind para escribir menos HTML, sin JavaScript.  
**Instalación:** `npm i -D daisyui` y añádelo como plugin en tu CSS de Tailwind.  
**Elige si:** usas Tailwind y quieres componentes sin JavaScript — **Evita si:** usas React y quieres control total; mira `ui`  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)  
**Más:** [ficha completa](human/fichas/daisyui.md) · [GitHub](https://github.com/saadeghi/daisyui)

#### 🌬️ tailwindcss
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 98.7k  
**Qué es:** Elimina el contexto de estilos disperso entre hojas y componentes.  
**Instalación:** `npm i tailwindcss` y configurar el plugin de PostCSS/CLI, o vía CDN para pruebas rápidas. Requiere un build step para producción.  
**Elige si:** quieres estilar rápido y consistente — **Evita si:** prefieres CSS-in-JS o estilos scoped por componente  
**Combina con:** [heroui](human/fichas/heroui.md) · [magicui](human/fichas/magicui.md)  
**Más:** [ficha completa](human/fichas/tailwindcss.md) · [GitHub](https://github.com/tailwindlabs/tailwindcss)

#### 🧯 normalize.css
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 53.5k  
**Qué es:** Resuelve las inconsistencias de margen, tipografía y formularios entre Chrome, Firefox y Safari.  
**Instalación:** `npm i normalize.css` e importarlo al inicio de tu CSS, o enlazar por CDN. No requiere build step.  
**Elige si:** quieres base CSS uniforme y ligera — **Evita si:** ya usas el preflight de Tailwind, que cubre lo mismo  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)  
**Más:** [ficha completa](human/fichas/normalize-css.md) · [GitHub](https://github.com/necolas/normalize.css)

### Animación y 3D

#### 🔺 three.js ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 118k  
**Qué es:** Abstrae la complejidad de WebGL en escenas, cámaras, luces y mallas.  
**Instalación:** `npm i three` o vía CDN/módulo ES. Para algo más que una demo necesitas familiaridad con conceptos de gráficos 3D.  
**Elige si:** renderizas 3D en web y quieres control a bajo nivel — **Evita si:** trabajas solo 2D o prefieres la ergonomía de React (react-three-fiber)  
**Combina con:** [react-three-fiber](human/fichas/react-three-fiber.md) · [GSAP](human/fichas/gsap.md)  
**Más:** [ficha completa](human/fichas/three-js.md) · [GitHub](https://github.com/mrdoob/three.js)

#### ✨ Anime.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 74.5k  
**Qué es:** API simple y potente para líneas de tiempo, scroll y animaciones complejas.  
**Instalación:** `npm i animejs`.  
**Elige si:** quieres animaciones potentes sin framework — **Evita si:** usas React y quieres animaciones declarativas; mira `motion`  
**Más:** [ficha completa](human/fichas/animejs.md) · [GitHub](https://github.com/juliangarnier/anime)

#### 🌀 motion
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 35k  
**Qué es:** Hizo accesible la animación en el ecosistema React.  
**Instalación:** `npm i motion` (o `framer-motion` para la versión legacy). Requiere React para los bindings `motion.*`.  
**Elige si:** animas componentes React con API declarativa — **Evita si:** necesitas timelines complejos no ligados a React (GSAP)  
**Combina con:** [magicui](human/fichas/magicui.md) · [react-three-fiber](human/fichas/react-three-fiber.md)  
**Más:** [ficha completa](human/fichas/motion.md) · [GitHub](https://github.com/motiondivision/motion)

#### 🔻 react-three-fiber
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 33.6k  
**Qué es:** Lleva la mentalidad componible de React al 3D sin abandonar three.js por debajo.  
**Instalación:** `npm i three @react-three/fiber` (y normalmente `@react-three/drei` para helpers). Requiere React + three.js.  
**Elige si:** haces 3D en React y quieres reactividad — **Evita si:** no usas React o necesitas control a bajo nivel (three.js directo)  
**Combina con:** [motion](human/fichas/motion.md)  
**Más:** [ficha completa](human/fichas/react-three-fiber.md) · [GitHub](https://github.com/pmndrs/react-three-fiber)

#### 🎞️ GSAP
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 30.4k  
**Qué es:** Es la herramienta de referencia del motion web profesional.  
**Instalación:** `npm i gsap` o vía CDN. Algunos plugins premium requieren membresía del Club GreenSock; los core son libres.  
**Elige si:** necesitas animación avanzada y control fino de timelines — **Evita si:** te basta animar componentes React con API declarativa (motion)  
**Combina con:** [motion](human/fichas/motion.md)  
**Más:** [ficha completa](human/fichas/gsap.md) · [GitHub](https://github.com/greensock/GSAP)

### Diseño visual, canvas y builders

#### ✏️ Excalidraw ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 135k  
**Qué es:** Dibuja diagramas rápidos que parecen bocetos, colabora en tiempo real y embébela en tus apps como componente React.  
**Instalación:** Úsala en excalidraw.com, `npm i @excalidraw/excalidraw` o self-host con Docker.  
**Elige si:** quieres diagramas rápidos con estilo boceto — **Evita si:** prefieres diagramas como texto; mira `mermaid`  
**Más:** [ficha completa](human/fichas/excalidraw.md) · [GitHub](https://github.com/excalidraw/excalidraw)

#### 🎨 open-design
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 107k  
**Qué es:** Resuelve el ir y venir entre prompt, preview y código exportable.  
**Instalación:** Clonar el repo y compilar la app Tauri, o usar los binarios de release según plataforma. Requiere claves API de al menos un proveedor (OpenAI/Anthropic/Google/DeepSeek).  
**Elige si:** generas UI desde texto y quieres edición visual — **Evita si:** prefieres editar visualmente sobre tu código existente (plasmic)  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [heroui](human/fichas/heroui.md)  
**Más:** [ficha completa](human/fichas/open-design.md) · [GitHub](https://github.com/nexu-io/open-design)

#### ✏️ penpot
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 62.2k  
**Qué es:** Es la alternativa abierta a Figma más conocida.  
**Instalación:** `docker compose` con los manifiestos oficiales (o plan cloud gestionado). Requiere varios contenedores y recursos no triviales, de ahí el setup 🔴.  
**Elige si:** quieres diseño abierto y soberano, self-host — **Evita si:** necesitas generación por IA (open-design) o no quieres operar Docker  
**Combina con:** [plasmic](human/fichas/plasmic.md)  
**Más:** [ficha completa](human/fichas/penpot.md) · [GitHub](https://github.com/penpot/penpot)

#### ✏️ tldraw
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 51.4k  
**Qué es:** Base de muchas herramientas de pizarra y de UI generativa con IA. Ofrece colaboración y personalización completa.  
**Instalación:** `npm i tldraw`.  
**Elige si:** construyes una app con lienzo infinito — **Evita si:** solo necesitas una pizarra lista; usa `excalidraw`  
**Más:** [ficha completa](human/fichas/tldraw.md) · [GitHub](https://github.com/tldraw/tldraw)

#### ✏️ Onlook
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 27.2k  
**Qué es:** Edita tu app en un lienzo visual o pide cambios a la IA, y Onlook escribe el código en tu proyecto.  
**Instalación:** Úsalo en su web o sigue el README para correrlo en local.  
**Elige si:** quieres editar tu app React visualmente con ayuda de IA — **Evita si:** necesitas diseño desde cero en vectores; mira `penpot`  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [ui](human/fichas/ui.md)  
**Más:** [ficha completa](human/fichas/onlook.md) · [GitHub](https://github.com/onlook-dev/onlook)

#### 🧱 plasmic
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 7.2k  
**Qué es:** Cubre el hueco entre no-code y desarrollo a medida.  
**Instalación:** `npm i @plasmicapp/loader-nextjs` (o el loader del framework) y conectar el proyecto a tu app. Requiere un proyecto React/Next existente.  
**Elige si:** quieres editar visual sobre tu código React — **Evita si:** generas desde texto sin codebase previo (open-design)  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)  
**Más:** [ficha completa](human/fichas/plasmic.md) · [GitHub](https://github.com/plasmicapp/plasmic)

### UI generada con IA y frontends para agentes

#### 🪄 CopilotKit ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 38.6k  
**Qué es:** Añade copilotos, chat y agentes que actúan sobre tu app, con estado compartido entre agente y UI. Se integra con LangGraph, Mastra y más.  
**Instalación:** `npx copilotkit@latest init` o `npm i @copilotkit/react-core @copilotkit/react-ui`.  
**Elige si:** quieres agentes que interactúen con la UI de tu app — **Evita si:** solo necesitas una ventana de chat; mira `assistant-ui`  
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [Mastra](human/fichas/mastra.md)  
**Más:** [ficha completa](human/fichas/copilotkit.md) · [GitHub](https://github.com/CopilotKit/CopilotKit)

#### 🪄 screenshot-to-code
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 81.1k  
**Qué es:** Sube una imagen o graba un video de una web y obtén código funcional que puedes iterar.  
**Instalación:** Clona el repo y ejecuta backend (`poetry run uvicorn`) y frontend (`yarn dev`), o usa Docker.  
**Elige si:** quieres pasar imágenes de diseño a código — **Evita si:** trabajas desde Figma; mira `figma-context-mcp`  
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)  
**Más:** [ficha completa](human/fichas/screenshot-to-code.md) · [GitHub](https://github.com/abi/screenshot-to-code)

#### 🪄 OpenUI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 15k  
**Qué es:** Permite que el modelo devuelva componentes interactivos (tablas, formularios, gráficos) que tu app renderiza.  
**Instalación:** Sigue el README para instalar el SDK de React.  
**Elige si:** quieres que tu agente responda con interfaces — **Evita si:** solo necesitas chat de texto; mira `assistant-ui`  
**Combina con:** [CopilotKit](human/fichas/copilotkit.md)  
**Más:** [ficha completa](human/fichas/openui.md) · [GitHub](https://github.com/thesysdev/openui)

#### 🪄 assistant-ui
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13k  
**Qué es:** Componentes componibles de chat con streaming, adjuntos, markdown y herramientas, compatibles con AI SDK y LangGraph.  
**Instalación:** `npx assistant-ui@latest init`.  
**Elige si:** necesitas una UI de chat pulida en React — **Evita si:** quieres agentes que manipulen tu app; mira `copilotkit`  
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md) · [ui](human/fichas/ui.md)  
**Más:** [ficha completa](human/fichas/assistant-ui.md) · [GitHub](https://github.com/assistant-ui/assistant-ui)

#### 🪄 Stitch SDK
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.8k  
**Qué es:** Automatiza Stitch, el generador de interfaces de Google, para integrarlo en tus flujos y agentes.  
**Instalación:** `npm i @google/stitch-sdk` (requiere acceso a Stitch).  
**Elige si:** quieres automatizar Stitch — **Evita si:** prefieres herramientas locales; mira `screenshot-to-code`  
**Combina con:** [Stitch Skills](human/fichas/stitch-skills.md)  
**Más:** [ficha completa](human/fichas/stitch-sdk.md) · [GitHub](https://github.com/google-labs-code/stitch-sdk)

### Skills de diseño para agentes

#### 🎯 Stitch Skills ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 8.7k  
**Qué es:** Skills en el estándar abierto Agent Skills que enseñan a Claude Code, Codex o Gemini CLI a diseñar con Stitch.  
**Instalación:** Copia las skills a la carpeta de skills de tu agente y configura el MCP de Stitch.  
**Elige si:** usas Stitch con un agente de código — **Evita si:** no usas Stitch  
**Combina con:** [Stitch SDK](human/fichas/stitch-sdk.md) · [Gemini CLI](human/fichas/gemini-cli.md)  
**Más:** [ficha completa](human/fichas/stitch-skills.md) · [GitHub](https://github.com/google-labs-code/stitch-skills)

#### 🎨 ui-ux-pro-max-skill
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 148k  
**Qué es:** Resuelve el punto débil habitual del código asistido por IA: la jerarquía visual y el acabado.  
**Instalación:** Clona el repo y sigue su README; instala la CLI vía Node (`npx` o instalación local) y copia las skills al directorio de skills de tu asistente. Requiere Node.js y un asistente compatible con skills.  
**Elige si:** generas UI con IA y el resultado se ve genérico o despulido — **Evita si:** no trabajas frontend o ya tienes un sistema de diseño impuesto  
**Combina con:** [taste-skill](human/fichas/taste-skill.md) · [impeccable](human/fichas/impeccable.md) · [tailwindcss](human/fichas/tailwindcss.md)  
**Más:** [ficha completa](human/fichas/ui-ux-pro-max-skill.md) · [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

#### 🍷 taste-skill
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 113k  
**Qué es:** Ataca el acabado "de plantilla" que delata a las UIs generadas por IA.  
**Instalación:** Clona el repo y copia las skills a tu directorio de skills (Codex, Cursor o Claude Code); las de imagen requieren un generador disponible y su correspondiente acceso/API.  
**Elige si:** quieres frontends con gusto y no te basta con UI funcional — **Evita si:** ya tienes un design system cerrado o no usas generadores de imagen  
**Combina con:** [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md) · [impeccable](human/fichas/impeccable.md)  
**Más:** [ficha completa](human/fichas/taste-skill.md) · [GitHub](https://github.com/Leonxlnx/taste-skill)

#### 💎 impeccable
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 107k  
**Qué es:** Ataca el patrón repetitivo de interfaces que "huelen" a IA.  
**Instalación:** `npx impeccable` (skill para Claude Code y compatibles). Requiere Node y un agente compatible con skills.  
**Elige si:** quieres frontends que no parezcan generados por IA — **Evita si:** no generas UI con agentes  
**Combina con:** [taste-skill](human/fichas/taste-skill.md) · [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md)  
**Más:** [ficha completa](human/fichas/impeccable.md) · [GitHub](https://github.com/pbakaus/impeccable)

#### ✏️ skills_emil
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 55.6k  
**Qué es:** Resuelve el handoff diseño↔código, no solo la estética final.  
**Instalación:** Copia el `SKILL.md` al directorio de skills de tu asistente (Claude Code, Codex, Cursor); es referencia local del autor, así que consulta la fuente original para la versión más reciente.  
**Elige si:** trabajas diseño+dev en equipo y sufres el handoff — **Evita si:** buscas componentes listos o trabajas solo  
**Combina con:** [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md)  
**Más:** [ficha completa](human/fichas/skills-emil.md) · [GitHub](https://github.com/emilkowalski/skills)

#### 📐 design.md
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 28.8k  
**Qué es:** Resuelve la inconsistencia de marca cuando varias personas o agentes tocan la UI.  
**Instalación:** Crear un `design.md` en el repo siguiendo el formato (sin dependencias). Solo necesitas un agente de código que lo cargue como contexto.  
**Elige si:** quieres consistencia de marca con IA y usas agentes para UI — **Evita si:** no usas agentes para generar código de UI  
**Combina con:** [impeccable](human/fichas/impeccable.md)  
**Más:** [ficha completa](human/fichas/design-md.md) · [GitHub](https://github.com/google-labs-code/design.md)

---

## 📊 10. Analítica & Visualización

Analítica web y de producto, BI y dashboards, chat con tus datos, librerías de gráficos y apps de datos en Python.

**⚖️ ¿Cuál elegir? — Umami, Plausible Analytics, Matomo**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Umami](human/fichas/umami.md) | quieres analítica web simple y privada | necesitas analítica de producto avanzada; mira `posthog` |
| [Plausible Analytics](human/fichas/plausible.md) | quieres analítica minimalista y privada | necesitas embudos y eventos complejos; mira `posthog` |
| [Matomo](human/fichas/matomo.md) | necesitas analítica completa como Google Analytics pero propia | quieres algo simple; mira `umami` |

**⚖️ ¿Cuál elegir? — Apache Superset, metabase, Redash**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Apache Superset](human/fichas/superset.md) | quieres BI empresarial abierto | buscas algo muy fácil para no técnicos; mira `metabase` |
| [metabase](human/fichas/metabase.md) | quieres BI accesible para perfiles no técnicos | necesitas analítica de eventos por usuario (posthog) |
| [Redash](human/fichas/redash.md) | tu equipo trabaja con SQL y quiere compartir rápido | necesitas BI con permisos finos; mira `superset` |

**⚖️ ¿Cuál elegir? — WrenAI, PandasAI**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [WrenAI](human/fichas/wrenai.md) | quieres text-to-SQL confiable para el negocio | solo analizas un CSV; mira `pandas-ai` |
| [PandasAI](human/fichas/pandas-ai.md) | quieres preguntar a tus tablas en lenguaje natural | necesitas text-to-SQL gobernado para la empresa; mira `wrenai` |

**⚖️ ¿Cuál elegir? — Recharts, D3.js, Chart.js, echarts**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Recharts](human/fichas/recharts.md) | tu app es React y quieres gráficos declarativos | no usas React; mira `chart-js` |
| [D3.js](human/fichas/d3.md) | necesitas visualizaciones totalmente personalizadas | quieres gráficos estándar rápido; mira `chart-js` o `recharts` |
| [Chart.js](human/fichas/chart-js.md) | quieres gráficos simples sin aprender una librería compleja | necesitas visualizaciones a medida; mira `d3` |
| [echarts](human/fichas/echarts.md) | necesitas gráficos ricos y variados embebidos | solo series temporales simples y priorizas peso (uPlot) |

**⚖️ ¿Cuál elegir? — Gradio, streamlit**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Gradio](human/fichas/gradio.md) | quieres una demo web de tu modelo rápido | construyes una app de datos con varias páginas; mira `streamlit` |
| [streamlit](human/fichas/streamlit.md) | quieres una UI de datos al vuelo y prototipos rápidos | necesitas una app productiva con control fino del frontend (dash) |

### Analítica web y de producto

#### 📈 Umami ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 40k  
**Qué es:** Mide visitas, campañas, eventos, conversiones e ingresos en un panel simple, cumpliendo GDPR.  
**Instalación:** `docker compose up -d` con el archivo del repo.  
**Elige si:** quieres analítica web simple y privada — **Evita si:** necesitas analítica de producto avanzada; mira `posthog`  
**Más:** [ficha completa](human/fichas/umami.md) · [GitHub](https://github.com/umami-software/umami)

#### 📈 posthog
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 40.7k  
**Qué es:** Cubre todo el ciclo de medición de producto sin integrar varias herramientas.  
**Instalación:** `docker compose` para self-host, o SDK vía `npm i posthog-js` / `pip install posthog` apuntando al cloud. El self-host requiere ClickHouse y recursos no triviales.  
**Elige si:** quieres entender el uso real y el comportamiento de usuarios — **Evita si:** solo necesitas BI sobre una BD estática (metabase)  
**Combina con:** [metabase](human/fichas/metabase.md)  
**Más:** [ficha completa](human/fichas/posthog.md) · [GitHub](https://github.com/PostHog/posthog)

#### 📈 Plausible Analytics
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 29.8k  
**Qué es:** Un panel de una sola página con lo esencial: visitas, fuentes, páginas y objetivos.  
**Instalación:** Self-host con `plausible/community-edition` y Docker Compose.  
**Elige si:** quieres analítica minimalista y privada — **Evita si:** necesitas embudos y eventos complejos; mira `posthog`  
**Más:** [ficha completa](human/fichas/plausible.md) · [GitHub](https://github.com/plausible/analytics)

#### 📈 Matomo
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 22k  
**Qué es:** Analítica web completa con embudos, mapas de calor y comercio electrónico, auto-hospedada.  
**Instalación:** Self-host con el paquete oficial o `docker run -p 8080:80 matomo`.  
**Elige si:** necesitas analítica completa como Google Analytics pero propia — **Evita si:** quieres algo simple; mira `umami`  
**Más:** [ficha completa](human/fichas/matomo.md) · [GitHub](https://github.com/matomo-org/matomo)

### BI, dashboards y chat con datos

#### 📊 Apache Superset ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 75.5k  
**Qué es:** Conecta tus bases SQL, crea gráficos y dashboards sin código o con SQL Lab, con control de acceso.  
**Instalación:** `git clone https://github.com/apache/superset && cd superset && docker compose -f docker-compose-image-tag.yml up`.  
**Elige si:** quieres BI empresarial abierto — **Evita si:** buscas algo muy fácil para no técnicos; mira `metabase`  
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [WrenAI](human/fichas/wrenai.md)  
**Más:** [ficha completa](human/fichas/superset.md) · [GitHub](https://github.com/apache/superset)

#### 📊 WrenAI ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.1k  
**Qué es:** Define tu modelo de datos una vez y los usuarios (o agentes) preguntan en lenguaje natural para obtener SQL, gráficos y respuestas.  
**Instalación:** Descarga el lanzador de releases o usa Docker Compose del repo.  
**Elige si:** quieres text-to-SQL confiable para el negocio — **Evita si:** solo analizas un CSV; mira `pandas-ai`  
**Combina con:** [Apache Superset](human/fichas/superset.md) · [DuckDB](human/fichas/duckdb.md)  
**Más:** [ficha completa](human/fichas/wrenai.md) · [GitHub](https://github.com/Canner/WrenAI)

#### 📊 Grafana
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 77.8k  
**Qué es:** Crea dashboards y alertas sobre Prometheus, Loki, bases SQL y decenas de fuentes. Estándar en monitoreo.  
**Instalación:** `docker run -d -p 3000:3000 grafana/grafana`.  
**Elige si:** necesitas monitoreo y alertas en tiempo real — **Evita si:** buscas BI de negocio; mira `superset` o `metabase`  
**Combina con:** [langfuse](human/fichas/langfuse.md)  
**Más:** [ficha completa](human/fichas/grafana.md) · [GitHub](https://github.com/grafana/grafana)

#### 📊 metabase
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 50.3k  
**Qué es:** Apunta a perfiles no técnicos que necesitan reporting propio.  
**Instalación:** `docker run metabase/metabase`, o JAR ejecutable con Java. Requiere una BD de aplicación (H2 por defecto, recomendado Postgres/MySQL para producción).  
**Elige si:** quieres BI accesible para perfiles no técnicos — **Evita si:** necesitas analítica de eventos por usuario (posthog)  
**Combina con:** [posthog](human/fichas/posthog.md) · [echarts](human/fichas/echarts.md)  
**Más:** [ficha completa](human/fichas/metabase.md) · [GitHub](https://github.com/metabase/metabase)

#### 📊 Redash
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 28.9k  
**Qué es:** Pensada para analistas que escriben SQL y quieren compartir resultados rápido con el equipo.  
**Instalación:** Self-host con el script de instalación o Docker Compose del repo.  
**Elige si:** tu equipo trabaja con SQL y quiere compartir rápido — **Evita si:** necesitas BI con permisos finos; mira `superset`  
**Más:** [ficha completa](human/fichas/redash.md) · [GitHub](https://github.com/getredash/redash)

#### 📊 PandasAI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.9k  
**Qué es:** Haces preguntas en lenguaje natural y genera el código de análisis o gráficos. Útil para analistas y apps de datos.  
**Instalación:** `pip install pandasai`.  
**Elige si:** quieres preguntar a tus tablas en lenguaje natural — **Evita si:** necesitas text-to-SQL gobernado para la empresa; mira `wrenai`  
**Combina con:** [DuckDB](human/fichas/duckdb.md)  
**Más:** [ficha completa](human/fichas/pandas-ai.md) · [GitHub](https://github.com/sinaptik-ai/pandas-ai)

### Librerías de gráficos

#### 📉 Recharts ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 27.7k  
**Qué es:** Construye gráficos con componentes de React. Muy usada en dashboards de apps React y en shadcn/ui.  
**Instalación:** `npm i recharts`.  
**Elige si:** tu app es React y quieres gráficos declarativos — **Evita si:** no usas React; mira `chart-js`  
**Combina con:** [ui](human/fichas/ui.md)  
**Más:** [ficha completa](human/fichas/recharts.md) · [GitHub](https://github.com/recharts/recharts)

#### 📉 D3.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 114k  
**Qué es:** Da control total sobre cada elemento visual. Base de muchas librerías de gráficos y del periodismo de datos.  
**Instalación:** `npm i d3`.  
**Elige si:** necesitas visualizaciones totalmente personalizadas — **Evita si:** quieres gráficos estándar rápido; mira `chart-js` o `recharts`  
**Más:** [ficha completa](human/fichas/d3.md) · [GitHub](https://github.com/d3/d3)

#### 📉 Chart.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 67.8k  
**Qué es:** Ocho tipos de gráfico listos, responsivos y animados con muy poco código. Ideal para dashboards web simples.  
**Instalación:** `npm i chart.js`.  
**Elige si:** quieres gráficos simples sin aprender una librería compleja — **Evita si:** necesitas visualizaciones a medida; mira `d3`  
**Más:** [ficha completa](human/fichas/chart-js.md) · [GitHub](https://github.com/chartjs/Chart.js)

#### 📉 echarts
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 67.7k  
**Qué es:** Cubre casi cualquier tipo de chart en el navegador.  
**Instalación:** `npm i echarts` o vía CDN. Para tipos especiales (mapas) puede necesitar datos geográficos aparte.  
**Elige si:** necesitas gráficos ricos y variados embebidos — **Evita si:** solo series temporales simples y priorizas peso (uPlot)  
**Combina con:** [metabase](human/fichas/metabase.md) · [heroui](human/fichas/heroui.md)  
**Más:** [ficha completa](human/fichas/echarts.md) · [GitHub](https://github.com/apache/echarts)

#### 📈 uPlot
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 10.6k  
**Qué es:** Apuesta por hacer una sola cosa (líneas/áreas temporales) mejor que ninguna.  
**Instalación:** `npm i uplot` o vía CDN. Sin dependencias; se integra en cualquier stack web.  
**Elige si:** priorizas velocidad y peso del bundle — **Evita si:** necesitas tipos de gráfico variados (echarts)  
**Combina con:** [swr](human/fichas/swr.md)  
**Más:** [ficha completa](human/fichas/uplot.md) · [GitHub](https://github.com/leeoniya/uPlot)

### Apps de datos en Python

#### 🧪 Gradio ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 44k  
**Qué es:** Envuelve una función Python en una interfaz web con entradas y salidas de texto, imagen, audio o chat. Base de Hugging Face Spaces.  
**Instalación:** `pip install gradio`.  
**Elige si:** quieres una demo web de tu modelo rápido — **Evita si:** construyes una app de datos con varias páginas; mira `streamlit`  
**Combina con:** [Transformers](human/fichas/transformers.md)  
**Más:** [ficha completa](human/fichas/gradio.md) · [GitHub](https://github.com/gradio-app/gradio)

#### 📊 streamlit
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 46.3k  
**Qué es:** Convierte un script de datos en una app web interactiva casi al instante.  
**Instalación:** `pip install streamlit` y `streamlit run app.py`. Requiere Python; no necesita frontend aparte.  
**Elige si:** quieres una UI de datos al vuelo y prototipos rápidos — **Evita si:** necesitas una app productiva con control fino del frontend (dash)  
**Combina con:** [dash](human/fichas/dash.md) · [data-science-ipython-notebooks](human/fichas/data-science-ipython-notebooks.md)  
**Más:** [ficha completa](human/fichas/streamlit.md) · [GitHub](https://github.com/streamlit/streamlit)

#### 🧮 dash
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 24.5k  
**Qué es:** Cubre el caso de dashboards productivos en Python sin salir del lenguaje.  
**Instalación:** `pip install dash`. Requiere Python y, para producción, un servidor WSGI (gunicorn/uwsgi).  
**Elige si:** quieres dashboards productivos en Python con control del frontend — **Evita si:** prefieres prototipos ultrarrápidos (streamlit)  
**Combina con:** [streamlit](human/fichas/streamlit.md) · [echarts](human/fichas/echarts.md)  
**Más:** [ficha completa](human/fichas/dash.md) · [GitHub](https://github.com/plotly/dash)

### Recursos y casos de uso

#### 📚 daily_stock_analysis ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟡 medio · ⭐ 69.5k  
**Qué es:** Combina datos de mercado, noticias en tiempo real y análisis con LLM para generar reportes automáticos por Telegram, Slack, correo o WeChat. Puede correr gratis con GitHub Actions.  
**Instalación:** Haz fork y configura los secretos para GitHub Actions, o ejecútalo con Docker siguiendo el README.  
**Elige si:** quieres un análisis bursátil diario automatizado — **Evita si:** buscas asesoría financiera: esto no lo es  
**Combina con:** [n8n](human/fichas/n8n.md)  
**Más:** [ficha completa](human/fichas/daily-stock-analysis.md) · [GitHub](https://github.com/ZhuLinsen/daily_stock_analysis)

#### 🗂️ awesome-dataviz
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 4.5k  
**Qué es:** Punto de partida para descubrir opciones de dataviz sin búsquedas dispersas.  
**Instalación:** No requiere instalación; se consulta en GitHub.  
**Elige si:** buscas opciones de visualización y aún no has elegido — **Evita si:** ya elegiste tu librería y solo necesitas usarla  
**Combina con:** [echarts](human/fichas/echarts.md) · [awesome-bigdata](human/fichas/awesome-bigdata.md)  
**Más:** [ficha completa](human/fichas/awesome-dataviz.md) · [GitHub](https://github.com/hal9ai/awesome-dataviz)

---

## 🖼️ 11. Generación de Imagen & Visión

Interfaces de difusión, modelos y control, restauración y upscaling, rostros y visión por computador.

**⚖️ ¿Cuál elegir? — stable-diffusion-webui, FLUX, ComfyUI, Stable Diffusion WebUI Forge**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [stable-diffusion-webui](human/fichas/stable-diffusion-webui.md) | quieres extensiones y comunidad amplia | prefieres un flujo moderno y limpio (InvokeAI) |
| [FLUX](human/fichas/flux.md) | quieres generar imágenes de alta calidad con modelos abiertos | no tienes GPU potente; usa una API en la nube |
| [ComfyUI](human/fichas/comfyui.md) | quieres control total y pipelines reproducibles | buscas simplicidad inmediata (Fooocus) |
| [Stable Diffusion WebUI Forge](human/fichas/sd-webui-forge.md) | quieres la WebUI clásica pero más rápida | prefieres flujos por nodos; mira `comfyui` |

**⚖️ ¿Cuál elegir? — InvokeAI, Krita AI Diffusion**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [InvokeAI](human/fichas/invokeai.md) | trabajas creatividad profesional y quieres una app estable con canvas | solo haces una prueba puntual (Fooocus) o prefieres grafos nodales (ComfyUI) |
| [Krita AI Diffusion](human/fichas/krita-ai-diffusion.md) | ilustras en Krita y quieres IA integrada | quieres automatizar generación en lote; mira `comfyui` |

**⚖️ ¿Cuál elegir? — GFPGAN, CodeFormer**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [GFPGAN](human/fichas/gfpgan.md) | restauras rostros borrosos o fundidos | necesitas upscaling general de la imagen (Real-ESRGAN) |
| [CodeFormer](human/fichas/codeformer.md) | quieres restaurar rostros | quieres escalar la imagen completa; mira `real-esrgan` |

**⚖️ ¿Cuál elegir? — Deep-Live-Cam, FaceFusion**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Deep-Live-Cam](human/fichas/deep-live-cam.md) | necesitas swap en vivo legítimo con consentimiento | no puedes garantizar uso ético/consentimiento o no tienes GPU |
| [FaceFusion](human/fichas/facefusion.md) | necesitas manipulación facial de calidad con consentimiento | no tienes consentimiento de las personas |

**⚖️ ¿Cuál elegir? — face_recognition, InsightFace**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [face_recognition](human/fichas/face-recognition.md) | necesitas reconocimiento facial básico y rápido de implementar | buscas restauración/animación (GFPGAN/LivePortrait) o precisión de producción (mejor DeepFace/InsightFace) |
| [InsightFace](human/fichas/insightface.md) | necesitas reconocimiento facial preciso | solo quieres detectar caras simples; mira `opencv` |

**⚖️ ¿Cuál elegir? — SAM 2, Segment Anything (SAM)**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [SAM 2](human/fichas/sam2.md) | necesitas segmentar objetos en video | solo trabajas con imágenes sueltas; `segment-anything` basta |
| [Segment Anything (SAM)](human/fichas/segment-anything.md) | necesitas segmentar objetos en imágenes | trabajas con video; mira `sam2` |

### Interfaces para generar imágenes

#### 🖼️ stable-diffusion-webui ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 165k  
**Qué es:** Es la UI que popularizó la difusión local.  
**Instalación:** `git clone` y ejecutar `webui-user.bat` (Windows) o `webui.sh` (Linux/Mac); el script crea el entorno e instala dependencias automáticamente. Requiere GPU con VRAM decente y checkpoints descargados aparte.  
**Elige si:** quieres extensiones y comunidad amplia — **Evita si:** prefieres un flujo moderno y limpio (InvokeAI)  
**Combina con:** [sd-webui-controlnet](human/fichas/sd-webui-controlnet.md)  
**Más:** [ficha completa](human/fichas/stable-diffusion-webui.md) · [GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

#### 🧠 ComfyUI
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 146k  
**Qué es:** Resuelve la composición de flujos de difusión complejos que una UI fija no permite.  
**Instalación:** `git clone` del repo y arranque con `python main.py` (o paquete portable en Windows); requiere descargar checkpoints aparte y una GPU con VRAM decente (8 GB+ recomendado).  
**Elige si:** quieres control total y pipelines reproducibles — **Evita si:** buscas simplicidad inmediata (Fooocus)  
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)  
**Más:** [ficha completa](human/fichas/comfyui.md) · [GitHub](https://github.com/Comfy-Org/ComfyUI)

#### 🎨 Fooocus
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 53.9k  
**Qué es:** Es la opción más sencilla para empezar con difusión local.  
**Instalación:** Descargar el paquete portable (un clic, descomprimir y ejecutar `run.bat` en Windows) o `git clone` con su script de arranque. Requiere GPU con VRAM moderada (6 GB+ recomendado).  
**Elige si:** quieres resultados ya, sin curva — **Evita si:** necesitas control fino del pipeline (ComfyUI)  
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)  
**Más:** [ficha completa](human/fichas/fooocus.md) · [GitHub](https://github.com/lllyasviel/Fooocus)

#### 🖌️ InvokeAI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 29.1k  
**Qué es:** Resuelve la fragmentación de herramientas SD reuniendo generación, edición y control en una sola app self-hosted.  
**Instalación:** Instalador automático multiplataforma (launcher) o `pip install invokeai`; arranca un servidor web local tras configurar los modelos. Requiere GPU NVIDIA con VRAM generosa (8 GB+) y pesos de SD/SDXL descargados.  
**Elige si:** trabajas creatividad profesional y quieres una app estable con canvas — **Evita si:** solo haces una prueba puntual (Fooocus) o prefieres grafos nodales (ComfyUI)  
**Combina con:** [diffusers](human/fichas/diffusers.md) · [ControlNet](human/fichas/controlnet.md)  
**Más:** [ficha completa](human/fichas/invokeai.md) · [GitHub](https://github.com/invoke-ai/InvokeAI)

#### 🖼️ Stable Diffusion WebUI Forge
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 13.1k  
**Qué es:** Mantiene la interfaz de AUTOMATIC1111 con mejoras de rendimiento y soporte de modelos nuevos como FLUX.  
**Instalación:** Descarga el paquete de un clic desde los releases o clona y ejecuta `webui-user`.  
**Elige si:** quieres la WebUI clásica pero más rápida — **Evita si:** prefieres flujos por nodos; mira `comfyui`  
**Combina con:** [ControlNet](human/fichas/controlnet.md)  
**Más:** [ficha completa](human/fichas/sd-webui-forge.md) · [GitHub](https://github.com/lllyasviel/stable-diffusion-webui-forge)

#### 🖼️ Krita AI Diffusion
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 10.9k  
**Qué es:** Pinta, selecciona y genera dentro de tu editor de imágenes favorito; usa ComfyUI por debajo.  
**Instalación:** Instala el plugin desde el gestor de Krita; él instala ComfyUI automáticamente.  
**Elige si:** ilustras en Krita y quieres IA integrada — **Evita si:** quieres automatizar generación en lote; mira `comfyui`  
**Combina con:** [ComfyUI](human/fichas/comfyui.md)  
**Más:** [ficha completa](human/fichas/krita-ai-diffusion.md) · [GitHub](https://github.com/Acly/krita-ai-diffusion)

### Modelos, librerías y control

#### 🌀 FLUX ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 26.1k  
**Qué es:** Modelos de texto a imagen de alta calidad, con variantes para edición, relleno y control.  
**Instalación:** `pip install -e ".[all]"` tras clonar el repo, o úsalo vía ComfyUI o Diffusers.  
**Elige si:** quieres generar imágenes de alta calidad con modelos abiertos — **Evita si:** no tienes GPU potente; usa una API en la nube  
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md)  
**Más:** [ficha completa](human/fichas/flux.md) · [GitHub](https://github.com/black-forest-labs/flux)

#### 🤗 diffusers
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 34.9k  
**Qué es:** Es la capa de abstracción que unifica el zoo de modelos de difusión bajo una misma interfaz Python.  
**Instalación:** `pip install diffusers transformers accelerate`; los pesos se descargan automáticamente desde el Hub al instanciar un pipeline. Requiere GPU para uso práctico (aunque corre en CPU, muy lento) y espacio en disco para los pesos.  
**Elige si:** programas generación y quieres control total por código — **Evita si:** quieres una UI lista (Fooocus) o grafos nodales (ComfyUI)  
**Combina con:** [ControlNet](human/fichas/controlnet.md) · [cosmos](human/fichas/cosmos.md)  
**Más:** [ficha completa](human/fichas/diffusers.md) · [GitHub](https://github.com/huggingface/diffusers)

#### 🧭 ControlNet
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 34.2k  
**Qué es:** Resuelve el problema de que el texto por sí solo no controla la composición de la imagen.  
**Instalación:** `git clone` del repo y entorno con sus dependencias; descargar los pesos de ControlNet además del modelo base de Stable Diffusion. Requiere GPU NVIDIA y disco para varios pares de pesos.  
**Elige si:** necesitas control estructural fino de la composición — **Evita si:** ya trabajas en SD WebUI (sd-webui-controlnet) o ComfyUI (tienen integración propia) y no necesitas el repo original  
**Combina con:** [diffusers](human/fichas/diffusers.md) · [ComfyUI](human/fichas/comfyui.md)  
**Más:** [ficha completa](human/fichas/controlnet.md) · [GitHub](https://github.com/lllyasviel/ControlNet)

#### 🧩 sd-webui-controlnet
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 17.8k  
**Qué es:** Lleva el control composicional al flujo de trabajo habitual de la WebUI sin tocar código.  
**Instalación:** Desde la pestaña Extensions de la WebUI (instalar por URL del repo) o `git clone` en `extensions/`; descargar luego los modelos ControlNet a `models/ControlNet`. Requiere la WebUI ya funcionando con GPU.  
**Elige si:** ya usas SD WebUI y quieres ControlNet sin cambiar de entorno — **Evita si:** trabajas en ComfyUI (usa sus propios nodos) o por código (diffusers)  
**Combina con:** [stable-diffusion-webui](human/fichas/stable-diffusion-webui.md) · [ControlNet](human/fichas/controlnet.md)  
**Más:** [ficha completa](human/fichas/sd-webui-controlnet.md) · [GitHub](https://github.com/Mikubill/sd-webui-controlnet)

#### 🪞 ComfyUI_IPAdapter_plus
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 6.2k  
**Qué es:** Funciona como un "LoRA de una sola imagen": le das un referente y la salida hereda su look.  
**Instalación:** Clonar el repo en `custom_nodes/` de ComfyUI (o instalarlo desde ComfyUI Manager) y colocar los modelos IPAdapter y los pesos de CLIP vision en `models/`. Requiere ComfyUI con GPU.  
**Elige si:** trabajas en ComfyUI y necesitas consistencia visual por referencia — **Evita si:** no usas ComfyUI o te basta con prompts de estilo  
**Combina con:** [ComfyUI](human/fichas/comfyui.md)  
**Más:** [ficha completa](human/fichas/comfyui-ipadapter-plus.md) · [GitHub](https://github.com/cubiq/ComfyUI_IPAdapter_plus)

### Restauración, upscaling y edición

#### 🩹 rembg ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 25.4k  
**Qué es:** Elimina fondos de fotos de producto o retratos con modelos como U2Net o BiRefNet.  
**Instalación:** `pip install "rembg[cpu,cli]"` y `rembg i entrada.png salida.png`.  
**Elige si:** necesitas quitar fondos en local — **Evita si:** necesitas segmentar objetos específicos; mira `sam2`  
**Combina con:** [ComfyUI](human/fichas/comfyui.md)  
**Más:** [ficha completa](human/fichas/rembg.md) · [GitHub](https://github.com/danielgatis/rembg)

#### 🙂 GFPGAN
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 37.7k  
**Qué es:** Resuelve el problema concreto de las caras "fundidas" que aparecen al reescalar o comprimir fotos.  
**Instalación:** `pip install gfpgan` o `git clone` con sus dependencias; los pesos del modelo se descargan en el primer uso. En Windows puede necesitar compilación de extensiones de CUDA.  
**Elige si:** restauras rostros borrosos o fundidos — **Evita si:** necesitas upscaling general de la imagen (Real-ESRGAN)  
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)  
**Más:** [ficha completa](human/fichas/gfpgan.md) · [GitHub](https://github.com/TencentARC/GFPGAN)

#### 🔍 Real-ESRGAN
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 37.4k  
**Qué es:** A diferencia de los upscalers bicúbicos, infiere detalle plausible al ampliar.  
**Instalación:** `pip install realesrgan` o ejecutable portable; los modelos preentrenados se descargan al primer uso. GPU recomendada (también hay build CPU).  
**Elige si:** reescalas imágenes o video a más resolución — **Evita si:** solo necesitas arreglar rostros (GFPGAN) o buscas difusión para reimaginar  
**Combina con:** [GFPGAN](human/fichas/gfpgan.md)  
**Más:** [ficha completa](human/fichas/real-esrgan.md) · [GitHub](https://github.com/xinntao/Real-ESRGAN)

#### 🩹 CodeFormer
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 18.2k  
**Qué es:** Recupera detalles de caras en fotos de baja calidad con buena fidelidad.  
**Instalación:** Clona el repo, `pip install -r requirements.txt` y ejecuta `inference_codeformer.py`.  
**Elige si:** quieres restaurar rostros — **Evita si:** quieres escalar la imagen completa; mira `real-esrgan`  
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)  
**Más:** [ficha completa](human/fichas/codeformer.md) · [GitHub](https://github.com/sczhou/CodeFormer)

### Rostros y retratos animados

#### 🎭 Deep-Live-Cam ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 97.9k  
**Qué es:** Convierte un cambio de rostro, que normalmente requiere pipeline complejo, en un flujo de "un clic".  
**Instalación:** `git clone`, instalar dependencias y proveedores de GPU (p. ej. ONNX Runtime con CUDA Execution Provider); descargar los modelos de swap indicados. Requiere GPU NVIDIA para tiempo real fluido.  
**Elige si:** necesitas swap en vivo legítimo con consentimiento — **Evita si:** no puedes garantizar uso ético/consentimiento o no tienes GPU  
**Combina con:** [face_recognition](human/fichas/face-recognition.md)  
**Más:** [ficha completa](human/fichas/deep-live-cam.md) · [GitHub](https://github.com/hacksider/Deep-Live-Cam)

#### 👤 face_recognition
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 56.9k  
**Qué es:** Envuelve dlib para que el reconocimiento facial sea trivial desde un script.  
**Instalación:** `pip install face_recognition` (requiere dlib y, en Windows, herramientas de compilación de C++/CMake). El modelo CNN para mayor precisión necesita GPU.  
**Elige si:** necesitas reconocimiento facial básico y rápido de implementar — **Evita si:** buscas restauración/animación (GFPGAN/LivePortrait) o precisión de producción (mejor DeepFace/InsightFace)  
**Combina con:** [Deep-Live-Cam](human/fichas/deep-live-cam.md)  
**Más:** [ficha completa](human/fichas/face-recognition.md) · [GitHub](https://github.com/ageitgey/face_recognition)

#### 🙂 FaceFusion
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 30.6k  
**Qué es:** Herramienta líder para face swap, mejora facial y sincronía labial, con controles de uso responsable.  
**Instalación:** Sigue el instalador del README (requiere Python, ffmpeg y opcionalmente GPU).  
**Elige si:** necesitas manipulación facial de calidad con consentimiento — **Evita si:** no tienes consentimiento de las personas  
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)  
**Más:** [ficha completa](human/fichas/facefusion.md) · [GitHub](https://github.com/facefusion/facefusion)

#### 🙂 InsightFace
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 30.2k  
**Qué es:** Base de muchas herramientas faciales; ofrece modelos de reconocimiento de última generación.  
**Instalación:** `pip install insightface onnxruntime`.  
**Elige si:** necesitas reconocimiento facial preciso — **Evita si:** solo quieres detectar caras simples; mira `opencv`  
**Combina con:** [FaceFusion](human/fichas/facefusion.md)  
**Más:** [ficha completa](human/fichas/insightface.md) · [GitHub](https://github.com/deepinsight/insightface)

#### 🧑 LivePortrait
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 19.4k  
**Qué es:** Convierte una foto en un avatar que sigue las expresiones de un "conductor".  
**Instalación:** `git clone`, crear entorno y `pip install -r requirements.txt`; descargar los pesos preentrenados indicados en el repo. Requiere GPU NVIDIA con VRAM generosa.  
**Elige si:** animas retratos a partir de una foto — **Evita si:** necesitas swap en vivo (Deep-Live-Cam) o no tienes GPU  
**Combina con:** [MoviePy](human/fichas/moviepy.md)  
**Más:** [ficha completa](human/fichas/liveportrait.md) · [GitHub](https://github.com/KlingAIResearch/LivePortrait)

### Visión por computador

#### 👁️ Ultralytics YOLO ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 63.3k  
**Qué es:** Entrena un detector con tus datos en pocas líneas y expórtalo a ONNX, TensorRT o móvil.  
**Instalación:** `pip install ultralytics` y `yolo predict model=yolo11n.pt source=imagen.jpg`.  
**Elige si:** necesitas detección de objetos práctica — **Evita si:** necesitas licencia permisiva para producto cerrado; revisa su licencia  
**Combina con:** [supervision](human/fichas/supervision.md) · [Label Studio](human/fichas/label-studio.md)  
**Más:** [ficha completa](human/fichas/ultralytics.md) · [GitHub](https://github.com/ultralytics/ultralytics)

#### 👁️ SAM 2 ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 20.1k  
**Qué es:** Marca un objeto en un fotograma y SAM 2 lo sigue en todo el video. Más rápido que SAM en imágenes.  
**Instalación:** Clona el repo, `pip install -e .` y descarga los checkpoints.  
**Elige si:** necesitas segmentar objetos en video — **Evita si:** solo trabajas con imágenes sueltas; `segment-anything` basta  
**Combina con:** [Label Studio](human/fichas/label-studio.md) · [supervision](human/fichas/supervision.md)  
**Más:** [ficha completa](human/fichas/sam2.md) · [GitHub](https://github.com/facebookresearch/sam2)

#### 👁️ OpenCV
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 91.5k  
**Qué es:** Procesamiento de imagen y video, detección, calibración de cámaras y más, en C++ y Python.  
**Instalación:** `pip install opencv-python`.  
**Elige si:** necesitas procesamiento de imagen o video — **Evita si:** necesitas detección de objetos moderna; mira `ultralytics`  
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [supervision](human/fichas/supervision.md)  
**Más:** [ficha completa](human/fichas/opencv.md) · [GitHub](https://github.com/opencv/opencv)

#### 👁️ Segment Anything (SAM)
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 55.1k  
**Qué es:** Genera máscaras precisas sin entrenamiento para el objeto que indiques. Su sucesor SAM 2 añade video.  
**Instalación:** `pip install git+https://github.com/facebookresearch/segment-anything.git` y descarga un checkpoint.  
**Elige si:** necesitas segmentar objetos en imágenes — **Evita si:** trabajas con video; mira `sam2`  
**Combina con:** [Label Studio](human/fichas/label-studio.md)  
**Más:** [ficha completa](human/fichas/segment-anything.md) · [GitHub](https://github.com/facebookresearch/segment-anything)

#### 👁️ supervision
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 51.6k  
**Qué es:** Se conecta a cualquier detector y te da utilidades para dibujar, contar en zonas, seguir objetos y evaluar.  
**Instalación:** `pip install supervision`.  
**Elige si:** construyes un proyecto de visión con detectores — **Evita si:** solo necesitas procesar imágenes; mira `opencv`  
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [OpenCV](human/fichas/opencv.md)  
**Más:** [ficha completa](human/fichas/supervision.md) · [GitHub](https://github.com/roboflow/supervision)

#### 👁️ Label Studio
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 28.7k  
**Qué es:** Crea datasets para entrenar o evaluar modelos con interfaces de anotación configurables y preetiquetado con IA.  
**Instalación:** `pip install label-studio` y `label-studio start`, o `docker run -p 8080:8080 heartexlabs/label-studio`.  
**Elige si:** necesitas crear datasets etiquetados — **Evita si:** solo evalúas prompts; mira `promptfoo`  
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [SAM 2](human/fichas/sam2.md)  
**Más:** [ficha completa](human/fichas/label-studio.md) · [GitHub](https://github.com/HumanSignal/label-studio)

### Suites generativas todo-en-uno

#### 🎬 Open-Generative-AI ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 33.8k  
**Qué es:** Centraliza la generación visual sin filtros restrictivos ni suscripción.  
**Instalación:** `git clone` del repo e instalar dependencias de Python/Node.js; configurar la clave de MuAPI (render en nube) o el backend de GPU local. Sin clave, solo queda la vía local con GPU.  
**Elige si:** quieres un hub de generación multi-modal sin atarte a un SaaS — **Evita si:** ya tienes tu pipeline local (ComfyUI) o necesitas control fino por nodo  
**Combina con:** [remotion](human/fichas/remotion.md)  
**Más:** [ficha completa](human/fichas/open-generative-ai.md) · [GitHub](https://github.com/Anil-matcha/Open-Generative-AI)

---

## 🎬 12. Audio, Voz & Video

Transcripción, síntesis y clonación de voz, agentes de voz, edición y subtítulos, video programático, video generativo y música.

**⚖️ ¿Cuál elegir? — whisper.cpp, whisper, faster-whisper**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [whisper.cpp](human/fichas/whisper-cpp.md) | quieres transcribir en local sin GPU | necesitas marcas de tiempo por palabra y diarización; mira `whisperx` |
| [whisper](human/fichas/whisper.md) | quieres la referencia robusta y no te obsesiona la latencia | necesitas más velocidad (faster-whisper) o timings por palabra (whisperX) |
| [faster-whisper](human/fichas/faster-whisper.md) | el rendimiento, la memoria o el coste de GPU importan | necesitas alineación/diarización (whisperX) o te basta el CLI oficial |

**⚖️ ¿Cuál elegir? — whisperX, NVIDIA NeMo Speech**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [whisperX](human/fichas/whisperx.md) | necesitas subtítulos precisos o diarización | te basta texto plano (whisper) o no quieres gestionar tokens de HF |
| [NVIDIA NeMo Speech](human/fichas/nemo.md) | necesitas ASR de máxima precisión y tienes GPU | quieres algo simple; mira `faster-whisper` |

**⚖️ ¿Cuál elegir? — Kokoro, GPT-SoVITS, TTS, Fish Speech, Chatterbox, IndexTTS, CosyVoice**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Kokoro](human/fichas/kokoro.md) | quieres TTS ligero, rápido y con licencia permisiva | necesitas clonar voces; mira `chatterbox` |
| [GPT-SoVITS](human/fichas/gpt-sovits.md) | quieres entrenar una voz con pocos datos | prefieres zero-shot sin entrenar; mira `chatterbox` |
| [TTS](human/fichas/tts.md) | quieres flexibilidad y varios modelos en una librería | necesitas tiempo real puro (supertonic) o soporte comercial (Coqui está inactivo) |
| [Fish Speech](human/fichas/fish-speech.md) | buscas TTS de alta calidad con clonación | necesitas licencia comercial sin restricciones; mira `chatterbox` |
| [Chatterbox](human/fichas/chatterbox.md) | quieres clonar voces con calidad alta y licencia libre | necesitas algo muy ligero en CPU; mira `kokoro` |
| [IndexTTS](human/fichas/index-tts.md) | necesitas controlar duración y emoción de la voz | buscas licencia totalmente libre; revisa su licencia |
| [CosyVoice](human/fichas/cosyvoice.md) | necesitas TTS multilingüe en streaming | quieres instalación muy simple; mira `kokoro` |

**⚖️ ¿Cuál elegir? — OmniVoice-Studio, VideoLingo**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OmniVoice-Studio](human/fichas/omnivoice-studio.md) | quieres suite de voz completa local (dictado + clonación + dubbing) | solo necesitas TTS simple por CLI/librería (TTS) o estabilidad de producción |
| [VideoLingo](human/fichas/videolingo.md) | quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar | solo necesitas transcribir o subtitular en el idioma original; te basta `whisperx` o `faster-whisper` |

**⚖️ ¿Cuál elegir? — Pipecat, LiveKit Agents**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Pipecat](human/fichas/pipecat.md) | construyes un agente de voz en Python | quieres infraestructura WebRTC gestionada; mira `livekit-agents` |
| [LiveKit Agents](human/fichas/livekit-agents.md) | necesitas agentes de voz escalables con WebRTC | quieres algo ligero sin servidor de medios; mira `pipecat` |

**⚖️ ¿Cuál elegir? — HyperFrames, MoviePy, remotion**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [HyperFrames](human/fichas/hyperframes.md) | quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva | tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual |
| [MoviePy](human/fichas/moviepy.md) | ensamblas video desde Python y quieres controlar cada clip por código | prefieres plantillas en React (`remotion`) o en HTML (`hyperframes`), o solo necesitas cortar sin recodificar (`lossless-cut`) |
| [remotion](human/fichas/remotion.md) | generas video a escala con React y quieres variantes parametrizadas | trabajas en Python (moviepy) o buscas un editor visual |

**⚖️ ¿Cuál elegir? — OBS Studio, OpenScreen**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OBS Studio](human/fichas/obs-studio.md) | necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas | lo que necesitas es montar o recortar el video ya grabado; usa `opencut` o `lossless-cut` |
| [OpenScreen](human/fichas/openscreen.md) | quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio | necesitas un proyecto mantenido; usa su continuación getopenscreen/openscreen, o `obs-studio` para grabación y streaming generales |

**⚖️ ¿Cuál elegir? — MoneyPrinterTurbo, video-use, videofy_minimal, Remotion Superpowers, OpenMontage**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [MoneyPrinterTurbo](human/fichas/moneyprinterturbo.md) | quieres producir videos cortos narrados a partir de un tema sin editar a mano | necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage` |
| [video-use](human/fichas/video-use.md) | quieres editar videos pidiéndoselo a tu agente | quieres una app de edición visual; mira `opencut` |
| [videofy_minimal](human/fichas/videofy-minimal.md) | quieres reels simples ya, sin montar un pipeline entero | necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy) |
| [Remotion Superpowers](human/fichas/remotion-superpowers.md) | usas Remotion con un agente y quieres producción completa | no usas Remotion |
| [OpenMontage](human/fichas/openmontage.md) | quieres producir videos completos con un agente | solo necesitas editar clips; mira `video-use` |

**⚖️ ¿Cuál elegir? — Wan2.2, HunyuanVideo, LTX-Video**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Wan2.2](human/fichas/wan2-2.md) | quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más | tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados |
| [HunyuanVideo](human/fichas/hunyuanvideo.md) | tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente |
| [LTX-Video](human/fichas/ltx-video.md) | necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x | empiezas un proyecto nuevo; Lightricks recomienda LTX-2.5 (repo Lightricks/LTX-2), o mira `wan2-2` y `wan2gp` |

### Transcripción (voz a texto)

#### 🎙️ whisper.cpp ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 55.1k  
**Qué es:** Transcribe voz a texto en local sin Python ni GPU obligatoria, incluso en tiempo real. Base de muchas apps de dictado.  
**Instalación:** `brew install whisper-cpp` o compila con `cmake`; descarga un modelo con el script incluido.  
**Elige si:** quieres transcribir en local sin GPU — **Evita si:** necesitas marcas de tiempo por palabra y diarización; mira `whisperx`  
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)  
**Más:** [ficha completa](human/fichas/whisper-cpp.md) · [GitHub](https://github.com/ggml-org/whisper.cpp)

#### 📝 whisper
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 112k  
**Qué es:** Cubre también identificación de idioma y traducción al inglés en la misma red.  
**Instalación:** `pip install -U openai-whisper` (requiere ffmpeg en el sistema y PyTorch). El modelo se descarga al primer uso según `--model` (de `tiny` a `large`).  
**Elige si:** quieres la referencia robusta y no te obsesiona la latencia — **Evita si:** necesitas más velocidad (faster-whisper) o timings por palabra (whisperX)  
**Combina con:** [whisperX](human/fichas/whisperx.md)  
**Más:** [ficha completa](human/fichas/whisper.md) · [GitHub](https://github.com/openai/whisper)

#### ⚡ faster-whisper
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 26.6k  
**Qué es:** Es el mismo modelo de OpenAI, pero con un runtime de inferencia optimizado.  
**Instalación:** `pip install faster-whisper` (necesita ffmpeg). El modelo se descarga al primer uso; en GPU requiere drivers CUDA compatibles con CTranslate2.  
**Elige si:** el rendimiento, la memoria o el coste de GPU importan — **Evita si:** necesitas alineación/diarización (whisperX) o te basta el CLI oficial  
**Combina con:** [whisperX](human/fichas/whisperx.md)  
**Más:** [ficha completa](human/fichas/faster-whisper.md) · [GitHub](https://github.com/SYSTRAN/faster-whisper)

#### 🎯 whisperX
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 25.2k  
**Qué es:** Convierte la salida "por segmento" de Whisper en timings palabra a palabra con etiqueta de speaker.  
**Instalación:** `pip install whisperx` (requiere PyTorch y, para diarización, un token de Hugging Face con acceso aceptado a los modelos pyannote).  
**Elige si:** necesitas subtítulos precisos o diarización — **Evita si:** te basta texto plano (whisper) o no quieres gestionar tokens de HF  
**Combina con:** [whisper](human/fichas/whisper.md) · [MoviePy](human/fichas/moviepy.md)  
**Más:** [ficha completa](human/fichas/whisperx.md) · [GitHub](https://github.com/m-bain/whisperX)

#### 🎙️ NVIDIA NeMo Speech
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 18.7k  
**Qué es:** Incluye modelos de ASR como Parakeet y Canary, que lideran rankings de transcripción, y herramientas para afinarlos.  
**Instalación:** `pip install "nemo_toolkit[asr]"`.  
**Elige si:** necesitas ASR de máxima precisión y tienes GPU — **Evita si:** quieres algo simple; mira `faster-whisper`  
**Combina con:** [Pipecat](human/fichas/pipecat.md)  
**Más:** [ficha completa](human/fichas/nemo.md) · [GitHub](https://github.com/NVIDIA-NeMo/Speech)

### Síntesis y clonación de voz

#### 🗣️ Kokoro ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 10k  
**Qué es:** Voces naturales en varios idiomas, incluido el español, rápido incluso en CPU.  
**Instalación:** `pip install kokoro soundfile` (requiere espeak-ng).  
**Elige si:** quieres TTS ligero, rápido y con licencia permisiva — **Evita si:** necesitas clonar voces; mira `chatterbox`  
**Combina con:** [Pipecat](human/fichas/pipecat.md) · [whisper.cpp](human/fichas/whisper-cpp.md)  
**Más:** [ficha completa](human/fichas/kokoro.md) · [GitHub](https://github.com/hexgrad/kokoro)

#### 🎚️ OmniVoice-Studio
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 107k  
**Qué es:** Reúne STT, TTS y dubbing en una sola app sin claves de API.  
**Instalación:** Clonar el repo e instalar dependencias Python según el README (sin paquete publicado); el README recomienda correr desde fuente por estar en beta.  
**Elige si:** quieres suite de voz completa local (dictado + clonación + dubbing) — **Evita si:** solo necesitas TTS simple por CLI/librería (TTS) o estabilidad de producción  
**Combina con:** [whisperX](human/fichas/whisperx.md)  
**Más:** [ficha completa](human/fichas/omnivoice-studio.md) · [GitHub](https://github.com/debpalash/VoiceStudio)

#### 🗣️ GPT-SoVITS
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 64.7k  
**Qué es:** Entrena una voz con muy pocos datos y sintetiza en varios idiomas. Muy popular entre creadores.  
**Instalación:** Descarga el paquete integrado de releases o sigue la instalación del README.  
**Elige si:** quieres entrenar una voz con pocos datos — **Evita si:** prefieres zero-shot sin entrenar; mira `chatterbox`  
**Combina con:** [RVC WebUI](human/fichas/rvc.md)  
**Más:** [ficha completa](human/fichas/gpt-sovits.md) · [GitHub](https://github.com/RVC-Boss/GPT-SoVITS)

#### 🗣️ VibeVoice
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 56.9k  
**Qué es:** Genera conversaciones de hasta 90 minutos con cuatro voces distintas, y tiene variantes de baja latencia.  
**Instalación:** Clona el repo, `pip install -e .` y descarga los modelos.  
**Elige si:** quieres generar podcasts o diálogos largos — **Evita si:** solo necesitas frases cortas; mira `kokoro`  
**Combina con:** [open-notebook](human/fichas/open-notebook.md)  
**Más:** [ficha completa](human/fichas/vibevoice.md) · [GitHub](https://github.com/microsoft/VibeVoice)

#### 🎙️ TTS
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 46.2k  
**Qué es:** Reúne en una sola librería modelos como Tacotron, VITS y XTTS, con CLI y API Python.  
**Instalación:** `pip install TTS` (o `coqui-tts`, el fork mantenido). Requiere PyTorch; la clonación con XTTS mejora con GPU.  
**Elige si:** quieres flexibilidad y varios modelos en una librería — **Evita si:** necesitas tiempo real puro (supertonic) o soporte comercial (Coqui está inactivo)  
**Combina con:** [whisperX](human/fichas/whisperx.md) · [MoviePy](human/fichas/moviepy.md)  
**Más:** [ficha completa](human/fichas/tts.md) · [GitHub](https://github.com/coqui-ai/TTS)

#### 🗣️ VoxCPM
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 42.2k  
**Qué es:** Pertenece a la familia CPM de modelos generativos de OpenBMB.  
**Instalación:** `pip install voxcpm` (o desde el repo) con PyTorch y GPU recomendada; los pesos se descargan al instanciar el modelo.  
**Elige si:** quieres voz muy natural o clonada y tienes GPU — **Evita si:** priorizas latencia mínima (supertonic) o no tienes GPU  
**Combina con:** [TTS](human/fichas/tts.md)  
**Más:** [ficha completa](human/fichas/voxcpm.md) · [GitHub](https://github.com/OpenBMB/VoxCPM)

#### 🗣️ RVC WebUI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 39.1k  
**Qué es:** Cambia la voz de una grabación manteniendo entonación. Muy usado para covers y doblaje.  
**Instalación:** Descarga el paquete de releases o instala con `pip` siguiendo el README.  
**Elige si:** quieres convertir una voz grabada en otra — **Evita si:** necesitas generar voz desde texto; mira `chatterbox`  
**Combina con:** [GPT-SoVITS](human/fichas/gpt-sovits.md)  
**Más:** [ficha completa](human/fichas/rvc.md) · [GitHub](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

#### 🗣️ Fish Speech
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 33.7k  
**Qué es:** Clona voces con pocos segundos de audio y genera habla natural en muchos idiomas.  
**Instalación:** Sigue el README (instalación con `pip` o Docker y descarga de pesos).  
**Elige si:** buscas TTS de alta calidad con clonación — **Evita si:** necesitas licencia comercial sin restricciones; mira `chatterbox`  
**Más:** [ficha completa](human/fichas/fish-speech.md) · [GitHub](https://github.com/fishaudio/fish-speech)

#### 🗣️ Chatterbox
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 27.7k  
**Qué es:** Clona una voz con unos segundos de audio y ajusta la expresividad. Multilingüe y con marca de agua.  
**Instalación:** `pip install chatterbox-tts`.  
**Elige si:** quieres clonar voces con calidad alta y licencia libre — **Evita si:** necesitas algo muy ligero en CPU; mira `kokoro`  
**Combina con:** [Pipecat](human/fichas/pipecat.md)  
**Más:** [ficha completa](human/fichas/chatterbox.md) · [GitHub](https://github.com/resemble-ai/chatterbox)

#### 🗣️ IndexTTS
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 25k  
**Qué es:** Clona voces sin entrenar y permite controlar la duración exacta, útil para doblaje.  
**Instalación:** Clona el repo e instala con `uv sync`, luego descarga los modelos.  
**Elige si:** necesitas controlar duración y emoción de la voz — **Evita si:** buscas licencia totalmente libre; revisa su licencia  
**Más:** [ficha completa](human/fichas/index-tts.md) · [GitHub](https://github.com/index-tts/index-tts)

#### 🗣️ CosyVoice
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 24.4k  
**Qué es:** Síntesis de voz natural con clonación y control de estilo, también en streaming.  
**Instalación:** Clona el repo, instala dependencias con conda y descarga los modelos.  
**Elige si:** necesitas TTS multilingüe en streaming — **Evita si:** quieres instalación muy simple; mira `kokoro`  
**Combina con:** [Pipecat](human/fichas/pipecat.md)  
**Más:** [ficha completa](human/fichas/cosyvoice.md) · [GitHub](https://github.com/QwenAudio/CosyVoice)

#### 🔊 supertonic
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 13.8k  
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.  
**Qué es:** Apunta a latencia mínima con privacidad total, sin nube ni llamadas de API.  
**Instalación:** Clonar el repo y seguir el ejemplo Node/Python, o probar la demo WebGPU (no hay paquete único oficial). Requiere un navegador/entorno con WebGPU o runtime ONNX adecuado.  
**Elige si:** quieres voz local en tiempo real y sin nube — **Evita si:** priorizas clonación de máxima fidelidad (VoxCPM) o flexibilidad multi-modelo (TTS)  
**Combina con:** [whisperX](human/fichas/whisperx.md) · [MoviePy](human/fichas/moviepy.md)  
**Más:** [ficha completa](human/fichas/supertonic.md) · [GitHub](https://github.com/supertone-oss-archive/supertonic)

#### 🗣️ LuxTTS
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 5.5k  
**Qué es:** Basado en ZipVoice, pensado para clonación rápida y realista con pocos recursos.  
**Instalación:** Sigue el README para instalar y descargar el modelo.  
**Elige si:** necesitas TTS con clonación muy rápido — **Evita si:** buscas el proyecto más maduro; mira `chatterbox`  
**Combina con:** [litellm](human/fichas/litellm.md) · [cosmos](human/fichas/cosmos.md) · [ComfyUI](human/fichas/comfyui.md)  
**Más:** [ficha completa](human/fichas/luxtts.md) · [GitHub](https://github.com/ysharma3501/LuxTTS)

### Agentes de voz en tiempo real

#### 📞 Pipecat ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 17.2k  
**Qué es:** Encadena STT, LLM y TTS con interrupciones y baja latencia, y conecta con teléfono, WebRTC o WhatsApp.  
**Instalación:** `pip install "pipecat-ai[daily,openai,cartesia]"` según tus proveedores.  
**Elige si:** construyes un agente de voz en Python — **Evita si:** quieres infraestructura WebRTC gestionada; mira `livekit-agents`  
**Combina con:** [Kokoro](human/fichas/kokoro.md) · [whisper.cpp](human/fichas/whisper-cpp.md)  
**Más:** [ficha completa](human/fichas/pipecat.md) · [GitHub](https://github.com/pipecat-ai/pipecat)

#### 📞 LiveKit Agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 15.2k  
**Qué es:** Construye agentes que hablan, escuchan y ven, con detección de turnos y telefonía, desplegables a escala.  
**Instalación:** `pip install "livekit-agents[openai,silero,deepgram]"`.  
**Elige si:** necesitas agentes de voz escalables con WebRTC — **Evita si:** quieres algo ligero sin servidor de medios; mira `pipecat`  
**Combina con:** [Kokoro](human/fichas/kokoro.md)  
**Más:** [ficha completa](human/fichas/livekit-agents.md) · [GitHub](https://github.com/livekit/agents)

### Edición, grabación y subtítulos

#### ✂️ FFmpeg ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 66.9k  
**Qué es:** FFmpeg es la base multimedia sobre la que se apoyan casi todos los editores, reproductores y pipelines de video. Incluye el CLI `ffmpeg` para convertir, recortar, concatenar, mezclar, quemar subtítulos y transmitir, `ffprobe` para inspeccionar archivos y las librerías libav* para integrarlo en tu propio software.  
**Instalación:** `brew install ffmpeg` (macOS) o `sudo apt install ffmpeg` (Linux); en Windows, descarga un binario desde ffmpeg.org.  
**Elige si:** necesitas convertir, cortar, mezclar o transmitir audio y video desde la línea de comandos o un script — **Evita si:** quieres una interfaz gráfica para cortar sin pérdida (`lossless-cut`) o componer video desde Python con objetos (`moviepy`)  
**Combina con:** [whisper](human/fichas/whisper.md) · [yt-dlp](human/fichas/yt-dlp.md) · [MoviePy](human/fichas/moviepy.md)  
**Más:** [ficha completa](human/fichas/ffmpeg.md) · [GitHub](https://github.com/FFmpeg/FFmpeg)

#### 🎬 MoviePy ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 15.1k  
**Qué es:** MoviePy convierte la edición de video en código Python: abres clips, los recortas, superpones texto o imágenes, mezclas audio y exportas a MP4, WebM o GIF. Es la pieza de ensamblaje habitual en pipelines que generan videos cortos a partir de imágenes, voz sintética y subtítulos.  
**Instalación:** `pip install moviepy` (Python 3.9+; trae FFmpeg mediante imageio-ffmpeg).  
**Elige si:** ensamblas video desde Python y quieres controlar cada clip por código — **Evita si:** prefieres plantillas en React (`remotion`) o en HTML (`hyperframes`), o solo necesitas cortar sin recodificar (`lossless-cut`)  
**Combina con:** [whisperX](human/fichas/whisperx.md) · [Kokoro](human/fichas/kokoro.md) · [ComfyUI](human/fichas/comfyui.md)  
**Más:** [ficha completa](human/fichas/moviepy.md) · [GitHub](https://github.com/Zulko/moviepy)

#### 🎞️ OpenCut
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 98k  
**Qué es:** OpenCut es un editor de video pensado como alternativa abierta a CapCut: privado (los videos no salen de tu dispositivo), sin funciones de pago y fácil de usar. Hoy se usa la versión clásica en opencut.app mientras el equipo reescribe el proyecto desde cero, con un núcleo en Rust para web, escritorio y móvil.  
**Instalación:** Úsalo directamente en opencut.app (versión clásica). Para la reescritura: instala proto, ejecuta `proto use` y `moon run web:dev`; la versión clásica se auto-hospeda con `docker compose up -d`.  
**Elige si:** quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut — **Evita si:** necesitas estabilidad o automatización hoy; para montar por código mira `moviepy` o `remotion`, y para cortes sin pérdida `lossless-cut`  
**Combina con:** [LosslessCut](human/fichas/lossless-cut.md) · [OBS Studio](human/fichas/obs-studio.md) · [whisperX](human/fichas/whisperx.md)  
**Más:** [ficha completa](human/fichas/opencut.md) · [GitHub](https://github.com/OpenCut-app/OpenCut)

#### ✂️ OBS Studio
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 79.3k  
**Qué es:** OBS Studio captura, compone, codifica, graba y transmite video en Windows, macOS y Linux. Combinas en escenas la pantalla, ventanas, webcam, navegador y archivos multimedia, mezclas el audio con filtros y emites a YouTube, Twitch u otro servicio RTMP, o grabas a disco.  
**Instalación:** Instalador oficial en obsproject.com; también `brew install --cask obs` (macOS), `winget install OBSProject.OBSStudio` (Windows) o `flatpak install flathub com.obsproject.Studio` (Linux).  
**Elige si:** necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas — **Evita si:** lo que necesitas es montar o recortar el video ya grabado; usa `opencut` o `lossless-cut`  
**Combina con:** [LosslessCut](human/fichas/lossless-cut.md) · [OpenCut](human/fichas/opencut.md) · [faster-whisper](human/fichas/faster-whisper.md)  
**Más:** [ficha completa](human/fichas/obs-studio.md) · [GitHub](https://github.com/obsproject/obs-studio)

#### ✂️ LosslessCut
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 45.9k  
**Qué es:** LosslessCut es una interfaz gráfica sobre FFmpeg para recortar y fusionar archivos de video y audio sin recompresión. Sirve para descartar gigas de material de cámara, GoPro o dron, extraer o reemplazar pistas, cambiar de contenedor (MKV a MP4) y editar metadatos o capítulos, en Windows, macOS y Linux.  
**Instalación:** Descarga gratis el binario para Windows, macOS o Linux desde GitHub Releases, o instálalo desde Mac App Store, Microsoft Store o Snap Store. Ya incluye FFmpeg.  
**Elige si:** necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica — **Evita si:** necesitas efectos, transiciones o un montaje con capas; mira `opencut` o, por código, `moviepy`  
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md) · [whisperX](human/fichas/whisperx.md) · [MoviePy](human/fichas/moviepy.md)  
**Más:** [ficha completa](human/fichas/lossless-cut.md) · [GitHub](https://github.com/mifi/lossless-cut)

#### 🖥️ OpenScreen
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 40k  
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.  
**Qué es:** OpenScreen graba una ventana o la pantalla completa con micrófono y audio del sistema, y después te deja pulir la demo: zooms que siguen al cursor, webcam superpuesta, fondos, anotaciones, recorte y velocidad por tramo. Exporta a MP4 o GIF en varias proporciones. El proyecto original está archivado; su continuación activa es getopenscreen/openscreen.  
**Instalación:** Descarga el instalador desde GitHub Releases, o usa `brew install --cask siddharthvaddem/openscreen/openscreen` (macOS) o `winget install SiddharthVaddem.OpenScreen` (Windows).  
**Elige si:** quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio — **Evita si:** necesitas un proyecto mantenido; usa su continuación getopenscreen/openscreen, o `obs-studio` para grabación y streaming generales  
**Combina con:** [LosslessCut](human/fichas/lossless-cut.md) · [OpenCut](human/fichas/opencut.md)  
**Más:** [ficha completa](human/fichas/openscreen.md) · [GitHub](https://github.com/siddharthvaddem/openscreen)

#### ✂️ VideoLingo
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 19.1k  
**Qué es:** VideoLingo reúne en una interfaz Streamlit el trabajo de un equipo de subtitulado: descarga el video con yt-dlp, lo transcribe con alineación por palabra, segmenta y traduce los subtítulos con un LLM y, si quieres, genera el doblaje con voz sintética o clonada. Produce archivos SRT y videos subtitulados o doblados.  
**Instalación:** `git clone https://github.com/Huanshere/VideoLingo.git && cd VideoLingo && uv run start.py` (en Windows, `OneKeyStart.bat`). Luego configura URL, clave y modelo del LLM en la barra lateral.  
**Elige si:** quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar — **Evita si:** solo necesitas transcribir o subtitular en el idioma original; te basta `whisperx` o `faster-whisper`  
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md) · [GPT-SoVITS](human/fichas/gpt-sovits.md) · [whisperX](human/fichas/whisperx.md)  
**Más:** [ficha completa](human/fichas/videolingo.md) · [GitHub](https://github.com/Huanshere/VideoLingo)

#### ✂️ DaVinci Resolve MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 4k  
**Qué es:** Expone la API oficial de scripting de DaVinci Resolve como herramientas MCP para Claude, Cursor, Codex y otros clientes. Cubre montaje, organización del media pool, render, marcadores, color, Fusion y Fairlight, y añade análisis de medios que nunca modifica los originales. Incluye un panel de control local en el navegador.  
**Instalación:** `npx davinci-resolve-mcp setup` (o `git clone` y `python install.py`). Antes, en Resolve Studio pon Preferences > General > External scripting using en Local.  
**Elige si:** editas en DaVinci Resolve y quieres que un agente MCP automatice montaje, render o metadatos — **Evita si:** no usas Resolve o prefieres montar video por código sin editor; mira `moviepy` o `ffmpeg`  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [FFmpeg](human/fichas/ffmpeg.md) · [whisper](human/fichas/whisper.md)  
**Más:** [ficha completa](human/fichas/davinci-resolve-mcp.md) · [GitHub](https://github.com/samuelgursky/davinci-resolve-mcp)

### Video programático y con agentes

#### 🎞️ HyperFrames ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 82k  
**Qué es:** HyperFrames define cada video como un archivo HTML con atributos de tiempo y pistas, animado con GSAP, CSS, Lottie, Three.js u otras librerías, y lo renderiza a MP4. Incluye CLI para crear, previsualizar y renderizar, un catálogo de unos 450 bloques (transiciones, subtítulos, gráficos, mapas) y skills para que Claude Code, Codex o Cursor produzcan videos a partir de una petición.  
**Instalación:** `npx hyperframes init my-video`, luego `npx hyperframes preview` y `npx hyperframes render` (Node.js 22+ y FFmpeg). Para agentes: `npx hyperframes skills update`, o en Claude Code `claude plugin marketplace add heygen-com/hyperframes` y `claude plugin install hyperframes@hyperframes`.  
**Elige si:** quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva — **Evita si:** tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [GSAP](human/fichas/gsap.md) · [Kokoro](human/fichas/kokoro.md) · [whisperX](human/fichas/whisperx.md)  
**Más:** [ficha completa](human/fichas/hyperframes.md) · [GitHub](https://github.com/heygen-com/hyperframes)

#### 🎞️ Remotion Agent Skills ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 6.8k  
**Qué es:** Enseñan al agente las buenas prácticas de Remotion: composiciones, animaciones, audio y render.  
**Instalación:** `npx skills add remotion-dev/skills` o copia a la carpeta de skills de tu agente.  
**Elige si:** haces videos con Remotion y un agente — **Evita si:** no usas Remotion  
**Combina con:** [remotion](human/fichas/remotion.md) · [Remotion Superpowers](human/fichas/remotion-superpowers.md)  
**Más:** [ficha completa](human/fichas/skills-remotion.md) · [GitHub](https://github.com/remotion-dev/skills)

#### 🎞️ Manim (ManimGL)
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 96.3k  
**Qué es:** Manim permite describir en código Python escenas con fórmulas LaTeX, gráficas, geometría y transformaciones animadas, y exportarlas a video. Este repo es ManimGL, la versión original que Grant Sanderson usa en 3Blue1Brown; la edición comunitaria (ManimCommunity/manim) es un fork más estable y mejor documentado.  
**Instalación:** `pip install manimgl` (Python 3.10+, con FFmpeg, OpenGL y, si quieres fórmulas, LaTeX; en Linux también Pango). Prueba con `manimgl example_scenes.py OpeningManimExample`.  
**Elige si:** quieres animaciones matemáticas o técnicas precisas definidas en código Python — **Evita si:** buscas estabilidad y documentación para empezar (usa la edición comunitaria ManimCommunity/manim) o motion graphics de marketing; mira `remotion` o `hyperframes`  
**Combina con:** [Kokoro](human/fichas/kokoro.md) · [MoviePy](human/fichas/moviepy.md) · [FFmpeg](human/fichas/ffmpeg.md)  
**Más:** [ficha completa](human/fichas/manim.md) · [GitHub](https://github.com/3b1b/manim)

#### ⚛️ remotion
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 72.2k  
**Qué es:** Convierte el video en un artefacto versionable y parametrizable desde tu código frontend.  
**Instalación:** `npm create video` (o `npm i remotion @remotion/cli`). Requiere Node y Chromium para render; el render final usa ffmpeg.  
**Elige si:** generas video a escala con React y quieres variantes parametrizadas — **Evita si:** trabajas en Python (moviepy) o buscas un editor visual  
**Combina con:** [Open-Generative-AI](human/fichas/open-generative-ai.md)  
**Más:** [ficha completa](human/fichas/remotion.md) · [GitHub](https://github.com/remotion-dev/remotion)

#### 🎞️ video-use
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 30.8k  
**Qué es:** El agente corta, une, subtitula y ajusta videos a partir de instrucciones en lenguaje natural.  
**Instalación:** Sigue el README para instalarlo y conectarlo a tu agente.  
**Elige si:** quieres editar videos pidiéndoselo a tu agente — **Evita si:** quieres una app de edición visual; mira `opencut`  
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md) · [Claude Code](human/fichas/claude-code.md)  
**Más:** [ficha completa](human/fichas/video-use.md) · [GitHub](https://github.com/browser-use/video-use)

#### 📲 videofy_minimal
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 656  
**Qué es:** Encadena TTS/STT y montaje en un solo flujo para pasar de texto a reel con lo mínimo.  
**Instalación:** Clonar el repo e instalar dependencias Python/Node según el README (sin paquete publicado). Requiere los modelos TTS/STT que el proyecto utilice.  
**Elige si:** quieres reels simples ya, sin montar un pipeline entero — **Evita si:** necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy)  
**Combina con:** [whisper](human/fichas/whisper.md) · [supertonic](human/fichas/supertonic.md)  
**Más:** [ficha completa](human/fichas/videofy-minimal.md) · [GitHub](https://github.com/schibsted/videofy_minimal)

#### 🎞️ Remotion Superpowers
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 164  
**Qué es:** Añade locución con IA, música, footage de stock e imágenes para producir videos en código.  
**Instalación:** Instálalo como plugin de Claude Code o copia las skills siguiendo el README.  
**Elige si:** usas Remotion con un agente y quieres producción completa — **Evita si:** no usas Remotion  
**Combina con:** [remotion](human/fichas/remotion.md) · [Remotion Agent Skills](human/fichas/skills-remotion.md)  
**Más:** [ficha completa](human/fichas/remotion-superpowers.md) · [GitHub](https://github.com/DojoCodingLabs/remotion-superpowers)

#### 🎞️ OpenMontage
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio  
**Qué es:** Describes el video y el agente investiga, escribe el guion, genera recursos y monta el resultado.  
**Instalación:** Sigue el README (el repo original ya no está disponible en GitHub; usa tu clon local).  
**Elige si:** quieres producir videos completos con un agente — **Evita si:** solo necesitas editar clips; mira `video-use`  
**Combina con:** [remotion](human/fichas/remotion.md)  
**Más:** [ficha completa](human/fichas/openmontage.md) · [GitHub](https://github.com/calesthio/OpenMontage.git)

### Video generativo y pipelines automáticos

#### 🎬 MoneyPrinterTurbo ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 142k  
**Qué es:** MoneyPrinterTurbo automatiza la producción de shorts: das un tema o palabras clave y escribe el guion con un LLM, busca clips en Pexels o Pixabay (o usa los tuyos o video generado por IA), genera locución, subtítulos y música, y monta el resultado en 9:16, 16:9 o 1:1. Se usa desde WebUI, API, CLI o pidiéndoselo a un agente con su skill.  
**Instalación:** `pip install mpt` y luego `mpt webui` (Python 3.11+), o `docker compose -f docker-compose.release.yml up`. Añade en la WebUI las claves del LLM y de Pexels o Pixabay.  
**Elige si:** quieres producir videos cortos narrados a partir de un tema sin editar a mano — **Evita si:** necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage`  
**Combina con:** [Ollama](human/fichas/ollama.md) · [Kokoro](human/fichas/kokoro.md) · [faster-whisper](human/fichas/faster-whisper.md)  
**Más:** [ficha completa](human/fichas/moneyprinterturbo.md) · [GitHub](https://github.com/harry0703/MoneyPrinterTurbo)

#### 🎬 Wan2.2 ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 18.5k  
**Qué es:** Wan2.2 publica pesos y código de inferencia de varios modelos de video: texto a video e imagen a video de 14B (MoE), un modelo híbrido de 5B que genera 720p a 24 fps en una RTX 4090, video guiado por voz (S2V) y animación o sustitución de personajes (Animate). Es la base de muchos flujos de ComfyUI y Diffusers.  
**Instalación:** `git clone https://github.com/Wan-Video/Wan2.2.git && cd Wan2.2 && pip install -r requirements.txt` (torch 2.4+); descarga pesos con `huggingface-cli download Wan-AI/Wan2.2-TI2V-5B --local-dir ./Wan2.2-TI2V-5B` y ejecuta `python generate.py --task ti2v-5B`.  
**Elige si:** quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más — **Evita si:** tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados  
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md) · [Real-ESRGAN](human/fichas/real-esrgan.md) · [CosyVoice](human/fichas/cosyvoice.md)  
**Más:** [ficha completa](human/fichas/wan2-2.md) · [GitHub](https://github.com/Wan-Video/Wan2.2)

#### 🎬 HunyuanVideo
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 12.8k  
**Qué es:** HunyuanVideo publica los pesos, la definición en PyTorch y el código de inferencia de un modelo de texto a video de más de 13.000 millones de parámetros, que genera clips de unos 5 segundos (129 fotogramas) en 540p o 720p. Las variantes de imagen a video, avatares guiados por audio y personalización viven en repos aparte.  
**Instalación:** `git clone https://github.com/Tencent-Hunyuan/HunyuanVideo`, entorno conda con Python 3.10, PyTorch con CUDA y `pip install -r requirements.txt`; luego descarga los pesos de Hugging Face (tencent/HunyuanVideo).  
**Elige si:** tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad — **Evita si:** trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente  
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md) · [Real-ESRGAN](human/fichas/real-esrgan.md)  
**Más:** [ficha completa](human/fichas/hunyuanvideo.md) · [GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo)

#### 🎬 LTX-Video
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 11.4k  
**Qué es:** LTX-Video es el repositorio de los modelos v0.9.x de Lightricks, un transformer de difusión (DiT) para texto a video, imagen a video, extensión de clips y video a video con condiciones por fotograma clave. Incluye variantes de 2B y 13B, destiladas y FP8, y LoRAs de control de pose, profundidad y bordes. Ya solo se mantiene como legado: los modelos nuevos están en LTX-2.  
**Instalación:** `git clone https://github.com/Lightricks/LTX-Video.git && cd LTX-Video && python -m pip install -e .[inference]` y después `python inference.py --prompt ...`; para la mejor calidad, el equipo recomienda su flujo de ComfyUI.  
**Elige si:** necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x — **Evita si:** empiezas un proyecto nuevo; Lightricks recomienda LTX-2.5 (repo Lightricks/LTX-2), o mira `wan2-2` y `wan2gp`  
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md) · [Real-ESRGAN](human/fichas/real-esrgan.md)  
**Más:** [ficha completa](human/fichas/ltx-video.md) · [GitHub](https://github.com/Lightricks/LTX-Video)

#### 🎬 WanGP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🔴 pesado  
**Aviso:** ⚠️ El repositorio original ya no está disponible en GitHub; se conserva el clon local.  
**Qué es:** WanGP, antes Wan2GP, es una interfaz web para ejecutar en tu GPU decenas de modelos generativos abiertos: video (Wan 2.1/2.2, LTX-2, Hunyuan Video), imagen (Flux, Qwen Image), voz y música (Chatterbox, Index TTS, Ace Step) y 3D. Añade cola de trabajos, LoRAs, galerías y un asistente local, Deepy, que planifica y lanza las generaciones por ti.  
**Instalación:** Ejecuta `scripts/install.sh` (o `scripts\install.bat` en Windows), o bien `git clone https://github.com/deepbeepmeep/Wan2GP.git`, entorno conda con Python 3.11, PyTorch con CUDA y `pip install -r requirements.txt`; arranca con `python wgp.py`.  
**Elige si:** quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano — **Evita si:** prefieres construir flujos por nodos con control fino (`comfyui`) o tienes una GPU grande y quieres el código oficial (`wan2-2`)  
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [MoviePy](human/fichas/moviepy.md) · [LosslessCut](human/fichas/lossless-cut.md)  
**Más:** [ficha completa](human/fichas/wan2gp.md) · [GitHub](https://github.com/deepbeepmeep/Wan2GP)

### Música y audio generativo

#### 🎵 AudioCraft ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 23.8k  
**Qué es:** AudioCraft reúne el código de inferencia y entrenamiento de los modelos de audio generativo de Meta: MusicGen (música a partir de texto o melodía), AudioGen (efectos de sonido), MAGNeT, JASCO (música condicionada por acordes y batería), el códec neuronal EnCodec y AudioSeal para marcas de agua. Está orientada a investigación, aunque se usa mucho para crear música de fondo.  
**Instalación:** `python -m pip install 'torch==2.1.0'` y luego `python -m pip install -U audiocraft` (Python 3.9). Conviene tener ffmpeg instalado; los modelos se descargan de Hugging Face al primer uso.  
**Elige si:** necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio — **Evita si:** necesitas uso comercial (los pesos son CC-BY-NC 4.0) o generar voz hablada; para voz mira `kokoro` o `chatterbox`  
**Combina con:** [MoviePy](human/fichas/moviepy.md) · [remotion](human/fichas/remotion.md) · [FFmpeg](human/fichas/ffmpeg.md)  
**Más:** [ficha completa](human/fichas/audiocraft.md) · [GitHub](https://github.com/facebookresearch/audiocraft)

---

## 📄 13. Documentos & Presentaciones

Convertir documentos a Markdown/JSON para IA, OCR, herramientas PDF, presentaciones y diagramas.

**⚖️ ¿Cuál elegir? — PaddleOCR, Docling, MinerU, Tesseract, Marker, Unlimited-OCR, olmOCR**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [PaddleOCR](human/fichas/paddleocr.md) | necesitas OCR preciso y multilingüe | solo quieres hacer buscables PDFs escaneados; mira `ocrmypdf` |
| [Docling](human/fichas/docling.md) | quieres convertir documentos a Markdown con buena estructura | solo tienes PDFs de texto simples; mira `markitdown` |
| [MinerU](human/fichas/mineru.md) | procesas documentos científicos o técnicos complejos | quieres algo ligero; mira `markitdown` |
| [Tesseract](human/fichas/tesseract.md) | quieres OCR clásico sin GPU | tus documentos tienen layouts complejos; mira `paddleocr` |
| [Marker](human/fichas/marker.md) | conviertes PDFs largos con fórmulas | necesitas uso comercial sin licencia; revisa su licencia |
| [Unlimited-OCR](human/fichas/unlimited-ocr.md) | procesas documentos muy largos con GPU | necesitas algo probado y ligero; mira `docling` |
| [olmOCR](human/fichas/olmocr.md) | procesas grandes volúmenes de PDFs con GPU | no tienes GPU; mira `ocrmypdf` o `tesseract` |

**⚖️ ¿Cuál elegir? — Stirling-PDF, pdfcraft**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Stirling-PDF](human/fichas/stirling-pdf.md) | quieres un iLovePDF privado | solo necesitas OCR; mira `ocrmypdf` |
| [pdfcraft](human/fichas/pdfcraft.md) | manipulas PDFs con privacidad y sin instalar nada | necesitas conversión a Markdown para IA (markitdown) o edición de contenido (no solo manipulación de páginas) |

**⚖️ ¿Cuál elegir? — Slidev, reveal.js, Marp**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Slidev](human/fichas/slidev.md) | haces presentaciones técnicas y quieres control como código | necesitas slides para negocio generadas con IA; mira `presenton` |
| [reveal.js](human/fichas/reveal-js.md) | quieres slides web por código, versionables | necesitas PPTX editable en Office (ppt-master) o un editor visual de slides |
| [Marp](human/fichas/marp.md) | quieres slides simples en Markdown | necesitas interactividad y componentes; mira `slidev` |

**⚖️ ¿Cuál elegir? — ppt-master, Presenton**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [ppt-master](human/fichas/ppt-master.md) | quieres PPTX editable de Office rápido | prefieres slides web por código (reveal.js) o control de diseño pixel-perfect |
| [Presenton](human/fichas/presenton.md) | quieres generar presentaciones de negocio con IA | prefieres control total como código; mira `slidev` |

### Conversión de documentos para IA

#### 🔄 Docling ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 70.4k  
**Qué es:** Entiende la estructura del documento (tablas, layout, fórmulas, orden de lectura) y la exporta para RAG y agentes.  
**Instalación:** `pip install docling` y `docling archivo.pdf`.  
**Elige si:** quieres convertir documentos a Markdown con buena estructura — **Evita si:** solo tienes PDFs de texto simples; mira `markitdown`  
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [RAGFlow](human/fichas/ragflow.md) · [Qdrant](human/fichas/qdrant.md)  
**Más:** [ficha completa](human/fichas/docling.md) · [GitHub](https://github.com/docling-project/docling)

#### 📝 markitdown
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 195k  
**Qué es:** Es la puerta de entrada habitual para ingesta de documentos en pipelines RAG.  
**Instalación:** `pip install markitdown` (o `pip install 'markitdown[all]'` para todos los formatos). Los convertidores de visión/audio requieren claves de API opcionales.  
**Elige si:** alimentas LLMs con documentos de formatos variados — **Evita si:** ya tienes el texto limpio o necesitas fidelidad de layout total (no es un reconstructor de PDF)  
**Combina con:** [ppt-master](human/fichas/ppt-master.md) · [open-notebook](human/fichas/open-notebook.md)  
**Más:** [ficha completa](human/fichas/markitdown.md) · [GitHub](https://github.com/microsoft/markitdown)

#### 🔄 MinerU
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 83.4k  
**Qué es:** Muy bueno con papers científicos, tablas y fórmulas; ofrece CLI, API y app de escritorio.  
**Instalación:** `pip install -U "mineru[core]"` y `mineru -p archivo.pdf -o salida`.  
**Elige si:** procesas documentos científicos o técnicos complejos — **Evita si:** quieres algo ligero; mira `markitdown`  
**Combina con:** [RAGFlow](human/fichas/ragflow.md)  
**Más:** [ficha completa](human/fichas/mineru.md) · [GitHub](https://github.com/opendatalab/MinerU)

#### 🔄 Pandoc
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 46.9k  
**Qué es:** La navaja suiza de la conversión de textos: genera Word o PDF desde Markdown y al revés.  
**Instalación:** `brew install pandoc` o el instalador de pandoc.org.  
**Elige si:** necesitas convertir entre formatos de texto — **Evita si:** necesitas extraer estructura de PDFs escaneados; mira `docling`  
**Combina con:** [markitdown](human/fichas/markitdown.md)  
**Más:** [ficha completa](human/fichas/pandoc.md) · [GitHub](https://github.com/jgm/pandoc)

#### 🔄 Marker
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.8k  
**Qué es:** Pensado para libros y papers, con opción de mejorar el resultado usando un LLM.  
**Instalación:** `pip install marker-pdf` y `marker_single archivo.pdf`.  
**Elige si:** conviertes PDFs largos con fórmulas — **Evita si:** necesitas uso comercial sin licencia; revisa su licencia  
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)  
**Más:** [ficha completa](human/fichas/marker.md) · [GitHub](https://github.com/datalab-to/marker)

#### 🔄 PDF Inspector
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 20k  
**Qué es:** Detecta si un PDF necesita OCR para enrutarlo al proceso correcto, y extrae texto rápido cuando no hace falta. De Firecrawl.  
**Instalación:** Añádelo como dependencia de Rust o usa sus bindings siguiendo el README.  
**Elige si:** procesas muchos PDFs y quieres ahorrar OCR — **Evita si:** necesitas la conversión completa a Markdown; mira `docling`  
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md) · [Docling](human/fichas/docling.md)  
**Más:** [ficha completa](human/fichas/pdf-inspector.md) · [GitHub](https://github.com/firecrawl/pdf-inspector)

#### 🔄 Unstructured
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 15.7k  
**Qué es:** Particiona más de 25 tipos de archivo en elementos (títulos, tablas, texto) y los prepara para bases vectoriales.  
**Instalación:** `pip install "unstructured[all-docs]"`.  
**Elige si:** tienes muchos formatos de documentos distintos — **Evita si:** solo procesas PDFs; mira `docling`  
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)  
**Más:** [ficha completa](human/fichas/unstructured.md) · [GitHub](https://github.com/Unstructured-IO/unstructured)

#### 📄 Youtube2Webpage
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.5k  
**Qué es:** Convierte una charla en un artículo navegable con contexto visual.  
**Instalación:** Clonar el repo y ejecutar el script Perl con yt-dlp y ffmpeg instalados en el sistema. Requiere Perl y los binarios mencionados.  
**Elige si:** quieres video → artículo con transcripción y capturas — **Evita si:** necesitas edición de video o el contenido no tiene subtítulos  
**Combina con:** [whisper](human/fichas/whisper.md)  
**Más:** [ficha completa](human/fichas/youtube2webpage.md) · [GitHub](https://github.com/obra/Youtube2Webpage)

### OCR

#### 🔠 PaddleOCR ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 92.5k  
**Qué es:** Reconoce texto en más de 80 idiomas y analiza documentos con tablas y layout. Incluye modelos pequeños para dispositivos.  
**Instalación:** `pip install paddleocr` (más `paddlepaddle`).  
**Elige si:** necesitas OCR preciso y multilingüe — **Evita si:** solo quieres hacer buscables PDFs escaneados; mira `ocrmypdf`  
**Combina con:** [Docling](human/fichas/docling.md)  
**Más:** [ficha completa](human/fichas/paddleocr.md) · [GitHub](https://github.com/PaddlePaddle/PaddleOCR)

#### 🔠 OCRmyPDF ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 35.3k  
**Qué es:** Convierte escaneos en PDF/A buscables manteniendo la imagen original.  
**Instalación:** `brew install ocrmypdf` o `apt install ocrmypdf`; luego `ocrmypdf entrada.pdf salida.pdf`.  
**Elige si:** tienes PDFs escaneados que quieres buscar — **Evita si:** necesitas extraer estructura; mira `docling`  
**Combina con:** [Tesseract](human/fichas/tesseract.md) · [Docling](human/fichas/docling.md)  
**Más:** [ficha completa](human/fichas/ocrmypdf.md) · [GitHub](https://github.com/ocrmypdf/OCRmyPDF)

#### 🔠 Tesseract
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 77.4k  
**Qué es:** Base de muchas herramientas de OCR, ligero y sin GPU.  
**Instalación:** `brew install tesseract` o `apt install tesseract-ocr`.  
**Elige si:** quieres OCR clásico sin GPU — **Evita si:** tus documentos tienen layouts complejos; mira `paddleocr`  
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md)  
**Más:** [ficha completa](human/fichas/tesseract.md) · [GitHub](https://github.com/tesseract-ocr/tesseract)

#### 🔠 Unlimited-OCR
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 31.1k  
**Qué es:** Extrae texto y estructura de documentos de muchas páginas sin dividirlos, pensado para contexto largo.  
**Instalación:** Sigue el README para descargar el modelo y ejecutar la inferencia (requiere GPU).  
**Elige si:** procesas documentos muy largos con GPU — **Evita si:** necesitas algo probado y ligero; mira `docling`  
**Combina con:** [litellm](human/fichas/litellm.md) · [cosmos](human/fichas/cosmos.md) · [ComfyUI](human/fichas/comfyui.md)  
**Más:** [ficha completa](human/fichas/unlimited-ocr.md) · [GitHub](https://github.com/baidu/Unlimited-OCR)

#### 🔠 olmOCR
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 19.8k  
**Qué es:** Pensado para crear datasets de entrenamiento a partir de millones de PDFs, con orden de lectura correcto.  
**Instalación:** `pip install olmocr` (requiere GPU NVIDIA).  
**Elige si:** procesas grandes volúmenes de PDFs con GPU — **Evita si:** no tienes GPU; mira `ocrmypdf` o `tesseract`  
**Combina con:** [vLLM](human/fichas/vllm.md)  
**Más:** [ficha completa](human/fichas/olmocr.md) · [GitHub](https://github.com/allenai/olmocr)

### Herramientas PDF

#### 📑 Stirling-PDF ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 96.2k  
**Qué es:** Más de 50 herramientas de PDF en el navegador sin enviar archivos a terceros.  
**Instalación:** `docker run -d -p 8080:8080 stirlingtools/stirling-pdf`.  
**Elige si:** quieres un iLovePDF privado — **Evita si:** solo necesitas OCR; mira `ocrmypdf`  
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md)  
**Más:** [ficha completa](human/fichas/stirling-pdf.md) · [GitHub](https://github.com/Stirling-Tools/Stirling-PDF)

#### 📑 PDFMathTranslate
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 38.3k  
**Qué es:** Ideal para leer artículos científicos en tu idioma sin perder el layout. Admite Google, DeepL, OpenAI, Ollama y más.  
**Instalación:** `pip install pdf2zh` y `pdf2zh archivo.pdf`, o la GUI web.  
**Elige si:** traduces PDFs técnicos y quieres conservar el formato — **Evita si:** necesitas editar el PDF; mira `stirling-pdf`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/pdfmathtranslate.md) · [GitHub](https://github.com/PDFMathTranslate/PDFMathTranslate)

#### 📄 pdfcraft
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 9.8k  
**Qué es:** Apunta a ser la alternativa local y sin nube a los servicios online de PDF.  
**Instalación:** Abrir la web en el navegador, o `npm install` y ejecutar en local desde el repo. No requiere backend ni GPU.  
**Elige si:** manipulas PDFs con privacidad y sin instalar nada — **Evita si:** necesitas conversión a Markdown para IA (markitdown) o edición de contenido (no solo manipulación de páginas)  
**Combina con:** [markitdown](human/fichas/markitdown.md)  
**Más:** [ficha completa](human/fichas/pdfcraft.md) · [GitHub](https://github.com/PDFCraftTool/pdfcraft)

#### 📑 PdfDing
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 1.8k  
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.  
**Qué es:** Organiza y lee tus PDFs desde cualquier dispositivo. El desarrollo se trasladó a Codeberg.  
**Instalación:** `docker run -p 8000:8000 mrmn2/pdfding` (revisa la versión actual en Codeberg).  
**Elige si:** quieres organizar y leer PDFs en tu servidor — **Evita si:** necesitas editar PDFs; mira `stirling-pdf`  
**Combina con:** [markitdown](human/fichas/markitdown.md) · [ppt-master](human/fichas/ppt-master.md) · [reveal.js](human/fichas/reveal-js.md)  
**Más:** [ficha completa](human/fichas/pdfding.md) · [GitHub](https://github.com/mrmn2/PdfDing)

### Presentaciones

#### 🖥️ Slidev ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 49.4k  
**Qué es:** Escribe tus slides en Markdown y obtén resaltado de código, diagramas, animaciones y exportación a PDF. Los agentes de código lo usan bien.  
**Instalación:** `npm init slidev@latest`.  
**Elige si:** haces presentaciones técnicas y quieres control como código — **Evita si:** necesitas slides para negocio generadas con IA; mira `presenton`  
**Combina con:** [Mermaid](human/fichas/mermaid.md)  
**Más:** [ficha completa](human/fichas/slidev.md) · [GitHub](https://github.com/slidevjs/slidev)

#### 📊 ppt-master
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 75.5k  
**Qué es:** Sustituye el maquetado manual de slides por un borrador estructurado por un LLM.  
**Instalación:** `git clone` del repo y `pip install -r requirements.txt`; requiere clave de API del modelo (Anthropic u OpenAI según configuración).  
**Elige si:** quieres PPTX editable de Office rápido — **Evita si:** prefieres slides web por código (reveal.js) o control de diseño pixel-perfect  
**Combina con:** [markitdown](human/fichas/markitdown.md)  
**Más:** [ficha completa](human/fichas/ppt-master.md) · [GitHub](https://github.com/hugohe3/ppt-master)

#### 🖥️ reveal.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 72.6k  
**Qué es:** Convierte las diapositivas en una página web versionable y reproducible por código.  
**Instalación:** `npm install reveal.js` (o clonar el repo y abrir `index.html` en el navegador). Para exportar a PDF usa el modo de impresión del navegador.  
**Elige si:** quieres slides web por código, versionables — **Evita si:** necesitas PPTX editable en Office (ppt-master) o un editor visual de slides  
**Combina con:** [markitdown](human/fichas/markitdown.md)  
**Más:** [ficha completa](human/fichas/reveal-js.md) · [GitHub](https://github.com/hakimel/reveal.js)

#### 🖥️ Marp
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 12.7k  
**Qué es:** Escribes Markdown con separadores y obtienes slides limpias; tiene extensión de VS Code.  
**Instalación:** `npm i -g @marp-team/marp-cli` o la extensión Marp for VS Code.  
**Elige si:** quieres slides simples en Markdown — **Evita si:** necesitas interactividad y componentes; mira `slidev`  
**Más:** [ficha completa](human/fichas/marp.md) · [GitHub](https://github.com/marp-team/marp)

#### 🖥️ Presenton
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 11.8k  
**Qué es:** Crea presentaciones editables a partir de un prompt o documento, con tus plantillas, y exporta a PPTX o PDF.  
**Instalación:** `docker run -it -p 5000:80 ghcr.io/presenton/presenton:latest`.  
**Elige si:** quieres generar presentaciones de negocio con IA — **Evita si:** prefieres control total como código; mira `slidev`  
**Combina con:** [Ollama](human/fichas/ollama.md)  
**Más:** [ficha completa](human/fichas/presenton.md) · [GitHub](https://github.com/presenton/presenton)

### Diagramas y documentación

#### 🗺️ Mermaid ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 91.1k  
**Qué es:** GitHub, Notion y muchos editores lo renderizan de forma nativa; los LLM lo escriben muy bien.  
**Instalación:** `npm i mermaid` o usa bloques ```mermaid en GitHub.  
**Elige si:** quieres diagramas como texto — **Evita si:** necesitas dibujar a mano alzada; mira `excalidraw`  
**Combina con:** [Slidev](human/fichas/slidev.md)  
**Más:** [ficha completa](human/fichas/mermaid.md) · [GitHub](https://github.com/mermaid-js/mermaid)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
