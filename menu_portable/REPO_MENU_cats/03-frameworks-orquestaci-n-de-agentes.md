# 3. Frameworks & Orquestación de Agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ag2`
role=library · exec=cloud · setup=medium · mcp=False · prov=['openai']

**Qué es:** framework maduro para sistemas multiagente con patrones de colaboración (heredero de AutoGen). Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo.
**Stack:** Python
**Repo:** https://github.com/ag2ai/ag2

**Instalación** [~]: `pip install ag2   (o: uv add ag2)`
_Nombre PyPI puede diferir de 'ag2'; verifica en pypi.org._

**Elige si:** construyes multiagente serio
**Evita si:** te basta un agente único.
**Combina con:** `langchain`, `langfuse`

## `autogen`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** AutoGen ![Maintenance Mode](https://github.com/microsoft/agent-framework).
**Stack:** python, typescript, javascript, postgres
**Repo:** https://github.com/microsoft/autogen.git

**Instalación** [~]: `git clone https://github.com/microsoft/autogen.git && cd autogen && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres autogen [![maintenance mode](https://img.shields.io/badge/status-maintenance%20m
**Evita si:** —

## `autoresearch`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic']

**Qué es:** enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. Proyecto pequeño y exploratorio más que una herramienta pulida.
**Stack:** Python
**Repo:** https://github.com/karpathy/autoresearch

**Instalación** [~]: `git clone https://github.com/karpathy/autoresearch && cd autoresearch && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** experimentas con research iterativo
**Evita si:** quieres salida pulida ([gpt-researcher](#-gpt-researcher)).
**Combina con:** `gpt-researcher`, `crawl4ai`
**Alternativas (elige una):** `gpt-researcher`

## `awesome-langgraph`
role=directory · exec=cloud · setup=easy · mcp=False · prov=['mcp']

**Qué es:** repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. Es una lista curada, no una herramienta ejecutable.
**Stack:** Markdown / Python-JS
**Repo:** https://github.com/von-development/awesome-LangGraph

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-LangGraph/). Si necesitas el código: git clone https://github.com/von-development/awesome-LangGraph`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** construyes con LangGraph
**Evita si:** no usas ese ecosistema.
**Combina con:** `langchain`

## `crewai`
role=library · exec=cloud · setup=easy · mcp=False · prov=['anthropic', 'mcp']

**Qué es:** framework para orquestar "crews" de agentes con roles y tareas. Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.
**Stack:** Python
**Repo:** https://github.com/crewAIInc/crewAI

**Instalación** [~]: `pip install crewai   (o: uv add crewai)`
_Nombre PyPI puede diferir de 'crewAI'; verifica en pypi.org._

**Elige si:** quieres velocidad
**Evita si:** necesitas control de bajo nivel.
**Combina con:** `langchain`, `mem0`

## `deer-flow`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google', 'mcp']

**Qué es:** super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. Coordina tareas complejas delegando en agentes especializados.
**Stack:** Python/TS
**Repo:** https://github.com/bytedance/deer-flow

**Instalación** [~]: `git clone https://github.com/bytedance/deer-flow && cd deer-flow && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un orquestador completo
**Evita si:** buscas algo minimalista.
**Combina con:** `gpt-researcher`, `firecrawl`

## `defending-code-reference-harness`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** A reference implementation for autonomous vulnerability discovery and remediation with Claude, based on our learnings from [partnering with security teams at several organizations](https://www.anthropic.com/glasswing) since launching Claude Mythos Preview. For a write up of these learnings along with best practices, see the [accompanying blog post](https://claude.com/blog/using-llms-to-secure-sour
**Stack:** python, typescript, docker
**Repo:** https://github.com/anthropics/defending-code-reference-harness.git

**Instalación** [~]: `pip install defending-code-reference-harness   (o: uv add defending-code-reference-harness)`
_Nombre PyPI puede diferir de 'defending-code-reference-harness'; verifica en pypi.org._

**Elige si:** quieres defending code reference harness
**Evita si:** —
**Combina con:** `ag2`, `crewai`, `langchain`

## `dify`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'local']

**Qué es:** plataforma integral para construir apps de IA con backend y UI listos. Combina orquestación de prompts, RAG, agentes y observabilidad en un mismo producto autoalojable.
**Stack:** Python/TS, Docker
**Repo:** https://github.com/langgenius/dify

**Instalación** [~]: `git clone https://github.com/langgenius/dify && cd dify && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres una app IA completa
**Evita si:** solo necesitas una librería.
**Combina con:** `langflow`, `flowise`

## `flowise`
role=app · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** builder visual drag-and-drop para pipelines LLM. Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible.
**Stack:** Node.js, web
**Repo:** https://github.com/FlowiseAI/Flowise

**Instalación** [~]: `git clone https://github.com/FlowiseAI/Flowise && cd Flowise && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un prototipo ya
**Evita si:** necesitas plataforma completa ([dify](#-dify)).
**Combina con:** `dify`, `langflow`
**Alternativas (elige una):** `dify`

## `gpt-researcher`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** agente autónomo que investiga en línea y consolida reportes citados y estructurados. Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.
**Stack:** Python, Next.js, FastAPI
**Repo:** https://github.com/assafelovic/gpt-researcher

**Instalación** [~]: `git clone https://github.com/assafelovic/gpt-researcher && cd gpt-researcher && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas research profundo citado
**Evita si:** solo quieres una respuesta corta.
**Combina con:** `firecrawl`, `browser-use`

## `guardrails`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** LATEST RELEASE / DEVELOPMENT VERSION**: The [develop](https://github.com/NVIDIA-NeMo/Guardrails/tree/develop) branch tracks the latest top of tree development. The latest released version is [0.21.0](https://github.com/NVIDIA-NeMo/Guardrails/tree/v0.21.0).
**Stack:** python, typescript, javascript, docker, langchain
**Repo:** https://github.com/NVIDIA-NeMo/Guardrails.git

**Instalación** [~]: `git clone https://github.com/NVIDIA-NeMo/Guardrails.git && cd Guardrails && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres nvidia nemo guardrails library
**Evita si:** —
**Combina con:** `ag2`, `crewai`, `langchain`

## `hermes-agent`
role=app · exec=local · setup=medium · mcp=False · prov=['openai', 'mcp']

**Qué es:** entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.
**Stack:** Rust (Tauri), TypeScript, Python
**Repo:** https://github.com/NousResearch/hermes-agent

**Instalación** [~]: `git clone https://github.com/NousResearch/hermes-agent && cd hermes-agent && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres agentes locales con UI
**Evita si:** prefieres orquestación en nube.
**Combina con:** `ecc`, `odysseus`

## `langchain`
role=library · exec=cloud · setup=medium · mcp=False · prov=['openai']

**Qué es:** framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.
**Stack:** Python/JS
**Repo:** https://github.com/langchain-ai/langchain

**Instalación** [~]: `pip install langchain   (o: uv add langchain)`
_Nombre PyPI puede diferir de 'langchain'; verifica en pypi.org._

**Elige si:** quieres la base estándar
**Evita si:** prefieres mínima abstracción.
**Combina con:** `langflow`, `langfuse`, `litellm`

## `langflow`
role=app · exec=hybrid · setup=medium · mcp=False · prov=['mcp']

**Qué es:** constructor visual de flujos LLM/agentes construido sobre LangChain. Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código.
**Stack:** Python, web
**Repo:** https://github.com/langflow-ai/langflow

**Instalación** [~]: `git clone https://github.com/langflow-ai/langflow && cd langflow && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** prefieres construir en visual
**Evita si:** quieres todo en código.
**Combina con:** `langchain`, `dify`

## `llm-council`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.
**Stack:** Python/web
**Repo:** https://github.com/karpathy/llm-council

**Instalación** [~]: `git clone https://github.com/karpathy/llm-council && cd llm-council && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres consenso entre modelos
**Evita si:** te basta un único LLM.
**Combina con:** `litellm`

## `mirofish`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=['openai']

**Qué es:** motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.
**Stack:** Python/web
**Repo:** https://github.com/666ghj/MiroFish

**Instalación** [~]: `git clone https://github.com/666ghj/MiroFish && cd MiroFish && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** simulas futuros/escenarios
**Evita si:** necesitas tareas deterministas.
**Combina con:** `openevolve`

## `multica`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['anthropic', 'google']

**Qué es:** plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas"). Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.
**Stack:** web/TS
**Repo:** https://github.com/multica-ai/multica

**Instalación** [?]: `git clone https://github.com/multica-ai/multica (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** mezclas trabajo humano y agentes
**Evita si:** quieres automatización 100% headless.
**Combina con:** `ruflo`, `chatwoot`

## `nemo-agent-toolkit`
role=library · exec=hybrid · setup=heavy · mcp=False · prov=['mcp', 'local']

**Qué es:** toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.
**Stack:** Python (Apache-2.0)
**Repo:** https://github.com/NVIDIA/NeMo-Agent-Toolkit

**Instalación** [~]: `pip install nemo-agent-toolkit   (o: uv add nemo-agent-toolkit)`
_Nombre PyPI puede diferir de 'NeMo-Agent-Toolkit'; verifica en pypi.org._

**Elige si:** trabajas con infra NVIDIA
**Evita si:** quieres algo ligero.
**Combina con:** `langchain`

## `openevolve`
role=runtime · exec=cloud · setup=heavy · mcp=False · prov=['openai', 'google']

**Qué es:** agente de codificación evolutivo que optimiza algoritmos por simulación genética. Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.
**Stack:** Python, PyTorch/numpy, Rust
**Repo:** https://github.com/algorithmicsuperintelligence/openevolve

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** optimizas problemas algorítmicos
**Evita si:** haces tareas de texto comunes.
**Combina con:** `llm-council`

## `openhands`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['anthropic', 'google']

**Qué es:** plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.
**Stack:** Python/TS, Docker
**Repo:** https://github.com/All-Hands-AI/OpenHands

**Instalación** [~]: `git clone https://github.com/All-Hands-AI/OpenHands && cd OpenHands && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un agente que "haga", no solo hable
**Evita si:** solo necesitas chat/RAG.
**Combina con:** `ecc`, `sandbox`

## `repomix`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Need discussion? Join us on <a href="https://discord.gg/wNYzTwZFku">Discord</a>!<br>.
**Stack:** javascript/typescript, typescript, javascript, docker, postgres
**Repo:** https://github.com/yamadashy/repomix.git

**Instalación** [~]: `npm install repomix   (o: pnpm add repomix)`
_Nombre npm puede diferir de 'repomix'; verifica en npmjs.com._

**Elige si:** quieres <div align="center" markdown="1">
**Evita si:** —
**Combina con:** `ag2`, `crewai`, `langchain`

## `ruflo`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=['anthropic', 'mcp', 'local']

**Qué es:** harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). Orquesta swarms de agentes especializados a escala.
**Stack:** Rust
**Repo:** https://github.com/ruvnet/ruflo

**Instalación** [?]: `git clone https://github.com/ruvnet/ruflo (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** orquestas muchos agentes a escala
**Evita si:** solo necesitas 1-2 agentes.
**Combina con:** `mem0`, `ecc`

## `tooljet`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** :star: If you find ToolJet useful, please consider giving us a star on GitHub! Your support helps us continue to innovate and deliver exciting features.
**Stack:** javascript/typescript, python, typescript, javascript, docker, postgres
**Repo:** https://github.com/ToolJet/ToolJet.git

**Instalación** [~]: `git clone https://github.com/ToolJet/ToolJet.git && cd ToolJet && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres tooljet is the open-source foundation of tooljet ai - the ai-native platform for
**Evita si:** —
**Combina con:** `ag2`, `crewai`, `langchain`
