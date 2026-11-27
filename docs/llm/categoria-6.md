# Alexandría para agentes · Memoria, RAG y búsqueda de conocimiento

Categoría 6 completa (30 repos, 3 subcategorías). Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=6 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `mem0` | memoria | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y… | 2 Intermedio | 77 | Apache-2.0 (OSI permisiva) | recomendado |
| `claude-mem` | memoria | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes… | 1 Básico | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `openviking` | memoria | Base de contexto para agentes que organiza memoria, documentos y skills y… | 3 Avanzado | 69 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `cognee` | memoria | Plataforma de memoria para agentes que combina grafos de conocimiento y… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | alternativa |
| `mempalace` | memoria | Memoria de IA local-first con almacenamiento verbatim y backend conectable… | 2 Intermedio | 67 | MIT (OSI permisiva) | sin grupo |
| `engram` | memoria | Memoria persistente para agentes de código en un solo binario Go con SQLite… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `graphiti` | memoria | Librería de Zep para construir grafos de conocimiento temporales en tiempo real… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `supermemory` | memoria | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia… | 1 Básico | 62 | MIT (OSI permisiva) | alternativa |
| `letta` | memoria | Harness de agentes con estado (Letta Code, antes MemGPT): memoria, identidad y… | 2 Intermedio | 57 | Apache-2.0 (OSI permisiva) | alternativa |
| `agentmemory` | memoria | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor… | 2 Intermedio | 53 | Apache-2.0 (OSI permisiva) | alternativa |
| `dsh-noema` | memoria | Plugin de memoria persistente para DeepSeek Harness con herramientas de… | 2 Intermedio | 48 | MIT (OSI permisiva) | sin grupo |
| `ragflow` | rag | Motor de RAG con comprensión profunda de documentos, citas y agentes… | 3 Avanzado | 82 | Apache-2.0 (OSI permisiva) | recomendado |
| `onyx` | rag | Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con… | 2 Intermedio | 70 | MIT + Onyx Enterprise License (ee/) (open-core) | sin grupo |
| `lightrag` | rag | RAG simple y rápido que combina grafo de conocimiento y vectores, de la… | 2 Intermedio | 66 | MIT (OSI permisiva) | alternativa |
| `kotaemon` | rag | Interfaz RAG limpia y personalizable para chatear con documentos, con modelos… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | sin grupo |
| `pageindex` | rag | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `meilisearch` | rag | Motor de búsqueda rápido en Rust con texto completo, búsqueda semántica e… | 1 Básico | 58 | MIT (source-available) | sin grupo |
| `txtai` | rag | Framework de IA todo en uno para búsqueda semántica, RAG, pipelines con LLM… | 2 Intermedio | 58 | Apache-2.0 (OSI permisiva) | sin grupo |
| `graphrag` | rag | Sistema de RAG de Microsoft que recupera información sobre un grafo de… | 2 Intermedio | 55 | MIT (OSI permisiva) | alternativa |
| `chonkie` | rag | Divide textos largos en fragmentos para indexarlos o recuperarlos, con… | 2 Intermedio | 51 | MIT (OSI permisiva) | sin grupo |
| `agentic-rag-for-dummies` | rag | Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta… | 2 Intermedio | 47 | MIT (OSI permisiva) | sin grupo |
| `milvus` | vectores | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de… | 3 Avanzado | 78 | Apache-2.0 (OSI permisiva) | recomendado |
| `qdrant` | vectores | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y… | 1 Básico | 66 | Apache-2.0 (OSI permisiva) | alternativa |
| `chroma` | vectores | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | alternativa |
| `lancedb` | vectores | Base de datos vectorial embebida sobre el formato columnar Lance: búsqueda… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `weaviate` | vectores | Base de datos vectorial nativa de la nube que guarda objetos y vectores, con… | 2 Intermedio | 59 | BSD-3-Clause (open-core) | alternativa |
| `turbovec` | vectores | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `faiss` | vectores | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en… | 2 Intermedio | 57 | MIT (OSI permisiva) | alternativa |
| `flagembedding` | vectores | Calcula representaciones y relevancia de textos con modelos BGE para ordenar… | 2 Intermedio | 57 | MIT (OSI permisiva) | sin grupo |
| `pgvector` | vectores | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos… | 2 Intermedio | 57 | PostgreSQL (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### mem0 (`mem0`)

- **Repo:** https://github.com/mem0ai/mem0 · Apache-2.0 · nivel 2 · 77/100 · recomendado en «Capas de memoria para apps y agentes de IA»
- **Qué es:** Capa de memoria para asistentes y agentes de IA de Mem0 («mem-zero»), de código abierto (Apache 2.0) con plataforma gestionada de pago. Muy activa; en abril de 2026 publicó un nuevo algoritmo de memoria y su evaluación es reproducible con…
- **Cuándo elegirlo:** Casos: Recordar preferencias de atención; Mantener contexto de una app entre conversaciones.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; LLM; embeddings; almacén; identificador ficticio de usuario; hardware prerequisites; API de IA: depends; Python; LLM; embeddings; almacén; identificador ficticio de usuario.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install mem0ai` — fuente: https://github.com/mem0ai/mem0/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda dos preferencias de un usuario ficticio y consulta una de ellas por su identificador Éxito: La búsqueda devuelve la preferencia del usuario correcto
- **Combina con:** `langgraph` [3/py], `crewai` [3/py], `qdrant` [6/vectores], `hermes-desktop` [8/workspaces], `agents-towards-production` [19/guias], `agno` [3/py]
- **Alternativas:** `cognee`, `graphiti`, `supermemory`, `letta`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): letta, cognee, supermemory. La migración de la v2 a la v3 de código abierto tiene guía propia. Las skills enseñan a integrar Mem0; no incluyen el servicio ni ejecutan gratis la memoria de tu aplicación.

### claude-mem (`claude-mem`)

- **Repo:** https://github.com/thedotmack/claude-mem · Apache-2.0 · nivel 1 · 74/100 · recomendado en «Memoria persistente para agentes de código»
- **Qué es:** Sistema de memoria persistente de código abierto (Apache 2.0) para agentes de código, de thedotmack. Muy activo (v15.19.0), con servicio en la nube opcional (CMEM Pro / cmem.ai) para copias y memoria alojada.
- **Cuándo elegirlo:** Casos: Conservar decisiones entre sesiones; Recuperar el motivo de un cambio de código.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Node 20.19+ o 22.12+; Bun y uv; agente admitido; proveedor del observador; hardware prerequisites; API de IA: opcional; Node 20.19+ o 22.12+; Bun y uv; agente admitido; proveedor del observador.
- **Instalación (documentada en la fuente; no ejecutada):** `npx claude-mem install` — fuente: https://github.com/thedotmack/claude-mem/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda una decisión ficticia en una sesión y consulta si se recupera en una nueva Éxito: Puedes distinguir captura, resumen y recuperación y ver qué proveedor los produjo
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal], `openclaw` [21/asistentes]
- **Alternativas:** `engram`, `agentmemory`
- **Riesgos y avisos:** Alternativas (elige una): engram, agentmemory. Las observaciones pueden contener código o secretos: revisa qué se sincroniza con la nube. Antigravity documentado es la variante CLI; algunos agentes solo buscan memoria y no capturan sesiones; no todos tienen las mismas funciones.

### OpenViking (`openviking`)

- **Repo:** https://github.com/volcengine/OpenViking · AGPL-3.0 · nivel 3 · 69/100
- **Qué es:** Base de datos de contexto de código abierto (AGPLv3) para agentes de IA, de Volcengine (ByteDance). Activa (v0.5.5), con un servicio alojado por Volcengine y un Studio web.
- **Cuándo elegirlo:** Casos: Conservar contexto de un proyecto; Consultar conocimientos y skills desde un almacén común.
- **Requisitos:** nivel 3: preparación pesada; uv; proveedor o Ollama; servidor; Node 18+ y macOS/Linux para instalador de plugins; hardware prerequisites; API de IA: depends; uv; proveedor o Ollama; servidor; Node 18+ y macOS/Linux para instalador de plugins.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install openviking --upgrade && openviking-server init` — fuente: https://github.com/volcengine/OpenViking/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda una nota de contexto ficticia y consulta cómo se recupera en otra sesión Éxito: Puedes inspeccionar el documento y la memoria que usa el agente
- **Combina con:** `claude-code` [20/terminal], `openclaw` [21/asistentes], `ollama` [8/motores]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La AGPLv3 obliga a publicar cambios si ofreces el servicio modificado a terceros. El instalador de plugins tiene restricciones de sistema; en Windows el autor orienta hacia la app de escritorio; no extrapoles soporte de hooks.

### cognee (`cognee`)

- **Repo:** https://github.com/topoteretes/cognee · Apache-2.0 · nivel 2 · 68/100 · alternativa en «Capas de memoria para apps y agentes de IA»
- **Qué es:** Plataforma de memoria de IA de código abierto (Apache 2.0) de topoteretes que da a los agentes memoria persistente a largo plazo, con artículo de investigación propio. Activa (v1.6.8) y con servicio gestionado Cognee Cloud.
- **Cuándo elegirlo:** Casos: Construir memoria de documentos; Recuperar contexto desde Claude Code o Codex.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python 3.10–3.14; modelos locales iniciales; plugins opcionales; hardware prerequisites; API de IA: opcional; Python 3.10–3.14; modelos locales iniciales; plugins opcionales.
- **Instalación (documentada en la fuente; no ejecutada):** `uv pip install "cognee[gliner]"` — fuente: https://github.com/topoteretes/cognee/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda un hecho ficticio con remember y recupéralo con recall sin configurar una clave LLM Éxito: Se devuelve el texto de origen y no una respuesta inventada
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `openclaw` [21/asistentes], `neo4j-mcp` [5/servidores]
- **Alternativas:** `mem0`, `graphiti`, `supermemory`, `letta`, `graphrag`
- **Riesgos y avisos:** Alternativas (elige una): graphiti, mem0, graphrag, letta. En la API, `ENABLE_BACKEND_ACCESS_CONTROL=false` solo para uso local de un usuario. Los plugins de los dos agentes están documentados; MCP usa stdio o HTTP; no asumas que sampling permite usar cualquier plan del cliente.

### mempalace (`mempalace`)

- **Repo:** https://github.com/MemPalace/mempalace · MIT · nivel 2 · 67/100
- **Qué es:** Sistema de memoria de IA «local primero» de código abierto (MIT) del proyecto MemPalace, distribuido en PyPI. Muy activo (v3.12.0); avisa de sitios web impostores: solo el repositorio, el paquete de PyPI y su web oficial son legítimos.
- **Cuándo elegirlo:** Casos: Recuperar decisiones antiguas; Consultar archivos de contexto sin resúmenes destructivos.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python o Docker; modelo de embeddings descargado; directorio de prueba; hardware prerequisites; API de IA: opcional; Python o Docker; modelo de embeddings descargado; directorio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/MemPalace/mempalace/blob/develop/README.md

  ```bash
  python -m venv .venv && source .venv/bin/activate
  pip install mempalace
  ```
- **Primera prueba propuesta (no ejecutada):** Indexa dos notas propias y busca una decisión con palabras distintas a las originales Éxito: Puedes abrir el fragmento literal y comprobar su origen
- **Combina con:** `claude-code` [20/terminal], `chroma` [6/vectores], `codex` [20/terminal]
- **Riesgos y avisos:** El primer uso descarga el modelo; montar archivos en Docker es necesario para que pueda leerlos; los porcentajes de benchmark son del autor.

### Engram (`engram`)

- **Repo:** https://github.com/Gentleman-Programming/engram · MIT · nivel 1 · 63/100 · alternativa en «Memoria persistente para agentes de código»
- **Qué es:** Memoria persistente para agentes de código de Gentleman-Programming, de código abierto (MIT) y financiada por donaciones, sin funciones de pago. Muy activa (v3.7.2) y parte del ecosistema Gentle-AI.
- **Cuándo elegirlo:** Casos: Recordar decisiones técnicas; Hacer una entrega de contexto entre sesiones.
- **Requisitos:** nivel 1: preparación sencilla; Binario oficial o Go; cliente MCP; directorio de memoria de prueba; hardware prerequisites; API de IA: no; Binario oficial o Go; cliente MCP; directorio de memoria de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install gentleman-programming/tap/engram` — fuente: https://github.com/Gentleman-Programming/engram/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda una decisión con su razón y recupérala por palabras clave Éxito: El registro aparece con contenido y contexto que puedes inspeccionar
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `gemini-cli` [20/terminal], `deepseek-harness` [20/terminal], `antigravity-cli` [20/terminal]
- **Alternativas:** `claude-mem`, `agentmemory`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): claude-mem, agentmemory. MCP no equivale por sí solo a captura automática; Codex añade requisitos de capacidad y sesión que debes revisar en la guía.

### Graphiti (`graphiti`)

- **Repo:** https://github.com/getzep/graphiti · Apache-2.0 · nivel 2 · 62/100 · alternativa en «Capas de memoria para apps y agentes de IA»
- **Qué es:** Framework de código abierto (Apache 2.0) de Zep para construir y consultar grafos de contexto temporales para agentes de IA. Activo (v0.31.2); Zep ofrece una plataforma empresarial gestionada sobre el mismo concepto.
- **Cuándo elegirlo:** Casos: Representar cambios de una relación comercial; Conservar hechos de conversaciones con fechas.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; Neo4j o FalkorDB; LLM y embeddings configurados; hardware prerequisites; API de IA: depends; Python; Neo4j o FalkorDB; LLM y embeddings configurados.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install graphiti-core` — fuente: https://github.com/getzep/graphiti/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade dos hechos con fechas distintas y consulta cuál era válido en cada momento Éxito: El grafo conserva relaciones temporales y sus fuentes
- **Combina con:** `claude-code` [20/terminal], `langgraph` [3/py], `mcp-neo4j` [5/servidores], `mirofish` [3/experimentos], `neo4j-mcp` [5/servidores]
- **Alternativas:** `mem0`, `cognee`, `supermemory`, `letta`, `graphrag`
- **Riesgos y avisos:** Alternativas (elige una): cognee, graphrag. Su MCP es una referencia experimental sin autenticación ni autorización: úsalo aislado para pruebas, no como despliegue público de producción.

### supermemory (`supermemory`)

- **Repo:** https://github.com/supermemoryai/supermemory · MIT · nivel 1 · 62/100 · alternativa en «Capas de memoria para apps y agentes de IA»
- **Qué es:** Motor de memoria y contexto para IA de Supermemory, que se define como laboratorio de investigación. El repositorio es MIT (servidor en versión 0.0.x) y el servicio principal es una API alojada; afirma ser el n.º 1 en LongMemEval, LoCoMo y…
- **Cuándo elegirlo:** Casos: Conservar contexto entre agentes; Buscar documentos y recuerdos de un proyecto.
- **Requisitos:** nivel 1: preparación sencilla; Node.js para ruta local; modelo elegido; cuenta para Cloud; hardware prerequisites; API de IA: depends; Node.js para ruta local; modelo elegido; cuenta para Cloud.
- **Instalación (documentada en la fuente; no ejecutada):** `npx supermemory local` — fuente: https://github.com/supermemoryai/supermemory/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda una nota de prueba y consulta su contenido desde una segunda sesión Éxito: Puedes verificar qué se almacenó y en qué instancia
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `ollama` [8/motores]
- **Alternativas:** `mem0`, `cognee`, `graphiti`, `letta`, `agentmemory`
- **Riesgos y avisos:** Alternativas (elige una): mem0, agentmemory. Con el MCP alojado los datos se procesan en sus servidores. Los plugins y MCP son vías de conexión; confirma que apuntan a la instancia local si buscas mantener el procesamiento en tu equipo.

### Letta (`letta`)

- **Repo:** https://github.com/letta-ai/letta-code · Apache-2.0 · nivel 2 · 57/100 · alternativa en «Capas de memoria para apps y agentes de IA»
- **Qué es:** Letta Code es el harness de agentes con estado de Letta (los creadores de MemGPT y de «sleep-time compute»), con licencia Apache 2.0, escrito en TypeScript.
- **Cuándo elegirlo:** Casos: Estudiar un agente con memoria persistente; Crear un asistente que conserve preferencias.
- **Requisitos:** nivel 2: preparación media; Node.js y npm, o Python 3.9+ con uv/pipx; credenciales del proveedor de modelos o cuenta de Letta; hardware prerequisites; API de IA: depends; Node.js y npm, o Python 3.9+ con uv/pipx; credenciales del proveedor de modelos o cuenta de Letta.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g @letta-ai/letta-code` — fuente: https://github.com/letta-ai/letta-code/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el enlace al código actual y crea un agente con una nota de memoria ficticia Éxito: Puedes recuperar esa nota en una conversación posterior
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `openclaw` [21/asistentes], `hermes-agent` [21/asistentes]
- **Alternativas:** `mem0`, `cognee`, `graphiti`, `supermemory`
- **Riesgos y avisos:** Alternativas (elige una): mem0, cognee. La ficha apuntaba a letta-ai/letta; se cambió a letta-ai/letta-code por decisión del propietario. Letta Cloud es el backend por defecto; equipos remotos y secretos requieren cuenta de Letta. AgentFile (.af) se eliminó.

### agentmemory (`agentmemory`)

- **Repo:** https://github.com/rohitg00/agentmemory · Apache-2.0 · nivel 2 · 53/100 · alternativa en «Memoria persistente para agentes de código»
- **Qué es:** Memoria persistente de código abierto (Apache 2.0) para sesiones de programación y agentes, de rohitg00, que se presenta como implementación del patrón «LLM Wiki» de Karpathy con puntuación de confianza, ciclo de vida, grafos y búsqueda…
- **Cuándo elegirlo:** Casos: Compartir contexto entre Claude Code y Codex; Consultar decisiones por proyecto.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node.js >=20; servidor local; hooks revisados en el cliente; hardware prerequisites; API de IA: opcional; Node.js >=20; servidor local; hooks revisados en el cliente.
- **Instalación (documentada en la fuente; no ejecutada):** `npx -y @agentmemory/agentmemory@latest` — fuente: https://github.com/rohitg00/agentmemory/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Registra una decisión ficticia y búscala desde otro cliente conectado al mismo servidor Éxito: Puedes inspeccionar el recuerdo y confirmar que ambos clientes usan la misma instancia
- **Combina con:** `claude-code` [20/terminal], `gemini-cli` [20/terminal], `hermes-agent` [21/asistentes], `deepseek-harness` [20/terminal]
- **Alternativas:** `claude-mem`, `engram`, `supermemory`
- **Riesgos y avisos:** Alternativas (elige una): engram, supermemory, claude-mem. No expongas los puertos 3111/3113 fuera de loopback sin autenticación. Las funciones y hooks dependen del runtime del cliente; la instalación de MCP no prueba que la captura automática esté activa.

### dsh-noema (`dsh-noema`)

- **Repo:** https://github.com/ZSeven-W/dsh-noema · MIT · nivel 2 · 48/100
- **Qué es:** Plugin de código abierto (MIT) de ZSeven-W que añade memoria a largo plazo a DeepSeek Harness usando Noema, un sistema de memoria local sin vectores.
- **Cuándo elegirlo:** Casos: Dar memoria a DeepSeek Harness; Importar una nota propia de otro agente.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; DeepSeek Harness compatible; plugin Noema; directorio de prueba; hardware prerequisites; API de IA: no; DeepSeek Harness compatible; plugin Noema; directorio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ZSeven-W/dsh-noema/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda un recuerdo ficticio desde DSH y comprueba que puedes verlo y eliminarlo desde ajustes Éxito: El recuerdo persiste y el panel muestra su contenido
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `hermes-agent` [21/asistentes], `deepseek-harness` [20/terminal]
- **Riesgos y avisos:** Requiere DeepSeek Harness (deepseek-harness). Importar archivos de memoria de Claude, Codex o Antigravity no es una integración para ejecutar este plugin dentro de esos clientes.

### RAGFlow (`ragflow`)

- **Repo:** https://github.com/infiniflow/ragflow · Apache-2.0 · nivel 3 · 82/100 · recomendado en «RAG con grafos e índices de conocimiento»
- **Qué es:** Motor RAG (generación aumentada por recuperación) de código abierto (Apache 2.0) de InfiniFlow, que fusiona RAG con capacidades de agente. Muy activo: la versión 1.0.0 salió el 6 de noviembre de 2026 y el código principal está ahora en Go…
- **Cuándo elegirlo:** Casos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento.
- **Requisitos:** nivel 3: preparación pesada, varios servicios con Docker Compose; Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos; hardware prerequisites; API de IA: depends; Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose -f docker-compose.yml up -d` — fuente: https://github.com/infiniflow/ragflow/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Indexa un PDF propio corto y pregunta por un dato identificable con cita Éxito: La respuesta permite abrir el fragmento y comprobar su procedencia
- **Combina con:** `ollama` [8/motores], `activepieces` [1/motores], `langfuse` [23/observabilidad], `paddleocr` [13/ocr]
- **Alternativas:** `lightrag`, `pageindex`, `graphrag`, `dify`
- **Riesgos y avisos:** Alternativas (elige una): dify, lightrag. El puerto 80 puede chocar con otros servicios web del mismo servidor. Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar.

### onyx (`onyx`)

- **Repo:** https://github.com/onyx-dot-app/onyx · MIT + Onyx Enterprise License (ee/) · nivel 2 · 70/100
- **Qué es:** Capa de conocimiento y contexto para equipos y agentes de IA de Onyx (antes Danswer). La Community Edition es MIT y la Enterprise Edition añade funciones para grandes organizaciones (GitHub marca la licencia como no estándar por esa…
- **Cuándo elegirlo:** Casos: Buscar conocimiento de equipo; Dar contexto organizacional a un agente de código.
- **Requisitos:** nivel 2: preparación media; Docker o ruta elegida; proveedor; fuente documental de prueba; hardware prerequisites; API de IA: depends; Docker o ruta elegida; proveedor; fuente documental de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install onyx-cli && onyx-cli deploy install` — fuente: https://github.com/onyx-dot-app/onyx/blob/main/documentation/snippets/quickstart.mdx
- **Primera prueba propuesta (no ejecutada):** Conecta dos documentos de prueba y formula una consulta que exija una cita Éxito: La respuesta muestra fuentes accesibles para el usuario que consulta
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `searxng` [4/busqueda], `firecrawl` [4/crawlers]
- **Alternativas:** `anything-llm`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): anything-llm. Respeta los permisos de las fuentes; revisa qué conectores sincronizan datos sensibles. Lite es un chat ligero y no indexa documentos; para la prueba documental necesitas el despliegue completo.

### LightRAG (`lightrag`)

- **Repo:** https://github.com/HKUDS/LightRAG · MIT · nivel 2 · 66/100 · alternativa en «RAG con grafos e índices de conocimiento»
- **Qué es:** Sistema RAG «simple y rápido» basado en grafos de conocimiento, del laboratorio HKUDS (Universidad de Hong Kong). MIT y muy activo; la última etiqueta es una release candidate (v1.5.8rc1) y en 2026 absorbió el proyecto multimodal…
- **Cuándo elegirlo:** Casos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python y uv; LLM; embeddings; almacenamiento; configuración .env; hardware prerequisites; API de IA: depends; Python y uv; LLM; embeddings; almacenamiento; configuración .env.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/HKUDS/LightRAG/blob/main/README.md

  ```bash
  # Install LightRAG Server as a tool using uv (recommended)
  uv tool install "lightrag-hku[api]"
  ```
- **Primera prueba propuesta (no ejecutada):** Indexa un documento ficticio y compara una consulta sobre una entidad con otra sobre sus relaciones Éxito: Puedes inspeccionar los resultados y las relaciones recuperadas
- **Combina con:** `pgvector` [6/vectores], `ollama` [8/motores], `docling` [13/conversion], `langfuse` [23/observabilidad], `ragas` [23/observabilidad], `deeptutor` [21/asistentes]
- **Alternativas:** `ragflow`, `pageindex`, `graphrag`
- **Riesgos y avisos:** Alternativas (elige una): graphrag, ragflow, pageindex. `lightrag-server` escucha en 0.0.0.0 sin autenticación por defecto: actívala antes de usarlo en red. Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta.

### kotaemon (`kotaemon`)

- **Repo:** https://github.com/Cinnamon/kotaemon · Apache-2.0 · nivel 2 · 61/100
- **Qué es:** Herramienta RAG de código abierto (Apache-2.0) de Cinnamon AI, pensada tanto para usuarios finales como para desarrolladores. Popular, aunque el ritmo de cambios se ha reducido (último push en julio de 2026).
- **Cuándo elegirlo:** Casos: hacer preguntas con citas sobre una carpeta de PDF propios; comparar estrategias RAG clásicas y basadas en grafos sobre el mismo corpus.
- **Requisitos:** nivel 2: preparación media; Python, Dockerfile, pyproject.toml; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Cinnamon/kotaemon/blob/main/README.md

  ```bash
  docker run -e GRADIO_SERVER_NAME=0.0.0.0 -e GRADIO_SERVER_PORT=7860 -v ./ktem_app_data:/app/ktem_app_data -p 7860:7860 -it --rm ghcr.io/cinnamon/kotaemon:main-full
  ```
- **Primera prueba propuesta (no ejecutada):** Arranca la imagen Docker main-lite (u ollama) del README, sube un PDF y haz una pregunta. Éxito: La respuesta incluye citas enlazadas a las páginas del documento.
- **Combina con:** `ollama` [8/motores], `lightrag`, `graphrag`, `docling` [13/conversion]
- **Riesgos y avisos:** Alternativas cercanas en el catálogo: anything-llm, open-notebook.

### PageIndex (`pageindex`)

- **Repo:** https://github.com/VectifyAI/PageIndex · MIT · nivel 2 · 60/100 · alternativa en «RAG con grafos e índices de conocimiento»
- **Qué es:** Sistema RAG «sin vectores» basado en razonamiento, de VectifyAI. La versión de código abierto es MIT (v0.7.0) y convive con productos en la nube: PageIndex Cloud, una API de búsqueda de páginas y una app de análisis de documentos.
- **Cuándo elegirlo:** Casos: Consultar informes largos por su estructura; Encontrar una sección de un contrato.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; documento de prueba; proveedor para modo local o cuenta Cloud; hardware prerequisites; API de IA: depends; Python; documento de prueba; proveedor para modo local o cuenta Cloud.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U pageindex` — fuente: https://github.com/VectifyAI/PageIndex/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Indexa un PDF con secciones y pregunta por un dato de una sección concreta Éxito: La recuperación señala la parte pertinente del documento
- **Combina con:** `claude-code` [20/terminal], `openai-agents-python` [3/py], `claude-agent-sdk-python` [3/py]
- **Alternativas:** `ragflow`, `lightrag`, `graphrag`
- **Riesgos y avisos:** Alternativa (elige una): lightrag. Cada consulta implica razonamiento del LLM: más latencia y coste por pregunta que una búsqueda vectorial. Sin base vectorial no significa sin modelo ni coste; su adaptador Claude es integración del proyecto y no una aprobación universal de planes.

### Meilisearch (`meilisearch`)

- **Repo:** https://github.com/meilisearch/meilisearch · MIT · nivel 1 · 58/100
- **Qué es:** Motor de búsqueda de código abierto de Meili SAS. La Community Edition es MIT; la Enterprise Edition añade sharding y otras funciones bajo licencia comercial o Business Source License 1.1. Proyecto muy popular y maduro con nube gestionada.
- **Cuándo elegirlo:** Casos: añadir búsqueda instantánea con facetas a una web o aplicación; combinar búsqueda por palabras y semántica como capa de recuperación para RAG.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, Dockerfile; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -it --rm -p 7700:7700 -v $(pwd)/meili_data:/meili_data getmeili/meilisearch:latest` — fuente: https://github.com/meilisearch/meilisearch/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Meilisearch con Docker o el script de instalación, sube un JSON de ejemplo y busca con una errata. Éxito: La búsqueda devuelve los documentos correctos en milisegundos pese a la errata.
- **Combina con:** `ollama` [8/motores], `langchain` [3/py], `firecrawl` [4/crawlers]
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Revisa la licencia antes de usar funciones Enterprise en producción.

### txtai (`txtai`)

- **Repo:** https://github.com/neuml/txtai · Apache-2.0 · nivel 2 · 58/100
- **Qué es:** Framework de código abierto (Apache-2.0) de NeuML, mantenido de forma continua desde 2020. Requiere Python 3.11 o superior.
- **Cuándo elegirlo:** Casos: indexar documentos y hacer búsqueda semántica con SQL en local; montar un RAG o un grafo de conocimiento sin desplegar varios servicios.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml, setup.py; hardware model_dependent; API de IA: opcional; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install txtai` — fuente: https://github.com/neuml/txtai/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install txtai`, indexa unas frases y busca por significado. Éxito: La búsqueda devuelve las frases más parecidas aunque no compartan palabras.
- **Combina con:** `transformers` [24/entrenamiento], `litellm` [23/serving], `llama-cpp` [8/motores], `claude-code` [20/terminal]
- **Riesgos y avisos:** Alternativas cercanas en el catálogo: llama-index, haystack.

### graphrag (`graphrag`)

- **Repo:** https://github.com/microsoft/graphrag · MIT · nivel 2 · 55/100 · alternativa en «RAG con grafos e índices de conocimiento»
- **Qué es:** Proyecto de investigación de Microsoft Research (MIT) que usa grafos de conocimiento para construir el contexto de respuesta de un LLM. Publicado en julio de 2024; según su README está mayormente en modo mantenimiento: no acepta PR ni…
- **Cuándo elegirlo:** Casos: Estudiar relaciones de un corpus; Comparar búsqueda local y resumen global.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python según guía; modelo y embeddings; corpus pequeño; presupuesto de indexación; hardware prerequisites; API de IA: depends; Python según guía; modelo y embeddings; corpus pequeño; presupuesto de indexación.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install graphrag` — fuente: https://github.com/microsoft/graphrag/blob/main/docs/get_started.md
- **Primera prueba propuesta (no ejecutada):** Indexa unos textos ficticios y pregunta por un tema que conecte varios de ellos Éxito: Puedes revisar entidades, comunidades y fuentes de la respuesta
- **Combina con:** `litellm` [23/serving], `mcp-neo4j` [5/servidores], `docling` [13/conversion], `graphify` [7/codigo], `scrapegraph-ai` [4/llm], `kotaemon`
- **Alternativas:** `ragflow`, `lightrag`, `pageindex`, `graphiti`, `cognee`
- **Riesgos y avisos:** Alternativas (elige una): graphiti, cognee, lightrag. Por su estado de mantenimiento, evalúa lightrag para proyectos nuevos. Proyecto de investigación en mantenimiento: el autor no prevé nuevas funciones ni nuevas PRs, aunque mantiene correcciones y dependencias.

### Chonkie (`chonkie`)

- **Repo:** https://github.com/feyninc/chonkie · MIT · nivel 2 · 51/100
- **Qué es:** Divide textos largos en fragmentos para indexarlos o recuperarlos, con estrategias simples y opciones basadas en modelos.
- **Cuándo elegirlo:** Casos: Dividir un manual por bloques para una búsqueda posterior.; Comparar fragmentos por tamaño fijo con los de una estrategia semántica.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: opcional; Entorno Python y un archivo de texto sintético..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.chonkie.ai
- **Primera prueba propuesta (no ejecutada):** Instala la variante básica y divide dos párrafos de prueba con una estrategia simple. Éxito: Obtienes fragmentos cuyo contenido y tamaño se pueden comprobar.
- **Riesgos y avisos:** El corte básico no necesita IA. Algunos fragmentadores, modelos o la API alojada tienen dependencias, credenciales y costes propios.

### agentic-rag-for-dummies (`agentic-rag-for-dummies`)

- **Repo:** https://github.com/GiovanniPasq/agentic-rag-for-dummies · MIT · nivel 2 · 47/100
- **Qué es:** Proyecto educativo de código abierto (MIT) de Giovanni Pasqualino que enseña a construir un sistema de RAG agéntico modular con LangGraph. Activo (v2.3.1), con cuaderno interactivo y proyecto ejecutable.
- **Cuándo elegirlo:** Casos: Aprender RAG por pasos; Comparar un pipeline local con otro proveedor.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; checkout; Ollama local; PDFs propios; Jupyter para notebook; hardware prerequisites; API de IA: depends; Python; checkout; Ollama local; PDFs propios; Jupyter para notebook.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -r requirements.txt` — fuente: https://github.com/GiovanniPasq/agentic-rag-for-dummies/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Coloca un PDF breve en docs y pregunta por un dato de una página concreta Éxito: Puedes ver documentos recuperados y aclarar una consulta ambigua
- **Combina con:** `langgraph` [3/py], `ollama` [8/motores], `qdrant` [6/vectores], `langfuse` [23/observabilidad], `ragas` [23/observabilidad]
- **Riesgos y avisos:** Es material de aprendizaje y referencia, no un producto para producción. No confundas instalar langchain-openai con completar todo el proyecto; revisa requisitos y la guía de ejecución de la app o notebook.

### Milvus (`milvus`)

- **Repo:** https://github.com/milvus-io/milvus · Apache-2.0 · nivel 3 · 78/100 · recomendado en «Bases y librerías vectoriales»
- **Qué es:** Base de datos vectorial de alto rendimiento y escalable, escrita en Go y C++, proyecto de la LF AI & Data Foundation bajo Apache 2.0. Madura y muy activa (v3.0.6), con versión gestionada en Zilliz Cloud.
- **Cuándo elegirlo:** Casos: Buscar productos por similitud; Indexar embeddings a gran escala.
- **Requisitos:** nivel 3: preparación pesada; Python para cliente; servidor o modo local según guía; vectores de prueba; hardware prerequisites; API de IA: no; Python para cliente; servidor o modo local según guía; vectores de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/milvus-io/milvus.git` — fuente: https://github.com/milvus-io/milvus/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una colección, inserta tres vectores y busca uno cercano Éxito: Puedes contrastar el vecino y los metadatos devueltos
- **Combina con:** `anything-llm` [8/workspaces], `lightrag` [6/rag], `llama-index` [3/py], `langchain4j` [3/ts]
- **Alternativas:** `qdrant`, `chroma`, `lancedb`, `weaviate`, `faiss`, `pgvector`
- **Riesgos y avisos:** Alternativas (elige una): qdrant, chroma, pgvector. Pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar.

### Qdrant (`qdrant`)

- **Repo:** https://github.com/qdrant/qdrant · Apache-2.0 · nivel 1 · 66/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Qdrant, motor de búsqueda vectorial y base de datos vectorial escrita en Rust, de Qdrant Solutions GmbH. Licencia Apache-2.0. Es madura (~36k estrellas, v1.20.x). También existe como servicio gestionado (Qdrant Cloud, con nivel gratuito).
- **Cuándo elegirlo:** Casos: Guardar embeddings de documentos; Combinar similitud y filtros de metadatos.
- **Requisitos:** nivel 1: preparación sencilla; Docker; vectores y metadatos de prueba; hardware prerequisites; API de IA: no; Docker; vectores y metadatos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 6333:6333 qdrant/qdrant` — fuente: https://github.com/qdrant/qdrant/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Inserta tres vectores pequeños con etiquetas y consulta el más parecido con un filtro Éxito: La búsqueda devuelve el registro esperado y respeta el filtro
- **Combina con:** `docling` [13/conversion], `activepieces` [1/motores], `llama-index` [3/py], `langchain` [3/py], `crawl4ai` [4/crawlers]
- **Alternativas:** `milvus`, `chroma`, `lancedb`, `weaviate`, `faiss`, `pgvector`
- **Riesgos y avisos:** Alternativas (elige una): milvus, chroma, pgvector, faiss. Configura autenticación (API key) antes de exponer el puerto 6333. La base vectorial almacena y busca; no genera por sí sola respuestas de un chatbot.

### Chroma (`chroma`)

- **Repo:** https://github.com/chroma-core/chroma · Apache-2.0 · nivel 1 · 64/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Infraestructura de datos de código abierto para IA (base de datos vectorial) de Chroma, con núcleo en Rust bajo Apache 2.0. Muy activa, publica versiones de PyPI y npm cada lunes; ofrece Chroma Cloud como servicio gestionado.
- **Cuándo elegirlo:** Casos: Prototipar búsqueda semántica local; Filtrar fragmentos por metadatos.
- **Requisitos:** nivel 1: preparación sencilla; Python; entorno virtual; dos documentos de prueba; hardware prerequisites; API de IA: no; Python; entorno virtual; dos documentos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install chromadb # python client` — fuente: https://github.com/chroma-core/chroma/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una colección con dos textos y consulta uno de sus temas Éxito: Se devuelve el documento relacionado y su identificador
- **Combina con:** `mempalace` [6/memoria], `anything-llm` [8/workspaces], `langchain` [3/py]
- **Alternativas:** `milvus`, `qdrant`, `lancedb`, `weaviate`, `faiss`, `pgvector`
- **Riesgos y avisos:** Alternativas (elige una): qdrant, pgvector, milvus, faiss. Distingue cliente embebido, servidor y Cloud; para guardar resultados entre reinicios configura persistencia.

### LanceDB (`lancedb`)

- **Repo:** https://github.com/lancedb/lancedb · Apache-2.0 · nivel 2 · 62/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Biblioteca de recuperación embebida de código abierto (Apache-2.0) de LanceDB Inc., con nube y edición empresarial aparte. Activa y en crecimiento.
- **Cuándo elegirlo:** Casos: añadir búsqueda vectorial a una app local sin desplegar un servidor; gestionar datos multimodales y sus embeddings con versiones para entrenamiento.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Rust, Cargo.toml, docker-compose.yml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install lancedb pandas` — fuente: https://github.com/lancedb/lancedb/blob/main/docs/web/quickstart.mdx
- **Primera prueba propuesta (no ejecutada):** Instala el SDK de Python, crea una tabla con vectores de ejemplo y lanza una búsqueda. Éxito: La búsqueda devuelve los vecinos más cercanos y la tabla queda guardada en una carpeta local.
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `duckdb` [25/datos], `polars` [25/datos]
- **Alternativas:** `milvus`, `qdrant`, `chroma`, `weaviate`, `faiss`, `pgvector`
- **Riesgos y avisos:** Alternativas (elige una): chroma.

### Weaviate (`weaviate`)

- **Repo:** https://github.com/weaviate/weaviate · BSD-3-Clause · nivel 2 · 59/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Base de datos vectorial de código abierto de Weaviate B.V. La mayor parte del repositorio es BSD-3-Clause; los archivos de `wl/` pertenecen a la edición Enterprise y requieren clave de licencia. Proyecto maduro con nube gestionada aparte.
- **Cuándo elegirlo:** Casos: montar la búsqueda semántica con filtros de un catálogo o base documental; servir la recuperación de un sistema RAG con búsqueda híbrida.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, docker-compose.yml, go.mod, pyproject.toml; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U weaviate-client` — fuente: https://github.com/weaviate/weaviate/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Weaviate con el Docker Compose del quickstart local, crea una colección y busca con el cliente de Python. Éxito: La consulta híbrida devuelve objetos ordenados por relevancia con sus propiedades.
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `ollama` [8/motores], `claude-code` [20/terminal]
- **Alternativas:** `milvus`, `qdrant`, `chroma`, `lancedb`, `faiss`, `pgvector`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): qdrant, milvus.

### turbovec (`turbovec`)

- **Repo:** https://github.com/RyanCodrai/turbovec · MIT · nivel 2 · 58/100
- **Qué es:** Índice vectorial en proceso para Python y Rust de Ryan Codrai, MIT, basado en el método TurboQuant de Google Research. Reciente y sin releases formales en GitHub.
- **Cuándo elegirlo:** Casos: Explorar índices vectoriales embebidos; Reducir memoria de una búsqueda local.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; wheel compatible o Rust y maturin para compilar; embeddings de prueba; hardware prerequisites; API de IA: no; Python; wheel compatible o Rust y maturin para compilar; embeddings de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install turbovec` — fuente: https://github.com/RyanCodrai/turbovec/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Indexa un conjunto pequeño y compara vecinos antes y después de cuantizar Éxito: Puedes medir memoria, tiempo y coincidencia en tus propios datos
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `haystack` [3/py]
- **Riesgos y avisos:** Sus cifras de rendimiento son benchmarks del autor; no predicen el comportamiento de tu máquina o corpus.

### Faiss (`faiss`)

- **Repo:** https://github.com/facebookresearch/faiss · MIT · nivel 2 · 57/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Biblioteca de Meta (Facebook Research) para búsqueda de similitud y agrupamiento de vectores densos, escrita en C++ con interfaz Python. MIT, madura y activa (v1.16.0); es una biblioteca, no un servidor de base de datos.
- **Cuándo elegirlo:** Casos: Comparar embeddings de imágenes; Experimentar con índices y compresión.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Paquete CPU o GPU compatible con tu sistema; vectores en memoria; hardware prerequisites; API de IA: no; Paquete CPU o GPU compatible con tu sistema; vectores en memoria.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/facebookresearch/faiss/blob/main/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Construye un índice con cinco vectores y consulta el más cercano a uno conocido Éxito: El resultado coincide con el vecino calculado para la muestra
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `transformers` [24/entrenamiento]
- **Alternativas:** `milvus`, `qdrant`, `chroma`, `lancedb`, `weaviate`, `pgvector`
- **Riesgos y avisos:** Alternativas (elige una): qdrant, chroma. Al no ser servidor, no trae persistencia, filtros por metadatos ni control de acceso. Es una biblioteca de índices, no una base con panel, autenticación y persistencia automática de una aplicación.

### FlagEmbedding (`flagembedding`)

- **Repo:** https://github.com/FlagOpen/FlagEmbedding · MIT · nivel 2 · 57/100
- **Qué es:** Calcula representaciones y relevancia de textos con modelos BGE para ordenar documentos según una consulta de búsqueda.
- **Cuándo elegirlo:** Casos: Encontrar el párrafo más relevante en un manual ficticio.; Comparar el orden de tres documentos antes y después de un reranker.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, setup.py; hardware model_dependent; API de IA: no; Python, dependencias del proyecto y pesos compatibles con la licencia y memoria de tu equipo..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/FlagOpen/FlagEmbedding/blob/897baa67c0ffddbfccf4e6776ff55310d67809d4/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona un modelo local pequeño en la guía y compara una consulta con tres frases. Éxito: La salida contiene puntuaciones o vectores y permite ordenar las frases de prueba.
- **Riesgos y avisos:** El código es MIT; revisa la licencia y requisitos de cada conjunto de pesos. No necesitas una API de IA para el ejemplo local.

### pgvector (`pgvector`)

- **Repo:** https://github.com/pgvector/pgvector · PostgreSQL · nivel 2 · 57/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Extensión de código abierto de PostgreSQL para búsqueda de similitud vectorial, de Andrew Kane. Se distribuye con una licencia de estilo PostgreSQL (GitHub la marca como no estándar); madura y activa (v0.8.7), sin releases en GitHub.
- **Cuándo elegirlo:** Casos: Buscar similitud junto a datos SQL; Filtrar resultados vectoriales por columnas del negocio.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; PostgreSQL; permisos de extensión; paquete o compilación adecuados al sistema; hardware prerequisites; API de IA: no; PostgreSQL; permisos de extensión; paquete o compilación adecuados al sistema.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install pgvector` — fuente: https://github.com/pgvector/pgvector/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Habilita la extensión en una base de prueba y compara tres vectores junto a sus filas Éxito: La consulta devuelve la fila más cercana usando la distancia elegida
- **Combina con:** `supabase` [22/infraestructura], `anything-llm` [8/workspaces], `librechat` [8/chats], `lightrag` [6/rag], `langchain4j` [3/ts]
- **Alternativas:** `milvus`, `qdrant`, `chroma`, `lancedb`, `weaviate`, `faiss`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): qdrant, chroma, milvus. Es una extensión de PostgreSQL; las instrucciones Windows con nmake requieren el entorno de compilación correspondiente.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-6.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Memoria, RAG y búsqueda de conocimiento», lee `docs/alexandria/categoria-6.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-6.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
