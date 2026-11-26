# Alexandría para agentes · Frameworks en TypeScript y multi-lenguaje

Categoría 3 «Construir agentes y coordinar equipos de IA» › subcategoría `ts`. 6 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=3&sub=ts · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `vercel-ai` | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | recomendado |
| `agent-framework` | Framework de Microsoft para agentes y workflows multiagente en Python y .NET… | 2 Intermedio | 66 | MIT (OSI permisiva) | sin grupo |
| `mastra` | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los… | 2 Intermedio | 65 | Apache-2.0 + licencia Enterprise (ee/) (open-core) | alternativa |
| `eve` | Ayuda a construir agentes con estado usando archivos de configuración… | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `langgraphjs` | Versión TypeScript de LangGraph para agentes con estado como grafos en Node o… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `langchain4j` | Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes… | 2 Intermedio | 53 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### AI SDK (Vercel) (`vercel-ai`)

- **Repo:** https://github.com/vercel/ai · Apache-2.0 · nivel 2 · 68/100 · recomendado en «Frameworks de agentes en TypeScript»
- **Qué es:** Toolkit TypeScript de Vercel (AI SDK) para construir aplicaciones y agentes con IA. El LICENSE es Apache-2.0 aunque GitHub no reconozca la licencia (NOASSERTION).
- **Cuándo elegirlo:** Casos: Construir una interfaz de chat; Extraer datos tipados de un mensaje.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node.js; proyecto TypeScript; paquete del proveedor; hardware prerequisites; API de IA: depends; Node.js; proyecto TypeScript; paquete del proveedor.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install ai` — fuente: https://github.com/vercel/ai/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade una respuesta de chat en streaming y una herramienta de consulta de estado Éxito: El texto llega por partes y la llamada devuelve el estado ficticio
- **Combina con:** `assistant-ui` [9/ia-ui], `ui` [9/componentes], `langfuse` [23/observabilidad], `ollama` [8/motores], `mem0` [6/memoria]
- **Alternativas:** `mastra`, `langgraphjs`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): langgraphjs, mastra. Ojo: algunos ejemplos del README usan modelos vía AI Gateway que requieren cuenta de Vercel. El README ofrece una skill para Claude Code; instalarla no paga la inferencia de la aplicación.

### Microsoft Agent Framework (`agent-framework`)

- **Repo:** https://github.com/microsoft/agent-framework · MIT · nivel 2 · 66/100
- **Qué es:** Framework open source (MIT) de Microsoft para construir, orquestar y desplegar agentes y workflows multiagente. Lo presentan como sucesor de AutoGen y Semantic Kernel, con guías oficiales de migración desde ambos.
- **Cuándo elegirlo:** Casos: Migrar una prueba de Semantic Kernel; Coordinar especialistas con un flujo explícito.
- **Requisitos:** nivel 2: preparación media; Python o .NET; proveedor configurado; hardware prerequisites; API de IA: depends; Python o .NET; proveedor configurado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/microsoft/agent-framework/blob/main/README.md

  ```bash
  pip install agent-framework
  # This installs the standard package set; install `agent-framework-lab` separately for experimental modules.
  # It may take a minute on first install on Windows.
  ```
- **Primera prueba propuesta (no ejecutada):** Prueba un agente y después un workflow con dos pasos y un punto de control Éxito: Puedes seguir las transiciones y recuperar el estado
- **Combina con:** `langfuse` [23/observabilidad], `copilotkit` [9/ia-ui], `ag2` [3/py], `ollama` [8/motores], `ai-agents-for-beginners` [19/guias]
- **Riesgos y avisos:** Sin alternativas declaradas en el catálogo; frameworks comparables: langgraph, crewai, openai-agents-python. La skill de construcción usa el agente; el runtime tiene autenticación y costes propios; módulos Lab son experimentales.

### Mastra (`mastra`)

- **Repo:** https://github.com/mastra-ai/mastra · Apache-2.0 + licencia Enterprise (ee/) · nivel 2 · 65/100 · alternativa en «Frameworks de agentes en TypeScript»
- **Qué es:** Framework en TypeScript para aplicaciones y agentes de IA, de Mastra. Doble licencia: Apache 2.0 para el núcleo y Mastra Enterprise License (código visible pero no libre) en los directorios `ee/`; GitHub lo marca NOASSERTION.
- **Cuándo elegirlo:** Casos: Añadir un agente a una app TypeScript; Pausar y reanudar un flujo de aprobación.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node.js y npm; proveedor elegido; hardware prerequisites; API de IA: depends; Node.js y npm; proveedor elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `npm create mastra@latest` — fuente: https://github.com/mastra-ai/mastra/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un proyecto y añade una herramienta que devuelva el precio de un producto ficticio Éxito: Puedes probar el agente y ver la herramienta usada en sus trazas
- **Combina con:** `copilotkit` [9/ia-ui], `langfuse` [23/observabilidad], `ollama` [8/motores], `composio` [22/infra], `openbot` [21/asistentes]
- **Alternativas:** `vercel-ai`, `langgraphjs`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): langgraphjs, vercel-ai. Las funciones de `ee/` requieren licencia comercial para producción. No copies el bloque de prompt del README como comando de terminal; el instalador es npm create mastra.

### Eve (`eve`)

- **Repo:** https://github.com/vercel/eve · Apache-2.0 · nivel 2 · 63/100
- **Qué es:** Ayuda a construir agentes con estado usando archivos de configuración, instrucciones y herramientas que puedes versionar con Git.
- **Cuándo elegirlo:** Casos: Probar un agente de preguntas sobre una tarea ficticia.; Versionar una habilidad de un asistente y revisar un cambio en sus instrucciones.
- **Requisitos:** nivel 2: preparación media, requiere programar con él, requiere clave de API; TypeScript, package.json; API de IA: sí; Node.js/npm y autenticación para el proveedor o AI Gateway documentado; hosting opcional..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://eve.dev/
- **Primera prueba propuesta (no ejecutada):** Lee la guía rápida, elige un proveedor y crea un agente en un proyecto temporal con texto ficticio. Éxito: La interfaz de terminal inicia y responde con el proveedor elegido.
- **Riesgos y avisos:** La licencia del framework no cubre AI Gateway, tokens ni despliegue; no asumas que tu suscripción de Codex o Claude Code concede acceso al modelo de Eve.

### LangGraph.js (`langgraphjs`)

- **Repo:** https://github.com/langchain-ai/langgraphjs · MIT · nivel 2 · 60/100 · alternativa en «Frameworks de agentes en TypeScript»
- **Qué es:** Port oficial en TypeScript de LangGraph, de LangChain Inc. (MIT), para construir agentes con estado como grafos. Es activo y maduro, y se publica como varios paquetes npm (`@langchain/langgraph`, CLI, SDK).
- **Cuándo elegirlo:** Casos: Controlar aprobación de una solicitud; Reanudar un agente en una app JavaScript.
- **Requisitos:** nivel 2: preparación media; Node.js; TypeScript; modelo solo para nodos LLM; hardware prerequisites; API de IA: opcional; Node.js; TypeScript; modelo solo para nodos LLM.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @langchain/langgraph @langchain/core` — fuente: https://github.com/langchain-ai/langgraphjs/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Monta un grafo que clasifica una solicitud y espera revisión antes de continuar Éxito: Se conserva el estado y se ve el siguiente paso
- **Combina con:** `langchain` [3/py], `langfuse` [23/observabilidad], `copilotkit` [9/ia-ui], `langgraph` [3/py], `agent-protocol` [22/infra], `social-media-agent` [21/asistentes]
- **Alternativas:** `vercel-ai`, `mastra`
- **Riesgos y avisos:** Alternativas (elige una): mastra, vercel-ai. Ollama está documentado mediante @langchain/ollama; revisa que el modelo soporte las herramientas necesarias.

### langchain4j (`langchain4j`)

- **Repo:** https://github.com/langchain4j/langchain4j · Apache-2.0 · nivel 2 · 53/100
- **Qué es:** Biblioteca open source (Apache-2.0) para integrar LLMs en aplicaciones Java y de la JVM. Pese al nombre, es un proyecto independiente de LangChain Inc. Es madura y activa (1.23.0) y se publica en Maven Central.
- **Cuándo elegirlo:** Casos: Añadir IA a Spring Boot; Recuperar documentos desde una aplicación JVM.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; JDK y Maven o Gradle según la integración; modelo; hardware prerequisites; API de IA: depends; JDK y Maven o Gradle según la integración; modelo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.langchain4j.dev/get-started
- **Primera prueba propuesta (no ejecutada):** Integra un chat que consulta un objeto de inventario de prueba en Java Éxito: El resultado devuelve el dato del objeto y puede validarse con un test
- **Combina con:** `ollama` [8/motores], `qdrant` [6/vectores], `pgvector` [6/vectores], `milvus` [6/vectores]
- **Riesgos y avisos:** Sin alternativas declaradas en el catálogo (spring-ai no figura). Qdrant, pgvector y milvus son alternativas entre sí: elige uno. Es una biblioteca Java independiente; no es un port con las mismas versiones o API que LangChain Python.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-3-ts.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Frameworks en TypeScript y multi-lenguaje», lee `docs/alexandria/categoria-3-ts.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-3-ts.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
