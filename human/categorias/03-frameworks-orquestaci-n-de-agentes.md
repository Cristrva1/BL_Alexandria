[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Construir agentes y coordinar equipos de IA

Frameworks, builders visuales y experimentos de coordinación. Separa la base técnica que integras del asistente listo que utilizas para una tarea.

34 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [LangGraph](../fichas/langgraph.md) | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. | Depende de la ruta elegida |
| [Mastra](../fichas/mastra.md) | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. | Depende de la ruta elegida |
| [Sim](../fichas/sim.md) | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. | Depende de la ruta elegida |
| [MiroFish](../fichas/mirofish.md) | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | Depende de la ruta elegida |

## Secciones

- [Frameworks de agentes en Python](#frameworks-de-agentes-en-python) — 18 repos
- [Frameworks en TypeScript y multi-lenguaje](#frameworks-en-typescript-y-multi-lenguaje) — 6 repos
- [Builders visuales y plataformas de agentes](#builders-visuales-y-plataformas-de-agentes) — 5 repos
- [Simulación, evolución y debate entre modelos](#simulación-evolución-y-debate-entre-modelos) — 5 repos

## Frameworks de agentes en Python

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [LangGraph](../fichas/langgraph.md) | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. | necesitas agentes con estado, control fino y persistencia | Depende de la ruta elegida |
| [langchain](../fichas/langchain.md) | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). | quieres la base estándar con máximas integraciones | Depende de la ruta elegida |
| [MetaGPT](../fichas/metagpt.md) | Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. | quieres estudiar un flujo multiagente basado en roles de desarrollo | Depende de la ruta elegida |
| [AutoGen](../fichas/autogen.md) | Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento. | mantienes un proyecto que ya usa AutoGen | Depende de la ruta elegida |
| [crewAI](../fichas/crewai.md) | Framework para orquestar "crews" de agentes con roles y tareas. | quieres velocidad y un modelo mental simple de "equipo" | Depende de la ruta elegida |
| [LlamaIndex](../fichas/llama-index.md) | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. | tu proyecto gira alrededor de RAG sobre tus documentos | Depende de la ruta elegida |
| [Agno](../fichas/agno.md) | Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. | quieres un framework de agentes con memoria y API lista | Depende de la ruta elegida |
| [DSPy](../fichas/dspy.md) | Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. | quieres optimizar prompts de forma sistemática con datos | Depende de la ruta elegida |
| [Deep Agents](../fichas/deepagents.md) | Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. | quieres un agente potente sin diseñar el bucle desde cero | Depende de la ruta elegida |
| [OpenAI Agents SDK](../fichas/openai-agents-python.md) | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. | usas OpenAI y quieres agentes multiagente con poco código | Depende de la ruta elegida |
| [smolagents](../fichas/smolagents.md) | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. | quieres un agente simple y transparente en Python | Depende de la ruta elegida |
| [Haystack](../fichas/haystack.md) | Framework de deepset para pipelines de RAG y agentes listos para producción. | quieres pipelines de RAG explícitos y listos para producción | Depende de la ruta elegida |
| [Agent Development Kit (ADK)](../fichas/adk-python.md) | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. | trabajas con Gemini o Google Cloud | Depende de la ruta elegida |
| [Pydantic AI](../fichas/pydantic-ai.md) | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. | quieres agentes tipados y validados en Python | Depende de la ruta elegida |
| [claude-agent-sdk-python](../fichas/claude-agent-sdk-python.md) | SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia. | buscas esta función: SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia. | API de IA opcional |
| [ag2](../fichas/ag2.md) | Framework maduro para sistemas multiagente con patrones de colaboración (heredero directo de AutoGen). | construyes multiagente serio en Python | Depende de la ruta elegida |
| [awesome-LangGraph](../fichas/awesome-langgraph.md) | Repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. | construyes con LangGraph y quieres patrones de referencia | Sin API de IA en la ruta básica |
| [LangGraph Supervisor](../fichas/langgraph-supervisor-py.md) | Librería archivada para crear un agente supervisor que coordina a otros agentes en LangGraph. | mantienes código que ya la usa | Depende de la ruta elegida |

## Frameworks en TypeScript y multi-lenguaje

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Mastra](../fichas/mastra.md) | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. | tu equipo trabaja en TypeScript y quiere agentes completos | Depende de la ruta elegida |
| [Semantic Kernel](../fichas/semantic-kernel.md) | SDK de Microsoft para integrar LLM en apps de C#, Python y Java con plugins y planificación. | tu app es .NET o Java y quieres IA integrada | Depende de la ruta elegida |
| [AI SDK (Vercel)](../fichas/vercel-ai.md) | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. | construyes una app web con IA en TypeScript | Depende de la ruta elegida |
| [Microsoft Agent Framework](../fichas/agent-framework.md) | Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel. | trabajas en el ecosistema Microsoft o .NET | Depende de la ruta elegida |
| [langchain4j](../fichas/langchain4j.md) | Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM. | tu aplicación usa Java y necesita integrar modelos o recuperación de documentos | Depende de la ruta elegida |
| [LangGraph.js](../fichas/langgraphjs.md) | Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. | quieres el modelo de LangGraph en TypeScript | Depende de la ruta elegida |

## Builders visuales y plataformas de agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Sim](../fichas/sim.md) | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. | quieres un constructor visual de agentes moderno y abierto | Depende de la ruta elegida |
| [AutoGPT](../fichas/autogpt.md) | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. | quieres agentes continuos con un editor visual propio | Depende de la ruta elegida |
| [dify](../fichas/dify.md) | Plataforma integral para construir apps de IA con backend y UI listos. | quieres una app IA completa autoalojada | Depende de la ruta elegida |
| [langflow](../fichas/langflow.md) | Constructor visual de flujos LLM/agentes construido sobre LangChain. | prefieres construir en visual sobre LangChain | Depende de la ruta elegida |
| [Flowise](../fichas/flowise.md) | Constructor visual para diseñar aplicaciones de IA conectando modelos, herramientas, memoria y fuentes de datos. | quieres un prototipo visual ya, en stack JS | Depende de la ruta elegida |

## Simulación, evolución y debate entre modelos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [MiroFish](../fichas/mirofish.md) | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | simulas futuros/escenarios con muchos actores | Depende de la ruta elegida |
| [llm-council](../fichas/llm-council.md) | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. | quieres consenso entre modelos o comparar proveedores | API de IA necesaria |
| [openevolve](../fichas/openevolve.md) | Agente de codificación evolutivo que optimiza algoritmos por simulación genética. | optimizas problemas algorítmicos donde cabe explorar muchas variantes | Depende de la ruta elegida |
| [hermes-agent-self-evolution](../fichas/hermes-agent-self-evolution.md) | Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA. | quieres experimentar con mejoras de Hermes medidas sobre un conjunto de evaluación | Depende de la ruta elegida |
| [jev-fraud](../fichas/jev-fraud.md) | Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude. | buscas esta función: Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude. | API de IA necesaria |

## Recetas relacionadas

- [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md) — Construir un frontend pulido con chat o funciones de IA integradas.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
