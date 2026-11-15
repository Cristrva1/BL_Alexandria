[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 2. Skills, Prompts & Guías de Agente](02-skills-prompts-gu-as-de-agente.md) · [4. Scraping, Búsqueda & Research Web ➡️](04-scraping-b-squeda-research-web.md)

# 🕸️ 3. Frameworks & Orquestación de Agentes

> Agentes de código, frameworks multiagente en Python y TypeScript, builders visuales, asistentes autónomos, research e infraestructura.

**73 repos** · 8 subcategorías · ⭐ 4.1M estrellas en total · 🆕 73 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [OpenCode](../fichas/opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. | `curl -fsSL https://opencode.ai/install \| bash` |
| [Claude Code](../fichas/claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. | `curl -fsSL https://claude.ai/install.sh \| bash` |
| [LangGraph](../fichas/langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. | `pip install -U langgraph` |
| [Mastra](../fichas/mastra.md) | 29.5k | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. | `npm create mastra@latest` |
| [Sim](../fichas/sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. | `npx simstudio` |
| [OpenClaw](../fichas/openclaw.md) | 394k | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | `npm install -g openclaw@latest` |
| [autoresearch](../fichas/autoresearch.md) | 100k | Enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. | `git clone` |
| [Composio](../fichas/composio.md) | 31.1k | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | `pip install composio` |
| [E2B](../fichas/e2b.md) | 14.9k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | `pip install e2b-code-interpreter` |
| [MiroFish](../fichas/mirofish.md) | 85.6k | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | `git clone` |

## 🧭 Subcategorías

- [Agentes de código (terminal e IDE)](#agentes-de-código-terminal-e-ide) — 17 repos
- [Frameworks de agentes en Python](#frameworks-de-agentes-en-python) — 17 repos
- [Frameworks en TypeScript y multi-lenguaje](#frameworks-en-typescript-y-multi-lenguaje) — 6 repos
- [Builders visuales y plataformas de agentes](#builders-visuales-y-plataformas-de-agentes) — 5 repos
- [Asistentes autónomos y equipos de agentes](#asistentes-autónomos-y-equipos-de-agentes) — 8 repos
- [Agentes de research autónomo](#agentes-de-research-autónomo) — 6 repos
- [Infraestructura: sandboxes, herramientas y protocolos](#infraestructura-sandboxes-herramientas-y-protocolos) — 10 repos
- [Simulación, evolución y debate entre modelos](#simulación-evolución-y-debate-entre-modelos) — 4 repos

## Agentes de código (terminal e IDE)

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [OpenCode](../fichas/opencode.md) 🆕 | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. | quieres un agente de código abierto y multi-modelo | 🟢 |
| ⭐ [Claude Code](../fichas/claude-code.md) 🆕 | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. | quieres el agente de código más capaz para tareas largas en tu repo | 🟢 |
| [Codex CLI](../fichas/codex.md) 🆕 | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. | usas ChatGPT u OpenAI y quieres un agente abierto en terminal | 🟢 |
| [Gemini CLI](../fichas/gemini-cli.md) 🆕 | 109k | Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. | quieres un agente de terminal potente con cuota gratuita | 🟢 |
| [OpenHands](../fichas/openhands.md) 🆕 | 93.5k | Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). | quieres un agente que "haga", no solo hable | 🟡 |
| [Cline](../fichas/cline.md) 🆕 | 71.6k | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. | quieres un agente dentro de VS Code con control de cada paso | 🟢 |
| [Open Interpreter](../fichas/open-interpreter.md) 🆕 | 68.9k | Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos. | quieres un agente que ejecute código usando modelos abiertos | 🟢 |
| [T3 Code](../fichas/t3code.md) 🆕 | 60.6k | Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. | usas varios agentes de código y quieres controlarlos desde una UI | 🟢 |
| [goose](../fichas/goose.md) 🆕 | 56.6k | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. | quieres un agente abierto con app de escritorio y MCP | 🟢 |
| [Aider](../fichas/aider.md) 🆕 | 50.1k | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. | quieres un agente sencillo que trabaje con Git paso a paso | 🟢 |
| [Continue](../fichas/continue.md) 🆕 | 36.5k | Agente de código open source para VS Code, JetBrains y CI, con chat, autocompletado y revisiones. | quieres autocompletado y chat en el IDE con modelos a elección | 🟢 |
| [openclaude](../fichas/openclaude.md) 🆕 | 34.4k | Agente de código abierto para terminal que conecta proveedores remotos y modelos locales con herramientas y MCP. | quieres evaluar un agente de terminal compatible con varios backends | 🟡 |
| [SWE-agent](../fichas/swe-agent.md) 🆕 | 20.8k | Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo. | investigas o automatizas la resolución de issues | 🟡 |
| [opencode](../fichas/opencode-legacy.md) 🆕 | 13.9k | Agente de código en Go del antiguo proyecto opencode-ai, archivado y continuado bajo el nombre Crush. | necesitas estudiar la implementación histórica de OpenCode en Go | 🟡 |
| [MiMo-Code](../fichas/mimo-code.md) 🆕 | 13.8k | Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente. | quieres evaluar el agente de código del ecosistema Xiaomi MiMo | 🟡 |
| [Open SWE](../fichas/open-swe.md) 🆕 | 11.2k | Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería. | quieres construir el agente de código interno de tu empresa | 🟡 |
| [OpenCursor](../fichas/opencursor.md) 🆕 | 6.1k | Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos. | quieres evaluar un agente de código integrado en VS Code | 🟡 |

## Frameworks de agentes en Python

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [LangGraph](../fichas/langgraph.md) 🆕 | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. | necesitas agentes con estado, control fino y persistencia | 🟡 |
| [langchain](../fichas/langchain.md) 🆕 | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). | quieres la base estándar con máximas integraciones | 🟡 |
| [MetaGPT](../fichas/metagpt.md) 🆕 | 71.3k | Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. | quieres estudiar un flujo multiagente basado en roles de desarrollo | 🟡 |
| [AutoGen](../fichas/autogen.md) 🆕 | 61.8k | Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento. | mantienes un proyecto que ya usa AutoGen | 🟡 |
| [crewAI](../fichas/crewai.md) 🆕 | 60.9k | Framework para orquestar "crews" de agentes con roles y tareas. | quieres velocidad y un modelo mental simple de "equipo" | 🟢 |
| [LlamaIndex](../fichas/llama-index.md) 🆕 | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. | tu proyecto gira alrededor de RAG sobre tus documentos | 🟢 |
| [Agno](../fichas/agno.md) 🆕 | 43.2k | Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. | quieres un framework de agentes con memoria y API lista | 🟢 |
| [DSPy](../fichas/dspy.md) 🆕 | 39.1k | Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. | quieres optimizar prompts de forma sistemática con datos | 🟡 |
| [Deep Agents](../fichas/deepagents.md) 🆕 | 31.3k | Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. | quieres un agente potente sin diseñar el bucle desde cero | 🟢 |
| [OpenAI Agents SDK](../fichas/openai-agents-python.md) 🆕 | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. | usas OpenAI y quieres agentes multiagente con poco código | 🟢 |
| [smolagents](../fichas/smolagents.md) 🆕 | 30.4k | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. | quieres un agente simple y transparente en Python | 🟢 |
| [Haystack](../fichas/haystack.md) 🆕 | 27k | Framework de deepset para pipelines de RAG y agentes listos para producción. | quieres pipelines de RAG explícitos y listos para producción | 🟡 |
| [Agent Development Kit (ADK)](../fichas/adk-python.md) 🆕 | 22.2k | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. | trabajas con Gemini o Google Cloud | 🟢 |
| [Pydantic AI](../fichas/pydantic-ai.md) 🆕 | 21.2k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. | quieres agentes tipados y validados en Python | 🟢 |
| [ag2](../fichas/ag2.md) 🆕 | 5.1k | Framework maduro para sistemas multiagente con patrones de colaboración (heredero directo de AutoGen). | construyes multiagente serio en Python | 🟡 |
| [awesome-LangGraph](../fichas/awesome-langgraph.md) 🆕 | 2k | Repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. | construyes con LangGraph y quieres patrones de referencia | 🟢 |
| [LangGraph Supervisor](../fichas/langgraph-supervisor-py.md) 🆕 | 1.7k | Librería archivada para crear un agente supervisor que coordina a otros agentes en LangGraph. | mantienes código que ya la usa | 🟢 |

## Frameworks en TypeScript y multi-lenguaje

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Mastra](../fichas/mastra.md) 🆕 | 29.5k | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. | tu equipo trabaja en TypeScript y quiere agentes completos | 🟢 |
| [Semantic Kernel](../fichas/semantic-kernel.md) 🆕 | 28.8k | SDK de Microsoft para integrar LLM en apps de C#, Python y Java con plugins y planificación. | tu app es .NET o Java y quieres IA integrada | 🟡 |
| [AI SDK (Vercel)](../fichas/vercel-ai.md) 🆕 | 28k | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. | construyes una app web con IA en TypeScript | 🟢 |
| [Microsoft Agent Framework](../fichas/agent-framework.md) 🆕 | 14.7k | Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel. | trabajas en el ecosistema Microsoft o .NET | 🟡 |
| [langchain4j](../fichas/langchain4j.md) 🆕 | 13.4k | Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM. | tu aplicación usa Java y necesita integrar modelos o recuperación de documentos | 🟡 |
| [LangGraph.js](../fichas/langgraphjs.md) 🆕 | 3.4k | Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. | quieres el modelo de LangGraph en TypeScript | 🟡 |

## Builders visuales y plataformas de agentes

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Sim](../fichas/sim.md) 🆕 | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. | quieres un constructor visual de agentes moderno y abierto | 🟡 |
| [AutoGPT](../fichas/autogpt.md) 🆕 | 188k | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. | quieres agentes continuos con un editor visual propio | 🔴 |
| [dify](../fichas/dify.md) 🆕 | 161k | Plataforma integral para construir apps de IA con backend y UI listos. | quieres una app IA completa autoalojada | 🟡 |
| [langflow](../fichas/langflow.md) 🆕 | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. | prefieres construir en visual sobre LangChain | 🟡 |
| [Flowise](../fichas/flowise.md) 🆕 | 55.6k | Builder visual drag-and-drop para pipelines LLM. | quieres un prototipo visual ya, en stack JS | 🟢 |

## Asistentes autónomos y equipos de agentes

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [OpenClaw](../fichas/openclaw.md) 🆕 | 394k | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | quieres un asistente personal que actúe por tus canales de chat | 🟡 |
| [hermes-agent](../fichas/hermes-agent.md) 🆕 | 263k | Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. | quieres agentes locales con UI y memoria persistente | 🟡 |
| [paperclip](../fichas/paperclip.md) 🆕 | 114k | Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. | necesitas coordinar varios agentes y seguir su trabajo en un panel | 🔴 |
| [ruflo](../fichas/ruflo.md) 🆕 | 81.7k | Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). | orquestas muchos agentes a escala y quieres rendimiento | 🔴 |
| [DeepTutor](../fichas/deeptutor.md) 🆕 | 59.2k | Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. | quieres un tutor con IA sobre tu propio material | 🟡 |
| [multica](../fichas/multica.md) 🆕 | 56.1k | Plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas"). | mezclas trabajo humano y agentes en un mismo flujo | 🟡 |
| [Mercury Agent](../fichas/mercury-agent.md) 🆕 | 3.9k | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. | quieres un asistente personal ligero con permisos claros | 🟢 |
| [social-media-agent](../fichas/social-media-agent.md) 🆕 | 3k | Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas. | quieres preparar publicaciones para X o LinkedIn con una etapa de aprobación | 🟡 |

## Agentes de research autónomo

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [autoresearch](../fichas/autoresearch.md) 🆕 | 100k | Enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. | experimentas con research iterativo o quieres un punto de partida | 🟡 |
| [deer-flow](../fichas/deer-flow.md) 🆕 | 85.3k | Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. | quieres un orquestador completo y extensible | 🟡 |
| [STORM](../fichas/storm.md) 🆕 | 31.9k | Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. | necesitas informes largos y citados sobre un tema | 🟡 |
| [gpt-researcher](../fichas/gpt-researcher.md) 🆕 | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. | necesitas research profundo citado | 🟡 |
| [open_deep_research](../fichas/open-deep-research.md) 🆕 | 12.7k | Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP. | quieres adaptar un agente de investigación construido con LangGraph | 🟡 |
| [local-deep-research](../fichas/local-deep-research.md) 🆕 | 9.6k | Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. | quieres investigar con un modelo local y conservar las fuentes consultadas | 🟡 |

## Infraestructura: sandboxes, herramientas y protocolos

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Composio](../fichas/composio.md) 🆕 | 31.1k | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | tu agente necesita actuar en muchas apps SaaS | 🟢 |
| ⭐ [E2B](../fichas/e2b.md) 🆕 | 14.9k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | tu agente ejecuta código y necesitas aislarlo | 🟢 |
| [agent-desktop](../fichas/agent-desktop.md) 🆕 | 23.8k | CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. | necesitas automatizar aplicaciones nativas desde un agente | 🟡 |
| [NemoClaw](../fichas/nemoclaw.md) 🆕 | 23k | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. | quieres correr agentes potentes con aislamiento corporativo | 🔴 |
| [codex-chatgpt-web](../fichas/codex-chatgpt-web.md) 🆕 | 15.7k | Integración de terceros que conecta una sesión de ChatGPT Web con el selector de modelos y herramientas de Codex. | quieres estudiar una integración entre ChatGPT Web y Codex | 🟡 |
| [sandbox](../fichas/sandbox.md) 🆕 | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. | quieres aislar la ejecución de agentes y reproducibilidad | 🟡 |
| [Gemini Computer Use (preview)](../fichas/computer-use-preview.md) 🆕 | 3.3k | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. | quieres probar computer use con Gemini | 🟡 |
| [NeMo-Agent-Toolkit](../fichas/nemo-agent-toolkit.md) 🆕 | 2.7k | Toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). | trabajas con infra NVIDIA o necesitas guardrails/eval empresarial | 🔴 |
| [nodeterm](../fichas/nodeterm.md) 🆕 | 2.5k | Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. | gestionas muchas terminales o sesiones de agentes y prefieres una organización visual | 🟡 |
| [Agent Protocol](../fichas/agent-protocol.md) 🆕 | 698 | Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado. | diseñas una plataforma que sirve agentes de distintos frameworks | 🟢 |

## Simulación, evolución y debate entre modelos

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [MiroFish](../fichas/mirofish.md) 🆕 | 85.6k | Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. | simulas futuros/escenarios con muchos actores | 🔴 |
| [llm-council](../fichas/llm-council.md) 🆕 | 26.5k | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. | quieres consenso entre modelos o comparar proveedores | 🟡 |
| [openevolve](../fichas/openevolve.md) 🆕 | 7.8k | Agente de codificación evolutivo que optimiza algoritmos por simulación genética. | optimizas problemas algorítmicos donde cabe explorar muchas variantes | 🔴 |
| [hermes-agent-self-evolution](../fichas/hermes-agent-self-evolution.md) 🆕 | 5.7k | Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA. | quieres experimentar con mejoras de Hermes medidas sobre un conjunto de evaluación | 🟡 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### OpenCode, Claude Code, Codex CLI, Gemini CLI, Cline, Open Interpreter, goose

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [OpenCode](../fichas/opencode.md) | 227k | quieres un agente de código abierto y multi-modelo | prefieres la experiencia oficial de un proveedor; mira `claude-code` o `codex` |
| [Claude Code](../fichas/claude-code.md) | 156k | quieres el agente de código más capaz para tareas largas en tu repo | necesitas un agente totalmente abierto y multi-modelo; mira `opencode` |
| [Codex CLI](../fichas/codex.md) | 135k | usas ChatGPT u OpenAI y quieres un agente abierto en terminal | trabajas con Claude como modelo principal; mira `claude-code` |
| [Gemini CLI](../fichas/gemini-cli.md) | 109k | quieres un agente de terminal potente con cuota gratuita | buscas el agente con mejor desempeño en tareas largas; mira `claude-code` |
| [Cline](../fichas/cline.md) | 71.6k | quieres un agente dentro de VS Code con control de cada paso | trabajas solo en terminal; mira `opencode` |
| [Open Interpreter](../fichas/open-interpreter.md) | 68.9k | quieres un agente que ejecute código usando modelos abiertos | buscas un agente maduro para repos grandes; mira `opencode` |
| [goose](../fichas/goose.md) | 56.6k | quieres un agente abierto con app de escritorio y MCP | solo programas en terminal y quieres el más usado; mira `opencode` |

### OpenHands, SWE-agent, Open SWE

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [OpenHands](../fichas/openhands.md) | 93.5k | quieres un agente que "haga", no solo hable | solo necesitas chat/RAG o no puedes correr Docker |
| [SWE-agent](../fichas/swe-agent.md) | 20.8k | investigas o automatizas la resolución de issues | quieres un asistente diario en tu terminal; mira `claude-code` |
| [Open SWE](../fichas/open-swe.md) | 11.2k | quieres construir el agente de código interno de tu empresa | solo quieres un agente para tu terminal; mira `claude-code` |

### LangGraph, langchain, MetaGPT, AutoGen, crewAI, LlamaIndex, Agno

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [LangGraph](../fichas/langgraph.md) | 45k | necesitas agentes con estado, control fino y persistencia | quieres algo mínimo para un agente simple; mira `smolagents` |
| [langchain](../fichas/langchain.md) | 150k | quieres la base estándar con máximas integraciones | prefieres mínima abstracción o un solo proveedor sin cambiar |
| [MetaGPT](../fichas/metagpt.md) | 71.3k | quieres estudiar un flujo multiagente basado en roles de desarrollo | un flujo determinista resuelve el problema sin un agente |
| [AutoGen](../fichas/autogen.md) | 61.8k | mantienes un proyecto que ya usa AutoGen | empiezas algo nuevo; mira `agent-framework` |
| [crewAI](../fichas/crewai.md) | 60.9k | quieres velocidad y un modelo mental simple de "equipo" | necesitas control de bajo nivel o orquestación muy custom |
| [LlamaIndex](../fichas/llama-index.md) | 52.9k | tu proyecto gira alrededor de RAG sobre tus documentos | necesitas orquestación general de agentes; mira `langgraph` |
| [Agno](../fichas/agno.md) | 43.2k | quieres un framework de agentes con memoria y API lista | necesitas grafos explícitos y controlables; mira `langgraph` |

### Mastra, AI SDK (Vercel), LangGraph.js

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Mastra](../fichas/mastra.md) | 29.5k | tu equipo trabaja en TypeScript y quiere agentes completos | trabajas en Python; mira `langgraph` o `pydantic-ai` |
| [AI SDK (Vercel)](../fichas/vercel-ai.md) | 28k | construyes una app web con IA en TypeScript | necesitas agentes complejos con memoria y workflows; mira `mastra` |
| [LangGraph.js](../fichas/langgraphjs.md) | 3.4k | quieres el modelo de LangGraph en TypeScript | buscas una experiencia TS más integrada; mira `mastra` |

### Sim, AutoGPT, dify, langflow, Flowise

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Sim](../fichas/sim.md) | 30.1k | quieres un constructor visual de agentes moderno y abierto | prefieres automatización general con cientos de apps; mira `n8n` |
| [AutoGPT](../fichas/autogpt.md) | 188k | quieres agentes continuos con un editor visual propio | buscas algo ligero y fácil de operar; mira `sim` o `flowise` |
| [dify](../fichas/dify.md) | 161k | quieres una app IA completa autoalojada | solo necesitas una librería o un prototipo puntual |
| [langflow](../fichas/langflow.md) | 157k | prefieres construir en visual sobre LangChain | quieres todo en código o no usas LangChain |
| [Flowise](../fichas/flowise.md) | 55.6k | quieres un prototipo visual ya, en stack JS | necesitas plataforma completa con RAG/observabilidad (dify) |

### OpenClaw, hermes-agent, Mercury Agent

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [OpenClaw](../fichas/openclaw.md) | 394k | quieres un asistente personal que actúe por tus canales de chat | necesitas un agente para tu empresa con varios usuarios; mira `hermes-agent` |
| [hermes-agent](../fichas/hermes-agent.md) | 263k | quieres agentes locales con UI y memoria persistente | prefieres orquestación en nube o no quieres compilar Tauri |
| [Mercury Agent](../fichas/mercury-agent.md) | 3.9k | quieres un asistente personal ligero con permisos claros | buscas el ecosistema más grande; mira `openclaw` |

### STORM, gpt-researcher, open_deep_research, local-deep-research

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [STORM](../fichas/storm.md) | 31.9k | necesitas informes largos y citados sobre un tema | quieres respuestas cortas con fuentes; mira `gpt-researcher` |
| [gpt-researcher](../fichas/gpt-researcher.md) | 30.7k | necesitas research profundo citado | solo quieres una respuesta corta o un chat simple |
| [open_deep_research](../fichas/open-deep-research.md) | 12.7k | quieres adaptar un agente de investigación construido con LangGraph | un flujo determinista resuelve el problema sin un agente |
| [local-deep-research](../fichas/local-deep-research.md) | 9.6k | quieres investigar con un modelo local y conservar las fuentes consultadas | un flujo determinista resuelve el problema sin un agente |

### E2B, NemoClaw, sandbox

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [E2B](../fichas/e2b.md) | 14.9k | tu agente ejecuta código y necesitas aislarlo | solo necesitas ejecutar código localmente de confianza |
| [NemoClaw](../fichas/nemoclaw.md) | 23k | quieres correr agentes potentes con aislamiento corporativo | solo necesitas un sandbox para ejecutar código; mira `e2b` |
| [sandbox](../fichas/sandbox.md) | 6.3k | quieres aislar la ejecución de agentes y reproducibilidad | te basta correr local sin sandbox o no puedes asumir el overhead de Docker |

## 🧪 Recetas que usan esta categoría

- [🔎 Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [🧠 Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md) — Que un agente de código entienda una base de código enorme sin gastar todo su contexto.
- [🌐 Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md) — Construir un frontend pulido con chat o funciones de IA integradas.
- [📎 RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
- [🛠️ Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
