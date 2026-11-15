[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Crear y usar agentes de IA

Agentes listos para trabajar y frameworks para construir los tuyos. Un agente de código se utiliza; un framework se integra dentro de una aplicación.

86 repos · 8 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [OpenCode](../fichas/opencode.md) | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. | Depende de la ruta elegida |
| [Claude Code](../fichas/claude-code.md) | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. | API de IA opcional |
| [LangGraph](../fichas/langgraph.md) | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. | Depende de la ruta elegida |
| [Mastra](../fichas/mastra.md) | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. | Depende de la ruta elegida |
| [Sim](../fichas/sim.md) | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. | Depende de la ruta elegida |
| [OpenClaw](../fichas/openclaw.md) | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | Depende de la ruta elegida |
| [autoresearch](../fichas/autoresearch.md) | Enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. | Sin API de IA en la ruta básica |
| [Composio](../fichas/composio.md) | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | Depende de la ruta elegida |
| [E2B](../fichas/e2b.md) | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | Sin API de IA en la ruta básica |
| [MiroFish](../fichas/mirofish.md) | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | Depende de la ruta elegida |

## Secciones

- [Agentes de código (terminal e IDE)](#agentes-de-código-terminal-e-ide) — 22 repos
- [Frameworks de agentes en Python](#frameworks-de-agentes-en-python) — 18 repos
- [Frameworks en TypeScript y multi-lenguaje](#frameworks-en-typescript-y-multi-lenguaje) — 6 repos
- [Builders visuales y plataformas de agentes](#builders-visuales-y-plataformas-de-agentes) — 5 repos
- [Asistentes autónomos y equipos de agentes](#asistentes-autónomos-y-equipos-de-agentes) — 12 repos
- [Agentes de research autónomo](#agentes-de-research-autónomo) — 6 repos
- [Infraestructura: sandboxes, herramientas y protocolos](#infraestructura-sandboxes-herramientas-y-protocolos) — 12 repos
- [Simulación, evolución y debate entre modelos](#simulación-evolución-y-debate-entre-modelos) — 5 repos

## Agentes de código (terminal e IDE)

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [OpenCode](../fichas/opencode.md) | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. | quieres un agente de código abierto y multi-modelo | Depende de la ruta elegida |
| [Claude Code](../fichas/claude-code.md) | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. | quieres el agente de código más capaz para tareas largas en tu repo | API de IA opcional |
| [Codex CLI](../fichas/codex.md) | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. | usas ChatGPT u OpenAI y quieres un agente abierto en terminal | API de IA opcional |
| [Gemini CLI](../fichas/gemini-cli.md) | Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. | quieres un agente de terminal potente con cuota gratuita | Depende de la ruta elegida |
| [OpenHands](../fichas/openhands.md) | Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). | quieres un agente que "haga", no solo hable | Depende de la ruta elegida |
| [Cline](../fichas/cline.md) | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. | quieres un agente dentro de VS Code con control de cada paso | Depende de la ruta elegida |
| [Open Interpreter](../fichas/open-interpreter.md) | Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos. | quieres un agente que ejecute código usando modelos abiertos | Depende de la ruta elegida |
| [T3 Code](../fichas/t3code.md) | Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. | usas varios agentes de código y quieres controlarlos desde una UI | API de IA opcional |
| [goose](../fichas/goose.md) | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. | quieres un agente abierto con app de escritorio y MCP | API de IA opcional |
| [Aider](../fichas/aider.md) | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. | quieres un agente sencillo que trabaje con Git paso a paso | Depende de la ruta elegida |
| [Continue](../fichas/continue.md) | Agente de código open source para VS Code, JetBrains y CI, con chat, autocompletado y revisiones. | quieres autocompletado y chat en el IDE con modelos a elección | Depende de la ruta elegida |
| [openclaude](../fichas/openclaude.md) | Agente de código abierto para terminal que conecta proveedores remotos y modelos locales con herramientas y MCP. | quieres evaluar un agente de terminal compatible con varios backends | API de IA opcional |
| [SWE-agent](../fichas/swe-agent.md) | Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo. | investigas o automatizas la resolución de issues | Depende de la ruta elegida |
| [opencode](../fichas/opencode-legacy.md) | Agente de código en Go del antiguo proyecto opencode-ai, archivado y continuado bajo el nombre Crush. | necesitas estudiar la implementación histórica de OpenCode en Go | Depende de la ruta elegida |
| [MiMo-Code](../fichas/mimo-code.md) | Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente. | quieres evaluar el agente de código del ecosistema Xiaomi MiMo | Depende de la ruta elegida |
| [Open SWE](../fichas/open-swe.md) | Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería. | quieres construir el agente de código interno de tu empresa | Depende de la ruta elegida |
| [openidea](../fichas/openidea.md) | Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes. | buscas esta función: Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes. | Sin API de IA en la ruta básica |
| [OpenCursor](../fichas/opencursor.md) | Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos. | quieres evaluar un agente de código integrado en VS Code | API de IA opcional |
| [opencode-manager](../fichas/opencode-manager.md) | Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil. | buscas esta función: Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil. | Depende de la ruta elegida |
| [dsh-game-studio](../fichas/dsh-game-studio.md) | Plugin de DeepSeek Harness para preparar y probar juegos pequeños con una interfaz de trabajo dentro del agente. | buscas esta función: Plugin de DeepSeek Harness para preparar y probar juegos pequeños con una interfaz de trabajo dentro del agente. | Sin API de IA en la ruta básica |
| [dsh-ios](../fichas/dsh-ios.md) | Plugin de DeepSeek Harness para desarrollar y operar aplicaciones en simuladores iOS o dispositivos compatibles. | buscas esta función: Plugin de DeepSeek Harness para desarrollar y operar aplicaciones en simuladores iOS o dispositivos compatibles. | Sin API de IA en la ruta básica |
| [dsh-android](../fichas/dsh-android.md) | Plugin de DeepSeek Harness para operar un emulador o dispositivo Android y revisar aplicaciones desde el agente. | buscas esta función: Plugin de DeepSeek Harness para operar un emulador o dispositivo Android y revisar aplicaciones desde el agente. | Sin API de IA en la ruta básica |

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

## Asistentes autónomos y equipos de agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [OpenClaw](../fichas/openclaw.md) | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | quieres un asistente personal que actúe por tus canales de chat | Depende de la ruta elegida |
| [hermes-agent](../fichas/hermes-agent.md) | Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. | quieres agentes locales con UI y memoria persistente | Depende de la ruta elegida |
| [paperclip](../fichas/paperclip.md) | Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. | necesitas coordinar varios agentes y seguir su trabajo en un panel | API de IA opcional |
| [ruflo](../fichas/ruflo.md) | Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). | orquestas muchos agentes a escala y quieres rendimiento | API de IA opcional |
| [DeepTutor](../fichas/deeptutor.md) | Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. | quieres un tutor con IA sobre tu propio material | Depende de la ruta elegida |
| [multica](../fichas/multica.md) | Plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas"). | mezclas trabajo humano y agentes en un mismo flujo | API de IA opcional |
| [OpenDots](../fichas/opendots.md) | Plataforma de asistentes de IA persistentes que coordinan conversaciones, llamadas y servicios conectados. | buscas esta función: Plataforma de asistentes de IA persistentes que coordinan conversaciones, llamadas y servicios conectados. | API de IA necesaria |
| [Mercury Agent](../fichas/mercury-agent.md) | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. | quieres un asistente personal ligero con permisos claros | Depende de la ruta elegida |
| [social-media-agent](../fichas/social-media-agent.md) | Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas. | quieres preparar publicaciones para X o LinkedIn con una etapa de aprobación | API de IA necesaria |
| [hello-halo](../fichas/hello-halo.md) | Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API. | buscas esta función: Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API. | API de IA opcional |
| [agentes-chat](../fichas/agentes-chat.md) | Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas. | buscas esta función: Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas. | API de IA opcional |
| [fugu](../fichas/fugu.md) | Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API. | buscas esta función: Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API. | API de IA necesaria |

## Agentes de research autónomo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [autoresearch](../fichas/autoresearch.md) | Enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. | experimentas con research iterativo o quieres un punto de partida | Sin API de IA en la ruta básica |
| [deer-flow](../fichas/deer-flow.md) | Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. | quieres un orquestador completo y extensible | Depende de la ruta elegida |
| [STORM](../fichas/storm.md) | Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. | necesitas informes largos y citados sobre un tema | Depende de la ruta elegida |
| [gpt-researcher](../fichas/gpt-researcher.md) | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. | necesitas research profundo citado | Depende de la ruta elegida |
| [open_deep_research](../fichas/open-deep-research.md) | Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP. | quieres adaptar un agente de investigación construido con LangGraph | Depende de la ruta elegida |
| [local-deep-research](../fichas/local-deep-research.md) | Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. | quieres investigar con un modelo local y conservar las fuentes consultadas | Depende de la ruta elegida |

## Infraestructura: sandboxes, herramientas y protocolos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Composio](../fichas/composio.md) | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | tu agente necesita actuar en muchas apps SaaS | Depende de la ruta elegida |
| [E2B](../fichas/e2b.md) | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | tu agente ejecuta código y necesitas aislarlo | Sin API de IA en la ruta básica |
| [claude-task-master](../fichas/claude-task-master.md) | Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. | buscas esta función: Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. | API de IA necesaria |
| [agent-desktop](../fichas/agent-desktop.md) | CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. | necesitas automatizar aplicaciones nativas desde un agente | Sin API de IA en la ruta básica |
| [NemoClaw](../fichas/nemoclaw.md) | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. | quieres correr agentes potentes con aislamiento corporativo | Depende de la ruta elegida |
| [codex-chatgpt-web](../fichas/codex-chatgpt-web.md) | Integración de terceros que conecta una sesión de ChatGPT Web con el selector de modelos y herramientas de Codex. | quieres estudiar una integración entre ChatGPT Web y Codex | API: por confirmar |
| [sandbox](../fichas/sandbox.md) | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. | quieres aislar la ejecución de agentes y reproducibilidad | Sin API de IA en la ruta básica |
| [Gemini Computer Use (preview)](../fichas/computer-use-preview.md) | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. | quieres probar computer use con Gemini | API de IA necesaria |
| [NeMo-Agent-Toolkit](../fichas/nemo-agent-toolkit.md) | Toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). | trabajas con infra NVIDIA o necesitas guardrails/eval empresarial | Depende de la ruta elegida |
| [shepherd](../fichas/shepherd.md) | Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos. | buscas esta función: Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos. | Sin API de IA en la ruta básica |
| [nodeterm](../fichas/nodeterm.md) | Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. | gestionas muchas terminales o sesiones de agentes y prefieres una organización visual | Sin API de IA en la ruta básica |
| [Agent Protocol](../fichas/agent-protocol.md) | Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado. | diseñas una plataforma que sirve agentes de distintos frameworks | Sin API de IA en la ruta básica |

## Simulación, evolución y debate entre modelos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [MiroFish](../fichas/mirofish.md) | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | simulas futuros/escenarios con muchos actores | Depende de la ruta elegida |
| [llm-council](../fichas/llm-council.md) | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. | quieres consenso entre modelos o comparar proveedores | API de IA necesaria |
| [openevolve](../fichas/openevolve.md) | Agente de codificación evolutivo que optimiza algoritmos por simulación genética. | optimizas problemas algorítmicos donde cabe explorar muchas variantes | Depende de la ruta elegida |
| [hermes-agent-self-evolution](../fichas/hermes-agent-self-evolution.md) | Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA. | quieres experimentar con mejoras de Hermes medidas sobre un conjunto de evaluación | Depende de la ruta elegida |
| [jev-fraud](../fichas/jev-fraud.md) | Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude. | buscas esta función: Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude. | API de IA necesaria |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md) — Que un agente de código entienda una base de código enorme sin gastar todo su contexto.
- [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md) — Construir un frontend pulido con chat o funciones de IA integradas.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
- [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
