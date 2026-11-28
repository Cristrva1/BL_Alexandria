# Revisión editorial de los 138 grupos de Alexandría

**Revisión del 27 de noviembre de 2026.**

Aplicación aprobada. Los cuatro retiros constan en el [registro](../data/retired.json). Guíame usa las decisiones de la [revisión editorial](../curation/guiame.json) y mantiene seis fichas pendientes de revisión.

De los **409 repos** agrupados, propongo **4 retiros** y **6 casos por validar**. Quedarían **138 principales**, **199 alternativas con diferencias útiles** y **62 fichas que conservaría como referencia o en otra función**. En **31 grupos** la opción principal propuesta difiere del primer puesto del ranking.

La opción principal representa el punto de partida habitual de cada grupo. Priorizo la función, el entorno, el acceso y la facilidad de adopción. Uso la puntuación como contexto, junto con las limitaciones publicadas. Algunas familias del inventario de seguridad se describen en términos documentales y defensivos.

[Retiros propuestos](#retiros-propuestos) · [Casos por validar](#casos-por-validar) · [Decisiones por grupo](#decisiones-por-grupo)

## Retiros propuestos

| Grupo | Ficha a retirar | Ficha que queda | Motivo | Último commit de la rama principal en hora CDMX y fuentes |
|---:|---|---|---|---|
| 124 | [`opendots`](https://github.com/CopilotKit/OpenDots) | [`openbot`](../human/fichas/openbot.md) | Los autores dejaron de mantener OpenDots e integraron la interfaz como tema de OpenBot. La sustitución está anunciada en el repositorio original. | [2026-11-25](https://github.com/CopilotKit/OpenDots/commit/f59b1d32c91ed70eaf8435caace4732ed438acf1) · [Proyecto](https://github.com/CopilotKit/OpenDots) · [Sustituto](https://github.com/CopilotKit/OpenBot) |
| 85 | [`geo-seo-claude`](https://github.com/zubair-trabzada/geo-seo-claude) | [`claude-seo`](../human/fichas/claude-seo.md) | Claude SEO ya documenta GEO, evaluación de citabilidad y exportación de informes PDF. El solapamiento cubre los tres motivos principales para ofrecer esta ficha por separado. | [2026-10-05](https://github.com/zubair-trabzada/geo-seo-claude/commit/989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c) · [Proyecto](https://github.com/zubair-trabzada/geo-seo-claude) · [Sustituto](https://github.com/AgriciDaniel/claude-seo) |
| 24 | [`backdoor`](https://github.com/ajsai47/backdoor) | [`claude-code-router`](../human/fichas/claude-code-router.md) | El adaptador multiproveedor para Claude Code repite la función que cubre Claude Code Router, con alcance más amplio en la documentación de este último. Propuesta editorial de retirar la ficha independiente. | [2026-05-22](https://github.com/ajsai47/backdoor/commit/7f9765aed856cfebc345df0c5312b78857d7fe5e) · [Proyecto](https://github.com/ajsai47/backdoor) · [Sustituto](https://github.com/musistudio/claude-code-router) |
| 52 | [`no-ai-slop`](https://github.com/petergyang/no-ai-slop) | [`humanizer`](../human/fichas/humanizer.md) | La revisión de patrones repetitivos conservando la voz del autor se solapa directamente con Humanizer. Propuesta editorial de retirar una tercera ficha de la misma tarea. | [2026-09-01](https://github.com/petergyang/no-ai-slop/commit/000650b156983f5159695b441477f4e63b25dc85) · [Proyecto](https://github.com/petergyang/no-ai-slop) · [Sustituto](https://github.com/blader/humanizer) |

OpenDots tiene un reemplazo anunciado por sus autores. Los otros tres retiros propuestos son decisiones editoriales de Alexandría por redundancia funcional.

### Referencias que habría que migrar si se aprueban los retiros

| Ficha | Alternativas que la mencionan | Combinaciones entrantes | Temas prácticos | Recetas |
|---|---:|---:|---:|---|
| `opendots` | 1 | 1 | 1 | — |
| `geo-seo-claude` | 1 | 1 | 4 | — |
| `backdoor` | 3 | 0 | 3 | — |
| `no-ai-slop` | 2 | 0 | 5 | — |

También hay que cotejar las menciones directas en guías y en el recomendador. En particular, `geo-seo-claude` aparece en las instrucciones para agentes y en la lógica de recomendaciones para Claude Code. Tras la aprobación, el procedimiento editorial cubre migración de referencias, registro y regeneración.

[Procedimiento de retiros](../human/mantenimiento.md#retirar-repos-obsoletos)

## Casos por validar

Estas fichas siguen justificadas mientras se comprueba el caso que puede distinguirlas. La última columna identifica la opción con la que haría la comparación.

| Grupo | Ficha | Qué decidiría su permanencia | Comparar con |
|---:|---|---|---|
| 6 | [`appsmith`](../human/fichas/appsmith.md) | Se solapa con ToolJet como constructor de paneles internos. Comparar los widgets y conectores que realmente usa el equipo y qué incluye cada edición antes de retirar la ficha. [Fuente primaria](https://github.com/appsmithorg/appsmith) | [`tooljet`](../human/fichas/tooljet.md) · [Documentación](https://github.com/ToolJet/ToolJet) |
| 10 | [`awesome-claude-skills`](../human/fichas/awesome-claude-skills.md) | El directorio general y multiplataforma se solapa con las otras colecciones. Verificar cuántos enlaces o recursos propios de Composio se perderían antes de retirar. [Fuente primaria](https://github.com/ComposioHQ/awesome-claude-skills) | [`antigravity-awesome-skills`](../human/fichas/antigravity-awesome-skills.md) · [Documentación](https://github.com/sickn33/agentic-awesome-skills) |
| 12 | [`superclaude-framework`](../human/fichas/superclaude-framework.md) | Comandos y modos del framework se solapan con ECC y parte de Superpowers. Validar si alguien aprovecha sus personas o un flujo propio en Claude Code. [Fuente primaria](https://github.com/SuperClaude-Org/SuperClaude_Framework) | [`superpowers`](../human/fichas/superpowers.md) · [Documentación](https://github.com/obra/superpowers) |
| 14 | [`gitnexus`](../human/fichas/gitnexus.md) | El mapa general de código ya está cubierto. Valorar su análisis de flujos y la licencia no comercial de la edición revisada frente a un caso real antes de retirarlo. [Fuente primaria](https://github.com/abhigyanpatwari/GitNexus) | [`codegraph`](../human/fichas/codegraph.md) · [Documentación](https://github.com/colbymchenry/codegraph) |
| 22 | [`sim`](../human/fichas/sim.md) | La construcción visual y el despliegue de agentes solapan Dify y Langflow. Conservar si sus permisos por espacio de trabajo, cliente de escritorio o integraciones aportan una ruta propia. [Fuente primaria](https://github.com/simstudioai/sim) | [`dify`](../human/fichas/dify.md) · [Documentación](https://github.com/langgenius/dify) |
| 113 | [`magicui`](../human/fichas/magicui.md) | Sus componentes de efecto y secciones animadas se solapan con React Bits. Comparar su catálogo concreto, registro y condiciones de sus plantillas antes de decidir. [Fuente primaria](https://github.com/magicuidesign/magicui) | [`react-bits`](../human/fichas/react-bits.md) · [Documentación](https://github.com/DavidHDev/react-bits) |

## Decisiones por grupo

Los números corresponden al orden de los grupos en el índice del corte. «Conservar con otra función» mantiene la ficha por un uso diferente, como dependencia, especialidad o referencia documental.

[Grupos de similares](../data/grupos.json) · [Rúbrica de calidad](../human/calidad.md)

### Automatizar procesos y crear herramientas internas

#### 006 Herramientas internas y bases de datos no-code

- **Principal** · [`tooljet`](../human/fichas/tooljet.md). Punto de partida para aplicaciones internas visuales sobre fuentes de datos.
- **Validar antes de decidir** · [`appsmith`](../human/fichas/appsmith.md). Se solapa con ToolJet como constructor de paneles internos. Comparar los widgets y conectores que realmente usa el equipo y qué incluye cada edición antes de retirar la ficha.
- **Alternativa que conservaría** · [`budibase`](../human/fichas/budibase.md). Formularios, portales y automatizaciones internas.
- **Conservar con otra función** · [`nocodb`](../human/fichas/nocodb.md). Hoja tipo Airtable sobre una base SQL. Mover al subgrupo de tablas de negocio.
- **Conservar con otra función** · [`teable`](../human/fichas/teable.md). Base visual centrada en PostgreSQL. Evaluar junto a NocoDB y Baserow.
- **Conservar con otra función** · [`baserow`](../human/fichas/baserow.md). Base visual autoalojada con su propio modelo de tablas. Mover al mismo subgrupo.
- **Conservar con otra función** · [`grist-core`](../human/fichas/grist-core.md). Hoja relacional con fórmulas Python. Conservar en tablas de negocio.

#### 008 Orquestadores de workflows de datos y tareas

- **Principal** · [`airflow`](../human/fichas/airflow.md). Flujos por lotes y amplio ecosistema de operadores.
- **Alternativa que conservaría** · [`kestra`](../human/fichas/kestra.md). Declaración YAML, interfaz y eventos.
- **Alternativa que conservaría** · [`prefect`](../human/fichas/prefect.md). Flujos declarados como funciones Python.
- **Alternativa que conservaría** · [`dagster`](../human/fichas/dagster.md). Activos de datos con linaje y pruebas.
- **Conservar con otra función** · [`trigger-dev`](../human/fichas/trigger-dev.md). Tareas en segundo plano para aplicaciones TypeScript. Mover a trabajos de aplicación.
- **Conservar con otra función** · [`windmill`](../human/fichas/windmill.md). Conversión de scripts en trabajos y aplicaciones internas. Enlazar como automatización de scripts.

#### 103 Automatización por eventos auto-hospedada

- **Principal** · [`node-red`](../human/fichas/node-red.md). Automatizaciones visuales por eventos con conectores e integración IoT.
- **Alternativa que conservaría** · [`huginn`](../human/fichas/huginn.md). Flujos autoalojados de vigilancia de fuentes y reacción a eventos online.

### Skills, plugins y métodos para agentes

#### 010 Catálogos de skills y plugins para agentes

- **Principal** · [`antigravity-awesome-skills`](../human/fichas/antigravity-awesome-skills.md). Puerta de entrada a un inventario amplio y portable de skills.
- **Alternativa que conservaría** · [`claude-plugins-official`](../human/fichas/claude-plugins-official.md). Fuente oficial de plugins de Anthropic.
- **Conservar con otra función** · [`wshobson-agents`](../human/fichas/wshobson-agents.md). Plugins y subagentes empaquetados. Ubicarlo como colección instalable.
- **Alternativa que conservaría** · [`awesome-claude-code`](../human/fichas/awesome-claude-code.md). Útil para el directorio específico de hooks, comandos y flujos de Claude Code.
- **Alternativa que conservaría** · [`awesome-agent-skills`](../human/fichas/awesome-agent-skills.md). Directorio de enlaces a skills de sus autores y equipos oficiales. Conservar por esa forma de curación, junto a la colección de playbooks instalables.
- **Validar antes de decidir** · [`awesome-claude-skills`](../human/fichas/awesome-claude-skills.md). El directorio general y multiplataforma se solapa con las otras colecciones. Verificar cuántos enlaces o recursos propios de Composio se perderían antes de retirar.

#### 012 Metodologías y harness para agentes de código

- **Principal** · [`superpowers`](../human/fichas/superpowers.md). Método para planificar, implementar con pruebas y revisar cambios.
- **Alternativa que conservaría** · [`ecc`](../human/fichas/ecc.md). Configura un entorno completo de skills, hooks y herramientas.
- **Alternativa que conservaría** · [`gstack`](../human/fichas/gstack.md). Conservar para el proceso específico de producto, ingeniería y lanzamiento que documenta.
- **Conservar con otra función** · [`agent-skills`](../human/fichas/agent-skills.md). Material portable para elegir skills individuales. Separar del método de trabajo completo.
- **Validar antes de decidir** · [`superclaude-framework`](../human/fichas/superclaude-framework.md). Comandos y modos del framework se solapan con ECC y parte de Superpowers. Validar si alguien aprovecha sus personas o un flujo propio en Claude Code.

#### 078 Desarrollo guiado por especificaciones

- **Principal** · [`spec-kit`](../human/fichas/spec-kit.md). Especificaciones, planes y tareas versionadas en el repositorio.
- **Alternativa que conservaría** · [`bmad-method`](../human/fichas/bmad-method.md). Conservar para equipos que necesitan el flujo detallado de roles de producto e ingeniería.

### Construir agentes y coordinar equipos de IA

#### 005 Frameworks de agentes en Python

- **Principal** · [`langgraph`](../human/fichas/langgraph.md). Base de flujos con estado, control explícito y checkpoints.
- **Alternativa que conservaría** · [`crewai`](../human/fichas/crewai.md). Equipos definidos por roles y tareas con un arranque más guiado.
- **Alternativa que conservaría** · [`openai-agents-python`](../human/fichas/openai-agents-python.md). SDK oficial para quien construye sobre OpenAI.
- **Alternativa que conservaría** · [`adk-python`](../human/fichas/adk-python.md). SDK para quien trabaja en el ecosistema Google y Vertex.
- **Alternativa que conservaría** · [`pydantic-ai`](../human/fichas/pydantic-ai.md). Contratos tipados y validación con Pydantic.
- **Alternativa que conservaría** · [`agno`](../human/fichas/agno.md). Plataforma de agentes con runtime y API de servicio.
- **Alternativa que conservaría** · [`smolagents`](../human/fichas/smolagents.md). Experimentos pequeños centrados en agentes que generan código.
- **Conservar con otra función** · [`deepagents`](../human/fichas/deepagents.md). Se apoya en LangGraph. Referenciar como ampliación para planificación, archivos y subagentes.

#### 022 Builders visuales de agentes

- **Principal** · [`dify`](../human/fichas/dify.md). Construcción visual y despliegue de aplicaciones de IA con documentos.
- **Alternativa que conservaría** · [`langflow`](../human/fichas/langflow.md). Flujos visuales extensibles como componentes de LangChain.
- **Alternativa que conservaría** · [`autogpt`](../human/fichas/autogpt.md). Plataforma de agentes y bloques reutilizables en su propio ecosistema.
- **Validar antes de decidir** · [`sim`](../human/fichas/sim.md). La construcción visual y el despliegue de agentes solapan Dify y Langflow. Conservar si sus permisos por espacio de trabajo, cliente de escritorio o integraciones aportan una ruta propia.

#### 050 Frameworks de RAG y orquestación de LLM

- **Principal** · [`langchain`](../human/fichas/langchain.md). Composición general de aplicaciones LLM con muchas integraciones.
- **Alternativa que conservaría** · [`haystack`](../human/fichas/haystack.md). Pipelines explícitos de recuperación y procesamiento documental.
- **Alternativa que conservaría** · [`llama-index`](../human/fichas/llama-index.md). Ingesta e indexación sobre colecciones de documentos propias.

#### 056 Frameworks de agentes en TypeScript

- **Principal** · [`vercel-ai`](../human/fichas/vercel-ai.md). Aplicaciones web TypeScript con chat, streaming y llamadas a modelos.
- **Alternativa que conservaría** · [`mastra`](../human/fichas/mastra.md). Flujos de agentes, RAG y evaluación explícitos en una aplicación TypeScript.
- **Alternativa que conservaría** · [`langgraphjs`](../human/fichas/langgraphjs.md). Agentes en grafos con estado y continuidad con la arquitectura LangGraph.

### Buscar, extraer y monitorear información web

#### 040 Crawlers que entregan contenido listo para LLM

- **Principal** · [`crawl4ai`](../human/fichas/crawl4ai.md). Crawling e ingestión desde una biblioteca que puedes manejar en tu entorno.
- **Alternativa que conservaría** · [`firecrawl`](../human/fichas/firecrawl.md). Operación gestionada por API y funciones integradas de búsqueda y rastreo.
- **Alternativa que conservaría** · [`jina-reader`](../human/fichas/jina-reader.md). Conversión directa de una URL individual con un servicio ligero.

#### 057 Scraping guiado por LLM

- **Principal** · [`scrapegraph-ai`](../human/fichas/scrapegraph-ai.md). Extracción semántica programable sobre páginas que el usuario puede consultar.
- **Alternativa que conservaría** · [`maxun`](../human/fichas/maxun.md). Extracción guiada sin código para convertir páginas en datos.
- **Alternativa que conservaría** · [`llm-scraper`](../human/fichas/llm-scraper.md). Extracción con contrato Zod para código TypeScript.

#### 087 Crawlee (Node.js y Python)

- **Principal** · [`crawlee`](../human/fichas/crawlee.md). Entrada de la familia en Node.js y TypeScript.
- **Alternativa que conservaría** · [`crawlee-python`](../human/fichas/crawlee-python.md). La misma familia en un ecosistema Python. Mantener ambas variantes en una sola explicación comparativa.

#### 095 Lectores RSS auto-hospedados

- **Principal** · [`freshrss`](../human/fichas/freshrss.md). Agregador multiusuario con extensiones y clientes móviles.
- **Alternativa que conservaría** · [`miniflux`](../human/fichas/miniflux.md). Servicio minimalista cuando el equipo prefiere PostgreSQL y un lector con menos superficie.

### Conectar herramientas con MCP

#### 083 Servidores MCP de navegador

- **Principal** · [`playwright-mcp`](../human/fichas/playwright-mcp.md). Ficha principal para interacción con páginas y validación de una interfaz propia.
- **Alternativa que conservaría** · [`chrome-devtools-mcp`](../human/fichas/chrome-devtools-mcp.md). Diagnóstico de consola, red y rendimiento en Chrome.

#### 093 SDKs de MCP en Python

- **Principal** · [`mcp-python-sdk`](../human/fichas/mcp-python-sdk.md). Base oficial para implementar el protocolo MCP en Python.
- **Alternativa que conservaría** · [`fastmcp`](../human/fichas/fastmcp.md). Framework de conveniencia con servicios y flujos de desarrollo adicionales.

#### 116 Servidores MCP de Neo4j

- **Principal** · [`neo4j-mcp`](../human/fichas/neo4j-mcp.md). Servidor oficial para consultas y lectura de esquema del grafo.
- **Conservar con otra función** · [`mcp-neo4j`](../human/fichas/mcp-neo4j.md). Labs solapa la consulta Cypher. Mantener en memoria, modelado y administración de Aura como referencia específica.

#### 117 SDKs de MCP en TypeScript

- **Principal** · [`mcp-typescript-sdk`](../human/fichas/mcp-typescript-sdk.md). Base oficial para implementar el protocolo MCP en TypeScript.
- **Alternativa que conservaría** · [`mcp-use`](../human/fichas/mcp-use.md). Stack complementario para construir y desplegar aplicaciones MCP con herramientas integradas.

### Memoria, RAG y búsqueda de conocimiento

#### 001 Memoria persistente para agentes de código

- **Principal** · [`claude-mem`](../human/fichas/claude-mem.md). Memoria de sesiones para un equipo que trabaja principalmente con Claude Code.
- **Alternativa que conservaría** · [`engram`](../human/fichas/engram.md). Servidor de memoria local en un binario Go con SQLite.
- **Alternativa que conservaría** · [`agentmemory`](../human/fichas/agentmemory.md). Memoria compartida cuando el mismo proyecto pasa por varios agentes.

#### 002 Capas de memoria para apps y agentes de IA

- **Principal** · [`mem0`](../human/fichas/mem0.md). Base práctica para añadir memoria de usuario persistente a una aplicación.
- **Alternativa que conservaría** · [`cognee`](../human/fichas/cognee.md). Transforma documentos en un grafo consultable.
- **Alternativa que conservaría** · [`graphiti`](../human/fichas/graphiti.md). Conserva la dimensión temporal de los hechos del grafo.
- **Alternativa que conservaría** · [`supermemory`](../human/fichas/supermemory.md). Memoria gestionada combinada con búsqueda híbrida de documentos y conectores sincronizados. Ese flujo sí justifica una alternativa frente a la memoria general de Mem0.
- **Conservar con otra función** · [`letta`](../human/fichas/letta.md). Runtime de agentes con estado. Ubicarlo como plataforma de agentes.

#### 007 Bases y librerías vectoriales

- **Principal** · [`qdrant`](../human/fichas/qdrant.md). Servidor vectorial de entrada para proyectos locales con filtros.
- **Alternativa que conservaría** · [`milvus`](../human/fichas/milvus.md). Escala distribuida y colecciones muy grandes.
- **Alternativa que conservaría** · [`chroma`](../human/fichas/chroma.md). Arranque embebido para prototipos de RAG.
- **Alternativa que conservaría** · [`lancedb`](../human/fichas/lancedb.md). Datos vectoriales en archivos locales y flujos sobre Arrow/Lance.
- **Alternativa que conservaría** · [`weaviate`](../human/fichas/weaviate.md). Búsqueda híbrida y vectorización integrada.
- **Alternativa que conservaría** · [`pgvector`](../human/fichas/pgvector.md). Reutiliza PostgreSQL cuando los datos ya viven ahí.
- **Conservar con otra función** · [`faiss`](../human/fichas/faiss.md). Librería de índices dentro del proceso. Mantener fuera de la comparación de bases con servicio.

#### 029 RAG con grafos e índices de conocimiento

- **Principal** · [`ragflow`](../human/fichas/ragflow.md). Aplicación integral que ingiere documentos y ofrece una experiencia de consulta.
- **Alternativa que conservaría** · [`lightrag`](../human/fichas/lightrag.md). Índice de conocimiento como componente de un sistema propio.
- **Alternativa que conservaría** · [`pageindex`](../human/fichas/pageindex.md). Navegación por la estructura jerárquica del documento.
- **Alternativa que conservaría** · [`graphrag`](../human/fichas/graphrag.md). Preguntas globales y resúmenes a partir de comunidades en un corpus.

### Entender código y comprobar su calidad

#### 014 Mapas e índices de código para agentes

- **Principal** · [`codegraph`](../human/fichas/codegraph.md). Entrada para navegar relaciones y símbolos del código desde el agente.
- **Alternativa que conservaría** · [`graphify`](../human/fichas/graphify.md). Grafo que abarca documentación y otros materiales además del código.
- **Alternativa que conservaría** · [`codebase-memory-mcp`](../human/fichas/codebase-memory-mcp.md). Índice persistente accesible por MCP con foco en consultas compactas.
- **Validar antes de decidir** · [`gitnexus`](../human/fichas/gitnexus.md). El mapa general de código ya está cubierto. Valorar su análisis de flujos y la licencia no comercial de la edición revisada frente a un caso real antes de retirarlo.
- **Conservar con otra función** · [`repomix`](../human/fichas/repomix.md). Exporta código como contexto. Mover junto a empaquetadores y enlazar como complemento.

#### 096 Detección de secretos en repos

- **Principal** · [`gitleaks`](../human/fichas/gitleaks.md). Detección de credenciales expuestas en Git y en la integración continua propia.
- **Alternativa que conservaría** · [`trufflehog`](../human/fichas/trufflehog.md). Inventario defensivo de filtraciones que abarcan servicios y almacenes además de Git.

### Chats, modelos locales y espacios privados

#### 004 Interfaces de chat con LLM

- **Principal** · [`open-webui`](../human/fichas/open-webui.md). Base autoalojada para chat multiusuario, modelos locales y documentos.
- **Alternativa que conservaría** · [`cherry-studio`](../human/fichas/cherry-studio.md). Aplicación de escritorio para manejar varios proveedores.
- **Alternativa que conservaría** · [`lobehub`](../human/fichas/lobehub.md). Flujo orientado a asistentes y extensiones de la propia aplicación.
- **Alternativa que conservaría** · [`librechat`](../human/fichas/librechat.md). Conservar para equipos que necesitan su gestión de usuarios y acceso.
- **Alternativa que conservaría** · [`jan`](../human/fichas/jan.md). Cliente de escritorio centrado en ejecutar modelos localmente.
- **Alternativa que conservaría** · [`chatbox`](../human/fichas/chatbox.md). Cliente sencillo que incluye una ruta móvil.
- **Alternativa que conservaría** · [`nextchat`](../human/fichas/nextchat.md). Conservar para un frontend ligero y despliegue estático o serverless documentado.
- **Conservar con otra función** · [`textgen`](../human/fichas/textgen.md). Banco de pruebas de backends y formatos de inferencia. Mover junto a herramientas de experimentación local.

#### 021 Motores para correr LLM en local

- **Principal** · [`ollama`](../human/fichas/ollama.md). Arranque sencillo para descargar y servir modelos locales.
- **Alternativa que conservaría** · [`llama-cpp`](../human/fichas/llama-cpp.md). Control fino de inferencia, cuantización y backends.
- **Alternativa que conservaría** · [`localai`](../human/fichas/localai.md). Servicio compatible con API de OpenAI y alcance multimodal.
- **Alternativa que conservaría** · [`llamafile`](../human/fichas/llamafile.md). Distribución autocontenida para ejecutar un modelo con poca instalación.
- **Conservar con otra función** · [`koboldcpp`](../human/fichas/koboldcpp.md). Interfaz y motor orientados a escritura creativa y rol. Reubicar en ese flujo.

#### 035 Workspaces privados con documentos y chat

- **Principal** · [`anything-llm`](../human/fichas/anything-llm.md). Aplicación lista para consultar documentos y usar modelos elegidos.
- **Alternativa que conservaría** · [`khoj`](../human/fichas/khoj.md). Segundo cerebro personal con notas, búsqueda y automatizaciones.
- **Conservar con otra función** · [`private-gpt`](../human/fichas/private-gpt.md). Capa de API y servicios privados para integrar en una aplicación propia.

#### 123 Alternativas a NotebookLM

- **Principal** · [`open-notebook`](../human/fichas/open-notebook.md). Cuaderno de fuentes para resumir, conversar y generar audio.
- **Alternativa que conservaría** · [`surfsense`](../human/fichas/surfsense.md). Investigación sobre fuentes conectadas y transformación de documentos en un espacio de trabajo.

### Diseñar y construir interfaces web

#### 009 Bibliotecas de componentes React

- **Principal** · [`ui`](../human/fichas/ui.md). Base modificable dentro del propio código para un frontend React con Tailwind.
- **Alternativa que conservaría** · [`ant-design`](../human/fichas/ant-design.md). Paneles empresariales con tablas y formularios densos.
- **Alternativa que conservaría** · [`mui`](../human/fichas/mui.md). Equipos que ya usan Material Design o su ecosistema.
- **Alternativa que conservaría** · [`chakra-ui`](../human/fichas/chakra-ui.md). Interfaces que aprovechan su API de estilos y componentes accesibles.
- **Alternativa que conservaría** · [`mantine`](../human/fichas/mantine.md). Aplicaciones con necesidad de hooks, formularios y utilidades integradas.
- **Alternativa que conservaría** · [`heroui`](../human/fichas/heroui.md). Componentes React instalables como biblioteca con un sistema visual propio y ruta Tailwind. Mantener cuando se prefiera ese paquete a copiar componentes al código.

#### 072 Componentes de chat y copilotos para React

- **Principal** · [`assistant-ui`](../human/fichas/assistant-ui.md). Componentes React cuando el resultado visible es un chat coherente.
- **Alternativa que conservaría** · [`copilotkit`](../human/fichas/copilotkit.md). Interfaces generadas dentro del flujo y agentes basados en AG-UI.

#### 091 Pizarras y diagramas a mano alzada

- **Principal** · [`excalidraw`](../human/fichas/excalidraw.md). Pizarra lista para hacer diagramas a mano alzada.
- **Conservar con otra función** · [`tldraw`](../human/fichas/tldraw.md). SDK para construir una pizarra o editor de lienzo infinito. Mantener en desarrollo de interfaces.

#### 113 Componentes animados para React

- **Principal** · [`react-bits`](../human/fichas/react-bits.md). Fuente general de componentes de animación para React.
- **Validar antes de decidir** · [`magicui`](../human/fichas/magicui.md). Sus componentes de efecto y secciones animadas se solapan con React Bits. Comparar su catálogo concreto, registro y condiciones de sus plantillas antes de decidir.

#### 122 Editores visuales de diseño con IA

- **Principal** · [`open-design`](../human/fichas/open-design.md). Diseño y prototipado visual colaborativo desde un encargo.
- **Alternativa que conservaría** · [`onlook`](../human/fichas/onlook.md). Edición visual sobre el código de una aplicación React y Tailwind existente.

#### 130 De diseño o captura a código

- **Principal** · [`screenshot-to-code`](../human/fichas/screenshot-to-code.md). Primer candidato cuando ya existe una captura o diseño que convertir en código.
- **Conservar con otra función** · [`stitch-sdk`](../human/fichas/stitch-sdk.md). Generación de pantallas desde una descripción con el servicio de Google. Mantener como ruta para crear un diseño original.

#### 133 Obtención de datos en React

- **Principal** · [`tanstack-query`](../human/fichas/tanstack-query.md). Gestión general de caché, sincronización y cambios de datos de servidor.
- **Alternativa que conservaría** · [`swr`](../human/fichas/swr.md). Lecturas autoactualizables y proyectos existentes que requieren una integración React más acotada.

### Dashboards, analítica y mapas

#### 026 Librerías de gráficos

- **Principal** · [`echarts`](../human/fichas/echarts.md). Visualización general cuando hacen falta tipos de gráfico y mapas variados.
- **Alternativa que conservaría** · [`recharts`](../human/fichas/recharts.md). Gráficos declarativos integrados en React.
- **Alternativa que conservaría** · [`chart-js`](../human/fichas/chart-js.md). Gráficos clásicos en canvas con poca configuración.
- **Alternativa que conservaría** · [`d3`](../human/fichas/d3.md). Composición visual a medida y control detallado de escalas y elementos.

#### 059 Analítica web auto-hospedada

- **Principal** · [`umami`](../human/fichas/umami.md). Analítica de sitios centrada en privacidad y preparación acotada.
- **Alternativa que conservaría** · [`matomo`](../human/fichas/matomo.md). Analítica más profunda y control de datos para organizaciones.
- **Alternativa que conservaría** · [`plausible`](../human/fichas/plausible.md). Alternativa de analítica ligera si se requiere la oferta gestionada con alojamiento europeo descrita por el proyecto.

#### 061 BI y dashboards

- **Principal** · [`metabase`](../human/fichas/metabase.md). Primera opción para que un equipo de negocio explore métricas con una interfaz guiada.
- **Alternativa que conservaría** · [`superset`](../human/fichas/superset.md). Exploración, visualizaciones y administración de BI más extensa.
- **Alternativa que conservaría** · [`redash`](../human/fichas/redash.md). Consultas SQL compartidas cuando el equipo construye sus vistas directamente sobre consultas.

#### 097 Paneles OSINT sobre globo 3D

- **Principal** · [`gods-eye-view`](../human/fichas/gods-eye-view.md). Referencia para visualizar información geoespacial pública en un globo.
- **Alternativa que conservaría** · [`osiris`](../human/fichas/osiris.md). Panel de eventos y noticias con información geográfica como parte de un tablero.

#### 111 Mapas web interactivos

- **Principal** · [`leaflet`](../human/fichas/leaflet.md). Mapa interactivo con marcadores, capas y GeoJSON de preparación ligera.
- **Alternativa que conservaría** · [`maplibre`](../human/fichas/maplibre.md). Renderizado de mapas vectoriales y estilos con aceleración gráfica.

#### 114 Búsqueda de usuarios en redes sociales

- **Principal** · `sherlock`. Ficha representativa del grupo para documentación de auditoría de presencia propia en Internet.
- **Conservar con otra función** · `maigret`. Referencia de inventario de la familia y evaluación de riesgos de privacidad. Evitar duplicar la recomendación genérica.

#### 121 Fotogrametría con drones

- **Principal** · [`webodm`](../human/fichas/webodm.md). Flujo visual para convertir fotografías aéreas en mapas y modelos.
- **Conservar con otra función** · [`odm`](../human/fichas/odm.md). Motor de procesamiento del ecosistema. Mantener como dependencia y ruta de procesamiento por código.

### Generar y editar imágenes con IA

#### 106 Interfaces de creación de imágenes

- **Principal** · [`invokeai`](../human/fichas/invokeai.md). Aplicación integrada de generación y edición con lienzo y gestión de modelos.
- **Alternativa que conservaría** · [`krita-ai-diffusion`](../human/fichas/krita-ai-diffusion.md). Conservar para quien ya edita ilustraciones dentro de Krita.

### Editar, grabar y generar video

#### 053 Modelos abiertos de video generativo

- **Principal** · [`wan2-2`](../human/fichas/wan2-2.md). Primera familia a evaluar para texto, imagen o audio como entrada al video generativo.
- **Alternativa que conservaría** · [`hunyuanvideo-1-5`](../human/fichas/hunyuanvideo-1-5.md). Variante Tencent más ligera para flujos que necesitan ese ecosistema.
- **Alternativa que conservaría** · [`hunyuanvideo`](../human/fichas/hunyuanvideo.md). Continuidad si los checkpoints, complementos o resultados existentes exigen la familia original.

#### 055 Editores de video

- **Principal** · [`shotcut`](../human/fichas/shotcut.md). Edición convencional local desde una interfaz gráfica.
- **Alternativa que conservaría** · [`kdenlive`](../human/fichas/kdenlive.md). Proyectos de edición multipista y trabajo con proxys.
- **Conservar con otra función** · [`opencut`](../human/fichas/opencut.md). Referencia de edición en navegador mientras la ficha describe una reescritura del proyecto principal.

#### 118 Generación automática de videos cortos

- **Principal** · [`moneyprinterturbo`](../human/fichas/moneyprinterturbo.md). Producción en un flujo de guion, material, voz y subtítulos para video corto.
- **Alternativa que conservaría** · [`short-video-factory`](../human/fichas/short-video-factory.md). Adaptación a videos de producto con una interfaz de escritorio.

### PDF, OCR y procesamiento de documentos

#### 011 Conversión de documentos a Markdown/JSON para IA

- **Principal** · [`docling`](../human/fichas/docling.md). Conversión local de documentos estructurados con tablas como punto de partida.
- **Alternativa que conservaría** · [`mineru`](../human/fichas/mineru.md). PDF científicos o multilingües con maquetación y fórmulas.
- **Alternativa que conservaría** · [`xberg`](../human/fichas/xberg.md). Extractor empaquetado en Rust con OCR y funciones de procesamiento adicionales.
- **Alternativa que conservaría** · [`marker`](../human/fichas/marker.md). Flujo especializado de PDF a Markdown con fórmulas y código.
- **Alternativa que conservaría** · [`unstructured`](../human/fichas/unstructured.md). Partición en elementos dentro de pipelines de ingestión.
- **Conservar con otra función** · [`tika`](../human/fichas/tika.md). Extracción de metadatos y texto de muchos formatos desde Java. Mantener como extractor general.

#### 032 OCR de documentos

- **Principal** · [`paddleocr`](../human/fichas/paddleocr.md). OCR general con idiomas y análisis de maquetación.
- **Alternativa que conservaría** · [`tesseract`](../human/fichas/tesseract.md). OCR tradicional en CPU con una instalación convencional.
- **Alternativa que conservaría** · [`olmocr`](../human/fichas/olmocr.md). Conversión de escaneos con un modelo de visión cuando se dispone de GPU.
- **Conservar con otra función** · [`unlimited-ocr`](../human/fichas/unlimited-ocr.md). Su arquitectura para secuencias documentales largas justifica una ficha de investigación especializada. Mover fuera de la primera elección de OCR general.

#### 128 Suites de herramientas PDF

- **Principal** · [`stirling-pdf`](../human/fichas/stirling-pdf.md). Suite PDF autoalojada para cubrir tareas variadas de documentos.
- **Alternativa que conservaría** · [`pdfcraft`](../human/fichas/pdfcraft.md). Edición habitual desde navegador para quienes prefieren prescindir de la instalación.

### Investigar finanzas y mercados

#### 076 Backtesting en Python

- **Principal** · [`backtesting-py`](../human/fichas/backtesting-py.md). Primer backtest legible sobre una serie OHLC.
- **Alternativa que conservaría** · [`vectorbt`](../human/fichas/vectorbt.md). Comparación masiva de configuraciones y señales mediante cálculos vectorizados.

### Organizar notas, archivos y servicios personales

#### 031 Notas y bases de conocimiento personales

- **Principal** · [`siyuan`](../human/fichas/siyuan.md). Base de notas con bloques referenciables y organización local.
- **Alternativa que conservaría** · [`trilium`](../human/fichas/trilium.md). Notas jerárquicas profundas y scripting.
- **Alternativa que conservaría** · [`logseq`](../human/fichas/logseq.md). Esquemas diarios y relaciones tipo grafo.
- **Alternativa que conservaría** · [`joplin`](../human/fichas/joplin.md). Markdown y sincronización con opción de cifrado.

#### 065 Finanzas personales

- **Principal** · [`actual`](../human/fichas/actual.md). Presupuesto doméstico local mediante sobres.
- **Alternativa que conservaría** · [`firefly-iii`](../human/fichas/firefly-iii.md). Reglas, contabilidad de doble entrada e informes.

#### 066 Bloqueo de anuncios por DNS

- **Principal** · [`pi-hole`](../human/fichas/pi-hole.md). Filtrado de anuncios y rastreadores por DNS para toda una red.
- **Alternativa que conservaría** · [`adguardhome`](../human/fichas/adguardhome.md). Conservar cuando se prioriza DNS cifrado o su control parental integrado.

#### 069 Espacios de trabajo local-first tipo Notion

- **Principal** · [`appflowy`](../human/fichas/appflowy.md). Wiki o espacio de trabajo con colaboración y alojamiento propio.
- **Alternativa que conservaría** · [`anytype-ts`](../human/fichas/anytype-ts.md). Conocimiento personal centrado en objetos y relaciones del cliente local.

#### 074 Proveedores de identidad y SSO

- **Principal** · [`keycloak`](../human/fichas/keycloak.md). Identidad y SSO para integraciones que requieren estándares y federación.
- **Alternativa que conservaría** · [`authentik`](../human/fichas/authentik.md). Flujos de acceso administrados visualmente y otra experiencia de operación.

#### 082 Bibliotecas de libros y cómics

- **Principal** · [`kavita`](../human/fichas/kavita.md). Biblioteca mixta con un lector orientado también a manga y cómics.
- **Alternativa que conservaría** · [`calibre-web`](../human/fichas/calibre-web.md). Publicación de una biblioteca cuyo catálogo ya está administrado en Calibre.

#### 084 Obsidian como segundo cerebro para agentes

- **Principal** · [`obsidian-second-brain`](../human/fichas/obsidian-second-brain.md). Sistema de contexto en Markdown compartido entre varios agentes.
- **Alternativa que conservaría** · [`claude-obsidian`](../human/fichas/claude-obsidian.md). Instrucciones específicas para Claude Code y actividades de organización de una bóveda.

#### 104 Gestión de fotos auto-hospedada

- **Principal** · [`immich`](../human/fichas/immich.md). Biblioteca con copia automática de fotos y videos desde móviles.
- **Alternativa que conservaría** · [`photoprism`](../human/fichas/photoprism.md). Organización de un archivo fotográfico existente con flujo web y etiquetado.

#### 109 Gestores de contraseñas

- **Principal** · [`keepassxc`](../human/fichas/keepassxc.md). Bóveda local para un usuario que administra su archivo de contraseñas.
- **Alternativa que conservaría** · [`vaultwarden`](../human/fichas/vaultwarden.md). Servidor para sincronización propia con clientes compatibles de Bitwarden.

### Analizar software y comprobar su seguridad

#### 027 Fuzzing de rutas y contenido web

- **Principal** · `dirsearch`. Ficha principal para documentar el grupo de revisión autorizada de superficie web.
- **Conservar con otra función** · `ffuf`. Referencia técnica para el inventario de herramientas de auditoría autorizada.
- **Conservar con otra función** · `feroxbuster`. Referencia de implementación en Rust para el inventario técnico.
- **Conservar con otra función** · `gobuster`. Referencia histórica y de continuidad para equipos que ya la documentan.

#### 046 Frameworks de C2 y post-explotación

- **Principal** · `sliver`. Ficha representativa para el inventario defensivo de familias C2.
- **Conservar con otra función** · `empire`. Referencia para documentación y reconocimiento defensivo de una familia distinta.
- **Conservar con otra función** · `mythic`. Referencia para documentación y reconocimiento defensivo de una familia distinta.

#### 048 Ingeniería inversa y desensambladores

- **Principal** · [`ghidra`](../human/fichas/ghidra.md). Análisis estático visual de binarios para mantenimiento y auditoría de software.
- **Alternativa que conservaría** · [`radare2`](../human/fichas/radare2.md). Análisis en terminal y continuidad de scripts existentes.
- **Alternativa que conservaría** · [`rizin`](../human/fichas/rizin.md). Ecosistema de Rizin y Cutter para equipos que ya usan esas integraciones.

#### 073 Emulación de adversarios

- **Principal** · `atomic-red-team`. Ficha principal para documentación de validación de detecciones y controles.
- **Conservar con otra función** · `caldera`. Conservar como referencia de laboratorio e inventario de emulación, fuera de flujos operativos recomendados.

#### 075 Análisis forense de discos

- **Principal** · [`autopsy`](../human/fichas/autopsy.md). Trabajo forense con interfaz, casos y módulos de ingestión.
- **Conservar con otra función** · [`sleuthkit`](../human/fichas/sleuthkit.md). Base de análisis de discos que usa Autopsy. Conservar como herramienta de consola y dependencia.

#### 080 Proxies de pruebas de aplicaciones web

- **Principal** · `zaproxy`. Ficha principal del grupo para revisión defensiva autorizada de aplicaciones web.
- **Conservar con otra función** · `caido`. Referencia de proxy comercial, útil al documentar herramientas existentes y sus planes.

#### 088 Bloqueo de IP por comportamiento

- **Principal** · [`crowdsec`](../human/fichas/crowdsec.md). Defensa de servicios con detección y reputación colaborativa.
- **Alternativa que conservaría** · [`fail2ban`](../human/fichas/fail2ban.md). Protección de un host a partir de reglas sobre sus propios logs.

#### 098 Escáneres de vulnerabilidades de contenedores

- **Principal** · [`trivy`](../human/fichas/trivy.md). Revisión defensiva de imágenes e infraestructura con un escáner integrado.
- **Alternativa que conservaría** · [`grype`](../human/fichas/grype.md). Escaneo centrado en paquetes y vulnerabilidades, especialmente con SBOM.

#### 099 Cracking de contraseñas

- **Principal** · `hashcat`. Ficha representativa para documentar auditorías de credenciales propias y su mitigación.
- **Conservar con otra función** · `john`. Referencia histórica y de compatibilidad en el inventario de evaluación defensiva de credenciales.

#### 102 Sondeo y escaneo de reconocimiento

- **Principal** · `httpx`. Ficha principal para inventario autorizado de servicios web propios.
- **Conservar con otra función** · `naabu`. Cubre inventario de puertos, distinto del inventario HTTP. Mantener como referencia defensiva en su propia ficha.

#### 108 Pruebas de carga

- **Principal** · [`locust`](../human/fichas/locust.md). Medición de rendimiento de servicios propios en suites escritas en Python.
- **Alternativa que conservaría** · [`k6`](../human/fichas/k6.md). Pruebas de rendimiento dentro del ecosistema JavaScript y Grafana.

#### 127 Listas de payloads y diccionarios

- **Principal** · `seclists`. Ficha principal para documentar la familia de referencias de auditoría en el inventario editorial.
- **Conservar con otra función** · `payloadsallthethings`. Referencia documental de la comunidad. Mantener fuera de las rutas de recomendación operativa.

#### 132 Pentesting autónomo con agentes

- **Principal** · `strix`. Ficha principal exclusivamente como representante del grupo en el inventario editorial de riesgos.
- **Conservar con otra función** · `shannon`. Referencia para documentar el alcance y los riesgos de esta familia. Excluir ambas fichas de rutas operativas de recomendación autónoma.

#### 134 WAF compatibles con SecLang y el OWASP CRS

- **Principal** · [`modsecurity`](../human/fichas/modsecurity.md). Motor WAF de referencia para servidores que requieren sus conectores o continuidad con configuraciones existentes.
- **Alternativa que conservaría** · [`coraza`](../human/fichas/coraza.md). Motor compatible con SecLang para aplicaciones e infraestructura Go.

#### 135 Modelado de amenazas

- **Principal** · [`threat-dragon`](../human/fichas/threat-dragon.md). Modelado visual de amenazas desde un diagrama de arquitectura.
- **Alternativa que conservaría** · [`pytm`](../human/fichas/pytm.md). Modelo de amenazas como código Python versionable y reproducible en integración continua.

#### 136 Aplicaciones web vulnerables para practicar

- **Principal** · `juice-shop`. Ficha de referencia de una aplicación educativa para seguridad de software.
- **Conservar con otra función** · `webgoat`. Material de formación guiada del ecosistema Java. Mantener como referencia curricular.

#### 137 Generadores de SBOM

- **Principal** · [`syft`](../human/fichas/syft.md). Generación de inventarios de componentes de imágenes y sistemas de archivos.
- **Alternativa que conservaría** · [`cdxgen`](../human/fichas/cdxgen.md). Inventario CycloneDX a partir de código de distintos lenguajes y evidencias de dependencias.

#### 138 Análisis de dependencias vulnerables (SCA)

- **Principal** · [`osv-scanner`](../human/fichas/osv-scanner.md). Revisión defensiva de dependencias desde lockfiles y la base OSV.
- **Alternativa que conservaría** · [`dependency-check`](../human/fichas/dependency-check.md). Continuidad de proyectos Java o .NET con integración en herramientas de construcción.
- **Alternativa que conservaría** · [`dep-scan`](../human/fichas/dep-scan.md). Auditoría con SBOM, alcance y documentos de intercambio de vulnerabilidades.

### WhatsApp, mensajería y chatbots

#### 013 APIs y librerías no oficiales de WhatsApp

- **Principal** · [`evolution-api`](../human/fichas/evolution-api.md). Entrada de alto nivel para conectar WhatsApp con automatizaciones y CRM.
- **Alternativa que conservaría** · [`waha`](../human/fichas/waha.md). API HTTP empaquetada con elección de motor.
- **Conservar con otra función** · [`whatsapp-web-js`](../human/fichas/whatsapp-web-js.md). Librería Node.js que opera WhatsApp Web mediante navegador.
- **Conservar con otra función** · [`baileys`](../human/fichas/baileys.md). Librería Node.js de bajo nivel por WebSocket.
- **Conservar con otra función** · [`whatsmeow`](../human/fichas/whatsmeow.md). Librería Go para una aplicación que integra el protocolo directamente.

#### 060 Chat de equipo auto-hospedado

- **Principal** · [`mattermost`](../human/fichas/mattermost.md). Comunicación para equipos que buscan un espacio de colaboración autoalojado.
- **Alternativa que conservaría** · [`rocket-chat`](../human/fichas/rocket-chat.md). Además del chat de equipo, atiende flujos omnicanal de soporte.
- **Alternativa que conservaría** · [`zulip`](../human/fichas/zulip.md). Organización de conversaciones por tema e hilos.

### CRM, ventas y marketing

#### 017 CRM y ERP auto-hospedados

- **Principal** · [`twenty-main`](../human/fichas/twenty-main.md). CRM autoalojado para un proyecto nuevo de ventas.
- **Alternativa que conservaría** · [`espocrm`](../human/fichas/espocrm.md). CRM ligero para equipos que quieren extender un stack PHP.
- **Alternativa que conservaría** · [`suitecrm`](../human/fichas/suitecrm.md). Continuidad de instalaciones y procesos procedentes de SugarCRM.
- **Conservar con otra función** · [`erpnext`](../human/fichas/erpnext.md). ERP con manufactura y contabilidad. Reubicar como ERP.
- **Conservar con otra función** · [`odoo`](../human/fichas/odoo.md). ERP modular con ecosistema de módulos. Comparar con ERPNext.

#### 081 Reservas y citas

- **Principal** · [`easyappointments`](../human/fichas/easyappointments.md). Agenda sencilla para una operación que asigna citas a proveedores de servicio.
- **Alternativa que conservaría** · [`cal.diy`](../human/fichas/cal-diy.md). Edición comunitaria del ecosistema Cal, útil si se necesitan sus flujos e integraciones y se acepta su alcance.

#### 094 Help desk y tickets

- **Principal** · [`freescout`](../human/fichas/freescout.md). Bandeja compartida y mesa de ayuda de preparación ligera.
- **Alternativa que conservaría** · [`zammad`](../human/fichas/zammad.md). Mesa de ayuda omnicanal con chat, teléfono o redes sociales.

### Aprender IA y escribir mejores prompts

#### 037 Cookbooks y ejemplos de apps con LLM

- **Principal** · [`awesome-llm-apps`](../human/fichas/awesome-llm-apps.md). Inventario de ejemplos que permite explorar capacidades de distintos proveedores.
- **Alternativa que conservaría** · [`openai-cookbook`](../human/fichas/openai-cookbook.md). Documentación práctica oficial para la API de OpenAI.
- **Alternativa que conservaría** · [`claude-cookbooks`](../human/fichas/claude-cookbooks.md). Documentación práctica oficial para la API de Claude.

#### 068 Cursos de Microsoft para principiantes

- **Principal** · [`generative-ai-for-beginners`](../human/fichas/generative-ai-for-beginners.md). Fundamentos y primer proyecto de IA generativa.
- **Alternativa que conservaría** · [`ai-agents-for-beginners`](../human/fichas/ai-agents-for-beginners.md). Curso especializado en construir agentes una vez cubiertos los fundamentos.

#### 092 Colecciones de prompts

- **Principal** · [`prompts-chat`](../human/fichas/prompts-chat.md). Punto de entrada para buscar ejemplos de prompts por tarea.
- **Conservar con otra función** · [`fabric`](../human/fichas/fabric.md). CLI ejecutable para aplicar patrones a textos. Mantener en la ruta de herramientas de terminal.

#### 112 Aprender LLM desde cero

- **Principal** · [`llms-from-scratch`](../human/fichas/llms-from-scratch.md). Implementación paso a paso de un modelo de lenguaje desde sus fundamentos.
- **Alternativa que conservaría** · [`llm-course`](../human/fichas/llm-course.md). Ruta por etapas que lleva de fundamentos a aplicaciones y despliegue.

### Programar con agentes de código

#### 003 Agentes de programación en terminal

- **Principal** · [`opencode`](../human/fichas/opencode.md). Entrada general para quien quiere elegir proveedor desde la terminal.
- **Alternativa que conservaría** · [`codex`](../human/fichas/codex.md). Ruta oficial para OpenAI o la sesión de ChatGPT cuando corresponda.
- **Alternativa que conservaría** · [`claude-code`](../human/fichas/claude-code.md). Ruta de Anthropic con su sistema de skills, hooks y subagentes.
- **Alternativa que conservaría** · [`gemini-cli`](../human/fichas/gemini-cli.md). Opción para instalaciones empresariales de Google Code Assist que lo utilicen.
- **Alternativa que conservaría** · [`antigravity-cli`](../human/fichas/antigravity-cli.md). Terminal para el flujo de Antigravity de Google.
- **Alternativa que conservaría** · [`qwen-code`](../human/fichas/qwen-code.md). Conservar como cliente del ecosistema Qwen cuando esa sea la elección del usuario.
- **Alternativa que conservaría** · [`aider`](../human/fichas/aider.md). Flujo centrado en Git, revisión y commits pequeños.
- **Alternativa que conservaría** · [`goose`](../human/fichas/goose.md). Cliente disponible también como app de escritorio con extensiones MCP.
- **Alternativa que conservaría** · [`mimo-code`](../human/fichas/mimo-code.md). Cliente del ecosistema Xiaomi MiMo, con un flujo diseñado alrededor de esos modelos. Mantener como entrada especializada por proveedor.

#### 062 Agentes que resuelven issues de software

- **Principal** · [`openhands`](../human/fichas/openhands.md). Espacio de trabajo autoalojado para revisar sesiones de ingeniería con varios agentes.
- **Alternativa que conservaría** · [`open-swe`](../human/fichas/open-swe.md). Flujo gestionado que convierte trabajo de ingeniería en propuestas revisables.
- **Conservar con otra función** · [`mini-swe-agent`](../human/fichas/mini-swe-agent.md). Implementación mínima de investigación y benchmarks. Conservar como referencia de ingeniería.

#### 086 Agentes de código en el editor

- **Principal** · [`cline`](../human/fichas/cline.md). Agente general en el editor con elección de proveedor y ruta de CLI.
- **Alternativa que conservaría** · [`kilocode`](../human/fichas/kilocode.md). Conservar para equipos que utilicen su catálogo de modos, agentes e integraciones.

#### 125 Gestores de sesiones de agentes de código

- **Principal** · [`t3code`](../human/fichas/t3code.md). Gestión de sesiones de distintos agentes desde una misma interfaz.
- **Conservar con otra función** · [`opencode-manager`](../human/fichas/opencode-manager.md). T3 Code gestiona sesiones de varios agentes. Mantener OpenCode Manager como opción especializada en el control remoto de OpenCode con Git, terminal y tareas programadas.

### Asistentes e investigación con agentes

#### 049 Agentes de investigación autónoma

- **Principal** · [`gpt-researcher`](../human/fichas/gpt-researcher.md). Investigación general con salida estructurada y fuentes.
- **Alternativa que conservaría** · [`storm`](../human/fichas/storm.md). Informes largos y estructurados al estilo enciclopédico.
- **Alternativa que conservaría** · [`local-deep-research`](../human/fichas/local-deep-research.md). Investigación que combina buscadores con documentos y modelos del propio entorno.

#### 051 Asistentes personales autónomos

- **Principal** · [`openclaw`](../human/fichas/openclaw.md). Asistente personal persistente disponible por varios canales.
- **Alternativa que conservaría** · [`hermes-agent`](../human/fichas/hermes-agent.md). Flujo centrado en memoria, skills y selección de proveedor o endpoint.
- **Alternativa que conservaría** · [`mercury-agent`](../human/fichas/mercury-agent.md). Conservar para perfiles que necesitan presupuestos y control estricto de permisos.

#### 119 Paneles para coordinar equipos de agentes

- **Principal** · [`paperclip`](../human/fichas/paperclip.md). Organización de equipos de agentes con objetivos, presupuestos y trazabilidad.
- **Alternativa que conservaría** · [`multica`](../human/fichas/multica.md). Asignación y revisión de trabajo de agentes de código con sus CLI y cuentas.

#### 124 Espacios de asistentes de CopilotKit

- **Principal** · [`openbot`](../human/fichas/openbot.md). Espacio autoalojable para asistentes cuando se requiere control de permisos y auditoría.
- **Retiro propuesto** · [`opendots`](https://github.com/CopilotKit/OpenDots). Los autores dejaron de mantener OpenDots e integraron la interfaz como tema de OpenBot. La sustitución está anunciada en el repositorio original.

### Infraestructura, despliegue y herramientas para agentes

#### 039 Paneles de auto-hospedaje y PaaS propios

- **Principal** · [`coolify`](../human/fichas/coolify.md). PaaS general para publicar servicios en infraestructura propia.
- **Alternativa que conservaría** · [`dokploy`](../human/fichas/dokploy.md). Alternativa cuando su flujo Docker y Traefik encaja mejor con la operación.
- **Conservar con otra función** · [`casaos`](../human/fichas/casaos.md). Ubicarlo en administración de servidores domésticos y archivos.

#### 044 Sandboxes para agentes

- **Principal** · [`e2b`](../human/fichas/e2b.md). Entorno ejecutable aislado en la nube para código generado por una aplicación.
- **Alternativa que conservaría** · [`sandbox`](../human/fichas/sandbox.md). Espacio de trabajo aislado que agrupa terminal, navegador y editores.
- **Conservar con otra función** · [`nemoclaw`](../human/fichas/nemoclaw.md). Stack de referencia específico de NVIDIA para proteger despliegues de agentes. Ubicar en despliegue seguro.

#### 070 Backends como servicio auto-hospedados

- **Principal** · [`supabase`](../human/fichas/supabase.md). Backend de entrada cuando se requiere PostgreSQL, Auth y almacenamiento.
- **Alternativa que conservaría** · [`appwrite`](../human/fichas/appwrite.md). Conservar para proyectos que prefieren su plataforma de funciones, mensajería y hosting.

#### 079 Proxies inversos con HTTPS automático

- **Principal** · [`caddy`](../human/fichas/caddy.md). Publicación con HTTPS automático para pocos servicios y configuración directa.
- **Alternativa que conservaría** · [`traefik`](../human/fichas/traefik.md). Descubrimiento dinámico de servicios en entornos Docker o Kubernetes.

#### 101 Redes privadas tipo mesh (WireGuard)

- **Principal** · [`netbird`](../human/fichas/netbird.md). Red privada autoalojable cuando también se requiere identidad y control de acceso.
- **Alternativa que conservaría** · [`headscale`](../human/fichas/headscale.md). Servidor de control compatible con los clientes Tailscale para equipos que ya usan ese ecosistema.

### Operar, evaluar y medir modelos de IA

#### 019 Observabilidad y trazas de LLM

- **Principal** · [`langfuse`](../human/fichas/langfuse.md). Trazas, gestión de prompts y evaluación de aplicaciones LLM en una misma plataforma.
- **Alternativa que conservaría** · [`opik`](../human/fichas/opik.md). Evaluaciones integradas en pruebas y flujos de equipo.
- **Alternativa que conservaría** · [`phoenix`](../human/fichas/phoenix.md). OpenTelemetry y análisis desde notebooks.
- **Alternativa que conservaría** · [`mlflow`](../human/fichas/mlflow.md). Equipos que ya gestionan experimentos y modelos mediante MLflow.
- **Conservar con otra función** · [`helicone`](../human/fichas/helicone.md). Observabilidad en la capa de pasarela. Mantener como integración de proxy.

#### 024 Pasarelas y routers de proveedores LLM

- **Principal** · [`litellm`](../human/fichas/litellm.md). Pasarela multiproveedor para aplicaciones con gestión centralizada.
- **Alternativa que conservaría** · [`omniroute`](../human/fichas/omniroute.md). Enrutador local centrado en cuotas de proveedores.
- **Conservar con otra función** · [`claude-code-router`](../human/fichas/claude-code-router.md). Adaptador de un cliente específico. Mantener en configuración de Claude Code.
- **Retiro propuesto** · [`backdoor`](https://github.com/ajsai47/backdoor). El adaptador multiproveedor para Claude Code repite la función que cubre Claude Code Router, con alcance más amplio en la documentación de este último. Propuesta editorial de retirar la ficha independiente.

#### 042 Evaluación y pruebas de LLM

- **Principal** · [`promptfoo`](../human/fichas/promptfoo.md). Pruebas de regresión declarativas para prompts y selecciones de modelos.
- **Alternativa que conservaría** · [`deepeval`](../human/fichas/deepeval.md). Suite de evaluación integrada con pruebas Python estilo pytest.
- **Alternativa que conservaría** · [`ragas`](../human/fichas/ragas.md). Métricas y colecciones de prueba especializadas en aplicaciones RAG.

#### 100 Compactar contexto y tokens

- **Principal** · [`rtk`](../human/fichas/rtk.md). Reducción de salida repetitiva de comandos antes de que llegue al agente.
- **Alternativa que conservaría** · [`headroom`](../human/fichas/headroom.md). Compresión del contexto de texto largo en el flujo de un modelo.

#### 131 Servidores de inferencia de alto rendimiento

- **Principal** · [`vllm`](../human/fichas/vllm.md). Servidor general de inferencia de LLM acelerada por GPU.
- **Alternativa que conservaría** · [`sglang`](../human/fichas/sglang.md). Conservar para flujos multimodales o de generación estructurada que se adapten mejor a su runtime.

### Modelos abiertos y entrenamiento

#### 023 Fine-tuning de LLM

- **Principal** · [`unsloth`](../human/fichas/unsloth.md). Punto de entrada a afinación de modelos de lenguaje en una GPU.
- **Alternativa que conservaría** · [`axolotl`](../human/fichas/axolotl.md). Experimentos reproducibles por YAML y configuraciones de varias GPU.
- **Alternativa que conservaría** · [`llama-factory`](../human/fichas/llama-factory.md). Interfaz visual para ejecutar una afinación guiada.
- **Alternativa que conservaría** · [`torchtune`](../human/fichas/torchtune.md). Recetas modificables con piezas nativas de PyTorch.

#### 054 Frameworks de deep learning

- **Principal** · [`pytorch`](../human/fichas/pytorch.md). Arranque general para desarrollar o adaptar modelos en Python.
- **Alternativa que conservaría** · [`tensorflow`](../human/fichas/tensorflow.md). Continuidad de modelos y despliegues que ya usan el ecosistema TensorFlow.
- **Alternativa que conservaría** · [`jax`](../human/fichas/jax.md). Investigación numérica con transformaciones, compilación XLA y acceso a TPU.

#### 126 Aprendizaje por refuerzo para LLM

- **Principal** · [`verl`](../human/fichas/verl.md). Referencia para equipos con infraestructura distribuida de post-entrenamiento por refuerzo.
- **Alternativa que conservaría** · [`openrlhf`](../human/fichas/openrlhf.md). Alternativa cuando se elige Ray y DeepSpeed o su esquema de ejecución asíncrona.

### Procesar datos y trabajar con notebooks

#### 018 Apps web de datos en Python

- **Principal** · [`streamlit`](../human/fichas/streamlit.md). Primera app de datos desde un script Python.
- **Alternativa que conservaría** · [`nicegui`](../human/fichas/nicegui.md). Interfaces Python con disposición y controles más personalizados.
- **Alternativa que conservaría** · [`panel`](../human/fichas/panel.md). Dashboards construidos con HoloViz y notebooks.
- **Conservar con otra función** · [`gradio`](../human/fichas/gradio.md). Demos de modelos con entradas y salidas. Mantener en una ruta de demos de IA.
- **Conservar con otra función** · [`reflex`](../human/fichas/reflex.md). Framework web completo en Python. Reubicar en creación de aplicaciones.

#### 036 Formatos de tabla para data lakes

- **Principal** · [`apache-iceberg`](../human/fichas/apache-iceberg.md). Formato interoperable para tablas analíticas cuando se parte de cero.
- **Alternativa que conservaría** · [`delta-lake`](../human/fichas/delta-lake.md). Continuidad con Spark y ecosistemas centrados en Delta.
- **Alternativa que conservaría** · [`hudi`](../human/fichas/hudi.md). Ingestión incremental y actualización frecuente de registros.

#### 043 Procesamiento de datos tabulares

- **Principal** · [`pandas`](../human/fichas/pandas.md). Base general para limpieza y transformación interactiva de tablas en Python.
- **Alternativa que conservaría** · [`polars`](../human/fichas/polars.md). Motor de DataFrames y consultas para flujos tabulares de mayor volumen.
- **Alternativa que conservaría** · [`duckdb`](../human/fichas/duckdb.md). SQL analítico local sobre archivos y fuentes tabulares.

#### 107 Notebooks

- **Principal** · [`jupyterlab`](../human/fichas/jupyterlab.md). Notebook general y entorno de trabajo con extensiones.
- **Alternativa que conservaría** · [`marimo`](../human/fichas/marimo.md). Notebook reactivo guardado como código, adecuado para versionar y publicar.

### Animación, gráficos y creación 3D

#### 034 Animación web en JavaScript

- **Principal** · [`motion`](../human/fichas/motion.md). Animación de interfaz integrada con React en un proyecto nuevo.
- **Alternativa que conservaría** · [`gsap`](../human/fichas/gsap.md). Secuencias de animación extensas y sincronizadas.
- **Alternativa que conservaría** · [`animejs`](../human/fichas/animejs.md). Animación directa sobre DOM o SVG en proyectos JavaScript sin depender de React.

#### 038 Motores 3D para la web

- **Principal** · [`three.js`](../human/fichas/three-js.md). Escenas y visualización 3D integradas en una web.
- **Alternativa que conservaría** · [`babylonjs`](../human/fichas/babylonjs.md). Motor con subsistemas de juego, física y XR.
- **Alternativa que conservaría** · [`playcanvas`](../human/fichas/playcanvas.md). Motor web orientado también a la edición visual y al desarrollo de juegos.

#### 077 Motores de videojuegos

- **Principal** · [`godot`](../human/fichas/godot.md). Desarrollo 2D o 3D con editor integrado.
- **Alternativa que conservaría** · [`bevy`](../human/fichas/bevy.md). Juegos o simulaciones en Rust con arquitectura ECS.

### Skills de diseño, contenido y especialidades

#### 030 Skills de diseño de interfaces para agentes

- **Principal** · [`taste-skill`](../human/fichas/taste-skill.md). Dirección visual al crear una web asistida por un agente.
- **Alternativa que conservaría** · [`impeccable`](../human/fichas/impeccable.md). Revisión de interfaz existente con reglas automáticas y hooks.
- **Alternativa que conservaría** · [`ui-ux-pro-max-skill`](../human/fichas/ui-ux-pro-max-skill.md). Biblioteca consultable de estilos, paletas y tipografías.
- **Alternativa que conservaría** · [`hallmark`](../human/fichas/hallmark.md). Conservar por temas prediseñados y auditoría de rediseño. Evitar duplicarlo como segunda dirección visual general.

#### 052 Skills para quitar el tono de IA a los textos

- **Principal** · [`humanizer`](../human/fichas/humanizer.md). Primera skill para revisar y reescribir prosa de forma general.
- **Conservar con otra función** · [`stop-slop`](../human/fichas/stop-slop.md). Conservar la rúbrica de edición como referencia accesible desde la ficha principal.
- **Retiro propuesto** · [`no-ai-slop`](https://github.com/petergyang/no-ai-slop). La revisión de patrones repetitivos conservando la voz del autor se solapa directamente con Humanizer. Propuesta editorial de retirar una tercera ficha de la misma tarea.

#### 064 Skills de visualización 3D

- **Principal** · [`threejs-skills`](../human/fichas/threejs-skills.md). Referencias especializadas para construir escenas 3D en la web con Three.js.
- **Alternativa que conservaría** · [`3dviz-pro-max`](../human/fichas/3dviz-pro-max.md). Conservar para proyectos que también necesitan la ruta Blender o una dirección visual 3D más amplia.

#### 085 Skills de SEO para agentes

- **Principal** · [`claude-seo`](../human/fichas/claude-seo.md). Primera skill para una auditoría general de SEO y presencia en buscadores de IA.
- **Retiro propuesto** · [`geo-seo-claude`](https://github.com/zubair-trabzada/geo-seo-claude). Claude SEO ya documenta GEO, evaluación de citabilidad y exportación de informes PDF. El solapamiento cubre los tres motivos principales para ofrecer esta ficha por separado.

#### 105 Skills para redes sociales

- **Principal** · [`instagram-agent-skill`](../human/fichas/instagram-agent-skill.md). Ficha inicial para preparar formatos y guiones de Instagram.
- **Alternativa que conservaría** · [`linkedin-agent-skill`](../human/fichas/linkedin-agent-skill.md). Contenido profesional y formato de publicación propio de LinkedIn.

### Visión artificial, rostros y percepción

#### 089 Etiquetado de datos para visión

- **Principal** · [`label-studio`](../human/fichas/label-studio.md). Etiquetado de datos cuando se combinan varias modalidades.
- **Alternativa que conservaría** · [`cvat`](../human/fichas/cvat.md). Anotación visual intensiva en equipo con flujos especializados de visión.

#### 090 Intercambio de rostros

- **Principal** · [`facefusion`](../human/fichas/facefusion.md). Ficha de posproducción creativa con imágenes o video y autorización de las personas representadas.
- **Alternativa que conservaría** · [`deep-live-cam`](../human/fichas/deep-live-cam.md). Variante de efectos visuales en directo para usos consentidos.

### Audio, transcripción, voz y música

#### 015 Clonación de voz y TTS multilingüe

- **Principal** · [`gpt-sovits`](../human/fichas/gpt-sovits.md). Entrada a la síntesis con una voz propia y flujo de entrenamiento guiado.
- **Alternativa que conservaría** · [`f5-tts`](../human/fichas/f5-tts.md). Clonación sin entrenamiento específico de la voz del usuario.
- **Alternativa que conservaría** · [`cosyvoice`](../human/fichas/cosyvoice.md). Ruta multilingüe con énfasis en chino y sus variantes.
- **Alternativa que conservaría** · [`fish-speech`](../human/fichas/fish-speech.md). Alternativa de síntesis multilingüe con rutas de inferencia de baja latencia a verificar en el entorno.
- **Alternativa que conservaría** · [`index-tts`](../human/fichas/index-tts.md). Control de duración y expresión para doblaje o narración.

#### 028 Agentes de voz en tiempo real

- **Principal** · [`pipecat`](../human/fichas/pipecat.md). Flujos programables de voz con componentes intercambiables.
- **Alternativa que conservaría** · [`livekit-agents`](../human/fichas/livekit-agents.md). Integración con una infraestructura LiveKit de audio y video.
- **Alternativa que conservaría** · [`dograh`](../human/fichas/dograh.md). Configuración visual y flujo orientado a telefonía.
- **Alternativa que conservaría** · [`ten-framework`](../human/fichas/ten-framework.md). Framework de voz y conversación multimodal con extensiones y rutas RTC o WebSocket. Conservar cuando ese runtime y ecosistema sean un requisito.

#### 033 Generación de música

- **Principal** · [`ace-step-1.5`](../human/fichas/ace-step-1-5.md). Generación local de música desde instrucciones.
- **Alternativa que conservaría** · [`yue`](../human/fichas/yue.md). Producción de canciones con letra y acompañamiento.
- **Conservar con otra función** · [`audiocraft`](../human/fichas/audiocraft.md). Biblioteca de investigación que incluye efectos y códec. Conservar como referencia técnica.

#### 045 TTS ligero y rápido

- **Principal** · [`kokoro`](../human/fichas/kokoro.md). Narración con ejecución del modelo en local.
- **Alternativa que conservaría** · [`edge-tts`](../human/fichas/edge-tts.md). Ruta ligera que usa un servicio en línea. Confirmar condiciones antes de depender de ella.
- **Conservar con otra función** · [`luxtts`](../human/fichas/luxtts.md). Conservar junto a adaptación de voz en local cuando esa capacidad sea el propósito.

#### 047 Transcripción con Whisper

- **Principal** · [`whisper-cpp`](../human/fichas/whisper-cpp.md). Transcripción local para una primera prueba en equipos con recursos variados.
- **Alternativa que conservaría** · [`faster-whisper`](../human/fichas/faster-whisper.md). Integración Python y backend CTranslate2 para flujos por lotes.
- **Conservar con otra función** · [`whisper`](../human/fichas/whisper.md). Implementación y pesos de referencia de OpenAI. Conservar como fuente del ecosistema.

#### 120 Transcripción con modelos NVIDIA y alineación

- **Principal** · [`whisperx`](../human/fichas/whisperx.md). Transcripción cuando se necesita alinear tiempos y separar hablantes.
- **Conservar con otra función** · [`nemo`](../human/fichas/nemo.md). Framework de voz de NVIDIA para construir o adaptar pipelines completos. Reubicar como framework de voz.

### Video con código y agentes creativos

#### 020 Video y escenas por código

- **Principal** · [`hyperframes`](../human/fichas/hyperframes.md). Composición de video con HTML y guía para agentes creativos.
- **Alternativa que conservaría** · [`remotion`](../human/fichas/remotion.md). Producción de video a partir de componentes React.
- **Alternativa que conservaría** · [`motion-canvas`](../human/fichas/motion-canvas.md). Escenas animadas y explicativas con edición en tiempo real.
- **Alternativa que conservaría** · [`revideo`](../human/fichas/revideo.md). Renderizado TypeScript para servicios y API de video.
- **Conservar con otra función** · [`moviepy`](../human/fichas/moviepy.md). Edición y composición desde Python. Mantener como herramienta de edición por código.

#### 063 Skills y flujos de producción de video

- **Principal** · [`openmontage`](../human/fichas/openmontage.md). Producción de video asistida con recursos propios y etapas componibles.
- **Alternativa que conservaría** · [`video-use`](../human/fichas/video-use.md). Edición y corte de material existente con FFmpeg y transcripción según la ruta documentada.
- **Conservar con otra función** · [`remotion-superpowers`](../human/fichas/remotion-superpowers.md). Mantener como ampliación de Remotion para quien ya eligió ese motor y quiere conectar etapas audiovisuales externas. Evitar presentarlo como otro motor de producción.

#### 115 Animaciones matemáticas (Manim)

- **Principal** · [`manim-community`](../human/fichas/manim-community.md). Animaciones matemáticas en Python con la documentación de la edición mantenida por la comunidad.
- **Conservar con otra función** · [`manim`](../human/fichas/manim.md). Conservar la variante original para reproducir escenas y proyectos de 3Blue1Brown.

### Presentaciones, diagramas y explicación visual

#### 041 Diagramas como código

- **Principal** · [`mermaid`](../human/fichas/mermaid.md). Diagramas técnicos rápidos que se integran en documentación Markdown.
- **Alternativa que conservaría** · [`d2`](../human/fichas/d2.md). Diseño declarativo con varios motores de disposición y exportación gráfica.
- **Alternativa que conservaría** · [`plantuml`](../human/fichas/plantuml.md). UML técnico y continuidad con diagramas de clases y secuencia existentes.

#### 058 Presentaciones desde Markdown

- **Principal** · [`slidev`](../human/fichas/slidev.md). Presentaciones técnicas en Markdown con código y componentes interactivos.
- **Alternativa que conservaría** · [`marp`](../human/fichas/marp.md). Presentación sencilla desde Markdown y edición en su ecosistema de herramientas.
- **Conservar con otra función** · [`reveal.js`](../human/fichas/reveal-js.md). Framework de presentación HTML con soporte opcional para Markdown. Ubicar junto a slides web personalizables.

#### 071 Skills de diagramas de arquitectura

- **Principal** · [`archify`](../human/fichas/archify.md). Diagramas interactivos que relacionan código o planes existentes.
- **Alternativa que conservaría** · [`diagram-design`](../human/fichas/diagram-design.md). Diagramas explicativos más libres en HTML y SVG, con instrucciones de composición.

#### 129 Generación de presentaciones con IA

- **Principal** · [`ppt-master`](../human/fichas/ppt-master.md). Elaboración de un PowerPoint editable asistido por un agente a partir de fuentes propias.
- **Alternativa que conservaría** · [`presenton`](../human/fichas/presenton.md). Servicio de generación de presentaciones con interfaz y API.

### Navegadores y automatización web

#### 016 Automatización de navegador y pruebas E2E

- **Principal** · [`playwright`](../human/fichas/playwright.md). Primera opción para pruebas de navegador de una aplicación nueva.
- **Alternativa que conservaría** · [`cypress`](../human/fichas/cypress.md). Pruebas de componentes y trabajo interactivo en el navegador.
- **Alternativa que conservaría** · [`selenium`](../human/fichas/selenium.md). Continuidad de suites WebDriver y ejecución sobre grids.
- **Alternativa que conservaría** · [`webdriverio`](../human/fichas/webdriverio.md). Automatización móvil con Appium en el flujo de pruebas.
- **Conservar con otra función** · [`puppeteer`](../human/fichas/puppeteer.md). Automatización programática para capturas o extracción. Mantener fuera de la primera selección de suites E2E.

#### 025 Agentes que navegan la web

- **Principal** · [`browser-use`](../human/fichas/browser-use.md). Referencia de biblioteca Python para automatizar navegación de flujos autorizados.
- **Alternativa que conservaría** · [`stagehand`](../human/fichas/stagehand.md). Ruta TypeScript con automatización programática y pasos en lenguaje natural.
- **Alternativa que conservaría** · [`skyvern`](../human/fichas/skyvern.md). Flujos repetitivos de formularios y operaciones con interfaz visual.
- **Conservar con otra función** · [`browser-harness`](../human/fichas/browser-harness.md). Conexión de un agente de código a una sesión de navegador. Ubicar como integración del cliente.

#### 067 CLIs de navegador para agentes

- **Principal** · [`playwright-cli`](../human/fichas/playwright-cli.md). Entrada en terminal ligada al ecosistema Playwright y a sus skills.
- **Alternativa que conservaría** · [`agent-browser`](../human/fichas/agent-browser.md). Conservar como CLI independiente para un flujo que usa referencias del árbol de accesibilidad.

#### 110 Motores de navegador independientes

- **Principal** · [`ladybird`](../human/fichas/ladybird.md). Ficha para seguir un navegador independiente en desarrollo.
- **Conservar con otra función** · [`servo`](../human/fichas/servo.md). Motor embebible en Rust. Mantener como referencia para integrar tecnologías web en aplicaciones.

## Alcance de la evidencia

Las 138 comparaciones usan las fichas del catálogo y los grupos del 2026-11-27. Se hizo un cribado de los 409 README públicos para detectar notas de sustitución o mantenimiento. Se contrastaron las opciones que podían salir con la documentación de sus sustitutos y se verificaron la identidad, la rama principal y el último commit de los cuatro retiros propuestos. Las recomendaciones reflejan evidencia documental. El alcance se limita a los repos de los 138 grupos.

[Índice compacto](../INDICE_IA.json) · [Índice detallado](../INDICE_IA.detalle.json) · [Puntuaciones](../data/metricas/puntuaciones.json)
