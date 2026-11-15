# 21. Asistentes e investigación con agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agentes-chat`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=asistentes,agent,typescript

**Qué es:** Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas.
**Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: API de IA opcional. El README documenta usar una cuenta o sesión del agente, además de las otras rutas que admita el producto.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. El razonamiento consume el plan o proveedor configurado. Alojamiento, conectores y otros servicios se evalúan aparte.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/agentes-chat/agentes-chat

**Instalación** [?]: `Seguir la instalación original: https://github.com/agentes-chat/agentes-chat/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `autoresearch`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=research,agents,python

**Qué es:** Proyecto pequeño y exploratorio de Karpathy, más que una herramienta pulida.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo del agente que ya utilizas. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/karpathy/autoresearch

**Instalación** [?]: `Seguir la instalación original: https://github.com/karpathy/autoresearch/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** experimentas con research iterativo o quieres un punto de partida
**Evita si:** quieres salida pulida y lista (gpt-researcher)
**Combina con:** `gpt-researcher`, `crawl4ai`

## `deeptutor`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,local · tags=learning,agents,rag,python

**Qué es:** Resuelve dudas, genera ejercicios y guía el estudio con RAG sobre tu material y memoria del alumno. Es un producto educativo, no un orquestador genérico.
**Stack:** Python, Next.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/HKUDS/DeepTutor

**Instalación** [?]: `Seguir la instalación original: https://github.com/HKUDS/DeepTutor/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un tutor con IA sobre tu propio material
**Evita si:** buscas un framework para construir agentes; mira `langgraph`
**Combina con:** `docling`
**Alternativas (elige una):** `open-notebook`

## `deer-flow`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,research,python,docker

**Qué es:** Coordina tareas complejas delegando en agentes especializados.
**Stack:** Python/TS, LangChain, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/bytedance/deer-flow

**Instalación** [?]: `Seguir la instalación original: https://github.com/bytedance/deer-flow/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un orquestador completo y extensible
**Evita si:** buscas algo minimalista o sin Docker
**Combina con:** `gpt-researcher`, `firecrawl`

## `fugu`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=asistentes,agent,shell

**Qué es:** Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API.
**Stack:** Shell
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/SakanaAI/fugu

**Instalación** [?]: `Seguir la instalación original: https://github.com/SakanaAI/fugu/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `gpt-researcher`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,research,python,docker

**Qué es:** Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.
**Stack:** Python, Next.js, FastAPI
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/assafelovic/gpt-researcher

**Instalación** [+]: `pip install gpt-researcher`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas research profundo citado
**Evita si:** solo quieres una respuesta corta o un chat simple
**Combina con:** `firecrawl`, `browser-use`
**Alternativas (elige una):** `storm`, `vane`, `open-deep-research`

## `hello-halo`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=asistentes,agent,typescript

**Qué es:** Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: API de IA opcional. El README documenta usar una cuenta o sesión del agente, además de las otras rutas que admita el producto.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. El razonamiento consume el plan o proveedor configurado. Alojamiento, conectores y otros servicios se evalúan aparte.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/openkursar/hello-halo

**Instalación** [?]: `Seguir la instalación original: https://github.com/openkursar/hello-halo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `hermes-agent`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=agents,python

**Qué es:** Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.
**Stack:** Rust (Tauri), TypeScript, Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
- Otras rutas: El proyecto documenta una suscripción propia de Nous Portal además de otros proveedores; los servicios incluidos y sus límites pertenecen a ese plan.
**Repo:** https://github.com/NousResearch/hermes-agent

**Instalación** [?]: `Seguir la instalación original: https://github.com/NousResearch/hermes-agent/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres agentes locales con UI y memoria persistente
**Evita si:** prefieres orquestación en nube o no quieres compilar Tauri
**Combina con:** `ecc`, `odysseus`
**Alternativas (elige una):** `openclaw`, `mercury-agent`

## `local-deep-research`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=research,academia,anthropic,arxiv,brave,deep-research,encryption,home-automation

**Qué es:** Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. Itera entre preguntas, búsquedas y síntesis y permite configurar motores de búsqueda y proveedores de modelos.
**Stack:** Python, Docker, pyproject.toml, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/LearningCircuit/local-deep-research

**Instalación** [+]: `pip install local-deep-research`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres investigar con un modelo local y conservar las fuentes consultadas
**Evita si:** un flujo determinista resuelve el problema sin un agente
**Alternativas (elige una):** `open-deep-research`

## `mercury-agent`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,chatbot,typescript

**Qué es:** Recuerda lo importante, pide permiso antes de actuar y trae 31 herramientas, tableros kanban y skills extensibles, con datos en SQLite.
**Stack:** TypeScript, SQLite
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/cosmicstack-labs/mercury-agent

**Instalación** [?]: `Seguir la instalación original: https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un asistente personal ligero con permisos claros
**Evita si:** buscas el ecosistema más grande; mira `openclaw`
**Combina con:** `claude-mem`
**Alternativas (elige una):** `openclaw`, `hermes-agent`

## `multica`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,go

**Qué es:** Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.
**Stack:** web/TS, Docker, PostgreSQL
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/multica-ai/multica

**Instalación** [?]: `Seguir la instalación original: https://github.com/multica-ai/multica/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** mezclas trabajo humano y agentes en un mismo flujo
**Evita si:** quieres automatización 100% headless o un producto maduro
**Combina con:** `ruflo`, `chatwoot`

## `open-deep-research`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=— · tags=research,python

**Qué es:** Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP. Organiza ciclos de planificación, búsqueda y síntesis mediante un grafo de investigación.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/langchain-ai/open_deep_research

**Instalación** [?]: `Seguir la instalación original: https://github.com/langchain-ai/open_deep_research/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres adaptar un agente de investigación construido con LangGraph
**Evita si:** un flujo determinista resuelve el problema sin un agente
**Combina con:** `langfuse`
**Alternativas (elige una):** `local-deep-research`, `gpt-researcher`

## `openclaw`
role=app · exec=hybrid · setup=medium · mcp=True · prov=anthropic,openai,local · tags=agents,chatbot,typescript

**Qué es:** Un solo operador, muchas superficies: el asistente vive en tu equipo, tiene memoria, ejecuta tareas reales y responde por los canales que ya usas. Es uno de los proyectos de IA más populares de GitHub.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/openclaw/openclaw

**Instalación** [+]: `npm install -g openclaw@latest`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres un asistente personal que actúe por tus canales de chat
**Evita si:** necesitas un agente para tu empresa con varios usuarios; mira `hermes-agent`
**Combina con:** `nemoclaw`, `claude-mem`
**Alternativas (elige una):** `hermes-agent`, `mercury-agent`

## `opendots`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=asistentes,agent,typescript

**Qué es:** Plataforma de asistentes de IA persistentes que coordinan conversaciones, llamadas y servicios conectados.
**Stack:** TypeScript, Dockerfile, package.json
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/CopilotKit/OpenDots

**Instalación** [?]: `Seguir la instalación original: https://github.com/CopilotKit/OpenDots/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plataforma de asistentes de IA persistentes que coordinan conversaciones, llamadas y servicios conectados.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `paperclip`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=asistentes,acpx,agent-orchestration,agent-skills,agentic-ai,ai-agents,ai-engineering,ai-governance

**Qué es:** Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. Conecta distintos runtimes y coordina sus encargos y costes desde una aplicación central.
**Stack:** TypeScript, Docker, Node.js
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/paperclipai/paperclip

**Instalación** [?]: `Seguir la instalación original: https://github.com/paperclipai/paperclip/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas coordinar varios agentes y seguir su trabajo en un panel
**Evita si:** un flujo determinista resuelve el problema sin un agente

## `ruflo`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=automation,agents,typescript

**Qué es:** Orquesta swarms de agentes especializados a escala.
**Stack:** Rust
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/ruvnet/ruflo

**Instalación** [+]: `npm install -g ruflo@latest`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** orquestas muchos agentes a escala y quieres rendimiento
**Evita si:** solo necesitas 1-2 agentes o no usas Claude Code/Codex
**Combina con:** `mem0`, `ecc`

## `social-media-agent`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=asistentes,typescript

**Qué es:** Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas. Usa un flujo de LangGraph para investigar el enlace, redactar y solicitar aprobación de la publicación.
**Stack:** TypeScript, pyproject.toml, Node.js
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. Revisar el plan, créditos, cuotas y facturación del proveedor antes de ejecutar.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/langchain-ai/social-media-agent

**Instalación** [?]: `Seguir la instalación original: https://github.com/langchain-ai/social-media-agent/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres preparar publicaciones para X o LinkedIn con una etapa de aprobación
**Evita si:** un flujo determinista resuelve el problema sin un agente
**Combina con:** `langgraphjs`

## `storm`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai · tags=research,agents,python

**Qué es:** Simula conversaciones entre perspectivas para hacer preguntas, busca fuentes y redacta un artículo estructurado y citado. Útil para informes de fondo.
**Stack:** Python, DSPy
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/stanford-oval/storm

**Instalación** [?]: `Seguir la instalación original: https://github.com/stanford-oval/storm/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas informes largos y citados sobre un tema
**Evita si:** quieres respuestas cortas con fuentes; mira `gpt-researcher`
**Combina con:** `searxng`, `firecrawl`
**Alternativas (elige una):** `gpt-researcher`
