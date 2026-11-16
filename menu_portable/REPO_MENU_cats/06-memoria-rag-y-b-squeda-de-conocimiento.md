# 6. Memoria, RAG y búsqueda de conocimiento — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agentic-rag-for-dummies`
role=library · exec=hybrid · setup=medium · mcp=False · prov=local · tags=rag,template,jupyter-notebook

**Qué es:** Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama.
**Stack:** Python; checkout; Ollama local; PDFs propios; Jupyter para notebook
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La app es Ollama-first; Colab alojado no trae Ollama y requiere cambiar de modelo o conectar una instancia; las APIs alternativas consumen
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No confundas instalar langchain-openai con completar todo el proyecto; revisa requisitos y la guía de ejecución de la app o notebook
- Coste: El coste depende del proveedor o la ruta. La app es Ollama-first; Colab alojado no trae Ollama y requiere cambiar de modelo o conectar una instancia; las APIs alternativas consumen
- Equipo: Preparación según la ruta elegida. Python; checkout; Ollama local; PDFs propios; Jupyter para notebook
**Repo:** https://github.com/GiovanniPasq/agentic-rag-for-dummies

**Instalación** [+]:

```
pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender RAG por pasos; Comparar un pipeline local con otro proveedor
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Coloca un PDF breve en docs y pregunta por un dato de una página concreta
**Qué comprobar:** Puedes ver documentos recuperados y aclarar una consulta ambigua
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `ollama`, `qdrant`, `langfuse`, `ragas`

## `agentmemory`
role=library · exec=hybrid · setup=easy · mcp=True · prov=— · tags=agents,memory,typescript

**Qué es:** Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes.
**Stack:** Node.js >=20; servidor local; hooks revisados en el cliente
**Acceso y costes:**
- API de IA: API de IA opcional. Captura y búsqueda por palabras funcionan sin clave; embeddings locales son opcionales; compresión LLM puede hacer una llamada por observación
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. Las funciones y hooks dependen del runtime del cliente; la instalación de MCP no prueba que la captura automática esté activa
- Coste: El coste depende del proveedor o la ruta. Captura y búsqueda por palabras funcionan sin clave; embeddings locales son opcionales; compresión LLM puede hacer una llamada por observación
- Equipo: Preparación según la ruta elegida. Node.js >=20; servidor local; hooks revisados en el cliente
**Repo:** https://github.com/rohitg00/agentmemory

**Instalación** [+]:

```
npx -y @agentmemory/agentmemory@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir contexto entre Claude Code y Codex; Consultar decisiones por proyecto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Registra una decisión ficticia y búscala desde otro cliente conectado al mismo servidor
**Qué comprobar:** Puedes inspeccionar el recuerdo y confirmar que ambos clientes usan la misma instancia
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `gemini-cli`, `hermes-agent`
**Alternativas (elige una):** `engram`, `supermemory`, `claude-mem`

## `chroma`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=vector-db,rag,rust

**Qué es:** Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local.
**Stack:** Python; entorno virtual; dos documentos de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta embebida del ejemplo no pide API; funciones de embeddings elegidas y Chroma Cloud pueden tener costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Distingue cliente embebido, servidor y Cloud; para guardar resultados entre reinicios configura persistencia
- Coste: Sin pago a un modelo en la ruta básica. La ruta embebida del ejemplo no pide API; funciones de embeddings elegidas y Chroma Cloud pueden tener costes
- Equipo: Preparación según la ruta elegida. Python; entorno virtual; dos documentos de prueba
**Repo:** https://github.com/chroma-core/chroma

**Instalación** [+]:

```
pip install chromadb # python client
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar búsqueda semántica local; Filtrar fragmentos por metadatos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una colección con dos textos y consulta uno de sus temas
**Qué comprobar:** Se devuelve el documento relacionado y su identificador
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mempalace`, `anything-llm`, `langchain`
**Alternativas (elige una):** `qdrant`, `pgvector`, `milvus`, `faiss`

## `claude-mem`
role=skill · exec=local · setup=easy · mcp=True · prov=anthropic,mcp · tags=memory,coding-agent,mcp,typescript

**Qué es:** Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA.
**Stack:** Node 20.19+ o 22.12+; Bun y uv; agente admitido; proveedor del observador
**Acceso y costes:**
- API de IA: API de IA opcional. El observador puede usar el plan Anthropic o claves propias según el proyecto; la prueba del observador alojado pide método de pago; revisa la opción seleccionada
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. Antigravity documentado es la variante CLI; algunos agentes solo buscan memoria y no capturan sesiones; no todos tienen las mismas funciones
- Coste: El coste depende del proveedor o la ruta. El observador puede usar el plan Anthropic o claves propias según el proyecto; la prueba del observador alojado pide método de pago; revisa la opción seleccionada
- Equipo: Preparación según la ruta elegida. Node 20.19+ o 22.12+; Bun y uv; agente admitido; proveedor del observador
**Repo:** https://github.com/thedotmack/claude-mem

**Instalación** [+]:

```
npx claude-mem install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conservar decisiones entre sesiones; Recuperar el motivo de un cambio de código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda una decisión ficticia en una sesión y consulta si se recupera en una nueva
**Qué comprobar:** Puedes distinguir captura, resumen y recuperación y ver qué proveedor los produjo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`
**Alternativas (elige una):** `engram`, `agentmemory`

## `cognee`
role=library · exec=hybrid · setup=easy · mcp=True · prov=openai,local · tags=memory,rag,python

**Qué es:** Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños.
**Stack:** Python 3.10–3.14; modelos locales iniciales; plugins opcionales
**Acceso y costes:**
- API de IA: API de IA opcional. GLiNER y embeddings locales cubren la ruta básica; generación, visión, transcripción o Cloud pueden añadir costes
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Los plugins de los dos agentes están documentados; MCP usa stdio o HTTP; no asumas que sampling permite usar cualquier plan del cliente
- Coste: El coste depende del proveedor o la ruta. GLiNER y embeddings locales cubren la ruta básica; generación, visión, transcripción o Cloud pueden añadir costes
- Equipo: Preparación según la ruta elegida. Python 3.10–3.14; modelos locales iniciales; plugins opcionales
**Repo:** https://github.com/topoteretes/cognee

**Instalación** [+]:

```
uv pip install "cognee[gliner]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir memoria de documentos; Recuperar contexto desde Claude Code o Codex
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda un hecho ficticio con remember y recupéralo con recall sin configurar una clave LLM
**Qué comprobar:** Se devuelve el texto de origen y no una respuesta inventada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `openclaw`
**Alternativas (elige una):** `graphiti`, `mem0`, `graphrag`, `letta`

## `dsh-noema`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=memoria,plugin,typescript

**Qué es:** Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.
**Stack:** DeepSeek Harness compatible; plugin Noema; directorio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La memoria básica no necesita API propia; el agente anfitrión mantiene sus costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Importar archivos de memoria de Claude, Codex o Antigravity no es una integración para ejecutar este plugin dentro de esos clientes
- Coste: Consumo del agente que ya utilizas. La memoria básica no necesita API propia; el agente anfitrión mantiene sus costes
- Equipo: Preparación según la ruta elegida. DeepSeek Harness compatible; plugin Noema; directorio de prueba
**Repo:** https://github.com/ZSeven-W/dsh-noema

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ZSeven-W/dsh-noema/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Dar memoria a DeepSeek Harness; Importar una nota propia de otro agente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda un recuerdo ficticio desde DSH y comprueba que puedes verlo y eliminarlo desde ajustes
**Qué comprobar:** El recuerdo persiste y el panel muestra su contenido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `hermes-agent`

## `engram`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=memory,mcp,coding-agent,go

**Qué es:** Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI.
**Stack:** Binario oficial o Go; cliente MCP; directorio de memoria de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. SQLite y FTS5 no requieren LLM ni API; el agente que interpreta los recuerdos mantiene sus costes
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. MCP no equivale por sí solo a captura automática; Codex añade requisitos de capacidad y sesión que debes revisar en la guía
- Coste: Sin pago a un modelo en la ruta básica. SQLite y FTS5 no requieren LLM ni API; el agente que interpreta los recuerdos mantiene sus costes
- Equipo: Preparación según la ruta elegida. Binario oficial o Go; cliente MCP; directorio de memoria de prueba
**Repo:** https://github.com/Gentleman-Programming/engram

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Gentleman-Programming/engram/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Recordar decisiones técnicas; Hacer una entrega de contexto entre sesiones
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda una decisión con su razón y recupérala por palabras clave
**Qué comprobar:** El registro aparece con contenido y contexto que puedes inspeccionar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `opencode`, `gemini-cli`
**Alternativas (elige una):** `claude-mem`, `agentmemory`

## `faiss`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=vector-db,python,cpp

**Qué es:** Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU.
**Stack:** Paquete CPU o GPU compatible con tu sistema; vectores en memoria
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa un LLM ni cobra una API; la variante GPU necesita hardware y dependencias propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca de índices, no una base con panel, autenticación y persistencia automática de una aplicación
- Coste: Sin pago a un modelo en la ruta básica. No usa un LLM ni cobra una API; la variante GPU necesita hardware y dependencias propias
- Equipo: Preparación según la ruta elegida. Paquete CPU o GPU compatible con tu sistema; vectores en memoria
**Repo:** https://github.com/facebookresearch/faiss

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/facebookresearch/faiss/blob/main/INSTALL.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar embeddings de imágenes; Experimentar con índices y compresión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Construye un índice con cinco vectores y consulta el más cercano a uno conocido
**Qué comprobar:** El resultado coincide con el vecino calculado para la muestra
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langchain`, `llama-index`, `transformers`
**Alternativas (elige una):** `qdrant`, `chroma`

## `graphiti`
role=library · exec=hybrid · setup=medium · mcp=True · prov=openai,anthropic · tags=memory,rag,python

**Qué es:** Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes.
**Stack:** Python; Neo4j o FalkorDB; LLM y embeddings configurados
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El valor por defecto usa OpenAI; admite servidores locales compatibles; base de grafos y embeddings también consumen recursos
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Su MCP es una referencia experimental sin autenticación ni autorización: úsalo aislado para pruebas, no como despliegue público de producción
- Coste: El coste depende del proveedor o la ruta. El valor por defecto usa OpenAI; admite servidores locales compatibles; base de grafos y embeddings también consumen recursos
- Equipo: Preparación según la ruta elegida. Python; Neo4j o FalkorDB; LLM y embeddings configurados
**Repo:** https://github.com/getzep/graphiti

**Instalación** [+]:

```
pip install graphiti-core
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Representar cambios de una relación comercial; Conservar hechos de conversaciones con fechas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade dos hechos con fechas distintas y consulta cuál era válido en cada momento
**Qué comprobar:** El grafo conserva relaciones temporales y sus fuentes
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `langgraph`, `mcp-neo4j`
**Alternativas (elige una):** `cognee`, `graphrag`

## `graphrag`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=rag,python

**Qué es:** Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.
**Stack:** Python según guía; modelo y embeddings; corpus pequeño; presupuesto de indexación
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La indexación usa LLM y puede ser costosa antes de la primera consulta; calcula un lote pequeño
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Proyecto de investigación en mantenimiento: el autor no prevé nuevas funciones ni nuevas PRs, aunque mantiene correcciones y dependencias
- Coste: El coste depende del proveedor o la ruta. La indexación usa LLM y puede ser costosa antes de la primera consulta; calcula un lote pequeño
- Equipo: Preparación según la ruta elegida. Python según guía; modelo y embeddings; corpus pequeño; presupuesto de indexación
**Repo:** https://github.com/microsoft/graphrag

**Instalación** [?]:

```
Seguir la instalación original: https://microsoft.github.io/graphrag/get_started/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar relaciones de un corpus; Comparar búsqueda local y resumen global
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa unos textos ficticios y pregunta por un tema que conecte varios de ellos
**Qué comprobar:** Puedes revisar entidades, comunidades y fuentes de la respuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `mcp-neo4j`, `docling`
**Alternativas (elige una):** `graphiti`, `cognee`, `lightrag`

## `letta`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=memory,agents,typescript

**Qué es:** Harness de agentes con estado (Letta Code, antes MemGPT): memoria, identidad y skills que el propio agente reescribe con el tiempo.
**Stack:** Node.js y npm, o Python 3.9+ con uv/pipx; credenciales del proveedor de modelos o cuenta de Letta
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El runtime, Letta Cloud y los modelos tienen condiciones propias; el comando npm no aporta créditos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Con `letta backend local`, los proveedores Ollama o LM Studio mantienen el estado del agente y el modelo en tu equipo (docs.letta.com/letta-code/models).
- Coste: El coste depende del proveedor o la ruta. El runtime, Letta Cloud y los modelos tienen condiciones propias; el comando npm no aporta créditos
- Equipo: Preparación según la ruta elegida. Node.js y npm, o Python 3.9+ con uv/pipx; Linux glibc 2.28+, macOS 14+ o Windows x64
**Repo:** https://github.com/letta-ai/letta-code

**Instalación** [+]:

```
npm install -g @letta-ai/letta-code
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un agente con memoria persistente; Crear un asistente que conserve preferencias
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el enlace al código actual y crea un agente con una nota de memoria ficticia
**Qué comprobar:** Puedes recuperar esa nota en una conversación posterior
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `vllm`, `openclaw`, `hermes-agent`
**Alternativas (elige una):** `mem0`, `cognee`

## `lightrag`
role=library · exec=hybrid · setup=medium · mcp=False · prov=openai,local · tags=rag,python

**Qué es:** RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong.
**Stack:** Python y uv; LLM; embeddings; almacenamiento; configuración .env
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Indexar y responder pueden llamar varios modelos; admite configuración Ollama; el coste depende de roles, corpus y proveedor
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta
- Coste: El coste depende del proveedor o la ruta. Indexar y responder pueden llamar varios modelos; admite configuración Ollama; el coste depende de roles, corpus y proveedor
- Equipo: Preparación según la ruta elegida. Python y uv; LLM; embeddings; almacenamiento; configuración .env
**Repo:** https://github.com/HKUDS/LightRAG

**Instalación** [+]:

```
# Install LightRAG Server as a tool using uv (recommended)
uv tool install "lightrag-hku[api]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa un documento ficticio y compara una consulta sobre una entidad con otra sobre sus relaciones
**Qué comprobar:** Puedes inspeccionar los resultados y las relaciones recuperadas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pgvector`, `ollama`, `docling`, `langfuse`, `ragas`
**Alternativas (elige una):** `graphrag`, `ragflow`, `pageindex`

## `mem0`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=memory,python

**Qué es:** Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental.
**Stack:** Python; LLM; embeddings; almacén; identificador ficticio de usuario
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La plataforma y el SDK abierto tienen rutas distintas; Ollama sirve para LLM local, pero el ejemplo conserva OpenAI para embeddings si no los cambias
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. Las skills enseñan a integrar Mem0; no incluyen el servicio ni ejecutan gratis la memoria de tu aplicación
- Coste: El coste depende del proveedor o la ruta. La plataforma y el SDK abierto tienen rutas distintas; Ollama sirve para LLM local, pero el ejemplo conserva OpenAI para embeddings si no los cambias
- Equipo: Preparación según la ruta elegida. Python; LLM; embeddings; almacén; identificador ficticio de usuario
**Repo:** https://github.com/mem0ai/mem0

**Instalación** [+]:

```
pip install mem0ai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Recordar preferencias de atención; Mantener contexto de una app entre conversaciones
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda dos preferencias de un usuario ficticio y consulta una de ellas por su identificador
**Qué comprobar:** La búsqueda devuelve la preferencia del usuario correcto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `crewai`, `qdrant`, `hermes-desktop`
**Alternativas (elige una):** `letta`, `cognee`, `supermemory`

## `mempalace`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=memory,python

**Qué es:** Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.
**Stack:** Python o Docker; modelo de embeddings descargado; directorio de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta básica usa embeddings locales sin API; proveedores opcionales de embeddings pueden costar; no necesita LLM generativo para buscar
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El primer uso descarga el modelo; montar archivos en Docker es necesario para que pueda leerlos; los porcentajes de benchmark son del autor
- Coste: El coste depende del proveedor o la ruta. La ruta básica usa embeddings locales sin API; proveedores opcionales de embeddings pueden costar; no necesita LLM generativo para buscar
- Equipo: Preparación según la ruta elegida. Python o Docker; modelo de embeddings descargado; directorio de prueba
**Repo:** https://github.com/MemPalace/mempalace

**Instalación** [+]:

```
python -m venv .venv && source .venv/bin/activate
pip install mempalace
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Recuperar decisiones antiguas; Consultar archivos de contexto sin resúmenes destructivos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa dos notas propias y busca una decisión con palabras distintas a las originales
**Qué comprobar:** Puedes abrir el fragmento literal y comprobar su origen
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `chroma`, `codex`

## `milvus`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=vector-db,rag,go,docker

**Qué es:** Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores.
**Stack:** Python para cliente; servidor o modo local según guía; vectores de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige LLM; infraestructura y generación de vectores se presupuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar
- Coste: Sin pago a un modelo en la ruta básica. No exige LLM; infraestructura y generación de vectores se presupuestan aparte
- Equipo: Preparación según la ruta elegida. Python para cliente; servidor o modo local según guía; vectores de prueba
**Repo:** https://github.com/milvus-io/milvus

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/milvus-io/milvus/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar productos por similitud; Indexar embeddings a gran escala
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una colección, inserta tres vectores y busca uno cercano
**Qué comprobar:** Puedes contrastar el vecino y los metadatos devueltos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `anything-llm`, `lightrag`, `llama-index`
**Alternativas (elige una):** `qdrant`, `chroma`

## `onyx`
role=app · exec=hybrid · setup=medium · mcp=True · prov=local · tags=rag,agent,python

**Qué es:** Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso.
**Stack:** Docker o ruta elegida; proveedor; fuente documental de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Community y Enterprise tienen condiciones distintas; modelos locales o APIs, almacenamiento y conectores añaden costes según ruta
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Lite es un chat ligero y no indexa documentos; para la prueba documental necesitas el despliegue completo
- Coste: El coste depende del proveedor o la ruta. Community y Enterprise tienen condiciones distintas; modelos locales o APIs, almacenamiento y conectores añaden costes según ruta
- Equipo: Preparación según la ruta elegida. Docker o ruta elegida; proveedor; fuente documental de prueba
**Repo:** https://github.com/onyx-dot-app/onyx

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/onyx-dot-app/onyx/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar conocimiento de equipo; Dar contexto organizacional a un agente de código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta dos documentos de prueba y formula una consulta que exija una cita
**Qué comprobar:** La respuesta muestra fuentes accesibles para el usuario que consulta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `searxng`, `firecrawl`
**Alternativas (elige una):** `anything-llm`

## `openviking`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=local · tags=memoria,server,python

**Qué es:** Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.
**Stack:** uv; proveedor o Ollama; servidor; Node 18+ y macOS/Linux para instalador de plugins
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La edición abierta AGPL no exige activación; Enterprise y proveedores tienen condiciones propias; el autor documenta Ollama y Codex OAuth
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Compatibilidad por confirmar
- Modelos locales: Modelos locales documentados. El instalador de plugins tiene restricciones de sistema; en Windows el autor orienta hacia la app de escritorio; no extrapoles soporte de hooks
- Coste: El coste depende del proveedor o la ruta. La edición abierta AGPL no exige activación; Enterprise y proveedores tienen condiciones propias; el autor documenta Ollama y Codex OAuth
- Equipo: Preparación según la ruta elegida. uv; proveedor o Ollama; servidor; Node 18+ y macOS/Linux para instalador de plugins
**Repo:** https://github.com/volcengine/OpenViking

**Instalación** [+]:

```
uv tool install openviking --upgrade && openviking-server init
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conservar contexto de un proyecto; Consultar conocimientos y skills desde un almacén común
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda una nota de contexto ficticia y consulta cómo se recupera en otra sesión
**Qué comprobar:** Puedes inspeccionar el documento y la memoria que usa el agente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `openclaw`, `ollama`

## `pageindex`
role=library · exec=cloud · setup=easy · mcp=False · prov=openai · tags=rag,docs,python

**Qué es:** Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos.
**Stack:** Python; documento de prueba; proveedor para modo local o cuenta Cloud
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El autor documenta API propia, Cloud y una ruta Claude Code con plan del usuario; revisa límites y condiciones de autenticación de esa ruta
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Sin base vectorial no significa sin modelo ni coste; su adaptador Claude es integración del proyecto y no una aprobación universal de planes
- Coste: El coste depende del proveedor o la ruta. El autor documenta API propia, Cloud y una ruta Claude Code con plan del usuario; revisa límites y condiciones de autenticación de esa ruta
- Equipo: Preparación según la ruta elegida. Python; documento de prueba; proveedor para modo local o cuenta Cloud
**Repo:** https://github.com/VectifyAI/PageIndex

**Instalación** [+]:

```
pip install -U pageindex
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar informes largos por su estructura; Encontrar una sección de un contrato
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa un PDF con secciones y pregunta por un dato de una sección concreta
**Qué comprobar:** La recuperación señala la parte pertinente del documento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `openai-agents-python`, `claude-agent-sdk-python`
**Alternativas (elige una):** `lightrag`

## `pgvector`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vector-db,postgres,rag

**Qué es:** Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales.
**Stack:** PostgreSQL; permisos de extensión; paquete o compilación adecuados al sistema
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; PostgreSQL, hosting y generación de embeddings son recursos separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una extensión de PostgreSQL; las instrucciones Windows con nmake requieren el entorno de compilación correspondiente
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo; PostgreSQL, hosting y generación de embeddings son recursos separados
- Equipo: Preparación según la ruta elegida. PostgreSQL; permisos de extensión; paquete o compilación adecuados al sistema
**Repo:** https://github.com/pgvector/pgvector

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/pgvector/pgvector/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar similitud junto a datos SQL; Filtrar resultados vectoriales por columnas del negocio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Habilita la extensión en una base de prueba y compara tres vectores junto a sus filas
**Qué comprobar:** La consulta devuelve la fila más cercana usando la distancia elegida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `supabase`, `anything-llm`, `librechat`, `lightrag`
**Alternativas (elige una):** `qdrant`, `chroma`

## `qdrant`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=vector-db,rag,rust,docker

**Qué es:** Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida.
**Stack:** Docker; vectores y metadatos de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El servidor no requiere modelo; generar embeddings y Qdrant Cloud pueden costar aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La base vectorial almacena y busca; no genera por sí sola respuestas de un chatbot
- Coste: Sin pago a un modelo en la ruta básica. El servidor no requiere modelo; generar embeddings y Qdrant Cloud pueden costar aparte
- Equipo: Preparación según la ruta elegida. Docker; vectores y metadatos de prueba
**Repo:** https://github.com/qdrant/qdrant

**Instalación** [+]:

```
docker run -p 6333:6333 qdrant/qdrant
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Guardar embeddings de documentos; Combinar similitud y filtros de metadatos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inserta tres vectores pequeños con etiquetas y consulta el más parecido con un filtro
**Qué comprobar:** La búsqueda devuelve el registro esperado y respeta el filtro
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `docling`, `activepieces`, `llama-index`, `langchain`, `crawl4ai`
**Alternativas (elige una):** `milvus`, `chroma`, `pgvector`, `faiss`

## `ragflow`
role=platform · exec=local · setup=heavy · mcp=False · prov=openai,local · tags=rag,docs,agents,docker

**Qué es:** Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable.
**Stack:** Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. LLM, embeddings y reranker se configuran por separado; modelos locales necesitan recursos adicionales; APIs remotas tienen consumo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar
- Coste: El coste depende del proveedor o la ruta. LLM, embeddings y reranker se configuran por separado; modelos locales necesitan recursos adicionales; APIs remotas tienen consumo
- Equipo: Preparación según la ruta elegida. Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos
**Repo:** https://github.com/infiniflow/ragflow

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/infiniflow/ragflow/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa un PDF propio corto y pregunta por un dato identificable con cita
**Qué comprobar:** La respuesta permite abrir el fragmento y comprobar su procedencia
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `activepieces`, `langfuse`
**Alternativas (elige una):** `dify`, `lightrag`

## `supermemory`
role=platform · exec=hybrid · setup=easy · mcp=True · prov=— · tags=memory,rag,typescript

**Qué es:** Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local.
**Stack:** Node.js para ruta local; modelo elegido; cuenta para Cloud
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La instancia local admite embeddings locales y Ollama; API Cloud y proveedores remotos tienen planes y consumo separados
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Los plugins y MCP son vías de conexión; confirma que apuntan a la instancia local si buscas mantener el procesamiento en tu equipo
- Coste: El coste depende del proveedor o la ruta. La instancia local admite embeddings locales y Ollama; API Cloud y proveedores remotos tienen planes y consumo separados
- Equipo: Preparación según la ruta elegida. Node.js para ruta local; modelo elegido; cuenta para Cloud
**Repo:** https://github.com/supermemoryai/supermemory

**Instalación** [+]:

```
npx supermemory local
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conservar contexto entre agentes; Buscar documentos y recuerdos de un proyecto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda una nota de prueba y consulta su contenido desde una segunda sesión
**Qué comprobar:** Puedes verificar qué se almacenó y en qué instancia
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `opencode`, `ollama`
**Alternativas (elige una):** `mem0`, `agentmemory`

## `turbovec`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=automation,vector-db,rust

**Qué es:** Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida.
**Stack:** Python; wheel compatible o Rust y maturin para compilar; embeddings de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no exige API; obtener embeddings y disponer de RAM sigue siendo necesario
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Sus cifras de rendimiento son benchmarks del autor; no predicen el comportamiento de tu máquina o corpus
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no exige API; obtener embeddings y disponer de RAM sigue siendo necesario
- Equipo: Preparación según la ruta elegida. Python; wheel compatible o Rust y maturin para compilar; embeddings de prueba
**Repo:** https://github.com/RyanCodrai/turbovec

**Instalación** [+]:

```
pip install turbovec
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar índices vectoriales embebidos; Reducir memoria de una búsqueda local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa un conjunto pequeño y compara vecinos antes y después de cuantizar
**Qué comprobar:** Puedes medir memoria, tiempo y coincidencia en tus propios datos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langchain`, `llama-index`, `haystack`
