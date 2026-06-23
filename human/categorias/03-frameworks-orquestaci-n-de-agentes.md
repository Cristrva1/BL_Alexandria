# Frameworks & Orquestación de Agentes

Generado: 2026-06-23T16:56:54.761958+00:00

| Repo | Rol | Instalacion | Decision | Uso real |
|---|---|---|---|---|
| ag2 | library | reference_only | reference | framework maduro para sistemas multiagente con patrones de colaboración (heredero de AutoGen). Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo. |
| crewAI | library | reference_only | reference | framework para orquestar "crews" de agentes con roles y tareas. Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica. |
| langchain | library | reference_only | reference | framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos. |
| langflow | app | reference_only | reference | constructor visual de flujos LLM/agentes construido sobre LangChain. Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código. |
| dify | platform | reference_only | reference | plataforma integral para construir apps de IA con backend y UI listos. Combina orquestación de prompts, RAG, agentes y observabilidad en un mismo producto autoalojable. |
| Flowise | app | reference_only | reference | builder visual drag-and-drop para pipelines LLM. Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible. |
| OpenHands | platform | reference_only | reference | plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox. |
| deer-flow | platform | reference_only | reference | super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. Coordina tareas complejas delegando en agentes especializados. |
| NeMo-Agent-Toolkit | library | deferred | defer | toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial. |
| hermes-agent | app | reference_only | reference | entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local. |
| openevolve | runtime | deferred | defer | agente de codificación evolutivo que optimiza algoritmos por simulación genética. Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones. |
| gpt-researcher | platform | reference_only | reference | agente autónomo que investiga en línea y consolida reportes citados y estructurados. Planifica sub-preguntas, busca fuentes y redacta un informe con referencias. |
| autoresearch | platform | reference_only | reference | enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. Proyecto pequeño y exploratorio más que una herramienta pulida. |
| ruflo | platform | deferred | defer | harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). Orquesta swarms de agentes especializados a escala. |
| multica | platform | reference_only | reference | plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas"). Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho. |
| MiroFish | platform | deferred | defer | motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho. |
| llm-council | platform | reference_only | reference | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso. |
| awesome-LangGraph | directory | reference_only | reference | repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. Es una lista curada, no una herramienta ejecutable. |
