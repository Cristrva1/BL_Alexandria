# 6. Memoria, LLM Ops & Observabilidad — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agentmemory`
role=library · exec=hybrid · setup=easy · mcp=True · prov=['openai', 'anthropic', 'google', 'mcp']

**Qué es:** memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes.
**Stack:** motor iii
**Repo:** https://github.com/rohitg00/agentmemory

**Instalación** [?]: `git clone https://github.com/rohitg00/agentmemory (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** cambias de asistente y quieres una memoria común
**Evita si:** te basta la memoria nativa del cliente.
**Combina con:** `mem0`, `ruflo`

## `headroom`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'mcp']

**Qué es:** utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial.
**Stack:** Python/TS
**Repo:** https://github.com/chopratejas/headroom

**Instalación** [~]: `pip install headroom   (o: uv add headroom)`
_Nombre PyPI puede diferir de 'headroom'; verifica en pypi.org._

**Elige si:** te quedas sin contexto
**Evita si:** tus prompts ya caben holgados.
**Combina con:** `context-engineering`, `codegraph`

## `langfuse`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente.
**Stack:** TS, Docker, self-host/cloud
**Repo:** https://github.com/langfuse/langfuse

**Instalación** [~]: `git clone https://github.com/langfuse/langfuse && cd langfuse && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** operas agentes en serio
**Evita si:** haces prototipos triviales.
**Combina con:** `langchain`, `litellm`, `ag2`

## `litellm`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.
**Stack:** Python
**Repo:** https://github.com/BerriAI/litellm

**Instalación** [~]: `pip install litellm   (o: uv add litellm)`
_Nombre PyPI puede diferir de 'litellm'; verifica en pypi.org._

**Elige si:** trabajas con múltiples modelos
**Evita si:** usas un único proveedor fijo.
**Combina con:** `langchain`, `langfuse`, `llm-council`

## `llmfit`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['local']

**Qué es:** herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar modelos con datos.
**Stack:** Go/Python
**Repo:** https://github.com/AlexsJones/llmfit

**Instalación** [~]: `pip install llmfit   (o: uv add llmfit)`
_Nombre PyPI puede diferir de 'llmfit'; verifica en pypi.org._

**Elige si:** necesitas elegir modelo con datos
**Evita si:** ya tienes el modelo decidido.
**Combina con:** `litellm`, `langfuse`

## `loguru`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa.
**Stack:** Python
**Repo:** https://github.com/Delgan/loguru

**Instalación** [~]: `pip install loguru   (o: uv add loguru)`
_Nombre PyPI puede diferir de 'loguru'; verifica en pypi.org._

**Elige si:** quieres logging fácil en Python
**Evita si:** ya usas el stdlib `logging` configurado.

## `mem0`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental.
**Stack:** Python/TS
**Repo:** https://github.com/mem0ai/mem0

**Instalación** [~]: `pip install mem0   (o: uv add mem0)`
_Nombre PyPI puede diferir de 'mem0'; verifica en pypi.org._

**Elige si:** quieres memoria estándar lista
**Evita si:** necesitas todo local sin API ([mempalace](#-mempalace)).
**Combina con:** `crewai`, `langchain`
**Alternativas (elige una):** `mempalace`

## `mempalace`
role=library · exec=local · setup=easy · mcp=False · prov=['anthropic', 'mcp']

**Qué es:** memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.
**Stack:** Python (PyPI)
**Repo:** https://github.com/MemPalace/mempalace

**Instalación** [~]: `pip install mempalace   (o: uv add mempalace)`
_Nombre PyPI puede diferir de 'mempalace'; verifica en pypi.org._

**Elige si:** la privacidad es prioridad
**Evita si:** quieres un SaaS gestionado.
**Combina con:** `open-notebook`, `odysseus`

## `sandbox`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=['mcp']

**Qué es:** entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado.
**Stack:** Docker/web
**Repo:** https://github.com/agent-infra/sandbox

**Instalación** [~]: `git clone https://github.com/agent-infra/sandbox && cd sandbox && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres aislar la ejecución de agentes
**Evita si:** te basta correr local sin sandbox.
**Combina con:** `openhands`, `ecc`

## `turbovec`
role=library · exec=local · setup=easy · mcp=False · prov=['openai', 'local']

**Qué es:** librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida.
**Stack:** Python / Rust
**Repo:** https://github.com/RyanCodrai/turbovec

**Instalación** [~]: `pip install turbovec   (o: uv add turbovec)`
_Nombre PyPI puede diferir de 'turbovec'; verifica en pypi.org._

**Elige si:** necesitas vector search veloz
**Evita si:** ya usas una vector DB completa.
**Combina con:** `mem0`, `graphrag`
