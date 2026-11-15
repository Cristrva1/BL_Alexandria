# 19. Aprender IA y escribir mejores prompts — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `12-factor-agents`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,learning,prompts,typescript

**Qué es:** Ensayo de Dex Horthy (HumanLayer) que resume lo aprendido construyendo agentes para clientes reales: los productos que funcionan son sobre todo software determinista con pasos de LLM bien colocados. Cada factor (controlar tus prompts, tu ventana de contexto y tu flujo de control, pausar y reanudar, contactar a humanos con tool calls, agentes pequeños) tiene su capítulo con diagramas y ejemplos.
**Stack:** Markdown, TypeScript (ejemplos)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/humanlayer/12-factor-agents

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework
**Evita si:** buscas tutoriales con código ejecutable paso a paso; mira `agents-towards-production` o `ai-agents-for-beginners`
**Combina con:** `context-engineering`, `langgraph`, `vercel-ai`

## `500-ai-agents-projects`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=guias,ai-agents,genai,python

**Qué es:** Colección de ideas, casos de uso y ejemplos de agentes de IA para distintos sectores y tareas. Organiza proyectos y enlaces que sirven como punto de partida para prototipos y aprendizaje.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ashishpatel26/500-AI-Agents-Projects

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas ejemplos de aplicaciones de agentes para adaptar a tu propio problema
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `agents-towards-production`
role=directory · exec=cloud · setup=medium · mcp=True · prov=openai,local · tags=agents,learning,notebooks,python

**Qué es:** Playbook de Nir Diamant (DiamantAI) con un tutorial por carpeta, en notebooks o scripts listos para ejecutar, sobre cada pieza del stack de un agente: tool calling seguro, datos web, RAG, memoria (Redis, Mem0, Cognee), Docker, FastAPI, GPU, MCP, A2A, LangGraph, seguridad, fine-tuning, trazas y evaluación. Muchos tutoriales los aportan empresas patrocinadoras.
**Stack:** Python, Jupyter, LangGraph, FastAPI, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/NirDiamant/agents-towards-production

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** ya tienes un prototipo de agente y necesitas resolver memoria, despliegue, seguridad u observabilidad
**Evita si:** estás empezando con agentes desde cero; mira `ai-agents-for-beginners`
**Combina con:** `langgraph`, `mem0`, `ollama`

## `ai-agents-for-beginners`
role=directory · exec=cloud · setup=medium · mcp=False · prov=openai,local · tags=agents,learning,notebooks,python

**Qué es:** Recorre desde qué es un agente hasta producción: frameworks, patrones de diseño (uso de herramientas, planificación, multiagente, metacognición), RAG agéntico, protocolos MCP, A2A y NLWeb, context engineering, memoria, agentes que usan el navegador, despliegue, agentes locales y seguridad. Cada lección trae README, video corto y ejemplos en Python.
**Stack:** Python, Jupyter, Microsoft Agent Framework, Microsoft Foundry
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/ai-agents-for-beginners

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** estás empezando con agentes y quieres un curso guiado, gratuito y disponible en español
**Evita si:** no quieres depender de Azure o ya llevas agentes a producción; mira `agents-towards-production` o `12-factor-agents`
**Combina con:** `generative-ai-for-beginners`, `agent-framework`, `mcp-for-beginners`

## `ai-engineering-hub`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=guias,agents,ai,llms,machine-learning,mcp,rag,jupyter notebook

**Qué es:** Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial. Cada carpeta presenta un ejemplo con sus dependencias y configuración propias.
**Stack:** Jupyter Notebook
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/patchy631/ai-engineering-hub

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres aprender implementando ejemplos de ingeniería de IA
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `awesome-harness-engineering`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=guias,reference,python

**Qué es:** Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ai-boost/awesome-harness-engineering

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas esta función: Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA.
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta

## `awesome-llm-apps`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google,local · tags=agents,rag,learning,python

**Qué es:** Repositorio de Shubham Saboo con plantillas de código abierto ordenadas por tipo: agentes simples de un solo archivo, agentes avanzados con herramientas y memoria, equipos multiagente, agentes de voz, agentes con MCP, RAG, chat con documentos y webs, fine-tuning y cursos rápidos de Google ADK y OpenAI Agents SDK. Según la app usa OpenAI, Anthropic, Google, xAI, DeepSeek o modelos abiertos.
**Stack:** Python, Streamlit, OpenAI Agents SDK, Google ADK, Agno
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Shubhamsaboo/awesome-llm-apps

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto
**Evita si:** buscas un curso estructurado con lecciones en orden; mira `ai-agents-for-beginners` o `generative-ai-for-beginners`
**Combina con:** `streamlit`, `openai-agents-python`, `adk-python`, `firecrawl`
**Alternativas (elige una):** `openai-cookbook`, `claude-cookbooks`

## `awesome-machine-learning`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=aprender,python

**Qué es:** Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema. Reúne enlaces a implementaciones, cursos y material para comparar herramientas.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/josephmisiti/awesome-machine-learning

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas alternativas de aprendizaje automático en distintos lenguajes
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `chatgpt-dan`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=prompts,chatgpt,gpt-3-5,gpt-4,jailbreak,openai,prompt

**Qué es:** Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT. Recopila variantes de instrucciones para estudiar intentos de alterar el comportamiento de asistentes.
**Stack:** Recursos y documentación
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/0xk1h0/ChatGPT_DAN

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres investigar prompts históricos y sus limitaciones
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `chatgpt-system-prompt`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=prompts,gpt,prompt,prompt-engineering,html

**Qué es:** Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts. Organiza documentos de referencia para estudiar estructuras de instrucciones y comportamiento de asistentes.
**Stack:** HTML
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/LouisShark/chatgpt_system_prompt

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres comparar patrones de prompts como material de investigación
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `claude-cookbooks`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=learning,notebooks,rag,python

**Qué es:** Notebooks y guías de Anthropic con código copiable para construir con Claude: clasificación, resumen, RAG (con Pinecone o embeddings de Voyage AI), tool use y un agente de atención al cliente, visión y extracción de formularios, subagentes, PDFs, salida JSON consistente, moderación, prompt caching y checklists de coste y latencia.
**Stack:** Python, Jupyter, Anthropic SDK, Claude Agent SDK
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/claude-cookbooks

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar
**Evita si:** tu app usa la API de OpenAI; mira `openai-cookbook`
**Combina con:** `prompt-eng-tutorial`, `anthropic-skills`, `promptfoo`
**Alternativas (elige una):** `openai-cookbook`, `awesome-llm-apps`

## `claude-quickstarts`
role=directory · exec=cloud · setup=medium · mcp=False · prov=anthropic · tags=guias,python

**Qué es:** Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora. Cada quickstart ofrece una aplicación base con código y pasos de configuración específicos.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/claude-quickstarts

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres partir de un ejemplo oficial al integrar la API de Claude
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `context-engineering`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,python

**Qué es:** Enseña de forma sistemática qué meter en el prompt y qué dejar fuera para que el modelo responda mejor.
**Stack:** Markdown/notebooks (Python)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/jasontang-ai/Context-Engineering

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres profundizar en contexto y RAG
**Evita si:** buscas skills ejecutables listas para copiar
**Combina con:** `andrej-karpathy-skills`, `headroom`

## `fabric`
role=app · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,local · tags=prompts,automation,go

**Qué es:** Organiza prompts reutilizables (patterns) para tareas como resumir videos, extraer ideas o analizar textos. Se encadena con pipes en la terminal.
**Stack:** Go, Markdown
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. El proyecto documenta un backend de OAuth de Codex; es una integración del proyecto, no una garantía general para otras apps.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/danielmiessler/Fabric

**Instalación** [?]: `Seguir la instalación original: https://github.com/danielmiessler/Fabric/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres prompts reutilizables desde la terminal
**Evita si:** buscas solo una lista de prompts para copiar; mira `prompts-chat`
**Combina con:** `ollama`, `yt-dlp`
**Alternativas (elige una):** `prompts-chat`

## `generative-ai-for-beginners`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,prompts,python

**Qué es:** Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. Leer el curso no requiere una API; ejecutar cada práctica puede requerir servicios o modelos específicos.
**Stack:** Python, TypeScript, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/generative-ai-for-beginners

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres un curso estructurado y gratuito para empezar
**Evita si:** ya construyes con LLM y buscas recetas concretas; mira `openai-cookbook`
**Combina con:** `ai-agents-for-beginners`, `mcp-for-beginners`
**Alternativas (elige una):** `llm-course`

## `how-to-train-your-gpt`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=learning

**Qué es:** Resuelve el "quiero entenderlo con explicación narrada" frente al código desnudo de nanoGPT.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/raiyanyahya/how-to-train-your-gpt

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una guía explicada y narrada
**Evita si:** prefieres solo el código limpio (nanoGPT) o buscas algo productivo
**Combina con:** `nanogpt`, `nanochat`

## `llm-course`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=learning,training,notebooks

**Qué es:** Tres rutas: fundamentos, científico de LLM (entrenar y afinar) e ingeniero de LLM (apps y despliegue), con recursos y notebooks ejecutables.
**Stack:** Markdown, Jupyter, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mlabonne/llm-course

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una ruta completa para aprender LLM
**Evita si:** buscas un curso introductorio de apps; mira `generative-ai-for-beginners`
**Combina con:** `unsloth`, `llama-factory`
**Alternativas (elige una):** `llms-from-scratch`, `generative-ai-for-beginners`

## `llm.c`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=learning

**Qué es:** Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framework.
**Stack:** C, CUDA
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/karpathy/llm.c

**Instalación** [?]: `Seguir la instalación original: https://github.com/karpathy/llm.c/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres bajo nivel sin abstracciones y tienes GPU CUDA
**Evita si:** prefieres PyTorch (nanoGPT) o no tienes CUDA
**Combina con:** `nanogpt`

## `llms-from-scratch`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=learning,training,python

**Qué es:** Construyes atención, GPT, preentrenamiento y fine-tuning desde cero, entendiendo cada pieza. Ideal para aprender cómo funcionan por dentro.
**Stack:** Python, PyTorch, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/rasbt/LLMs-from-scratch

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres entender los LLM implementándolos
**Evita si:** solo quieres usar modelos existentes
**Combina con:** `pytorch`
**Alternativas (elige una):** `llm-course`, `nanogpt`

## `loop-engineering`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,skills,typescript

**Qué es:** Propone dejar de escribir prompts aislados y diseñar ciclos con objetivo, verificación y puntuación para que el agente itere solo. Incluye starters y herramientas de línea de comandos.
**Stack:** TypeScript, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/cobusgreyling/loop-engineering

**Instalación** [?]: `Seguir la instalación original: https://github.com/cobusgreyling/loop-engineering/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres que tu agente de código itere solo con criterios medibles
**Evita si:** solo necesitas una lista de skills; mira `awesome-agent-skills`
**Combina con:** `claude-code`, `codex`, `superpowers`

## `machinelearning`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,python

**Qué es:** Ejemplos educativos de algoritmos de machine learning y redes neuronales con Python. Agrupa implementaciones y ejercicios de clasificación, reducción de dimensiones y aprendizaje profundo.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/wepe/MachineLearning

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres explorar implementaciones pequeñas de algoritmos clásicos
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `mvanhorn`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=guias,reference

**Qué es:** Perfil público de mvanhorn para consultar sus proyectos, herramientas y contribuciones de desarrollo.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/mvanhorn/mvanhorn

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas esta función: Perfil público de mvanhorn para consultar sus proyectos, herramientas y contribuciones de desarrollo.
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta

## `nanochat`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=learning,python

**Qué es:** Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/karpathy/nanochat

**Instalación** [?]: `Seguir la instalación original: https://github.com/karpathy/nanochat/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres el pipeline completo de un chat end-to-end
**Evita si:** solo necesitas el core del modelo (nanoGPT) o un modelo listo para usar
**Combina con:** `nanogpt`

## `nanogpt`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=learning,python

**Qué es:** Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/karpathy/nanoGPT

**Instalación** [?]: `Seguir la instalación original: https://github.com/karpathy/nanoGPT/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres entender el entrenamiento de un GPT desde cero
**Evita si:** solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat)
**Combina con:** `nanochat`
**Alternativas (elige una):** `llms-from-scratch`

## `openai-cookbook`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,notebooks,python

**Qué es:** Reúne recetas sobre embeddings, function calling, RAG, evaluación, agentes y voz. Sirve como referencia práctica al construir con la API de OpenAI.
**Stack:** Python, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/openai/openai-cookbook

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** construyes sobre la API de OpenAI y quieres ejemplos oficiales
**Evita si:** usas Claude como modelo principal; mira `claude-cookbooks`
**Combina con:** `openai-python`, `openai-agents-python`
**Alternativas (elige una):** `claude-cookbooks`, `awesome-llm-apps`

## `prompt-eng-tutorial`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=learning,prompts,notebooks

**Qué es:** Nueve capítulos con ejercicios sobre claridad, roles, ejemplos, razonamiento paso a paso y cómo evitar alucinaciones. Cada lección se practica contra la API de Claude.
**Stack:** Python, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/prompt-eng-interactive-tutorial

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres aprender prompts con práctica guiada
**Evita si:** buscas una guía amplia multi-modelo; mira `prompt-engineering-guide`
**Combina con:** `claude-cookbooks`
**Alternativas (elige una):** `prompt-engineering-guide`

## `prompt-engineering-guide`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=learning,prompts,rag

**Qué es:** Explica técnicas de prompting, riesgos y aplicaciones con ejemplos y referencias a papers. Disponible en varios idiomas, incluido el español.
**Stack:** MDX, Next.js, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/dair-ai/Prompt-Engineering-Guide

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una referencia amplia de técnicas de prompting
**Evita si:** prefieres ejercicios prácticos con corrección; mira `prompt-eng-tutorial`
**Combina con:** `context-engineering`
**Alternativas (elige una):** `prompt-eng-tutorial`

## `prompt-master`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,prompts

**Qué es:** Te ayuda a escribir mejores prompts con meta-prompting reutilizable, como una capa por encima de cualquier IA.
**Stack:** Markdown/skill
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/nidhinjs/prompt-master

**Instalación** [?]: `Seguir la instalación original: https://github.com/nidhinjs/prompt-master/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres dejar de re-promptear y acertar antes
**Evita si:** ya tienes prompts afinados y estables
**Combina con:** `andrej-karpathy-skills`

## `prompts-chat`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=prompts,chatbot

**Qué es:** Reúne miles de prompts de rol y tarea para ChatGPT, Claude y otros, con buscador web. Puedes desplegar tu propia copia para tu organización.
**Stack:** Next.js, TypeScript, CSV
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/f/prompts.chat

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas prompts listos para copiar
**Evita si:** quieres ejecutarlos como comandos encadenables; mira `fabric`
**Alternativas (elige una):** `fabric`

## `python-machine-learning-book`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,data-mining,data-science,logistic-regression,machine-learning,machine-learning-algorithms,neural-network,python

**Qué es:** Código de la primera edición del libro Python Machine Learning, con ejemplos de algoritmos y evaluación. Presenta notebooks y scripts que acompañan los capítulos y conceptos del libro.
**Stack:** Jupyter Notebook
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/rasbt/python-machine-learning-book

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres estudiar los ejemplos de la primera edición del libro
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `system-prompts-and-models-of-ai-tools`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=prompts,ai,bolt,cluely,copilot,cursor,cursorai,devin

**Qué es:** Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño. Organiza archivos por herramienta para consultar y comparar instrucciones y formatos.
**Stack:** Recursos y documentación
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres investigar patrones de prompts utilizados por asistentes
**Evita si:** no utilizas un agente o flujo compatible con estas instrucciones

## `train-llm-from-scratch`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=aprender,gemini,large-language-models,llm,openai,training,transformers,python

**Qué es:** Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación. Implementa un Transformer y recorre preparación de datos, entrenamiento y ajuste del modelo.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/FareedKhan-dev/train-llm-from-scratch

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres entender el entrenamiento de un LLM mediante una implementación completa
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico
