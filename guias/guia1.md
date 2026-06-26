# 🌌 Catálogo de Repositorios de IA & Automatización


---

### Leyenda de badges

Cada ficha abre con una línea **Etiquetas:** que nombra cada valor — `Ejecución <x> · [MCP 🔌 ·] Rol <y> · Setup <z>`:

- **Ejecución:** 🏠 local-first (corre en tu máquina, sin depender de un servicio externo) · ☁️ API/cloud (depende de un proveedor o servicio remoto) · 🔀 híbrido (puede operar local o vía API según la configuración)
- **MCP:** 🔌 expone o consume Model Context Protocol — el estándar abierto que permite que asistentes como Claude o Cursor usen herramientas y datos externos de forma uniforme
- **Rol:** ⚙️ plataforma (producto integral con UI y backend) · 🧩 motor/runtime (componente que ejecuta lógica de IA) · 📚 librería/SDK (importas desde tu código) · 🎨 skill/prompt (instrucción o habilidad para un asistente) · 📂 directorio/recurso (catálogo o índice curado) · 🖥️ app/UI (aplicación visual con interfaz propia)
- **Setup:** 🟢 fácil (un comando CLI o instalar paquete) · 🟡 medio (requiere configurar servicios, credenciales o dependencias) · 🔴 pesado (necesita GPU, infraestructura o self-host con varios componentes)

---

<!-- BL_ALEXANDRIA_STATUS -->
> Estado actual: **185 repos detectados** en la biblioteca local; **186 repos curados** con ficha completa en esta guía. Los repos nuevos sin ficha curada se agregan al apéndice automático sin reescribir el cuerpo editorial.
<!-- /BL_ALEXANDRIA_STATUS -->

## 📂 Mapa de categorías


| # | Categoría | Repos | Para qué |
|---|---|---|---|
| 1 | [Automatización, Mensajería & CRM](#1-automatización-mensajería--crm) | 12 | WhatsApp, workflows, CRM, email, notificaciones — bots de venta, gateways multicanal, bandejas de soporte |
| 2 | [Skills, Prompts & Guías de Agente](#2-skills-prompts--guías-de-agente) | 21 | Habilidades `SKILL.md`, playbooks, calidad de prompts — catálogos de skills, anti-slop, metodologías de agente |
| 3 | [Frameworks & Orquestación de Agentes](#3-frameworks--orquestación-de-agentes) | 18 | Multiagente, research autónomo, low-code de IA — crews, grafos de agentes, builders visuales |
| 4 | [Scraping, Búsqueda & Research Web](#4-scraping-búsqueda--research-web) | 14 | Crawling, extracción, navegación con LLM — scrapers, navegadores agentizados, datasets sociales |
| 5 | [MCP & Conectividad](#5-mcp--conectividad) | 7 | Servidores/clientes MCP, APIs públicas — SDK del protocolo, servidores de referencia, directorios |
| 6 | [Memoria, LLM Ops & Observabilidad](#6-memoria-llm-ops--observabilidad) | 10 | Memoria de agentes, gateways, trazas, logging — memorias persistentes, proxies de LLM, telemetría |
| 7 | [Inteligencia de Código, Datos & Entrenamiento](#7-inteligencia-de-código-datos--entrenamiento) | 13 | Indexar repos, grafos, entrenar modelos desde cero — codegraph, RAG sobre código, nanoGPT/llm.c |
| 8 | [Workspaces de IA Local & Notebooks](#8-workspaces-de-ia-local--notebooks) | 5 | Entornos privados todo-en-uno, NotebookLM — asistentes locales soberanos, clones open-source |
| 9 | [Diseño, UI & Frontend](#9-diseño-ui--frontend) | 15 | Diseño asistido, libs de componentes, animación, 3D — Figma open-source, shadcn/Tailwind, GSAP/three.js |
| 10 | [Analítica & Visualización](#10-analítica--visualización) | 7 | Product analytics, dashboards, gráficos — PostHog, Metabase, ECharts, uPlot, Streamlit |
| 11 | [Generación de Imagen & Visión](#11-generación-de-imagen--visión) | 15 | Difusión, control, restauración, rostros — ComfyUI, SD WebUI, ControlNet, GFPGAN, LivePortrait |
| 12 | [Audio, Voz & Video](#12-audio-voz--video) | 15 | STT, TTS, edición y render de video — whisper/whisperX, supertonic, moviepy/remotion, lossless-cut |
| 13 | [Documentos & Presentaciones](#13-documentos--presentaciones) | 4 | Conversión a Markdown, PPTX, PDF, slides — markitdown, ppt-master, reveal.js, pdfcraft |

> Cada repo vive en **una** categoría; los cruces se resuelven con "Combina con". Excluidos por ser propios: `Binarias_Labs_C21`, `Binarias_Labs_Pruebas`.

---

## 🔗 Recetas de integración (stacks listos)

Combos end-to-end que unen varios repos. Útiles cuando un repo solo no resuelve el flujo completo.

### 🟢 1. Bot de WhatsApp con IA
**Objetivo:** atención/ventas automatizada por WhatsApp con un agente LLM.
**Stack:** [evolution-api](#-evolution-api) (canal WhatsApp) → [n8n](#-n8n) (orquestación) + [n8n-mcp](#-n8n-mcp) y [n8n-skills](#-n8n-skills) (que Claude construya los flujos) → LLM → [chatwoot](#-chatwoot) (handoff a humano) + [novu](#-novu) (notificaciones).
**Cómo encaja:** evolution-api recibe/envía mensajes vía webhook; n8n enruta y llama al LLM; chatwoot centraliza cuando entra un agente humano.
**Cuándo NO:** si solo necesitas respuestas simples sin handoff humano, basta con evolution-api + un webhook propio; si no quieres self-host, usa un SaaS de WhatsApp.

### 🎬 2. Pipeline de Reels / video corto
**Objetivo:** convertir contenido en video corto con voz y subtítulos.
**Stack:** [whisperX](#-whisperx) (subtítulos alineados) + [supertonic](#-supertonic) o [TTS](#-tts) (voz) + [ComfyUI](#-comfyui) o [Fooocus](#-fooocus) (visuales) + [Real-ESRGAN](#-real-esrgan) (upscale) → [moviepy](#-moviepy) o [remotion](#-remotion) (ensamblaje) → [lossless-cut](#-lossless-cut) (corte final).
**Cómo encaja:** [videofy_minimal](#-videofy_minimal) puede orquestar el flujo simple; remotion/moviepy escalan a variantes programáticas.
**Cuándo NO:** si no tienes GPU para los modelos de difusión, usa un servicio de generación de imagen en la nube; si solo necesitas cortar y subtitular un video existente, whisperX + lossless-cut bastan.

### 🔎 3. Agente de research profundo
**Objetivo:** investigación citada y estructurada a partir de la web.
**Stack:** [gpt-researcher](#-gpt-researcher) o [deer-flow](#-deer-flow) (orquestador) + [firecrawl](#-firecrawl) / [crawl4ai](#-crawl4ai) (extracción) + [browser-use](#-browser-use) (navegación) + [markitdown](#-markitdown) (ingesta) + [langfuse](#-langfuse) (trazas).
**Cómo encaja:** el orquestador coordina sub-agentes que extraen, leen y sintetizan; firecrawl/crawl4ai convierten páginas a Markdown limpio; browser-use maneja sitios dinámicos; langfuse registra cada paso para depurar.
**Cuándo NO:** si la investigación es sobre fuentes internas (no web), prescinde de firecrawl/browser-use y usa markitdown + RAG local.

### 🏠 4. Workspace privado local soberano
**Objetivo:** asistente todo-en-uno sin fuga de datos.
**Stack:** [odysseus](#-odysseus) (workspace) + [open-notebook](#-open-notebook) (conocimiento) + [ECC](#-ecc) (control seguro de agentes) + Ollama (modelos) + [mem0](#-mem0) (memoria).
**Cómo encaja:** odysseus centraliza chat, docs y tareas; open-notebook indexa tus fuentes con RAG local; ECC valida lo que el agente ejecuta en tu sistema; mem0 da memoria entre sesiones.
**Cuándo NO:** si no te importa la soberanía de datos, un SaaS (NotebookLM, Copilot) es más simple; si tu hardware no corre modelos locales, usa APIs comerciales con ECC.

### 🧠 5. Análisis de repos grandes
**Objetivo:** que un asistente entienda una base de código enorme barato.
**Stack:** [codegraph](#-codegraph) (índice local) + [graphify](#-graphify) / [graphrag](#-graphrag) (grafo) + [GitNexus](#-gitnexus) (exploración) + Claude Code.
**Cómo encaja:** codegraph indexa el repo en un grafo local; graphify/graphrag enriquecen las relaciones; GitNexus expone la navegación; Claude Code consulta el índice para responder sobre el código.
**Cuándo NO:** si el repo es pequeño (<10k líneas), Claude Code con `@` references basta; si necesitas análisis跨-repo, combina varios codegraph.

### 📈 6. Marketing de agencia
**Objetivo:** operar campañas y contenido a escala.
**Stack:** [marketingskills](#-marketingskills) + [agency-agents](#-agency-agents) (playbooks) + [mautic](#-mautic) (automatización) + [listmonk](#-listmonk) (email) + [posthog](#-posthog) / [metabase](#-metabase) (analítica) + [Open-Generative-AI](#-open-generative-ai) (creativos).
**Cómo encaja:** los playbooks guían al agente en cada canal; mautic segmenta y nutre leads; listmonk envía newsletters; posthog/metabase miden conversión; Open-Generative-AI genera visuales.
**Cuándo NO:** si operas una sola marca pequeña, mautic es excesivo; si no necesitas email masivo, prescinde de listmonk.

### 🌐 7. Web app moderna con IA
**Objetivo:** construir frontend pulido rápido.
**Stack:** [open-design](#-open-design) o [plasmic](#-plasmic) (diseño→código) + [tailwindcss](#-tailwindcss) + [heroui](#-heroui) o [ui](#-ui-shadcn) (componentes) + [GSAP](#-gsap) / [motion](#-motion) / [three.js](#-threejs) (animación/3D) + [swr](#-swr) (datos) + [echarts](#-echarts) / [uPlot](#-uplot) (gráficos).
**Cómo encaja:** open-design/plasmic generan la estructura visual; Tailwind + shadcn/heroui dan componentes pulidos; GSAP/motion/three.js añaden animación; SWR gestiona el fetch; echarts/uPlot renderizan datos.
**Cuándo NO:** si el proyecto es una landing estática, Tailwind + un componente de hero bastan; si necesitas un dashboard complejo, prioriza echarts/streamlit sobre animación.

### 🔌 8. Construir una app/servidor MCP
**Objetivo:** exponer datos o herramientas propias a asistentes.
**Stack:** [mcp-use](#-mcp-use) (framework) + [mcp](#-mcp) (SDK) + [servers](#-servers) (ejemplos de referencia) + [awesome-mcp-servers](#-awesome-mcp-servers) (qué ya existe).
**Cómo encaja:** mcp-use abstrae el protocolo para que pases de prototipo a app desplegable; mcp da el SDK base; servers muestra patrones reales; awesome-mcp-servers evita que reinventes lo que ya existe.
**Cuándo NO:** si solo necesitas consumir un servidor MCP existente, no construyas uno — busca en awesome-mcp-servers primero.

### 📊 9. Documentos → presentaciones
**Objetivo:** pasar texto/informes a slides editables.
**Stack:** [markitdown](#-markitdown) (todo → Markdown limpio) → [ppt-master](#-ppt-master) (PPTX) o [reveal.js](#-revealjs) (slides web).
**Cómo encaja:** markitdown normaliza cualquier formato (PDF, DOCX, HTML) a Markdown; ppt-master genera PPTX editable en Office; reveal.js produce slides web navegables.
**Cuándo NO:** si el contenido ya está en Markdown, salta markitdown; si necesitas diseño pixel-perfect, una herramienta de slides dedicada (Gamma, Pitch) da más control.

---

## 1. Automatización, Mensajería & CRM

WhatsApp, motores de workflow, CRM, email y notificaciones.

### 🔍 Escaneo rápido

| Repo | Qué es | Ejec. | Elige si… |
|---|---|---|---|
| [twenty-main](#-twenty-main) | CRM open-source tipo Salesforce | 🔀 | Quieres un CRM versionable como código |
| [evolution-api](#-evolution-api) | API multi-instancia de WhatsApp | 🏠 | Necesitas WhatsApp robusto en producción |
| [OpenWA](#-openwa) | SDK ligero de WhatsApp | 🏠 | Prototipas un bot simple sin infra pesada |
| [whatsapp-agentkit](#-whatsapp-agentkit) | Plantilla guiada de bot WhatsApp | 🔀 | Quieres un bot en <30 min sin programar |
| [activepieces](#-activepieces) | Automatización tipo Zapier (MCP) | 🔀 | Buscas low-code extensible con IA |
| [n8n](#-n8n) | Motor de workflows self-host | 🏠 | Necesitas automatización seria y flexible |
| [n8n_io](#-n8n_io) | Espejo del repo oficial de n8n | 🏠 | (duplicado — usa `n8n`) |
| [huginn](#-huginn) | Agentes por eventos/polling | 🏠 | Monitoreas fuentes y reaccionas a cambios |
| [mautic](#-mautic) | Marketing automation open-source | 🏠 | Quieres segmentación y nurturing soberano |
| [chatwoot](#-chatwoot) | Bandeja unificada de soporte | 🏠 | Centralizas conversaciones multicanal |
| [listmonk](#-listmonk) | Newsletters y listas de correo | 🏠 | Email masivo self-hosted y rápido |
| [novu](#-novu) | Infra de notificaciones multicanal | 🔀 | Unificas email/SMS/push/chat en un backend |

### ⚖️ ¿Cuál elegir? — Canal de WhatsApp

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **evolution-api** | Producción, múltiples instancias | Escala con Docker + webhooks | Solo quieres un prototipo rápido |
| **OpenWA** | Scripts/bots individuales | Ligero, SDK Python/JS | Necesitas alta disponibilidad |
| **whatsapp-agentkit** | Arranque sin código | Genera el bot con Claude Code | Quieres control total del stack |

### ⚖️ ¿Cuál elegir? — Plataforma de automatización

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **n8n** | Workflows complejos de negocio | Cientos de nodos + IA nativa | Quieres algo minimalista |
| **activepieces** | Reemplazo de Zapier con IA | Piezas TS + MCP, low-code | Ya tienes ecosistema n8n maduro |
| **huginn** | Monitoreo por eventos | Agents encadenables/polling | Necesitas editor visual amigable |
| **mautic** | Marketing/email nurturing | Segmentación y campañas | Solo necesitas automatización genérica |

### 👥 twenty-main
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** CRM open-source orientado a desarrolladores, alternativa moderna y personalizable a Salesforce/HubSpot que modela tu negocio mediante objetos y campos propios.
**Por qué destaca:** es uno de los CRM open-source más populares y con mayor crecimiento en GitHub, valorado por su UI moderna y su enfoque versionable como código.
**Cómo funciona:** una arquitectura basada en metadatos define objetos, campos y relaciones sobre PostgreSQL, con backend NestJS y frontend React.
**Instalación:** vía `docker compose` con la imagen oficial, o clonando el repo y levantando los servicios con el stack Node/PostgreSQL.
**Casos:** pipelines de venta versionados como código · panel a medida con objetos/campos propios.
**Stack:** TypeScript, React, NestJS, PostgreSQL, Docker — **Modelo/API:** opcional (plugins Claude Code/Codex para consultar el CRM en lenguaje natural).
**Elige si:** quieres un CRM que se adapte 1:1 a tu negocio — **Evita si:** buscas algo plug-and-play sin self-host.
**Combina con:** [evolution-api](#-evolution-api) · [n8n](#-n8n)
**Repo:** [GitHub](https://github.com/twentyhq/twenty)

### 🧬 evolution-api
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** API REST robusta que actúa como middleware para automatizar WhatsApp y mensajería multicanal, exponiendo el envío/recepción de mensajes a tus aplicaciones.
**Por qué destaca:** es una de las puertas de enlace de WhatsApp open-source más usadas en LATAM y Brasil para entornos de producción, con comunidad activa y soporte de webhooks.
**Cómo funciona:** mantiene sesiones de WhatsApp por instancia y reenvía eventos vía webhooks, apoyándose en Node.js/Fastify y Redis para estado y colas.
**Instalación:** despliegue habitual con `docker compose` usando la imagen oficial, configurando variables de entorno y Redis.
**Casos:** notificaciones de pedidos/facturas · enrutar mensajes a agentes vía webhook.
**Stack:** Node.js/TypeScript, Fastify, Redis, Docker — **Modelo/API:** no usa IA directa; es el puente al LLM.
**Elige si:** operas WhatsApp en producción — **Evita si:** solo necesitas un bot de prueba.
**Combina con:** [n8n](#-n8n) · [chatwoot](#-chatwoot) · receta [Bot WhatsApp](#-1-bot-de-whatsapp-con-ia)
**Repo:** [GitHub](https://github.com/EvolutionAPI/evolution-api)

### 🌐 OpenWA
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraestructura pesada.
**Por qué destaca:** muy adoptado para prototipos y bots individuales por su simplicidad y su API expresiva, con una comunidad consolidada alrededor de wa-automate.
**Cómo funciona:** controla una sesión de WhatsApp Web mediante automatización del navegador y expone eventos y métodos a tus scripts en Node.js (y bindings para Python).
**Instalación:** vía `npm i @open-wa/wa-automate` en proyectos Node.js (o el paquete equivalente para Python).
**Casos:** bot que escucha eventos y ejecuta scripts locales · respuestas rápidas con panel local.
**Stack:** Python, JavaScript/Node.js — **Modelo/API:** no nativa (requiere orquestación externa).
**Elige si:** desarrollas scripts independientes — **Evita si:** necesitas infra multi-instancia.
**Combina con:** [n8n](#-n8n) · [evolution-api](#-evolution-api)
**Repo:** [GitHub](https://github.com/open-wa/wa-automate-nodejs)

### 🤖 whatsapp-agentkit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de programar, partiendo de preguntas sobre tu negocio.
**Por qué destaca:** baja drásticamente la barrera de entrada al delegar la generación del código en un asistente de IA, ideal para arranques rápidos y no técnicos.
**Cómo funciona:** un flujo de preguntas conversacionales alimenta a Claude Code, que autogenera el código del bot y la configuración del webhook de WhatsApp.
**Instalación:** `git clone` del repo y seguir el asistente con Claude Code para generar y desplegar el bot.
**Casos:** prototipo de atención al cliente · setup de webhook por preguntas conversacionales.
**Stack:** Node.js/Python, APIs de WhatsApp — **Modelo/API:** Claude (Code / Sonnet) para la autogeneración.
**Elige si:** quieres arrancar sin partir de cero — **Evita si:** necesitas control fino del stack.
**Combina con:** [evolution-api](#-evolution-api) · [n8n-mcp](#-n8n-mcp)
**Repo:** [GitHub](https://github.com/Hainrixz/whatsapp-agentkit)

### 🧩 activepieces
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y piezas reutilizables.
**Por qué destaca:** muy adoptada como reemplazo open-source de Zapier, destaca por su soporte temprano de MCP y por permitir crear piezas propias en TypeScript.
**Cómo funciona:** ejecuta flujos de pasos (triggers y acciones) basados en "pieces" en TypeScript, con motor Node.js y soporte de conectores de IA y MCP.
**Instalación:** vía `docker compose` para self-host, o usando su versión cloud.
**Casos:** lead → consulta CRM → notifica al equipo · flujos para usuarios técnicos y no técnicos.
**Stack:** Node.js, TypeScript, self-host/web — **Modelo/API:** OpenAI, Anthropic, MCP.
**Elige si:** quieres reemplazar Zapier con piezas propias — **Evita si:** ya dominas n8n.
**Combina con:** [n8n](#-n8n) · [novu](#-novu)
**Repo:** [GitHub](https://github.com/activepieces/activepieces)

### 🔁 n8n
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos.
**Por qué destaca:** se ha convertido en un estándar de facto para automatización self-hosted, muy adoptado por su enorme catálogo de nodos y su fuerte integración de IA.
**Cómo funciona:** encadena nodos (triggers, transformaciones, integraciones) en un grafo de workflow ejecutado por un runtime Node.js, con nodos de IA basados en LangChain.
**Instalación:** vía `docker compose` o imagen Docker oficial; también `npx n8n` para una prueba rápida local.
**Casos:** extraer leads → enriquecer con IA → notificar · pipelines de negocio sin SaaS cerrado.
**Stack:** Node.js, Docker — **Modelo/API:** múltiples por nodo; se potencia con MCP y LLMs.
**Elige si:** quieres el motor central de automatización — **Evita si:** buscas algo minimalista.
**Combina con:** [n8n-mcp](#-n8n-mcp) · [n8n-skills](#-n8n-skills) · [evolution-api](#-evolution-api)
**Repo:** [GitHub](https://github.com/n8n-io/n8n)

### 🔁 n8n_io
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** copia local del repositorio oficial de n8n (mismo proyecto que [n8n](#-n8n)), mantenida como referencia o espejo del código fuente.
**Por qué destaca:** no aporta valor propio frente a la ficha principal; existe solo como duplicado del proyecto oficial.
**Cómo funciona:** es idéntica a n8n; encadena nodos en workflows ejecutados por un runtime Node.js.
**Instalación:** la misma que n8n (`docker compose`, imagen Docker oficial o `npx n8n`).
**Casos:** referencia/duplicado del código fuente de n8n.
**Stack:** Node.js — **Modelo/API:** igual que n8n.
**Elige si:** — **Evita si:** ya usas la ficha [n8n](#-n8n) (es el mismo proyecto).
**Combina con:** ver [n8n](#-n8n)
**Repo:** [GitHub](https://github.com/n8n-io/n8n)

### 🤖 huginn
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú".
**Por qué destaca:** proyecto veterano y muy respetado en la comunidad open-source para monitoreo y scraping, valorado por su privacidad y su modelo de agentes encadenables.
**Cómo funciona:** define "agents" que hacen polling o reciben webhooks y se conectan entre sí pasando eventos, sobre un stack Ruby on Rails con base de datos.
**Instalación:** vía `docker` (imagen oficial) o desplegando la app Rails manualmente.
**Casos:** vigilar fuentes externas y disparar acciones · scraping + reglas de automatización.
**Stack:** Ruby, Node.js, BD, self-host — **Modelo/API:** no nativa; se integra vía APIs.
**Elige si:** automatizas tareas orientadas a eventos — **Evita si:** quieres editor visual amigable.
**Combina con:** [n8n](#-n8n) · [novu](#-novu)
**Repo:** [GitHub](https://github.com/huginn/huginn)

### 📣 mautic
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo.
**Por qué destaca:** es la solución de marketing automation open-source más conocida y madura, respaldada por una fundación y comunidad amplia.
**Cómo funciona:** ejecuta campañas, scoring de leads y nurturing por email mediante reglas y segmentos, sobre una aplicación PHP con base de datos MySQL.
**Instalación:** vía `docker compose` o instalación PHP/MySQL tradicional sobre un servidor web.
**Casos:** nurturing por email · campañas segmentadas y scoring de leads.
**Stack:** PHP, MySQL, self-host — **Modelo/API:** no nativa; complementa flujos de contenido IA.
**Elige si:** necesitas automatización de marketing seria — **Evita si:** te basta una newsletter simple ([listmonk](#-listmonk)).
**Combina con:** [listmonk](#-listmonk) · [marketingskills](#-marketingskills) · receta [Marketing de agencia](#-6-marketing-de-agencia)
**Repo:** [GitHub](https://github.com/mautic/mautic)

### 💬 chatwoot
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada.
**Por qué destaca:** es una de las alternativas open-source más populares a Intercom/Zendesk, valorada por centralizar el soporte multicanal con handoff humano.
**Cómo funciona:** centraliza conversaciones por canal en una bandeja con tickets y agentes, sobre un stack Ruby on Rails con PostgreSQL y Redis para tiempo real.
**Instalación:** vía `docker compose` con la imagen oficial, o instalación manual del stack Rails.
**Casos:** centralizar WhatsApp/web/correo en un panel · tickets y agentes.
**Stack:** Ruby on Rails, Node.js, PostgreSQL, Redis, Docker — **Modelo/API:** integración externa de IA.
**Elige si:** das soporte por varios canales — **Evita si:** solo necesitas enviar mensajes salientes.
**Combina con:** [evolution-api](#-evolution-api) · [novu](#-novu)
**Repo:** [GitHub](https://github.com/chatwoot/chatwoot)

### 📬 listmonk
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS.
**Por qué destaca:** muy popular por su rapidez y su single-binary en Go, es una opción ligera y soberana muy recomendada para email masivo.
**Cómo funciona:** gestiona listas, suscriptores y campañas desde un panel y envía vía SMTP, sobre un binario en Go con base de datos PostgreSQL.
**Instalación:** vía `docker compose` o descargando el binario único de Go y apuntándolo a PostgreSQL.
**Casos:** newsletter propia para leads · campañas de email desde workflows.
**Stack:** Go, PostgreSQL, self-host — **Modelo/API:** no nativa; integrable con generadores de contenido.
**Elige si:** quieres email marketing simple y propio — **Evita si:** necesitas nurturing avanzado ([mautic](#-mautic)).
**Combina con:** [mautic](#-mautic) · [n8n](#-n8n)
**Repo:** [GitHub](https://github.com/knadh/listmonk)

### 🔔 novu
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend.
**Por qué destaca:** es el estándar open-source de referencia para notificaciones, muy adoptado por evitar integrar y mantener cada proveedor por separado.
**Cómo funciona:** define workflows de notificación que enrutan mensajes a distintos proveedores por canal, con un inbox unificado, sobre un stack Node.js/TypeScript.
**Instalación:** vía `docker compose` para self-host, o usando su plataforma cloud.
**Casos:** mensajes transaccionales y de producto desde un backend · inbox unificado.
**Stack:** Node.js, TypeScript, Docker — **Modelo/API:** compatible con agentes/automatizaciones externas.
**Elige si:** envías notificaciones por varios canales — **Evita si:** solo necesitas email ([listmonk](#-listmonk)).
**Combina con:** [chatwoot](#-chatwoot) · [activepieces](#-activepieces)
**Repo:** [GitHub](https://github.com/novuhq/novu)

---

## 2. Skills, Prompts & Guías de Agente

Habilidades `SKILL.md`, playbooks, guías `CLAUDE.md` y herramientas para mejorar prompts y comportamiento de agentes.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… |
|---|---|---|---|
| [andrej-karpathy-skills](#-andrej-karpathy-skills) | 4 principios para asistentes de código | 🎨 | Quieres respuestas más útiles y menos ruido |
| [antigravity-awesome-skills](#-antigravity-awesome-skills) | Catálogo de +1.678 skills | 📂 | Buscas skills ya hechas por dominio |
| [awesome-agent-skills](#-awesome-agent-skills) | Skills oficiales de marcas líderes | 📂 | Quieres skills de Anthropic/Google/Stripe… |
| [awesome-claude-code](#-awesome-claude-code) | Scripts/hooks/agentes para Claude Code | 📂 | Personalizas Claude Code a fondo |
| [superpowers](#-superpowers) | Metodología completa de desarrollo | 🎨 | Quieres un método composable para tu agente |
| [skills](#-skills) | Colección de skills (aihero.dev) | 📂 | Exploras skills de referencia |
| [claude-plugins-official](#-claude-plugins-official) | Plugins oficiales de Claude | 📂 | Buscas extensiones oficiales |
| [agents-towards-production](#-agents-towards-production) | Playbook agente→producto | 📂 | Llevas un agente de prototipo a prod |
| [Context-Engineering](#-context-engineering) | Curso/guía de ingeniería de contexto | 📂 | Quieres dominar el manejo del contexto |
| [agent-toolkit](#-agent-toolkit) | Skills de productividad diaria | 🎨 | Aceleras tareas repetitivas |
| [n8n-skills](#-n8n-skills) | 14 skills para flujos n8n sin fallos | 🎨 | Generas JSON de n8n sin errores |
| [marketingskills](#-marketingskills) | Skills de marketing/growth | 🎨 | Automatizas conversión, copy y SEO |
| [agency-agents](#-agency-agents) | Playbooks de agencia multicanal | 🎨 | Operas 50-200 marcas en paralelo |
| [geo-seo-claude](#-geo-seo-claude) | SEO/GEO para buscadores con IA | 🎨 | Optimizas para ChatGPT/Perplexity/AI Overviews |
| [prompt-master](#-prompt-master) | Genera prompts precisos para cualquier IA | 🎨 | Quieres acertar el prompt al primer intento |
| [ui-ux-pro-max-skill](#-ui-ux-pro-max-skill) | Inteligencia de diseño UI/UX | 🎨 | Elevas el acabado visual generado por IA |
| [taste-skill](#-taste-skill) | Skills anti-slop para frontends premium | 🎨 | Quieres UIs con mejor gusto, no boilerplate |
| [skills_emil](#-skills_emil) | Skills de colaboración diseño-dev | 🎨 | Mejoras el handoff diseñador↔ingeniero |
| [SkillSpector](#-skillspector) | Auditoría de seguridad de skills | 🎨 | Revisas skills por patrones riesgosos |
| [humanizer](#-humanizer) | Quita "tells" de texto IA | 🎨 | Quieres prosa que no suene a IA |
| [stop-slop](#-stop-slop) | Elimina patrones de "slop" en prosa | 🎨 | Pules estilo de escritura del LLM |

### ⚖️ ¿Cuál elegir? — Catálogos de skills vs. metodología

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **antigravity-awesome-skills** | Buscas una skill puntual ya hecha | Volumen (+1.678) y categorías | Quieres curaduría oficial |
| **awesome-agent-skills** | Quieres skills oficiales de marcas | Calidad/respaldo de marca | Necesitas máxima cantidad |
| **awesome-claude-code** | Específico de Claude Code | Hooks/agentes/extensiones | Usas otro asistente |
| **superpowers** | Quieres un método, no piezas sueltas | Metodología composable completa | Solo buscas una skill aislada |

### ⚖️ ¿Cuál elegir? — Anti-slop / calidad de escritura y diseño

| Repo | Foco | Ventaja clave |
|---|---|---|
| **humanizer** / **stop-slop** | Prosa más humana | Quitan tells y patrones de IA en texto |
| **taste-skill** / **ui-ux-pro-max-skill** / **impeccable** | Frontends con gusto | Layout, tipografía y motion superiores |
| **prompt-master** | Prompting | Prompts precisos sin reintentos |

### 🧠 andrej-karpathy-skills
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** guía de 4 principios (inspirada en las ideas de Andrej Karpathy sobre asistentes de código) que define cómo debe responder un agente para maximizar utilidad y reducir verbosidad innecesaria.
**Por qué destaca:** condensa una filosofía conocida en reglas cortas y portables entre herramientas, lo que la hace fácil de adoptar sin atarse a un asistente concreto.
**Cómo funciona:** se carga como `CLAUDE.md`/instrucciones de sistema que el asistente lee al inicio de la sesión y aplica a cada respuesta.
**Instalación:** clona el repo y copia el `CLAUDE.md` (o su contenido) en tu proyecto o en el directorio de configuración del asistente.
**Casos:** mejorar señal/ruido del asistente · base de buenas prácticas diarias.
**Stack:** Markdown (`CLAUDE.md`) — **Modelo/API:** Claude Code, Cursor, Gemini CLI.
**Elige si:** quieres respuestas más útiles ya — **Evita si:** buscas skills ejecutables concretas.
**Combina con:** [awesome-claude-code](#-awesome-claude-code) · [Context-Engineering](#-context-engineering)
**Repo:** [GitHub](https://github.com/multica-ai/andrej-karpathy-skills)

### 🗂️ antigravity-awesome-skills
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** catálogo masivo con más de 1.678 habilidades (`SKILL.md`) categorizadas por dominio (desarrollo, QA, DevOps, seguridad, marketing) listas para instalar en distintos asistentes.
**Por qué destaca:** su volumen y categorización lo convierten en un punto de partida cómodo para encontrar una skill ya hecha en lugar de reescribir prompts desde cero.
**Cómo funciona:** cada skill es una carpeta con su `SKILL.md`; copias la que necesites en el directorio de skills de tu asistente y este la descubre.
**Instalación:** clona el repo y copia las carpetas de skill deseadas a tu directorio de skills (por ejemplo `~/.claude/skills`); incluye CLI en Node/Python para ayudar a explorarlas.
**Casos:** encontrar una skill lista por dominio · evitar reinventar prompts.
**Stack:** Node.js (CLI), Python — **Modelo/API:** Claude Code, Cursor, Antigravity, Copilot, Kiro.
**Elige si:** quieres opciones por cantidad — **Evita si:** prefieres curaduría oficial ([awesome-agent-skills](#-awesome-agent-skills)).
**Combina con:** [SkillSpector](#-skillspector) · [awesome-agent-skills](#-awesome-agent-skills)
**Repo:** [GitHub](https://github.com/sickn33/antigravity-awesome-skills)

### 🏅 awesome-agent-skills
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** colección curada de habilidades oficiales y comunitarias publicadas por marcas líderes (Anthropic, Google, Stripe, Netlify…) como referencia de calidad para agentes.
**Por qué destaca:** la procedencia de marca da confianza sobre que las skills siguen buenas prácticas y se mantienen, frente a aportes anónimos.
**Cómo funciona:** lista y enlaza skills en formato `SKILL.md`/Markdown que copias al directorio de skills del asistente para activarlas.
**Instalación:** clona el repo (o sigue sus enlaces a cada fuente) y copia las skills elegidas al directorio de skills de tu asistente.
**Casos:** adoptar skills respaldadas por marca · referencia de calidad.
**Stack:** Markdown — **Modelo/API:** Claude Code, Codex, Antigravity, Gemini.
**Elige si:** valoras respaldo de marca — **Evita si:** necesitas máxima cantidad.
**Combina con:** [antigravity-awesome-skills](#-antigravity-awesome-skills)
**Repo:** [GitHub](https://github.com/VoltAgent/awesome-agent-skills)

### ⭐ awesome-claude-code
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** lista "awesome" curada de scripts, agentes, hooks, slash commands y extensiones específicos del ecosistema de Claude Code.
**Por qué destaca:** es una referencia muy seguida por quienes personalizan Claude Code, al reunir patrones probados por la comunidad en un solo lugar.
**Cómo funciona:** funciona como índice de recursos enlazados que copias o adaptas (hooks, comandos, configuraciones) dentro de tu instalación de Claude Code.
**Instalación:** clona o navega el repo y copia los recursos que quieras a tu configuración de Claude Code (`~/.claude`, hooks, comandos).
**Casos:** personalizar Claude Code · descubrir patrones probados.
**Stack:** Python / Markdown — **Modelo/API:** Claude Code.
**Elige si:** vives en Claude Code — **Evita si:** usas otro asistente.
**Combina con:** [claude-plugins-official](#-claude-plugins-official) · [superpowers](#-superpowers)
**Repo:** [GitHub](https://github.com/hesreallyhim/awesome-claude-code)

### 💪 superpowers
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque.
**Por qué destaca:** ofrece un sistema coherente en lugar de piezas sueltas, lo que da consistencia al flujo de trabajo del agente entre tareas.
**Cómo funciona:** combina skills modulares con metaprompts/instrucciones que el agente lee y encadena para seguir un método paso a paso.
**Instalación:** clona el repo y copia las skills e instrucciones a tu directorio de skills del asistente (p. ej. `~/.claude/skills`).
**Casos:** dar a tu agente un método consistente · estandarizar el flujo de desarrollo.
**Stack:** Markdown/skills — **Modelo/API:** Claude Code y compatibles.
**Elige si:** quieres método, no fragmentos — **Evita si:** solo necesitas una skill aislada.
**Combina con:** [awesome-claude-code](#-awesome-claude-code) · [agent-toolkit](#-agent-toolkit)
**Repo:** [GitHub](https://github.com/obra/superpowers)

### 📦 skills
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** colección de skills de referencia mantenida por el proyecto aihero.dev / Total TypeScript, pensada como ejemplos limpios y bien construidos.
**Por qué destaca:** su valor está en la claridad y el mantenimiento, sirviendo de plantilla para aprender a escribir tus propias skills.
**Cómo funciona:** cada skill es un `SKILL.md` (a veces con scripts TS asociados) que copias al directorio de skills del asistente.
**Instalación:** clona el repo y copia las skills elegidas a tu directorio de skills, o úsalas como referencia para crear las tuyas.
**Casos:** explorar ejemplos de skills bien construidas · base para crear las propias.
**Stack:** Markdown/TypeScript — **Modelo/API:** Claude Code y compatibles.
**Elige si:** buscas referencias limpias — **Evita si:** quieres un catálogo masivo.
**Combina con:** [awesome-agent-skills](#-awesome-agent-skills)
**Repo:** [GitHub](https://github.com/total-typescript/skills)

### 🔌 claude-plugins-official
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** plugins y extensiones oficiales para Claude, distribuidos junto al repositorio de Claude Code de Anthropic.
**Por qué destaca:** al venir directamente de Anthropic, ofrece procedencia oficial y compatibilidad garantizada frente a aportes de terceros.
**Cómo funciona:** se integran como plugins del cliente Claude Code, que los carga desde su configuración de plugins.
**Instalación:** sigue las instrucciones del repo oficial (clonar/instalar el plugin) y actívalo desde la configuración de plugins de Claude Code.
**Casos:** ampliar Claude con extensiones soportadas · referencia de plugins oficiales.
**Stack:** Markdown/JS — **Modelo/API:** Claude.
**Elige si:** quieres extensiones oficiales — **Evita si:** buscas aportes comunitarios amplios.
**Combina con:** [awesome-claude-code](#-awesome-claude-code)
**Repo:** [GitHub](https://github.com/anthropics/claude-code)

### 🎓 agents-towards-production
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟡 medio
**Qué es:** playbook open-source con tutoriales end-to-end para llevar agentes GenAI de prototipo a producto real, cubriendo el ciclo completo de producción.
**Por qué destaca:** es uno de los recursos más completos para producción, porque integra estado, memoria, despliegue, guardrails y observabilidad en un solo recorrido práctico.
**Cómo funciona:** ofrece notebooks y proyectos guiados que combinan frameworks de agentes con stack de despliegue (Docker, FastAPI) y herramientas de trazabilidad.
**Instalación:** clona el repo y sigue cada tutorial instalando sus dependencias Python (`pip install -r requirements.txt` por módulo).
**Casos:** workflows con estado, memoria vectorial, despliegue Docker/FastAPI, guardrails, observabilidad.
**Stack:** Python, varios — **Modelo/API:** múltiples.
**Elige si:** vas a producción con agentes — **Evita si:** solo experimentas localmente.
**Combina con:** [langfuse](#-langfuse) · [ag2](#-ag2)
**Repo:** [GitHub](https://github.com/NirDiamant/agents-towards-production)

### 🧩 Context-Engineering
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso.
**Por qué destaca:** aporta un marco conceptual sólido y didáctico en un tema cada vez más decisivo para el rendimiento de los agentes.
**Cómo funciona:** combina lecciones en Markdown y notebooks que enseñan técnicas de selección, compresión y estructuración de contexto, de forma agnóstica al modelo.
**Instalación:** clona el repo y abre los notebooks/Markdown localmente; no requiere instalación más allá de un entorno de notebooks.
**Casos:** diseñar prompts y contexto eficientes · entender límites de ventana.
**Stack:** Markdown/notebooks — **Modelo/API:** agnóstico.
**Elige si:** quieres profundizar en contexto — **Evita si:** buscas skills ejecutables.
**Combina con:** [andrej-karpathy-skills](#-andrej-karpathy-skills) · [headroom](#-headroom)
**Repo:** [GitHub](https://github.com/davidkimai/Context-Engineering)

### 🧰 agent-toolkit
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación.
**Por qué destaca:** vienen listas para usar en formato Agent Skills, reduciendo el tiempo de configuración para flujos profesionales comunes.
**Cómo funciona:** cada skill es un `SKILL.md` con scripts auxiliares que el asistente carga desde su directorio de skills.
**Instalación:** clona el repo y copia las carpetas de skill a tu directorio de skills de Claude Code.
**Casos:** acelerar tareas repetitivas · estandarizar flujos profesionales.
**Stack:** Markdown/scripts — **Modelo/API:** Claude Code.
**Elige si:** quieres productividad inmediata — **Evita si:** buscas un método integral ([superpowers](#-superpowers)).
**Combina con:** [superpowers](#-superpowers)
**Repo:** [GitHub](https://github.com/leonardocouy/agent-toolkit)

### 🛠️ n8n-skills
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando errores al generar su JSON.
**Por qué destaca:** ataca un problema concreto y frecuente —el JSON de n8n generado por IA suele fallar— reduciendo bucles de error y timeouts.
**Cómo funciona:** las skills aportan plantillas y reglas de validación que guían al modelo a producir nodos y conexiones n8n sintácticamente válidos.
**Instalación:** clona el repo y copia las skills (`SKILL.md`) a tu directorio de skills de Claude Code u otro asistente compatible.
**Casos:** evitar errores de sintaxis al generar JSON de n8n · plantillas de workflows complejos.
**Stack:** `SKILL.md`, Markdown — **Modelo/API:** Claude Code u otro que lea skills.
**Elige si:** generas workflows n8n con IA — **Evita si:** no usas n8n.
**Combina con:** [n8n](#-n8n) · [n8n-mcp](#-n8n-mcp)
**Repo:** [GitHub](https://github.com/czlonkowski/n8n-skills)

### 📈 marketingskills
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** colección de skills de marketing que cubren conversión, copywriting, SEO, analítica y growth para usar con agentes de código.
**Por qué destaca:** está pensada para marketers técnicos y founders, agrupando tareas de growth habituales en skills reutilizables.
**Cómo funciona:** cada skill es un `SKILL.md` con instrucciones de dominio que el asistente carga para ejecutar la tarea de marketing correspondiente.
**Instalación:** clona el repo y copia las skills a tu directorio de skills (Claude Code, Codex, Cursor o Windsurf).
**Casos:** optimización de conversión · copywriting y landing assistido.
**Stack:** Markdown/skills — **Modelo/API:** Claude Code, Codex, Cursor, Windsurf.
**Elige si:** automatizas marketing con agentes — **Evita si:** necesitas ejecución (no skills).
**Combina con:** [agency-agents](#-agency-agents) · [mautic](#-mautic) · receta [Marketing de agencia](#-6-marketing-de-agencia)
**Repo:** [GitHub](https://github.com/coreyhaines31/marketingskills)

### 🏢 agency-agents
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟡 medio
**Qué es:** conjunto de playbooks y agentes especializados (incluye un Digital Marketing Pro) diseñados para operar una agencia multicanal a escala.
**Por qué destaca:** orientado a operaciones reales de agencia, con flujos estructurados y alineación a regulación (EU AI Act) para gestionar muchas marcas a la vez.
**Cómo funciona:** define agentes y playbooks (flujo estratégico de 12 partes, atribución de embudos) ejecutados sobre un stack Python/Node.js con modelos de frontera.
**Instalación:** clona el repo e instala sus dependencias (Python/Node.js) siguiendo el README para configurar los agentes.
**Casos:** flujo estratégico de 12 partes · análisis de atribución de embudos.
**Stack:** Python, Node.js — **Modelo/API:** Claude 3.5 Sonnet y multimodales de frontera.
**Elige si:** operas una agencia — **Evita si:** eres un solo proyecto pequeño.
**Combina con:** [marketingskills](#-marketingskills) · [geo-seo-claude](#-geo-seo-claude)
**Repo:** [GitHub](https://github.com/msitarzewski/agency-agents)

### 🌍 geo-seo-claude
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** skill GEO-first con soporte SEO clásico para optimizar la visibilidad de sitios ante motores de búsqueda con IA (Generative Engine Optimization).
**Por qué destaca:** se enfoca en "hacia dónde va el tráfico" (respuestas de IA) en lugar de solo el SEO tradicional, anticipando el cambio en el descubrimiento.
**Cómo funciona:** la skill aporta criterios y checklists que el asistente aplica para estructurar contenido optimizado para ChatGPT, Claude, Perplexity, Gemini y AI Overviews.
**Instalación:** clona el repo y copia el `SKILL.md` a tu directorio de skills de Claude Code o asistente compatible.
**Casos:** visibilidad en ChatGPT/Claude/Perplexity/Gemini/AI Overviews · base SEO tradicional.
**Stack:** Markdown/skill — **Modelo/API:** Claude Code y compatibles.
**Elige si:** te importa el descubrimiento por IA — **Evita si:** solo haces SEO clásico.
**Combina con:** [marketingskills](#-marketingskills) · [agency-agents](#-agency-agents)
**Repo:** [GitHub](https://github.com/zubair-trabzada/geo-seo-claude)

### 🎯 prompt-master
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** skill que ayuda a redactar prompts precisos para cualquier herramienta de IA, buscando el mejor resultado sin desperdiciar tokens.
**Por qué destaca:** es transversal a casi cualquier IA (texto, imagen, video, código), lo que la hace útil como capa de "meta-prompting" reutilizable.
**Cómo funciona:** la skill guía al asistente para clarificar la intención y construir el prompt óptimo, conservando contexto y memoria entre iteraciones.
**Instalación:** clona el repo y copia el `SKILL.md` a tu directorio de skills, o pega su contenido como instrucción en la IA que uses.
**Casos:** acertar el prompt al primer intento · retención de contexto y memoria.
**Stack:** Markdown/skill — **Modelo/API:** Claude, ChatGPT, Gemini, Cursor, Midjourney, etc.
**Elige si:** quieres dejar de re-promptear — **Evita si:** ya tienes prompts afinados.
**Combina con:** [andrej-karpathy-skills](#-andrej-karpathy-skills)
**Repo:** [GitHub](https://github.com/nidhinjs/prompt-master)
