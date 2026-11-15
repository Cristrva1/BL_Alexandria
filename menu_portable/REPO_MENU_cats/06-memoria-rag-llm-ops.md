# 6. Memoria, RAG & LLM Ops — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agentmemory`
role=library · exec=hybrid · setup=easy · mcp=True · prov=—

**Qué es:** Resuelve el "re-explica todo" al cambiar de asistente: la memoria vive fuera del cliente.
**Stack:** motor iii, MCP
**Repo:** https://github.com/rohitg00/agentmemory

**Instalación** [?]: `git clone https://github.com/rohitg00/agentmemory (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** cambias de asistente y quieres una memoria común entre ellos
**Evita si:** te basta la memoria nativa de un único cliente o no usas MCP
**Combina con:** `mem0`, `ruflo`
**Alternativas (elige una):** `engram`, `supermemory`, `claude-mem`

## `chroma`
role=runtime · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Se usa embebida en tu script Python o como servidor, con embeddings automáticos. Perfecta para prototipos de RAG.
**Stack:** Rust, Python, TypeScript
**Repo:** https://github.com/chroma-core/chroma

**Instalación** [~]: `git clone https://github.com/chroma-core/chroma && cd chroma && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** empiezas con RAG y quieres lo más simple
**Evita si:** necesitas gran escala y filtros complejos; mira `qdrant` o `milvus`
**Combina con:** `llama-index`, `langchain`
**Alternativas (elige una):** `qdrant`, `pgvector`, `milvus`, `faiss`

## `claude-mem`
role=skill · exec=local · setup=easy · mcp=True · prov=['anthropic', 'mcp']

**Qué es:** Registra lo que hace el agente en cada sesión, lo resume y vuelve a inyectar lo relevante al empezar la siguiente. Evita repetir contexto en proyectos largos.
**Stack:** TypeScript, SQLite, Chroma
**Repo:** https://github.com/thedotmack/claude-mem

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/claude-mem/). Si necesitas el código: git clone https://github.com/thedotmack/claude-mem`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** usas Claude Code a diario y repites contexto entre sesiones
**Evita si:** necesitas memoria para una app propia; mira `mem0`
**Combina con:** `claude-code`, `superpowers`
**Alternativas (elige una):** `engram`, `agentmemory`

## `cognee`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'local']

**Qué es:** Convierte documentos y conversaciones en un grafo de conocimiento consultable para dar memoria de largo plazo a tus agentes.
**Stack:** Python
**Repo:** https://github.com/topoteretes/cognee

**Instalación** [~]: `pip install cognee   (o: uv add cognee)`
_Nombre PyPI puede diferir de 'cognee'; verifica en pypi.org._

**Elige si:** quieres memoria basada en grafo con poco esfuerzo
**Evita si:** necesitas un grafo temporal en tiempo real; mira `graphiti`
**Combina con:** `qdrant`, `mcp-neo4j`
**Alternativas (elige una):** `graphiti`, `mem0`, `graphrag`, `letta`

## `deepeval`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai']

**Qué es:** Escribe pruebas para tus apps de LLM con métricas como fidelidad, relevancia o alucinación, e intégralas en tu CI.
**Stack:** Python
**Repo:** https://github.com/confident-ai/deepeval

**Instalación** [~]: `pip install deepeval   (o: uv add deepeval)`
_Nombre PyPI puede diferir de 'DeepEval'; verifica en pypi.org._

**Elige si:** quieres tests de LLM en Python como pytest
**Evita si:** prefieres configurar en YAML y comparar modelos; mira `promptfoo`
**Combina con:** `langfuse`
**Alternativas (elige una):** `ragas`, `promptfoo`

## `engram`
role=runtime · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Da a cualquier agente compatible con MCP una memoria local de decisiones y aprendizajes, sin dependencias pesadas.
**Stack:** Go, SQLite
**Repo:** https://github.com/Gentleman-Programming/engram

**Instalación** [?]: `git clone https://github.com/Gentleman-Programming/engram (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres memoria local simple para cualquier agente
**Evita si:** solo usas Claude Code y quieres algo automático; mira `claude-mem`
**Combina con:** `claude-code`, `opencode`
**Alternativas (elige una):** `claude-mem`, `agentmemory`

## `faiss`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Base de muchas bases vectoriales; ideal para investigación o cuando quieres índices en memoria sin servidor.
**Stack:** C++, Python, CUDA
**Repo:** https://github.com/facebookresearch/faiss

**Instalación** [~]: `pip install faiss   (o: uv add faiss)`
_Nombre PyPI puede diferir de 'Faiss'; verifica en pypi.org._

**Elige si:** necesitas índices vectoriales en memoria y máximo control
**Evita si:** quieres persistencia y API listas; mira `qdrant`
**Combina con:** `transformers`
**Alternativas (elige una):** `qdrant`, `chroma`

## `graphiti`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic']

**Qué es:** Actualiza el grafo con cada nuevo dato sin recalcular todo y guarda cuándo era válido cada hecho. Ideal para memoria de agentes que cambia.
**Stack:** Python, Neo4j
**Repo:** https://github.com/getzep/graphiti

**Instalación** [~]: `pip install graphiti   (o: uv add graphiti)`
_Nombre PyPI puede diferir de 'Graphiti'; verifica en pypi.org._

**Elige si:** necesitas memoria que cambie con el tiempo y se pueda consultar
**Evita si:** solo quieres RAG sobre documentos estáticos; mira `lightrag`
**Combina con:** `mcp-neo4j`
**Alternativas (elige una):** `cognee`, `graphrag`

## `graphrag`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve las preguntas que requieren conectar entidades dispersas en muchos documentos, donde el RAG clásico falla.
**Stack:** Python
**Repo:** https://github.com/microsoft/graphrag

**Instalación** [~]: `pip install graphrag   (o: uv add graphrag)`
_Nombre PyPI puede diferir de 'graphrag'; verifica en pypi.org._

**Elige si:** tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto
**Evita si:** un RAG simple basta o el coste de indexado con LLM es prohibitivo
**Combina con:** `graphify`, `mcp-neo4j`, `turbovec`
**Alternativas (elige una):** `graphiti`, `cognee`, `lightrag`

## `guardrails`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Controla de qué puede hablar tu bot, bloquea jailbreaks y valida entradas y salidas con reglas en el lenguaje Colang.
**Stack:** Python, Colang
**Repo:** https://github.com/NVIDIA-NeMo/Guardrails

**Instalación** [~]: `pip install nemo guardrails   (o: uv add nemo guardrails)`
_Nombre PyPI puede diferir de 'NeMo Guardrails'; verifica en pypi.org._

**Elige si:** necesitas políticas de seguridad en un chatbot
**Evita si:** solo quieres probar vulnerabilidades; mira `promptfoo`
**Combina con:** `langchain`

## `headroom`
role=library · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el dolor habitual de los agentes: quedarse sin ventana de contexto a mitad de una tarea larga.
**Stack:** Python/TypeScript
**Repo:** https://github.com/headroomlabs-ai/headroom

**Instalación** [~]: `pip install headroom   (o: uv add headroom)`
_Nombre PyPI puede diferir de 'headroom'; verifica en pypi.org._

**Elige si:** te quedas sin contexto en sesiones largas
**Evita si:** tus prompts ya caben holgados o la pérdida de detalle por resumen es inaceptable
**Combina con:** `context-engineering`, `codegraph`

## `langfuse`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve la opacidad: ves qué prompt, qué modelo, qué coste y qué salida tuvo cada paso de tu pipeline.
**Stack:** TypeScript, Docker, PostgreSQL, self-host/cloud
**Repo:** https://github.com/langfuse/langfuse

**Instalación** [~]: `git clone https://github.com/langfuse/langfuse && cd langfuse && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** operas agentes en serio y necesitas trazas/costes/eval
**Evita si:** haces prototipos triviales o no quieres operar el backend
**Combina con:** `langchain`, `litellm`, `ag2`
**Alternativas (elige una):** `phoenix`, `opik`, `mlflow`

## `letta`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Crea agentes que gestionan su propia memoria en bloques editables y archivos, y persisten entre conversaciones. Incluye servidor, API y entorno de desarrollo.
**Stack:** Python, PostgreSQL
**Repo:** https://github.com/letta-ai/letta

**Instalación** [~]: `git clone https://github.com/letta-ai/letta && cd letta && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres agentes con memoria de largo plazo gestionada
**Evita si:** solo necesitas una capa de memoria para tu app; mira `mem0`
**Combina con:** `ollama`
**Alternativas (elige una):** `mem0`, `cognee`

## `lightrag`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'local']

**Qué es:** Construye un grafo de entidades a partir de tus documentos y consulta en modo local, global o híbrido. Más barato que GraphRAG.
**Stack:** Python
**Repo:** https://github.com/HKUDS/LightRAG

**Instalación** [~]: `pip install lightrag   (o: uv add lightrag)`
_Nombre PyPI puede diferir de 'LightRAG'; verifica en pypi.org._

**Elige si:** quieres RAG con grafo sin el coste de GraphRAG
**Evita si:** no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index`
**Combina con:** `ollama`, `qdrant`
**Alternativas (elige una):** `graphrag`, `ragflow`, `pageindex`

## `litellm`
role=library · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el lock-in: cambias de proveedor o añades fallback sin reescribir el código de tu app.
**Stack:** Python
**Repo:** https://github.com/BerriAI/litellm

**Instalación** [~]: `pip install litellm   (o: uv add litellm)`
_Nombre PyPI puede diferir de 'litellm'; verifica en pypi.org._

**Elige si:** trabajas con múltiples modelos o quieres fallback/control de costos
**Evita si:** usas un único proveedor fijo y no necesitas abstracción
**Combina con:** `langchain`, `langfuse`, `llm-council`

## `loguru`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve la fricción del módulo `logging` stdlib, que exige boilerplate para algo tan básico como imprimir logs legibles.
**Stack:** Python
**Repo:** https://github.com/Delgan/loguru

**Instalación** [~]: `pip install loguru   (o: uv add loguru)`
_Nombre PyPI puede diferir de 'loguru'; verifica en pypi.org._

**Elige si:** quieres logging fácil y legible en Python sin pelear con stdlib
**Evita si:** ya usas el stdlib `logging` configurado o tienes un stack de observabilidad corporativo
**Combina con:** `litellm`

## `mem0`
role=library · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el "amnesia" del LLM: el agente conserva preferencias y hechos entre sesiones sin reenviar todo el historial.
**Stack:** Python/TypeScript, vector DBs (Qdrant, Chroma, pgvector)
**Repo:** https://github.com/mem0ai/mem0

**Instalación** [~]: `pip install mem0   (o: uv add mem0)`
_Nombre PyPI puede diferir de 'mem0'; verifica en pypi.org._

**Elige si:** quieres memoria estándar lista con integraciones amplias
**Evita si:** necesitas todo local sin llamadas a API (mempalace) o control total del almacenamiento
**Combina con:** `crewai`, `langchain`, `agentmemory`
**Alternativas (elige una):** `letta`, `cognee`, `supermemory`

## `mempalace`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve la memoria privada: cero llamadas a API, tus textos no salen de tu máquina.
**Stack:** Python (PyPI)
**Repo:** https://github.com/MemPalace/mempalace

**Instalación** [~]: `pip install mempalace   (o: uv add mempalace)`
_Nombre PyPI puede diferir de 'mempalace'; verifica en pypi.org._

**Elige si:** la privacidad es prioridad y no quieres llamadas a API
**Evita si:** quieres un SaaS gestionado con escalado automático o integraciones de framework ya hechas (mem0)
**Combina con:** `open-notebook`, `odysseus`

## `milvus`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Pensada para producción con grandes volúmenes, alta disponibilidad y varios tipos de índices. Tiene una versión ligera para empezar.
**Stack:** Go, C++, Kubernetes
**Repo:** https://github.com/milvus-io/milvus

**Instalación** [?]: `git clone https://github.com/milvus-io/milvus (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** esperas volúmenes muy grandes de vectores
**Evita si:** tu proyecto es pequeño; mira `chroma` o `qdrant`
**Combina con:** `llama-index`
**Alternativas (elige una):** `qdrant`, `chroma`

## `mlflow`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Registra experimentos, versiona modelos y, para LLM, ofrece trazas, evaluación y gestión de prompts.
**Stack:** Python, React
**Repo:** https://github.com/mlflow/mlflow

**Instalación** [~]: `git clone https://github.com/mlflow/mlflow && cd mlflow && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tu equipo hace ML clásico y LLM y quiere una sola plataforma
**Evita si:** solo trazas LLM y quieres algo más ligero; mira `langfuse`
**Combina con:** `transformers`, `dspy`
**Alternativas (elige una):** `langfuse`

## `opik`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Traza llamadas, ejecuta evaluaciones automáticas y monitorea producción con paneles. Incluye optimizador de prompts.
**Stack:** Python, Java, TypeScript, ClickHouse
**Repo:** https://github.com/comet-ml/opik

**Instalación** [~]: `git clone https://github.com/comet-ml/opik && cd opik && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres observabilidad y evaluación en un solo producto abierto
**Evita si:** prefieres la opción más extendida; mira `langfuse`
**Combina con:** `langgraph`
**Alternativas (elige una):** `langfuse`, `phoenix`

## `pageindex`
role=library · exec=cloud · setup=easy · mcp=False · prov=['openai']

**Qué es:** Genera un árbol tipo índice del documento y deja que el LLM navegue por él como un experto. Funciona bien con informes largos y estructurados.
**Stack:** Python
**Repo:** https://github.com/VectifyAI/PageIndex

**Instalación** [~]: `pip install pageindex   (o: uv add pageindex)`
_Nombre PyPI puede diferir de 'PageIndex'; verifica en pypi.org._

**Elige si:** tus documentos son largos y con estructura clara
**Evita si:** tienes miles de documentos cortos; usa búsqueda vectorial
**Combina con:** `docling`
**Alternativas (elige una):** `lightrag`

## `pgvector`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Guarda embeddings en una columna y búscalos con SQL, con índices HNSW o IVFFlat. Evita añadir otra base de datos.
**Stack:** C, PostgreSQL
**Repo:** https://github.com/pgvector/pgvector

**Instalación** [?]: `git clone https://github.com/pgvector/pgvector (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** ya usas PostgreSQL y quieres vectores
**Evita si:** tienes volúmenes muy grandes; mira `milvus`
**Combina con:** `n8n`, `llama-index`
**Alternativas (elige una):** `qdrant`, `chroma`

## `phoenix`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Visualiza trazas de agentes y RAG, ejecuta evaluaciones y gestiona datasets y experimentos. Corre en local o en tu servidor.
**Stack:** Python, TypeScript, OpenTelemetry
**Repo:** https://github.com/Arize-ai/phoenix

**Instalación** [~]: `git clone https://github.com/Arize-ai/phoenix && cd phoenix && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres observabilidad basada en OpenTelemetry
**Evita si:** buscas la plataforma más usada; mira `langfuse`
**Combina con:** `llama-index`, `langgraph`
**Alternativas (elige una):** `langfuse`, `opik`

## `promptfoo`
role=app · exec=local · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Defines casos de prueba en YAML y comparas salidas de varios modelos con aserciones. También escanea vulnerabilidades como inyección de prompts.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/promptfoo/promptfoo

**Instalación** [~]: `git clone https://github.com/promptfoo/promptfoo && cd promptfoo && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres pruebas automáticas de prompts y seguridad
**Evita si:** necesitas observabilidad en producción; mira `langfuse`
**Combina con:** `langfuse`, `litellm`
**Alternativas (elige una):** `deepeval`, `ragas`, `dspy`

## `qdrant`
role=runtime · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Guarda embeddings con metadatos y los busca con filtros rápidos, a escala. Muy usada como memoria de RAG y agentes.
**Stack:** Rust, Docker
**Repo:** https://github.com/qdrant/qdrant

**Instalación** [~]: `git clone https://github.com/qdrant/qdrant && cd qdrant && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres una base vectorial dedicada y rápida
**Evita si:** ya tienes PostgreSQL y poco volumen; mira `pgvector`
**Combina con:** `llama-index`, `langchain`, `n8n`
**Alternativas (elige una):** `milvus`, `chroma`, `pgvector`, `faiss`

## `ragas`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai']

**Qué es:** Mide fidelidad, relevancia del contexto y calidad de respuestas, y genera conjuntos de prueba a partir de tus documentos.
**Stack:** Python
**Repo:** https://github.com/vibrantlabsai/ragas

**Instalación** [~]: `pip install ragas   (o: uv add ragas)`
_Nombre PyPI puede diferir de 'Ragas'; verifica en pypi.org._

**Elige si:** evalúas un sistema RAG
**Evita si:** necesitas red teaming de seguridad; mira `promptfoo`
**Combina con:** `llama-index`, `langfuse`
**Alternativas (elige una):** `deepeval`, `promptfoo`

## `ragflow`
role=platform · exec=local · setup=heavy · mcp=False · prov=['openai', 'local']

**Qué es:** Procesa PDFs, tablas e imágenes con parsing visual, crea bases de conocimiento con citas trazables y añade agentes y workflows.
**Stack:** Go, Python, React, Elasticsearch, Docker
**Repo:** https://github.com/infiniflow/ragflow

**Instalación** [~]: `git clone https://github.com/infiniflow/ragflow && cd ragflow && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** tus documentos son complejos y necesitas citas fiables
**Evita si:** quieres algo ligero en un portátil; mira `anything-llm`
**Combina con:** `ollama`, `docling`
**Alternativas (elige una):** `dify`, `lightrag`

## `sglang`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** Compite con vLLM en velocidad, con caché de prefijos RadixAttention y buen soporte de salidas estructuradas. Muy usado para modelos grandes como DeepSeek.
**Stack:** Python, CUDA
**Repo:** https://github.com/sgl-project/sglang

**Instalación** [~]: `git clone https://github.com/sgl-project/sglang && cd sglang && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** buscas el máximo rendimiento en servicio de LLM
**Evita si:** quieres la opción más documentada; mira `vllm`
**Combina con:** `litellm`
**Alternativas (elige una):** `vllm`

## `supermemory`
role=platform · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Guarda y recupera lo que importa de documentos, conversaciones y webs para dar contexto a tus modelos. Ofrece API, SDK y una app de usuario.
**Stack:** TypeScript, Cloudflare
**Repo:** https://github.com/supermemoryai/supermemory

**Instalación** [~]: `git clone https://github.com/supermemoryai/supermemory && cd supermemory && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres una API de memoria lista para tu app
**Evita si:** prefieres librería en Python; mira `mem0`
**Combina con:** `vercel-ai`
**Alternativas (elige una):** `mem0`, `agentmemory`

## `turbovec`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el coste de memoria y cómputo de la búsqueda vectorial cuando una vector DB completa es demasiado para tu escala.
**Stack:** Python / Rust
**Repo:** https://github.com/RyanCodrai/turbovec

**Instalación** [~]: `pip install turbovec   (o: uv add turbovec)`
_Nombre PyPI puede diferir de 'turbovec'; verifica en pypi.org._

**Elige si:** necesitas vector search veloz y embebido sin desplegar una DB
**Evita si:** ya usas una vector DB completa con persistencia y escalado horizontal
**Combina con:** `mem0`, `graphrag`

## `vllm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** Sirve modelos abiertos a muchos usuarios con una API compatible con OpenAI, gracias a PagedAttention y batching continuo.
**Stack:** Python, CUDA, PyTorch
**Repo:** https://github.com/vllm-project/vllm

**Instalación** [~]: `git clone https://github.com/vllm-project/vllm && cd vllm && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas servir LLM abiertos a muchos usuarios en GPU
**Evita si:** solo los usas tú en un portátil; mira `ollama`
**Combina con:** `litellm`, `open-webui`
**Alternativas (elige una):** `sglang`
