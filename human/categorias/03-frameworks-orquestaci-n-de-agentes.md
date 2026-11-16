[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Construir agentes y coordinar equipos de IA

Frameworks, builders visuales y experimentos de coordinación. Separa la base técnica que integras del asistente listo que utilizas para una tarea.

30 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [LangGraph](../fichas/langgraph.md) | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. | API de IA opcional |
| [Mastra](../fichas/mastra.md) | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. | Depende de la ruta elegida |
| [Sim](../fichas/sim.md) | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. | Depende de la ruta elegida |
| [MiroFish](../fichas/mirofish.md) | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | API de IA necesaria |

## Secciones

- [Frameworks de agentes en Python](#frameworks-de-agentes-en-python) — 16 repos
- [Frameworks en TypeScript y multi-lenguaje](#frameworks-en-typescript-y-multi-lenguaje) — 5 repos
- [Builders visuales y plataformas de agentes](#builders-visuales-y-plataformas-de-agentes) — 4 repos
- [Simulación, evolución y debate entre modelos](#simulación-evolución-y-debate-entre-modelos) — 5 repos

## Frameworks de agentes en Python

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [LangGraph](../fichas/langgraph.md) | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. | Tu objetivo encaja con estos ejemplos: Pausar una devolución hasta su revisión; Retomar una investigación interrumpida | API de IA opcional |
| [langchain](../fichas/langchain.md) | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). | Tu objetivo encaja con estos ejemplos: Consultar un catálogo de prueba; Responder sobre documentos propios | Depende de la ruta elegida |
| [MetaGPT](../fichas/metagpt.md) | Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. | Tu objetivo encaja con estos ejemplos: Bocetar requisitos de una app; Simular roles de un equipo de software | Depende de la ruta elegida |
| [crewAI](../fichas/crewai.md) | Framework para orquestar "crews" de agentes con roles y tareas. | Tu objetivo encaja con estos ejemplos: Preparar investigación de mercado; Separar investigación y redacción de producto | Depende de la ruta elegida |
| [LlamaIndex](../fichas/llama-index.md) | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. | Tu objetivo encaja con estos ejemplos: Consultar políticas internas; Encontrar cláusulas en contratos ficticios | Depende de la ruta elegida |
| [Agno](../fichas/agno.md) | Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. | Tu objetivo encaja con estos ejemplos: Servir un agente mediante una API; Investigar fallos mediante trazas | Depende de la ruta elegida |
| [DSPy](../fichas/dspy.md) | Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. | Tu objetivo encaja con estos ejemplos: Clasificar solicitudes de soporte; Optimizar un extractor de datos | Depende de la ruta elegida |
| [Deep Agents](../fichas/deepagents.md) | Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. | Tu objetivo encaja con estos ejemplos: Resumir documentos de proyecto; Dividir una revisión de archivos en tareas | Depende de la ruta elegida |
| [OpenAI Agents SDK](../fichas/openai-agents-python.md) | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. | Tu objetivo encaja con estos ejemplos: Enrutar consultas por departamento; Validar una respuesta antes de aceptarla | Depende de la ruta elegida |
| [smolagents](../fichas/smolagents.md) | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. | Tu objetivo encaja con estos ejemplos: Calcular indicadores de un CSV; Transformar datos consultados en un resumen | Depende de la ruta elegida |
| [Haystack](../fichas/haystack.md) | Framework de deepset para pipelines de RAG y agentes listos para producción. | Tu objetivo encaja con estos ejemplos: Responder sobre manuales propios; Comparar recuperación de dos consultas | Depende de la ruta elegida |
| [Agent Development Kit (ADK)](../fichas/adk-python.md) | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. | Tu objetivo encaja con estos ejemplos: Consultar información de negocio; Evaluar la selección de herramientas | Depende de la ruta elegida |
| [Pydantic AI](../fichas/pydantic-ai.md) | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. | Tu objetivo encaja con estos ejemplos: Extraer campos de mensajes; Validar datos generados antes de guardarlos | Depende de la ruta elegida |
| [claude-agent-sdk-python](../fichas/claude-agent-sdk-python.md) | SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia. | Tu objetivo encaja con estos ejemplos: Integrar revisión de archivos en una aplicación; Conservar sesiones de un agente propio | API de IA necesaria |
| [ag2](../fichas/ag2.md) | Framework AG2 actual para agentes y redes de colaboración en Python; AG2 Classic conserva por separado la API heredada autogen. | Tu objetivo encaja con estos ejemplos: Coordinar redactor y verificador; Incluir intervención humana en un equipo | Depende de la ruta elegida |
| [awesome-LangGraph](../fichas/awesome-langgraph.md) | Repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. | Tu objetivo encaja con estos ejemplos: Encontrar un flujo con memoria; Localizar evaluadores de agentes | Sin clave propia de API de IA en la ruta básica |

## Frameworks en TypeScript y multi-lenguaje

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Mastra](../fichas/mastra.md) | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. | Tu objetivo encaja con estos ejemplos: Añadir un agente a una app TypeScript; Pausar y reanudar un flujo de aprobación | Depende de la ruta elegida |
| [AI SDK (Vercel)](../fichas/vercel-ai.md) | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. | Tu objetivo encaja con estos ejemplos: Construir una interfaz de chat; Extraer datos tipados de un mensaje | Depende de la ruta elegida |
| [Microsoft Agent Framework](../fichas/agent-framework.md) | Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel. | Tu objetivo encaja con estos ejemplos: Migrar una prueba de Semantic Kernel; Coordinar especialistas con un flujo explícito | Depende de la ruta elegida |
| [langchain4j](../fichas/langchain4j.md) | Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM. | Tu objetivo encaja con estos ejemplos: Añadir IA a Spring Boot; Recuperar documentos desde una aplicación JVM | Depende de la ruta elegida |
| [LangGraph.js](../fichas/langgraphjs.md) | Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. | Tu objetivo encaja con estos ejemplos: Controlar aprobación de una solicitud; Reanudar un agente en una app JavaScript | API de IA opcional |

## Builders visuales y plataformas de agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Sim](../fichas/sim.md) | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. | Tu objetivo encaja con estos ejemplos: Automatizar una clasificación de mensajes; Probar un flujo con Ollama antes de usar una API | Depende de la ruta elegida |
| [AutoGPT](../fichas/autogpt.md) | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. | Tu objetivo encaja con estos ejemplos: Procesar solicitudes recurrentes; Componer una investigación con revisión humana | Depende de la ruta elegida |
| [dify](../fichas/dify.md) | Plataforma integral para construir apps de IA con backend y UI listos. | Tu objetivo encaja con estos ejemplos: Crear un asistente sobre políticas; Diseñar un workflow visual de clasificación | Depende de la ruta elegida |
| [langflow](../fichas/langflow.md) | Constructor visual de flujos LLM/agentes construido sobre LangChain. | Tu objetivo encaja con estos ejemplos: Prototipar un agente visual; Exponer un flujo como herramienta MCP | Depende de la ruta elegida |

## Simulación, evolución y debate entre modelos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [MiroFish](../fichas/mirofish.md) | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | Tu objetivo encaja con estos ejemplos: Explorar reacciones hipotéticas a un anuncio; Comparar escenarios narrativos antes de investigar datos reales | API de IA necesaria |
| [llm-council](../fichas/llm-council.md) | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. | Tu objetivo encaja con estos ejemplos: Comparar explicaciones de un concepto; Revisar opciones para una decisión técnica | API de IA necesaria |
| [openevolve](../fichas/openevolve.md) | Agente de codificación evolutivo que optimiza algoritmos por simulación genética. | Tu objetivo encaja con estos ejemplos: Optimizar una función medible; Buscar mejores reglas de ordenación | Depende de la ruta elegida |
| [hermes-agent-self-evolution](../fichas/hermes-agent-self-evolution.md) | Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA. | Tu objetivo encaja con estos ejemplos: Refinar una skill de revisión de código; Comparar instrucciones con fallos observados | API de IA necesaria |
| [jev-fraud](../fichas/jev-fraud.md) | Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude. | Tu objetivo encaja con estos ejemplos: Estudiar clasificación con escalado de casos inciertos; Comparar confianza y aciertos sobre un conjunto ficticio | API de IA opcional |

## Recetas relacionadas

- [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md) — Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.
- [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md) — Construir un frontend pulido con chat o funciones de IA integradas.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
