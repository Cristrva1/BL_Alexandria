# 🌌 Guía completa de BL_Alexandria

Las **498 fichas** de la biblioteca en un solo documento, agrupadas por categoría y subcategoría. Úsala para leer de corrido o buscar con Ctrl+F; para navegar por partes usa la [guía humana](human/README.md) o el [explorador interactivo](docs/index.html).

## 🧭 Cómo leer cada ficha

- **Etiquetas:** Ejecución 🏠 local · ☁️ cloud/API · 🔀 híbrido — Rol ⚙️ plataforma · 🧩 motor · 📚 librería · 🎨 skill · 📂 catálogo · 🖥️ app — Setup 🟢 fácil · 🟡 medio · 🔴 pesado — 🔌 MCP.
- **⭐** junto al nombre: punto de partida editorial. El número de estrellas viene de GitHub.
- **Elige si / Evita si** te dicen en una línea si encaja; **Combina con** lleva a sus complementos.

## 📂 Mapa de categorías

| # | Categoría | Repos | Para qué |
|---:|---|---:|---|
| 1 | [🤖 Automatizar negocios y comunicación](#-1-automatizar-negocios-y-comunicación) | 35 | Conecta aplicaciones, organiza clientes, atiende mensajes o programa procesos. Empieza por un motor de flujos; añade canales y CRM según tu objetivo. |
| 2 | [🧠 Mejorar tu agente: skills y prompts](#-2-mejorar-tu-agente-skills-y-prompts) | 54 | Instrucciones, plugins y métodos que añades a un agente que ya utilizas. Distingue una skill concreta de un directorio que solo enlaza a otras. |
| 3 | [🕸️ Crear y usar agentes de IA](#️-3-crear-y-usar-agentes-de-ia) | 73 | Agentes listos para trabajar y frameworks para construir los tuyos. Un agente de código se utiliza; un framework se integra dentro de una aplicación. |
| 4 | [🕷️ Buscar y extraer información web](#️-4-buscar-y-extraer-información-web) | 34 | Buscadores, crawlers y navegadores. Usa un crawler para extraer páginas, un navegador para interactuar y un agente para investigar con un modelo. |
| 5 | [🔌 Conectar herramientas con MCP](#-5-conectar-herramientas-con-mcp) | 24 | SDKs, servidores y conectores que dejan a un agente usar herramientas. El servidor MCP aporta acciones o datos; el modelo pertenece al cliente. |
| 6 | [🧬 Memoria, conocimiento y operación de IA](#-6-memoria-conocimiento-y-operación-de-ia) | 35 | Guarda memoria, consulta documentos con RAG, sirve modelos y evalúa resultados. Una base vectorial y un sistema RAG completo resuelven capas distintas. |
| 7 | [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](#-7-entender-código-trabajar-con-datos-y-entrenar-modelos) | 44 | Herramientas para analizar código, procesar datos, aprender machine learning y entrenar modelos. Separa los ejemplos de aprendizaje de las librerías que integras. |
| 8 | [🏠 Usar modelos y asistentes locales](#-8-usar-modelos-y-asistentes-locales) | 25 | Motores de modelos, clientes de chat y espacios de trabajo. Instalar una interfaz local no garantiza que el modelo sea local: comprueba su backend. |
| 9 | [🎨 Diseñar y construir interfaces](#-9-diseñar-y-construir-interfaces) | 35 | Componentes, estilos, animación, diseño visual y herramientas para crear pantallas. Las librerías de UI no necesitan por sí solas una API de IA. |
| 10 | [📊 Analizar datos, crear dashboards y mapas](#-10-analizar-datos-crear-dashboards-y-mapas) | 23 | Herramientas para explorar datos, crear gráficos, medir productos y visualizar fuentes abiertas. El chat con datos sí puede añadir un modelo; un gráfico convencional no lo necesita. |
| 11 | [🖼️ Generar imágenes y trabajar con visión](#️-11-generar-imágenes-y-trabajar-con-visión) | 28 | Generación, restauración, detección, segmentación y etiquetado de imágenes. Revisa por separado la licencia de los pesos y el hardware del modelo. |
| 12 | [🎬 Crear audio, voz y video](#-12-crear-audio-voz-y-video) | 50 | Transcribe, sintetiza voz, edita o genera video. El montaje local y la generación mediante un proveedor son rutas con requisitos diferentes. |
| 13 | [📄 Trabajar con documentos y presentaciones](#-13-trabajar-con-documentos-y-presentaciones) | 24 | Extrae texto, aplica OCR, transforma PDFs o crea diapositivas. Empieza por el formato de entrada y el resultado que necesitas. |
| 14 | [📈 Investigar finanzas y mercados](#-14-investigar-finanzas-y-mercados) | 14 | Agentes de investigación, análisis cuantitativo, backtesting y bots de ejemplo. Distingue una explicación o simulación de una operación con fondos reales. |

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

## 🤖 1. Automatizar negocios y comunicación

Conecta aplicaciones, organiza clientes, atiende mensajes o programa procesos. Empieza por un motor de flujos; añade canales y CRM según tu objetivo.

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

**⚖️ ¿Cuál elegir? — NocoDB, Appsmith, ToolJet, Budibase**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [NocoDB](human/fichas/nocodb.md) | quieres un Airtable propio sobre tu base de datos | necesitas apps internas con lógica compleja; mira `appsmith` |
| [Appsmith](human/fichas/appsmith.md) | necesitas herramientas internas con lógica y muchas fuentes de datos | solo quieres hojas colaborativas; mira `nocodb` |
| [ToolJet](human/fichas/tooljet.md) | quieres herramientas internas con IA para generarlas | prefieres un proyecto con licencia más permisiva; mira `appsmith` |
| [Budibase](human/fichas/budibase.md) | quieres apps internas y agentes en una sola plataforma self-host | buscas el editor más flexible para backoffices; mira `appsmith` |

### Motores de workflow y automatización

#### 🔁 n8n ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 211k<br>
**Qué es:** Conecta cualquier app con cualquier otra en tu propio servidor, sin pagar una suscripción mensual por cada flujo.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/n8n-io/n8n/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres el motor central de automatización con máximo catálogo — **Evita si:** buscas algo minimalista o sin self-host<br>
**Combina con:** [n8n-mcp](human/fichas/n8n-mcp.md) · [n8n-skills](human/fichas/n8n-skills.md) · [evolution-api](human/fichas/evolution-api.md)<br>
**Más:** [ficha completa](human/fichas/n8n.md) · [GitHub](https://github.com/n8n-io/n8n)

#### 🤖 huginn
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 50.5k<br>
**Qué es:** Vigila webs, feeds y APIs y dispara acciones cuando algo cambia, todo alojado por ti y sin depender de terceros.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/huginn/huginn/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** automatizas tareas orientadas a eventos y valoras la privacidad — **Evita si:** quieres editor visual moderno o IA nativa (n8n)<br>
**Combina con:** [novu](human/fichas/novu.md)<br>
**Más:** [ficha completa](human/fichas/huginn.md) · [GitHub](https://github.com/huginn/huginn)

#### 🤖 cal.diy
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 50k<br>
**Qué es:** Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia. Despliega la aplicación de calendario y configura base de datos, disponibilidad e integraciones.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/calcom/cal.diy/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar una agenda autoalojada para uso personal — **Evita si:** solo necesitas una integración sencilla sin operar una plataforma<br>
**Más:** [ficha completa](human/fichas/cal-diy.md) · [GitHub](https://github.com/calcom/cal.diy)

#### 🔁 Kestra
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.2k<br>
**Qué es:** Define flujos en YAML con un editor web, cientos de plugins y disparadores por calendario o eventos. Pensado para equipos de datos y plataforma que quieren orquestación como código.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/kestra-io/kestra/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres workflows declarativos en YAML con UI y control de versiones — **Evita si:** buscas automatizaciones de negocio con nodos visuales; mira `n8n`<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [Apache Superset](human/fichas/superset.md)<br>
**Más:** [ficha completa](human/fichas/kestra.md) · [GitHub](https://github.com/kestra-io/kestra)

#### 🧩 activepieces
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 25.5k<br>
**Qué es:** Orquesta tus apps con flujos visuales sin código y conserva el control al alojarlo en tu servidor.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/activepieces/activepieces/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres reemplazar Zapier con piezas propias en TypeScript — **Evita si:** ya dominas n8n y su ecosistema te basta<br>
**Combina con:** [novu](human/fichas/novu.md)<br>
**Más:** [ficha completa](human/fichas/activepieces.md) · [GitHub](https://github.com/activepieces/activepieces)

#### 🔁 Node-RED
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 23.8k<br>
**Qué es:** Conecta dispositivos, APIs y servicios arrastrando nodos en el navegador. Es muy usado en IoT, domótica e industria por su ligereza y su enorme biblioteca de nodos de la comunidad.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/node-red/node-red/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas con IoT o eventos y quieres algo ligero y probado — **Evita si:** necesitas integraciones SaaS y nodos de IA listos; mira `n8n`<br>
**Más:** [ficha completa](human/fichas/node-red.md) · [GitHub](https://github.com/node-red/node-red)

#### 🔁 Windmill
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.6k<br>
**Qué es:** Convierte scripts de Python, TypeScript, Go o SQL en workflows, endpoints y apps con UI generada. Sirve a equipos técnicos que quieren la flexibilidad del código con la comodidad de un orquestador visual.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/windmill-labs/windmill/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu equipo programa y quiere workflows versionados en código — **Evita si:** prefieres arrastrar nodos sin escribir código; mira `n8n`<br>
**Combina con:** [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/windmill.md) · [GitHub](https://github.com/windmill-labs/windmill)

#### 🔁 Trigger.dev
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 16.8k<br>
**Qué es:** Escribe tareas largas o con reintentos en TypeScript dentro de tu app y Trigger.dev las ejecuta, reintenta y monitorea. Ideal para equipos de producto con Next.js o Node que no quieren operar colas.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/triggerdotdev/trigger.dev/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu app es TypeScript y necesitas tareas largas confiables sin montar colas — **Evita si:** quieres un editor visual para no programadores; mira `n8n`<br>
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/trigger-dev.md) · [GitHub](https://github.com/triggerdotdev/trigger.dev)

### Ecosistema n8n

#### 🔁 Self-hosted AI Starter Kit ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 15.4k<br>
**Qué es:** Kit oficial de n8n que levanta un entorno de IA privado: n8n para orquestar, Ollama para modelos, Qdrant como base vectorial y PostgreSQL. Útil para prototipar agentes y RAG sin enviar datos fuera.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un stack de IA local funcionando hoy con n8n — **Evita si:** vas a producción con alta carga; arma tu propio despliegue<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md)<br>
**Más:** [ficha completa](human/fichas/self-hosted-ai-starter-kit.md) · [GitHub](https://github.com/n8n-io/self-hosted-ai-starter-kit)

#### 🔁 Awesome n8n Templates
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 26.4k<br>
**Qué es:** Colección de plantillas de n8n para estudiar o importar automatizaciones de servicios y tareas habituales. Cada workflow tiene dependencias y posibles consumos externos que debes revisar antes de activarlo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/enescingoz/awesome-n8n-templates/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas n8n y quieres partir de flujos hechos — **Evita si:** no usas n8n<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [n8n-mcp](human/fichas/n8n-mcp.md) · [n8n-skills](human/fichas/n8n-skills.md)<br>
**Más:** [ficha completa](human/fichas/awesome-n8n-templates.md) · [GitHub](https://github.com/enescingoz/awesome-n8n-templates)

#### 🔌 n8n-mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 23.3k<br>
**Qué es:** Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. El cliente MCP y la instancia de n8n conservan sus propios requisitos de acceso.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/czlonkowski/n8n-mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** generas flujos n8n con IA y quieres menos alucinaciones de parámetros — **Evita si:** no usas n8n o construyes los flujos a mano<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [n8n-skills](human/fichas/n8n-skills.md)<br>
**Más:** [ficha completa](human/fichas/n8n-mcp.md) · [GitHub](https://github.com/czlonkowski/n8n-mcp)

#### 🛠️ n8n-skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 6.6k<br>
**Qué es:** Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas. La skill no sustituye la instancia de n8n ni las credenciales de los servicios de un workflow.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/czlonkowski/n8n-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** generas workflows n8n con IA y te cansan los fallos de JSON — **Evita si:** no usas n8n<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [n8n-mcp](human/fichas/n8n-mcp.md)<br>
**Más:** [ficha completa](human/fichas/n8n-skills.md) · [GitHub](https://github.com/czlonkowski/n8n-skills)

### WhatsApp y mensajería

#### 💬 whatsapp-web.js ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 22.9k<br>
**Qué es:** Permite enviar y recibir mensajes, medios y grupos desde código usando una sesión de WhatsApp Web. Muy usada para bots y prototipos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install whatsapp-web.js` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres programar un bot de WhatsApp en Node rápido — **Evita si:** necesitas una API REST multi-sesión lista; mira `evolution-api` o `waha`<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [chatwoot](human/fichas/chatwoot.md)<br>
**Más:** [ficha completa](human/fichas/whatsapp-web-js.md) · [GitHub](https://github.com/wwebjs/whatsapp-web.js)

#### 🌐 OpenWA
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 16.9k<br>
**Qué es:** Envía y recibe mensajes de WhatsApp desde tu propio script con una API sencilla y expresiva.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/rmyndharis/OpenWA/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** desarrollas scripts o bots individuales y quieres arrancar rápido — **Evita si:** necesitas infra multi-instancia o alta disponibilidad (evolution-api)<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [evolution-api](human/fichas/evolution-api.md)<br>
**Más:** [ficha completa](human/fichas/openwa.md) · [GitHub](https://github.com/rmyndharis/OpenWA)

#### 💬 Baileys
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 11.6k<br>
**Qué es:** Implementa el protocolo de WhatsApp Web directamente, así que consume muy pocos recursos. Es la base de muchas APIs de WhatsApp, incluida Evolution API.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas WhatsApp en código con bajo consumo de recursos — **Evita si:** prefieres una API REST lista; mira `evolution-api`<br>
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/baileys.md) · [GitHub](https://github.com/WhiskeySockets/Baileys)

#### 🌐 fluxer
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 10.9k<br>
**Qué es:** Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio. Organiza canales y comunicación de grupos; no es un generador de audio o video.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/fluxerapp/fluxer/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres probar algo nuevo y seguir su evolución — **Evita si:** necesitas estabilidad de producción (API aún en finalización)<br>
**Combina con:** [Open-Generative-AI](human/fichas/open-generative-ai.md)<br>
**Más:** [ficha completa](human/fichas/fluxer.md) · [GitHub](https://github.com/fluxerapp/fluxer)

#### 🧬 evolution-api
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 10.1k<br>
**Qué es:** Conecta WhatsApp a tu stack mediante una API REST propia, sin quedar atado a un proveedor cerrado.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/evolution-foundation/evolution-api/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** operas WhatsApp en producción con varias instancias — **Evita si:** solo necesitas un bot de prueba o un único script (OpenWA basta)<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [chatwoot](human/fichas/chatwoot.md)<br>
**Más:** [ficha completa](human/fichas/evolution-api.md) · [GitHub](https://github.com/evolution-foundation/evolution-api)

#### 🤖 whatsmeow
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 7.9k<br>
**Qué es:** Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web. Gestiona la sesión del cliente y permite enviar mensajes, recibir eventos y mantener el estado de la cuenta.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/tulir/whatsmeow/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas integrar WhatsApp Web en un servicio escrito en Go — **Evita si:** solo necesitas una integración sencilla sin operar una plataforma<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/whatsmeow.md) · [GitHub](https://github.com/tulir/whatsmeow)

#### 💬 WAHA
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 7.8k<br>
**Qué es:** Expone WhatsApp como API HTTP con webhooks, lista para conectar a n8n o a tu backend. Ofrece motores basados en navegador o en WebSocket.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/devlikeapro/waha/blob/core/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una API REST de WhatsApp lista en minutos — **Evita si:** necesitas multi-instancia avanzada gratis; mira `evolution-api`<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [chatwoot](human/fichas/chatwoot.md)<br>
**Más:** [ficha completa](human/fichas/waha.md) · [GitHub](https://github.com/devlikeapro/waha)

#### 🤖 whatsapp-agentkit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 567<br>
**Qué es:** Arranca un bot de WhatsApp con IA sin escribir código, a partir de una plantilla guiada.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres arrancar sin partir de cero y te vale con lo que Claude Code genere — **Evita si:** necesitas control fino del stack o ya tienes el bot hecho<br>
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [n8n-mcp](human/fichas/n8n-mcp.md)<br>
**Más:** [ficha completa](human/fichas/whatsapp-agentkit.md) · [GitHub](https://github.com/Hainrixz/whatsapp-agentkit)

### Chatbots y asistentes conversacionales

#### 🤖 Typebot ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 10.6k<br>
**Qué es:** Diseña conversaciones con bloques arrastrables (preguntas, condiciones, integraciones, IA) y publícalas en web o WhatsApp. Pensado para captar leads y formularios conversacionales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/baptisteArno/typebot.io/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un chatbot guiado sin programar, con buena UX — **Evita si:** necesitas un agente abierto con razonamiento libre; mira `botpress`<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [evolution-api](human/fichas/evolution-api.md)<br>
**Más:** [ficha completa](human/fichas/typebot.md) · [GitHub](https://github.com/baptisteArno/typebot.io)

#### 🤖 Rasa
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 21.4k<br>
**Qué es:** Permite crear asistentes de texto y voz con control total del diálogo y de los datos. Muy usado en empresas que necesitan bots on-premise y predecibles.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/RasaHQ/rasa/blob/3.6.x/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas un asistente on-premise con diálogo muy controlado — **Evita si:** quieres algo rápido con LLM y sin entrenar; mira `botpress` o `typebot`<br>
**Combina con:** [chatwoot](human/fichas/chatwoot.md)<br>
**Más:** [ficha completa](human/fichas/rasa.md) · [GitHub](https://github.com/RasaHQ/rasa)

#### 🤖 Botpress
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 15k<br>
**Qué es:** Combina un estudio visual con código para crear agentes que usan bases de conocimiento, herramientas y canales. Su producto principal hoy es cloud; el repo contiene SDK, integraciones y CLI.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/botpress/botpress/blob/master/readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un agente conversacional multicanal con poco código — **Evita si:** necesitas todo self-host y sin nube; mira `rasa` o `typebot`<br>
**Combina con:** [chatwoot](human/fichas/chatwoot.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/botpress.md) · [GitHub](https://github.com/botpress/botpress)

### CRM, ERP y soporte al cliente

#### 👥 Odoo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 55.8k<br>
**Qué es:** Integra CRM, ventas, facturación, inventario, RR. HH. y sitio web en una sola plataforma modular. La usan pymes y grandes empresas en todo el mundo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/odoo/odoo/blob/20.0/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas un ERP completo con CRM integrado — **Evita si:** solo quieres un CRM ligero; mira `twenty-main`<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [metabase](human/fichas/metabase.md)<br>
**Más:** [ficha completa](human/fichas/odoo.md) · [GitHub](https://github.com/odoo/odoo)

#### 👥 twenty-main
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 60.9k<br>
**Qué es:** La premisa es tratar el CRM como una pieza más de tu stack: lo construyes, lo despliegas y lo versionas igual que el código.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/twentyhq/twenty/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un CRM que se adapte 1:1 a tu negocio y vivir en self-host — **Evita si:** buscas algo plug-and-play gestionado o no quieres operar PostgreSQL y Docker<br>
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/twenty-main.md) · [GitHub](https://github.com/twentyhq/twenty)

#### 👥 ERPNext
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 41.3k<br>
**Qué es:** Cubre la operación completa de una empresa sin licencias de pago. Muy usado por pymes y en manufactura y distribución.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/frappe/erpnext/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un ERP completo y totalmente libre — **Evita si:** buscas el mayor ecosistema de módulos; mira `odoo`<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [metabase](human/fichas/metabase.md)<br>
**Más:** [ficha completa](human/fichas/erpnext.md) · [GitHub](https://github.com/frappe/erpnext)

#### 💬 chatwoot
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 39.9k<br>
**Qué es:** Reúne WhatsApp, email, web chat y redes en una sola bandeja, con paso a un humano cuando el bot no basta. Alternativa abierta a Intercom o Zendesk.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/chatwoot/chatwoot/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** das soporte por varios canales y necesitas handoff humano — **Evita si:** solo necesitas enviar mensajes salientes (evolution-api)<br>
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [novu](human/fichas/novu.md)<br>
**Más:** [ficha completa](human/fichas/chatwoot.md) · [GitHub](https://github.com/chatwoot/chatwoot)

#### 🤖 crm
**Etiquetas:** Ejecución ☁️ cloud/API · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 12.1k<br>
**Qué es:** CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia. Un agente trabaja sobre una cola y un presupuesto de investigación y mantiene la información del CRM.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/trycompai/crm/blob/release/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar un CRM donde el agente organiza el seguimiento — **Evita si:** solo necesitas una integración sencilla sin operar una plataforma<br>
**Más:** [ficha completa](human/fichas/compai-crm.md) · [GitHub](https://github.com/trycompai/crm)

### Email, marketing y notificaciones

#### 🔔 novu ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 40.3k<br>
**Qué es:** Envía notificaciones por email, SMS, push y chat desde una sola API, sin integrar y mantener cada proveedor por separado.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/novuhq/novu/blob/next/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** envías notificaciones por varios canales y quieres un único backend — **Evita si:** solo necesitas email (listmonk)<br>
**Combina con:** [chatwoot](human/fichas/chatwoot.md) · [activepieces](human/fichas/activepieces.md)<br>
**Más:** [ficha completa](human/fichas/novu.md) · [GitHub](https://github.com/novuhq/novu)

#### 📬 listmonk
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 24.3k<br>
**Qué es:** Envía newsletters y campañas a miles de suscriptores desde un solo binario ligero que consume muy pocos recursos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/knadh/listmonk/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres email marketing simple, rápido y propio — **Evita si:** necesitas nurturing avanzado o scoring de leads (mautic)<br>
**Combina con:** [mautic](human/fichas/mautic.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/listmonk.md) · [GitHub](https://github.com/knadh/listmonk)

#### 📣 mautic
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 11k<br>
**Qué es:** Nutre leads por email con reglas y segmentos automáticos, sin ceder los datos de tus clientes a un SaaS.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mautic/mautic/blob/7.x/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas automatización de marketing seria y soberana — **Evita si:** te basta una newsletter simple (listmonk)<br>
**Combina con:** [listmonk](human/fichas/listmonk.md) · [Marketing Skills](human/fichas/marketingskills.md)<br>
**Más:** [ficha completa](human/fichas/mautic.md) · [GitHub](https://github.com/mautic/mautic)

### Apps internas y bases de datos no-code

#### 🧱 NocoDB ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 65.5k<br>
**Qué es:** Ofrece vistas de tabla, kanban, galería y formularios sobre PostgreSQL, MySQL o SQLite, con API REST automática. Útil como backoffice rápido para equipos no técnicos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/nocodb/nocodb/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un Airtable propio sobre tu base de datos — **Evita si:** necesitas apps internas con lógica compleja; mira `appsmith`<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/nocodb.md) · [GitHub](https://github.com/nocodb/nocodb)

#### 🧱 Appsmith
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 41.3k<br>
**Qué es:** Arrastra widgets, conéctalos a más de 25 bases de datos o cualquier API y añade lógica en JavaScript. Pensada para equipos que construyen backoffices rápido.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/appsmithorg/appsmith/blob/release/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas herramientas internas con lógica y muchas fuentes de datos — **Evita si:** solo quieres hojas colaborativas; mira `nocodb`<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/appsmith.md) · [GitHub](https://github.com/appsmithorg/appsmith)

#### 🧱 ToolJet
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 41.2k<br>
**Qué es:** Construye apps internas arrastrando componentes y conectando bases y APIs, o genéralas describiéndolas con IA. Pensada para equipos de operaciones y TI.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/ToolJet/ToolJet/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres herramientas internas con IA para generarlas — **Evita si:** prefieres un proyecto con licencia más permisiva; mira `appsmith`<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/tooljet.md) · [GitHub](https://github.com/ToolJet/ToolJet)

#### 🧱 Budibase
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 28.4k<br>
**Qué es:** Genera apps CRUD, formularios y flujos a partir de bases existentes y ahora añade agentes de IA agnósticos de modelo. Pensada para equipos de operaciones.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Budibase/budibase/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres apps internas y agentes en una sola plataforma self-host — **Evita si:** buscas el editor más flexible para backoffices; mira `appsmith`<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/budibase.md) · [GitHub](https://github.com/Budibase/budibase)

---

## 🧠 2. Mejorar tu agente: skills y prompts

Instrucciones, plugins y métodos que añades a un agente que ya utilizas. Distingue una skill concreta de un directorio que solo enlaza a otras.

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
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 195k<br>
**Qué es:** Repositorio de Anthropic con skills listas para Claude Code, Claude.ai y la API: creativas, técnicas (pruebas de apps web, creación de servidores MCP) y empresariales, más las skills de docx, pptx, xlsx y PDF que Claude usa para generar archivos. Incluye la especificación del estándar Agent Skills y una plantilla para crear las tuyas.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres skills oficiales de Anthropic o un ejemplo de referencia para escribir las tuyas — **Evita si:** buscas volumen o skills de comunidad para varios agentes; mira `awesome-agent-skills` o `antigravity-awesome-skills`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) · [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/anthropic-skills.md) · [GitHub](https://github.com/anthropics/skills)

#### 🔌 Claude Code Plugins Directory ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 47.3k<br>
**Qué es:** Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. Cada plugin puede tener requisitos distintos; el marketplace completo no es una aplicación que debas desplegar.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/claude-plugins-official/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando — **Evita si:** buscas recursos comunitarios o trabajas con otro agente; mira `awesome-claude-code` o `wshobson-agents`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [Awesome Claude Code](human/fichas/awesome-claude-code.md)<br>
**Más:** [ficha completa](human/fichas/claude-plugins-official.md) · [GitHub](https://github.com/anthropics/claude-plugins-official)

#### 🗂️ Awesome Claude Skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 79.5k<br>
**Qué es:** Recopilación de skills por áreas (documentos, desarrollo, datos, marketing, escritura, multimedia, productividad, seguridad) que enlaza skills oficiales de Anthropic y de la comunidad, y aloja algunas propias. Incluye el plugin connect-apps, que usa Composio para que Claude envíe correos, cree issues o publique en Slack.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo — **Evita si:** solo quieres skills de procedencia oficial; mira `anthropic-skills` o `awesome-agent-skills`<br>
**Combina con:** [Composio](human/fichas/composio.md) · [Claude Code](human/fichas/claude-code.md) · [SkillSpector](human/fichas/skillspector.md)<br>
**Más:** [ficha completa](human/fichas/awesome-claude-skills.md) · [GitHub](https://github.com/ComposioHQ/awesome-claude-skills)

#### ⭐ Awesome Claude Code
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 58k<br>
**Qué es:** Índice comunitario del ecosistema de Claude Code organizado por temas: guías de inicio, recursos oficiales de Anthropic, skills, orquestación de agentes, memoria, observabilidad y coste, seguridad, status lines y configuración. Cada entrada incluye una breve valoración del mantenedor.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/hesreallyhim/awesome-claude-code/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Claude Code a diario y quieres descubrir herramientas y flujos probados por la comunidad — **Evita si:** trabajas con otro agente o solo quieres plugins oficiales; mira `claude-plugins-official` o `awesome-agent-skills`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) · [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/awesome-claude-code.md) · [GitHub](https://github.com/hesreallyhim/awesome-claude-code)

#### 🗂️ Agentic Awesome Skills
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 49.7k<br>
**Qué es:** Antes llamada Antigravity Awesome Skills, reúne miles de skills por dominio (desarrollo, seguridad, DevOps, datos, marketing) instalables en Claude Code, Codex, Cursor, Gemini CLI, Kiro, OpenCode y otros agentes. Incluye bundles por rol, plugins temáticos y AAS Core, un MCP local para que el agente busque en el catálogo y elija skills antes de instalarlas.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código — **Evita si:** prefieres pocas skills oficiales y revisadas; mira `anthropic-skills` o `awesome-agent-skills`<br>
**Combina con:** [SkillSpector](human/fichas/skillspector.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/antigravity-awesome-skills.md) · [GitHub](https://github.com/sickn33/agentic-awesome-skills)

#### 🗂️ wshobson/agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 42.5k<br>
**Qué es:** Colección de Seth Hobson que agrupa subagentes especialistas, skills y comandos en plugins por área: desarrollo Python y JavaScript, revisión de código, testing, infraestructura, seguridad y más. Se escribe una sola vez en formato de plugin de Claude Code y unos adaptadores generan las versiones para Codex, Cursor, OpenCode, Antigravity CLI, GitHub Copilot y Pi.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/wshobson/agents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin — **Evita si:** solo quieres plugins oficiales de Anthropic y socios; mira `claude-plugins-official`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [SkillSpector](human/fichas/skillspector.md)<br>
**Más:** [ficha completa](human/fichas/wshobson-agents.md) · [GitHub](https://github.com/wshobson/agents)

#### 🗂️ Awesome GitHub Copilot
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 41.2k<br>
**Qué es:** Repositorio de la organización GitHub que reúne personalizaciones de Copilot aportadas por la comunidad: agentes especializados (algunos conectados a servidores MCP), instrucciones que se aplican por tipo de archivo, skills, plugins y un cookbook de recetas para las APIs de Copilot. Tiene web con búsqueda, un Learning Hub y un llms.txt para agentes.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/github/awesome-copilot/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu equipo trabaja con GitHub Copilot en VS Code o Copilot CLI y quiere personalizarlo — **Evita si:** usas Claude Code u otro agente; mira `claude-plugins-official` o `antigravity-awesome-skills`<br>
**Combina con:** [GitHub MCP Server](human/fichas/github-mcp-server.md) · [Spec Kit](human/fichas/spec-kit.md) · [GitHub CLI](human/fichas/cli.md)<br>
**Más:** [ficha completa](human/fichas/awesome-copilot.md) · [GitHub](https://github.com/github/awesome-copilot)

#### 🏅 Awesome Agent Skills
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 37.2k<br>
**Qué es:** Índice mantenido por VoltAgent que enlaza skills publicadas por los equipos de cada producto (Anthropic, Google, Vercel, Stripe, Cloudflare, Supabase, Hugging Face, Trail of Bits...) y una sección de comunidad revisada a mano. Incluye la tabla de carpetas de skills por agente (Claude Code, Codex, Cursor, Gemini CLI, Copilot, OpenCode, Windsurf) y normas de calidad para escribir skills.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/VoltAgent/awesome-agent-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres skills con procedencia clara, publicadas por el equipo que mantiene cada herramienta — **Evita si:** prefieres instalar un lote grande con un solo comando; mira `antigravity-awesome-skills`<br>
**Combina con:** [SkillSpector](human/fichas/skillspector.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/awesome-agent-skills.md) · [GitHub](https://github.com/VoltAgent/awesome-agent-skills)

#### 🧠 autoskills
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 7k<br>
**Qué es:** CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia. Inspecciona archivos de configuración y propone o instala skills relacionadas con el stack detectado.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx autoskills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres preparar un conjunto de skills adaptado al stack de un proyecto — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Combina con:** [Awesome Agent Skills](human/fichas/awesome-agent-skills.md)<br>
**Más:** [ficha completa](human/fichas/autoskills.md) · [GitHub](https://github.com/midudev/autoskills)

#### 🧠 gemini-skills
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 4.5k<br>
**Qué es:** Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini. Añaden instrucciones y referencias sobre las interacciones y patrones de desarrollo de Gemini.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/google-gemini/gemini-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** construyes aplicaciones que llaman a Gemini y necesitas contexto actualizado para el agente — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/gemini-skills.md) · [GitHub](https://github.com/google-gemini/gemini-skills)

#### 🧠 awesome-agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 3k<br>
**Qué es:** Directorio de herramientas y proyectos abiertos para construir y operar agentes de inteligencia artificial. Agrupa frameworks, agentes y entornos de desarrollo mediante enlaces a sus repositorios.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/kyrolabs/awesome-agents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres explorar alternativas de agentes antes de elegir una implementación — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/awesome-agents.md) · [GitHub](https://github.com/kyrolabs/awesome-agents)

### Metodologías y harness para agentes de código

#### 🧭 Agent Skills (Addy Osmani) ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 118k<br>
**Qué es:** Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. Instala las piezas que necesitas mediante la ruta de tu agente y revisa las dependencias de cada skill.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/addyosmani/agent-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres skills de ingeniería web de calidad para tu agente — **Evita si:** buscas un catálogo enorme de skills de todo tipo; mira `antigravity-awesome-skills`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/agent-skills.md) · [GitHub](https://github.com/addyosmani/agent-skills)

#### 📦 skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 325k<br>
**Qué es:** Muestra cómo se escribe una buena skill para agentes, con pocos ejemplos pero de alta calidad para usarlos como plantilla.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mattpocock/skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas referencias limpias y didácticas — **Evita si:** quieres un catálogo masivo (antigravity-awesome-skills)<br>
**Combina con:** [Awesome Agent Skills](human/fichas/awesome-agent-skills.md)<br>
**Más:** [ficha completa](human/fichas/skills.md) · [GitHub](https://github.com/mattpocock/skills)

#### 💪 superpowers
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 318k<br>
**Qué es:** Le da a tu agente de código un método de trabajo completo y coherente (planear, probar, revisar), no piezas sueltas.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/obra/superpowers/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres método, no fragmentos sueltos — **Evita si:** solo necesitas una skill aislada puntual<br>
**Combina con:** [Awesome Claude Code](human/fichas/awesome-claude-code.md) · [agent-toolkit](human/fichas/agent-toolkit.md)<br>
**Más:** [ficha completa](human/fichas/superpowers.md) · [GitHub](https://github.com/obra/superpowers)

#### 🌌 ECC
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 303k<br>
**Qué es:** Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto. Se integra con distintos agentes mediante rutas de instalación específicas; no es una plataforma de modelos locales.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/affaan-m/ECC/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** ejecutas agentes con acceso real a tu máquina y necesitas contención — **Evita si:** solo haces prompts de chat sin ejecución de código<br>
**Combina con:** [OpenHands](human/fichas/openhands.md) · [sandbox](human/fichas/sandbox.md) · [hermes-agent](human/fichas/hermes-agent.md)<br>
**Más:** [ficha completa](human/fichas/ecc.md) · [GitHub](https://github.com/affaan-m/ECC)

#### 🧠 andrej-karpathy-skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 233k<br>
**Qué es:** Ajusta el comportamiento de tu asistente con principios claros, sin atarte a una herramienta concreta.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres respuestas más útiles ya, sin curar prompts largos — **Evita si:** buscas skills ejecutables con scripts concretos<br>
**Combina con:** [Awesome Claude Code](human/fichas/awesome-claude-code.md) · [Context-Engineering](human/fichas/context-engineering.md)<br>
**Más:** [ficha completa](human/fichas/andrej-karpathy-skills.md) · [GitHub](https://github.com/multica-ai/andrej-karpathy-skills)

#### 🧭 Ponytail
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 191k<br>
**Qué es:** Empuja al agente a reutilizar, borrar y simplificar antes de añadir código nuevo. Reduce soluciones infladas y cambios innecesarios.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/DietrichGebert/ponytail/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente tiende a sobrecomplicar las soluciones — **Evita si:** necesitas una metodología completa de proyecto; mira `bmad-method`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [superpowers](human/fichas/superpowers.md) · [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md)<br>
**Más:** [ficha completa](human/fichas/ponytail.md) · [GitHub](https://github.com/DietrichGebert/ponytail)

#### 🧭 Spec Kit
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 150k<br>
**Qué es:** Te guía para escribir especificación, plan y tareas antes de que el agente programe. Funciona con Copilot, Claude Code, Gemini CLI y otros.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/github/spec-kit/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres que el agente siga una especificación antes de programar — **Evita si:** buscas roles completos de equipo ágil; mira `bmad-method`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [Gemini CLI](human/fichas/gemini-cli.md)<br>
**Más:** [ficha completa](human/fichas/spec-kit.md) · [GitHub](https://github.com/github/spec-kit)

#### 🧠 security-audit-skill
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 72.7k<br>
**Qué es:** Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados. Divide la revisión en reconocimiento, búsqueda por cobertura y verificación de candidatos antes del informe.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/cloudflare/security-audit-skill/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un proceso reproducible de revisión de seguridad con agentes — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Combina con:** [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/security-audit-skill.md) · [GitHub](https://github.com/cloudflare/security-audit-skill)

#### 🧭 BMAD Method
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 55.4k<br>
**Qué es:** Organiza el trabajo con IA en roles y documentos (brief, PRD, arquitectura, historias) que el agente de código sigue paso a paso. Útil para proyectos medianos donde los prompts sueltos se pierden.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un proceso completo de producto a código con agentes — **Evita si:** prefieres algo ligero centrado en especificaciones; mira `spec-kit`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/bmad-method.md) · [GitHub](https://github.com/bmad-code-org/BMAD-METHOD)

#### 🧠 codex-plugin-cc
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 35.1k<br>
**Qué es:** Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas. Añade comandos de revisión y delegación y conecta Claude Code con el runtime de Codex.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/openai/codex-plugin-cc/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres revisar código con Codex dentro de tu flujo de Claude Code — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/codex-plugin-cc.md) · [GitHub](https://github.com/openai/codex-plugin-cc)

#### 🛡️ SkillSpector
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 26.1k<br>
**Qué es:** Resuelve el riesgo de ejecutar skills de terceros sin revisión.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA/SkillSpector/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** instalas skills externas o curas catálogos — **Evita si:** solo usas skills propias de confianza<br>
**Combina con:** [Agentic Awesome Skills](human/fichas/antigravity-awesome-skills.md)<br>
**Más:** [ficha completa](human/fichas/skillspector.md) · [GitHub](https://github.com/NVIDIA/SkillSpector)

#### 🧠 SuperClaude_Framework
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 23.9k<br>
**Qué es:** Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code. Instala instrucciones y componentes de flujo para organizar fases del desarrollo asistido.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `pipx install superclaude` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres estructurar el trabajo de Claude Code con comandos y convenciones — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/superclaude-framework.md) · [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework)

#### 🧠 claude-token-efficient
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 6.2k<br>
**Qué es:** Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto. Añade reglas de concisión al contexto del proyecto e incluye perfiles y ejemplos de evaluación.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/drona23/claude-token-efficient/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres probar respuestas más breves en tareas con mucha salida de texto — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/claude-token-efficient.md) · [GitHub](https://github.com/drona23/claude-token-efficient)

#### 🧰 agent-toolkit
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 2.7k<br>
**Qué es:** Te da skills listas para tareas comunes, para que tu agente sea productivo desde el primer día.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/softaworks/agent-toolkit/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres productividad inmediata con tareas comunes — **Evita si:** buscas un método integral (superpowers)<br>
**Combina con:** [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/agent-toolkit.md) · [GitHub](https://github.com/softaworks/agent-toolkit)

#### 🧠 grok-plugin-claude-code
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 30<br>
**Qué es:** Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar. Envuelve el modo no interactivo de Grok CLI para ejecutar encargos y recuperar sus resultados.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Claude Code y quieres consultar Grok dentro de ese flujo — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/grok-plugin-claude-code.md) · [GitHub](https://github.com/zachdunn/grok-plugin-claude-code)

### Escritura y calidad de texto

#### 🧑 Humanizer ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 69.1k<br>
**Qué es:** Detecta 26 patrones típicos de la prosa de LLM (contrastes tipo 'no es X, es Y', cierres dramáticos, tríadas forzadas, frases de falsa profundidad, importancia inflada) y reescribe el texto sin cambiar lo que dice. Puede imitar tu estilo si le das una muestra y, sobre un archivo, solo toca la prosa: no el código, los datos ni el frontmatter.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/blader/humanizer/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** publicas textos redactados con IA y quieres que se lean como escritos por una persona — **Evita si:** quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop`<br>
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/humanizer.md) · [GitHub](https://github.com/blader/humanizer)

#### 🧹 Stop Slop
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 18.9k<br>
**Qué es:** Un SKILL.md con tres archivos de referencia (frases a eliminar, estructuras a evitar y ejemplos antes/después) que enseña a Claude o a cualquier LLM a quitar muletillas, contrastes binarios, fragmentos dramáticos, voz pasiva y otros patrones predecibles. Cierra con una rúbrica de cinco dimensiones para decidir si el texto necesita otra vuelta.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/hardikpandya/stop-slop/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt — **Evita si:** prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer`<br>
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/stop-slop.md) · [GitHub](https://github.com/hardikpandya/stop-slop)

### Skills de dominio: marketing, SEO y negocio

#### 📈 Marketing Skills ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 60.4k<br>
**Qué es:** Skills de Corey Haines para marketers técnicos y founders que trabajan con agentes de código: conversión, copywriting, SEO y SEO para IA, anuncios, emails, analítica y atribución, pricing, lanzamientos, retención y ventas. La skill product-marketing guarda el contexto de tu producto y las demás la consultan antes de actuar.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add coreyhaines31/marketingskills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** eres founder o marketer técnico y quieres que tu agente de código haga trabajo de growth con marcos probados — **Evita si:** necesitas una herramienta que envíe campañas o mida resultados; mira `mautic`, `listmonk` o `posthog`<br>
**Combina con:** [The Agency (agency-agents)](human/fichas/agency-agents.md) · [GEO-SEO Claude](human/fichas/geo-seo-claude.md) · [mautic](human/fichas/mautic.md) · [posthog](human/fichas/posthog.md)<br>
**Más:** [ficha completa](human/fichas/marketingskills.md) · [GitHub](https://github.com/coreyhaines31/marketingskills)

#### 🏢 The Agency (agency-agents)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 168k<br>
**Qué es:** Plantillas de subagente en Markdown agrupadas por divisiones, como una agencia completa: ingeniería, diseño, paid media, ventas, marketing, producto, testing, seguridad, soporte, finanzas, videojuegos y más. Cada agente define identidad, misión, flujo de trabajo, entregables con ejemplos y métricas de éxito, y hay runbooks que arman equipos para escenarios como un MVP o una campaña.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/msitarzewski/agency-agents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código — **Evita si:** solo necesitas skills de marketing y growth; mira `marketingskills`<br>
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [GEO-SEO Claude](human/fichas/geo-seo-claude.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/agency-agents.md) · [GitHub](https://github.com/msitarzewski/agency-agents)

#### 🧠 financial-services
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 41.3k<br>
**Qué es:** Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros. Reúne instrucciones y conectores para tareas como análisis de empresas y gestión de documentos financieros.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/financial-services/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar flujos financieros dentro del ecosistema de Claude — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/financial-services.md) · [GitHub](https://github.com/anthropics/financial-services)

#### 🌍 GEO-SEO Claude
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 11.7k<br>
**Qué es:** Añade a Claude Code comandos `/geo` que auditan un sitio para buscadores con IA (ChatGPT, Claude, Perplexity, Gemini, AI Overviews) sin dejar el SEO técnico: citabilidad del contenido, acceso de crawlers de IA en robots.txt, menciones de marca, datos estructurados y llms.txt. Genera informes para clientes en Markdown o PDF y lleva un pequeño CRM de prospectos.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres medir y mejorar cómo te citan los buscadores con IA, no solo tu posición en Google — **Evita si:** solo haces SEO clásico o no usas Claude Code; mira `marketingskills`<br>
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [The Agency (agency-agents)](human/fichas/agency-agents.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/geo-seo-claude.md) · [GitHub](https://github.com/zubair-trabzada/geo-seo-claude)

#### 🧠 social-media-research-skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 6.5k<br>
**Qué es:** Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. Guía al agente por flujos de investigación que consultan datos sociales y producen informes de negocio.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo de APIs o servicios<br>
**Comando documentado:** `npx skills add ScrapeCreators/social-media-research-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres investigación de contenido social desde un agente compatible con Agent Skills — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/social-media-research-skills.md) · [GitHub](https://github.com/ScrapeCreators/social-media-research-skills)

#### 📈 Arcads AI Video Skill Pack
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 1.7k<br>
**Qué es:** Repo de trabajo que convierte Claude Code o Cursor en un estudio de anuncios: genera videos UGC, presentaciones de producto, lookbooks y miniaturas de YouTube con los modelos de Arcads, y anuncios estáticos para Meta con 37 plantillas. Incluye pipelines multipaso (estilo Pixar o plastilina con ffmpeg), subtitulado con Whisper y HyperFrames, y publicación como anuncios pausados en Meta.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor — **Evita si:** quieres generar video con modelos abiertos sin servicio de pago; mira `comfyui` u `openmontage`<br>
**Combina con:** [HyperFrames](human/fichas/hyperframes.md) · [whisper](human/fichas/whisper.md) · [FFmpeg](human/fichas/ffmpeg.md) · [Marketing Skills](human/fichas/marketingskills.md)<br>
**Más:** [ficha completa](human/fichas/arcads-claude-code.md) · [GitHub](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial)

### Prompts y prompt engineering

#### 💡 Prompt Engineering Guide ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 80.1k<br>
**Qué es:** Explica técnicas de prompting, riesgos y aplicaciones con ejemplos y referencias a papers. Disponible en varios idiomas, incluido el español.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una referencia amplia de técnicas de prompting — **Evita si:** prefieres ejercicios prácticos con corrección; mira `prompt-eng-tutorial`<br>
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md)<br>
**Más:** [ficha completa](human/fichas/prompt-engineering-guide.md) · [GitHub](https://github.com/dair-ai/Prompt-Engineering-Guide)

#### 💡 Fabric ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 44.6k<br>
**Qué es:** Organiza prompts reutilizables (patterns) para tareas como resumir videos, extraer ideas o analizar textos. Se encadena con pipes en la terminal.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/danielmiessler/Fabric/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres prompts reutilizables desde la terminal — **Evita si:** buscas solo una lista de prompts para copiar; mira `prompts-chat`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [yt-dlp](human/fichas/yt-dlp.md)<br>
**Más:** [ficha completa](human/fichas/fabric.md) · [GitHub](https://github.com/danielmiessler/Fabric)

#### 💡 prompts.chat
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 177k<br>
**Qué es:** Reúne miles de prompts de rol y tarea para ChatGPT, Claude y otros, con buscador web. Puedes desplegar tu propia copia para tu organización.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/f/prompts.chat/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas prompts listos para copiar — **Evita si:** quieres ejecutarlos como comandos encadenables; mira `fabric`<br>
**Más:** [ficha completa](human/fichas/prompts-chat.md) · [GitHub](https://github.com/f/prompts.chat)

#### 🧠 system-prompts-and-models-of-ai-tools
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 145k<br>
**Qué es:** Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño. Organiza archivos por herramienta para consultar y comparar instrucciones y formatos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres investigar patrones de prompts utilizados por asistentes — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/system-prompts-and-models-of-ai-tools.md) · [GitHub](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

#### 💡 Anthropic's Prompt Engineering Tutorial
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 39.3k<br>
**Qué es:** Nueve capítulos con ejercicios sobre claridad, roles, ejemplos, razonamiento paso a paso y cómo evitar alucinaciones. Cada lección se practica contra la API de Claude.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/prompt-eng-interactive-tutorial/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres aprender prompts con práctica guiada — **Evita si:** buscas una guía amplia multi-modelo; mira `prompt-engineering-guide`<br>
**Combina con:** [Claude Cookbooks](human/fichas/claude-cookbooks.md)<br>
**Más:** [ficha completa](human/fichas/prompt-eng-tutorial.md) · [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial)

#### 🎯 prompt-master
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 16k<br>
**Qué es:** Te ayuda a escribir mejores prompts con meta-prompting reutilizable, como una capa por encima de cualquier IA.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/nidhinjs/prompt-master/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres dejar de re-promptear y acertar antes — **Evita si:** ya tienes prompts afinados y estables<br>
**Combina con:** [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md)<br>
**Más:** [ficha completa](human/fichas/prompt-master.md) · [GitHub](https://github.com/nidhinjs/prompt-master)

#### 🧠 ChatGPT_DAN
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 13.2k<br>
**Qué es:** Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT. Recopila variantes de instrucciones para estudiar intentos de alterar el comportamiento de asistentes.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/0xk1h0/ChatGPT_DAN/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres investigar prompts históricos y sus limitaciones — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/chatgpt-dan.md) · [GitHub](https://github.com/0xk1h0/ChatGPT_DAN)

#### 🧠 chatgpt_system_prompt
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 10.9k<br>
**Qué es:** Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts. Organiza documentos de referencia para estudiar estructuras de instrucciones y comportamiento de asistentes.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/LouisShark/chatgpt_system_prompt/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres comparar patrones de prompts como material de investigación — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/chatgpt-system-prompt.md) · [GitHub](https://github.com/LouisShark/chatgpt_system_prompt)

### Guías, cursos y cookbooks

#### 🎓 Generative AI for Beginners ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 124k<br>
**Qué es:** Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. Leer el curso no requiere una API; ejecutar cada práctica puede requerir servicios o modelos específicos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/generative-ai-for-beginners/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un curso estructurado y gratuito para empezar — **Evita si:** ya construyes con LLM y buscas recetas concretas; mira `openai-cookbook`<br>
**Combina con:** [AI Agents for Beginners](human/fichas/ai-agents-for-beginners.md) · [MCP for Beginners](human/fichas/mcp-for-beginners.md)<br>
**Más:** [ficha completa](human/fichas/generative-ai-for-beginners.md) · [GitHub](https://github.com/microsoft/generative-ai-for-beginners)

#### 🎓 AI Agents for Beginners ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 79.6k<br>
**Qué es:** Recorre desde qué es un agente hasta producción: frameworks, patrones de diseño (uso de herramientas, planificación, multiagente, metacognición), RAG agéntico, protocolos MCP, A2A y NLWeb, context engineering, memoria, agentes que usan el navegador, despliegue, agentes locales y seguridad. Cada lección trae README, video corto y ejemplos en Python.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/ai-agents-for-beginners/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** estás empezando con agentes y quieres un curso guiado, gratuito y disponible en español — **Evita si:** no quieres depender de Azure o ya llevas agentes a producción; mira `agents-towards-production` o `12-factor-agents`<br>
**Combina con:** [Generative AI for Beginners](human/fichas/generative-ai-for-beginners.md) · [Microsoft Agent Framework](human/fichas/agent-framework.md) · [MCP for Beginners](human/fichas/mcp-for-beginners.md)<br>
**Más:** [ficha completa](human/fichas/ai-agents-for-beginners.md) · [GitHub](https://github.com/microsoft/ai-agents-for-beginners)

#### 🎓 Awesome LLM Apps
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 145k<br>
**Qué es:** Repositorio de Shubham Saboo con plantillas de código abierto ordenadas por tipo: agentes simples de un solo archivo, agentes avanzados con herramientas y memoria, equipos multiagente, agentes de voz, agentes con MCP, RAG, chat con documentos y webs, fine-tuning y cursos rápidos de Google ADK y OpenAI Agents SDK. Según la app usa OpenAI, Anthropic, Google, xAI, DeepSeek o modelos abiertos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto — **Evita si:** buscas un curso estructurado con lecciones en orden; mira `ai-agents-for-beginners` o `generative-ai-for-beginners`<br>
**Combina con:** [streamlit](human/fichas/streamlit.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md) · [Agent Development Kit (ADK)](human/fichas/adk-python.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/awesome-llm-apps.md) · [GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps)

#### 🎓 OpenAI Cookbook
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 77.1k<br>
**Qué es:** Reúne recetas sobre embeddings, function calling, RAG, evaluación, agentes y voz. Sirve como referencia práctica al construir con la API de OpenAI.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/openai/openai-cookbook/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** construyes sobre la API de OpenAI y quieres ejemplos oficiales — **Evita si:** usas Claude como modelo principal; mira `claude-cookbooks`<br>
**Combina con:** [openai-python](human/fichas/openai-python.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md)<br>
**Más:** [ficha completa](human/fichas/openai-cookbook.md) · [GitHub](https://github.com/openai/openai-cookbook)

#### 🎓 Claude Cookbooks
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 54.7k<br>
**Qué es:** Notebooks y guías de Anthropic con código copiable para construir con Claude: clasificación, resumen, RAG (con Pinecone o embeddings de Voyage AI), tool use y un agente de atención al cliente, visión y extracción de formularios, subagentes, PDFs, salida JSON consistente, moderación, prompt caching y checklists de coste y latencia.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/claude-cookbooks/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar — **Evita si:** tu app usa la API de OpenAI; mira `openai-cookbook`<br>
**Combina con:** [Anthropic's Prompt Engineering Tutorial](human/fichas/prompt-eng-tutorial.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [promptfoo](human/fichas/promptfoo.md)<br>
**Más:** [ficha completa](human/fichas/claude-cookbooks.md) · [GitHub](https://github.com/anthropics/claude-cookbooks)

#### 🧠 ai-engineering-hub
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 41.9k<br>
**Qué es:** Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial. Cada carpeta presenta un ejemplo con sus dependencias y configuración propias.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/patchy631/ai-engineering-hub/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres aprender implementando ejemplos de ingeniería de IA — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/ai-engineering-hub.md) · [GitHub](https://github.com/patchy631/ai-engineering-hub)

#### 🧠 500-AI-Agents-Projects
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 39.9k<br>
**Qué es:** Colección de ideas, casos de uso y ejemplos de agentes de IA para distintos sectores y tareas. Organiza proyectos y enlaces que sirven como punto de partida para prototipos y aprendizaje.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas ejemplos de aplicaciones de agentes para adaptar a tu propio problema — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/500-ai-agents-projects.md) · [GitHub](https://github.com/ashishpatel26/500-AI-Agents-Projects)

#### 🎓 12-Factor Agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 27.2k<br>
**Qué es:** Ensayo de Dex Horthy (HumanLayer) que resume lo aprendido construyendo agentes para clientes reales: los productos que funcionan son sobre todo software determinista con pasos de LLM bien colocados. Cada factor (controlar tus prompts, tu ventana de contexto y tu flujo de control, pausar y reanudar, contactar a humanos con tool calls, agentes pequeños) tiene su capítulo con diagramas y ejemplos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/humanlayer/12-factor-agents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework — **Evita si:** buscas tutoriales con código ejecutable paso a paso; mira `agents-towards-production` o `ai-agents-for-beginners`<br>
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md) · [LangGraph](human/fichas/langgraph.md) · [AI SDK (Vercel)](human/fichas/vercel-ai.md)<br>
**Más:** [ficha completa](human/fichas/12-factor-agents.md) · [GitHub](https://github.com/humanlayer/12-factor-agents)

#### 🎓 Agents Towards Production
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 21.9k<br>
**Qué es:** Playbook de Nir Diamant (DiamantAI) con un tutorial por carpeta, en notebooks o scripts listos para ejecutar, sobre cada pieza del stack de un agente: tool calling seguro, datos web, RAG, memoria (Redis, Mem0, Cognee), Docker, FastAPI, GPU, MCP, A2A, LangGraph, seguridad, fine-tuning, trazas y evaluación. Muchos tutoriales los aportan empresas patrocinadoras.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/NirDiamant/agents-towards-production/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** ya tienes un prototipo de agente y necesitas resolver memoria, despliegue, seguridad u observabilidad — **Evita si:** estás empezando con agentes desde cero; mira `ai-agents-for-beginners`<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [mem0](human/fichas/mem0.md) · [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/agents-towards-production.md) · [GitHub](https://github.com/NirDiamant/agents-towards-production)

#### 🧠 claude-quickstarts
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 21k<br>
**Qué es:** Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora. Cada quickstart ofrece una aplicación base con código y pasos de configuración específicos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/claude-quickstarts/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres partir de un ejemplo oficial al integrar la API de Claude — **Evita si:** no utilizas un agente o flujo compatible con estas instrucciones<br>
**Más:** [ficha completa](human/fichas/claude-quickstarts.md) · [GitHub](https://github.com/anthropics/claude-quickstarts)

#### 🎓 Loop Engineering
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 11.8k<br>
**Qué es:** Propone dejar de escribir prompts aislados y diseñar ciclos con objetivo, verificación y puntuación para que el agente itere solo. Incluye starters y herramientas de línea de comandos.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/cobusgreyling/loop-engineering/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres que tu agente de código itere solo con criterios medibles — **Evita si:** solo necesitas una lista de skills; mira `awesome-agent-skills`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/loop-engineering.md) · [GitHub](https://github.com/cobusgreyling/loop-engineering)

#### 🧩 Context-Engineering
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 9.3k<br>
**Qué es:** Enseña de forma sistemática qué meter en el prompt y qué dejar fuera para que el modelo responda mejor.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/jasontang-ai/Context-Engineering/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres profundizar en contexto y RAG — **Evita si:** buscas skills ejecutables listas para copiar<br>
**Combina con:** [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md) · [headroom](human/fichas/headroom.md)<br>
**Más:** [ficha completa](human/fichas/context-engineering.md) · [GitHub](https://github.com/jasontang-ai/Context-Engineering)

---

## 🕸️ 3. Crear y usar agentes de IA

Agentes listos para trabajar y frameworks para construir los tuyos. Un agente de código se utiliza; un framework se integra dentro de una aplicación.

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

**⚖️ ¿Cuál elegir? — LangGraph, langchain, MetaGPT, AutoGen, crewAI, LlamaIndex, Agno**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [LangGraph](human/fichas/langgraph.md) | necesitas agentes con estado, control fino y persistencia | quieres algo mínimo para un agente simple; mira `smolagents` |
| [langchain](human/fichas/langchain.md) | quieres la base estándar con máximas integraciones | prefieres mínima abstracción o un solo proveedor sin cambiar |
| [MetaGPT](human/fichas/metagpt.md) | quieres estudiar un flujo multiagente basado en roles de desarrollo | un flujo determinista resuelve el problema sin un agente |
| [AutoGen](human/fichas/autogen.md) | mantienes un proyecto que ya usa AutoGen | empiezas algo nuevo; mira `agent-framework` |
| [crewAI](human/fichas/crewai.md) | quieres velocidad y un modelo mental simple de "equipo" | necesitas control de bajo nivel o orquestación muy custom |
| [LlamaIndex](human/fichas/llama-index.md) | tu proyecto gira alrededor de RAG sobre tus documentos | necesitas orquestación general de agentes; mira `langgraph` |
| [Agno](human/fichas/agno.md) | quieres un framework de agentes con memoria y API lista | necesitas grafos explícitos y controlables; mira `langgraph` |

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

**⚖️ ¿Cuál elegir? — STORM, gpt-researcher, open_deep_research, local-deep-research**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [STORM](human/fichas/storm.md) | necesitas informes largos y citados sobre un tema | quieres respuestas cortas con fuentes; mira `gpt-researcher` |
| [gpt-researcher](human/fichas/gpt-researcher.md) | necesitas research profundo citado | solo quieres una respuesta corta o un chat simple |
| [open_deep_research](human/fichas/open-deep-research.md) | quieres adaptar un agente de investigación construido con LangGraph | un flujo determinista resuelve el problema sin un agente |
| [local-deep-research](human/fichas/local-deep-research.md) | quieres investigar con un modelo local y conservar las fuentes consultadas | un flujo determinista resuelve el problema sin un agente |

**⚖️ ¿Cuál elegir? — E2B, NemoClaw, sandbox**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [E2B](human/fichas/e2b.md) | tu agente ejecuta código y necesitas aislarlo | solo necesitas ejecutar código localmente de confianza |
| [NemoClaw](human/fichas/nemoclaw.md) | quieres correr agentes potentes con aislamiento corporativo | solo necesitas un sandbox para ejecutar código; mira `e2b` |
| [sandbox](human/fichas/sandbox.md) | quieres aislar la ejecución de agentes y reproducibilidad | te basta correr local sin sandbox o no puedes asumir el overhead de Docker |

### Agentes de código (terminal e IDE)

#### 👨‍💻 OpenCode ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 227k<br>
**Qué es:** Ofrece una TUI cuidada, modo cliente-servidor, LSP y agentes configurables. Sirve si quieres un agente libre de proveedor.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/anomalyco/opencode/blob/dev/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un agente de código abierto y multi-modelo — **Evita si:** prefieres la experiencia oficial de un proveedor; mira `claude-code` o `codex`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md) · [Awesome Agent Skills](human/fichas/awesome-agent-skills.md)<br>
**Más:** [ficha completa](human/fichas/opencode.md) · [GitHub](https://github.com/anomalyco/opencode)

#### 👨‍💻 Claude Code ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 156k<br>
**Qué es:** Lee y edita archivos, ejecuta comandos, hace commits y abre PRs a partir de instrucciones en lenguaje natural. Se extiende con skills, plugins, subagentes, hooks y servidores MCP.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `winget install Anthropic.ClaudeCode` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres el agente de código más capaz para tareas largas en tu repo — **Evita si:** necesitas un agente totalmente abierto y multi-modelo; mira `opencode`<br>
**Combina con:** [superpowers](human/fichas/superpowers.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [claude-mem](human/fichas/claude-mem.md) · [Context7](human/fichas/context7.md)<br>
**Más:** [ficha completa](human/fichas/claude-code.md) · [GitHub](https://github.com/anthropics/claude-code)

#### 👨‍💻 Codex CLI
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 135k<br>
**Qué es:** Lee tu repositorio, propone y aplica cambios y ejecuta comandos dentro de un sandbox. Usa AGENTS.md para el contexto del proyecto y admite MCP.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g @openai/codex` (comprobar los pasos completos en la ficha).<br>
**Elige si:** usas ChatGPT u OpenAI y quieres un agente abierto en terminal — **Evita si:** trabajas con Claude como modelo principal; mira `claude-code`<br>
**Combina con:** [Agent Skills (Addy Osmani)](human/fichas/agent-skills.md) · [Spec Kit](human/fichas/spec-kit.md) · [Context7](human/fichas/context7.md)<br>
**Más:** [ficha completa](human/fichas/codex.md) · [GitHub](https://github.com/openai/codex)

#### 👨‍💻 Gemini CLI
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 109k<br>
**Qué es:** Programa, investiga y automatiza tareas desde la terminal con contexto de millones de tokens y búsqueda de Google integrada. Admite MCP y extensiones.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx @google/gemini-cli` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres un agente de terminal potente con cuota gratuita — **Evita si:** buscas el agente con mejor desempeño en tareas largas; mira `claude-code`<br>
**Combina con:** [Stitch Skills](human/fichas/stitch-skills.md) · [Context7](human/fichas/context7.md)<br>
**Más:** [ficha completa](human/fichas/gemini-cli.md) · [GitHub](https://github.com/google-gemini/gemini-cli)

#### 🙌 OpenHands
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 93.5k<br>
**Qué es:** El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/OpenHands/OpenHands/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un agente que "haga", no solo hable — **Evita si:** solo necesitas chat/RAG o no puedes correr Docker<br>
**Combina con:** [ECC](human/fichas/ecc.md) · [sandbox](human/fichas/sandbox.md)<br>
**Más:** [ficha completa](human/fichas/openhands.md) · [GitHub](https://github.com/OpenHands/OpenHands)

#### 👨‍💻 Cline
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 71.6k<br>
**Qué es:** Planifica, edita archivos, ejecuta comandos y usa el navegador pidiendo aprobación en cada paso. Admite MCP y casi cualquier proveedor.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm i -g cline` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres un agente dentro de VS Code con control de cada paso — **Evita si:** trabajas solo en terminal; mira `opencode`<br>
**Combina con:** [Context7](human/fichas/context7.md) · [Playwright MCP](human/fichas/playwright-mcp.md)<br>
**Más:** [ficha completa](human/fichas/cline.md) · [GitHub](https://github.com/cline/cline)

#### 👨‍💻 Open Interpreter
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 68.9k<br>
**Qué es:** Ejecuta código y comandos en tu máquina para cumplir tareas descritas en lenguaje natural. Su versión actual se enfoca en modelos abiertos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/openinterpreter/openinterpreter/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un agente que ejecute código usando modelos abiertos — **Evita si:** buscas un agente maduro para repos grandes; mira `opencode`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [E2B](human/fichas/e2b.md)<br>
**Más:** [ficha completa](human/fichas/open-interpreter.md) · [GitHub](https://github.com/openinterpreter/openinterpreter)

#### 👨‍💻 T3 Code
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 60.6k<br>
**Qué es:** No sustituye al agente: orquesta Claude Code, Codex y otros desde una UI cómoda, también en el móvil. Útil para lanzar y revisar sesiones a distancia.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx t3@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** usas varios agentes de código y quieres controlarlos desde una UI — **Evita si:** solo usas un agente en la terminal<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [OpenCode](human/fichas/opencode.md)<br>
**Más:** [ficha completa](human/fichas/t3code.md) · [GitHub](https://github.com/pingdotgg/t3code)

#### 👨‍💻 goose
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 56.6k<br>
**Qué es:** Funciona como app de escritorio o CLI y va más allá del código: automatiza tareas de desarrollo y de sistema con extensiones MCP. Nacido en Block.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/aaif-goose/goose/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un agente abierto con app de escritorio y MCP — **Evita si:** solo programas en terminal y quieres el más usado; mira `opencode`<br>
**Combina con:** [Playwright MCP](human/fichas/playwright-mcp.md) · [GitHub MCP Server](human/fichas/github-mcp-server.md)<br>
**Más:** [ficha completa](human/fichas/goose.md) · [GitHub](https://github.com/aaif-goose/goose)

#### 👨‍💻 Aider
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 50.1k<br>
**Qué es:** Le pides cambios en lenguaje natural y Aider edita los archivos y confirma cada cambio en Git. Funciona con casi cualquier modelo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Aider-AI/aider/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un agente sencillo que trabaje con Git paso a paso — **Evita si:** necesitas autonomía en tareas largas; mira `claude-code`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/aider.md) · [GitHub](https://github.com/Aider-AI/aider)

#### 👨‍💻 Continue
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 36.5k<br>
**Qué es:** Integra chat, edición y autocompletado en el IDE con cualquier modelo, y permite ejecutar comprobaciones de IA en los PRs.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/continuedev/continue/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres autocompletado y chat en el IDE con modelos a elección — **Evita si:** buscas un agente autónomo para tareas largas; mira `cline`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/continue.md) · [GitHub](https://github.com/continuedev/continue)

#### 🕸️ openclaude
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 34.4k<br>
**Qué es:** Agente de código abierto para terminal que conecta proveedores remotos y modelos locales con herramientas y MCP. Mantiene una conversación de desarrollo con streaming, comandos y herramientas sobre el workspace.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g @twigpine/openclaude@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres evaluar un agente de terminal compatible con varios backends — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/openclaude.md) · [GitHub](https://github.com/Twigpine/openclaude)

#### 👨‍💻 SWE-agent
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 20.8k<br>
**Qué es:** Resuelve issues reales con el modelo que elijas y sirve como base de investigación en agentes de software. También tiene usos en ciberseguridad y retos de programación.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/SWE-agent/SWE-agent/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** investigas o automatizas la resolución de issues — **Evita si:** quieres un asistente diario en tu terminal; mira `claude-code`<br>
**Combina con:** [SWE-bench](human/fichas/swe-bench.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/swe-agent.md) · [GitHub](https://github.com/SWE-agent/SWE-agent)

#### 🕸️ opencode
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 13.9k<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** Agente de código en Go del antiguo proyecto opencode-ai, archivado y continuado bajo el nombre Crush. Conserva una interfaz de terminal y el historial del agente original para consulta.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/opencode-ai/opencode/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas estudiar la implementación histórica de OpenCode en Go — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/opencode-legacy.md) · [GitHub](https://github.com/opencode-ai/opencode)

#### 🕸️ MiMo-Code
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 13.8k<br>
**Qué es:** Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente. Mantiene el contexto del proyecto y usa herramientas para ejecutar tareas de desarrollo desde una conversación.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres evaluar el agente de código del ecosistema Xiaomi MiMo — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/mimo-code.md) · [GitHub](https://github.com/XiaomiMiMo/MiMo-Code)

#### 👨‍💻 Open SWE
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 11.2k<br>
**Qué es:** Trabaja en segundo plano a partir de issues o mensajes, planifica, programa en un sandbox y abre PRs. Inspirado en los agentes internos de empresas como Stripe o Ramp.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/langchain-ai/open-swe/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres construir el agente de código interno de tu empresa — **Evita si:** solo quieres un agente para tu terminal; mira `claude-code`<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [E2B](human/fichas/e2b.md)<br>
**Más:** [ficha completa](human/fichas/open-swe.md) · [GitHub](https://github.com/langchain-ai/open-swe)

#### 🕸️ OpenCursor
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.1k<br>
**Qué es:** Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos. Integra conversación y acciones sobre el workspace con proveedores remotos o locales y herramientas MCP.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/PawanOsman/OpenCursor/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres evaluar un agente de código integrado en VS Code — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/opencursor.md) · [GitHub](https://github.com/PawanOsman/OpenCursor)

### Frameworks de agentes en Python

#### 🐍 LangGraph ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 45k<br>
**Qué es:** Modela agentes y flujos multiagente como grafos de nodos con estado compartido y checkpoints. Pensado para agentes de producción que deben ser controlables y recuperables.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -U langgraph` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas agentes con estado, control fino y persistencia — **Evita si:** quieres algo mínimo para un agente simple; mira `smolagents`<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/langgraph.md) · [GitHub](https://github.com/langchain-ai/langgraph)

#### 🦜 langchain
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 150k<br>
**Qué es:** Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv add langchain` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres la base estándar con máximas integraciones — **Evita si:** prefieres mínima abstracción o un solo proveedor sin cambiar<br>
**Combina con:** [langflow](human/fichas/langflow.md) · [langfuse](human/fichas/langfuse.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/langchain.md) · [GitHub](https://github.com/langchain-ai/langchain)

#### 🕸️ MetaGPT
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 71.3k<br>
**Qué es:** Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. Asigna responsabilidades y artefactos a agentes que colaboran sobre un encargo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install --upgrade metagpt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres estudiar un flujo multiagente basado en roles de desarrollo — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/metagpt.md) · [GitHub](https://github.com/FoundationAgents/MetaGPT)

#### 🐍 AutoGen
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 61.8k<br>
**Qué es:** Popularizó los sistemas multiagente que conversan para resolver tareas. Microsoft recomienda usar Agent Framework para proyectos nuevos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/autogen/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** mantienes un proyecto que ya usa AutoGen — **Evita si:** empiezas algo nuevo; mira `agent-framework`<br>
**Combina con:** [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/autogen.md) · [GitHub](https://github.com/microsoft/autogen)

#### 👥 crewAI
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 60.9k<br>
**Qué es:** Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/crewAIInc/crewAI/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres velocidad y un modelo mental simple de "equipo" — **Evita si:** necesitas control de bajo nivel o orquestación muy custom<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [mem0](human/fichas/mem0.md)<br>
**Más:** [ficha completa](human/fichas/crewai.md) · [GitHub](https://github.com/crewAIInc/crewAI)

#### 🐍 LlamaIndex
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 52.9k<br>
**Qué es:** Ofrece cargadores para cientos de fuentes, índices, motores de consulta y agentes centrados en documentos. Su plataforma LlamaParse procesa PDFs complejos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install llama-index` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tu proyecto gira alrededor de RAG sobre tus documentos — **Evita si:** necesitas orquestación general de agentes; mira `langgraph`<br>
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [Docling](human/fichas/docling.md) · [Ragas](human/fichas/ragas.md)<br>
**Más:** [ficha completa](human/fichas/llama-index.md) · [GitHub](https://github.com/run-llama/llama_index)

#### 🐍 Agno
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 43.2k<br>
**Qué es:** Construye agentes con memoria, RAG y herramientas, y sírvelos como API con su plataforma. Antes se llamaba Phidata.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/agno-agi/agno/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un framework de agentes con memoria y API lista — **Evita si:** necesitas grafos explícitos y controlables; mira `langgraph`<br>
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [mem0](human/fichas/mem0.md)<br>
**Más:** [ficha completa](human/fichas/agno.md) · [GitHub](https://github.com/agno-agi/agno)

#### 🐍 DSPy
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 39.1k<br>
**Qué es:** Defines módulos con firmas de entrada y salida y DSPy optimiza automáticamente los prompts y ejemplos con tus métricas. Útil para pipelines que deben mejorar con datos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install dspy` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres optimizar prompts de forma sistemática con datos — **Evita si:** solo necesitas una llamada simple al modelo<br>
**Combina con:** [Ragas](human/fichas/ragas.md) · [MLflow](human/fichas/mlflow.md)<br>
**Más:** [ficha completa](human/fichas/dspy.md) · [GitHub](https://github.com/stanfordnlp/dspy)

#### 🐍 Deep Agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 31.3k<br>
**Qué es:** Da a cualquier modelo las capacidades de los agentes profundos (planificar, delegar, usar archivos) sin construirlas tú. Cada pieza se puede extender o reemplazar.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv add deepagents` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres un agente potente sin diseñar el bucle desde cero — **Evita si:** necesitas control total del grafo; usa `langgraph` directamente<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/deepagents.md) · [GitHub](https://github.com/langchain-ai/deepagents)

#### 🐍 OpenAI Agents SDK
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.7k<br>
**Qué es:** Define agentes con instrucciones y herramientas, pasa el control entre ellos y añade validaciones. Funciona con modelos de OpenAI y otros compatibles.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install openai-agents` (comprobar los pasos completos en la ficha).<br>
**Elige si:** usas OpenAI y quieres agentes multiagente con poco código — **Evita si:** necesitas control de estado avanzado; mira `langgraph`<br>
**Combina con:** [openai-python](human/fichas/openai-python.md) · [FastMCP](human/fichas/fastmcp.md)<br>
**Más:** [ficha completa](human/fichas/openai-agents-python.md) · [GitHub](https://github.com/openai/openai-agents-python)

#### 🐍 smolagents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.4k<br>
**Qué es:** Sus agentes expresan las acciones como código en vez de JSON, lo que reduce pasos y errores. El núcleo cabe en unas mil líneas.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/huggingface/smolagents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un agente simple y transparente en Python — **Evita si:** necesitas flujos con estado y aprobación humana; mira `langgraph`<br>
**Combina con:** [E2B](human/fichas/e2b.md) · [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/smolagents.md) · [GitHub](https://github.com/huggingface/smolagents)

#### 🐍 Haystack
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 27k<br>
**Qué es:** Compone pipelines modulares de recuperación, generación y agentes con componentes intercambiables. Muy usado en búsqueda empresarial.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install haystack-ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres pipelines de RAG explícitos y listos para producción — **Evita si:** buscas el ecosistema más grande de integraciones; mira `llama-index`<br>
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/haystack.md) · [GitHub](https://github.com/deepset-ai/haystack)

#### 🐍 Agent Development Kit (ADK)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 22.2k<br>
**Qué es:** Define agentes y sistemas multiagente con herramientas, memoria y evaluación, con interfaz web de pruebas incluida. Se despliega fácil en Google Cloud.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install google-adk` (comprobar los pasos completos en la ficha).<br>
**Elige si:** trabajas con Gemini o Google Cloud — **Evita si:** tu stack es OpenAI; mira `openai-agents-python`<br>
**Combina con:** [Gemini CLI](human/fichas/gemini-cli.md) · [FastMCP](human/fichas/fastmcp.md)<br>
**Más:** [ficha completa](human/fichas/adk-python.md) · [GitHub](https://github.com/google/adk-python)

#### 🐍 Pydantic AI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 21.2k<br>
**Qué es:** Construye agentes con salidas validadas, herramientas tipadas e inyección de dependencias, al estilo FastAPI. Incluye evaluación y observabilidad con Logfire.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/pydantic/pydantic-ai/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres agentes tipados y validados en Python — **Evita si:** necesitas grafos complejos con persistencia; mira `langgraph`<br>
**Combina con:** [langfuse](human/fichas/langfuse.md) · [FastMCP](human/fichas/fastmcp.md)<br>
**Más:** [ficha completa](human/fichas/pydantic-ai.md) · [GitHub](https://github.com/pydantic/pydantic-ai)

#### 🤝 ag2
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 5.1k<br>
**Qué es:** Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install ag2` (comprobar los pasos completos en la ficha).<br>
**Elige si:** construyes multiagente serio en Python — **Evita si:** te basta un agente único o quieres orquestación visual<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/ag2.md) · [GitHub](https://github.com/ag2ai/ag2)

#### 🕸️ awesome-LangGraph
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 2k<br>
**Qué es:** Es una lista curada, no una herramienta ejecutable.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/vonzosten/awesome-LangGraph/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** construyes con LangGraph y quieres patrones de referencia — **Evita si:** no usas ese ecosistema<br>
**Combina con:** [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/awesome-langgraph.md) · [GitHub](https://github.com/vonzosten/awesome-LangGraph)

#### 🐍 LangGraph Supervisor
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.7k<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** Facilitaba el patrón supervisor en sistemas multiagente. LangChain ahora recomienda implementar ese patrón directamente con herramientas.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install langgraph-supervisor` (comprobar los pasos completos en la ficha).<br>
**Elige si:** mantienes código que ya la usa — **Evita si:** empiezas un proyecto nuevo; usa el patrón con herramientas en `langgraph`<br>
**Más:** [ficha completa](human/fichas/langgraph-supervisor-py.md) · [GitHub](https://github.com/langchain-ai/langgraph-supervisor-py)

### Frameworks en TypeScript y multi-lenguaje

#### 🟦 Mastra ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 29.5k<br>
**Qué es:** Reúne en un solo paquete agentes con memoria, workflows con estado, RAG, evals y un playground local. Pensado para equipos web que trabajan en TypeScript.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm create mastra@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tu equipo trabaja en TypeScript y quiere agentes completos — **Evita si:** trabajas en Python; mira `langgraph` o `pydantic-ai`<br>
**Combina con:** [CopilotKit](human/fichas/copilotkit.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/mastra.md) · [GitHub](https://github.com/mastra-ai/mastra)

#### 🟦 Semantic Kernel
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 28.8k<br>
**Qué es:** Pensado para empresas que ya usan .NET o Java y quieren añadir IA con patrones conocidos. Su evolución para agentes es Microsoft Agent Framework.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install semantic-kernel` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tu app es .NET o Java y quieres IA integrada — **Evita si:** empiezas un sistema de agentes nuevo; mira `agent-framework`<br>
**Más:** [ficha completa](human/fichas/semantic-kernel.md) · [GitHub](https://github.com/microsoft/semantic-kernel)

#### 🟦 AI SDK (Vercel)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 28k<br>
**Qué es:** Unifica la llamada a decenas de proveedores con una API común y trae hooks de React para chat con streaming. Es la base de muchos frameworks de agentes en TS.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** construyes una app web con IA en TypeScript — **Evita si:** necesitas agentes complejos con memoria y workflows; mira `mastra`<br>
**Combina con:** [ui](human/fichas/ui.md) · [assistant-ui](human/fichas/assistant-ui.md)<br>
**Más:** [ficha completa](human/fichas/vercel-ai.md) · [GitHub](https://github.com/vercel/ai)

#### 🟦 Microsoft Agent Framework
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 14.7k<br>
**Qué es:** Une la simplicidad de AutoGen con las capacidades empresariales de Semantic Kernel: workflows con estado, observabilidad y despliegue en Azure.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install agent-framework` (comprobar los pasos completos en la ficha).<br>
**Elige si:** trabajas en el ecosistema Microsoft o .NET — **Evita si:** quieres el ecosistema open source más grande; mira `langgraph`<br>
**Más:** [ficha completa](human/fichas/agent-framework.md) · [GitHub](https://github.com/microsoft/agent-framework)

#### 🕸️ langchain4j
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 13.4k<br>
**Qué es:** Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM. Ofrece interfaces comunes para proveedores y conectores y se integra con frameworks de Java.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/langchain4j/langchain4j/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu aplicación usa Java y necesita integrar modelos o recuperación de documentos — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/langchain4j.md) · [GitHub](https://github.com/langchain4j/langchain4j)

#### 🟦 LangGraph.js
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 3.4k<br>
**Qué es:** Lleva el modelo de grafos con estado, checkpoints y human-in-the-loop de LangGraph al ecosistema JavaScript.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install @langchain/langgraph @langchain/core` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres el modelo de LangGraph en TypeScript — **Evita si:** buscas una experiencia TS más integrada; mira `mastra`<br>
**Combina con:** [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/langgraphjs.md) · [GitHub](https://github.com/langchain-ai/langgraphjs)

### Builders visuales y plataformas de agentes

#### 🧩 Sim ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.1k<br>
**Qué es:** Diseña agentes conectando bloques en un canvas, prueba en vivo y despliega como API o chat. Open source y auto-hospedable.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/simstudioai/sim/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un constructor visual de agentes moderno y abierto — **Evita si:** prefieres automatización general con cientos de apps; mira `n8n`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/sim.md) · [GitHub](https://github.com/simstudioai/sim)

#### 🧩 AutoGPT
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 188k<br>
**Qué es:** El famoso proyecto de agentes autónomos evolucionó a una plataforma con editor de bloques, marketplace y servidor para agentes que corren en segundo plano.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Significant-Gravitas/AutoGPT/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres agentes continuos con un editor visual propio — **Evita si:** buscas algo ligero y fácil de operar; mira `sim` o `flowise`<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/autogpt.md) · [GitHub](https://github.com/Significant-Gravitas/AutoGPT)

#### 🧱 dify
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 161k<br>
**Qué es:** Combina orquestación de prompts, RAG, agentes, workflows y observabilidad en un mismo producto autoalojable.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/langgenius/dify/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una app IA completa autoalojada — **Evita si:** solo necesitas una librería o un prototipo puntual<br>
**Combina con:** [langflow](human/fichas/langflow.md) · [Flowise](human/fichas/flowise.md)<br>
**Más:** [ficha completa](human/fichas/dify.md) · [GitHub](https://github.com/langgenius/dify)

#### 🔗 langflow
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 157k<br>
**Qué es:** Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código Python.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install langflow` (comprobar los pasos completos en la ficha).<br>
**Elige si:** prefieres construir en visual sobre LangChain — **Evita si:** quieres todo en código o no usas LangChain<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [dify](human/fichas/dify.md)<br>
**Más:** [ficha completa](human/fichas/langflow.md) · [GitHub](https://github.com/langflow-ai/langflow)

#### 🌊 Flowise
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 55.6k<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** Constructor visual para diseñar aplicaciones de IA conectando modelos, herramientas, memoria y fuentes de datos. La instalación de Flowise y el acceso al modelo son decisiones separadas.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g flowise` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres un prototipo visual ya, en stack JS — **Evita si:** necesitas plataforma completa con RAG/observabilidad (dify)<br>
**Combina con:** [dify](human/fichas/dify.md) · [langflow](human/fichas/langflow.md)<br>
**Más:** [ficha completa](human/fichas/flowise.md) · [GitHub](https://github.com/FlowiseAI/Flowise)

### Asistentes autónomos y equipos de agentes

#### 🦾 OpenClaw ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 394k<br>
**Qué es:** Un solo operador, muchas superficies: el asistente vive en tu equipo, tiene memoria, ejecuta tareas reales y responde por los canales que ya usas. Es uno de los proyectos de IA más populares de GitHub.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g openclaw@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres un asistente personal que actúe por tus canales de chat — **Evita si:** necesitas un agente para tu empresa con varios usuarios; mira `hermes-agent`<br>
**Combina con:** [NemoClaw](human/fichas/nemoclaw.md) · [claude-mem](human/fichas/claude-mem.md)<br>
**Más:** [ficha completa](human/fichas/openclaw.md) · [GitHub](https://github.com/openclaw/openclaw)

#### ☤ hermes-agent
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 263k<br>
**Qué es:** Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/NousResearch/hermes-agent/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres agentes locales con UI y memoria persistente — **Evita si:** prefieres orquestación en nube o no quieres compilar Tauri<br>
**Combina con:** [ECC](human/fichas/ecc.md) · [odysseus](human/fichas/odysseus.md)<br>
**Más:** [ficha completa](human/fichas/hermes-agent.md) · [GitHub](https://github.com/NousResearch/hermes-agent)

#### 🕸️ paperclip
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 114k<br>
**Qué es:** Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. Conecta distintos runtimes y coordina sus encargos y costes desde una aplicación central.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/paperclipai/paperclip/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas coordinar varios agentes y seguir su trabajo en un panel — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/paperclip.md) · [GitHub](https://github.com/paperclipai/paperclip)

#### 🐝 ruflo
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 81.7k<br>
**Qué es:** Orquesta swarms de agentes especializados a escala.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g ruflo@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** orquestas muchos agentes a escala y quieres rendimiento — **Evita si:** solo necesitas 1-2 agentes o no usas Claude Code/Codex<br>
**Combina con:** [mem0](human/fichas/mem0.md) · [ECC](human/fichas/ecc.md)<br>
**Más:** [ficha completa](human/fichas/ruflo.md) · [GitHub](https://github.com/ruvnet/ruflo)

#### 🦾 DeepTutor
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 59.2k<br>
**Qué es:** Resuelve dudas, genera ejercicios y guía el estudio con RAG sobre tu material y memoria del alumno. Es un producto educativo, no un orquestador genérico.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/HKUDS/DeepTutor/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un tutor con IA sobre tu propio material — **Evita si:** buscas un framework para construir agentes; mira `langgraph`<br>
**Combina con:** [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/deeptutor.md) · [GitHub](https://github.com/HKUDS/DeepTutor)

#### 🧑‍🤝‍🧑 multica
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 56.1k<br>
**Qué es:** Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/multica-ai/multica/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** mezclas trabajo humano y agentes en un mismo flujo — **Evita si:** quieres automatización 100% headless o un producto maduro<br>
**Combina con:** [ruflo](human/fichas/ruflo.md) · [chatwoot](human/fichas/chatwoot.md)<br>
**Más:** [ficha completa](human/fichas/multica.md) · [GitHub](https://github.com/multica-ai/multica)

#### 🦾 Mercury Agent
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 3.9k<br>
**Qué es:** Recuerda lo importante, pide permiso antes de actuar y trae 31 herramientas, tableros kanban y skills extensibles, con datos en SQLite.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un asistente personal ligero con permisos claros — **Evita si:** buscas el ecosistema más grande; mira `openclaw`<br>
**Combina con:** [claude-mem](human/fichas/claude-mem.md)<br>
**Más:** [ficha completa](human/fichas/mercury-agent.md) · [GitHub](https://github.com/cosmicstack-labs/mercury-agent)

#### 🕸️ social-media-agent
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 3k<br>
**Qué es:** Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas. Usa un flujo de LangGraph para investigar el enlace, redactar y solicitar aprobación de la publicación.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/langchain-ai/social-media-agent/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres preparar publicaciones para X o LinkedIn con una etapa de aprobación — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Combina con:** [LangGraph.js](human/fichas/langgraphjs.md)<br>
**Más:** [ficha completa](human/fichas/social-media-agent.md) · [GitHub](https://github.com/langchain-ai/social-media-agent)

### Agentes de research autónomo

#### 🔬 autoresearch ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 100k<br>
**Qué es:** Proyecto pequeño y exploratorio de Karpathy, más que una herramienta pulida.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/karpathy/autoresearch/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** experimentas con research iterativo o quieres un punto de partida — **Evita si:** quieres salida pulida y lista (gpt-researcher)<br>
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [crawl4ai](human/fichas/crawl4ai.md)<br>
**Más:** [ficha completa](human/fichas/autoresearch.md) · [GitHub](https://github.com/karpathy/autoresearch)

#### 🦌 deer-flow
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 85.3k<br>
**Qué es:** Coordina tareas complejas delegando en agentes especializados.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/bytedance/deer-flow/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un orquestador completo y extensible — **Evita si:** buscas algo minimalista o sin Docker<br>
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/deer-flow.md) · [GitHub](https://github.com/bytedance/deer-flow)

#### 🔎 STORM
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 31.9k<br>
**Qué es:** Simula conversaciones entre perspectivas para hacer preguntas, busca fuentes y redacta un artículo estructurado y citado. Útil para informes de fondo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/stanford-oval/storm/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas informes largos y citados sobre un tema — **Evita si:** quieres respuestas cortas con fuentes; mira `gpt-researcher`<br>
**Combina con:** [SearXNG](human/fichas/searxng.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/storm.md) · [GitHub](https://github.com/stanford-oval/storm)

#### 🔍 gpt-researcher
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.7k<br>
**Qué es:** Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install gpt-researcher` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas research profundo citado — **Evita si:** solo quieres una respuesta corta o un chat simple<br>
**Combina con:** [firecrawl](human/fichas/firecrawl.md) · [browser-use](human/fichas/browser-use.md)<br>
**Más:** [ficha completa](human/fichas/gpt-researcher.md) · [GitHub](https://github.com/assafelovic/gpt-researcher)

#### 🕸️ open_deep_research
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 12.7k<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP. Organiza ciclos de planificación, búsqueda y síntesis mediante un grafo de investigación.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/langchain-ai/open_deep_research/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres adaptar un agente de investigación construido con LangGraph — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Combina con:** [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/open-deep-research.md) · [GitHub](https://github.com/langchain-ai/open_deep_research)

#### 🕸️ local-deep-research
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 9.6k<br>
**Qué es:** Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. Itera entre preguntas, búsquedas y síntesis y permite configurar motores de búsqueda y proveedores de modelos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install local-deep-research` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres investigar con un modelo local y conservar las fuentes consultadas — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/local-deep-research.md) · [GitHub](https://github.com/LearningCircuit/local-deep-research)

### Infraestructura: sandboxes, herramientas y protocolos

#### 🛠️ Composio ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 31.1k<br>
**Qué es:** Da a cualquier agente herramientas listas para Gmail, Slack, GitHub, Notion y cientos más, gestionando OAuth por ti. Funciona con los principales frameworks y por MCP.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install composio` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tu agente necesita actuar en muchas apps SaaS — **Evita si:** quieres todo auto-hospedado sin servicio externo<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md) · [Mastra](human/fichas/mastra.md)<br>
**Más:** [ficha completa](human/fichas/composio.md) · [GitHub](https://github.com/ComposioHQ/composio)

#### 🛠️ E2B ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 14.9k<br>
**Qué es:** Arranca microVMs aisladas en milisegundos donde el agente puede ejecutar código, instalar paquetes o usar un escritorio. Muy usado para intérpretes de código y agentes de datos.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo de APIs o servicios<br>
**Comando documentado:** `pip install e2b-code-interpreter` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tu agente ejecuta código y necesitas aislarlo — **Evita si:** solo necesitas ejecutar código localmente de confianza<br>
**Combina con:** [smolagents](human/fichas/smolagents.md) · [Open SWE](human/fichas/open-swe.md)<br>
**Más:** [ficha completa](human/fichas/e2b.md) · [GitHub](https://github.com/e2b-dev/E2B)

#### 🕸️ agent-desktop
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 23.8k<br>
**Qué es:** CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. Expone elementos de la interfaz como referencias sobre las que el agente puede actuar y comprobar resultados.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install -g agent-desktop` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas automatizar aplicaciones nativas desde un agente — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Combina con:** [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/agent-desktop.md) · [GitHub](https://github.com/vercel-labs/agent-desktop)

#### 🛠️ NemoClaw
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 23k<br>
**Qué es:** Ejecuta agentes populares dentro de los sandboxes de NVIDIA OpenShell con inferencia gestionada y políticas de seguridad. Pensado para empresas.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA/NemoClaw/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres correr agentes potentes con aislamiento corporativo — **Evita si:** solo necesitas un sandbox para ejecutar código; mira `e2b`<br>
**Combina con:** [OpenClaw](human/fichas/openclaw.md) · [hermes-agent](human/fichas/hermes-agent.md) · [Nemotron (NVIDIA)](human/fichas/nemotron.md)<br>
**Más:** [ficha completa](human/fichas/nemoclaw.md) · [GitHub](https://github.com/NVIDIA/NemoClaw)

#### 🕸️ codex-chatgpt-web
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 15.7k<br>
**Qué es:** Integración de terceros que conecta una sesión de ChatGPT Web con el selector de modelos y herramientas de Codex. Un launcher usa la sesión de la cuenta y enlaza herramientas mediante MCP para conservar el contexto de la tarea.<br>
**Acceso:** API: por confirmar · Coste por confirmar<br>
**Arranque:** [Instrucciones originales](https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar una integración entre ChatGPT Web y Codex — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/codex-chatgpt-web.md) · [GitHub](https://github.com/miuuyy/codex-chatgpt-web)

#### 📦 sandbox
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 6.3k<br>
**Qué es:** Resuelve el riesgo de dejar que un agente toque tu host: todo corre contenido en un contenedor reproducible.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/agent-infra/sandbox/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres aislar la ejecución de agentes y reproducibilidad — **Evita si:** te basta correr local sin sandbox o no puedes asumir el overhead de Docker<br>
**Combina con:** [OpenHands](human/fichas/openhands.md) · [ECC](human/fichas/ecc.md)<br>
**Más:** [ficha completa](human/fichas/sandbox.md) · [GitHub](https://github.com/agent-infra/sandbox)

#### 🛠️ Gemini Computer Use (preview)
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 3.3k<br>
**Qué es:** Muestra cómo un modelo Gemini con computer use controla un navegador para completar tareas. Es una vista previa, no un agente de propósito general.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/google-gemini/computer-use-preview/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres probar computer use con Gemini — **Evita si:** buscas automatización web robusta; mira `browser-use` o `stagehand`<br>
**Combina con:** [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/computer-use-preview.md) · [GitHub](https://github.com/google-gemini/computer-use-preview)

#### 🟩 NeMo-Agent-Toolkit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 2.7k<br>
**Qué es:** Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install nvidia-nat` (comprobar los pasos completos en la ficha).<br>
**Elige si:** trabajas con infra NVIDIA o necesitas guardrails/eval empresarial — **Evita si:** quieres algo ligero y agnóstico<br>
**Combina con:** [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/nemo-agent-toolkit.md) · [GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

#### 🕸️ nodeterm
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 2.5k<br>
**Qué es:** Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. Mantiene terminales reales en nodos movibles y muestra sesiones de trabajo en un tablero.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/eneskirca/nodeterm/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** gestionas muchas terminales o sesiones de agentes y prefieres una organización visual — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Más:** [ficha completa](human/fichas/nodeterm.md) · [GitHub](https://github.com/eneskirca/nodeterm)

#### 🛠️ Agent Protocol
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 698<br>
**Qué es:** Define cómo se ejecuta un agente, cómo recibe entradas y cómo guarda su estado, sin atarse a un framework. Es una especificación, no un runtime.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/langchain-ai/agent-protocol/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** diseñas una plataforma que sirve agentes de distintos frameworks — **Evita si:** solo necesitas construir un agente<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md)<br>
**Más:** [ficha completa](human/fichas/agent-protocol.md) · [GitHub](https://github.com/langchain-ai/agent-protocol)

### Simulación, evolución y debate entre modelos

#### 🐟 MiroFish ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 85.6k<br>
**Qué es:** Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/666ghj/MiroFish/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** simulas futuros/escenarios con muchos actores — **Evita si:** necesitas tareas deterministas o resultados reproducibles<br>
**Combina con:** [openevolve](human/fichas/openevolve.md)<br>
**Más:** [ficha completa](human/fichas/mirofish.md) · [GitHub](https://github.com/666ghj/MiroFish)

#### 🏛️ llm-council
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 26.5k<br>
**Qué es:** Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/karpathy/llm-council/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres consenso entre modelos o comparar proveedores — **Evita si:** te basta un único LLM o el coste multi-modelo no es asumible<br>
**Combina con:** [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/llm-council.md) · [GitHub](https://github.com/karpathy/llm-council)

#### 🧬 openevolve
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 7.8k<br>
**Qué es:** Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install openevolve` (comprobar los pasos completos en la ficha).<br>
**Elige si:** optimizas problemas algorítmicos donde cabe explorar muchas variantes — **Evita si:** haces tareas de texto comunes o buscas respuesta inmediata<br>
**Combina con:** [llm-council](human/fichas/llm-council.md)<br>
**Más:** [ficha completa](human/fichas/openevolve.md) · [GitHub](https://github.com/algorithmicsuperintelligence/openevolve)

#### 🕸️ hermes-agent-self-evolution
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 5.7k<br>
**Qué es:** Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA. Evalúa variantes de texto, analiza trazas y selecciona mejoras sin reentrenar pesos de un modelo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/NousResearch/hermes-agent-self-evolution/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres experimentar con mejoras de Hermes medidas sobre un conjunto de evaluación — **Evita si:** un flujo determinista resuelve el problema sin un agente<br>
**Combina con:** [hermes-agent](human/fichas/hermes-agent.md)<br>
**Más:** [ficha completa](human/fichas/hermes-agent-self-evolution.md) · [GitHub](https://github.com/NousResearch/hermes-agent-self-evolution)

---

## 🕷️ 4. Buscar y extraer información web

Buscadores, crawlers y navegadores. Usa un crawler para extraer páginas, un navegador para interactuar y un agente para investigar con un modelo.

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

**⚖️ ¿Cuál elegir? — agent-browser, playwright-cli**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [agent-browser](human/fichas/agent-browser.md) | necesitas navegación programable con salidas compactas para un agente | la fuente ya ofrece una API o un archivo de datos suficiente |
| [playwright-cli](human/fichas/playwright-cli.md) | tu agente vive en CLI y el contexto es un recurso caro | necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP) |

**⚖️ ¿Cuál elegir? — Agent-Reach, snscrape**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Agent-Reach](human/fichas/agent-reach.md) | tu agente necesita leer redes sociales sin APIs de pago | necesitas datos con garantías de términos de servicio |
| [snscrape](human/fichas/snscrape.md) | recolectas varias redes y no te sirve una API oficial | solo necesitas Instagram (instaloader) o la plataforma ya bloqueó el acceso no oficial |

### Crawlers y extracción para IA

#### 🔥 firecrawl ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 202k<br>
**Qué es:** Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. Se ha vuelto la opción de referencia para alimentar pipelines RAG y agentes con web limpia; muy adoptada y con integración MCP de primera clase.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install firecrawl` (comprobar los pasos completos en la ficha).<br>
**Elige si:** alimentas agentes/RAG con web y quieres salida limpia — **Evita si:** solo quieres HTML crudo o el presupuesto de API no encaja<br>
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [crawl4ai](human/fichas/crawl4ai.md)<br>
**Más:** [ficha completa](human/fichas/firecrawl.md) · [GitHub](https://github.com/firecrawl/firecrawl)

#### 🩹 Scrapling
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 103k<br>
**Qué es:** Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. Proyecto en alza por su enfoque "auto-reparable" de selectores, que evita reescribir scrapers cada vez que el sitio se actualiza.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install scrapling` (comprobar los pasos completos en la ficha).<br>
**Elige si:** los sitios cambian o te bloquean a menudo — **Evita si:** el target es estable y simple, o no necesitas stealth<br>
**Combina con:** [scrapy](human/fichas/scrapy.md)<br>
**Más:** [ficha completa](human/fichas/scrapling.md) · [GitHub](https://github.com/D4Vinci/Scrapling)

#### 🕷️ crawl4ai
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 87.4k<br>
**Qué es:** Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. Una de las alternativas open-source más populares a las APIs de pago; gratuita, self-host y muy activa en la comunidad de scraping para LLMs.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install crawl4ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas volumen barato y self-host — **Evita si:** quieres una API hosted simple sin operar navegadores (firecrawl)<br>
**Combina con:** [firecrawl](human/fichas/firecrawl.md) · [gpt-researcher](human/fichas/gpt-researcher.md)<br>
**Más:** [ficha completa](human/fichas/crawl4ai.md) · [GitHub](https://github.com/unclecode/crawl4ai)

#### 🐍 scrapy
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 65.4k<br>
**Qué es:** Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. Estándar de facto del scraping en Python desde hace más de una década, con enorme ecosistema de extensiones y base instalada masiva.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install scrapy` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres un crawler sólido y configurable a escala — **Evita si:** buscas salida lista para LLM o algo puntual sin curva de framework<br>
**Combina con:** [scrapely](human/fichas/scrapely.md) · [crawlee-python](human/fichas/crawlee-python.md)<br>
**Más:** [ficha completa](human/fichas/scrapy.md) · [GitHub](https://github.com/scrapy/scrapy)

#### 🦗 crawlee
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 26.4k<br>
**Qué es:** Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. Mantenido por Apify, es la referencia de crawling en el ecosistema JavaScript y trae evasión de bloqueos lista de fábrica.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx crawlee create` (comprobar los pasos completos en la ficha).<br>
**Elige si:** scrapeas con Node y necesitas antibloqueo — **Evita si:** trabajas en Python (crawlee-python) o no necesitas evasión<br>
**Combina con:** [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/crawlee.md) · [GitHub](https://github.com/apify/crawlee)

#### 🕷️ Jina Reader
**Etiquetas:** Ejecución ☁️ cloud/API · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 12.3k<br>
**Qué es:** Pega `https://r.jina.ai/` delante de una URL y obtienes su contenido limpio. También busca en la web con `s.jina.ai`.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/jina-ai/reader/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas leer páginas como Markdown al instante — **Evita si:** vas a rastrear sitios completos; mira `crawl4ai` o `firecrawl`<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/jina-reader.md) · [GitHub](https://github.com/jina-ai/reader)

#### 🦗 crawlee-python
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 9.7k<br>
**Qué es:** Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. Acerca las ventajas del Crawlee de Node a quienes ya viven en Python, con respaldo oficial de Apify y adopción en crecimiento.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/apify/crawlee-python/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres Crawlee en Python con antibloqueo — **Evita si:** ya usas scrapy y te basta, o no necesitas evasión<br>
**Combina con:** [scrapy](human/fichas/scrapy.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/crawlee-python.md) · [GitHub](https://github.com/apify/crawlee-python)

#### 🕷️ awesome-web-scraping
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 8.2k<br>
**Qué es:** Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos. Organiza opciones por lenguaje y función para investigar alternativas de extracción.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/lorien/awesome-web-scraping/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres comparar librerías de scraping antes de elegir tu stack — **Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente<br>
**Más:** [ficha completa](human/fichas/awesome-web-scraping.md) · [GitHub](https://github.com/lorien/awesome-web-scraping)

#### 🕷️ scrapydweb
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 3.4k<br>
**Qué es:** Panel web para administrar clústeres de Scrapyd y consultar trabajos, logs y estadísticas de Scrapy. Conecta servidores Scrapyd y centraliza despliegues, tareas programadas y seguimiento de crawls.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install scrapydweb` (comprobar los pasos completos en la ficha).<br>
**Elige si:** operas varios spiders de Scrapy y necesitas un panel de administración — **Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente<br>
**Combina con:** [scrapy](human/fichas/scrapy.md)<br>
**Más:** [ficha completa](human/fichas/scrapydweb.md) · [GitHub](https://github.com/my8100/scrapydweb)

#### 📐 scrapely
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.9k<br>
**Qué es:** Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales. Pieza histórica del ecosistema Scrapy; nicho y poco activa hoy, pero útil cuando se quiere extraer "por demostración" en lugar de programar selectores.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install scrapely` (comprobar los pasos completos en la ficha).<br>
**Elige si:** prefieres enseñar por ejemplos y el sitio es homogéneo — **Evita si:** necesitas un crawler completo o el proyecto exige mantenimiento activo<br>
**Combina con:** [scrapy](human/fichas/scrapy.md)<br>
**Más:** [ficha completa](human/fichas/scrapely.md) · [GitHub](https://github.com/scrapy/scrapely)

### Scraping guiado por LLM

#### 🕸️ Scrapegraph-ai ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 32.8k<br>
**Qué es:** Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. Muy popular por permitir scraping "by prompt", combinando extracción con razonamiento del modelo y soporte para múltiples proveedores.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install scrapegraphai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres estructura semántica "by prompt" en Python — **Evita si:** te basta un esquema simple (llm-scraper) o el coste de LLM por página es alto<br>
**Combina con:** [crawl4ai](human/fichas/crawl4ai.md) · [graphrag](human/fichas/graphrag.md)<br>
**Más:** [ficha completa](human/fichas/scrapegraph-ai.md) · [GitHub](https://github.com/ScrapeGraphAI/Scrapegraph-ai)

#### 🧠 Maxun
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.4k<br>
**Qué es:** Grabas lo que quieres extraer haciendo clic en la página y Maxun crea un robot que lo repite, con paginación y programación. Ideal para equipos sin programadores.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/getmaxun/maxun/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres extraer datos web sin programar — **Evita si:** programas y prefieres librerías; mira `crawl4ai` o `scrapy`<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/maxun.md) · [GitHub](https://github.com/getmaxun/maxun)

#### 🧾 llm-scraper
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 7k<br>
**Qué es:** Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. Popular por su simplicidad: salida tipada y validada sin escribir parsers, integrándose directamente con Playwright y los SDKs de LLM.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mishushakov/llm-scraper/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres salida tipada y validada en stack TS — **Evita si:** prefieres extracción semántica por grafos (Scrapegraph-ai) o trabajas en Python<br>
**Combina con:** [playwright](human/fichas/playwright.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/llm-scraper.md) · [GitHub](https://github.com/mishushakov/llm-scraper)

### Navegadores y automatización web

#### 🌐 Stagehand ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 26.1k<br>
**Qué es:** Usa `act`, `extract` y `observe` para que la IA haga lo difícil y tu código lo predecible. Basado en Playwright.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/browserbase/stagehand/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres automatización web robusta con un toque de IA en TS — **Evita si:** quieres que un agente navegue solo; mira `browser-use`<br>
**Combina con:** [Mastra](human/fichas/mastra.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/stagehand.md) · [GitHub](https://github.com/browserbase/stagehand)

#### 🌐 browser-use
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 121k<br>
**Qué es:** Resuelve la fragilidad del scraping basado en CSS: el agente "ve" la página como un humano y decide la siguiente acción.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/browser-use/browser-use/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres navegación como humano y tolerancia a cambios de UI — **Evita si:** necesitas scripts deterministas y baratos (playwright) o no quieres depender de un LLM por paso<br>
**Combina con:** [playwright](human/fichas/playwright.md) · [gpt-researcher](human/fichas/gpt-researcher.md)<br>
**Más:** [ficha completa](human/fichas/browser-use.md) · [GitHub](https://github.com/browser-use/browser-use)

#### 🎭 playwright
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 100k<br>
**Qué es:** Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. Se ha convertido en el estándar moderno de automatización de browser, desplazando a Selenium/Puppeteer por su fiabilidad y su auto-espera de elementos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/playwright/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas control preciso y reproducible del browser — **Evita si:** quieres que el agente navegue por visión (browser-use) o no necesitas un navegador real<br>
**Combina con:** [browser-use](human/fichas/browser-use.md) · [crawlee](human/fichas/crawlee.md)<br>
**Más:** [ficha completa](human/fichas/playwright.md) · [GitHub](https://github.com/microsoft/playwright)

#### 🌐 Puppeteer
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 95.8k<br>
**Qué es:** Automatiza navegación, capturas, PDFs y pruebas. Es la base de muchas herramientas de scraping.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm i puppeteer` (comprobar los pasos completos en la ficha).<br>
**Elige si:** trabajas en Node y quieres controlar Chrome — **Evita si:** necesitas varios navegadores y pruebas E2E; mira `playwright`<br>
**Combina con:** [Lightpanda](human/fichas/lightpanda.md)<br>
**Más:** [ficha completa](human/fichas/puppeteer.md) · [GitHub](https://github.com/puppeteer/puppeteer)

#### 🕷️ agent-browser
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 51.2k<br>
**Qué es:** CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. Mantiene una sesión de navegador y permite abrir páginas, inspeccionarlas y actuar por referencias desde la terminal.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install -g agent-browser` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas navegación programable con salidas compactas para un agente — **Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente<br>
**Combina con:** [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/agent-browser.md) · [GitHub](https://github.com/vercel-labs/agent-browser)

#### 🌐 Lightpanda
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 42k<br>
**Qué es:** Ejecuta JavaScript y es compatible con Puppeteer y Playwright por CDP, usando una fracción de memoria. Ideal para scraping masivo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/lightpanda-io/browser/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas muchos navegadores headless con poca memoria — **Evita si:** necesitas compatibilidad total con sitios complejos; usa Chrome con `playwright`<br>
**Combina con:** [Puppeteer](human/fichas/puppeteer.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/lightpanda.md) · [GitHub](https://github.com/lightpanda-io/browser)

#### 🌐 Selenium
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 34.6k<br>
**Qué es:** Estándar W3C WebDriver, muy usado en pruebas empresariales con Selenium Grid para paralelizar.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/SeleniumHQ/selenium/blob/trunk/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu equipo ya usa Selenium o necesitas muchos lenguajes — **Evita si:** empiezas de cero; mira `playwright`<br>
**Más:** [ficha completa](human/fichas/selenium.md) · [GitHub](https://github.com/SeleniumHQ/selenium)

#### 🌐 Skyvern
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 23.4k<br>
**Qué es:** Completa formularios, compras o descargas en sitios que nunca vio, entendiendo la página con visión. Incluye UI, API y workflows.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install skyvern` (comprobar los pasos completos en la ficha).<br>
**Elige si:** automatizas portales web que cambian a menudo — **Evita si:** necesitas scraping masivo y barato; mira `crawl4ai`<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/skyvern.md) · [GitHub](https://github.com/Skyvern-AI/skyvern)

#### 🌐 Browser Harness
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 19.1k<br>
**Qué es:** Conecta el agente a tu navegador por CDP con un arnés pequeño y editable. Útil cuando necesitas libertad total y tus cuentas ya abiertas.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/browser-use/browser-harness/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente debe usar tu navegador real con sesión — **Evita si:** necesitas aislamiento; mira `playwright-mcp`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/browser-harness.md) · [GitHub](https://github.com/browser-use/browser-harness)

#### 🎭 playwright-cli
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 15.2k<br>
**Qué es:** Resuelve el problema de los árboles de accesibilidad y los JSON de herramientas que inflan el prompt en cada turno.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/playwright-cli/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente vive en CLI y el contexto es un recurso caro — **Evita si:** necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP)<br>
**Combina con:** [playwright](human/fichas/playwright.md) · [browser-use](human/fichas/browser-use.md)<br>
**Más:** [ficha completa](human/fichas/playwright-cli.md) · [GitHub](https://github.com/microsoft/playwright-cli)

#### 🕷️ camofox-browser
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 12.3k<br>
**Qué es:** Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes. Expone un navegador derivado de Firefox mediante herramientas y endpoints de automatización.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/jo-inc/camofox-browser/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas evaluar una alternativa de navegador automatizado para agentes — **Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente<br>
**Más:** [ficha completa](human/fichas/camofox-browser.md) · [GitHub](https://github.com/jo-inc/camofox-browser)

#### 🕷️ awesome-chrome-devtools
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 7.2k<br>
**Qué es:** Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol. Agrupa depuradores, visores de trazas y clientes del protocolo para localizar una herramienta adecuada.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ChromeDevTools/awesome-chrome-devtools/blob/master/readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas utilidades para depurar o automatizar Chrome — **Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente<br>
**Más:** [ficha completa](human/fichas/awesome-chrome-devtools.md) · [GitHub](https://github.com/ChromeDevTools/awesome-chrome-devtools)

### Búsqueda, monitoreo y research web

#### 🔍 SearXNG ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 39.6k<br>
**Qué es:** Combina resultados de más de 70 servicios sin rastrearte. Muchos agentes de investigación lo usan como API de búsqueda gratuita y propia.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/searxng/searxng/blob/master/README.rst); no se deduce un paquete por el nombre.<br>
**Elige si:** tus agentes necesitan buscar en la web sin coste por consulta — **Evita si:** necesitas resultados con SLA comercial<br>
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [Open WebUI](human/fichas/open-webui.md) · [Vane](human/fichas/vane.md)<br>
**Más:** [ficha completa](human/fichas/searxng.md) · [GitHub](https://github.com/searxng/searxng)

#### 🔍 Agent-Reach
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 112k<br>
**Qué es:** Un solo comando para que el agente lea y busque en redes y plataformas populares, incluidas chinas como Bilibili y XiaoHongShu.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Panniantong/Agent-Reach/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente necesita leer redes sociales sin APIs de pago — **Evita si:** necesitas datos con garantías de términos de servicio<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [last30days](human/fichas/last30days-skill.md)<br>
**Más:** [ficha completa](human/fichas/agent-reach.md) · [GitHub](https://github.com/Panniantong/Agent-Reach)

#### 🔍 last30days
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 67.7k<br>
**Qué es:** Busca lo que la gente está diciendo ahora sobre un tema y lo resume con fuentes. Prioriza señales reales como votos, likes y apuestas.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/mvanhorn/last30days-skill/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres saber qué se dice ahora sobre un tema — **Evita si:** necesitas un informe académico; mira `storm`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Agent-Reach](human/fichas/agent-reach.md)<br>
**Más:** [ficha completa](human/fichas/last30days-skill.md) · [GitHub](https://github.com/mvanhorn/last30days-skill)

#### 🔍 Vane
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 38.2k<br>
**Qué es:** Busca en la web con SearXNG y responde con citas usando modelos locales o en la nube. Incluye modos de enfoque para académico, YouTube o Reddit.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ItzCrazyKns/Vane/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un buscador con respuestas citadas auto-hospedado — **Evita si:** necesitas informes largos; mira `gpt-researcher`<br>
**Combina con:** [SearXNG](human/fichas/searxng.md) · [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/vane.md) · [GitHub](https://github.com/ItzCrazyKns/Vane)

#### 🔍 changedetection.io
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 35.8k<br>
**Qué es:** Vigila precios, stock, documentación o cualquier texto de una página y te avisa cuando cambia. Admite navegador real para sitios con JavaScript.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/dgtlmoon/changedetection.io/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres alertas cuando cambia una página — **Evita si:** necesitas extraer datos estructurados; mira `maxun`<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/changedetection.md) · [GitHub](https://github.com/dgtlmoon/changedetection.io)

#### 🔍 ArchiveBox
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 29k<br>
**Qué es:** Le das URLs, marcadores o historial y guarda copias completas para siempre. Útil para investigación y preservación de fuentes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install archivebox` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres conservar copias fieles de páginas web — **Evita si:** solo necesitas el texto para un LLM; mira `jina-reader`<br>
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md)<br>
**Más:** [ficha completa](human/fichas/archivebox.md) · [GitHub](https://github.com/ArchiveBox/ArchiveBox)

### Redes sociales y descarga de medios

#### 📱 yt-dlp ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 208k<br>
**Qué es:** Descarga videos, audios, subtítulos y metadatos de YouTube y miles de plataformas. Base de muchos pipelines de transcripción.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/yt-dlp/yt-dlp/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas bajar audio o video de la web — **Evita si:** solo necesitas metadatos sociales; mira `instaloader`<br>
**Combina con:** [whisperX](human/fichas/whisperx.md) · [FFmpeg](human/fichas/ffmpeg.md) · [Fabric](human/fichas/fabric.md)<br>
**Más:** [ficha completa](human/fichas/yt-dlp.md) · [GitHub](https://github.com/yt-dlp/yt-dlp)

#### 📸 instaloader
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13.9k<br>
**Qué es:** Resuelve el archivado masivo de Instagram sin recurrir a APIs oficiales de pago ni herramientas manuales.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/instaloader/instaloader/blob/master/README.rst); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas datos de Instagram de forma fiable — **Evita si:** quieres varias redes a la vez (snscrape) o el contenido requiere API oficial por ToS<br>
**Combina con:** [snscrape](human/fichas/snscrape.md)<br>
**Más:** [ficha completa](human/fichas/instaloader.md) · [GitHub](https://github.com/instaloader/instaloader)

#### 🐦 snscrape
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 5.5k<br>
**Qué es:** Resuelve la recolección histórica de datos sociales cuando las APIs de pago no son viables o no existen.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/JustAnotherArchivist/snscrape/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** recolectas varias redes y no te sirve una API oficial — **Evita si:** solo necesitas Instagram (instaloader) o la plataforma ya bloqueó el acceso no oficial<br>
**Combina con:** [instaloader](human/fichas/instaloader.md)<br>
**Más:** [ficha completa](human/fichas/snscrape.md) · [GitHub](https://github.com/JustAnotherArchivist/snscrape)

---

## 🔌 5. Conectar herramientas con MCP

SDKs, servidores y conectores que dejan a un agente usar herramientas. El servidor MCP aporta acciones o datos; el modelo pertenece al cliente.

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
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 28.5k<br>
**Qué es:** Convierte funciones Python en herramientas MCP con un decorador y añade autenticación, composición de servidores y cliente de pruebas. Su versión 1 se integró en el SDK oficial.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `uv add fastmcp` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres crear un servidor MCP en Python rápido — **Evita si:** trabajas en TypeScript; mira `mcp-typescript-sdk`<br>
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/fastmcp.md) · [GitHub](https://github.com/PrefectHQ/fastmcp)

#### 🧰 MCP TypeScript SDK ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13.8k<br>
**Qué es:** Base de la mayoría de servidores MCP en Node.js, con transportes stdio y HTTP.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** creas servidores MCP en TypeScript — **Evita si:** trabajas en Python; mira `fastmcp`<br>
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md)<br>
**Más:** [ficha completa](human/fichas/mcp-typescript-sdk.md) · [GitHub](https://github.com/modelcontextprotocol/typescript-sdk)

#### 🧰 MCP Python SDK
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 24.9k<br>
**Qué es:** Implementación de referencia del protocolo en Python, con la API FastMCP integrada para servidores sencillos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install "mcp[cli]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres el SDK oficial con mínima dependencia — **Evita si:** quieres funciones extra como auth y composición; mira `fastmcp`<br>
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md)<br>
**Más:** [ficha completa](human/fichas/mcp-python-sdk.md) · [GitHub](https://github.com/modelcontextprotocol/python-sdk)

#### 🧰 MCP Inspector
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 11.3k<br>
**Qué es:** Conéctate a cualquier servidor MCP, lista sus herramientas y recursos y lánzalos a mano para ver respuestas y errores.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx @modelcontextprotocol/inspector` (comprobar los pasos completos en la ficha).<br>
**Elige si:** desarrollas un servidor MCP — **Evita si:** solo usas servidores ya hechos<br>
**Combina con:** [FastMCP](human/fichas/fastmcp.md) · [MCP TypeScript SDK](human/fichas/mcp-typescript-sdk.md)<br>
**Más:** [ficha completa](human/fichas/mcp-inspector.md) · [GitHub](https://github.com/modelcontextprotocol/inspector)

#### 🛠️ mcp-use
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 11k<br>
**Qué es:** Resuelve el salto del SDK base (verboso) a algo productivo: registro de tools, inspector y despliegue incluidos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mcp-use/mcp-use/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** construyes un servidor MCP propio y quieres productividad — **Evita si:** solo buscas usar uno ya hecho (awesome-mcp-servers) o necesitas control a nivel spec<br>
**Combina con:** [mcp](human/fichas/mcp.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/mcp-use.md) · [GitHub](https://github.com/mcp-use/mcp-use)

#### 🧰 LangChain MCP Adapters
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 3.6k<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** Permite que tus agentes de LangGraph usen cualquier servidor MCP sin escribir adaptadores. El repo está archivado y su función se integró en LangChain.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install langchain-mcp-adapters` (comprobar los pasos completos en la ficha).<br>
**Elige si:** usas LangGraph y quieres herramientas MCP — **Evita si:** no usas LangChain<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/langchain-mcp-adapters.md) · [GitHub](https://github.com/langchain-ai/langchain-mcp-adapters)

### Servidores MCP destacados

#### 🔌 Context7 ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 64.8k<br>
**Qué es:** Evita que el modelo invente APIs viejas: busca la documentación vigente de la librería que estás usando y la inyecta en el prompt.<br>
**Acceso:** Sin API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/upstash/context7/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente de código usa librerías que cambian a menudo — **Evita si:** trabajas sin conexión a internet<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Cline](human/fichas/cline.md) · [OpenCode](human/fichas/opencode.md)<br>
**Más:** [ficha completa](human/fichas/context7.md) · [GitHub](https://github.com/upstash/context7)

#### 🔌 Playwright MCP ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 39.7k<br>
**Qué es:** Da a tu agente un navegador real controlado por el árbol de accesibilidad, sin depender de capturas. Ideal para pruebas y automatización web.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx @playwright/mcp@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres que tu agente use un navegador real — **Evita si:** necesitas depurar rendimiento y consola; mira `chrome-devtools-mcp`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/playwright-mcp.md) · [GitHub](https://github.com/microsoft/playwright-mcp)

#### 📚 servers
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 92k<br>
**Qué es:** Resuelve la falta de ejemplos canónicos: muestra cómo se construye un servidor MCP correcto, paso a paso.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/modelcontextprotocol/servers/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres ejemplos canónicos y plantillas fiables — **Evita si:** buscas soluciones listas para producción (son demos educativas, no hardening)<br>
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/servers.md) · [GitHub](https://github.com/modelcontextprotocol/servers)

#### 🔌 Chrome DevTools MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 56.3k<br>
**Qué es:** Tu agente de código puede abrir páginas, leer errores de consola, inspeccionar peticiones y medir rendimiento para depurar de verdad.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente necesita depurar una web como lo harías en DevTools — **Evita si:** solo quieres automatizar navegación; mira `playwright-mcp`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/chrome-devtools-mcp.md) · [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)

#### 🔌 GitHub MCP Server
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 34.5k<br>
**Qué es:** Conecta asistentes y agentes con la plataforma GitHub: repositorios, issues, pull requests, Actions y seguridad.<br>
**Acceso:** Sin API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/github/github-mcp-server/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente trabaja con GitHub — **Evita si:** usas otra forja como GitLab<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/github-mcp-server.md) · [GitHub](https://github.com/github/github-mcp-server)

#### 🔌 Blender MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 34.5k<br>
**Qué es:** Crea y modifica escenas, objetos y materiales hablando con tu asistente. Útil para prototipos 3D rápidos.<br>
**Acceso:** Sin API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uvx blender-mcp` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres manejar Blender con tu agente — **Evita si:** no trabajas en 3D<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/blender-mcp.md) · [GitHub](https://github.com/ahujasid/mcp-for-blender)

#### 🔌 Serena
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 31.4k<br>
**Qué es:** En vez de leer archivos enteros, el agente busca símbolos, referencias y edita a nivel de función usando servidores de lenguaje. Ahorra tokens en repos grandes.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/oraios/serena/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente trabaja en un repo grande y gasta muchos tokens leyendo — **Evita si:** tu proyecto es pequeño<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/serena.md) · [GitHub](https://github.com/oraios/serena)

#### 🔌 Figma Context MCP
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 16.2k<br>
**Qué es:** Simplifica la respuesta de la API de Figma y da al agente solo lo relevante (estructura, estilos, medidas) para convertir un diseño en código.<br>
**Acceso:** Sin API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/GLips/Figma-Context-MCP/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** implementas diseños de Figma con un agente de código — **Evita si:** no usas Figma<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [ui](human/fichas/ui.md) · [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/figma-context-mcp.md) · [GitHub](https://github.com/GLips/Figma-Context-MCP)

#### 🔌 annas-mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 1.1k<br>
**Qué es:** Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos. Expone búsquedas y descargas como herramientas MCP y permite seleccionar espejos disponibles.<br>
**Acceso:** Sin API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/iosifache/annas-mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas integrar búsquedas de documentos en un cliente MCP — **Evita si:** una conexión directa cubre el caso sin añadir infraestructura<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/annas-mcp.md) · [GitHub](https://github.com/iosifache/annas-mcp)

#### 🕸️ mcp-neo4j
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 989<br>
**Qué es:** Resuelve el acceso natural a grafos desde un LLM: el asistente consulta y escribe Cypher sin que tú escribas el glue a mano.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Neo4j con IA y quieres que el asistente hable Cypher — **Evita si:** no trabajas con grafos o tu base es relacional pura<br>
**Combina con:** [graphrag](human/fichas/graphrag.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/mcp-neo4j.md) · [GitHub](https://github.com/neo4j-contrib/mcp-neo4j)

### Directorios, clientes y aprendizaje

#### 📚 MCP for Beginners ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 17.7k<br>
**Qué es:** Explica los fundamentos del Model Context Protocol, seguridad y despliegue con ejercicios por lenguaje. Disponible en varios idiomas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/mcp-for-beginners/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres aprender MCP de forma estructurada — **Evita si:** ya construyes servidores MCP; ve directo a `fastmcp`<br>
**Combina con:** [FastMCP](human/fichas/fastmcp.md) · [MCP Inspector](human/fichas/mcp-inspector.md)<br>
**Más:** [ficha completa](human/fichas/mcp-for-beginners.md) · [GitHub](https://github.com/microsoft/mcp-for-beginners)

#### 🌍 public-apis
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 499k<br>
**Qué es:** Resuelve el descubrimiento: en un solo lugar tienes URLs, autenticación y HTTPS de cada API en lugar de buscarlas una a una.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/public-apis/public-apis/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas datos externos y no sabes qué API usar — **Evita si:** ya tienes tus fuentes definidas o necesitas SLA empresarial (son APIs públicas, sin garantías)<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/public-apis.md) · [GitHub](https://github.com/public-apis/public-apis)

#### 🗂️ awesome-mcp-servers
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 97.7k<br>
**Qué es:** Resuelve el "¿ya existe un servidor para X?" antes de que construyas el tuyo desde cero.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/punkpeye/awesome-mcp-servers/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas antes de construir — **Evita si:** ya sabes que necesitas uno a medida y no te vale ninguno listado<br>
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [servers](human/fichas/servers.md)<br>
**Más:** [ficha completa](human/fichas/awesome-mcp-servers.md) · [GitHub](https://github.com/punkpeye/awesome-mcp-servers)

#### 📚 Awesome MCP Clients
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 6.6k<br>
**Qué es:** Ayuda a elegir dónde usar tus servidores MCP: chats de escritorio, editores, CLIs y plataformas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/punkpeye/awesome-mcp-clients/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas un cliente para tus servidores MCP — **Evita si:** buscas servidores; mira `awesome-mcp-servers`<br>
**Combina con:** [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/awesome-mcp-clients.md) · [GitHub](https://github.com/punkpeye/awesome-mcp-clients)

#### 🧩 mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 4.7k<br>
**Qué es:** Resuelve la fragmentación: cada integración de IA dejaba de ser ad-hoc y pasa a hablar un protocolo común.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/google/mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** programas MCP a bajo nivel o necesitas conformidad estricta con la spec — **Evita si:** prefieres un framework de alto nivel que abstraiga el protocolo (mcp-use)<br>
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [servers](human/fichas/servers.md)<br>
**Más:** [ficha completa](human/fichas/mcp.md) · [GitHub](https://github.com/google/mcp)

### Dominios y recursos de infraestructura

#### 🔌 FreeDomain
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 208k<br>
**Qué es:** Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. Reúne instrucciones para registrar un dominio, configurar nameservers y conectar un proyecto.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/DigitalPlatDev/FreeDomain/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres aprender el flujo de dominios y DNS con sus recursos de referencia — **Evita si:** una conexión directa cubre el caso sin añadir infraestructura<br>
**Más:** [ficha completa](human/fichas/freedomain.md) · [GitHub](https://github.com/DigitalPlatDev/FreeDomain)

#### 🔌 free-for-dev
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 143k<br>
**Qué es:** Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. Agrupa servicios por capacidad para comparar opciones antes de configurar un proyecto.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ripienaar/free-for-dev/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas servicios de desarrollo con un nivel gratuito disponible — **Evita si:** una conexión directa cubre el caso sin añadir infraestructura<br>
**Más:** [ficha completa](human/fichas/free-for-dev.md) · [GitHub](https://github.com/ripienaar/free-for-dev)

### Redes y transporte

#### 🔌 MasterDnsVPN
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 7.3k<br>
**Qué es:** Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. Coordina cliente y servidor con retransmisión y selección de resolvers para enlaces con restricciones.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar transporte de red sobre DNS en un entorno de pruebas — **Evita si:** una conexión directa cubre el caso sin añadir infraestructura<br>
**Más:** [ficha completa](human/fichas/masterdnsvpn.md) · [GitHub](https://github.com/masterking32/MasterDnsVPN)

---

## 🧬 6. Memoria, conocimiento y operación de IA

Guarda memoria, consulta documentos con RAG, sirve modelos y evalúa resultados. Una base vectorial y un sistema RAG completo resuelven capas distintas.

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

**⚖️ ¿Cuál elegir? — headroom, rtk**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [headroom](human/fichas/headroom.md) | te quedas sin contexto en sesiones largas | tus prompts ya caben holgados o la pérdida de detalle por resumen es inaceptable |
| [rtk](human/fichas/rtk.md) | tu agente consume demasiado contexto leyendo salidas extensas de terminal | el coste operativo supera el volumen de uso del proyecto |

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
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 117k<br>
**Qué es:** Registra lo que hace el agente en cada sesión, lo resume y vuelve a inyectar lo relevante al empezar la siguiente. Evita repetir contexto en proyectos largos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/thedotmack/claude-mem/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Claude Code a diario y repites contexto entre sesiones — **Evita si:** necesitas memoria para una app propia; mira `mem0`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/claude-mem.md) · [GitHub](https://github.com/thedotmack/claude-mem)

#### 🧠 mem0
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 69k<br>
**Qué es:** Resuelve el "amnesia" del LLM: el agente conserva preferencias y hechos entre sesiones sin reenviar todo el historial.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install mem0ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres memoria estándar lista con integraciones amplias — **Evita si:** necesitas todo local sin llamadas a API (mempalace) o control total del almacenamiento<br>
**Combina con:** [crewAI](human/fichas/crewai.md) · [langchain](human/fichas/langchain.md) · [agentmemory](human/fichas/agentmemory.md)<br>
**Más:** [ficha completa](human/fichas/mem0.md) · [GitHub](https://github.com/mem0ai/mem0)

#### 🏛️ mempalace
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 60.6k<br>
**Qué es:** Resuelve la memoria privada: cero llamadas a API, tus textos no salen de tu máquina.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/MemPalace/mempalace/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** la privacidad es prioridad y no quieres llamadas a API — **Evita si:** quieres un SaaS gestionado con escalado automático o integraciones de framework ya hechas (mem0)<br>
**Combina con:** [open-notebook](human/fichas/open-notebook.md) · [odysseus](human/fichas/odysseus.md)<br>
**Más:** [ficha completa](human/fichas/mempalace.md) · [GitHub](https://github.com/MemPalace/mempalace)

#### 🧠 cognee
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 33.3k<br>
**Qué es:** Convierte documentos y conversaciones en un grafo de conocimiento consultable para dar memoria de largo plazo a tus agentes.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install cognee` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres memoria basada en grafo con poco esfuerzo — **Evita si:** necesitas un grafo temporal en tiempo real; mira `graphiti`<br>
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [mcp-neo4j](human/fichas/mcp-neo4j.md)<br>
**Más:** [ficha completa](human/fichas/cognee.md) · [GitHub](https://github.com/topoteretes/cognee)

#### 🧠 Graphiti
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 32.8k<br>
**Qué es:** Actualiza el grafo con cada nuevo dato sin recalcular todo y guarda cuándo era válido cada hecho. Ideal para memoria de agentes que cambia.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install graphiti-core` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas memoria que cambie con el tiempo y se pueda consultar — **Evita si:** solo quieres RAG sobre documentos estáticos; mira `lightrag`<br>
**Combina con:** [mcp-neo4j](human/fichas/mcp-neo4j.md)<br>
**Más:** [ficha completa](human/fichas/graphiti.md) · [GitHub](https://github.com/getzep/graphiti)

#### 🧠 supermemory
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 31.6k<br>
**Qué es:** Guarda y recupera lo que importa de documentos, conversaciones y webs para dar contexto a tus modelos. Ofrece API, SDK y una app de usuario.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/supermemoryai/supermemory/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una API de memoria lista para tu app — **Evita si:** prefieres librería en Python; mira `mem0`<br>
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md)<br>
**Más:** [ficha completa](human/fichas/supermemory.md) · [GitHub](https://github.com/supermemoryai/supermemory)

#### 💾 agentmemory
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.4k<br>
**Qué es:** Resuelve el "re-explica todo" al cambiar de asistente: la memoria vive fuera del cliente.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/rohitg00/agentmemory/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** cambias de asistente y quieres una memoria común entre ellos — **Evita si:** te basta la memoria nativa de un único cliente o no usas MCP<br>
**Combina con:** [mem0](human/fichas/mem0.md) · [ruflo](human/fichas/ruflo.md)<br>
**Más:** [ficha completa](human/fichas/agentmemory.md) · [GitHub](https://github.com/rohitg00/agentmemory)

#### 🧠 Letta
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 25.4k<br>
**Qué es:** Crea agentes que gestionan su propia memoria en bloques editables y archivos, y persisten entre conversaciones. Incluye servidor, API y entorno de desarrollo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/letta-ai/letta/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres agentes con memoria de largo plazo gestionada — **Evita si:** solo necesitas una capa de memoria para tu app; mira `mem0`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/letta.md) · [GitHub](https://github.com/letta-ai/letta)

#### 🧠 Engram
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 8.2k<br>
**Qué es:** Da a cualquier agente compatible con MCP una memoria local de decisiones y aprendizajes, sin dependencias pesadas.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/Gentleman-Programming/engram/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres memoria local simple para cualquier agente — **Evita si:** solo usas Claude Code y quieres algo automático; mira `claude-mem`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [OpenCode](human/fichas/opencode.md)<br>
**Más:** [ficha completa](human/fichas/engram.md) · [GitHub](https://github.com/Gentleman-Programming/engram)

### RAG y motores de conocimiento

#### 📎 RAGFlow ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 94.2k<br>
**Qué es:** Procesa PDFs, tablas e imágenes con parsing visual, crea bases de conocimiento con citas trazables y añade agentes y workflows.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/infiniflow/ragflow/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tus documentos son complejos y necesitas citas fiables — **Evita si:** quieres algo ligero en un portátil; mira `anything-llm`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/ragflow.md) · [GitHub](https://github.com/infiniflow/ragflow)

#### 📎 LightRAG
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 40.7k<br>
**Qué es:** Construye un grafo de entidades a partir de tus documentos y consulta en modo local, global o híbrido. Más barato que GraphRAG.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/HKUDS/LightRAG/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres RAG con grafo sin el coste de GraphRAG — **Evita si:** no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md)<br>
**Más:** [ficha completa](human/fichas/lightrag.md) · [GitHub](https://github.com/HKUDS/LightRAG)

#### 📎 PageIndex
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.4k<br>
**Qué es:** Genera un árbol tipo índice del documento y deja que el LLM navegue por él como un experto. Funciona bien con informes largos y estructurados.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/VectifyAI/PageIndex/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tus documentos son largos y con estructura clara — **Evita si:** tienes miles de documentos cortos; usa búsqueda vectorial<br>
**Combina con:** [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/pageindex.md) · [GitHub](https://github.com/VectifyAI/PageIndex)

#### 🔗 graphrag
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 36.6k<br>
**Qué es:** Resuelve las preguntas que requieren conectar entidades dispersas en muchos documentos, donde el RAG clásico falla.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/graphrag/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto — **Evita si:** un RAG simple basta o el coste de indexado con LLM es prohibitivo<br>
**Combina con:** [graphify](human/fichas/graphify.md) · [mcp-neo4j](human/fichas/mcp-neo4j.md) · [turbovec](human/fichas/turbovec.md)<br>
**Más:** [ficha completa](human/fichas/graphrag.md) · [GitHub](https://github.com/microsoft/graphrag)

### Bases vectoriales y búsqueda semántica

#### 🧮 Qdrant ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 35.6k<br>
**Qué es:** Guarda embeddings con metadatos y los busca con filtros rápidos, a escala. Muy usada como memoria de RAG y agentes.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/qdrant/qdrant/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una base vectorial dedicada y rápida — **Evita si:** ya tienes PostgreSQL y poco volumen; mira `pgvector`<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [langchain](human/fichas/langchain.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/qdrant.md) · [GitHub](https://github.com/qdrant/qdrant)

#### 🧮 Milvus
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 46.7k<br>
**Qué es:** Pensada para producción con grandes volúmenes, alta disponibilidad y varios tipos de índices. Tiene una versión ligera para empezar.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/milvus-io/milvus/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** esperas volúmenes muy grandes de vectores — **Evita si:** tu proyecto es pequeño; mira `chroma` o `qdrant`<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/milvus.md) · [GitHub](https://github.com/milvus-io/milvus)

#### 🧮 Faiss
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 41.7k<br>
**Qué es:** Base de muchas bases vectoriales; ideal para investigación o cuando quieres índices en memoria sin servidor.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/facebookresearch/faiss/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas índices vectoriales en memoria y máximo control — **Evita si:** quieres persistencia y API listas; mira `qdrant`<br>
**Combina con:** [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/faiss.md) · [GitHub](https://github.com/facebookresearch/faiss)

#### 🧮 Chroma
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 29.7k<br>
**Qué es:** Se usa embebida en tu script Python o como servidor, con embeddings automáticos. Perfecta para prototipos de RAG.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install chromadb` (comprobar los pasos completos en la ficha).<br>
**Elige si:** empiezas con RAG y quieres lo más simple — **Evita si:** necesitas gran escala y filtros complejos; mira `qdrant` o `milvus`<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/chroma.md) · [GitHub](https://github.com/chroma-core/chroma)

#### 🧮 pgvector
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.7k<br>
**Qué es:** Guarda embeddings en una columna y búscalos con SQL, con índices HNSW o IVFFlat. Evita añadir otra base de datos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/pgvector/pgvector/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** ya usas PostgreSQL y quieres vectores — **Evita si:** tienes volúmenes muy grandes; mira `milvus`<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/pgvector.md) · [GitHub](https://github.com/pgvector/pgvector)

#### ⚡ turbovec
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 17.5k<br>
**Qué es:** Resuelve el coste de memoria y cómputo de la búsqueda vectorial cuando una vector DB completa es demasiado para tu escala.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/RyanCodrai/turbovec/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas vector search veloz y embebido sin desplegar una DB — **Evita si:** ya usas una vector DB completa con persistencia y escalado horizontal<br>
**Combina con:** [mem0](human/fichas/mem0.md) · [graphrag](human/fichas/graphrag.md)<br>
**Más:** [ficha completa](human/fichas/turbovec.md) · [GitHub](https://github.com/RyanCodrai/turbovec)

### Serving y gateways de LLM

#### 🚀 vLLM ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 96.9k<br>
**Qué es:** Sirve modelos abiertos a muchos usuarios con una API compatible con OpenAI, gracias a PagedAttention y batching continuo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install vllm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas servir LLM abiertos a muchos usuarios en GPU — **Evita si:** solo los usas tú en un portátil; mira `ollama`<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [Open WebUI](human/fichas/open-webui.md)<br>
**Más:** [ficha completa](human/fichas/vllm.md) · [GitHub](https://github.com/vllm-project/vllm)

#### 🔀 litellm
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 63.3k<br>
**Qué es:** Resuelve el lock-in: cambias de proveedor o añades fallback sin reescribir el código de tu app.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/BerriAI/litellm/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas con múltiples modelos o quieres fallback/control de costos — **Evita si:** usas un único proveedor fijo y no necesitas abstracción<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [langfuse](human/fichas/langfuse.md) · [llm-council](human/fichas/llm-council.md)<br>
**Más:** [ficha completa](human/fichas/litellm.md) · [GitHub](https://github.com/BerriAI/litellm)

#### 🚀 SGLang
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 38.9k<br>
**Qué es:** Compite con vLLM en velocidad, con caché de prefijos RadixAttention y buen soporte de salidas estructuradas. Muy usado para modelos grandes como DeepSeek.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/sgl-project/sglang/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas el máximo rendimiento en servicio de LLM — **Evita si:** quieres la opción más documentada; mira `vllm`<br>
**Combina con:** [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/sglang.md) · [GitHub](https://github.com/sgl-project/sglang)

#### 🧬 TensorRT-LLM
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 15.1k<br>
**Qué es:** Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados. Transforma modelos compatibles y los ejecuta con optimizaciones de memoria, precisión y paralelismo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** despliegas LLM en GPU NVIDIA y necesitas optimizar la inferencia — **Evita si:** el coste operativo supera el volumen de uso del proyecto<br>
**Más:** [ficha completa](human/fichas/tensorrt-llm.md) · [GitHub](https://github.com/NVIDIA/TensorRT-LLM)

#### 🧬 backdoor
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 302<br>
**Qué es:** Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. Traduce solicitudes y gestiona la configuración de proveedores como servicios compatibles u Ollama.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/ajsai47/backdoor/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar cómo conectar otros modelos al harness de Claude Code — **Evita si:** el coste operativo supera el volumen de uso del proyecto<br>
**Más:** [ficha completa](human/fichas/backdoor.md) · [GitHub](https://github.com/ajsai47/backdoor)

### Ahorro de contexto y tokens

#### 🗜️ headroom ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 79.7k<br>
**Qué es:** Resuelve el dolor habitual de los agentes: quedarse sin ventana de contexto a mitad de una tarea larga.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/headroomlabs-ai/headroom/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** te quedas sin contexto en sesiones largas — **Evita si:** tus prompts ya caben holgados o la pérdida de detalle por resumen es inaceptable<br>
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md) · [codegraph](human/fichas/codegraph.md)<br>
**Más:** [ficha completa](human/fichas/headroom.md) · [GitHub](https://github.com/headroomlabs-ai/headroom)

#### 🧬 rtk
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 86.6k<br>
**Qué es:** Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. Resume resultados de pruebas, diffs y logs antes de entregarlos al agente y registra el ahorro observado.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `winget install rtk-ai.rtk` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tu agente consume demasiado contexto leyendo salidas extensas de terminal — **Evita si:** el coste operativo supera el volumen de uso del proyecto<br>
**Más:** [ficha completa](human/fichas/rtk.md) · [GitHub](https://github.com/rtk-ai/rtk)

### Observabilidad, evaluación y guardrails

#### 📡 promptfoo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 27.2k<br>
**Qué es:** Defines casos de prueba en YAML y comparas salidas de varios modelos con aserciones. También escanea vulnerabilidades como inyección de prompts.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/promptfoo/promptfoo/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres pruebas automáticas de prompts y seguridad — **Evita si:** necesitas observabilidad en producción; mira `langfuse`<br>
**Combina con:** [langfuse](human/fichas/langfuse.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/promptfoo.md) · [GitHub](https://github.com/promptfoo/promptfoo)

#### 📡 langfuse
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 37.4k<br>
**Qué es:** Resuelve la opacidad: ves qué prompt, qué modelo, qué coste y qué salida tuvo cada paso de tu pipeline.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/langfuse/langfuse/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** operas agentes en serio y necesitas trazas/costes/eval — **Evita si:** haces prototipos triviales o no quieres operar el backend<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [litellm](human/fichas/litellm.md) · [ag2](human/fichas/ag2.md)<br>
**Más:** [ficha completa](human/fichas/langfuse.md) · [GitHub](https://github.com/langfuse/langfuse)

#### 📡 MLflow
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 28.8k<br>
**Qué es:** Registra experimentos, versiona modelos y, para LLM, ofrece trazas, evaluación y gestión de prompts.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/mlflow/mlflow/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu equipo hace ML clásico y LLM y quiere una sola plataforma — **Evita si:** solo trazas LLM y quieres algo más ligero; mira `langfuse`<br>
**Combina con:** [Transformers](human/fichas/transformers.md) · [DSPy](human/fichas/dspy.md)<br>
**Más:** [ficha completa](human/fichas/mlflow.md) · [GitHub](https://github.com/mlflow/mlflow)

#### 📝 loguru
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 24.2k<br>
**Qué es:** Resuelve la fricción del módulo `logging` stdlib, que exige boilerplate para algo tan básico como imprimir logs legibles.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install loguru` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres logging fácil y legible en Python sin pelear con stdlib — **Evita si:** ya usas el stdlib `logging` configurado o tienes un stack de observabilidad corporativo<br>
**Combina con:** [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/loguru.md) · [GitHub](https://github.com/Delgan/loguru)

#### 📡 Opik
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 23.4k<br>
**Qué es:** Traza llamadas, ejecuta evaluaciones automáticas y monitorea producción con paneles. Incluye optimizador de prompts.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install opik` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres observabilidad y evaluación en un solo producto abierto — **Evita si:** prefieres la opción más extendida; mira `langfuse`<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md)<br>
**Más:** [ficha completa](human/fichas/opik.md) · [GitHub](https://github.com/comet-ml/opik)

#### 📡 DeepEval
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 19.5k<br>
**Qué es:** Escribe pruebas para tus apps de LLM con métricas como fidelidad, relevancia o alucinación, e intégralas en tu CI.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -U deepeval` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres tests de LLM en Python como pytest — **Evita si:** prefieres configurar en YAML y comparar modelos; mira `promptfoo`<br>
**Combina con:** [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/deepeval.md) · [GitHub](https://github.com/confident-ai/deepeval)

#### 📡 Ragas
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 16.3k<br>
**Qué es:** Mide fidelidad, relevancia del contexto y calidad de respuestas, y genera conjuntos de prueba a partir de tus documentos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install ragas` (comprobar los pasos completos en la ficha).<br>
**Elige si:** evalúas un sistema RAG — **Evita si:** necesitas red teaming de seguridad; mira `promptfoo`<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/ragas.md) · [GitHub](https://github.com/vibrantlabsai/ragas)

#### 📡 Phoenix
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 12.3k<br>
**Qué es:** Visualiza trazas de agentes y RAG, ejecuta evaluaciones y gestiona datasets y experimentos. Corre en local o en tu servidor.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install arize-phoenix` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres observabilidad basada en OpenTelemetry — **Evita si:** buscas la plataforma más usada; mira `langfuse`<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [LangGraph](human/fichas/langgraph.md)<br>
**Más:** [ficha completa](human/fichas/phoenix.md) · [GitHub](https://github.com/Arize-ai/phoenix)

#### 📡 NeMo Guardrails
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 7.5k<br>
**Qué es:** Controla de qué puede hablar tu bot, bloquea jailbreaks y valida entradas y salidas con reglas en el lenguaje Colang.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA-NeMo/Guardrails/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas políticas de seguridad en un chatbot — **Evita si:** solo quieres probar vulnerabilidades; mira `promptfoo`<br>
**Combina con:** [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/guardrails.md) · [GitHub](https://github.com/NVIDIA-NeMo/Guardrails)

---

## 🧑‍💻 7. Entender código, trabajar con datos y entrenar modelos

Herramientas para analizar código, procesar datos, aprender machine learning y entrenar modelos. Separa los ejemplos de aprendizaje de las librerías que integras.

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
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 29.3k<br>
**Qué es:** Genera un archivo XML, Markdown o texto con la estructura y el código del repo, respetando .gitignore y contando tokens. También funciona como servidor MCP.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx repomix` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres dar tu repo completo a un LLM — **Evita si:** el repo es enorme; mira `codebase-memory-mcp` o `serena`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/repomix.md) · [GitHub](https://github.com/yamadashy/repomix)

#### 🕸️ graphify
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 148k<br>
**Qué es:** Resuelve el onboarding visual: un índice textual no basta cuando hay relaciones entre archivos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pipx install graphify` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres ver conexiones visualmente o auditar un sistema — **Evita si:** solo necesitas índice textual barato (codegraph) o tu proyecto es trivial<br>
**Combina con:** [codegraph](human/fichas/codegraph.md) · [graphrag](human/fichas/graphrag.md)<br>
**Más:** [ficha completa](human/fichas/graphify.md) · [GitHub](https://github.com/Graphify-Labs/graphify)

#### 📊 codegraph
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 77.6k<br>
**Qué es:** Resuelve el coste de contexto de los agentes en repos grandes.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/colbymchenry/codegraph/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas repos grandes y el contexto del agente es caro — **Evita si:** tu base de código es pequeña y no justifica mantener un índice<br>
**Combina con:** [graphify](human/fichas/graphify.md) · [headroom](human/fichas/headroom.md)<br>
**Más:** [ficha completa](human/fichas/codegraph.md) · [GitHub](https://github.com/colbymchenry/codegraph)

#### 🧬 codebase-memory-mcp
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 48.6k<br>
**Qué es:** Indexa repos en milisegundos y da al agente herramientas MCP para entender arquitectura, dependencias y cambios sin leer archivo por archivo.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu agente trabaja en repos grandes — **Evita si:** tu repo es pequeño; usa `repomix`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Serena](human/fichas/serena.md)<br>
**Más:** [ficha completa](human/fichas/codebase-memory-mcp.md) · [GitHub](https://github.com/DeusData/codebase-memory-mcp)

#### 🧭 GitNexus
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 48.5k<br>
**Qué es:** Resuelve el "llegar a un proyecto ajeno y no saber por dónde empezar": lo navegas y lo discutes en vez de leer ficheros sueltos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install -g gitnexus` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres entender un repo puntual de forma visual — **Evita si:** necesitas indexar muchos repos a escala (codegraph) o no quieres front web<br>
**Combina con:** [codegraph](human/fichas/codegraph.md)<br>
**Más:** [ficha completa](human/fichas/gitnexus.md) · [GitHub](https://github.com/abhigyanpatwari/GitNexus)

#### 🧬 tree-sitter
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 27.5k<br>
**Qué es:** Genera parsers rápidos que actualizan el árbol sintáctico mientras editas. Lo usan editores, Aider, ast-grep y muchas herramientas de código con IA.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/tree-sitter/tree-sitter/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** construyes herramientas que entienden código — **Evita si:** solo necesitas buscar patrones; mira `ast-grep`<br>
**Combina con:** [ast-grep](human/fichas/ast-grep.md) · [Aider](human/fichas/aider.md)<br>
**Más:** [ficha completa](human/fichas/tree-sitter.md) · [GitHub](https://github.com/tree-sitter/tree-sitter)

#### 🧬 DeepWiki Open
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 18.4k<br>
**Qué es:** Analiza un repositorio y crea documentación navegable con diagramas y un chat para preguntar sobre el código.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres documentación automática de un repositorio — **Evita si:** necesitas contexto de librerías externas; mira `context7`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/deepwiki-open.md) · [GitHub](https://github.com/AsyncFuncAI/deepwiki-open)

### Calidad, seguridad y benchmarks de código

#### 🛡️ Semgrep ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 17.7k<br>
**Qué es:** Encuentra bugs y vulnerabilidades con miles de reglas comunitarias o propias. Muy usado en CI de seguridad.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install semgrep` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres análisis de seguridad en CI — **Evita si:** solo quieres refactors estructurales; mira `ast-grep`<br>
**Combina con:** [Defending Code Reference Harness](human/fichas/defending-code-reference-harness.md)<br>
**Más:** [ficha completa](human/fichas/semgrep.md) · [GitHub](https://github.com/semgrep/semgrep)

#### 🛡️ ast-grep
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 16.6k<br>
**Qué es:** Busca y reemplaza código por su estructura (AST), no por texto. Útil para refactors masivos y reglas de lint propias.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ast-grep/ast-grep/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas buscar o reescribir código por estructura — **Evita si:** buscas análisis de seguridad con reglas existentes; mira `semgrep`<br>
**Combina con:** [tree-sitter](human/fichas/tree-sitter.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/ast-grep.md) · [GitHub](https://github.com/ast-grep/ast-grep)

#### 🛡️ Defending Code Reference Harness
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 7.8k<br>
**Qué es:** Implementación de referencia para descubrir y corregir vulnerabilidades de forma autónoma con Claude, basada en experiencia con equipos de seguridad.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/defending-code-reference-harness/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un flujo de seguridad con agentes probado — **Evita si:** solo necesitas un escáner estático; mira `semgrep`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Semgrep](human/fichas/semgrep.md)<br>
**Más:** [ficha completa](human/fichas/defending-code-reference-harness.md) · [GitHub](https://github.com/anthropics/defending-code-reference-harness)

#### 🛡️ SWE-bench
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 6.2k<br>
**Qué es:** Da al modelo un repositorio y un issue y comprueba si su parche pasa las pruebas. Es la referencia para medir agentes de código.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/SWE-bench/SWE-bench/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas medir agentes de código con un estándar — **Evita si:** solo quieres usar un agente<br>
**Combina con:** [SWE-agent](human/fichas/swe-agent.md)<br>
**Más:** [ficha completa](human/fichas/swe-bench.md) · [GitHub](https://github.com/SWE-bench/SWE-bench)

### Entrenar y afinar modelos

#### 🏋️ Unsloth ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 79.5k<br>
**Qué es:** Afina modelos como Qwen, Llama o Gemma en una sola GPU y expórtalos a GGUF u Ollama. Ofrece notebooks gratuitos y una interfaz local.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/unslothai/unsloth/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres afinar un LLM con pocos recursos — **Evita si:** necesitas muchas técnicas y una UI de entrenamiento; mira `llama-factory`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [TRL](human/fichas/trl.md)<br>
**Más:** [ficha completa](human/fichas/unsloth.md) · [GitHub](https://github.com/unslothai/unsloth)

#### 🧑‍💻 tensorflow
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 202k<br>
**Qué es:** Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. Define operaciones y modelos y ofrece herramientas de entrenamiento e inferencia en distintos dispositivos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install tensorflow` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tu proyecto necesita el ecosistema TensorFlow para entrenamiento o despliegue — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/tensorflow.md) · [GitHub](https://github.com/tensorflow/tensorflow)

#### 🏋️ Transformers
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 169k<br>
**Qué es:** Da acceso a cientos de miles de modelos con una API común para inferencia y entrenamiento. Es la base del ecosistema de modelos abiertos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/huggingface/transformers/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas con modelos abiertos en Python — **Evita si:** solo quieres chatear con un modelo local; mira `ollama`<br>
**Combina con:** [PEFT](human/fichas/peft.md) · [TRL](human/fichas/trl.md) · [PyTorch](human/fichas/pytorch.md)<br>
**Más:** [ficha completa](human/fichas/transformers.md) · [GitHub](https://github.com/huggingface/transformers)

#### 🏋️ PyTorch
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 106k<br>
**Qué es:** Base de la mayoría de investigación y modelos abiertos actuales.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/pytorch/pytorch/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** entrenas o investigas modelos — **Evita si:** solo consumes APIs de LLM<br>
**Combina con:** [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/pytorch.md) · [GitHub](https://github.com/pytorch/pytorch)

#### 🏋️ LLaMA-Factory
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 76k<br>
**Qué es:** Soporta LoRA, QLoRA, ajuste completo, DPO y más desde una UI o CLI. Muy usado en investigación e industria.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/hiyouga/LlamaFactory/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres muchas técnicas de fine-tuning con UI — **Evita si:** buscas la opción más eficiente en memoria; mira `unsloth`<br>
**Combina con:** [PEFT](human/fichas/peft.md) · [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/llama-factory.md) · [GitHub](https://github.com/hiyouga/LlamaFactory)

#### 🏋️ PEFT
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 21.9k<br>
**Qué es:** Adapta modelos grandes entrenando solo una pequeña parte de los parámetros, ahorrando memoria y tiempo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install peft` (comprobar los pasos completos en la ficha).<br>
**Elige si:** afinas modelos con código propio — **Evita si:** prefieres una herramienta lista; mira `unsloth`<br>
**Combina con:** [Transformers](human/fichas/transformers.md) · [TRL](human/fichas/trl.md)<br>
**Más:** [ficha completa](human/fichas/peft.md) · [GitHub](https://github.com/huggingface/peft)

#### 🏋️ TRL
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 19.7k<br>
**Qué es:** Ofrece entrenadores listos para ajuste supervisado y por preferencias, usados para alinear modelos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install trl` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas SFT o RL sobre modelos abiertos — **Evita si:** quieres algo sin código; mira `llama-factory`<br>
**Combina con:** [Transformers](human/fichas/transformers.md) · [PEFT](human/fichas/peft.md) · [Unsloth](human/fichas/unsloth.md)<br>
**Más:** [ficha completa](human/fichas/trl.md) · [GitHub](https://github.com/huggingface/trl)

#### 🧑‍💻 warp
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 7.3k<br>
**Qué es:** Framework de NVIDIA que compila funciones de Python en kernels para simulación física y cálculo en CPU o GPU. Compila funciones especializadas y aporta primitivas de geometría, física y diferenciación.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install warp-lang` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres escribir simulaciones o kernels de cálculo acelerado desde Python — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/warp.md) · [GitHub](https://github.com/NVIDIA/warp)

#### 🧑‍💻 bionemo-recipes
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 877<br>
**Qué es:** Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. Presenta configuraciones de entrenamiento con TransformerEngine y frameworks distribuidos para modelos biológicos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA-BioNeMo/bionemo-recipes/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas en entrenamiento de modelos para datos biológicos — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/bionemo-recipes.md) · [GitHub](https://github.com/NVIDIA-BioNeMo/bionemo-recipes)

### Aprender LLMs desde cero

#### 📘 LLM Course ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 85.1k<br>
**Qué es:** Tres rutas: fundamentos, científico de LLM (entrenar y afinar) e ingeniero de LLM (apps y despliegue), con recursos y notebooks ejecutables.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mlabonne/llm-course/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una ruta completa para aprender LLM — **Evita si:** buscas un curso introductorio de apps; mira `generative-ai-for-beginners`<br>
**Combina con:** [Unsloth](human/fichas/unsloth.md) · [LLaMA-Factory](human/fichas/llama-factory.md)<br>
**Más:** [ficha completa](human/fichas/llm-course.md) · [GitHub](https://github.com/mlabonne/llm-course)

#### 📘 LLMs from Scratch
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 108k<br>
**Qué es:** Construyes atención, GPT, preentrenamiento y fine-tuning desde cero, entendiendo cada pieza. Ideal para aprender cómo funcionan por dentro.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/rasbt/LLMs-from-scratch/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres entender los LLM implementándolos — **Evita si:** solo quieres usar modelos existentes<br>
**Combina con:** [PyTorch](human/fichas/pytorch.md)<br>
**Más:** [ficha completa](human/fichas/llms-from-scratch.md) · [GitHub](https://github.com/rasbt/LLMs-from-scratch)

#### 🧑‍💻 awesome-machine-learning
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 74.8k<br>
**Qué es:** Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema. Reúne enlaces a implementaciones, cursos y material para comparar herramientas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/josephmisiti/awesome-machine-learning/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas alternativas de aprendizaje automático en distintos lenguajes — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/awesome-machine-learning.md) · [GitHub](https://github.com/josephmisiti/awesome-machine-learning)

#### 🔬 nanoGPT
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 64.8k<br>
**Qué es:** Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/karpathy/nanoGPT/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres entender el entrenamiento de un GPT desde cero — **Evita si:** solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat)<br>
**Combina con:** [nanochat](human/fichas/nanochat.md)<br>
**Más:** [ficha completa](human/fichas/nanogpt.md) · [GitHub](https://github.com/karpathy/nanoGPT)

#### 💬 nanochat
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 60.6k<br>
**Qué es:** Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/karpathy/nanochat/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres el pipeline completo de un chat end-to-end — **Evita si:** solo necesitas el core del modelo (nanoGPT) o un modelo listo para usar<br>
**Combina con:** [nanoGPT](human/fichas/nanogpt.md)<br>
**Más:** [ficha completa](human/fichas/nanochat.md) · [GitHub](https://github.com/karpathy/nanochat)

#### ⚙️ llm.c
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 31.5k<br>
**Qué es:** Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framework.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/karpathy/llm.c/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres bajo nivel sin abstracciones y tienes GPU CUDA — **Evita si:** prefieres PyTorch (nanoGPT) o no tienes CUDA<br>
**Combina con:** [nanoGPT](human/fichas/nanogpt.md)<br>
**Más:** [ficha completa](human/fichas/llm-c.md) · [GitHub](https://github.com/karpathy/llm.c)

#### 🧑‍💻 train-llm-from-scratch
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 13.2k<br>
**Qué es:** Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación. Implementa un Transformer y recorre preparación de datos, entrenamiento y ajuste del modelo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres entender el entrenamiento de un LLM mediante una implementación completa — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/train-llm-from-scratch.md) · [GitHub](https://github.com/FareedKhan-dev/train-llm-from-scratch)

#### 🧑‍💻 python-machine-learning-book
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 12.7k<br>
**Qué es:** Código de la primera edición del libro Python Machine Learning, con ejemplos de algoritmos y evaluación. Presenta notebooks y scripts que acompañan los capítulos y conceptos del libro.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/rasbt/python-machine-learning-book/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar los ejemplos de la primera edición del libro — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/python-machine-learning-book.md) · [GitHub](https://github.com/rasbt/python-machine-learning-book)

#### 🧑‍💻 MachineLearning
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 5.8k<br>
**Qué es:** Ejemplos educativos de algoritmos de machine learning y redes neuronales con Python. Agrupa implementaciones y ejercicios de clasificación, reducción de dimensiones y aprendizaje profundo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/wepe/MachineLearning/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres explorar implementaciones pequeñas de algoritmos clásicos — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/machinelearning.md) · [GitHub](https://github.com/wepe/MachineLearning)

#### 📘 how-to-train-your-gpt
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 4.2k<br>
**Qué es:** Resuelve el "quiero entenderlo con explicación narrada" frente al código desnudo de nanoGPT.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/raiyanyahya/how-to-train-your-gpt/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una guía explicada y narrada — **Evita si:** prefieres solo el código limpio (nanoGPT) o buscas algo productivo<br>
**Combina con:** [nanoGPT](human/fichas/nanogpt.md) · [nanochat](human/fichas/nanochat.md)<br>
**Más:** [ficha completa](human/fichas/how-to-train-your-gpt.md) · [GitHub](https://github.com/raiyanyahya/how-to-train-your-gpt)

### Modelos abiertos y fundacionales

#### 🧠 TimesFM ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 35.5k<br>
**Qué es:** Predice ventas, demanda o tráfico a partir del histórico sin entrenar un modelo propio (zero-shot).<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/google-research/timesfm/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas pronósticos rápidos sin entrenar modelos — **Evita si:** necesitas explicabilidad estadística clásica<br>
**Combina con:** [Polars](human/fichas/polars.md) · [DuckDB](human/fichas/duckdb.md)<br>
**Más:** [ficha completa](human/fichas/timesfm.md) · [GitHub](https://github.com/google-research/timesfm)

#### 🧩 DeepSeek-Coder
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 24.4k<br>
**Qué es:** Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia infraestructura.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un modelo de código abierto y desplegable on-prem — **Evita si:** prefieres APIs comerciales gestionadas o no tienes GPU para servirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [codegraph](human/fichas/codegraph.md)<br>
**Más:** [ficha completa](human/fichas/deepseek-coder.md) · [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder)

#### 🌌 cosmos
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 12.4k<br>
**Qué es:** Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA/cosmos/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas IA física/robótica y necesitas datos sintéticos — **Evita si:** haces tareas de texto/UI o no tienes GPU para servirlo<br>
**Combina con:** [diffusers](human/fichas/diffusers.md)<br>
**Más:** [ficha completa](human/fichas/cosmos.md) · [GitHub](https://github.com/NVIDIA/cosmos)

#### 🧠 Nemotron (NVIDIA)
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 2.3k<br>
**Qué es:** Reúne guías de entrenamiento, despliegue y casos de uso de los modelos Nemotron, pensados para IA agéntica eficiente.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas GPUs NVIDIA y quieres modelos abiertos optimizados — **Evita si:** buscas la forma más simple de correr modelos; mira `ollama`<br>
**Combina con:** [vLLM](human/fichas/vllm.md) · [NemoClaw](human/fichas/nemoclaw.md)<br>
**Más:** [ficha completa](human/fichas/nemotron.md) · [GitHub](https://github.com/NVIDIA-NeMo/Nemotron)

### CLIs y SDKs de desarrollo

#### 🧰 GitHub CLI ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 47k<br>
**Qué es:** No es un agente: es la herramienta que los agentes de código usan para abrir PRs, revisar issues o lanzar workflows.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/cli/cli/blob/trunk/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas con GitHub desde la terminal o con agentes — **Evita si:** usas GitLab u otra forja<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [GitHub MCP Server](human/fichas/github-mcp-server.md)<br>
**Más:** [ficha completa](human/fichas/cli.md) · [GitHub](https://github.com/cli/cli)

#### 🐍 openai-python
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 32.2k<br>
**Qué es:** Resuelve el glue HTTP: no escribes peticiones a mano, usas clientes tipados con streaming.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `pip install openai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** usas modelos de OpenAI desde Python y quieres el cliente oficial — **Evita si:** quieres abstracción multi-proveedor (litellm) o no usas OpenAI<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/openai-python.md) · [GitHub](https://github.com/openai/openai-python)

### Datos y notebooks

#### 🗃️ DuckDB ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 43.1k<br>
**Qué es:** El "SQLite de la analítica": sin servidor, embebida en Python, R o Node, y capaz de procesar millones de filas en segundos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/duckdb/duckdb/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres SQL analítico rápido sin montar servidores — **Evita si:** necesitas una base transaccional multiusuario; usa PostgreSQL<br>
**Combina con:** [marimo](human/fichas/marimo.md) · [Apache Superset](human/fichas/superset.md)<br>
**Más:** [ficha completa](human/fichas/duckdb.md) · [GitHub](https://github.com/duckdb/duckdb)

#### 🗃️ marimo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 23.6k<br>
**Qué es:** Al cambiar una celda se recalculan las dependientes, evitando estados ocultos. Incluye SQL, gráficos interactivos y asistente de IA.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install marimo` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres notebooks reproducibles y versionables — **Evita si:** dependes de extensiones de Jupyter<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [Polars](human/fichas/polars.md)<br>
**Más:** [ficha completa](human/fichas/marimo.md) · [GitHub](https://github.com/marimo-team/marimo)

#### 🗃️ Polars
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.3k<br>
**Qué es:** API expresiva con ejecución perezosa y paralela para procesar datos grandes en un solo equipo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install polars` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tu análisis con pandas es lento — **Evita si:** prefieres SQL; mira `duckdb`<br>
**Combina con:** [marimo](human/fichas/marimo.md)<br>
**Más:** [ficha completa](human/fichas/polars.md) · [GitHub](https://github.com/pola-rs/polars)

#### 📓 data-science-ipython-notebooks
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 29.4k<br>
**Qué es:** Resuelve el "aprender DS con ejemplos reales" sin tener que montarlos tú desde cero.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/donnemartin/data-science-ipython-notebooks/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** estudias/consultas DS con ejemplos ejecutables — **Evita si:** buscas una librería, no ejemplos, o necesitas material actualizado a las versiones más recientes<br>
**Combina con:** [dash](human/fichas/dash.md) · [streamlit](human/fichas/streamlit.md)<br>
**Más:** [ficha completa](human/fichas/data-science-ipython-notebooks.md) · [GitHub](https://github.com/donnemartin/data-science-ipython-notebooks)

#### 🗄️ awesome-bigdata
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 14.7k<br>
**Qué es:** Resuelve el "qué uso para X a escala": un panorama del stack de datos grandes en un solo vistazo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/oxnr/awesome-bigdata/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** diseñas pipelines de datos grandes y necesitas descubrir el ecosistema — **Evita si:** tu proyecto es pequeño y no justifica herramientas de big data<br>
**Combina con:** [awesome-dataviz](human/fichas/awesome-dataviz.md)<br>
**Más:** [ficha completa](human/fichas/awesome-bigdata.md) · [GitHub](https://github.com/oxnr/awesome-bigdata)

#### 🧑‍💻 hudi
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 6.4k<br>
**Qué es:** Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. Añade índices, actualizaciones y procesamiento incremental a tablas de un lago de datos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/apache/hudi/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas gestionar cambios y cargas incrementales en un data lake — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/hudi.md) · [GitHub](https://github.com/apache/hudi)

#### 🧑‍💻 GlobalBuildingAtlas
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 2.3k<br>
**Qué es:** Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. Publica distintas capas geoespaciales y herramientas para estimar alturas y construir representaciones de edificios.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas geometría de edificios para análisis territorial o visualización urbana — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Combina con:** [three.js](human/fichas/three-js.md)<br>
**Más:** [ficha completa](human/fichas/globalbuildingatlas.md) · [GitHub](https://github.com/zhu-xlab/GlobalBuildingAtlas)

#### 🧑‍💻 BigData
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 642<br>
**Qué es:** Colección educativa de proyectos de datos con ejercicios de Hive, HDFS, Spark, HBase y sistemas de recomendación. Las carpetas desarrollan problemas de ingestión, análisis y procesamiento distribuido de datos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/monsonlee/BigData/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar ejemplos prácticos del ecosistema de big data — **Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico<br>
**Más:** [ficha completa](human/fichas/bigdata.md) · [GitHub](https://github.com/monsonlee/BigData)

---

## 🏠 8. Usar modelos y asistentes locales

Motores de modelos, clientes de chat y espacios de trabajo. Instalar una interfaz local no garantiza que el modelo sea local: comprueba su backend.

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
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 187k<br>
**Qué es:** Un comando para bajar y ejecutar modelos como Qwen, Gemma, DeepSeek o gpt-oss. Casi todas las apps de IA local lo soportan.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ollama/ollama/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres modelos locales funcionando en minutos — **Evita si:** necesitas servir a muchos usuarios con GPU; mira `vllm`<br>
**Combina con:** [Open WebUI](human/fichas/open-webui.md) · [n8n](human/fichas/n8n.md) · [AnythingLLM](human/fichas/anything-llm.md)<br>
**Más:** [ficha completa](human/fichas/ollama.md) · [GitHub](https://github.com/ollama/ollama)

#### 🦙 llama.cpp
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 135k<br>
**Qué es:** Base de Ollama, LM Studio y muchas apps. Incluye un servidor compatible con OpenAI y herramientas para cuantizar modelos GGUF.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ggml-org/llama.cpp/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres el máximo control y rendimiento local — **Evita si:** prefieres simplicidad; mira `ollama`<br>
**Combina con:** [Open WebUI](human/fichas/open-webui.md)<br>
**Más:** [ficha completa](human/fichas/llama-cpp.md) · [GitHub](https://github.com/ggml-org/llama.cpp)

#### 🦙 LocalAI
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 50.4k<br>
**Qué es:** Sustituye la API de OpenAI por una propia que corre modelos abiertos de muchos tipos. Útil para apps que ya hablan con OpenAI.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mudler/LocalAI/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una API tipo OpenAI local para varias modalidades — **Evita si:** solo necesitas chat local simple; mira `ollama`<br>
**Combina con:** [AnythingLLM](human/fichas/anything-llm.md)<br>
**Más:** [ficha completa](human/fichas/localai.md) · [GitHub](https://github.com/mudler/LocalAI)

#### 🦙 exo
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 48.4k<br>
**Qué es:** Une Macs, PCs o teléfonos en un clúster que comparte la carga de un modelo que no cabría en uno solo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/exo-explore/exo/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tienes varios equipos y quieres correr un modelo grande — **Evita si:** un solo equipo te basta; mira `ollama`<br>
**Combina con:** [Open WebUI](human/fichas/open-webui.md)<br>
**Más:** [ficha completa](human/fichas/exo.md) · [GitHub](https://github.com/exo-explore/exo)

#### 📏 llmfit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 39k<br>
**Qué es:** Resuelve la elección subjetiva de modelo: la conviertes en un flujo objetivo y reproducible con métricas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `uv tool install -U llmfit` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas elegir modelo con datos y reproducibilidad — **Evita si:** ya tienes el modelo decidido o tu caso no justifica un harness de evaluación<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/llmfit.md) · [GitHub](https://github.com/AlexsJones/llmfit)

#### 🦙 llamafile
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 26.6k<br>
**Qué es:** Empaqueta modelo y motor en un ejecutable que funciona en Windows, macOS y Linux sin instalar nada. Proyecto de Mozilla.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mozilla-ai/llamafile/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres repartir un modelo que funcione con doble clic — **Evita si:** vas a cambiar de modelos a menudo; mira `ollama`<br>
**Más:** [ficha completa](human/fichas/llamafile.md) · [GitHub](https://github.com/mozilla-ai/llamafile)

#### 🏠 transformers.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 16.4k<br>
**Qué es:** Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript. Carga modelos compatibles y realiza inferencia en el navegador o en entornos JavaScript sin un servidor de modelos propio.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm i @huggingface/transformers` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres ejecutar un modelo compatible dentro del navegador — **Evita si:** no quieres mantener modelos o un entorno de ejecución propio<br>
**Combina con:** [swr](human/fichas/swr.md)<br>
**Más:** [ficha completa](human/fichas/transformers-js.md) · [GitHub](https://github.com/huggingface/transformers.js)

### Interfaces de chat auto-hospedadas

#### 💬 Open WebUI ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 159k<br>
**Qué es:** Da a tu equipo un chat privado con usuarios, documentos, búsqueda web, herramientas y modelos locales o en la nube.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install open-webui` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas un ChatGPT privado para tu equipo — **Evita si:** solo quieres una app de escritorio individual; mira `jan`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [SearXNG](human/fichas/searxng.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/open-webui.md) · [GitHub](https://github.com/open-webui/open-webui)

#### 💬 Jan ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 45.7k<br>
**Qué es:** Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. Comprueba el modelo y backend activo: el modo local necesita recursos de tu equipo y la ruta remota conserva sus propios requisitos de acceso.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/janhq/jan/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un ChatGPT local en tu escritorio — **Evita si:** necesitas multiusuario; mira `open-webui`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/jan.md) · [GitHub](https://github.com/janhq/jan)

#### 💬 LobeHub
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 85.5k<br>
**Qué es:** Antes LobeChat: chat elegante con agentes, plugins, base de conocimiento y despliegue en un clic. Ahora añade agentes que trabajan en tus chats de equipo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/lobehub/lobehub/blob/canary/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un chat bonito y extensible con agentes — **Evita si:** necesitas el máximo control empresarial; mira `librechat`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/lobehub.md) · [GitHub](https://github.com/lobehub/lobehub)

#### 💬 Cherry Studio
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 53.5k<br>
**Qué es:** Chatea con decenas de proveedores y modelos locales, usa asistentes predefinidos, MCP y base de conocimiento desde una sola app.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/CherryHQ/cherry-studio/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una app de escritorio multi-proveedor completa — **Evita si:** solo quieres modelos locales simples; mira `jan`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/cherry-studio.md) · [GitHub](https://github.com/CherryHQ/cherry-studio)

#### 💬 Text Generation WebUI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 47.7k<br>
**Qué es:** La clásica "oobabooga": carga modelos en muchos formatos y backends, con chat, modo notebook y entrenamiento LoRA.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/oobabooga/textgen/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres experimentar con muchos backends locales — **Evita si:** quieres algo sencillo; mira `jan` u `ollama`<br>
**Más:** [ficha completa](human/fichas/textgen.md) · [GitHub](https://github.com/oobabooga/textgen)

#### 💬 LibreChat
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 47.1k<br>
**Qué es:** Une OpenAI, Anthropic, Google, Azure, OpenRouter y modelos locales con agentes, artifacts, búsqueda y control de usuarios.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/LibreChat-AI/LibreChat/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres todos los proveedores en un chat con SSO — **Evita si:** usas sobre todo modelos locales; mira `open-webui`<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/librechat.md) · [GitHub](https://github.com/LibreChat-AI/LibreChat)

#### 🏠 chatbox
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 42.3k<br>
**Qué es:** Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. Configura conexiones de modelos y conserva conversaciones en una aplicación multiplataforma.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/chatboxai/chatbox/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un cliente de escritorio que conecte varios modelos — **Evita si:** no quieres mantener modelos o un entorno de ejecución propio<br>
**Más:** [ficha completa](human/fichas/chatbox.md) · [GitHub](https://github.com/chatboxai/chatbox)

### Workspaces privados y segundos cerebros

#### 🏠 AnythingLLM ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 68.3k<br>
**Qué es:** Organiza documentos en espacios de trabajo, crea RAG sin configurar nada y añade agentes con herramientas. Escritorio o Docker multiusuario.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres RAG privado sin programar — **Evita si:** necesitas un pipeline de RAG a medida; mira `llama-index`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/anything-llm.md) · [GitHub](https://github.com/Mintplex-Labs/anything-llm)

#### ⛺ odysseus
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 95.6k<br>
**Qué es:** Sustituye la dispersión entre varios SaaS por un único panel que tú controlas.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/odysseus-dev/odysseus/blob/dev/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres operación privada todo-en-uno y aceptas operar la infra — **Evita si:** prefieres SaaS gestionado sin mantenimiento<br>
**Combina con:** [open-notebook](human/fichas/open-notebook.md) · [ECC](human/fichas/ecc.md) · [mem0](human/fichas/mem0.md)<br>
**Más:** [ficha completa](human/fichas/odysseus.md) · [GitHub](https://github.com/odysseus-dev/odysseus)

#### 🏠 PrivateGPT
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 57.6k<br>
**Qué es:** Ofrece una API lista para construir apps de IA sin que los datos salgan de tu entorno. Funciona con cualquier motor compatible con OpenAI.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/zylon-ai/private-gpt/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** construyes un producto de IA que no puede enviar datos fuera — **Evita si:** quieres una app lista para usuarios finales; mira `anything-llm`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md)<br>
**Más:** [ficha completa](human/fichas/private-gpt.md) · [GitHub](https://github.com/zylon-ai/private-gpt)

#### 🏠 Khoj
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 38.1k<br>
**Qué es:** Busca en tus documentos y en internet, crea agentes personalizados, programa resúmenes y hace investigación profunda. Accesible desde web, Obsidian, Emacs o WhatsApp.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/khoj-ai/khoj/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un asistente sobre tus notas personales — **Evita si:** necesitas una plataforma de equipo; mira `anything-llm`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/khoj.md) · [GitHub](https://github.com/khoj-ai/khoj)

#### 🏠 server
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 37.5k<br>
**Qué es:** Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia. Opera una nube personal con usuarios, almacenamiento y aplicaciones integrables.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/nextcloud/server/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas una plataforma autoalojada para documentos y colaboración — **Evita si:** no quieres mantener modelos o un entorno de ejecución propio<br>
**Más:** [ficha completa](human/fichas/nextcloud-server.md) · [GitHub](https://github.com/nextcloud/server)

#### 🏠 Hermes Desktop
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 14.6k<br>
**Qué es:** Para quien quiere usar Hermes Agent como aplicación y no solo desde la terminal.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/fathah/hermes-desktop/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Hermes Agent y prefieres una app de escritorio — **Evita si:** no usas Hermes<br>
**Combina con:** [hermes-agent](human/fichas/hermes-agent.md)<br>
**Más:** [ficha completa](human/fichas/hermes-desktop.md) · [GitHub](https://github.com/fathah/hermes-desktop)

#### 🏠 muse-spark
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 15<br>
**Aviso:** ⚠️ Procedencia y funcionalidad sin verificar; conservar como referencia.<br>
**Qué es:** Proyecto de terceros que se presenta como un estudio de IA de escritorio; su afiliación y funciones no están verificadas. El README describe un cliente multimodal y distribuciones binarias; el alcance real no se comprobó ejecutándolo.<br>
**Acceso:** API: por confirmar · Coste por confirmar<br>
**Arranque:** [Instrucciones originales](https://github.com/muse-spark-app/muse-spark/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** solo deseas revisar su procedencia y código antes de evaluar el proyecto — **Evita si:** no quieres mantener modelos o un entorno de ejecución propio<br>
**Más:** [ficha completa](human/fichas/muse-spark.md) · [GitHub](https://github.com/muse-spark-app/muse-spark)

### NotebookLM: alternativas y clientes

#### 📓 SurfSense ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 16.9k<br>
**Qué es:** Conecta tus fuentes (archivos, Slack, Notion, GitHub, web) y conversa con ellas con citas, genera podcasts y reportes. Puede funcionar sin conexión.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/MODSetter/SurfSense/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un NotebookLM propio y con más fuentes — **Evita si:** solo quieres el NotebookLM de Google por código; mira `notebooklm-py`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/surfsense.md) · [GitHub](https://github.com/MODSetter/SurfSense)

#### 📓 open-notebook
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 42k<br>
**Qué es:** Resuelve el envío de documentos sensibles a la nube que implica el NotebookLM oficial.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/lfnovo/open-notebook/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres NotebookLM privado y sin cuotas — **Evita si:** prefieres el NotebookLM real automatizado (notebooklm-py)<br>
**Combina con:** [odysseus](human/fichas/odysseus.md) · [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/open-notebook.md) · [GitHub](https://github.com/lfnovo/open-notebook)

#### 🎙️ notebooklm-py
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 20.2k<br>
**Qué es:** Cubre el vacío de automatización que la interfaz web oficial no ofrece.<br>
**Acceso:** Sin API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/teng-lin/notebooklm-py/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** automatizas el NotebookLM real y aceptas el riesgo de API no oficial — **Evita si:** quieres todo local (open-notebook)<br>
**Combina con:** [notebooklm-mcp-cli](human/fichas/notebooklm-mcp-cli.md)<br>
**Más:** [ficha completa](human/fichas/notebooklm-py.md) · [GitHub](https://github.com/teng-lin/notebooklm-py)

#### 🎚️ notebooklm-mcp-cli
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 6.5k<br>
**Qué es:** Convierte NotebookLM en una herramienta invocable por asistentes.<br>
**Acceso:** Sin API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** integras NotebookLM con tu asistente MCP — **Evita si:** prefieres la API directa en scripts (notebooklm-py)<br>
**Combina con:** [notebooklm-py](human/fichas/notebooklm-py.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/notebooklm-mcp-cli.md) · [GitHub](https://github.com/jacob-bd/gemini-notebook-mcp-cli)

---

## 🎨 9. Diseñar y construir interfaces

Componentes, estilos, animación, diseño visual y herramientas para crear pantallas. Las librerías de UI no necesitan por sí solas una API de IA.

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
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 128k<br>
**Qué es:** El código fuente pasa a ser tuyo y lo editas a voluntad.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/shadcn-ui/ui/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres ser dueño del código de UI — **Evita si:** prefieres una lib "llave en mano" con updates automáticos (heroui)<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [plasmic](human/fichas/plasmic.md)<br>
**Más:** [ficha completa](human/fichas/ui.md) · [GitHub](https://github.com/shadcn-ui/ui)

#### 🧱 Ant Design
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 100k<br>
**Qué es:** Componentes muy completos para apps de negocio: tablas, formularios, fechas y layouts de backoffice.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install antd` (comprobar los pasos completos en la ficha).<br>
**Elige si:** construyes apps empresariales con muchos datos — **Evita si:** quieres un estilo más personalizado; mira `ui`<br>
**Combina con:** [echarts](human/fichas/echarts.md)<br>
**Más:** [ficha completa](human/fichas/ant-design.md) · [GitHub](https://github.com/ant-design/ant-design)

#### 🧱 Material UI
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 99.3k<br>
**Qué es:** Cientos de componentes accesibles y personalizables para apps React, con temas y sistema de estilos propio.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mui/material-ui/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una librería React completa y probada — **Evita si:** prefieres copiar componentes y estilarlos con Tailwind; mira `ui`<br>
**Combina con:** [Recharts](human/fichas/recharts.md)<br>
**Más:** [ficha completa](human/fichas/mui.md) · [GitHub](https://github.com/mui/material-ui)

#### 🧱 React Bits
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 52k<br>
**Qué es:** Fondos, textos animados y efectos listos para copiar en proyectos React y Next.js.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/DavidHDev/react-bits/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres efectos visuales llamativos en React — **Evita si:** necesitas componentes de formulario y datos; mira `ui`<br>
**Combina con:** [ui](human/fichas/ui.md) · [motion](human/fichas/motion.md)<br>
**Más:** [ficha completa](human/fichas/react-bits.md) · [GitHub](https://github.com/DavidHDev/react-bits)

#### 🔄 swr
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 32.5k<br>
**Qué es:** Cubre el caso de consumir APIs en frontend sin manejar caché a mano.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/vercel/swr/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** manejas datos remotos en React y quieres caché simple — **Evita si:** prefieres React Query con su modelo de caché global más rico<br>
**Combina con:** [heroui](human/fichas/heroui.md)<br>
**Más:** [ficha completa](human/fichas/swr.md) · [GitHub](https://github.com/vercel/swr)

#### 🦸 heroui
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 31.2k<br>
**Qué es:** Resuelve la accesibilidad seria sin renunciar a un estilado moderno.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install @heroui/styles @heroui/react` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres calidad + accesibilidad listas — **Evita si:** quieres control copy-paste del código (ui)<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [swr](human/fichas/swr.md)<br>
**Más:** [ficha completa](human/fichas/heroui.md) · [GitHub](https://github.com/heroui-inc/heroui)

#### 🧱 Lucide
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 25.8k<br>
**Qué es:** Iconos limpios y uniformes, usados por shadcn/ui y muchas apps.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/lucide-icons/lucide/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas iconos consistentes — **Evita si:** buscas ilustraciones, no iconos<br>
**Combina con:** [ui](human/fichas/ui.md)<br>
**Más:** [ficha completa](human/fichas/lucide.md) · [GitHub](https://github.com/lucide-icons/lucide)

#### ✨ magicui
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.3k<br>
**Qué es:** Apunta al impacto visual más que a la accesibilidad estricta.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/magicuidesign/magicui/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** priorizas estética y velocidad — **Evita si:** necesitas accesibilidad estricta (heroui)<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [motion](human/fichas/motion.md)<br>
**Más:** [ficha completa](human/fichas/magicui.md) · [GitHub](https://github.com/magicuidesign/magicui)

#### 🧱 Radix Primitives
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 19.5k<br>
**Qué es:** Resuelven accesibilidad, foco y teclado en diálogos, menús o tooltips, dejándote el estilo. Son la base de shadcn/ui.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/radix-ui/primitives/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** construyes tu propio sistema de diseño — **Evita si:** quieres componentes ya estilados; mira `ui`<br>
**Combina con:** [ui](human/fichas/ui.md) · [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/radix-primitives.md) · [GitHub](https://github.com/radix-ui/primitives)

### CSS y estilos

#### 🎨 daisyUI ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 42.8k<br>
**Qué es:** Añade clases como `btn` o `card` sobre Tailwind para escribir menos HTML, sin JavaScript.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/saadeghi/daisyui/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Tailwind y quieres componentes sin JavaScript — **Evita si:** usas React y quieres control total; mira `ui`<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/daisyui.md) · [GitHub](https://github.com/saadeghi/daisyui)

#### 🌬️ tailwindcss
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 98.6k<br>
**Qué es:** Elimina el contexto de estilos disperso entre hojas y componentes.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/tailwindlabs/tailwindcss/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estilar rápido y consistente — **Evita si:** prefieres CSS-in-JS o estilos scoped por componente<br>
**Combina con:** [heroui](human/fichas/heroui.md) · [magicui](human/fichas/magicui.md)<br>
**Más:** [ficha completa](human/fichas/tailwindcss.md) · [GitHub](https://github.com/tailwindlabs/tailwindcss)

#### 🧯 normalize.css
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 53.5k<br>
**Qué es:** Resuelve las inconsistencias de margen, tipografía y formularios entre Chrome, Firefox y Safari.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install --save normalize.css` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres base CSS uniforme y ligera — **Evita si:** ya usas el preflight de Tailwind, que cubre lo mismo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/normalize-css.md) · [GitHub](https://github.com/necolas/normalize.css)

### Animación y 3D

#### 🔺 three.js ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 118k<br>
**Qué es:** Abstrae la complejidad de WebGL en escenas, cámaras, luces y mallas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mrdoob/three.js/blob/dev/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** renderizas 3D en web y quieres control a bajo nivel — **Evita si:** trabajas solo 2D o prefieres la ergonomía de React (react-three-fiber)<br>
**Combina con:** [react-three-fiber](human/fichas/react-three-fiber.md) · [GSAP](human/fichas/gsap.md)<br>
**Más:** [ficha completa](human/fichas/three-js.md) · [GitHub](https://github.com/mrdoob/three.js)

#### ✨ Anime.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 74.7k<br>
**Qué es:** API simple y potente para líneas de tiempo, scroll y animaciones complejas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/juliangarnier/anime/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres animaciones potentes sin framework — **Evita si:** usas React y quieres animaciones declarativas; mira `motion`<br>
**Más:** [ficha completa](human/fichas/animejs.md) · [GitHub](https://github.com/juliangarnier/anime)

#### 🌀 motion
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 35.2k<br>
**Qué es:** Hizo accesible la animación en el ecosistema React.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install motion` (comprobar los pasos completos en la ficha).<br>
**Elige si:** animas componentes React con API declarativa — **Evita si:** necesitas timelines complejos no ligados a React (GSAP)<br>
**Combina con:** [magicui](human/fichas/magicui.md) · [react-three-fiber](human/fichas/react-three-fiber.md)<br>
**Más:** [ficha completa](human/fichas/motion.md) · [GitHub](https://github.com/motiondivision/motion)

#### 🔻 react-three-fiber
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 33.7k<br>
**Qué es:** Lleva la mentalidad componible de React al 3D sin abandonar three.js por debajo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/pmndrs/react-three-fiber/blob/master/readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** haces 3D en React y quieres reactividad — **Evita si:** no usas React o necesitas control a bajo nivel (three.js directo)<br>
**Combina con:** [motion](human/fichas/motion.md)<br>
**Más:** [ficha completa](human/fichas/react-three-fiber.md) · [GitHub](https://github.com/pmndrs/react-three-fiber)

#### 🎞️ GSAP
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 30.6k<br>
**Qué es:** Es la herramienta de referencia del motion web profesional.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install gsap` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas animación avanzada y control fino de timelines — **Evita si:** te basta animar componentes React con API declarativa (motion)<br>
**Combina con:** [motion](human/fichas/motion.md)<br>
**Más:** [ficha completa](human/fichas/gsap.md) · [GitHub](https://github.com/greensock/GSAP)

### Diseño visual, canvas y builders

#### ✏️ Excalidraw ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 136k<br>
**Qué es:** Dibuja diagramas rápidos que parecen bocetos, colabora en tiempo real y embébela en tus apps como componente React.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/excalidraw/excalidraw/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres diagramas rápidos con estilo boceto — **Evita si:** prefieres diagramas como texto; mira `mermaid`<br>
**Más:** [ficha completa](human/fichas/excalidraw.md) · [GitHub](https://github.com/excalidraw/excalidraw)

#### 🎨 open-design
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 108k<br>
**Qué es:** Resuelve el ir y venir entre prompt, preview y código exportable.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/nexu-io/open-design/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** generas UI desde texto y quieres edición visual — **Evita si:** prefieres editar visualmente sobre tu código existente (plasmic)<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [heroui](human/fichas/heroui.md)<br>
**Más:** [ficha completa](human/fichas/open-design.md) · [GitHub](https://github.com/nexu-io/open-design)

#### ✏️ penpot
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 62.4k<br>
**Qué es:** Es la alternativa abierta a Figma más conocida.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/penpot/penpot/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres diseño abierto y soberano, self-host — **Evita si:** necesitas generación por IA (open-design) o no quieres operar Docker<br>
**Combina con:** [plasmic](human/fichas/plasmic.md)<br>
**Más:** [ficha completa](human/fichas/penpot.md) · [GitHub](https://github.com/penpot/penpot)

#### ✏️ tldraw
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 51.4k<br>
**Qué es:** Base de muchas herramientas de pizarra y de UI generativa con IA. Ofrece colaboración y personalización completa.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm i tldraw` (comprobar los pasos completos en la ficha).<br>
**Elige si:** construyes una app con lienzo infinito — **Evita si:** solo necesitas una pizarra lista; usa `excalidraw`<br>
**Más:** [ficha completa](human/fichas/tldraw.md) · [GitHub](https://github.com/tldraw/tldraw)

#### ✏️ Onlook
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 27.2k<br>
**Qué es:** Edita tu app en un lienzo visual o pide cambios a la IA, y Onlook escribe el código en tu proyecto.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/onlook-dev/onlook/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres editar tu app React visualmente con ayuda de IA — **Evita si:** necesitas diseño desde cero en vectores; mira `penpot`<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [ui](human/fichas/ui.md)<br>
**Más:** [ficha completa](human/fichas/onlook.md) · [GitHub](https://github.com/onlook-dev/onlook)

#### 🧱 plasmic
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 7.2k<br>
**Qué es:** Cubre el hueco entre no-code y desarrollo a medida.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/plasmicapp/plasmic/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres editar visual sobre tu código React — **Evita si:** generas desde texto sin codebase previo (open-design)<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/plasmic.md) · [GitHub](https://github.com/plasmicapp/plasmic)

### UI generada con IA y frontends para agentes

#### 🪄 CopilotKit ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 38.7k<br>
**Qué es:** Añade copilotos, chat y agentes que actúan sobre tu app, con estado compartido entre agente y UI. Se integra con LangGraph, Mastra y más.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/CopilotKit/CopilotKit/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres agentes que interactúen con la UI de tu app — **Evita si:** solo necesitas una ventana de chat; mira `assistant-ui`<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [Mastra](human/fichas/mastra.md)<br>
**Más:** [ficha completa](human/fichas/copilotkit.md) · [GitHub](https://github.com/CopilotKit/CopilotKit)

#### 🪄 screenshot-to-code
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 81.2k<br>
**Qué es:** Sube una imagen o graba un video de una web y obtén código funcional que puedes iterar.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/abi/screenshot-to-code/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres pasar imágenes de diseño a código — **Evita si:** trabajas desde Figma; mira `figma-context-mcp`<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/screenshot-to-code.md) · [GitHub](https://github.com/abi/screenshot-to-code)

#### 🪄 OpenUI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 15.2k<br>
**Qué es:** Permite que el modelo devuelva componentes interactivos (tablas, formularios, gráficos) que tu app renderiza.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/thesysdev/openui/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres que tu agente responda con interfaces — **Evita si:** solo necesitas chat de texto; mira `assistant-ui`<br>
**Combina con:** [CopilotKit](human/fichas/copilotkit.md)<br>
**Más:** [ficha completa](human/fichas/openui.md) · [GitHub](https://github.com/thesysdev/openui)

#### 🪄 assistant-ui
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13.2k<br>
**Qué es:** Componentes componibles de chat con streaming, adjuntos, markdown y herramientas, compatibles con AI SDK y LangGraph.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx assistant-ui@latest init` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas una UI de chat pulida en React — **Evita si:** quieres agentes que manipulen tu app; mira `copilotkit`<br>
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md) · [ui](human/fichas/ui.md)<br>
**Más:** [ficha completa](human/fichas/assistant-ui.md) · [GitHub](https://github.com/assistant-ui/assistant-ui)

#### 🪄 Stitch SDK
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.9k<br>
**Qué es:** Automatiza Stitch, el generador de interfaces de Google, para integrarlo en tus flujos y agentes.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `npm install @google/stitch-sdk` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres automatizar Stitch — **Evita si:** prefieres herramientas locales; mira `screenshot-to-code`<br>
**Combina con:** [Stitch Skills](human/fichas/stitch-skills.md)<br>
**Más:** [ficha completa](human/fichas/stitch-sdk.md) · [GitHub](https://github.com/google-labs-code/stitch-sdk)

### Skills de diseño para agentes

#### 🎯 Stitch Skills ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 8.9k<br>
**Qué es:** Skills en el estándar abierto Agent Skills que enseñan a Claude Code, Codex o Gemini CLI a diseñar con Stitch.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/google-labs-code/stitch-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Stitch con un agente de código — **Evita si:** no usas Stitch<br>
**Combina con:** [Stitch SDK](human/fichas/stitch-sdk.md) · [Gemini CLI](human/fichas/gemini-cli.md)<br>
**Más:** [ficha completa](human/fichas/stitch-skills.md) · [GitHub](https://github.com/google-labs-code/stitch-skills)

#### 🎨 ui-ux-pro-max-skill
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 150k<br>
**Qué es:** Resuelve el punto débil habitual del código asistido por IA: la jerarquía visual y el acabado.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** generas UI con IA y el resultado se ve genérico o despulido — **Evita si:** no trabajas frontend o ya tienes un sistema de diseño impuesto<br>
**Combina con:** [taste-skill](human/fichas/taste-skill.md) · [impeccable](human/fichas/impeccable.md) · [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/ui-ux-pro-max-skill.md) · [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

#### 🍷 taste-skill
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 116k<br>
**Qué es:** Ataca el acabado "de plantilla" que delata a las UIs generadas por IA.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres frontends con gusto y no te basta con UI funcional — **Evita si:** ya tienes un design system cerrado o no usas generadores de imagen<br>
**Combina con:** [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md) · [impeccable](human/fichas/impeccable.md)<br>
**Más:** [ficha completa](human/fichas/taste-skill.md) · [GitHub](https://github.com/Leonxlnx/taste-skill)

#### 💎 impeccable
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 110k<br>
**Qué es:** Ataca el patrón repetitivo de interfaces que "huelen" a IA.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx impeccable` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres frontends que no parezcan generados por IA — **Evita si:** no generas UI con agentes<br>
**Combina con:** [taste-skill](human/fichas/taste-skill.md) · [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md)<br>
**Más:** [ficha completa](human/fichas/impeccable.md) · [GitHub](https://github.com/pbakaus/impeccable)

#### 🎨 Front-End-Checklist
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 74.7k<br>
**Qué es:** Checklist y recursos para revisar aspectos de calidad de un frontend antes de entregarlo. Organiza comprobaciones de implementación y publica material para revisión humana y agentes.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/thedaviddias/Front-End-Checklist/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres una lista de revisión de interfaz y entrega web — **Evita si:** tu interfaz ya cubre el mismo propósito con una herramienta equivalente<br>
**Más:** [ficha completa](human/fichas/front-end-checklist.md) · [GitHub](https://github.com/thedaviddias/Front-End-Checklist)

#### ✏️ skills_emil
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 56.9k<br>
**Qué es:** Resuelve el handoff diseño↔código, no solo la estética final.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/emilkowalski/skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas diseño+dev en equipo y sufres el handoff — **Evita si:** buscas componentes listos o trabajas solo<br>
**Combina con:** [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md)<br>
**Más:** [ficha completa](human/fichas/skills-emil.md) · [GitHub](https://github.com/emilkowalski/skills)

#### 📐 design.md
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 28.9k<br>
**Qué es:** Resuelve la inconsistencia de marca cuando varias personas o agentes tocan la UI.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/google-labs-code/design.md/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres consistencia de marca con IA y usas agentes para UI — **Evita si:** no usas agentes para generar código de UI<br>
**Combina con:** [impeccable](human/fichas/impeccable.md)<br>
**Más:** [ficha completa](human/fichas/design-md.md) · [GitHub](https://github.com/google-labs-code/design.md)

---

## 📊 10. Analizar datos, crear dashboards y mapas

Herramientas para explorar datos, crear gráficos, medir productos y visualizar fuentes abiertas. El chat con datos sí puede añadir un modelo; un gráfico convencional no lo necesita.

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
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 40.2k<br>
**Qué es:** Mide visitas, campañas, eventos, conversiones e ingresos en un panel simple, cumpliendo GDPR.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/umami-software/umami/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres analítica web simple y privada — **Evita si:** necesitas analítica de producto avanzada; mira `posthog`<br>
**Más:** [ficha completa](human/fichas/umami.md) · [GitHub](https://github.com/umami-software/umami)

#### 📈 posthog
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 40.8k<br>
**Qué es:** Cubre todo el ciclo de medición de producto sin integrar varias herramientas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/PostHog/posthog/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres entender el uso real y el comportamiento de usuarios — **Evita si:** solo necesitas BI sobre una BD estática (metabase)<br>
**Combina con:** [metabase](human/fichas/metabase.md)<br>
**Más:** [ficha completa](human/fichas/posthog.md) · [GitHub](https://github.com/PostHog/posthog)

#### 📈 Plausible Analytics
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 29.8k<br>
**Qué es:** Un panel de una sola página con lo esencial: visitas, fuentes, páginas y objetivos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/plausible/analytics/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres analítica minimalista y privada — **Evita si:** necesitas embudos y eventos complejos; mira `posthog`<br>
**Más:** [ficha completa](human/fichas/plausible.md) · [GitHub](https://github.com/plausible/analytics)

#### 📈 Matomo
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 22k<br>
**Qué es:** Analítica web completa con embudos, mapas de calor y comercio electrónico, auto-hospedada.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/matomo-org/matomo/blob/6.x-dev/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas analítica completa como Google Analytics pero propia — **Evita si:** quieres algo simple; mira `umami`<br>
**Más:** [ficha completa](human/fichas/matomo.md) · [GitHub](https://github.com/matomo-org/matomo)

### BI, dashboards y chat con datos

#### 📊 Apache Superset ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 75.5k<br>
**Qué es:** Conecta tus bases SQL, crea gráficos y dashboards sin código o con SQL Lab, con control de acceso.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/apache/superset/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres BI empresarial abierto — **Evita si:** buscas algo muy fácil para no técnicos; mira `metabase`<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [WrenAI](human/fichas/wrenai.md)<br>
**Más:** [ficha completa](human/fichas/superset.md) · [GitHub](https://github.com/apache/superset)

#### 📊 WrenAI ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.2k<br>
**Qué es:** Define tu modelo de datos una vez y los usuarios (o agentes) preguntan en lenguaje natural para obtener SQL, gráficos y respuestas.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install wrenai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres text-to-SQL confiable para el negocio — **Evita si:** solo analizas un CSV; mira `pandas-ai`<br>
**Combina con:** [Apache Superset](human/fichas/superset.md) · [DuckDB](human/fichas/duckdb.md)<br>
**Más:** [ficha completa](human/fichas/wrenai.md) · [GitHub](https://github.com/Canner/WrenAI)

#### 📊 Grafana
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 77.9k<br>
**Qué es:** Crea dashboards y alertas sobre Prometheus, Loki, bases SQL y decenas de fuentes. Estándar en monitoreo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/grafana/grafana/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas monitoreo y alertas en tiempo real — **Evita si:** buscas BI de negocio; mira `superset` o `metabase`<br>
**Combina con:** [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/grafana.md) · [GitHub](https://github.com/grafana/grafana)

#### 📊 metabase
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 50.3k<br>
**Qué es:** Apunta a perfiles no técnicos que necesitan reporting propio.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/metabase/metabase/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres BI accesible para perfiles no técnicos — **Evita si:** necesitas analítica de eventos por usuario (posthog)<br>
**Combina con:** [posthog](human/fichas/posthog.md) · [echarts](human/fichas/echarts.md)<br>
**Más:** [ficha completa](human/fichas/metabase.md) · [GitHub](https://github.com/metabase/metabase)

#### 📊 Redash
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 28.9k<br>
**Qué es:** Pensada para analistas que escriben SQL y quieren compartir resultados rápido con el equipo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/getredash/redash/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu equipo trabaja con SQL y quiere compartir rápido — **Evita si:** necesitas BI con permisos finos; mira `superset`<br>
**Más:** [ficha completa](human/fichas/redash.md) · [GitHub](https://github.com/getredash/redash)

#### 📊 PandasAI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.9k<br>
**Qué es:** Haces preguntas en lenguaje natural y genera el código de análisis o gráficos. Útil para analistas y apps de datos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install pandasai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres preguntar a tus tablas en lenguaje natural — **Evita si:** necesitas text-to-SQL gobernado para la empresa; mira `wrenai`<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md)<br>
**Más:** [ficha completa](human/fichas/pandas-ai.md) · [GitHub](https://github.com/sinaptik-ai/pandas-ai)

### Librerías de gráficos

#### 📉 Recharts ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 27.7k<br>
**Qué es:** Construye gráficos con componentes de React. Muy usada en dashboards de apps React y en shadcn/ui.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/recharts/recharts/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tu app es React y quieres gráficos declarativos — **Evita si:** no usas React; mira `chart-js`<br>
**Combina con:** [ui](human/fichas/ui.md)<br>
**Más:** [ficha completa](human/fichas/recharts.md) · [GitHub](https://github.com/recharts/recharts)

#### 📉 D3.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 114k<br>
**Qué es:** Da control total sobre cada elemento visual. Base de muchas librerías de gráficos y del periodismo de datos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/d3/d3/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas visualizaciones totalmente personalizadas — **Evita si:** quieres gráficos estándar rápido; mira `chart-js` o `recharts`<br>
**Más:** [ficha completa](human/fichas/d3.md) · [GitHub](https://github.com/d3/d3)

#### 📉 Chart.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 67.8k<br>
**Qué es:** Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web. No utiliza un modelo de IA para generar los gráficos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/chartjs/Chart.js/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres gráficos simples sin aprender una librería compleja — **Evita si:** necesitas visualizaciones a medida; mira `d3`<br>
**Más:** [ficha completa](human/fichas/chart-js.md) · [GitHub](https://github.com/chartjs/Chart.js)

#### 📉 echarts
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 67.7k<br>
**Qué es:** Cubre casi cualquier tipo de chart en el navegador.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/apache/echarts/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas gráficos ricos y variados embebidos — **Evita si:** solo series temporales simples y priorizas peso (uPlot)<br>
**Combina con:** [metabase](human/fichas/metabase.md) · [heroui](human/fichas/heroui.md)<br>
**Más:** [ficha completa](human/fichas/echarts.md) · [GitHub](https://github.com/apache/echarts)

#### 📈 uPlot
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 10.6k<br>
**Qué es:** Apuesta por hacer una sola cosa (líneas/áreas temporales) mejor que ninguna.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/leeoniya/uPlot/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** priorizas velocidad y peso del bundle — **Evita si:** necesitas tipos de gráfico variados (echarts)<br>
**Combina con:** [swr](human/fichas/swr.md)<br>
**Más:** [ficha completa](human/fichas/uplot.md) · [GitHub](https://github.com/leeoniya/uPlot)

### Apps de datos en Python

#### 🧪 Gradio ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 44.1k<br>
**Qué es:** Envuelve una función Python en una interfaz web con entradas y salidas de texto, imagen, audio o chat. Base de Hugging Face Spaces.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install --upgrade gradio` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres una demo web de tu modelo rápido — **Evita si:** construyes una app de datos con varias páginas; mira `streamlit`<br>
**Combina con:** [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/gradio.md) · [GitHub](https://github.com/gradio-app/gradio)

#### 📊 streamlit
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 46.4k<br>
**Qué es:** Convierte un script de datos en una app web interactiva casi al instante.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install streamlit` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres una UI de datos al vuelo y prototipos rápidos — **Evita si:** necesitas una app productiva con control fino del frontend (dash)<br>
**Combina con:** [dash](human/fichas/dash.md) · [data-science-ipython-notebooks](human/fichas/data-science-ipython-notebooks.md)<br>
**Más:** [ficha completa](human/fichas/streamlit.md) · [GitHub](https://github.com/streamlit/streamlit)

#### 🧮 dash
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 24.5k<br>
**Qué es:** Cubre el caso de dashboards productivos en Python sin salir del lenguaje.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/plotly/dash/blob/dev/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres dashboards productivos en Python con control del frontend — **Evita si:** prefieres prototipos ultrarrápidos (streamlit)<br>
**Combina con:** [streamlit](human/fichas/streamlit.md) · [echarts](human/fichas/echarts.md)<br>
**Más:** [ficha completa](human/fichas/dash.md) · [GitHub](https://github.com/plotly/dash)

### Recursos y casos de uso

#### 🗂️ awesome-dataviz
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 4.5k<br>
**Qué es:** Punto de partida para descubrir opciones de dataviz sin búsquedas dispersas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/hal9ai/awesome-dataviz/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas opciones de visualización y aún no has elegido — **Evita si:** ya elegiste tu librería y solo necesitas usarla<br>
**Combina con:** [echarts](human/fichas/echarts.md) · [awesome-bigdata](human/fichas/awesome-bigdata.md)<br>
**Más:** [ficha completa](human/fichas/awesome-dataviz.md) · [GitHub](https://github.com/hal9ai/awesome-dataviz)

#### 📊 data-analyst-roadmap
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 1.1k<br>
**Qué es:** Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y orientación de carrera. Organiza conocimientos y recursos desde bases de datos y programación hasta visualización y comunicación.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mtahiraslan/data-analyst-roadmap/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres ordenar un plan de aprendizaje para análisis de datos — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/data-analyst-roadmap.md) · [GitHub](https://github.com/mtahiraslan/data-analyst-roadmap)

#### 📊 DataAnalystPortfolioProjects
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 912<br>
**Qué es:** Portafolio de ejemplos de análisis de datos con SQL, Python, Tableau, Excel y Hive. Presenta ejercicios de limpieza, exploración y construcción de dashboards sobre conjuntos de datos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/PriyankaJhaTheDeveloper/DataAnalystPortfolioProjects/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres consultar ejemplos para construir tu propio portafolio de análisis — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/dataanalystportfolioprojects.md) · [GitHub](https://github.com/PriyankaJhaTheDeveloper/DataAnalystPortfolioProjects)

### Inteligencia de fuentes abiertas y mapas

#### 📊 osiris
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 11.7k<br>
**Qué es:** Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. Agrega feeds y los representa en una interfaz geográfica con distintas capas de información.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/simplifaisoul/osiris/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres visualizar varias fuentes de actualidad en un mapa — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/osiris.md) · [GitHub](https://github.com/simplifaisoul/osiris)

#### 📊 Pythia
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 1.2k<br>
**Qué es:** Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción. Combina un panel de eventos con MiroFish y modelos locales para consultar información agregada.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/jangles-byte/Pythia/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres explorar fuentes OSINT y escenarios desde un panel local — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/pythia.md) · [GitHub](https://github.com/jangles-byte/Pythia)

---

## 🖼️ 11. Generar imágenes y trabajar con visión

Generación, restauración, detección, segmentación y etiquetado de imágenes. Revisa por separado la licencia de los pesos y el hardware del modelo.

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
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 165k<br>
**Qué es:** Es la UI que popularizó la difusión local.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres extensiones y comunidad amplia — **Evita si:** prefieres un flujo moderno y limpio (InvokeAI)<br>
**Combina con:** [sd-webui-controlnet](human/fichas/sd-webui-controlnet.md)<br>
**Más:** [ficha completa](human/fichas/stable-diffusion-webui.md) · [GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

#### 🧠 ComfyUI
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 147k<br>
**Qué es:** Resuelve la composición de flujos de difusión complejos que una UI fija no permite.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres control total y pipelines reproducibles — **Evita si:** buscas simplicidad inmediata (Fooocus)<br>
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/comfyui.md) · [GitHub](https://github.com/Comfy-Org/ComfyUI)

#### 🎨 Fooocus
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 53.9k<br>
**Qué es:** Es la opción más sencilla para empezar con difusión local.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/lllyasviel/Fooocus/blob/main/readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres resultados ya, sin curva — **Evita si:** necesitas control fino del pipeline (ComfyUI)<br>
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/fooocus.md) · [GitHub](https://github.com/lllyasviel/Fooocus)

#### 🖌️ InvokeAI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 29.1k<br>
**Qué es:** Resuelve la fragmentación de herramientas SD reuniendo generación, edición y control en una sola app self-hosted.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/invoke-ai/InvokeAI/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas creatividad profesional y quieres una app estable con canvas — **Evita si:** solo haces una prueba puntual (Fooocus) o prefieres grafos nodales (ComfyUI)<br>
**Combina con:** [diffusers](human/fichas/diffusers.md) · [ControlNet](human/fichas/controlnet.md)<br>
**Más:** [ficha completa](human/fichas/invokeai.md) · [GitHub](https://github.com/invoke-ai/InvokeAI)

#### 🖼️ Stable Diffusion WebUI Forge
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 13.1k<br>
**Qué es:** Mantiene la interfaz de AUTOMATIC1111 con mejoras de rendimiento y soporte de modelos nuevos como FLUX.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres la WebUI clásica pero más rápida — **Evita si:** prefieres flujos por nodos; mira `comfyui`<br>
**Combina con:** [ControlNet](human/fichas/controlnet.md)<br>
**Más:** [ficha completa](human/fichas/sd-webui-forge.md) · [GitHub](https://github.com/lllyasviel/stable-diffusion-webui-forge)

#### 🖼️ Krita AI Diffusion
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 10.9k<br>
**Qué es:** Pinta, selecciona y genera dentro de tu editor de imágenes favorito; usa ComfyUI por debajo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Acly/krita-ai-diffusion/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** ilustras en Krita y quieres IA integrada — **Evita si:** quieres automatizar generación en lote; mira `comfyui`<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/krita-ai-diffusion.md) · [GitHub](https://github.com/Acly/krita-ai-diffusion)

### Modelos, librerías y control

#### 🌀 FLUX ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 26.1k<br>
**Qué es:** Modelos de texto a imagen de alta calidad, con variantes para edición, relleno y control.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/black-forest-labs/flux/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres generar imágenes de alta calidad con modelos abiertos — **Evita si:** no tienes GPU potente; usa una API en la nube<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md)<br>
**Más:** [ficha completa](human/fichas/flux.md) · [GitHub](https://github.com/black-forest-labs/flux)

#### 🤗 diffusers
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 34.9k<br>
**Qué es:** Es la capa de abstracción que unifica el zoo de modelos de difusión bajo una misma interfaz Python.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/huggingface/diffusers/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** programas generación y quieres control total por código — **Evita si:** quieres una UI lista (Fooocus) o grafos nodales (ComfyUI)<br>
**Combina con:** [ControlNet](human/fichas/controlnet.md) · [cosmos](human/fichas/cosmos.md)<br>
**Más:** [ficha completa](human/fichas/diffusers.md) · [GitHub](https://github.com/huggingface/diffusers)

#### 🧭 ControlNet
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 34.2k<br>
**Qué es:** Resuelve el problema de que el texto por sí solo no controla la composición de la imagen.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/lllyasviel/ControlNet/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas control estructural fino de la composición — **Evita si:** ya trabajas en SD WebUI (sd-webui-controlnet) o ComfyUI (tienen integración propia) y no necesitas el repo original<br>
**Combina con:** [diffusers](human/fichas/diffusers.md) · [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/controlnet.md) · [GitHub](https://github.com/lllyasviel/ControlNet)

#### 🧩 sd-webui-controlnet
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 17.8k<br>
**Qué es:** Lleva el control composicional al flujo de trabajo habitual de la WebUI sin tocar código.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Mikubill/sd-webui-controlnet/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** ya usas SD WebUI y quieres ControlNet sin cambiar de entorno — **Evita si:** trabajas en ComfyUI (usa sus propios nodos) o por código (diffusers)<br>
**Combina con:** [stable-diffusion-webui](human/fichas/stable-diffusion-webui.md) · [ControlNet](human/fichas/controlnet.md)<br>
**Más:** [ficha completa](human/fichas/sd-webui-controlnet.md) · [GitHub](https://github.com/Mikubill/sd-webui-controlnet)

#### 🪞 ComfyUI_IPAdapter_plus
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 6.2k<br>
**Qué es:** Funciona como un "LoRA de una sola imagen": le das un referente y la salida hereda su look.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/cubiq/ComfyUI_IPAdapter_plus/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** trabajas en ComfyUI y necesitas consistencia visual por referencia — **Evita si:** no usas ComfyUI o te basta con prompts de estilo<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/comfyui-ipadapter-plus.md) · [GitHub](https://github.com/cubiq/ComfyUI_IPAdapter_plus)

### Restauración, upscaling y edición

#### 🩹 rembg ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 25.5k<br>
**Qué es:** Elimina fondos de fotos de producto o retratos con modelos como U2Net o BiRefNet.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/danielgatis/rembg/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas quitar fondos en local — **Evita si:** necesitas segmentar objetos específicos; mira `sam2`<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/rembg.md) · [GitHub](https://github.com/danielgatis/rembg)

#### 🙂 GFPGAN
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 37.7k<br>
**Qué es:** Resuelve el problema concreto de las caras "fundidas" que aparecen al reescalar o comprimir fotos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/TencentARC/GFPGAN/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** restauras rostros borrosos o fundidos — **Evita si:** necesitas upscaling general de la imagen (Real-ESRGAN)<br>
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/gfpgan.md) · [GitHub](https://github.com/TencentARC/GFPGAN)

#### 🔍 Real-ESRGAN
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 37.5k<br>
**Qué es:** A diferencia de los upscalers bicúbicos, infiere detalle plausible al ampliar.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/xinntao/Real-ESRGAN/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** reescalas imágenes o video a más resolución — **Evita si:** solo necesitas arreglar rostros (GFPGAN) o buscas difusión para reimaginar<br>
**Combina con:** [GFPGAN](human/fichas/gfpgan.md)<br>
**Más:** [ficha completa](human/fichas/real-esrgan.md) · [GitHub](https://github.com/xinntao/Real-ESRGAN)

#### 🩹 CodeFormer
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 18.2k<br>
**Qué es:** Recupera detalles de caras en fotos de baja calidad con buena fidelidad.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/sczhou/CodeFormer/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres restaurar rostros — **Evita si:** quieres escalar la imagen completa; mira `real-esrgan`<br>
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/codeformer.md) · [GitHub](https://github.com/sczhou/CodeFormer)

### Rostros y retratos animados

#### 🎭 Deep-Live-Cam ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 98.1k<br>
**Qué es:** Convierte un cambio de rostro, que normalmente requiere pipeline complejo, en un flujo de "un clic".<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas swap en vivo legítimo con consentimiento — **Evita si:** no puedes garantizar uso ético/consentimiento o no tienes GPU<br>
**Combina con:** [face_recognition](human/fichas/face-recognition.md)<br>
**Más:** [ficha completa](human/fichas/deep-live-cam.md) · [GitHub](https://github.com/hacksider/Deep-Live-Cam)

#### 👤 face_recognition
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 56.9k<br>
**Qué es:** Envuelve dlib para que el reconocimiento facial sea trivial desde un script.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ageitgey/face_recognition/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas reconocimiento facial básico y rápido de implementar — **Evita si:** buscas restauración/animación (GFPGAN/LivePortrait) o precisión de producción (mejor DeepFace/InsightFace)<br>
**Combina con:** [Deep-Live-Cam](human/fichas/deep-live-cam.md)<br>
**Más:** [ficha completa](human/fichas/face-recognition.md) · [GitHub](https://github.com/ageitgey/face_recognition)

#### 🙂 FaceFusion
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 30.7k<br>
**Qué es:** Herramienta líder para face swap, mejora facial y sincronía labial, con controles de uso responsable.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/facefusion/facefusion/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas manipulación facial de calidad con consentimiento — **Evita si:** no tienes consentimiento de las personas<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/facefusion.md) · [GitHub](https://github.com/facefusion/facefusion)

#### 🙂 InsightFace
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 30.2k<br>
**Qué es:** Base de muchas herramientas faciales; ofrece modelos de reconocimiento de última generación.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/deepinsight/insightface/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas reconocimiento facial preciso — **Evita si:** solo quieres detectar caras simples; mira `opencv`<br>
**Combina con:** [FaceFusion](human/fichas/facefusion.md)<br>
**Más:** [ficha completa](human/fichas/insightface.md) · [GitHub](https://github.com/deepinsight/insightface)

#### 🧑 LivePortrait
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 19.5k<br>
**Qué es:** Convierte una foto en un avatar que sigue las expresiones de un "conductor".<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** animas retratos a partir de una foto — **Evita si:** necesitas swap en vivo (Deep-Live-Cam) o no tienes GPU<br>
**Combina con:** [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/liveportrait.md) · [GitHub](https://github.com/KlingAIResearch/LivePortrait)

### Visión por computador

#### 👁️ Ultralytics YOLO ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 63.4k<br>
**Qué es:** Entrena un detector con tus datos en pocas líneas y expórtalo a ONNX, TensorRT o móvil.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install ultralytics` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas detección de objetos práctica — **Evita si:** necesitas licencia permisiva para producto cerrado; revisa su licencia<br>
**Combina con:** [supervision](human/fichas/supervision.md) · [Label Studio](human/fichas/label-studio.md)<br>
**Más:** [ficha completa](human/fichas/ultralytics.md) · [GitHub](https://github.com/ultralytics/ultralytics)

#### 👁️ SAM 2 ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 20.1k<br>
**Qué es:** Marca un objeto en un fotograma y SAM 2 lo sigue en todo el video. Más rápido que SAM en imágenes.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/facebookresearch/sam2/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas segmentar objetos en video — **Evita si:** solo trabajas con imágenes sueltas; `segment-anything` basta<br>
**Combina con:** [Label Studio](human/fichas/label-studio.md) · [supervision](human/fichas/supervision.md)<br>
**Más:** [ficha completa](human/fichas/sam2.md) · [GitHub](https://github.com/facebookresearch/sam2)

#### 👁️ OpenCV
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 91.6k<br>
**Qué es:** Procesamiento de imagen y video, detección, calibración de cámaras y más, en C++ y Python.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/opencv/opencv/blob/5.x/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas procesamiento de imagen o video — **Evita si:** necesitas detección de objetos moderna; mira `ultralytics`<br>
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [supervision](human/fichas/supervision.md)<br>
**Más:** [ficha completa](human/fichas/opencv.md) · [GitHub](https://github.com/opencv/opencv)

#### 👁️ Segment Anything (SAM)
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 55.1k<br>
**Qué es:** Genera máscaras precisas sin entrenamiento para el objeto que indiques. Su sucesor SAM 2 añade video.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/facebookresearch/segment-anything/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas segmentar objetos en imágenes — **Evita si:** trabajas con video; mira `sam2`<br>
**Combina con:** [Label Studio](human/fichas/label-studio.md)<br>
**Más:** [ficha completa](human/fichas/segment-anything.md) · [GitHub](https://github.com/facebookresearch/segment-anything)

#### 👁️ supervision
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 51.6k<br>
**Qué es:** Se conecta a cualquier detector y te da utilidades para dibujar, contar en zonas, seguir objetos y evaluar.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install supervision` (comprobar los pasos completos en la ficha).<br>
**Elige si:** construyes un proyecto de visión con detectores — **Evita si:** solo necesitas procesar imágenes; mira `opencv`<br>
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [OpenCV](human/fichas/opencv.md)<br>
**Más:** [ficha completa](human/fichas/supervision.md) · [GitHub](https://github.com/roboflow/supervision)

#### 👁️ Label Studio
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 28.7k<br>
**Qué es:** Crea datasets para entrenar o evaluar modelos con interfaces de anotación configurables y preetiquetado con IA.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install label-studio` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas crear datasets etiquetados — **Evita si:** solo evalúas prompts; mira `promptfoo`<br>
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [SAM 2](human/fichas/sam2.md)<br>
**Más:** [ficha completa](human/fichas/label-studio.md) · [GitHub](https://github.com/HumanSignal/label-studio)

### Suites generativas todo-en-uno

#### 🎬 Open-Generative-AI ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 34.7k<br>
**Qué es:** Estudio abierto de generación de imagen y video que utiliza modelos ofrecidos mediante servicios de MuAPI. El código de la interfaz está disponible; las generaciones y otras modalidades del servicio tienen requisitos y tarifas propios.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un hub de generación multi-modal sin atarte a un SaaS — **Evita si:** ya tienes tu pipeline local (ComfyUI) o necesitas control fino por nodo<br>
**Combina con:** [remotion](human/fichas/remotion.md)<br>
**Más:** [ficha completa](human/fichas/open-generative-ai.md) · [GitHub](https://github.com/Anil-matcha/Open-Generative-AI)

### Sensores y percepción espacial

#### 🖼️ RuView
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 104k<br>
**Qué es:** Proyecto de detección espacial que experimenta con señales WiFi para estimar presencia y movimiento. Procesa señales de radio y conecta componentes de detección con paneles y sistemas de domótica.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/ruvnet/RuView/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres investigar percepción mediante radiofrecuencia y sensores WiFi — **Evita si:** no dispones de datos o hardware compatibles con el proyecto<br>
**Más:** [ficha completa](human/fichas/ruview.md) · [GitHub](https://github.com/ruvnet/RuView)

---

## 🎬 12. Crear audio, voz y video

Transcribe, sintetiza voz, edita o genera video. El montaje local y la generación mediante un proveedor son rutas con requisitos diferentes.

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

**⚖️ ¿Cuál elegir? — Manim (ManimGL), manim**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Manim (ManimGL)](human/fichas/manim.md) | quieres animaciones matemáticas o técnicas precisas definidas en código Python | buscas estabilidad y documentación para empezar (usa la edición comunitaria ManimCommunity/manim) o motion graphics de marketing; mira `remotion` o `hyperframes` |
| [manim](human/fichas/manim-community.md) | necesitas animaciones matemáticas precisas y reproducibles | tu flujo audiovisual actual ya cubre esa etapa |

**⚖️ ¿Cuál elegir? — MoneyPrinterTurbo, OpenMontage, video-use, videofy_minimal, Remotion Superpowers**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [MoneyPrinterTurbo](human/fichas/moneyprinterturbo.md) | quieres producir videos cortos narrados a partir de un tema sin editar a mano | necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage` |
| [OpenMontage](human/fichas/openmontage.md) | quieres producir videos completos con un agente | solo necesitas editar clips; mira `video-use` |
| [video-use](human/fichas/video-use.md) | quieres editar videos pidiéndoselo a tu agente | quieres una app de edición visual; mira `opencut` |
| [videofy_minimal](human/fichas/videofy-minimal.md) | quieres reels simples ya, sin montar un pipeline entero | necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy) |
| [Remotion Superpowers](human/fichas/remotion-superpowers.md) | usas Remotion con un agente y quieres producción completa | no usas Remotion |

**⚖️ ¿Cuál elegir? — Wan2.2, HunyuanVideo, LTX-Video**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Wan2.2](human/fichas/wan2-2.md) | quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más | tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados |
| [HunyuanVideo](human/fichas/hunyuanvideo.md) | tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente |
| [LTX-Video](human/fichas/ltx-video.md) | necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x | empiezas un proyecto nuevo; Lightricks recomienda LTX-2.5 (repo Lightricks/LTX-2), o mira `wan2-2` y `wan2gp` |

### Transcripción (voz a texto)

#### 🎙️ whisper.cpp ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 55.2k<br>
**Qué es:** Transcribe voz a texto en local sin Python ni GPU obligatoria, incluso en tiempo real. Base de muchas apps de dictado.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ggml-org/whisper.cpp/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres transcribir en local sin GPU — **Evita si:** necesitas marcas de tiempo por palabra y diarización; mira `whisperx`<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/whisper-cpp.md) · [GitHub](https://github.com/ggml-org/whisper.cpp)

#### 📝 whisper
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 113k<br>
**Qué es:** Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. El idioma, el tamaño del modelo y la calidad del audio condicionan el resultado.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install -U openai-whisper` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres la referencia robusta y no te obsesiona la latencia — **Evita si:** necesitas más velocidad (faster-whisper) o timings por palabra (whisperX)<br>
**Combina con:** [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/whisper.md) · [GitHub](https://github.com/openai/whisper)

#### ⚡ faster-whisper
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 26.8k<br>
**Qué es:** Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. Puede reducir requisitos frente a otras implementaciones; mide calidad y rendimiento con tu propio audio.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install faster-whisper` (comprobar los pasos completos en la ficha).<br>
**Elige si:** el rendimiento, la memoria o el coste de GPU importan — **Evita si:** necesitas alineación/diarización (whisperX) o te basta el CLI oficial<br>
**Combina con:** [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/faster-whisper.md) · [GitHub](https://github.com/SYSTRAN/faster-whisper)

#### 🎯 whisperX
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 25.3k<br>
**Qué es:** Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. Las etapas, modelos y credenciales requeridos cambian según las funciones que actives.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install whisperx` (comprobar los pasos completos en la ficha).<br>
**Elige si:** necesitas subtítulos precisos o diarización — **Evita si:** te basta texto plano (whisper) o no quieres gestionar tokens de HF<br>
**Combina con:** [whisper](human/fichas/whisper.md) · [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/whisperx.md) · [GitHub](https://github.com/m-bain/whisperX)

#### 🎙️ NVIDIA NeMo Speech
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 18.8k<br>
**Qué es:** Incluye modelos de ASR como Parakeet y Canary, que lideran rankings de transcripción, y herramientas para afinarlos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA-NeMo/Speech/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas ASR de máxima precisión y tienes GPU — **Evita si:** quieres algo simple; mira `faster-whisper`<br>
**Combina con:** [Pipecat](human/fichas/pipecat.md)<br>
**Más:** [ficha completa](human/fichas/nemo.md) · [GitHub](https://github.com/NVIDIA-NeMo/Speech)

### Síntesis y clonación de voz

#### 🗣️ Kokoro ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 10.1k<br>
**Qué es:** Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. Comprueba los idiomas, dependencias de audio y condiciones de la variante que utilices.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install kokoro` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres TTS ligero, rápido y con licencia permisiva — **Evita si:** necesitas clonar voces; mira `chatterbox`<br>
**Combina con:** [Pipecat](human/fichas/pipecat.md) · [whisper.cpp](human/fichas/whisper-cpp.md)<br>
**Más:** [ficha completa](human/fichas/kokoro.md) · [GitHub](https://github.com/hexgrad/kokoro)

#### 🎚️ OmniVoice-Studio
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 111k<br>
**Qué es:** Reúne STT, TTS y dubbing en una sola app sin claves de API.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/debpalash/VoiceStudio/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres suite de voz completa local (dictado + clonación + dubbing) — **Evita si:** solo necesitas TTS simple por CLI/librería (TTS) o estabilidad de producción<br>
**Combina con:** [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/omnivoice-studio.md) · [GitHub](https://github.com/debpalash/VoiceStudio)

#### 🗣️ GPT-SoVITS
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 65.1k<br>
**Qué es:** Entrena una voz con muy pocos datos y sintetiza en varios idiomas. Muy popular entre creadores.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres entrenar una voz con pocos datos — **Evita si:** prefieres zero-shot sin entrenar; mira `chatterbox`<br>
**Combina con:** [RVC WebUI](human/fichas/rvc.md)<br>
**Más:** [ficha completa](human/fichas/gpt-sovits.md) · [GitHub](https://github.com/RVC-Boss/GPT-SoVITS)

#### 🗣️ VibeVoice
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 57.2k<br>
**Qué es:** Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. Elige una variante concreta antes de asumir idiomas, duración, hardware o soporte de tiempo real.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/VibeVoice/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres generar podcasts o diálogos largos — **Evita si:** solo necesitas frases cortas; mira `kokoro`<br>
**Combina con:** [open-notebook](human/fichas/open-notebook.md)<br>
**Más:** [ficha completa](human/fichas/vibevoice.md) · [GitHub](https://github.com/microsoft/VibeVoice)

#### 🎙️ TTS
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 46.2k<br>
**Qué es:** Reúne en una sola librería modelos como Tacotron, VITS y XTTS, con CLI y API Python.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install TTS` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres flexibilidad y varios modelos en una librería — **Evita si:** necesitas tiempo real puro (supertonic) o soporte comercial (Coqui está inactivo)<br>
**Combina con:** [whisperX](human/fichas/whisperx.md) · [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/tts.md) · [GitHub](https://github.com/coqui-ai/TTS)

#### 🗣️ VoxCPM
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 42.5k<br>
**Qué es:** Pertenece a la familia CPM de modelos generativos de OpenBMB.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install voxcpm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres voz muy natural o clonada y tienes GPU — **Evita si:** priorizas latencia mínima (supertonic) o no tienes GPU<br>
**Combina con:** [TTS](human/fichas/tts.md)<br>
**Más:** [ficha completa](human/fichas/voxcpm.md) · [GitHub](https://github.com/OpenBMB/VoxCPM)

#### 🗣️ RVC WebUI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 39.3k<br>
**Qué es:** Cambia la voz de una grabación manteniendo entonación. Muy usado para covers y doblaje.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres convertir una voz grabada en otra — **Evita si:** necesitas generar voz desde texto; mira `chatterbox`<br>
**Combina con:** [GPT-SoVITS](human/fichas/gpt-sovits.md)<br>
**Más:** [ficha completa](human/fichas/rvc.md) · [GitHub](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

#### 🗣️ Fish Speech
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 33.7k<br>
**Qué es:** Clona voces con pocos segundos de audio y genera habla natural en muchos idiomas.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/fishaudio/fish-speech/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas TTS de alta calidad con clonación — **Evita si:** necesitas licencia comercial sin restricciones; mira `chatterbox`<br>
**Más:** [ficha completa](human/fichas/fish-speech.md) · [GitHub](https://github.com/fishaudio/fish-speech)

#### 🗣️ Chatterbox
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 27.8k<br>
**Qué es:** Clona una voz con unos segundos de audio y ajusta la expresividad. Multilingüe y con marca de agua.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install chatterbox-tts` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres clonar voces con calidad alta y licencia libre — **Evita si:** necesitas algo muy ligero en CPU; mira `kokoro`<br>
**Combina con:** [Pipecat](human/fichas/pipecat.md)<br>
**Más:** [ficha completa](human/fichas/chatterbox.md) · [GitHub](https://github.com/resemble-ai/chatterbox)

#### 🗣️ IndexTTS
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 25.1k<br>
**Qué es:** Clona voces sin entrenar y permite controlar la duración exacta, útil para doblaje.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/index-tts/index-tts/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas controlar duración y emoción de la voz — **Evita si:** buscas licencia totalmente libre; revisa su licencia<br>
**Más:** [ficha completa](human/fichas/index-tts.md) · [GitHub](https://github.com/index-tts/index-tts)

#### 🗣️ CosyVoice
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 24.4k<br>
**Qué es:** Síntesis de voz natural con clonación y control de estilo, también en streaming.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/QwenAudio/CosyVoice/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas TTS multilingüe en streaming — **Evita si:** quieres instalación muy simple; mira `kokoro`<br>
**Combina con:** [Pipecat](human/fichas/pipecat.md)<br>
**Más:** [ficha completa](human/fichas/cosyvoice.md) · [GitHub](https://github.com/QwenAudio/CosyVoice)

#### 🔊 supertonic
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 13.8k<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** Motor de texto a voz que ofrece modelos y ejemplos para sintetizar audio en dispositivos y navegadores compatibles. El soporte por idioma, dispositivo y variante debe comprobarse en la documentación actual.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install supertonic` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres voz local en tiempo real y sin nube — **Evita si:** priorizas clonación de máxima fidelidad (VoxCPM) o flexibilidad multi-modelo (TTS)<br>
**Combina con:** [whisperX](human/fichas/whisperx.md) · [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/supertonic.md) · [GitHub](https://github.com/supertone-oss-archive/supertonic)

#### 🎬 edge-tts
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 12.5k<br>
**Qué es:** Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. Envía texto al servicio de voz y guarda el audio y los subtítulos desde Python o la terminal.<br>
**Acceso:** Sin API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install edge-tts` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres generar narración sin instalar un modelo de voz local — **Evita si:** tu flujo audiovisual actual ya cubre esa etapa<br>
**Combina con:** [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/edge-tts.md) · [GitHub](https://github.com/rany2/edge-tts)

#### 🗣️ LuxTTS
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 5.6k<br>
**Qué es:** Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. La velocidad y el consumo de memoria dependen de la variante y del hardware.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ysharma3501/LuxTTS/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas TTS con clonación muy rápido — **Evita si:** buscas el proyecto más maduro; mira `chatterbox`<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [cosmos](human/fichas/cosmos.md) · [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/luxtts.md) · [GitHub](https://github.com/ysharma3501/LuxTTS)

### Agentes de voz en tiempo real

#### 📞 Pipecat ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 17.3k<br>
**Qué es:** Encadena STT, LLM y TTS con interrupciones y baja latencia, y conecta con teléfono, WebRTC o WhatsApp.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install pipecat-ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** construyes un agente de voz en Python — **Evita si:** quieres infraestructura WebRTC gestionada; mira `livekit-agents`<br>
**Combina con:** [Kokoro](human/fichas/kokoro.md) · [whisper.cpp](human/fichas/whisper-cpp.md)<br>
**Más:** [ficha completa](human/fichas/pipecat.md) · [GitHub](https://github.com/pipecat-ai/pipecat)

#### 📞 LiveKit Agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 15.2k<br>
**Qué es:** Construye agentes que hablan, escuchan y ven, con detección de turnos y telefonía, desplegables a escala.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/livekit/agents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas agentes de voz escalables con WebRTC — **Evita si:** quieres algo ligero sin servidor de medios; mira `pipecat`<br>
**Combina con:** [Kokoro](human/fichas/kokoro.md)<br>
**Más:** [ficha completa](human/fichas/livekit-agents.md) · [GitHub](https://github.com/livekit/agents)

### Edición, grabación y subtítulos

#### ✂️ FFmpeg ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 67.3k<br>
**Qué es:** FFmpeg es la base multimedia sobre la que se apoyan casi todos los editores, reproductores y pipelines de video. Incluye el CLI `ffmpeg` para convertir, recortar, concatenar, mezclar, quemar subtítulos y transmitir, `ffprobe` para inspeccionar archivos y las librerías libav* para integrarlo en tu propio software.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/FFmpeg/FFmpeg/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas convertir, cortar, mezclar o transmitir audio y video desde la línea de comandos o un script — **Evita si:** quieres una interfaz gráfica para cortar sin pérdida (`lossless-cut`) o componer video desde Python con objetos (`moviepy`)<br>
**Combina con:** [whisper](human/fichas/whisper.md) · [yt-dlp](human/fichas/yt-dlp.md) · [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/ffmpeg.md) · [GitHub](https://github.com/FFmpeg/FFmpeg)

#### 🎬 MoviePy ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 15.2k<br>
**Qué es:** MoviePy convierte la edición de video en código Python: abres clips, los recortas, superpones texto o imágenes, mezclas audio y exportas a MP4, WebM o GIF. Es la pieza de ensamblaje habitual en pipelines que generan videos cortos a partir de imágenes, voz sintética y subtítulos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install moviepy` (comprobar los pasos completos en la ficha).<br>
**Elige si:** ensamblas video desde Python y quieres controlar cada clip por código — **Evita si:** prefieres plantillas en React (`remotion`) o en HTML (`hyperframes`), o solo necesitas cortar sin recodificar (`lossless-cut`)<br>
**Combina con:** [whisperX](human/fichas/whisperx.md) · [Kokoro](human/fichas/kokoro.md) · [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/moviepy.md) · [GitHub](https://github.com/Zulko/moviepy)

#### 🎞️ OpenCut
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 98.4k<br>
**Qué es:** Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. El README diferencia opencut.app y opencut-classic de la reescritura en curso; comprueba qué versión necesitas antes de compilar.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/OpenCut-app/OpenCut/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut — **Evita si:** necesitas estabilidad o automatización hoy; para montar por código mira `moviepy` o `remotion`, y para cortes sin pérdida `lossless-cut`<br>
**Combina con:** [LosslessCut](human/fichas/lossless-cut.md) · [OBS Studio](human/fichas/obs-studio.md) · [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/opencut.md) · [GitHub](https://github.com/OpenCut-app/OpenCut)

#### ✂️ OBS Studio
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 79.6k<br>
**Qué es:** OBS Studio captura, compone, codifica, graba y transmite video en Windows, macOS y Linux. Combinas en escenas la pantalla, ventanas, webcam, navegador y archivos multimedia, mezclas el audio con filtros y emites a YouTube, Twitch u otro servicio RTMP, o grabas a disco.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/obsproject/obs-studio/blob/master/README.rst); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas — **Evita si:** lo que necesitas es montar o recortar el video ya grabado; usa `opencut` o `lossless-cut`<br>
**Combina con:** [LosslessCut](human/fichas/lossless-cut.md) · [OpenCut](human/fichas/opencut.md) · [faster-whisper](human/fichas/faster-whisper.md)<br>
**Más:** [ficha completa](human/fichas/obs-studio.md) · [GitHub](https://github.com/obsproject/obs-studio)

#### ✂️ LosslessCut
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 46k<br>
**Qué es:** LosslessCut es una interfaz gráfica sobre FFmpeg para recortar y fusionar archivos de video y audio sin recompresión. Sirve para descartar gigas de material de cámara, GoPro o dron, extraer o reemplazar pistas, cambiar de contenedor (MKV a MP4) y editar metadatos o capítulos, en Windows, macOS y Linux.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mifi/lossless-cut/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica — **Evita si:** necesitas efectos, transiciones o un montaje con capas; mira `opencut` o, por código, `moviepy`<br>
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md) · [whisperX](human/fichas/whisperx.md) · [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/lossless-cut.md) · [GitHub](https://github.com/mifi/lossless-cut)

#### 🖥️ OpenScreen
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 40k<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** OpenScreen graba una ventana o la pantalla completa con micrófono y audio del sistema, y después te deja pulir la demo: zooms que siguen al cursor, webcam superpuesta, fondos, anotaciones, recorte y velocidad por tramo. Exporta a MP4 o GIF en varias proporciones. El proyecto original está archivado; su continuación activa es getopenscreen/openscreen.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/siddharthvaddem/openscreen/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio — **Evita si:** necesitas un proyecto mantenido; usa su continuación getopenscreen/openscreen, o `obs-studio` para grabación y streaming generales<br>
**Combina con:** [LosslessCut](human/fichas/lossless-cut.md) · [OpenCut](human/fichas/opencut.md)<br>
**Más:** [ficha completa](human/fichas/openscreen.md) · [GitHub](https://github.com/siddharthvaddem/openscreen)

#### ✂️ VideoLingo
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 19.3k<br>
**Qué es:** VideoLingo reúne en una interfaz Streamlit el trabajo de un equipo de subtitulado: descarga el video con yt-dlp, lo transcribe con alineación por palabra, segmenta y traduce los subtítulos con un LLM y, si quieres, genera el doblaje con voz sintética o clonada. Produce archivos SRT y videos subtitulados o doblados.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Huanshere/VideoLingo/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar — **Evita si:** solo necesitas transcribir o subtitular en el idioma original; te basta `whisperx` o `faster-whisper`<br>
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md) · [GPT-SoVITS](human/fichas/gpt-sovits.md) · [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/videolingo.md) · [GitHub](https://github.com/Huanshere/VideoLingo)

#### 🎬 palmier-pro
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 14.8k<br>
**Qué es:** Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios actuales. Permite trabajar con una línea de tiempo y enlazar agentes mediante MCP en las versiones que lo incorporan.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/palmier-io/palmier-pro/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas macOS y quieres explorar edición de video asistida por agentes — **Evita si:** tu flujo audiovisual actual ya cubre esa etapa<br>
**Más:** [ficha completa](human/fichas/palmier-pro.md) · [GitHub](https://github.com/palmier-io/palmier-pro)

#### ✂️ DaVinci Resolve MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 4.1k<br>
**Qué es:** Expone la API oficial de scripting de DaVinci Resolve como herramientas MCP para Claude, Cursor, Codex y otros clientes. Cubre montaje, organización del media pool, render, marcadores, color, Fusion y Fairlight, y añade análisis de medios que nunca modifica los originales. Incluye un panel de control local en el navegador.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** editas en DaVinci Resolve y quieres que un agente MCP automatice montaje, render o metadatos — **Evita si:** no usas Resolve o prefieres montar video por código sin editor; mira `moviepy` o `ffmpeg`<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [FFmpeg](human/fichas/ffmpeg.md) · [whisper](human/fichas/whisper.md)<br>
**Más:** [ficha completa](human/fichas/davinci-resolve-mcp.md) · [GitHub](https://github.com/samuelgursky/davinci-resolve-mcp)

### Video programático y con agentes

#### 🎞️ HyperFrames ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 84.4k<br>
**Qué es:** HyperFrames define cada video como un archivo HTML con atributos de tiempo y pistas, animado con GSAP, CSS, Lottie, Three.js u otras librerías, y lo renderiza a MP4. Incluye CLI para crear, previsualizar y renderizar, un catálogo de unos 450 bloques (transiciones, subtítulos, gráficos, mapas) y skills para que Claude Code, Codex o Cursor produzcan videos a partir de una petición.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx hyperframes init my-video` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva — **Evita si:** tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [GSAP](human/fichas/gsap.md) · [Kokoro](human/fichas/kokoro.md) · [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/hyperframes.md) · [GitHub](https://github.com/heygen-com/hyperframes)

#### 🎞️ Remotion Agent Skills ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 7.1k<br>
**Qué es:** Enseñan al agente las buenas prácticas de Remotion: composiciones, animaciones, audio y render.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add remotion-dev/skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** haces videos con Remotion y un agente — **Evita si:** no usas Remotion<br>
**Combina con:** [remotion](human/fichas/remotion.md) · [Remotion Superpowers](human/fichas/remotion-superpowers.md)<br>
**Más:** [ficha completa](human/fichas/skills-remotion.md) · [GitHub](https://github.com/remotion-dev/skills)

#### 🎞️ Manim (ManimGL)
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 96.5k<br>
**Qué es:** Manim permite describir en código Python escenas con fórmulas LaTeX, gráficas, geometría y transformaciones animadas, y exportarlas a video. Este repo es ManimGL, la versión original que Grant Sanderson usa en 3Blue1Brown; la edición comunitaria (ManimCommunity/manim) es un fork más estable y mejor documentado.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install manimgl` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres animaciones matemáticas o técnicas precisas definidas en código Python — **Evita si:** buscas estabilidad y documentación para empezar (usa la edición comunitaria ManimCommunity/manim) o motion graphics de marketing; mira `remotion` o `hyperframes`<br>
**Combina con:** [Kokoro](human/fichas/kokoro.md) · [MoviePy](human/fichas/moviepy.md) · [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/manim.md) · [GitHub](https://github.com/3b1b/manim)

#### 🎞️ OpenMontage
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 80.5k<br>
**Qué es:** Describes el video y el agente investiga, escribe el guion, genera recursos y monta el resultado.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres producir videos completos con un agente — **Evita si:** solo necesitas editar clips; mira `video-use`<br>
**Combina con:** [remotion](human/fichas/remotion.md)<br>
**Más:** [ficha completa](human/fichas/openmontage.md) · [GitHub](https://github.com/OpenMontageInc/OpenMontage)

#### ⚛️ remotion
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 73.2k<br>
**Qué es:** Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. El render no requiere por sí solo una API de IA; revisa las condiciones de licencia del proyecto.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx create-video@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** generas video a escala con React y quieres variantes parametrizadas — **Evita si:** trabajas en Python (moviepy) o buscas un editor visual<br>
**Combina con:** [Open-Generative-AI](human/fichas/open-generative-ai.md)<br>
**Más:** [ficha completa](human/fichas/remotion.md) · [GitHub](https://github.com/remotion-dev/remotion)

#### 🎬 manim
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 42.5k<br>
**Qué es:** Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. Define objetos geométricos y transformaciones en código y renderiza la escena como video.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ManimCommunity/manim/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas animaciones matemáticas precisas y reproducibles — **Evita si:** tu flujo audiovisual actual ya cubre esa etapa<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/manim-community.md) · [GitHub](https://github.com/ManimCommunity/manim)

#### 🎞️ video-use
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 31.1k<br>
**Qué es:** El agente corta, une, subtitula y ajusta videos a partir de instrucciones en lenguaje natural.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/browser-use/video-use/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres editar videos pidiéndoselo a tu agente — **Evita si:** quieres una app de edición visual; mira `opencut`<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/video-use.md) · [GitHub](https://github.com/browser-use/video-use)

#### 🎬 rea-video
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 8.6k<br>
**Qué es:** Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md. Clasifica planos y registra capas, ritmo y técnicas de producción en un formato legible por agentes.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/JuneYaooo/rea-video/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar o recrear la estructura de un video de referencia — **Evita si:** tu flujo audiovisual actual ya cubre esa etapa<br>
**Combina con:** [remotion](human/fichas/remotion.md)<br>
**Más:** [ficha completa](human/fichas/rea-video.md) · [GitHub](https://github.com/JuneYaooo/rea-video)

#### 📲 videofy_minimal
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 656<br>
**Qué es:** Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. La ruta documentada requiere APIs de OpenAI y ElevenLabs aunque la interfaz y el montaje se ejecuten en tu equipo.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/schibsted/videofy_minimal/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres reels simples ya, sin montar un pipeline entero — **Evita si:** necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy)<br>
**Combina con:** [whisper](human/fichas/whisper.md) · [supertonic](human/fichas/supertonic.md)<br>
**Más:** [ficha completa](human/fichas/videofy-minimal.md) · [GitHub](https://github.com/schibsted/videofy_minimal)

#### 🎞️ Remotion Superpowers
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 168<br>
**Qué es:** Añade locución con IA, música, footage de stock e imágenes para producir videos en código.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/DojoCodingLabs/remotion-superpowers/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** usas Remotion con un agente y quieres producción completa — **Evita si:** no usas Remotion<br>
**Combina con:** [remotion](human/fichas/remotion.md) · [Remotion Agent Skills](human/fichas/skills-remotion.md)<br>
**Más:** [ficha completa](human/fichas/remotion-superpowers.md) · [GitHub](https://github.com/DojoCodingLabs/remotion-superpowers)

### Video generativo y pipelines automáticos

#### 🎬 MoneyPrinterTurbo ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 144k<br>
**Qué es:** MoneyPrinterTurbo automatiza la producción de shorts: das un tema o palabras clave y escribe el guion con un LLM, busca clips en Pexels o Pixabay (o usa los tuyos o video generado por IA), genera locución, subtítulos y música, y monta el resultado en 9:16, 16:9 o 1:1. Se usa desde WebUI, API, CLI o pidiéndoselo a un agente con su skill.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres producir videos cortos narrados a partir de un tema sin editar a mano — **Evita si:** necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage`<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Kokoro](human/fichas/kokoro.md) · [faster-whisper](human/fichas/faster-whisper.md)<br>
**Más:** [ficha completa](human/fichas/moneyprinterturbo.md) · [GitHub](https://github.com/harry0703/MoneyPrinterTurbo)

#### 🎬 Wan2.2 ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 18.7k<br>
**Qué es:** Wan2.2 publica pesos y código de inferencia de varios modelos de video: texto a video e imagen a video de 14B (MoE), un modelo híbrido de 5B que genera 720p a 24 fps en una RTX 4090, video guiado por voz (S2V) y animación o sustitución de personajes (Animate). Es la base de muchos flujos de ComfyUI y Diffusers.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Wan-Video/Wan2.2/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más — **Evita si:** tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md) · [Real-ESRGAN](human/fichas/real-esrgan.md) · [CosyVoice](human/fichas/cosyvoice.md)<br>
**Más:** [ficha completa](human/fichas/wan2-2.md) · [GitHub](https://github.com/Wan-Video/Wan2.2)

#### 🎬 HunyuanVideo
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 12.8k<br>
**Qué es:** HunyuanVideo publica los pesos, la definición en PyTorch y el código de inferencia de un modelo de texto a video de más de 13.000 millones de parámetros, que genera clips de unos 5 segundos (129 fotogramas) en 540p o 720p. Las variantes de imagen a video, avatares guiados por audio y personalización viven en repos aparte.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad — **Evita si:** trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md) · [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/hunyuanvideo.md) · [GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo)

#### 🎬 WanGP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 11.8k<br>
**Qué es:** WanGP, antes Wan2GP, es una interfaz web para ejecutar en tu GPU decenas de modelos generativos abiertos: video (Wan 2.1/2.2, LTX-2, Hunyuan Video), imagen (Flux, Qwen Image), voz y música (Chatterbox, Index TTS, Ace Step) y 3D. Añade cola de trabajos, LoRAs, galerías y un asistente local, Deepy, que planifica y lanza las generaciones por ti.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/deepbeepmeep/WanGP/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano — **Evita si:** prefieres construir flujos por nodos con control fino (`comfyui`) o tienes una GPU grande y quieres el código oficial (`wan2-2`)<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [MoviePy](human/fichas/moviepy.md) · [LosslessCut](human/fichas/lossless-cut.md)<br>
**Más:** [ficha completa](human/fichas/wan2gp.md) · [GitHub](https://github.com/deepbeepmeep/WanGP)

#### 🎬 LTX-Video
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 11.4k<br>
**Qué es:** LTX-Video es el repositorio de los modelos v0.9.x de Lightricks, un transformer de difusión (DiT) para texto a video, imagen a video, extensión de clips y video a video con condiciones por fotograma clave. Incluye variantes de 2B y 13B, destiladas y FP8, y LoRAs de control de pose, profundidad y bordes. Ya solo se mantiene como legado: los modelos nuevos están en LTX-2.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Lightricks/LTX-Video/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x — **Evita si:** empiezas un proyecto nuevo; Lightricks recomienda LTX-2.5 (repo Lightricks/LTX-2), o mira `wan2-2` y `wan2gp`<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md) · [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/ltx-video.md) · [GitHub](https://github.com/Lightricks/LTX-Video)

#### 🎬 short-video-factory
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.1k<br>
**Qué es:** Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. Encadena generación de texto y voz con montaje automático en una interfaz de escritorio.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/YILS-LIN/short-video-factory/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres producir variantes de videos promocionales desde materiales existentes — **Evita si:** tu flujo audiovisual actual ya cubre esa etapa<br>
**Más:** [ficha completa](human/fichas/short-video-factory.md) · [GitHub](https://github.com/YILS-LIN/short-video-factory)

#### 🎬 AI-Youtube-Shorts-Generator
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.1k<br>
**Qué es:** Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM. Transcribe, puntúa segmentos y recorta el video a formato vertical para producir clips cortos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres convertir videos largos en una primera selección de shorts — **Evita si:** tu flujo audiovisual actual ya cubre esa etapa<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/ai-youtube-shorts-generator.md) · [GitHub](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)

### Música y audio generativo

#### 🎵 AudioCraft ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 23.9k<br>
**Qué es:** AudioCraft reúne el código de inferencia y entrenamiento de los modelos de audio generativo de Meta: MusicGen (música a partir de texto o melodía), AudioGen (efectos de sonido), MAGNeT, JASCO (música condicionada por acordes y batería), el códec neuronal EnCodec y AudioSeal para marcas de agua. Está orientada a investigación, aunque se usa mucho para crear música de fondo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/facebookresearch/audiocraft/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio — **Evita si:** necesitas uso comercial (los pesos son CC-BY-NC 4.0) o generar voz hablada; para voz mira `kokoro` o `chatterbox`<br>
**Combina con:** [MoviePy](human/fichas/moviepy.md) · [remotion](human/fichas/remotion.md) · [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/audiocraft.md) · [GitHub](https://github.com/facebookresearch/audiocraft)

#### 🎬 ACE-Step-1.5
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 14.8k<br>
**Qué es:** Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. Combina modelos de generación musical y una interfaz de inferencia para producir audio y personalizar estilos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas experimentar con generación musical en tu propio equipo — **Evita si:** tu flujo audiovisual actual ya cubre esa etapa<br>
**Más:** [ficha completa](human/fichas/ace-step-1-5.md) · [GitHub](https://github.com/ace-step/ACE-Step-1.5)

#### 🎬 Music-Megathread
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 3.1k<br>
**Qué es:** Directorio de reproductores, herramientas, servicios y otros recursos relacionados con música. Agrupa enlaces a proyectos y servicios musicales para explorar alternativas por función.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/MoonWalker440/Music-Megathread/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** buscas recursos musicales y quieres comparar opciones desde una lista — **Evita si:** tu flujo audiovisual actual ya cubre esa etapa<br>
**Más:** [ficha completa](human/fichas/music-megathread.md) · [GitHub](https://github.com/MoonWalker440/Music-Megathread)

---

## 📄 13. Trabajar con documentos y presentaciones

Extrae texto, aplica OCR, transforma PDFs o crea diapositivas. Empieza por el formato de entrada y el resultado que necesitas.

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
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 70.6k<br>
**Qué es:** Entiende la estructura del documento (tablas, layout, fórmulas, orden de lectura) y la exporta para RAG y agentes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install docling` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres convertir documentos a Markdown con buena estructura — **Evita si:** solo tienes PDFs de texto simples; mira `markitdown`<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [RAGFlow](human/fichas/ragflow.md) · [Qdrant](human/fichas/qdrant.md)<br>
**Más:** [ficha completa](human/fichas/docling.md) · [GitHub](https://github.com/docling-project/docling)

#### 📝 markitdown
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 195k<br>
**Qué es:** Es la puerta de entrada habitual para ingesta de documentos en pipelines RAG.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install markitdown` (comprobar los pasos completos en la ficha).<br>
**Elige si:** alimentas LLMs con documentos de formatos variados — **Evita si:** ya tienes el texto limpio o necesitas fidelidad de layout total (no es un reconstructor de PDF)<br>
**Combina con:** [ppt-master](human/fichas/ppt-master.md) · [open-notebook](human/fichas/open-notebook.md)<br>
**Más:** [ficha completa](human/fichas/markitdown.md) · [GitHub](https://github.com/microsoft/markitdown)

#### 🔄 MinerU
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 83.7k<br>
**Qué es:** Muy bueno con papers científicos, tablas y fórmulas; ofrece CLI, API y app de escritorio.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/opendatalab/MinerU/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** procesas documentos científicos o técnicos complejos — **Evita si:** quieres algo ligero; mira `markitdown`<br>
**Combina con:** [RAGFlow](human/fichas/ragflow.md)<br>
**Más:** [ficha completa](human/fichas/mineru.md) · [GitHub](https://github.com/opendatalab/MinerU)

#### 🔄 Pandoc
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 46.9k<br>
**Qué es:** La navaja suiza de la conversión de textos: genera Word o PDF desde Markdown y al revés.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/jgm/pandoc/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas convertir entre formatos de texto — **Evita si:** necesitas extraer estructura de PDFs escaneados; mira `docling`<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/pandoc.md) · [GitHub](https://github.com/jgm/pandoc)

#### 🔄 Marker
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.9k<br>
**Qué es:** Pensado para libros y papers, con opción de mejorar el resultado usando un LLM.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install marker-pdf` (comprobar los pasos completos en la ficha).<br>
**Elige si:** conviertes PDFs largos con fórmulas — **Evita si:** necesitas uso comercial sin licencia; revisa su licencia<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/marker.md) · [GitHub](https://github.com/datalab-to/marker)

#### 🔄 PDF Inspector
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 20k<br>
**Qué es:** Detecta si un PDF necesita OCR para enrutarlo al proceso correcto, y extrae texto rápido cuando no hace falta. De Firecrawl.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install pdf-inspector` (comprobar los pasos completos en la ficha).<br>
**Elige si:** procesas muchos PDFs y quieres ahorrar OCR — **Evita si:** necesitas la conversión completa a Markdown; mira `docling`<br>
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md) · [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/pdf-inspector.md) · [GitHub](https://github.com/firecrawl/pdf-inspector)

#### 🔄 Unstructured
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 15.7k<br>
**Qué es:** Particiona más de 25 tipos de archivo en elementos (títulos, tablas, texto) y los prepara para bases vectoriales.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install "unstructured[all-docs]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** tienes muchos formatos de documentos distintos — **Evita si:** solo procesas PDFs; mira `docling`<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/unstructured.md) · [GitHub](https://github.com/Unstructured-IO/unstructured)

#### 📄 Youtube2Webpage
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.5k<br>
**Qué es:** Convierte una charla en un artículo navegable con contexto visual.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/obra/Youtube2Webpage/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres video → artículo con transcripción y capturas — **Evita si:** necesitas edición de video o el contenido no tiene subtítulos<br>
**Combina con:** [whisper](human/fichas/whisper.md)<br>
**Más:** [ficha completa](human/fichas/youtube2webpage.md) · [GitHub](https://github.com/obra/Youtube2Webpage)

### OCR

#### 🔠 PaddleOCR ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 92.7k<br>
**Qué es:** Reconoce texto en más de 80 idiomas y analiza documentos con tablas y layout. Incluye modelos pequeños para dispositivos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas OCR preciso y multilingüe — **Evita si:** solo quieres hacer buscables PDFs escaneados; mira `ocrmypdf`<br>
**Combina con:** [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/paddleocr.md) · [GitHub](https://github.com/PaddlePaddle/PaddleOCR)

#### 🔠 OCRmyPDF ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 35.3k<br>
**Qué es:** Convierte escaneos en PDF/A buscables manteniendo la imagen original.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ocrmypdf/OCRmyPDF/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** tienes PDFs escaneados que quieres buscar — **Evita si:** necesitas extraer estructura; mira `docling`<br>
**Combina con:** [Tesseract](human/fichas/tesseract.md) · [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/ocrmypdf.md) · [GitHub](https://github.com/ocrmypdf/OCRmyPDF)

#### 🔠 Tesseract
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 77.5k<br>
**Qué es:** Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma. La precisión depende del idioma, el escaneo y la preparación de la imagen.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/tesseract-ocr/tesseract/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres OCR clásico sin GPU — **Evita si:** tus documentos tienen layouts complejos; mira `paddleocr`<br>
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md)<br>
**Más:** [ficha completa](human/fichas/tesseract.md) · [GitHub](https://github.com/tesseract-ocr/tesseract)

#### 🔠 Unlimited-OCR
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 31.2k<br>
**Qué es:** Extrae texto y estructura de documentos de muchas páginas sin dividirlos, pensado para contexto largo.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/baidu/Unlimited-OCR/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** procesas documentos muy largos con GPU — **Evita si:** necesitas algo probado y ligero; mira `docling`<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [cosmos](human/fichas/cosmos.md) · [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/unlimited-ocr.md) · [GitHub](https://github.com/baidu/Unlimited-OCR)

#### 🔠 olmOCR
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 19.8k<br>
**Qué es:** Pensado para crear datasets de entrenamiento a partir de millones de PDFs, con orden de lectura correcto.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install olmocr` (comprobar los pasos completos en la ficha).<br>
**Elige si:** procesas grandes volúmenes de PDFs con GPU — **Evita si:** no tienes GPU; mira `ocrmypdf` o `tesseract`<br>
**Combina con:** [vLLM](human/fichas/vllm.md)<br>
**Más:** [ficha completa](human/fichas/olmocr.md) · [GitHub](https://github.com/allenai/olmocr)

### Herramientas PDF

#### 📑 Stirling-PDF ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 96.6k<br>
**Qué es:** Más de 50 herramientas de PDF en el navegador sin enviar archivos a terceros.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un iLovePDF privado — **Evita si:** solo necesitas OCR; mira `ocrmypdf`<br>
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md)<br>
**Más:** [ficha completa](human/fichas/stirling-pdf.md) · [GitHub](https://github.com/Stirling-Tools/Stirling-PDF)

#### 📑 PDFMathTranslate
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 38.4k<br>
**Qué es:** Ideal para leer artículos científicos en tu idioma sin perder el layout. Admite Google, DeepL, OpenAI, Ollama y más.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install pdf2zh` (comprobar los pasos completos en la ficha).<br>
**Elige si:** traduces PDFs técnicos y quieres conservar el formato — **Evita si:** necesitas editar el PDF; mira `stirling-pdf`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/pdfmathtranslate.md) · [GitHub](https://github.com/PDFMathTranslate/PDFMathTranslate)

#### 📄 pdfcraft
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 9.8k<br>
**Qué es:** Apunta a ser la alternativa local y sin nube a los servicios online de PDF.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** manipulas PDFs con privacidad y sin instalar nada — **Evita si:** necesitas conversión a Markdown para IA (markitdown) o edición de contenido (no solo manipulación de páginas)<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/pdfcraft.md) · [GitHub](https://github.com/PDFCraftTool/pdfcraft)

#### 📑 PdfDing
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 1.8k<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** Organiza y lee tus PDFs desde cualquier dispositivo. El desarrollo se trasladó a Codeberg.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mrmn2/PdfDing/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres organizar y leer PDFs en tu servidor — **Evita si:** necesitas editar PDFs; mira `stirling-pdf`<br>
**Combina con:** [markitdown](human/fichas/markitdown.md) · [ppt-master](human/fichas/ppt-master.md) · [reveal.js](human/fichas/reveal-js.md)<br>
**Más:** [ficha completa](human/fichas/pdfding.md) · [GitHub](https://github.com/mrmn2/PdfDing)

### Presentaciones

#### 🖥️ Slidev ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 49.5k<br>
**Qué es:** Escribe tus slides en Markdown y obtén resaltado de código, diagramas, animaciones y exportación a PDF. Los agentes de código lo usan bien.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/slidevjs/slidev/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** haces presentaciones técnicas y quieres control como código — **Evita si:** necesitas slides para negocio generadas con IA; mira `presenton`<br>
**Combina con:** [Mermaid](human/fichas/mermaid.md)<br>
**Más:** [ficha completa](human/fichas/slidev.md) · [GitHub](https://github.com/slidevjs/slidev)

#### 📊 ppt-master
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 76.8k<br>
**Qué es:** Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. Necesita un agente con acceso a un modelo; los servicios opcionales de imágenes o contenido se revisan por separado.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add hugohe3/ppt-master` (comprobar los pasos completos en la ficha).<br>
**Elige si:** quieres PPTX editable de Office rápido — **Evita si:** prefieres slides web por código (reveal.js) o control de diseño pixel-perfect<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/ppt-master.md) · [GitHub](https://github.com/hugohe3/ppt-master)

#### 🖥️ reveal.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 72.6k<br>
**Qué es:** Convierte las diapositivas en una página web versionable y reproducible por código.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/hakimel/reveal.js/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres slides web por código, versionables — **Evita si:** necesitas PPTX editable en Office (ppt-master) o un editor visual de slides<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/reveal-js.md) · [GitHub](https://github.com/hakimel/reveal.js)

#### 🖥️ Marp
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 12.7k<br>
**Qué es:** Escribes Markdown con separadores y obtienes slides limpias; tiene extensión de VS Code.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/marp-team/marp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres slides simples en Markdown — **Evita si:** necesitas interactividad y componentes; mira `slidev`<br>
**Más:** [ficha completa](human/fichas/marp.md) · [GitHub](https://github.com/marp-team/marp)

#### 🖥️ Presenton
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 11.9k<br>
**Qué es:** Crea presentaciones editables a partir de un prompt o documento, con tus plantillas, y exporta a PPTX o PDF.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/presenton/presenton/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres generar presentaciones de negocio con IA — **Evita si:** prefieres control total como código; mira `slidev`<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/presenton.md) · [GitHub](https://github.com/presenton/presenton)

### Diagramas y documentación

#### 🗺️ Mermaid ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 91.1k<br>
**Qué es:** GitHub, Notion y muchos editores lo renderizan de forma nativa; los LLM lo escriben muy bien.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mermaid-js/mermaid/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres diagramas como texto — **Evita si:** necesitas dibujar a mano alzada; mira `excalidraw`<br>
**Combina con:** [Slidev](human/fichas/slidev.md)<br>
**Más:** [ficha completa](human/fichas/mermaid.md) · [GitHub](https://github.com/mermaid-js/mermaid)

#### 📄 archify
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 96.5k<br>
**Qué es:** Skill para convertir ideas, planes y bases de código en diagramas y visualizaciones HTML interactivas. El agente transforma una descripción en una visualización que se puede abrir y explorar en el navegador.<br>
**Acceso:** Sin API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/tt-a1i/archify/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres explicar una arquitectura o un plan mediante una visualización interactiva — **Evita si:** el formato de salida no encaja con tus documentos<br>
**Combina con:** [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/archify.md) · [GitHub](https://github.com/tt-a1i/archify)

---

## 📈 14. Investigar finanzas y mercados

Agentes de investigación, análisis cuantitativo, backtesting y bots de ejemplo. Distingue una explicación o simulación de una operación con fondos reales.

### Agentes de investigación financiera

#### 📚 daily_stock_analysis ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟡 medio · ⭐ 72.3k<br>
**Qué es:** Combina datos de mercado, noticias en tiempo real y análisis con LLM para generar reportes automáticos por Telegram, Slack, correo o WeChat. Puede correr gratis con GitHub Actions.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres un análisis bursátil diario automatizado — **Evita si:** buscas asesoría financiera: esto no lo es<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/daily-stock-analysis.md) · [GitHub](https://github.com/ZhuLinsen/daily_stock_analysis)

#### 📊 dexter ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟡 medio · ⭐ 27.8k<br>
**Qué es:** Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis. Ejecuta tareas de investigación con herramientas y modelos y organiza la evidencia obtenida.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/virattt/dexter/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres experimentar con investigación financiera asistida por un agente — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/dexter.md) · [GitHub](https://github.com/virattt/dexter)

#### 📊 TradingAgents
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 123k<br>
**Qué es:** Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de trading. Coordina roles que consultan datos, comparan argumentos y generan resultados de investigación.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/TauricResearch/TradingAgents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar arquitecturas multiagente aplicadas a investigación de mercados — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/tradingagents.md) · [GitHub](https://github.com/TauricResearch/TradingAgents)

#### 📊 FinceptTerminal
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 33.8k<br>
**Qué es:** Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes. Combina módulos de mercado y análisis en una aplicación de escritorio con integraciones de datos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres explorar una terminal abierta de investigación y datos financieros — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/finceptterminal.md) · [GitHub](https://github.com/Fincept-Corporation/FinceptTerminal)

#### 📊 AutoHedge
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 6.7k<br>
**Qué es:** Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado. Distribuye análisis y decisiones entre agentes con funciones especializadas y herramientas de mercado.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/The-Swarm-Corporation/AutoHedge/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar una arquitectura de agentes para investigación de trading — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/autohedge.md) · [GitHub](https://github.com/The-Swarm-Corporation/AutoHedge)

#### 📊 QuantHarness
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 2.9k<br>
**Qué es:** Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de trading. Coordina agentes con LangChain y LangGraph y presenta sus análisis mediante una interfaz web.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Y-Research-SBU/QuantHarness/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar la coordinación de agentes sobre señales de precio — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/quantharness.md) · [GitHub](https://github.com/Y-Research-SBU/QuantHarness)

### Modelos y backtesting cuantitativo

#### 📊 qlib ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 50.3k<br>
**Qué es:** Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias. Organiza preparación de datos, entrenamiento, predicción y backtesting en pipelines de investigación.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/qlib/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** necesitas experimentar con modelos y evaluaciones cuantitativas reproducibles — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/qlib.md) · [GitHub](https://github.com/microsoft/qlib)

#### 📊 chartAnalyst
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 21<br>
**Qué es:** Experimento de aprendizaje profundo que usa redes convolucionales para reconocer patrones en gráficos bursátiles. Convierte ventanas de precios en representaciones que una CNN usa para clasificar patrones.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/huima58/chartAnalyst/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar aprendizaje sobre imágenes de series financieras — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/chartanalyst.md) · [GitHub](https://github.com/huima58/chartAnalyst)

### Bots y conexiones a exchanges

#### 📊 binance-trader
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟡 medio · ⭐ 2.8k<br>
**Qué es:** Bot experimental de Python para estudiar estrategias y automatización con la API de Binance. Consulta precios y procesa reglas de estrategia mediante scripts de prueba y ejecución.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/yasinkuyu/binance-trader/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar cómo se estructura un bot experimental conectado a Binance — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/binance-trader.md) · [GitHub](https://github.com/yasinkuyu/binance-trader)

#### 📊 crypto-trader
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 633<br>
**Aviso:** ⚠️ Archivado en GitHub: ya no recibe cambios.<br>
**Qué es:** Biblioteca de Python con bindings de la API de Gemini y un ejemplo de estrategia de criptomonedas. Expone operaciones de la API del exchange y tipos para construir solicitudes y órdenes.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/pirate/crypto-trader/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres consultar una implementación sencilla de integración con Gemini — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/crypto-trader.md) · [GitHub](https://github.com/pirate/crypto-trader)

#### 📊 open-sol-bot
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 406<br>
**Qué es:** Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado. Conecta servicios de la cadena y componentes de aplicación para seguir eventos y procesar operaciones.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ChainBuff/open-sol-bot/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar automatización y seguimiento de transacciones en Solana — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/open-sol-bot.md) · [GitHub](https://github.com/ChainBuff/open-sol-bot)

#### 📊 IntelliTrader
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 158<br>
**Qué es:** Bot configurable de criptomonedas con componentes de simulación, señales y conexión a exchanges. Aplica una configuración de estrategias y proveedores para observar o ejecutar operaciones.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/jazzonaut/IntelliTrader/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar la arquitectura de un bot con modo de trading virtual — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/intellitrader.md) · [GitHub](https://github.com/jazzonaut/IntelliTrader)

### Ejemplos y aprendizaje

#### 📊 machine-learning-for-trading
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 21.8k<br>
**Qué es:** Material y código de Machine Learning for Trading para estudiar datos, modelos y evaluación de estrategias. Recorre un flujo de investigación desde la obtención de datos hasta pruebas y despliegue de modelos.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/stefan-jansen/machine-learning-for-trading/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres aprender un proceso de investigación de trading basado en datos — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/machine-learning-for-trading.md) · [GitHub](https://github.com/stefan-jansen/machine-learning-for-trading)

#### 📊 stocks
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 28<br>
**Qué es:** Scripts para recopilar recomendaciones de analistas bursátiles y preparar datos para su evaluación histórica. Extrae recomendaciones de sitios externos y organiza matrices para compararlas con resultados posteriores.<br>
**Acceso:** Sin API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/omerdr/stocks/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** quieres estudiar el rendimiento histórico de recomendaciones publicadas — **Evita si:** necesitas resultados operativos validados en vez de material de investigación<br>
**Más:** [ficha completa](human/fichas/stocks-analyst.md) · [GitHub](https://github.com/omerdr/stocks)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
