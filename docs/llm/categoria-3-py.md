# Alexandría para agentes · Frameworks de agentes en Python

Categoría 3 «Construir agentes y coordinar equipos de IA» › subcategoría `py`. 21 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=3&sub=py · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `langchain` | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG… | 2 Intermedio | 80 | MIT (OSI permisiva) | recomendado |
| `crewai` | Framework para orquestar "crews" de agentes con roles y tareas. | 2 Intermedio | 72 | MIT (OSI permisiva) | alternativa |
| `langgraph` | Framework de LangChain para agentes con estado como grafos, con persistencia… | 2 Intermedio | 72 | MIT (OSI permisiva) | recomendado |
| `agentscope` | Framework de agentes en Python de origen Alibaba: agentes ReAct, multiagente… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `deepagents` | Arnés de agentes de LangChain listo para usar, con planificación, subagentes y… | 1 Básico | 70 | MIT (OSI permisiva) | alternativa |
| `dspy` | Framework de Stanford para programar modelos de lenguaje en vez de escribir… | 2 Intermedio | 67 | MIT (OSI permisiva) | sin grupo |
| `openai-agents-python` | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas… | 2 Intermedio | 67 | MIT (OSI permisiva) | alternativa |
| `adk-python` | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado… | 2 Intermedio | 66 | Apache-2.0 (OSI permisiva) | alternativa |
| `haystack` | Framework de deepset para pipelines de RAG y agentes listos para producción. | 2 Intermedio | 66 | Apache-2.0 (OSI permisiva) | alternativa |
| `pydantic-ai` | Framework de agentes del equipo de Pydantic, tipado de punta a punta y… | 2 Intermedio | 66 | MIT (OSI permisiva) | alternativa |
| `chatdev` | Plataforma multiagente sin código de OpenBMB: configura equipos de agentes por… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `ag2` | Framework AG2 actual para agentes y redes de colaboración en Python; AG2… | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `llama-index` | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes… | 2 Intermedio | 63 | MIT (OSI permisiva) | alternativa |
| `agno` | Framework y runtime de agentes en Python con memoria, conocimiento y equipos… | 1 Básico | 61 | Apache-2.0 (OSI permisiva) | alternativa |
| `metagpt` | Framework de agentes que representa roles de un equipo de software para… | 2 Intermedio | 61 | MIT (OSI permisiva) | sin grupo |
| `openmanus` | Agente general de código abierto inspirado en Manus: planifica tareas y usa… | 2 Intermedio | 61 | MIT (OSI permisiva) | sin grupo |
| `camel` | Framework multiagente de investigación para generar datos sintéticos… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | sin grupo |
| `claude-agent-sdk-python` | SDK oficial de Python para integrar el bucle de Claude Code, herramientas… | 2 Intermedio | 57 | MIT (OSI permisiva) | sin grupo |
| `semantic-router` | Clasifica consultas por intención y decide a qué función enviarlas usando… | 2 Intermedio | 55 | MIT (OSI permisiva) | sin grupo |
| `smolagents` | Librería mínima de Hugging Face para agentes que razonan escribiendo y… | 2 Intermedio | 55 | Apache-2.0 (OSI permisiva) | alternativa |
| `awesome-langgraph` | Repositorio de recursos, librerías y arquitecturas del ecosistema… | 1 Básico | 34 | CC0-1.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### langchain (`langchain`)

- **Repo:** https://github.com/langchain-ai/langchain · MIT · nivel 2 · 80/100 · recomendado en «Frameworks de RAG y orquestación de LLM»
- **Qué es:** Framework (MIT) de LangChain Inc. para construir agentes y aplicaciones con LLM encadenando componentes intercambiables e integraciones de terceros.
- **Cuándo elegirlo:** Casos: Consultar un catálogo de prueba; Responder sobre documentos propios.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python y uv; proveedor o modelo local; hardware prerequisites; API de IA: depends; Python y uv; proveedor o modelo local.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add langchain` — fuente: https://github.com/langchain-ai/langchain/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Pregunta por existencias a una herramienta con tres productos ficticios Éxito: La respuesta coincide con los datos y muestra la llamada a la herramienta
- **Combina con:** `langgraph`, `langfuse` [23/observabilidad], `qdrant` [6/vectores], `ollama` [8/motores]
- **Alternativas:** `haystack`, `llama-index`
- **Riesgos y avisos:** Alternativas (elige una): llama-index, haystack. Se quitaron langflow y litellm: no son necesarias y el README no las documenta. Instala la integración del modelo además del paquete base; compatibilidad con Anthropic API no equivale a Claude Code.

### crewAI (`crewai`)

- **Repo:** https://github.com/crewAIInc/crewAI · MIT · nivel 2 · 72/100 · alternativa en «Frameworks de agentes en Python»
- **Qué es:** Framework Python de código abierto (MIT) de CrewAI Inc. para flujos multiagente en producción, con abstracciones de alto nivel y API de bajo nivel. Es open core: CrewAI AMP Suite añade un plano de control comercial. Muy activo (1.15.41).
- **Cuándo elegirlo:** Casos: Preparar investigación de mercado; Separar investigación y redacción de producto.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python >=3.10 y <3.14; uv; proveedor o Ollama/LM Studio; hardware prerequisites; API de IA: depends; Python >=3.10 y <3.14; uv; proveedor o Ollama/LM Studio.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install crewai` — fuente: https://github.com/crewAIInc/crewAI/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una crew que investiga y luego redacta una comparación de dos productos Éxito: Puedes revisar la salida y las fuentes de cada tarea
- **Combina con:** `mem0` [6/memoria], `langfuse` [23/observabilidad], `fastmcp` [5/sdk], `500-ai-agents-projects` [19/guias], `ai-engineering-hub` [19/guias], `copilotkit` [9/ia-ui]
- **Alternativas:** `langgraph`, `deepagents`, `openai-agents-python`, `pydantic-ai`, `adk-python`, `agno`, `smolagents`, `metagpt`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): langgraph, agno, metagpt. Se quitó langchain: CrewAI no lo requiere. Claude Code y Codex tienen skills documentadas; Antigravity sigue sin confirmar para esta integración.

### LangGraph (`langgraph`)

- **Repo:** https://github.com/langchain-ai/langgraph · MIT · nivel 2 · 72/100 · recomendado en «Frameworks de agentes en Python»
- **Qué es:** Framework de orquestación de bajo nivel (MIT) de LangChain Inc. para construir, gestionar y desplegar agentes con estado y de larga duración. Es maduro y muy activo (1.2.22), y lo usan en producción empresas como Klarna, Replit o Elastic…
- **Cuándo elegirlo:** Casos: Pausar una devolución hasta su revisión; Retomar una investigación interrumpida.
- **Requisitos:** nivel 2: preparación media; Python y entorno virtual; modelo solo para nodos LLM; hardware prerequisites; API de IA: opcional; Python y entorno virtual; modelo solo para nodos LLM.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U langgraph` — fuente: https://github.com/langchain-ai/langgraph/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un grafo que guarda un pedido y se detiene para revisión humana Éxito: Puedes inspeccionar el estado y reanudar el pedido
- **Combina con:** `langchain`, `deepagents`, `langfuse` [23/observabilidad], `mem0` [6/memoria]
- **Alternativas:** `crewai`, `deepagents`, `openai-agents-python`, `pydantic-ai`, `adk-python`, `agno`, `smolagents`
- **Riesgos y avisos:** Alternativas (elige una): crewai, openai-agents-python, pydantic-ai, adk-python, agno. Ollama se configura mediante la integración LangChain; no es un plugin del editor.

### AgentScope (`agentscope`)

- **Repo:** https://github.com/agentscope-ai/agentscope · Apache-2.0 · nivel 2 · 71/100
- **Qué es:** Framework de agentes de código abierto (Apache-2.0) desarrollado por el equipo de AgentScope (origen en Alibaba/Tongyi). La versión 2.0 se presenta como lista para producción; requiere Python 3.11 o superior y tiene desarrollo muy activo.
- **Cuándo elegirlo:** Casos: construir un agente con herramientas MCP y memoria que puedas inspeccionar paso a paso; orquestar un equipo de agentes con un líder que delega tareas.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml; hardware model_dependent; API de IA: opcional; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `uv pip install agentscope` — fuente: https://github.com/agentscope-ai/agentscope/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `uv pip install agentscope` y ejecuta el ejemplo de inicio rápido con un modelo configurado. Éxito: El agente responde y usa al menos una herramienta, y puedes ver sus pasos en la salida.
- **Combina con:** `ollama` [8/motores], `fastmcp` [5/sdk], `langfuse` [23/observabilidad], `litellm` [23/serving]
- **Riesgos y avisos:** Alternativas cercanas en el catálogo: crewai, ag2, camel.

### Deep Agents (`deepagents`)

- **Repo:** https://github.com/langchain-ai/deepagents · MIT · nivel 1 · 70/100 · alternativa en «Frameworks de agentes en Python»
- **Qué es:** Harness de agentes de código abierto (MIT) de LangChain, «con pilas incluidas», que funciona sin configuración y es extensible. Activo (0.7.38), con versión JS/TS.
- **Cuándo elegirlo:** Casos: Resumir documentos de proyecto; Dividir una revisión de archivos en tareas.
- **Requisitos:** nivel 1: preparación sencilla; Python y uv; modelo con herramientas; directorio de prueba; hardware prerequisites; API de IA: depends; Python y uv; modelo con herramientas; directorio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add deepagents` — fuente: https://github.com/langchain-ai/deepagents/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Pide un plan y un informe sobre tres archivos de ejemplo Éxito: Puedes revisar el plan, las lecturas y el informe guardado
- **Combina con:** `langgraph`, `langchain`, `langfuse` [23/observabilidad], `awesome-langgraph`, `nemoclaw` [22/infra], `open-swe` [20/ingenieria]
- **Alternativas:** `langgraph`, `crewai`, `openai-agents-python`, `pydantic-ai`, `adk-python`, `agno`, `smolagents`
- **Riesgos y avisos:** Alternativa (elige una): openai-agents-python. Si da shell al agente, úsalo dentro de un sandbox. Su parecido con Claude Code no acredita el uso de la suscripción de Claude Code.

### DSPy (`dspy`)

- **Repo:** https://github.com/stanfordnlp/dspy · MIT · nivel 2 · 67/100
- **Qué es:** Framework de Stanford NLP (MIT) para «programar, no promptear» modelos de lenguaje (Declarative Self-improving Python). Maduro y activo (3.5.0).
- **Cuándo elegirlo:** Casos: Clasificar solicitudes de soporte; Optimizar un extractor de datos.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; modelo elegido; casos etiquetados; hardware prerequisites; API de IA: depends; Python; modelo elegido; casos etiquetados.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install dspy` — fuente: https://github.com/stanfordnlp/dspy/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clasifica tema y urgencia de cinco mensajes ficticios antes de optimizar Éxito: Obtienes campos estructurados y una medida de aciertos
- **Combina con:** `mlflow` [23/observabilidad], `langfuse` [23/observabilidad], `ragas` [23/observabilidad], `hermes-agent-self-evolution` [3/experimentos], `opik` [23/observabilidad]
- **Alternativas:** `promptfoo`
- **Riesgos y avisos:** Alternativa (elige una): promptfoo. Si actualizas desde versiones con LiteLLM, revisa la guía de migración. Reserva ejemplos distintos para medir el resultado de la optimización.

### OpenAI Agents SDK (`openai-agents-python`)

- **Repo:** https://github.com/openai/openai-agents-python · MIT · nivel 2 · 67/100 · alternativa en «Frameworks de agentes en Python»
- **Qué es:** SDK oficial de OpenAI (MIT) para flujos multiagente, ligero y agnóstico de proveedor. Muy activo (v0.24.0), con versión JS/TS.
- **Cuándo elegirlo:** Casos: Enrutar consultas por departamento; Validar una respuesta antes de aceptarla.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python y uv; modelo y credenciales; hardware prerequisites; API de IA: depends; Python y uv; modelo y credenciales.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/openai/openai-agents-python/blob/main/README.md

  ```bash
  uv init
  uv add openai-agents
  ```
- **Primera prueba propuesta (no ejecutada):** Deriva una consulta a un especialista de facturación ficticio Éxito: La traza muestra el traspaso y su respuesta
- **Combina con:** `litellm` [23/serving], `openai-python` [7/herramientas], `langfuse` [23/observabilidad], `fastmcp` [5/sdk], `awesome-llm-apps` [19/guias], `composio` [22/infra]
- **Alternativas:** `langgraph`, `crewai`, `deepagents`, `pydantic-ai`, `adk-python`, `agno`, `smolagents`
- **Riesgos y avisos:** Alternativas (elige una): pydantic-ai, langgraph, smolagents, deepagents, adk-python. Las trazas están activadas por defecto y van al panel de OpenAI; se…. Es una biblioteca de aplicaciones; la disponibilidad de adaptadores no confirma por sí sola una ruta local completa.

### Agent Development Kit (ADK) (`adk-python`)

- **Repo:** https://github.com/google/adk-python · Apache-2.0 · nivel 2 · 66/100 · alternativa en «Frameworks de agentes en Python»
- **Qué es:** Agent Development Kit (ADK) 2.0 de Google (Apache 2.0): framework Python «code-first» para construir, evaluar y desplegar agentes. Muy activo (v2.14.1), con versiones en Java, Kotlin, Go y TypeScript.
- **Cuándo elegirlo:** Casos: Consultar información de negocio; Evaluar la selección de herramientas.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python 3.11+; entorno virtual; modelo configurado; hardware prerequisites; API de IA: depends; Python 3.11+; entorno virtual; modelo configurado.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install google-adk` — fuente: https://github.com/google/adk-python/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta el horario de una tienda ficticia mediante una herramienta del agente Éxito: El agente devuelve el dato de la herramienta
- **Combina con:** `litellm` [23/serving], `fastmcp` [5/sdk], `langfuse` [23/observabilidad], `google-skills` [2/catalogos], `awesome-llm-apps` [19/guias], `gemini-skills` [2/catalogos]
- **Alternativas:** `langgraph`, `crewai`, `deepagents`, `openai-agents-python`, `pydantic-ai`, `agno`, `smolagents`
- **Riesgos y avisos:** Alternativas (elige una): langgraph, openai-agents-python. Se quitó gemini-cli: no es una integración. Que Google publique ADK no lo convierte en configuración de Antigravity.

### Haystack (`haystack`)

- **Repo:** https://github.com/deepset-ai/haystack · Apache-2.0 · nivel 2 · 66/100 · alternativa en «Frameworks de RAG y orquestación de LLM»
- **Qué es:** Framework de orquestación de IA de código abierto (Apache 2.0) de deepset para aplicaciones LLM en producción con Python. Maduro y activo (v3.5.0); deepset ofrece soporte y plataforma comerciales (Haystack Enterprise).
- **Cuándo elegirlo:** Casos: Responder sobre manuales propios; Comparar recuperación de dos consultas.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; documentos; componentes de recuperación y generación; hardware prerequisites; API de IA: depends; Python; documentos; componentes de recuperación y generación.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install haystack-ai` — fuente: https://github.com/deepset-ai/haystack/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Recupera un párrafo de un manual antes de generar la respuesta Éxito: Puedes inspeccionar el párrafo y contrastar la salida
- **Combina con:** `qdrant` [6/vectores], `docling` [13/conversion], `ollama` [8/motores], `langfuse` [23/observabilidad], `turbovec` [6/vectores]
- **Alternativas:** `langchain`, `llama-index`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): llama-index, langchain. Desactiva la telemetría si tu política lo exige. El MCP se publica mediante el proyecto compañero Hayhooks y requiere configurar y servir pipelines; sus modelos y claves se eligen aparte.

### Pydantic AI (`pydantic-ai`)

- **Repo:** https://github.com/pydantic/pydantic-ai · MIT · nivel 2 · 66/100 · alternativa en «Frameworks de agentes en Python»
- **Qué es:** SDK de IA para Python (MIT) del equipo de Pydantic: un bucle de agente tipado y extensible. Muy activo (v2.68.0). Se apoya en productos comerciales de la misma empresa (Logfire, AI Gateway).
- **Cuándo elegirlo:** Casos: Extraer campos de mensajes; Validar datos generados antes de guardarlos.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python y uv; esquema de salida; modelo; hardware prerequisites; API de IA: depends; Python y uv; esquema de salida; modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add pydantic-ai` — fuente: https://github.com/pydantic/pydantic-ai/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Extrae nombre, importe y moneda de una factura ficticia Éxito: El resultado respeta los tipos o informa del fallo de validación
- **Combina con:** `langfuse` [23/observabilidad], `fastmcp` [5/sdk], `ollama` [8/motores], `browser-use` [32/agentes-web], `loguru` [23/observabilidad], `mcp-python-sdk` [5/sdk]
- **Alternativas:** `langgraph`, `crewai`, `deepagents`, `openai-agents-python`, `adk-python`, `agno`, `smolagents`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): openai-agents-python, smolagents, langgraph. Empieza con el paquete base; el harness de programación es un componente adicional.

### ChatDev (`chatdev`)

- **Repo:** https://github.com/OpenBMB/ChatDev · Apache-2.0 · nivel 2 · 64/100
- **Qué es:** Proyecto de investigación y plataforma de OpenBMB (Tsinghua) bajo Apache-2.0. ChatDev 2.0 (DevAll), publicada en enero de 2026, es una plataforma multiagente sin código; la versión 1.x, la «empresa de software virtual», se conserva en una…
- **Cuándo elegirlo:** Casos: prototipar una pequeña aplicación con agentes que actúan como roles de un equipo; estudiar patrones de colaboración multiagente de los artículos del proyecto. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose, requiere clave de API; Python, Dockerfile, package.json, pyproject.toml, requirements.txt; API de IA: sí.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up --build` — fuente: https://github.com/OpenBMB/ChatDev/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca la aplicación con `docker compose up --build`, configura una clave de modelo y ejecuta un flujo de ejemplo. Éxito: El flujo termina y muestra los mensajes entre agentes y el artefacto generado.
- **Combina con:** `blender` [26/creacion-3d], `blender-mcp` [5/servidores], `litellm` [23/serving]
- **Riesgos y avisos:** El código generado por agentes debe revisarse antes de usarse; ejecútalo en contenedores.

### ag2 (`ag2`)

- **Repo:** https://github.com/ag2ai/ag2 · Apache-2.0 · nivel 2 · 63/100
- **Qué es:** AG2 (Apache 2.0), «AgentOS de código abierto» surgido de AutoGen y mantenido por un grupo de voluntarios de varias organizaciones (administradores: Chi Wang y Qingyun Wu).
- **Cuándo elegirlo:** Casos: Coordinar redactor y verificador; Incluir intervención humana en un equipo.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python 3.11+; extra del proveedor elegido; hardware prerequisites; API de IA: depends; Python 3.11+; extra del proveedor elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install ag2[openai]` — fuente: https://github.com/ag2ai/ag2/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Haz que un agente resuma una conversación y otro revise las omisiones Éxito: Se registran los intercambios usando import ag2
- **Combina con:** `ollama` [8/motores], `langfuse` [23/observabilidad], `agent-framework` [3/ts]
- **Riesgos y avisos:** Se quitó langchain porque no hay integración documentada. Si tu código usa `import autogen`, instala ag2-classic. AG2 v1 no sustituye directamente Classic: ConversableAgent y GroupChat siguen en ag2-classic con import autogen.

### LlamaIndex (`llama-index`)

- **Repo:** https://github.com/run-llama/llama_index · MIT · nivel 2 · 63/100 · alternativa en «Frameworks de RAG y orquestación de LLM»
- **Qué es:** Framework de código abierto (MIT) de LlamaIndex (run-llama) para aplicaciones RAG y agentes sobre datos propios. Activo (v0.14.26), pero el README avisa de que la empresa ha desplazado su foco principal a LlamaParse, su plataforma…
- **Cuándo elegirlo:** Casos: Consultar políticas internas; Encontrar cláusulas en contratos ficticios.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; dos documentos; modelo generativo y embeddings; hardware prerequisites; API de IA: depends; Python; dos documentos; modelo generativo y embeddings.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/run-llama/llama_index/blob/main/README.md

  ```sh
  # custom selection of integrations to work with core
  pip install llama-index-core
  pip install llama-index-llms-openai
  pip install llama-index-llms-ollama
  pip install llama-index-embeddings-huggingface
  ```
- **Primera prueba propuesta (no ejecutada):** Pregunta por una cifra que solo aparece en uno de tus dos documentos Éxito: Se recupera el documento correcto y puedes contrastar el fragmento
- **Combina con:** `qdrant` [6/vectores], `docling` [13/conversion], `ragas` [23/observabilidad], `ollama` [8/motores]
- **Alternativas:** `langchain`, `haystack`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): haystack, langchain. Ten en cuenta el cambio de foco de la empresa al planificar proyectos largos. Configura también embeddings locales si quieres que todo el procesamiento sea local.

### Agno (`agno`)

- **Repo:** https://github.com/agno-agi/agno · Apache-2.0 · nivel 1 · 61/100 · alternativa en «Frameworks de agentes en Python»
- **Qué es:** Plataforma de agentes «autogestionada» (Apache 2.0) de Agno. Muy activa (v3.2.0).
- **Cuándo elegirlo:** Casos: Servir un agente mediante una API; Investigar fallos mediante trazas.
- **Requisitos:** nivel 1: preparación sencilla; Python; plantilla; PostgreSQL; proveedor de modelos; hardware prerequisites; API de IA: depends; Python; plantilla; PostgreSQL; proveedor de modelos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.agno.com/agent-platform/overview
- **Primera prueba propuesta (no ejecutada):** Conecta el MCP de documentación y pide que explique el montaje de la plataforma local Éxito: El agente consulta la guía y enumera servicios y credenciales necesarios
- **Combina con:** `claude-agent-sdk-python`, `qdrant` [6/vectores], `mem0` [6/memoria], `500-ai-agents-projects` [19/guias]
- **Alternativas:** `langgraph`, `crewai`, `deepagents`, `openai-agents-python`, `pydantic-ai`, `adk-python`, `smolagents`
- **Riesgos y avisos:** Alternativas (elige una): crewai, langgraph. AgentOS UI es un servicio alojado por Agno: revisa qué datos ve. MCP HTTP accesible desde los tres clientes; no significa que sus planes paguen los agentes desplegados.

### MetaGPT (`metagpt`)

- **Repo:** https://github.com/FoundationAgents/MetaGPT · MIT · nivel 2 · 61/100
- **Qué es:** Framework multiagente open source (MIT) de FoundationAgents (antes geekan/MetaGPT) que asigna roles a LLMs para que colaboren como un equipo. Tiene mucha repercusión (~71k estrellas), pero poca actividad: la última release es la v0.8.1 de…
- **Cuándo elegirlo:** Casos: Bocetar requisitos de una app; Simular roles de un equipo de software.
- **Requisitos:** nivel 2: preparación media; Python según guía estable; proveedor o Ollama; directorio de salida de prueba; hardware prerequisites; API de IA: depends; Python según guía estable; proveedor o Ollama; directorio de salida de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/FoundationAgents/MetaGPT/blob/main/README.md

  ```bash
  pip install --upgrade metagpt
  # or `pip install --upgrade git+https://github.com/geekan/MetaGPT.git`
  # or `git clone https://github.com/geekan/MetaGPT && cd MetaGPT && pip install --upgrade -e .`
  ```
- **Primera prueba propuesta (no ejecutada):** Pide el diseño de una lista de tareas mínima y revisa requisitos y estructura antes del código Éxito: Obtienes artefactos separados que puedes revisar y corregir
- **Combina con:** `ollama` [8/motores], `e2b` [22/infra], `claude-code` [20/terminal]
- **Alternativas:** `crewai`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): crewai. Mantenimiento bajo: sin releases desde 2024. Los artefactos generados no acreditan una aplicación lista ni sustituyen pruebas y revisión.

### OpenManus (`openmanus`)

- **Repo:** https://github.com/FoundationAgents/OpenManus · MIT · nivel 2 · 61/100
- **Qué es:** Implementación abierta (MIT) de un agente general al estilo Manus, creada por miembros de MetaGPT y la comunidad FoundationAgents. Los autores la describen como una implementación sencilla; ritmo de cambios alto y sin versiones estables…
- **Cuándo elegirlo:** Casos: delegar una investigación web que termine en un informe guardado en disco; experimentar con un agente general en local antes de elegir un framework. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Python, Dockerfile, requirements.txt, setup.py; API de IA: sí.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/FoundationAgents/OpenManus.git` — fuente: https://github.com/FoundationAgents/OpenManus/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea el entorno con uv según el README, configura la clave del modelo en config.toml y lanza una tarea pequeña de búsqueda. Éxito: El agente completa los pasos visibles en consola y deja el resultado en el espacio de trabajo.
- **Combina con:** `browser-use` [32/agentes-web], `playwright` [32/bibliotecas], `litellm` [23/serving]
- **Riesgos y avisos:** El agente ejecuta código y navega por sí mismo: úsalo en un entorno aislado y con datos de prueba.

### CAMEL (`camel`)

- **Repo:** https://github.com/camel-ai/camel · Apache-2.0 · nivel 2 · 60/100
- **Qué es:** Framework multiagente de código abierto (Apache-2.0) de la comunidad CAMEL-AI, nacido del artículo «CAMEL: Communicative Agents» (2023). Orientado a investigación sobre las leyes de escala de los agentes; desarrollo activo.
- **Cuándo elegirlo:** Casos: generar datos sintéticos con agentes que dialogan en roles; montar un experimento de simulación con muchos agentes y medir su comportamiento.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; hardware model_dependent; API de IA: opcional; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install camel-ai` — fuente: https://github.com/camel-ai/camel/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install camel-ai`, configura la clave de un modelo y ejecuta el ejemplo de ChatAgent. Éxito: El agente responde y el script termina sin errores mostrando la conversación.
- **Combina con:** `ollama` [8/motores], `qdrant` [6/vectores], `firecrawl` [4/crawlers], `vllm` [23/serving]
- **Riesgos y avisos:** Alternativas cercanas en el catálogo: crewai, ag2, agentscope.

### claude-agent-sdk-python (`claude-agent-sdk-python`)

- **Repo:** https://github.com/anthropics/claude-agent-sdk-python · MIT · nivel 2 · 57/100
- **Qué es:** SDK oficial de Anthropic (MIT) para usar desde Python el bucle de agente de Claude Code. Es muy activo (v0.2.182), con publicaciones casi a diario, pero sigue en 0.x y su API puede cambiar.
- **Cuándo elegirlo:** Casos: Integrar revisión de archivos en una aplicación; Conservar sesiones de un agente propio.
- **Requisitos:** nivel 2: preparación media, requiere programar con él, requiere clave de API; Python; credenciales API de Anthropic o proveedor admitido; directorio de prueba; hardware prerequisites; API de IA: sí; Python; credenciales API de Anthropic o proveedor admitido; directorio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install claude-agent-sdk` — fuente: https://github.com/anthropics/claude-agent-sdk-python/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un agente con permiso de lectura y pídele localizar un fallo en un archivo ficticio Éxito: Puedes ver herramientas llamadas y contrastar el fallo antes de permitir ediciones
- **Combina con:** `claude-code` [20/terminal], `fastmcp` [5/sdk], `langfuse` [23/observabilidad], `e2b` [22/infra], `agno`, `pageindex` [6/rag]
- **Riesgos y avisos:** Sin alternativas declaradas; comparable a openai-agents-python (otro proveedor). Integra el motor Claude Code; la guía limita ofrecer login o límites claude.ai a terceros sin autorización previa.

### Semantic Router (`semantic-router`)

- **Repo:** https://github.com/aurelio-labs/semantic-router · MIT · nivel 2 · 55/100
- **Qué es:** Clasifica consultas por intención y decide a qué función enviarlas usando similitud entre ejemplos y texto de entrada.
- **Cuándo elegirlo:** Casos: Rutar consultas ficticias a preguntas frecuentes o ayuda técnica.; Separar solicitudes sobre facturación de solicitudes de soporte.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Makefile, compose.yaml, pyproject.toml; API de IA: opcional; Python, una versión actual de la rama 1.x y un codificador compatible..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.aurelio.ai/docs/semantic-router/v1/get-started/introduction
- **Primera prueba propuesta (no ejecutada):** Crea dos rutas con frases ficticias y usa un codificador local documentado. Éxito: Frases similares llegan a la ruta esperada y puedes revisar las que no encajan.
- **Riesgos y avisos:** El aviso por una dependencia comprometida afecta a versiones 0.1.8 a anteriores a 0.1.15. Evita esas versiones y revisa las dependencias fijadas.

### smolagents (`smolagents`)

- **Repo:** https://github.com/huggingface/smolagents · Apache-2.0 · nivel 2 · 55/100 · alternativa en «Frameworks de agentes en Python»
- **Qué es:** Biblioteca minimalista de agentes de Hugging Face (Apache 2.0): la lógica principal cabe en unas 1.000 líneas. Activa (v1.26.0).
- **Cuándo elegirlo:** Casos: Calcular indicadores de un CSV; Transformar datos consultados en un resumen.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; modelo; ejecutor aislado; hardware prerequisites; API de IA: depends; Python; modelo; ejecutor aislado.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "smolagents[toolkit]"` — fuente: https://github.com/huggingface/smolagents/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Calcula el total y promedio de cinco importes ficticios y revisa el código generado Éxito: Los resultados coinciden con los números de entrada
- **Combina con:** `e2b` [22/infra], `transformers` [24/entrenamiento], `litellm` [23/serving], `langfuse` [23/observabilidad], `agents-course` [19/guias]
- **Alternativas:** `langgraph`, `crewai`, `deepagents`, `openai-agents-python`, `pydantic-ai`, `adk-python`, `agno`
- **Riesgos y avisos:** Alternativas (elige una): pydantic-ai, openai-agents-python. No ejecutes CodeAgent sin sandbox con datos o credenciales reales. El agente ejecuta código: usa el aislamiento documentado y archivos de prueba.

### awesome-LangGraph (`awesome-langgraph`)

- **Repo:** https://github.com/vonzosten/awesome-LangGraph · CC0-1.0 · nivel 1 · 34/100
- **Qué es:** Índice curado (CC0) de vonzosten sobre el ecosistema LangChain y LangGraph: frameworks, plantillas y proyectos reales. Activo; último cambio en octubre de 2026.
- **Cuándo elegirlo:** Casos: Encontrar un flujo con memoria; Localizar evaluadores de agentes.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; necesidad concreta; hardware prerequisites; API de IA: no; Navegador; necesidad concreta.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/vonzosten/awesome-LangGraph/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Busca una plantilla de aprobación humana y contrasta su versión con las guías oficiales Éxito: Tienes un candidato y sabes qué aporta al flujo
- **Combina con:** `langgraph`, `langchain`, `deepagents`
- **Riesgos y avisos:** Todavía recomienda langchain-mcp-adapters, archivado y retirado del catálogo (MCP pasó al paquete principal de LangChain): desactualización detectada. Las integraciones de los enlaces no acreditan compatibilidad del directorio completo.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-3-py.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Frameworks de agentes en Python», lee `docs/alexandria/categoria-3-py.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-3-py.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
