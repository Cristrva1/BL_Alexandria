# Alexandría para agentes · Asistentes e investigación con agentes

Categoría 21 completa (17 repos, 2 subcategorías). Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=21 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `openclaw` | asistentes | Asistente personal de IA que corre en tus dispositivos y te atiende por… | 2 Intermedio | 82 | MIT (OSI permisiva) | recomendado |
| `hermes-agent` | asistentes | Asistente de Nous Research con memoria, skills y herramientas; usa proveedores… | 2 Intermedio | 74 | MIT (OSI permisiva) | alternativa |
| `deeptutor` | asistentes | Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus… | 2 Intermedio | 69 | Apache-2.0 (OSI permisiva) | sin grupo |
| `ruflo` | asistentes | Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes… | 3 Avanzado | 69 | MIT (OSI permisiva) | sin grupo |
| `openbot` | asistentes | Espacio autoalojable de CopilotKit para compañeros de IA con navegador propio… | 2 Intermedio | 67 | MIT (OSI permisiva) | recomendado |
| `paperclip` | asistentes | Servidor y panel para organizar equipos de agentes con objetivos, tareas… | 3 Avanzado | 67 | MIT (OSI permisiva) | recomendado |
| `multica` | asistentes | Workspace para asignar y revisar trabajo de agentes de código mediante sus CLI… | 2 Intermedio | 56 | Apache-2.0 con condiciones adicionales (open-core) | alternativa |
| `agentes-chat` | asistentes | Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que… | 2 Intermedio | 50 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `hello-halo` | asistentes | Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con… | 1 Básico | 50 | MIT con términos adicionales (OSI permisiva) | sin grupo |
| `mercury-agent` | asistentes | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por… | 1 Básico | 49 | MIT (OSI permisiva) | alternativa |
| `opendots` | asistentes | Interfaz abierta de asistentes persistentes que requiere CopilotKit… | 2 Intermedio | 48 | MIT (OSI permisiva) | alternativa |
| `social-media-agent` | asistentes | Agente de LangChain que convierte enlaces en publicaciones para redes sociales… | 2 Intermedio | 46 | MIT (OSI permisiva) | sin grupo |
| `deer-flow` | research | Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con… | 2 Intermedio | 67 | MIT (OSI permisiva) | sin grupo |
| `gpt-researcher` | research | Agente autónomo que investiga en línea y consolida reportes citados y… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | recomendado |
| `storm` | research | Sistema de Stanford que investiga un tema en la web y escribe un informe largo… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `local-deep-research` | research | Agente de investigación que combina buscadores, documentos y modelos locales o… | 2 Intermedio | 58 | MIT (OSI permisiva) | alternativa |
| `autoresearch` | research | Experimento para iterar sobre entrenamiento de nanochat con un agente de código… | 3 Avanzado | 48 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OpenClaw (`openclaw`)

- **Repo:** https://github.com/openclaw/openclaw · MIT · nivel 2 · 82/100 · recomendado en «Asistentes personales autónomos»
- **Qué es:** OpenClaw, asistente de IA personal open source que corre en tu equipo y atiende en tus canales de chat. Licencia MIT. Lo desarrolla la OpenClaw Foundation, una organización 501(c)(3) independiente, y es el repo con más estrellas del…
- **Cuándo elegirlo:** Casos: Probar un asistente personal; Conectar un agente a un canal propio.
- **Requisitos:** nivel 2: preparación media; Node compatible o instalador; proveedor o harness; canal de prueba opcional; hardware prerequisites; API de IA: opcional; Node compatible o instalador; proveedor o harness; canal de prueba opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g openclaw@latest --allow-scripts=openclaw` — fuente: https://github.com/openclaw/openclaw/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Completa onboarding y consulta gateway status y dashboard antes de conectar mensajería Éxito: Puedes identificar estado, proveedor y permisos del Gateway
- **Combina con:** `nemoclaw` [22/infra], `claude-mem` [6/memoria], `claude-code` [20/terminal], `ollama` [8/motores]
- **Alternativas:** `hermes-agent`, `mercury-agent`
- **Riesgos y avisos:** Alternativas (elige una): hermes-agent, mercury-agent. Superficie de ataque amplia (canales y credenciales): conviene aislarlo. La interfaz y memoria locales no mantienen locales los prompts enviados a proveedores; el backend Claude CLI usa el ejecutable autenticado y Codex tiene su….

### hermes-agent (`hermes-agent`)

- **Repo:** https://github.com/NousResearch/hermes-agent · MIT · nivel 2 · 74/100 · alternativa en «Asistentes personales autónomos»
- **Qué es:** Hermes Agent, agente de Nous Research que se mejora a sí mismo. Licencia MIT. Es muy activo (~264k estrellas) y tiene versión de escritorio.
- **Cuándo elegirlo:** Casos: Evaluar memoria de un asistente; Comparar un modelo local con Nous Portal.
- **Requisitos:** nivel 2: preparación media; Equipo compatible; proveedor o endpoint local; perfil de prueba; hardware prerequisites; API de IA: opcional; Equipo compatible; proveedor o endpoint local; perfil de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash` — fuente: https://github.com/NousResearch/hermes-agent/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un perfil nuevo y pide recordar una nota ficticia antes de importar historial Éxito: Puedes comprobar la nota guardada y el proveedor usado
- **Combina con:** `nemoclaw` [22/infra], `ollama` [8/motores], `ecc` [2/metodologia]
- **Alternativas:** `openclaw`, `mercury-agent`
- **Riesgos y avisos:** Alternativas (elige una): openclaw, mercury-agent. Importar ajustes e historial de Claude Code no equivale a usar su plan como motor; las herramientas de búsqueda, voz e imagen tienen proveedores separados.

### DeepTutor (`deeptutor`)

- **Repo:** https://github.com/HKUDS/DeepTutor · Apache-2.0 · nivel 2 · 69/100
- **Qué es:** DeepTutor, sistema de tutoría personalizada con agentes, de la organización HKUDS. Licencia Apache-2.0. Es muy activo, con releases casi semanales (v1.7.3), tiene ~60k estrellas y busca mantenedores.
- **Cuándo elegirlo:** Casos: Estudiar un tema desde apuntes propios; Preparar preguntas de repaso.
- **Requisitos:** nivel 2: preparación media; Python y paquete completo o Docker; modelo y embeddings; documento corto propio; hardware prerequisites; API de IA: opcional; Python y paquete completo o Docker; modelo y embeddings; documento corto propio.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/HKUDS/DeepTutor/blob/main/README.md

  ```bash
  mkdir -p my-deeptutor && cd my-deeptutor
  python -m pip install -U "deeptutor[full]"
  deeptutor init     # ports + LLM provider + optional embedding/search
  deeptutor start    # starts backend + frontend
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una base con un texto breve y pide una explicación con referencias al contenido Éxito: Puedes contrastar la respuesta con fragmentos del texto
- **Combina con:** `lightrag` [6/rag], `docling` [13/conversion], `ollama` [8/motores]
- **Alternativas:** `open-notebook`
- **Riesgos y avisos:** Alternativas (elige una): open-notebook. Documenta consultas a Claude Code, Codex y Antigravity; la conexión del agente, la generación principal y los embeddings son configuraciones diferentes.

### ruflo (`ruflo`)

- **Repo:** https://github.com/ruvnet/ruflo · MIT · nivel 3 · 69/100
- **Qué es:** Ruflo, meta-harness de agentes para Claude Code y Codex, de @ruvnet. Licencia MIT. Tiene ~82k estrellas y está activo; el README es muy promocional (swarms, federación, ruOS).
- **Cuándo elegirlo:** Casos: Coordinar tareas de código; Estudiar memoria compartida entre agentes.
- **Requisitos:** nivel 3: preparación pesada; Node; carpeta de proyecto; Claude Code o cliente MCP; modelo para agentes; hardware prerequisites; API de IA: opcional; Node; carpeta de proyecto; Claude Code o cliente MCP; modelo para agentes.
- **Instalación (documentada en la fuente; no ejecutada):** `npx ruflo@latest init` — fuente: https://github.com/ruvnet/ruflo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Inicializa una carpeta de prueba y examina los agentes, hooks y configuración añadidos antes de encargar trabajo Éxito: Puedes identificar los archivos creados y herramientas MCP disponibles
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Se quita mem0 de las combinaciones porque ruflo trae su propia memoria. Cuidado con las afirmaciones de marketing. Claude Code tiene integración de proyecto; otros clientes usan el servidor MCP estándar y no heredan necesariamente sus hooks ni todas las funciones.

### OpenBot (`openbot`)

- **Repo:** https://github.com/CopilotKit/OpenBot · MIT · nivel 2 · 67/100 · recomendado en «Espacios de asistentes de CopilotKit»
- **Qué es:** Plataforma de CopilotKit (creadores de AG-UI) para «compañeros de trabajo» de IA autoalojables, en TypeScript. La plantilla es MIT, pero necesita CopilotKit Intelligence, con licencia aparte: gratuita en local para uso personal, de prueba…
- **Cuándo elegirlo:** Casos: Dar a un asistente un navegador propio con aprobaciones; Conectar un agente existente por AG-UI a un espacio común. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 2: preparación pesada, app o instalador listo para usar; TypeScript, docker-compose.yml, package.json; hardware prerequisites; API de IA: depends; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 3001:3001 --env-file .env -e EMBEDDED_POSTGRES=on -v openbot-data:/var/lib/postgresql ghcr.io/copilotkit/openbot:latest` — fuente: https://github.com/CopilotKit/OpenBot/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la app de escritorio, configura un modelo y pide una búsqueda web que requiera aprobación Éxito: La acción queda pendiente de tu aprobación y aparece en la auditoría
- **Combina con:** `copilotkit` [9/ia-ui], `langgraph` [3/py], `mastra` [3/ts], `crewai` [3/py], `firecrawl` [4/crawlers], `composio` [22/infra]
- **Alternativas:** `opendots`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativa (elige una): opendots. OpenDots es ahora una «skin» de OpenBot y su repositorio queda como starter mantenido por la comunidad.

### paperclip (`paperclip`)

- **Repo:** https://github.com/paperclipai/paperclip · MIT · nivel 3 · 67/100 · recomendado en «Paneles para coordinar equipos de agentes»
- **Qué es:** Paperclip, servidor Node.js con interfaz React para orquestar equipos de agentes de IA como si fueran una empresa. Licencia MIT. Creado en marzo de 2026, ya tiene ~114k estrellas; hay lista de espera para un servicio cloud.
- **Cuándo elegirlo:** Casos: Organizar tareas de varios agentes; Auditar una propuesta antes de aprobarla.
- **Requisitos:** nivel 3: preparación pesada; Node 24.11+; pnpm 9.15+ para desarrollo; agentes configurados; proyecto de prueba; hardware prerequisites; API de IA: opcional; Node 24.11+; pnpm 9.15+ para desarrollo; agentes configurados; proyecto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/paperclipai/paperclip.git` — fuente: https://github.com/paperclipai/paperclip/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una tarea de explicación para un agente y revisa historial y presupuesto antes de activar heartbeats Éxito: Puedes atribuir una ejecución a su tarea, agente y coste registrado
- **Combina con:** `openclaw`, `claude-code` [20/terminal], `codex` [20/terminal], `hermes-agent`
- **Alternativas:** `multica`
- **Riesgos y avisos:** Alternativa (elige una): multica. Conviene vigilar el gasto con presupuestos. El panel organiza trabajo y no constituye por sí solo una empresa autónoma; las integraciones Claude y Codex dependen de sus adaptadores y cuentas.

### multica (`multica`)

- **Repo:** https://github.com/multica-ai/multica · Apache-2.0 con condiciones adicionales · nivel 2 · 56/100 · alternativa en «Paneles para coordinar equipos de agentes»
- **Qué es:** Multica, workspace para asignar trabajo a agentes de programación como si fueran compañeros de equipo, de multica-ai, escrito en Go. Es source-available: «Multica License», Apache-2.0 con condiciones adicionales sobre servicios alojados…
- **Cuándo elegirlo:** Casos: Organizar trabajo entre agentes; Revisar entregas en un espacio compartido.
- **Requisitos:** nivel 2: preparación media; Un CLI de agente instalado y autenticado; Docker si autoalojas servidor; hardware prerequisites; API de IA: opcional; Un CLI de agente instalado y autenticado; Docker si autoalojas servidor.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --with-server` — fuente: https://github.com/multica-ai/multica/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Asigna una tarea de explicación a un agente en un proyecto de prueba antes de crear automatizaciones Éxito: Puedes ver tarea, sesión y resultado atribuibles al agente
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal], `andrej-karpathy-skills` [2/metodologia]
- **Alternativas:** `paperclip`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): paperclip. Se quitan ruflo y chatwoot (sin relación documentada). La licencia no es OSI. Se declara source-available con licencia Multica que añade condiciones a Apache; no debe resumirse como Apache puro ni como una garantía de sustituir empleados.

### agentes-chat (`agentes-chat`)

- **Repo:** https://github.com/agentes-chat/agentes-chat · AGPL-3.0 · nivel 2 · 50/100
- **Qué es:** agentes.chat, alternativa autoalojada a Slack donde trabajan juntos personas y agentes de IA, de Codari Global, LLC. Licencia AGPL-3.0, con licencia comercial y CLA.
- **Cuándo elegirlo:** Casos: Evaluar un espacio de colaboración con agentes; Organizar consultas en canales.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker Compose y PostgreSQL; proveedor o computadora conectada; equipo de prueba; hardware prerequisites; API de IA: opcional; Docker Compose y PostgreSQL; proveedor o computadora conectada; equipo de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://agentes.chat/install | sh` — fuente: https://github.com/agentes-chat/agentes-chat/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un canal de prueba y pide al agente una respuesta sin conectar acciones externas Éxito: Puedes revisar conversación, herramientas permitidas y aprobaciones
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `github-mcp-server` [5/servidores]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Proyecto muy joven. Claude Code puede usarse en computadora conectada; la ruta Codex está todavía en pruebas y no se presenta como verificación de producción.

### hello-halo (`hello-halo`)

- **Repo:** https://github.com/openkursar/hello-halo · MIT con términos adicionales · nivel 1 · 50/100
- **Qué es:** Halo AI Workstation, estación de trabajo de IA de escritorio open source, de OpenKursar. El LICENSE es MIT (GitHub muestra NOASSERTION). Tiene ~1.9k estrellas (v3.0.5).
- **Cuándo elegirlo:** Casos: Explorar un asistente de escritorio; Revisar tareas de código visualmente.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Aplicación para tu sistema; cuenta o proveedor compatible; carpeta de prueba; hardware prerequisites; API de IA: opcional; Aplicación para tu sistema; cuenta o proveedor compatible; carpeta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/openkursar/hello-halo.git` — fuente: https://github.com/openkursar/hello-halo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un espacio con un archivo de ejemplo y solicita una explicación antes de activar control del navegador Éxito: Puedes revisar el motor y los cambios propuestos
- **Combina con:** `anthropic-skills` [2/catalogos], `context7` [5/servidores], `playwright-mcp` [5/servidores]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Integra motores Claude Code y Codex; que Halo SDK esté orientado a modelos abiertos no confirma por sí solo inferencia local configurada.

### Mercury Agent (`mercury-agent`)

- **Repo:** https://github.com/cosmicstack-labs/mercury-agent · MIT · nivel 1 · 49/100 · alternativa en «Asistentes personales autónomos»
- **Qué es:** Mercury, agente personal open source «con alma» (personalidad escrita por el usuario), de cosmicstack-labs. Licencia MIT. Tiene ~4k estrellas.
- **Cuándo elegirlo:** Casos: Probar un asistente persistente; Estudiar presupuestos de tokens.
- **Requisitos:** nivel 1: preparación sencilla; Node 22 o posterior; proveedor u Ollama/LM Studio; perfil de prueba; hardware prerequisites; API de IA: opcional; Node 22 o posterior; proveedor u Ollama/LM Studio; perfil de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i -g @cosmicstack/mercury-agent` — fuente: https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca mercury, comprueba status y pide una respuesta sobre una nota ficticia sin conectar canales Éxito: Puedes identificar proveedor, servicio en segundo plano y permisos
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `searxng` [4/busqueda]
- **Alternativas:** `openclaw`, `hermes-agent`
- **Riesgos y avisos:** Alternativas (elige una): openclaw, hermes-agent. Se quita claude-mem (es un plugin de Claude Code y OpenClaw, no de Mercury). El asistente inicia un servicio en segundo plano; revisa su estado antes de añadir canales o ejecución programada.

### OpenDots (`opendots`)

- **Repo:** https://github.com/CopilotKit/OpenDots · MIT · nivel 2 · 48/100 · alternativa en «Espacios de asistentes de CopilotKit»
- **Qué es:** OpenDots, plantilla open source de CopilotKit para agentes persistentes, cada uno con su propio ordenador, en web y móvil. Licencia MIT. Tiene ~6.6k estrellas; CopilotKit ofrece ahora la versión más robusta como skin de OpenBot.
- **Cuándo elegirlo:** Casos: Probar un asistente persistente; Estudiar aprobación de acciones conectadas.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Node; CopilotKit Intelligence; proveedores y conectores elegidos; hardware prerequisites; API de IA: sí; Node; CopilotKit Intelligence; proveedores y conectores elegidos.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/CopilotKit/OpenDots/blob/main/README.md

  ```sh
  git clone https://github.com/CopilotKit/OpenDots.git
  cd OpenDots
  npm ci
  cp .env.example .env
  npm run dev
  ```
- **Primera prueba propuesta (no ejecutada):** Configura un Dot de prueba y haz una pregunta sin conceder herramientas de escritura Éxito: Puedes comprobar la respuesta y el panel de conexiones
- **Combina con:** `copilotkit` [9/ia-ui], `composio` [22/infra], `servers` [5/servidores]
- **Alternativas:** `openbot`
- **Riesgos y avisos:** Alternativa (elige una): openbot. No es autónomo del todo: depende de un servicio de CopilotKit. Autoalojar OpenDots no incluye automáticamente el servicio Intelligence ni una pila enteramente local.

### social-media-agent (`social-media-agent`)

- **Repo:** https://github.com/langchain-ai/social-media-agent · MIT · nivel 2 · 46/100
- **Qué es:** Social Media Agent, agente de ejemplo de LangChain que convierte una URL en publicaciones para X y LinkedIn. Licencia MIT. Tiene ~3k estrellas; es más una plantilla que un producto.
- **Cuándo elegirlo:** Casos: Preparar una propuesta para LinkedIn; Convertir un artículo en un borrador corto.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Node y Yarn; claves de modelo y servicios; cuentas sociales solo al conectar publicación; hardware prerequisites; API de IA: sí; Node y Yarn; claves de modelo y servicios; cuentas sociales solo al conectar publicación.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/langchain-ai/social-media-agent/blob/main/README.md

  ```bash
  git clone https://github.com/langchain-ai/social-media-agent.git
  
  yarn install
  ```
- **Primera prueba propuesta (no ejecutada):** Genera un borrador desde un enlace propio y recházalo o edítalo sin publicarlo Éxito: Puedes revisar texto y aprobación antes de cualquier publicación
- **Combina con:** `langgraphjs` [3/ts], `firecrawl` [4/crawlers], `supabase` [22/infraestructura]
- **Riesgos y avisos:** Sin alternativas declaradas. Publica en cuentas reales: revisa siempre antes de aprobar. El flujo incluye revisión humana; configurar el servidor local no evita las claves y permisos que requieren las integraciones.

### deer-flow (`deer-flow`)

- **Repo:** https://github.com/bytedance/deer-flow · MIT · nivel 2 · 67/100
- **Qué es:** DeerFlow 2.0, «super agent harness» open source de ByteDance, construido sobre LangGraph y LangChain. Licencia MIT. Es una reescritura completa sin código compartido con la v1 (el framework Deep Research sigue en la rama 1.x), tiene ~85k…
- **Cuándo elegirlo:** Casos: Investigar un tema con fuentes; Coordinar una generación de informe.
- **Requisitos:** nivel 2: preparación media; Docker o entorno de desarrollo; modelo configurado; carpeta de prueba; hardware prerequisites; API de IA: depends; Docker o entorno de desarrollo; modelo configurado; carpeta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/bytedance/deer-flow/blob/main/README.md

  ```bash
  git clone https://github.com/bytedance/deer-flow.git
  cd deer-flow
  make setup          # interactive wizard: writes config.yaml and .env (about 2 minutes)
  ```
- **Primera prueba propuesta (no ejecutada):** Completa setup y solicita un informe corto con fuentes antes de habilitar herramientas de escritura Éxito: Puedes contrastar las referencias y revisar las acciones del agente
- **Combina con:** `langgraph` [3/py], `firecrawl` [4/crawlers], `searxng` [4/busqueda], `sandbox` [22/infra]
- **Riesgos y avisos:** Sin alternativas declaradas; se solapa con gpt-researcher en el modo investigación (solo anotado). Documenta el skill claude-to-deerflow para controlar una instancia activa; pedir a Codex que instale el proyecto no demuestra una integración runtime con Codex.

### gpt-researcher (`gpt-researcher`)

- **Repo:** https://github.com/assafelovic/gpt-researcher · Apache-2.0 · nivel 2 · 61/100 · recomendado en «Agentes de investigación autónoma»
- **Qué es:** GPT Researcher, agente open source de investigación profunda en web y documentos locales, de @assafelovic. Licencia Apache-2.0. Es maduro (desde 2023, ~31k estrellas, v3.8.0).
- **Cuándo elegirlo:** Casos: Preparar un informe de mercado con fuentes; Investigar documentación técnica.
- **Requisitos:** nivel 2: preparación media; Python 3.11+; proveedor y buscador; cliente MCP solo si eliges esa ruta; hardware prerequisites; API de IA: opcional; Python 3.11+; proveedor y buscador; cliente MCP solo si eliges esa ruta.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install gpt-researcher` — fuente: https://github.com/assafelovic/gpt-researcher/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Haz una pregunta acotada y verifica dos fuentes antes de reutilizar el informe Éxito: Puedes recuperar contexto y enlaces que respaldan conclusiones
- **Combina con:** `claude-code` [20/terminal], `firecrawl` [4/crawlers], `ollama` [8/motores], `searxng` [4/busqueda]
- **Alternativas:** `storm`, `local-deep-research`, `vane`
- **Riesgos y avisos:** Alternativas (elige una): storm, vane, local-deep-research. Se quita browser-use de las combinaciones (no hay integración documentada). El MCP está ahora en gptr-mcp, proyecto compañero con stdio y transportes de red; el skill y el servidor de investigación requieren configuración propia.

### STORM (`storm`)

- **Repo:** https://github.com/stanford-oval/storm · MIT · nivel 2 · 60/100 · alternativa en «Agentes de investigación autónoma»
- **Qué es:** STORM y Co-STORM, sistemas de investigación de Stanford OVAL (artículos en NAACL y EMNLP 2024) que escriben informes tipo Wikipedia con citas. Licencia MIT. Tiene ~32k estrellas, pero sin cambios desde septiembre de 2025.
- **Cuándo elegirlo:** Casos: Preparar una revisión de un tema; Comparar perspectivas antes de escribir.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Conda y Python 3.11; modelo; credenciales del buscador configurado; hardware prerequisites; API de IA: sí; Conda y Python 3.11; modelo; credenciales del buscador configurado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/stanford-oval/storm/blob/main/README.md

  ```shell
  git clone https://github.com/stanford-oval/storm.git
      cd storm
  
  conda create -n storm python=3.11
     conda activate storm
     pip install -r requirements.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Investiga un tema acotado y comprueba manualmente dos citas del borrador Éxito: Puedes rastrear las afirmaciones a sus fuentes
- **Combina con:** `litellm` [23/serving], `searxng` [4/busqueda], `qdrant` [6/vectores]
- **Alternativas:** `gpt-researcher`, `local-deep-research`
- **Riesgos y avisos:** Alternativas (elige una): gpt-researcher. Actividad baja. Las citas y el texto generado requieren revisión; una interfaz de modelo configurable no confirma una ruta local lista para usar.

### local-deep-research (`local-deep-research`)

- **Repo:** https://github.com/LearningCircuit/local-deep-research · MIT · nivel 2 · 58/100 · alternativa en «Agentes de investigación autónoma»
- **Qué es:** Local Deep Research, asistente de investigación agéntica que puede ejecutarse totalmente en local, de LearningCircuit. Licencia MIT. Tiene ~9.6k estrellas (v2.0.1); según su propio README, alcanza ~95% en SimpleQA con Qwen3.6-27B en una…
- **Cuándo elegirlo:** Casos: Consultar documentos privados; Preparar una revisión bibliográfica.
- **Requisitos:** nivel 2: preparación media; Modelo local o remoto; buscador; Python o Docker; equipo adecuado al modelo; hardware prerequisites; API de IA: opcional; Modelo local o remoto; buscador; Python o Docker; equipo adecuado al modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install local-deep-research` — fuente: https://github.com/LearningCircuit/local-deep-research/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Investiga una pregunta pequeña con Ollama y SearXNG y abre las fuentes citadas Éxito: Puedes identificar buscador, modelo y evidencia utilizada
- **Combina con:** `ollama` [8/motores], `searxng` [4/busqueda], `llama-cpp` [8/motores]
- **Alternativas:** `gpt-researcher`, `storm`
- **Riesgos y avisos:** Alternativa (elige una): gpt-researcher. El MCP documentado usa stdio para uso local y carece de autenticación y límite de peticiones; el benchmark del autor no garantiza exactitud en cualquier tema.

### autoresearch (`autoresearch`)

- **Repo:** https://github.com/karpathy/autoresearch · — · nivel 3 · 48/100
- **Qué es:** autoresearch, experimento de @karpathy en el que un agente investiga de forma autónoma sobre el entrenamiento de nanochat con una sola GPU. Licencia MIT según el README, pero sin archivo LICENSE (GitHub no detecta licencia).
- **Cuándo elegirlo:** Casos: Estudiar optimización de entrenamiento; Aprender a registrar experimentos reproducibles.
- **Requisitos:** nivel 3: preparación media, necesita GPU; GPU NVIDIA; Python 3.10+; uv; agente y presupuesto de cómputo; hardware prerequisites; API de IA: no; GPU NVIDIA; Python 3.10+; uv; agente y presupuesto de cómputo.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/karpathy/autoresearch/blob/master/README.md

  ```bash
  # 2. Install dependencies
  uv sync
  ```
- **Primera prueba propuesta (no ejecutada):** Lee program.md y ejecuta primero un experimento manual pequeño antes de permitir iteraciones Éxito: Puedes comparar métrica y cambio concreto del experimento
- **Combina con:** `nanochat` [19/aprender], `claude-code` [20/terminal], `codex` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Se quitan gpt-researcher y crawl4ai: es investigación en entrenamiento de modelos, no en la web. Probado por el autor en H100 y no diseñado actualmente para CPU o MPS; no se traslada su sugerencia de desactivar permisos como requisito para principiantes.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-21.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Asistentes e investigación con agentes», lee `docs/alexandria/categoria-21.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-21.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
