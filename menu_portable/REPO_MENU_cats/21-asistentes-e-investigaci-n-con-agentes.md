# 21. Asistentes e investigación con agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agentes-chat`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=asistentes,agent,typescript

**Qué es:** Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas.
**Stack:** Docker Compose y PostgreSQL; proveedor o computadora conectada; equipo de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Autoalojado AGPL, Cloud de pago y licencia comercial alternativa; API o cuentas de agentes por separado
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Claude Code puede usarse en computadora conectada; la ruta Codex está todavía en pruebas y no se presenta como verificación de producción
- Coste: El coste depende del proveedor o la ruta. Autoalojado AGPL, Cloud de pago y licencia comercial alternativa; API o cuentas de agentes por separado
- Equipo: Preparación según la ruta elegida. Docker Compose y PostgreSQL; proveedor o computadora conectada; equipo de prueba
**Repo:** https://github.com/agentes-chat/agentes-chat

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/agentes-chat/agentes-chat/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar un espacio de colaboración con agentes; Organizar consultas en canales
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un canal de prueba y pide al agente una respuesta sin conectar acciones externas
**Qué comprobar:** Puedes revisar conversación, herramientas permitidas y aprobaciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `github-mcp-server`

## `autoresearch`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=research,agents,python

**Qué es:** Experimento para iterar sobre entrenamiento de nanochat con un agente de código y una GPU NVIDIA.
**Stack:** GPU NVIDIA; Python 3.10+; uv; agente y presupuesto de cómputo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el plan del agente y cómputo para entrenar el modelo local; el código actual necesita GPU NVIDIA
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Probado por el autor en H100 y no diseñado actualmente para CPU o MPS; no se traslada su sugerencia de desactivar permisos como requisito para principiantes
- Coste: Consumo del agente que ya utilizas. Usa el plan del agente y cómputo para entrenar el modelo local; el código actual necesita GPU NVIDIA
- Equipo: Preparación según la ruta elegida. GPU NVIDIA; Python 3.10+; uv; agente y presupuesto de cómputo
**Repo:** https://github.com/karpathy/autoresearch

**Instalación** [+]:

```
# 2. Install dependencies
uv sync
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar optimización de entrenamiento; Aprender a registrar experimentos reproducibles
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee program.md y ejecuta primero un experimento manual pequeño antes de permitir iteraciones
**Qué comprobar:** Puedes comparar métrica y cambio concreto del experimento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nanochat`, `claude-code`, `codex`

## `deeptutor`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,local · tags=learning,agents,rag,python

**Qué es:** Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos.
**Stack:** Python y paquete completo o Docker; modelo y embeddings; documento corto propio
**Acceso y costes:**
- API de IA: API de IA opcional. Admite proveedores API, modelos locales y consultas a agentes con sus cuentas; OAuth Codex está marcado experimental
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. Documenta consultas a Claude Code, Codex y Antigravity; la conexión del agente, la generación principal y los embeddings son configuraciones diferentes
- Coste: El coste depende del proveedor o la ruta. Admite proveedores API, modelos locales y consultas a agentes con sus cuentas; OAuth Codex está marcado experimental
- Equipo: Preparación según la ruta elegida. Python y paquete completo o Docker; modelo y embeddings; documento corto propio
**Repo:** https://github.com/HKUDS/DeepTutor

**Instalación** [+]:

```
mkdir -p my-deeptutor && cd my-deeptutor
python -m pip install -U "deeptutor[full]"
deeptutor init     # ports + LLM provider + optional embedding/search
deeptutor start    # starts backend + frontend
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un tema desde apuntes propios; Preparar preguntas de repaso
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una base con un texto breve y pide una explicación con referencias al contenido
**Qué comprobar:** Puedes contrastar la respuesta con fragmentos del texto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `lightrag`, `docling`, `ollama`
**Alternativas (elige una):** `open-notebook`

## `deer-flow`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,research,python,docker

**Qué es:** Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles.
**Stack:** Docker o entorno de desarrollo; modelo configurado; carpeta de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Los modelos, herramientas y sandbox tienen costes por configuración; la integración Claude Code no incluye inferencia del servidor
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Documenta el skill claude-to-deerflow para controlar una instancia activa; pedir a Codex que instale el proyecto no demuestra una integración runtime con Codex
- Coste: El coste depende del proveedor o la ruta. Los modelos, herramientas y sandbox tienen costes por configuración; la integración Claude Code no incluye inferencia del servidor
- Equipo: Preparación según la ruta elegida. Docker o entorno de desarrollo; modelo configurado; carpeta de prueba
**Repo:** https://github.com/bytedance/deer-flow

**Instalación** [+]:

```
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
make setup          # interactive wizard: writes config.yaml and .env (about 2 minutes)
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Investigar un tema con fuentes; Coordinar una generación de informe
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Completa setup y solicita un informe corto con fuentes antes de habilitar herramientas de escritura
**Qué comprobar:** Puedes contrastar las referencias y revisar las acciones del agente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `firecrawl`, `searxng`

## `gpt-researcher`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,research,python,docker

**Qué es:** Agente autónomo que investiga en línea y consolida reportes citados y estructurados.
**Stack:** Python 3.11+; proveedor y buscador; cliente MCP solo si eliges esa ruta
**Acceso y costes:**
- API de IA: API de IA opcional. Admite endpoints locales compatibles o API; búsqueda y otras herramientas pueden cobrar aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El MCP está ahora en gptr-mcp, proyecto compañero con stdio y transportes de red; el skill y el servidor de investigación requieren configuración propia
- Coste: El coste depende del proveedor o la ruta. Admite endpoints locales compatibles o API; búsqueda y otras herramientas pueden cobrar aparte
- Equipo: Preparación según la ruta elegida. Python 3.11+; proveedor y buscador; cliente MCP solo si eliges esa ruta
**Repo:** https://github.com/assafelovic/gpt-researcher

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/assafelovic/gpt-researcher/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un informe de mercado con fuentes; Investigar documentación técnica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Haz una pregunta acotada y verifica dos fuentes antes de reutilizar el informe
**Qué comprobar:** Puedes recuperar contexto y enlaces que respaldan conclusiones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `firecrawl`, `ollama`
**Alternativas (elige una):** `storm`, `vane`, `local-deep-research`

## `hello-halo`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=asistentes,agent,typescript

**Qué es:** Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API.
**Stack:** Aplicación para tu sistema; cuenta o proveedor compatible; carpeta de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Admite cuentas Claude o ChatGPT y proveedores API; sus cuotas son externas
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Integra motores Claude Code y Codex; que Halo SDK esté orientado a modelos abiertos no confirma por sí solo inferencia local configurada
- Coste: El coste depende del proveedor o la ruta. Admite cuentas Claude o ChatGPT y proveedores API; sus cuotas son externas
- Equipo: Preparación según la ruta elegida. Aplicación para tu sistema; cuenta o proveedor compatible; carpeta de prueba
**Repo:** https://github.com/openkursar/hello-halo

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/openkursar/hello-halo/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un asistente de escritorio; Revisar tareas de código visualmente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un espacio con un archivo de ejemplo y solicita una explicación antes de activar control del navegador
**Qué comprobar:** Puedes revisar el motor y los cambios propuestos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `anthropic-skills`, `context7`, `playwright-mcp`

## `hermes-agent`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=agents,python

**Qué es:** Asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados.
**Stack:** Equipo compatible; proveedor o endpoint local; perfil de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. API, Portal por suscripción o endpoint local según configuración; documenta también ruta ChatGPT/Codex
- Claude Code: Referencia para la herramienta; no es una integración
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Importar ajustes e historial de Claude Code no equivale a usar su plan como motor; las herramientas de búsqueda, voz e imagen tienen proveedores separados
- Coste: El coste depende del proveedor o la ruta. API, Portal por suscripción o endpoint local según configuración; documenta también ruta ChatGPT/Codex
- Equipo: Preparación según la ruta elegida. Equipo compatible; proveedor o endpoint local; perfil de prueba
**Repo:** https://github.com/NousResearch/hermes-agent

**Instalación** [?]:

```
Seguir la instalación original: https://hermes-agent.nousresearch.com/docs/getting-started/installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar memoria de un asistente; Comparar un modelo local con Nous Portal
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un perfil nuevo y pide recordar una nota ficticia antes de importar historial
**Qué comprobar:** Puedes comprobar la nota guardada y el proveedor usado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nemoclaw`, `ollama`, `ecc`
**Alternativas (elige una):** `openclaw`, `mercury-agent`

## `local-deep-research`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=— · tags=research,academia,anthropic,arxiv,brave,deep-research,encryption,home-automation

**Qué es:** Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes.
**Stack:** Modelo local o remoto; buscador; Python o Docker; equipo adecuado al modelo
**Acceso y costes:**
- API de IA: API de IA opcional. Modelos locales y SearXNG ofrecen ruta sin API de pago; motores y modelos remotos tienen condiciones propias
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El MCP documentado usa stdio para uso local y carece de autenticación y límite de peticiones; el benchmark del autor no garantiza exactitud en cualquier tema
- Coste: El coste depende del proveedor o la ruta. Modelos locales y SearXNG ofrecen ruta sin API de pago; motores y modelos remotos tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Modelo local o remoto; buscador; Python o Docker; equipo adecuado al modelo
**Repo:** https://github.com/LearningCircuit/local-deep-research

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/LearningCircuit/local-deep-research/blob/main/docs/installation.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar documentos privados; Preparar una revisión bibliográfica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Investiga una pregunta pequeña con Ollama y SearXNG y abre las fuentes citadas
**Qué comprobar:** Puedes identificar buscador, modelo y evidencia utilizada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `searxng`, `llama-cpp`
**Alternativas (elige una):** `gpt-researcher`

## `mercury-agent`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,chatbot,typescript

**Qué es:** Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web.
**Stack:** Node 22 o posterior; proveedor u Ollama/LM Studio; perfil de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. API, Mercury Cloud o modelos locales según elección; Ollama Cloud no es inferencia local
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El asistente inicia un servicio en segundo plano; revisa su estado antes de añadir canales o ejecución programada
- Coste: El coste depende del proveedor o la ruta. API, Mercury Cloud o modelos locales según elección; Ollama Cloud no es inferencia local
- Equipo: Preparación según la ruta elegida. Node 22 o posterior; proveedor u Ollama/LM Studio; perfil de prueba
**Repo:** https://github.com/cosmicstack-labs/mercury-agent

**Instalación** [+]:

```
npm i -g @cosmicstack/mercury-agent
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar presupuestos de tokens
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Arranca mercury, comprueba status y pide una respuesta sobre una nota ficticia sin conectar canales
**Qué comprobar:** Puedes identificar proveedor, servicio en segundo plano y permisos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `searxng`
**Alternativas (elige una):** `openclaw`, `hermes-agent`

## `multica`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,go

**Qué es:** Workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias.
**Stack:** Un CLI de agente instalado y autenticado; Docker si autoalojas servidor
**Acceso y costes:**
- API de IA: API de IA opcional. Usa las cuentas de los agentes y alojamiento propio o servicio; no incluye créditos
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Se declara source-available con licencia Multica que añade condiciones a Apache; no debe resumirse como Apache puro ni como una garantía de sustituir empleados
- Coste: El coste depende del proveedor o la ruta. Usa las cuentas de los agentes y alojamiento propio o servicio; no incluye créditos
- Equipo: Preparación según la ruta elegida. Un CLI de agente instalado y autenticado; Docker si autoalojas servidor
**Repo:** https://github.com/multica-ai/multica

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/multica-ai/multica/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar trabajo entre agentes; Revisar entregas en un espacio compartido
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Asigna una tarea de explicación a un agente en un proyecto de prueba antes de crear automatizaciones
**Qué comprobar:** Puedes ver tarea, sesión y resultado atribuibles al agente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`
**Alternativas (elige una):** `paperclip`

## `openbot`
role=app · exec=hybrid · setup=heavy · mcp=True · prov=openai,anthropic,google,local · tags=agents,computer-use,ag-ui,mcp,typescript

**Qué es:** Espacio autoalojable de CopilotKit para compañeros de IA con navegador propio, permisos, aprobaciones y auditoría, conectables por AG-UI.
**Stack:** TypeScript, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Elige OpenAI, Claude, Gemini o un endpoint compatible con OpenAI; el despliegue en Kubernetes de evaluación usa una clave de modelo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El README describe una operación totalmente local con OpenBot, Intelligence y un modelo compatible; las apps conectadas siguen usando internet.
- Coste: El coste depende del proveedor o la ruta. La plantilla es MIT, pero CopilotKit Intelligence tiene licencia aparte: local gratuita para uso personal, prueba para Kubernetes y licencia de producción después.
- Equipo: Preparación según la ruta elegida. Docker para PostgreSQL, la API y los Bots; Bun para ejecutar desde el código; Kubernetes y Helm para equipos.
**Repo:** https://github.com/CopilotKit/OpenBot

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/CopilotKit/OpenBot/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Dar a un asistente un navegador propio con aprobaciones; Conectar un agente existente por AG-UI a un espacio común
**Evita si:** necesitas una herramienta estable y auditada para datos sensibles
**Primera prueba propuesta:** Instala la app de escritorio, configura un modelo y pide una búsqueda web que requiera aprobación
**Qué comprobar:** La acción queda pendiente de tu aprobación y aparece en la auditoría
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `copilotkit`, `langgraph`, `mastra`, `crewai`, `firecrawl`, `composio`
**Alternativas (elige una):** `opendots`

## `openclaw`
role=app · exec=hybrid · setup=medium · mcp=True · prov=anthropic,openai,local · tags=agents,chatbot,typescript

**Qué es:** Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más.
**Stack:** Node compatible o instalador; proveedor o harness; canal de prueba opcional
**Acceso y costes:**
- API de IA: API de IA opcional. Modelos locales, API y harnesses con cuentas tienen costes distintos; los canales también pueden cobrar
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La interfaz y memoria locales no mantienen locales los prompts enviados a proveedores; el backend Claude CLI usa el ejecutable autenticado y Codex tiene su propio harness
- Coste: El coste depende del proveedor o la ruta. Modelos locales, API y harnesses con cuentas tienen costes distintos; los canales también pueden cobrar
- Equipo: Preparación según la ruta elegida. Node compatible o instalador; proveedor o harness; canal de prueba opcional
**Repo:** https://github.com/openclaw/openclaw

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/openclaw/openclaw/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente personal; Conectar un agente a un canal propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Completa onboarding y consulta gateway status y dashboard antes de conectar mensajería
**Qué comprobar:** Puedes identificar estado, proveedor y permisos del Gateway
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nemoclaw`, `claude-mem`, `claude-code`, `ollama`
**Alternativas (elige una):** `hermes-agent`, `mercury-agent`

## `opendots`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=asistentes,agent,typescript

**Qué es:** Interfaz abierta de asistentes persistentes que requiere CopilotKit Intelligence, alojado, evaluado localmente o con licencia.
**Stack:** Node; CopilotKit Intelligence; proveedores y conectores elegidos
**Acceso y costes:**
- API de IA: API de IA necesaria. La UI MIT requiere Intelligence hospedado, evaluación Docker local o despliegue autoalojado con licencia; modelos y voz pueden cobrar aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Autoalojar OpenDots no incluye automáticamente el servicio Intelligence ni una pila enteramente local
- Coste: El coste depende del proveedor o la ruta. La UI MIT requiere Intelligence hospedado, evaluación Docker local o despliegue autoalojado con licencia; modelos y voz pueden cobrar aparte
- Equipo: Preparación según la ruta elegida. Node; CopilotKit Intelligence; proveedores y conectores elegidos
**Repo:** https://github.com/CopilotKit/OpenDots

**Instalación** [+]:

```
git clone https://github.com/CopilotKit/OpenDots.git
cd OpenDots
npm ci
cp .env.example .env
npm run dev
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar aprobación de acciones conectadas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un Dot de prueba y haz una pregunta sin conceder herramientas de escritura
**Qué comprobar:** Puedes comprobar la respuesta y el panel de conexiones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `copilotkit`, `composio`, `servers`
**Alternativas (elige una):** `openbot`

## `paperclip`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=asistentes,acpx,agent-orchestration,agent-skills,agentic-ai,ai-agents,ai-engineering,ai-governance

**Qué es:** Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo.
**Stack:** Node 24.11+; pnpm 9.15+ para desarrollo; agentes configurados; proyecto de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Usa modelos y agentes propios; servidor, proveedores y servicios conectados tienen costes independientes
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El panel organiza trabajo y no constituye por sí solo una empresa autónoma; las integraciones Claude y Codex dependen de sus adaptadores y cuentas
- Coste: El coste depende del proveedor o la ruta. Usa modelos y agentes propios; servidor, proveedores y servicios conectados tienen costes independientes
- Equipo: Preparación según la ruta elegida. Node 24.11+; pnpm 9.15+ para desarrollo; agentes configurados; proyecto de prueba
**Repo:** https://github.com/paperclipai/paperclip

**Instalación** [?]:

```
Seguir la instalación original: https://docs.paperclip.ing/reference/cli/installation/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar tareas de varios agentes; Auditar una propuesta antes de aprobarla
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una tarea de explicación para un agente y revisa historial y presupuesto antes de activar heartbeats
**Qué comprobar:** Puedes atribuir una ejecución a su tarea, agente y coste registrado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openclaw`, `claude-code`, `codex`, `hermes-agent`
**Alternativas (elige una):** `multica`

## `ruflo`
role=platform · exec=hybrid · setup=heavy · mcp=True · prov=— · tags=automation,agents,typescript

**Qué es:** Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow).
**Stack:** Node; carpeta de proyecto; Claude Code o cliente MCP; modelo para agentes
**Acceso y costes:**
- API de IA: API de IA opcional. Usa el proveedor o plan de los agentes; el plugin local ruvllm documenta Ollama
- Claude Code: Integración documentada por el proyecto
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Claude Code tiene integración de proyecto; otros clientes usan el servidor MCP estándar y no heredan necesariamente sus hooks ni todas las funciones
- Coste: El coste depende del proveedor o la ruta. Usa el proveedor o plan de los agentes; el plugin local ruvllm documenta Ollama
- Equipo: Preparación según la ruta elegida. Node; carpeta de proyecto; Claude Code o cliente MCP; modelo para agentes
**Repo:** https://github.com/ruvnet/ruflo

**Instalación** [+]:

```
npx ruflo@latest init
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Coordinar tareas de código; Estudiar memoria compartida entre agentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inicializa una carpeta de prueba y examina los agentes, hooks y configuración añadidos antes de encargar trabajo
**Qué comprobar:** Puedes identificar los archivos creados y herramientas MCP disponibles
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`

## `social-media-agent`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=asistentes,typescript

**Qué es:** Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas.
**Stack:** Node y Yarn; claves de modelo y servicios; cuentas sociales solo al conectar publicación
**Acceso y costes:**
- API de IA: API de IA necesaria. APIs del modelo, servicios de ejecución y redes tienen sus costes y límites
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El flujo incluye revisión humana; configurar el servidor local no evita las claves y permisos que requieren las integraciones
- Coste: Consumo de APIs o servicios. APIs del modelo, servicios de ejecución y redes tienen sus costes y límites
- Equipo: Preparación según la ruta elegida. Node y Yarn; claves de modelo y servicios; cuentas sociales solo al conectar publicación
**Repo:** https://github.com/langchain-ai/social-media-agent

**Instalación** [+]:

```
git clone https://github.com/langchain-ai/social-media-agent.git

yarn install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una propuesta para LinkedIn; Convertir un artículo en un borrador corto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera un borrador desde un enlace propio y recházalo o edítalo sin publicarlo
**Qué comprobar:** Puedes revisar texto y aprobación antes de cualquier publicación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraphjs`, `firecrawl`, `supabase`

## `storm`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai · tags=research,agents,python

**Qué es:** Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia.
**Stack:** Conda y Python 3.11; modelo; credenciales del buscador configurado
**Acceso y costes:**
- API de IA: API de IA necesaria. Los ejemplos usan modelos y buscadores con API y sus costes; no incluye suscripciones ni créditos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Las citas y el texto generado requieren revisión; una interfaz de modelo configurable no confirma una ruta local lista para usar
- Coste: Consumo de APIs o servicios. Los ejemplos usan modelos y buscadores con API y sus costes; no incluye suscripciones ni créditos
- Equipo: Preparación según la ruta elegida. Conda y Python 3.11; modelo; credenciales del buscador configurado
**Repo:** https://github.com/stanford-oval/storm

**Instalación** [+]:

```
git clone https://github.com/stanford-oval/storm.git
    cd storm

conda create -n storm python=3.11
   conda activate storm
   pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una revisión de un tema; Comparar perspectivas antes de escribir
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Investiga un tema acotado y comprueba manualmente dos citas del borrador
**Qué comprobar:** Puedes rastrear las afirmaciones a sus fuentes
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `searxng`, `qdrant`
**Alternativas (elige una):** `gpt-researcher`
