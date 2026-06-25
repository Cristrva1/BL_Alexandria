# 🌌 Catálogo de Repositorios de IA & Automatización

Catálogo operativo de los **185 repositorios** locales del workspace, diseñado para **entender, comparar, elegir y combinar** repos rápido.

---

## 🧭 Cómo usar esta guía

Hay **tres formas de leerla** según lo que necesites:

| Si quieres… | Ve a… |
|---|---|
| **Barrer todo de un vistazo** y filtrar candidatos | La **tabla de escaneo** al inicio de cada categoría |
| **Decidir entre repos parecidos** (¿whisper o whisperX?) | Las **comparativas "¿cuál elegir?"** dentro de cada categoría |
| **Montar algo end-to-end** combinando varios | Las [**Recetas de integración**](#-recetas-de-integración-stacks-listos) |

> Cada ficha incluye un campo **Combina con** que enlaza a repos complementarios: ese es el hilo para descubrir integraciones sin salir de la ficha.

### Leyenda de badges

Cada ficha abre con una línea **Etiquetas:** que nombra cada valor — `Ejecución <x> · [MCP 🔌 ·] Rol <y> · Setup <z>`:

- **Ejecución:** 🏠 local-first · ☁️ API/cloud · 🔀 híbrido (local o API)
- **MCP:** 🔌 expone o consume Model Context Protocol
- **Rol:** ⚙️ plataforma · 🧩 motor/runtime · 📚 librería/SDK · 🎨 skill/prompt · 📂 directorio/recurso · 🖥️ app/UI
- **Setup:** 🟢 fácil (CLI/instalar) · 🟡 medio (config/servicios) · 🔴 pesado (GPU/infra/self-host)

---

<!-- BL_ALEXANDRIA_STATUS -->
> Estado actual: **185 repos detectados** en la biblioteca local; **186 repos curados** con ficha completa en esta guía. Los repos nuevos sin ficha curada se agregan al apéndice automático sin reescribir el cuerpo editorial.
<!-- /BL_ALEXANDRIA_STATUS -->

## 📂 Mapa de categorías


| # | Categoría | Repos | Para qué |
|---|---|---|---|
| 1 | [Automatización, Mensajería & CRM](#1-automatización-mensajería--crm) | 12 | WhatsApp, workflows, CRM, email, notificaciones |
| 2 | [Skills, Prompts & Guías de Agente](#2-skills-prompts--guías-de-agente) | 21 | Habilidades `SKILL.md`, playbooks, calidad de prompts |
| 3 | [Frameworks & Orquestación de Agentes](#3-frameworks--orquestación-de-agentes) | 18 | Multiagente, research autónomo, low-code de IA |
| 4 | [Scraping, Búsqueda & Research Web](#4-scraping-búsqueda--research-web) | 14 | Crawling, extracción, navegación con LLM |
| 5 | [MCP & Conectividad](#5-mcp--conectividad) | 7 | Servidores/clientes MCP, APIs públicas |
| 6 | [Memoria, LLM Ops & Observabilidad](#6-memoria-llm-ops--observabilidad) | 10 | Memoria de agentes, gateways, trazas, logging |
| 7 | [Inteligencia de Código, Datos & Entrenamiento](#7-inteligencia-de-código-datos--entrenamiento) | 13 | Indexar repos, grafos, entrenar modelos desde cero |
| 8 | [Workspaces de IA Local & Notebooks](#8-workspaces-de-ia-local--notebooks) | 5 | Entornos privados todo-en-uno, NotebookLM |
| 9 | [Diseño, UI & Frontend](#9-diseño-ui--frontend) | 15 | Diseño asistido, libs de componentes, animación, 3D |
| 10 | [Analítica & Visualización](#10-analítica--visualización) | 7 | Product analytics, dashboards, gráficos |
| 11 | [Generación de Imagen & Visión](#11-generación-de-imagen--visión) | 15 | Difusión, control, restauración, rostros |
| 12 | [Audio, Voz & Video](#12-audio-voz--video) | 15 | STT, TTS, edición y render de video |
| 13 | [Documentos & Presentaciones](#13-documentos--presentaciones) | 4 | Conversión a Markdown, PPTX, PDF, slides |

> Cada repo vive en **una** categoría; los cruces se resuelven con "Combina con". Excluidos por ser propios: `Binarias_Labs_C21`, `Binarias_Labs_Pruebas`.

---

## 🔗 Recetas de integración (stacks listos)

Combos end-to-end que unen varios repos. Útiles cuando un repo solo no resuelve el flujo completo.

### 🟢 1. Bot de WhatsApp con IA
**Objetivo:** atención/ventas automatizada por WhatsApp con un agente LLM.
**Stack:** [evolution-api](#-evolution-api) (canal WhatsApp) → [n8n](#-n8n) (orquestación) + [n8n-mcp](#-n8n-mcp) y [n8n-skills](#-n8n-skills) (que Claude construya los flujos) → LLM → [chatwoot](#-chatwoot) (handoff a humano) + [novu](#-novu) (notificaciones).
**Cómo encaja:** evolution-api recibe/envía mensajes vía webhook; n8n enruta y llama al LLM; chatwoot centraliza cuando entra un agente humano.

### 🎬 2. Pipeline de Reels / video corto
**Objetivo:** convertir contenido en video corto con voz y subtítulos.
**Stack:** [whisperX](#-whisperx) (subtítulos alineados) + [supertonic](#-supertonic) o [TTS](#-tts) (voz) + [ComfyUI](#-comfyui) o [Fooocus](#-fooocus) (visuales) + [Real-ESRGAN](#-real-esrgan) (upscale) → [moviepy](#-moviepy) o [remotion](#-remotion) (ensamblaje) → [lossless-cut](#-lossless-cut) (corte final).
**Cómo encaja:** [videofy_minimal](#-videofy_minimal) puede orquestar el flujo simple; remotion/moviepy escalan a variantes programáticas.

### 🔎 3. Agente de research profundo
**Objetivo:** investigación citada y estructurada a partir de la web.
**Stack:** [gpt-researcher](#-gpt-researcher) o [deer-flow](#-deer-flow) (orquestador) + [firecrawl](#-firecrawl) / [crawl4ai](#-crawl4ai) (extracción) + [browser-use](#-browser-use) (navegación) + [markitdown](#-markitdown) (ingesta) + [langfuse](#-langfuse) (trazas).

### 🏠 4. Workspace privado local soberano
**Objetivo:** asistente todo-en-uno sin fuga de datos.
**Stack:** [odysseus](#-odysseus) (workspace) + [open-notebook](#-open-notebook) (conocimiento) + [ECC](#-ecc) (control seguro de agentes) + Ollama (modelos) + [mem0](#-mem0) (memoria).

### 🧠 5. Análisis de repos grandes
**Objetivo:** que un asistente entienda una base de código enorme barato.
**Stack:** [codegraph](#-codegraph) (índice local) + [graphify](#-graphify) / [graphrag](#-graphrag) (grafo) + [GitNexus](#-gitnexus) (exploración) + Claude Code.

### 📈 6. Marketing de agencia
**Objetivo:** operar campañas y contenido a escala.
**Stack:** [marketingskills](#-marketingskills) + [agency-agents](#-agency-agents) (playbooks) + [mautic](#-mautic) (automatización) + [listmonk](#-listmonk) (email) + [posthog](#-posthog) / [metabase](#-metabase) (analítica) + [Open-Generative-AI](#-open-generative-ai) (creativos).

### 🌐 7. Web app moderna con IA
**Objetivo:** construir frontend pulido rápido.
**Stack:** [open-design](#-open-design) o [plasmic](#-plasmic) (diseño→código) + [tailwindcss](#-tailwindcss) + [heroui](#-heroui) o [ui](#-ui-shadcn) (componentes) + [GSAP](#-gsap) / [motion](#-motion) / [three.js](#-threejs) (animación/3D) + [swr](#-swr) (datos) + [echarts](#-echarts) / [uPlot](#-uplot) (gráficos).

### 🔌 8. Construir una app/servidor MCP
**Objetivo:** exponer datos o herramientas propias a asistentes.
**Stack:** [mcp-use](#-mcp-use) (framework) + [mcp](#-mcp) (SDK) + [servers](#-servers) (ejemplos de referencia) + [awesome-mcp-servers](#-awesome-mcp-servers) (qué ya existe).

### 📊 9. Documentos → presentaciones
**Objetivo:** pasar texto/informes a slides editables.
**Stack:** [markitdown](#-markitdown) (todo → Markdown limpio) → [ppt-master](#-ppt-master) (PPTX) o [reveal.js](#-revealjs) (slides web).

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

### 🎨 ui-ux-pro-max-skill
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** habilidades que dotan al asistente de inteligencia de diseño UI/UX y estilos avanzados para producir interfaces más profesionales.
**Por qué destaca:** eleva de forma notable el acabado visual de las interfaces generadas por IA, un punto débil habitual del código generado.
**Cómo funciona:** combina skills con una CLI (uipro-cli) que inyecta criterios de layout, jerarquía y estilo (Tailwind/CSS) en el flujo del asistente.
**Instalación:** clona el repo y sigue su README; instala la CLI vía Node (`npx`/instalación local) y copia las skills al directorio de skills.
**Casos:** mejorar layouts y jerarquía visual · acabado profesional con Tailwind/CSS.
**Stack:** Node.js (uipro-cli), Python — **Modelo/API:** todos los LLMs de código.
**Elige si:** generas UI con IA y quieres calidad — **Evita si:** no trabajas frontend.
**Combina con:** [taste-skill](#-taste-skill) · [impeccable](#-impeccable) · [tailwindcss](#-tailwindcss)
**Repo:** [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

### 🍷 taste-skill
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** skills "anti-slop" para producir frontends premium (layout, tipografía, motion) más skills de generación de imagen para crear mood boards de referencia.
**Por qué destaca:** ataca el aspecto "de plantilla" que delata a las UIs generadas por IA, aportando criterio de diseño además de código.
**Cómo funciona:** las skills inyectan guías de gusto visual y, opcionalmente, llaman a generadores de imagen para boards de referencia (web/mobile/brand).
**Instalación:** clona el repo y copia las skills a tu directorio de skills (Codex, Cursor o Claude Code); las de imagen requieren un generador disponible.
**Casos:** subir el gusto de UIs construidas por IA · boards de referencia (web/mobile/brand).
**Stack:** Markdown/skills — **Modelo/API:** Codex, Cursor, Claude Code (+ generadores de imagen).
**Elige si:** quieres frontends con gusto — **Evita si:** te basta UI funcional básica.
**Combina con:** [ui-ux-pro-max-skill](#-ui-ux-pro-max-skill) · [impeccable](#-impeccable)
**Repo:** [GitHub](https://github.com/Leonxlnx/taste-skill)

### ✏️ skills_emil
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering).
**Por qué destaca:** pone el foco en el handoff y la colaboración, no solo en la estética, algo menos cubierto por otras skills de UI.
**Cómo funciona:** se entrega como un `SKILL.md` (skill emil-design-eng) que el asistente carga para guiar decisiones de diseño-implementación.
**Instalación:** copia el `SKILL.md` al directorio de skills de tu asistente (referencia local; ver fuente original del autor).
**Casos:** mejorar el handoff diseño↔ingeniería · resultados UI más consistentes.
**Stack:** Markdown (skills) — **Modelo/API:** no claro (repo local).
**Elige si:** trabajas diseño+dev en equipo — **Evita si:** buscas componentes listos.
**Combina con:** [design.md](#-designmd) · [ui-ux-pro-max-skill](#-ui-ux-pro-max-skill)
**Repo:** [GitHub](https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md)

### 🛡️ SkillSpector
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** herramienta para auditar la seguridad de skills y detectar patrones potencialmente riesgosos antes de instalarlas.
**Por qué destaca:** aporta una capa de seguridad muy necesaria sobre catálogos enormes de skills de terceros, y proviene de NVIDIA.
**Cómo funciona:** analiza los archivos de skill en busca de comandos peligrosos o patrones sospechosos y reporta hallazgos, de forma agnóstica al asistente.
**Instalación:** clona el repo e instala sus dependencias (Python/Node) según el README; ejecútalo sobre el directorio de skills que quieras auditar.
**Casos:** auditar skills de terceros antes de instalarlas · detectar comandos peligrosos.
**Stack:** Python/Node — **Modelo/API:** agnóstico.
**Elige si:** instalas skills externas — **Evita si:** solo usas skills propias confiables.
**Combina con:** [antigravity-awesome-skills](#-antigravity-awesome-skills)
**Repo:** [GitHub](https://github.com/NVIDIA/SkillSpector)

### 🧑 humanizer
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** skill para Claude Code/OpenCode que elimina las señales típicas ("tells") de la escritura generada por IA para que el texto suene más natural.
**Por qué destaca:** es simple y de foco único, lo que la hace muy efectiva y fácil de adoptar para pulir prosa.
**Cómo funciona:** aplica reglas de reescritura sobre el texto del LLM para quitar muletillas y patrones reconocibles de IA.
**Instalación:** clona el repo y copia el `SKILL.md` al directorio de skills de Claude Code u OpenCode.
**Casos:** redactar correos/posts que no suenen a IA · pulir borradores de LLM.
**Stack:** Markdown/skill — **Modelo/API:** Claude Code, OpenCode.
**Elige si:** publicas prosa generada por IA — **Evita si:** escribes a mano.
**Combina con:** [stop-slop](#-stop-slop)
**Repo:** [GitHub](https://github.com/blader/humanizer)

### 🧹 stop-slop
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** skill que enseña al modelo a eliminar patrones y "tells" de la prosa generada por IA, mejorando ritmo y estilo.
**Por qué destaca:** aporta reglas concretas y accionables contra el "slop", útiles con cualquier LLM y no atadas a un asistente.
**Cómo funciona:** define instrucciones de estilo que el asistente aplica al reescribir, evitando frases y cadencias predecibles.
**Instalación:** clona el repo y copia el `SKILL.md` al directorio de skills de tu asistente, o úsalo como instrucción de estilo.
**Casos:** limpiar frases y ritmos predecibles · mejorar estilo del LLM.
**Stack:** Markdown/skill — **Modelo/API:** cualquier LLM.
**Elige si:** quieres prosa más natural — **Evita si:** ya usas [humanizer](#-humanizer) (solapan).
**Combina con:** [humanizer](#-humanizer)
**Repo:** [GitHub](https://github.com/hardikpandya/stop-slop)

---

## 3. Frameworks & Orquestación de Agentes

Plataformas para construir sistemas multiagente, research autónomo y flujos low-code de IA.

### 🔍 Escaneo rápido

| Repo | Qué es | Ejec. | Elige si… |
|---|---|---|---|
| [ag2](#-ag2) | Framework multiagente maduro | ☁️ | Construyes sistemas multiagente en prod |
| [crewAI](#-crewai) | Equipos de agentes con roles | ☁️ | Quieres avanzar rápido con "crews" |
| [langchain](#-langchain) | Framework base de apps LLM | ☁️ | Necesitas el estándar de orquestación |
| [langflow](#-langflow) | Constructor visual de flujos LLM | 🔀 | Prefieres iterar componentes en visual |
| [dify](#-dify) | Plataforma integral de apps IA | 🔀 | Quieres backend+UI listos para apps |
| [Flowise](#-flowise) | Builder visual de pipelines LLM | 🔀 | Prototipas pipelines drag-and-drop |
| [OpenHands](#-openhands) | Agentes que ejecutan en entornos dev | 🔀 | Quieres un agente que programe/ejecute |
| [deer-flow](#-deer-flow) | Super-agente con sub-agentes y sandbox | 🔀 | Buscas orquestación potente extensible |
| [NeMo-Agent-Toolkit](#-nemo-agent-toolkit) | Toolkit de agentes de NVIDIA | 🔀 | Estás en stack NVIDIA/empresa |
| [hermes-agent](#-hermes-agent) | Entorno desktop/CLI de agentes locales | 🏠 | Ejecutas agentes locales con razonamiento |
| [openevolve](#-openevolve) | Agente de código evolutivo | ☁️ | Optimizas algoritmos por evolución |
| [gpt-researcher](#-gpt-researcher) | Agente de research autónomo | 🔀 | Necesitas reportes citados profundos |
| [autoresearch](#-autoresearch) | Research iterativo experimental | 🔀 | Exploras automatización de investigación |
| [deer-flow](#-deer-flow) | (ver arriba) | 🔀 | — |
| [ruflo](#-ruflo) | Swarm multiagente (Rust) para Claude/Codex | 🔀 | Coordinas 100+ agentes con memoria |
| [multica](#-multica) | Plataforma humanos+agentes lado a lado | 🔀 | Mezclas equipo humano y agentes |
| [MiroFish](#-mirofish) | Motor de predicción multiagente | 🔀 | Simulas escenarios/futuros con agentes |
| [llm-council](#-llm-council) | "Consejo" de varios LLMs deliberando | 🔀 | Quieres respuestas por consenso multi-modelo |
| [awesome-LangGraph](#-awesome-langgraph) | Recursos del ecosistema LangGraph | 📂 | Construyes grafos cíclicos de agentes |

### ⚖️ ¿Cuál elegir? — Frameworks de agentes

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **langchain** | Base general de apps LLM | Ecosistema enorme y estándar | Quieres algo ligero/sin abstracción |
| **ag2** | Multiagente colaborativo serio | Patrones de colaboración maduros | Solo necesitas un agente simple |
| **crewAI** | Equipos con roles rápido | DX ágil para "crews" | Necesitas control de bajo nivel |
| **OpenHands** | Agente que codifica y ejecuta | Acciones reales en entorno dev | Solo quieres chat/RAG |
| **deer-flow** | Orquestación con sub-agentes/sandbox | Super-agente extensible por skills | Buscas algo minimalista |

### ⚖️ ¿Cuál elegir? — Low-code / visual de IA

| Repo | Cuándo usarlo | Ventaja clave |
|---|---|---|
| **dify** | App IA completa (backend+UI) | Plataforma integral lista |
| **langflow** | Iterar componentes de agente | Visual sobre LangChain |
| **Flowise** | Prototipo rápido de pipeline | Drag-and-drop sencillo |

### 🤝 ag2
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework maduro para sistemas multiagente con patrones de colaboración (heredero de AutoGen). Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo.
**Por qué destaca:** uno de los frameworks multiagente de referencia, con amplia adopción y comunidad activa heredada de AutoGen.
**Cómo funciona:** define agentes conversacionales (asistente, ejecutor de código, usuario) que intercambian mensajes según patrones predefinidos; corre sobre Python y se conecta a APIs de LLM.
**Instalación:** `pip install ag2` (o `pyautogen`).
**Casos:** equipos de agentes que se reparten tareas · flujos de decisión estructurados.
**Stack:** Python — **Modelo/API:** OpenAI, Anthropic, locales.
**Elige si:** construyes multiagente serio — **Evita si:** te basta un agente único.
**Combina con:** [langchain](#-langchain) · [langfuse](#-langfuse)
**Repo:** [GitHub](https://github.com/ag2ai/ag2)

### 👥 crewAI
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** framework para orquestar "crews" de agentes con roles y tareas. Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.
**Por qué destaca:** muy popular por su curva de aprendizaje suave; es de las formas más rápidas de montar un equipo de agentes funcional.
**Cómo funciona:** declaras agentes (rol, meta, herramientas) y tareas, y CrewAI orquesta su ejecución; está escrito en Python y es independiente de LangChain.
**Instalación:** `pip install crewai` (o `crewai[tools]`).
**Casos:** avanzar rápido en flujos de agentes · prototipos colaborativos.
**Stack:** Python — **Modelo/API:** múltiples.
**Elige si:** quieres velocidad — **Evita si:** necesitas control de bajo nivel.
**Combina con:** [langchain](#-langchain) · [mem0](#-mem0)
**Repo:** [GitHub](https://github.com/crewAIInc/crewAI)

### 🦜 langchain
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.
**Por qué destaca:** estándar de facto del ecosistema LLM, con la comunidad e integraciones más grandes del sector.
**Cómo funciona:** encadena componentes (prompts, modelos, retrievers, tools) en pipelines o agentes; disponible en Python y JS/TS.
**Instalación:** `pip install langchain` o `npm install langchain`.
**Casos:** orquestar LLM + herramientas + memoria · base de casi cualquier app de IA.
**Stack:** Python/JS — **Modelo/API:** prácticamente todos.
**Elige si:** quieres la base estándar — **Evita si:** prefieres mínima abstracción.
**Combina con:** [langflow](#-langflow) · [langfuse](#-langfuse) · [litellm](#-litellm)
**Repo:** [GitHub](https://github.com/langchain-ai/langchain)

### 🔗 langflow
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** constructor visual de flujos LLM/agentes construido sobre LangChain. Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código.
**Por qué destaca:** une la potencia del ecosistema LangChain con una interfaz visual, muy valorado para prototipar sin escribir todo el código.
**Cómo funciona:** cada nodo del lienzo envuelve un componente LangChain; el flujo se ejecuta como un grafo y se expone vía API. Corre sobre Python con frontend web.
**Instalación:** `pip install langflow` o vía Docker.
**Casos:** iterar componentes de agente sin código · prototipar pipelines.
**Stack:** Python, web — **Modelo/API:** múltiples.
**Elige si:** prefieres construir en visual — **Evita si:** quieres todo en código.
**Combina con:** [langchain](#-langchain) · [dify](#-dify)
**Repo:** [GitHub](https://github.com/langflow-ai/langflow)

### 🧱 dify
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma integral para construir apps de IA con backend y UI listos. Combina orquestación de prompts, RAG, agentes y observabilidad en un mismo producto autoalojable.
**Por qué destaca:** todo-en-uno muy popular para llevar apps de IA a producción sin ensamblar piezas sueltas.
**Cómo funciona:** define apps (chatbot, agente, workflow) desde un panel web; el backend en Python orquesta modelos y herramientas, y se despliega con Docker.
**Instalación:** `docker compose up` desde el repo (o cloud gestionado).
**Casos:** desplegar un chatbot/asistente con RAG · apps IA para clientes.
**Stack:** Python/TS, Docker — **Modelo/API:** múltiples + locales.
**Elige si:** quieres una app IA completa — **Evita si:** solo necesitas una librería.
**Combina con:** [langflow](#-langflow) · [Flowise](#-flowise)
**Repo:** [GitHub](https://github.com/langgenius/dify)

### 🌊 Flowise
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** builder visual drag-and-drop para pipelines LLM. Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible.
**Por qué destaca:** muy adoptado para prototipar flujos LLM en minutos sin escribir código.
**Cómo funciona:** cada nodo encapsula un componente (LLM, retriever, tool); el grafo se ejecuta en un backend Node.js y se sirve por API. Basado en LangChain.js.
**Instalación:** `npm install -g flowise && npx flowise start` o vía Docker.
**Casos:** prototipar un flujo LLM rápido · demos sin código.
**Stack:** Node.js, web — **Modelo/API:** múltiples.
**Elige si:** quieres un prototipo ya — **Evita si:** necesitas plataforma completa ([dify](#-dify)).
**Combina con:** [dify](#-dify) · [langflow](#-langflow)
**Repo:** [GitHub](https://github.com/FlowiseAI/Flowise)

### 🙌 OpenHands
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.
**Por qué destaca:** uno de los proyectos open-source de agentes de programación más populares, con foco en acciones reales en lugar de solo respuestas.
**Cómo funciona:** un bucle agente-acción-observación ejecuta tareas dentro de un contenedor aislado; backend en Python con UI web, sobre Docker.
**Instalación:** `docker run` de la imagen oficial (o `pip install openhands-ai`).
**Casos:** agente que edita código, corre comandos y navega · automatizar tareas dev.
**Stack:** Python/TS, Docker — **Modelo/API:** múltiples.
**Elige si:** quieres un agente que "haga", no solo hable — **Evita si:** solo necesitas chat/RAG.
**Combina con:** [ECC](#-ecc) · [sandbox](#-sandbox)
**Repo:** [GitHub](https://github.com/All-Hands-AI/OpenHands)

### 🦌 deer-flow
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. Coordina tareas complejas delegando en agentes especializados.
**Por qué destaca:** orquestación potente y extensible; alcanzó gran visibilidad (#1 en GitHub Trending en su lanzamiento v2) y cuenta con el respaldo de ByteDance.
**Cómo funciona:** un orquestador reparte sub-tareas a agentes con herramientas y sandbox, integrando memoria entre pasos; implementado en Python/TS.
**Instalación:** `git clone` del repo y arranque con sus scripts (o Docker).
**Casos:** research profundo · tareas complejas multi-paso con herramientas.
**Stack:** Python/TS — **Modelo/API:** múltiples.
**Elige si:** quieres un orquestador completo — **Evita si:** buscas algo minimalista.
**Combina con:** [gpt-researcher](#-gpt-researcher) · [firecrawl](#-firecrawl)
**Repo:** [GitHub](https://github.com/bytedance/deer-flow)

### 🟩 NeMo-Agent-Toolkit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🔴 pesado
**Qué es:** toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.
**Por qué destaca:** respaldo y rendimiento de NVIDIA, orientado a despliegues empresariales sobre su stack de modelos e infra.
**Cómo funciona:** compone agentes y herramientas mediante perfiles configurables y los conecta a modelos NVIDIA NIM u otros compatibles; librería Python (Apache-2.0).
**Instalación:** `pip install nvidia-nat` (o `git clone` del repo).
**Casos:** agentes empresariales en stack NVIDIA · pipelines con modelos propios.
**Stack:** Python (Apache-2.0) — **Modelo/API:** NVIDIA y compatibles.
**Elige si:** trabajas con infra NVIDIA — **Evita si:** quieres algo ligero.
**Combina con:** [langchain](#-langchain)
**Repo:** [GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

### ☤ hermes-agent
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.
**Por qué destaca:** aprovecha el razonamiento estructurado de los modelos Hermes y prioriza la ejecución local frente a depender de la nube.
**Cómo funciona:** una app de escritorio (Tauri) coordina agentes con backend Python que invocan modelos Hermes locales o APIs comerciales como fallback.
**Instalación:** `git clone` y build con Tauri/Cargo (más dependencias Python).
**Casos:** delegar tareas en sandbox local · panel de control de escritorio (Tauri).
**Stack:** Rust (Tauri), TypeScript, Python — **Modelo/API:** Hermes-3-Llama-3 + APIs comerciales.
**Elige si:** quieres agentes locales con UI — **Evita si:** prefieres orquestación en nube.
**Combina con:** [ECC](#-ecc) · [odysseus](#-odysseus)
**Repo:** [GitHub](https://github.com/NousResearch/hermes-agent)

### 🧬 openevolve
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** agente de codificación evolutivo que optimiza algoritmos por simulación genética. Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.
**Por qué destaca:** supera la generación en un solo paso al explorar el espacio de soluciones, encontrando algoritmos inéditos (inspirado en AlphaEvolve).
**Cómo funciona:** un bucle evolutivo usa el LLM como operador de mutación y una función de evaluación como fitness; implementado en Python con numpy/PyTorch y componentes en Rust.
**Instalación:** `pip install openevolve` (o `git clone` del repo).
**Casos:** empaquetado geométrico · optimización de carteras · mejorar scripts en tiempo real.
**Stack:** Python, PyTorch/numpy, Rust — **Modelo/API:** modelos de frontera creativos (Claude/GPT-4o).
**Elige si:** optimizas problemas algorítmicos — **Evita si:** haces tareas de texto comunes.
**Combina con:** [llm-council](#-llm-council)
**Repo:** [GitHub](https://github.com/algorithmicsuperintelligence/openevolve)

### 🔍 gpt-researcher
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** agente autónomo que investiga en línea y consolida reportes citados y estructurados. Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.
**Por qué destaca:** muy popular para research profundo; automatiza horas de búsqueda recopilando y citando lo más relevante.
**Cómo funciona:** un agente planificador genera consultas, agentes de búsqueda recopilan fuentes web y un redactor sintetiza el reporte; backend Python (FastAPI) con frontend Next.js.
**Instalación:** `pip install gpt-researcher` o vía Docker.
**Casos:** análisis de un tema con fuentes · reportes en PDF/Markdown.
**Stack:** Python, Next.js, FastAPI — **Modelo/API:** GPT-4o, Claude, Gemini + locales.
**Elige si:** necesitas research profundo citado — **Evita si:** solo quieres una respuesta corta.
**Combina con:** [firecrawl](#-firecrawl) · [browser-use](#-browser-use) · receta [Research profundo](#-3-agente-de-research-profundo)
**Repo:** [GitHub](https://github.com/assafelovic/gpt-researcher)

### 🔬 autoresearch
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. Proyecto pequeño y exploratorio más que una herramienta pulida.
**Por qué destaca:** propuesta sencilla para experimentar con investigación autónoma en varias pasadas; valioso como punto de partida más que como producto cerrado.
**Cómo funciona:** repite ciclos de búsqueda y refinamiento sobre un tema, refinando consultas con cada iteración; implementado en Python.
**Instalación:** `git clone` del repo y ejecución de sus scripts en Python (consulta el README).
**Casos:** loops de búsqueda y refinamiento · exploración de un tema en varias pasadas.
**Stack:** Python — **Modelo/API:** múltiples.
**Elige si:** experimentas con research iterativo — **Evita si:** quieres salida pulida ([gpt-researcher](#-gpt-researcher)).
**Combina con:** [gpt-researcher](#-gpt-researcher) · [crawl4ai](#-crawl4ai)
**Repo:** [GitHub](https://github.com/karpathy/autoresearch)

### 🐝 ruflo
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). Orquesta swarms de agentes especializados a escala.
**Por qué destaca:** motor en Rust con embeddings, memoria persistente y plugins, orientado a coordinación masiva de agentes con seguridad de nivel enterprise; proyecto de nicho pero ambicioso.
**Cómo funciona:** un coordinador en Rust reparte trabajo entre agentes, comparte memoria federada y comunica equipos; se apoya en CLIs de agentes como Claude Code y Codex.
**Instalación:** `cargo install` o build desde fuente con `git clone` (consulta el README).
**Casos:** swarms de agentes especializados · memoria autoaprendida y comms entre equipos.
**Stack:** Rust — **Modelo/API:** Claude Code, Codex.
**Elige si:** orquestas muchos agentes a escala — **Evita si:** solo necesitas 1-2 agentes.
**Combina con:** [mem0](#-mem0) · [ECC](#-ecc)
**Repo:** [GitHub](https://github.com/ruvnet/ruflo)

### 🧑‍🤝‍🧑 multica
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas"). Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.
**Por qué destaca:** propone equipos mixtos humano+agente en un flujo común, en lugar de automatización totalmente headless.
**Cómo funciona:** según lo descrito, ofrece un entorno web donde humanos y agentes comparten tareas y contexto; pila web/TypeScript.
**Instalación:** consulta el README del repo (`git clone` / instalación web).
**Casos:** equipos mixtos humano+agente · operación con agentes como colaboradores.
**Stack:** web/TS — **Modelo/API:** múltiples.
**Elige si:** mezclas trabajo humano y agentes — **Evita si:** quieres automatización 100% headless.
**Combina con:** [ruflo](#-ruflo) · [chatwoot](#-chatwoot)
**Repo:** [GitHub](https://github.com/multica-ai/multica)

### 🐟 MiroFish
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.
**Por qué destaca:** simula futuros con agentes que tienen personalidad, memoria y lógica que evolucionan, ofreciendo una "vista de dios" del escenario.
**Cómo funciona:** según lo descrito, instancia muchos agentes con perfiles y memoria que interactúan en un mundo simulado para estimar resultados; pila Python/web.
**Instalación:** consulta el README del repo (`git clone` y ejecución en Python).
**Casos:** simular impacto de una noticia/política · predecir tendencias en un "sandbox" social.
**Stack:** Python/web — **Modelo/API:** múltiples.
**Elige si:** simulas futuros/escenarios — **Evita si:** necesitas tareas deterministas.
**Combina con:** [openevolve](#-openevolve)
**Repo:** [GitHub](https://github.com/666ghj/MiroFish)

### 🏛️ llm-council
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.
**Por qué destaca:** combina perspectivas de varios modelos para reducir el sesgo de uno solo; propuesta sencilla y didáctica popularizada por Karpathy.
**Cómo funciona:** envía la consulta a varios LLMs, los hace revisar las respuestas de los demás y agrega un resultado de consenso; app ligera en Python/web.
**Instalación:** `git clone` del repo y ejecución según su README.
**Casos:** respuestas por consenso multi-modelo · reducir sesgo de un solo modelo.
**Stack:** Python/web — **Modelo/API:** múltiples LLMs.
**Elige si:** quieres consenso entre modelos — **Evita si:** te basta un único LLM.
**Combina con:** [litellm](#-litellm)
**Repo:** [GitHub](https://github.com/karpathy/llm-council)

### 🕸️ awesome-LangGraph
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. Es una lista curada, no una herramienta ejecutable.
**Por qué destaca:** índice organizado por áreas (RAG, web, finanzas, salud, seguridad) que facilita encontrar patrones y proyectos de referencia para LangGraph.
**Cómo funciona:** una lista "awesome" en Markdown con enlaces a proyectos, plantillas y tutoriales del ecosistema LangGraph.
**Instalación:** no requiere instalación; se consulta el repo (o `git clone` para uso offline).
**Casos:** estructurar grafos cíclicos de agentes · políticas de enrutamiento y estado.
**Stack:** Markdown / Python-JS — **Modelo/API:** N/A (recurso).
**Elige si:** construyes con LangGraph — **Evita si:** no usas ese ecosistema.
**Combina con:** [langchain](#-langchain)
**Repo:** [GitHub](https://github.com/von-development/awesome-LangGraph)

---

## 4. Scraping, Búsqueda & Research Web

Crawling, extracción estructurada y navegación web con LLMs.

### 🔍 Escaneo rápido

| Repo | Qué es | Lenguaje | Elige si… |
|---|---|---|---|
| [firecrawl](#-firecrawl) | API search+scrape para agentes | TS/API | Quieres web → Markdown/JSON listo para LLM |
| [crawl4ai](#-crawl4ai) | Crawling a gran escala para IA | Python | Recolectas grandes volúmenes barato |
| [scrapy](#-scrapy) | Framework clásico de scraping | Python | Necesitas un crawler maduro y robusto |
| [crawlee](#-crawlee) | Framework de crawling moderno | Node.js | Scrapeas con Node y antibloqueo |
| [crawlee-python](#-crawlee-python) | Crawlee para Python | Python | Quieres Crawlee pero en Python |
| [Scrapling](#-scrapling) | Scraping adaptativo anti-bloqueo | Python | Las páginas cambian o te bloquean |
| [scrapely](#-scrapely) | Extracción por ejemplos (sin reglas) | Python | Extraes por plantilla aprendida |
| [llm-scraper](#-llm-scraper) | Web → datos estructurados con LLM | TS | Defines un esquema y el LLM lo llena |
| [Scrapegraph-ai](#-scrapegraph-ai) | Scraping por grafos + LLM | Python | Combinas extracción y estructura semántica |
| [playwright](#-playwright) | Automatización/testing de navegador | TS/Python | Necesitas control preciso del browser |
| [playwright-cli](#-playwright-cli) | Playwright como CLI + skills | TS | Tu agente automatiza web vía CLI |
| [browser-use](#-browser-use) | Navegación web por visión para LLM | Python | El agente "ve" la pantalla y actúa |
| [instaloader](#-instaloader) | Descarga de datos de Instagram | Python | Extraes contenido/metadata de IG |
| [snscrape](#-snscrape) | Scraper de redes sociales | Python | Recolectas posts sin API oficial |

### ⚖️ ¿Cuál elegir? — Crawling/scraping

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **firecrawl** | Alimentar agentes con web limpia | Salida lista para LLM (MD/JSON) | Solo necesitas un crawler crudo |
| **crawl4ai** | Volumen alto orientado a IA | Costo/fiabilidad a escala | Quieres scraping puntual simple |
| **scrapy** | Crawler robusto y maduro | Ecosistema y control total | No quieres curva de framework |
| **crawlee** / **crawlee-python** | Antibloqueo moderno | Rotación/proxies integrados | Te sirve scrapy clásico |
| **Scrapling** | Sitios que cambian/bloquean | Selectores adaptativos | El sitio es estable y simple |

### ⚖️ ¿Cuál elegir? — Web estructurada con LLM / navegación

| Repo | Cuándo usarlo | Ventaja clave |
|---|---|---|
| **llm-scraper** | Quieres un esquema tipado | LLM rellena tu schema |
| **Scrapegraph-ai** | Extracción semántica por grafos | Combina scraping + razonamiento |
| **browser-use** | El agente debe navegar como humano | Control visual, sin selectores fijos |
| **playwright** / **playwright-cli** | Control determinista del browser | Reproducible y multiplataforma |

### 🔥 firecrawl
**Etiquetas:** Ejecución ☁️ API/cloud · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript.
**Por qué destaca:** se ha vuelto la opción de referencia para alimentar pipelines RAG y agentes con web limpia; muy adoptada y con integración MCP de primera clase.
**Cómo funciona:** renderiza la página (incluido JS), normaliza el HTML y lo convierte a Markdown/JSON; expone endpoints scrape/crawl/search/map vía API REST y SDKs.
**Instalación:** API hosted con clave (`npm i @mendable/firecrawl-js` o `pip install firecrawl-py`); también self-host con Docker.
**Casos:** convertir páginas complejas en contexto limpio · search + crawl para research.
**Stack:** API/SDK, hosted o self-host — **Modelo/API:** MCP y agentes; no atado a un proveedor.
**Elige si:** alimentas agentes con web — **Evita si:** solo quieres HTML crudo.
**Combina con:** [gpt-researcher](#-gpt-researcher) · [crawl4ai](#-crawl4ai) · receta [Research profundo](#-3-agente-de-research-profundo)
**Repo:** [GitHub](https://github.com/firecrawl/firecrawl)

### 🕷️ crawl4ai
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA.
**Por qué destaca:** una de las alternativas open-source más populares a las APIs de pago; gratuita, self-host y muy activa en la comunidad de scraping para LLMs.
**Cómo funciona:** usa Playwright para controlar un navegador headless, ejecuta el render asíncrono y limpia el resultado a Markdown/JSON con estrategias de extracción configurables.
**Instalación:** `pip install crawl4ai` seguido de `crawl4ai-setup` para instalar los navegadores de Playwright.
**Casos:** pipeline que recolecta muchas páginas para análisis · salida lista para IA.
**Stack:** Python — **Modelo/API:** agnóstico; se integra con análisis posterior.
**Elige si:** necesitas volumen barato — **Evita si:** quieres una API hosted simple ([firecrawl](#-firecrawl)).
**Combina con:** [firecrawl](#-firecrawl) · [gpt-researcher](#-gpt-researcher)
**Repo:** [GitHub](https://github.com/unclecode/crawl4ai)

### 🐍 scrapy
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala.
**Por qué destaca:** estándar de facto del scraping en Python desde hace más de una década, con enorme ecosistema de extensiones y base instalada masiva.
**Cómo funciona:** define spiders que emiten requests asíncronas sobre el motor Twisted, procesa respuestas con selectores y pasa los items por pipelines de limpieza/almacenamiento.
**Instalación:** `pip install scrapy`; el comando `scrapy startproject` genera el andamiaje del proyecto.
**Casos:** spiders robustos · pipelines de extracción a gran escala.
**Stack:** Python — **Modelo/API:** N/A.
**Elige si:** quieres un crawler sólido y configurable — **Evita si:** buscas salida lista para LLM.
**Combina con:** [scrapely](#-scrapely) · [crawlee-python](#-crawlee-python)
**Repo:** [GitHub](https://github.com/scrapy/scrapy)

### 🦗 crawlee
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework moderno de crawling para Node.js con antibloqueo integrado, unifico scraping de HTTP y de navegador bajo una misma API con colas y reintentos.
**Por qué destaca:** mantenido por Apify, es la referencia de crawling en el ecosistema JavaScript y trae evasión de bloqueos lista de fábrica.
**Cómo funciona:** gestiona una cola de URLs y un pool autoescalable de crawlers (Cheerio para HTTP o Playwright/Puppeteer para navegador), con rotación de proxies y huellas para evitar baneos.
**Instalación:** `npm i crawlee` o, para empezar, `npx crawlee create`.
**Casos:** scraping a escala con rotación de proxies · colas y reintentos.
**Stack:** Node.js/TypeScript — **Modelo/API:** N/A.
**Elige si:** scrapeas con Node — **Evita si:** trabajas en Python ([crawlee-python](#-crawlee-python)).
**Combina con:** [playwright](#-playwright)
**Repo:** [GitHub](https://github.com/apify/crawlee)

### 🦗 crawlee-python
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python.
**Por qué destaca:** acerca las ventajas del Crawlee de Node a quienes ya viven en Python, con respaldo oficial de Apify y adopción en crecimiento.
**Cómo funciona:** ofrece crawlers basados en BeautifulSoup/HTTPX o en Playwright, con una cola de requests unificada, autoescalado y gestión de sesiones y proxies.
**Instalación:** `pip install crawlee` (extras como `crawlee[playwright]` para el modo navegador).
**Casos:** crawling moderno con antibloqueo en Python · integrar con stack de datos Python.
**Stack:** Python — **Modelo/API:** N/A.
**Elige si:** quieres Crawlee en Python — **Evita si:** ya usas scrapy y te basta.
**Combina con:** [scrapy](#-scrapy) · [playwright](#-playwright)
**Repo:** [GitHub](https://github.com/apify/crawlee-python)

### 🩹 Scrapling
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.
**Por qué destaca:** proyecto en alza por su enfoque "auto-reparable" de selectores, que evita reescribir scrapers cada vez que el sitio se actualiza.
**Cómo funciona:** rastrea atributos y posiciones de los elementos para reencontrarlos tras cambios en el DOM, con fetchers sigilosos que imitan navegadores reales para sortear bloqueos.
**Instalación:** `pip install scrapling` (con `scrapling install` para los navegadores del modo sigiloso).
**Casos:** páginas que cambian de estructura · evadir bloqueos sin reescribir selectores.
**Stack:** Python — **Modelo/API:** N/A.
**Elige si:** los sitios cambian o te bloquean — **Evita si:** el target es estable y simple.
**Combina con:** [scrapy](#-scrapy)
**Repo:** [GitHub](https://github.com/D4Vinci/Scrapling)

### 📐 scrapely
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales.
**Por qué destaca:** pieza histórica del ecosistema Scrapy; nicho y poco activa hoy, pero útil cuando se quiere extraer "por demostración" en lugar de programar selectores.
**Cómo funciona:** se le da una URL de ejemplo con los datos marcados, induce una plantilla mediante alineación de HTML y la aplica a nuevas páginas con la misma estructura.
**Instalación:** `pip install scrapely`.
**Casos:** extraer campos repetidos sin escribir reglas · scraping por plantilla.
**Stack:** Python — **Modelo/API:** N/A.
**Elige si:** prefieres enseñar por ejemplos — **Evita si:** necesitas un crawler completo.
**Combina con:** [scrapy](#-scrapy)
**Repo:** [GitHub](https://github.com/scrapy/scrapely)

### 🧾 llm-scraper
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.
**Por qué destaca:** popular por su simplicidad: salida tipada y validada sin escribir parsers, integrándose directamente con Playwright y los SDKs de LLM.
**Cómo funciona:** carga la página con Playwright, la pasa a texto/markdown y pide al LLM que devuelva un objeto conforme al esquema Zod, garantizando tipos correctos.
**Instalación:** `npm i llm-scraper playwright` y la SDK del proveedor de LLM elegido.
**Casos:** extraer datos tipados de sitios · automatizar datasets estructurados.
**Stack:** TypeScript — **Modelo/API:** LLMs vía SDK.
**Elige si:** quieres salida tipada — **Evita si:** prefieres extracción semántica por grafos ([Scrapegraph-ai](#-scrapegraph-ai)).
**Combina con:** [playwright](#-playwright) · [firecrawl](#-firecrawl)
**Repo:** [GitHub](https://github.com/mishushakov/llm-scraper)

### 🕸️ Scrapegraph-ai
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping.
**Por qué destaca:** muy popular por permitir scraping "por prompt", combinando extracción con razonamiento del modelo y soporte para múltiples proveedores.
**Cómo funciona:** construye un grafo dirigido de nodos (fetch, parse, generación con LLM) que recorre la página y produce el resultado estructurado pedido.
**Instalación:** `pip install scrapegraphai` más `playwright install` para el render dinámico.
**Casos:** extracción semántica de sitios · datasets útiles para IA.
**Stack:** Python — **Modelo/API:** múltiples LLMs.
**Elige si:** quieres estructura semántica — **Evita si:** te basta un esquema simple ([llm-scraper](#-llm-scraper)).
**Combina con:** [crawl4ai](#-crawl4ai) · [graphrag](#-graphrag)
**Repo:** [GitHub](https://github.com/ScrapeGraphAI/Scrapegraph-ai)

### 🎭 playwright
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.
**Por qué destaca:** se ha convertido en el estándar moderno de automatización de browser, desplazando a Selenium/Puppeteer por su fiabilidad y su auto-espera de elementos.
**Cómo funciona:** lanza navegadores reales en modo headless o con UI y los controla por protocolo, con waits automáticos, interceptación de red y captura de DOM/screenshots.
**Instalación:** `npm i playwright` o `pip install playwright`, seguido de `playwright install` para los navegadores.
**Casos:** testing E2E · scraping dinámico · scripting reproducible.
**Stack:** Node.js o Python — **Modelo/API:** se integra con MCP y agentes.
**Elige si:** necesitas control preciso del browser — **Evita si:** quieres que el agente navegue por visión ([browser-use](#-browser-use)).
**Combina con:** [browser-use](#-browser-use) · [crawlee](#-crawlee)
**Repo:** [GitHub](https://github.com/microsoft/playwright)

### 🎭 playwright-cli
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto.
**Por qué destaca:** alternativa token-eficiente a Playwright MCP; útil para agentes de código (Claude Code, etc.) que necesitan tocar la web sin inflar el prompt.
**Cómo funciona:** envuelve comandos de Playwright en un CLI que el agente invoca paso a paso, evitando cargar árboles de accesibilidad o esquemas enormes en cada turno.
**Instalación:** parte del repositorio de Playwright; se usa vía CLI con `npx`/`npm` dentro del agente de código.
**Casos:** que un agente automatice el browser de forma token-eficiente · alternativa a Playwright MCP.
**Stack:** TypeScript/CLI — **Modelo/API:** agentes de código (Claude Code, etc.).
**Elige si:** tu agente vive en CLI — **Evita si:** necesitas estado persistente (usa Playwright MCP).
**Combina con:** [playwright](#-playwright)
**Repo:** [GitHub](https://github.com/microsoft/playwright)

### 🌐 browser-use
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** biblioteca que da a los LLMs la capacidad de usar navegadores reales con interfaz para modelos de visión, dejando que el agente perciba la pantalla y actúe sin selectores fijos.
**Por qué destaca:** uno de los proyectos de agentes-web más virales y populares, por permitir automatización web robusta guiada por modelos multimodales.
**Cómo funciona:** controla el navegador con Playwright, extrae el estado de la página (DOM + capturas) y deja que un LLM con visión decida la siguiente acción de click/escritura/navegación.
**Instalación:** `pip install browser-use` y `playwright install`; requiere clave de un LLM con visión.
**Casos:** agente que entra a un e-commerce, filtra y compra · recuperación ante pop-ups/errores.
**Stack:** Python 3.11+, Rust (core), Playwright — **Modelo/API:** multimodales con visión (GPT-4o, Claude, Gemini).
**Elige si:** quieres navegación como humano — **Evita si:** necesitas scripts deterministas ([playwright](#-playwright)).
**Combina con:** [playwright](#-playwright) · [gpt-researcher](#-gpt-researcher)
**Repo:** [GitHub](https://github.com/browser-use/browser-use)

### 📸 instaloader
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram.
**Por qué destaca:** utilidad veterana y muy usada para archivar Instagram; simple, enfocada y con CLI lista para usar.
**Cómo funciona:** consulta los endpoints públicos de Instagram y guarda los medios con su metadata en JSON, soportando sesiones logueadas y descargas incrementales.
**Instalación:** `pip install instaloader`; se usa como CLI (`instaloader perfil`) o importando el módulo.
**Casos:** archivar contenido de perfiles · datasets de medios sociales.
**Stack:** Python — **Modelo/API:** N/A.
**Elige si:** necesitas datos de Instagram — **Evita si:** quieres varias redes ([snscrape](#-snscrape)).
**Combina con:** [snscrape](#-snscrape)
**Repo:** [GitHub](https://github.com/instaloader/instaloader)

### 🐦 snscrape
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** scraper de redes sociales (Twitter/X, Reddit, Telegram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves.
**Por qué destaca:** referencia clásica para datasets sociales históricos sin pagar API, aunque su fiabilidad depende de los cambios y restricciones de cada plataforma.
**Cómo funciona:** raspa los endpoints y páginas públicas de cada red, devolviendo los resultados como objetos o JSON desde CLI o como librería de Python.
**Instalación:** `pip install snscrape` (o desde el repo para la versión de desarrollo).
**Casos:** recolectar posts/tweets para análisis · datasets sociales históricos.
**Stack:** Python — **Modelo/API:** N/A.
**Elige si:** recolectas varias redes — **Evita si:** solo necesitas Instagram ([instaloader](#-instaloader)).
**Combina con:** [instaloader](#-instaloader)
**Repo:** [GitHub](https://github.com/JustAnotherArchivist/snscrape)

---

## 5. MCP & Conectividad

Servidores y clientes Model Context Protocol, y catálogos de APIs para conectar herramientas.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… |
|---|---|---|---|
| [mcp](#-mcp) | Protocolo/SDK base de MCP | 📚 | Trabajas con el estándar MCP directamente |
| [mcp-use](#-mcp-use) | Framework para MCP Apps/Servers | 📚 | Construyes tu propio servidor/app MCP |
| [servers](#-servers) | Servidores MCP de referencia | 📂 | Quieres ejemplos oficiales para aprender |
| [awesome-mcp-servers](#-awesome-mcp-servers) | Directorio de servidores MCP | 📂 | Buscas un servidor ya hecho |
| [mcp-neo4j](#-mcp-neo4j) | Servidores MCP para Neo4j | 🧩 | Conectas grafos Neo4j a un asistente |
| [n8n-mcp](#-n8n-mcp) | MCP que expone los nodos de n8n | 🧩 | Quieres que la IA configure flujos n8n |
| [public-apis](#-public-apis) | Directorio de APIs públicas | 📂 | Buscas fuentes de datos externas |

### ⚖️ ¿Cuál elegir? — Crear vs. descubrir MCP

| Repo | Para qué |
|---|---|
| **mcp** | El SDK/spec base si programas a bajo nivel |
| **mcp-use** | Framework para pasar de prueba a app MCP desplegable |
| **servers** | Implementaciones de referencia mantenidas por el steering group |
| **awesome-mcp-servers** | Buscar antes de construir: ¿ya existe el servidor que necesito? |

### 🧩 mcp
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto.
**Por qué destaca:** es el protocolo de referencia del ecosistema, adoptado por Claude, Cursor y muchos otros clientes, lo que lo convierte en la base sobre la que se construye todo lo demás.
**Cómo funciona:** define el protocolo MCP (mensajes JSON-RPC entre cliente y servidor) y ofrece SDKs en TS/Python para implementar servidores y clientes conformes.
**Instalación:** `npm install @modelcontextprotocol/sdk` o `pip install mcp` según el lenguaje.
**Casos:** base de interoperabilidad · construir servidores/clientes conforme al estándar.
**Stack:** TS/Python — **Modelo/API:** clientes MCP.
**Elige si:** programas MCP a bajo nivel — **Evita si:** prefieres un framework de alto nivel ([mcp-use](#-mcp-use)).
**Combina con:** [mcp-use](#-mcp-use) · [servers](#-servers)
**Repo:** [GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol)

### 🛠️ mcp-use
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable.
**Por qué destaca:** abstrae el protocolo en una capa de alto nivel con SDK, inspector y documentación, lo que acorta mucho el camino de la idea a producción frente a usar el SDK base.
**Cómo funciona:** envuelve el protocolo MCP exponiendo APIs de alto nivel para registrar herramientas/recursos y conectar con clientes como Claude o ChatGPT.
**Instalación:** `npm install mcp-use` o `pip install mcp-use` según el stack.
**Casos:** exponer datos/herramientas internas vía MCP · pasar de local a app desplegable.
**Stack:** TypeScript o Python — **Modelo/API:** ChatGPT, Claude y agentes MCP.
**Elige si:** construyes un servidor MCP propio — **Evita si:** solo buscas usar uno ya hecho.
**Combina con:** [mcp](#-mcp) · [awesome-mcp-servers](#-awesome-mcp-servers) · receta [App MCP](#-8-construir-una-appservidor-mcp)
**Repo:** [GitHub](https://github.com/mcp-use/mcp-use)

### 📚 servers
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 directorio/recurso · Setup 🟡 medio
**Qué es:** colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad.
**Por qué destaca:** es la fuente canónica y didáctica para entender cómo se construye un servidor MCP correcto, respaldada por los mantenedores del propio protocolo.
**Cómo funciona:** cada subdirectorio es un servidor MCP de ejemplo (filesystem, fetch, etc.) que se ejecuta y se conecta a un cliente compatible mediante el protocolo MCP.
**Instalación:** ejecutar un servidor del repo con `npx` (p. ej. `npx -y @modelcontextprotocol/server-filesystem`) y añadirlo a la config del cliente MCP.
**Casos:** aprender a construir un servidor MCP · ejemplos educativos de features.
**Stack:** TS/Python — **Modelo/API:** clientes MCP.
**Elige si:** quieres ejemplos canónicos — **Evita si:** buscas soluciones listas para prod (son demos).
**Combina con:** [mcp-use](#-mcp-use) · [awesome-mcp-servers](#-awesome-mcp-servers)
**Repo:** [GitHub](https://github.com/modelcontextprotocol/servers)

### 🗂️ awesome-mcp-servers
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar.
**Por qué destaca:** es uno de los listados de referencia más consultados del ecosistema MCP y ayuda a no reinventar servidores que ya existen.
**Cómo funciona:** lista en Markdown con enlaces a cada servidor; eliges uno, sigues su README y lo añades a la config de tu cliente MCP.
**Instalación:** sin instalación propia; se consulta el README y luego se instala el servidor elegido (normalmente vía `npx` o `pip`).
**Casos:** descubrir un servidor ya hecho antes de implementar uno · referencia rápida de integración.
**Stack:** Markdown — **Modelo/API:** Anthropic/MCP y cualquier cliente compatible.
**Elige si:** buscas antes de construir — **Evita si:** ya sabes que necesitas uno a medida.
**Combina con:** [mcp-use](#-mcp-use) · [servers](#-servers)
**Repo:** [GitHub](https://github.com/punkpeye/awesome-mcp-servers)

### 🕸️ mcp-neo4j
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud.
**Por qué destaca:** lo mantiene la propia comunidad de Neo4j y viene contenedorizado y listo para HTTP, lo que facilita llevar grafos a producción con IA.
**Cómo funciona:** expone consultas Cypher y operaciones sobre el grafo como herramientas MCP que el cliente invoca mediante el protocolo.
**Instalación:** `pip install mcp-neo4j-cypher` (o imagen Docker) y registrar el servidor en la config del cliente MCP.
**Casos:** consultar/escribir grafos Neo4j desde un asistente · backends de conocimiento.
**Stack:** Python, Docker — **Modelo/API:** clientes MCP.
**Elige si:** usas Neo4j con IA — **Evita si:** no trabajas con grafos.
**Combina con:** [graphrag](#-graphrag) · [awesome-mcp-servers](#-awesome-mcp-servers)
**Repo:** [GitHub](https://github.com/neo4j-contrib/mcp-neo4j)

### 🔌 n8n-mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n para ayudar a construir y depurar flujos.
**Por qué destaca:** reduce drásticamente los errores cuando se pide a una IA que arme un workflow de n8n, al darle acceso fiable a los parámetros reales de cada nodo.
**Cómo funciona:** el cliente MCP (Claude, Cursor…) invoca herramientas del servidor para consultar nodos, propiedades y ejemplos vía el protocolo MCP.
**Instalación:** `npx n8n-mcp` y añadirlo a la config del cliente MCP (p. ej. Claude Desktop).
**Casos:** que Claude investigue parámetros del nodo de Gmail para armar un flujo · reducir errores al construir workflows.
**Stack:** Node.js/TypeScript, MCP — **Modelo/API:** Claude Desktop/Code, Cursor, Gemini CLI.
**Elige si:** generas flujos n8n con IA — **Evita si:** no usas n8n.
**Combina con:** [n8n](#-n8n) · [n8n-skills](#-n8n-skills) · receta [Bot WhatsApp](#-1-bot-de-whatsapp-con-ia)
**Repo:** [GitHub](https://github.com/czlonkowski/n8n-mcp)

### 🌍 public-apis
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos.
**Por qué destaca:** es una de las referencias más estrelladas de GitHub para encontrar fuentes de datos externas sin tener que buscarlas una a una.
**Cómo funciona:** tabla en Markdown organizada por temática con la URL, autenticación y nivel de HTTPS de cada API.
**Instalación:** sin instalación; se navega el README (o su versión web) y se consume cada API según su propia documentación.
**Casos:** conectar fuentes externas de datos · encontrar una API para un proyecto.
**Stack:** Markdown — **Modelo/API:** N/A.
**Elige si:** buscas datos externos — **Evita si:** ya tienes tus fuentes definidas.
**Combina con:** [n8n](#-n8n) · [firecrawl](#-firecrawl)
**Repo:** [GitHub](https://github.com/public-apis/public-apis)

---

## 6. Memoria, LLM Ops & Observabilidad

Memoria persistente de agentes, gateways de modelos, trazas/evaluación y logging.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… |
|---|---|---|---|
| [mem0](#-mem0) | Capa de memoria para agentes | 📚 | Quieres memoria persistente estándar |
| [agentmemory](#-agentmemory) | Memoria persistente para agentes de código | 📚 | Tu agente debe recordar entre sesiones |
| [mempalace](#-mempalace) | Memoria local-first verbatim | 📚 | Quieres memoria sin llamadas a API |
| [turbovec](#-turbovec) | Búsqueda vectorial rápida (TurboQuant) | 📚 | Necesitas vector search eficiente |
| [litellm](#-litellm) | Gateway unificado a 100+ LLMs | 📚 | Cambias de proveedor sin tocar código |
| [langfuse](#-langfuse) | Observabilidad/trazas de LLM | ⚙️ | Quieres ver y evaluar tus llamadas LLM |
| [llmfit](#-llmfit) | Evaluación/ajuste de LLMs | 📚 | Mides calidad/fit de modelos |
| [headroom](#-headroom) | Compactación de contexto | 📚 | Te quedas sin ventana de contexto |
| [sandbox](#-sandbox) | Entorno sandbox all-in-one para agentes | ⚙️ | Necesitas browser+terminal+VSCode+MCP aislados |
| [loguru](#-loguru) | Logging simple para Python | 📚 | Quieres logs limpios sin boilerplate |

### ⚖️ ¿Cuál elegir? — Memoria de agentes

| Repo | Cuándo usarlo | Ventaja clave |
|---|---|---|
| **mem0** | Memoria estándar para apps/agentes | Popular, integraciones amplias |
| **agentmemory** | Agentes de código que re-explican todo | Recuerdo entre sesiones, multi-cliente |
| **mempalace** | Privacidad total, sin API | Verbatim, alto recall, zero API calls |
| **turbovec** | Capa de recuperación vectorial | Rapidez (TurboQuant) en Python/Rust |

### 🧠 mem0
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental.
**Por qué destaca:** es uno de los proyectos de memoria de agentes más adoptados, con SDK estable e integraciones amplias en el ecosistema de frameworks.
**Cómo funciona:** combina extracción de hechos vía LLM con almacenamiento en vector DBs (Qdrant, etc.) para indexar y consultar memorias relevantes por similitud.
**Instalación:** `pip install mem0ai` (también SDK en npm) o servicio gestionado.
**Casos:** recordar preferencias del usuario entre sesiones · memoria long-term para agentes.
**Stack:** Python/TS — **Modelo/API:** múltiples + vector DBs.
**Elige si:** quieres memoria estándar lista — **Evita si:** necesitas todo local sin API ([mempalace](#-mempalace)).
**Combina con:** [crewAI](#-crewai) · [langchain](#-langchain)
**Repo:** [GitHub](https://github.com/mem0ai/mem0)

### 💾 agentmemory
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes.
**Por qué destaca:** evita re-explicar el contexto al cambiar de asistente, ofreciendo una memoria compartida poco común entre herramientas de coding.
**Cómo funciona:** se conecta vía MCP para que distintos clientes lean y escriban en el mismo almacén persistente del motor iii.
**Instalación:** instalación del servidor MCP según el repo y configuración en cada cliente compatible.
**Casos:** que el agente "recuerde todo" y no re-expliques el contexto · memoria multi-cliente vía MCP.
**Stack:** motor iii — **Modelo/API:** cualquier cliente MCP.
**Elige si:** cambias de asistente y quieres una memoria común — **Evita si:** te basta la memoria nativa del cliente.
**Combina con:** [mem0](#-mem0) · [ruflo](#-ruflo)
**Repo:** [GitHub](https://github.com/rohitg00/agentmemory)

### 🏛️ mempalace
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.
**Por qué destaca:** prioriza la privacidad total (cero llamadas a API) reportando recall competitivo en benchmarks de memoria de largo plazo.
**Cómo funciona:** guarda los textos verbatim y los recupera mediante un backend de búsqueda conectable, sin depender de un LLM remoto para almacenar.
**Instalación:** `pip install` desde PyPI.
**Casos:** memoria privada para agentes · recuerdo de largo plazo sin enviar datos a la nube.
**Stack:** Python (PyPI) — **Modelo/API:** local, backend conectable.
**Elige si:** la privacidad es prioridad — **Evita si:** quieres un SaaS gestionado.
**Combina con:** [open-notebook](#-open-notebook) · [odysseus](#-odysseus)
**Repo:** [GitHub](https://github.com/MemPalace/mempalace)

### ⚡ turbovec
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida.
**Por qué destaca:** apuesta por la eficiencia, aplicando una técnica de cuantización moderna para acelerar la búsqueda con bajo coste de memoria.
**Cómo funciona:** comprime los vectores con TurboQuant y resuelve las consultas por similitud, con bindings disponibles en Python y Rust.
**Instalación:** `pip install` (Python) o crate de Rust según el repo.
**Casos:** capa de recuperación para RAG · vector search eficiente embebido.
**Stack:** Python / Rust — **Modelo/API:** N/A (infra de vectores).
**Elige si:** necesitas vector search veloz — **Evita si:** ya usas una vector DB completa.
**Combina con:** [mem0](#-mem0) · [graphrag](#-graphrag)
**Repo:** [GitHub](https://github.com/RyanCodrai/turbovec)

### 🔀 litellm
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.
**Por qué destaca:** es un estándar de facto para abstraer proveedores, muy adoptado por su routing, control de costos y fallback entre modelos.
**Cómo funciona:** traduce cada petición al formato del proveedor destino y puede correr como proxy/gateway con balanceo, reintentos y registro de uso.
**Instalación:** `pip install litellm` (o despliegue del proxy vía Docker).
**Casos:** probar varios modelos sin reescribir código · balancear costo/fallback entre proveedores.
**Stack:** Python — **Modelo/API:** OpenAI, Anthropic, Google, locales, etc.
**Elige si:** trabajas con múltiples modelos — **Evita si:** usas un único proveedor fijo.
**Combina con:** [langchain](#-langchain) · [langfuse](#-langfuse) · [llm-council](#-llm-council)
**Repo:** [GitHub](https://github.com/BerriAI/litellm)

### 📡 langfuse
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente.
**Por qué destaca:** es una de las plataformas de LLM observability de referencia, con self-host y cloud e integraciones con los frameworks más usados.
**Cómo funciona:** instrumentas tu app con sus SDKs (o vía OpenTelemetry) para enviar trazas, costos y evaluaciones a un backend con UI de análisis.
**Instalación:** Docker Compose para self-host o cuenta cloud; SDKs vía `pip`/`npm`.
**Casos:** ver el detalle de cada llamada/agente · evaluar prompts y medir costos.
**Stack:** TS, Docker, self-host/cloud — **Modelo/API:** SDKs para múltiples frameworks.
**Elige si:** operas agentes en serio — **Evita si:** haces prototipos triviales.
**Combina con:** [langchain](#-langchain) · [litellm](#-litellm) · [ag2](#-ag2)
**Repo:** [GitHub](https://github.com/langfuse/langfuse)

### 📏 llmfit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar modelos con datos.
**Por qué destaca:** proyecto enfocado y de nicho, útil para llevar la elección de modelo a un flujo objetivo y automatizable en CI.
**Cómo funciona:** ejecuta evaluaciones sobre las salidas de varios modelos y reporta métricas de calidad, integrable en pipelines de integración continua.
**Instalación:** instalación según el repo (binario Go o paquete Python).
**Casos:** comparar modelos para una tarea · CI de calidad de prompts/modelos.
**Stack:** Go/Python — **Modelo/API:** múltiples.
**Elige si:** necesitas elegir modelo con datos — **Evita si:** ya tienes el modelo decidido.
**Combina con:** [litellm](#-litellm) · [langfuse](#-langfuse)
**Repo:** [GitHub](https://github.com/AlexsJones/llmfit)

### 🗜️ headroom
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial.
**Por qué destaca:** proyecto pequeño y específico que ataca un dolor habitual de los agentes (quedarse sin ventana de contexto) de forma directa.
**Cómo funciona:** resume y condensa el contexto entrante para maximizar la señal por token antes de pasarlo al modelo, de forma agnóstica al proveedor.
**Instalación:** instalación según el repo (`pip`/`npm`).
**Casos:** resumir/condensar contexto largo · ganar espacio en la ventana.
**Stack:** Python/TS — **Modelo/API:** agnóstico.
**Elige si:** te quedas sin contexto — **Evita si:** tus prompts ya caben holgados.
**Combina con:** [Context-Engineering](#-context-engineering) · [codegraph](#-codegraph)
**Repo:** [GitHub](https://github.com/chopratejas/headroom)

### 📦 sandbox
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado.
**Por qué destaca:** concentra en un solo contenedor todas las herramientas que un agente necesita, ofreciendo un entorno reproducible y aislado poco común.
**Cómo funciona:** levanta un contenedor con los servicios expuestos vía web y conectables por clientes MCP, aislando la ejecución del host.
**Instalación:** `docker run` de la imagen del proyecto.
**Casos:** ejecutar agentes de forma aislada · entorno reproducible para tareas dev.
**Stack:** Docker/web — **Modelo/API:** clientes MCP.
**Elige si:** quieres aislar la ejecución de agentes — **Evita si:** te basta correr local sin sandbox.
**Combina con:** [OpenHands](#-openhands) · [ECC](#-ecc)
**Repo:** [GitHub](https://github.com/agent-infra/sandbox)

### 📝 loguru
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa.
**Por qué destaca:** es una de las librerías de logging más populares en Python por su API mínima y su gran ergonomía frente al módulo estándar.
**Cómo funciona:** expone un único objeto `logger` preconfigurado con rotación, formato enriquecido y captura de excepciones en una sola línea.
**Instalación:** `pip install loguru`.
**Casos:** logs legibles sin configuración · instrumentar pipelines y scripts.
**Stack:** Python — **Modelo/API:** N/A.
**Elige si:** quieres logging fácil en Python — **Evita si:** ya usas el stdlib `logging` configurado.
**Combina con:** cualquier pipeline Python
**Repo:** [GitHub](https://github.com/Delgan/loguru)

---

## 7. Inteligencia de Código, Datos & Entrenamiento

Indexar/mapear repos, grafos de conocimiento, ciencia de datos y entrenar modelos desde cero.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… |
|---|---|---|---|
| [codegraph](#-codegraph) | Índice semántico de código local | 🧩 | Quieres que la IA entienda repos grandes barato |
| [graphify](#-graphify) | Grafo de conocimiento de proyecto | 🧩 | Visualizas relaciones de código/PDF/imagen |
| [graphrag](#-graphrag) | RAG basado en grafos | 📚 | Necesitas recuperación contextual por grafo |
| [GitNexus](#-gitnexus) | Exploración de repos Git | 🖥️ | Navegas y entiendes un repo visualmente |
| [DeepSeek-Coder](#-deepseek-coder) | Modelo de código abierto | 🧩 | Generas/revisas código con modelo propio |
| [nanoGPT](#-nanogpt) | GPT mínimo entrenable | 📚 | Aprendes/entrenas un GPT desde cero |
| [nanochat](#-nanochat) | ChatGPT mínimo full-stack | 📚 | Entrenas un chat end-to-end didáctico |
| [llm.c](#-llmc) | Entrenamiento de LLM en C/CUDA puro | 📚 | Quieres entrenar sin frameworks pesados |
| [how-to-train-your-gpt](#-how-to-train-your-gpt) | Guía para entrenar un GPT | 📂 | Buscas un tutorial práctico |
| [cosmos](#-cosmos) | World models de NVIDIA | 🧩 | Generas mundos/datos para IA física |
| [data-science-ipython-notebooks](#-data-science-ipython-notebooks) | Notebooks de ciencia de datos | 📂 | Aprendes/consultas DS y ML |
| [awesome-bigdata](#-awesome-bigdata) | Directorio de big data | 📂 | Buscas herramientas de datos a escala |
| [openai-python](#-openai-python) | SDK oficial de OpenAI | 📚 | Llamas a la API de OpenAI desde Python |

### ⚖️ ¿Cuál elegir? — Entender código vs. grafos

| Repo | Cuándo usarlo | Ventaja clave |
|---|---|---|
| **codegraph** | Reducir lectura/tokens en repos grandes | 100% local, ahorra ~58% de tool calls |
| **graphify** | Auditoría/onboarding visual | HTML interactivo + reporte + JSON |
| **graphrag** | Recuperación contextual avanzada | RAG sobre grafo de conocimiento |
| **GitNexus** | Explorar un repo Git concreto | Navegación e ideas sobre el repo |

### ⚖️ ¿Cuál elegir? — Entrenar desde cero (didáctico)

| Repo | Nivel | Ventaja clave |
|---|---|---|
| **nanoGPT** | Intro a entrenar GPT | Minimalista y claro (Karpathy) |
| **nanochat** | Chat full-stack mínimo | Pipeline completo de un ChatGPT |
| **llm.c** | Bajo nivel C/CUDA | Sin frameworks, máximo control |
| **how-to-train-your-gpt** | Tutorial guiado | Paso a paso explicado |

### 📊 codegraph
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟢 fácil
**Qué es:** CLI que indexa tu código y da a los asistentes de IA inteligencia semántica 100% local, permitiéndoles entender la estructura y el flujo de un repo sin leer archivo por archivo ni gastar llamadas a herramientas.
**Por qué destaca:** convierte repos enormes en algo navegable para la IA con coste casi nulo; muy valorado en flujos de agentes de código por su ahorro real de tokens.
**Cómo funciona:** construye un índice semántico local del repositorio que el asistente consulta vía comandos; se acopla a Claude Code, Gemini y Cursor sin necesidad de un modelo propio.
**Instalación:** `npm install -g codegraph` (binario autónomo de Node.js) y luego `codegraph index .`.
**Casos:** `codegraph index .` para que el asistente entienda el flujo sin leer archivo por archivo.
**Stack:** JavaScript/Node.js (binario autónomo) — **Modelo/API:** no requiere IA; se acopla a Claude Code, Gemini, Cursor.
**Elige si:** trabajas repos grandes — **Evita si:** tu base de código es pequeña.
**Combina con:** [graphify](#-graphify) · [headroom](#-headroom) · receta [Análisis de repos](#-5-análisis-de-repos-grandes)
**Repo:** [GitHub](https://github.com/colbymchenry/codegraph)

### 🕸️ graphify
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** generador de grafos de conocimiento para proyectos locales que mapea código, PDFs, imágenes y video en diagramas interactivos, revelando cómo se conectan las piezas de un sistema.
**Por qué destaca:** combina visualización navegable, reporte legible y datos exportables en un solo paso, ideal para auditorías y onboarding cuando un índice de texto no basta.
**Cómo funciona:** analiza las fuentes del proyecto y produce un grafo con nodos y relaciones; opcionalmente usa un LLM (cloud o local) para enriquecer el análisis semántico.
**Instalación:** `pipx install graphify` o `uv tool install graphify`, luego `/graphify .` sobre el proyecto.
**Casos:** `/graphify .` para mapear llamadas de funciones · auditoría rápida de un sistema.
**Stack:** Python 3.10+, uv/pipx — **Modelo/API:** opcional (OpenAI/Anthropic o locales Llama/Mistral).
**Elige si:** quieres ver conexiones visualmente — **Evita si:** solo necesitas índice textual ([codegraph](#-codegraph)).
**Combina con:** [codegraph](#-codegraph) · [graphrag](#-graphrag)
**Repo:** [GitHub](https://github.com/safishamsi/graphify)

### 🔗 graphrag
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.
**Por qué destaca:** proyecto de Microsoft Research muy difundido que mejora notablemente las respuestas en preguntas que requieren conectar entidades dispersas en muchos documentos.
**Cómo funciona:** un LLM extrae entidades y relaciones para construir el grafo, lo resume por comunidades y luego responde combinando recuperación local y global con embeddings.
**Instalación:** `pip install graphrag` y luego `graphrag index` / `graphrag query` sobre tu corpus.
**Casos:** preguntas complejas sobre un corpus · recuperación que entiende relaciones.
**Stack:** Python — **Modelo/API:** múltiples LLMs + embeddings.
**Elige si:** tu corpus tiene relaciones ricas — **Evita si:** un RAG simple basta.
**Combina con:** [graphify](#-graphify) · [mcp-neo4j](#-mcp-neo4j) · [turbovec](#-turbovec)
**Repo:** [GitHub](https://github.com/microsoft/graphrag)

### 🧭 GitNexus
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva.
**Por qué destaca:** facilita comprender un repo concreto de forma interactiva en vez de leer ficheros sueltos, útil cuando llegas a un proyecto ajeno.
**Cómo funciona:** una interfaz web (TypeScript) recorre el repositorio y lo presenta como vistas navegables, apoyándose en LLMs para responder preguntas y sugerir ideas.
**Instalación:** `git clone https://github.com/abhigyanpatwari/GitNexus` y arranque del front web según el README.
**Casos:** onboarding en un repo nuevo · navegar relaciones y discutir ideas.
**Stack:** web/TS — **Modelo/API:** múltiples.
**Elige si:** quieres entender un repo puntual — **Evita si:** necesitas indexar muchos repos ([codegraph](#-codegraph)).
**Combina con:** [codegraph](#-codegraph) · receta [Análisis de repos](#-5-análisis-de-repos-grandes)
**Repo:** [GitHub](https://github.com/abhigyanpatwari/GitNexus)

### 🧩 DeepSeek-Coder
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software.
**Por qué destaca:** una de las alternativas abiertas más fuertes para tareas de código, competitiva con modelos propietarios y desplegable en tu propia infraestructura.
**Cómo funciona:** modelos transformer ejecutados con PyTorch sobre GPU; se cargan en local (p. ej. vía Hugging Face Transformers o vLLM) o se consumen por API.
**Instalación:** `pip install transformers torch` y descarga de pesos desde Hugging Face, o uso vía API de DeepSeek.
**Casos:** generación y revisión de código · asistencia técnica con modelo propio.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** modelos DeepSeek (local o API).
**Elige si:** quieres un modelo de código abierto — **Evita si:** prefieres APIs comerciales gestionadas.
**Combina con:** [litellm](#-litellm) · [codegraph](#-codegraph)
**Repo:** [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder)

### 🔬 nanoGPT
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo.
**Por qué destaca:** referencia didáctica de Karpathy ampliamente usada para aprender cómo funciona realmente el entrenamiento de un GPT, sin capas de abstracción.
**Cómo funciona:** define el modelo GPT y su bucle de entrenamiento en PyTorch sobre GPU, reproduciendo resultados tipo GPT-2 con unos pocos cientos de líneas.
**Instalación:** `git clone https://github.com/karpathy/nanoGPT` y `pip install torch numpy transformers datasets tiktoken`.
**Casos:** aprender cómo se entrena un GPT · experimentos pequeños reproducibles.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** entrena modelos propios.
**Elige si:** quieres entender el entrenamiento — **Evita si:** solo consumes modelos vía API.
**Combina con:** [nanochat](#-nanochat) · [llm.c](#-llmc)
**Repo:** [GitHub](https://github.com/karpathy/nanoGPT)

### 💬 nanochat
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible.
**Por qué destaca:** referencia didáctica de Karpathy que muestra el ciclo completo de un asistente conversacional en un solo repo compacto y legible.
**Cómo funciona:** encadena las etapas pretrain → SFT → inferencia en PyTorch sobre GPU, con scripts que entrenan y luego sirven el modelo de chat.
**Instalación:** `git clone https://github.com/karpathy/nanochat` y seguir el script de entrenamiento del README (entorno PyTorch con GPU).
**Casos:** ver el ciclo completo (pretrain→SFT→chat) · base educativa.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** entrena modelos propios.
**Elige si:** quieres el pipeline completo — **Evita si:** solo necesitas el core ([nanoGPT](#-nanogpt)).
**Combina con:** [nanoGPT](#-nanogpt)
**Repo:** [GitHub](https://github.com/karpathy/nanochat)

### ⚙️ llm.c
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🔴 pesado
**Qué es:** implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo.
**Por qué destaca:** referencia didáctica de Karpathy que reproduce GPT-2 con dependencias mínimas, ideal para entender qué hace realmente la GPU bajo el capó.
**Cómo funciona:** escribe a mano los kernels de las pasadas forward/backward en C y CUDA, gestionando memoria y operaciones que normalmente oculta un framework.
**Instalación:** `git clone https://github.com/karpathy/llm.c`, instalar CUDA toolkit y compilar con `make`.
**Casos:** entrenar GPT-2 con mínima dependencia · entender el cómputo de bajo nivel.
**Stack:** C, CUDA — **Modelo/API:** entrena modelos propios.
**Elige si:** quieres bajo nivel sin abstracciones — **Evita si:** prefieres PyTorch ([nanoGPT](#-nanogpt)).
**Combina con:** [nanoGPT](#-nanogpt)
**Repo:** [GitHub](https://github.com/karpathy/llm.c)

### 📘 how-to-train-your-gpt
**Etiquetas:** Ejecución 🏠 local-first · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción.
**Por qué destaca:** repo pequeño y poco conocido, útil como complemento explicado al entrenamiento; honestamente, es un material de aprendizaje modesto frente a referencias como nanoGPT.
**Cómo funciona:** recorre en Python el proceso de entrenar un GPT con explicaciones intercaladas, apoyándose en el ecosistema PyTorch.
**Instalación:** `git clone https://github.com/raiyanyahya/how-to-train-your-gpt` y seguir las instrucciones del repositorio.
**Casos:** seguir un paso a paso de entrenamiento · material de estudio.
**Stack:** Python — **Modelo/API:** entrena modelos propios.
**Elige si:** quieres una guía explicada — **Evita si:** prefieres solo el código ([nanoGPT](#-nanogpt)).
**Combina con:** [nanoGPT](#-nanogpt) · [nanochat](#-nanochat)
**Repo:** [GitHub](https://github.com/raiyanyahya/how-to-train-your-gpt)

### 🌌 cosmos
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots.
**Por qué destaca:** iniciativa de NVIDIA con ecosistema y pesos publicados en Hugging Face, una referencia clave para la generación de datos de simulación física.
**Cómo funciona:** ejecuta modelos generativos de mundo en Python sobre GPU para producir vídeo/escenas sintéticas que sirven como datos de entrenamiento o simulación.
**Instalación:** `git clone https://github.com/NVIDIA/Cosmos`, instalar dependencias del repo y descargar pesos Cosmos desde Hugging Face (requiere GPU potente).
**Casos:** generar datos/mundos sintéticos · entrenar agentes físicos/robótica.
**Stack:** Python, GPU — **Modelo/API:** modelos Cosmos de NVIDIA.
**Elige si:** trabajas IA física/robótica — **Evita si:** haces tareas de texto/UI.
**Combina con:** [diffusers](#-diffusers)
**Repo:** [GitHub](https://github.com/NVIDIA/Cosmos)

### 📓 data-science-ipython-notebooks
**Etiquetas:** Ejecución 🏠 local-first · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep learning y big data, con ejemplos listos para ejecutar.
**Por qué destaca:** uno de los repositorios de referencia más populares para aprender DS de forma práctica, con material abundante y bien organizado por temas.
**Cómo funciona:** son notebooks Jupyter autocontenidos que se abren y ejecutan localmente, mostrando explicaciones y código sobre las librerías clásicas del ecosistema Python.
**Instalación:** `git clone https://github.com/donnemartin/data-science-ipython-notebooks` y abrir los notebooks con `jupyter lab`.
**Casos:** aprender pandas/NumPy/ML · consultar ejemplos prácticos.
**Stack:** Python, Jupyter — **Modelo/API:** N/A.
**Elige si:** estudias/consultas DS — **Evita si:** buscas una librería, no ejemplos.
**Combina con:** [dash](#-dash) · [streamlit](#-streamlit)
**Repo:** [GitHub](https://github.com/donnemartin/data-science-ipython-notebooks)

### 🗄️ awesome-bigdata
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala.
**Por qué destaca:** lista "awesome" ampliamente referenciada que ofrece un panorama completo del stack de datos grandes en un solo vistazo.
**Cómo funciona:** es un documento Markdown con enlaces clasificados; se consulta directamente en GitHub sin instalar nada.
**Instalación:** no requiere instalación; se navega online en el repositorio de GitHub.
**Casos:** elegir stack de datos a escala · descubrir herramientas por categoría.
**Stack:** Markdown — **Modelo/API:** N/A.
**Elige si:** diseñas pipelines de datos grandes — **Evita si:** tu proyecto es pequeño.
**Combina con:** [awesome-dataviz](#-awesome-dataviz)
**Repo:** [GitHub](https://github.com/oxnr/awesome-bigdata)

### 🐍 openai-python
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** SDK oficial de OpenAI para Python, que expone de forma tipada y cómoda la API (chat, embeddings, imágenes, audio) y es la base habitual para apps que usan sus modelos.
**Por qué destaca:** cliente oficial y al día mantenido por OpenAI, con amplia adopción y soporte inmediato de las novedades de la API.
**Cómo funciona:** envuelve las peticiones HTTP a la API en clientes Python síncronos y asíncronos, con tipado y streaming integrados.
**Instalación:** `pip install openai` y configurar `OPENAI_API_KEY`.
**Casos:** llamar a la API de OpenAI · base para apps que usan GPT.
**Stack:** Python — **Modelo/API:** OpenAI.
**Elige si:** usas modelos de OpenAI — **Evita si:** quieres abstracción multi-proveedor ([litellm](#-litellm)).
**Combina con:** [litellm](#-litellm) · [langchain](#-langchain)
**Repo:** [GitHub](https://github.com/openai/openai-python)

---

## 8. Workspaces de IA Local & Notebooks

Entornos privados todo-en-uno y herramientas tipo NotebookLM.

### 🔍 Escaneo rápido

| Repo | Qué es | Ejec. | Elige si… |
|---|---|---|---|
| [ECC](#-ecc) | Arnés/OS para agentes con seguridad | 🏠 | Quieres ejecutar agentes con escudo de seguridad |
| [odysseus](#-odysseus) | Workspace privado todo-en-uno | 🏠 | Quieres un "Copilot" local soberano |
| [open-notebook](#-open-notebook) | NotebookLM open-source privado | 🏠 | Procesas fuentes y generas audios localmente |
| [notebooklm-py](#-notebooklm-py) | API Python para NotebookLM | ☁️ | Automatizas NotebookLM desde scripts |
| [notebooklm-mcp-cli](#-notebooklm-mcp-cli) | CLI/MCP para NotebookLM | ☁️ | Integras NotebookLM con clientes MCP |

### ⚖️ ¿Cuál elegir? — Local privado vs. NotebookLM

| Repo | Cuándo usarlo | Ventaja clave |
|---|---|---|
| **odysseus** | Asistente administrativo integral | Chat+docs+correo+calendario local |
| **open-notebook** | Conocimiento privado tipo NotebookLM | 100% local, sin cuotas |
| **notebooklm-py / notebooklm-mcp-cli** | Automatizar el NotebookLM real de Google | Sube y sintetiza fuentes a escala |

### 🌌 ECC
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura, sirviendo de capa intermedia entre el modelo y tu sistema.
**Por qué destaca:** aporta una capa de seguridad de ejecución poco común en arneses de agentes, orientada a equipos que dan acceso real a su máquina a herramientas como Claude Code o Cursor.
**Cómo funciona:** intercepta y valida las acciones del agente (comandos, ficheros) mediante un core en Rust con hooks y memoria persistente antes de dejarlas tocar el sistema.
**Instalación:** `git clone` del repo y compilación del core en Rust más dependencias en TS/Python/Go.
**Casos:** que Claude ejecute comandos bash sin poner en riesgo el sistema · memoria persistente y hooks.
**Stack:** Rust (core), TypeScript, Python, Go — **Modelo/API:** Claude Code, Cursor, Zed, Codex, Gemini, Copilot.
**Elige si:** ejecutas agentes con riesgo — **Evita si:** solo haces prompts de chat.
**Combina con:** [OpenHands](#-openhands) · [sandbox](#-sandbox) · [hermes-agent](#-hermes-agent)
**Repo:** [GitHub](https://github.com/affaan-m/ECC)

### ⛺ odysseus
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado.
**Por qué destaca:** ofrece una alternativa local y soberana a las suites tipo Copilot/Workspace AI, juntando en un solo lugar lo que normalmente reparten varios SaaS.
**Cómo funciona:** un backend Python orquesta los agentes sobre una base PostgreSQL y una UI React, conectando con modelos locales vía Ollama/Llama.cpp o con APIs comerciales.
**Instalación:** `docker compose` para levantar backend, base de datos y frontend, o despliegue manual con Python y Node.
**Casos:** asistente administrativo privado · redactar correos y agendar desde tus documentos.
**Stack:** Python, React, PostgreSQL — **Modelo/API:** Ollama/Llama.cpp o APIs comerciales.
**Elige si:** quieres operación privada todo-en-uno — **Evita si:** prefieres SaaS gestionado.
**Combina con:** [open-notebook](#-open-notebook) · [ECC](#-ecc) · [mem0](#-mem0) · receta [Workspace privado](#-4-workspace-privado-local-soberano)
**Repo:** [GitHub](https://github.com/pewdiepie-archdaemon/odysseus)

### 📓 open-notebook
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo.
**Por qué destaca:** cubre la demanda de un NotebookLM sin envío de datos a la nube y es uno de los proyectos de referencia en la comunidad open-source para este caso.
**Cómo funciona:** un backend FastAPI indexa las fuentes y las consulta vía RAG contra modelos servidos por Ollama, con una UI React/Next.js para notebooks y audio.
**Instalación:** `docker` (imagen oficial) o `pip` más Ollama para los modelos locales.
**Casos:** subir un manual y generar un audio explicativo · chats de consulta sobre tus PDFs.
**Stack:** Python (FastAPI), React/Next.js — **Modelo/API:** Llama 3/Gemma 2 vía Ollama o APIs comerciales.
**Elige si:** quieres NotebookLM privado — **Evita si:** prefieres el NotebookLM real automatizado ([notebooklm-py](#-notebooklm-py)).
**Combina con:** [odysseus](#-odysseus) · [markitdown](#-markitdown)
**Repo:** [GitHub](https://github.com/lfnovo/open-notebook)

### 🎙️ notebooklm-py
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código.
**Por qué destaca:** abre el NotebookLM real a la automatización, algo que la interfaz web oficial no permite, útil para procesar fuentes a escala.
**Cómo funciona:** envuelve los endpoints internos de NotebookLM en una librería Python que sube fuentes y dispara síntesis usando tu sesión/credenciales de Google.
**Instalación:** `pip install` de la librería más configuración de credenciales de Google.
**Casos:** subir 20 PDFs y pedir una síntesis temática · automatizar generación de notas de audio.
**Stack:** Python — **Modelo/API:** NotebookLM/Google (Gemini Pro/Ultra).
**Elige si:** automatizas el NotebookLM real — **Evita si:** quieres todo local ([open-notebook](#-open-notebook)).
**Combina con:** [notebooklm-mcp-cli](#-notebooklm-mcp-cli)
**Repo:** [GitHub](https://github.com/teng-lin/notebooklm-py)

### 🎚️ notebooklm-mcp-cli
**Etiquetas:** Ejecución ☁️ API/cloud · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil
**Qué es:** CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP.
**Por qué destaca:** expone NotebookLM como herramienta MCP, permitiendo que asistentes como Claude lo usen como un servicio más dentro de sus flujos.
**Cómo funciona:** levanta un servidor MCP en Python que traduce las llamadas del cliente a operaciones de NotebookLM (crear, actualizar y consultar notebooks).
**Instalación:** `pip install` o `git clone` y registro del servidor MCP en tu cliente.
**Casos:** crear/actualizar notebooks en la nube desde MCP · flujos repetibles de audio.
**Stack:** Python, MCP — **Modelo/API:** NotebookLM/Google.
**Elige si:** integras NotebookLM con tu asistente — **Evita si:** prefieres la API directa ([notebooklm-py](#-notebooklm-py)).
**Combina con:** [notebooklm-py](#-notebooklm-py) · [awesome-mcp-servers](#-awesome-mcp-servers)
**Repo:** [GitHub](https://github.com/jacob-bd/notebooklm-mcp-cli)

---

## 9. Diseño, UI & Frontend

Diseño asistido, librerías de componentes, animación y 3D.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… |
|---|---|---|---|
| [open-design](#-open-design) | Diseño colaborativo asistido por IA | 🖥️ | Maquetas y animas UI desde texto |
| [penpot](#-penpot) | Diseño/prototipado open-source | 🖥️ | Quieres alternativa abierta a Figma |
| [plasmic](#-plasmic) | Builder visual sobre tu código | 🖥️ | Construyes UI conectada a tu codebase |
| [design.md](#-designmd) | Spec de identidad visual para agentes | 🎨 | Das al agente un sistema de diseño persistente |
| [impeccable](#-impeccable) | Guía de diseño para agentes de código | 🎨 | Evitas los "tells" de UI generada por IA |
| [tailwindcss](#-tailwindcss) | Framework CSS utility-first | 📚 | Estilas rápido y consistente |
| [magicui](#-magicui) | Componentes UI atractivos | 📚 | Quieres acabado visual con poco esfuerzo |
| [heroui](#-heroui) | Componentes React accesibles (MCP) | 📚 | Montas SaaS/landing accesible y moderna |
| [ui](#-ui-shadcn) | Componentes copy-paste (shadcn) | 📚 | Quieres control total del código de UI |
| [normalize.css](#-normalizecss) | Reset/normalización CSS | 📚 | Igualas estilos base entre navegadores |
| [GSAP](#-gsap) | Librería de animación web | 📚 | Necesitas animaciones avanzadas |
| [motion](#-motion) | Animación declarativa (Framer Motion) | 📚 | Animas componentes React fácil |
| [three.js](#-threejs) | Motor 3D para la web | 📚 | Renderizas 3D en el navegador |
| [react-three-fiber](#-react-three-fiber) | three.js para React | 📚 | Quieres 3D declarativo en React |
| [swr](#-swr) | Data fetching para React | 📚 | Manejas datos remotos en frontend |

### ⚖️ ¿Cuál elegir? — Diseño asistido vs. builder

| Repo | Cuándo usarlo | Ventaja clave |
|---|---|---|
| **open-design** | Generar/animar UI desde instrucciones | Bidireccional, multimodelo (AMR) |
| **plasmic** | Editar visualmente sobre tu código | Conecta con componentes propios |
| **penpot** | Diseño/prototipo colaborativo | Open-source self-host |
| **design.md / impeccable** | Guiar a un agente a diseñar bien | Sistema/reglas persistentes anti-slop |

### ⚖️ ¿Cuál elegir? — Librerías de componentes

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **ui (shadcn)** | Control total del código | Copy-paste, sin capa pesada | Quieres componentes "llave en mano" |
| **heroui** | Accesibilidad y producción | React Aria + Tailwind + MCP | No usas React/Tailwind |
| **magicui** | Estética y velocidad | Componentes vistosos listos | Necesitas accesibilidad estricta |
| **tailwindcss** | Base de estilos de todo lo anterior | Utility-first universal | Prefieres CSS-in-JS |

### 🎨 open-design
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** editor/workspace de diseño colaborativo asistido por IA que genera, maqueta y anima interfaces a partir de instrucciones en lenguaje natural; alternativa libre a Claude Design Artifacts.
**Por qué destaca:** combina generación por IA con edición visual real y enruta varios modelos en una sola herramienta, algo poco común en editores abiertos.
**Cómo funciona:** app de escritorio en React + Tauri (Rust) que traduce prompts a UI editable y la sincroniza de vuelta, con enrutador AMR que reparte peticiones entre modelos.
**Instalación:** clonar el repo y compilar la app Tauri (binarios de release según plataforma).
**Casos:** describir e ver cómo la IA maqueta y anima una UI exportable · importar sistemas de diseño (Figma, Tailwind).
**Stack:** TypeScript/React, Tauri (Rust) — **Modelo/API:** GPT-4o, Claude, Gemini, DeepSeek vía AMR.
**Elige si:** generas UI desde texto — **Evita si:** prefieres editar sobre tu código ([plasmic](#-plasmic)).
**Combina con:** [tailwindcss](#-tailwindcss) · [heroui](#-heroui) · receta [Web app moderna](#-7-web-app-moderna-con-ia)
**Repo:** [GitHub](https://github.com/nexu-io/open-design)

### ✏️ penpot
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🔴 pesado
**Qué es:** plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos.
**Por qué destaca:** es la alternativa abierta a Figma más madura y adoptada, con estándares web (SVG) y self-host real.
**Cómo funciona:** suite web basada en SVG y CSS que corre sobre varios servicios desplegados con Docker, con colaboración en tiempo real.
**Instalación:** `docker compose` con los manifiestos oficiales (o plan cloud gestionado).
**Casos:** diseñar landings, componentes y sistemas de marca · colaboración self-host.
**Stack:** stack web self-host, Docker — **Modelo/API:** no nativa.
**Elige si:** quieres diseño abierto y soberano — **Evita si:** necesitas generación por IA ([open-design](#-open-design)).
**Combina con:** [design.md](#-designmd) · [plasmic](#-plasmic)
**Repo:** [GitHub](https://github.com/penpot/penpot)

### 🧱 plasmic
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real.
**Por qué destaca:** une edición visual tipo no-code con tus componentes y datos existentes, reduciendo el salto entre diseñador y desarrollador.
**Cómo funciona:** editor visual web que genera/consume componentes React/Next.js de tu repo y los sirve vía SDK o código generado.
**Instalación:** `npm i @plasmicapp/loader-nextjs` (o el loader del framework) y conectar el proyecto.
**Casos:** construir landings/experiencias sobre un stack existente · edición visual de componentes propios.
**Stack:** Node.js, React/Next.js — **Modelo/API:** no específica.
**Elige si:** quieres editar visual sobre tu código — **Evita si:** generas desde texto ([open-design](#-open-design)).
**Combina con:** [tailwindcss](#-tailwindcss) · [ui](#-ui-shadcn)
**Repo:** [GitHub](https://github.com/plasmicapp/plasmic)

### 📐 design.md
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** especificación de formato para describir una identidad visual a agentes de código (tokens YAML + prosa), de modo que el agente herede un sistema de diseño coherente.
**Por qué destaca:** propuesta de Google Labs que aporta no solo los valores sino el "por qué" y cómo aplicarlos, algo que un simple archivo de tokens no transmite.
**Cómo funciona:** archivo Markdown/YAML que el agente lee como contexto persistente, combinando tokens de diseño con guías en prosa.
**Instalación:** crear un `design.md` en el repo siguiendo el formato (sin dependencias).
**Casos:** dar al agente un sistema de diseño persistente · mantener coherencia de marca.
**Stack:** Markdown/YAML — **Modelo/API:** agentes de código.
**Elige si:** quieres consistencia de marca con IA — **Evita si:** no usas agentes para UI.
**Combina con:** [impeccable](#-impeccable) · [skills_emil](#-skills_emil)
**Repo:** [GitHub](https://github.com/google-labs-code/design.md)

### 💎 impeccable
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio.
**Por qué destaca:** ataca de forma deliberada el "AI slop" visual con reglas deterministas, un enfoque diferenciado frente a prompts genéricos de diseño.
**Cómo funciona:** se instala como skill que añade comandos y detectores; itera la UI en el navegador y señala patrones delatores (Inter, gradientes morados, etc.).
**Instalación:** `npx impeccable` (skill para Claude Code y compatibles).
**Casos:** evitar Inter+gradientes morados en todo · iterar diseño en vivo en el navegador.
**Stack:** Node (`npx impeccable`) — **Modelo/API:** Claude Code y compatibles.
**Elige si:** quieres frontends que no parezcan IA — **Evita si:** no generas UI con agentes.
**Combina con:** [taste-skill](#-taste-skill) · [ui-ux-pro-max-skill](#-ui-ux-pro-max-skill) · [design.md](#-designmd)
**Repo:** [GitHub](https://github.com/pbakaus/impeccable)

### 🌬️ tailwindcss
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado.
**Por qué destaca:** se ha vuelto el estándar de facto del estilado web moderno y la base sobre la que se montan casi todas las librerías de componentes actuales.
**Cómo funciona:** motor que escanea tus archivos y genera solo el CSS de las utilidades usadas, optimizando el bundle final.
**Instalación:** `npm i tailwindcss` y configurar el plugin de PostCSS/CLI (o CDN para pruebas).
**Casos:** estilar landings y apps · base de estilos de casi cualquier lib de componentes.
**Stack:** Node.js, CSS — **Modelo/API:** N/A.
**Elige si:** quieres estilar rápido — **Evita si:** prefieres CSS-in-JS.
**Combina con:** [heroui](#-heroui) · [ui](#-ui-shadcn) · [magicui](#-magicui)
**Repo:** [GitHub](https://github.com/tailwindlabs/tailwindcss)

### ✨ magicui
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces modernas con buen acabado desde el inicio.
**Por qué destaca:** prioriza el impacto visual con piezas vistosas listas para usar, popular en landings y portfolios que buscan diferenciarse rápido.
**Cómo funciona:** componentes React/Next.js sobre Tailwind y motion que se copian o instalan vía CLI compatible con shadcn.
**Instalación:** `npx shadcn add` apuntando al registro de Magic UI (o copiar el componente).
**Casos:** landing o dashboard con buen acabado desde el inicio · prototipado vistoso.
**Stack:** Node.js, React/Next.js — **Modelo/API:** N/A.
**Elige si:** priorizas estética y velocidad — **Evita si:** necesitas accesibilidad estricta ([heroui](#-heroui)).
**Combina con:** [tailwindcss](#-tailwindcss) · [motion](#-motion)
**Repo:** [GitHub](https://github.com/magicuidesign/magicui)

### 🦸 heroui
**Etiquetas:** Ejecución 🏠 local-first · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes.
**Por qué destaca:** combina accesibilidad seria, integración MCP para asistentes y soporte de Next.js/React 19, una mezcla poco habitual en kits de UI.
**Cómo funciona:** componentes React construidos sobre React Aria (comportamiento/accesibilidad) y estilados con Tailwind, instalables por módulos.
**Instalación:** `npm i @heroui/react` y configurar el plugin de Tailwind.
**Casos:** dashboards, SaaS o landings consistentes · base accesible.
**Stack:** Node.js, React, Tailwind — **Modelo/API:** tooling MCP/asistentes.
**Elige si:** quieres calidad + accesibilidad — **Evita si:** quieres control copy-paste ([ui](#-ui-shadcn)).
**Combina con:** [tailwindcss](#-tailwindcss) · [swr](#-swr)
**Repo:** [GitHub](https://github.com/heroui-inc/heroui)

### 🧱 ui (shadcn)
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada.
**Por qué destaca:** popularizó el modelo "el código es tuyo": sin capa pesada ni lock-in, se ha vuelto la base de incontables design systems.
**Cómo funciona:** CLI que copia el código fuente de cada componente (Radix + Tailwind) directamente a tu proyecto para que lo edites a voluntad.
**Instalación:** `npx shadcn@latest init` y luego `npx shadcn add <componente>`.
**Casos:** pantallas administrativas o landings sobre tu stack · base de un design system propio.
**Stack:** Node.js, React, Tailwind — **Modelo/API:** N/A.
**Elige si:** quieres dueño del código — **Evita si:** prefieres una lib "llave en mano" ([heroui](#-heroui)).
**Combina con:** [tailwindcss](#-tailwindcss) · [plasmic](#-plasmic)
**Repo:** [GitHub](https://github.com/shadcn-ui/ui)

### 🧯 normalize.css
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme.
**Por qué destaca:** clásico ampliamente usado que, en lugar de borrar estilos, preserva los defaults útiles y corrige solo las inconsistencias.
**Cómo funciona:** un único CSS que ajusta elementos donde los navegadores difieren, sin imponer una estética propia.
**Instalación:** `npm i normalize.css` e importarlo (o enlazar por CDN).
**Casos:** base consistente antes de estilar · igualar rendering cross-browser.
**Stack:** CSS — **Modelo/API:** N/A.
**Elige si:** quieres base CSS uniforme — **Evita si:** ya usas el preflight de Tailwind.
**Combina con:** [tailwindcss](#-tailwindcss)
**Repo:** [GitHub](https://github.com/necolas/normalize.css)

### 🎞️ GSAP
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados.
**Por qué destaca:** referencia veterana del motion web profesional, con rendimiento y precisión difíciles de igualar para animación detallada.
**Cómo funciona:** motor JavaScript que anima propiedades de cualquier objeto/DOM mediante tweens y timelines, con plugins como ScrollTrigger.
**Instalación:** `npm i gsap` (o CDN).
**Casos:** animaciones avanzadas y timelines · efectos scroll y transiciones complejas.
**Stack:** JavaScript — **Modelo/API:** N/A.
**Elige si:** necesitas animación avanzada — **Evita si:** te basta animar componentes React ([motion](#-motion)).
**Combina con:** [three.js](#-threejs) · [motion](#-motion)
**Repo:** [GitHub](https://github.com/greensock/GSAP)

### 🌀 motion
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código.
**Por qué destaca:** su API declarativa hizo accesible la animación en React y es de las más adoptadas del ecosistema.
**Cómo funciona:** componentes `motion.*` y hooks que interpolan props de estado y manejan entradas/salidas y gestos automáticamente.
**Instalación:** `npm i motion` (o `framer-motion`).
**Casos:** animar entradas/salidas de componentes · microinteracciones fáciles.
**Stack:** JavaScript/React — **Modelo/API:** N/A.
**Elige si:** animas en React — **Evita si:** necesitas timelines complejos ([GSAP](#-gsap)).
**Combina con:** [magicui](#-magicui) · [react-three-fiber](#-react-three-fiber)
**Repo:** [GitHub](https://github.com/motiondivision/motion)

### 🔺 three.js
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** motor 3D (WebGL) para renderizar gráficos y escenas interactivas directamente en el navegador.
**Por qué destaca:** es el estándar del 3D web, con un ecosistema enorme de ejemplos, loaders y helpers alrededor.
**Cómo funciona:** abstrae WebGL en escenas, cámaras, luces y mallas, gestionando el bucle de render por ti.
**Instalación:** `npm i three` (o CDN/módulo ES).
**Casos:** escenas 3D, visualizaciones inmersivas · experiencias web interactivas.
**Stack:** JavaScript/WebGL — **Modelo/API:** N/A.
**Elige si:** renderizas 3D en web — **Evita si:** trabajas solo 2D.
**Combina con:** [react-three-fiber](#-react-three-fiber) · [GSAP](#-gsap)
**Repo:** [GitHub](https://github.com/mrdoob/three.js)

### 🔻 react-three-fiber
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos.
**Por qué destaca:** lleva la mentalidad declarativa y componible de React al 3D, integrándose con el resto del ecosistema (estado, hooks, drei).
**Cómo funciona:** reconciliador que traduce el árbol JSX a objetos de three.js y los actualiza con los cambios de estado de React.
**Instalación:** `npm i three @react-three/fiber`.
**Casos:** escenas 3D dentro de apps React · integrar 3D con el ecosistema React.
**Stack:** JavaScript/React — **Modelo/API:** N/A.
**Elige si:** haces 3D en React — **Evita si:** no usas React ([three.js](#-threejs) directo).
**Combina con:** [three.js](#-threejs) · [motion](#-motion)
**Repo:** [GitHub](https://github.com/pmndrs/react-three-fiber)

### 🔄 swr
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano.
**Por qué destaca:** creada por Vercel, ofrece una DX muy pulida para consumir APIs y es referencia junto a React Query.
**Cómo funciona:** hook `useSWR(key, fetcher)` que cachea por clave, revalida en foco/intervalo y deduplica peticiones.
**Instalación:** `npm i swr`.
**Casos:** consumir APIs en frontend con caché y revalidación · datos en tiempo casi real.
**Stack:** JavaScript/React — **Modelo/API:** N/A.
**Elige si:** manejas datos remotos en React — **Evita si:** prefieres otra solución de datos.
**Combina con:** [heroui](#-heroui) · receta [Web app moderna](#-7-web-app-moderna-con-ia)
**Repo:** [GitHub](https://github.com/vercel/swr)

---

## 10. Analítica & Visualización

Product analytics, dashboards y librerías de gráficos.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… |
|---|---|---|---|
| [posthog](#-posthog) | Product analytics + session replay | ⚙️ | Mides uso real y conversión |
| [metabase](#-metabase) | Dashboards/BI sobre tus datos | ⚙️ | Quieres reporting sin SQL pesado |
| [dash](#-dash) | Apps analíticas en Python | 📚 | Montas dashboards en Python |
| [echarts](#-echarts) | Librería de gráficos potente | 📚 | Gráficos ricos embebidos en web |
| [uPlot](#-uplot) | Gráficos de series temporales livianos | 📚 | Necesitas charts rápidos y ligeros |
| [streamlit](#-streamlit) | Apps de datos rápidas en Python | 📚 | Prototipas una UI de datos al vuelo |
| [awesome-dataviz](#-awesome-dataviz) | Directorio de visualización | 📂 | Buscas herramientas de dataviz |

### ⚖️ ¿Cuál elegir? — Plataforma vs. librería

| Repo | Cuándo usarlo | Ventaja clave |
|---|---|---|
| **posthog** | Analítica de producto/eventos | Funnels, replay, autohospedable |
| **metabase** | BI/reporting para negocio | Dashboards sin código |
| **dash / streamlit** | Apps de datos a medida (Python) | Control total del frontend de datos |
| **echarts / uPlot** | Gráficos embebidos en tu web | echarts=potente · uPlot=ligero/rápido |

### 📈 posthog
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite.
**Por qué destaca:** referente open source de analítica de producto, autohospedable y muy adoptado por equipos que quieren evitar el lock-in de herramientas SaaS.
**Cómo funciona:** instrumentas eventos con su SDK (JS/Python/etc.) que se ingieren en su backend, y exploras todo desde su panel web con funnels y grabaciones.
**Instalación:** `docker compose` para self-host, o SDK vía `npm i posthog-js` / `pip install posthog`.
**Casos:** medir conversiones antes/después de cambios · funnels y session replay.
**Stack:** Python/Node, self-host o cloud — **Modelo/API:** complementa apps instrumentadas con agentes.
**Elige si:** quieres entender el uso real — **Evita si:** solo necesitas BI sobre una BD ([metabase](#-metabase)).
**Combina con:** [metabase](#-metabase) · receta [Marketing de agencia](#-6-marketing-de-agencia)
**Repo:** [GitHub](https://github.com/PostHog/posthog)

### 📊 metabase
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL.
**Por qué destaca:** de las plataformas BI open source más populares por su facilidad de uso y su editor visual de consultas accesible para perfiles no técnicos.
**Cómo funciona:** se conecta a tu BD, define preguntas mediante un constructor visual o SQL y las agrupa en dashboards interactivos servidos por web.
**Instalación:** `docker run metabase/metabase`, o JAR ejecutable con Java.
**Casos:** tableros de marketing/ventas · reporting sin escribir SQL.
**Stack:** Java/Clojure, BD, web — **Modelo/API:** N/A.
**Elige si:** quieres BI accesible — **Evita si:** necesitas analítica de eventos ([posthog](#-posthog)).
**Combina con:** [posthog](#-posthog) · [echarts](#-echarts)
**Repo:** [GitHub](https://github.com/metabase/metabase)

### 🧮 dash
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos.
**Por qué destaca:** estándar de facto para dashboards productivos en Python, respaldado por Plotly y muy usado en entornos científicos y empresariales.
**Cómo funciona:** declaras el layout y callbacks en Python sobre un servidor Flask, y renderiza gráficos interactivos con Plotly en el navegador.
**Instalación:** `pip install dash`.
**Casos:** dashboard interno de campañas/telemetría · paneles con Plotly.
**Stack:** Python, Plotly, web — **Modelo/API:** consume resultados de pipelines IA.
**Elige si:** quieres dashboards en Python — **Evita si:** prefieres prototipos ultrarrápidos ([streamlit](#-streamlit)).
**Combina con:** [streamlit](#-streamlit) · [echarts](#-echarts)
**Repo:** [GitHub](https://github.com/plotly/dash)

### 📉 echarts
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos.
**Por qué destaca:** una de las librerías de charts más completas y populares del ecosistema web, con renderizado de alto rendimiento y comunidad muy activa.
**Cómo funciona:** configuras un objeto de opciones en JavaScript que la librería pinta sobre Canvas o SVG, con soporte de mapas, series y animaciones.
**Instalación:** `npm i echarts`, o vía CDN.
**Casos:** gráficos interactivos, mapas y series complejas · reporting embebido en apps web.
**Stack:** JavaScript/TypeScript — **Modelo/API:** N/A.
**Elige si:** necesitas gráficos ricos — **Evita si:** solo series temporales simples ([uPlot](#-uplot)).
**Combina con:** [metabase](#-metabase) · [heroui](#-heroui)
**Repo:** [GitHub](https://github.com/apache/echarts)

### 📈 uPlot
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento.
**Por qué destaca:** célebre por su tamaño minúsculo (pocos KB) y velocidad de renderizado, ideal cuando el peso del bundle y los FPS importan.
**Cómo funciona:** dibuja líneas y áreas directamente sobre Canvas con una API minimalista en JavaScript optimizada para datasets enormes.
**Instalación:** `npm i uplot`, o vía CDN.
**Casos:** dashboards con muchísimos puntos · charts rápidos en frontend.
**Stack:** JavaScript — **Modelo/API:** N/A.
**Elige si:** priorizas velocidad/peso — **Evita si:** necesitas tipos de gráfico variados ([echarts](#-echarts)).
**Combina con:** [swr](#-swr) · receta [Web app moderna](#-7-web-app-moderna-con-ia)
**Repo:** [GitHub](https://github.com/leeoniya/uPlot)

### 📊 streamlit
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS.
**Por qué destaca:** muy popular en la comunidad de data science e IA por convertir un script en una app web interactiva casi al instante.
**Cómo funciona:** ejecuta tu script de arriba abajo en cada interacción y mapea widgets y gráficos a una UI web reactiva servida automáticamente.
**Instalación:** `pip install streamlit`.
**Casos:** prototipo para consultar datos/resultados de un modelo · demos de datos.
**Stack:** Python — **Modelo/API:** frontend ideal para LLMs/pipelines.
**Elige si:** quieres una UI de datos al vuelo — **Evita si:** necesitas una app productiva ([dash](#-dash)).
**Combina con:** [dash](#-dash) · [data-science-ipython-notebooks](#-data-science-ipython-notebooks)
**Repo:** [GitHub](https://github.com/streamlit/streamlit)

### 🗂️ awesome-dataviz
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad.
**Por qué destaca:** punto de partida cómodo de la serie "awesome" para descubrir y comparar opciones de dataviz sin búsquedas dispersas.
**Cómo funciona:** es una lista en Markdown alojada en GitHub, organizada por categorías con enlaces a cada herramienta y recurso.
**Instalación:** no requiere instalación; se consulta en GitHub.
**Casos:** elegir una librería de charts · descubrir recursos de dataviz.
**Stack:** Markdown — **Modelo/API:** N/A.
**Elige si:** buscas opciones de visualización — **Evita si:** ya elegiste tu librería.
**Combina con:** [echarts](#-echarts) · [awesome-bigdata](#-awesome-bigdata)
**Repo:** [GitHub](https://github.com/javierluraschi/awesome-dataviz)

---

## 11. Generación de Imagen & Visión

Motores de difusión, control/condicionamiento, restauración y rostros.

### 🔍 Escaneo rápido

| Repo | Qué es | Ejec. | Elige si… |
|---|---|---|---|
| [ComfyUI](#-comfyui) | Pipelines visuales por nodos | 🏠 | Quieres control fino y modular |
| [stable-diffusion-webui](#-stable-diffusion-webui) | UI web clásica de SD | 🏠 | Quieres el ecosistema y extensiones |
| [Fooocus](#-fooocus) | Generación de imagen sin fricción | 🏠 | Quieres resultados rápidos y simples |
| [InvokeAI](#-invokeai) | Suite profesional de SD | 🏠 | Buscas flujo creativo pulido |
| [diffusers](#-diffusers) | Librería de pipelines de difusión | 🏠 | Programas generación desde Python |
| [ControlNet](#-controlnet) | Control estructural de generación | 🏠 | Guías composición con poses/bordes |
| [sd-webui-controlnet](#-sd-webui-controlnet) | ControlNet para SD WebUI | 🏠 | Ya usas SD WebUI |
| [ComfyUI_IPAdapter_plus](#-comfyui_ipadapter_plus) | Condicionamiento imagen→imagen | 🏠 | Mantienes identidad/estilo en ComfyUI |
| [GFPGAN](#-gfpgan) | Restauración facial | 🏠 | Recuperas rostros degradados |
| [Real-ESRGAN](#-real-esrgan) | Superresolución/upscaling | 🏠 | Reescalas imágenes con calidad |
| [LivePortrait](#-liveportrait) | Anima retratos estáticos | 🏠 | Conviertes una foto en avatar animado |
| [Deep-Live-Cam](#-deep-live-cam) | Face swap en tiempo real | 🏠 | Haces swaps en vivo (uso responsable) |
| [face_recognition](#-face_recognition) | Reconocimiento facial | 🏠 | Detectas/identificas rostros |
| [Open-Generative-AI](#-open-generative-ai) | Hub de +200 modelos imagen/video | 🔀 | Generas video/imagen desde terminal |
| [fluxer](#-fluxer) | Plataforma generativa (audio/video) | 🔀 | Exploras una plataforma generativa nueva |

### ⚖️ ¿Cuál elegir? — Motor de generación de imagen

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **ComfyUI** | Pipelines complejos/repetibles | Control por nodos, muy potente | Quieres simplicidad inmediata |
| **stable-diffusion-webui** | Ecosistema y extensiones | Comunidad enorme, plugins | Prefieres flujo moderno limpio |
| **Fooocus** | Resultados rápidos sin tuning | Mínima fricción técnica | Necesitas control fino |
| **InvokeAI** | Trabajo creativo profesional | Flujo pulido y unificado | Solo quieres una prueba puntual |
| **diffusers** | Generación desde código | Estándar reutilizable (HF) | Quieres una UI lista |

### ⚖️ ¿Cuál elegir? — Control y restauración

| Repo | Foco | Ventaja clave |
|---|---|---|
| **ControlNet / sd-webui-controlnet** | Control estructural (pose/bordes) | Composición precisa |
| **ComfyUI_IPAdapter_plus** | Referencia de estilo/identidad | Consistencia visual sin reentrenar |
| **GFPGAN** | Restaurar rostros | Recupera caras degradadas |
| **Real-ESRGAN** | Upscaling general | Reescala con detalle |

### 🧠 ComfyUI
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** motor local modular para crear pipelines visuales de generación con IA mediante un grafo de nodos, donde cada paso (carga de modelo, sampling, postproceso) es un bloque conectable y reutilizable.
**Por qué destaca:** es la referencia para flujos de difusión avanzados y reproducibles, con una comunidad enorme y un ecosistema de nodos/extensiones muy activo.
**Cómo funciona:** ejecuta modelos de difusión (Stable Diffusion, SDXL, Flux) sobre PyTorch+GPU, encadenando nodos en un grafo visual servido desde una interfaz web local.
**Instalación:** `git clone` del repo y arranque con `python main.py` (o paquete portable en Windows); requiere descargar checkpoints aparte.
**Casos:** pipeline para generar/transformar/exportar imágenes de campaña · composición fina y repetible.
**Stack:** Python, GPU, modelos locales — **Modelo/API:** local-first (difusión).
**Elige si:** quieres control total — **Evita si:** buscas simplicidad ([Fooocus](#-fooocus)).
**Combina con:** [ComfyUI_IPAdapter_plus](#-comfyui_ipadapter_plus) · [Real-ESRGAN](#-real-esrgan) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/comfyanonymous/ComfyUI)

### 🖼️ stable-diffusion-webui
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🔴 pesado
**Qué es:** interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador.
**Por qué destaca:** fue la UI que popularizó SD y mantiene una de las comunidades y catálogos de plugins más grandes del ecosistema.
**Cómo funciona:** levanta un servidor Gradio que orquesta modelos de difusión sobre PyTorch+GPU, con pestañas y scripts para cada modo de generación.
**Instalación:** `git clone` y ejecutar `webui-user.bat` (Windows) o `webui.sh` (Linux/Mac); el script crea el entorno e instala dependencias automáticamente.
**Casos:** probar estilos rápido desde una UI · usar el enorme ecosistema de extensiones.
**Stack:** Python, GPU, modelos locales — **Modelo/API:** local-first (difusión).
**Elige si:** quieres extensiones y comunidad — **Evita si:** prefieres flujo moderno/limpio ([InvokeAI](#-invokeai)).
**Combina con:** [sd-webui-controlnet](#-sd-webui-controlnet)
**Repo:** [GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

### 🎨 Fooocus
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes.
**Por qué destaca:** es la opción más sencilla para empezar con difusión local, muy valorada por quienes quieren calidad sin aprender ajustes finos.
**Cómo funciona:** corre modelos de difusión SDXL sobre PyTorch+GPU optimizando prompts y sampling de forma automática, con una UI web ligera.
**Instalación:** descargar el paquete portable (un clic, descomprimir y ejecutar `run.bat` en Windows) o `git clone` con su script de arranque.
**Casos:** artes de campaña sin montar pipeline · iteración rápida diaria.
**Stack:** Python, GPU, modelos locales — **Modelo/API:** local-first (difusión).
**Elige si:** quieres resultados ya — **Evita si:** necesitas control fino ([ComfyUI](#-comfyui)).
**Combina con:** [Real-ESRGAN](#-real-esrgan)
**Repo:** [GitHub](https://github.com/lllyasviel/Fooocus)

### 🖌️ InvokeAI
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🔴 pesado
**Qué es:** suite profesional y unificada para Stable Diffusion que combina una UI pulida con canvas, capas, inpainting y gestión de modelos y workflows.
**Por qué destaca:** ofrece la experiencia creativa más estable y profesional del ecosistema SD, con respaldo comercial y un canvas potente.
**Cómo funciona:** integra modelos de difusión sobre PyTorch+GPU en una aplicación con backend propio y editor visual tipo lienzo para iterar sobre la imagen.
**Instalación:** instalador automático multiplataforma (launcher) o `pip install invokeai`; arranca un servidor web local tras configurar los modelos.
**Casos:** trabajo creativo serio con SD · canvas e inpainting profesional.
**Stack:** Python, GPU, modelos locales — **Modelo/API:** local-first (difusión).
**Elige si:** trabajas creatividad profesional — **Evita si:** solo haces una prueba puntual ([Fooocus](#-fooocus)).
**Combina con:** [diffusers](#-diffusers) · [ControlNet](#-controlnet)
**Repo:** [GitHub](https://github.com/invoke-ai/InvokeAI)

### 🤗 diffusers
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🔴 pesado
**Qué es:** librería de Hugging Face para construir y ejecutar pipelines de modelos de difusión (imagen, video, audio) desde código, con APIs estandarizadas para schedulers y modelos.
**Por qué destaca:** es el estándar de facto para usar difusión programáticamente, mantenido por Hugging Face y con soporte inmediato para los modelos más nuevos.
**Cómo funciona:** carga modelos open-source (Stable Diffusion, SDXL, Flux) desde el Hub y ejecuta su inferencia sobre PyTorch+GPU mediante clases `Pipeline` componibles.
**Instalación:** `pip install diffusers transformers accelerate`; los pesos se descargan automáticamente desde el Hub al instanciar un pipeline.
**Casos:** generación/transformación visual desde scripts propios · base reutilizable.
**Stack:** Python, PyTorch — **Modelo/API:** modelos open-source (local/self-host).
**Elige si:** programas generación — **Evita si:** quieres una UI lista ([Fooocus](#-fooocus)).
**Combina con:** [ControlNet](#-controlnet) · [cosmos](#-cosmos)
**Repo:** [GitHub](https://github.com/huggingface/diffusers)

### 🧭 ControlNet
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** método y modelos para condicionar la generación text-to-image con señales externas como poses, bordes, profundidad o mapas de segmentación, fijando la estructura del resultado.
**Por qué destaca:** revolucionó el control de la difusión al permitir guiar la composición sin perder calidad, y es trabajo de referencia ampliamente citado y adoptado.
**Cómo funciona:** añade una red paralela entrenable a un modelo de difusión sobre PyTorch+GPU que inyecta la condición (mapa de control) en cada paso de denoising.
**Instalación:** `git clone` del repo y entorno con sus dependencias; descargar los pesos de ControlNet además del modelo base de Stable Diffusion.
**Casos:** guiar creativos con siluetas/poses/layouts · control compositivo preciso.
**Stack:** Python, difusión, GPU — **Modelo/API:** local (Stable Diffusion).
**Elige si:** necesitas control estructural — **Evita si:** ya trabajas en SD WebUI ([sd-webui-controlnet](#-sd-webui-controlnet)).
**Combina con:** [diffusers](#-diffusers) · [ComfyUI](#-comfyui)
**Repo:** [GitHub](https://github.com/lllyasviel/ControlNet)

### 🧩 sd-webui-controlnet
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI, con preprocesadores para poses, bordes, profundidad y más.
**Por qué destaca:** es la forma estándar de usar ControlNet dentro del ecosistema AUTOMATIC1111, muy popular entre quienes ya trabajan en esa UI.
**Cómo funciona:** se instala como extensión de la WebUI y añade un panel que aplica modelos ControlNet sobre la difusión PyTorch+GPU del propio WebUI.
**Instalación:** desde la pestaña Extensions de la WebUI (instalar por URL del repo) o `git clone` en `extensions/`; descargar luego los modelos ControlNet.
**Casos:** afinar creativos en SD WebUI con poses/sketches/mapas.
**Stack:** Python, SD WebUI, modelos ControlNet — **Modelo/API:** local (difusión).
**Elige si:** ya usas SD WebUI — **Evita si:** trabajas en ComfyUI o por código.
**Combina con:** [stable-diffusion-webui](#-stable-diffusion-webui) · [ControlNet](#-controlnet)
**Repo:** [GitHub](https://github.com/Mikubill/sd-webui-controlnet)

### 🪞 ComfyUI_IPAdapter_plus
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una imagen de referencia para transferir estilo o identidad.
**Por qué destaca:** es la implementación de referencia de IPAdapter en ComfyUI y un nodo casi imprescindible para mantener coherencia visual entre piezas.
**Cómo funciona:** inyecta embeddings de una imagen de referencia (vía CLIP vision) en el modelo de difusión sobre PyTorch+GPU durante el sampling de ComfyUI.
**Instalación:** clonar el repo en `custom_nodes/` de ComfyUI (o instalarlo desde ComfyUI Manager) y colocar los modelos IPAdapter/CLIP vision.
**Casos:** mantener identidad/estilo entre piezas de una campaña · control por referencia visual.
**Stack:** Python, ComfyUI — **Modelo/API:** local (difusión).
**Elige si:** trabajas en ComfyUI y necesitas consistencia — **Evita si:** no usas ComfyUI.
**Combina con:** [ComfyUI](#-comfyui)
**Repo:** [GitHub](https://github.com/cubiq/ComfyUI_IPAdapter_plus)

### 🙂 GFPGAN
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** algoritmo de restauración facial que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados.
**Por qué destaca:** resuelve muy bien un problema concreto y es una utilidad ampliamente reutilizada como paso de postproceso en pipelines de imagen.
**Cómo funciona:** aplica una red GAN sobre PyTorch (GPU opcional) que detecta el rostro y regenera detalle realista preservando la identidad.
**Instalación:** `pip install gfpgan` o `git clone` con sus dependencias; los pesos del modelo se descargan en el primer uso.
**Casos:** mejorar retratos/frames antes de reutilizarlos · recuperar rostros degradados.
**Stack:** Python, PyTorch, GPU opcional — **Modelo/API:** modelos locales.
**Elige si:** restauras rostros — **Evita si:** necesitas upscaling general ([Real-ESRGAN](#-real-esrgan)).
**Combina con:** [Real-ESRGAN](#-real-esrgan)
**Repo:** [GitHub](https://github.com/TencentARC/GFPGAN)

### 🔍 Real-ESRGAN
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** herramienta de superresolución y restauración para imágenes reales que reescala y limpia material de baja calidad sin rehacerlo.
**Por qué destaca:** es uno de los upscalers open-source más usados y citados, con resultados sólidos en fotos y arte, ampliamente integrado en otras UIs.
**Cómo funciona:** emplea una red GAN práctica sobre PyTorch+GPU entrenada con degradaciones sintéticas para inferir detalle al ampliar la imagen.
**Instalación:** `pip install realesrgan` o ejecutable portable; los modelos preentrenados se descargan al primer uso.
**Casos:** reescalar creativos antiguos · mejorar detalle de assets comprimidos.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** modelos locales.
**Elige si:** reescalas imágenes — **Evita si:** solo necesitas arreglar rostros ([GFPGAN](#-gfpgan)).
**Combina con:** [GFPGAN](#-gfpgan) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/xinntao/Real-ESRGAN)

### 🧑 LivePortrait
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen.
**Por qué destaca:** ofrece animación facial rápida y controlable (con retoque de ojos y boca), muy popular para crear avatares y presentadores a partir de una foto.
**Cómo funciona:** usa un modelo de keypoints/warping implícito sobre PyTorch+GPU que deforma la cara de origen siguiendo el movimiento del conductor.
**Instalación:** `git clone`, crear entorno y `pip install -r requirements.txt`; descargar los pesos preentrenados indicados en el repo.
**Casos:** convertir una foto en avatar/recurso animado · presentadores virtuales.
**Stack:** Python, GPU — **Modelo/API:** modelos locales.
**Elige si:** animas retratos — **Evita si:** necesitas swap en vivo ([Deep-Live-Cam](#-deep-live-cam)).
**Combina con:** [moviepy](#-moviepy)
**Repo:** [GitHub](https://github.com/KwaiVGI/LivePortrait)

### 🎭 Deep-Live-Cam
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video con salvaguardas de uso.
**Por qué destaca:** es de los proyectos de swap en vivo más conocidos por su facilidad de uso de un clic; incluye chequeos contra contenido inapropiado.
**Cómo funciona:** combina detección y reenactment facial sobre PyTorch+GPU para reemplazar el rostro fotograma a fotograma en flujo en directo.
**Instalación:** `git clone`, instalar dependencias y proveedores de GPU (p. ej. ONNX Runtime); descargar los modelos de swap indicados.
**Casos:** animar personajes · contenido creativo con rostro (uso responsable y consentido).
**Stack:** Python, GPU — **Modelo/API:** modelos locales.
**Elige si:** necesitas swap en vivo legítimo — **Evita si:** no puedes garantizar uso ético/consentimiento.
**Combina con:** [face_recognition](#-face_recognition)
**Repo:** [GitHub](https://github.com/hacksider/Deep-Live-Cam)

### 👤 face_recognition
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería de Python sencilla para detección y reconocimiento facial, con una API de alto nivel para localizar, comparar e identificar caras en imágenes.
**Por qué destaca:** es de las librerías de reconocimiento facial más populares y accesibles, ideal para prototipos por su API mínima.
**Cómo funciona:** envuelve los modelos de dlib (detección HOG/CNN y embeddings faciales) para comparar rostros por distancia entre vectores.
**Instalación:** `pip install face_recognition` (requiere dlib y, en Windows, herramientas de compilación de C++/CMake).
**Casos:** detectar/identificar rostros en imágenes · etiquetado automático.
**Stack:** Python, dlib — **Modelo/API:** modelos locales.
**Elige si:** necesitas reconocimiento facial básico — **Evita si:** buscas restauración/animación.
**Combina con:** [Deep-Live-Cam](#-deep-live-cam)
**Repo:** [GitHub](https://github.com/ageitgey/face_recognition)

### 🎬 Open-Generative-AI
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes.
**Por qué destaca:** ofrece un hub unificado sin filtros restrictivos ni suscripción, pensado para conectar la generación visual a flujos de agentes.
**Cómo funciona:** orquesta modelos de difusión y video vía la API en nube MuAPI o sobre GPUs locales, exponiéndolos tras una interfaz de línea de comandos.
**Instalación:** `git clone` del repo e instalar dependencias de Python/Node.js; configurar la clave de MuAPI o el backend de GPU local.
**Casos:** generar un clip promocional desde terminal · activos visuales rápidos para agentes.
**Stack:** Python, Node.js — **Modelo/API:** MuAPI (render en nube) o GPUs locales.
**Elige si:** quieres un hub de generación — **Evita si:** ya tienes tu pipeline local ([ComfyUI](#-comfyui)).
**Combina con:** [remotion](#-remotion) · receta [Marketing de agencia](#-6-marketing-de-agencia)
**Repo:** [GitHub](https://github.com/Anil-matcha/Open-Generative-AI)

### 🌐 fluxer
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop; su API y self-host aún están en finalización.
**Por qué destaca:** apuesta por audio/video con mejoras continuas, aunque es un proyecto poco maduro y con documentación e instalación todavía limitadas (honestamente, oscuro).
**Cómo funciona:** cliente en TypeScript/web que orquesta múltiples modelos generativos a través de servicios, con backend self-host aún no estabilizado.
**Instalación:** descargar el cliente Canary (web/desktop) o `git clone` del repo y compilar con el toolchain de Node/TS; self-host sujeto a cambios.
**Casos:** explorar una plataforma generativa emergente · cliente Canary web/desktop.
**Stack:** web/TS — **Modelo/API:** múltiples.
**Elige si:** quieres probar algo nuevo — **Evita si:** necesitas estabilidad de producción (API aún en finalización).
**Combina con:** [Open-Generative-AI](#-open-generative-ai)
**Repo:** [GitHub](https://github.com/fluxerapp/fluxer)

---

## 12. Audio, Voz & Video

Transcripción (STT), síntesis de voz (TTS) y edición/render de video.

### 🔍 Escaneo rápido

| Repo | Qué es | Tipo | Elige si… |
|---|---|---|---|
| [whisper](#-whisper) | STT estándar multilingüe | STT | Quieres la referencia de transcripción |
| [faster-whisper](#-faster-whisper) | Whisper más rápido y ligero | STT | Te importa el rendimiento |
| [whisperX](#-whisperx) | Whisper + alineación y diarización | STT | Necesitas subtítulos con timings finos |
| [supertonic](#-supertonic) | TTS ultrarrápido local (WebGPU) | TTS | Quieres voz local de baja latencia |
| [VoxCPM](#-voxcpm) | TTS de alta fidelidad sin tokenizador | TTS | Buscas voz muy fluida/clonación |
| [TTS](#-tts) | Toolkit TTS multilingüe (Coqui) | TTS | Quieres flexibilidad y clonación |
| [OmniVoice-Studio](#-omnivoice-studio) | Suite de voz/dubbing local | TTS/STT | Dictado, clonación y doblaje en local |
| [lossless-cut](#-lossless-cut) | Corte de video sin recomprimir | Video | Cortas clips rápido sin perder calidad |
| [moviepy](#-moviepy) | Edición de video programática | Video | Ensamblas video desde scripts |
| [remotion](#-remotion) | Video por código (React) | Video | Generas variantes de video a escala |
| [videofy_minimal](#-videofy_minimal) | Texto → video corto local | Video | Conviertes contenido en reels simple |
| [OpenCut](#-opencut) | Editor de video open-source | Video | Quieres un editor libre tipo CapCut |
| [openscreen](#-openscreen) | Grabación de pantalla | Video | Grabas screencasts (archivado) |
| [Youtube2Webpage](#-youtube2webpage) | Video de YouTube → página | Video | Conviertes un video en artículo |
| [hyperframes](#-hyperframes) | Framework de animación por frames | Video | Generas animaciones programáticas |

### ⚖️ ¿Cuál elegir? — Transcripción (STT)

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **whisper** | Referencia general de STT | Robustez a ruido/acentos | Necesitas máxima velocidad |
| **faster-whisper** | Lotes/latencia importan | Mucho más eficiente (CTranslate2) | Ya te basta whisper |
| **whisperX** | Subtítulos finos/diarización | Alineación precisa + speakers | Solo quieres texto plano |

### ⚖️ ¿Cuál elegir? — Síntesis de voz (TTS)

| Repo | Cuándo usarlo | Ventaja clave |
|---|---|---|
| **supertonic** | Voz en tiempo real local | Baja latencia (WebGPU) |
| **VoxCPM** | Máxima fluidez/clonación | Sin tokenizador tradicional |
| **TTS (Coqui)** | Flexibilidad y multi-idioma | Toolkit completo y reutilizable |
| **OmniVoice-Studio** | Suite todo-en-uno (646 idiomas) | Dictado + clonación + dubbing |

### 📝 whisper
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo.
**Por qué destaca:** es la referencia de facto del STT abierto, base de innumerables forks y servicios de transcripción.
**Cómo funciona:** red Transformer encoder-decoder entrenada con audio supervisado; corre sobre PyTorch y procesa el audio en ventanas de 30s; la CLI `whisper` genera SRT/VTT.
**Instalación:** `pip install -U openai-whisper` (requiere ffmpeg en el sistema).
**Casos:** `whisper grabacion.mp3 --model medium` para SRT con timestamps · subtitulado automático.
**Stack:** Python 3.9+, PyTorch — **Modelo/API:** local (modelos tiny→large), sin API de pago.
**Elige si:** quieres la referencia — **Evita si:** necesitas más velocidad ([faster-whisper](#-faster-whisper)).
**Combina con:** [whisperX](#-whisperx) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/openai/whisper)

### ⚡ faster-whisper
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión.
**Por qué destaca:** es la versión preferida en producción por su relación velocidad/calidad; muy adoptada en pipelines y servidores de transcripción.
**Cómo funciona:** ejecuta los mismos modelos Whisper convertidos al runtime optimizado CTranslate2, con cuantización int8/float16 que acelera CPU y GPU.
**Instalación:** `pip install faster-whisper` (necesita ffmpeg).
**Casos:** procesar lotes de audio/video con menos latencia · transcripción en producción.
**Stack:** Python, CTranslate2 — **Modelo/API:** modelos Whisper locales.
**Elige si:** el rendimiento importa — **Evita si:** necesitas alineación/diarización ([whisperX](#-whisperx)).
**Combina con:** [whisperX](#-whisperx)
**Repo:** [GitHub](https://github.com/SYSTRAN/faster-whisper)

### 🎯 whisperX
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional.
**Por qué destaca:** es la opción de referencia cuando los timings palabra a palabra y el "quién habla" importan, muy usada para subtítulos de reels y entrevistas.
**Cómo funciona:** combina faster-whisper para la transcripción, modelos wav2vec2 para forzar la alineación y pyannote para la diarización.
**Instalación:** `pip install whisperx` (requiere PyTorch y, para diarización, un token de Hugging Face).
**Casos:** subtítulos bien ajustados para reels/entrevistas · separar hablantes.
**Stack:** Python, modelos Whisper — **Modelo/API:** local.
**Elige si:** necesitas subtítulos precisos — **Evita si:** te basta texto plano ([whisper](#-whisper)).
**Combina con:** [whisper](#-whisper) · [moviepy](#-moviepy) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/m-bain/whisperX)

### 🔊 supertonic
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU.
**Por qué destaca:** logra latencia muy baja con privacidad total al no depender de la nube, atractivo para voz en tiempo real.
**Cómo funciona:** ejecuta modelos ONNX/PyTorch acelerados por WebGPU desde el navegador o por Rust/Python en escritorio.
**Instalación:** clonar el repo y seguir el ejemplo Node/Python, o probar la demo WebGPU (no hay paquete único oficial).
**Casos:** respuesta por voz en tiempo real · locuciones de anuncios local.
**Stack:** Python, Rust (ONNX/PyTorch), Node.js — **Modelo/API:** modelos propios de Hugging Face, gratis.
**Elige si:** quieres voz local en tiempo real — **Evita si:** priorizas clonación de máxima fidelidad ([VoxCPM](#-voxcpm)).
**Combina con:** [whisperX](#-whisperx) · [moviepy](#-moviepy)
**Repo:** [GitHub](https://github.com/supertone-inc/supertonic)

### 🗣️ VoxCPM
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y fluidez muy naturales, con clonación de voz.
**Por qué destaca:** ofrece una naturalidad sobresaliente y clonación fiel a partir de pocos segundos de audio, dentro del ecosistema CPM de OpenBMB.
**Cómo funciona:** modelo de difusión/autorregresivo sobre PyTorch que genera el habla en un espacio continuo en lugar de tokens discretos; requiere GPU.
**Instalación:** `pip install voxcpm` (o desde el repo) con PyTorch y GPU recomendada.
**Casos:** clonación de voz de alta calidad · locuciones muy naturales.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** modelos propios locales.
**Elige si:** quieres voz muy natural/clonada — **Evita si:** priorizas latencia mínima ([supertonic](#-supertonic)).
**Combina con:** [TTS](#-tts)
**Repo:** [GitHub](https://github.com/OpenBMB/VoxCPM)

### 🎙️ TTS
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz.
**Por qué destaca:** es uno de los kits TTS abiertos más completos y reutilizados; aunque Coqui cerró, su código y modelos (XTTS) siguen siendo referencia comunitaria.
**Cómo funciona:** librería Python que carga modelos (Tacotron, VITS, XTTS) sobre PyTorch y expone CLI y API para generar o clonar voz.
**Instalación:** `pip install TTS` (o `coqui-tts`, el fork mantenido).
**Casos:** locuciones automáticas para anuncios/demos · clonación de voz.
**Stack:** Python, modelos descargables — **Modelo/API:** local.
**Elige si:** quieres flexibilidad — **Evita si:** necesitas tiempo real puro ([supertonic](#-supertonic)).
**Combina con:** [whisperX](#-whisperx) · [moviepy](#-moviepy)
**Repo:** [GitHub](https://github.com/coqui-ai/TTS)

### 🎚️ OmniVoice-Studio
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** suite de voz de escritorio open-source planteada como alternativa a ElevenLabs, con dictado en tiempo real, clonación zero-shot y doblaje de video en hasta 646 idiomas, todo local.
**Por qué destaca:** reúne dictado, clonación y dubbing en una sola app sin claves de API ni nube, algo poco común; es un proyecto pequeño y poco conocido, valídalo antes de depender de él.
**Cómo funciona:** envuelve modelos locales de STT y TTS en una interfaz de escritorio Python que orquesta transcripción, síntesis y reemplazo de audio en video.
**Instalación:** clonar el repo e instalar dependencias Python según el README (sin paquete publicado).
**Casos:** dictado de escritorio · doblar videos · clonar voz sin API keys.
**Stack:** desktop/Python — **Modelo/API:** modelos locales.
**Elige si:** quieres suite de voz completa local — **Evita si:** solo necesitas TTS simple ([TTS](#-tts)).
**Combina con:** [whisperX](#-whisperx)
**Repo:** [GitHub](https://github.com/debpalash/OmniVoice-Studio)

### ✂️ lossless-cut
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la calidad original.
**Por qué destaca:** es la herramienta de referencia para cortes sin pérdida, muy popular por su rapidez y por procesar archivos enormes al instante.
**Cómo funciona:** GUI Electron sobre ffmpeg que opera por copia de stream (sin recompresión), por lo que los cortes son casi instantáneos.
**Instalación:** descargar el binario para Windows/macOS/Linux desde releases (también vía Microsoft Store/Flatpak).
**Casos:** preparar clips para reels/anuncios sin editor pesado · cortes rápidos sin pérdida.
**Stack:** Node.js/Electron, ffmpeg — **Modelo/API:** N/A.
**Elige si:** cortas material rápido — **Evita si:** necesitas edición compositiva ([moviepy](#-moviepy)).
**Combina con:** [moviepy](#-moviepy) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/mifi/lossless-cut)

### 🎬 moviepy
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería Python para edición de video programática: cortar, concatenar, superponer texto, subtítulos y audio, y exportar el resultado.
**Por qué destaca:** es la librería de edición de video más usada en Python, ideal para pipelines reproducibles y generación automatizada de clips.
**Cómo funciona:** envuelve ffmpeg y NumPy/Pillow para manipular clips como objetos y renderizar el montaje final por código.
**Instalación:** `pip install moviepy` (incluye ffmpeg vía imageio-ffmpeg).
**Casos:** montar videos cortos desde imágenes, subtítulos y voz · overlays y texto por script.
**Stack:** Python, ffmpeg — **Modelo/API:** capa de ensamblaje final.
**Elige si:** ensamblas video por código — **Evita si:** prefieres React/programático web ([remotion](#-remotion)).
**Combina con:** [whisperX](#-whisperx) · [TTS](#-tts) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/Zulko/moviepy)

### ⚛️ remotion
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4.
**Por qué destaca:** muy popular para generar video a escala y plantillas parametrizadas (uno de los proyectos de video-por-código más activos del ecosistema JS).
**Cómo funciona:** renderiza componentes React frame a frame con un navegador headless y los une con ffmpeg; permite props para crear miles de variantes.
**Instalación:** `npm create video` (o `npm i remotion @remotion/cli`).
**Casos:** generar variantes de video a escala · plantillas de video programáticas.
**Stack:** Node.js, React — **Modelo/API:** N/A.
**Elige si:** generas video a escala con React — **Evita si:** trabajas en Python ([moviepy](#-moviepy)).
**Combina con:** [Open-Generative-AI](#-open-generative-ai) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/remotion-dev/remotion)

### 📲 videofy_minimal
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo.
**Por qué destaca:** prioriza la simplicidad para pasar de texto a reel rápido; es un proyecto pequeño y experimental, conviene revisar su estado antes de usarlo en serio.
**Cómo funciona:** combina TTS/STT y un montador de video local para sincronizar narración, texto y fondos en un clip corto.
**Instalación:** clonar el repo e instalar dependencias Python/Node según el README (sin paquete publicado).
**Casos:** transformar noticias/contenido en reels · video corto rápido sin pipeline complejo.
**Stack:** Python/Node — **Modelo/API:** local + TTS/STT.
**Elige si:** quieres reels simples ya — **Evita si:** necesitas variantes programáticas ([remotion](#-remotion)).
**Combina con:** [whisper](#-whisper) · [supertonic](#-supertonic)
**Repo:** [GitHub](https://github.com/schibsted/videofy_minimal)

### 🎞️ OpenCut
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** editor de video open-source con UI moderna, planteado como alternativa libre tipo CapCut, usable en web o escritorio.
**Por qué destaca:** propuesta abierta y sin ataduras de plataforma que ha ganado tracción rápida como alternativa libre a editores propietarios.
**Cómo funciona:** app web en TypeScript/Next.js que edita en el navegador y procesa video con ffmpeg (WebAssembly/local).
**Instalación:** usar la versión web o clonar el repo y `npm install && npm run dev`.
**Casos:** edición de video con UI libre · cortes y montajes sin software propietario.
**Stack:** web/TS — **Modelo/API:** N/A.
**Elige si:** quieres un editor libre con UI — **Evita si:** prefieres edición por código ([moviepy](#-moviepy)).
**Combina con:** [lossless-cut](#-lossless-cut)
**Repo:** [GitHub](https://github.com/OpenCut-app/OpenCut)

### 🖥️ openscreen
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** herramienta ligera de grabación de pantalla para screencasts y demos; el proyecto original está archivado y continúa mediante un fork comunitario.
**Por qué destaca:** opción sencilla y abierta para capturar pantalla, aunque su estado archivado obliga a revisar el fork mantenido antes de adoptarla.
**Cómo funciona:** app web en TypeScript que usa las APIs de captura del navegador para grabar pantalla y exportar el video.
**Instalación:** clonar el repo (o el fork) y `npm install && npm run dev`.
**Casos:** grabar screencasts/demos · capturar tutoriales.
**Stack:** web/TS — **Modelo/API:** N/A.
**Elige si:** necesitas screencast simple — **Evita si:** quieres algo mantenido (está archivado).
**Combina con:** [OpenCut](#-opencut)
**Repo:** [GitHub](https://github.com/lacymorrow/openscreen)

### 📄 Youtube2Webpage
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado.
**Por qué destaca:** automatiza el paso de charla a artículo combinando texto e imágenes; es una utilidad de nicho y poco conocida, pero efectiva para su propósito.
**Cómo funciona:** usa yt-dlp para descargar video y subtítulos y ffmpeg para extraer fotogramas, ensamblando todo en una página HTML.
**Instalación:** clonar el repo y ejecutar el script Perl con yt-dlp y ffmpeg instalados.
**Casos:** convertir una charla en artículo legible · documentar video como texto+imágenes.
**Stack:** Perl, yt-dlp — **Modelo/API:** N/A.
**Elige si:** quieres video → artículo — **Evita si:** necesitas edición de video.
**Combina con:** [whisper](#-whisper)
**Repo:** [GitHub](https://github.com/obra/Youtube2Webpage)

### 🎞️ hyperframes
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework npm para generar animaciones frame a frame de forma programática desde código.
**Por qué destaca:** da control fino sobre cada fotograma de la animación; es un proyecto pequeño y poco difundido, conviene comprobar su madurez antes de apostar por él.
**Cómo funciona:** librería TypeScript/Node que renderiza secuencias de frames programáticamente y los exporta para componerlos en video.
**Instalación:** `npm i hyperframes` (o clonar el repo).
**Casos:** animaciones generadas por código · secuencias frame a frame.
**Stack:** Node.js/TypeScript — **Modelo/API:** N/A.
**Elige si:** generas animación por frames — **Evita si:** prefieres video en React ([remotion](#-remotion)).
**Combina con:** [remotion](#-remotion)
**Repo:** [GitHub](https://github.com/heygen-com/hyperframes)

---

## 13. Documentos & Presentaciones

Conversión de formatos, generación de slides y herramientas de PDF.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… |
|---|---|---|---|
| [markitdown](#-markitdown) | Cualquier formato → Markdown para LLM | 📚 | Ingestas PDF/Word/Excel para IA |
| [ppt-master](#-ppt-master) | Texto → PowerPoint editable | 🧩 | Generas presentaciones PPTX rápido |
| [pdfcraft](#-pdfcraft) | Herramientas PDF en el navegador | 🖥️ | Editas/manipulas PDF privado y local |
| [reveal.js](#-revealjs) | Slides en HTML | 📚 | Quieres presentaciones web por código |

### 📝 markitdown
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman.
**Por qué destaca:** proyecto oficial de Microsoft muy adoptado como puerta de entrada para pipelines RAG, por su salida ordenada y su catálogo de plugins.
**Cómo funciona:** detecta el tipo de archivo y aplica el extractor adecuado (parsers de Office, OCR por visión, Whisper para audio), normalizando todo a Markdown estructurado.
**Instalación:** `pip install markitdown` (o `pip install 'markitdown[all]'` para todos los formatos).
**Casos:** convertir carpetas de informes (XLSX/PDF) a `.md` · ingesta de datos para IA.
**Stack:** Python 3.8+ — **Modelo/API:** opcional (visión para OCR, Whisper para audio).
**Elige si:** alimentas LLMs con documentos — **Evita si:** ya tienes el texto limpio.
**Combina con:** [ppt-master](#-ppt-master) · [open-notebook](#-open-notebook) · receta [Docs → presentaciones](#-9-documentos--presentaciones)
**Repo:** [GitHub](https://github.com/microsoft/markitdown)

### 📊 ppt-master
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil
**Qué es:** generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas para abrir y ajustar en Office.
**Por qué destaca:** entrega un PPTX realmente editable en lugar de un PDF plano, ahorrando el tedio de maquetar slides desde cero.
**Cómo funciona:** un LLM estructura el contenido en secciones y diapositivas, y luego python-pptx genera el archivo .pptx con sus formas, textos y diseño.
**Instalación:** `git clone` del repo y `pip install -r requirements.txt`; requiere clave de API del modelo.
**Casos:** pasar un informe Markdown a un borrador de slides corporativos en segundos.
**Stack:** Python, python-pptx — **Modelo/API:** Claude 3.5 Sonnet o GPT-4o para estructurar.
**Elige si:** quieres PPTX editable — **Evita si:** prefieres slides web ([reveal.js](#-revealjs)).
**Combina con:** [markitdown](#-markitdown) · receta [Docs → presentaciones](#-9-documentos--presentaciones)
**Repo:** [GitHub](https://github.com/hugohe3/ppt-master)

### 📄 pdfcraft
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada.
**Por qué destaca:** todo el procesamiento ocurre en tu navegador, así que los documentos nunca salen de tu equipo ni dependen de un servicio de pago.
**Cómo funciona:** carga el PDF en el cliente y manipula sus páginas con librerías JS de PDF en el propio navegador, sin subir nada a la nube.
**Instalación:** abrir la web en el navegador, o `npm install` y ejecutar en local desde el repo.
**Casos:** combinar/dividir/convertir PDF sin subirlos a la nube · manipulación local.
**Stack:** web/TS — **Modelo/API:** N/A.
**Elige si:** manipulas PDFs con privacidad — **Evita si:** necesitas conversión a Markdown para IA ([markitdown](#-markitdown)).
**Combina con:** [markitdown](#-markitdown)
**Repo:** [GitHub](https://github.com/PDFCraftTool/pdfcraft)

### 🖥️ reveal.js
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados.
**Por qué destaca:** estándar de facto para slides como código, muy popular y respaldado por una comunidad amplia y años de uso en producción.
**Cómo funciona:** defines las diapositivas como elementos HTML anidados y la librería JS las renderiza en el navegador con navegación, animaciones y exportación a PDF.
**Instalación:** `npm install reveal.js` (o clonar el repo y abrir `index.html` en el navegador).
**Casos:** slides web versionables como código · presentaciones interactivas en el navegador.
**Stack:** JavaScript/HTML — **Modelo/API:** N/A.
**Elige si:** quieres slides web — **Evita si:** necesitas PPTX editable en Office ([ppt-master](#-ppt-master)).
**Combina con:** [markitdown](#-markitdown)
**Repo:** [GitHub](https://github.com/hakimel/reveal.js)

---

<!-- BL_ALEXANDRIA_AUTO_APPEND_START -->
## 🆕 Repos detectados pendientes de curaduría

Generado: 2026-06-25T05:05:06.808623+00:00

Esta sección se actualiza automáticamente para no destruir la guía curada. Integra manualmente estas fichas al cuerpo principal cuando quieras dejar la guía completamente editorial.

| Repo | Categoria | Instalacion | Resumen |
|---|---:|---|---|
| [tools](human/fichas/tools.md) | 0 | reference_only |  |
| [appsmith](human/fichas/appsmith.md) | 1 | reference_only | Organizations build custom applications like dashboards, admin panels, customer 360, IT automation, and service management tools to help their teams work more efficiently and effectively. Appsmith is an open-source low-code platform that streamlines custom application development, deployment, and maintenance. Learn more on our [website](https://www.appsmith.com?utm_source=github&utm_medium=organic&utm_campaign=readme. |
| [budibase](human/fichas/budibase.md) | 1 | reference_only | AI Agents that run your operations Budibase is an open-source operations platform that saves engineers 100s of hours building Agents, Apps and Automations, securely. |
| [browser-harness](human/fichas/browser-harness.md) | 2 | reference_only | Browser Harness ♞. |
| [guia](human/fichas/guia.md) | 2 | reference_only | Catálogo operativo de los **156 repositorios** locales del workspace, diseñado para **entender, comparar, elegir y combinar** repos rápido. |
| [last30days-skill](human/fichas/last30days-skill.md) | 2 | reference_only | An AI agent-led search engine scored by upvotes, likes, and real money - not editors.**. |
| [OpenMontage](human/fichas/openmontage.md) | 2 | reference_only | Turn your AI coding assistant into a full video production studio. Describe what you want in plain language — your agent handles research, scripting, asset generation, editing, and final composition. |
| [skills_remotion](human/fichas/skills-remotion.md) | 2 | reference_only | This is an internal package and has no documentation. |
| [stitch-sdk](human/fichas/stitch-sdk.md) | 2 | reference_only | Generate UI screens from text prompts and extract their HTML and screenshots programmatically. |
| [autogen](human/fichas/autogen.md) | 3 | reference_only | AutoGen ![Maintenance Mode](https://github.com/microsoft/agent-framework). |
| [codebase-memory-mcp](human/fichas/codebase-memory-mcp.md) | 3 | reference_only | The fastest and most efficient code intelligence engine for AI coding agents.** Full-indexes an average repository in milliseconds, the Linux kernel (28M LOC, 75K files) in 3 minutes. Answers structural queries in under 1ms. Ships as a single static binary for macOS, Linux, and Windows — download, run `install`, done. |
| [defending-code-reference-harness](human/fichas/defending-code-reference-harness.md) | 3 | reference_only | A reference implementation for autonomous vulnerability discovery and remediation with Claude, based on our learnings from partnering with security teams at several organizations since launching Claude Mythos Preview. For a write up of these learnings along with best practices, see the accompanying blog post (also avail. |
| [Guardrails](human/fichas/guardrails.md) | 3 | reference_only | LATEST RELEASE / DEVELOPMENT VERSION**: The develop branch tracks the latest top of tree development. The latest released version is 0.21.0. |
| [ponytail](human/fichas/ponytail.md) | 3 | reference_only | You know him. Long ponytail. Oval glasses. Has been at the company longer than the version control. You show him fifty lines; he looks at them, says nothing, and replaces them with one. |
| [repomix](human/fichas/repomix.md) | 3 | global | Need discussion? Join us on Discord ! . |
| [ToolJet](human/fichas/tooljet.md) | 3 | reference_only | :star: If you find ToolJet useful, please consider giving us a star on GitHub! Your support helps us continue to innovate and deliver exciting features. |
| [ArchiveBox](human/fichas/archivebox.md) | 4 | reference_only | ▶️ Quickstart \| Demo \| GitHub \| Documentation \| Info & Motivation \| Communi. |
| [awesome-mcp-clients](human/fichas/awesome-mcp-clients.md) | 5 | reference_only | A curated list of awesome Model Context Protocol (MCP) clients. |
| [github-mcp-server](human/fichas/github-mcp-server.md) | 5 | reference_only | The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read repositories and code files, manage issues and PRs, analyze code, and automate workflows. All through natural language interactions. |
| [daily_stock_analysis](human/fichas/daily-stock-analysis.md) | 9 | reference_only | 🤖 基于 AI 大模型的 A股/港股/美股/日股/韩股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/Discord/Slack/邮箱. |
| [gradio](human/fichas/gradio.md) | 9 | reference_only | English \| 中文. |
| [Nemotron](human/fichas/nemotron.md) | 9 | deferred | Open and efficient models for agentic AI.** Training recipes, deployment guides, and use-case examples for the Nemotron family. |
| [stitch-skills](human/fichas/stitch-skills.md) | 9 | reference_only | A collection of agent skills and plugins for Google Stitch, following the Agent Skills open standard. Compatible with coding agents such as Codex, Antigravity, Gemini CLI, Claude Code, and Cursor. |
| [ui](human/fichas/ui.md) | 9 | reference_only | A set of beautifully designed components that you can customize, extend, and build on. Start here then make it your own. Open Source. Open Code. **Use this to build your own component library**. |
| [vllm](human/fichas/vllm.md) | 9 | reference_only | Easy, fast, and cheap LLM serving for everyone. |
| [LuxTTS](human/fichas/luxtts.md) | 11 | reference_only | LuxTTS is an lightweight zipvoice based text-to-speech model designed for high quality voice cloning and realistic generation at speeds exceeding 150x realtime. |
| [NeMo](human/fichas/nemo.md) | 11 | reference_only | Checkout our HuggingFace🤗 collection for the latest open weight checkpoints and demos!. |
| [FFmpeg](human/fichas/ffmpeg.md) | 12 | reference_only | FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata. |
| [VibeVoice](human/fichas/vibevoice.md) | 12 | reference_only | 🎙️ VibeVoice: Open-Source Frontier Voice AI. |
| [video-use](human/fichas/video-use.md) | 12 | reference_only | Introducing **video-use** — edit videos with Claude Code. 100% open source. |
<!-- BL_ALEXANDRIA_AUTO_APPEND_END -->
