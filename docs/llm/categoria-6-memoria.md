# Alexandría para agentes · Memoria persistente para agentes

Categoría 6 «Memoria, RAG y búsqueda de conocimiento» › subcategoría `memoria`. 11 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=6&sub=memoria · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `mem0` | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y… | 2 Intermedio | 76 | Apache-2.0 (OSI permisiva) | recomendado |
| `claude-mem` | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes… | 1 Básico | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `openviking` | Base de contexto para agentes que organiza memoria, documentos y skills y… | 3 Avanzado | 69 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `cognee` | Plataforma de memoria para agentes que combina grafos de conocimiento y… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | alternativa |
| `mempalace` | Memoria de IA local-first con almacenamiento verbatim y backend conectable… | 2 Intermedio | 67 | MIT (OSI permisiva) | sin grupo |
| `engram` | Memoria persistente para agentes de código en un solo binario Go con SQLite… | 1 Básico | 62 | MIT (OSI permisiva) | alternativa |
| `graphiti` | Librería de Zep para construir grafos de conocimiento temporales en tiempo real… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | alternativa |
| `supermemory` | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia… | 1 Básico | 61 | MIT (OSI permisiva) | alternativa |
| `letta` | Harness de agentes con estado (Letta Code, antes MemGPT): memoria, identidad y… | 2 Intermedio | 55 | Apache-2.0 (OSI permisiva) | alternativa |
| `agentmemory` | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor… | 2 Intermedio | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `dsh-noema` | Plugin de memoria persistente para DeepSeek Harness con herramientas de… | 2 Intermedio | 47 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### mem0 (`mem0`)

- **Repo:** https://github.com/mem0ai/mem0 · Apache-2.0 · nivel 2 · 76/100 · recomendado en «Capas de memoria para apps y agentes de IA»
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

- **Repo:** https://github.com/Gentleman-Programming/engram · MIT · nivel 1 · 62/100 · alternativa en «Memoria persistente para agentes de código»
- **Qué es:** Memoria persistente para agentes de código de Gentleman-Programming, de código abierto (MIT) y financiada por donaciones, sin funciones de pago. Muy activa (v3.7.2) y parte del ecosistema Gentle-AI.
- **Cuándo elegirlo:** Casos: Recordar decisiones técnicas; Hacer una entrega de contexto entre sesiones.
- **Requisitos:** nivel 1: preparación sencilla; Binario oficial o Go; cliente MCP; directorio de memoria de prueba; hardware prerequisites; API de IA: no; Binario oficial o Go; cliente MCP; directorio de memoria de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install gentleman-programming/tap/engram` — fuente: https://github.com/Gentleman-Programming/engram/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda una decisión con su razón y recupérala por palabras clave Éxito: El registro aparece con contenido y contexto que puedes inspeccionar
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `gemini-cli` [20/terminal], `deepseek-harness` [20/terminal], `antigravity-cli` [20/terminal]
- **Alternativas:** `claude-mem`, `agentmemory`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): claude-mem, agentmemory. MCP no equivale por sí solo a captura automática; Codex añade requisitos de capacidad y sesión que debes revisar en la guía.

### Graphiti (`graphiti`)

- **Repo:** https://github.com/getzep/graphiti · Apache-2.0 · nivel 2 · 61/100 · alternativa en «Capas de memoria para apps y agentes de IA»
- **Qué es:** Framework de código abierto (Apache 2.0) de Zep para construir y consultar grafos de contexto temporales para agentes de IA. Activo (v0.31.2); Zep ofrece una plataforma empresarial gestionada sobre el mismo concepto.
- **Cuándo elegirlo:** Casos: Representar cambios de una relación comercial; Conservar hechos de conversaciones con fechas.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; Neo4j o FalkorDB; LLM y embeddings configurados; hardware prerequisites; API de IA: depends; Python; Neo4j o FalkorDB; LLM y embeddings configurados.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install graphiti-core` — fuente: https://github.com/getzep/graphiti/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade dos hechos con fechas distintas y consulta cuál era válido en cada momento Éxito: El grafo conserva relaciones temporales y sus fuentes
- **Combina con:** `claude-code` [20/terminal], `langgraph` [3/py], `mcp-neo4j` [5/servidores], `mirofish` [3/experimentos], `neo4j-mcp` [5/servidores]
- **Alternativas:** `mem0`, `cognee`, `supermemory`, `letta`, `graphrag`
- **Riesgos y avisos:** Alternativas (elige una): cognee, graphrag. Su MCP es una referencia experimental sin autenticación ni autorización: úsalo aislado para pruebas, no como despliegue público de producción.

### supermemory (`supermemory`)

- **Repo:** https://github.com/supermemoryai/supermemory · MIT · nivel 1 · 61/100 · alternativa en «Capas de memoria para apps y agentes de IA»
- **Qué es:** Motor de memoria y contexto para IA de Supermemory, que se define como laboratorio de investigación. El repositorio es MIT (servidor en versión 0.0.x) y el servicio principal es una API alojada; afirma ser el n.º 1 en LongMemEval, LoCoMo y…
- **Cuándo elegirlo:** Casos: Conservar contexto entre agentes; Buscar documentos y recuerdos de un proyecto.
- **Requisitos:** nivel 1: preparación sencilla; Node.js para ruta local; modelo elegido; cuenta para Cloud; hardware prerequisites; API de IA: depends; Node.js para ruta local; modelo elegido; cuenta para Cloud.
- **Instalación (documentada en la fuente; no ejecutada):** `npx supermemory local` — fuente: https://github.com/supermemoryai/supermemory/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda una nota de prueba y consulta su contenido desde una segunda sesión Éxito: Puedes verificar qué se almacenó y en qué instancia
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `ollama` [8/motores]
- **Alternativas:** `mem0`, `cognee`, `graphiti`, `letta`, `agentmemory`
- **Riesgos y avisos:** Alternativas (elige una): mem0, agentmemory. Con el MCP alojado los datos se procesan en sus servidores. Los plugins y MCP son vías de conexión; confirma que apuntan a la instancia local si buscas mantener el procesamiento en tu equipo.

### Letta (`letta`)

- **Repo:** https://github.com/letta-ai/letta-code · Apache-2.0 · nivel 2 · 55/100 · alternativa en «Capas de memoria para apps y agentes de IA»
- **Qué es:** Letta Code es el harness de agentes con estado de Letta (los creadores de MemGPT y de «sleep-time compute»), con licencia Apache 2.0, escrito en TypeScript.
- **Cuándo elegirlo:** Casos: Estudiar un agente con memoria persistente; Crear un asistente que conserve preferencias.
- **Requisitos:** nivel 2: preparación media; Node.js y npm, o Python 3.9+ con uv/pipx; credenciales del proveedor de modelos o cuenta de Letta; hardware prerequisites; API de IA: depends; Node.js y npm, o Python 3.9+ con uv/pipx; credenciales del proveedor de modelos o cuenta de Letta.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g @letta-ai/letta-code` — fuente: https://github.com/letta-ai/letta-code/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el enlace al código actual y crea un agente con una nota de memoria ficticia Éxito: Puedes recuperar esa nota en una conversación posterior
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `openclaw` [21/asistentes], `hermes-agent` [21/asistentes]
- **Alternativas:** `mem0`, `cognee`, `graphiti`, `supermemory`
- **Riesgos y avisos:** Alternativas (elige una): mem0, cognee. La ficha apuntaba a letta-ai/letta; se cambió a letta-ai/letta-code por decisión del propietario. Letta Cloud es el backend por defecto; equipos remotos y secretos requieren cuenta de Letta. AgentFile (.af) se eliminó.

### agentmemory (`agentmemory`)

- **Repo:** https://github.com/rohitg00/agentmemory · Apache-2.0 · nivel 2 · 52/100 · alternativa en «Memoria persistente para agentes de código»
- **Qué es:** Memoria persistente de código abierto (Apache 2.0) para sesiones de programación y agentes, de rohitg00, que se presenta como implementación del patrón «LLM Wiki» de Karpathy con puntuación de confianza, ciclo de vida, grafos y búsqueda…
- **Cuándo elegirlo:** Casos: Compartir contexto entre Claude Code y Codex; Consultar decisiones por proyecto.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node.js >=20; servidor local; hooks revisados en el cliente; hardware prerequisites; API de IA: opcional; Node.js >=20; servidor local; hooks revisados en el cliente.
- **Instalación (documentada en la fuente; no ejecutada):** `npx -y @agentmemory/agentmemory@latest` — fuente: https://github.com/rohitg00/agentmemory/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Registra una decisión ficticia y búscala desde otro cliente conectado al mismo servidor Éxito: Puedes inspeccionar el recuerdo y confirmar que ambos clientes usan la misma instancia
- **Combina con:** `claude-code` [20/terminal], `gemini-cli` [20/terminal], `hermes-agent` [21/asistentes], `deepseek-harness` [20/terminal]
- **Alternativas:** `claude-mem`, `engram`, `supermemory`
- **Riesgos y avisos:** Alternativas (elige una): engram, supermemory, claude-mem. No expongas los puertos 3111/3113 fuera de loopback sin autenticación. Las funciones y hooks dependen del runtime del cliente; la instalación de MCP no prueba que la captura automática esté activa.

### dsh-noema (`dsh-noema`)

- **Repo:** https://github.com/ZSeven-W/dsh-noema · MIT · nivel 2 · 47/100
- **Qué es:** Plugin de código abierto (MIT) de ZSeven-W que añade memoria a largo plazo a DeepSeek Harness usando Noema, un sistema de memoria local sin vectores.
- **Cuándo elegirlo:** Casos: Dar memoria a DeepSeek Harness; Importar una nota propia de otro agente.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; DeepSeek Harness compatible; plugin Noema; directorio de prueba; hardware prerequisites; API de IA: no; DeepSeek Harness compatible; plugin Noema; directorio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ZSeven-W/dsh-noema/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Guarda un recuerdo ficticio desde DSH y comprueba que puedes verlo y eliminarlo desde ajustes Éxito: El recuerdo persiste y el panel muestra su contenido
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `hermes-agent` [21/asistentes], `deepseek-harness` [20/terminal]
- **Riesgos y avisos:** Requiere DeepSeek Harness (deepseek-harness). Importar archivos de memoria de Claude, Codex o Antigravity no es una integración para ejecutar este plugin dentro de esos clientes.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-6-memoria.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Memoria persistente para agentes», lee `docs/alexandria/categoria-6-memoria.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-6-memoria.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
