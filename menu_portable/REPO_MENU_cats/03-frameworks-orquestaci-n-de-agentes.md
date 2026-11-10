# 3. Frameworks & Orquestación de Agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `adk-python`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['google', 'openai', 'anthropic']

**Qué es:** Define agentes y sistemas multiagente con herramientas, memoria y evaluación, con interfaz web de pruebas incluida. Se despliega fácil en Google Cloud.
**Stack:** Python
**Repo:** https://github.com/google/adk-python

**Instalación** [~]: `pip install agent development kit (adk)   (o: uv add agent development kit (adk))`
_Nombre PyPI puede diferir de 'Agent Development Kit (ADK)'; verifica en pypi.org._

**Elige si:** trabajas con Gemini o Google Cloud
**Evita si:** tu stack es OpenAI; mira `openai-agents-python`
**Combina con:** `gemini-cli`, `fastmcp`
**Alternativas (elige una):** `langgraph`, `openai-agents-python`

## `ag2`
role=library · exec=cloud · setup=medium · mcp=False · prov=—

**Qué es:** Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo.
**Stack:** Python
**Repo:** https://github.com/ag2ai/ag2

**Instalación** [~]: `pip install ag2   (o: uv add ag2)`
_Nombre PyPI puede diferir de 'ag2'; verifica en pypi.org._

**Elige si:** construyes multiagente serio en Python
**Evita si:** te basta un agente único o quieres orquestación visual
**Combina con:** `langchain`, `langfuse`
**Alternativas (elige una):** `autogen`

## `agent-framework`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic']

**Qué es:** Une la simplicidad de AutoGen con las capacidades empresariales de Semantic Kernel: workflows con estado, observabilidad y despliegue en Azure.
**Stack:** Python, C#, .NET
**Repo:** https://github.com/microsoft/agent-framework

**Instalación** [~]: `git clone https://github.com/microsoft/agent-framework && cd agent-framework && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** trabajas en el ecosistema Microsoft o .NET
**Evita si:** quieres el ecosistema open source más grande; mira `langgraph`
**Alternativas (elige una):** `autogen`, `semantic-kernel`

## `agent-protocol`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Define cómo se ejecuta un agente, cómo recibe entradas y cómo guarda su estado, sin atarse a un framework. Es una especificación, no un runtime.
**Stack:** OpenAPI, Python
**Repo:** https://github.com/langchain-ai/agent-protocol

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Agent Protocol/). Si necesitas el código: git clone https://github.com/langchain-ai/agent-protocol`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** diseñas una plataforma que sirve agentes de distintos frameworks
**Evita si:** solo necesitas construir un agente
**Combina con:** `langgraph`

## `agno`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Construye agentes con memoria, RAG y herramientas, y sírvelos como API con su plataforma. Antes se llamaba Phidata.
**Stack:** Python, FastAPI
**Repo:** https://github.com/agno-agi/agno

**Instalación** [~]: `git clone https://github.com/agno-agi/agno && cd agno && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un framework de agentes con memoria y API lista
**Evita si:** necesitas grafos explícitos y controlables; mira `langgraph`
**Combina con:** `qdrant`, `mem0`
**Alternativas (elige una):** `crewai`

## `aider`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Le pides cambios en lenguaje natural y Aider edita los archivos y confirma cada cambio en Git. Funciona con casi cualquier modelo.
**Stack:** Python, tree-sitter, Git
**Repo:** https://github.com/Aider-AI/aider

**Instalación** [~]: `git clone https://github.com/Aider-AI/aider && cd aider && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un agente sencillo que trabaje con Git paso a paso
**Evita si:** necesitas autonomía en tareas largas; mira `claude-code`
**Combina con:** `ollama`, `litellm`
**Alternativas (elige una):** `opencode`, `cline`, `continue`

## `autogen`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Popularizó los sistemas multiagente que conversan para resolver tareas. Microsoft recomienda usar Agent Framework para proyectos nuevos.
**Stack:** Python, .NET
**Repo:** https://github.com/microsoft/autogen

**Instalación** [~]: `git clone https://github.com/microsoft/autogen && cd autogen && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** mantienes un proyecto que ya usa AutoGen
**Evita si:** empiezas algo nuevo; mira `agent-framework`
**Combina con:** `litellm`
**Alternativas (elige una):** `agent-framework`, `ag2`, `crewai`

## `autogpt`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=['openai', 'anthropic']

**Qué es:** El famoso proyecto de agentes autónomos evolucionó a una plataforma con editor de bloques, marketplace y servidor para agentes que corren en segundo plano.
**Stack:** Python, TypeScript, Next.js, Docker
**Repo:** https://github.com/Significant-Gravitas/AutoGPT

**Instalación** [~]: `git clone https://github.com/Significant-Gravitas/AutoGPT && cd AutoGPT && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres agentes continuos con un editor visual propio
**Evita si:** buscas algo ligero y fácil de operar; mira `sim` o `flowise`
**Combina con:** `n8n`
**Alternativas (elige una):** `sim`, `langflow`, `flowise`

## `autoresearch`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Proyecto pequeño y exploratorio de Karpathy, más que una herramienta pulida.
**Stack:** Python
**Repo:** https://github.com/karpathy/autoresearch

**Instalación** [~]: `git clone https://github.com/karpathy/autoresearch && cd autoresearch && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** experimentas con research iterativo o quieres un punto de partida
**Evita si:** quieres salida pulida y lista (gpt-researcher)
**Combina con:** `gpt-researcher`, `crawl4ai`

## `awesome-langgraph`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Es una lista curada, no una herramienta ejecutable.
**Stack:** Markdown / Python-JS (LangGraph)
**Repo:** https://github.com/vonzosten/awesome-LangGraph

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-LangGraph/). Si necesitas el código: git clone https://github.com/vonzosten/awesome-LangGraph`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** construyes con LangGraph y quieres patrones de referencia
**Evita si:** no usas ese ecosistema
**Combina con:** `langchain`

## `claude-code`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=['anthropic', 'mcp']

**Qué es:** Lee y edita archivos, ejecuta comandos, hace commits y abre PRs a partir de instrucciones en lenguaje natural. Se extiende con skills, plugins, subagentes, hooks y servidores MCP.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/anthropics/claude-code

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres el agente de código más capaz para tareas largas en tu repo
**Evita si:** necesitas un agente totalmente abierto y multi-modelo; mira `opencode`
**Combina con:** `superpowers`, `anthropic-skills`, `claude-mem`, `context7`
**Alternativas (elige una):** `codex`, `gemini-cli`, `opencode`, `goose`

## `cline`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Planifica, edita archivos, ejecuta comandos y usa el navegador pidiendo aprobación en cada paso. Admite MCP y casi cualquier proveedor.
**Stack:** TypeScript, VS Code API
**Repo:** https://github.com/cline/cline

**Instalación** [~]: `git clone https://github.com/cline/cline && cd cline && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un agente dentro de VS Code con control de cada paso
**Evita si:** trabajas solo en terminal; mira `opencode`
**Combina con:** `context7`, `playwright-mcp`
**Alternativas (elige una):** `continue`, `aider`

## `codex`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=['openai', 'mcp']

**Qué es:** Lee tu repositorio, propone y aplica cambios y ejecuta comandos dentro de un sandbox. Usa AGENTS.md para el contexto del proyecto y admite MCP.
**Stack:** Rust, TypeScript
**Repo:** https://github.com/openai/codex

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** usas ChatGPT u OpenAI y quieres un agente abierto en terminal
**Evita si:** trabajas con Claude como modelo principal; mira `claude-code`
**Combina con:** `agent-skills`, `spec-kit`, `context7`
**Alternativas (elige una):** `claude-code`, `gemini-cli`, `opencode`

## `composio`
role=platform · exec=cloud · setup=easy · mcp=True · prov=['openai', 'anthropic', 'mcp']

**Qué es:** Da a cualquier agente herramientas listas para Gmail, Slack, GitHub, Notion y cientos más, gestionando OAuth por ti. Funciona con los principales frameworks y por MCP.
**Stack:** TypeScript, Python
**Repo:** https://github.com/ComposioHQ/composio

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** tu agente necesita actuar en muchas apps SaaS
**Evita si:** quieres todo auto-hospedado sin servicio externo
**Combina con:** `langgraph`, `openai-agents-python`, `mastra`

## `computer-use-preview`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=['google']

**Qué es:** Muestra cómo un modelo Gemini con computer use controla un navegador para completar tareas. Es una vista previa, no un agente de propósito general.
**Stack:** Python, Playwright
**Repo:** https://github.com/google-gemini/computer-use-preview

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres probar computer use con Gemini
**Evita si:** buscas automatización web robusta; mira `browser-use` o `stagehand`
**Combina con:** `playwright`
**Alternativas (elige una):** `browser-use`, `skyvern`

## `continue`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Integra chat, edición y autocompletado en el IDE con cualquier modelo, y permite ejecutar comprobaciones de IA en los PRs.
**Stack:** TypeScript, Kotlin
**Repo:** https://github.com/continuedev/continue

**Instalación** [~]: `git clone https://github.com/continuedev/continue && cd continue && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres autocompletado y chat en el IDE con modelos a elección
**Evita si:** buscas un agente autónomo para tareas largas; mira `cline`
**Combina con:** `ollama`
**Alternativas (elige una):** `cline`, `aider`

## `crewai`
role=library · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.
**Stack:** Python
**Repo:** https://github.com/crewAIInc/crewAI

**Instalación** [~]: `pip install crewai   (o: uv add crewai)`
_Nombre PyPI puede diferir de 'crewAI'; verifica en pypi.org._

**Elige si:** quieres velocidad y un modelo mental simple de "equipo"
**Evita si:** necesitas control de bajo nivel o orquestación muy custom
**Combina con:** `langchain`, `mem0`
**Alternativas (elige una):** `autogen`, `langgraph`, `agno`

## `deepagents`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=['anthropic', 'openai']

**Qué es:** Da a cualquier modelo las capacidades de los agentes profundos (planificar, delegar, usar archivos) sin construirlas tú. Cada pieza se puede extender o reemplazar.
**Stack:** Python, LangGraph
**Repo:** https://github.com/langchain-ai/deepagents

**Instalación** [~]: `git clone https://github.com/langchain-ai/deepagents && cd deepagents && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un agente potente sin diseñar el bucle desde cero
**Evita si:** necesitas control total del grafo; usa `langgraph` directamente
**Combina con:** `langgraph`, `langfuse`
**Alternativas (elige una):** `openai-agents-python`

## `deeptutor`
role=app · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'local']

**Qué es:** Resuelve dudas, genera ejercicios y guía el estudio con RAG sobre tu material y memoria del alumno. Es un producto educativo, no un orquestador genérico.
**Stack:** Python, Next.js
**Repo:** https://github.com/HKUDS/DeepTutor

**Instalación** [~]: `git clone https://github.com/HKUDS/DeepTutor && cd DeepTutor && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un tutor con IA sobre tu propio material
**Evita si:** buscas un framework para construir agentes; mira `langgraph`
**Combina con:** `docling`
**Alternativas (elige una):** `open-notebook`

## `deer-flow`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Coordina tareas complejas delegando en agentes especializados.
**Stack:** Python/TS, LangChain, Docker
**Repo:** https://github.com/bytedance/deer-flow

**Instalación** [~]: `git clone https://github.com/bytedance/deer-flow && cd deer-flow && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un orquestador completo y extensible
**Evita si:** buscas algo minimalista o sin Docker
**Combina con:** `gpt-researcher`, `firecrawl`

## `dify`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Combina orquestación de prompts, RAG, agentes, workflows y observabilidad en un mismo producto autoalojable.
**Stack:** Python/TS, React, PostgreSQL, Redis, Docker
**Repo:** https://github.com/langgenius/dify

**Instalación** [~]: `git clone https://github.com/langgenius/dify && cd dify && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres una app IA completa autoalojada
**Evita si:** solo necesitas una librería o un prototipo puntual
**Combina con:** `langflow`, `flowise`
**Alternativas (elige una):** `sim`, `ragflow`

## `dspy`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Defines módulos con firmas de entrada y salida y DSPy optimiza automáticamente los prompts y ejemplos con tus métricas. Útil para pipelines que deben mejorar con datos.
**Stack:** Python
**Repo:** https://github.com/stanfordnlp/dspy

**Instalación** [~]: `pip install dspy   (o: uv add dspy)`
_Nombre PyPI puede diferir de 'DSPy'; verifica en pypi.org._

**Elige si:** quieres optimizar prompts de forma sistemática con datos
**Evita si:** solo necesitas una llamada simple al modelo
**Combina con:** `ragas`, `mlflow`
**Alternativas (elige una):** `promptfoo`

## `e2b`
role=platform · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Arranca microVMs aisladas en milisegundos donde el agente puede ejecutar código, instalar paquetes o usar un escritorio. Muy usado para intérpretes de código y agentes de datos.
**Stack:** Python, TypeScript, Firecracker
**Repo:** https://github.com/e2b-dev/E2B

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** tu agente ejecuta código y necesitas aislarlo
**Evita si:** solo necesitas ejecutar código localmente de confianza
**Combina con:** `smolagents`, `open-swe`
**Alternativas (elige una):** `sandbox`

## `flowise`
role=app · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible.
**Stack:** Node.js/TypeScript, React
**Repo:** https://github.com/FlowiseAI/Flowise

**Instalación** [~]: `git clone https://github.com/FlowiseAI/Flowise && cd Flowise && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un prototipo visual ya, en stack JS
**Evita si:** necesitas plataforma completa con RAG/observabilidad (dify)
**Combina con:** `dify`, `langflow`
**Alternativas (elige una):** `sim`, `autogpt`

## `gemini-cli`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=['google', 'mcp']

**Qué es:** Programa, investiga y automatiza tareas desde la terminal con contexto de millones de tokens y búsqueda de Google integrada. Admite MCP y extensiones.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/google-gemini/gemini-cli

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres un agente de terminal potente con cuota gratuita
**Evita si:** buscas el agente con mejor desempeño en tareas largas; mira `claude-code`
**Combina con:** `stitch-skills`, `context7`
**Alternativas (elige una):** `claude-code`, `codex`, `opencode`

## `goose`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Funciona como app de escritorio o CLI y va más allá del código: automatiza tareas de desarrollo y de sistema con extensiones MCP. Nacido en Block.
**Stack:** Rust, TypeScript, Electron
**Repo:** https://github.com/aaif-goose/goose

**Instalación** [~]: `git clone https://github.com/aaif-goose/goose && cd goose && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un agente abierto con app de escritorio y MCP
**Evita si:** solo programas en terminal y quieres el más usado; mira `opencode`
**Combina con:** `playwright-mcp`, `github-mcp-server`
**Alternativas (elige una):** `opencode`, `claude-code`, `open-interpreter`

## `gpt-researcher`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.
**Stack:** Python, Next.js, FastAPI
**Repo:** https://github.com/assafelovic/gpt-researcher

**Instalación** [~]: `git clone https://github.com/assafelovic/gpt-researcher && cd gpt-researcher && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas research profundo citado
**Evita si:** solo quieres una respuesta corta o un chat simple
**Combina con:** `firecrawl`, `browser-use`
**Alternativas (elige una):** `storm`, `vane`

## `haystack`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Compone pipelines modulares de recuperación, generación y agentes con componentes intercambiables. Muy usado en búsqueda empresarial.
**Stack:** Python
**Repo:** https://github.com/deepset-ai/haystack

**Instalación** [~]: `pip install haystack   (o: uv add haystack)`
_Nombre PyPI puede diferir de 'Haystack'; verifica en pypi.org._

**Elige si:** quieres pipelines de RAG explícitos y listos para producción
**Evita si:** buscas el ecosistema más grande de integraciones; mira `llama-index`
**Combina con:** `qdrant`, `docling`
**Alternativas (elige una):** `llama-index`, `langchain`

## `hermes-agent`
role=app · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.
**Stack:** Rust (Tauri), TypeScript, Python
**Repo:** https://github.com/NousResearch/hermes-agent

**Instalación** [~]: `git clone https://github.com/NousResearch/hermes-agent && cd hermes-agent && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres agentes locales con UI y memoria persistente
**Evita si:** prefieres orquestación en nube o no quieres compilar Tauri
**Combina con:** `ecc`, `odysseus`
**Alternativas (elige una):** `openclaw`, `mercury-agent`

## `langchain`
role=library · exec=cloud · setup=medium · mcp=False · prov=—

**Qué es:** Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.
**Stack:** Python/JS/TS
**Repo:** https://github.com/langchain-ai/langchain

**Instalación** [~]: `pip install langchain   (o: uv add langchain)`
_Nombre PyPI puede diferir de 'langchain'; verifica en pypi.org._

**Elige si:** quieres la base estándar con máximas integraciones
**Evita si:** prefieres mínima abstracción o un solo proveedor sin cambiar
**Combina con:** `langflow`, `langfuse`, `litellm`
**Alternativas (elige una):** `llama-index`, `haystack`, `semantic-kernel`

## `langflow`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código Python.
**Stack:** Python, React, Docker
**Repo:** https://github.com/langflow-ai/langflow

**Instalación** [~]: `git clone https://github.com/langflow-ai/langflow && cd langflow && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** prefieres construir en visual sobre LangChain
**Evita si:** quieres todo en código o no usas LangChain
**Combina con:** `langchain`, `dify`
**Alternativas (elige una):** `sim`, `autogpt`

## `langgraph`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Modela agentes y flujos multiagente como grafos de nodos con estado compartido y checkpoints. Pensado para agentes de producción que deben ser controlables y recuperables.
**Stack:** Python, LangChain
**Repo:** https://github.com/langchain-ai/langgraph

**Instalación** [~]: `git clone https://github.com/langchain-ai/langgraph && cd langgraph && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas agentes con estado, control fino y persistencia
**Evita si:** quieres algo mínimo para un agente simple; mira `smolagents`
**Combina con:** `langchain`, `langfuse`
**Alternativas (elige una):** `crewai`, `openai-agents-python`, `pydantic-ai`, `langgraph-supervisor-py`, `adk-python`

## `langgraph-supervisor-py`
role=library · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Facilitaba el patrón supervisor en sistemas multiagente. LangChain ahora recomienda implementar ese patrón directamente con herramientas.
**Stack:** Python, LangGraph
**Repo:** https://github.com/langchain-ai/langgraph-supervisor-py

**Instalación** [~]: `pip install langgraph supervisor   (o: uv add langgraph supervisor)`
_Nombre PyPI puede diferir de 'LangGraph Supervisor'; verifica en pypi.org._

**Elige si:** mantienes código que ya la usa
**Evita si:** empiezas un proyecto nuevo; usa el patrón con herramientas en `langgraph`
**Alternativas (elige una):** `langgraph`

## `langgraphjs`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Lleva el modelo de grafos con estado, checkpoints y human-in-the-loop de LangGraph al ecosistema JavaScript.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/langchain-ai/langgraphjs

**Instalación** [~]: `git clone https://github.com/langchain-ai/langgraphjs && cd langgraphjs && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres el modelo de LangGraph en TypeScript
**Evita si:** buscas una experiencia TS más integrada; mira `mastra`
**Combina con:** `langfuse`
**Alternativas (elige una):** `mastra`, `vercel-ai`

## `llama-index`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Ofrece cargadores para cientos de fuentes, índices, motores de consulta y agentes centrados en documentos. Su plataforma LlamaParse procesa PDFs complejos.
**Stack:** Python, TypeScript
**Repo:** https://github.com/run-llama/llama_index

**Instalación** [~]: `pip install llamaindex   (o: uv add llamaindex)`
_Nombre PyPI puede diferir de 'LlamaIndex'; verifica en pypi.org._

**Elige si:** tu proyecto gira alrededor de RAG sobre tus documentos
**Evita si:** necesitas orquestación general de agentes; mira `langgraph`
**Combina con:** `qdrant`, `docling`, `ragas`
**Alternativas (elige una):** `haystack`, `langchain`

## `llm-council`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.
**Stack:** Python, React, FastAPI, PostgreSQL
**Repo:** https://github.com/karpathy/llm-council

**Instalación** [~]: `git clone https://github.com/karpathy/llm-council && cd llm-council && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres consenso entre modelos o comparar proveedores
**Evita si:** te basta un único LLM o el coste multi-modelo no es asumible
**Combina con:** `litellm`

## `mastra`
role=library · exec=hybrid · setup=easy · mcp=True · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Reúne en un solo paquete agentes con memoria, workflows con estado, RAG, evals y un playground local. Pensado para equipos web que trabajan en TypeScript.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/mastra-ai/mastra

**Instalación** [~]: `npm install mastra   (o: pnpm add mastra)`
_Nombre npm puede diferir de 'Mastra'; verifica en npmjs.com._

**Elige si:** tu equipo trabaja en TypeScript y quiere agentes completos
**Evita si:** trabajas en Python; mira `langgraph` o `pydantic-ai`
**Combina con:** `copilotkit`, `langfuse`
**Alternativas (elige una):** `langgraphjs`, `vercel-ai`

## `mercury-agent`
role=app · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Recuerda lo importante, pide permiso antes de actuar y trae 31 herramientas, tableros kanban y skills extensibles, con datos en SQLite.
**Stack:** TypeScript, SQLite
**Repo:** https://github.com/cosmicstack-labs/mercury-agent

**Instalación** [~]: `git clone https://github.com/cosmicstack-labs/mercury-agent && cd mercury-agent && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un asistente personal ligero con permisos claros
**Evita si:** buscas el ecosistema más grande; mira `openclaw`
**Combina con:** `claude-mem`
**Alternativas (elige una):** `openclaw`, `hermes-agent`

## `mirofish`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.
**Stack:** Python/web, Docker, PostgreSQL
**Repo:** https://github.com/666ghj/MiroFish

**Instalación** [~]: `git clone https://github.com/666ghj/MiroFish && cd MiroFish && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** simulas futuros/escenarios con muchos actores
**Evita si:** necesitas tareas deterministas o resultados reproducibles
**Combina con:** `openevolve`

## `multica`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.
**Stack:** web/TS, Docker, PostgreSQL
**Repo:** https://github.com/multica-ai/multica

**Instalación** [~]: `git clone https://github.com/multica-ai/multica && cd multica && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** mezclas trabajo humano y agentes en un mismo flujo
**Evita si:** quieres automatización 100% headless o un producto maduro
**Combina con:** `ruflo`, `chatwoot`

## `nemo-agent-toolkit`
role=library · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.
**Stack:** Python, FastAPI (Apache-2.0)
**Repo:** https://github.com/NVIDIA/NeMo-Agent-Toolkit

**Instalación** [~]: `pip install nemo-agent-toolkit   (o: uv add nemo-agent-toolkit)`
_Nombre PyPI puede diferir de 'NeMo-Agent-Toolkit'; verifica en pypi.org._

**Elige si:** trabajas con infra NVIDIA o necesitas guardrails/eval empresarial
**Evita si:** quieres algo ligero y agnóstico
**Combina con:** `langchain`

## `nemoclaw`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Ejecuta agentes populares dentro de los sandboxes de NVIDIA OpenShell con inferencia gestionada y políticas de seguridad. Pensado para empresas.
**Stack:** TypeScript, contenedores
**Repo:** https://github.com/NVIDIA/NemoClaw

**Instalación** [~]: `git clone https://github.com/NVIDIA/NemoClaw && cd NemoClaw && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres correr agentes potentes con aislamiento corporativo
**Evita si:** solo necesitas un sandbox para ejecutar código; mira `e2b`
**Combina con:** `openclaw`, `hermes-agent`, `nemotron`
**Alternativas (elige una):** `sandbox`

## `open-interpreter`
role=runtime · exec=local · setup=easy · mcp=False · prov=['openai', 'local']

**Qué es:** Ejecuta código y comandos en tu máquina para cumplir tareas descritas en lenguaje natural. Su versión actual se enfoca en modelos abiertos.
**Stack:** Rust, Python
**Repo:** https://github.com/openinterpreter/openinterpreter

**Instalación** [~]: `git clone https://github.com/openinterpreter/openinterpreter && cd openinterpreter && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un agente que ejecute código usando modelos abiertos
**Evita si:** buscas un agente maduro para repos grandes; mira `opencode`
**Combina con:** `ollama`, `e2b`
**Alternativas (elige una):** `goose`

## `open-swe`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=['anthropic', 'openai']

**Qué es:** Trabaja en segundo plano a partir de issues o mensajes, planifica, programa en un sandbox y abre PRs. Inspirado en los agentes internos de empresas como Stripe o Ramp.
**Stack:** Python, LangGraph, TypeScript
**Repo:** https://github.com/langchain-ai/open-swe

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres construir el agente de código interno de tu empresa
**Evita si:** solo quieres un agente para tu terminal; mira `claude-code`
**Combina con:** `langgraph`, `e2b`
**Alternativas (elige una):** `openhands`, `swe-agent`

## `openai-agents-python`
role=library · exec=hybrid · setup=easy · mcp=True · prov=['openai']

**Qué es:** Define agentes con instrucciones y herramientas, pasa el control entre ellos y añade validaciones. Funciona con modelos de OpenAI y otros compatibles.
**Stack:** Python
**Repo:** https://github.com/openai/openai-agents-python

**Instalación** [~]: `pip install openai agents sdk   (o: uv add openai agents sdk)`
_Nombre PyPI puede diferir de 'OpenAI Agents SDK'; verifica en pypi.org._

**Elige si:** usas OpenAI y quieres agentes multiagente con poco código
**Evita si:** necesitas control de estado avanzado; mira `langgraph`
**Combina con:** `openai-python`, `fastmcp`
**Alternativas (elige una):** `pydantic-ai`, `langgraph`, `smolagents`, `deepagents`, `adk-python`

## `openclaw`
role=app · exec=hybrid · setup=medium · mcp=True · prov=['anthropic', 'openai', 'local']

**Qué es:** Un solo operador, muchas superficies: el asistente vive en tu equipo, tiene memoria, ejecuta tareas reales y responde por los canales que ya usas. Es uno de los proyectos de IA más populares de GitHub.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/openclaw/openclaw

**Instalación** [~]: `git clone https://github.com/openclaw/openclaw && cd openclaw && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un asistente personal que actúe por tus canales de chat
**Evita si:** necesitas un agente para tu empresa con varios usuarios; mira `hermes-agent`
**Combina con:** `nemoclaw`, `claude-mem`
**Alternativas (elige una):** `hermes-agent`, `mercury-agent`

## `opencode`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Ofrece una TUI cuidada, modo cliente-servidor, LSP y agentes configurables. Sirve si quieres un agente libre de proveedor.
**Stack:** TypeScript, Go, Bun
**Repo:** https://github.com/anomalyco/opencode

**Instalación** [~]: `git clone https://github.com/anomalyco/opencode && cd opencode && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un agente de código abierto y multi-modelo
**Evita si:** prefieres la experiencia oficial de un proveedor; mira `claude-code` o `codex`
**Combina con:** `ollama`, `litellm`, `awesome-agent-skills`
**Alternativas (elige una):** `claude-code`, `codex`, `goose`, `gemini-cli`, `aider`

## `openevolve`
role=runtime · exec=cloud · setup=heavy · mcp=False · prov=—

**Qué es:** Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.
**Stack:** Python, PyTorch/numpy, Rust
**Repo:** https://github.com/algorithmicsuperintelligence/openevolve

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** optimizas problemas algorítmicos donde cabe explorar muchas variantes
**Evita si:** haces tareas de texto comunes o buscas respuesta inmediata
**Combina con:** `llm-council`

## `openhands`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.
**Stack:** Python/TS, Docker
**Repo:** https://github.com/OpenHands/OpenHands

**Instalación** [~]: `git clone https://github.com/OpenHands/OpenHands && cd OpenHands && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un agente que "haga", no solo hable
**Evita si:** solo necesitas chat/RAG o no puedes correr Docker
**Combina con:** `ecc`, `sandbox`
**Alternativas (elige una):** `open-swe`, `swe-agent`

## `pydantic-ai`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Construye agentes con salidas validadas, herramientas tipadas e inyección de dependencias, al estilo FastAPI. Incluye evaluación y observabilidad con Logfire.
**Stack:** Python, Pydantic
**Repo:** https://github.com/pydantic/pydantic-ai

**Instalación** [~]: `pip install pydantic ai   (o: uv add pydantic ai)`
_Nombre PyPI puede diferir de 'Pydantic AI'; verifica en pypi.org._

**Elige si:** quieres agentes tipados y validados en Python
**Evita si:** necesitas grafos complejos con persistencia; mira `langgraph`
**Combina con:** `langfuse`, `fastmcp`
**Alternativas (elige una):** `openai-agents-python`, `smolagents`, `langgraph`

## `ruflo`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Orquesta swarms de agentes especializados a escala.
**Stack:** Rust
**Repo:** https://github.com/ruvnet/ruflo

**Instalación** [?]: `git clone https://github.com/ruvnet/ruflo (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** orquestas muchos agentes a escala y quieres rendimiento
**Evita si:** solo necesitas 1-2 agentes o no usas Claude Code/Codex
**Combina con:** `mem0`, `ecc`

## `sandbox`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** Resuelve el riesgo de dejar que un agente toque tu host: todo corre contenido en un contenedor reproducible.
**Stack:** Docker, web, MCP
**Repo:** https://github.com/agent-infra/sandbox

**Instalación** [~]: `git clone https://github.com/agent-infra/sandbox && cd sandbox && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres aislar la ejecución de agentes y reproducibilidad
**Evita si:** te basta correr local sin sandbox o no puedes asumir el overhead de Docker
**Combina con:** `openhands`, `ecc`
**Alternativas (elige una):** `nemoclaw`, `e2b`

## `semantic-kernel`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['openai']

**Qué es:** Pensado para empresas que ya usan .NET o Java y quieren añadir IA con patrones conocidos. Su evolución para agentes es Microsoft Agent Framework.
**Stack:** C#, Python, Java
**Repo:** https://github.com/microsoft/semantic-kernel

**Instalación** [~]: `pip install semantic kernel   (o: uv add semantic kernel)`
_Nombre PyPI puede diferir de 'Semantic Kernel'; verifica en pypi.org._

**Elige si:** tu app es .NET o Java y quieres IA integrada
**Evita si:** empiezas un sistema de agentes nuevo; mira `agent-framework`
**Alternativas (elige una):** `agent-framework`, `langchain`

## `sim`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Diseña agentes conectando bloques en un canvas, prueba en vivo y despliega como API o chat. Open source y auto-hospedable.
**Stack:** TypeScript, Next.js, PostgreSQL
**Repo:** https://github.com/simstudioai/sim

**Instalación** [~]: `git clone https://github.com/simstudioai/sim && cd sim && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un constructor visual de agentes moderno y abierto
**Evita si:** prefieres automatización general con cientos de apps; mira `n8n`
**Combina con:** `ollama`, `langfuse`
**Alternativas (elige una):** `flowise`, `langflow`, `dify`, `autogpt`

## `smolagents`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'local']

**Qué es:** Sus agentes expresan las acciones como código en vez de JSON, lo que reduce pasos y errores. El núcleo cabe en unas mil líneas.
**Stack:** Python
**Repo:** https://github.com/huggingface/smolagents

**Instalación** [~]: `pip install smolagents   (o: uv add smolagents)`
_Nombre PyPI puede diferir de 'smolagents'; verifica en pypi.org._

**Elige si:** quieres un agente simple y transparente en Python
**Evita si:** necesitas flujos con estado y aprobación humana; mira `langgraph`
**Combina con:** `e2b`, `transformers`
**Alternativas (elige una):** `pydantic-ai`, `openai-agents-python`

## `storm`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['openai']

**Qué es:** Simula conversaciones entre perspectivas para hacer preguntas, busca fuentes y redacta un artículo estructurado y citado. Útil para informes de fondo.
**Stack:** Python, DSPy
**Repo:** https://github.com/stanford-oval/storm

**Instalación** [~]: `git clone https://github.com/stanford-oval/storm && cd storm && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas informes largos y citados sobre un tema
**Evita si:** quieres respuestas cortas con fuentes; mira `gpt-researcher`
**Combina con:** `searxng`, `firecrawl`
**Alternativas (elige una):** `gpt-researcher`

## `swe-agent`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic']

**Qué es:** Resuelve issues reales con el modelo que elijas y sirve como base de investigación en agentes de software. También tiene usos en ciberseguridad y retos de programación.
**Stack:** Python, Docker
**Repo:** https://github.com/SWE-agent/SWE-agent

**Instalación** [~]: `git clone https://github.com/SWE-agent/SWE-agent && cd SWE-agent && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** investigas o automatizas la resolución de issues
**Evita si:** quieres un asistente diario en tu terminal; mira `claude-code`
**Combina con:** `swe-bench`, `litellm`
**Alternativas (elige una):** `openhands`, `open-swe`

## `t3code`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** No sustituye al agente: orquesta Claude Code, Codex y otros desde una UI cómoda, también en el móvil. Útil para lanzar y revisar sesiones a distancia.
**Stack:** TypeScript, Electron, React Native
**Repo:** https://github.com/pingdotgg/t3code

**Instalación** [~]: `git clone https://github.com/pingdotgg/t3code && cd t3code && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** usas varios agentes de código y quieres controlarlos desde una UI
**Evita si:** solo usas un agente en la terminal
**Combina con:** `claude-code`, `codex`, `opencode`

## `vercel-ai`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Unifica la llamada a decenas de proveedores con una API común y trae hooks de React para chat con streaming. Es la base de muchos frameworks de agentes en TS.
**Stack:** TypeScript, React, Next.js
**Repo:** https://github.com/vercel/ai

**Instalación** [~]: `npm install ai sdk (vercel)   (o: pnpm add ai sdk (vercel))`
_Nombre npm puede diferir de 'AI SDK (Vercel)'; verifica en npmjs.com._

**Elige si:** construyes una app web con IA en TypeScript
**Evita si:** necesitas agentes complejos con memoria y workflows; mira `mastra`
**Combina con:** `ui`, `assistant-ui`
**Alternativas (elige una):** `langgraphjs`, `mastra`
