# 📚 Catálogo de BL_Alexandria

**964 repos** de IA y automatización en **32 categorías**, con una línea por repo. Estrellas de GitHub al 2026-11-14.

[🗺️ Guía humana](human/README.md) · [🔎 Explorador interactivo](docs/index.html) · [🧪 Recetas](human/playbooks/README.md) · [🆕 Novedades](human/novedades.md) · [🤖 Para agentes](AGENTS.md)

> Empieza por una tarea y revisa acceso y costes antes de instalar. Las estrellas indican popularidad; no certifican la calidad o adecuación.

## Índice

1. [🤖 Automatizar procesos y crear herramientas internas](#-1-automatizar-procesos-y-crear-herramientas-internas) — 19
2. [🧠 Skills, plugins y métodos para agentes](#-2-skills-plugins-y-métodos-para-agentes) — 33
3. [🕸️ Construir agentes y coordinar equipos de IA](#️-3-construir-agentes-y-coordinar-equipos-de-ia) — 36
4. [🕷️ Buscar, extraer y monitorear información web](#️-4-buscar-extraer-y-monitorear-información-web) — 28
5. [🔌 Conectar herramientas con MCP](#-5-conectar-herramientas-con-mcp) — 27
6. [🧬 Memoria, RAG y búsqueda de conocimiento](#-6-memoria-rag-y-búsqueda-de-conocimiento) — 30
7. [🧑‍💻 Entender código y comprobar su calidad](#-7-entender-código-y-comprobar-su-calidad) — 26
8. [🏠 Chats, modelos locales y espacios privados](#-8-chats-modelos-locales-y-espacios-privados) — 33
9. [🎨 Diseñar y construir interfaces web](#-9-diseñar-y-construir-interfaces-web) — 33
10. [📊 Dashboards, analítica y mapas](#-10-dashboards-analítica-y-mapas) — 33
11. [🖼️ Generar y editar imágenes con IA](#️-11-generar-y-editar-imágenes-con-ia) — 11
12. [🎬 Editar, grabar y generar video](#-12-editar-grabar-y-generar-video) — 21
13. [📄 PDF, OCR y procesamiento de documentos](#-13-pdf-ocr-y-procesamiento-de-documentos) — 22
14. [📈 Investigar finanzas y mercados](#-14-investigar-finanzas-y-mercados) — 25
15. [🗂️ Organizar notas, archivos y servicios personales](#️-15-organizar-notas-archivos-y-servicios-personales) — 51
16. [🔍 Analizar software y comprobar su seguridad](#-16-analizar-software-y-comprobar-su-seguridad) — 141
17. [🤖 WhatsApp, mensajería y chatbots](#-17-whatsapp-mensajería-y-chatbots) — 18
18. [🤖 CRM, ventas y marketing](#-18-crm-ventas-y-marketing) — 19
19. [🧠 Aprender IA y escribir mejores prompts](#-19-aprender-ia-y-escribir-mejores-prompts) — 30
20. [🕸️ Programar con agentes de código](#️-20-programar-con-agentes-de-código) — 21
21. [🕸️ Asistentes e investigación con agentes](#️-21-asistentes-e-investigación-con-agentes) — 17
22. [🕸️ Infraestructura, despliegue y herramientas para agentes](#️-22-infraestructura-despliegue-y-herramientas-para-agentes) — 32
23. [🧬 Operar, evaluar y medir modelos de IA](#-23-operar-evaluar-y-medir-modelos-de-ia) — 30
24. [🧑‍💻 Modelos abiertos y entrenamiento](#-24-modelos-abiertos-y-entrenamiento) — 25
25. [🧑‍💻 Procesar datos y trabajar con notebooks](#-25-procesar-datos-y-trabajar-con-notebooks) — 21
26. [🎨 Animación, gráficos y creación 3D](#-26-animación-gráficos-y-creación-3d) — 32
27. [🎨 Skills de diseño, contenido y especialidades](#-27-skills-de-diseño-contenido-y-especialidades) — 38
28. [🖼️ Visión artificial, rostros y percepción](#️-28-visión-artificial-rostros-y-percepción) — 21
29. [🎬 Audio, transcripción, voz y música](#-29-audio-transcripción-voz-y-música) — 34
30. [🎬 Video con código y agentes creativos](#-30-video-con-código-y-agentes-creativos) — 25
31. [📄 Presentaciones, diagramas y explicación visual](#-31-presentaciones-diagramas-y-explicación-visual) — 12
32. [🕷️ Navegadores y automatización web](#️-32-navegadores-y-automatización-web) — 20
## 🤖 1. Automatizar procesos y crear herramientas internas

_Motores de flujos (Activepieces, Windmill, Node-RED, Huginn, Kestra, Trigger.dev) y apps internas sin código (NocoDB, ToolJet, Appsmith, Budibase). Elige primero el motor del proceso y conecta después datos, canales y modelos; para WhatsApp y atención al cliente se combinan con Evolution API, Dify y Chatwoot._ → [página de la categoría](human/categorias/01-automatizaci-n-mensajer-a-crm.md)

### Motores de workflow y automatización

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [huginn](human/fichas/huginn.md) | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Apache Airflow](human/fichas/airflow.md) | Orquestador de workflows de la Apache Software Foundation: DAGs en Python con planificador, workers, reintentos e interfaz de monitorización. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Kestra](human/fichas/kestra.md) | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Celery](human/fichas/celery.md) | Envía trabajos Python a una cola para que procesos separados los ejecuten y la aplicación no tenga que esperar. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [activepieces](human/fichas/activepieces.md) | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Temporal](human/fichas/temporal.md) | Plataforma de ejecución duradera: workflows en código que sobreviven a fallos, con reintentos, temporizadores y estado persistido por el servidor. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Prefect](human/fichas/prefect.md) | Framework de orquestación en Python: convierte scripts en flujos con decoradores, reintentos, caché, programación y servidor de monitorización. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Node-RED](human/fichas/node-red.md) | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Windmill](human/fichas/windmill.md) | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Trigger.dev](human/fichas/trigger-dev.md) | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Dagger](human/fichas/dagger.md) | Pipelines de entrega como código con contenedores: SDKs en 8 lenguajes, cache content-addressed y telemetría OpenTelemetry. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Dagster](human/fichas/dagster.md) | Orquestador de datos orientado a activos: declaras tablas, modelos o informes como funciones Python y Dagster los mantiene actualizados con linaje. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### Apps internas y bases de datos no-code

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [NocoDB](human/fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Appsmith](human/fichas/appsmith.md) | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [ToolJet](human/fichas/tooljet.md) | Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Budibase](human/fichas/budibase.md) | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Teable](human/fichas/teable.md) | Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja, formularios, automatizaciones y funciones de IA. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Grist](human/fichas/grist-core.md) | Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas tipadas y formato portable basado en SQLite. | API de IA opcional | ⚙️ plataforma | 🟢 fácil |
| [Baserow](human/fichas/baserow.md) | Base de datos sin código autoalojable (Django y Vue) con constructor de aplicaciones, automatizaciones, dashboards y API-first. | API de IA opcional | ⚙️ plataforma | 🟢 fácil |

## 🧠 2. Skills, plugins y métodos para agentes

_Catálogos de skills, plugins y métodos generales de desarrollo. Elige según tu cliente y consulta las especialidades de diseño o negocio en su sala específica._ → [página de la categoría](human/categorias/02-skills-prompts-gu-as-de-agente.md)

### Catálogos y marketplaces de skills

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Anthropic Skills](human/fichas/anthropic-skills.md) | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| ⭐ [Claude Code Plugins Directory](human/fichas/claude-plugins-official.md) | Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [Awesome Claude Skills](human/fichas/awesome-claude-skills.md) | Colección de guías para automatizar servicios como Google Calendar y Zoho Books desde un agente con Rube MCP de Composio. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [Awesome Claude Code](human/fichas/awesome-claude-code.md) | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [Agentic Awesome Skills (AAS)](human/fichas/antigravity-awesome-skills.md) | Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada Antigravity Awesome Skills. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [wshobson/agents](human/fichas/wshobson-agents.md) | Colección de plugins, agentes y skills con adaptadores documentados para Claude Code, Codex, Antigravity y otros clientes. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [Awesome GitHub Copilot](human/fichas/awesome-copilot.md) | Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub Copilot. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [Awesome Agent Skills](human/fichas/awesome-agent-skills.md) | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [Claude Code Templates](human/fichas/claude-code-templates.md) | Reúne componentes para Claude Code con buscador, entre ellos skills, agentes, hooks y configuraciones de herramientas. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |
| [Awesome Claude Code Subagents](human/fichas/awesome-claude-code-subagents.md) | Reúne perfiles especializados para Claude Code que puedes leer y comparar antes de adoptar uno en tu propio proyecto. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |
| [skills](human/fichas/google-skills.md) | Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [plugins](human/fichas/plugins.md) | Especificación y colección oficial de plugins de Cursor para estudiar e instalar extensiones de ese agente. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [autoskills](human/fichas/autoskills.md) | CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [gemini-skills](human/fichas/gemini-skills.md) | Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [awesome-agents](human/fichas/awesome-agents.md) | Directorio de herramientas y proyectos abiertos para construir y operar agentes de inteligencia artificial. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Metodologías y harness para agentes de código

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Agent Skills (Addy Osmani)](human/fichas/agent-skills.md) | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [skills](human/fichas/skills.md) | Skills de ingeniería de Matt Pocock para trabajar sobre requisitos, diseño, implementación y revisión, con plugins para Claude Code y Codex. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [superpowers](human/fichas/superpowers.md) | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [ECC](human/fichas/ecc.md) | Sistema de skills, hooks y configuración para agentes de código, con rutas nativas y adaptadores cuya capacidad varía según el cliente. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🔴 pesado |
| [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md) | Instrucciones para declarar supuestos, simplificar cambios y comprobar objetivos al programar, inspiradas en observaciones de Karpathy. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [Ponytail](human/fichas/ponytail.md) | Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribes. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [Spec Kit](human/fichas/spec-kit.md) | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [gstack](human/fichas/gstack.md) | Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [BMAD Method](human/fichas/bmad-method.md) | Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [book-to-skill](human/fichas/book-to-skill.md) | Herramientas para convertir un libro técnico en PDF en una skill que un agente pueda consultar durante el trabajo. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [codex-plugin-cc](human/fichas/codex-plugin-cc.md) | Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |
| [elephant-goldfish-model](human/fichas/elephant-goldfish-model.md) | Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complementarias. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [Improve de shadcn](human/fichas/shadcn-improve.md) | Organiza una auditoría de código en un plan que un modelo diferente puede implementar después de una revisión humana. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [claude-token-efficient](human/fichas/claude-token-efficient.md) | Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [claude-code-hooks-mastery](human/fichas/claude-code-hooks-mastery.md) | Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de trabajo. | API de IA opcional | 📂 catálogo/recurso | 🟢 fácil |
| [agent-toolkit](human/fichas/agent-toolkit.md) | Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [grok-plugin-claude-code](human/fichas/grok-plugin-claude-code.md) | Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar. | API: por confirmar | 🎨 skill/prompt | 🟢 fácil |
| [HUMANS.md Plugins](human/fichas/humans-md-plugins.md) | Carga preferencias de trabajo de un archivo HUMANS.md al iniciar una sesión en asistentes compatibles con el plugin. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |

## 🕸️ 3. Construir agentes y coordinar equipos de IA

_Frameworks, builders visuales y experimentos de coordinación. Separa la base técnica que integras del asistente listo que utilizas para una tarea._ → [página de la categoría](human/categorias/03-frameworks-orquestaci-n-de-agentes.md)

### Frameworks de agentes en Python

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [LangGraph](human/fichas/langgraph.md) | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. | API de IA opcional | 🧩 motor/runtime | 🟡 medio |
| [langchain](human/fichas/langchain.md) | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [MetaGPT](human/fichas/metagpt.md) | Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. | Depende de la ruta elegida | 🧩 motor/runtime | 🟡 medio |
| [crewAI](human/fichas/crewai.md) | Framework para orquestar "crews" de agentes con roles y tareas. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [OpenManus](human/fichas/openmanus.md) | Agente general de código abierto inspirado en Manus: planifica tareas y usa navegador, Python y archivos mediante herramientas y MCP. | API de IA necesaria | 🖥️ app | 🟡 medio |
| [LlamaIndex](human/fichas/llama-index.md) | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [Agno](human/fichas/agno.md) | Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. | Depende de la ruta elegida | 🧩 motor/runtime | 🟢 fácil |
| [DSPy](human/fichas/dspy.md) | Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [AgentScope](human/fichas/agentscope.md) | Framework de agentes en Python de origen Alibaba: agentes ReAct, multiagente, herramientas MCP, sandbox, voz en tiempo real y servicio desplegable. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [ChatDev](human/fichas/chatdev.md) | Plataforma multiagente sin código de OpenBMB: configura equipos de agentes por roles; la versión 1.0 simulaba una empresa de software. | API de IA necesaria | 🖥️ app | 🟡 medio |
| [Deep Agents](human/fichas/deepagents.md) | Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. | Depende de la ruta elegida | 🧩 motor/runtime | 🟢 fácil |
| [OpenAI Agents SDK](human/fichas/openai-agents-python.md) | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [smolagents](human/fichas/smolagents.md) | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [Haystack](human/fichas/haystack.md) | Framework de deepset para pipelines de RAG y agentes listos para producción. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [Agent Development Kit (ADK)](human/fichas/adk-python.md) | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [Pydantic AI](human/fichas/pydantic-ai.md) | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [CAMEL](human/fichas/camel.md) | Framework multiagente de investigación para generar datos sintéticos, automatizar tareas y simular sociedades de agentes con muchos proveedores. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [claude-agent-sdk-python](human/fichas/claude-agent-sdk-python.md) | SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia. | API de IA necesaria | 📚 librería/SDK | 🟡 medio |
| [ag2](human/fichas/ag2.md) | Framework AG2 actual para agentes y redes de colaboración en Python; AG2 Classic conserva por separado la API heredada autogen. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [Semantic Router](human/fichas/semantic-router.md) | Clasifica consultas por intención y decide a qué función enviarlas usando similitud entre ejemplos y texto de entrada. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [awesome-LangGraph](human/fichas/awesome-langgraph.md) | Repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Frameworks en TypeScript y multi-lenguaje

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Mastra](human/fichas/mastra.md) | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [AI SDK (Vercel)](human/fichas/vercel-ai.md) | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [Microsoft Agent Framework](human/fichas/agent-framework.md) | Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel. | Depende de la ruta elegida | 🧩 motor/runtime | 🟡 medio |
| [langchain4j](human/fichas/langchain4j.md) | Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [Eve](human/fichas/eve.md) | Ayuda a construir agentes con estado usando archivos de configuración, instrucciones y herramientas que puedes versionar con Git. | API de IA necesaria | 📚 librería/SDK | 🟡 medio |
| [LangGraph.js](human/fichas/langgraphjs.md) | Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. | API de IA opcional | 🧩 motor/runtime | 🟡 medio |

### Builders visuales y plataformas de agentes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Sim](human/fichas/sim.md) | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. | Depende de la ruta elegida | ⚙️ plataforma | 🟡 medio |
| [AutoGPT](human/fichas/autogpt.md) | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. | Depende de la ruta elegida | ⚙️ plataforma | 🔴 pesado |
| [dify](human/fichas/dify.md) | Plataforma integral para construir apps de IA con backend y UI listos. | Depende de la ruta elegida | ⚙️ plataforma | 🟡 medio |
| [langflow](human/fichas/langflow.md) | Constructor visual de flujos LLM/agentes construido sobre LangChain. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |

### Simulación, evolución y debate entre modelos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [MiroFish](human/fichas/mirofish.md) | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | API de IA necesaria | ⚙️ plataforma | 🔴 pesado |
| [llm-council](human/fichas/llm-council.md) | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. | API de IA necesaria | ⚙️ plataforma | 🟡 medio |
| [openevolve](human/fichas/openevolve.md) | Agente de codificación evolutivo que optimiza algoritmos por simulación genética. | Depende de la ruta elegida | 🧩 motor/runtime | 🔴 pesado |
| [hermes-agent-self-evolution](human/fichas/hermes-agent-self-evolution.md) | Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA. | API de IA necesaria | 📚 librería/SDK | 🟡 medio |
| [jev-fraud](human/fichas/jev-fraud.md) | Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude. | API de IA opcional | 📚 librería/SDK | 🟡 medio |

## 🕷️ 4. Buscar, extraer y monitorear información web

_Buscadores, crawlers, extracción y seguimiento de páginas o redes. Para hacer clic y operar interfaces utiliza la sala de navegadores y automatización web._ → [página de la categoría](human/categorias/04-scraping-b-squeda-research-web.md)

### Crawlers y extracción para IA

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [firecrawl](human/fichas/firecrawl.md) | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Scrapling](human/fichas/scrapling.md) | Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [crawl4ai](human/fichas/crawl4ai.md) | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [scrapy](human/fichas/scrapy.md) | Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [crawlee](human/fichas/crawlee.md) | Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Colly](human/fichas/colly.md) | Framework de scraping y crawling para Go: callbacks por selector, límites por dominio, caché, cookies y ejecución paralela. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Katana](human/fichas/katana.md) | Crawler web de ProjectDiscovery en Go, en modo estándar o headless, con análisis de JavaScript, control de alcance y salida JSON. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Jina Reader](human/fichas/jina-reader.md) | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [defuddle](human/fichas/defuddle.md) | Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [crawlee-python](human/fichas/crawlee-python.md) | Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [awesome-web-scraping](human/fichas/awesome-web-scraping.md) | Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Scraping guiado por LLM

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Scrapegraph-ai](human/fichas/scrapegraph-ai.md) | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [Maxun](human/fichas/maxun.md) | Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [llm-scraper](human/fichas/llm-scraper.md) | Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |

### Búsqueda, monitoreo y research web

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [SearXNG](human/fichas/searxng.md) | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Agent-Reach](human/fichas/agent-reach.md) | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [last30days](human/fichas/last30days-skill.md) | Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |
| [RSSHub](human/fichas/rsshub.md) | Generador de feeds RSS para miles de webs y redes sin RSS propio; instancia pública o autoalojada con Docker. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Vane](human/fichas/vane.md) | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). | Depende de la ruta elegida | 🖥️ app | 🟢 fácil |
| [changedetection.io](human/fichas/changedetection.md) | Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [ArchiveBox](human/fichas/archivebox.md) | Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [FreshRSS](human/fichas/freshrss.md) | Agregador de noticias RSS autoalojado, ligero y multiusuario, con API para apps móviles, WebSub, extracción por XPath y extensiones. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [wallabag](human/fichas/wallabag.md) | Aplicación autoalojada para guardar páginas web y leerlas más tarde sin distracciones, con apps móviles y extensión de navegador. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Miniflux](human/fichas/miniflux.md) | Lector de feeds minimalista y rápido en Go sobre PostgreSQL, con privacidad, búsqueda de texto completo y más de 25 integraciones. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |

### Redes sociales y descarga de medios

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [yt-dlp](human/fichas/yt-dlp.md) | Descargador de audio y video por línea de comandos compatible con miles de sitios. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [spotDL](human/fichas/spotdl.md) | CLI que toma listas y canciones de Spotify, busca coincidencias en YouTube y las descarga con carátula, letras y metadatos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [gallery-dl](human/fichas/gallery-dl.md) | Programa de línea de comandos para descargar galerías y colecciones de imágenes de muchos sitios, con nombres de archivo configurables. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [instaloader](human/fichas/instaloader.md) | Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |

## 🔌 5. Conectar herramientas con MCP

_SDKs, servidores, clientes y directorios MCP. Un servidor aporta acciones o datos; el modelo y su acceso pertenecen al cliente que lo utiliza._ → [página de la categoría](human/categorias/05-mcp-conectividad.md)

### SDKs y frameworks para crear MCP

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [FastMCP](human/fichas/fastmcp.md) | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| ⭐ [MCP TypeScript SDK](human/fichas/mcp-typescript-sdk.md) | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [MCP Python SDK](human/fichas/mcp-python-sdk.md) | SDK oficial de Python para crear servidores y clientes del Model Context Protocol. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [MCP Inspector](human/fichas/mcp-inspector.md) | Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [mcp-use](human/fichas/mcp-use.md) | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. | API de IA opcional | 📚 librería/SDK | 🟡 medio |

### Servidores MCP destacados

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Context7](human/fichas/context7.md) | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| ⭐ [Playwright MCP](human/fichas/playwright-mcp.md) | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [servers](human/fichas/servers.md) | Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |
| [Chrome DevTools MCP](human/fichas/chrome-devtools-mcp.md) | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [GitHub MCP Server](human/fichas/github-mcp-server.md) | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [Blender MCP](human/fichas/blender-mcp.md) | Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [Serena](human/fichas/serena.md) | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [MCP Toolbox for Databases](human/fichas/mcp-toolbox.md) | Servidor MCP de Google para bases de datos: herramientas genéricas listas y un framework para definir consultas seguras para agentes. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [Figma Context MCP](human/fichas/figma-context-mcp.md) | Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [unity-mcp](human/fichas/unity-mcp.md) | Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [Claude Context](human/fichas/claude-context.md) | Permite que asistentes busquen funciones y conceptos por significado en una base de código a través de un conector MCP. | API de IA necesaria | 🧩 motor/runtime | 🟡 medio |
| [GhidraMCP](human/fichas/ghidramcp.md) | Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [MCP servers for AWS](human/fichas/aws-mcp.md) | Colección oficial de AWS Labs con decenas de servidores MCP para documentación, infraestructura como código, EKS, ECS, serverless y otros servicios. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [Home Assistant MCP](human/fichas/ha-mcp.md) | Conecta Home Assistant con un asistente mediante MCP para consultar entidades y trabajar con automatizaciones de domótica. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [annas-mcp](human/fichas/annas-mcp.md) | Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [mcp-neo4j](human/fichas/mcp-neo4j.md) | Servidores experimentales de Neo4j Labs para consultar grafos, memoria y recursos Aura desde clientes MCP. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [Neo4j MCP (oficial)](human/fichas/neo4j-mcp.md) | Servidor MCP oficial de Neo4j para que un asistente lea el esquema de un grafo y ejecute consultas Cypher de lectura o escritura. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |

### Directorios, clientes y aprendizaje

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [MCP for Beginners](human/fichas/mcp-for-beginners.md) | Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [public-apis](human/fichas/public-apis.md) | Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md) | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [Awesome MCP Clients](human/fichas/awesome-mcp-clients.md) | Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y agentes. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [Google MCP](human/fichas/mcp.md) | Directorio de servidores MCP oficiales de Google, ejemplos y orientación para desplegarlos en Google Cloud. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |

## 🧬 6. Memoria, RAG y búsqueda de conocimiento

_Memoria persistente, sistemas RAG y bases vectoriales. La memoria mantiene contexto; RAG recupera documentos; una base vectorial almacena el índice de búsqueda._ → [página de la categoría](human/categorias/06-memoria-rag-llm-ops.md)

### Memoria persistente para agentes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [claude-mem](human/fichas/claude-mem.md) | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |
| [mem0](human/fichas/mem0.md) | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [mempalace](human/fichas/mempalace.md) | Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [OpenViking](human/fichas/openviking.md) | Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información. | Depende de la ruta elegida | ⚙️ plataforma | 🔴 pesado |
| [cognee](human/fichas/cognee.md) | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [Graphiti](human/fichas/graphiti.md) | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [supermemory](human/fichas/supermemory.md) | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. | Depende de la ruta elegida | ⚙️ plataforma | 🟢 fácil |
| [agentmemory](human/fichas/agentmemory.md) | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [Engram](human/fichas/engram.md) | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [Letta](human/fichas/letta.md) | Harness de agentes con estado (Letta Code, antes MemGPT): memoria, identidad y skills que el propio agente reescribe con el tiempo. | Depende de la ruta elegida | ⚙️ plataforma | 🟡 medio |
| [dsh-noema](human/fichas/dsh-noema.md) | Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### RAG y motores de conocimiento

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [RAGFlow](human/fichas/ragflow.md) | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | Depende de la ruta elegida | ⚙️ plataforma | 🔴 pesado |
| [Meilisearch](human/fichas/meilisearch.md) | Motor de búsqueda rápido en Rust con texto completo, búsqueda semántica e híbrida, facetas, tolerancia a erratas y API sencilla. | API de IA opcional | ⚙️ plataforma | 🟢 fácil |
| [LightRAG](human/fichas/lightrag.md) | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [PageIndex](human/fichas/pageindex.md) | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [graphrag](human/fichas/graphrag.md) | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [onyx](human/fichas/onyx.md) | Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [kotaemon](human/fichas/kotaemon.md) | Interfaz RAG limpia y personalizable para chatear con documentos, con modelos locales o por API y soporte de GraphRAG y LightRAG. | API de IA opcional | 🖥️ app | 🟡 medio |
| [txtai](human/fichas/txtai.md) | Framework de IA todo en uno para búsqueda semántica, RAG, pipelines con LLM, flujos y agentes sobre una base de embeddings propia. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [Chonkie](human/fichas/chonkie.md) | Divide textos largos en fragmentos para indexarlos o recuperarlos, con estrategias simples y opciones basadas en modelos. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [agentic-rag-for-dummies](human/fichas/agentic-rag-for-dummies.md) | Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |

### Bases vectoriales y búsqueda semántica

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Qdrant](human/fichas/qdrant.md) | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [Milvus](human/fichas/milvus.md) | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [Faiss](human/fichas/faiss.md) | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Chroma](human/fichas/chroma.md) | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [pgvector](human/fichas/pgvector.md) | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [turbovec](human/fichas/turbovec.md) | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Weaviate](human/fichas/weaviate.md) | Base de datos vectorial nativa de la nube que guarda objetos y vectores, con búsqueda híbrida, filtros, RAG y vectorización integrada. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [FlagEmbedding](human/fichas/flagembedding.md) | Calcula representaciones y relevancia de textos con modelos BGE para ordenar documentos según una consulta de búsqueda. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [LanceDB](human/fichas/lancedb.md) | Base de datos vectorial embebida sobre el formato columnar Lance: búsqueda vectorial, de texto completo y SQL sin servidor que mantener. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |

## 🧑‍💻 7. Entender código y comprobar su calidad

_Índices de código, análisis, calidad, benchmarks y herramientas de desarrollo. Empieza por comprender el proyecto y después elige qué comprobaciones necesitas._ → [página de la categoría](human/categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md)

### Entender y empaquetar código para agentes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Repomix](human/fichas/repomix.md) | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [graphify](human/fichas/graphify.md) | CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AST y la extracción semántica tiene rutas separadas. | API de IA opcional | 🧩 motor/runtime | 🟡 medio |
| [codegraph](human/fichas/codegraph.md) | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [codebase-memory-mcp](human/fichas/codebase-memory-mcp.md) | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [GitNexus](human/fichas/gitnexus.md) | Explora flujos de ejecución y previsualiza renombrados semánticos con el índice de GitNexus. El visor web se conecta al servidor del CLI. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [tree-sitter](human/fichas/tree-sitter.md) | Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [floorplan](human/fichas/floorplan.md) | Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |

### Calidad, seguridad y benchmarks de código

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [ast-grep](human/fichas/ast-grep.md) | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Open Code Review](human/fichas/open-code-review.md) | Revisa cambios de código con reglas y un informe guiado, usando su propio proveedor de IA o el asistente de programación que ya tienes. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [Ruff](human/fichas/ruff.md) | Linter y formateador de Python extremadamente rápido escrito en Rust, compatible con Flake8, isort y Black, con más de 800 reglas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Gitleaks](human/fichas/gitleaks.md) | Detector de secretos (contraseñas, claves de API, tokens) en repositorios git, archivos y stdin, usable como hook o acción de CI. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [TruffleHog](human/fichas/trufflehog.md) | Busca, clasifica, verifica y analiza credenciales filtradas en git, chats, wikis, logs, almacenes de objetos y sistemas de archivos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Biome](human/fichas/biome.md) | Formateador y linter en un solo binario para JavaScript, TypeScript, JSX, JSON, CSS, GraphQL y más, usable por CLI y LSP. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [pre-commit](human/fichas/pre-commit.md) | Framework para gestionar y ejecutar hooks de git multilenguaje antes de cada commit: linters, formateadores y escáneres declarados en YAML. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [SonarQube Community Build](human/fichas/sonarqube.md) | Plataforma de inspección continua de calidad y seguridad del código: análisis estático de bugs, vulnerabilidades y mantenibilidad en muchos lenguajes. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [SWE-bench](human/fichas/swe-bench.md) | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. | API de IA opcional | 📚 librería/SDK | 🔴 pesado |

### CLIs y SDKs de desarrollo

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [GitHub CLI](human/fichas/cli.md) | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [fzf](human/fichas/fzf.md) | Buscador difuso de línea de comandos y kit de interfaces de terminal para seleccionar archivos, historial o cualquier lista de forma interactiva. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [lazygit](human/fichas/lazygit.md) | Interfaz de terminal sencilla para git: preparar fragmentos o líneas, rebase interactivo, cherry-pick y gestión de ramas con atajos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [ripgrep](human/fichas/ripgrep.md) | Búsqueda recursiva de texto por expresiones regulares muy rápida que respeta .gitignore y omite archivos ocultos y binarios. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [openai-python](human/fichas/openai-python.md) | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. | API de IA necesaria | 📚 librería/SDK | 🟢 fácil |
| [npkill](human/fichas/npkill.md) | Muestra cuánto espacio ocupan carpetas generadas por herramientas de desarrollo y permite revisarlas antes de eliminar residuos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [APScheduler](human/fichas/apscheduler.md) | Programa funciones Python para un horario, un intervalo o una fecha concreta dentro de una aplicación propia. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Requests Cache](human/fichas/requests-cache.md) | Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas y reducir viajes repetidos a un servicio HTTP. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [PyBreaker](human/fichas/pybreaker.md) | Protege una integración Python con un interruptor que pausa llamadas tras varios fallos y después permite comprobar si volvió el servicio. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Hishel](human/fichas/hishel.md) | Añade caché a peticiones HTTP de Python con políticas de expiración y adaptadores de almacenamiento reutilizables. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

## 🏠 8. Chats, modelos locales y espacios privados

_Motores locales, chats y workspaces. Tener la interfaz en tu equipo no garantiza que el modelo sea local: comprueba su backend y los requisitos de cada ficha._ → [página de la categoría](human/categorias/08-ia-local-modelos-chats-workspaces.md)

### Motores para correr modelos en local

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Ollama](human/fichas/ollama.md) | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [llama.cpp](human/fichas/llama-cpp.md) | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [LocalAI](human/fichas/localai.md) | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [exo](human/fichas/exo.md) | Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [airllm](human/fichas/airllm.md) | Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [llmfit](human/fichas/llmfit.md) | Inspector de hardware que estima qué modelos de lenguaje y cuantizaciones caben en tu CPU, RAM y GPU. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [llamafile](human/fichas/llamafile.md) | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [MLC LLM](human/fichas/mlc-llm.md) | Motor universal de despliegue de LLM con compilación de ML: ejecuta modelos en GPU de escritorio, móviles y navegador con API compatible con OpenAI. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [FreeToken](human/fichas/freetoken.md) | Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [transformers.js](human/fichas/transformers-js.md) | Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [KoboldCpp](human/fichas/koboldcpp.md) | Ejecutable único basado en llama.cpp para correr modelos GGUF en local con interfaz web KoboldAI Lite y APIs compatibles con OpenAI y Ollama. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [magnitude](human/fichas/magnitude.md) | Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [MLX LM](human/fichas/mlx-lm.md) | Paquete de Apple para generar texto y afinar LLM en Apple Silicon con MLX: miles de modelos del Hub, cuantización, LoRA y servidor HTTP. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [InferSSD](human/fichas/inferssd.md) | Ejecuta modelos locales de tipo MoE leyendo partes de sus pesos desde un SSD cuando no caben completos en memoria o VRAM. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |

### Interfaces de chat auto-hospedadas

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Open WebUI](human/fichas/open-webui.md) | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. | API de IA opcional | 🖥️ app | 🟢 fácil |
| ⭐ [Jan](human/fichas/jan.md) | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [NextChat](human/fichas/nextchat.md) | Cliente de chat de IA ligero y multiplataforma (web, escritorio y móvil) para Claude, GPT, Gemini, DeepSeek y modelos autoalojados, con soporte MCP. | API de IA necesaria | 🖥️ app | 🟢 fácil |
| [LobeHub](human/fichas/lobehub.md) | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. | Depende de la ruta elegida | 🖥️ app | 🟢 fácil |
| [Cherry Studio](human/fichas/cherry-studio.md) | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [Text Generation WebUI](human/fichas/textgen.md) | App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [LibreChat](human/fichas/librechat.md) | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. | API de IA opcional | 🖥️ app | 🟡 medio |
| [chatbox](human/fichas/chatbox.md) | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [SillyTavern](human/fichas/sillytavern.md) | Interfaz local avanzada para chatear con LLM: une muchas APIs, personajes, rol, generación de imágenes, voz y extensiones. | API de IA opcional | 🖥️ app | 🟡 medio |

### Workspaces privados y segundos cerebros

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [AnythingLLM](human/fichas/anything-llm.md) | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [odysseus](human/fichas/odysseus.md) | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. | Depende de la ruta elegida | ⚙️ plataforma | 🔴 pesado |
| [PrivateGPT](human/fichas/private-gpt.md) | Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. | Depende de la ruta elegida | ⚙️ plataforma | 🟡 medio |
| [Khoj](human/fichas/khoj.md) | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [Hermes Desktop](human/fichas/hermes-desktop.md) | App de escritorio que envuelve al agente Hermes en una interfaz nativa. | Depende de la ruta elegida | 🖥️ app | 🟢 fácil |
| [Claude Second Brain](human/fichas/claude-second-brain.md) | Organiza una bóveda de Obsidian para que Claude Code consulte y mantenga notas con instrucciones y búsqueda local. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### NotebookLM: alternativas y clientes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [SurfSense](human/fichas/surfsense.md) | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [open-notebook](human/fichas/open-notebook.md) | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [notebooklm-py](human/fichas/notebooklm-py.md) | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [notebooklm-mcp-cli](human/fichas/notebooklm-mcp-cli.md) | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |

## 🎨 9. Diseñar y construir interfaces web

_Componentes, estilos, editores visuales y herramientas de UI con IA. Elige la base de tu interfaz y consulta animación o skills especializadas en sus salas._ → [página de la categoría](human/categorias/09-dise-o-ui-frontend.md)

### Componentes, iconos y sistemas de diseño

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [ui](human/fichas/ui.md) | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Ant Design](human/fichas/ant-design.md) | Lenguaje de diseño empresarial y librería de componentes React de Ant Group. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Material UI](human/fichas/mui.md) | Librería de componentes React completa que implementa Material Design de Google. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Storybook](human/fichas/storybook.md) | Taller de frontend para construir, documentar y probar componentes y páginas de UI de forma aislada en React, Vue, Angular y otros. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [React Bits](human/fichas/react-bits.md) | Efectos de texto, fondos gráficos y componentes interactivos para añadir animaciones puntuales a una interfaz React. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [TanStack Query](human/fichas/tanstack-query.md) | Biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor en React, Vue, Solid, Svelte, Angular y otros frameworks. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Chakra UI](human/fichas/chakra-ui.md) | Sistema de componentes React accesibles para crear productos y sistemas de diseño con rapidez, compatible con Next.js RSC. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [swr](human/fichas/swr.md) | Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Astryx](human/fichas/astryx.md) | Añade a una web componentes y temas de un sistema de diseño que puedes adaptar sin construir cada elemento desde cero. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Mantine](human/fichas/mantine.md) | Biblioteca de componentes React completa con más de 100 componentes, hooks, formularios, gráficos, fechas y notificaciones. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [heroui](human/fichas/heroui.md) | Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Lucide](human/fichas/lucide.md) | Librería de más de 1500 iconos SVG consistentes, con paquetes para React, Vue y más. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [magicui](human/fichas/magicui.md) | Componentes React para componer secciones de página con shadcn y Tailwind, como una cuadrícula Bento o un bloque de video. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Radix Primitives](human/fichas/radix-primitives.md) | Componentes React sin estilos y accesibles para construir sistemas de diseño propios. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [konva](human/fichas/konva.md) | Biblioteca de canvas para construir editores gráficos, diagramas e interfaces con formas y objetos interactivos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### CSS y estilos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [daisyUI](human/fichas/daisyui.md) | La librería de componentes más popular para Tailwind CSS, con clases semánticas y temas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [tailwindcss](human/fichas/tailwindcss.md) | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [normalize.css](human/fichas/normalize-css.md) | Hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [flexoki](human/fichas/flexoki.md) | Paleta de color para texto, código e interfaces que puede servir de referencia al definir un sistema visual. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Diseño visual, canvas y builders

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Excalidraw](human/fichas/excalidraw.md) | Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [open-design](human/fichas/open-design.md) | Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural. | API de IA opcional | 🖥️ app | 🟡 medio |
| [penpot](human/fichas/penpot.md) | Plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🔴 pesado |
| [tldraw](human/fichas/tldraw.md) | SDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Onlook](human/fichas/onlook.md) | Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma. | Depende de la ruta elegida | 🖥️ app | 🟢 fácil |
| [plasmic](human/fichas/plasmic.md) | Builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |

### UI generada con IA y frontends para agentes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [CopilotKit](human/fichas/copilotkit.md) | Stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [screenshot-to-code](human/fichas/screenshot-to-code.md) | Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue. | Depende de la ruta elegida | 🖥️ app | 🟢 fácil |
| [ai-website-cloner-template](human/fichas/ai-website-cloner-template.md) | Plantilla para que un agente de código estudie una web de referencia y prepare una implementación de su interfaz. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [json-render](human/fichas/json-render.md) | Framework para generar interfaces desde una representación JSON y un catálogo de componentes definido por el desarrollador. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [OpenUI](human/fichas/openui.md) | Estándar abierto de Thesys para UI generativa: el LLM responde con interfaces, no solo texto. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [assistant-ui](human/fichas/assistant-ui.md) | Librería React y TypeScript para interfaces de chat con IA de calidad producción. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [UI SDK (Vercel)](human/fichas/ui-sdk.md) | Colección de comportamientos y recursos para que agentes construyan interfaces con patrones de interacción definidos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Stitch SDK](human/fichas/stitch-sdk.md) | SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código. | API de IA necesaria | 📚 librería/SDK | 🟢 fácil |

## 📊 10. Dashboards, analítica y mapas

_Analítica web, BI, gráficos y herramientas geoespaciales. Medir visitas, consultar un negocio y procesar fotografías para crear mapas requieren piezas diferentes._ → [página de la categoría](human/categorias/10-anal-tica-visualizaci-n.md)

### Analítica web y de producto

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Umami](human/fichas/umami.md) | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [posthog](human/fichas/posthog.md) | Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [Plausible Analytics](human/fichas/plausible.md) | Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Matomo](human/fichas/matomo.md) | Alternativa open source a Google Analytics con control total de los datos. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |

### BI, dashboards y chat con datos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Apache Superset](human/fichas/superset.md) | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| ⭐ [WrenAI](human/fichas/wrenai.md) | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. | Depende de la ruta elegida | ⚙️ plataforma | 🟡 medio |
| [Grafana](human/fichas/grafana.md) | Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [metabase](human/fichas/metabase.md) | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Redash](human/fichas/redash.md) | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Evidence](human/fichas/evidence.md) | BI como código: informes y visualizaciones interactivas escritos en SQL y Markdown, autoalojables o publicados en Evidence Studio. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Librerías de gráficos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Recharts](human/fichas/recharts.md) | Librería de gráficos para React construida con D3, declarativa y componible. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [D3.js](human/fichas/d3.md) | Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y HTML. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Chart.js](human/fichas/chart-js.md) | Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [echarts](human/fichas/echarts.md) | Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [uPlot](human/fichas/uplot.md) | Biblioteca compacta de gráficos de series temporales en JavaScript, orientada a renderizar datos con Canvas y controles programables. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |

### Recursos y casos de uso

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [awesome-bigdata](human/fichas/awesome-bigdata.md) | Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [awesome-dataviz](human/fichas/awesome-dataviz.md) | Directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [data-analyst-roadmap](human/fichas/data-analyst-roadmap.md) | Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y orientación de carrera. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Inteligencia de fuentes abiertas y mapas

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Sherlock](human/fichas/sherlock.md) | CLI OSINT que busca un nombre de usuario en más de 400 redes sociales y sitios para localizar cuentas asociadas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [gods-eye-view](human/fichas/gods-eye-view.md) | Visualizador geoespacial en un globo 3D que reúne fuentes abiertas para explorar información espacial en el navegador. | API de IA opcional | 🖥️ app | 🟡 medio |
| [Maigret](human/fichas/maigret.md) | Recopila un dossier sobre una persona a partir de un nombre de usuario comprobando miles de sitios y extrayendo datos públicos de los perfiles. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [theHarvester](human/fichas/theharvester.md) | Herramienta OSINT de reconocimiento que reúne correos, subdominios, IP y nombres de un dominio desde buscadores, certificados y fuentes públicas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [osiris](human/fichas/osiris.md) | Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. | API de IA opcional | 🖥️ app | 🟡 medio |
| [Recon-ng](human/fichas/recon-ng.md) | Framework modular de reconocimiento web OSINT con espacios de trabajo, base de datos y módulos al estilo de Metasploit. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Pythia](human/fichas/pythia.md) | Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |

### Datos geoespaciales, fotogrametría y mapas

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Leaflet](human/fichas/leaflet.md) | Biblioteca JavaScript ligera para mapas web interactivos: unos 40 kB, capas de teselas, marcadores, GeoJSON y un ecosistema enorme de plugins. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [QGIS](human/fichas/qgis.md) | Sistema de información geográfica libre y multiplataforma: gestión de datos espaciales, cartografía, análisis, Python y QGIS Server. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [deck.gl](human/fichas/deck-gl.md) | Framework de visualización en WebGL2/WebGPU para grandes conjuntos de datos, con capas apilables sobre mapas y vistas 3D. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [MapLibre GL JS](human/fichas/maplibre.md) | Biblioteca abierta de mapas vectoriales interactivos en el navegador con renderizado GPU, nacida como fork de Mapbox GL JS antes de su cambio de licencia. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [kepler.gl](human/fichas/kepler-gl.md) | Herramienta web de exploración visual de grandes datos geográficos sin código, también usable como componente React y widget de Jupyter. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [ODM](human/fichas/odm.md) | Herramientas para convertir fotografías aéreas en mapas, nubes de puntos, modelos 3D y modelos de elevación. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [WebODM](human/fichas/webodm.md) | Interfaz para procesar fotografías aéreas y obtener mapas y modelos con el ecosistema de OpenDroneMap. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [GlobalBuildingAtlas](human/fichas/globalbuildingatlas.md) | Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🔴 pesado |

## 🖼️ 11. Generar y editar imágenes con IA

_Interfaces y modelos de generación, recorte, restauración y ampliación. Distingue la aplicación, sus modelos y el coste o equipo para generar cada imagen._ → [página de la categoría](human/categorias/11-generaci-n-de-imagen-visi-n.md)

### Interfaces para generar imágenes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [ComfyUI](human/fichas/comfyui.md) | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | API de IA opcional | 🧩 motor/runtime | 🔴 pesado |
| [InvokeAI](human/fichas/invokeai.md) | Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🔴 pesado |
| [Krita AI Diffusion](human/fichas/krita-ai-diffusion.md) | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. | API de IA opcional | 🖥️ app | 🟡 medio |

### Modelos, librerías y control

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [FLUX.2](human/fichas/flux2.md) | Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágenes, con variantes rápidas para GPU domésticas. | API de IA opcional | 🧩 motor/runtime | 🔴 pesado |
| [diffusers](human/fichas/diffusers.md) | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |

### Restauración, upscaling y edición

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [rembg](human/fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [Upscayl](human/fichas/upscayl.md) | Aplicación de escritorio libre para ampliar y mejorar imágenes con IA (Real-ESRGAN sobre NCNN Vulkan) en Linux, macOS y Windows. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Real-ESRGAN](human/fichas/real-esrgan.md) | Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [CodeFormer](human/fichas/codeformer.md) | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [ImageMagick](human/fichas/imagemagick.md) | Convierte, redimensiona y prepara imágenes desde la terminal. Puedes generar miniaturas y variantes web en tu equipo sin un modelo de IA. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [chaiNNer](human/fichas/chainner.md) | Interfaz por nodos para encadenar procesamiento de imágenes con IA y clásico: escalado, restauración, conversión y lotes, en Windows, macOS y Linux. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |

## 🎬 12. Editar, grabar y generar video

_Editores, grabadores, utilidades de medios y modelos de video generativo. La edición de material existente y la generación de nuevas escenas tienen requisitos distintos._ → [página de la categoría](human/categorias/12-audio-voz-video.md)

### Edición, grabación y subtítulos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [FFmpeg](human/fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OpenCut](human/fichas/opencut.md) | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [OBS Studio](human/fichas/obs-studio.md) | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [LosslessCut](human/fichas/lossless-cut.md) | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [HandBrake](human/fichas/handbrake.md) | Transcodificador de vídeo libre para Linux, macOS y Windows con interfaz gráfica, CLI, presets por dispositivo y colas de trabajo. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [VideoLingo](human/fichas/videolingo.md) | App para reconocer voz, traducir subtítulos y preparar doblaje, con ASR local por defecto y proveedores configurables por etapa. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [Concat](human/fichas/concat.md) | Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Shotcut](human/fichas/shotcut.md) | Editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Kdenlive](human/fichas/kdenlive.md) | Editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [DaVinci Resolve MCP](human/fichas/davinci-resolve-mcp.md) | Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [libass](human/fichas/libass.md) | Dibuja subtítulos ASS y SSA con estilos, posiciones y tiempos en programas de video, bibliotecas multimedia y reproductores compatibles. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [OpenRV](human/fichas/openrv.md) | Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [pysubs2](human/fichas/pysubs2.md) | Convierte formatos de subtítulos y ajusta sus tiempos en lote desde Python o la terminal, sin cambiar el video ni usar una API de IA. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |

### Video generativo y pipelines automáticos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [MoneyPrinterTurbo](human/fichas/moneyprinterturbo.md) | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| ⭐ [Wan2.2](human/fichas/wan2-2.md) | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | API de IA opcional | 🧩 motor/runtime | 🔴 pesado |
| [HunyuanVideo](human/fichas/hunyuanvideo.md) | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [WanGP](human/fichas/wan2gp.md) | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. | API de IA opcional | 🖥️ app | 🔴 pesado |
| [LTX-2](human/fichas/ltx-2.md) | Código oficial de inferencia y entrenamiento LoRA de LTX-2 y LTX-2.5, modelo DiT de Lightricks que genera vídeo con audio sincronizado. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [short-video-factory](human/fichas/short-video-factory.md) | Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [AI-Youtube-Shorts-Generator](human/fichas/ai-youtube-shorts-generator.md) | Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM. | API de IA necesaria | 🖥️ app | 🟡 medio |
| [HunyuanVideo 1.5](human/fichas/hunyuanvideo-1-5.md) | Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más. | API de IA opcional | 🧩 motor/runtime | 🔴 pesado |

## 📄 13. PDF, OCR y procesamiento de documentos

_Extracción de texto, OCR, conversión y gestión de PDF. Empieza por el formato de entrada y comprueba con una muestra si conserva el contenido que necesitas._ → [página de la categoría](human/categorias/13-documentos-presentaciones.md)

### Conversión de documentos para IA

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Docling](human/fichas/docling.md) | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [markitdown](human/fichas/markitdown.md) | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [MinerU](human/fichas/mineru.md) | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. | API de IA opcional | 🖥️ app | 🟡 medio |
| [Pandoc](human/fichas/pandoc.md) | Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Marker](human/fichas/marker.md) | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [PDF Inspector](human/fichas/pdf-inspector.md) | Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Unstructured](human/fichas/unstructured.md) | ETL open source que transforma documentos complejos en datos estructurados para LLM. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [Xberg (antes Kreuzberg)](human/fichas/xberg.md) | Motor de extracción de documentos en Rust: texto, tablas y metadatos de más de 100 formatos, con OCR, transcripción, embeddings y MCP. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [Apache Tika](human/fichas/tika.md) | Kit de Apache que detecta y extrae texto y metadatos de más de mil tipos de archivo; desde 4.0 emite Markdown pensado para LLM y RAG. | API de IA opcional | ⚙️ plataforma | 🟡 medio |

### OCR

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [PaddleOCR](human/fichas/paddleocr.md) | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| ⭐ [OCRmyPDF](human/fichas/ocrmypdf.md) | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Tesseract](human/fichas/tesseract.md) | Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Unlimited-OCR](human/fichas/unlimited-ocr.md) | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [Surya](human/fichas/surya.md) | OCR multilingüe y análisis de layout con un VLM de 689M parámetros: orden de lectura, tablas en HTML y más de 90 idiomas. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [olmOCR](human/fichas/olmocr.md) | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. | API de IA opcional | 🖥️ app | 🔴 pesado |
| [pdf-craft](human/fichas/pdf-craft.md) | Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |

### Herramientas PDF

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Stirling-PDF](human/fichas/stirling-pdf.md) | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [PDFMathTranslate](human/fichas/pdfmathtranslate.md) | Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe. | Depende de la ruta elegida | 🖥️ app | 🟢 fácil |
| [docuseal](human/fichas/docuseal.md) | Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [pdfcraft](human/fichas/pdfcraft.md) | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Gestión y archivo de documentos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [paperless-ngx](human/fichas/paperless-ngx.md) | Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [PdfDing](human/fichas/pdfding.md) | Gestor, visor y editor de PDF autoalojado (AGPL-3.0) con colecciones, etiquetas, anotaciones y progreso de lectura; se desarrolla en Codeberg. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

## 📈 14. Investigar finanzas y mercados

_Agentes de investigación, análisis cuantitativo, backtesting y bots de ejemplo. Distingue una explicación o simulación de una operación con fondos reales._ → [página de la categoría](human/categorias/14-investigar-finanzas-y-mercados.md)

### Agentes de investigación financiera

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [daily_stock_analysis](human/fichas/daily-stock-analysis.md) | Sistema que analiza acciones de varios mercados con LLM y envía un tablero de decisiones diario. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| ⭐ [dexter](human/fichas/dexter.md) | Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [TradingAgents](human/fichas/tradingagents.md) | Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de trading. | Depende de la ruta elegida | 🧩 motor/runtime | 🟡 medio |
| [Vibe-Trading](human/fichas/vibe-trading.md) | Agente de investigación y trabajo con estrategias de trading que utiliza modelos y componentes configurables. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [FinceptTerminal](human/fichas/finceptterminal.md) | Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes. | API de IA opcional | 🖥️ app | 🔴 pesado |
| [FinGPT](human/fichas/fingpt.md) | Proyecto de LLM financieros abiertos de AI4Finance: modelos ajustados con LoRA, datos y recetas para análisis de sentimiento y tareas financieras. | API de IA opcional | 🧩 motor/runtime | 🔴 pesado |
| [AutoHedge](human/fichas/autohedge.md) | Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado. | API de IA necesaria | 🧩 motor/runtime | 🔴 pesado |
| [QuantHarness](human/fichas/quantharness.md) | Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de trading. | API de IA necesaria | 🧩 motor/runtime | 🟡 medio |
| [PolyWeather](human/fichas/polyweather.md) | Reúne datos meteorológicos y de mercados de predicción para explorar cómo las previsiones afectan a contratos relacionados con el clima. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Modelos y backtesting cuantitativo

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [qlib](human/fichas/qlib.md) | Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [OpenBB Open Data Platform](human/fichas/openbb.md) | Plataforma abierta de datos financieros (ODP): conecta fuentes públicas y con licencia una vez y las expone a Python, Excel, APIs REST y servidores MCP. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [nautilus_trader](human/fichas/nautilus-trader.md) | Motor de trading y backtesting con arquitectura orientada a eventos para investigar y desarrollar estrategias. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [yfinance](human/fichas/yfinance.md) | Biblioteca Python no oficial para descargar datos de mercado y fundamentales de Yahoo! Finance en DataFrames de pandas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [FinRL](human/fichas/finrl.md) | Biblioteca y ejemplos para investigar estrategias de trading mediante aprendizaje por refuerzo y simulaciones. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [vectorbt](human/fichas/vectorbt.md) | Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Backtesting.py](human/fichas/backtesting-py.md) | Framework ligero de Python para hacer backtesting de estrategias de trading sobre datos OHLC, con optimización y gráficos interactivos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [lumibot](human/fichas/lumibot.md) | Framework de Python para desarrollar estrategias, realizar backtesting y conectar simulación u operación con brokers. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [Prediction Market Backtesting](human/fichas/prediction-market-backtesting.md) | Añade ejemplos y componentes de backtesting para analizar mercados de predicción con datos y estrategias históricas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### Bots y conexiones a exchanges

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [freqtrade](human/fichas/freqtrade.md) | Bot de trading de criptomonedas con herramientas para preparar estrategias, hacer backtesting y operar en simulación. | API de IA opcional | 🖥️ app | 🟡 medio |
| [ccxt](human/fichas/ccxt.md) | Biblioteca que unifica APIs de exchanges para consultar mercados y desarrollar integraciones de trading. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [hummingbot](human/fichas/hummingbot.md) | Software para desarrollar y ejecutar bots de trading de criptomonedas mediante conectores y estrategias configurables. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [binance-trader](human/fichas/binance-trader.md) | Bot experimental de Python para estudiar estrategias y automatización con la API de Binance. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [open-sol-bot](human/fichas/open-sol-bot.md) | Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [py-sdk](human/fichas/py-sdk.md) | SDK Python de Polymarket para integrar funciones de su plataforma mediante las APIs y credenciales correspondientes. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### Ejemplos y aprendizaje

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [machine-learning-for-trading](human/fichas/machine-learning-for-trading.md) | Material y código de Machine Learning for Trading para estudiar datos, modelos y evaluación de estrategias. | API de IA opcional | 📂 catálogo/recurso | 🔴 pesado |

## 🗂️ 15. Organizar notas, archivos y servicios personales

_Notas, sincronización, privacidad, aprendizaje y servidores personales. Distingue una aplicación lista, un plugin y la infraestructura que debes administrar._ → [página de la categoría](human/categorias/15-notas-archivos-y-servicios-personales.md)

### Notas, bóvedas y conocimiento personal

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Anytype Desktop](human/fichas/anytype-ts.md) | Cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento personal. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [AppFlowy](human/fichas/appflowy.md) | Espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento propio. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [Memos](human/fichas/memos.md) | App de notas rápidas autoalojada con línea temporal personal, Markdown, etiquetas, compartición controlada, API y servidor MCP. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Joplin](human/fichas/joplin.md) | App de notas y tareas centrada en la privacidad, offline first, con sincronización cifrada de extremo a extremo y apps para escritorio y móvil. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [obsidian-skills](human/fichas/obsidian-skills.md) | Skills para que un agente trabaje con Obsidian y sus formatos de notas, bases de datos y lienzos. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [SiYuan](human/fichas/siyuan.md) | Espacio de conocimiento por bloques, local-first y autoalojable, con referencias bidireccionales, consultas SQL, mapas mentales y funciones de IA. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [Logseq](human/fichas/logseq.md) | Plataforma de gestión del conocimiento local-first en forma de esquema, con páginas enlazadas, diario, consultas y grafo, en Markdown u Org. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Trilium Notes](human/fichas/trilium.md) | App de notas jerárquicas para bases de conocimiento grandes: clonado de notas, scripts, relaciones, mapas y servidor de sincronización autoalojado. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [karakeep](human/fichas/karakeep.md) | Gestor autoalojado de marcadores, notas e imágenes con búsqueda y funciones opcionales de clasificación mediante IA. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [Obsidian: distribución y extensiones](human/fichas/obsidian-releases.md) | Repositorio de distribución de Obsidian y sus listados de plugins y temas; no contiene el código completo de la aplicación. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [claude-obsidian](human/fichas/claude-obsidian.md) | Instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro de una bóveda de notas de Obsidian. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [kepano-obsidian](human/fichas/kepano-obsidian.md) | Plantilla de una bóveda de Obsidian para estudiar una forma de organizar notas e información personal. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [obsidian-minimal](human/fichas/obsidian-minimal.md) | Tema configurable de Obsidian para ajustar la apariencia y reducir distracciones al trabajar con notas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [obsidian-clipper](human/fichas/obsidian-clipper.md) | Extensión oficial para capturar páginas y fragmentos de la web y guardarlos como notas en Obsidian. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [obsidian-second-brain](human/fichas/obsidian-second-brain.md) | Sistema de memoria y notas en Markdown para compartir contexto de trabajo entre agentes y una bóveda de Obsidian. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [obsidian-sample-plugin](human/fichas/obsidian-sample-plugin.md) | Plantilla oficial para programar un plugin de Obsidian con una estructura inicial y configuración de desarrollo. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [jsoncanvas](human/fichas/jsoncanvas.md) | Especificación abierta de JSON Canvas para describir nodos y conexiones de un lienzo visual en un archivo. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [obsidian-help](human/fichas/obsidian-help.md) | Documentación oficial de Obsidian para aprender sus funciones, configuración y formas de organizar una bóveda. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [obsidian-importer](human/fichas/obsidian-importer.md) | Plugin oficial para convertir datos de otras aplicaciones en archivos Markdown que puedes abrir en Obsidian. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Sincronización y gestión de archivos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Immich](human/fichas/immich.md) | Gestión autoalojada de fotos y vídeos de alto rendimiento, alternativa a Google Photos, con copia automática desde el móvil y búsqueda con IA local. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [syncthing](human/fichas/syncthing.md) | Aplicación para sincronizar archivos entre dispositivos directamente y controlar qué carpetas se comparten. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [PhotoPrism](human/fichas/photoprism.md) | App de fotos con IA y privacidad primero para explorar, organizar y compartir fotos y vídeos, autoalojada o en la nube. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [server](human/fichas/nextcloud-server.md) | Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |

### Credenciales y privacidad

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [vaultwarden](human/fichas/vaultwarden.md) | Servidor no oficial compatible con clientes Bitwarden para alojar una bóveda de credenciales en infraestructura propia. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Pi-hole](human/fichas/pi-hole.md) | Sumidero DNS para bloquear anuncios y rastreadores en toda la red sin instalar nada en los dispositivos, con panel web y DHCP opcional. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [AdGuardHome](human/fichas/adguardhome.md) | Servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una red desde una configuración central. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Keycloak](human/fichas/keycloak.md) | IdP estándar de la industria (Red Hat/CNCF): OIDC, SAML, federación y admin amplio en Java. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | hard |
| [HashiCorp Vault](human/fichas/vault.md) | Gestión de secretos y cifrado como servicio: dinámicos, KV, PKI. BSL 1.1 desde 1.15+ (IBM); no es OSI open source puro. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | hard |
| [KeePassXC](human/fichas/keepassxc.md) | Gestor de contraseñas local multiplataforma (fork comunitario de KeePassX) con TOTP, SSH agent y navegador. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [authentik](human/fichas/authentik.md) | IdP/SSO open source (MIT núcleo; enterprise/ bajo licencia distinta): OAuth2, SAML, LDAP y flujos visuales. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | hard |
| [age](human/fichas/age.md) | Cifrado de ficheros moderno y simple (clave/recipient) sin OpenPGP: CLI pequeña y auditable. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [SOPS](human/fichas/sops.md) | Cifra secretos en YAML/JSON/ENV para GitOps con claves age, PGP o KMS; integrado en flujos CI. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Bitwarden Clients](human/fichas/bitwarden-clients.md) | Clientes oficiales de Bitwarden para gestionar credenciales y utilizar funciones como compartir información con Send. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Libros, podcasts y bibliotecas personales

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Jellyfin](human/fichas/jellyfin.md) | Sistema multimedia libre para gestionar y transmitir películas, series, música y libros desde tu servidor, alternativa a Plex y Emby. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Calibre-Web](human/fichas/calibre-web.md) | Aplicación web para explorar, leer y descargar libros electrónicos de una base de datos de Calibre, con usuarios, OPDS y lector en el navegador. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [audiobookshelf](human/fichas/audiobookshelf.md) | Servidor personal para organizar audiolibros y podcasts, escuchar contenido y conservar el progreso de reproducción. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Kavita](human/fichas/kavita.md) | Servidor de lectura rápido y multiplataforma para manga, cómics y libros, con lector web, usuarios, OPDS y metadatos. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |

### Automatización del hogar

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Home Assistant](human/fichas/home-assistant.md) | Motor de Home Assistant para conectar dispositivos y automatizar acciones del hogar con control local. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [Frigate NVR](human/fichas/frigate.md) | Grabador de vídeo en red (NVR) local con detección de objetos por IA en tiempo real para cámaras IP, integrado con Home Assistant. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Zigbee2MQTT](human/fichas/zigbee2mqtt.md) | Puente de Zigbee a MQTT para usar dispositivos Zigbee de muchas marcas sin pasarelas propietarias, integrable con Home Assistant y otros. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [ESPHome](human/fichas/esphome.md) | Sistema para crear firmware de ESP32, ESP8266, RP2040 y otros microcontroladores con archivos YAML y controlarlos desde Home Assistant. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |

### Herramientas y organización personal

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [ai-job-search](human/fichas/ai-job-search.md) | Proyecto basado en Claude Code para evaluar vacantes, adaptar currículums y preparar cartas e entrevistas de empleo. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [cleanyourtv](human/fichas/cleanyourtv.md) | Herramienta para revisar y retirar aplicaciones preinstaladas de dispositivos Android TV o Google TV mediante ADB. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Actual Budget](human/fichas/actual.md) | App de finanzas personales local-first basada en presupuesto por sobres, con sincronización entre dispositivos y servidor autoalojable. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Firefly III](human/fichas/firefly-iii.md) | Gestor autoalojado de finanzas personales con contabilidad de doble entrada, presupuestos, reglas, informes y API, sin IA ni nube. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [optimizerDuck](human/fichas/optimizerduck.md) | Aplicación para revisar y ajustar opciones de rendimiento, privacidad y configuración de un equipo con Windows. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [universal-android-debloater-next-generation](human/fichas/universal-android-debloater-next-generation.md) | Interfaz para revisar y retirar paquetes preinstalados de dispositivos Android mediante ADB y listas de aplicaciones. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Ghostfolio](human/fichas/ghostfolio.md) | Software abierto de gestión de patrimonio para seguir acciones, ETF y criptomonedas con métricas de rendimiento, autoalojado o en la nube. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [iSponsorBlockTV](human/fichas/isponsorblocktv.md) | Usa la base de SponsorBlock para saltar segmentos marcados durante la reproducción de YouTube en televisores compatibles. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [40-questions](human/fichas/40-questions.md) | Colección de preguntas para revisar un año o una década y reflexionar sobre objetivos, hábitos y decisiones personales. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Aprendizaje asistido

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [OpenMAIC](human/fichas/openmaic.md) | Aplicación educativa con varios agentes que prepara clases y actividades mediante modelos y recursos configurables. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |

## 🔍 16. Analizar software y comprobar su seguridad

_Depuradores, descompiladores, análisis de binarios, pruebas de intrusión, detección y seguridad de nube. Trabaja sobre sistemas propios o con autorización escrita y separa análisis, pruebas activas y defensa._ → [página de la categoría](human/categorias/16-analisis-de-software-y-seguridad.md)

### Ingeniería inversa y formatos binarios

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [ghidra](human/fichas/ghidra.md) | Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [ImHex](human/fichas/imhex.md) | Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras y describir formatos mediante patrones. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [jadx](human/fichas/jadx.md) | Descompilador de archivos DEX y APK para explorar código Java reconstruido y recursos de aplicaciones Android. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Apktool](human/fichas/apktool.md) | Herramienta para decodificar recursos y reconstruir paquetes APK de Android durante el análisis de una aplicación. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [ILSpy](human/fichas/ilspy.md) | Descompilador de .NET para explorar ensamblados y estudiar el código y metadatos de aplicaciones compatibles. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [radare2](human/fichas/radare2.md) | Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [frida](human/fichas/frida.md) | Herramientas de instrumentación dinámica para observar y modificar el comportamiento de programas durante su ejecución. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [YARA](human/fichas/yara.md) | Motor de reglas para identificar malware y artefactos por patrones de bytes, strings y condiciones lógicas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [angr](human/fichas/angr.md) | Plataforma en Python para analizar programas binarios mediante técnicas como ejecución simbólica y análisis de flujo. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [capa](human/fichas/capa.md) | Detecta capacidades en binarios/malware (anti-debug, C2, persistencia…) mediante reglas y análisis estático. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [rizin](human/fichas/rizin.md) | Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |

### Depuración e inspección de procesos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [x64dbg](human/fichas/x64dbg.md) | Depurador de Windows para inspeccionar programas en ejecución y estudiar instrucciones, memoria y llamadas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [dnSpyEx](human/fichas/dnspy.md) | Depurador y editor de ensamblados .NET para inspeccionar y analizar aplicaciones de esa plataforma. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [pwndbg](human/fichas/pwndbg.md) | Mejoras para GDB/LLDB orientadas a exploit-dev: heap, ROPgadget, contexto de registros y más. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [raddebugger](human/fichas/raddebugger.md) | Depurador gráfico nativo para inspeccionar procesos, código y memoria durante el análisis de programas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Tráfico, rendimiento y pruebas

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [mitmproxy](human/fichas/mitmproxy.md) | Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [sqlmap](human/fichas/sqlmap.md) | Herramienta de pruebas de penetración que detecta y explota automáticamente inyecciones SQL y permite tomar el control de servidores de bases de datos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Nuclei](human/fichas/nuclei.md) | Escáner de vulnerabilidades rápido basado en plantillas YAML de la comunidad para aplicaciones, APIs, redes, DNS y configuraciones cloud. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [k6](human/fichas/k6.md) | Herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de tráfico. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Locust](human/fichas/locust.md) | Herramienta de pruebas de carga y rendimiento donde los escenarios de usuario se escriben en Python normal, con interfaz web en tiempo real. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [hashcat](human/fichas/hashcat.md) | Utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más de 630 modos de hash y 10 modos de ataque. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [bettercap](human/fichas/bettercap.md) | Framework MITM/red/Wi-Fi: sniffing, proxying y ataques de red en ejercicios con autorización escrita. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [ffuf](human/fichas/ffuf.md) | Fuzzer web rápido en Go para descubrir contenido, hosts virtuales y parámetros, con filtros, modo interactivo y proxy. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [ZAP (Zed Attack Proxy)](human/fichas/zaproxy.md) | Escáner de seguridad de aplicaciones web más usado (antes OWASP ZAP, ahora ZAP by Checkmarx): proxy interceptor, araña y escaneo activo. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [dirsearch](human/fichas/dirsearch.md) | Dirbuster en Python ampliamente usado para descubrir rutas y ficheros en aplicaciones web de laboratorio. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OWASP Juice Shop](human/fichas/juice-shop.md) | Aplicación web vulnerable oficial de OWASP para entrenar AppSec: cientos de retos y puntuación. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Gobuster](human/fichas/gobuster.md) | Fuzzing y descubrimiento de directorios, DNS y buckets en Go; clásico de pentest web autorizado. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [John the Ripper (jumbo)](human/fichas/john.md) | Crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo: cientos de tipos de hash y cifrado, CPU, GPU y FPGA. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [pwntools](human/fichas/pwntools.md) | Framework Python para CTF y desarrollo de exploits: tubos, packing, ROP y utilidades de binarios. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [THC Hydra](human/fichas/thc-hydra.md) | Fuerza bruta multi-protocolo (SSH, HTTP, FTP…) solo contra objetivos con autorización explícita. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Wireshark](human/fichas/wireshark.md) | Analizador de protocolos de red de referencia: captura y decodifica paquetes de cientos de protocolos, con TShark para línea de comandos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [WPScan](human/fichas/wpscan.md) | Escáner de WordPress: usuarios, temas, plugins y vulns vía API (25 req/día gratis; DB Enterprise de pago). | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [WebGoat](human/fichas/webgoat.md) | Aplicación web deliberadamente insegura de OWASP con lecciones guiadas para aprender y practicar vulnerabilidades del Top 10. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [feroxbuster](human/fichas/feroxbuster.md) | Dirbuster rápido en Rust con recursión, filtros y salidas flexibles para descubrimiento de contenidos web. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Aircrack-ng](human/fichas/aircrack-ng.md) | Suite de auditoría Wi-Fi (captura, ataque a handshakes, cracking) solo sobre redes propias o autorizadas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [AFL++](human/fichas/aflplusplus.md) | Fuzzer de cobertura de referencia (AFL++) para encontrar crashes en software propio o autorizado. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [syzkaller](human/fichas/syzkaller.md) | Fuzzer de kernels (Linux y otros) de Google: encuentra bugs de syscall a gran escala; infraestructura pesada. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [OWASP Nettacker](human/fichas/nettacker.md) | Marco OWASP de pruebas de penetración automatizadas: escaneo de puertos, subdominios, servicios y vulnerabilidades con módulos YAML. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Caido](human/fichas/caido.md) | Proxy de pentest web moderno (alternativa a Burp): core HTTP gratis (Basic); Individual/Team/Enterprise de pago. No es open source. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OWASP OWTF](human/fichas/owtf.md) | Offensive Web Testing Framework de OWASP: orquesta herramientas de pentest web siguiendo la WSTG y PTES desde una interfaz web. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [OWASP crAPI](human/fichas/crapi.md) | API deliberadamente vulnerable de OWASP (completely ridiculous API) para practicar los riesgos del API Security Top 10. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [OWASP WrongSecrets](human/fichas/wrongsecrets.md) | Aplicación vulnerable de OWASP con retos sobre cómo no gestionar secretos en código, contenedores, Kubernetes, nube y binarios. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OWASP secureCodeBox](human/fichas/securecodebox.md) | Orquesta escáneres de seguridad (Nmap, ZAP, Nuclei, Trivy y otros) en Kubernetes para automatizar análisis continuos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |

### Reconocimiento y superficie de ataque

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [masscan](human/fichas/masscan.md) | Escáner de puertos a escala Internet (AGPL): asíncrono y muy rápido; peligroso si se apunta fuera de alcance. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [RustScan](human/fichas/rustscan.md) | Escaneo de puertos ultrarrápido en Rust que encadena automáticamente a Nmap para el detalle de servicios. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Amass](human/fichas/amass.md) | Mapea la superficie de ataque externa: subdominios, ASNs, certificados y hosts descubiertos a partir de OSINT y sondeos activos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [subfinder](human/fichas/subfinder.md) | Herramienta rápida de enumeración pasiva de subdominios a partir de fuentes públicas en línea, diseñada para encadenarse con otras. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Nmap](human/fichas/nmap.md) | El escáner de red de referencia: descubre hosts, puertos, servicios y sistemas operativos, con scripts NSE para detección avanzada. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [httpx](human/fichas/httpx.md) | Sondea URLs y hosts HTTP/HTTPS a gran velocidad: códigos, títulos, tecnologías y cadenas de redirección para filtrar activos vivos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Naabu](human/fichas/naabu.md) | Escáner de puertos SYN/CONNECT/UDP en Go, ligero y pensado para encadenarse con Nmap y con Nuclei. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [interactsh](human/fichas/interactsh.md) | Servidor de callbacks OOB para detectar SSRF, XXE y vulnerabilidades ciegas con correlaciones HTTP/DNS/SMTP. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [dnsx](human/fichas/dnsx.md) | Resolución DNS masiva del ecosistema ProjectDiscovery: A/AAAA/CNAME y más, lista para encadenar con Subfinder y httpx. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Explotación, C2 y post-explotación

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Metasploit Framework](human/fichas/metasploit.md) | Framework de referencia para pruebas de penetración: módulos de exploits, cargas útiles, escáneres y post-explotación con consola interactiva. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [PEASS-ng](human/fichas/peass-ng.md) | LinPEAS/WinPEAS: scripts y binarios que enumeran rutas de escalada de privilegios en hosts Linux/Windows/macOS comprometidos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Evilginx2](human/fichas/evilginx2.md) | Proxy de phishing que captura credenciales y cookies de sesión (bypass MFA) en simulaciones de ingeniería social autorizadas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [SET](human/fichas/social-engineer-toolkit.md) | Toolkit clásico de ingeniería social (TrustedSec): plantillas de phishing y vectores solo con consentimiento. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Atomic Red Team](human/fichas/atomic-red-team.md) | Biblioteca de pruebas ATT&CK pequeñas y documentadas para validar detecciones y controles en un laboratorio propio. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |
| [Sliver](human/fichas/sliver.md) | Framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [CALDERA](human/fichas/caldera.md) | Framework Apache de emulación de adversario automatizado: agentes, adversarios ATT&CK y operaciones controladas desde web. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Empire](human/fichas/empire.md) | Framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma para labs autorizados. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Ligolo-ng](human/fichas/ligolo-ng.md) | Túneles de pivoting modernos (agente/proxy) para moverse por redes de un alcance de pentest autorizado. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Mythic](human/fichas/mythic.md) | Framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía mythic-cli. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |

### Active Directory y red interna

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [mimikatz](human/fichas/mimikatz.md) | Referencia para extracción de credenciales Windows (LSASS, tickets, DCSync) en laboratorios aislados. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Impacket](human/fichas/impacket.md) | Biblioteca Python de protocolos Windows (SMB, MSRPC, Kerberos…) usada como base de casi todo el tooling de Active Directory. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [GOAD](human/fichas/goad.md) | Lab Active Directory vulnerable (Orange Cyberdefense) para practicar ataques AD en VMs locales aisladas. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | hard |
| [Responder](human/fichas/responder.md) | Envenena LLMNR/NBT-NS/mDNS y captura hashes en redes internas de laboratorio. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [NetExec](human/fichas/netexec.md) | Suite de post-explotación y enumeración de redes Windows/AD (sucesora de CrackMapExec) para validar credenciales y movimientos laterales. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Rubeus](human/fichas/rubeus.md) | Toolkit C# de abuso Kerberos (TGT/TGS, kerberoast, AS-REP) para laboratorios AD autorizados. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Certipy](human/fichas/certipy.md) | Enumeración y abuso de Active Directory Certificate Services (AD CS) en laboratorios autorizados. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [BloodHound Community Edition](human/fichas/bloodhound.md) | Aplicación de análisis de rutas de ataque basada en grafos para Active Directory, Entra ID y otros sistemas de identidad (edición comunitaria). | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |

### Detección, SIEM e IDS

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [osquery](human/fichas/osquery.md) | Instrumenta el endpoint como base SQL: procesos, sockets, usuarios y más, base de muchos EDR y hunts. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Fail2ban](human/fichas/fail2ban.md) | Bloquea IPs tras intentos fallidos de autenticación leyendo logs (ssh, web…); defensa clásica de hosts. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Wazuh](human/fichas/wazuh.md) | Plataforma de seguridad abierta con SIEM y XDR: agentes en los equipos, detección de intrusiones, integridad de archivos, vulnerabilidades y cumplimiento. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [CrowdSec](human/fichas/crowdsec.md) | IDS/IPS, WAF y detección de bots abiertos con lista de bloqueo colaborativa de IP maliciosas, para Linux, Windows, Docker y Kubernetes. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Sigma](human/fichas/sigma.md) | Formato y reglas de detección SIEM multi-vendor: escribe una vez, convierte a Elastic, Splunk, QRadar, etc. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |
| [ModSecurity](human/fichas/modsecurity.md) | Motor WAF de código abierto (libmodsecurity v3) que inspecciona peticiones HTTP con reglas SecLang como el OWASP Core Rule Set. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | hard |
| [Zeek](human/fichas/zeek.md) | Analizador de tráfico de red (ex Bro): telemetría rica de protocolos para caza de amenazas y forense de red. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Arkime](human/fichas/arkime.md) | Captura e indexación de PCAP a escala (ex Moloch) con UI de búsqueda para NSM/forense de red. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Suricata](human/fichas/suricata.md) | IDS/IPS y motor de inspección de tráfico de red de referencia (OISF): firmas, protocolos y captura a alta velocidad. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Security Onion](human/fichas/securityonion.md) | Distribución SOC completa (Suricata/Zeek/Elastic…) para laboratorios y sensores; pesada en recursos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [OWASP Coraza](human/fichas/coraza.md) | WAF en Go compatible con ModSecurity SecLang y el OWASP Core Rule Set, embebible en servidores y proxies como Caddy, Envoy o Traefik. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [OWASP CRS](human/fichas/coreruleset.md) | Reglas WAF OWASP (Core Rule Set) para ModSecurity/Coraza: protege apps web con firmas comunitarias. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |
| [Elastic detection-rules](human/fichas/detection-rules.md) | Reglas de detección de Elastic Security (ELv2): punto de partida para SIEM Elastic; licencia no OSI. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |
| [Shuffle](human/fichas/shuffle.md) | SOAR open source (AGPL): automatiza playbooks de respuesta conectando tools de seguridad vía workflows. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Pi.Alert](human/fichas/pi-alert-leiweibau.md) | Lleva un inventario de dispositivos de una red propia y avisa cuando aparece uno nuevo o deja de responder uno conocido. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |

### Nube, contenedores e IaC

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Trivy](human/fichas/trivy.md) | Escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC, secretos y licencias en imágenes, repositorios, Kubernetes y nube. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Prowler](human/fichas/prowler.md) | Auditoría multi-cloud open source (AWS, Azure, GCP…) de configuración y marcos CIS: CLI Apache-2.0; Cloud/Private Cloud son de pago. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Grype](human/fichas/grype.md) | Escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja paquetes con CVE y prioriza remediación. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OSV-Scanner](human/fichas/osv-scanner.md) | Escáner SCA de Google contra la base OSV: lockfiles, imágenes y directorios de código. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Syft](human/fichas/syft.md) | Genera SBOMs (Software Bill of Materials) de imágenes, directorios y remotes para alimentar Grype u otros scanners. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Falco](human/fichas/falco.md) | Runtime security para contenedores y Linux: reglas que alertan sobre syscalls anómalas en nodos y clústeres Kubernetes. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Checkov](human/fichas/checkov.md) | SAST de infraestructura como código: Terraform, Kubernetes, CloudFormation y más, con políticas de misconfig y secretos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [kube-bench](human/fichas/kube-bench.md) | Comprueba un clúster Kubernetes contra el CIS Kubernetes Benchmark y reporta fallos de configuración. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Cosign](human/fichas/cosign.md) | Firma y verificación de contenedores y artefactos (Sigstore): clave o keyless con OIDC. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Pacu](human/fichas/pacu.md) | Framework de explotación AWS (Rhino Security Labs) para auditorías ofensivas en cuentas de prueba dedicadas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [ScubaGear](human/fichas/scubagear.md) | Auditoría PowerShell de configuración Microsoft 365 (CISA SCuBA) contra baselines de seguridad. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |

### Análisis y pruebas con agentes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [rea](human/fichas/rea.md) | Herramientas e instrucciones para estudiar el comportamiento y la estructura de software mediante agentes de código. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [strix](human/fichas/strix.md) | Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [shannon](human/fichas/shannon.md) | Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [craft-anything](human/fichas/craft-anything.md) | Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [garak](human/fichas/garak.md) | Escáner de vulnerabilidades de LLM de NVIDIA: prueba jailbreaks, inyección de prompts, fugas de datos, alucinaciones y toxicidad con sondas automáticas. | API de IA opcional | 🖥️ app | 🟡 medio |

### Protección y verificación de software

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Semgrep](human/fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Lynis](human/fichas/lynis.md) | Herramienta de auditoría de seguridad y endurecimiento para Linux, macOS y otros Unix, sin agente, que sugiere mejoras concretas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OWASP Dependency-Check](human/fichas/dependency-check.md) | Análisis de composición de software (SCA) de OWASP: detecta dependencias con CVE publicados en Java, .NET, JavaScript, Python y más. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [bla](human/fichas/bla.md) | Herramientas para aplicar protecciones y comprobar superficies de software frente a análisis automatizado por agentes. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [DefectDojo](human/fichas/defectdojo.md) | Gestor OWASP de vulnerabilidades y DevSecOps: importa resultados de más de 200 escáneres, deduplica hallazgos y sigue su corrección. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Dependency-Track](human/fichas/dependency-track.md) | Plataforma OWASP que ingiere SBOM CycloneDX y vigila de forma continua vulnerabilidades, licencias y riesgo de los componentes de tus proyectos. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [OWASP Threat Dragon](human/fichas/threat-dragon.md) | Herramienta OWASP de modelado de amenazas: diagramas de flujo de datos con amenazas STRIDE, LINDDUN o CIA, en escritorio o web. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OWASP Noir](human/fichas/noir.md) | Descubre endpoints y parámetros en el código fuente (y API ocultas) para mapear la superficie de ataque y alimentar pruebas DAST. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OWASP dep-scan](human/fichas/dep-scan.md) | Auditoría OWASP de riesgo en dependencias: vulnerabilidades, avisos, licencias y alcanzabilidad a partir de SBOM CycloneDX generados con cdxgen. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OWASP pytm](human/fichas/pytm.md) | Modelado de amenazas como código en Python: describe el sistema y obtén diagramas de flujo, secuencia y un informe de amenazas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [cdxgen](human/fichas/cdxgen.md) | Generador de SBOM CycloneDX del ecosistema OWASP para código fuente, contenedores y binarios en decenas de lenguajes y gestores de paquetes. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OWASP Java HTML Sanitizer](human/fichas/java-html-sanitizer.md) | Biblioteca Java de OWASP que limpia HTML de terceros con políticas configurables para incrustarlo sin riesgo de XSS. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [OWASP Java Encoder](human/fichas/owasp-java-encoder.md) | Codificación contextual de salida para Java (HTML, JavaScript, CSS, XML, URI) que previene XSS, sin dependencias en tiempo de ejecución. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |

### Directorios y aprendizaje

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [PayloadsAllTheThings](human/fichas/payloadsallthethings.md) | Enciclopedia práctica de payloads y técnicas web (XSS, SQLi, SSRF…) mantenida por la comunidad de pentest. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [SecLists](human/fichas/seclists.md) | Colección OWASP de wordlists y payloads (dirs, users, passwords, fuzzing) de referencia para pruebas autorizadas. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP CheatSheet Series](human/fichas/cheatsheetseries.md) | Cheatsheets OWASP de desarrollo seguro: ASVS, auth, XSS, secrets… orientadas a builders y defensores. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP MASTG](human/fichas/mastg.md) | Guía OWASP de pruebas de seguridad de apps móviles (Android e iOS): técnicas, herramientas y casos de prueba ligados a MASVS. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [HackTricks](human/fichas/hacktricks.md) | Wiki práctica de pentest y privilege escalation (book.hacktricks.xyz) con técnicas actualizadas por la comunidad. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP Web Security Testing Guide](human/fichas/wstg.md) | Guía OWASP de referencia para probar la seguridad de aplicaciones web: metodología y casos de prueba con identificadores WSTG. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP Top 10](human/fichas/owasp-top10.md) | Documento de concienciación de OWASP con los diez riesgos más críticos en aplicaciones web, con ejemplos, prevención y CWE asociados. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP ASVS](human/fichas/asvs.md) | Estándar OWASP de verificación de seguridad de aplicaciones: requisitos verificables en tres niveles para diseñar, desarrollar y auditar. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP MASVS](human/fichas/masvs.md) | Estándar OWASP de verificación de seguridad de aplicaciones móviles: controles para almacenamiento, criptografía, red, plataforma y resiliencia. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP API Security Top 10](human/fichas/owasp-api-security.md) | Top 10 de OWASP sobre riesgos de seguridad en API: autorización a nivel de objeto, autenticación rota, consumo de recursos y más. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP Developer Guide](human/fichas/owasp-devguide.md) | Guía OWASP para desarrolladores: principios de seguridad, requisitos, diseño, implementación, verificación y proyectos OWASP útiles en cada fase. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [awesome-reverse-engineering](human/fichas/awesome-reverse-engineering.md) | Directorio de herramientas y recursos para aprender análisis de binarios, aplicaciones, firmware y protocolos. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP Top 10 for LLM Applications](human/fichas/owasp-llm-top10.md) | Top 10 de riesgos de seguridad en aplicaciones con LLM y GenAI (inyección de prompts, fuga de datos, agencia excesiva) del GenAI Security Project. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP AI Testing Guide](human/fichas/owasp-ai-testing-guide.md) | Metodología OWASP para evaluar la seguridad y fiabilidad de sistemas de IA: casos de prueba para aplicación, modelo, infraestructura y datos. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [OWASP AISVS](human/fichas/aisvs.md) | Estándar OWASP de verificación de seguridad para sistemas de IA: requisitos verificables para datos, modelos, agentes e infraestructura. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [awesome-ai-reverse-engineering](human/fichas/awesome-ai-reverse-engineering.md) | Directorio de herramientas de ingeniería inversa y análisis de software que pueden trabajar con agentes de IA. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Skills de análisis y seguridad

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [security-audit-skill](human/fichas/security-audit-skill.md) | Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [Cybersecurity Skills (comunidad)](human/fichas/cybersecurity-skills.md) | Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [SkillSpector](human/fichas/skillspector.md) | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [Defending Code Reference Harness](human/fichas/defending-code-reference-harness.md) | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades. | Depende de la ruta elegida | 🎨 skill/prompt | 🟡 medio |

### Respuesta a incidentes y forense

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Volatility 3](human/fichas/volatility3.md) | Framework forense de memoria RAM (v3): analiza dumps Windows/Linux/macOS para procesos, redes y malware. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Velociraptor](human/fichas/velociraptor.md) | EDR/IR open source para recolección forense a escala: consultas VQL sobre endpoints Windows, Linux y macOS. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Hayabusa](human/fichas/hayabusa.md) | Triaje forense de event logs Windows con reglas Sigma: rápido, firmado y orientado a DFIR. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Autopsy](human/fichas/autopsy.md) | GUI forense sobre The Sleuth Kit: casos, timelines e ingest modules para investigar discos en laboratorio. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [The Sleuth Kit](human/fichas/sleuthkit.md) | Toolkit forense de sistemas de archivos: recupera y analiza particiones, ficheros borrados y metadatos en evidencias de disco. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### Inteligencia de amenazas

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [OpenCTI](human/fichas/opencti.md) | Plataforma de threat intel orientada a grafos (Filigran): Community Edition Apache-2.0; Enterprise añade playbooks, SSO, IA y más bajo licencia EE. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | hard |
| [MISP](human/fichas/misp.md) | Plataforma de intercambio de threat intelligence: eventos, IOCs, taxonomías y sincronización entre organizaciones. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | hard |

## 🤖 17. WhatsApp, mensajería y chatbots

_Conecta WhatsApp y otros canales o prepara un chatbot. Distingue el canal de mensajes, el modelo que responde y la bandeja donde una persona retoma la conversación._ → [página de la categoría](human/categorias/17-mensajeria-chatbots.md)

### WhatsApp y mensajería

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [whatsapp-web.js](human/fichas/whatsapp-web-js.md) | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [OpenWA](human/fichas/openwa.md) | Gateway autoalojado de WhatsApp con API, panel de sesiones y servidor MCP HTTP opcional, del proyecto rmyndharis/OpenWA. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Baileys](human/fichas/baileys.md) | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [evolution-api](human/fichas/evolution-api.md) | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [whatsmeow](human/fichas/whatsmeow.md) | Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [WAHA](human/fichas/waha.md) | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [signal-cli](human/fichas/signal-cli.md) | Interfaz de línea de comandos y API (JSON-RPC y D-Bus) no oficial para registrar, verificar, enviar y recibir mensajes de Signal. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [whatsapp-agentkit](human/fichas/whatsapp-agentkit.md) | Instrucciones y scripts que guían a Claude Code para construir un bot de WhatsApp; el bot resultante necesita sus propios proveedores y credenciales. | API de IA necesaria | 🎨 skill/prompt | 🟢 fácil |

### Chatbots y asistentes conversacionales

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Typebot](human/fichas/typebot.md) | Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [python-telegram-bot](human/fichas/python-telegram-bot.md) | Biblioteca Python asíncrona de referencia para crear bots de Telegram, con cobertura completa de la Bot API y utilidades de alto nivel. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [discord.js](human/fichas/discord-js.md) | Módulo Node.js de referencia para interactuar con la API de Discord y crear bots, con paquetes para voz, REST y gateway. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Botpress](human/fichas/botpress.md) | Hub de SDKs, CLI e integraciones para desarrollar y desplegar conexiones en el ecosistema Botpress. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |

### Comunidades,chat y llamadas

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Rocket.Chat](human/fichas/rocket-chat.md) | Plataforma de comunicación autoalojable para equipos y atención al cliente, con chat, llamadas, federación, omnicanal y marketplace de apps. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Mattermost](human/fichas/mattermost.md) | Plataforma de colaboración autoalojada y open core, alternativa a Slack: chat, automatización de flujos, llamadas, pantalla compartida e integración con IA. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Zulip](human/fichas/zulip.md) | Chat de equipo open source con hilos por tema: combina lo mejor del email y del chat para trabajo remoto. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | hard |
| [Element Web](human/fichas/element-web.md) | Cliente web Matrix (Element): chats, salas y cifrado E2E contra un homeserver como Synapse. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [fluxer](human/fichas/fluxer.md) | Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Synapse](human/fichas/synapse.md) | Servidor doméstico de Matrix de referencia, mantenido por Element: chat federado, abierto e interoperable que puedes alojar tú mismo. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |

## 🤖 18. CRM, ventas y marketing

_Gestiona clientes, soporte, campañas, correo y publicaciones. Un CRM guarda la relación con el cliente; una herramienta de campañas distribuye mensajes. Comprueba los servicios externos y sus tarifas._ → [página de la categoría](human/categorias/18-crm-ventas-marketing.md)

### CRM, ERP y soporte al cliente

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Odoo](human/fichas/odoo.md) | Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [twenty-main](human/fichas/twenty-main.md) | CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [ERPNext](human/fichas/erpnext.md) | ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [chatwoot](human/fichas/chatwoot.md) | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [crm](human/fichas/compai-crm.md) | CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [Zammad](human/fichas/zammad.md) | Sistema de helpdesk y tickets autoalojado y omnicanal: correo, chat, teléfono y redes sociales en una sola interfaz web. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [SuiteCRM](human/fichas/suitecrm.md) | CRM open source clásico (fork de SugarCRM): contactos, oportunidades, casos y portal en PHP. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [FreeScout](human/fichas/freescout.md) | Helpdesk y bandeja de entrada compartida muy ligera, alternativa abierta a Help Scout y Zendesk, en PHP y desplegable incluso en hosting compartido. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [EspoCRM](human/fichas/espocrm.md) | CRM web ligero y autoalojable para gestionar contactos, cuentas, oportunidades y actividades, con API REST y personalización sin código. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |

### Email, marketing y notificaciones

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [novu](human/fichas/novu.md) | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [postiz-app](human/fichas/postiz-app.md) | Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [open-seo](human/fichas/open-seo.md) | Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [listmonk](human/fichas/listmonk.md) | Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [cloud-mail](human/fichas/cloud-mail.md) | Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [mautic](human/fichas/mautic.md) | Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [sellbird](human/fichas/sellbird.md) | Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |

### Reservas y programación de citas

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [cal.diy](human/fichas/cal-diy.md) | Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Easy!Appointments](human/fichas/easyappointments.md) | Aplicación web autoalojada de reserva de citas: clientes reservan online según la disponibilidad de proveedores y servicios, con sincronización con Google Calendar. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |

### Encuestas y feedback

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Formbricks](human/fichas/formbricks.md) | Encuestas y experience management open source (alternativa a Qualtrics): formularios, in-app surveys y analitica autoalojable. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |

## 🧠 19. Aprender IA y escribir mejores prompts

_Cursos, ejemplos, guías y colecciones de prompts. Son material de aprendizaje: cada ejemplo puede necesitar sus propias cuentas, dependencias o modelos._ → [página de la categoría](human/categorias/19-aprender-ia-prompts.md)

### Prompts y prompt engineering

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Prompt Engineering Guide](human/fichas/prompt-engineering-guide.md) | Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| ⭐ [Fabric](human/fichas/fabric.md) | CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [prompts.chat](human/fichas/prompts-chat.md) | La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [system-prompts-and-models-of-ai-tools](human/fichas/system-prompts-and-models-of-ai-tools.md) | Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [prompt-master](human/fichas/prompt-master.md) | Skill de Claude que ayuda a formular encargos para distintas herramientas de IA; no garantiza ahorro de tokens. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [ChatGPT_DAN](human/fichas/chatgpt-dan.md) | Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [chatgpt_system_prompt](human/fichas/chatgpt-system-prompt.md) | Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Guías, cursos y cookbooks

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Generative AI for Beginners](human/fichas/generative-ai-for-beginners.md) | Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. | API de IA opcional | 📂 catálogo/recurso | 🟢 fácil |
| ⭐ [AI Agents for Beginners](human/fichas/ai-agents-for-beginners.md) | Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español. | API de IA opcional | 📂 catálogo/recurso | 🟡 medio |
| [Awesome LLM Apps](human/fichas/awesome-llm-apps.md) | Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. | API de IA opcional | 📂 catálogo/recurso | 🟡 medio |
| [OpenAI Cookbook](human/fichas/openai-cookbook.md) | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. | API de IA opcional | 📂 catálogo/recurso | 🟢 fácil |
| [Claude Cookbooks](human/fichas/claude-cookbooks.md) | Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización. | API de IA opcional | 📂 catálogo/recurso | 🟢 fácil |
| [ai-engineering-hub](human/fichas/ai-engineering-hub.md) | Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial. | API de IA opcional | 📂 catálogo/recurso | 🟢 fácil |
| [500-AI-Agents-Projects](human/fichas/500-ai-agents-projects.md) | Colección de casos de uso y agentes autocontenidos, junto con enlaces a implementaciones externas. | API de IA opcional | 📂 catálogo/recurso | 🟢 fácil |
| [Hugging Face Agents Course](human/fichas/agents-course.md) | Curso oficial y gratuito de agentes de IA de Hugging Face: de los fundamentos a smolagents, LangGraph y LlamaIndex, con proyecto final certificable. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [12-Factor Agents](human/fichas/12-factor-agents.md) | Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12 Factor Apps. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [Agents Towards Production](human/fichas/agents-towards-production.md) | Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad, trazas y evaluación. | API de IA opcional | 📂 catálogo/recurso | 🟡 medio |
| [claude-quickstarts](human/fichas/claude-quickstarts.md) | Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora. | API de IA opcional | 📂 catálogo/recurso | 🟡 medio |
| [Loop Engineering](human/fichas/loop-engineering.md) | Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [Context-Engineering](human/fichas/context-engineering.md) | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [awesome-harness-engineering](human/fichas/awesome-harness-engineering.md) | Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Aprender LLMs desde cero

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [LLM Course](human/fichas/llm-course.md) | Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. | API de IA opcional | 📂 catálogo/recurso | 🟢 fácil |
| [LLMs from Scratch](human/fichas/llms-from-scratch.md) | Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. | API de IA opcional | 📂 catálogo/recurso | 🟡 medio |
| [ML for Beginners](human/fichas/ml-for-beginners.md) | Curso gratuito de Microsoft de 12 semanas y 26 lecciones de machine learning clásico, con cuestionarios, en Python y R. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [awesome-machine-learning](human/fichas/awesome-machine-learning.md) | Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [labml.ai Annotated Paper Implementations](human/fichas/annotated-dl-papers.md) | Más de 60 implementaciones sencillas en PyTorch de papers de deep learning con notas explicativas lado a lado: transformers, optimizadores, GAN, RL y más. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [nanochat](human/fichas/nanochat.md) | Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [llm.c](human/fichas/llm-c.md) | Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [train-llm-from-scratch](human/fichas/train-llm-from-scratch.md) | Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🔴 pesado |
| [how-to-train-your-gpt](human/fichas/how-to-train-your-gpt.md) | Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

## 🕸️ 20. Programar con agentes de código

_Agentes de terminal, extensiones de editor y entornos para programar con IA. Revisa qué cliente utilizas, cómo inicia sesión y si el modelo usa un plan, una API o un servidor local._ → [página de la categoría](human/categorias/20-agentes-de-codigo.md)

### Agentes de terminal

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [OpenCode](human/fichas/opencode.md) | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| ⭐ [Claude Code](human/fichas/claude-code.md) | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [DeepSeek Harness (DSH)](human/fichas/deepseek-harness.md) | Harness de agentes de DeepSeek en vista previa, con arquitectura de plugins, Web UI local y proveedores de modelos configurables. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |
| [Codex CLI](human/fichas/codex.md) | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [Gemini CLI](human/fichas/gemini-cli.md) | CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigravity CLI. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [Open Interpreter](human/fichas/open-interpreter.md) | Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos. | Depende de la ruta elegida | 🧩 motor/runtime | 🟢 fácil |
| [goose](human/fichas/goose.md) | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [Aider](human/fichas/aider.md) | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [Qwen Code](human/fichas/qwen-code.md) | Agente de código de terminal del equipo Qwen, multiprotocolo (OpenAI, Anthropic, Gemini, Qwen o modelos locales), con skills, subagentes y MCP. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [MiMo-Code](human/fichas/mimo-code.md) | Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente. | API de IA opcional | 🖥️ app | 🟡 medio |
| [Antigravity CLI](human/fichas/antigravity-cli.md) | Agente de programación de Google para la terminal (agy), con subagentes, MCP y skills; se distribuye en binarios, sin código fuente. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Editores y extensiones de código

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Zed](human/fichas/zed.md) | Editor de código de alto rendimiento y multijugador, de los creadores de Atom y Tree-sitter, con IA integrada y agentes externos por ACP. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [Cline](human/fichas/cline.md) | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [Kilo Code](human/fichas/kilocode.md) | Agente de código abierto para VS Code, JetBrains y la terminal, con más de 500 modelos, modos de trabajo y marketplace de agentes, skills y MCP. | API de IA necesaria | 🖥️ app | 🟢 fácil |
| [openidea](human/fichas/openidea.md) | Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [OpenCursor](human/fichas/opencursor.md) | Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos. | API de IA opcional | 🖥️ app | 🟡 medio |

### Agentes para issues y tareas de ingeniería

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [OpenHands](human/fichas/openhands.md) | Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Open SWE](human/fichas/open-swe.md) | Robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisables. | API de IA necesaria | 🧩 motor/runtime | 🟡 medio |
| [mini-swe-agent](human/fichas/mini-swe-agent.md) | Agente de ingeniería de software mínimo (unas 100 líneas) del equipo de SWE-bench y SWE-agent: solo usa bash y rinde alto en SWE-bench. | API de IA opcional | 🖥️ app | 🟢 fácil |

### Interfaces para gestionar sesiones

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [T3 Code](human/fichas/t3code.md) | Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [opencode-manager](human/fichas/opencode-manager.md) | Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |

## 🕸️ 21. Asistentes e investigación con agentes

_Asistentes personales, equipos de agentes e investigación con fuentes. Compara la tarea que completan, las herramientas que pueden usar y la revisión que necesitas hacer del resultado._ → [página de la categoría](human/categorias/21-asistentes-investigacion.md)

### Asistentes autónomos y equipos de agentes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [OpenClaw](human/fichas/openclaw.md) | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | API de IA opcional | 🖥️ app | 🟡 medio |
| [hermes-agent](human/fichas/hermes-agent.md) | Asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados. | API de IA opcional | 🖥️ app | 🟡 medio |
| [paperclip](human/fichas/paperclip.md) | Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [ruflo](human/fichas/ruflo.md) | Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [DeepTutor](human/fichas/deeptutor.md) | Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. | API de IA opcional | 🖥️ app | 🟡 medio |
| [multica](human/fichas/multica.md) | Workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [OpenJarvis](human/fichas/openjarvis.md) | Crea un asistente personal con chat y flujos que pueden usar modelos locales, con conectores opcionales para tus servicios. | API de IA opcional | 🖥️ app | 🟡 medio |
| [OpenBot](human/fichas/openbot.md) | Espacio autoalojable de CopilotKit para compañeros de IA con navegador propio, permisos, aprobaciones y auditoría, conectables por AG-UI. | Depende de la ruta elegida | 🖥️ app | 🔴 pesado |
| [Mercury Agent](human/fichas/mercury-agent.md) | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [social-media-agent](human/fichas/social-media-agent.md) | Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas. | API de IA necesaria | 🧩 motor/runtime | 🟡 medio |
| [hello-halo](human/fichas/hello-halo.md) | Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [agentes-chat](human/fichas/agentes-chat.md) | Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas. | API de IA opcional | 🖥️ app | 🟡 medio |

### Agentes de research autónomo

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [autoresearch](human/fichas/autoresearch.md) | Experimento para iterar sobre entrenamiento de nanochat con un agente de código y una GPU NVIDIA. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [deer-flow](human/fichas/deer-flow.md) | Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. | Depende de la ruta elegida | ⚙️ plataforma | 🟡 medio |
| [STORM](human/fichas/storm.md) | Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. | API de IA necesaria | 🧩 motor/runtime | 🟡 medio |
| [gpt-researcher](human/fichas/gpt-researcher.md) | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [local-deep-research](human/fichas/local-deep-research.md) | Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. | API de IA opcional | ⚙️ plataforma | 🟡 medio |

## 🕸️ 22. Infraestructura, despliegue y herramientas para agentes

_Sandboxes, herramientas de ejecución, backend y alojamiento. Son piezas de infraestructura: separa el coste del servidor, los servicios conectados y las llamadas al modelo._ → [página de la categoría](human/categorias/22-infraestructura-despliegue.md)

### Infraestructura: sandboxes, herramientas y protocolos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Composio](human/fichas/composio.md) | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| ⭐ [E2B](human/fichas/e2b.md) | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [claude-task-master](human/fichas/claude-task-master.md) | Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. | API de IA opcional | 🖥️ app | 🟡 medio |
| [agent-desktop](human/fichas/agent-desktop.md) | CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [NemoClaw](human/fichas/nemoclaw.md) | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. | Depende de la ruta elegida | ⚙️ plataforma | 🔴 pesado |
| [Kiri](human/fichas/kiri.md) | Ejecuta contenedores de desarrollo y permite verlos desde una aplicación de escritorio que crea su propio contexto de Docker. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Agent Substrate](human/fichas/agent-substrate.md) | Aloja tareas con estado en Kubernetes y permite probar cómo se suspenden y reanudan dentro de entornos separados. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [sandbox](human/fichas/sandbox.md) | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Gemini Computer Use (preview)](human/fichas/computer-use-preview.md) | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. | API de IA necesaria | 🧩 motor/runtime | 🟡 medio |
| [shepherd](human/fichas/shepherd.md) | Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [nodeterm](human/fichas/nodeterm.md) | Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. | API de IA opcional | 🖥️ app | 🟡 medio |
| [Agent Protocol](human/fichas/agent-protocol.md) | Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [Screen Relay](human/fichas/screen-relay.md) | Muestra en el navegador un escritorio de prueba para ver una aplicación gráfica sin usar tu escritorio personal. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🔴 pesado |

### Dominios y recursos de infraestructura

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [FreeDomain](human/fichas/freedomain.md) | Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [free-for-dev](human/fichas/free-for-dev.md) | Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

### Redes y transporte

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [frp](human/fichas/frp.md) | Proxy inverso rápido para exponer servidores locales detrás de NAT o cortafuegos a internet, con TCP, UDP, HTTP, HTTPS y modo P2P. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Headscale](human/fichas/headscale.md) | Implementación abierta y autoalojada del servidor de control de Tailscale para crear tu propia red privada WireGuard con los clientes oficiales. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [NetBird](human/fichas/netbird.md) | Red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso granular, autoalojable o en la nube. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [WireGuard Easy](human/fichas/wg-easy.md) | La forma más sencilla de ejecutar WireGuard VPN con interfaz web para gestionar clientes, códigos QR, estadísticas y 2FA. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Pangolin Community Edition](human/fichas/pangolin.md) | Controla qué personas pueden entrar a aplicaciones propias mediante un proxy y reglas de acceso administradas por tu equipo. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Tailcat](human/fichas/tailcat.md) | Conecta dos equipos propios para el intercambio temporal de datos mediante un enlace cifrado entre los extremos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [MasterDnsVPN](human/fichas/masterdnsvpn.md) | Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |

### Alojamiento y backend

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [supabase](human/fichas/supabase.md) | Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Uptime Kuma](human/fichas/uptime-kuma.md) | Monitor de disponibilidad autoalojado y fácil de usar: comprueba webs y servicios, envía alertas a más de 90 canales y publica páginas de estado. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Caddy](human/fichas/caddy.md) | Servidor web y proxy inverso extensible con HTTPS automático por defecto, configurable con Caddyfile o JSON y API. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [coolify](human/fichas/coolify.md) | Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [Traefik Proxy](human/fichas/traefik.md) | Proxy inverso y balanceador de carga dinámico para contenedores y microservicios que se configura automáticamente desde Docker, Kubernetes y otros. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Appwrite](human/fichas/appwrite.md) | Plataforma de backend abierta orientada a agentes y desarrolladores: autenticación, bases de datos, almacenamiento, funciones, mensajería, tiempo real y hosting, con MCP. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [Portainer CE](human/fichas/portainer.md) | Interfaz web ligera para gestionar contenedores en Docker, Swarm, Podman, Kubernetes y ACI (Community Edition). | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [Dokploy](human/fichas/dokploy.md) | Plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku, para desplegar aplicaciones y bases de datos con Docker y Traefik. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [CasaOS](human/fichas/casaos.md) | Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [LibreTranslate](human/fichas/libretranslate.md) | Traduce texto con una interfaz web y una API que puedes alojar en tu equipo usando modelos de traducción de Argos. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |

## 🧬 23. Operar, evaluar y medir modelos de IA

_Servidores de inferencia, gateways, evaluación, trazas y control de contexto. Cada pieza cubre una etapa: ejecutar el modelo, observarlo o comprobar la calidad de sus respuestas._ → [página de la categoría](human/categorias/23-operacion-evaluacion-modelos.md)

### Serving y gateways de LLM

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [vLLM](human/fichas/vllm.md) | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [OmniRoute](human/fichas/omniroute.md) | Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso. | API de IA opcional | ⚙️ plataforma | 🔴 pesado |
| [litellm](human/fichas/litellm.md) | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [Ray](human/fichas/ray.md) | Motor de cómputo distribuido para IA: escala Python de un portátil a un clúster, con bibliotecas para datos, entrenamiento, ajuste, RL y serving. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [SGLang](human/fichas/sglang.md) | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [claude-code-router](human/fichas/claude-code-router.md) | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. | Depende de la ruta elegida | ⚙️ plataforma | 🔴 pesado |
| [TensorRT-LLM](human/fichas/tensorrt-llm.md) | Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [Portkey AI Gateway](human/fichas/portkey-gateway.md) | Centraliza llamadas a distintos proveedores de modelos mediante una pasarela con reglas de ruta, presupuestos y registro de solicitudes. | API de IA necesaria | ⚙️ plataforma | 🔴 pesado |
| [Xinference](human/fichas/xinference.md) | Plataforma abierta de inferencia para modelos de lenguaje, visión, embeddings, reranking, imagen, audio y vídeo, con API compatible con OpenAI y varios motores. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [BentoML](human/fichas/bentoml.md) | Framework Python para convertir modelos y pipelines de IA en APIs de producción, con empaquetado en imágenes Docker y despliegue reproducible. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [GPUStack](human/fichas/gpustack.md) | Gestor de clústeres de GPU para servir modelos de IA: configura vLLM, SGLang o TensorRT-LLM, expone APIs compatibles con OpenAI y aprovisiona instancias GPU. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |

### Ahorro de contexto y tokens

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [headroom](human/fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [rtk](human/fichas/rtk.md) | Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [TOON](human/fichas/toon-format.md) | Convierte listas de objetos JSON a un texto con encabezado y filas para experimentar con entradas más compactas para modelos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [GPTCache](human/fichas/gptcache.md) | Reutiliza respuestas de consultas parecidas a un modelo mediante una caché semántica con reglas de comparación configurables. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [LLMLingua](human/fichas/llmlingua.md) | Acorta texto de entrada para modelos de lenguaje y permite medir cuánto contexto conservas antes de enviar el prompt. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### Observabilidad, evaluación y guardrails

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [promptfoo](human/fichas/promptfoo.md) | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [langfuse](human/fichas/langfuse.md) | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [MLflow](human/fichas/mlflow.md) | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. | API de IA opcional | ⚙️ plataforma | 🟢 fácil |
| [loguru](human/fichas/loguru.md) | Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Opik](human/fichas/opik.md) | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [ccusage](human/fichas/ccusage.md) | Resume los tokens y estima el coste de tus sesiones de asistentes a partir de los registros locales de sus terminales. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [DeepEval](human/fichas/deepeval.md) | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [Ragas](human/fichas/ragas.md) | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. | Depende de la ruta elegida | 📚 librería/SDK | 🟢 fácil |
| [LM Evaluation Harness](human/fichas/lm-eval-harness.md) | Arnés estándar de EleutherAI para evaluar modelos de lenguaje en cientos de benchmarks académicos con backends Hugging Face, vLLM, SGLang o APIs. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [Phoenix](human/fichas/phoenix.md) | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. | API de IA opcional | ⚙️ plataforma | 🟢 fácil |
| [Claude-Code-Usage-Monitor](human/fichas/claude-code-usage-monitor.md) | Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [OpenLLMetry](human/fichas/openllmetry.md) | Instrumentación abierta basada en OpenTelemetry para aplicaciones de LLM: traza llamadas a modelos, bases vectoriales y frameworks hacia tu backend de observabilidad. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [NeMo Guardrails](human/fichas/guardrails.md) | Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM. | Depende de la ruta elegida | 📚 librería/SDK | 🟡 medio |
| [Helicone](human/fichas/helicone.md) | Pasarela de IA y plataforma de observabilidad de LLM abierta: registra peticiones, costes y latencias, gestiona prompts y enruta a más de 100 modelos. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |

## 🧑‍💻 24. Modelos abiertos y entrenamiento

_Modelos, bibliotecas de entrenamiento y ajuste fino. Revisa la licencia de los pesos, la memoria necesaria y la opción de inferencia antes de descargar o entrenar._ → [página de la categoría](human/categorias/24-modelos-entrenamiento.md)

### Entrenar y afinar modelos

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Unsloth](human/fichas/unsloth.md) | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales. | API de IA opcional | 🖥️ app | 🟡 medio |
| [tensorflow](human/fichas/tensorflow.md) | Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [Transformers](human/fichas/transformers.md) | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [PyTorch](human/fichas/pytorch.md) | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [LLaMA-Factory](human/fichas/llama-factory.md) | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [scikit-learn](human/fichas/scikit-learn.md) | La biblioteca de machine learning clásico en Python: clasificación, regresión, clustering, reducción de dimensión, selección de modelos y preprocesado. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Keras 3](human/fichas/keras.md) | API de deep learning multibackend: el mismo código de modelo se ejecuta sobre JAX, TensorFlow o PyTorch (y OpenVINO para inferencia). | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [DeepSpeed](human/fichas/deepspeed.md) | Biblioteca de optimización de entrenamiento e inferencia distribuidos de Microsoft: ZeRO, paralelismo y descarga a CPU/NVMe para modelos enormes. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [JAX](human/fichas/jax.md) | Biblioteca de Google para cómputo numérico de alto rendimiento: NumPy diferenciable, compilación JIT con XLA y vectorización en CPU, GPU y TPU. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [PyTorch Lightning](human/fichas/pytorch-lightning.md) | Framework que estructura el entrenamiento en PyTorch y lo escala de una GPU a miles sin cambiar el código, con Lightning Fabric para control experto. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [verl](human/fichas/verl.md) | Framework flexible y eficiente de post-entrenamiento por refuerzo para LLM (HybridFlow): PPO, GRPO y otros algoritmos con FSDP/Megatron y vLLM/SGLang. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [PEFT](human/fichas/peft.md) | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [TRL](human/fichas/trl.md) | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Axolotl](human/fichas/axolotl.md) | Framework de post-entrenamiento de LLM por configuración YAML: ajuste completo, LoRA/QLoRA, DPO/GRPO, multimodal y entrenamiento distribuido. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [OpenRLHF](human/fichas/openrlhf.md) | Framework de RLHF y RL agéntico escalable basado en Ray, vLLM y DeepSpeed: PPO, REINFORCE++, GRPO, RLOO y entrenamiento asíncrono. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [Accelerate](human/fichas/accelerate.md) | Biblioteca de Hugging Face para ejecutar el mismo código de PyTorch en una GPU, varias, TPU o con DeepSpeed y FSDP, con precisión mixta, cambiando pocas líneas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [torchtune](human/fichas/torchtune.md) | Biblioteca nativa de PyTorch para post-entrenamiento de LLM con recetas de ajuste completo, LoRA/QLoRA, DPO y destilación; ya sin mantenimiento activo. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [bionemo-recipes](human/fichas/bionemo-recipes.md) | Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🔴 pesado |

### Modelos abiertos y fundacionales

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [TimesFM](human/fichas/timesfm.md) | Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por versión. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [DeepSeek-V3](human/fichas/deepseek-v3.md) | Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su API compatible con OpenAI o en servidores con varias GPU. | API de IA opcional | 🧩 motor/runtime | 🔴 pesado |
| [laya](human/fichas/laya.md) | Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [cosmos](human/fichas/cosmos.md) | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. | API de IA opcional | 🧩 motor/runtime | 🔴 pesado |
| [Gemma (biblioteca JAX)](human/fichas/gemma.md) | Biblioteca oficial de Google DeepMind para usar y ajustar los modelos de pesos abiertos Gemma en JAX: muestreo, multimodal, LoRA y ajuste fino. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [Nemotron (NVIDIA)](human/fichas/nemotron.md) | Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. | API de IA opcional | 📂 catálogo/recurso | 🔴 pesado |
| [Kimi K2.7 Code](human/fichas/kimi-k2-7-code.md) | Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face. | API de IA opcional | 🧩 motor/runtime | 🔴 pesado |

## 🧑‍💻 25. Procesar datos y trabajar con notebooks

_Motores de consulta, tablas, notebooks y aplicaciones de datos. Empieza por un archivo pequeño y distingue una herramienta de análisis de un catálogo o conjunto de datos de referencia._ → [página de la categoría](human/categorias/25-datos-notebooks.md)

### Datos y notebooks

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [DuckDB](human/fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [ClickHouse](human/fichas/clickhouse.md) | Base de datos analítica columnar de código abierto para consultas SQL en tiempo real sobre miles de millones de filas, autoalojable o en la nube. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [pandas](human/fichas/pandas.md) | Biblioteca estándar de Python para analizar y transformar datos tabulares con DataFrame y Series: limpieza, agrupaciones, uniones, series temporales y E/S. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Apache Spark](human/fichas/spark.md) | Motor unificado de Apache para procesar datos a gran escala en clúster: SQL y DataFrames, streaming, machine learning (MLlib) y API de pandas sobre Spark. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | hard |
| [Polars](human/fichas/polars.md) | Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Apache Arrow](human/fichas/arrow.md) | Formato columnar en memoria y conjunto de bibliotecas multilenguaje para intercambiar y analizar datos sin copias entre procesos y herramientas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [PyGWalker](human/fichas/pygwalker.md) | Convierte un DataFrame de pandas o Polars en una interfaz de exploración visual tipo Tableau dentro de Jupyter, Streamlit o marimo, arrastrando campos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [JupyterLab](human/fichas/jupyterlab.md) | Entorno web de Project Jupyter con notebooks, terminal, editor de texto y explorador de archivos, ampliable mediante extensiones. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [dbt](human/fichas/dbt.md) | Herramienta para transformar datos dentro del almacén con modelos SQL versionados, pruebas, documentación y dependencias, como se hace con el software. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Apache Iceberg](human/fichas/apache-iceberg.md) | Formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Delta Lake](human/fichas/delta-lake.md) | Capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Ibis](human/fichas/ibis.md) | Biblioteca Python de dataframes portable: escribe la consulta una vez y ejecútala en DuckDB, Polars, ClickHouse, Spark, Postgres o más de 20 motores. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [hudi](human/fichas/hudi.md) | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [dlt (data load tool)](human/fichas/dlt.md) | Biblioteca Python para cargar datos de APIs, bases de datos y archivos en destinos como DuckDB, Postgres o almacenes en la nube, con esquema y carga incremental. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |

### Apps de datos en Python

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Gradio](human/fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| ⭐ [marimo](human/fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [streamlit](human/fichas/streamlit.md) | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [Reflex](human/fichas/reflex.md) | Framework para crear aplicaciones web completas (frontend y backend) solo con Python, con estado en clases, componentes y despliegue propio o gestionado. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [dash](human/fichas/dash.md) | Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [NiceGUI](human/fichas/nicegui.md) | Framework Python para interfaces web en el navegador con botones, gráficos, mapas, tablas y escenas 3D, útil para paneles, robótica y herramientas internas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Panel](human/fichas/panel.md) | Framework de HoloViz para dashboards y apps de datos en Python que funcionan igual en un notebook y como aplicación web servida con `panel serve`. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |

## 🎨 26. Animación, gráficos y creación 3D

_Animación web, motores gráficos, modelado y renderizado 3D. Una librería se integra en una aplicación; un editor se utiliza directamente. Consulta el formato de entrada y el equipo necesario._ → [página de la categoría](human/categorias/26-animacion-graficos-3d.md)

### Animación y 3D

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [three.js](human/fichas/three-js.md) | Biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Anime.js](human/fichas/animejs.md) | Motor de animación JavaScript ligero para CSS, SVG, DOM y objetos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [PixiJS](human/fichas/pixijs.md) | Motor de renderizado 2D para la web sobre WebGL y WebGPU, muy rápido, para juegos, gráficos interactivos y aplicaciones visuales en el navegador. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [motion](human/fichas/motion.md) | Librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [react-three-fiber](human/fichas/react-three-fiber.md) | Renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [GSAP](human/fichas/gsap.md) | Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Babylon.js](human/fichas/babylonjs.md) | Motor 3D completo para la web de Microsoft y la comunidad, con física, materiales PBR, WebXR, editor de nodos y playground en línea. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [PlayCanvas Engine](human/fichas/playcanvas.md) | Motor gráfico web de código abierto sobre WebGPU y WebGL2 para apps, juegos y visualizaciones 2D y 3D, con soporte de Gaussian splats y glTF. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [zdog](human/fichas/zdog.md) | Motor de gráficos pseudo-3D que permite dibujar y animar ilustraciones sencillas mediante canvas o SVG. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [pixelfx](human/fichas/pixelfx.md) | Colección de efectos de pixel art hechos con código y una skill para ayudar a generar efectos propios. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [regl](human/fichas/regl.md) | Biblioteca funcional para organizar comandos de renderizado WebGL y dibujar gráficos acelerados en una aplicación web. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [webgl-noise](human/fichas/webgl-noise.md) | Rutinas de ruido procedural para shaders de WebGL, útiles para crear texturas y efectos visuales en tiempo real. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [scenejs](human/fichas/scenejs.md) | Biblioteca JavaScript para crear y controlar animaciones mediante líneas de tiempo y propiedades de elementos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [pencil](human/fichas/pencil.md) | Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |

### Creación, renderizado y animación 3D

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Godot Engine](human/fichas/godot.md) | Motor de videojuegos 2D y 3D libre (MIT) con editor integrado, scripting en GDScript o C# y exportación a escritorio, móvil, web y consolas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Bevy](human/fichas/bevy.md) | Motor de juegos en Rust basado en datos y en el patrón ECS, libre (MIT o Apache-2.0), modular y con funciones 2D y 3D para juegos y simulaciones. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [FreeCAD](human/fichas/freecad.md) | Modelador CAD 3D paramétrico libre para diseño de producto, ingeniería mecánica y arquitectura (BIM), con planos técnicos, FEM, CAM y Python. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [blender](human/fichas/blender.md) | Código de Blender, la aplicación para modelar, animar, renderizar y editar escenas y contenido tridimensional. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [filament](human/fichas/filament.md) | Motor de renderizado físicamente basado para integrar gráficos 3D en aplicaciones móviles, web y de escritorio. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [OpenSCAD](human/fichas/openscad.md) | CAD 3D por código: describes la pieza en un lenguaje de script y OpenSCAD la compila a un sólido exportable (STL, 3MF), ideal para piezas paramétricas. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [meshoptimizer](human/fichas/meshoptimizer.md) | Biblioteca para optimizar geometría y reducir el coste de almacenar y renderizar mallas tridimensionales. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [ozz-animation](human/fichas/ozz-animation.md) | Biblioteca C++ y herramientas para preparar y reproducir animación esquelética dentro de motores y aplicaciones. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Open Reality](human/fichas/openreality.md) | Convierte video propio en escenas 3D consultables y ofrece herramientas MCP para trabajar con la reconstrucción desde un asistente. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [awesome-cad](human/fichas/awesome-cad.md) | Directorio de programas, bibliotecas y recursos de diseño asistido por computadora organizados por especialidad. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [video2threejs](human/fichas/video2threejs.md) | Explica con un caso cómo reconstruir la apariencia de un video como una escena navegable en Three.js. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |

### Física y simulación

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Genesis World](human/fichas/genesis-world.md) | Plataforma de simulación para IA física y robótica con motor multifísica unificado (rígidos, FEM, MPM, fluidos), render fotorrealista y paralelismo masivo en GPU. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | hard |
| [MuJoCo](human/fichas/mujoco.md) | Motor de física de Google DeepMind para simular estructuras articuladas con contacto, estándar en robótica, biomecánica y aprendizaje por refuerzo. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [warp](human/fichas/warp.md) | Framework de NVIDIA para kernels y simulación física en CPU o GPU; no es un modelo ni un terminal. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [planck.js](human/fichas/planck-js.md) | Motor de física 2D para simular cuerpos, colisiones y uniones dentro de juegos o aplicaciones JavaScript. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [react-three-rapier](human/fichas/react-three-rapier.md) | Integración del motor de física Rapier con React Three Fiber para añadir simulación a escenas tridimensionales. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [MotionBricks](human/fichas/motionbricks.md) | Genera movimiento de personajes a partir de poses y objetivos mediante modelos locales y una escena de demostración. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [Robotics for Antigravity](human/fichas/robotics-antigravity-plugin.md) | Añade a Antigravity instrucciones para crear, probar y observar escenas de robótica con flujos como la simulación en MuJoCo. | Depende de la ruta elegida | 🎨 skill/prompt | 🟡 medio |

## 🎨 27. Skills de diseño, contenido y especialidades

_Skills y plugins para diseño, escritura, marketing, ciencia y negocio. Se añaden a un agente compatible; generar imágenes, publicar o consultar servicios puede requerir cuentas adicionales._ → [página de la categoría](human/categorias/27-skills-especializadas.md)

### Skills de diseño para agentes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Stitch Skills](human/fichas/stitch-skills.md) | Colección de skills de agente para trabajar con el servidor MCP de Google Stitch. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |
| [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md) | Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla". | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [taste-skill](human/fichas/taste-skill.md) | Skill design-taste-frontend para dirección visual y revisión de sitios; otros skills del pack antiguo se movieron a repos propios. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [impeccable](human/fichas/impeccable.md) | Vocabulario y playbooks de diseño para agentes, con detector determinista y hooks según herramienta. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |
| [Front-End-Checklist](human/fichas/front-end-checklist.md) | Checklist y recursos para revisar aspectos de calidad de un frontend antes de entregarlo. | API de IA opcional | 📂 catálogo/recurso | 🟢 fácil |
| [skills_emil](human/fichas/skills-emil.md) | Colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering). | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [hallmark](human/fichas/hallmark.md) | Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [design.md](human/fichas/design-md.md) | Especificación y CLI para documentar identidad visual en DESIGN.md,validar tokens y comparar versiones. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [anatomy](human/fichas/anatomy.md) | Skill para crear ilustraciones isométricas e interactivas de máquinas y sistemas con SVG y efectos visuales opcionales. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [gsap-skills](human/fichas/gsap-skills.md) | Skills oficiales con instrucciones y ejemplos para que agentes creen animaciones y utilicen plugins de GSAP. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [modern-web-guidance](human/fichas/modern-web-guidance.md) | Herramienta y skill para que un agente consulte documentación actual sobre prácticas y APIs de desarrollo web. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [Android Skills](human/fichas/android-skills.md) | Añade guías oficiales de Android a Claude Code, Codex o Antigravity para revisar, compilar y probar aplicaciones Android. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [logo-design-skill](human/fichas/logo-design-skill.md) | Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de diseño. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [threejs-skills](human/fichas/threejs-skills.md) | Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [blender-skills](human/fichas/blender-skills.md) | Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexiones MCP. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [motion-design-skill](human/fichas/motion-design-skill.md) | Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interfaces. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [threejs-game-skills](human/fichas/threejs-game-skills.md) | Skills para que un agente construya juegos de navegador con Three.js, interfaz y recursos visuales o sonoros opcionales. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [dream-loop](human/fichas/dream-loop.md) | Skill que combina Blender, generación de imágenes y revisión por un agente para preparar visuales tridimensionales. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [design-dna](human/fichas/design-dna.md) | Skill para analizar referencias visuales, extraer decisiones de diseño y generar interfaces con un estilo coherente. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [3dviz-pro-max](human/fichas/3dviz-pro-max.md) | Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [genjutsu](human/fichas/genjutsu.md) | Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [Creative Architect](human/fichas/creative-architect.md) | Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |

### Escritura y calidad de texto

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Humanizer](human/fichas/humanizer.md) | Skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [i-have-adhd](human/fichas/i-have-adhd.md) | Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [Stop Slop](human/fichas/stop-slop.md) | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |

### Skills de dominio: marketing, SEO y negocio

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Marketing Skills](human/fichas/marketingskills.md) | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |
| [The Agency (agency-agents)](human/fichas/agency-agents.md) | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [scientific-agent-skills](human/fichas/scientific-agent-skills.md) | Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [financial-services](human/fichas/financial-services.md) | Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [Knowledge Work Plugins](human/fichas/knowledge-work-plugins.md) | Añade a Claude flujos de trabajo por especialidad, como preparar reuniones de ventas, revisar datos y organizar soporte. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [claude-seo](human/fichas/claude-seo.md) | Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [Claude Ads](human/fichas/claude-ads.md) | Audita campañas de publicidad con Claude Code y organiza los hallazgos por plataforma, evidencia y prioridad. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [skills](human/fichas/minimalist-entrepreneur-skills.md) | Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con un agente. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [instagram-agent-skill](human/fichas/instagram-agent-skill.md) | Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [social-media-research-skills](human/fichas/social-media-research-skills.md) | Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [linkedin-agent-skill](human/fichas/linkedin-agent-skill.md) | Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [Arcads AI Video Skill Pack](human/fichas/arcads-claude-code.md) | Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, Sora, Veo, Kling). | API de IA necesaria | 🎨 skill/prompt | 🟡 medio |
| [Shopify AI Toolkit](human/fichas/shopify-ai-toolkit.md) | Aporta guías y herramientas de Shopify para asistir el desarrollo de temas y aplicaciones con fuentes del fabricante. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |

## 🖼️ 28. Visión artificial, rostros y percepción

_Detección, seguimiento, segmentación, rostros y percepción espacial. Distingue el modelo, sus pesos y las herramientas para preparar datos. Comprueba requisitos y permisos sobre las imágenes._ → [página de la categoría](human/categorias/28-vision-percepcion.md)

### Rostros y retratos animados

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Deep-Live-Cam](human/fichas/deep-live-cam.md) | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [FaceFusion](human/fichas/facefusion.md) | Plataforma para intercambio y mejora de rostros en imágenes y video. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [InsightFace](human/fichas/insightface.md) | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [DeepFace](human/fichas/deepface.md) | Biblioteca Python ligera de reconocimiento facial y análisis de atributos (edad, género, emoción) que envuelve modelos como ArcFace, FaceNet o VGG-Face. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [LivePortrait](human/fichas/liveportrait.md) | Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas). | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |

### Visión por computador

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Ultralytics YOLO](human/fichas/ultralytics.md) | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| ⭐ [SAM 3](human/fichas/sam3.md) | Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en imágenes y video todos los objetos que describas con una frase corta. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [OpenCV](human/fichas/opencv.md) | La librería de visión por computadora de referencia, con miles de algoritmos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [supervision](human/fichas/supervision.md) | Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. | API de IA opcional | 📚 librería/SDK | 🟢 fácil |
| [mediapipe](human/fichas/mediapipe.md) | Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplicaciones. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Detectron2](human/fichas/detectron2.md) | Biblioteca de Meta AI para detección de objetos y segmentación (instancias, panóptica, keypoints) sobre PyTorch, con un zoo de modelos preentrenados. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | hard |
| [openpose](human/fichas/openpose.md) | Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [Label Studio](human/fichas/label-studio.md) | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. | API de IA opcional | ⚙️ plataforma | 🟢 fácil |
| [CVAT Community](human/fichas/cvat.md) | Plataforma autoalojable para anotar imágenes, vídeo, audio y 3D con equipos, preanotación con modelos y exportación a más de 20 formatos de datasets. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |
| [tfjs-models](human/fichas/tfjs-models.md) | Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en aplicaciones. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [dlib](human/fichas/dlib.md) | Toolkit C++ con bindings de Python para aprendizaje automático y visión: detección de caras, 68 puntos faciales, seguimiento de objetos y optimización. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [kornia](human/fichas/kornia.md) | Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en PyTorch. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [mmpose](human/fichas/mmpose.md) | Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento humano. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [EasyMocap](human/fichas/easymocap.md) | Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imágenes. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [4D-Humans](human/fichas/4d-humans.md) | Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de video. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [WHAM](human/fichas/wham.md) | Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de video. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |

## 🎬 29. Audio, transcripción, voz y música

_Transcripción, síntesis, clonación de voz, agentes de audio y música. Compara idioma, latencia, procesamiento local y servicios externos según la tarea concreta._ → [página de la categoría](human/categorias/29-audio-voz-musica.md)

### Transcripción (voz a texto)

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [whisper.cpp](human/fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [whisper](human/fichas/whisper.md) | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [faster-whisper](human/fichas/faster-whisper.md) | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [whisperX](human/fichas/whisperx.md) | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [Buzz](human/fichas/buzz.md) | Transcribe grabaciones y exporta subtítulos en una aplicación de escritorio que puede usar Whisper en tu propio equipo. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [NeMo Speech](human/fichas/nemo.md) | Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [sherpa-onnx](human/fichas/sherpa-onnx.md) | Motor de voz offline con ONNX Runtime: reconocimiento, síntesis, VAD, diarización e identificación de hablante en móvil, embebido, escritorio y servidor. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |

### Síntesis y clonación de voz

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Kokoro](human/fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [VoiceStudio](human/fichas/omnivoice-studio.md) | App local de voz con modelos descargables,edición AGPL y una oferta comercial separada. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [GPT-SoVITS](human/fichas/gpt-sovits.md) | Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [VibeVoice](human/fichas/vibevoice.md) | Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🔴 pesado |
| [VoxCPM](human/fichas/voxcpm.md) | VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación de voz. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |
| [RVC WebUI](human/fichas/rvc.md) | Interfaz y herramientas para convertir una grabación a otra voz mediante modelos locales. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟡 medio |
| [Fish Speech](human/fichas/fish-speech.md) | Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [IndexTTS](human/fichas/index-tts.md) | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [CosyVoice](human/fichas/cosyvoice.md) | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [F5-TTS](human/fichas/f5-tts.md) | Síntesis de voz con clonación a partir de pocos segundos de audio de referencia, basada en flow matching con Diffusion Transformer; incluye app Gradio y CLI. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [edge-tts](human/fichas/edge-tts.md) | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [LuxTTS](human/fichas/luxtts.md) | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [ElevenLabs (SDK de Python)](human/fichas/elevenlabs-python.md) | SDK oficial de Python para la API de pago de ElevenLabs: voz sintética, clonación, transcripción, música y agentes de voz. | API de IA necesaria | 📚 librería/SDK | 🟢 fácil |

### Agentes de voz en tiempo real

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Pipecat](human/fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | API de IA opcional | 🧩 motor/runtime | 🟡 medio |
| [LiveKit Agents](human/fichas/livekit-agents.md) | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. | API de IA opcional | 🧩 motor/runtime | 🟡 medio |
| [TEN Framework](human/fichas/ten-framework.md) | Framework para agentes de voz conversacionales en tiempo real, con grafo de extensiones (ASR, LLM, TTS, VAD, turnos), diseñador visual y ejemplos listos. | API de IA necesaria | 📚 librería/SDK | hard |
| [dograh](human/fichas/dograh.md) | Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables. | Depende de la ruta elegida | 🖥️ app | 🟡 medio |

### Música y audio generativo

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [AudioCraft](human/fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [ACE-Step-1.5](human/fichas/ace-step-1-5.md) | Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🔴 pesado |
| [YuE2](human/fichas/yue.md) | Modelo abierto de generación de canciones completas (voz y acompañamiento) a partir de letra y estilo, con partitura editable, covers y una skill para agentes. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | hard |

### Procesamiento y limpieza de audio

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [Ultimate Vocal Remover (UVR)](human/fichas/ultimate-vocal-remover.md) | Aplicación de escritorio para separar voz e instrumentos de canciones con modelos de IA (MDX-Net, VR, Demucs), sin necesidad de programar. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Audacity](human/fichas/audacity.md) | Editor y grabador de audio multipista libre para Windows, macOS y Linux, con efectos, análisis y plugins, incluidos plugins de IA locales de Intel. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [pyannote.audio](human/fichas/pyannote-audio.md) | Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos preentrenados y un servicio premium opcional. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [rnnoise](human/fichas/rnnoise.md) | Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟡 medio |
| [earshot](human/fichas/earshot.md) | Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP. | API de IA opcional | 🧩 motor/runtime | 🟡 medio |
| [Demucs](human/fichas/demucs.md) | Modelo de separación de fuentes musicales (voz, batería, bajo y resto) con Hybrid Transformer; continuación mantenida por su autor tras archivarse el repo de Meta. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [rubberband](human/fichas/rubberband.md) | Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

## 🎬 30. Video con código y agentes creativos

_Herramientas y skills para escenas, motion graphics y montaje programático. Distingue el renderizado del video de la generación de sus imágenes o voces, que puede necesitar otros proveedores._ → [página de la categoría](human/categorias/30-video-codigo-agentes.md)

### Motores de video y escenas por código

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [HyperFrames](human/fichas/hyperframes.md) | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| ⭐ [MoviePy](human/fichas/moviepy.md) | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Manim (ManimGL)](human/fichas/manim.md) | Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [remotion](human/fichas/remotion.md) | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [manim](human/fichas/manim-community.md) | Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Motion Canvas](human/fichas/motion-canvas.md) | Biblioteca TypeScript para crear animaciones y vídeos explicativos con código, con editor en tiempo real que sincroniza animaciones con una pista de voz. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [mediabunny](human/fichas/mediabunny.md) | Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Revideo](human/fichas/revideo.md) | Motor TypeScript para crear vídeos con código y renderizarlos sin interfaz desde una API, con reproductor React para previsualizar escenas en el navegador. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### Skills y métodos de producción audiovisual

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Remotion Agent Skills](human/fichas/skills-remotion.md) | Skills oficiales de Remotion para que tu agente de código cree videos con React. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |
| [OpenMontage](human/fichas/openmontage.md) | Pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [video-use](human/fichas/video-use.md) | Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe. | API de IA necesaria | 🎨 skill/prompt | 🟢 fácil |
| [brag](human/fichas/brag.md) | Skills para que un agente convierta un proyecto o sitio en un video breve de lanzamiento con composición y música. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [video-shotcraft](human/fichas/video-shotcraft.md) | Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de sonido. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [lemo-opuscar](human/fichas/lemo-opuscar.md) | Biblioteca de estilos para video por código orientada a Claude,con licencias diferentes para código,guías y medios. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [FFmpeg Skill](human/fichas/ffmpeg-skill.md) | Da a agentes herramientas locales de FFmpeg para recortar, reencuadrar, normalizar audio y exportar video con pasos trazables. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [rea-video](human/fichas/rea-video.md) | Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [openfilm](human/fichas/openfilm.md) | Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [srt-whiteboard-animation](human/fichas/srt-whiteboard-animation.md) | Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos SRT. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [claude-animated-shorts](human/fichas/claude-animated-shorts.md) | Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [huashu-motion](human/fichas/huashu-motion.md) | Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión visual. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [Papermorph](human/fichas/papermorph.md) | Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visuales. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [motionmaxxing](human/fichas/motionmaxxing.md) | Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código. | API de IA opcional | 🎨 skill/prompt | 🟡 medio |
| [Remotion Superpowers](human/fichas/remotion-superpowers.md) | Orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa. | API de IA necesaria | 🎨 skill/prompt | 🟢 fácil |

### Aplicaciones y flujos de producción

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [HyperFrames Launches](human/fichas/hyperframes-launches.md) | Publica composiciones con código usadas en videos de lanzamiento de HeyGen para estudiar cómo se montan escenas y animaciones. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟡 medio |
| [videofy_minimal](human/fichas/videofy-minimal.md) | Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. | API de IA necesaria | 🖥️ app | 🟢 fácil |

## 📄 31. Presentaciones, diagramas y explicación visual

_Presentaciones, diagramas y documentación visual. Elige entre editar una pieza, escribir su estructura o generarla con un agente; revisa cómo se exporta antes de empezar._ → [página de la categoría](human/categorias/31-presentaciones-diagramas.md)

### Presentaciones

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Slidev](human/fichas/slidev.md) | Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [ppt-master](human/fichas/ppt-master.md) | Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. | API de IA opcional | 🎨 skill/prompt | 🟢 fácil |
| [reveal.js](human/fichas/reveal-js.md) | Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Marp](human/fichas/marp.md) | Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separado. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |
| [Presenton](human/fichas/presenton.md) | Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. | API de IA opcional | 🖥️ app | 🟢 fácil |

### Diagramas y documentación

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Mermaid](human/fichas/mermaid.md) | Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [archify](human/fichas/archify.md) | Skill para convertir ideas, planes y bases de código en diagramas y visualizaciones HTML interactivas. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [diagram-design](human/fichas/diagram-design.md) | Skill para que un agente cree diagramas explicativos con HTML y SVG, con criterios de composición y legibilidad. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟡 medio |
| [D2](human/fichas/d2.md) | Lenguaje declarativo de diagramas que convierte texto en diagramas SVG, PNG, PDF o PPTX, con temas, modo boceto y tres motores de layout incluidos. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [PlantUML](human/fichas/plantuml.md) | Herramienta clásica que genera diagramas UML y técnicos (secuencia, clases, actividad, Gantt, mapas mentales) a partir de descripciones de texto. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [draw.io](human/fichas/drawio.md) | Editor de diagramas en el navegador o escritorio, sin servidor: diagramas de flujo, redes, UML y arquitectura cloud, con importación de Mermaid y PlantUML. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Kroki](human/fichas/kroki.md) | Servidor que unifica más de 25 lenguajes de diagramas (PlantUML, Mermaid, D2, Graphviz, Excalidraw…) detrás de una sola API HTTP que devuelve SVG o PNG. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |

## 🕷️ 32. Navegadores y automatización web

_Navegadores, librerías de pruebas y agentes que interactúan con sitios web. Para leer páginas estáticas consulta extracción web; para operar una interfaz empieza por estas herramientas._ → [página de la categoría](human/categorias/32-navegadores-automatizacion-web.md)

### Automatización y pruebas por código

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [playwright](human/fichas/playwright.md) | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Puppeteer](human/fichas/puppeteer.md) | Librería de Google para controlar Chrome y Firefox desde Node.js. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Cypress](human/fichas/cypress.md) | Framework de pruebas end-to-end y de componentes para todo lo que corre en un navegador, con ejecución interactiva, recarga en vivo y depuración paso a paso. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟢 fácil |
| [Selenium](human/fichas/selenium.md) | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [FlareSolverr](human/fichas/flaresolverr.md) | Servidor proxy que abre páginas protegidas por Cloudflare o DDoS-GUARD en un Chrome automatizado y devuelve el HTML y las cookies para otros clientes HTTP. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟢 fácil |
| [WebdriverIO](human/fichas/webdriverio.md) | Framework de automatización de navegadores y apps móviles para Node.js basado en WebDriver, WebDriver BiDi y Appium, con servidor MCP para asistentes de IA. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |

### Herramientas de navegación para agentes

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Stagehand](human/fichas/stagehand.md) | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | API de IA necesaria | 📚 librería/SDK | 🟢 fácil |
| [browser-use](human/fichas/browser-use.md) | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. | API de IA opcional | 📚 librería/SDK | 🟡 medio |
| [agent-browser](human/fichas/agent-browser.md) | CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | 🟢 fácil |
| [Skyvern](human/fichas/skyvern.md) | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. | API de IA opcional | ⚙️ plataforma | 🟡 medio |
| [Browser Harness](human/fichas/browser-harness.md) | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🟢 fácil |
| [playwright-cli](human/fichas/playwright-cli.md) | Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. | Sin clave propia de API de IA en la ruta básica | 🎨 skill/prompt | 🟢 fácil |
| [Nanobrowser](human/fichas/nanobrowser.md) | Extensión de Chrome con un agente de IA que navega, hace clic y rellena formularios en tu propio navegador, con tu clave de API o un modelo local. | API de IA opcional | 🖥️ app | 🟢 fácil |
| [Steel Browser](human/fichas/steel-browser.md) | API de navegador autoalojable para agentes y apps: sesiones de Chrome con cookies, proxies, extensiones y repetición, controlables por Puppeteer, Playwright o Selenium. | Sin clave propia de API de IA en la ruta básica | ⚙️ plataforma | 🟡 medio |

### Navegadores y servidores de ejecución

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| ⭐ [Lightpanda](human/fichas/lightpanda.md) | Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome. | API de IA opcional | 🧩 motor/runtime | 🟢 fácil |
| [Ladybird](human/fichas/ladybird.md) | Navegador web realmente independiente con motor propio (LibWeb y LibJS) basado en estándares, sin código de Chromium, WebKit ni Gecko; aún en pre-alfa. | Sin clave propia de API de IA en la ruta básica | 🖥️ app | hard |
| [Servo](human/fichas/servo.md) | Motor de navegador escrito en Rust, ligero y paralelo, pensado para incrustar tecnologías web en aplicaciones; prototipo de la Linux Foundation Europe. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | hard |
| [Camoufox](human/fichas/camoufox.md) | Navegador basado en Firefox para scraping y agentes que genera una identidad de dispositivo coherente en cada arranque y se controla con Playwright. | Sin clave propia de API de IA en la ruta básica | 📚 librería/SDK | 🟡 medio |
| [Kitesurf](human/fichas/kitesurf.md) | Explora un motor experimental para renderizar páginas en Workers y obtener capturas desde código o herramientas compatibles. | Sin clave propia de API de IA en la ruta básica | 🧩 motor/runtime | 🔴 pesado |

### Directorios y recursos de navegador

| Repo | Qué hace | API de IA | Tipo | Preparación |
|---|---|---|---|---|
| [awesome-chrome-devtools](human/fichas/awesome-chrome-devtools.md) | Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol. | Sin clave propia de API de IA en la ruta básica | 📂 catálogo/recurso | 🟢 fácil |

## 🧰 Utilidades internas del hub

| Carpeta | Qué es |
|---|---|
| [Guía (histórica)](human/fichas/guia.md) | Guía editorial original de la biblioteca, hoy integrada en las fichas de cada repo. |
| [tools](human/fichas/tools.md) | Carpeta interna de herramientas auxiliares del hub; no es un producto para instalar. |

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
