# 6. Memoria, RAG y búsqueda de conocimiento — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agentic-rag-for-dummies`
role=library · exec=hybrid · setup=medium · mcp=False · prov=local · tags=rag,template,jupyter-notebook

**Qué es:** Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama.
**Stack:** Jupyter Notebook, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/GiovanniPasq/agentic-rag-for-dummies

**Instalación** [?]: `Seguir la instalación original: https://github.com/GiovanniPasq/agentic-rag-for-dummies/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `agentmemory`
role=library · exec=hybrid · setup=easy · mcp=True · prov=— · tags=agents,memory,typescript

**Qué es:** Resuelve el "re-explica todo" al cambiar de asistente: la memoria vive fuera del cliente.
**Stack:** motor iii, MCP
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/rohitg00/agentmemory

**Instalación** [?]: `Seguir la instalación original: https://github.com/rohitg00/agentmemory/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** cambias de asistente y quieres una memoria común entre ellos
**Evita si:** te basta la memoria nativa de un único cliente o no usas MCP
**Combina con:** `mem0`, `ruflo`
**Alternativas (elige una):** `engram`, `supermemory`, `claude-mem`

## `chroma`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=vector-db,rag,rust

**Qué es:** Se usa embebida en tu script Python o como servidor, con embeddings automáticos. Perfecta para prototipos de RAG.
**Stack:** Rust, Python, TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/chroma-core/chroma

**Instalación** [+]: `pip install chromadb`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** empiezas con RAG y quieres lo más simple
**Evita si:** necesitas gran escala y filtros complejos; mira `qdrant` o `milvus`
**Combina con:** `llama-index`, `langchain`
**Alternativas (elige una):** `qdrant`, `pgvector`, `milvus`, `faiss`

## `claude-mem`
role=skill · exec=local · setup=easy · mcp=True · prov=anthropic,mcp · tags=memory,coding-agent,mcp,typescript

**Qué es:** Registra lo que hace el agente en cada sesión, lo resume y vuelve a inyectar lo relevante al empezar la siguiente. Evita repetir contexto en proyectos largos.
**Stack:** TypeScript, SQLite, Chroma
**Acceso y costes:**
- API de IA: API de IA opcional. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: El coste depende del proveedor o la ruta. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/thedotmack/claude-mem

**Instalación** [?]: `Seguir la instalación original: https://github.com/thedotmack/claude-mem/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Claude Code a diario y repites contexto entre sesiones
**Evita si:** necesitas memoria para una app propia; mira `mem0`
**Combina con:** `claude-code`, `superpowers`
**Alternativas (elige una):** `engram`, `agentmemory`

## `cognee`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,local · tags=memory,rag,python

**Qué es:** Convierte documentos y conversaciones en un grafo de conocimiento consultable para dar memoria de largo plazo a tus agentes.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/topoteretes/cognee

**Instalación** [+]: `pip install cognee`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres memoria basada en grafo con poco esfuerzo
**Evita si:** necesitas un grafo temporal en tiempo real; mira `graphiti`
**Combina con:** `qdrant`, `mcp-neo4j`
**Alternativas (elige una):** `graphiti`, `mem0`, `graphrag`, `letta`

## `dsh-noema`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=memoria,plugin,typescript

**Qué es:** Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
- Otras rutas: Plugin para DeepSeek Harness (DSH). La cuenta, API o modelo se configura en ese anfitrión; no se declara instalación nativa en Claude Code o Codex.
**Repo:** https://github.com/ZSeven-W/dsh-noema

**Instalación** [?]: `Seguir la instalación original: https://github.com/ZSeven-W/dsh-noema/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `engram`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=memory,mcp,coding-agent,go

**Qué es:** Da a cualquier agente compatible con MCP una memoria local de decisiones y aprendizajes, sin dependencias pesadas.
**Stack:** Go, SQLite
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo del agente que ya utilizas. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Gentleman-Programming/engram

**Instalación** [?]: `Seguir la instalación original: https://github.com/Gentleman-Programming/engram/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres memoria local simple para cualquier agente
**Evita si:** solo usas Claude Code y quieres algo automático; mira `claude-mem`
**Combina con:** `claude-code`, `opencode`
**Alternativas (elige una):** `claude-mem`, `agentmemory`

## `faiss`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=vector-db,python,cpp

**Qué es:** Base de muchas bases vectoriales; ideal para investigación o cuando quieres índices en memoria sin servidor.
**Stack:** C++, Python, CUDA
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/facebookresearch/faiss

**Instalación** [?]: `Seguir la instalación original: https://github.com/facebookresearch/faiss/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas índices vectoriales en memoria y máximo control
**Evita si:** quieres persistencia y API listas; mira `qdrant`
**Combina con:** `transformers`
**Alternativas (elige una):** `qdrant`, `chroma`

## `graphiti`
role=library · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic · tags=memory,rag,python

**Qué es:** Actualiza el grafo con cada nuevo dato sin recalcular todo y guarda cuándo era válido cada hecho. Ideal para memoria de agentes que cambia.
**Stack:** Python, Neo4j
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/getzep/graphiti

**Instalación** [+]: `pip install graphiti-core`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas memoria que cambie con el tiempo y se pueda consultar
**Evita si:** solo quieres RAG sobre documentos estáticos; mira `lightrag`
**Combina con:** `mcp-neo4j`
**Alternativas (elige una):** `cognee`, `graphrag`

## `graphrag`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=rag,python

**Qué es:** Resuelve las preguntas que requieren conectar entidades dispersas en muchos documentos, donde el RAG clásico falla.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/microsoft/graphrag

**Instalación** [?]: `Seguir la instalación original: https://github.com/microsoft/graphrag/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto
**Evita si:** un RAG simple basta o el coste de indexado con LLM es prohibitivo
**Combina con:** `graphify`, `mcp-neo4j`, `turbovec`
**Alternativas (elige una):** `graphiti`, `cognee`, `lightrag`

## `letta`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=memory,agents,python

**Qué es:** Crea agentes que gestionan su propia memoria en bloques editables y archivos, y persisten entre conversaciones. Incluye servidor, API y entorno de desarrollo.
**Stack:** Python, PostgreSQL
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/letta-ai/letta

**Instalación** [?]: `Seguir la instalación original: https://github.com/letta-ai/letta/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres agentes con memoria de largo plazo gestionada
**Evita si:** solo necesitas una capa de memoria para tu app; mira `mem0`
**Combina con:** `ollama`
**Alternativas (elige una):** `mem0`, `cognee`

## `lightrag`
role=library · exec=hybrid · setup=medium · mcp=False · prov=openai,local · tags=rag,python

**Qué es:** Construye un grafo de entidades a partir de tus documentos y consulta en modo local, global o híbrido. Más barato que GraphRAG.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/HKUDS/LightRAG

**Instalación** [?]: `Seguir la instalación original: https://github.com/HKUDS/LightRAG/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres RAG con grafo sin el coste de GraphRAG
**Evita si:** no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index`
**Combina con:** `ollama`, `qdrant`
**Alternativas (elige una):** `graphrag`, `ragflow`, `pageindex`

## `mem0`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=memory,python

**Qué es:** Resuelve el "amnesia" del LLM: el agente conserva preferencias y hechos entre sesiones sin reenviar todo el historial.
**Stack:** Python/TypeScript, vector DBs (Qdrant, Chroma, pgvector)
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/mem0ai/mem0

**Instalación** [+]: `pip install mem0ai`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres memoria estándar lista con integraciones amplias
**Evita si:** necesitas todo local sin llamadas a API (mempalace) o control total del almacenamiento
**Combina con:** `crewai`, `langchain`, `agentmemory`
**Alternativas (elige una):** `letta`, `cognee`, `supermemory`

## `mempalace`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=memory,python

**Qué es:** Resuelve la memoria privada: cero llamadas a API, tus textos no salen de tu máquina.
**Stack:** Python (PyPI)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo del agente que ya utilizas. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/MemPalace/mempalace

**Instalación** [?]: `Seguir la instalación original: https://github.com/MemPalace/mempalace/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** la privacidad es prioridad y no quieres llamadas a API
**Evita si:** quieres un SaaS gestionado con escalado automático o integraciones de framework ya hechas (mem0)
**Combina con:** `open-notebook`, `odysseus`

## `milvus`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=vector-db,rag,go,docker

**Qué es:** Pensada para producción con grandes volúmenes, alta disponibilidad y varios tipos de índices. Tiene una versión ligera para empezar.
**Stack:** Go, C++, Kubernetes
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/milvus-io/milvus

**Instalación** [?]: `Seguir la instalación original: https://github.com/milvus-io/milvus/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** esperas volúmenes muy grandes de vectores
**Evita si:** tu proyecto es pequeño; mira `chroma` o `qdrant`
**Combina con:** `llama-index`
**Alternativas (elige una):** `qdrant`, `chroma`

## `onyx`
role=app · exec=hybrid · setup=medium · mcp=True · prov=local · tags=rag,agent,python

**Qué es:** Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso.
**Stack:** Python, package.json, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/onyx-dot-app/onyx

**Instalación** [?]: `Seguir la instalación original: https://github.com/onyx-dot-app/onyx/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución
**Alternativas (elige una):** `anything-llm`

## `openviking`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=local · tags=memoria,server,python

**Qué es:** Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.
**Stack:** Python, Cargo.toml, Dockerfile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/volcengine/OpenViking

**Instalación** [?]: `Seguir la instalación original: https://github.com/volcengine/OpenViking/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución
**Combina con:** `claude-code`

## `pageindex`
role=library · exec=cloud · setup=easy · mcp=False · prov=openai · tags=rag,docs,python

**Qué es:** Genera un árbol tipo índice del documento y deja que el LLM navegue por él como un experto. Funciona bien con informes largos y estructurados.
**Stack:** Python
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. El proyecto documenta usar Claude Code con una suscripción o una API key. La modalidad cloud de PageIndex tiene requisitos propios.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/VectifyAI/PageIndex

**Instalación** [?]: `Seguir la instalación original: https://github.com/VectifyAI/PageIndex/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tus documentos son largos y con estructura clara
**Evita si:** tienes miles de documentos cortos; usa búsqueda vectorial
**Combina con:** `docling`
**Alternativas (elige una):** `lightrag`

## `pgvector`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vector-db,postgres,rag

**Qué es:** Guarda embeddings en una columna y búscalos con SQL, con índices HNSW o IVFFlat. Evita añadir otra base de datos.
**Stack:** C, PostgreSQL
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/pgvector/pgvector

**Instalación** [?]: `Seguir la instalación original: https://github.com/pgvector/pgvector/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** ya usas PostgreSQL y quieres vectores
**Evita si:** tienes volúmenes muy grandes; mira `milvus`
**Combina con:** `n8n`, `llama-index`
**Alternativas (elige una):** `qdrant`, `chroma`

## `qdrant`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=vector-db,rag,rust,docker

**Qué es:** Guarda embeddings con metadatos y los busca con filtros rápidos, a escala. Muy usada como memoria de RAG y agentes.
**Stack:** Rust, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/qdrant/qdrant

**Instalación** [?]: `Seguir la instalación original: https://github.com/qdrant/qdrant/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres una base vectorial dedicada y rápida
**Evita si:** ya tienes PostgreSQL y poco volumen; mira `pgvector`
**Combina con:** `llama-index`, `langchain`, `n8n`
**Alternativas (elige una):** `milvus`, `chroma`, `pgvector`, `faiss`

## `ragflow`
role=platform · exec=local · setup=heavy · mcp=False · prov=openai,local · tags=rag,docs,agents,docker

**Qué es:** Procesa PDFs, tablas e imágenes con parsing visual, crea bases de conocimiento con citas trazables y añade agentes y workflows.
**Stack:** Go, Python, React, Elasticsearch, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/infiniflow/ragflow

**Instalación** [?]: `Seguir la instalación original: https://github.com/infiniflow/ragflow/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tus documentos son complejos y necesitas citas fiables
**Evita si:** quieres algo ligero en un portátil; mira `anything-llm`
**Combina con:** `ollama`, `docling`
**Alternativas (elige una):** `dify`, `lightrag`

## `supermemory`
role=platform · exec=hybrid · setup=easy · mcp=False · prov=— · tags=memory,rag,typescript

**Qué es:** Guarda y recupera lo que importa de documentos, conversaciones y webs para dar contexto a tus modelos. Ofrece API, SDK y una app de usuario.
**Stack:** TypeScript, Cloudflare
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/supermemoryai/supermemory

**Instalación** [?]: `Seguir la instalación original: https://github.com/supermemoryai/supermemory/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres una API de memoria lista para tu app
**Evita si:** prefieres librería en Python; mira `mem0`
**Combina con:** `vercel-ai`
**Alternativas (elige una):** `mem0`, `agentmemory`

## `turbovec`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=automation,vector-db,rust

**Qué es:** Resuelve el coste de memoria y cómputo de la búsqueda vectorial cuando una vector DB completa es demasiado para tu escala.
**Stack:** Python / Rust
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/RyanCodrai/turbovec

**Instalación** [?]: `Seguir la instalación original: https://github.com/RyanCodrai/turbovec/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas vector search veloz y embebido sin desplegar una DB
**Evita si:** ya usas una vector DB completa con persistencia y escalado horizontal
**Combina con:** `mem0`, `graphrag`
