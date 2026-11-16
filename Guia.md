# 🌌 Guía completa de BL_Alexandria

Las **638 fichas** de la biblioteca en un solo documento, agrupadas por categoría y subcategoría. Úsala para leer de corrido o buscar con Ctrl+F; para navegar por partes usa la [guía humana](human/README.md) o el [explorador interactivo](docs/index.html).

## 🧭 Cómo leer cada ficha

- **Etiquetas:** Ejecución 🏠 local · ☁️ cloud/API · 🔀 híbrido — Rol ⚙️ plataforma · 🧩 motor · 📚 librería · 🎨 skill · 📂 catálogo · 🖥️ app — Setup 🟢 fácil · 🟡 medio · 🔴 pesado — 🔌 MCP.
- **⭐** junto al nombre: punto de partida editorial. El número de estrellas viene de GitHub.
- **Elige si / Evita si** te dicen en una línea si encaja; **Combina con** lleva a sus complementos.

## 📂 Mapa de categorías

| # | Categoría | Repos | Para qué |
|---:|---|---:|---|
| 1 | [🤖 Automatizar procesos y crear herramientas internas](#-1-automatizar-procesos-y-crear-herramientas-internas) | 15 | Motores de flujos, ecosistema n8n y aplicaciones internas. Elige el motor del proceso y conecta después sus fuentes de datos, canales y modelos. |
| 2 | [🧠 Skills, plugins y métodos para agentes](#-2-skills-plugins-y-métodos-para-agentes) | 30 | Catálogos de skills, plugins y métodos generales de desarrollo. Elige según tu cliente y consulta las especialidades de diseño o negocio en su sala específica. |
| 3 | [🕸️ Construir agentes y coordinar equipos de IA](#️-3-construir-agentes-y-coordinar-equipos-de-ia) | 30 | Frameworks, builders visuales y experimentos de coordinación. Separa la base técnica que integras del asistente listo que utilizas para una tarea. |
| 4 | [🕷️ Buscar, extraer y monitorear información web](#️-4-buscar-extraer-y-monitorear-información-web) | 20 | Buscadores, crawlers, extracción y seguimiento de páginas o redes. Para hacer clic y operar interfaces utiliza la sala de navegadores y automatización web. |
| 5 | [🔌 Conectar herramientas con MCP](#-5-conectar-herramientas-con-mcp) | 23 | SDKs, servidores, clientes y directorios MCP. Un servidor aporta acciones o datos; el modelo y su acceso pertenecen al cliente que lo utiliza. |
| 6 | [🧬 Memoria, RAG y búsqueda de conocimiento](#-6-memoria-rag-y-búsqueda-de-conocimiento) | 23 | Memoria persistente, sistemas RAG y bases vectoriales. La memoria mantiene contexto; RAG recupera documentos; una base vectorial almacena el índice de búsqueda. |
| 7 | [🧑‍💻 Entender código y comprobar su calidad](#-7-entender-código-y-comprobar-su-calidad) | 13 | Índices de código, análisis, calidad, benchmarks y herramientas de desarrollo. Empieza por comprender el proyecto y después elige qué comprobaciones necesitas. |
| 8 | [🏠 Chats, modelos locales y espacios privados](#-8-chats-modelos-locales-y-espacios-privados) | 27 | Motores locales, chats y workspaces. Tener la interfaz en tu equipo no garantiza que el modelo sea local: comprueba su backend y los requisitos de cada ficha. |
| 9 | [🎨 Diseñar y construir interfaces web](#-9-diseñar-y-construir-interfaces-web) | 28 | Componentes, estilos, editores visuales y herramientas de UI con IA. Elige la base de tu interfaz y consulta animación o skills especializadas en sus salas. |
| 10 | [📊 Dashboards, analítica y mapas](#-10-dashboards-analítica-y-mapas) | 22 | Analítica web, BI, gráficos y herramientas geoespaciales. Medir visitas, consultar un negocio y procesar fotografías para crear mapas requieren piezas diferentes. |
| 11 | [🖼️ Generar y editar imágenes con IA](#️-11-generar-y-editar-imágenes-con-ia) | 9 | Interfaces y modelos de generación, recorte, restauración y ampliación. Distingue la aplicación, sus modelos y el coste o equipo para generar cada imagen. |
| 12 | [🎬 Editar, grabar y generar video](#-12-editar-grabar-y-generar-video) | 15 | Editores, grabadores, utilidades de medios y modelos de video generativo. La edición de material existente y la generación de nuevas escenas tienen requisitos distintos. |
| 13 | [📄 PDF, OCR y procesamiento de documentos](#-13-pdf-ocr-y-procesamiento-de-documentos) | 19 | Extracción de texto, OCR, conversión y gestión de PDF. Empieza por el formato de entrada y comprueba con una muestra si conserva el contenido que necesitas. |
| 14 | [📈 Investigar finanzas y mercados](#-14-investigar-finanzas-y-mercados) | 22 | Agentes de investigación, análisis cuantitativo, backtesting y bots de ejemplo. Distingue una explicación o simulación de una operación con fondos reales. |
| 15 | [🗂️ Organizar notas, archivos y servicios personales](#️-15-organizar-notas-archivos-y-servicios-personales) | 27 | Notas, sincronización, privacidad, aprendizaje y servidores personales. Distingue una aplicación lista, un plugin y la infraestructura que debes administrar. |
| 16 | [🔍 Analizar software y comprobar su seguridad](#-16-analizar-software-y-comprobar-su-seguridad) | 26 | Depuradores, descompiladores, análisis de binarios y agentes de pruebas. Trabaja sobre software propio o con autorización y separa análisis, modificación y pruebas activas. |
| 17 | [🤖 WhatsApp, mensajería y chatbots](#-17-whatsapp-mensajería-y-chatbots) | 10 | Conecta WhatsApp y otros canales o prepara un chatbot. Distingue el canal de mensajes, el modelo que responde y la bandeja donde una persona retoma la conversación. |
| 18 | [🤖 CRM, ventas y marketing](#-18-crm-ventas-y-marketing) | 13 | Gestiona clientes, soporte, campañas, correo y publicaciones. Un CRM guarda la relación con el cliente; una herramienta de campañas distribuye mensajes. Comprueba los servicios externos y sus tarifas. |
| 19 | [🧠 Aprender IA y escribir mejores prompts](#-19-aprender-ia-y-escribir-mejores-prompts) | 30 | Cursos, ejemplos, guías y colecciones de prompts. Son material de aprendizaje: cada ejemplo puede necesitar sus propias cuentas, dependencias o modelos. |
| 20 | [🕸️ Programar con agentes de código](#️-20-programar-con-agentes-de-código) | 19 | Agentes de terminal, extensiones de editor y entornos para programar con IA. Revisa qué cliente utilizas, cómo inicia sesión y si el modelo usa un plan, una API o un servidor local. |
| 21 | [🕸️ Asistentes e investigación con agentes](#️-21-asistentes-e-investigación-con-agentes) | 17 | Asistentes personales, equipos de agentes e investigación con fuentes. Compara la tarea que completan, las herramientas que pueden usar y la revisión que necesitas hacer del resultado. |
| 22 | [🕸️ Infraestructura, despliegue y herramientas para agentes](#️-22-infraestructura-despliegue-y-herramientas-para-agentes) | 17 | Sandboxes, herramientas de ejecución, backend y alojamiento. Son piezas de infraestructura: separa el coste del servidor, los servicios conectados y las llamadas al modelo. |
| 23 | [🧬 Operar, evaluar y medir modelos de IA](#-23-operar-evaluar-y-medir-modelos-de-ia) | 19 | Servidores de inferencia, gateways, evaluación, trazas y control de contexto. Cada pieza cubre una etapa: ejecutar el modelo, observarlo o comprobar la calidad de sus respuestas. |
| 24 | [🧑‍💻 Modelos abiertos y entrenamiento](#-24-modelos-abiertos-y-entrenamiento) | 14 | Modelos, bibliotecas de entrenamiento y ajuste fino. Revisa la licencia de los pesos, la memoria necesaria y la opción de inferencia antes de descargar o entrenar. |
| 25 | [🧑‍💻 Procesar datos y trabajar con notebooks](#-25-procesar-datos-y-trabajar-con-notebooks) | 9 | Motores de consulta, tablas, notebooks y aplicaciones de datos. Empieza por un archivo pequeño y distingue una herramienta de análisis de un catálogo o conjunto de datos de referencia. |
| 26 | [🎨 Animación, gráficos y creación 3D](#-26-animación-gráficos-y-creación-3d) | 19 | Animación web, motores gráficos, modelado y renderizado 3D. Una librería se integra en una aplicación; un editor se utiliza directamente. Consulta el formato de entrada y el equipo necesario. |
| 27 | [🎨 Skills de diseño, contenido y especialidades](#-27-skills-de-diseño-contenido-y-especialidades) | 36 | Skills y plugins para diseño, escritura, marketing, ciencia y negocio. Se añaden a un agente compatible; generar imágenes, publicar o consultar servicios puede requerir cuentas adicionales. |
| 28 | [🖼️ Visión artificial, rostros y percepción](#️-28-visión-artificial-rostros-y-percepción) | 19 | Detección, seguimiento, segmentación, rostros y percepción espacial. Distingue el modelo, sus pesos y las herramientas para preparar datos. Comprueba requisitos y permisos sobre las imágenes. |
| 29 | [🎬 Audio, transcripción, voz y música](#-29-audio-transcripción-voz-y-música) | 25 | Transcripción, síntesis, clonación de voz, agentes de audio y música. Compara idioma, latencia, procesamiento local y servicios externos según la tarea concreta. |
| 30 | [🎬 Video con código y agentes creativos](#-30-video-con-código-y-agentes-creativos) | 22 | Herramientas y skills para escenas, motion graphics y montaje programático. Distingue el renderizado del video de la generación de sus imágenes o voces, que puede necesitar otros proveedores. |
| 31 | [📄 Presentaciones, diagramas y explicación visual](#-31-presentaciones-diagramas-y-explicación-visual) | 8 | Presentaciones, diagramas y documentación visual. Elige entre editar una pieza, escribir su estructura o generarla con un agente; revisa cómo se exporta antes de empezar. |
| 32 | [🕷️ Navegadores y automatización web](#️-32-navegadores-y-automatización-web) | 12 | Navegadores, librerías de pruebas y agentes que interactúan con sitios web. Para leer páginas estáticas consulta extracción web; para operar una interfaz empieza por estas herramientas. |

## 🧪 Recetas de integración

- **[💬 Bot de WhatsApp con IA](human/playbooks/bot-de-whatsapp-con-ia.md)** — Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta. [evolution-api](human/fichas/evolution-api.md) → [n8n](human/fichas/n8n.md) → [n8n-mcp](human/fichas/n8n-mcp.md) → [n8n-skills](human/fichas/n8n-skills.md) → [chatwoot](human/fichas/chatwoot.md) → [novu](human/fichas/novu.md)
- **[🎬 Pipeline de Reels / video corto](human/playbooks/pipeline-de-reels-video-corto.md)** — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados. [whisperX](human/fichas/whisperx.md) → [Kokoro](human/fichas/kokoro.md) → [ComfyUI](human/fichas/comfyui.md) → [Real-ESRGAN](human/fichas/real-esrgan.md) → [remotion](human/fichas/remotion.md) → [FFmpeg](human/fichas/ffmpeg.md) → [MoneyPrinterTurbo](human/fichas/moneyprinterturbo.md)
- **[🔎 Agente de research profundo](human/playbooks/agente-de-research-profundo.md)** — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas. [gpt-researcher](human/fichas/gpt-researcher.md) → [SearXNG](human/fichas/searxng.md) → [crawl4ai](human/fichas/crawl4ai.md) → [browser-use](human/fichas/browser-use.md) → [markitdown](human/fichas/markitdown.md) → [langfuse](human/fichas/langfuse.md)
- **[🏠 Workspace privado local soberano](human/playbooks/workspace-privado-local-soberano.md)** — Preparar chat, documentos y memoria con rutas locales, comprobando por separado modelos, herramientas y conexiones externas. [Ollama](human/fichas/ollama.md) → [odysseus](human/fichas/odysseus.md) → [open-notebook](human/fichas/open-notebook.md) → [mem0](human/fichas/mem0.md) → [SearXNG](human/fichas/searxng.md)
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

## 🤖 1. Automatizar procesos y crear herramientas internas

Motores de flujos, ecosistema n8n y aplicaciones internas. Elige el motor del proceso y conecta después sus fuentes de datos, canales y modelos.

**⚖️ ¿Cuál elegir? — n8n, huginn, Kestra, activepieces, Node-RED, Windmill, Trigger.dev**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [n8n](human/fichas/n8n.md) | Tu objetivo encaja con estos ejemplos: Un formulario de contacto genera un registro para seguimiento comercial; Un flujo resume documentos con Ollama en lugar de una API remota | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [huginn](human/fichas/huginn.md) | Tu objetivo encaja con estos ejemplos: Vigilar novedades de un sitio que publica una fuente RSS; Transformar un webhook entrante en un evento para otros agentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Kestra](human/fichas/kestra.md) | Tu objetivo encaja con estos ejemplos: Programar una importación diaria de archivos con reintentos; Combinar tareas de datos con una consulta a un modelo Ollama | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [activepieces](human/fichas/activepieces.md) | Tu objetivo encaja con estos ejemplos: Pasar respuestas de un formulario a una aplicación de negocio; Solicitar aprobación humana antes de continuar una automatización | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Node-RED](human/fichas/node-red.md) | Tu objetivo encaja con estos ejemplos: Mostrar lecturas de un sensor recibidas por MQTT; Convertir un webhook en una secuencia de acciones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Windmill](human/fichas/windmill.md) | Tu objetivo encaja con estos ejemplos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Trigger.dev](human/fichas/trigger-dev.md) | Tu objetivo encaja con estos ejemplos: Procesar en segundo plano un archivo subido por un usuario; Reintentar una tarea de generación cuando falla el proveedor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — NocoDB, Appsmith, ToolJet, Budibase**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [NocoDB](human/fichas/nocodb.md) | Tu objetivo encaja con estos ejemplos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Appsmith](human/fichas/appsmith.md) | Tu objetivo encaja con estos ejemplos: Preparar un panel para que soporte consulte expedientes; Construir un formulario interno que actualiza datos mediante una API | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [ToolJet](human/fichas/tooljet.md) | Tu objetivo encaja con estos ejemplos: Crear un panel interno para consultar pedidos y su estado; Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Budibase](human/fichas/budibase.md) | Tu objetivo encaja con estos ejemplos: Registrar solicitudes internas y seguir su estado; Montar un proceso que combina formulario, automatización y agente de IA | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Motores de workflow y automatización

#### 🔁 n8n ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 211k<br>
**Qué es:** Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Un formulario de contacto genera un registro para seguimiento comercial; Un flujo resume documentos con Ollama en lugar de una API remota — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n-mcp](human/fichas/n8n-mcp.md) · [n8n-skills](human/fichas/n8n-skills.md) · [evolution-api](human/fichas/evolution-api.md) · [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md)<br>
**Más:** [ficha completa](human/fichas/n8n.md) · [GitHub](https://github.com/n8n-io/n8n)

#### 🤖 huginn
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 50.5k<br>
**Qué es:** Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú".<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `docker run -it -p 3000:3000 ghcr.io/huginn/huginn` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Vigilar novedades de un sitio que publica una fuente RSS; Transformar un webhook entrante en un evento para otros agentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md) · [coolify](human/fichas/coolify.md) · [changedetection.io](human/fichas/changedetection.md)<br>
**Más:** [ficha completa](human/fichas/huginn.md) · [GitHub](https://github.com/huginn/huginn)

#### 🔁 Kestra
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.2k<br>
**Qué es:** Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run --pull=always --rm -it -p 8080:8080 --user=root `
  --name kestra `
  -v "kestra_data:/app/storage" `
  -v "kestra_db:/app/data" `
  -v "/var/run/docker.sock:/var/run/docker.sock" `
  -v "C:/Temp:/tmp" `
  -e KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true `
  kestra/kestra:latest-slim server local` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Programar una importación diaria de archivos con reintentos; Combinar tareas de datos con una consulta a un modelo Ollama — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [Apache Superset](human/fichas/superset.md) · [Claude Code](human/fichas/claude-code.md) · [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/kestra.md) · [GitHub](https://github.com/kestra-io/kestra)

#### 🧩 activepieces
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 25.5k<br>
**Qué es:** Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://www.activepieces.com/docs/install/overview); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Pasar respuestas de un formulario a una aplicación de negocio; Solicitar aprobación humana antes de continuar una automatización — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [NocoDB](human/fichas/nocodb.md) · [Claude Code](human/fichas/claude-code.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/activepieces.md) · [GitHub](https://github.com/activepieces/activepieces)

#### 🔁 Node-RED
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 23.8k<br>
**Qué es:** Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://nodered.org/docs/getting-started/local); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Mostrar lecturas de un sensor recibidas por MQTT; Convertir un webhook en una secuencia de acciones — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Home Assistant](human/fichas/home-assistant.md) · [Ollama](human/fichas/ollama.md) · [Grafana](human/fichas/grafana.md)<br>
**Más:** [ficha completa](human/fichas/node-red.md) · [GitHub](https://github.com/node-red/node-red)

#### 🔁 Windmill
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.6k<br>
**Qué es:** Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `curl https://raw.githubusercontent.com/windmill-labs/windmill/main/docker-compose.yml -o docker-compose.yml
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/Caddyfile -o Caddyfile
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/.env -o .env

docker compose up -d` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [Claude Code](human/fichas/claude-code.md) · [Polars](human/fichas/polars.md)<br>
**Más:** [ficha completa](human/fichas/windmill.md) · [GitHub](https://github.com/windmill-labs/windmill)

#### 🔁 Trigger.dev
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 16.8k<br>
**Qué es:** Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://trigger.dev/docs/quick-start); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Procesar en segundo plano un archivo subido por un usuario; Reintentar una tarea de generación cuando falla el proveedor — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md) · [FFmpeg](human/fichas/ffmpeg.md) · [playwright](human/fichas/playwright.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/trigger-dev.md) · [GitHub](https://github.com/triggerdotdev/trigger.dev)

### Ecosistema n8n

#### 🔁 Self-hosted AI Starter Kit ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 15.4k<br>
**Qué es:** Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
cp .env.example .env # you should update secrets and passwords inside
docker compose --profile cpu up` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente local que responde preguntas sobre material de ejemplo; Explorar cómo se conectan n8n, Ollama y una base vectorial — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n-mcp](human/fichas/n8n-mcp.md) · [Open WebUI](human/fichas/open-webui.md) · [Docling](human/fichas/docling.md) · [Awesome n8n Templates](human/fichas/awesome-n8n-templates.md)<br>
**Más:** [ficha completa](human/fichas/self-hosted-ai-starter-kit.md) · [GitHub](https://github.com/n8n-io/self-hosted-ai-starter-kit)

#### 🔁 Awesome n8n Templates
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 26.4k<br>
**Qué es:** Colección de plantillas de n8n para estudiar o importar automatizaciones de servicios y tareas habituales.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/enescingoz/awesome-n8n-templates/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una plantilla que clasifica correo con Ollama; Adaptar una alerta de precio que avisa por Telegram — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [n8n-mcp](human/fichas/n8n-mcp.md) · [n8n-skills](human/fichas/n8n-skills.md) · [Self-hosted AI Starter Kit](human/fichas/self-hosted-ai-starter-kit.md)<br>
**Más:** [ficha completa](human/fichas/awesome-n8n-templates.md) · [GitHub](https://github.com/enescingoz/awesome-n8n-templates)

#### 🔌 n8n-mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 23.3k<br>
**Qué es:** Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/SELF_HOSTING.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Investigar por qué falló una ejecución de un flujo propio; Preparar y validar un flujo de prueba con ayuda del agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [n8n-skills](human/fichas/n8n-skills.md) · [Claude Code](human/fichas/claude-code.md) · [MCP Inspector](human/fichas/mcp-inspector.md)<br>
**Más:** [ficha completa](human/fichas/n8n-mcp.md) · [GitHub](https://github.com/czlonkowski/n8n-mcp)

#### 🛠️ n8n-skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 6.6k<br>
**Qué es:** Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `# Install directly as a Claude Code plugin
/plugin install czlonkowski/n8n-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Corregir una expresión que no encuentra un campo de entrada; Elegir nodos y validar un flujo antes de activarlo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n-mcp](human/fichas/n8n-mcp.md) · [n8n](human/fichas/n8n.md) · [Claude Code](human/fichas/claude-code.md) · [Awesome n8n Templates](human/fichas/awesome-n8n-templates.md)<br>
**Más:** [ficha completa](human/fichas/n8n-skills.md) · [GitHub](https://github.com/czlonkowski/n8n-skills)

### Apps internas y bases de datos no-code

#### 🧱 NocoDB ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 65.5k<br>
**Qué es:** Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `docker run -d \
  --name noco \
  -v "$(pwd)"/nocodb:/usr/app/data/ \
  -p 8080:8080 \
  nocodb/nocodb:latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [activepieces](human/fichas/activepieces.md) · [metabase](human/fichas/metabase.md)<br>
**Más:** [ficha completa](human/fichas/nocodb.md) · [GitHub](https://github.com/nocodb/nocodb)

#### 🧱 Appsmith
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 41.3k<br>
**Qué es:** Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.appsmith.com/getting-started/setup/installation-guides); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un panel para que soporte consulte expedientes; Construir un formulario interno que actualiza datos mediante una API — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [supabase](human/fichas/supabase.md) · [n8n](human/fichas/n8n.md) · [metabase](human/fichas/metabase.md)<br>
**Más:** [ficha completa](human/fichas/appsmith.md) · [GitHub](https://github.com/appsmithorg/appsmith)

#### 🧱 ToolJet
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 41.2k<br>
**Qué es:** Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.tooljet.com/docs/setup/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un panel interno para consultar pedidos y su estado; Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/tooljet.md) · [GitHub](https://github.com/ToolJet/ToolJet)

#### 🧱 Budibase
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 28.4k<br>
**Qué es:** Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.budibase.com); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Registrar solicitudes internas y seguir su estado; Montar un proceso que combina formulario, automatización y agente de IA — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [supabase](human/fichas/supabase.md) · [n8n](human/fichas/n8n.md) · [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/budibase.md) · [GitHub](https://github.com/Budibase/budibase)

---

## 🧠 2. Skills, plugins y métodos para agentes

Catálogos de skills, plugins y métodos generales de desarrollo. Elige según tu cliente y consulta las especialidades de diseño o negocio en su sala específica.

**⚖️ ¿Cuál elegir? — Claude Code Plugins Directory, Awesome Claude Skills, Awesome Claude Code, Agentic Awesome Skills (AAS), wshobson/agents, Awesome Agent Skills**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) | Tu objetivo encaja con estos ejemplos: Añadir una herramienta de revisión al flujo de desarrollo; Conectar un servicio mediante un plugin publicado en el marketplace oficial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Awesome Claude Skills](human/fichas/awesome-claude-skills.md) | Tu objetivo encaja con estos ejemplos: Encontrar instrucciones para revisar documentos de trabajo; Descubrir un conector para una aplicación que ya usas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Awesome Claude Code](human/fichas/awesome-claude-code.md) | Tu objetivo encaja con estos ejemplos: Encontrar ejemplos para personalizar una sesión de Claude Code; Comparar herramientas que muestran el uso del agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Agentic Awesome Skills (AAS)](human/fichas/antigravity-awesome-skills.md) | Tu objetivo encaja con estos ejemplos: Añadir una skill de brainstorming a un proyecto; Seleccionar un pequeño conjunto de instrucciones de diseño y seguridad | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [wshobson/agents](human/fichas/wshobson-agents.md) | Tu objetivo encaja con estos ejemplos: Aplicar patrones de pruebas a un módulo Python; Adaptar el mismo conjunto de agentes a otra herramienta mediante sus generadores | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Awesome Agent Skills](human/fichas/awesome-agent-skills.md) | Tu objetivo encaja con estos ejemplos: Encontrar una skill de Supabase para un proyecto existente; Localizar instrucciones de frontend publicadas por un equipo mantenedor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Agent Skills (Addy Osmani), superpowers**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Agent Skills (Addy Osmani)](human/fichas/agent-skills.md) | Tu objetivo encaja con estos ejemplos: Preparar una especificación antes de escribir una funcionalidad; Revisar un diff con criterios de calidad y pruebas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [superpowers](human/fichas/superpowers.md) | Tu objetivo encaja con estos ejemplos: Dividir una funcionalidad en tareas que se puedan verificar; Trabajar con pruebas y revisión antes de cerrar un cambio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Spec Kit, BMAD Method**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Spec Kit](human/fichas/spec-kit.md) | Tu objetivo encaja con estos ejemplos: Especificar una función con requisitos y criterios de aceptación; Mantener un flujo común en un equipo que usa agentes diferentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [BMAD Method](human/fichas/bmad-method.md) | Tu objetivo encaja con estos ejemplos: Convertir una idea de producto en un primer cambio acotado; Revisar requisitos y decisiones antes de implementar una función | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Catálogos y marketplaces de skills

#### 🗂️ Anthropic Skills ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 195k<br>
**Qué es:** Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `/plugin marketplace add anthropics/skills

/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer campos de un formulario PDF propio; Crear una presentación usando las instrucciones de la skill de diapositivas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) · [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/anthropic-skills.md) · [GitHub](https://github.com/anthropics/skills)

#### 🔌 Claude Code Plugins Directory ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 47.3k<br>
**Qué es:** Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://code.claude.com/docs/en/plugins); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir una herramienta de revisión al flujo de desarrollo; Conectar un servicio mediante un plugin publicado en el marketplace oficial — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [Awesome Claude Code](human/fichas/awesome-claude-code.md)<br>
**Más:** [ficha completa](human/fichas/claude-plugins-official.md) · [GitHub](https://github.com/anthropics/claude-plugins-official)

#### 🗂️ Awesome Claude Skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 79.5k<br>
**Qué es:** Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar instrucciones para revisar documentos de trabajo; Descubrir un conector para una aplicación que ya usas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Composio](human/fichas/composio.md) · [Claude Code](human/fichas/claude-code.md) · [SkillSpector](human/fichas/skillspector.md)<br>
**Más:** [ficha completa](human/fichas/awesome-claude-skills.md) · [GitHub](https://github.com/ComposioHQ/awesome-claude-skills)

#### ⭐ Awesome Claude Code
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 58k<br>
**Qué es:** Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/hesreallyhim/awesome-claude-code/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar ejemplos para personalizar una sesión de Claude Code; Comparar herramientas que muestran el uso del agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) · [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/awesome-claude-code.md) · [GitHub](https://github.com/hesreallyhim/awesome-claude-code)

#### 🗂️ Agentic Awesome Skills (AAS)
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 49.7k<br>
**Qué es:** Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada Antigravity Awesome Skills.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `gh skill preview sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md@v20.8.0
gh skill install sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md --agent codex --scope user --pin v20.8.0` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir una skill de brainstorming a un proyecto; Seleccionar un pequeño conjunto de instrucciones de diseño y seguridad — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [SkillSpector](human/fichas/skillspector.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/antigravity-awesome-skills.md) · [GitHub](https://github.com/sickn33/agentic-awesome-skills)

#### 🗂️ wshobson/agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 42.5k<br>
**Qué es:** Colección de plugins, agentes y skills con adaptadores documentados para Claude Code, Codex, Antigravity y otros clientes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `/plugin marketplace add wshobson/agents
/plugin install python-development@claude-code-workflows` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aplicar patrones de pruebas a un módulo Python; Adaptar el mismo conjunto de agentes a otra herramienta mediante sus generadores — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [SkillSpector](human/fichas/skillspector.md)<br>
**Más:** [ficha completa](human/fichas/wshobson-agents.md) · [GitHub](https://github.com/wshobson/agents)

#### 🗂️ Awesome GitHub Copilot
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 41.2k<br>
**Qué es:** Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub Copilot.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `copilot plugin install <plugin-name>@awesome-copilot` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir instrucciones de equipo al asistente de programación; Estudiar un agente especializado antes de adaptarlo a un proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [GitHub MCP Server](human/fichas/github-mcp-server.md) · [Spec Kit](human/fichas/spec-kit.md) · [GitHub CLI](human/fichas/cli.md)<br>
**Más:** [ficha completa](human/fichas/awesome-copilot.md) · [GitHub](https://github.com/github/awesome-copilot)

#### 🏅 Awesome Agent Skills
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 37.2k<br>
**Qué es:** Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/VoltAgent/awesome-agent-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una skill de Supabase para un proyecto existente; Localizar instrucciones de frontend publicadas por un equipo mantenedor — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [SkillSpector](human/fichas/skillspector.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/awesome-agent-skills.md) · [GitHub](https://github.com/VoltAgent/awesome-agent-skills)

#### 🎨 skills
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 24.3k<br>
**Qué es:** Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add google/skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar la configuración de un servicio Cloud en un entorno de prueba; Aprender a consultar métricas de Ads sin crear campañas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/google-skills.md) · [GitHub](https://github.com/google/skills)

#### 📂 plugins
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 16.3k<br>
**Qué es:** Especificación y colección oficial de plugins de Cursor para estudiar e instalar extensiones de ese agente.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/cursor/plugins/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una integración de un servicio que ya utiliza tu equipo; Estudiar cómo empaquetar reglas y skills para Cursor — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/plugins.md) · [GitHub](https://github.com/cursor/plugins)

#### 🧠 autoskills
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 7k<br>
**Qué es:** CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx autoskills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar skills adecuadas para un proyecto React existente; Revisar qué archivos de skills se incorporarían sin descargarlos todos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Awesome Agent Skills](human/fichas/awesome-agent-skills.md)<br>
**Más:** [ficha completa](human/fichas/autoskills.md) · [GitHub](https://github.com/midudev/autoskills)

#### 🧠 gemini-skills
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 4.5k<br>
**Qué es:** Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Interactively browse and install skills.
npx skills add google-gemini/gemini-skills --list

# Install a specific skill (e.g., gemini-api-dev).
npx skills add google-gemini/gemini-skills --skill gemini-api-dev` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar cómo integrar el SDK de Gemini en una aplicación; Preparar una llamada multimodal con datos de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/gemini-skills.md) · [GitHub](https://github.com/google-gemini/gemini-skills)

#### 🧠 awesome-agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 3k<br>
**Qué es:** Directorio de herramientas y proyectos abiertos para construir y operar agentes de inteligencia artificial.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/kyrolabs/awesome-agents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Descubrir un asistente personal que trabaja con modelos locales; Encontrar frameworks para estudiar equipos de agentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/awesome-agents.md) · [GitHub](https://github.com/kyrolabs/awesome-agents)

### Metodologías y harness para agentes de código

#### 🧭 Agent Skills (Addy Osmani) ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 118k<br>
**Qué es:** Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add addyosmani/agent-skills            # install all 25 skills
npx skills add addyosmani/agent-skills --list     # browse before installing` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una especificación antes de escribir una funcionalidad; Revisar un diff con criterios de calidad y pruebas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/agent-skills.md) · [GitHub](https://github.com/addyosmani/agent-skills)

#### 📦 skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 325k<br>
**Qué es:** Skills de ingeniería de Matt Pocock para trabajar sobre requisitos, diseño, implementación y revisión, con plugins para Claude Code y Codex.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `claude plugin install mattpocock-skills@claude-plugins-official` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar requisitos de una función antes de implementarla; Organizar una refactorización pequeña con un plan revisable — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Awesome Agent Skills](human/fichas/awesome-agent-skills.md)<br>
**Más:** [ficha completa](human/fichas/skills.md) · [GitHub](https://github.com/mattpocock/skills)

#### 💪 superpowers
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 318k<br>
**Qué es:** Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `/plugin install superpowers@claude-plugins-official` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Dividir una funcionalidad en tareas que se puedan verificar; Trabajar con pruebas y revisión antes de cerrar un cambio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Awesome Claude Code](human/fichas/awesome-claude-code.md) · [agent-toolkit](human/fichas/agent-toolkit.md)<br>
**Más:** [ficha completa](human/fichas/superpowers.md) · [GitHub](https://github.com/obra/superpowers)

#### 🌌 ECC
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🔴 pesado · ⭐ 303k<br>
**Qué es:** Sistema de skills, hooks y configuración para agentes de código, con rutas nativas y adaptadores cuya capacidad varía según el cliente.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx ecc-universal@2.2.3 setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Configurar convenciones, skills y comprobaciones para un equipo; Probar una mejora de contexto sin activar todos los componentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [OpenHands](human/fichas/openhands.md) · [sandbox](human/fichas/sandbox.md) · [hermes-agent](human/fichas/hermes-agent.md)<br>
**Más:** [ficha completa](human/fichas/ecc.md) · [GitHub](https://github.com/affaan-m/ECC)

#### 🧠 andrej-karpathy-skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 233k<br>
**Qué es:** Instrucciones para declarar supuestos, simplificar cambios y comprobar objetivos al programar, inspiradas en observaciones de Karpathy.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `/plugin marketplace add forrestchang/andrej-karpathy-skills

/plugin install andrej-karpathy-skills@karpathy-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Evitar una refactorización amplia para corregir un fallo pequeño; Hacer explícitas dudas y criterios de éxito antes de programar — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Awesome Claude Code](human/fichas/awesome-claude-code.md) · [Context-Engineering](human/fichas/context-engineering.md)<br>
**Más:** [ficha completa](human/fichas/andrej-karpathy-skills.md) · [GitHub](https://github.com/multica-ai/andrej-karpathy-skills)

#### 🧭 Ponytail
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 191k<br>
**Qué es:** Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `/plugin marketplace add DietrichGebert/ponytail

/plugin install ponytail@ponytail` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar deuda técnica y detectar código que se puede eliminar; Evaluar alternativas sencillas antes de crear una abstracción nueva — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [superpowers](human/fichas/superpowers.md) · [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md)<br>
**Más:** [ficha completa](human/fichas/ponytail.md) · [GitHub](https://github.com/DietrichGebert/ponytail)

#### 🧭 Spec Kit
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 150k<br>
**Qué es:** Kit de GitHub para desarrollo guiado por especificaciones con agentes de código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.github.io/spec-kit/installation.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Especificar una función con requisitos y criterios de aceptación; Mantener un flujo común en un equipo que usa agentes diferentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [Gemini CLI](human/fichas/gemini-cli.md)<br>
**Más:** [ficha completa](human/fichas/spec-kit.md) · [GitHub](https://github.com/github/spec-kit)

#### 🎨 gstack
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 142k<br>
**Qué es:** Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host auto      # or: ./setup --host codex
./setup --status                         # one row per install: host, tier, scope, version, path` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una revisión de producto antes de implementar; Abrir un navegador de prueba para revisar una interfaz propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/gstack.md) · [GitHub](https://github.com/garrytan/gstack)

#### 🧭 BMAD Method
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 55.4k<br>
**Qué es:** Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add bmad-code-org/BMAD-METHOD/skills/core-tools --skill '*'
npx skills add bmad-code-org/BMAD-METHOD/skills/method --skill '*'` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir una idea de producto en un primer cambio acotado; Revisar requisitos y decisiones antes de implementar una función — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/bmad-method.md) · [GitHub](https://github.com/bmad-code-org/BMAD-METHOD)

#### 🎨 book-to-skill
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 37.9k<br>
**Qué es:** Herramientas para convertir un libro técnico en PDF en una skill que un agente pueda consultar durante el trabajo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `# One command, any host — via the cross-agent skills CLI:
npx skills add virgiliojr94/book-to-skill` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una guía de consulta a partir de documentación interna; Convertir notas técnicas propias en instrucciones reutilizables del agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/book-to-skill.md) · [GitHub](https://github.com/virgiliojr94/book-to-skill)

#### 🧠 codex-plugin-cc
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 35.1k<br>
**Qué es:** Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `/plugin marketplace add openai/codex-plugin-cc

/plugin install codex@openai-codex` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Pedir una segunda revisión de un cambio desde Claude Code; Delegar una tarea acotada a Codex manteniendo el contexto principal — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/codex-plugin-cc.md) · [GitHub](https://github.com/openai/codex-plugin-cc)

#### 🧠 SuperClaude_Framework
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 23.9k<br>
**Qué es:** Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Install from PyPI
pipx install superclaude

# Install commands (installs all 30 slash commands)
superclaude install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Usar un rol especializado para revisar una decisión de arquitectura; Organizar un flujo de desarrollo con comandos de trabajo coherentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/superclaude-framework.md) · [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework)

#### 🎨 elephant-goldfish-model
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 19.3k<br>
**Qué es:** Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complementarias.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `claude plugin marketplace add google/elephant-goldfish-model
claude plugin install egm@egm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar alternativas para una funcionalidad antes de elegir una; Revisar una especificación con un contexto de lectura renovado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/elephant-goldfish-model.md) · [GitHub](https://github.com/google/elephant-goldfish-model)

#### 🧠 claude-token-efficient
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 6.2k<br>
**Qué es:** Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `git clone https://github.com/drona23/claude-token-efficient
cp claude-token-efficient/profiles/CLAUDE.coding.md your-project/CLAUDE.md` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir respuestas repetitivas en una sesión larga; Mantener un estilo de comunicación conciso para tareas de código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-token-efficient.md) · [GitHub](https://github.com/drona23/claude-token-efficient)

#### 📂 claude-code-hooks-mastery
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 4k<br>
**Qué es:** Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de trabajo.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/disler/claude-code-hooks-mastery/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Registrar cuándo empieza y termina una sesión de trabajo; Comprender un control que revisa una acción antes de ejecutarla — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-code-hooks-mastery.md) · [GitHub](https://github.com/disler/claude-code-hooks-mastery)

#### 🧰 agent-toolkit
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 2.7k<br>
**Qué es:** Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add softaworks/agent-toolkit` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aclarar una petición ambigua antes de programar; Documentar el contrato entre frontend y backend — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/agent-toolkit.md) · [GitHub](https://github.com/softaworks/agent-toolkit)

#### 🧠 grok-plugin-claude-code
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 30<br>
**Qué es:** Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar.<br>
**Acceso:** API: por confirmar · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `/plugin marketplace add zachdunn/grok-plugin-claude-code
/plugin install grok-cc@grok-plugin-claude-code` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Solicitar una segunda opinión sobre un cambio pequeño usando Grok; Delegar una tarea acotada desde una sesión de Claude Code — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/grok-plugin-claude-code.md) · [GitHub](https://github.com/zachdunn/grok-plugin-claude-code)

---

## 🕸️ 3. Construir agentes y coordinar equipos de IA

Frameworks, builders visuales y experimentos de coordinación. Separa la base técnica que integras del asistente listo que utilizas para una tarea.

**⚖️ ¿Cuál elegir? — LangGraph, MetaGPT, crewAI, Agno, Deep Agents, OpenAI Agents SDK, smolagents**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [LangGraph](human/fichas/langgraph.md) | Tu objetivo encaja con estos ejemplos: Pausar una devolución hasta su revisión; Retomar una investigación interrumpida | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [MetaGPT](human/fichas/metagpt.md) | Tu objetivo encaja con estos ejemplos: Bocetar requisitos de una app; Simular roles de un equipo de software | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [crewAI](human/fichas/crewai.md) | Tu objetivo encaja con estos ejemplos: Preparar investigación de mercado; Separar investigación y redacción de producto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Agno](human/fichas/agno.md) | Tu objetivo encaja con estos ejemplos: Servir un agente mediante una API; Investigar fallos mediante trazas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Deep Agents](human/fichas/deepagents.md) | Tu objetivo encaja con estos ejemplos: Resumir documentos de proyecto; Dividir una revisión de archivos en tareas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [OpenAI Agents SDK](human/fichas/openai-agents-python.md) | Tu objetivo encaja con estos ejemplos: Enrutar consultas por departamento; Validar una respuesta antes de aceptarla | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [smolagents](human/fichas/smolagents.md) | Tu objetivo encaja con estos ejemplos: Calcular indicadores de un CSV; Transformar datos consultados en un resumen | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — langchain, LlamaIndex, Haystack**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [langchain](human/fichas/langchain.md) | Tu objetivo encaja con estos ejemplos: Consultar un catálogo de prueba; Responder sobre documentos propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LlamaIndex](human/fichas/llama-index.md) | Tu objetivo encaja con estos ejemplos: Consultar políticas internas; Encontrar cláusulas en contratos ficticios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Haystack](human/fichas/haystack.md) | Tu objetivo encaja con estos ejemplos: Responder sobre manuales propios; Comparar recuperación de dos consultas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Mastra, AI SDK (Vercel), LangGraph.js**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Mastra](human/fichas/mastra.md) | Tu objetivo encaja con estos ejemplos: Añadir un agente a una app TypeScript; Pausar y reanudar un flujo de aprobación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [AI SDK (Vercel)](human/fichas/vercel-ai.md) | Tu objetivo encaja con estos ejemplos: Construir una interfaz de chat; Extraer datos tipados de un mensaje | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LangGraph.js](human/fichas/langgraphjs.md) | Tu objetivo encaja con estos ejemplos: Controlar aprobación de una solicitud; Reanudar un agente en una app JavaScript | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Sim, AutoGPT, dify, langflow**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Sim](human/fichas/sim.md) | Tu objetivo encaja con estos ejemplos: Automatizar una clasificación de mensajes; Probar un flujo con Ollama antes de usar una API | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [AutoGPT](human/fichas/autogpt.md) | Tu objetivo encaja con estos ejemplos: Procesar solicitudes recurrentes; Componer una investigación con revisión humana | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [dify](human/fichas/dify.md) | Tu objetivo encaja con estos ejemplos: Crear un asistente sobre políticas; Diseñar un workflow visual de clasificación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [langflow](human/fichas/langflow.md) | Tu objetivo encaja con estos ejemplos: Prototipar un agente visual; Exponer un flujo como herramienta MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Frameworks de agentes en Python

#### 🐍 LangGraph ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 45k<br>
**Qué es:** Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -U langgraph` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Pausar una devolución hasta su revisión; Retomar una investigación interrumpida — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/langgraph.md) · [GitHub](https://github.com/langchain-ai/langgraph)

#### 🦜 langchain
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 150k<br>
**Qué es:** Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas).<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv add langchain` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar un catálogo de prueba; Responder sobre documentos propios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langflow](human/fichas/langflow.md) · [langfuse](human/fichas/langfuse.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/langchain.md) · [GitHub](https://github.com/langchain-ai/langchain)

#### 🕸️ MetaGPT
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 71.3k<br>
**Qué es:** Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install --upgrade metagpt
# or `pip install --upgrade git+https://github.com/geekan/MetaGPT.git`
# or `git clone https://github.com/geekan/MetaGPT && cd MetaGPT && pip install --upgrade -e .`` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Bocetar requisitos de una app; Simular roles de un equipo de software — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/metagpt.md) · [GitHub](https://github.com/FoundationAgents/MetaGPT)

#### 👥 crewAI
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 60.9k<br>
**Qué es:** Framework para orquestar "crews" de agentes con roles y tareas.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv tool install crewai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar investigación de mercado; Separar investigación y redacción de producto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [mem0](human/fichas/mem0.md)<br>
**Más:** [ficha completa](human/fichas/crewai.md) · [GitHub](https://github.com/crewAIInc/crewAI)

#### 🐍 LlamaIndex
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 52.9k<br>
**Qué es:** Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# custom selection of integrations to work with core
pip install llama-index-core
pip install llama-index-llms-openai
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar políticas internas; Encontrar cláusulas en contratos ficticios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [Docling](human/fichas/docling.md) · [Ragas](human/fichas/ragas.md)<br>
**Más:** [ficha completa](human/fichas/llama-index.md) · [GitHub](https://github.com/run-llama/llama_index)

#### 🐍 Agno
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 43.2k<br>
**Qué es:** Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.agno.com/agent-platform/overview); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un agente mediante una API; Investigar fallos mediante trazas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [mem0](human/fichas/mem0.md)<br>
**Más:** [ficha completa](human/fichas/agno.md) · [GitHub](https://github.com/agno-agi/agno)

#### 🐍 DSPy
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 39.1k<br>
**Qué es:** Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install dspy` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar solicitudes de soporte; Optimizar un extractor de datos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ragas](human/fichas/ragas.md) · [MLflow](human/fichas/mlflow.md)<br>
**Más:** [ficha completa](human/fichas/dspy.md) · [GitHub](https://github.com/stanfordnlp/dspy)

#### 🐍 Deep Agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 31.3k<br>
**Qué es:** Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv add deepagents` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Resumir documentos de proyecto; Dividir una revisión de archivos en tareas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/deepagents.md) · [GitHub](https://github.com/langchain-ai/deepagents)

#### 🐍 OpenAI Agents SDK
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.7k<br>
**Qué es:** SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv init
uv add openai-agents` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Enrutar consultas por departamento; Validar una respuesta antes de aceptarla — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [openai-python](human/fichas/openai-python.md) · [FastMCP](human/fichas/fastmcp.md)<br>
**Más:** [ficha completa](human/fichas/openai-agents-python.md) · [GitHub](https://github.com/openai/openai-agents-python)

#### 🐍 smolagents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.4k<br>
**Qué es:** Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install "smolagents[toolkit]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Calcular indicadores de un CSV; Transformar datos consultados en un resumen — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [E2B](human/fichas/e2b.md) · [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/smolagents.md) · [GitHub](https://github.com/huggingface/smolagents)

#### 🐍 Haystack
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 27k<br>
**Qué es:** Framework de deepset para pipelines de RAG y agentes listos para producción.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install haystack-ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Responder sobre manuales propios; Comparar recuperación de dos consultas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/haystack.md) · [GitHub](https://github.com/deepset-ai/haystack)

#### 🐍 Agent Development Kit (ADK)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 22.2k<br>
**Qué es:** Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install google-adk` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar información de negocio; Evaluar la selección de herramientas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Gemini CLI](human/fichas/gemini-cli.md) · [FastMCP](human/fichas/fastmcp.md)<br>
**Más:** [ficha completa](human/fichas/adk-python.md) · [GitHub](https://github.com/google/adk-python)

#### 🐍 Pydantic AI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 21.2k<br>
**Qué es:** Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv add pydantic-ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer campos de mensajes; Validar datos generados antes de guardarlos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langfuse](human/fichas/langfuse.md) · [FastMCP](human/fichas/fastmcp.md)<br>
**Más:** [ficha completa](human/fichas/pydantic-ai.md) · [GitHub](https://github.com/pydantic/pydantic-ai)

#### 📚 claude-agent-sdk-python
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 8.5k<br>
**Qué es:** SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `pip install claude-agent-sdk` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Integrar revisión de archivos en una aplicación; Conservar sesiones de un agente propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-agent-sdk-python.md) · [GitHub](https://github.com/anthropics/claude-agent-sdk-python)

#### 🤝 ag2
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 5.1k<br>
**Qué es:** AG2 v1 utiliza import ag2 y su propia arquitectura de agentes y redes. Los proyectos con ConversableAgent, GroupChat e import autogen deben seguir la distribución ag2-classic y su documentación de migración.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install ag2[openai]` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Coordinar redactor y verificador; Incluir intervención humana en un equipo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/ag2.md) · [GitHub](https://github.com/ag2ai/ag2)

#### 🕸️ awesome-LangGraph
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 2k<br>
**Qué es:** Repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/vonzosten/awesome-LangGraph/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar un flujo con memoria; Localizar evaluadores de agentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/awesome-langgraph.md) · [GitHub](https://github.com/vonzosten/awesome-LangGraph)

### Frameworks en TypeScript y multi-lenguaje

#### 🟦 Mastra ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 29.5k<br>
**Qué es:** Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm create mastra@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir un agente a una app TypeScript; Pausar y reanudar un flujo de aprobación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [CopilotKit](human/fichas/copilotkit.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/mastra.md) · [GitHub](https://github.com/mastra-ai/mastra)

#### 🟦 AI SDK (Vercel)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 28k<br>
**Qué es:** Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una interfaz de chat; Extraer datos tipados de un mensaje — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ui](human/fichas/ui.md) · [assistant-ui](human/fichas/assistant-ui.md)<br>
**Más:** [ficha completa](human/fichas/vercel-ai.md) · [GitHub](https://github.com/vercel/ai)

#### 🟦 Microsoft Agent Framework
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 14.7k<br>
**Qué es:** Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install agent-framework
# This installs the standard package set; install `agent-framework-lab` separately for experimental modules.
# It may take a minute on first install on Windows.` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Migrar una prueba de Semantic Kernel; Coordinar especialistas con un flujo explícito — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/agent-framework.md) · [GitHub](https://github.com/microsoft/agent-framework)

#### 🕸️ langchain4j
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 13.4k<br>
**Qué es:** Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.langchain4j.dev/get-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir IA a Spring Boot; Recuperar documentos desde una aplicación JVM — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/langchain4j.md) · [GitHub](https://github.com/langchain4j/langchain4j)

#### 🟦 LangGraph.js
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 3.4k<br>
**Qué es:** Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install @langchain/langgraph @langchain/core` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Controlar aprobación de una solicitud; Reanudar un agente en una app JavaScript — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/langgraphjs.md) · [GitHub](https://github.com/langchain-ai/langgraphjs)

### Builders visuales y plataformas de agentes

#### 🧩 Sim ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.1k<br>
**Qué es:** Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx sim-setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar una clasificación de mensajes; Probar un flujo con Ollama antes de usar una API — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/sim.md) · [GitHub](https://github.com/simstudioai/sim)

#### 🧩 AutoGPT
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 188k<br>
**Qué es:** Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run -d \
  --name autogpt \
  --restart unless-stopped \
  --shm-size 2g \
  --ulimit nofile=65536:65536 \
  --log-driver json-file \
  --log-opt max-size=50m \
  --log-opt max-file=5 \
  -p 127.0.0.1:3000:3000 \
  -e AUTOGPT_PUBLIC_URL=http://localhost:3000 \
  -v autogpt-data:/data \
  significantgravitas/autogpt:latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Procesar solicitudes recurrentes; Componer una investigación con revisión humana — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/autogpt.md) · [GitHub](https://github.com/Significant-Gravitas/AutoGPT)

#### 🧱 dify
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 161k<br>
**Qué es:** Plataforma integral para construir apps de IA con backend y UI listos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/langgenius/dify/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un asistente sobre políticas; Diseñar un workflow visual de clasificación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langflow](human/fichas/langflow.md)<br>
**Más:** [ficha completa](human/fichas/dify.md) · [GitHub](https://github.com/langgenius/dify)

#### 🔗 langflow
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 157k<br>
**Qué es:** Constructor visual de flujos LLM/agentes construido sobre LangChain.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv pip install langflow -U

uv run langflow run` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un agente visual; Exponer un flujo como herramienta MCP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [dify](human/fichas/dify.md)<br>
**Más:** [ficha completa](human/fichas/langflow.md) · [GitHub](https://github.com/langflow-ai/langflow)

### Simulación, evolución y debate entre modelos

#### 🐟 MiroFish ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 85.6k<br>
**Qué es:** Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `# 1. Configure environment variables (same as source deployment)
cp .env.example .env

# 2. Pull image and start
docker compose up -d` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar reacciones hipotéticas a un anuncio; Comparar escenarios narrativos antes de investigar datos reales — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [openevolve](human/fichas/openevolve.md)<br>
**Más:** [ficha completa](human/fichas/mirofish.md) · [GitHub](https://github.com/666ghj/MiroFish)

#### 🏛️ llm-council
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 26.5k<br>
**Qué es:** "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `uv sync

cd frontend
npm install
cd ..` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar explicaciones de un concepto; Revisar opciones para una decisión técnica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/llm-council.md) · [GitHub](https://github.com/karpathy/llm-council)

#### 🧬 openevolve
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 7.8k<br>
**Qué es:** Agente de codificación evolutivo que optimiza algoritmos por simulación genética.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/algorithmicsuperintelligence/openevolve.git
cd openevolve
pip install -e .` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Optimizar una función medible; Buscar mejores reglas de ordenación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [llm-council](human/fichas/llm-council.md)<br>
**Más:** [ficha completa](human/fichas/openevolve.md) · [GitHub](https://github.com/algorithmicsuperintelligence/openevolve)

#### 🕸️ hermes-agent-self-evolution
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 5.7k<br>
**Qué es:** Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `# Install
git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
cd hermes-agent-self-evolution
pip install -e ".[dev]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Refinar una skill de revisión de código; Comparar instrucciones con fallos observados — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [hermes-agent](human/fichas/hermes-agent.md)<br>
**Más:** [ficha completa](human/fichas/hermes-agent-self-evolution.md) · [GitHub](https://github.com/NousResearch/hermes-agent-self-evolution)

#### 📚 jev-fraud
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 17<br>
**Qué es:** Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/Nutlope/jev-fraud.git
   cd jev-fraud
   npm install
   cp .env.example .env.local

npm run dev -- --port 3017` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar clasificación con escalado de casos inciertos; Comparar confianza y aciertos sobre un conjunto ficticio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/jev-fraud.md) · [GitHub](https://github.com/Nutlope/jev-fraud)

---

## 🕷️ 4. Buscar, extraer y monitorear información web

Buscadores, crawlers, extracción y seguimiento de páginas o redes. Para hacer clic y operar interfaces utiliza la sala de navegadores y automatización web.

**⚖️ ¿Cuál elegir? — firecrawl, crawl4ai, Jina Reader**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [firecrawl](human/fichas/firecrawl.md) | Tu objetivo encaja con estos ejemplos: Preparar páginas para un buscador documental; Crear un mapa de URLs de una web propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [crawl4ai](human/fichas/crawl4ai.md) | Tu objetivo encaja con estos ejemplos: Preparar artículos para RAG; Extraer datos estructurados con un modelo local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Jina Reader](human/fichas/jina-reader.md) | Tu objetivo encaja con estos ejemplos: Convertir un artículo a texto para consulta; Preparar una página para un índice documental | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Scrapegraph-ai, Maxun, llm-scraper**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Scrapegraph-ai](human/fichas/scrapegraph-ai.md) | Tu objetivo encaja con estos ejemplos: Extraer fichas de productos; Transformar artículos en registros estructurados | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Maxun](human/fichas/maxun.md) | Tu objetivo encaja con estos ejemplos: Convertir un listado en datos consultables; Monitorear cambios de un catálogo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [llm-scraper](human/fichas/llm-scraper.md) | Tu objetivo encaja con estos ejemplos: Extraer campos sin escribir selectores específicos; Normalizar información de páginas similares | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Crawlers y extracción para IA

#### 🔥 firecrawl ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 202k<br>
**Qué es:** Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx -y firecrawl-cli@latest init --all --browser` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar páginas para un buscador documental; Crear un mapa de URLs de una web propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [crawl4ai](human/fichas/crawl4ai.md)<br>
**Más:** [ficha completa](human/fichas/firecrawl.md) · [GitHub](https://github.com/firecrawl/firecrawl)

#### 🩹 Scrapling
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 103k<br>
**Qué es:** Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install "scrapling[fetchers]"
<br>
    scrapling install           # normal install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Recopilar un catálogo público permitido; Extraer texto para un índice de búsqueda — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [scrapy](human/fichas/scrapy.md)<br>
**Más:** [ficha completa](human/fichas/scrapling.md) · [GitHub](https://github.com/D4Vinci/Scrapling)

#### 🕷️ crawl4ai
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 87.4k<br>
**Qué es:** Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -U crawl4ai
crawl4ai-setup        # installs the browser, once` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar artículos para RAG; Extraer datos estructurados con un modelo local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/crawl4ai.md) · [GitHub](https://github.com/unclecode/crawl4ai)

#### 🐍 scrapy
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 65.4k<br>
**Qué es:** Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install scrapy` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Recopilar listados públicos permitidos; Programar extracción repetible con pipelines — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [crawlee-python](human/fichas/crawlee-python.md)<br>
**Más:** [ficha completa](human/fichas/scrapy.md) · [GitHub](https://github.com/scrapy/scrapy)

#### 🦗 crawlee
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 26.4k<br>
**Qué es:** Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx crawlee create my-crawler` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Rastrear una documentación propia; Extraer datos de páginas con JavaScript — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/crawlee.md) · [GitHub](https://github.com/apify/crawlee)

#### 🕷️ Jina Reader
**Etiquetas:** Ejecución ☁️ cloud/API · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 12.3k<br>
**Qué es:** Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run --rm -p 3000:8081 ghcr.io/jina-ai/reader:oss
# then: curl http://localhost:3000/https://example.com` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un artículo a texto para consulta; Preparar una página para un índice documental — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/jina-reader.md) · [GitHub](https://github.com/jina-ai/reader)

#### 📚 defuddle
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 10k<br>
**Qué es:** Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install defuddle` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar artículos para lectura; Limpiar HTML antes de indexarlo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/defuddle.md) · [GitHub](https://github.com/kepano/defuddle)

#### 🦗 crawlee-python
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 9.7k<br>
**Qué es:** Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `python -m pip install 'crawlee[all]'` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Recopilar documentos públicos; Crear un crawler con reintentos y exportación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [scrapy](human/fichas/scrapy.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/crawlee-python.md) · [GitHub](https://github.com/apify/crawlee-python)

#### 🕷️ awesome-web-scraping
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 8.2k<br>
**Qué es:** Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/lorien/awesome-web-scraping/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar un parser para Python; Encontrar herramientas de extracción para JavaScript — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/awesome-web-scraping.md) · [GitHub](https://github.com/lorien/awesome-web-scraping)

### Scraping guiado por LLM

#### 🕸️ Scrapegraph-ai ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 32.8k<br>
**Qué es:** Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install scrapegraphai

# IMPORTANT (for fetching websites content)
playwright install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer fichas de productos; Transformar artículos en registros estructurados — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [crawl4ai](human/fichas/crawl4ai.md) · [graphrag](human/fichas/graphrag.md)<br>
**Más:** [ficha completa](human/fichas/scrapegraph-ai.md) · [GitHub](https://github.com/ScrapeGraphAI/Scrapegraph-ai)

#### 🧠 Maxun
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.4k<br>
**Qué es:** Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.maxun.dev/installation/docker); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un listado en datos consultables; Monitorear cambios de un catálogo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/maxun.md) · [GitHub](https://github.com/getmaxun/maxun)

#### 🧾 llm-scraper
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 7k<br>
**Qué es:** Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm i zod playwright llm-scraper` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer campos sin escribir selectores específicos; Normalizar información de páginas similares — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [playwright](human/fichas/playwright.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/llm-scraper.md) · [GitHub](https://github.com/mishushakov/llm-scraper)

### Búsqueda, monitoreo y research web

#### 🔍 SearXNG ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 39.6k<br>
**Qué es:** Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://docs.searxng.org/admin/installation.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir búsqueda a una herramienta de investigación; Disponer de un metabuscador propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [Open WebUI](human/fichas/open-webui.md) · [Vane](human/fichas/vane.md)<br>
**Más:** [ficha completa](human/fichas/searxng.md) · [GitHub](https://github.com/searxng/searxng)

#### 🔍 Agent-Reach
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 112k<br>
**Qué es:** CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Leer una discusión pública para investigación; Obtener transcripciones de un video permitido — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [last30days](human/fichas/last30days-skill.md)<br>
**Más:** [ficha completa](human/fichas/agent-reach.md) · [GitHub](https://github.com/Panniantong/Agent-Reach)

#### 🔍 last30days
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 67.7k<br>
**Qué es:** Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una reunión sobre una empresa; Revisar novedades de una herramienta — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Agent-Reach](human/fichas/agent-reach.md)<br>
**Más:** [ficha completa](human/fichas/last30days-skill.md) · [GitHub](https://github.com/mvanhorn/last30days-skill)

#### 🔍 Vane
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 38.2k<br>
**Qué es:** Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica).<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Investigar un tema con citas; Consultar la web usando Ollama — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [SearXNG](human/fichas/searxng.md) · [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/vane.md) · [GitHub](https://github.com/ItzCrazyKns/Vane)

#### 🔍 changedetection.io
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 35.8k<br>
**Qué es:** Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run -d --restart always -p "127.0.0.1:5000:5000" -v datastore-volume:/datastore --name changedetection.io docker.io/dgtlmoon/changedetection.io` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Detectar cambios de precio permitidos; Monitorear avisos de una página — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/changedetection.md) · [GitHub](https://github.com/dgtlmoon/changedetection.io)

#### 🔍 ArchiveBox
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 29k<br>
**Qué es:** Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ArchiveBox/ArchiveBox/wiki/Quickstart); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preservar documentación que cambia; Crear una biblioteca de fuentes de una investigación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md)<br>
**Más:** [ficha completa](human/fichas/archivebox.md) · [GitHub](https://github.com/ArchiveBox/ArchiveBox)

### Redes sociales y descarga de medios

#### 📱 yt-dlp ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 208k<br>
**Qué es:** Descargador de audio y video por línea de comandos compatible con miles de sitios.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/yt-dlp/yt-dlp/wiki/Installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Respaldar videos propios; Obtener medios permitidos para edición — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [whisperX](human/fichas/whisperx.md) · [FFmpeg](human/fichas/ffmpeg.md) · [Fabric](human/fichas/fabric.md)<br>
**Más:** [ficha completa](human/fichas/yt-dlp.md) · [GitHub](https://github.com/yt-dlp/yt-dlp)

#### 📸 instaloader
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13.9k<br>
**Qué es:** Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip3 install instaloader` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Respaldar publicaciones propias; Actualizar una colección autorizada sin repetir todo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/instaloader.md) · [GitHub](https://github.com/instaloader/instaloader)

---

## 🔌 5. Conectar herramientas con MCP

SDKs, servidores, clientes y directorios MCP. Un servidor aporta acciones o datos; el modelo y su acceso pertenecen al cliente que lo utiliza.

**⚖️ ¿Cuál elegir? — FastMCP, MCP Python SDK**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [FastMCP](human/fichas/fastmcp.md) | Tu objetivo encaja con estos ejemplos: Exponer una función de inventario como herramienta; Probar autenticación de un servidor propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [MCP Python SDK](human/fichas/mcp-python-sdk.md) | Tu objetivo encaja con estos ejemplos: Conectar una función Python a MCP; Servir un recurso de texto desde una aplicación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — MCP TypeScript SDK, mcp-use**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [MCP TypeScript SDK](human/fichas/mcp-typescript-sdk.md) | Tu objetivo encaja con estos ejemplos: Construir un servidor MCP en TypeScript; Crear un cliente que enumere herramientas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [mcp-use](human/fichas/mcp-use.md) | Tu objetivo encaja con estos ejemplos: Construir una herramienta con interfaz embebida; Desplegar un servidor MCP para una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Playwright MCP, Chrome DevTools MCP**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Playwright MCP](human/fichas/playwright-mcp.md) | Tu objetivo encaja con estos ejemplos: Probar una navegación de tu app; Inspeccionar un formulario de desarrollo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Chrome DevTools MCP](human/fichas/chrome-devtools-mcp.md) | Tu objetivo encaja con estos ejemplos: Diagnosticar una pantalla que falla; Inspeccionar rendimiento de una página propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### SDKs y frameworks para crear MCP

#### 🧰 FastMCP ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 28.5k<br>
**Qué es:** La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `uv add fastmcp` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Exponer una función de inventario como herramienta; Probar autenticación de un servidor propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/fastmcp.md) · [GitHub](https://github.com/PrefectHQ/fastmcp)

#### 🧰 MCP TypeScript SDK ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13.8k<br>
**Qué es:** SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install @modelcontextprotocol/server` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un servidor MCP en TypeScript; Crear un cliente que enumere herramientas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md)<br>
**Más:** [ficha completa](human/fichas/mcp-typescript-sdk.md) · [GitHub](https://github.com/modelcontextprotocol/typescript-sdk)

#### 🧰 MCP Python SDK
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 24.9k<br>
**Qué es:** SDK oficial de Python para crear servidores y clientes del Model Context Protocol.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `uv add "mcp[cli]"      # or: pip install "mcp[cli]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar una función Python a MCP; Servir un recurso de texto desde una aplicación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [MCP Inspector](human/fichas/mcp-inspector.md)<br>
**Más:** [ficha completa](human/fichas/mcp-python-sdk.md) · [GitHub](https://github.com/modelcontextprotocol/python-sdk)

#### 🧰 MCP Inspector
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 11.3k<br>
**Qué es:** Herramienta oficial para probar y depurar servidores MCP desde una interfaz web.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx @modelcontextprotocol/inspector                   # web UI (default)` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar un esquema MCP; Reproducir un fallo de una herramienta — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [FastMCP](human/fichas/fastmcp.md) · [MCP TypeScript SDK](human/fichas/mcp-typescript-sdk.md)<br>
**Más:** [ficha completa](human/fichas/mcp-inspector.md) · [GitHub](https://github.com/modelcontextprotocol/inspector)

#### 🛠️ mcp-use
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 11k<br>
**Qué es:** Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx -y create-mcp-use-app@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una herramienta con interfaz embebida; Desplegar un servidor MCP para una app propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Google MCP](human/fichas/mcp.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/mcp-use.md) · [GitHub](https://github.com/mcp-use/mcp-use)

### Servidores MCP destacados

#### 🔌 Context7 ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 64.8k<br>
**Qué es:** Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx ctx7 setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar APIs recientes durante programación; Evitar mezclar instrucciones de versiones distintas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Cline](human/fichas/cline.md) · [OpenCode](human/fichas/opencode.md)<br>
**Más:** [ficha completa](human/fichas/context7.md) · [GitHub](https://github.com/upstash/context7)

#### 🔌 Playwright MCP ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 39.7k<br>
**Qué es:** Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `claude mcp add playwright npx @playwright/mcp@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar una navegación de tu app; Inspeccionar un formulario de desarrollo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/playwright-mcp.md) · [GitHub](https://github.com/microsoft/playwright-mcp)

#### 📚 servers
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 92k<br>
**Qué es:** Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/modelcontextprotocol/servers/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender cómo se implementa memoria MCP; Estudiar acceso a un repositorio Git de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/servers.md) · [GitHub](https://github.com/modelcontextprotocol/servers)

#### 🔌 Chrome DevTools MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 56.3k<br>
**Qué es:** Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diagnosticar una pantalla que falla; Inspeccionar rendimiento de una página propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/chrome-devtools-mcp.md) · [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)

#### 🔌 GitHub MCP Server
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 34.5k<br>
**Qué es:** Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/github/github-mcp-server/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una base de código; Revisar el estado de una pull request — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/github-mcp-server.md) · [GitHub](https://github.com/github/github-mcp-server)

#### 🔌 Blender MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 34.5k<br>
**Qué es:** Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `winget install --id=astral-sh.uv -e
uvx mcp-for-blender setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Bocetar una escena 3D; Automatizar ajustes de objetos y materiales — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/blender-mcp.md) · [GitHub](https://github.com/ahujasid/mcp-for-blender)

#### 🔌 Serena
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 31.4k<br>
**Qué es:** Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv tool install -p 3.13 serena-agent` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Navegar una base de código grande; Refactorizar un símbolo con contexto semántico — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/serena.md) · [GitHub](https://github.com/oraios/serena)

#### 🔌 Figma Context MCP
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 16.2k<br>
**Qué es:** Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/GLips/Figma-Context-MCP/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Implementar una tarjeta a partir de un diseño; Consultar tipografía y espaciado de una pantalla — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [ui](human/fichas/ui.md) · [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/figma-context-mcp.md) · [GitHub](https://github.com/GLips/Figma-Context-MCP)

#### 🧩 unity-mcp
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 16k<br>
**Qué es:** Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/CoplayDev/unity-mcp/blob/beta/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Bocetar escenas de una demo; Ejecutar pruebas del proyecto desde un agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [blender](human/fichas/blender.md)<br>
**Más:** [ficha completa](human/fichas/unity-mcp.md) · [GitHub](https://github.com/CoplayDev/unity-mcp)

#### 🧩 GhidraMCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 11.9k<br>
**Qué es:** Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP ghidra-mcp --ghidra-server http://127.0.0.1:8080/` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar funciones de un binario propio; Estudiar llamadas en un ejecutable de laboratorio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ghidra](human/fichas/ghidra.md)<br>
**Más:** [ficha completa](human/fichas/ghidramcp.md) · [GitHub](https://github.com/LaurieWired/GhidraMCP)

#### 🧩 treg
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 8k<br>
**Qué es:** Registro y conexión de herramientas para agentes que organiza acceso a servicios, cuentas y credenciales de proveedores.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `/plugin marketplace add superdesigndev/treg
/plugin install treg@treg` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar datos para una investigación comercial; Compartir herramientas de un equipo sin pegar sus claves en el chat — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/treg.md) · [GitHub](https://github.com/superdesigndev/treg)

#### 🔌 annas-mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 1.1k<br>
**Qué es:** Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/iosifache/annas-mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Localizar un documento de dominio público; Estudiar una interfaz de búsqueda documental MCP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/annas-mcp.md) · [GitHub](https://github.com/iosifache/annas-mcp)

#### 🕸️ mcp-neo4j
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 989<br>
**Qué es:** Colección del programa Neo4j Labs, mantenida por el equipo Field GenAI, con servidores para Cypher, memoria, modelado y Aura. Los autores advierten que no tiene SLA ni garantías de compatibilidad del equipo de producto y enlazan un repositorio distinto para el servidor oficial de producto.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar relaciones en un grafo; Estudiar memoria de entidades entre sesiones — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [graphrag](human/fichas/graphrag.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/mcp-neo4j.md) · [GitHub](https://github.com/neo4j-contrib/mcp-neo4j)

### Directorios, clientes y aprendizaje

#### 📚 MCP for Beginners ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 17.7k<br>
**Qué es:** Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/mcp-for-beginners/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender conceptos MCP desde cero; Comparar un servidor Python con otro TypeScript — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [FastMCP](human/fichas/fastmcp.md) · [MCP Inspector](human/fichas/mcp-inspector.md)<br>
**Más:** [ficha completa](human/fichas/mcp-for-beginners.md) · [GitHub](https://github.com/microsoft/mcp-for-beginners)

#### 🌍 public-apis
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 499k<br>
**Qué es:** Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/public-apis/public-apis/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar datos de clima para una demo; Comparar APIs públicas de geocodificación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/public-apis.md) · [GitHub](https://github.com/public-apis/public-apis)

#### 🗂️ awesome-mcp-servers
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 97.7k<br>
**Qué es:** Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/punkpeye/awesome-mcp-servers/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar una conexión a archivos propios; Encontrar un servidor para una base de datos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [servers](human/fichas/servers.md)<br>
**Más:** [ficha completa](human/fichas/awesome-mcp-servers.md) · [GitHub](https://github.com/punkpeye/awesome-mcp-servers)

#### 📚 Awesome MCP Clients
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 6.6k<br>
**Qué es:** Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/punkpeye/awesome-mcp-clients/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una interfaz para herramientas MCP; Comparar clientes con modelos locales — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/awesome-mcp-clients.md) · [GitHub](https://github.com/punkpeye/awesome-mcp-clients)

#### 🧩 Google MCP
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 4.7k<br>
**Qué es:** Reúne servidores MCP de servicios Google y ejemplos de despliegue. Sirve para elegir una conexión y revisar sus credenciales y costes. No es el repositorio de la especificación general de MCP.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/google/mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar un servicio Google a un agente; Aprender a alojar un servidor MCP en Cloud Run — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [mcp-use](human/fichas/mcp-use.md) · [servers](human/fichas/servers.md)<br>
**Más:** [ficha completa](human/fichas/mcp.md) · [GitHub](https://github.com/google/mcp)

---

## 🧬 6. Memoria, RAG y búsqueda de conocimiento

Memoria persistente, sistemas RAG y bases vectoriales. La memoria mantiene contexto; RAG recupera documentos; una base vectorial almacena el índice de búsqueda.

**⚖️ ¿Cuál elegir? — claude-mem, RAGFlow, mem0, LightRAG, PageIndex, graphrag, cognee**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [claude-mem](human/fichas/claude-mem.md) | Tu objetivo encaja con estos ejemplos: Conservar decisiones entre sesiones; Recuperar el motivo de un cambio de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [RAGFlow](human/fichas/ragflow.md) | Tu objetivo encaja con estos ejemplos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [mem0](human/fichas/mem0.md) | Tu objetivo encaja con estos ejemplos: Recordar preferencias de atención; Mantener contexto de una app entre conversaciones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LightRAG](human/fichas/lightrag.md) | Tu objetivo encaja con estos ejemplos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [PageIndex](human/fichas/pageindex.md) | Tu objetivo encaja con estos ejemplos: Consultar informes largos por su estructura; Encontrar una sección de un contrato | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [graphrag](human/fichas/graphrag.md) | Tu objetivo encaja con estos ejemplos: Estudiar relaciones de un corpus; Comparar búsqueda local y resumen global | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [cognee](human/fichas/cognee.md) | Tu objetivo encaja con estos ejemplos: Construir memoria de documentos; Recuperar contexto desde Claude Code o Codex | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Qdrant, Milvus, Faiss, Chroma, pgvector**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Qdrant](human/fichas/qdrant.md) | Tu objetivo encaja con estos ejemplos: Guardar embeddings de documentos; Combinar similitud y filtros de metadatos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Milvus](human/fichas/milvus.md) | Tu objetivo encaja con estos ejemplos: Buscar productos por similitud; Indexar embeddings a gran escala | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Faiss](human/fichas/faiss.md) | Tu objetivo encaja con estos ejemplos: Comparar embeddings de imágenes; Experimentar con índices y compresión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Chroma](human/fichas/chroma.md) | Tu objetivo encaja con estos ejemplos: Prototipar búsqueda semántica local; Filtrar fragmentos por metadatos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [pgvector](human/fichas/pgvector.md) | Tu objetivo encaja con estos ejemplos: Buscar similitud junto a datos SQL; Filtrar resultados vectoriales por columnas del negocio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Memoria persistente para agentes

#### 🧠 claude-mem ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 117k<br>
**Qué es:** Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx claude-mem install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conservar decisiones entre sesiones; Recuperar el motivo de un cambio de código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/claude-mem.md) · [GitHub](https://github.com/thedotmack/claude-mem)

#### 🧠 mem0
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 69k<br>
**Qué es:** Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install mem0ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Recordar preferencias de atención; Mantener contexto de una app entre conversaciones — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [crewAI](human/fichas/crewai.md) · [langchain](human/fichas/langchain.md) · [agentmemory](human/fichas/agentmemory.md)<br>
**Más:** [ficha completa](human/fichas/mem0.md) · [GitHub](https://github.com/mem0ai/mem0)

#### 🏛️ mempalace
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 60.6k<br>
**Qué es:** Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `python -m venv .venv && source .venv/bin/activate
pip install mempalace` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Recuperar decisiones antiguas; Consultar archivos de contexto sin resúmenes destructivos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [open-notebook](human/fichas/open-notebook.md) · [odysseus](human/fichas/odysseus.md)<br>
**Más:** [ficha completa](human/fichas/mempalace.md) · [GitHub](https://github.com/MemPalace/mempalace)

#### ⚙️ OpenViking
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 42.2k<br>
**Qué es:** Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv tool install openviking --upgrade && openviking-server init` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conservar contexto de un proyecto; Consultar conocimientos y skills desde un almacén común — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/openviking.md) · [GitHub](https://github.com/volcengine/OpenViking)

#### 🧠 cognee
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 33.3k<br>
**Qué es:** Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv pip install "cognee[gliner]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir memoria de documentos; Recuperar contexto desde Claude Code o Codex — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Qdrant](human/fichas/qdrant.md) · [mcp-neo4j](human/fichas/mcp-neo4j.md)<br>
**Más:** [ficha completa](human/fichas/cognee.md) · [GitHub](https://github.com/topoteretes/cognee)

#### 🧠 Graphiti
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 32.8k<br>
**Qué es:** Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install graphiti-core` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Representar cambios de una relación comercial; Conservar hechos de conversaciones con fechas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [mcp-neo4j](human/fichas/mcp-neo4j.md)<br>
**Más:** [ficha completa](human/fichas/graphiti.md) · [GitHub](https://github.com/getzep/graphiti)

#### 🧠 supermemory
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 31.6k<br>
**Qué es:** Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx supermemory local` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conservar contexto entre agentes; Buscar documentos y recuerdos de un proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md)<br>
**Más:** [ficha completa](human/fichas/supermemory.md) · [GitHub](https://github.com/supermemoryai/supermemory)

#### 💾 agentmemory
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 30.4k<br>
**Qué es:** Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx -y @agentmemory/agentmemory@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir contexto entre Claude Code y Codex; Consultar decisiones por proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [mem0](human/fichas/mem0.md) · [ruflo](human/fichas/ruflo.md)<br>
**Más:** [ficha completa](human/fichas/agentmemory.md) · [GitHub](https://github.com/rohitg00/agentmemory)

#### 🧠 Letta
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 25.4k<br>
**Qué es:** Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT).<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g @letta-ai/letta-code` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un agente con memoria persistente; Crear un asistente que conserve preferencias — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/letta.md) · [GitHub](https://github.com/letta-ai/letta)

#### 🧠 Engram
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 8.2k<br>
**Qué es:** Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Gentleman-Programming/engram/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Recordar decisiones técnicas; Hacer una entrega de contexto entre sesiones — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [OpenCode](human/fichas/opencode.md)<br>
**Más:** [ficha completa](human/fichas/engram.md) · [GitHub](https://github.com/Gentleman-Programming/engram)

#### 📚 dsh-noema
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 144<br>
**Qué es:** Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/ZSeven-W/dsh-noema/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Dar memoria a DeepSeek Harness; Importar una nota propia de otro agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dsh-noema.md) · [GitHub](https://github.com/ZSeven-W/dsh-noema)

### RAG y motores de conocimiento

#### 📎 RAGFlow ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 94.2k<br>
**Qué es:** Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/infiniflow/ragflow/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/ragflow.md) · [GitHub](https://github.com/infiniflow/ragflow)

#### 📎 LightRAG
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 40.7k<br>
**Qué es:** RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Install LightRAG Server as a tool using uv (recommended)
uv tool install "lightrag-hku[api]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md)<br>
**Más:** [ficha completa](human/fichas/lightrag.md) · [GitHub](https://github.com/HKUDS/LightRAG)

#### 📎 PageIndex
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.4k<br>
**Qué es:** Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -U pageindex` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar informes largos por su estructura; Encontrar una sección de un contrato — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/pageindex.md) · [GitHub](https://github.com/VectifyAI/PageIndex)

#### 🔗 graphrag
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 36.6k<br>
**Qué es:** Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://microsoft.github.io/graphrag/get_started/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar relaciones de un corpus; Comparar búsqueda local y resumen global — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [graphify](human/fichas/graphify.md) · [mcp-neo4j](human/fichas/mcp-neo4j.md) · [turbovec](human/fichas/turbovec.md)<br>
**Más:** [ficha completa](human/fichas/graphrag.md) · [GitHub](https://github.com/microsoft/graphrag)

#### 🖥️ onyx
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 33.4k<br>
**Qué es:** Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/onyx-dot-app/onyx/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar conocimiento de equipo; Dar contexto organizacional a un agente de código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/onyx.md) · [GitHub](https://github.com/onyx-dot-app/onyx)

#### 📚 agentic-rag-for-dummies
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 4.4k<br>
**Qué es:** Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -r requirements.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender RAG por pasos; Comparar un pipeline local con otro proveedor — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/agentic-rag-for-dummies.md) · [GitHub](https://github.com/GiovanniPasq/agentic-rag-for-dummies)

### Bases vectoriales y búsqueda semántica

#### 🧮 Qdrant ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 35.6k<br>
**Qué es:** Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `docker run -p 6333:6333 qdrant/qdrant` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Guardar embeddings de documentos; Combinar similitud y filtros de metadatos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Docling](human/fichas/docling.md) · [n8n](human/fichas/n8n.md) · [LlamaIndex](human/fichas/llama-index.md) · [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/qdrant.md) · [GitHub](https://github.com/qdrant/qdrant)

#### 🧮 Milvus
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 46.7k<br>
**Qué es:** Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/milvus-io/milvus/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar productos por similitud; Indexar embeddings a gran escala — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/milvus.md) · [GitHub](https://github.com/milvus-io/milvus)

#### 🧮 Faiss
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 41.7k<br>
**Qué es:** Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar embeddings de imágenes; Experimentar con índices y compresión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/faiss.md) · [GitHub](https://github.com/facebookresearch/faiss)

#### 🧮 Chroma
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 29.7k<br>
**Qué es:** Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install chromadb # python client` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar búsqueda semántica local; Filtrar fragmentos por metadatos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/chroma.md) · [GitHub](https://github.com/chroma-core/chroma)

#### 🧮 pgvector
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.7k<br>
**Qué es:** Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/pgvector/pgvector/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar similitud junto a datos SQL; Filtrar resultados vectoriales por columnas del negocio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/pgvector.md) · [GitHub](https://github.com/pgvector/pgvector)

#### ⚡ turbovec
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 17.5k<br>
**Qué es:** Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install turbovec` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar índices vectoriales embebidos; Reducir memoria de una búsqueda local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [mem0](human/fichas/mem0.md) · [graphrag](human/fichas/graphrag.md)<br>
**Más:** [ficha completa](human/fichas/turbovec.md) · [GitHub](https://github.com/RyanCodrai/turbovec)

---

## 🧑‍💻 7. Entender código y comprobar su calidad

Índices de código, análisis, calidad, benchmarks y herramientas de desarrollo. Empieza por comprender el proyecto y después elige qué comprobaciones necesitas.

**⚖️ ¿Cuál elegir? — Repomix, codegraph, codebase-memory-mcp, GitNexus**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Repomix](human/fichas/repomix.md) | Tu objetivo encaja con estos ejemplos: Preparar contexto de código para una consulta; Compartir una muestra reproducible de un proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [codegraph](human/fichas/codegraph.md) | Tu objetivo encaja con estos ejemplos: Preparar una refactorización; Encontrar rutas de ejecución de un proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [codebase-memory-mcp](human/fichas/codebase-memory-mcp.md) | Tu objetivo encaja con estos ejemplos: Navegar dependencias de código; Seleccionar pruebas afectadas por un cambio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [GitNexus](human/fichas/gitnexus.md) | Tu objetivo encaja con estos ejemplos: Entender una base de código nueva; Inspeccionar el alcance de una refactorización | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Entender y empaquetar código para agentes

#### 🧬 Repomix ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 29.3k<br>
**Qué es:** Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx repomix@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar contexto de código para una consulta; Compartir una muestra reproducible de un proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/repomix.md) · [GitHub](https://github.com/yamadashy/repomix)

#### 🕸️ graphify
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 148k<br>
**Qué es:** Permite consultar símbolos y relaciones de una base de código desde distintos agentes. El análisis de código es determinista y local; documentos, PDFs, imágenes y video requieren la ruta semántica y sus dependencias. Ofrece adaptadores documentados para Claude Code, Codex y Antigravity.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # detects your assistant and registers the skill` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar impacto de un cambio; Relacionar documentación y estructura de código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [codegraph](human/fichas/codegraph.md) · [graphrag](human/fichas/graphrag.md)<br>
**Más:** [ficha completa](human/fichas/graphify.md) · [GitHub](https://github.com/Graphify-Labs/graphify)

#### 📊 codegraph
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 77.6k<br>
**Qué es:** CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm i -g @colbymchenry/codegraph` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una refactorización; Encontrar rutas de ejecución de un proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [graphify](human/fichas/graphify.md) · [headroom](human/fichas/headroom.md)<br>
**Más:** [ficha completa](human/fichas/codegraph.md) · [GitHub](https://github.com/colbymchenry/codegraph)

#### 🧬 codebase-memory-mcp
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 48.6k<br>
**Qué es:** Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Navegar dependencias de código; Seleccionar pruebas afectadas por un cambio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Serena](human/fichas/serena.md)<br>
**Más:** [ficha completa](human/fichas/codebase-memory-mcp.md) · [GitHub](https://github.com/DeusData/codebase-memory-mcp)

#### 🧭 GitNexus
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 48.5k<br>
**Qué es:** Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Run from your repository root
npx gitnexus analyze

# Connect your editors once
npx gitnexus setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Entender una base de código nueva; Inspeccionar el alcance de una refactorización — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [codegraph](human/fichas/codegraph.md)<br>
**Más:** [ficha completa](human/fichas/gitnexus.md) · [GitHub](https://github.com/abhigyanpatwari/GitNexus)

#### 🧬 tree-sitter
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 27.5k<br>
**Qué es:** Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://tree-sitter.github.io/tree-sitter/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un analizador de código; Extraer símbolos para una herramienta de edición — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ast-grep](human/fichas/ast-grep.md) · [Aider](human/fichas/aider.md)<br>
**Más:** [ficha completa](human/fichas/tree-sitter.md) · [GitHub](https://github.com/tree-sitter/tree-sitter)

#### 🧬 DeepWiki Open
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 18.4k<br>
**Qué es:** Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar documentación inicial de una app; Crear una guía para incorporarse a un proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/deepwiki-open.md) · [GitHub](https://github.com/AsyncFuncAI/deepwiki-open)

#### 🎨 floorplan
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 4.4k<br>
**Qué es:** Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `claude plugin marketplace add haydenschmitty/floorplan
claude plugin install floorplan@floorplan` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar la arquitectura a alguien nuevo; Encontrar dónde se inicia una petición de la interfaz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/floorplan.md) · [GitHub](https://github.com/haydenschmitty/floorplan)

### Calidad, seguridad y benchmarks de código

#### 🛡️ ast-grep
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 16.6k<br>
**Qué es:** CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install --global @ast-grep/cli` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Migrar llamadas de una API; Aplicar reglas de lint personalizadas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tree-sitter](human/fichas/tree-sitter.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/ast-grep.md) · [GitHub](https://github.com/ast-grep/ast-grep)

#### 🛡️ SWE-bench
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 6.2k<br>
**Qué es:** Benchmark para evaluar si los modelos resuelven issues reales de GitHub.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone git@github.com:SWE-bench/SWE-bench.git
cd SWE-bench
pip install -e .` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar soluciones a issues reproducibles; Estudiar evaluación de agentes de programación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/swe-bench.md) · [GitHub](https://github.com/SWE-bench/SWE-bench)

#### 📚 dsh-qa
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 12<br>
**Qué es:** Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npm install @zseven-w/dsh-qa           # the orchestrator
npm install @zseven-w/dsh-browser      # browser sessions` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Repetir una prueba de registro en desarrollo; Guardar evidencia de un fallo de interfaz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dsh-qa.md) · [GitHub](https://github.com/ZSeven-W/dsh-qa)

### CLIs y SDKs de desarrollo

#### 🧰 GitHub CLI ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 47k<br>
**Qué es:** CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/cli/cli/blob/trunk/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar issues desde terminal; Revisar ejecuciones de Actions — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [GitHub MCP Server](human/fichas/github-mcp-server.md)<br>
**Más:** [ficha completa](human/fichas/cli.md) · [GitHub](https://github.com/cli/cli)

#### 🐍 openai-python
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 32.2k<br>
**Qué es:** SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `# install from PyPI
pip install openai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Integrar respuestas de IA en una app Python; Procesar audio o imágenes desde código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/openai-python.md) · [GitHub](https://github.com/openai/openai-python)

---

## 🏠 8. Chats, modelos locales y espacios privados

Motores locales, chats y workspaces. Tener la interfaz en tu equipo no garantiza que el modelo sea local: comprueba su backend y los requisitos de cada ficha.

**⚖️ ¿Cuál elegir? — Ollama, llama.cpp, LocalAI, llamafile**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Ollama](human/fichas/ollama.md) | Tu objetivo encaja con estos ejemplos: Probar un LLM local; Conectar un modelo local a Codex CLI | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [llama.cpp](human/fichas/llama-cpp.md) | Tu objetivo encaja con estos ejemplos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LocalAI](human/fichas/localai.md) | Tu objetivo encaja con estos ejemplos: Ofrecer una API local a una aplicación; Probar texto o voz con distintos backends | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [llamafile](human/fichas/llamafile.md) | Tu objetivo encaja con estos ejemplos: Distribuir una demo local de un LLM; Probar inferencia sin montar un servidor complejo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Open WebUI, AnythingLLM, Jan, SurfSense, LobeHub, PrivateGPT, Cherry Studio**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Open WebUI](human/fichas/open-webui.md) | Tu objetivo encaja con estos ejemplos: Unificar chats de modelos locales; Crear una interfaz compartida para un equipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [AnythingLLM](human/fichas/anything-llm.md) | Tu objetivo encaja con estos ejemplos: Consultar documentación propia; Separar bases de conocimiento por proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Jan](human/fichas/jan.md) | Tu objetivo encaja con estos ejemplos: Conversar con un modelo privado; Comparar un modelo local con una API | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [SurfSense](human/fichas/surfsense.md) | Tu objetivo encaja con estos ejemplos: Revisar un contrato de prueba con comentarios; Extraer datos de un archivo Excel ficticio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LobeHub](human/fichas/lobehub.md) | Tu objetivo encaja con estos ejemplos: Organizar agentes para tareas de equipo; Conectar un agente de código a un espacio de trabajo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [PrivateGPT](human/fichas/private-gpt.md) | Tu objetivo encaja con estos ejemplos: Construir una API privada sobre documentos; Usar un modelo local como backend de programación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Cherry Studio](human/fichas/cherry-studio.md) | Tu objetivo encaja con estos ejemplos: Comparar respuestas de varios modelos; Organizar una base documental de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Motores para correr modelos en local

#### 🦙 Ollama ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 187k<br>
**Qué es:** La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.ollama.com/quickstart); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un LLM local; Conectar un modelo local a Codex CLI — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Open WebUI](human/fichas/open-webui.md) · [n8n](human/fichas/n8n.md) · [litellm](human/fichas/litellm.md) · [crawl4ai](human/fichas/crawl4ai.md)<br>
**Más:** [ficha completa](human/fichas/ollama.md) · [GitHub](https://github.com/ollama/ollama)

#### 🦙 llama.cpp
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 135k<br>
**Qué es:** Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ggml-org/llama.cpp/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Open WebUI](human/fichas/open-webui.md) · [llmfit](human/fichas/llmfit.md) · [LibreChat](human/fichas/librechat.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/llama-cpp.md) · [GitHub](https://github.com/ggml-org/llama.cpp)

#### 🦙 LocalAI
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 50.4k<br>
**Qué es:** Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `docker run -ti --name local-ai -p 8080:8080 localai/localai:latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Ofrecer una API local a una aplicación; Probar texto o voz con distintos backends — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [AnythingLLM](human/fichas/anything-llm.md) · [Open WebUI](human/fichas/open-webui.md) · [LibreChat](human/fichas/librechat.md)<br>
**Más:** [ficha completa](human/fichas/localai.md) · [GitHub](https://github.com/mudler/LocalAI)

#### 🦙 exo
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 48.4k<br>
**Qué es:** Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `brew install --cask exo` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir memoria entre equipos compatibles; Experimentar con inferencia distribuida local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Open WebUI](human/fichas/open-webui.md) · [LibreChat](human/fichas/librechat.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/exo.md) · [GitHub](https://github.com/exo-explore/exo)

#### 🧩 airllm
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 42.4k<br>
**Qué es:** Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install airllm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar inferencia por carga de capas; Probar un modelo que supera la VRAM disponible — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/airllm.md) · [GitHub](https://github.com/lyogavin/airllm)

#### 📏 llmfit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 39k<br>
**Qué es:** Inspecciona el hardware y recomienda modelos según memoria, aceleradores y estimaciones de velocidad. Ayuda a elegir antes de descargar; no evalúa la calidad del modelo en una tarea de negocio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `winget install --exact --id AlexsJones.llmfit` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Elegir un modelo antes de descargarlo; Comparar requisitos de dos cuantizaciones — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [llama.cpp](human/fichas/llama-cpp.md) · [vLLM](human/fichas/vllm.md)<br>
**Más:** [ficha completa](human/fichas/llmfit.md) · [GitHub](https://github.com/AlexsJones/llmfit)

#### 🦙 llamafile
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 26.6k<br>
**Qué es:** Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mozilla-ai/llamafile/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Distribuir una demo local de un LLM; Probar inferencia sin montar un servidor complejo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Open WebUI](human/fichas/open-webui.md) · [AnythingLLM](human/fichas/anything-llm.md) · [LibreChat](human/fichas/librechat.md)<br>
**Más:** [ficha completa](human/fichas/llamafile.md) · [GitHub](https://github.com/mozilla-ai/llamafile)

#### 🧩 FreeToken
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 17.2k<br>
**Qué es:** Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `uv pip install "freetoken[accel]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Experimentar con inferencia de modelos MoE; Evaluar un backend de aceleración local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/freetoken.md) · [GitHub](https://github.com/FlashML-org/FreeToken)

#### 🏠 transformers.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 16.4k<br>
**Qué es:** Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm i @huggingface/transformers` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar texto en el navegador; Procesar audio o imágenes sin servidor de modelos externo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [swr](human/fichas/swr.md)<br>
**Más:** [ficha completa](human/fichas/transformers-js.md) · [GitHub](https://github.com/huggingface/transformers.js)

#### 🧩 magnitude
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 7.8k<br>
**Qué es:** Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `curl -fsSL https://magnitude.dev/install.sh | sh` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un modelo local a Codex; Comparar backends de inferencia en tu equipo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/magnitude.md) · [GitHub](https://github.com/magnitudedev/magnitude)

### Interfaces de chat auto-hospedadas

#### 💬 Open WebUI ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 159k<br>
**Qué es:** Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar chats de modelos locales; Crear una interfaz compartida para un equipo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md) · [SearXNG](human/fichas/searxng.md)<br>
**Más:** [ficha completa](human/fichas/open-webui.md) · [GitHub](https://github.com/open-webui/open-webui)

#### 💬 Jan ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 45.7k<br>
**Qué es:** Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://jan.ai/docs); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conversar con un modelo privado; Comparar un modelo local con una API — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [llmfit](human/fichas/llmfit.md) · [Ollama](human/fichas/ollama.md) · [Playwright MCP](human/fichas/playwright-mcp.md)<br>
**Más:** [ficha completa](human/fichas/jan.md) · [GitHub](https://github.com/janhq/jan)

#### 💬 LobeHub
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 85.5k<br>
**Qué es:** Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `mkdir lobehub && cd lobehub
bash <(curl -fsSL https://lobe.li/setup.sh) -l en
docker compose up -d` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar agentes para tareas de equipo; Conectar un agente de código a un espacio de trabajo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md) · [Playwright MCP](human/fichas/playwright-mcp.md)<br>
**Más:** [ficha completa](human/fichas/lobehub.md) · [GitHub](https://github.com/lobehub/lobehub)

#### 💬 Cherry Studio
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 53.5k<br>
**Qué es:** App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://cherryai.com/docs/en/getting-started/quick-start/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar respuestas de varios modelos; Organizar una base documental de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md) · [Playwright MCP](human/fichas/playwright-mcp.md)<br>
**Más:** [ficha completa](human/fichas/cherry-studio.md) · [GitHub](https://github.com/CherryHQ/cherry-studio)

#### 💬 Text Generation WebUI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 47.7k<br>
**Qué es:** App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/oobabooga/textgen/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar modelos GGUF sin una API remota; Servir un endpoint local para otra app — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LibreChat](human/fichas/librechat.md) · [llmfit](human/fichas/llmfit.md) · [Unsloth](human/fichas/unsloth.md)<br>
**Más:** [ficha completa](human/fichas/textgen.md) · [GitHub](https://github.com/oobabooga/textgen)

#### 💬 LibreChat
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 47.1k<br>
**Qué es:** Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://www.librechat.ai/docs); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar proveedores en una interfaz; Crear asistentes con herramientas y archivos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [Ollama](human/fichas/ollama.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/librechat.md) · [GitHub](https://github.com/LibreChat-AI/LibreChat)

#### 🏠 chatbox
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 42.3k<br>
**Qué es:** Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/chatboxai/chatbox/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conversar con varios proveedores; Probar un modelo local desde escritorio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md) · [LocalAI](human/fichas/localai.md)<br>
**Más:** [ficha completa](human/fichas/chatbox.md) · [GitHub](https://github.com/chatboxai/chatbox)

### Workspaces privados y segundos cerebros

#### 🏠 AnythingLLM ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 68.3k<br>
**Qué es:** App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar documentación propia; Separar bases de conocimiento por proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Qdrant](human/fichas/qdrant.md) · [litellm](human/fichas/litellm.md) · [LocalAI](human/fichas/localai.md)<br>
**Más:** [ficha completa](human/fichas/anything-llm.md) · [GitHub](https://github.com/Mintplex-Labs/anything-llm)

#### ⛺ odysseus
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 95.6k<br>
**Qué es:** Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/odysseus-dev/odysseus.git
cd odysseus
cp .env.example .env
docker compose up -d --build` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar notas y tareas con IA; Comparar respuestas de modelos desde un workspace — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [open-notebook](human/fichas/open-notebook.md) · [ECC](human/fichas/ecc.md) · [mem0](human/fichas/mem0.md)<br>
**Más:** [ficha completa](human/fichas/odysseus.md) · [GitHub](https://github.com/odysseus-dev/odysseus)

#### 🏠 PrivateGPT
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 57.6k<br>
**Qué es:** Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.privategpt.dev/getting-started/quickstart); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una API privada sobre documentos; Usar un modelo local como backend de programación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [vLLM](human/fichas/vllm.md) · [llama.cpp](human/fichas/llama-cpp.md)<br>
**Más:** [ficha completa](human/fichas/private-gpt.md) · [GitHub](https://github.com/zylon-ai/private-gpt)

#### 🏠 Khoj
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 38.1k<br>
**Qué es:** Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.khoj.dev/get-started/setup); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar notas desde Obsidian; Crear un asistente de investigación personal — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/khoj.md) · [GitHub](https://github.com/khoj-ai/khoj)

#### 🏠 Hermes Desktop
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 14.6k<br>
**Qué es:** App de escritorio que envuelve al agente Hermes en una interfaz nativa.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/fathah/hermes-desktop/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Usar Hermes desde una interfaz de escritorio; Consultar una instancia remota de Hermes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [hermes-agent](human/fichas/hermes-agent.md)<br>
**Más:** [ficha completa](human/fichas/hermes-desktop.md) · [GitHub](https://github.com/fathah/hermes-desktop)

#### 🏠 Muse Spark — afiliación por verificar
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 15<br>
**Aviso:** ⚠️ Procedencia y funcionalidad sin verificar; conservar como referencia.<br>
**Qué es:** Proyecto de terceros que se presenta como un estudio de IA de escritorio; su afiliación y funciones no están verificadas.<br>
**Acceso:** API: por confirmar · Coste por confirmar<br>
**Arranque:** [Instrucciones originales](https://github.com/muse-spark-app/muse-spark/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Verificar procedencia de un instalador antes de usarlo; Contrastar afirmaciones de privacidad con documentación verificable — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/muse-spark.md) · [GitHub](https://github.com/muse-spark-app/muse-spark)

### NotebookLM: alternativas y clientes

#### 📓 SurfSense ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 16.9k<br>
**Qué es:** Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/MODSetter/SurfSense/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar un contrato de prueba con comentarios; Extraer datos de un archivo Excel ficticio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/surfsense.md) · [GitHub](https://github.com/MODSetter/SurfSense)

#### 📓 open-notebook
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 42k<br>
**Qué es:** Aplicación auto-hospedada para reunir fuentes, consultar documentos y producir resúmenes o audio. Permite elegir proveedores de chat, embeddings y audio locales o remotos; la privacidad del procesamiento depende de esa configuración.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/lfnovo/open-notebook/blob/main/docs/0-START-HERE/quick-start-local.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar documentos en una libreta; Generar un resumen o audio sobre material propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [odysseus](human/fichas/odysseus.md) · [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/open-notebook.md) · [GitHub](https://github.com/lfnovo/open-notebook)

#### 🎙️ notebooklm-py
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 20.2k<br>
**Qué es:** API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/teng-lin/notebooklm-py/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar consultas documentales; Exportar mapas o resúmenes propios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [notebooklm-mcp-cli](human/fichas/notebooklm-mcp-cli.md)<br>
**Más:** [ficha completa](human/fichas/notebooklm-py.md) · [GitHub](https://github.com/teng-lin/notebooklm-py)

#### 🎚️ notebooklm-mcp-cli
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 6.5k<br>
**Qué es:** CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install notebooklm-mcp-cli` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Administrar fuentes desde un agente; Exportar contenido generado por NotebookLM — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [notebooklm-py](human/fichas/notebooklm-py.md) · [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md)<br>
**Más:** [ficha completa](human/fichas/notebooklm-mcp-cli.md) · [GitHub](https://github.com/jacob-bd/gemini-notebook-mcp-cli)

---

## 🎨 9. Diseñar y construir interfaces web

Componentes, estilos, editores visuales y herramientas de UI con IA. Elige la base de tu interfaz y consulta animación o skills especializadas en sus salas.

**⚖️ ¿Cuál elegir? — ui, daisyUI, Ant Design, Material UI, heroui**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [ui](human/fichas/ui.md) | Tu objetivo encaja con estos ejemplos: Construir un formulario con componentes propios; Crear un sistema de interfaz con código modificable | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [daisyUI](human/fichas/daisyui.md) | Tu objetivo encaja con estos ejemplos: Diseñar una web con clases semánticas; Añadir temas a un panel sencillo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Ant Design](human/fichas/ant-design.md) | Tu objetivo encaja con estos ejemplos: Crear un panel administrativo; Montar formularios de gestión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Material UI](human/fichas/mui.md) | Tu objetivo encaja con estos ejemplos: Crear un dashboard Material Design; Construir una pantalla de ajustes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [heroui](human/fichas/heroui.md) | Tu objetivo encaja con estos ejemplos: Construir formularios accesibles; Crear una interfaz con temas compartidos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — React Bits, magicui**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [React Bits](human/fichas/react-bits.md) | Tu objetivo encaja con estos ejemplos: Crear un encabezado animado; Prototipar una interacción visual | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [magicui](human/fichas/magicui.md) | Tu objetivo encaja con estos ejemplos: Prototipar una sección de landing; Añadir una interacción de presentación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Excalidraw, tldraw**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Excalidraw](human/fichas/excalidraw.md) | Tu objetivo encaja con estos ejemplos: Explicar un flujo a un equipo; Bocetar una interfaz antes de construirla | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [tldraw](human/fichas/tldraw.md) | Tu objetivo encaja con estos ejemplos: Construir una pizarra de colaboración; Crear un editor de diagramas propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — open-design, Onlook**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [open-design](human/fichas/open-design.md) | Tu objetivo encaja con estos ejemplos: Prototipar un dashboard; Iterar una interfaz con feedback de equipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Onlook](human/fichas/onlook.md) | Tu objetivo encaja con estos ejemplos: Ajustar una interfaz React de forma visual; Prototipar un rediseño sobre código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — CopilotKit, assistant-ui**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [CopilotKit](human/fichas/copilotkit.md) | Tu objetivo encaja con estos ejemplos: Añadir asistencia contextual a una app; Mostrar componentes generados a partir de respuestas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [assistant-ui](human/fichas/assistant-ui.md) | Tu objetivo encaja con estos ejemplos: Construir un chat para una app; Añadir herramientas y adjuntos a una conversación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — screenshot-to-code, Stitch SDK**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [screenshot-to-code](human/fichas/screenshot-to-code.md) | Tu objetivo encaja con estos ejemplos: Convertir un mockup propio en prototipo; Explorar una estructura HTML a partir de una captura | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Stitch SDK](human/fichas/stitch-sdk.md) | Tu objetivo encaja con estos ejemplos: Automatizar borradores de UI; Conectar herramientas Stitch a un agente mediante proxy MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Componentes, iconos y sistemas de diseño

#### 🧱 ui ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 128k<br>
**Qué es:** Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://ui.shadcn.com/docs/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un formulario con componentes propios; Crear un sistema de interfaz con código modificable — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [plasmic](human/fichas/plasmic.md)<br>
**Más:** [ficha completa](human/fichas/ui.md) · [GitHub](https://github.com/shadcn-ui/ui)

#### 🧱 Ant Design
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 100k<br>
**Qué es:** Lenguaje de diseño empresarial y librería de componentes React de Ant Group.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install antd` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un panel administrativo; Montar formularios de gestión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [echarts](human/fichas/echarts.md)<br>
**Más:** [ficha completa](human/fichas/ant-design.md) · [GitHub](https://github.com/ant-design/ant-design)

#### 🧱 Material UI
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 99.3k<br>
**Qué es:** Librería de componentes React completa que implementa Material Design de Google.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://mui.com/material-ui/getting-started/installation/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un dashboard Material Design; Construir una pantalla de ajustes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Recharts](human/fichas/recharts.md)<br>
**Más:** [ficha completa](human/fichas/mui.md) · [GitHub](https://github.com/mui/material-ui)

#### 🧱 React Bits
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 52k<br>
**Qué es:** La mayor colección open source de componentes React animados e interactivos para webs llamativas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx shadcn@latest add @react-bits/SplitText-TS-TW` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un encabezado animado; Prototipar una interacción visual — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ui](human/fichas/ui.md) · [motion](human/fichas/motion.md)<br>
**Más:** [ficha completa](human/fichas/react-bits.md) · [GitHub](https://github.com/DavidHDev/react-bits)

#### 🔄 swr
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 32.5k<br>
**Qué es:** Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://swr.vercel.app/docs/getting-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Actualizar un panel sin recargar; Revalidar datos al volver a una pestaña — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [heroui](human/fichas/heroui.md)<br>
**Más:** [ficha completa](human/fichas/swr.md) · [GitHub](https://github.com/vercel/swr)

#### 🦸 heroui
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 31.2k<br>
**Qué es:** Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install @heroui/styles @heroui/react` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir formularios accesibles; Crear una interfaz con temas compartidos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [swr](human/fichas/swr.md)<br>
**Más:** [ficha completa](human/fichas/heroui.md) · [GitHub](https://github.com/heroui-inc/heroui)

#### 🧱 Lucide
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 25.8k<br>
**Qué es:** Librería de más de 1500 iconos SVG consistentes, con paquetes para React, Vue y más.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://lucide.dev/guide/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar iconos de navegación; Ilustrar acciones en una interfaz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ui](human/fichas/ui.md)<br>
**Más:** [ficha completa](human/fichas/lucide.md) · [GitHub](https://github.com/lucide-icons/lucide)

#### ✨ magicui
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.3k<br>
**Qué es:** Librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces modernas con buen acabado desde el inicio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://magicui.design/docs); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una sección de landing; Añadir una interacción de presentación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [motion](human/fichas/motion.md)<br>
**Más:** [ficha completa](human/fichas/magicui.md) · [GitHub](https://github.com/magicuidesign/magicui)

#### 🧱 Radix Primitives
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 19.5k<br>
**Qué es:** Componentes React sin estilos y accesibles para construir sistemas de diseño propios.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://www.radix-ui.com/primitives/docs/overview/getting-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un menú accesible; Crear un sistema de diseño sin estilos impuestos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ui](human/fichas/ui.md) · [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/radix-primitives.md) · [GitHub](https://github.com/radix-ui/primitives)

#### 📚 konva
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 15k<br>
**Qué es:** Biblioteca de canvas para construir editores gráficos, diagramas e interfaces con formas y objetos interactivos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install konva` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un editor de anotaciones; Crear un pequeño diagrama interactivo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/konva.md) · [GitHub](https://github.com/konvajs/konva)

### CSS y estilos

#### 🎨 daisyUI ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 42.8k<br>
**Qué es:** La librería de componentes más popular para Tailwind CSS, con clases semánticas y temas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://daisyui.com/docs/install/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una web con clases semánticas; Añadir temas a un panel sencillo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/daisyui.md) · [GitHub](https://github.com/saadeghi/daisyui)

#### 🌬️ tailwindcss
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 98.6k<br>
**Qué es:** Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://tailwindcss.com/docs/installation/using-vite); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar un formulario responsive; Definir colores y espaciado consistentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [heroui](human/fichas/heroui.md) · [magicui](human/fichas/magicui.md)<br>
**Más:** [ficha completa](human/fichas/tailwindcss.md) · [GitHub](https://github.com/tailwindlabs/tailwindcss)

#### 🧯 normalize.css
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 53.5k<br>
**Qué es:** Hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install --save normalize.css` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar una base de estilos; Reducir diferencias iniciales de formularios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/normalize-css.md) · [GitHub](https://github.com/necolas/normalize.css)

#### 📂 flexoki
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 3.8k<br>
**Qué es:** Paleta de color para texto, código e interfaces que puede servir de referencia al definir un sistema visual.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/kepano/flexoki/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Definir una paleta para una app de notas; Crear un tema de editor — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/flexoki.md) · [GitHub](https://github.com/kepano/flexoki)

### Diseño visual, canvas y builders

#### ✏️ Excalidraw ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 136k<br>
**Qué es:** Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/excalidraw/excalidraw/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar un flujo a un equipo; Bocetar una interfaz antes de construirla — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/excalidraw.md) · [GitHub](https://github.com/excalidraw/excalidraw)

#### 🎨 open-design
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 108k<br>
**Qué es:** Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/nexu-io/open-design.git
cd open-design/deploy
cp .env.example .env
echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
docker compose up -d
# open http://127.0.0.1:7456` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un dashboard; Iterar una interfaz con feedback de equipo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [heroui](human/fichas/heroui.md)<br>
**Más:** [ficha completa](human/fichas/open-design.md) · [GitHub](https://github.com/nexu-io/open-design)

#### ✏️ penpot
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 62.4k<br>
**Qué es:** Plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://help.penpot.app/technical-guide/getting-started/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una interfaz antes de programarla; Colaborar en un sistema de diseño — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [plasmic](human/fichas/plasmic.md)<br>
**Más:** [ficha completa](human/fichas/penpot.md) · [GitHub](https://github.com/penpot/penpot)

#### ✏️ tldraw
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 51.4k<br>
**Qué es:** SDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm i tldraw` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una pizarra de colaboración; Crear un editor de diagramas propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/tldraw.md) · [GitHub](https://github.com/tldraw/tldraw)

#### ✏️ Onlook
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 27.2k<br>
**Qué es:** Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.onlook.com/developers/running-locally); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar una interfaz React de forma visual; Prototipar un rediseño sobre código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md) · [ui](human/fichas/ui.md)<br>
**Más:** [ficha completa](human/fichas/onlook.md) · [GitHub](https://github.com/onlook-dev/onlook)

#### 🧱 plasmic
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 7.2k<br>
**Qué es:** Builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install @plasmicapp/loader-nextjs` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Permitir editar contenido visual de una web; Prototipar una página conectada a React — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/plasmic.md) · [GitHub](https://github.com/plasmicapp/plasmic)

### UI generada con IA y frontends para agentes

#### 🪄 CopilotKit ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 38.7k<br>
**Qué es:** Stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx copilotkit@latest create` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir asistencia contextual a una app; Mostrar componentes generados a partir de respuestas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [Mastra](human/fichas/mastra.md)<br>
**Más:** [ficha completa](human/fichas/copilotkit.md) · [GitHub](https://github.com/CopilotKit/CopilotKit)

#### 🪄 screenshot-to-code
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 81.2k<br>
**Qué es:** Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/abi/screenshot-to-code/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un mockup propio en prototipo; Explorar una estructura HTML a partir de una captura — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/screenshot-to-code.md) · [GitHub](https://github.com/abi/screenshot-to-code)

#### 📚 ai-website-cloner-template
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 39.1k<br>
**Qué es:** Plantilla para que un agente de código estudie una web de referencia y prepare una implementación de su interfaz.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar cómo traducir un diseño a componentes; Prototipar una variante de una página propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ai-website-cloner-template.md) · [GitHub](https://github.com/JCodesMore/ai-website-cloner-template)

#### 📚 json-render
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 19.6k<br>
**Qué es:** Framework para generar interfaces desde una representación JSON y un catálogo de componentes definido por el desarrollador.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# for React
npm install @json-render/core @json-render/react` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear interfaces dinámicas desde datos; Acotar la UI que puede proponer un modelo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/json-render.md) · [GitHub](https://github.com/vercel-labs/json-render)

#### 🪄 OpenUI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 15.2k<br>
**Qué es:** Estándar abierto de Thesys para UI generativa: el LLM responde con interfaces, no solo texto.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx @openuidev/cli@latest create --name genui-chat-app` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear respuestas de chat con interfaz; Construir formularios generados y acotados — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [CopilotKit](human/fichas/copilotkit.md)<br>
**Más:** [ficha completa](human/fichas/openui.md) · [GitHub](https://github.com/thesysdev/openui)

#### 🪄 assistant-ui
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 13.2k<br>
**Qué es:** Librería React y TypeScript para interfaces de chat con IA de calidad producción.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx assistant-ui@latest create   # new project` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un chat para una app; Añadir herramientas y adjuntos a una conversación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md) · [ui](human/fichas/ui.md)<br>
**Más:** [ficha completa](human/fichas/assistant-ui.md) · [GitHub](https://github.com/assistant-ui/assistant-ui)

#### 📚 UI SDK (Vercel)
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 4.6k<br>
**Qué es:** Colección de comportamientos y recursos para que agentes construyan interfaces con patrones de interacción definidos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install @ui-sdk/react @ui-sdk/core` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear componentes con comportamientos reutilizables; Guiar a un agente con patrones de interfaz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ui-sdk.md) · [GitHub](https://github.com/vercel-labs/ui)

#### 🪄 Stitch SDK
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 1.9k<br>
**Qué es:** SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código.<br>
**Acceso:** API de IA necesaria · Coste por confirmar<br>
**Comando documentado:** `npm install @google/stitch-sdk` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar borradores de UI; Conectar herramientas Stitch a un agente mediante proxy MCP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Stitch Skills](human/fichas/stitch-skills.md)<br>
**Más:** [ficha completa](human/fichas/stitch-sdk.md) · [GitHub](https://github.com/google-labs-code/stitch-sdk)

---

## 📊 10. Dashboards, analítica y mapas

Analítica web, BI, gráficos y herramientas geoespaciales. Medir visitas, consultar un negocio y procesar fotografías para crear mapas requieren piezas diferentes.

**⚖️ ¿Cuál elegir? — Umami, Plausible Analytics, Matomo**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Umami](human/fichas/umami.md) | Tu objetivo encaja con estos ejemplos: Medir visitas de una web; Comparar campañas mediante eventos propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Plausible Analytics](human/fichas/plausible.md) | Tu objetivo encaja con estos ejemplos: Medir una web de contenido; Comparar conversiones de una landing | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Matomo](human/fichas/matomo.md) | Tu objetivo encaja con estos ejemplos: Gestionar analítica en servidor propio; Crear informes de comportamiento de una web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Apache Superset, metabase, Redash**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Apache Superset](human/fichas/superset.md) | Tu objetivo encaja con estos ejemplos: Explorar métricas de una base SQL; Compartir un dashboard interno | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [metabase](human/fichas/metabase.md) | Tu objetivo encaja con estos ejemplos: Explorar ventas sin escribir cada consulta SQL; Compartir un informe operativo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Redash](human/fichas/redash.md) | Tu objetivo encaja con estos ejemplos: Compartir consultas de negocio; Crear dashboards a partir de fuentes SQL | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — WrenAI, PandasAI**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [WrenAI](human/fichas/wrenai.md) | Tu objetivo encaja con estos ejemplos: Definir ingresos de forma consistente; Crear dashboards desde preguntas de negocio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [PandasAI](human/fichas/pandas-ai.md) | Tu objetivo encaja con estos ejemplos: Explorar una tabla con lenguaje natural; Generar un gráfico desde una pregunta | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Recharts, D3.js, Chart.js, echarts**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Recharts](human/fichas/recharts.md) | Tu objetivo encaja con estos ejemplos: Visualizar una serie de ventas; Comparar categorías en un dashboard React | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [D3.js](human/fichas/d3.md) | Tu objetivo encaja con estos ejemplos: Diseñar una visualización a medida; Explorar relaciones entre datos con interacción | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Chart.js](human/fichas/chart-js.md) | Tu objetivo encaja con estos ejemplos: Añadir gráficos a una página sencilla; Comparar resultados por periodo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [echarts](human/fichas/echarts.md) | Tu objetivo encaja con estos ejemplos: Construir un dashboard interactivo; Combinar mapa y estadísticas en una web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Analítica web y de producto

#### 📈 Umami ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 40.2k<br>
**Qué es:** Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/umami-software/umami.git
cd umami
pnpm install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Medir visitas de una web; Comparar campañas mediante eventos propios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/umami.md) · [GitHub](https://github.com/umami-software/umami)

#### 📈 posthog
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 40.8k<br>
**Qué es:** Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx -y @posthog/wizard@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Entender abandono en un flujo de registro; Revisar errores y sesiones de una app — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [metabase](human/fichas/metabase.md)<br>
**Más:** [ficha completa](human/fichas/posthog.md) · [GitHub](https://github.com/PostHog/posthog)

#### 📈 Plausible Analytics
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 29.8k<br>
**Qué es:** Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/plausible/community-edition/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Medir una web de contenido; Comparar conversiones de una landing — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/plausible.md) · [GitHub](https://github.com/plausible/analytics)

#### 📈 Matomo
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 22k<br>
**Qué es:** Alternativa open source a Google Analytics con control total de los datos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://matomo.org/faq/how-to-install/faq_18271/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Gestionar analítica en servidor propio; Crear informes de comportamiento de una web — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/matomo.md) · [GitHub](https://github.com/matomo-org/matomo)

### BI, dashboards y chat con datos

#### 📊 Apache Superset ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 75.5k<br>
**Qué es:** Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://superset.apache.org/docs/quickstart/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar métricas de una base SQL; Compartir un dashboard interno — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [WrenAI](human/fichas/wrenai.md)<br>
**Más:** [ficha completa](human/fichas/superset.md) · [GitHub](https://github.com/apache/superset)

#### 📊 WrenAI ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 18.2k<br>
**Qué es:** BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install wrenai

npx skills add Canner/WrenAI` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Definir ingresos de forma consistente; Crear dashboards desde preguntas de negocio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Apache Superset](human/fichas/superset.md) · [DuckDB](human/fichas/duckdb.md)<br>
**Más:** [ficha completa](human/fichas/wrenai.md) · [GitHub](https://github.com/Canner/WrenAI)

#### 📊 Grafana
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 77.9k<br>
**Qué es:** Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://grafana.com/docs/grafana/latest/setup-grafana/installation/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Observar consumo de un servicio; Compartir métricas de una operación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/grafana.md) · [GitHub](https://github.com/grafana/grafana)

#### 📊 metabase
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 50.3k<br>
**Qué es:** Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://www.metabase.com/docs/latest/installation-and-operation/installing-metabase); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar ventas sin escribir cada consulta SQL; Compartir un informe operativo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [posthog](human/fichas/posthog.md) · [echarts](human/fichas/echarts.md)<br>
**Más:** [ficha completa](human/fichas/metabase.md) · [GitHub](https://github.com/metabase/metabase)

#### 📊 Redash
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 28.9k<br>
**Qué es:** Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://redash.io/help/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir consultas de negocio; Crear dashboards a partir de fuentes SQL — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/redash.md) · [GitHub](https://github.com/getredash/redash)

#### 📊 PandasAI
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 23.9k<br>
**Qué es:** Librería para conversar con tus datos (SQL, CSV, Parquet) usando LLM.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install pandasai
pip install pandasai-litellm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una tabla con lenguaje natural; Generar un gráfico desde una pregunta — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md)<br>
**Más:** [ficha completa](human/fichas/pandas-ai.md) · [GitHub](https://github.com/sinaptik-ai/pandas-ai)

### Librerías de gráficos

#### 📉 Recharts ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 27.7k<br>
**Qué es:** Librería de gráficos para React construida con D3, declarativa y componible.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `# latest stable
npm install recharts react-is` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Visualizar una serie de ventas; Comparar categorías en un dashboard React — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ui](human/fichas/ui.md)<br>
**Más:** [ficha completa](human/fichas/recharts.md) · [GitHub](https://github.com/recharts/recharts)

#### 📉 D3.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 114k<br>
**Qué es:** Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y HTML.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://d3js.org/getting-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una visualización a medida; Explorar relaciones entre datos con interacción — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/d3.md) · [GitHub](https://github.com/d3/d3)

#### 📉 Chart.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 67.8k<br>
**Qué es:** Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://www.chartjs.org/docs/latest/getting-started/index); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir gráficos a una página sencilla; Comparar resultados por periodo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/chart-js.md) · [GitHub](https://github.com/chartjs/Chart.js)

#### 📉 echarts
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 67.7k<br>
**Qué es:** Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://echarts.apache.org/handbook/en/get-started/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un dashboard interactivo; Combinar mapa y estadísticas en una web — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [metabase](human/fichas/metabase.md) · [heroui](human/fichas/heroui.md)<br>
**Más:** [ficha completa](human/fichas/echarts.md) · [GitHub](https://github.com/apache/echarts)

#### 📈 uPlot
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 10.6k<br>
**Qué es:** Permite visualizar series temporales, líneas, áreas y otros formatos en una página. Su rendimiento depende del volumen, configuración, navegador y equipo; conviene medirlo con una muestra representativa.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/leeoniya/uPlot/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Mostrar métricas temporales de un sensor; Comparar rendimiento de gráficas con tus propios datos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [swr](human/fichas/swr.md)<br>
**Más:** [ficha completa](human/fichas/uplot.md) · [GitHub](https://github.com/leeoniya/uPlot)

### Recursos y casos de uso

#### 🗂️ awesome-dataviz
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 4.5k<br>
**Qué es:** Directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/hal9ai/awesome-dataviz/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una biblioteca de mapas; Comparar gráficos para React y JavaScript — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [echarts](human/fichas/echarts.md) · [awesome-bigdata](human/fichas/awesome-bigdata.md)<br>
**Más:** [ficha completa](human/fichas/awesome-dataviz.md) · [GitHub](https://github.com/hal9ai/awesome-dataviz)

#### 📊 data-analyst-roadmap
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 1.1k<br>
**Qué es:** Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y orientación de carrera.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mtahiraslan/data-analyst-roadmap/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar un plan inicial de estudio; Identificar conocimientos para un primer proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/data-analyst-roadmap.md) · [GitHub](https://github.com/mtahiraslan/data-analyst-roadmap)

### Inteligencia de fuentes abiertas y mapas

#### 🖥️ gods-eye-view
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 64.9k<br>
**Qué es:** Visualizador geoespacial en un globo 3D que reúne fuentes abiertas para explorar información espacial en el navegador.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/bilawalsidhu/gods-eye-view.git
cd gods-eye-view
npm ci
npm run doctor
npm run dev` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar información geoespacial pública; Consultar el globo desde un agente MCP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/gods-eye-view.md) · [GitHub](https://github.com/bilawalsidhu/gods-eye-view)

#### 📊 osiris
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 11.7k<br>
**Qué es:** Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/simplifaisoul/osiris.git
cd osiris
npm install
npm run dev` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar noticias por ubicación; Comparar eventos públicos en un globo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/osiris.md) · [GitHub](https://github.com/simplifaisoul/osiris)

#### 📊 Pythia
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 1.2k<br>
**Qué es:** Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/jangles-byte/Pythia && cd Pythia
cp .env.example .env          # sensible defaults — no keys needed
./run-all.sh                  # starts Osiris + the engine and opens the UI` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Resumir fuentes públicas con un LLM local; Comparar escenarios sobre un conjunto de eventos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/pythia.md) · [GitHub](https://github.com/jangles-byte/Pythia)

### Fotogrametría y mapas desde imágenes

#### 🖥️ ODM
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.6k<br>
**Qué es:** Herramientas para convertir fotografías aéreas en mapas, nubes de puntos, modelos 3D y modelos de elevación.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `# Windows
docker run -ti --rm -v c:/Users/youruser/datasets:/datasets opendronemap/odm --project-path /datasets project` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un mapa a partir de fotos de dron; Producir una nube de puntos para inspección — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/odm.md) · [GitHub](https://github.com/OpenDroneMap/ODM)

#### ⚙️ WebODM
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 4.3k<br>
**Qué es:** Interfaz para procesar fotografías aéreas y obtener mapas y modelos con el ecosistema de OpenDroneMap.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.webodm.org/installation/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Procesar imágenes de dron desde una interfaz; Comparar resultados de dos vuelos de práctica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ODM](human/fichas/odm.md)<br>
**Más:** [ficha completa](human/fichas/webodm.md) · [GitHub](https://github.com/WebODM/WebODM)

---

## 🖼️ 11. Generar y editar imágenes con IA

Interfaces y modelos de generación, recorte, restauración y ampliación. Distingue la aplicación, sus modelos y el coste o equipo para generar cada imagen.

**⚖️ ¿Cuál elegir? — InvokeAI, Krita AI Diffusion**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [InvokeAI](human/fichas/invokeai.md) | Tu objetivo encaja con estos ejemplos: Retocar una ilustración por regiones; Organizar variantes de una producción visual | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Krita AI Diffusion](human/fichas/krita-ai-diffusion.md) | Tu objetivo encaja con estos ejemplos: Completar un fondo en una ilustración; Usar un boceto para guiar una imagen | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Interfaces para generar imágenes

#### 🧠 ComfyUI ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 147k<br>
**Qué es:** Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install comfy-cli
comfy install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un pipeline reproducible de imagen; Comparar dos ajustes del mismo modelo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/comfyui.md) · [GitHub](https://github.com/Comfy-Org/ComfyUI)

#### 🖌️ InvokeAI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 29.1k<br>
**Qué es:** Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/invoke-ai/InvokeAI/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Retocar una ilustración por regiones; Organizar variantes de una producción visual — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [diffusers](human/fichas/diffusers.md)<br>
**Más:** [ficha completa](human/fichas/invokeai.md) · [GitHub](https://github.com/invoke-ai/InvokeAI)

#### 🖼️ Krita AI Diffusion
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 10.9k<br>
**Qué es:** Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.interstice.cloud/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Completar un fondo en una ilustración; Usar un boceto para guiar una imagen — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/krita-ai-diffusion.md) · [GitHub](https://github.com/Acly/krita-ai-diffusion)

### Modelos, librerías y control

#### 🌀 FLUX.2 ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 2.9k<br>
**Qué es:** Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágenes, con variantes rápidas para GPU domésticas.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `python3.12 -m venv .venv
source .venv/bin/activate
pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --no-cache-dir` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Generar imágenes de producto en tu propia GPU; Editar una foto combinando varias imágenes de referencia — **Evita si:** Necesitas uso comercial con las variantes 9B o [dev] sin licencia, o no tienes GPU; revisa los límites antes de elegirlo<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md)<br>
**Más:** [ficha completa](human/fichas/flux2.md) · [GitHub](https://github.com/black-forest-labs/flux2)

#### 🤗 diffusers
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 34.9k<br>
**Qué es:** Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install --upgrade diffusers[torch]` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Integrar generación de imágenes en Python; Experimentar con modelos de video o audio compatibles — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [cosmos](human/fichas/cosmos.md)<br>
**Más:** [ficha completa](human/fichas/diffusers.md) · [GitHub](https://github.com/huggingface/diffusers)

### Restauración, upscaling y edición

#### 🩹 rembg ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 25.5k<br>
**Qué es:** Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install "rembg[cpu,cli]" # for library + cli` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Crear un recorte para una composición — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/rembg.md) · [GitHub](https://github.com/danielgatis/rembg)

#### 🔍 Real-ESRGAN
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 37.5k<br>
**Qué es:** Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/xinntao/Real-ESRGAN.git
    cd Real-ESRGAN

# Install basicsr - https://github.com/xinntao/BasicSR
    # We use BasicSR for both training and inference
    pip install basicsr
    # facexlib and gfpgan are for face enhancement
    pip install facexlib
    pip install gfpgan
    pip install -r requirements.txt
    python setup.py develop` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una ilustración para mayor tamaño; Mejorar visualmente una copia de material de baja resolución — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/real-esrgan.md) · [GitHub](https://github.com/xinntao/Real-ESRGAN)

#### 🩹 CodeFormer
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 18.2k<br>
**Qué es:** Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/sczhou/CodeFormer/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Experimentar con restauración de una fotografía; Comparar restauradores sobre material propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/codeformer.md) · [GitHub](https://github.com/sczhou/CodeFormer)

### Suites generativas todo-en-uno

#### 🎬 Open-Generative-AI ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 34.7k<br>
**Qué es:** Reúne herramientas de generación de imagen y video. Los modelos alojados consumen servicios externos; la app de escritorio permite configurar motores locales independientes. Las rutas difieren en hardware, instalación, licencia de pesos y costes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar imagen local desde una interfaz; Comparar una ruta local con un servicio de video remoto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [remotion](human/fichas/remotion.md)<br>
**Más:** [ficha completa](human/fichas/open-generative-ai.md) · [GitHub](https://github.com/Anil-matcha/Open-Generative-AI)

---

## 🎬 12. Editar, grabar y generar video

Editores, grabadores, utilidades de medios y modelos de video generativo. La edición de material existente y la generación de nuevas escenas tienen requisitos distintos.

**⚖️ ¿Cuál elegir? — Wan2.2, HunyuanVideo**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Wan2.2](human/fichas/wan2-2.md) | Tu objetivo encaja con estos ejemplos: Prototipar una escena desde texto; Animar una imagen propia con un modelo local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [HunyuanVideo](human/fichas/hunyuanvideo.md) | Tu objetivo encaja con estos ejemplos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Edición, grabación y subtítulos

#### ✂️ FFmpeg ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 67.3k<br>
**Qué es:** Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://ffmpeg.org/download.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un video para una plataforma; Extraer audio de una grabación propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [whisper](human/fichas/whisper.md) · [yt-dlp](human/fichas/yt-dlp.md) · [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/ffmpeg.md) · [GitHub](https://github.com/FFmpeg/FFmpeg)

#### 🎞️ OpenCut
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 98.4k<br>
**Qué es:** Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/OpenCut-app/OpenCut/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar una alternativa de edición abierta; Estudiar la arquitectura de un editor con plugins — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LosslessCut](human/fichas/lossless-cut.md) · [OBS Studio](human/fichas/obs-studio.md) · [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/opencut.md) · [GitHub](https://github.com/OpenCut-app/OpenCut)

#### ✂️ OBS Studio
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 79.6k<br>
**Qué es:** App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://obsproject.com/download); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Grabar una explicación de pantalla; Preparar escenas para una transmisión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LosslessCut](human/fichas/lossless-cut.md) · [OpenCut](human/fichas/opencut.md) · [faster-whisper](human/fichas/faster-whisper.md)<br>
**Más:** [ficha completa](human/fichas/obs-studio.md) · [GitHub](https://github.com/obsproject/obs-studio)

#### ✂️ LosslessCut
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 46k<br>
**Qué es:** App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://losslesscut.app/docs/getting-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Quitar una parte de una grabación; Separar o unir medios compatibles — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md) · [whisperX](human/fichas/whisperx.md) · [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/lossless-cut.md) · [GitHub](https://github.com/mifi/lossless-cut)

#### ✂️ VideoLingo
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 19.3k<br>
**Qué es:** Combina reconocimiento de voz, alineación, traducción, segmentación y doblaje. La ruta revisada utiliza Qwen3-ASR y ForcedAligner localmente por defecto; traducción y TTS tienen requisitos y costes distintos según proveedor.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/Huanshere/VideoLingo.git && cd VideoLingo
uv run start.py` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Subtitular un tutorial propio; Preparar una traducción de una demostración — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [yt-dlp](human/fichas/yt-dlp.md) · [GPT-SoVITS](human/fichas/gpt-sovits.md) · [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/videolingo.md) · [GitHub](https://github.com/Huanshere/VideoLingo)

#### 🖥️ Concat
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 17.6k<br>
**Qué es:** Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/jub0t/Concat/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Editar un video sin subir el material; Automatizar una variante de montaje mediante MCP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/concat.md) · [GitHub](https://github.com/jub0t/Concat)

#### 🎬 palmier-pro
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 14.8k<br>
**Qué es:** Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios actuales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/palmier-io/palmier-pro/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar cortes con un agente; Revisar una secuencia desde herramientas externas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/palmier-pro.md) · [GitHub](https://github.com/palmier-io/palmier-pro)

#### ✂️ DaVinci Resolve MCP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 4.1k<br>
**Qué es:** Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx davinci-resolve-mcp setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar material desde un agente; Preparar ajustes de render con revisión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [FFmpeg](human/fichas/ffmpeg.md) · [whisper](human/fichas/whisper.md)<br>
**Más:** [ficha completa](human/fichas/davinci-resolve-mcp.md) · [GitHub](https://github.com/samuelgursky/davinci-resolve-mcp)

#### 🖥️ OpenRV
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 797<br>
**Qué es:** Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://aswf-openrv.readthedocs.io/en/latest/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar una entrega de animación; Comparar versiones de un efecto visual — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/openrv.md) · [GitHub](https://github.com/AcademySoftwareFoundation/OpenRV)

### Video generativo y pipelines automáticos

#### 🎬 MoneyPrinterTurbo ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 144k<br>
**Qué es:** App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `python -m pip install mpt
mpt webui` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un borrador de video de producto; Generar variantes de un tutorial propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Kokoro](human/fichas/kokoro.md) · [faster-whisper](human/fichas/faster-whisper.md)<br>
**Más:** [ficha completa](human/fichas/moneyprinterturbo.md) · [GitHub](https://github.com/harry0703/MoneyPrinterTurbo)

#### 🎬 Wan2.2 ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 18.7k<br>
**Qué es:** Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/Wan-Video/Wan2.2.git
cd Wan2.2

# Ensure torch >= 2.4.0
# If the installation of `flash_attn` fails, try installing the other packages first and install `flash_attn` last
pip install -r requirements.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una escena desde texto; Animar una imagen propia con un modelo local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md) · [Real-ESRGAN](human/fichas/real-esrgan.md) · [CosyVoice](human/fichas/cosyvoice.md)<br>
**Más:** [ficha completa](human/fichas/wan2-2.md) · [GitHub](https://github.com/Wan-Video/Wan2.2)

#### 🎬 HunyuanVideo
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 12.8k<br>
**Qué es:** Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ComfyUI](human/fichas/comfyui.md) · [diffusers](human/fichas/diffusers.md) · [Real-ESRGAN](human/fichas/real-esrgan.md)<br>
**Más:** [ficha completa](human/fichas/hunyuanvideo.md) · [GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo)

#### 🎬 WanGP
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 11.8k<br>
**Qué es:** App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/deepbeepmeep/Wan2GP/blob/main/docs/INSTALLATION.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar varios modelos desde una interfaz; Preparar clips locales con una GPU limitada — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [MoviePy](human/fichas/moviepy.md) · [LosslessCut](human/fichas/lossless-cut.md)<br>
**Más:** [ficha completa](human/fichas/wan2gp.md) · [GitHub](https://github.com/deepbeepmeep/WanGP)

#### 🎬 short-video-factory
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.1k<br>
**Qué es:** Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/YILS-LIN/short-video-factory/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un borrador de producto; Preparar variantes de un anuncio propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/short-video-factory.md) · [GitHub](https://github.com/YILS-LIN/short-video-factory)

#### 🎬 AI-Youtube-Shorts-Generator
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.1k<br>
**Qué es:** Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM.<br>
**Acceso:** API de IA necesaria · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator.git
   cd AI-Youtube-Shorts-Generator

pip install -r requirements.txt
   # Only if you plan to use --mode local:
   pip install -r requirements-local.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Obtener clips de un tutorial propio; Comparar criterios de selección de momentos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/ai-youtube-shorts-generator.md) · [GitHub](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)

---

## 📄 13. PDF, OCR y procesamiento de documentos

Extracción de texto, OCR, conversión y gestión de PDF. Empieza por el formato de entrada y comprueba con una muestra si conserva el contenido que necesitas.

**⚖️ ¿Cuál elegir? — PaddleOCR, Docling, MinerU, Tesseract, Marker, Unlimited-OCR, olmOCR**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [PaddleOCR](human/fichas/paddleocr.md) | Tu objetivo encaja con estos ejemplos: Digitalizar un formulario propio; Extraer texto y estructura de una página escaneada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Docling](human/fichas/docling.md) | Tu objetivo encaja con estos ejemplos: Preparar documentos para RAG; Extraer tablas antes de un análisis | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [MinerU](human/fichas/mineru.md) | Tu objetivo encaja con estos ejemplos: Preparar PDFs complejos para un índice; Extraer tablas y fórmulas de un documento propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Tesseract](human/fichas/tesseract.md) | Tu objetivo encaja con estos ejemplos: Digitalizar texto de una fotografía propia; Incorporar OCR local a un script | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Marker](human/fichas/marker.md) | Tu objetivo encaja con estos ejemplos: Extraer contenido de informes; Preparar documentos escaneados para búsqueda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Unlimited-OCR](human/fichas/unlimited-ocr.md) | Tu objetivo encaja con estos ejemplos: Estudiar parsing de documentos largos; Comparar un VLM OCR con otro motor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [olmOCR](human/fichas/olmocr.md) | Tu objetivo encaja con estos ejemplos: Preparar PDFs para entrenamiento documental; Procesar escaneos con un VLM | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Stirling-PDF, pdfcraft**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Stirling-PDF](human/fichas/stirling-pdf.md) | Tu objetivo encaja con estos ejemplos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [pdfcraft](human/fichas/pdfcraft.md) | Tu objetivo encaja con estos ejemplos: Editar PDFs desde un navegador; Convertir o dividir un documento de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Conversión de documentos para IA

#### 🔄 Docling ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 70.6k<br>
**Qué es:** Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install docling` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar documentos para RAG; Extraer tablas antes de un análisis — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [Haystack](human/fichas/haystack.md) · [Qdrant](human/fichas/qdrant.md)<br>
**Más:** [ficha completa](human/fichas/docling.md) · [GitHub](https://github.com/docling-project/docling)

#### 📝 markitdown
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 195k<br>
**Qué es:** Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/markitdown/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar documentos Office para consulta; Crear una copia textual de un informe — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ppt-master](human/fichas/ppt-master.md) · [open-notebook](human/fichas/open-notebook.md)<br>
**Más:** [ficha completa](human/fichas/markitdown.md) · [GitHub](https://github.com/microsoft/markitdown)

#### 🔄 MinerU
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 83.7k<br>
**Qué es:** Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv pip install -U "mineru>=4.0,<5"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar PDFs complejos para un índice; Extraer tablas y fórmulas de un documento propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [RAGFlow](human/fichas/ragflow.md)<br>
**Más:** [ficha completa](human/fichas/mineru.md) · [GitHub](https://github.com/opendatalab/MinerU)

#### 🔄 Pandoc
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 46.9k<br>
**Qué es:** Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://pandoc.org/installing.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Generar documentos desde Markdown; Convertir un libro propio a EPUB — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/pandoc.md) · [GitHub](https://github.com/jgm/pandoc)

#### 🔄 Marker
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.9k<br>
**Qué es:** Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install marker-pdf` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer contenido de informes; Preparar documentos escaneados para búsqueda — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/marker.md) · [GitHub](https://github.com/datalab-to/marker)

#### 🔄 PDF Inspector
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 20k<br>
**Qué es:** Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install pdf-inspector` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Decidir cuándo hace falta OCR; Extraer texto con posiciones de un PDF — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md) · [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/pdf-inspector.md) · [GitHub](https://github.com/firecrawl/pdf-inspector)

#### 🔄 Unstructured
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 15.7k<br>
**Qué es:** ETL open source que transforma documentos complejos en datos estructurados para LLM.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Unstructured-IO/unstructured/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar documentos para una base de conocimiento; Crear un pipeline ETL de archivos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md)<br>
**Más:** [ficha completa](human/fichas/unstructured.md) · [GitHub](https://github.com/Unstructured-IO/unstructured)

### OCR

#### 🔠 PaddleOCR ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 92.7k<br>
**Qué es:** Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/installation.en.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Digitalizar un formulario propio; Extraer texto y estructura de una página escaneada — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/paddleocr.md) · [GitHub](https://github.com/PaddlePaddle/PaddleOCR)

#### 🔠 OCRmyPDF ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 35.3k<br>
**Qué es:** Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://ocrmypdf.readthedocs.io/en/latest/installation.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Hacer buscables documentos escaneados; Preparar un archivo histórico propio para indexación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Tesseract](human/fichas/tesseract.md) · [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/ocrmypdf.md) · [GitHub](https://github.com/ocrmypdf/OCRmyPDF)

#### 🔠 Tesseract
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 77.5k<br>
**Qué es:** Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://tesseract-ocr.github.io/tessdoc/Installation.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Digitalizar texto de una fotografía propia; Incorporar OCR local a un script — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md)<br>
**Más:** [ficha completa](human/fichas/tesseract.md) · [GitHub](https://github.com/tesseract-ocr/tesseract)

#### 🔠 Unlimited-OCR
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 31.2k<br>
**Qué es:** Modelo de Baidu para parsear documentos largos de una sola pasada con visión.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install torch==2.13.0 torchvision pillow transformers==4.52.1 huggingface-hub==0.36.0 \
  tokenizers==0.21.4 addict==2.4.0 einops==0.8.2 easydict==1.13` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar parsing de documentos largos; Comparar un VLM OCR con otro motor — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [cosmos](human/fichas/cosmos.md) · [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/unlimited-ocr.md) · [GitHub](https://github.com/baidu/Unlimited-OCR)

#### 🔠 olmOCR
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 19.8k<br>
**Qué es:** Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install olmocr` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar PDFs para entrenamiento documental; Procesar escaneos con un VLM — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [vLLM](human/fichas/vllm.md)<br>
**Más:** [ficha completa](human/fichas/olmocr.md) · [GitHub](https://github.com/allenai/olmocr)

#### 📚 pdf-craft
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 6.7k<br>
**Qué es:** Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `python -m pip install "pdf-craft[local]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una versión editable de un escaneo propio; Preparar un EPUB desde material autorizado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Unlimited-OCR](human/fichas/unlimited-ocr.md)<br>
**Más:** [ficha completa](human/fichas/pdf-craft.md) · [GitHub](https://github.com/oomol-lab/pdf-craft)

### Herramientas PDF

#### 📑 Stirling-PDF ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 96.6k<br>
**Qué es:** Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [OCRmyPDF](human/fichas/ocrmypdf.md)<br>
**Más:** [ficha completa](human/fichas/stirling-pdf.md) · [GitHub](https://github.com/Stirling-Tools/Stirling-PDF)

#### 📑 PDFMathTranslate
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 38.4k<br>
**Qué es:** Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install uv
   uv tool install --python 3.12 pdf2zh` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Leer un artículo en otro idioma; Crear una versión bilingüe de documentación propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/pdfmathtranslate.md) · [GitHub](https://github.com/PDFMathTranslate/PDFMathTranslate)

#### ⚙️ docuseal
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 19.1k<br>
**Qué es:** Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run --name docuseal -p 3000:3000 -v.:/data docuseal/docuseal` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar formularios internos de prueba; Evaluar un flujo de firma documental — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/docuseal.md) · [GitHub](https://github.com/docusealco/docuseal)

#### 📄 pdfcraft
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 9.8k<br>
**Qué es:** Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Editar PDFs desde un navegador; Convertir o dividir un documento de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/pdfcraft.md) · [GitHub](https://github.com/PDFCraftTool/pdfcraft)

#### 📑 PdfDing
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 1.8k<br>
**Qué es:** Gestor y visor de PDFs auto-hospedado, ligero, con etiquetas y progreso de lectura.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://docs.pdfding.com/getting_started/docker/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una colección de PDFs; Consultar documentos desde varios dispositivos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [markitdown](human/fichas/markitdown.md) · [ppt-master](human/fichas/ppt-master.md) · [reveal.js](human/fichas/reveal-js.md)<br>
**Más:** [ficha completa](human/fichas/pdfding.md) · [GitHub](https://codeberg.org/mrmn/PdfDing)

### Gestión y archivo de documentos

#### ⚙️ paperless-ngx
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 48.1k<br>
**Qué es:** Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://docs.paperless-ngx.com/setup/#installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar recibos de prueba; Construir un archivo documental buscable — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/paperless-ngx.md) · [GitHub](https://github.com/paperless-ngx/paperless-ngx)

---

## 📈 14. Investigar finanzas y mercados

Agentes de investigación, análisis cuantitativo, backtesting y bots de ejemplo. Distingue una explicación o simulación de una operación con fondos reales.

### Agentes de investigación financiera

#### 📚 daily_stock_analysis ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟡 medio · ⭐ 72.3k<br>
**Qué es:** Sistema que analiza acciones de varios mercados con LLM y envía un tablero de decisiones diario.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# 克隆项目
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

# 安装依赖
pip install -r requirements.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un resumen de investigación; Comparar noticias y datos de una lista de seguimiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/daily-stock-analysis.md) · [GitHub](https://github.com/ZhuLinsen/daily_stock_analysis)

#### 📊 dexter ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟡 medio · ⭐ 27.8k<br>
**Qué es:** Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/virattt/dexter/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar investigación de una empresa; Comparar explicaciones con documentos fuente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dexter.md) · [GitHub](https://github.com/virattt/dexter)

#### 📊 TradingAgents
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 123k<br>
**Qué es:** Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de trading.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents

pip install .` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar debate entre agentes financieros; Comparar proveedores sobre la misma muestra histórica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/tradingagents.md) · [GitHub](https://github.com/TauricResearch/TradingAgents)

#### 🖥️ Vibe-Trading
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 38.2k<br>
**Qué es:** Agente de investigación y trabajo con estrategias de trading que utiliza modelos y componentes configurables.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install vibe-trading-ai
vibe-trading init
vibe-trading` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar sensibilidad de una estrategia; Organizar artefactos de investigación reproducibles — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/vibe-trading.md) · [GitHub](https://github.com/HKUDS/Vibe-Trading)

#### 📊 FinceptTerminal
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🔴 pesado · ⭐ 33.8k<br>
**Qué es:** Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar indicadores de varios mercados; Comparar información económica de fuentes distintas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/finceptterminal.md) · [GitHub](https://github.com/Fincept-Corporation/FinceptTerminal)

#### 📊 AutoHedge
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 6.7k<br>
**Qué es:** Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado.<br>
**Acceso:** API de IA necesaria · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -U autohedge` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar coordinación de analistas y riesgo; Revisar el diseño de un pipeline de trading — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/autohedge.md) · [GitHub](https://github.com/The-Swarm-Corporation/AutoHedge)

#### 📊 QuantHarness
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 2.9k<br>
**Qué es:** Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de trading.<br>
**Acceso:** API de IA necesaria · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -r requirements.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar agentes que interpretan gráficos; Comparar componentes de un análisis experimental — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/quantharness.md) · [GitHub](https://github.com/Y-Research-SBU/QuantHarness)

### Modelos y backtesting cuantitativo

#### 📊 qlib ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 50.3k<br>
**Qué es:** Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install pyqlib` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar modelos sobre datos temporales; Investigar un pipeline cuantitativo reproducible — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/qlib.md) · [GitHub](https://github.com/microsoft/qlib)

#### 📚 nautilus_trader
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 31.5k<br>
**Qué es:** Motor de trading y backtesting con arquitectura orientada a eventos para investigar y desarrollar estrategias.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install -U nautilus_trader --pre` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un motor orientado a eventos; Comparar simulaciones con datos registrados — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/nautilus-trader.md) · [GitHub](https://github.com/nautechsystems/nautilus_trader)

#### 📚 FinRL
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 17.1k<br>
**Qué es:** Biblioteca y ejemplos para investigar estrategias de trading mediante aprendizaje por refuerzo y simulaciones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/AI4Finance-Foundation/FinRL.git
cd FinRL

pip install -e .` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar entornos de RL financiero; Comparar políticas en simulación histórica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/finrl.md) · [GitHub](https://github.com/AI4Finance-Foundation/FinRL)

#### 📚 vectorbt
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 9.9k<br>
**Qué es:** Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -U vectorbt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar indicadores en una serie; Explorar sensibilidad de una regla histórica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/vectorbt.md) · [GitHub](https://github.com/polakowo/vectorbt)

#### 📚 lumibot
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 2.2k<br>
**Qué es:** Framework de Python para desarrollar estrategias, realizar backtesting y conectar simulación u operación con brokers.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install lumibot` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar una estrategia de reglas; Estudiar decisiones de una estrategia AI en backtest — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/lumibot.md) · [GitHub](https://github.com/Lumiwealth/lumibot)

### Bots y conexiones a exchanges

#### 🖥️ freqtrade
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 56.9k<br>
**Qué es:** Bot de trading de criptomonedas con herramientas para preparar estrategias, hacer backtesting y operar en simulación.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://www.freqtrade.io/en/stable/docker_quickstart/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar una regla en datos históricos; Evaluar una estrategia en simulación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/freqtrade.md) · [GitHub](https://github.com/freqtrade/freqtrade)

#### 📚 ccxt
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 44.9k<br>
**Qué es:** Biblioteca que unifica APIs de exchanges para consultar mercados y desarrollar integraciones de trading.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install ccxt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar consultas de varios mercados; Construir una integración de datos de exchange — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ccxt.md) · [GitHub](https://github.com/ccxt/ccxt)

#### 🖥️ hummingbot
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 21.2k<br>
**Qué es:** Software para desarrollar y ejecutar bots de trading de criptomonedas mediante conectores y estrategias configurables.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Clone the repository
git clone https://github.com/hummingbot/hummingbot.git
cd hummingbot

# Create the conda environment, build extensions, and expose the `hbot` CLI
make install

# Activate the environment
conda activate hummingbot
hbot --help` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un conector de exchange; Evaluar un bot en un entorno de práctica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/hummingbot.md) · [GitHub](https://github.com/hummingbot/hummingbot)

#### 📊 binance-trader
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🖥️ app · Setup 🟡 medio · ⭐ 2.8k<br>
**Qué es:** Bot experimental de Python para estudiar estrategias y automatización con la API de Binance.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/yasinkuyu/binance-trader/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una estrategia de ejemplo; Analizar cómo se conecta un bot a un exchange — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/binance-trader.md) · [GitHub](https://github.com/yasinkuyu/binance-trader)

#### 📊 open-sol-bot
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 406<br>
**Qué es:** Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/ChainBuff/open-sol-bot/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un bot de seguimiento on-chain; Revisar una integración de Telegram con blockchain — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/open-sol-bot.md) · [GitHub](https://github.com/ChainBuff/open-sol-bot)

#### 📚 py-sdk
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 154<br>
**Qué es:** SDK Python de Polymarket para integrar funciones de su plataforma mediante las APIs y credenciales correspondientes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv add polymarket-client` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar la API pública de Polymarket; Preparar una migración desde el cliente antiguo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/py-sdk.md) · [GitHub](https://github.com/Polymarket/py-sdk)

### Ejemplos y aprendizaje

#### 📊 machine-learning-for-trading
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 21.8k<br>
**Qué es:** Material y código de Machine Learning for Trading para estudiar datos, modelos y evaluación de estrategias.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/stefan-jansen/machine-learning-for-trading/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender investigación cuantitativa; Estudiar costes y sesgos de un backtest — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/machine-learning-for-trading.md) · [GitHub](https://github.com/stefan-jansen/machine-learning-for-trading)

#### 🖥️ PixelFund-AI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6<br>
**Qué es:** Aplicación de simulación bursátil con agentes e interfaz en pixel art para explorar carteras y operaciones virtuales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `cp .env.example .env
npm install
npm run dev:all` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una cartera virtual con ciclo de órdenes; Prototipar una interfaz de comité de inversión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/pixelfund-ai.md) · [GitHub](https://github.com/kyjwang/PixelFund-AI)

#### 🖥️ pixel-hedge-fund
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 5<br>
**Qué es:** Demostración de una oficina financiera en pixel art con interfaz de análisis y conexiones configurables a mercados.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `cd pixel-hedge-fund   # repo root
npm install
npm run dev -- --port 5173` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una interfaz financiera en pixel art; Mostrar estados y movimientos de una simulación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/pixel-hedge-fund.md) · [GitHub](https://github.com/jaypolanco96/pixel-hedge-fund)

#### 🖥️ company-pixel-office
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 4<br>
**Qué es:** Demostración de una oficina de trading en pixel art para estudiar su interfaz y la representación visual de un equipo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ATK-zk/company-pixel-office/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una visualización de equipo en pixel art; Prototipar un panel de estados narrativo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/company-pixel-office.md) · [GitHub](https://github.com/ATK-zk/company-pixel-office)

---

## 🗂️ 15. Organizar notas, archivos y servicios personales

Notas, sincronización, privacidad, aprendizaje y servidores personales. Distingue una aplicación lista, un plugin y la infraestructura que debes administrar.

**⚖️ ¿Cuál elegir? — Anytype Desktop, AppFlowy**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Anytype Desktop](human/fichas/anytype-ts.md) | Tu objetivo encaja con estos ejemplos: Organizar notas y proyectos personales; Diseñar una colección con campos propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [AppFlowy](human/fichas/appflowy.md) | Tu objetivo encaja con estos ejemplos: Organizar un proyecto colaborativo; Construir una wiki de equipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — claude-obsidian, obsidian-second-brain**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [claude-obsidian](human/fichas/claude-obsidian.md) | Tu objetivo encaja con estos ejemplos: Organizar apuntes por conceptos; Consultar decisiones desde una bóveda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [obsidian-second-brain](human/fichas/obsidian-second-brain.md) | Tu objetivo encaja con estos ejemplos: Compartir un diario de decisiones entre agentes; Consultar apuntes con búsqueda y fuentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Notas, bóvedas y conocimiento personal

#### 🖥️ Anytype Desktop ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 9.1k<br>
**Qué es:** Cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento personal.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/anyproto/anytype-ts/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar notas y proyectos personales; Diseñar una colección con campos propios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/anytype-ts.md) · [GitHub](https://github.com/anyproto/anytype-ts)

#### 🖥️ AppFlowy
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 78.9k<br>
**Qué es:** Espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento propio.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar un proyecto colaborativo; Construir una wiki de equipo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/appflowy.md) · [GitHub](https://github.com/AppFlowy-IO/AppFlowy)

#### 🎨 obsidian-skills
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 52.6k<br>
**Qué es:** Skills para que un agente trabaje con Obsidian y sus formatos de notas, bases de datos y lienzos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `claude plugin marketplace add obsidianmd/obsidian-skills
claude plugin install obsidian@obsidian-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Guiar un agente para trabajar con notas; Crear bases y lienzos en formatos Obsidian — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Obsidian: distribución y extensiones](human/fichas/obsidian-releases.md)<br>
**Más:** [ficha completa](human/fichas/obsidian-skills.md) · [GitHub](https://github.com/obsidianmd/obsidian-skills)

#### ⚙️ karakeep
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 30.5k<br>
**Qué es:** Gestor autoalojado de marcadores, notas e imágenes con búsqueda y funciones opcionales de clasificación mediante IA.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.karakeep.com/Installation/docker); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una biblioteca de enlaces; Clasificar artículos con un modelo local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/karakeep.md) · [GitHub](https://github.com/karakeep-app/karakeep)

#### 🖥️ Obsidian: distribución y extensiones
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 23.3k<br>
**Qué es:** Repositorio de distribución de Obsidian y sus listados de plugins y temas; no contiene el código completo de la aplicación.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/obsidianmd/obsidian-releases/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una distribución oficial; Estudiar el catálogo de temas y plugins — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/obsidian-releases.md) · [GitHub](https://github.com/obsidianmd/obsidian-releases)

#### 🎨 claude-obsidian
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 16.5k<br>
**Qué es:** Instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro de una bóveda de notas de Obsidian.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `claude plugin marketplace add AgriciDaniel/claude-obsidian
claude plugin install claude-obsidian@agricidaniel-claude-obsidian` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar apuntes por conceptos; Consultar decisiones desde una bóveda — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-obsidian.md) · [GitHub](https://github.com/AgriciDaniel/claude-obsidian)

#### 📚 kepano-obsidian
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 6k<br>
**Qué es:** Plantilla de una bóveda de Obsidian para estudiar una forma de organizar notas e información personal.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/kepano/kepano-obsidian/blob/main/Readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una organización de notas; Adaptar una plantilla personal de conocimiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/kepano-obsidian.md) · [GitHub](https://github.com/kepano/kepano-obsidian)

#### 🖥️ obsidian-minimal
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 5.7k<br>
**Qué es:** Tema configurable de Obsidian para ajustar la apariencia y reducir distracciones al trabajar con notas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://minimal.guide/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar tipografía de una bóveda; Crear una interfaz de notas con menos distracciones — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/obsidian-minimal.md) · [GitHub](https://github.com/kepano/obsidian-minimal)

#### 🖥️ obsidian-clipper
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 5.6k<br>
**Qué es:** Extensión oficial para capturar páginas y fragmentos de la web y guardarlos como notas en Obsidian.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://help.obsidian.md/web-clipper); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Capturar lecturas con una plantilla; Extraer un resumen opcional con Interpreter — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/obsidian-clipper.md) · [GitHub](https://github.com/obsidianmd/obsidian-clipper)

#### 🎨 obsidian-second-brain
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 5.3k<br>
**Qué es:** Sistema de memoria y notas en Markdown para compartir contexto de trabajo entre agentes y una bóveda de Obsidian.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `/plugin marketplace add eugeniughelbur/obsidian-second-brain
/plugin install obsidian-second-brain@obsidian-second-brain` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir un diario de decisiones entre agentes; Consultar apuntes con búsqueda y fuentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/obsidian-second-brain.md) · [GitHub](https://github.com/eugeniughelbur/obsidian-second-brain)

#### 📚 obsidian-sample-plugin
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 4.7k<br>
**Qué es:** Plantilla oficial para programar un plugin de Obsidian con una estructura inicial y configuración de desarrollo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender a programar un plugin; Prototipar una función para notas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/obsidian-sample-plugin.md) · [GitHub](https://github.com/obsidianmd/obsidian-sample-plugin)

#### 📂 jsoncanvas
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 3.9k<br>
**Qué es:** Especificación abierta de JSON Canvas para describir nodos y conexiones de un lienzo visual en un archivo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/obsidianmd/jsoncanvas/blob/main/readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Intercambiar un mapa de ideas; Estudiar un formato abierto de lienzo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/jsoncanvas.md) · [GitHub](https://github.com/obsidianmd/jsoncanvas)

#### 📂 obsidian-help
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 2k<br>
**Qué es:** Documentación oficial de Obsidian para aprender sus funciones, configuración y formas de organizar una bóveda.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/obsidianmd/obsidian-help/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender funciones básicas de Obsidian; Consultar cómo configurar una bóveda — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/obsidian-help.md) · [GitHub](https://github.com/obsidianmd/obsidian-help)

#### 🖥️ obsidian-importer
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 1.8k<br>
**Qué es:** Plugin oficial para convertir datos de otras aplicaciones en archivos Markdown que puedes abrir en Obsidian.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/obsidianmd/obsidian-importer/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Migrar una muestra desde otra app; Verificar un formato de exportación antes de migrar — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/obsidian-importer.md) · [GitHub](https://github.com/obsidianmd/obsidian-importer)

### Sincronización y gestión de archivos

#### 🖥️ syncthing
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 90.4k<br>
**Qué es:** Aplicación para sincronizar archivos entre dispositivos directamente y controlar qué carpetas se comparten.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/syncthing/syncthing/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir una carpeta personal entre equipos; Mantener una colección de notas sincronizada — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/syncthing.md) · [GitHub](https://github.com/syncthing/syncthing)

#### 🏠 server
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 37.5k<br>
**Qué es:** Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://nextcloud.com/install/#instructions-server); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Alojar documentos de un equipo; Sincronizar archivos y calendarios propios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/nextcloud-server.md) · [GitHub](https://github.com/nextcloud/server)

### Credenciales y privacidad

#### ⚙️ vaultwarden
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 70.7k<br>
**Qué es:** Servidor no oficial compatible con clientes Bitwarden para alojar una bóveda de credenciales en infraestructura propia.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/dani-garcia/vaultwarden/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar alojamiento propio de una bóveda; Evaluar compatibilidad con clientes Bitwarden — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Bitwarden Clients](human/fichas/bitwarden-clients.md)<br>
**Más:** [ficha completa](human/fichas/vaultwarden.md) · [GitHub](https://github.com/dani-garcia/vaultwarden)

#### ⚙️ AdGuardHome
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 38.5k<br>
**Qué es:** Servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una red desde una configuración central.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Filtrar dominios en una red propia; Estudiar consultas y reglas DNS — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/adguardhome.md) · [GitHub](https://github.com/AdguardTeam/AdGuardHome)

#### 🖥️ Bitwarden Clients
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 14.2k<br>
**Qué es:** Clientes oficiales de Bitwarden para gestionar credenciales y utilizar funciones como compartir información con Send.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://bitwarden.com/download/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Gestionar credenciales desde extensión y escritorio; Estudiar un flujo Send con contenido ficticio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/bitwarden-clients.md) · [GitHub](https://github.com/bitwarden/clients)

### Libros, podcasts y bibliotecas personales

#### ⚙️ audiobookshelf
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 15k<br>
**Qué es:** Servidor personal para organizar audiolibros y podcasts, escuchar contenido y conservar el progreso de reproducción.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://audiobookshelf.org/docs/category/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar audiolibros propios o autorizados; Gestionar una colección de podcasts — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/audiobookshelf.md) · [GitHub](https://github.com/advplyr/audiobookshelf)

### Automatización del hogar

#### ⚙️ Home Assistant
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 92.3k<br>
**Qué es:** Motor de Home Assistant para conectar dispositivos y automatizar acciones del hogar con control local.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://www.home-assistant.io/installation/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Controlar una luz de práctica por horario; Visualizar sensores de una vivienda — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/home-assistant.md) · [GitHub](https://github.com/home-assistant/core)

### Herramientas y organización personal

#### 🎨 ai-job-search
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 71.8k<br>
**Qué es:** Proyecto basado en Claude Code para evaluar vacantes, adaptar currículums y preparar cartas e entrevistas de empleo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/ai-job-search-dev/ai-job-search/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Adaptar un CV a una oferta; Preparar preguntas para una entrevista — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ai-job-search.md) · [GitHub](https://github.com/ai-job-search-dev/ai-job-search)

#### 🖥️ cleanyourtv
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 57.9k<br>
**Qué es:** Herramienta para revisar y retirar aplicaciones preinstaladas de dispositivos Android TV o Google TV mediante ADB.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Gathin23/cleanyourtv/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar apps preinstaladas de una TV propia; Planificar un launcher sin perder funciones necesarias — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/cleanyourtv.md) · [GitHub](https://github.com/Gathin23/cleanyourtv)

#### 🖥️ optimizerDuck
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 11.7k<br>
**Qué es:** Aplicación para revisar y ajustar opciones de rendimiento, privacidad y configuración de un equipo con Windows.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://optimizerduck.vercel.app/docs/guides/getting-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar opciones de privacidad de Windows; Revisar un ajuste concreto de rendimiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/optimizerduck.md) · [GitHub](https://github.com/itsfatduck/optimizerDuck)

#### 🖥️ universal-android-debloater-next-generation
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 10.1k<br>
**Qué es:** Interfaz para revisar y retirar paquetes preinstalados de dispositivos Android mediante ADB y listas de aplicaciones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/wiki/Getting-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar software preinstalado de un dispositivo; Preparar una selección revisada por modelo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/universal-android-debloater-next-generation.md) · [GitHub](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation)

#### 📂 40-questions
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 1.9k<br>
**Qué es:** Colección de preguntas para revisar un año o una década y reflexionar sobre objetivos, hábitos y decisiones personales.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/kepano/40-questions/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una revisión anual; Explorar prioridades y hábitos personales — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/40-questions.md) · [GitHub](https://github.com/kepano/40-questions)

### Aprendizaje asistido

#### 🖥️ OpenMAIC
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 43.6k<br>
**Qué es:** Aplicación educativa con varios agentes que prepara clases y actividades mediante modelos y recursos configurables.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una actividad de estudio; Crear un borrador de clase con materiales propios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/openmaic.md) · [GitHub](https://github.com/THU-MAIC/OpenMAIC)

---

## 🔍 16. Analizar software y comprobar su seguridad

Depuradores, descompiladores, análisis de binarios y agentes de pruebas. Trabaja sobre software propio o con autorización y separa análisis, modificación y pruebas activas.

**⚖️ ¿Cuál elegir? — ghidra, radare2, rizin**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [ghidra](human/fichas/ghidra.md) | Tu objetivo encaja con estos ejemplos: Estudiar código nativo compilado; Documentar una biblioteca propia sin símbolos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [radare2](human/fichas/radare2.md) | Tu objetivo encaja con estos ejemplos: Inspeccionar un archivo ELF propio; Estudiar instrucciones de un programa de laboratorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [rizin](human/fichas/rizin.md) | Tu objetivo encaja con estos ejemplos: Aprender análisis desde consola; Revisar metadatos de una biblioteca propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Ingeniería inversa y formatos binarios

#### 🖥️ ghidra ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 100k<br>
**Qué es:** Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar código nativo compilado; Documentar una biblioteca propia sin símbolos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ghidra.md) · [GitHub](https://github.com/NationalSecurityAgency/ghidra)

#### 🖥️ ImHex
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 55.9k<br>
**Qué es:** Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras y describir formatos mediante patrones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/WerWolv/ImHex/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un formato de archivo; Comparar dos versiones de una estructura binaria — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/imhex.md) · [GitHub](https://github.com/WerWolv/ImHex)

#### 🖥️ jadx
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 51.8k<br>
**Qué es:** Descompilador de archivos DEX y APK para explorar código Java reconstruido y recursos de aplicaciones Android.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/skylot/jadx/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una app Android propia; Documentar recursos y referencias de un APK — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/jadx.md) · [GitHub](https://github.com/skylot/jadx)

#### 🖥️ Apktool
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 27.2k<br>
**Qué es:** Herramienta para decodificar recursos y reconstruir paquetes APK de Android durante el análisis de una aplicación.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://apktool.org/wiki/the-basics/intro); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar recursos de una app Android; Revisar una configuración de manifiesto propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/apktool.md) · [GitHub](https://github.com/iBotPeaches/Apktool)

#### 🖥️ ILSpy
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 27.1k<br>
**Qué es:** Descompilador de .NET para explorar ensamblados y estudiar el código y metadatos de aplicaciones compatibles.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/icsharpcode/ILSpy/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comprender una dependencia .NET; Estudiar cómo se representa código compilado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ilspy.md) · [GitHub](https://github.com/icsharpcode/ILSpy)

#### 🖥️ radare2
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 25.4k<br>
**Qué es:** Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/radareorg/radare2/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Inspeccionar un archivo ELF propio; Estudiar instrucciones de un programa de laboratorio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/radare2.md) · [GitHub](https://github.com/radareorg/radare2)

#### 🖥️ frida
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 22.8k<br>
**Qué es:** Herramientas de instrumentación dinámica para observar y modificar el comportamiento de programas durante su ejecución.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://frida.re/docs/home/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar comportamiento dinámico de una app propia; Depurar una llamada que no aparece en logs — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/frida.md) · [GitHub](https://github.com/frida/frida)

#### 📚 angr
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 9.4k<br>
**Qué es:** Plataforma en Python para analizar programas binarios mediante técnicas como ejecución simbólica y análisis de flujo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://docs.angr.io/introductory-errata/install); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar ejecución simbólica; Analizar rutas de un binario de práctica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/angr.md) · [GitHub](https://github.com/angr/angr)

#### 🖥️ rizin
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 4.2k<br>
**Qué es:** Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://rizin.re/install/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender análisis desde consola; Revisar metadatos de una biblioteca propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/rizin.md) · [GitHub](https://github.com/rizinorg/rizin)

### Depuración e inspección de procesos

#### 🖥️ x64dbg
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 50.3k<br>
**Qué es:** Depurador de Windows para inspeccionar programas en ejecución y estudiar instrucciones, memoria y llamadas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/x64dbg/x64dbg/blob/development/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender depuración en Windows; Investigar un fallo reproducible de una app propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/x64dbg.md) · [GitHub](https://github.com/x64dbg/x64dbg)

#### 🖥️ dnSpy
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 11.5k<br>
**Qué es:** Depurador y editor de ensamblados .NET para inspeccionar y analizar aplicaciones de esa plataforma.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/dnSpyEx/dnSpy/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar estructura de una app .NET; Depurar un programa propio sin proyecto fuente completo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dnspy.md) · [GitHub](https://github.com/dnSpyEx/dnSpy)

#### 🖥️ raddebugger
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 8.8k<br>
**Qué es:** Depurador gráfico nativo para inspeccionar procesos, código y memoria durante el análisis de programas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/EpicGames/raddebugger/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender depuración nativa; Inspeccionar un fallo de una app propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/raddebugger.md) · [GitHub](https://github.com/EpicGames/raddebugger)

### Tráfico, rendimiento y pruebas

#### 🖥️ mitmproxy
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 47k<br>
**Qué es:** Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://docs.mitmproxy.org/stable/overview-installation/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/mitmproxy.md) · [GitHub](https://github.com/mitmproxy/mitmproxy)

#### 🖥️ k6
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 32.3k<br>
**Qué es:** Herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de tráfico.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://grafana.com/docs/k6/latest/set-up/install-k6/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Medir un endpoint en desarrollo; Definir un umbral reproducible de rendimiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/k6.md) · [GitHub](https://github.com/grafana/k6)

### Análisis y pruebas con agentes

#### 🎨 rea
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 460k<br>
**Qué es:** Herramientas e instrucciones para estudiar el comportamiento y la estructura de software mediante agentes de código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx rea-agents setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Entender estructura de una app propia; Comparar dos versiones de un formato de laboratorio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/rea.md) · [GitHub](https://github.com/morluto/rea)

#### 🖥️ strix
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 75.6k<br>
**Qué es:** Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/usestrix/strix/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una revisión de seguridad en laboratorio; Integrar un escaneo autorizado en CI de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/strix.md) · [GitHub](https://github.com/usestrix/strix)

#### 🖥️ shannon
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 51.9k<br>
**Qué es:** Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx @keygraph/shannon@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar una app propia en un laboratorio; Comparar evidencias y veredictos de una prueba autorizada — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/shannon.md) · [GitHub](https://github.com/KeygraphHQ/shannon)

#### 🖥️ craft-anything
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 32.9k<br>
**Qué es:** Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/storytold/craft-anything && cd craft-anything
cargo run --release -p craft-anything                # the desktop app
cargo install --path apps/craft-anything-cli         # the CLI, as `craft-anything-cli`
craft-anything-cli doctor                            # checks the install, coding agents and engines` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comprender una implementación propia existente; Comparar comportamiento antes de una reimplementación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/craft-anything.md) · [GitHub](https://github.com/storytold/craft-anything)

### Protección y verificación de software

#### 🛡️ Semgrep ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 17.7k<br>
**Qué es:** Análisis estático ligero para muchos lenguajes con reglas que se parecen al código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv tool install semgrep` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Defending Code Reference Harness](human/fichas/defending-code-reference-harness.md)<br>
**Más:** [ficha completa](human/fichas/semgrep.md) · [GitHub](https://github.com/semgrep/semgrep)

#### 🖥️ bla
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 5.7k<br>
**Qué es:** Herramientas para aplicar protecciones y comprobar superficies de software frente a análisis automatizado por agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx bla-agents setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar protección de artefactos propios; Evaluar compatibilidad de un endurecimiento con tus pruebas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/bla.md) · [GitHub](https://github.com/qybaihe/bla)

### Directorios y aprendizaje

#### 📂 awesome-reverse-engineering
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 2.1k<br>
**Qué es:** Directorio de herramientas y recursos para aprender análisis de binarios, aplicaciones, firmware y protocolos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/morluto/awesome-reverse-engineering/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar un analizador de ELF; Encontrar material introductorio de ensamblador — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/awesome-reverse-engineering.md) · [GitHub](https://github.com/morluto/awesome-reverse-engineering)

#### 📂 awesome-ai-reverse-engineering
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 108<br>
**Qué es:** Directorio de herramientas de ingeniería inversa y análisis de software que pueden trabajar con agentes de IA.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/zhuyansen/awesome-ai-reverse-engineering/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una integración MCP para análisis; Comparar herramientas con backends locales — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/awesome-ai-reverse-engineering.md) · [GitHub](https://github.com/zhuyansen/awesome-ai-reverse-engineering)

### Skills de análisis y seguridad

#### 🧠 security-audit-skill
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 72.7k<br>
**Qué es:** Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add https://github.com/cloudflare/security-audit-skill \
  --skill security-audit` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una revisión de código autorizada; Evaluar la calidad de hallazgos generados por un agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/security-audit-skill.md) · [GitHub](https://github.com/cloudflare/security-audit-skill)

#### 🎨 Cybersecurity Skills (comunidad)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 36.2k<br>
**Qué es:** Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una revisión de configuración; Preparar un ejercicio de respuesta defensiva — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/cybersecurity-skills.md) · [GitHub](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)

#### 🛡️ SkillSpector
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 26.1k<br>
**Qué es:** Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate

# Install for production use
make install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Examinar una skill antes de incorporarla al agente; Añadir un escaneo de skills a una revisión de cambios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Agentic Awesome Skills (AAS)](human/fichas/antigravity-awesome-skills.md)<br>
**Más:** [ficha completa](human/fichas/skillspector.md) · [GitHub](https://github.com/NVIDIA/SkillSpector)

#### 🛡️ Defending Code Reference Harness
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 7.8k<br>
**Qué es:** Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/anthropics/defending-code-reference-harness
cd defending-code-reference-harness
claude` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender un flujo de modelado de amenazas; Priorizar y revisar parches en software autorizado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Semgrep](human/fichas/semgrep.md)<br>
**Más:** [ficha completa](human/fichas/defending-code-reference-harness.md) · [GitHub](https://github.com/anthropics/defending-code-reference-harness)

---

## 🤖 17. WhatsApp, mensajería y chatbots

Conecta WhatsApp y otros canales o prepara un chatbot. Distingue el canal de mensajes, el modelo que responde y la bandeja donde una persona retoma la conversación.

**⚖️ ¿Cuál elegir? — whatsapp-web.js, Baileys, evolution-api, WAHA**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [whatsapp-web.js](human/fichas/whatsapp-web-js.md) | Tu objetivo encaja con estos ejemplos: Estudiar un bot de atención en laboratorio; Conectar eventos WhatsApp Web a una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Baileys](human/fichas/baileys.md) | Tu objetivo encaja con estos ejemplos: Aprender el flujo multidispositivo; Conectar eventos de una cuenta propia a una app | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [evolution-api](human/fichas/evolution-api.md) | Tu objetivo encaja con estos ejemplos: Conectar atención de WhatsApp a una app; Recibir eventos en una automatización de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [WAHA](human/fichas/waha.md) | Tu objetivo encaja con estos ejemplos: Prototipar un webhook de mensajería; Evaluar un gateway HTTP para una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### WhatsApp y mensajería

#### 💬 whatsapp-web.js ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 22.9k<br>
**Qué es:** Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install whatsapp-web.js` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un bot de atención en laboratorio; Conectar eventos WhatsApp Web a una app propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [Ollama](human/fichas/ollama.md) · [chatwoot](human/fichas/chatwoot.md)<br>
**Más:** [ficha completa](human/fichas/whatsapp-web-js.md) · [GitHub](https://github.com/wwebjs/whatsapp-web.js)

#### 🌐 OpenWA
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 16.9k<br>
**Qué es:** Gateway autoalojado de WhatsApp con API, panel de sesiones y servidor MCP HTTP opcional, del proyecto rmyndharis/OpenWA.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access (the dashboard is bundled into the API image and served on the same port)
# Dashboard: http://localhost:2785
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una integración de mensajería; Consultar estados desde un agente MCP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [chatwoot](human/fichas/chatwoot.md) · [Typebot](human/fichas/typebot.md) · [n8n](human/fichas/n8n.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/openwa.md) · [GitHub](https://github.com/rmyndharis/OpenWA)

#### 💬 Baileys
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 11.6k<br>
**Qué es:** Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender el flujo multidispositivo; Conectar eventos de una cuenta propia a una app — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [n8n](human/fichas/n8n.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/baileys.md) · [GitHub](https://github.com/WhiskeySockets/Baileys)

#### 🧬 evolution-api
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 10.1k<br>
**Qué es:** API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/evolution-foundation/evolution-api/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar atención de WhatsApp a una app; Recibir eventos en una automatización de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [chatwoot](human/fichas/chatwoot.md) · [Typebot](human/fichas/typebot.md) · [dify](human/fichas/dify.md)<br>
**Más:** [ficha completa](human/fichas/evolution-api.md) · [GitHub](https://github.com/evolution-foundation/evolution-api)

#### 🤖 whatsmeow
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 7.9k<br>
**Qué es:** Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/tulir/whatsmeow/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una integración de eventos en Go; Estudiar almacenamiento de sesiones WhatsApp Web — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [Ollama](human/fichas/ollama.md) · [chatwoot](human/fichas/chatwoot.md)<br>
**Más:** [ficha completa](human/fichas/whatsmeow.md) · [GitHub](https://github.com/tulir/whatsmeow)

#### 💬 WAHA
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 7.8k<br>
**Qué es:** API REST de WhatsApp en un contenedor Docker, con varios motores y panel web.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run -it --rm -p 3000:3000/tcp --name waha devlikeapro/waha` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un webhook de mensajería; Evaluar un gateway HTTP para una app propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [chatwoot](human/fichas/chatwoot.md) · [Typebot](human/fichas/typebot.md)<br>
**Más:** [ficha completa](human/fichas/waha.md) · [GitHub](https://github.com/devlikeapro/waha)

#### 🤖 whatsapp-agentkit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 567<br>
**Qué es:** Instrucciones y scripts que guían a Claude Code para construir un bot de WhatsApp; el bot resultante necesita sus propios proveedores y credenciales.<br>
**Acceso:** API de IA necesaria · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/Hainrixz/whatsapp-agentkit.git
cd whatsapp-agentkit
bash start.sh` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un asistente de preguntas frecuentes; Diseñar una consulta de horarios en un número de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [chatwoot](human/fichas/chatwoot.md) · [coolify](human/fichas/coolify.md)<br>
**Más:** [ficha completa](human/fichas/whatsapp-agentkit.md) · [GitHub](https://github.com/Hainrixz/whatsapp-agentkit)

### Chatbots y asistentes conversacionales

#### 🤖 Typebot ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 10.6k<br>
**Qué es:** Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.typebot.io/self-hosting/get-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un formulario conversacional; Probar un flujo de preguntas frecuentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [chatwoot](human/fichas/chatwoot.md) · [n8n](human/fichas/n8n.md) · [OpenWA](human/fichas/openwa.md)<br>
**Más:** [ficha completa](human/fichas/typebot.md) · [GitHub](https://github.com/baptisteArno/typebot.io)

#### 🤖 Botpress
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 15k<br>
**Qué es:** El repositorio actual reúne paquetes e integraciones abiertas y un CLI para crear y desplegar extensiones. Botpress Cloud y sus modelos tienen condiciones de servicio separadas. Clonar este código no instala toda la plataforma alojada.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g @botpress/cli # for npm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender el SDK de integraciones Botpress; Prototipar una conexión para un chatbot alojado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [Odoo](human/fichas/odoo.md) · [cal.diy](human/fichas/cal-diy.md)<br>
**Más:** [ficha completa](human/fichas/botpress.md) · [GitHub](https://github.com/botpress/botpress)

### Comunidades,chat y llamadas

#### 🌐 fluxer
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 10.9k<br>
**Qué es:** Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/fluxerapp/fluxer/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar conversación de una comunidad; Probar una interfaz de mensajería y VoIP propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [Ollama](human/fichas/ollama.md) · [coolify](human/fichas/coolify.md)<br>
**Más:** [ficha completa](human/fichas/fluxer.md) · [GitHub](https://github.com/fluxerapp/fluxer)

---

## 🤖 18. CRM, ventas y marketing

Gestiona clientes, soporte, campañas, correo y publicaciones. Un CRM guarda la relación con el cliente; una herramienta de campañas distribuye mensajes. Comprueba los servicios externos y sus tarifas.

**⚖️ ¿Cuál elegir? — Odoo, ERPNext**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Odoo](human/fichas/odoo.md) | Tu objetivo encaja con estos ejemplos: Evaluar un CRM para un negocio; Estudiar cómo se conectan ventas e inventario | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [ERPNext](human/fichas/erpnext.md) | Tu objetivo encaja con estos ejemplos: Evaluar inventario y ventas; Estudiar un ERP con datos de muestra | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### CRM, ERP y soporte al cliente

#### 👥 Odoo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 55.8k<br>
**Qué es:** Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://www.odoo.com/documentation/master/administration/install/install.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar un CRM para un negocio; Estudiar cómo se conectan ventas e inventario — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [metabase](human/fichas/metabase.md) · [Botpress](human/fichas/botpress.md)<br>
**Más:** [ficha completa](human/fichas/odoo.md) · [GitHub](https://github.com/odoo/odoo)

#### 👥 twenty-main
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 60.9k<br>
**Qué es:** CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/twentyhq/twenty/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Modelar un proceso comercial propio; Desarrollar una app sobre un CRM — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [n8n](human/fichas/n8n.md) · [evolution-api](human/fichas/evolution-api.md) · [cal.diy](human/fichas/cal-diy.md)<br>
**Más:** [ficha completa](human/fichas/twenty-main.md) · [GitHub](https://github.com/twentyhq/twenty)

#### 👥 ERPNext
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 41.3k<br>
**Qué es:** ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/frappe/frappe_docker
cd frappe_docker

docker compose -f pwd.yml up -d` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar inventario y ventas; Estudiar un ERP con datos de muestra — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [metabase](human/fichas/metabase.md) · [paperless-ngx](human/fichas/paperless-ngx.md)<br>
**Más:** [ficha completa](human/fichas/erpnext.md) · [GitHub](https://github.com/frappe/erpnext)

#### 💬 chatwoot
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 39.9k<br>
**Qué es:** Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/chatwoot/chatwoot/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una mesa de soporte; Comparar atención humana y asistencia AI — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [evolution-api](human/fichas/evolution-api.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/chatwoot.md) · [GitHub](https://github.com/chatwoot/chatwoot)

#### 🤖 crm
**Etiquetas:** Ejecución ☁️ cloud/API · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 12.1k<br>
**Qué es:** CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/trycompai/crm.git && cd crm
cp .env.example .env          # then fill in the values below
bun install

docker compose up -d          # Postgres on :5432

bun run db:deploy             # apply migrations
bun run db:seed               # optional: a believable pipeline to look at
bun run dev` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un CRM con investigación de contactos; Organizar tareas con evidencia de su origen — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [sellbird](human/fichas/sellbird.md) · [cal.diy](human/fichas/cal-diy.md) · [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/compai-crm.md) · [GitHub](https://github.com/trycompai/crm)

### Email, marketing y notificaciones

#### 🔔 novu ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 40.3k<br>
**Qué es:** Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.novu.co/platform/quickstart); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir una bandeja de notificaciones a una app; Coordinar avisos de email y chat — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [AI SDK (Vercel)](human/fichas/vercel-ai.md) · [LangGraph](human/fichas/langgraph.md) · [listmonk](human/fichas/listmonk.md)<br>
**Más:** [ficha completa](human/fichas/novu.md) · [GitHub](https://github.com/novuhq/novu)

#### ⚙️ postiz-app
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 41.6k<br>
**Qué es:** Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.postiz.com/quickstart); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar un calendario de contenido; Evaluar generación asistida de borradores — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [Claude Code](human/fichas/claude-code.md) · [coolify](human/fichas/coolify.md)<br>
**Más:** [ficha completa](human/fichas/postiz-app.md) · [GitHub](https://github.com/gitroomhq/postiz-app)

#### ⚙️ open-seo
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 27.7k<br>
**Qué es:** Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/every-app/open-seo/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Investigar palabras clave de una web propia; Preparar una revisión técnica SEO — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [coolify](human/fichas/coolify.md) · [GEO-SEO Claude](human/fichas/geo-seo-claude.md)<br>
**Más:** [ficha completa](human/fichas/open-seo.md) · [GitHub](https://github.com/every-app/open-seo)

#### 📬 listmonk
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 24.3k<br>
**Qué es:** Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Download the compose file to the current directory.
curl -LO https://github.com/knadh/listmonk/raw/master/docker-compose.yml

# Run the services in the background.
docker compose up -d` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Gestionar una newsletter propia; Evaluar segmentación de una lista de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [novu](human/fichas/novu.md) · [postiz-app](human/fichas/postiz-app.md)<br>
**Más:** [ficha completa](human/fichas/listmonk.md) · [GitHub](https://github.com/knadh/listmonk)

#### ⚙️ cloud-mail
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 16k<br>
**Qué es:** Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/maillab/cloud-mail/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar correo sobre Workers; Gestionar buzones de un dominio de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [open-seo](human/fichas/open-seo.md) · [changedetection.io](human/fichas/changedetection.md)<br>
**Más:** [ficha completa](human/fichas/cloud-mail.md) · [GitHub](https://github.com/maillab/cloud-mail)

#### 📣 mautic
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 11k<br>
**Qué es:** Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.mautic.org/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar segmentación de audiencias; Prototipar una secuencia de marketing — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [Marketing Skills](human/fichas/marketingskills.md) · [posthog](human/fichas/posthog.md)<br>
**Más:** [ficha completa](human/fichas/mautic.md) · [GitHub](https://github.com/mautic/mautic)

#### 🖥️ sellbird
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 5.6k<br>
**Qué es:** Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# 1. Install. Use python3.13, not python3: on macOS bare python3 is 3.9.
python3.13 -m venv .venv && source .venv/bin/activate && pip install -e .` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un borrador de prospección; Evaluar criterios de selección de empresas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [crm](human/fichas/compai-crm.md)<br>
**Más:** [ficha completa](human/fichas/sellbird.md) · [GitHub](https://github.com/ethanplusai/sellbird)

### Reservas y programación de citas

#### 🤖 cal.diy
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 50k<br>
**Qué es:** Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/calcom/cal.diy/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Experimentar con una agenda personal autoalojada; Probar la duración y disponibilidad de distintos tipos de cita — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md) · [twenty-main](human/fichas/twenty-main.md) · [Botpress](human/fichas/botpress.md)<br>
**Más:** [ficha completa](human/fichas/cal-diy.md) · [GitHub](https://github.com/calcom/cal.diy)

---

## 🧠 19. Aprender IA y escribir mejores prompts

Cursos, ejemplos, guías y colecciones de prompts. Son material de aprendizaje: cada ejemplo puede necesitar sus propias cuentas, dependencias o modelos.

**⚖️ ¿Cuál elegir? — Prompt Engineering Guide, Anthropic's Prompt Engineering Tutorial**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Prompt Engineering Guide](human/fichas/prompt-engineering-guide.md) | Tu objetivo encaja con estos ejemplos: Aprender a pedir un resumen estructurado; Comparar técnicas de prompting antes de elegir una | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Anthropic's Prompt Engineering Tutorial](human/fichas/prompt-eng-tutorial.md) | Tu objetivo encaja con estos ejemplos: Practicar instrucciones claras; Aprender a separar datos y órdenes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Fabric, prompts.chat**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Fabric](human/fichas/fabric.md) | Tu objetivo encaja con estos ejemplos: Extraer acciones de una reunión; Convertir notas en un esquema de artículo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [prompts.chat](human/fichas/prompts-chat.md) | Tu objetivo encaja con estos ejemplos: Encontrar una plantilla para estudiar; Compartir una biblioteca interna de prompts | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Generative AI for Beginners, LLM Course, LLMs from Scratch**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Generative AI for Beginners](human/fichas/generative-ai-for-beginners.md) | Tu objetivo encaja con estos ejemplos: Empezar a construir una app generativa; Comparar nube con Foundry Local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LLM Course](human/fichas/llm-course.md) | Tu objetivo encaja con estos ejemplos: Crear un plan de aprendizaje de LLM; Estudiar cuantización GGUF | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LLMs from Scratch](human/fichas/llms-from-scratch.md) | Tu objetivo encaja con estos ejemplos: Aprender cómo funciona un Transformer; Estudiar ajuste de instrucciones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Awesome LLM Apps, OpenAI Cookbook, Claude Cookbooks**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Awesome LLM Apps](human/fichas/awesome-llm-apps.md) | Tu objetivo encaja con estos ejemplos: Aprender con un asistente de viajes; Estudiar un RAG con Llama local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [OpenAI Cookbook](human/fichas/openai-cookbook.md) | Tu objetivo encaja con estos ejemplos: Extraer campos de un texto; Aprender a evaluar respuestas de una aplicación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Claude Cookbooks](human/fichas/claude-cookbooks.md) | Tu objetivo encaja con estos ejemplos: Clasificar tickets ficticios; Estudiar llamadas a herramientas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Prompts y prompt engineering

#### 💡 Prompt Engineering Guide ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 80.1k<br>
**Qué es:** Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender a pedir un resumen estructurado; Comparar técnicas de prompting antes de elegir una — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md)<br>
**Más:** [ficha completa](human/fichas/prompt-engineering-guide.md) · [GitHub](https://github.com/dair-ai/Prompt-Engineering-Guide)

#### 💡 Fabric ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 44.6k<br>
**Qué es:** CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `go install github.com/danielmiessler/fabric/cmd/fabric@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer acciones de una reunión; Convertir notas en un esquema de artículo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [yt-dlp](human/fichas/yt-dlp.md)<br>
**Más:** [ficha completa](human/fichas/fabric.md) · [GitHub](https://github.com/danielmiessler/Fabric)

#### 💡 prompts.chat
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 177k<br>
**Qué es:** La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/f/prompts.chat/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una plantilla para estudiar; Compartir una biblioteca interna de prompts — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/prompts-chat.md) · [GitHub](https://github.com/f/prompts.chat)

#### 🧠 system-prompts-and-models-of-ai-tools
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 145k<br>
**Qué es:** Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar instrucciones de herramientas de código; Preparar una plantilla propia de sistema — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/system-prompts-and-models-of-ai-tools.md) · [GitHub](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

#### 💡 Anthropic's Prompt Engineering Tutorial
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 39.3k<br>
**Qué es:** Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/prompt-eng-interactive-tutorial/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Practicar instrucciones claras; Aprender a separar datos y órdenes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Cookbooks](human/fichas/claude-cookbooks.md)<br>
**Más:** [ficha completa](human/fichas/prompt-eng-tutorial.md) · [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial)

#### 🎯 prompt-master
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 16k<br>
**Qué es:** Skill que recopila contexto y restricciones para redactar prompts destinados a herramientas de código, imagen y otros servicios. La instalación documentada corresponde a Claude; los nombres de otros productos describen destinos de los prompts generados.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `mkdir -p ~/.claude/skills
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Redactar un encargo de programación; Preparar un prompt de imagen con requisitos concretos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md)<br>
**Más:** [ficha completa](human/fichas/prompt-master.md) · [GitHub](https://github.com/nidhinjs/prompt-master)

#### 🧠 ChatGPT_DAN
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 13.2k<br>
**Qué es:** Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/0xk1h0/ChatGPT_DAN/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar la historia de prompts de roleplay; Reconocer intentos de manipulación de instrucciones — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/chatgpt-dan.md) · [GitHub](https://github.com/0xk1h0/ChatGPT_DAN)

#### 🧠 chatgpt_system_prompt
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 10.9k<br>
**Qué es:** Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/LouisShark/chatgpt_system_prompt/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender estructura de instrucciones; Diseñar límites para un asistente propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/chatgpt-system-prompt.md) · [GitHub](https://github.com/LouisShark/chatgpt_system_prompt)

### Guías, cursos y cookbooks

#### 🎓 Generative AI for Beginners ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 124k<br>
**Qué es:** Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/generative-ai-for-beginners/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Empezar a construir una app generativa; Comparar nube con Foundry Local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [AI Agents for Beginners](human/fichas/ai-agents-for-beginners.md) · [MCP for Beginners](human/fichas/mcp-for-beginners.md)<br>
**Más:** [ficha completa](human/fichas/generative-ai-for-beginners.md) · [GitHub](https://github.com/microsoft/generative-ai-for-beginners)

#### 🎓 AI Agents for Beginners ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 79.6k<br>
**Qué es:** Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/ai-agents-for-beginners/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender patrones de agentes; Estudiar herramientas y memoria con ejemplos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Generative AI for Beginners](human/fichas/generative-ai-for-beginners.md) · [Microsoft Agent Framework](human/fichas/agent-framework.md) · [MCP for Beginners](human/fichas/mcp-for-beginners.md)<br>
**Más:** [ficha completa](human/fichas/ai-agents-for-beginners.md) · [GitHub](https://github.com/microsoft/ai-agents-for-beginners)

#### 🎓 Awesome LLM Apps
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 145k<br>
**Qué es:** Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender con un asistente de viajes; Estudiar un RAG con Llama local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [streamlit](human/fichas/streamlit.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md) · [Agent Development Kit (ADK)](human/fichas/adk-python.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/awesome-llm-apps.md) · [GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps)

#### 🎓 OpenAI Cookbook
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 77.1k<br>
**Qué es:** Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales.<br>
**Acceso:** API de IA opcional · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/openai/openai-cookbook/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer campos de un texto; Aprender a evaluar respuestas de una aplicación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [openai-python](human/fichas/openai-python.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md)<br>
**Más:** [ficha completa](human/fichas/openai-cookbook.md) · [GitHub](https://github.com/openai/openai-cookbook)

#### 🎓 Claude Cookbooks
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 54.7k<br>
**Qué es:** Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización.<br>
**Acceso:** API de IA opcional · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/claude-cookbooks/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar tickets ficticios; Estudiar llamadas a herramientas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Anthropic's Prompt Engineering Tutorial](human/fichas/prompt-eng-tutorial.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [promptfoo](human/fichas/promptfoo.md)<br>
**Más:** [ficha completa](human/fichas/claude-cookbooks.md) · [GitHub](https://github.com/anthropics/claude-cookbooks)

#### 🧠 ai-engineering-hub
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 41.9k<br>
**Qué es:** Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/patchy631/ai-engineering-hub/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender RAG con Ollama; Comparar técnicas de ajuste fino — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ai-engineering-hub.md) · [GitHub](https://github.com/patchy631/ai-engineering-hub)

#### 🧠 500-AI-Agents-Projects
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 39.9k<br>
**Qué es:** Colección de casos de uso y agentes autocontenidos, junto con enlaces a implementaciones externas.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una idea de agente para un sector; Comparar un ejemplo local con uno por API — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/500-ai-agents-projects.md) · [GitHub](https://github.com/ashishpatel26/500-AI-Agents-Projects)

#### 🎓 12-Factor Agents
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 27.2k<br>
**Qué es:** Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12 Factor Apps.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/humanlayer/12-factor-agents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar un diseño antes de programar; Estudiar recuperación de errores en agentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md) · [LangGraph](human/fichas/langgraph.md) · [AI SDK (Vercel)](human/fichas/vercel-ai.md)<br>
**Más:** [ficha completa](human/fichas/12-factor-agents.md) · [GitHub](https://github.com/humanlayer/12-factor-agents)

#### 🎓 Agents Towards Production
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 21.9k<br>
**Qué es:** Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad, trazas y evaluación.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/NirDiamant/agents-towards-production.git
cd agents-towards-production` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender a desplegar un agente; Comparar un servicio LLM con Ollama on-prem — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [mem0](human/fichas/mem0.md) · [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/agents-towards-production.md) · [GitHub](https://github.com/NirDiamant/agents-towards-production)

#### 🧠 claude-quickstarts
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 21k<br>
**Qué es:** Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora.<br>
**Acceso:** API de IA opcional · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/anthropics/claude-quickstarts/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar soporte con Claude; Estudiar una demo de uso de computadora — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-quickstarts.md) · [GitHub](https://github.com/anthropics/claude-quickstarts)

#### 🎓 Loop Engineering
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 11.8k<br>
**Qué es:** Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx @cobusgreyling/loop init . --pattern daily-triage --tool claude
npx @cobusgreyling/loop doctor .` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar un ciclo de revisión de issues; Estimar el coste de un bucle antes de automatizarlo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [superpowers](human/fichas/superpowers.md)<br>
**Más:** [ficha completa](human/fichas/loop-engineering.md) · [GitHub](https://github.com/cobusgreyling/loop-engineering)

#### 🧩 Context-Engineering
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 9.3k<br>
**Qué es:** Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/jasontang-ai/Context-Engineering/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar contexto para una tarea larga; Estudiar memoria y recuperación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md) · [headroom](human/fichas/headroom.md)<br>
**Más:** [ficha completa](human/fichas/context-engineering.md) · [GitHub](https://github.com/jasontang-ai/Context-Engineering)

#### 📂 awesome-harness-engineering
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 5.2k<br>
**Qué es:** Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ai-boost/awesome-harness-engineering/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar el entorno de un agente; Encontrar recursos de evaluación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/awesome-harness-engineering.md) · [GitHub](https://github.com/ai-boost/awesome-harness-engineering)

#### 📂 mvanhorn
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 53<br>
**Qué es:** Perfil público de mvanhorn para consultar sus proyectos, herramientas y contribuciones de desarrollo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mvanhorn/mvanhorn/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar herramientas de un autor; Explorar contribuciones a otros proyectos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/mvanhorn.md) · [GitHub](https://github.com/mvanhorn/mvanhorn)

### Aprender LLMs desde cero

#### 📘 LLM Course ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 85.1k<br>
**Qué es:** Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/mlabonne/llm-course/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un plan de aprendizaje de LLM; Estudiar cuantización GGUF — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Unsloth](human/fichas/unsloth.md) · [LLaMA-Factory](human/fichas/llama-factory.md)<br>
**Más:** [ficha completa](human/fichas/llm-course.md) · [GitHub](https://github.com/mlabonne/llm-course)

#### 📘 LLMs from Scratch
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 108k<br>
**Qué es:** Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender cómo funciona un Transformer; Estudiar ajuste de instrucciones — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [PyTorch](human/fichas/pytorch.md)<br>
**Más:** [ficha completa](human/fichas/llms-from-scratch.md) · [GitHub](https://github.com/rasbt/LLMs-from-scratch)

#### 🧑‍💻 awesome-machine-learning
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 74.8k<br>
**Qué es:** Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/josephmisiti/awesome-machine-learning/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Descubrir bibliotecas de clasificación; Encontrar herramientas de visión por lenguaje — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/awesome-machine-learning.md) · [GitHub](https://github.com/josephmisiti/awesome-machine-learning)

#### 💬 nanochat
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 60.6k<br>
**Qué es:** Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv sync --extra cpu    # (or) Use for CPU-only / MPS` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una cadena de entrenamiento a chat; Reproducir un experimento con presupuesto delimitado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/nanochat.md) · [GitHub](https://github.com/karpathy/nanochat)

#### ⚙️ llm.c
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 31.5k<br>
**Qué es:** Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/karpathy/llm.c/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar entrenamiento sin un framework pesado; Comparar una implementación C con PyTorch — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/llm-c.md) · [GitHub](https://github.com/karpathy/llm.c)

#### 🧑‍💻 train-llm-from-scratch
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 13.2k<br>
**Qué es:** Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/FareedKhan-dev/train-llm-from-scratch.git
cd train-llm-from-scratch
pip install -e .` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comprender la preparación de un corpus; Explorar un entrenamiento pequeño controlado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/train-llm-from-scratch.md) · [GitHub](https://github.com/FareedKhan-dev/train-llm-from-scratch)

#### 🧑‍💻 python-machine-learning-book
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟡 medio · ⭐ 12.7k<br>
**Qué es:** Código de la primera edición del libro Python Machine Learning, con ejemplos de algoritmos y evaluación.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/rasbt/python-machine-learning-book/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender regresión y clasificación; Entender validación de modelos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/python-machine-learning-book.md) · [GitHub](https://github.com/rasbt/python-machine-learning-book)

#### 📘 how-to-train-your-gpt
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 4.2k<br>
**Qué es:** Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Install everything you need
pip install jupyter tiktoken torch numpy datasets matplotlib --index-url https://download.pytorch.org/whl/cpu

# Start with chapter 2 (tokenization)
jupyter notebook notebooks/02_tokenization.ipynb` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender tokenización paso a paso; Comprender atención con ejemplos pequeños — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [nanochat](human/fichas/nanochat.md)<br>
**Más:** [ficha completa](human/fichas/how-to-train-your-gpt.md) · [GitHub](https://github.com/raiyanyahya/how-to-train-your-gpt)

---

## 🕸️ 20. Programar con agentes de código

Agentes de terminal, extensiones de editor y entornos para programar con IA. Revisa qué cliente utilizas, cómo inicia sesión y si el modelo usa un plan, una API o un servidor local.

**⚖️ ¿Cuál elegir? — OpenCode, Claude Code, Codex CLI, Gemini CLI, Cline, Open Interpreter, goose**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OpenCode](human/fichas/opencode.md) | Tu objetivo encaja con estos ejemplos: Comprender un repositorio nuevo; Planificar una corrección pequeña | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Claude Code](human/fichas/claude-code.md) | Tu objetivo encaja con estos ejemplos: Entender código sin editar; Preparar una propuesta de corrección | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Codex CLI](human/fichas/codex.md) | Tu objetivo encaja con estos ejemplos: Explorar un proyecto; Preparar un cambio y revisar su diff | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Gemini CLI](human/fichas/gemini-cli.md) | Tu objetivo encaja con estos ejemplos: Estudiar un agente empresarial de Google; Planificar una migración de CLI | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Cline](human/fichas/cline.md) | Tu objetivo encaja con estos ejemplos: Explicar un error de código; Comparar una propuesta antes de editar | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Open Interpreter](human/fichas/open-interpreter.md) | Tu objetivo encaja con estos ejemplos: Probar un agente con distintos harnesses; Reutilizar un cliente del SDK de Codex | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [goose](human/fichas/goose.md) | Tu objetivo encaja con estos ejemplos: Automatizar una tarea de desarrollo; Comparar agentes conectados por ACP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — OpenHands, Open SWE**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OpenHands](human/fichas/openhands.md) | Tu objetivo encaja con estos ejemplos: Centralizar sesiones de agentes; Preparar una automatización de ingeniería | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Open SWE](human/fichas/open-swe.md) | Tu objetivo encaja con estos ejemplos: Diseñar una fábrica interna de cambios; Estudiar un agente asíncrono con revisión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Agentes de terminal

#### 👨‍💻 OpenCode ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 227k<br>
**Qué es:** Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm i -g @opencode/cli@latest      # or bun/pnpm/yarn` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comprender un repositorio nuevo; Planificar una corrección pequeña — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md) · [Awesome Agent Skills](human/fichas/awesome-agent-skills.md)<br>
**Más:** [ficha completa](human/fichas/opencode.md) · [GitHub](https://github.com/anomalyco/opencode)

#### 👨‍💻 Claude Code ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 156k<br>
**Qué es:** Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `winget install Anthropic.ClaudeCode` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Entender código sin editar; Preparar una propuesta de corrección — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [superpowers](human/fichas/superpowers.md) · [Anthropic Skills](human/fichas/anthropic-skills.md) · [claude-mem](human/fichas/claude-mem.md) · [Context7](human/fichas/context7.md)<br>
**Más:** [ficha completa](human/fichas/claude-code.md) · [GitHub](https://github.com/anthropics/claude-code)

#### 👨‍💻 Codex CLI
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 135k<br>
**Qué es:** Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Install using npm
npm install -g @openai/codex` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un proyecto; Preparar un cambio y revisar su diff — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Agent Skills (Addy Osmani)](human/fichas/agent-skills.md) · [Spec Kit](human/fichas/spec-kit.md) · [Context7](human/fichas/context7.md)<br>
**Más:** [ficha completa](human/fichas/codex.md) · [GitHub](https://github.com/openai/codex)

#### 👨‍💻 Gemini CLI
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 109k<br>
**Qué es:** Agente de terminal de Google. Su aviso actual diferencia el acceso empresarial de Gemini Code Assist, Antigravity CLI para usuarios individuales y Gemini API CLI para llamadas sin estado. Revisa esa distinción antes de instalar o asumir una cuota gratuita.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Using npx (no installation required)
npx @google/gemini-cli` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un agente empresarial de Google; Planificar una migración de CLI — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Stitch Skills](human/fichas/stitch-skills.md) · [Context7](human/fichas/context7.md)<br>
**Más:** [ficha completa](human/fichas/gemini-cli.md) · [GitHub](https://github.com/google-gemini/gemini-cli)

#### 👨‍💻 Open Interpreter
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 68.9k<br>
**Qué es:** Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://www.openinterpreter.com/docs/terminal/install); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un agente con distintos harnesses; Reutilizar un cliente del SDK de Codex — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [E2B](human/fichas/e2b.md)<br>
**Más:** [ficha completa](human/fichas/open-interpreter.md) · [GitHub](https://github.com/openinterpreter/openinterpreter)

#### 👨‍💻 goose
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 56.6k<br>
**Qué es:** Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://goose-docs.ai/docs/getting-started/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar una tarea de desarrollo; Comparar agentes conectados por ACP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Playwright MCP](human/fichas/playwright-mcp.md) · [GitHub MCP Server](human/fichas/github-mcp-server.md)<br>
**Más:** [ficha completa](human/fichas/goose.md) · [GitHub](https://github.com/aaif-goose/goose)

#### 👨‍💻 Aider
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 50.1k<br>
**Qué es:** Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `python -m pip install aider-install
aider-install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Corregir una función pequeña; Programar en pareja desde terminal — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/aider.md) · [GitHub](https://github.com/Aider-AI/aider)

#### 🕸️ openclaude
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 34.4k<br>
**Qué es:** Agente de código abierto para terminal que conecta proveedores remotos y modelos locales con herramientas y MCP.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g @twigpine/openclaude@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Usar un agente con Ollama; Comparar un backend API con Codex OAuth — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/openclaude.md) · [GitHub](https://github.com/Twigpine/openclaude)

#### 🕸️ MiMo-Code
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 13.8k<br>
**Qué es:** Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente de terminal; Estudiar memoria y herramientas del proyecto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/mimo-code.md) · [GitHub](https://github.com/XiaomiMiMo/MiMo-Code)

### Editores y extensiones de código

#### 👨‍💻 Cline
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 71.6k<br>
**Qué es:** Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm i -g cline` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar un error de código; Comparar una propuesta antes de editar — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Context7](human/fichas/context7.md) · [Playwright MCP](human/fichas/playwright-mcp.md)<br>
**Más:** [ficha completa](human/fichas/cline.md) · [GitHub](https://github.com/cline/cline)

#### 🖥️ openidea
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 9k<br>
**Qué es:** Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/l0ng-ai/openidea/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar código con atajos tipo IntelliJ; Probar un editor nativo con plugins — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/openidea.md) · [GitHub](https://github.com/l0ng-ai/openidea)

#### 🕸️ OpenCursor
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.1k<br>
**Qué es:** Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/PawanOsman/OpenCursor/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Trabajar con un agente dentro de VS Code; Comparar inferencia local con cuenta remota — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/opencursor.md) · [GitHub](https://github.com/PawanOsman/OpenCursor)

### Agentes para issues y tareas de ingeniería

#### 🙌 OpenHands
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 93.5k<br>
**Qué es:** Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g @openhands/agent-canvas
agent-canvas` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Centralizar sesiones de agentes; Preparar una automatización de ingeniería — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ECC](human/fichas/ecc.md) · [sandbox](human/fichas/sandbox.md)<br>
**Más:** [ficha completa](human/fichas/openhands.md) · [GitHub](https://github.com/OpenHands/OpenHands)

#### 👨‍💻 Open SWE
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 11.2k<br>
**Qué es:** Robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisables.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/langchain-ai/open-swe/blob/main/docs/INSTALLATION.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una fábrica interna de cambios; Estudiar un agente asíncrono con revisión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [E2B](human/fichas/e2b.md)<br>
**Más:** [ficha completa](human/fichas/open-swe.md) · [GitHub](https://github.com/langchain-ai/open-swe)

### Interfaces para gestionar sesiones

#### 👨‍💻 T3 Code
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 60.6k<br>
**Qué es:** Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Controlar una sesión desde otro dispositivo; Comparar trabajo de Claude Code y Codex — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md) · [OpenCode](human/fichas/opencode.md)<br>
**Más:** [ficha completa](human/fichas/t3code.md) · [GitHub](https://github.com/pingdotgg/t3code)

#### 🖥️ opencode-manager
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 1.1k<br>
**Qué es:** Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://opencodemanager.app/docs/getting-started/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Gestionar sesiones desde el navegador; Consultar un proyecto desde el móvil — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/opencode-manager.md) · [GitHub](https://github.com/chriswritescode-dev/opencode-manager)

### Desarrollo móvil y de juegos

#### 📚 dsh-game-studio
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 556<br>
**Qué es:** Plugin de DeepSeek Harness para preparar y probar juegos pequeños con una interfaz de trabajo dentro del agente.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `dsh plugin --profile web add @zseven-w/dsh-game-studio@latest
dsh web` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un minijuego educativo; Prototipar mecánicas con plantillas 2D — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dsh-game-studio.md) · [GitHub](https://github.com/ZSeven-W/dsh-game-studio)

#### 📚 dsh-ios
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 466<br>
**Qué es:** Plugin de DeepSeek Harness para desarrollar y operar aplicaciones en simuladores iOS o dispositivos compatibles.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `dsh plugin --profile web add @zseven-w/dsh-ios@latest
dsh web` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Inspeccionar una interfaz iOS propia; Revisar logs de una app de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dsh-ios.md) · [GitHub](https://github.com/ZSeven-W/dsh-ios)

#### 📚 dsh-android
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 351<br>
**Qué es:** Plugin de DeepSeek Harness para operar un emulador o dispositivo Android y revisar aplicaciones desde el agente.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `dsh plugin --profile web add @zseven-w/dsh-android@latest
dsh web` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Inspeccionar una app Android de prueba; Recoger logcat de una app propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dsh-android.md) · [GitHub](https://github.com/ZSeven-W/dsh-android)

---

## 🕸️ 21. Asistentes e investigación con agentes

Asistentes personales, equipos de agentes e investigación con fuentes. Compara la tarea que completan, las herramientas que pueden usar y la revisión que necesitas hacer del resultado.

**⚖️ ¿Cuál elegir? — OpenClaw, hermes-agent, Mercury Agent**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OpenClaw](human/fichas/openclaw.md) | Tu objetivo encaja con estos ejemplos: Probar un asistente personal; Conectar un agente a un canal propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [hermes-agent](human/fichas/hermes-agent.md) | Tu objetivo encaja con estos ejemplos: Evaluar memoria de un asistente; Comparar un modelo local con Nous Portal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Mercury Agent](human/fichas/mercury-agent.md) | Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar presupuestos de tokens | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — STORM, gpt-researcher**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [STORM](human/fichas/storm.md) | Tu objetivo encaja con estos ejemplos: Preparar una revisión de un tema; Comparar perspectivas antes de escribir | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [gpt-researcher](human/fichas/gpt-researcher.md) | Tu objetivo encaja con estos ejemplos: Preparar un informe de mercado con fuentes; Investigar documentación técnica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Asistentes autónomos y equipos de agentes

#### 🦾 OpenClaw ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 394k<br>
**Qué es:** Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/openclaw/openclaw/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente personal; Conectar un agente a un canal propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [NemoClaw](human/fichas/nemoclaw.md) · [claude-mem](human/fichas/claude-mem.md)<br>
**Más:** [ficha completa](human/fichas/openclaw.md) · [GitHub](https://github.com/openclaw/openclaw)

#### ☤ hermes-agent
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 263k<br>
**Qué es:** Asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://hermes-agent.nousresearch.com/docs/getting-started/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar memoria de un asistente; Comparar un modelo local con Nous Portal — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ECC](human/fichas/ecc.md) · [odysseus](human/fichas/odysseus.md)<br>
**Más:** [ficha completa](human/fichas/hermes-agent.md) · [GitHub](https://github.com/NousResearch/hermes-agent)

#### 🕸️ paperclip
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 114k<br>
**Qué es:** Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.paperclip.ing/reference/cli/installation/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar tareas de varios agentes; Auditar una propuesta antes de aprobarla — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/paperclip.md) · [GitHub](https://github.com/paperclipai/paperclip)

#### 🐝 ruflo
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 81.7k<br>
**Qué es:** Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow).<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx ruflo@latest init` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Coordinar tareas de código; Estudiar memoria compartida entre agentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [mem0](human/fichas/mem0.md) · [ECC](human/fichas/ecc.md)<br>
**Más:** [ficha completa](human/fichas/ruflo.md) · [GitHub](https://github.com/ruvnet/ruflo)

#### 🦾 DeepTutor
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 59.2k<br>
**Qué es:** Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `mkdir -p my-deeptutor && cd my-deeptutor
python -m pip install -U "deeptutor[full]"
deeptutor init     # ports + LLM provider + optional embedding/search
deeptutor start    # starts backend + frontend` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un tema desde apuntes propios; Preparar preguntas de repaso — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Docling](human/fichas/docling.md)<br>
**Más:** [ficha completa](human/fichas/deeptutor.md) · [GitHub](https://github.com/HKUDS/DeepTutor)

#### 🧑‍🤝‍🧑 multica
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 56.1k<br>
**Qué es:** Workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/multica-ai/multica/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar trabajo entre agentes; Revisar entregas en un espacio compartido — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ruflo](human/fichas/ruflo.md) · [chatwoot](human/fichas/chatwoot.md)<br>
**Más:** [ficha completa](human/fichas/multica.md) · [GitHub](https://github.com/multica-ai/multica)

#### 🖥️ OpenDots
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.6k<br>
**Qué es:** Interfaz abierta de asistentes persistentes que requiere CopilotKit Intelligence, alojado, evaluado localmente o con licencia.<br>
**Acceso:** API de IA necesaria · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/CopilotKit/OpenDots.git
cd OpenDots
npm ci
cp .env.example .env
npm run dev` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar aprobación de acciones conectadas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/opendots.md) · [GitHub](https://github.com/CopilotKit/OpenDots)

#### 🦾 Mercury Agent
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 3.9k<br>
**Qué es:** Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm i -g @cosmicstack/mercury-agent` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar presupuestos de tokens — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [claude-mem](human/fichas/claude-mem.md)<br>
**Más:** [ficha completa](human/fichas/mercury-agent.md) · [GitHub](https://github.com/cosmicstack-labs/mercury-agent)

#### 🕸️ social-media-agent
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 3k<br>
**Qué es:** Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `git clone https://github.com/langchain-ai/social-media-agent.git

yarn install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una propuesta para LinkedIn; Convertir un artículo en un borrador corto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LangGraph.js](human/fichas/langgraphjs.md)<br>
**Más:** [ficha completa](human/fichas/social-media-agent.md) · [GitHub](https://github.com/langchain-ai/social-media-agent)

#### 🖥️ hello-halo
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 1.9k<br>
**Qué es:** Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/openkursar/hello-halo/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un asistente de escritorio; Revisar tareas de código visualmente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/hello-halo.md) · [GitHub](https://github.com/openkursar/hello-halo)

#### 🖥️ agentes-chat
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 1.4k<br>
**Qué es:** Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/agentes-chat/agentes-chat/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar un espacio de colaboración con agentes; Organizar consultas en canales — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/agentes-chat.md) · [GitHub](https://github.com/agentes-chat/agentes-chat)

#### 🖥️ fugu
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 1k<br>
**Qué es:** Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/SakanaAI/fugu/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un sistema multiagente como proveedor; Comparar un flujo de código con Fugu — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/fugu.md) · [GitHub](https://github.com/SakanaAI/fugu)

### Agentes de research autónomo

#### 🔬 autoresearch ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 100k<br>
**Qué es:** Experimento para iterar sobre entrenamiento de nanochat con un agente de código y una GPU NVIDIA.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `# 2. Install dependencies
uv sync` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar optimización de entrenamiento; Aprender a registrar experimentos reproducibles — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [crawl4ai](human/fichas/crawl4ai.md)<br>
**Más:** [ficha completa](human/fichas/autoresearch.md) · [GitHub](https://github.com/karpathy/autoresearch)

#### 🦌 deer-flow
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 85.3k<br>
**Qué es:** Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
make setup          # interactive wizard: writes config.yaml and .env (about 2 minutes)` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Investigar un tema con fuentes; Coordinar una generación de informe — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [gpt-researcher](human/fichas/gpt-researcher.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/deer-flow.md) · [GitHub](https://github.com/bytedance/deer-flow)

#### 🔎 STORM
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 31.9k<br>
**Qué es:** Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `git clone https://github.com/stanford-oval/storm.git
    cd storm

conda create -n storm python=3.11
   conda activate storm
   pip install -r requirements.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una revisión de un tema; Comparar perspectivas antes de escribir — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [SearXNG](human/fichas/searxng.md) · [firecrawl](human/fichas/firecrawl.md)<br>
**Más:** [ficha completa](human/fichas/storm.md) · [GitHub](https://github.com/stanford-oval/storm)

#### 🔍 gpt-researcher
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 30.7k<br>
**Qué es:** Agente autónomo que investiga en línea y consolida reportes citados y estructurados.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/assafelovic/gpt-researcher/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un informe de mercado con fuentes; Investigar documentación técnica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [firecrawl](human/fichas/firecrawl.md) · [browser-use](human/fichas/browser-use.md)<br>
**Más:** [ficha completa](human/fichas/gpt-researcher.md) · [GitHub](https://github.com/assafelovic/gpt-researcher)

#### 🕸️ local-deep-research
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 9.6k<br>
**Qué es:** Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/installation.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar documentos privados; Preparar una revisión bibliográfica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/local-deep-research.md) · [GitHub](https://github.com/LearningCircuit/local-deep-research)

---

## 🕸️ 22. Infraestructura, despliegue y herramientas para agentes

Sandboxes, herramientas de ejecución, backend y alojamiento. Son piezas de infraestructura: separa el coste del servidor, los servicios conectados y las llamadas al modelo.

**⚖️ ¿Cuál elegir? — E2B, NemoClaw, sandbox**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [E2B](human/fichas/e2b.md) | Tu objetivo encaja con estos ejemplos: Ejecutar código aislado de una app; Preparar un entorno temporal para un agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [NemoClaw](human/fichas/nemoclaw.md) | Tu objetivo encaja con estos ejemplos: Estudiar aislamiento para OpenClaw; Comparar políticas de ejecución de agentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [sandbox](human/fichas/sandbox.md) | Tu objetivo encaja con estos ejemplos: Probar herramientas de un agente en un contenedor; Consultar una interfaz de navegador aislada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Infraestructura: sandboxes, herramientas y protocolos

#### 🛠️ Composio ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 31.1k<br>
**Qué es:** Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/ComposioHQ/composio/blob/next/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar un agente a un CRM; Explorar herramientas de consulta de un servicio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md) · [OpenAI Agents SDK](human/fichas/openai-agents-python.md) · [Mastra](human/fichas/mastra.md)<br>
**Más:** [ficha completa](human/fichas/composio.md) · [GitHub](https://github.com/ComposioHQ/composio)

#### 🛠️ E2B ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 14.9k<br>
**Qué es:** Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo de APIs o servicios<br>
**Comando documentado:** `npm i e2b` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Ejecutar código aislado de una app; Preparar un entorno temporal para un agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [smolagents](human/fichas/smolagents.md) · [Open SWE](human/fichas/open-swe.md)<br>
**Más:** [ficha completa](human/fichas/e2b.md) · [GitHub](https://github.com/e2b-dev/E2B)

#### 🖥️ claude-task-master
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 28.4k<br>
**Qué es:** Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `claude mcp add taskmaster-ai -- npx -y task-master-ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Descomponer un proyecto web; Revisar orden y dependencias de tareas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-task-master.md) · [GitHub](https://github.com/eyaltoledano/claude-task-master)

#### 🕸️ agent-desktop
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 23.8k<br>
**Qué es:** CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install -g agent-desktop
agent-desktop status                # platform, permissions, supported surfaces
agent-desktop permissions --guide   # macOS: walks you through the Accessibility grant` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Inspeccionar una app de escritorio propia; Preparar una prueba de interfaz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/agent-desktop.md) · [GitHub](https://github.com/vercel-labs/agent-desktop)

#### 🛠️ NemoClaw
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 23k<br>
**Qué es:** Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/get-started/quickstart); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar aislamiento para OpenClaw; Comparar políticas de ejecución de agentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [OpenClaw](human/fichas/openclaw.md) · [hermes-agent](human/fichas/hermes-agent.md) · [Nemotron (NVIDIA)](human/fichas/nemotron.md)<br>
**Más:** [ficha completa](human/fichas/nemoclaw.md) · [GitHub](https://github.com/NVIDIA/NemoClaw)

#### 🕸️ codex-chatgpt-web
**Etiquetas:** Ejecución ☁️ cloud/API · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 15.7k<br>
**Qué es:** Integración de terceros que conecta una sesión de ChatGPT Web con el selector de modelos y herramientas de Codex.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un adaptador de navegador para Codex; Comparar transporte web con acceso oficial — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/codex-chatgpt-web.md) · [GitHub](https://github.com/miuuyy/codex-chatgpt-web)

#### 📦 sandbox
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 6.3k<br>
**Qué es:** Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `# Recommended: Enable API Key authentication (protects all services: API, JupyterLab, VNC)
# - Supports three methods: X-AIO-API-Key header, Authorization: Bearer header, ?api_key= query parameter
# - Without SANDBOX_API_KEY, services remain open (backward compatible)
docker run --security-opt seccomp=unconfined --rm -it \
  -e SANDBOX_API_KEY=your-secret-key \
  -p 127.0.0.1:8080:8080 ghcr.io/agent-infra/sandbox:latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar herramientas de un agente en un contenedor; Consultar una interfaz de navegador aislada — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [OpenHands](human/fichas/openhands.md) · [ECC](human/fichas/ecc.md)<br>
**Más:** [ficha completa](human/fichas/sandbox.md) · [GitHub](https://github.com/agent-infra/sandbox)

#### 🛠️ Gemini Computer Use (preview)
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 3.3k<br>
**Qué es:** Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `git clone https://github.com/google-gemini/computer-use-preview.git
cd computer-use-preview

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar automatización visual de navegador; Evaluar tareas de formularios ficticios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/computer-use-preview.md) · [GitHub](https://github.com/google-gemini/computer-use-preview)

#### 📚 shepherd
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 2.6k<br>
**Qué es:** Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install shepherd-ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar reproducción de ejecuciones; Comparar una traza con un resultado final — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/shepherd.md) · [GitHub](https://github.com/shepherd-agents/shepherd)

#### 🕸️ nodeterm
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 2.5k<br>
**Qué es:** Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/eneskirca/nodeterm/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar varias sesiones de código; Asociar sesiones con worktrees — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/nodeterm.md) · [GitHub](https://github.com/eneskirca/nodeterm)

#### 🛠️ Agent Protocol
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 698<br>
**Qué es:** Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/langchain-ai/agent-protocol/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una API de agentes; Comparar protocolos antes de implementar — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md)<br>
**Más:** [ficha completa](human/fichas/agent-protocol.md) · [GitHub](https://github.com/langchain-ai/agent-protocol)

### Dominios y recursos de infraestructura

#### 🔌 FreeDomain
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 208k<br>
**Qué es:** Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/DigitalPlatDev/FreeDomain/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender DNS; Evaluar un dominio para un proyecto personal — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/freedomain.md) · [GitHub](https://github.com/DigitalPlatDev/FreeDomain)

#### 🔌 free-for-dev
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 143k<br>
**Qué es:** Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ripienaar/free-for-dev/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar infraestructura para una demo; Comparar niveles gratuitos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/free-for-dev.md) · [GitHub](https://github.com/ripienaar/free-for-dev)

### Redes y transporte

#### 🔌 MasterDnsVPN
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app · Setup 🟡 medio · ⭐ 7.3k<br>
**Qué es:** Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar transporte sobre DNS; Probar conectividad en un laboratorio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/masterdnsvpn.md) · [GitHub](https://github.com/masterking32/MasterDnsVPN)

### Alojamiento y backend

#### ⚙️ supabase
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 115k<br>
**Qué es:** Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://supabase.com/docs/guides/getting-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un backend para una web; Conectar un agente a un esquema de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/supabase.md) · [GitHub](https://github.com/supabase/supabase)

#### ⚙️ coolify
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 66.1k<br>
**Qué es:** Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://coolify.io/docs/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Alojar una demo web; Administrar despliegues en servidor propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/coolify.md) · [GitHub](https://github.com/coollabsio/coolify)

#### ⚙️ CasaOS
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 37.6k<br>
**Qué es:** Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/IceWhaleTech/CasaOS/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar servicios domésticos; Explorar un servidor personal — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/casaos.md) · [GitHub](https://github.com/IceWhaleTech/CasaOS)

---

## 🧬 23. Operar, evaluar y medir modelos de IA

Servidores de inferencia, gateways, evaluación, trazas y control de contexto. Cada pieza cubre una etapa: ejecutar el modelo, observarlo o comprobar la calidad de sus respuestas.

**⚖️ ¿Cuál elegir? — vLLM, SGLang**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [vLLM](human/fichas/vllm.md) | Tu objetivo encaja con estos ejemplos: Servir un modelo propio; Estudiar rendimiento de inferencia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [SGLang](human/fichas/sglang.md) | Tu objetivo encaja con estos ejemplos: Servir un modelo para una aplicación; Estudiar inferencia multimodal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — headroom, rtk**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [headroom](human/fichas/headroom.md) | Tu objetivo encaja con estos ejemplos: Reducir salidas extensas de herramientas; Comparar una sesión con y sin compresión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [rtk](human/fichas/rtk.md) | Tu objetivo encaja con estos ejemplos: Reducir salida repetitiva de comandos; Estudiar consumo de contexto por tarea | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — promptfoo, DeepEval, Ragas**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [promptfoo](human/fichas/promptfoo.md) | Tu objetivo encaja con estos ejemplos: Evaluar un prompt de soporte; Probar regresiones de un RAG | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [DeepEval](human/fichas/deepeval.md) | Tu objetivo encaja con estos ejemplos: Detectar regresiones de un chatbot; Probar relevancia de respuestas RAG | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Ragas](human/fichas/ragas.md) | Tu objetivo encaja con estos ejemplos: Medir un RAG con datos controlados; Comparar versiones de una cadena | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — langfuse, MLflow, Opik, Phoenix**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [langfuse](human/fichas/langfuse.md) | Tu objetivo encaja con estos ejemplos: Depurar un asistente; Comparar versiones de un prompt | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [MLflow](human/fichas/mlflow.md) | Tu objetivo encaja con estos ejemplos: Registrar experimentos de ML; Añadir trazas a una app de IA | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Opik](human/fichas/opik.md) | Tu objetivo encaja con estos ejemplos: Depurar una cadena RAG; Revisar fallos con un agente de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Phoenix](human/fichas/phoenix.md) | Tu objetivo encaja con estos ejemplos: Depurar una app con OpenTelemetry; Consultar trazas desde un agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Serving y gateways de LLM

#### 🚀 vLLM ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 96.9k<br>
**Qué es:** Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `uv pip install vllm
vllm download-kernels  # precompiled kernels for faster startup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un modelo propio; Estudiar rendimiento de inferencia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [Open WebUI](human/fichas/open-webui.md)<br>
**Más:** [ficha completa](human/fichas/vllm.md) · [GitHub](https://github.com/vllm-project/vllm)

#### ⚙️ OmniRoute
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 87.5k<br>
**Qué es:** Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.54/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Centralizar proveedores de un agente; Comparar rutas y límites de consumo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/omniroute.md) · [GitHub](https://github.com/cheaper-inference/OmniRoute)

#### 🔀 litellm
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 63.3k<br>
**Qué es:** Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv add litellm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar llamadas a varios modelos; Enrutar un agente por un gateway propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [Open WebUI](human/fichas/open-webui.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/litellm.md) · [GitHub](https://github.com/BerriAI/litellm)

#### 🚀 SGLang
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 38.9k<br>
**Qué es:** Framework de servicio de alto rendimiento para LLM y modelos multimodales.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `uv pip install --prerelease=allow sglang` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un modelo para una aplicación; Estudiar inferencia multimodal — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/sglang.md) · [GitHub](https://github.com/sgl-project/sglang)

#### ⚙️ claude-code-router
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 38.1k<br>
**Qué es:** Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g @musistudio/claude-code-router
ccr ui` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar proveedores desde Claude Code; Organizar perfiles para Codex — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-code-router.md) · [GitHub](https://github.com/musistudio/claude-code-router)

#### 🧬 TensorRT-LLM
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 15.1k<br>
**Qué es:** Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://nvidia.github.io/TensorRT-LLM/installation/index.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Optimizar inferencia en GPU propia; Estudiar kernels y runtimes de NVIDIA — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/tensorrt-llm.md) · [GitHub](https://github.com/NVIDIA/TensorRT-LLM)

#### 🧬 backdoor
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 302<br>
**Qué es:** Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/ajsai47/backdoor
cd backdoor
./backdoor   # animated setup wizard — picks your provider, writes your config, launches Claude Code` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un backend local con Claude Code; Comparar proveedores compatibles — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/backdoor.md) · [GitHub](https://github.com/ajsai47/backdoor)

### Ahorro de contexto y tokens

#### 🗜️ headroom ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 79.7k<br>
**Qué es:** Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install headroom-ai` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir salidas extensas de herramientas; Comparar una sesión con y sin compresión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Context-Engineering](human/fichas/context-engineering.md) · [codegraph](human/fichas/codegraph.md)<br>
**Más:** [ficha completa](human/fichas/headroom.md) · [GitHub](https://github.com/headroomlabs-ai/headroom)

#### 🧬 rtk
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 86.6k<br>
**Qué es:** Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `winget install rtk-ai.rtk` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir salida repetitiva de comandos; Estudiar consumo de contexto por tarea — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/rtk.md) · [GitHub](https://github.com/rtk-ai/rtk)

### Observabilidad, evaluación y guardrails

#### 📡 promptfoo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 27.2k<br>
**Qué es:** CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g promptfoo
promptfoo init --example getting-started` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar un prompt de soporte; Probar regresiones de un RAG — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langfuse](human/fichas/langfuse.md) · [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/promptfoo.md) · [GitHub](https://github.com/promptfoo/promptfoo)

#### 📡 langfuse
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 37.4k<br>
**Qué es:** Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Get a copy of the latest Langfuse repository
  git clone --depth=1 https://github.com/langfuse/langfuse.git
  cd langfuse

  # Run the langfuse docker compose
  docker compose up` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar un asistente; Comparar versiones de un prompt — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langchain](human/fichas/langchain.md) · [litellm](human/fichas/litellm.md) · [ag2](human/fichas/ag2.md)<br>
**Más:** [ficha completa](human/fichas/langfuse.md) · [GitHub](https://github.com/langfuse/langfuse)

#### 📡 MLflow
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 28.8k<br>
**Qué es:** Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uvx mlflow server` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Registrar experimentos de ML; Añadir trazas a una app de IA — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Transformers](human/fichas/transformers.md) · [DSPy](human/fichas/dspy.md)<br>
**Más:** [ficha completa](human/fichas/mlflow.md) · [GitHub](https://github.com/mlflow/mlflow)

#### 📝 loguru
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 24.2k<br>
**Qué es:** Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install loguru` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar una automatización; Añadir logs legibles a una app — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md)<br>
**Más:** [ficha completa](human/fichas/loguru.md) · [GitHub](https://github.com/Delgan/loguru)

#### 📡 Opik
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 23.4k<br>
**Qué es:** Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install opik
opik configure` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar una cadena RAG; Revisar fallos con un agente de código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LangGraph](human/fichas/langgraph.md)<br>
**Más:** [ficha completa](human/fichas/opik.md) · [GitHub](https://github.com/comet-ml/opik)

#### 📡 DeepEval
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 19.5k<br>
**Qué es:** Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install -U deepeval` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Detectar regresiones de un chatbot; Probar relevancia de respuestas RAG — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/deepeval.md) · [GitHub](https://github.com/confident-ai/deepeval)

#### 📡 Ragas
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 16.3k<br>
**Qué es:** Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install ragas` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Medir un RAG con datos controlados; Comparar versiones de una cadena — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [langfuse](human/fichas/langfuse.md)<br>
**Más:** [ficha completa](human/fichas/ragas.md) · [GitHub](https://github.com/vibrantlabsai/ragas)

#### 📡 Phoenix
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 12.3k<br>
**Qué es:** Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install arize-phoenix
phoenix serve` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar una app con OpenTelemetry; Consultar trazas desde un agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [LlamaIndex](human/fichas/llama-index.md) · [LangGraph](human/fichas/langgraph.md)<br>
**Más:** [ficha completa](human/fichas/phoenix.md) · [GitHub](https://github.com/Arize-ai/phoenix)

#### 🖥️ Claude-Code-Usage-Monitor
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 8.8k<br>
**Qué es:** Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `# Install directly from PyPI with uv (easiest)
uv tool install claude-monitor

# Run from anywhere
claude-monitor  # or cmonitor, ccmonitor for short` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar el uso de una sesión; Estudiar alertas y proyecciones de cuota — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-code-usage-monitor.md) · [GitHub](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor)

#### 📡 NeMo Guardrails
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 7.5k<br>
**Qué es:** Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install nemoguardrails` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Guiar un asistente de soporte; Evaluar controles de una app propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [langchain](human/fichas/langchain.md)<br>
**Más:** [ficha completa](human/fichas/guardrails.md) · [GitHub](https://github.com/NVIDIA-NeMo/Guardrails)

---

## 🧑‍💻 24. Modelos abiertos y entrenamiento

Modelos, bibliotecas de entrenamiento y ajuste fino. Revisa la licencia de los pesos, la memoria necesaria y la opción de inferencia antes de descargar o entrenar.

**⚖️ ¿Cuál elegir? — Unsloth, LLaMA-Factory**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Unsloth](human/fichas/unsloth.md) | Tu objetivo encaja con estos ejemplos: Probar inferencia local; Preparar un ajuste fino pequeño | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LLaMA-Factory](human/fichas/llama-factory.md) | Tu objetivo encaja con estos ejemplos: Ajustar un modelo con ejemplos propios; Comparar un adaptador antes de exportarlo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Entrenar y afinar modelos

#### 🏋️ Unsloth ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 79.5k<br>
**Qué es:** App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `winget install --id UnslothAI.Unsloth -e` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar inferencia local; Preparar un ajuste fino pequeño — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md) · [TRL](human/fichas/trl.md)<br>
**Más:** [ficha completa](human/fichas/unsloth.md) · [GitHub](https://github.com/unslothai/unsloth)

#### 🧑‍💻 tensorflow
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 202k<br>
**Qué es:** Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install tensorflow` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender redes neuronales; Construir un clasificador educativo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/tensorflow.md) · [GitHub](https://github.com/tensorflow/tensorflow)

#### 🏋️ Transformers
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 169k<br>
**Qué es:** Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `# pip
pip install "transformers[torch]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar un texto localmente; Probar un modelo de visión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [PEFT](human/fichas/peft.md) · [TRL](human/fichas/trl.md) · [PyTorch](human/fichas/pytorch.md)<br>
**Más:** [ficha completa](human/fichas/transformers.md) · [GitHub](https://github.com/huggingface/transformers)

#### 🏋️ PyTorch
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 106k<br>
**Qué es:** Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://pytorch.org/get-started/locally/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender tensores; Entrenar una red educativa — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/pytorch.md) · [GitHub](https://github.com/pytorch/pytorch)

#### 🏋️ LLaMA-Factory
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 76k<br>
**Qué es:** Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone --depth 1 https://github.com/hiyouga/LlamaFactory.git
cd LlamaFactory
pip install -e .
pip install -r requirements/metrics.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar un modelo con ejemplos propios; Comparar un adaptador antes de exportarlo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [PEFT](human/fichas/peft.md) · [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/llama-factory.md) · [GitHub](https://github.com/hiyouga/LlamaFactory)

#### 🏋️ PEFT
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 21.9k<br>
**Qué es:** Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install peft` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar un modelo con menos parámetros; Reutilizar un adaptador entrenado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Transformers](human/fichas/transformers.md) · [TRL](human/fichas/trl.md)<br>
**Más:** [ficha completa](human/fichas/peft.md) · [GitHub](https://github.com/huggingface/peft)

#### 🏋️ TRL
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 19.7k<br>
**Qué es:** Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install trl` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender ajuste supervisado; Estudiar DPO o GRPO — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Transformers](human/fichas/transformers.md) · [PEFT](human/fichas/peft.md) · [Unsloth](human/fichas/unsloth.md)<br>
**Más:** [ficha completa](human/fichas/trl.md) · [GitHub](https://github.com/huggingface/trl)

#### 🧑‍💻 bionemo-recipes
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 877<br>
**Qué es:** Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA-BioNeMo/bionemo-recipes/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar modelos de secuencias biológicas; Reproducir un entrenamiento de investigación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/bionemo-recipes.md) · [GitHub](https://github.com/NVIDIA-BioNeMo/bionemo-recipes)

### Modelos abiertos y fundacionales

#### 🧠 TimesFM ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 35.5k<br>
**Qué es:** Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por versión.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Install TimesFM with PyTorch
pip install timesfm[torch]` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar demanda con series temporales; Comparar un baseline de pronóstico — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Polars](human/fichas/polars.md) · [DuckDB](human/fichas/duckdb.md)<br>
**Más:** [ficha completa](human/fichas/timesfm.md) · [GitHub](https://github.com/google-research/timesfm)

#### 🧩 DeepSeek-V3
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 105k<br>
**Qué es:** Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su API compatible con OpenAI o en servidores con varias GPU.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar un modelo abierto potente a un agente mediante la API de DeepSeek; Estudiar cómo se sirve un modelo MoE grande con vLLM o SGLang — **Evita si:** Quieres correr un modelo en un equipo doméstico; elige un modelo pequeño con Ollama y revisa los límites antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [SGLang](human/fichas/sglang.md) · [vLLM](human/fichas/vllm.md)<br>
**Más:** [ficha completa](human/fichas/deepseek-v3.md) · [GitHub](https://github.com/deepseek-ai/DeepSeek-V3)

#### 🧩 laya
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 35.5k<br>
**Qué es:** Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `python -m pip install laya` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar consultas por intención; Elegir una opción estructurada — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/laya.md) · [GitHub](https://github.com/NandhaKishorM/laya)

#### 🌌 cosmos
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 12.4k<br>
**Qué es:** Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA/cosmos/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar datos sintéticos para robótica; Estudiar generación de escenas físicas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [diffusers](human/fichas/diffusers.md)<br>
**Más:** [ficha completa](human/fichas/cosmos.md) · [GitHub](https://github.com/NVIDIA/cosmos)

#### 🧠 Nemotron (NVIDIA)
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 2.3k<br>
**Qué es:** Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar modelos abiertos de NVIDIA; Preparar un pipeline guiado de adaptación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [vLLM](human/fichas/vllm.md) · [NemoClaw](human/fichas/nemoclaw.md)<br>
**Más:** [ficha completa](human/fichas/nemotron.md) · [GitHub](https://github.com/NVIDIA-NeMo/Nemotron)

#### 🧩 Kimi K2.7 Code
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado<br>
**Qué es:** Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar generación de código; Estudiar uso de herramientas con un modelo abierto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/kimi-k2-7-code.md) · [Repositorio original](https://huggingface.co/moonshotai/Kimi-K2.7-Code)

---

## 🧑‍💻 25. Procesar datos y trabajar con notebooks

Motores de consulta, tablas, notebooks y aplicaciones de datos. Empieza por un archivo pequeño y distingue una herramienta de análisis de un catálogo o conjunto de datos de referencia.

**⚖️ ¿Cuál elegir? — DuckDB, Polars**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [DuckDB](human/fichas/duckdb.md) | Tu objetivo encaja con estos ejemplos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Polars](human/fichas/polars.md) | Tu objetivo encaja con estos ejemplos: Transformar tablas; Preparar datos antes de un dashboard | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Gradio, streamlit**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Gradio](human/fichas/gradio.md) | Tu objetivo encaja con estos ejemplos: Crear una demo de un modelo; Preparar una herramienta interna de texto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [streamlit](human/fichas/streamlit.md) | Tu objetivo encaja con estos ejemplos: Preparar un dashboard de ventas ficticias; Explorar un simulador de demanda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Datos y notebooks

#### 🗃️ DuckDB ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 43.1k<br>
**Qué es:** Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://duckdb.org/docs/installation/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [marimo](human/fichas/marimo.md) · [Apache Superset](human/fichas/superset.md)<br>
**Más:** [ficha completa](human/fichas/duckdb.md) · [GitHub](https://github.com/duckdb/duckdb)

#### 🗃️ marimo ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 23.6k<br>
**Qué es:** Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install marimo && marimo tutorial intro` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar datos en un notebook; Convertir un análisis en una app — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [DuckDB](human/fichas/duckdb.md) · [Polars](human/fichas/polars.md)<br>
**Más:** [ficha completa](human/fichas/marimo.md) · [GitHub](https://github.com/marimo-team/marimo)

#### 🗃️ Polars
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 40.3k<br>
**Qué es:** Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install polars` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Transformar tablas; Preparar datos antes de un dashboard — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [marimo](human/fichas/marimo.md)<br>
**Más:** [ficha completa](human/fichas/polars.md) · [GitHub](https://github.com/pola-rs/polars)

#### 🗄️ awesome-bigdata
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 14.7k<br>
**Qué es:** Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/oxnr/awesome-bigdata/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar el ecosistema de datos; Comparar motores antes de montar infraestructura — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [awesome-dataviz](human/fichas/awesome-dataviz.md)<br>
**Más:** [ficha completa](human/fichas/awesome-bigdata.md) · [GitHub](https://github.com/oxnr/awesome-bigdata)

#### 🧑‍💻 hudi
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 6.4k<br>
**Qué es:** Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://hudi.apache.org/docs/quick-start-guide.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un lakehouse; Preparar ingestión incremental — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/hudi.md) · [GitHub](https://github.com/apache/hudi)

#### 🧑‍💻 GlobalBuildingAtlas
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🔴 pesado · ⭐ 2.3k<br>
**Qué es:** Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar edificios en un GIS; Preparar una escena urbana de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [three.js](human/fichas/three-js.md)<br>
**Más:** [ficha completa](human/fichas/globalbuildingatlas.md) · [GitHub](https://github.com/zhu-xlab/GlobalBuildingAtlas)

### Apps de datos en Python

#### 🧪 Gradio ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 44.1k<br>
**Qué es:** Librería Python para crear y compartir apps web de modelos de ML en minutos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install --upgrade gradio` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una demo de un modelo; Preparar una herramienta interna de texto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Transformers](human/fichas/transformers.md)<br>
**Más:** [ficha completa](human/fichas/gradio.md) · [GitHub](https://github.com/gradio-app/gradio)

#### 📊 streamlit
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 46.4k<br>
**Qué es:** Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install streamlit` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un dashboard de ventas ficticias; Explorar un simulador de demanda — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [dash](human/fichas/dash.md)<br>
**Más:** [ficha completa](human/fichas/streamlit.md) · [GitHub](https://github.com/streamlit/streamlit)

#### 🧮 dash
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 24.5k<br>
**Qué es:** Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://dash.plotly.com/getting-started); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un tablero interactivo; Comparar escenarios con controles — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [streamlit](human/fichas/streamlit.md) · [echarts](human/fichas/echarts.md)<br>
**Más:** [ficha completa](human/fichas/dash.md) · [GitHub](https://github.com/plotly/dash)

---

## 🎨 26. Animación, gráficos y creación 3D

Animación web, motores gráficos, modelado y renderizado 3D. Una librería se integra en una aplicación; un editor se utiliza directamente. Consulta el formato de entrada y el equipo necesario.

**⚖️ ¿Cuál elegir? — Anime.js, motion, GSAP**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Anime.js](human/fichas/animejs.md) | Tu objetivo encaja con estos ejemplos: Mostrar una transición de estado; Animar un SVG sencillo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [motion](human/fichas/motion.md) | Tu objetivo encaja con estos ejemplos: Animar apertura de contenido; Crear una transición de lista | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [GSAP](human/fichas/gsap.md) | Tu objetivo encaja con estos ejemplos: Sincronizar una transición compleja; Animar un diagrama explicativo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Animación y 3D

#### 🔺 three.js ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 118k<br>
**Qué es:** Biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://threejs.org/manual/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un visor 3D web; Prototipar una escena interactiva — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [react-three-fiber](human/fichas/react-three-fiber.md) · [GSAP](human/fichas/gsap.md)<br>
**Más:** [ficha completa](human/fichas/three-js.md) · [GitHub](https://github.com/mrdoob/three.js)

#### ✨ Anime.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 74.7k<br>
**Qué es:** Motor de animación JavaScript ligero para CSS, SVG, DOM y objetos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/juliangarnier/anime/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Mostrar una transición de estado; Animar un SVG sencillo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/animejs.md) · [GitHub](https://github.com/juliangarnier/anime)

#### 🌀 motion
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 35.2k<br>
**Qué es:** Librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# React / JavaScript
npm install motion` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Animar apertura de contenido; Crear una transición de lista — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [magicui](human/fichas/magicui.md) · [react-three-fiber](human/fichas/react-three-fiber.md)<br>
**Más:** [ficha completa](human/fichas/motion.md) · [GitHub](https://github.com/motiondivision/motion)

#### 🔻 react-three-fiber
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 33.7k<br>
**Qué es:** Renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install three @types/three @react-three/fiber` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un configurador 3D; Construir una escena React interactiva — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [motion](human/fichas/motion.md)<br>
**Más:** [ficha completa](human/fichas/react-three-fiber.md) · [GitHub](https://github.com/pmndrs/react-three-fiber)

#### 🎞️ GSAP
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 30.6k<br>
**Qué es:** Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install gsap` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Sincronizar una transición compleja; Animar un diagrama explicativo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [motion](human/fichas/motion.md)<br>
**Más:** [ficha completa](human/fichas/gsap.md) · [GitHub](https://github.com/greensock/GSAP)

#### 📚 zdog
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 10.7k<br>
**Qué es:** Motor de gráficos pseudo-3D que permite dibujar y animar ilustraciones sencillas mediante canvas o SVG.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/metafizzy/zdog/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar un icono pseudo-3D; Preparar una ilustración interactiva — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/zdog.md) · [GitHub](https://github.com/metafizzy/zdog)

#### 📚 pixelfx
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 7.5k<br>
**Qué es:** Colección de efectos de pixel art hechos con código y una skill para ayudar a generar efectos propios.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/patch-gg/pixelfx/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir un efecto a un juego; Preparar una hoja de sprites — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/pixelfx.md) · [GitHub](https://github.com/patch-gg/pixelfx)

#### 📚 regl
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 5.6k<br>
**Qué es:** Biblioteca funcional para organizar comandos de renderizado WebGL y dibujar gráficos acelerados en una aplicación web.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm i -S regl` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar visualización acelerada; Aprender render funcional — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/regl.md) · [GitHub](https://github.com/regl-project/regl)

#### 📚 webgl-noise
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 3k<br>
**Qué es:** Rutinas de ruido procedural para shaders de WebGL, útiles para crear texturas y efectos visuales en tiempo real.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ashima/webgl-noise/blob/master/README); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear textura de nube procedural; Explorar variaciones de una superficie — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/webgl-noise.md) · [GitHub](https://github.com/ashima/webgl-noise)

#### 📚 scenejs
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 2.8k<br>
**Qué es:** Biblioteca JavaScript para crear y controlar animaciones mediante líneas de tiempo y propiedades de elementos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install scenejs` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una animación de interfaz; Explorar una línea de tiempo web — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/scenejs.md) · [GitHub](https://github.com/daybrush/scenejs)

#### 🖥️ pencil
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 1.9k<br>
**Qué es:** Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://www.pencil2d.org/download/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender animación dibujada a mano; Crear una prueba de movimiento 2D — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/pencil.md) · [GitHub](https://github.com/pencil2d/pencil)

### Creación, renderizado y animación 3D

#### 🖥️ blender
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 22k<br>
**Qué es:** Código de Blender, la aplicación para modelar, animar, renderizar y editar escenas y contenido tridimensional.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/blender/blender/blob/main/.github/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Modelar un objeto sencillo; Preparar una escena de presentación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/blender.md) · [GitHub](https://github.com/blender/blender)

#### 📚 filament
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 20.7k<br>
**Qué es:** Motor de renderizado físicamente basado para integrar gráficos 3D en aplicaciones móviles, web y de escritorio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/google/filament/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Integrar un visor 3D móvil; Estudiar render físicamente basado — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/filament.md) · [GitHub](https://github.com/google/filament)

#### 📚 meshoptimizer
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 8.9k<br>
**Qué es:** Biblioteca para optimizar geometría y reducir el coste de almacenar y renderizar mallas tridimensionales.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone -b v1.3 https://github.com/zeux/meshoptimizer.git` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir peso de un asset 3D; Preparar mallas para render en tiempo real — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/meshoptimizer.md) · [GitHub](https://github.com/zeux/meshoptimizer)

#### 📚 ozz-animation
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 3.1k<br>
**Qué es:** Biblioteca C++ y herramientas para preparar y reproducir animación esquelética dentro de motores y aplicaciones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/guillaumeblanc/ozz-animation/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Reproducir animaciones de personajes; Combinar clips en un motor propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ozz-animation.md) · [GitHub](https://github.com/guillaumeblanc/ozz-animation)

#### 📂 awesome-cad
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 243<br>
**Qué es:** Directorio de programas, bibliotecas y recursos de diseño asistido por computadora organizados por especialidad.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mlightcad/awesome-cad/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar software CAD; Comparar bibliotecas de geometría — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/awesome-cad.md) · [GitHub](https://github.com/mlightcad/awesome-cad)

### Física y simulación

#### 🧑‍💻 warp
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 7.3k<br>
**Qué es:** Framework de NVIDIA para kernels y simulación física en CPU o GPU; no es un modelo ni un terminal.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install warp-lang` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar simulación física; Prototipar cómputo para robótica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/warp.md) · [GitHub](https://github.com/NVIDIA/warp)

#### 📚 planck.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 5.3k<br>
**Qué es:** Motor de física 2D para simular cuerpos, colisiones y uniones dentro de juegos o aplicaciones JavaScript.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://piqnt.com/planck.js/docs/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar física de un juego 2D; Explicar gravedad con una simulación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/planck-js.md) · [GitHub](https://github.com/piqnt/planck.js)

#### 📚 react-three-rapier
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 1.6k<br>
**Qué es:** Integración del motor de física Rapier con React Three Fiber para añadir simulación a escenas tridimensionales.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/pmndrs/react-three-rapier/blob/main/readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una escena física React; Prototipar interacción con objetos 3D — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/react-three-rapier.md) · [GitHub](https://github.com/pmndrs/react-three-rapier)

---

## 🎨 27. Skills de diseño, contenido y especialidades

Skills y plugins para diseño, escritura, marketing, ciencia y negocio. Se añaden a un agente compatible; generar imágenes, publicar o consultar servicios puede requerir cuentas adicionales.

**⚖️ ¿Cuál elegir? — threejs-skills, 3dviz-pro-max**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [threejs-skills](human/fichas/threejs-skills.md) | Tu objetivo encaja con estos ejemplos: Preparar una escena web; Revisar migraciones de Three.js | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [3dviz-pro-max](human/fichas/3dviz-pro-max.md) | Tu objetivo encaja con estos ejemplos: Preparar una visualización de producto; Crear una escena explicativa | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Humanizer, Stop Slop**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Humanizer](human/fichas/humanizer.md) | Tu objetivo encaja con estos ejemplos: Mejorar claridad de un correo; Revisar prosa repetitiva | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Stop Slop](human/fichas/stop-slop.md) | Tu objetivo encaja con estos ejemplos: Reducir frases vagas; Revisar un borrador antes de publicarlo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Skills de diseño para agentes

#### 🎯 Stitch Skills ⭐
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 8.9k<br>
**Qué es:** Colección de skills de agente para trabajar con el servidor MCP de Google Stitch.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/google-labs-code/stitch-skills/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una interfaz con Stitch; Convertir una pantalla en componentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Stitch SDK](human/fichas/stitch-sdk.md) · [Gemini CLI](human/fichas/gemini-cli.md)<br>
**Más:** [ficha completa](human/fichas/stitch-skills.md) · [GitHub](https://github.com/google-labs-code/stitch-skills)

#### 🎨 ui-ux-pro-max-skill
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 150k<br>
**Qué es:** Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla".<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `# Install CLI globally
npm install -g ui-ux-pro-max-cli` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un sistema de diseño; Revisar un formulario — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [taste-skill](human/fichas/taste-skill.md) · [impeccable](human/fichas/impeccable.md) · [tailwindcss](human/fichas/tailwindcss.md)<br>
**Más:** [ficha completa](human/fichas/ui-ux-pro-max-skill.md) · [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

#### 🍷 taste-skill
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 116k<br>
**Qué es:** Skill design-taste-frontend para dirección visual y revisión de sitios; otros skills del pack antiguo se movieron a repos propios.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una web de empresa; Revisar dirección visual de una landing — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md) · [impeccable](human/fichas/impeccable.md)<br>
**Más:** [ficha completa](human/fichas/taste-skill.md) · [GitHub](https://github.com/Leonxlnx/taste-skill)

#### 💎 impeccable
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 110k<br>
**Qué es:** Vocabulario y playbooks de diseño para agentes, con detector determinista y hooks según herramienta.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx impeccable install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Auditar una interfaz; Pulir un componente concreto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [taste-skill](human/fichas/taste-skill.md) · [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md)<br>
**Más:** [ficha completa](human/fichas/impeccable.md) · [GitHub](https://github.com/pbakaus/impeccable)

#### 🎨 Front-End-Checklist
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 74.7k<br>
**Qué es:** Checklist y recursos para revisar aspectos de calidad de un frontend antes de entregarlo.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/thedaviddias/Front-End-Checklist/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una revisión de frontend; Crear criterios de entrega de una web — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/front-end-checklist.md) · [GitHub](https://github.com/thedaviddias/Front-End-Checklist)

#### ✏️ skills_emil
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 56.9k<br>
**Qué es:** Colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering).<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills@latest add emilkowalski/skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar estados de un componente; Preparar decisiones de movimiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md)<br>
**Más:** [ficha completa](human/fichas/skills-emil.md) · [GitHub](https://github.com/emilkowalski/skills)

#### 🎨 hallmark
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 55.1k<br>
**Qué es:** Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add nutlope/hallmark -g` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una página de empresa; Revisar una landing genérica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/hallmark.md) · [GitHub](https://github.com/Nutlope/hallmark)

#### 📐 design.md
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 28.9k<br>
**Qué es:** Especificación y CLI para documentar identidad visual en DESIGN.md,validar tokens y comparar versiones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npx @google/design.md lint DESIGN.md` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar una identidad visual; Comparar dos versiones de tokens — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [impeccable](human/fichas/impeccable.md)<br>
**Más:** [ficha completa](human/fichas/design-md.md) · [GitHub](https://github.com/google-labs-code/design.md)

#### 🎨 anatomy
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 27.3k<br>
**Qué es:** Skill para crear ilustraciones isométricas e interactivas de máquinas y sistemas con SVG y efectos visuales opcionales.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add wheresryan22/anatomy -g` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar un mecanismo; Crear una ilustración isométrica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/anatomy.md) · [GitHub](https://github.com/wheresryan22/anatomy)

#### 🎨 gsap-skills
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 18.5k<br>
**Qué es:** Skills oficiales con instrucciones y ejemplos para que agentes creen animaciones y utilicen plugins de GSAP.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add https://github.com/greensock/gsap-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una transición web; Revisar uso de ScrollTrigger — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/gsap-skills.md) · [GitHub](https://github.com/greensock/gsap-skills)

#### 🎨 modern-web-guidance
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 15.6k<br>
**Qué es:** Herramienta y skill para que un agente consulte documentación actual sobre prácticas y APIs de desarrollo web.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx modern-web-guidance@latest install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar APIs web actuales; Revisar patrones heredados — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/modern-web-guidance.md) · [GitHub](https://github.com/GoogleChrome/modern-web-guidance)

#### 🎨 logo-design-skill
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 6.9k<br>
**Qué es:** Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de diseño.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un logotipo; Preparar variantes monocromas — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/logo-design-skill.md) · [GitHub](https://github.com/kaankiziltug/logo-design-skill)

#### 🎨 threejs-skills
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 4.2k<br>
**Qué es:** Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add cloudai-x/threejs-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una escena web; Revisar migraciones de Three.js — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/threejs-skills.md) · [GitHub](https://github.com/CloudAI-X/threejs-skills)

#### 🎨 blender-skills
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 3.3k<br>
**Qué es:** Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexiones MCP.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `git clone https://github.com/arjun988/blender-skills.git
cp -r blender-skills/.claude/skills /path/to/your/project/.claude/skills/` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un objeto para un juego; Revisar un pipeline de assets 3D — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [blender](human/fichas/blender.md)<br>
**Más:** [ficha completa](human/fichas/blender-skills.md) · [GitHub](https://github.com/arjun988/blender-skills)

#### 🎨 motion-design-skill
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 3.1k<br>
**Qué es:** Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interfaces.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add LottieFiles/motion-design-skill` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Planificar movimiento de un componente; Revisar una transición de interfaz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/motion-design-skill.md) · [GitHub](https://github.com/LottieFiles/motion-design-skill)

#### 🎨 threejs-game-skills
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 2.8k<br>
**Qué es:** Skills para que un agente construya juegos de navegador con Three.js, interfaz y recursos visuales o sonoros opcionales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add majidmanzarpour/threejs-game-skills --skill '*' -a codex -g -y` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un juego de navegador; Añadir QA a una escena Three.js — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/threejs-game-skills.md) · [GitHub](https://github.com/majidmanzarpour/threejs-game-skills)

#### 🎨 dream-loop
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 2.2k<br>
**Qué es:** Skill que combina Blender, generación de imágenes y revisión por un agente para preparar visuales tridimensionales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/achimala/dream-loop/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una escena 3D; Comparar dirección visual de un juego — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dream-loop.md) · [GitHub](https://github.com/achimala/dream-loop)

#### 🎨 design-dna
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 2.1k<br>
**Qué es:** Skill para analizar referencias visuales, extraer decisiones de diseño y generar interfaces con un estilo coherente.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add zanwei/design-dna` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar un estilo existente; Aplicar una identidad a una pantalla nueva — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/design-dna.md) · [GitHub](https://github.com/zanwei/design-dna)

#### 🎨 3dviz-pro-max
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 1.3k<br>
**Qué es:** Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/viettranx/3dviz-pro-max/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una visualización de producto; Crear una escena explicativa — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/3dviz-pro-max.md) · [GitHub](https://github.com/viettranx/3dviz-pro-max)

#### 🎨 genjutsu
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 799<br>
**Qué es:** Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add https://genjutsu.athevon.dev -g` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una microinteracción; Planificar movimiento en una app — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/genjutsu.md) · [GitHub](https://github.com/AThevon/genjutsu)

#### 🎨 Creative Architect
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 24<br>
**Qué es:** Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `/plugin marketplace add Hainrixz/creative-architect
/plugin install creative-architect@creative-architect` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Planificar un anuncio UGC — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/creative-architect.md) · [GitHub](https://github.com/Hainrixz/creative-architect)

### Escritura y calidad de texto

#### 🧑 Humanizer ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 69.1k<br>
**Qué es:** Skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add blader/humanizer --global --agent codex` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Mejorar claridad de un correo; Revisar prosa repetitiva — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/humanizer.md) · [GitHub](https://github.com/blader/humanizer)

#### 🎨 i-have-adhd
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 61.2k<br>
**Qué es:** Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/ayghri/i-have-adhd/blob/main/INSTALL.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir distracciones en instrucciones; Organizar una explicación de trabajo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/i-have-adhd.md) · [GitHub](https://github.com/ayghri/i-have-adhd)

#### 🧹 Stop Slop
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 18.9k<br>
**Qué es:** Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/hardikpandya/stop-slop/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir frases vagas; Revisar un borrador antes de publicarlo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/stop-slop.md) · [GitHub](https://github.com/hardikpandya/stop-slop)

#### 🎨 no-ai-slop
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 13.5k<br>
**Qué es:** Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Editar una publicación; Mejorar claridad de un informe — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/no-ai-slop.md) · [GitHub](https://github.com/petergyang/no-ai-slop)

### Skills de dominio: marketing, SEO y negocio

#### 📈 Marketing Skills ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 60.4k<br>
**Qué es:** Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add coreyhaines31/marketingskills --skill cro copywriting` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar el texto de una landing; Preparar un plan de medición — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [The Agency (agency-agents)](human/fichas/agency-agents.md) · [GEO-SEO Claude](human/fichas/geo-seo-claude.md) · [mautic](human/fichas/mautic.md) · [posthog](human/fichas/posthog.md)<br>
**Más:** [ficha completa](human/fichas/marketingskills.md) · [GitHub](https://github.com/coreyhaines31/marketingskills)

#### 🏢 The Agency (agency-agents)
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 168k<br>
**Qué es:** Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/msitarzewski/agency-agents/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Seleccionar un perfil de frontend; Revisar un brief de marketing — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [GEO-SEO Claude](human/fichas/geo-seo-claude.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/agency-agents.md) · [GitHub](https://github.com/msitarzewski/agency-agents)

#### 🎨 scientific-agent-skills
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 57.2k<br>
**Qué es:** Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add K-Dense-AI/scientific-agent-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un dataset científico; Preparar una revisión bibliográfica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/scientific-agent-skills.md) · [GitHub](https://github.com/K-Dense-AI/scientific-agent-skills)

#### 🧠 financial-services
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 41.3k<br>
**Qué es:** Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Add the marketplace
claude plugin marketplace add anthropics/financial-services

# Core skills + connectors (install first)
claude plugin install financial-analysis@claude-for-financial-services` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un análisis de empresa; Estudiar conciliación de registros ficticios — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/financial-services.md) · [GitHub](https://github.com/anthropics/financial-services)

#### 🎨 claude-seo
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 29.4k<br>
**Qué es:** Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
/seo setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una auditoría SEO inicial; Revisar indexabilidad de una landing — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-seo.md) · [GitHub](https://github.com/AgriciDaniel/claude-seo)

#### 🌍 GEO-SEO Claude
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 11.7k<br>
**Qué es:** Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/zubair-trabzada/geo-seo-claude.git
cd geo-seo-claude
./install.sh` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar schema de una web; Preparar un informe GEO inicial — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Marketing Skills](human/fichas/marketingskills.md) · [The Agency (agency-agents)](human/fichas/agency-agents.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/geo-seo-claude.md) · [GitHub](https://github.com/zubair-trabzada/geo-seo-claude)

#### 🎨 skills
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 11.2k<br>
**Qué es:** Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con un agente.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `/plugin marketplace add slavingia/skills
/plugin install minimalist-entrepreneur` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un problema de cliente; Preparar preguntas de validación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/minimalist-entrepreneur-skills.md) · [GitHub](https://github.com/slavingia/skills)

#### 🎨 instagram-agent-skill
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 6.5k<br>
**Qué es:** Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un Reel; Revisar un caption — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/instagram-agent-skill.md) · [GitHub](https://github.com/Jakeschincariol/instagram-agent-skill)

#### 🧠 social-media-research-skills
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 6.5k<br>
**Qué es:** Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add ScrapeCreators/social-media-research-skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar temas de contenido; Analizar comentarios públicos de una marca — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/social-media-research-skills.md) · [GitHub](https://github.com/ScrapeCreators/social-media-research-skills)

#### 🎨 linkedin-agent-skill
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 3.6k<br>
**Qué es:** Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `git clone https://github.com/Jakeschincariol/linkedin-agent-skill.git
cp -r linkedin-agent-skill/skills/li-* ~/.claude/skills/` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Planificar una semana de contenido; Revisar un perfil profesional — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/linkedin-agent-skill.md) · [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill)

#### 📈 Arcads AI Video Skill Pack
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 1.7k<br>
**Qué es:** Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, Sora, Veo, Kling).<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `git clone https://github.com/krusemediallc/arcads-claude-code.git
cd arcads-claude-code` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un anuncio vertical; Preparar variantes de una imagen de producto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [HyperFrames](human/fichas/hyperframes.md) · [whisper](human/fichas/whisper.md) · [FFmpeg](human/fichas/ffmpeg.md) · [Marketing Skills](human/fichas/marketingskills.md)<br>
**Más:** [ficha completa](human/fichas/arcads-claude-code.md) · [GitHub](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial)

---

## 🖼️ 28. Visión artificial, rostros y percepción

Detección, seguimiento, segmentación, rostros y percepción espacial. Distingue el modelo, sus pesos y las herramientas para preparar datos. Comprueba requisitos y permisos sobre las imágenes.

**⚖️ ¿Cuál elegir? — Deep-Live-Cam, FaceFusion**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Deep-Live-Cam](human/fichas/deep-live-cam.md) | Tu objetivo encaja con estos ejemplos: Estudiar un efecto facial consentido; Probar un pipeline local de video | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [FaceFusion](human/fichas/facefusion.md) | Tu objetivo encaja con estos ejemplos: Preparar un efecto facial consentido; Evaluar un flujo local de imagen | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — face_recognition, InsightFace**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [face_recognition](human/fichas/face-recognition.md) | Tu objetivo encaja con estos ejemplos: Estudiar detección facial; Comparar dos fotos propias en un laboratorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [InsightFace](human/fichas/insightface.md) | Tu objetivo encaja con estos ejemplos: Estudiar alineación facial; Evaluar detección en un dataset de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Rostros y retratos animados

#### 🎭 Deep-Live-Cam ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 98.1k<br>
**Qué es:** Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone --depth 1 https://github.com/hacksider/Deep-Live-Cam.git` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un efecto facial consentido; Probar un pipeline local de video — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [face_recognition](human/fichas/face-recognition.md)<br>
**Más:** [ficha completa](human/fichas/deep-live-cam.md) · [GitHub](https://github.com/hacksider/Deep-Live-Cam)

#### 👤 face_recognition
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 56.9k<br>
**Qué es:** Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip3 install face_recognition` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar detección facial; Comparar dos fotos propias en un laboratorio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Deep-Live-Cam](human/fichas/deep-live-cam.md)<br>
**Más:** [ficha completa](human/fichas/face-recognition.md) · [GitHub](https://github.com/ageitgey/face_recognition)

#### 🙂 FaceFusion
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 30.7k<br>
**Qué es:** Plataforma para intercambio y mejora de rostros en imágenes y video.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://docs.facefusion.io/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un efecto facial consentido; Evaluar un flujo local de imagen — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/facefusion.md) · [GitHub](https://github.com/facefusion/facefusion)

#### 🙂 InsightFace
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 30.2k<br>
**Qué es:** Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/deepinsight/insightface/blob/master/python-package/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar alineación facial; Evaluar detección en un dataset de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [FaceFusion](human/fichas/facefusion.md)<br>
**Más:** [ficha completa](human/fichas/insightface.md) · [GitHub](https://github.com/deepinsight/insightface)

#### 🧑 LivePortrait
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 19.5k<br>
**Qué es:** Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas).<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/KlingTeam/LivePortrait
cd LivePortrait

# create env using conda
conda create -n LivePortrait python=3.10
conda activate LivePortrait` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una animación consentida de un retrato; Estudiar retargeting facial — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/liveportrait.md) · [GitHub](https://github.com/KlingAIResearch/LivePortrait)

### Visión por computador

#### 👁️ Ultralytics YOLO ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 63.4k<br>
**Qué es:** Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install ultralytics` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Contar objetos de muestra; Probar segmentación en un prototipo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [supervision](human/fichas/supervision.md) · [Label Studio](human/fichas/label-studio.md)<br>
**Más:** [ficha completa](human/fichas/ultralytics.md) · [GitHub](https://github.com/ultralytics/ultralytics)

#### 👁️ SAM 3 ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 12.3k<br>
**Qué es:** Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en imágenes y video todos los objetos que describas con una frase corta.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/facebookresearch/sam3.git
cd sam3
pip install -e .` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Recortar todas las personas o productos de una foto con una frase; Seguir un objeto descrito con texto a lo largo de un video — **Evita si:** No tienes una GPU NVIDIA compatible o necesitas una licencia permisiva como Apache; revisa los límites antes de elegirlo<br>
**Combina con:** [Label Studio](human/fichas/label-studio.md) · [supervision](human/fichas/supervision.md)<br>
**Más:** [ficha completa](human/fichas/sam3.md) · [GitHub](https://github.com/facebookresearch/sam3)

#### 👁️ OpenCV
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 91.6k<br>
**Qué es:** La librería de visión por computadora de referencia, con miles de algoritmos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/opencv/opencv/blob/5.x/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar imágenes antes de OCR; Estudiar procesamiento visual básico — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [supervision](human/fichas/supervision.md)<br>
**Más:** [ficha completa](human/fichas/opencv.md) · [GitHub](https://github.com/opencv/opencv)

#### 👁️ supervision
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 51.6k<br>
**Qué es:** Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install supervision` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Visualizar detecciones; Contar cruces en un video de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [OpenCV](human/fichas/opencv.md)<br>
**Más:** [ficha completa](human/fichas/supervision.md) · [GitHub](https://github.com/roboflow/supervision)

#### 📚 mediapipe
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 37.7k<br>
**Qué es:** Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplicaciones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://developers.google.com/edge/mediapipe/solutions/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una interacción con manos; Prototipar visión en dispositivo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/mediapipe.md) · [GitHub](https://github.com/google-ai-edge/mediapipe)

#### 🧩 openpose
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 34.6k<br>
**Qué es:** Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar estimación de postura; Preparar puntos de movimiento para una demo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/openpose.md) · [GitHub](https://github.com/CMU-Perceptual-Computing-Lab/openpose)

#### 👁️ Label Studio
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🟢 fácil · ⭐ 28.7k<br>
**Qué es:** Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker pull heartexlabs/label-studio:latest
docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un dataset de imágenes; Revisar etiquetas de texto o audio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ultralytics YOLO](human/fichas/ultralytics.md) · [SAM 3](human/fichas/sam3.md)<br>
**Más:** [ficha completa](human/fichas/label-studio.md) · [GitHub](https://github.com/HumanSignal/label-studio)

#### 📚 tfjs-models
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 14.8k<br>
**Qué es:** Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en aplicaciones.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/tensorflow/tfjs-models/blob/master/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar ML en el navegador; Preparar una demo de landmarks — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/tfjs-models.md) · [GitHub](https://github.com/tensorflow/tfjs-models)

#### 📚 kornia
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 12.4k<br>
**Qué es:** Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en PyTorch.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install kornia` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar datos visuales; Estudiar geometría diferenciable — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/kornia.md) · [GitHub](https://github.com/kornia/kornia)

#### 🧩 mmpose
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 8.1k<br>
**Qué es:** Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento humano.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://mmpose.readthedocs.io/en/latest/installation.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar modelos de pose; Preparar una demo de análisis de movimiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/mmpose.md) · [GitHub](https://github.com/open-mmlab/mmpose)

#### 🧩 EasyMocap
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 5k<br>
**Qué es:** Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imágenes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://chingswy.github.io/easymocap-public-doc/quickstart/quickstart.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar captura multicámara; Explorar reconstrucción de movimiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/easymocap.md) · [GitHub](https://github.com/zju3dv/EasyMocap)

#### 🧩 4D-Humans
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 1.7k<br>
**Qué es:** Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de video.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/shubham-goel/4D-Humans.git
cd 4D-Humans
conda env create -f environment.yml
conda activate 4D-humans` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar reconstrucción humana 3D; Explorar seguimiento en un clip corto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/4d-humans.md) · [GitHub](https://github.com/shubham-goel/4D-Humans)

#### 🧩 WHAM
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 1.2k<br>
**Qué es:** Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de video.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/yohanshin/WHAM/blob/main/docs/INSTALL.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar movimiento humano 3D; Comparar reconstrucción antes y después de refinamiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/wham.md) · [GitHub](https://github.com/yohanshin/WHAM)

### Sensores y percepción espacial

#### 🖼️ RuView
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 104k<br>
**Qué es:** Proyecto de detección espacial que experimenta con señales WiFi para estimar presencia y movimiento.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `# Check the local setup and get source-cited guidance
npx @ruvnet/ruview@0.9.1 doctor
npx @ruvnet/ruview@0.9.1 guidance --topic sensing --query "model loading"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar sensado WiFi en laboratorio; Explorar una visualización espacial simulada — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ruview.md) · [GitHub](https://github.com/ruvnet/RuView)

---

## 🎬 29. Audio, transcripción, voz y música

Transcripción, síntesis, clonación de voz, agentes de audio y música. Compara idioma, latencia, procesamiento local y servicios externos según la tarea concreta.

**⚖️ ¿Cuál elegir? — whisper.cpp, whisper, faster-whisper**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [whisper.cpp](human/fichas/whisper-cpp.md) | Tu objetivo encaja con estos ejemplos: Transcribir una nota offline; Preparar texto base para subtítulos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [whisper](human/fichas/whisper.md) | Tu objetivo encaja con estos ejemplos: Preparar una transcripción local; Traducir habla al inglés como borrador | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [faster-whisper](human/fichas/faster-whisper.md) | Tu objetivo encaja con estos ejemplos: Transcribir lotes pequeños; Comparar CPU con GPU | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — whisperX, NeMo Speech**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [whisperX](human/fichas/whisperx.md) | Tu objetivo encaja con estos ejemplos: Preparar subtítulos por palabra; Separar intervenciones de una entrevista | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [NeMo Speech](human/fichas/nemo.md) | Tu objetivo encaja con estos ejemplos: Estudiar modelos de voz de NVIDIA; Preparar un experimento ASR | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Kokoro, edge-tts, LuxTTS**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Kokoro](human/fichas/kokoro.md) | Tu objetivo encaja con estos ejemplos: Narrar una nota propia; Probar una voz para una demo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [edge-tts](human/fichas/edge-tts.md) | Tu objetivo encaja con estos ejemplos: Preparar una voz de prueba online; Explorar voces disponibles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LuxTTS](human/fichas/luxtts.md) | Tu objetivo encaja con estos ejemplos: Preparar una narración local; Explorar adaptación de voz consentida | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — GPT-SoVITS, Fish Speech, IndexTTS, CosyVoice**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [GPT-SoVITS](human/fichas/gpt-sovits.md) | Tu objetivo encaja con estos ejemplos: Prototipar una voz para contenido propio; Estudiar adaptación con pocos ejemplos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Fish Speech](human/fichas/fish-speech.md) | Tu objetivo encaja con estos ejemplos: Estudiar generación expresiva; Preparar una prueba de voz multilingüe | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [IndexTTS](human/fichas/index-tts.md) | Tu objetivo encaja con estos ejemplos: Prototipar narración con duración controlada; Estudiar expresión de voz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [CosyVoice](human/fichas/cosyvoice.md) | Tu objetivo encaja con estos ejemplos: Explorar síntesis multilingüe; Estudiar streaming de voz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Pipecat, LiveKit Agents**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Pipecat](human/fichas/pipecat.md) | Tu objetivo encaja con estos ejemplos: Prototipar un agente de voz; Comparar combinaciones STT/LLM/TTS | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [LiveKit Agents](human/fichas/livekit-agents.md) | Tu objetivo encaja con estos ejemplos: Construir un asistente de voz; Evaluar conversación en tiempo real | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Transcripción (voz a texto)

#### 🎙️ whisper.cpp ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 55.2k<br>
**Qué es:** Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/ggml-org/whisper.cpp.git` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Transcribir una nota offline; Preparar texto base para subtítulos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/whisper-cpp.md) · [GitHub](https://github.com/ggml-org/whisper.cpp)

#### 📝 whisper
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 113k<br>
**Qué es:** Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install -U openai-whisper` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una transcripción local; Traducir habla al inglés como borrador — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/whisper.md) · [GitHub](https://github.com/openai/whisper)

#### ⚡ faster-whisper
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 26.8k<br>
**Qué es:** Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install faster-whisper` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Transcribir lotes pequeños; Comparar CPU con GPU — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/faster-whisper.md) · [GitHub](https://github.com/SYSTRAN/faster-whisper)

#### 🎯 whisperX
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 25.3k<br>
**Qué es:** Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install whisperx` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar subtítulos por palabra; Separar intervenciones de una entrevista — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [whisper](human/fichas/whisper.md) · [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/whisperx.md) · [GitHub](https://github.com/m-bain/whisperX)

#### 🎙️ NeMo Speech
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 18.8k<br>
**Qué es:** Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/NVIDIA-NeMo/Speech.git
cd Speech
uv sync --extra all --extra cu13     # CUDA 13.x (recommended) — use --extra cu12 for CUDA 12.x` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar modelos de voz de NVIDIA; Preparar un experimento ASR — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Pipecat](human/fichas/pipecat.md)<br>
**Más:** [ficha completa](human/fichas/nemo.md) · [GitHub](https://github.com/NVIDIA-NeMo/Speech)

### Síntesis y clonación de voz

#### 🗣️ Kokoro ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 10.1k<br>
**Qué es:** Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/hexgrad/kokoro/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Narrar una nota propia; Probar una voz para una demo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Pipecat](human/fichas/pipecat.md) · [whisper.cpp](human/fichas/whisper-cpp.md)<br>
**Más:** [ficha completa](human/fichas/kokoro.md) · [GitHub](https://github.com/hexgrad/kokoro)

#### 🎚️ VoiceStudio
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 111k<br>
**Qué es:** App local de voz con modelos descargables,edición AGPL y una oferta comercial separada.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/debpalash/VoiceStudio/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una narración local; Probar transcripción o doblaje de material propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/omnivoice-studio.md) · [GitHub](https://github.com/debpalash/VoiceStudio)

#### 🗣️ GPT-SoVITS
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 65.1k<br>
**Qué es:** Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `conda create -n GPTSoVits python=3.10
conda activate GPTSoVits

pip install -r extra-req.txt --no-deps
pip install -r requirements.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una voz para contenido propio; Estudiar adaptación con pocos ejemplos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [RVC WebUI](human/fichas/rvc.md)<br>
**Más:** [ficha completa](human/fichas/gpt-sovits.md) · [GitHub](https://github.com/RVC-Boss/GPT-SoVITS)

#### 🗣️ VibeVoice
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🔴 pesado · ⭐ 57.2k<br>
**Qué es:** Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/microsoft/VibeVoice/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar transcripción por hablantes; Probar generación de voz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [open-notebook](human/fichas/open-notebook.md)<br>
**Más:** [ficha completa](human/fichas/vibevoice.md) · [GitHub](https://github.com/microsoft/VibeVoice)

#### 🗣️ VoxCPM
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🔴 pesado · ⭐ 42.5k<br>
**Qué es:** VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación de voz.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `pip install voxcpm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar narración local; Explorar diseño de voz consentido — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/voxcpm.md) · [GitHub](https://github.com/OpenBMB/VoxCPM)

#### 🗣️ RVC WebUI
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟡 medio · ⭐ 39.3k<br>
**Qué es:** Interfaz y herramientas para convertir una grabación a otra voz mediante modelos locales.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un efecto de voz consentido; Estudiar conversión frente a TTS — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [GPT-SoVITS](human/fichas/gpt-sovits.md)<br>
**Más:** [ficha completa](human/fichas/rvc.md) · [GitHub](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

#### 🗣️ Fish Speech
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 33.7k<br>
**Qué es:** Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://speech.fish.audio/install/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar generación expresiva; Preparar una prueba de voz multilingüe — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/fish-speech.md) · [GitHub](https://github.com/fishaudio/fish-speech)

#### 🗣️ IndexTTS
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 25.1k<br>
**Qué es:** Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/index-tts/index-tts.git && cd index-tts

pip install -U uv  # or see the link above for other install methods` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar narración con duración controlada; Estudiar expresión de voz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/index-tts.md) · [GitHub](https://github.com/index-tts/index-tts)

#### 🗣️ CosyVoice
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 24.4k<br>
**Qué es:** Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
    # If you failed to clone the submodule due to network failures, please run the following command until success
    cd CosyVoice
    git submodule update --init --recursive` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar síntesis multilingüe; Estudiar streaming de voz — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Pipecat](human/fichas/pipecat.md)<br>
**Más:** [ficha completa](human/fichas/cosyvoice.md) · [GitHub](https://github.com/QwenAudio/CosyVoice)

#### 🎬 edge-tts
**Etiquetas:** Ejecución ☁️ cloud/API · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 12.5k<br>
**Qué es:** Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Coste por confirmar<br>
**Comando documentado:** `pipx install edge-tts` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una voz de prueba online; Explorar voces disponibles — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [MoviePy](human/fichas/moviepy.md)<br>
**Más:** [ficha completa](human/fichas/edge-tts.md) · [GitHub](https://github.com/rany2/edge-tts)

#### 🗣️ LuxTTS
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 5.6k<br>
**Qué es:** Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/ysharma3501/LuxTTS.git
cd LuxTTS
pip install -r requirements.txt` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una narración local; Explorar adaptación de voz consentida — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [litellm](human/fichas/litellm.md) · [cosmos](human/fichas/cosmos.md) · [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/luxtts.md) · [GitHub](https://github.com/ysharma3501/LuxTTS)

### Agentes de voz en tiempo real

#### 📞 Pipecat ⭐
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 17.3k<br>
**Qué es:** Framework open source para agentes de voz y apps multimodales en tiempo real.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv tool install "pipecat-ai[cli]"
pipecat init` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un agente de voz; Comparar combinaciones STT/LLM/TTS — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Kokoro](human/fichas/kokoro.md) · [whisper.cpp](human/fichas/whisper-cpp.md)<br>
**Más:** [ficha completa](human/fichas/pipecat.md) · [GitHub](https://github.com/pipecat-ai/pipecat)

#### 📞 LiveKit Agents
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 15.2k<br>
**Qué es:** Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install "livekit-agents[openai,deepgram,cartesia]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un asistente de voz; Evaluar conversación en tiempo real — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Kokoro](human/fichas/kokoro.md)<br>
**Más:** [ficha completa](human/fichas/livekit-agents.md) · [GitHub](https://github.com/livekit/agents)

#### 🖥️ dograh
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟡 medio · ⭐ 6.1k<br>
**Qué es:** Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables.<br>
**Acceso:** Depende de la ruta elegida · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/dograh-hq/dograh/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar un agente de voz; Editar un workflow mediante MCP — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/dograh.md) · [GitHub](https://github.com/dograh-hq/dograh)

### Música y audio generativo

#### 🎵 AudioCraft ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 23.9k<br>
**Qué es:** Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/facebookresearch/audiocraft/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar generación de música; Estudiar sonidos a partir de texto — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [MoviePy](human/fichas/moviepy.md) · [remotion](human/fichas/remotion.md) · [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/audiocraft.md) · [GitHub](https://github.com/facebookresearch/audiocraft)

#### 🎬 ACE-Step-1.5
**Etiquetas:** Ejecución 🏠 local · Rol ⚙️ plataforma · Setup 🔴 pesado · ⭐ 14.8k<br>
**Qué es:** Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `# 2. Clone & install
git clone https://github.com/ACE-Step/ACE-Step-1.5.git
cd ACE-Step-1.5
uv sync

# 3. Launch Gradio UI (models auto-download on first run)
uv run acestep` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una base musical de prueba; Comparar variantes de generación local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/ace-step-1-5.md) · [GitHub](https://github.com/ace-step/ACE-Step-1.5)

#### 🎬 Music-Megathread
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 3.1k<br>
**Qué es:** Directorio de reproductores, herramientas, servicios y otros recursos relacionados con música.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/MoonWalker440/Music-Megathread/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar un reproductor; Explorar herramientas de audio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/music-megathread.md) · [GitHub](https://github.com/MoonWalker440/Music-Megathread)

### Procesamiento y limpieza de audio

#### 🧩 rnnoise
**Etiquetas:** Ejecución 🏠 local · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 6k<br>
**Qué es:** Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/xiph/rnnoise/blob/main/README); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir ruido de una grabación; Estudiar una red de supresión de ruido — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/rnnoise.md) · [GitHub](https://github.com/xiph/rnnoise)

#### 🧩 earshot
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 4.8k<br>
**Qué es:** Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
earshot doctor --fetch     # downloads the two models now (~1.1 GB)` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar una mezcla con un agente; Analizar un efecto sonoro — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/earshot.md) · [GitHub](https://github.com/Leonxlnx/earshot)

#### 📚 rubberband
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 813<br>
**Qué es:** Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/breakfastquay/rubberband/blob/default/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar duración de una narración; Explorar cambio de tono — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/rubberband.md) · [GitHub](https://github.com/breakfastquay/rubberband)

---

## 🎬 30. Video con código y agentes creativos

Herramientas y skills para escenas, motion graphics y montaje programático. Distingue el renderizado del video de la generación de sus imágenes o voces, que puede necesitar otros proveedores.

**⚖️ ¿Cuál elegir? — HyperFrames, MoviePy, remotion**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [HyperFrames](human/fichas/hyperframes.md) | Tu objetivo encaja con estos ejemplos: Preparar un video explicativo por código; Crear una pieza de presentación con HTML | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [MoviePy](human/fichas/moviepy.md) | Tu objetivo encaja con estos ejemplos: Automatizar variantes de un video; Componer clips y rótulos desde Python | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [remotion](human/fichas/remotion.md) | Tu objetivo encaja con estos ejemplos: Crear una plantilla de video con datos; Preparar títulos animados | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Manim (ManimGL), manim**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Manim (ManimGL)](human/fichas/manim.md) | Tu objetivo encaja con estos ejemplos: Explicar una transformación matemática; Preparar una animación geométrica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [manim](human/fichas/manim-community.md) | Tu objetivo encaja con estos ejemplos: Preparar una explicación matemática; Crear una animación de geometría | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — OpenMontage, video-use, Remotion Superpowers**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [OpenMontage](human/fichas/openmontage.md) | Tu objetivo encaja con estos ejemplos: Preparar un video con recursos locales; Comparar un pipeline con servicios opcionales | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [video-use](human/fichas/video-use.md) | Tu objetivo encaja con estos ejemplos: Editar una entrevista propia; Seleccionar tomas de un tutorial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Remotion Superpowers](human/fichas/remotion-superpowers.md) | Tu objetivo encaja con estos ejemplos: Preparar un video narrado; Combinar clips y subtítulos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Motores de video y escenas por código

#### 🎞️ HyperFrames ⭐
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 84.4k<br>
**Qué es:** Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx hyperframes init my-video` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un video explicativo por código; Crear una pieza de presentación con HTML — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [GSAP](human/fichas/gsap.md) · [Kokoro](human/fichas/kokoro.md) · [whisperX](human/fichas/whisperx.md)<br>
**Más:** [ficha completa](human/fichas/hyperframes.md) · [GitHub](https://github.com/heygen-com/hyperframes)

#### 🎬 MoviePy ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 15.2k<br>
**Qué es:** Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://zulko.github.io/moviepy/getting_started/install.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar variantes de un video; Componer clips y rótulos desde Python — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [whisperX](human/fichas/whisperx.md) · [Kokoro](human/fichas/kokoro.md) · [ComfyUI](human/fichas/comfyui.md)<br>
**Más:** [ficha completa](human/fichas/moviepy.md) · [GitHub](https://github.com/Zulko/moviepy)

#### 🎞️ Manim (ManimGL)
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 96.5k<br>
**Qué es:** Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `# Install manimgl
pip install manimgl

# Try it out
manimgl` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar una transformación matemática; Preparar una animación geométrica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Kokoro](human/fichas/kokoro.md) · [MoviePy](human/fichas/moviepy.md) · [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/manim.md) · [GitHub](https://github.com/3b1b/manim)

#### ⚛️ remotion
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 73.2k<br>
**Qué es:** Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx create-video@latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una plantilla de video con datos; Preparar títulos animados — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Open-Generative-AI](human/fichas/open-generative-ai.md)<br>
**Más:** [ficha completa](human/fichas/remotion.md) · [GitHub](https://github.com/remotion-dev/remotion)

#### 🎬 manim
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 42.5k<br>
**Qué es:** Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://docs.manim.community/en/stable/installation.html); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una explicación matemática; Crear una animación de geometría — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md)<br>
**Más:** [ficha completa](human/fichas/manim-community.md) · [GitHub](https://github.com/ManimCommunity/manim)

#### 📚 mediabunny
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 7.5k<br>
**Qué es:** Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install mediabunny` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Procesar video dentro de una aplicación web; Construir una herramienta de conversión en navegador — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/mediabunny.md) · [GitHub](https://github.com/Vanilagy/mediabunny)

### Skills y métodos de producción audiovisual

#### 🎞️ Remotion Agent Skills ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 7.1k<br>
**Qué es:** Skills oficiales de Remotion para que tu agente de código cree videos con React.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add remotion-dev/skills` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender Remotion con un agente; Preparar una plantilla de video — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [remotion](human/fichas/remotion.md) · [Remotion Superpowers](human/fichas/remotion-superpowers.md)<br>
**Más:** [ficha completa](human/fichas/skills-remotion.md) · [GitHub](https://github.com/remotion-dev/skills)

#### 🎞️ OpenMontage
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 80.5k<br>
**Qué es:** Pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un video con recursos locales; Comparar un pipeline con servicios opcionales — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [remotion](human/fichas/remotion.md)<br>
**Más:** [ficha completa](human/fichas/openmontage.md) · [GitHub](https://github.com/OpenMontageInc/OpenMontage)

#### 🎞️ video-use
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 31.1k<br>
**Qué es:** Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Arranque:** [Instrucciones originales](https://github.com/browser-use/video-use/blob/main/install.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Editar una entrevista propia; Seleccionar tomas de un tutorial — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [FFmpeg](human/fichas/ffmpeg.md) · [Claude Code](human/fichas/claude-code.md)<br>
**Más:** [ficha completa](human/fichas/video-use.md) · [GitHub](https://github.com/browser-use/video-use)

#### 🎨 hypit
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 29.9k<br>
**Qué es:** Skills para agentes que organizan generación y edición de videos mediante modelos, servicios y recursos configurables.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add hypit-ai/hypit -g` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear versiones de un video propio; Coordinar subtítulos y B-roll de un tutorial — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/hypit.md) · [GitHub](https://github.com/hypit-ai/hypit)

#### 🎨 brag
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 21.5k<br>
**Qué es:** Skills para que un agente convierta un proyecto o sitio en un video breve de lanzamiento con composición y música.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add https://github.com/latent-spaces/brag --skill brag-slim` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Presentar una demo de producto; Preparar una pieza de lanzamiento — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/brag.md) · [GitHub](https://github.com/latent-spaces/brag)

#### 🎨 video-shotcraft
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 19.7k<br>
**Qué es:** Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de sonido.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add Vincentwei1021/video-shotcraft` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una promo de producto; Organizar planos sincronizados con sonido — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/video-shotcraft.md) · [GitHub](https://github.com/Vincentwei1021/video-shotcraft)

#### 🎨 lemo-opuscar
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 16.3k<br>
**Qué es:** Biblioteca de estilos para video por código orientada a Claude,con licencias diferentes para código,guías y medios.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una dirección visual para un video; Preparar una pieza por código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/lemo-opuscar.md) · [GitHub](https://github.com/lemomo-ai/lemo-opuscar)

#### 🎬 rea-video
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 8.6k<br>
**Qué es:** Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/JuneYaooo/rea-video/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar ritmo de una pieza; Preparar un plan de recreación con material propio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [remotion](human/fichas/remotion.md)<br>
**Más:** [ficha completa](human/fichas/rea-video.md) · [GitHub](https://github.com/JuneYaooo/rea-video)

#### 🎨 openfilm
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 7.2k<br>
**Qué es:** Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add openfilm/openfilm` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un video editable; Revisar el resultado de un agente en un editor — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/openfilm.md) · [GitHub](https://github.com/openfilm/openfilm)

#### 🎨 srt-whiteboard-animation
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 5.6k<br>
**Qué es:** Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos SRT.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/geeklee/srt-whiteboard-animation/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una explicación de pizarra; Prototipar una secuencia narrada — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/srt-whiteboard-animation.md) · [GitHub](https://github.com/geeklee/srt-whiteboard-animation)

#### 🎨 claude-animated-shorts
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 3.4k<br>
**Qué es:** Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/mromidev/claude-animated-shorts/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un corto animado de prueba; Estudiar personajes 2D en escena 3D — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/claude-animated-shorts.md) · [GitHub](https://github.com/mromidev/claude-animated-shorts)

#### 🎨 huashu-motion
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 2.7k<br>
**Qué es:** Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión visual.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add alchaincyf/huashu-motion` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una presentación de producto; Explorar estilos de motion graphics — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/huashu-motion.md) · [GitHub](https://github.com/alchaincyf/huashu-motion)

#### 🎨 Papermorph
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 1.7k<br>
**Qué es:** Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visuales.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code   # or --agent opencode` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una lección animada; Explorar una historia interactiva — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/papermorph.md) · [GitHub](https://github.com/DozenTwelve/Papermorph)

#### 🎨 motionmaxxing
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 1.6k<br>
**Qué es:** Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `git clone https://github.com/Tejashmakwana/motionmaxxing ~/.claude/skills/motionmaxxing
bash ~/.claude/skills/motionmaxxing/install.sh        # checks the requirements; installs nothing system-wide` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Mejorar una pieza de lanzamiento; Preparar una animación tipográfica — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/motionmaxxing.md) · [GitHub](https://github.com/Tejashmakwana/motionmaxxing)

#### 🎞️ Remotion Superpowers
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 168<br>
**Qué es:** Orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `codex plugin marketplace add DojoCodingLabs/remotion-superpowers
codex plugin add remotion-superpowers@remotion-superpowers` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un video narrado; Combinar clips y subtítulos — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [remotion](human/fichas/remotion.md) · [Remotion Agent Skills](human/fichas/skills-remotion.md)<br>
**Más:** [ficha completa](human/fichas/remotion-superpowers.md) · [GitHub](https://github.com/DojoCodingLabs/remotion-superpowers)

### Aplicaciones y flujos de producción

#### 📲 videofy_minimal
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 656<br>
**Qué es:** Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión.<br>
**Acceso:** API de IA necesaria · Consumo de APIs o servicios<br>
**Comando documentado:** `uv sync
npm install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una noticia para señalización; Probar una pieza informativa breve — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [whisper](human/fichas/whisper.md)<br>
**Más:** [ficha completa](human/fichas/videofy-minimal.md) · [GitHub](https://github.com/schibsted/videofy_minimal)

---

## 📄 31. Presentaciones, diagramas y explicación visual

Presentaciones, diagramas y documentación visual. Elige entre editar una pieza, escribir su estructura o generarla con un agente; revisa cómo se exporta antes de empezar.

**⚖️ ¿Cuál elegir? — Slidev, reveal.js, Marp**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Slidev](human/fichas/slidev.md) | Tu objetivo encaja con estos ejemplos: Preparar una charla técnica; Explicar un ejemplo de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [reveal.js](human/fichas/reveal-js.md) | Tu objetivo encaja con estos ejemplos: Preparar una presentación web; Mostrar un ejemplo interactivo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Marp](human/fichas/marp.md) | Tu objetivo encaja con estos ejemplos: Preparar slides sencillas; Versionar una presentación en Git | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — ppt-master, Presenton**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [ppt-master](human/fichas/ppt-master.md) | Tu objetivo encaja con estos ejemplos: Preparar una presentación de un informe; Adaptar una plantilla corporativa | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Presenton](human/fichas/presenton.md) | Tu objetivo encaja con estos ejemplos: Preparar una presentación desde un documento; Comparar una plantilla con generación libre | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Presentaciones

#### 🖥️ Slidev ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 49.5k<br>
**Qué es:** Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm init slidev` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una charla técnica; Explicar un ejemplo de código — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Mermaid](human/fichas/mermaid.md)<br>
**Más:** [ficha completa](human/fichas/slidev.md) · [GitHub](https://github.com/slidevjs/slidev)

#### 📊 ppt-master
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 76.8k<br>
**Qué es:** Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una presentación de un informe; Adaptar una plantilla corporativa — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/ppt-master.md) · [GitHub](https://github.com/hugohe3/ppt-master)

#### 🖥️ reveal.js
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 72.6k<br>
**Qué es:** Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://revealjs.com/installation); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una presentación web; Mostrar un ejemplo interactivo — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [markitdown](human/fichas/markitdown.md)<br>
**Más:** [ficha completa](human/fichas/reveal-js.md) · [GitHub](https://github.com/hakimel/reveal.js)

#### 🖥️ Marp
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 12.7k<br>
**Qué es:** Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separado.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/marp-team/marp/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar slides sencillas; Versionar una presentación en Git — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/marp.md) · [GitHub](https://github.com/marp-team/marp)

#### 🖥️ Presenton
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 11.9k<br>
**Qué es:** Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `docker run -it --name presenton \
  -p 5001:80 \
  -e AUTH_USERNAME=admin \
  -e AUTH_PASSWORD=change-this-password \
  -v "./app_data:/app_data" \
  ghcr.io/presenton/presenton:latest` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una presentación desde un documento; Comparar una plantilla con generación libre — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Ollama](human/fichas/ollama.md)<br>
**Más:** [ficha completa](human/fichas/presenton.md) · [GitHub](https://github.com/presenton/presenton)

### Diagramas y documentación

#### 🗺️ Mermaid ⭐
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 91.1k<br>
**Qué es:** Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/mermaid-js/mermaid/blob/develop/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar un proceso; Preparar un diagrama de secuencia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Slidev](human/fichas/slidev.md)<br>
**Más:** [ficha completa](human/fichas/mermaid.md) · [GitHub](https://github.com/mermaid-js/mermaid)

#### 📄 archify
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 96.5k<br>
**Qué es:** Skill para convertir ideas, planes y bases de código en diagramas y visualizaciones HTML interactivas.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Arranque:** [Instrucciones originales](https://github.com/tt-a1i/archify/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar una arquitectura; Preparar un plan de trabajo visual — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/archify.md) · [GitHub](https://github.com/tt-a1i/archify)

#### 🎨 diagram-design
**Etiquetas:** Ejecución 🏠 local · Rol 🎨 skill/prompt · Setup 🟡 medio · ⭐ 67.2k<br>
**Qué es:** Skill para que un agente cree diagramas explicativos con HTML y SVG, con criterios de composición y legibilidad.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Consumo del agente que ya utilizas<br>
**Comando documentado:** `npx skills add cathrynlavery/diagram-design` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar un proceso comercial; Explicar una arquitectura con SVG — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/diagram-design.md) · [GitHub](https://github.com/cathrynlavery/diagram-design)

---

## 🕷️ 32. Navegadores y automatización web

Navegadores, librerías de pruebas y agentes que interactúan con sitios web. Para leer páginas estáticas consulta extracción web; para operar una interfaz empieza por estas herramientas.

**⚖️ ¿Cuál elegir? — playwright, Puppeteer, Selenium**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [playwright](human/fichas/playwright.md) | Tu objetivo encaja con estos ejemplos: Probar un formulario; Crear regresiones de una web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Puppeteer](human/fichas/puppeteer.md) | Tu objetivo encaja con estos ejemplos: Automatizar una captura; Extraer datos de una página propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Selenium](human/fichas/selenium.md) | Tu objetivo encaja con estos ejemplos: Automatizar pruebas funcionales; Comparar comportamiento entre navegadores | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — Stagehand, browser-use, Skyvern**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [Stagehand](human/fichas/stagehand.md) | Tu objetivo encaja con estos ejemplos: Prototipar extracción estructurada; Automatizar un formulario de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [browser-use](human/fichas/browser-use.md) | Tu objetivo encaja con estos ejemplos: Extraer información de una web propia; Probar navegación con un agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [Skyvern](human/fichas/skyvern.md) | Tu objetivo encaja con estos ejemplos: Automatizar un flujo propio; Evaluar extracción basada en visión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**⚖️ ¿Cuál elegir? — agent-browser, playwright-cli**

| Repo | Elígelo si… | Evítalo si… |
|---|---|---|
| [agent-browser](human/fichas/agent-browser.md) | Tu objetivo encaja con estos ejemplos: Verificar una interfaz; Preparar capturas y consultas de una página | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| [playwright-cli](human/fichas/playwright-cli.md) | Tu objetivo encaja con estos ejemplos: Probar un flujo con un agente; Registrar una secuencia de navegación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

### Automatización y pruebas por código

#### 🎭 playwright
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 100k<br>
**Qué es:** Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm i -D @playwright/test
npx playwright install` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un formulario; Crear regresiones de una web — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [browser-use](human/fichas/browser-use.md) · [crawlee](human/fichas/crawlee.md)<br>
**Más:** [ficha completa](human/fichas/playwright.md) · [GitHub](https://github.com/microsoft/playwright)

#### 🌐 Puppeteer
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 95.8k<br>
**Qué es:** Librería de Google para controlar Chrome y Firefox desde Node.js.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm i puppeteer # Downloads compatible Chrome during installation.` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar una captura; Extraer datos de una página propia — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Lightpanda](human/fichas/lightpanda.md)<br>
**Más:** [ficha completa](human/fichas/puppeteer.md) · [GitHub](https://github.com/puppeteer/puppeteer)

#### 🌐 Selenium
**Etiquetas:** Ejecución 🏠 local · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 34.6k<br>
**Qué es:** Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://selenium.dev/documentation/); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar pruebas funcionales; Comparar comportamiento entre navegadores — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/selenium.md) · [GitHub](https://github.com/SeleniumHQ/selenium)

### Herramientas de navegación para agentes

#### 🌐 Stagehand ⭐
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil · ⭐ 26.1k<br>
**Qué es:** SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural.<br>
**Acceso:** API de IA necesaria · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pnpm add @browserbasehq/stagehand 'zod@~4.4.3'` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar extracción estructurada; Automatizar un formulario de prueba — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Mastra](human/fichas/mastra.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/stagehand.md) · [GitHub](https://github.com/browserbase/stagehand)

#### 🌐 browser-use
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio · ⭐ 121k<br>
**Qué es:** Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/browser-use/browser-use/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer información de una web propia; Probar navegación con un agente — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [playwright](human/fichas/playwright.md) · [gpt-researcher](human/fichas/gpt-researcher.md)<br>
**Más:** [ficha completa](human/fichas/browser-use.md) · [GitHub](https://github.com/browser-use/browser-use)

#### 🕷️ agent-browser
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🖥️ app · Setup 🟢 fácil · ⭐ 51.2k<br>
**Qué es:** CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `npm install -g agent-browser
agent-browser install           # download Chrome for Testing (first time only)` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Verificar una interfaz; Preparar capturas y consultas de una página — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/agent-browser.md) · [GitHub](https://github.com/vercel-labs/agent-browser)

#### 🌐 Skyvern
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio · ⭐ 23.4k<br>
**Qué es:** Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `pip install "skyvern[server]"` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar un flujo propio; Evaluar extracción basada en visión — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [n8n](human/fichas/n8n.md)<br>
**Más:** [ficha completa](human/fichas/skyvern.md) · [GitHub](https://github.com/Skyvern-AI/skyvern)

#### 🌐 Browser Harness
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 19.1k<br>
**Qué es:** Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/browser-use/browser-harness/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un agente con un browser propio; Inspeccionar una página autenticada de laboratorio — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Claude Code](human/fichas/claude-code.md) · [Codex CLI](human/fichas/codex.md)<br>
**Más:** [ficha completa](human/fichas/browser-harness.md) · [GitHub](https://github.com/browser-use/browser-harness)

#### 🎭 playwright-cli
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil · ⭐ 15.2k<br>
**Qué es:** Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · El coste depende del proveedor o la ruta<br>
**Comando documentado:** `npm install -g @playwright/cli@latest
playwright-cli --help` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un flujo con un agente; Registrar una secuencia de navegación — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [playwright](human/fichas/playwright.md) · [browser-use](human/fichas/browser-use.md)<br>
**Más:** [ficha completa](human/fichas/playwright-cli.md) · [GitHub](https://github.com/microsoft/playwright-cli)

### Navegadores y servidores de ejecución

#### 🌐 Lightpanda
**Etiquetas:** Ejecución 🏠 local · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil · ⭐ 42k<br>
**Qué es:** Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome.<br>
**Acceso:** API de IA opcional · El coste depende del proveedor o la ruta<br>
**Arranque:** [Instrucciones originales](https://github.com/lightpanda-io/browser/blob/main/README.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar navegación headless; Explorar un agente con modelo local — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Combina con:** [Puppeteer](human/fichas/puppeteer.md) · [playwright](human/fichas/playwright.md)<br>
**Más:** [ficha completa](human/fichas/lightpanda.md) · [GitHub](https://github.com/lightpanda-io/browser)

#### 🕷️ camofox-browser
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio · ⭐ 12.3k<br>
**Qué es:** Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Comando documentado:** `git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# -> http://localhost:9377` (comprobar los pasos completos en la ficha).<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Probar automatización de una web propia; Evaluar una herramienta de navegación para agentes — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/camofox-browser.md) · [GitHub](https://github.com/jo-inc/camofox-browser)

### Directorios y recursos de navegador

#### 🕷️ awesome-chrome-devtools
**Etiquetas:** Ejecución 🏠 local · Rol 📂 catálogo/recurso · Setup 🟢 fácil · ⭐ 7.2k<br>
**Qué es:** Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol.<br>
**Acceso:** Sin clave propia de API de IA en la ruta básica · Sin pago a un modelo en la ruta básica<br>
**Arranque:** [Instrucciones originales](https://github.com/ChromeDevTools/awesome-chrome-devtools/blob/master/readme.md); no se deduce un paquete por el nombre.<br>
**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una herramienta de depuración; Explorar clientes de DevTools Protocol — **Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo<br>
**Más:** [ficha completa](human/fichas/awesome-chrome-devtools.md) · [GitHub](https://github.com/ChromeDevTools/awesome-chrome-devtools)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
