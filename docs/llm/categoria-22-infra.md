# Alexandría para agentes · Infraestructura: sandboxes, herramientas y protocolos

Categoría 22 «Infraestructura, despliegue y herramientas para agentes» › subcategoría `infra`. 13 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=22&sub=infra · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `composio` | Plataforma con más de 1000 integraciones con autenticación gestionada para que… | 1 Básico | 74 | MIT (OSI permisiva) | sin grupo |
| `nemoclaw` | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de… | 3 Avanzado | 69 | Apache-2.0 (OSI permisiva) | recomendado |
| `agent-desktop` | CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y… | 2 Intermedio | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `e2b` | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y… | 1 Básico | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `sandbox` | Entorno sandbox all-in-one para agentes que reúne navegador, terminal… | 2 Intermedio | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `shepherd` | Capa de ejecución que registra acciones y estado de un agente para permitir… | 2 Intermedio | 49 | MIT (OSI permisiva) | sin grupo |
| `agent-protocol` | Especificación de LangChain para exponer cualquier agente con una API estándar… | 1 Básico | 48 | MIT (OSI permisiva) | sin grupo |
| `nodeterm` | Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con… | 2 Intermedio | 48 | BUSL-1.1 (source-available) | sin grupo |
| `computer-use-preview` | Implementación de referencia de Google para que Gemini vea la pantalla y opere… | 2 Intermedio | 45 | Apache-2.0 (OSI permisiva) | sin grupo |
| `claude-task-master` | Sistema de gestión de tareas con IA que prepara y organiza trabajo de… | 2 Intermedio | 42 | MIT + Commons Clause (source-available) | sin grupo |
| `agent-substrate` | Aloja tareas con estado en Kubernetes y permite probar cómo se suspenden y… | 3 Avanzado | — | Apache-2.0 | sin grupo |
| `kiri` | Ejecuta contenedores de desarrollo y permite verlos desde una aplicación de… | 2 Intermedio | — | Apache-2.0 | sin grupo |
| `screen-relay` | Muestra en el navegador un escritorio de prueba para ver una aplicación gráfica… | 3 Avanzado | — | Apache-2.0 | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Composio (`composio`)

- **Repo:** https://github.com/ComposioHQ/composio · MIT · nivel 1 · 74/100
- **Qué es:** Composio, monorepo de SDKs que da a los agentes más de 1000 toolkits preautenticados, de ComposioHQ. Licencia MIT para los SDKs; la plataforma es un servicio con API key. Tiene ~31k estrellas.
- **Cuándo elegirlo:** Casos: Conectar un agente a un CRM; Explorar herramientas de consulta de un servicio.
- **Requisitos:** nivel 1: preparación sencilla; Cuenta Composio; CLI o SDK; cuenta externa de prueba; hardware prerequisites; API de IA: no; Cuenta Composio; CLI o SDK; cuenta externa de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @composio/core @composio/openai-agents @openai/agents` — fuente: https://github.com/ComposioHQ/composio/blob/next/README.md
- **Primera prueba propuesta (no ejecutada):** Busca una herramienta de consulta y revisa sus permisos antes de enlazar una cuenta Éxito: Puedes identificar acción, aplicación y alcance de autorización
- **Combina con:** `openai-agents-python` [3/py], `langgraph` [3/py], `mastra` [3/ts], `claude-code` [20/terminal], `awesome-claude-skills` [2/catalogos], `openbot` [21/asistentes]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Dependencia de un servicio comercial para las credenciales de terceros. El CLI ofrece una superficie local para Claude Code; el SDK de Claude Agent no equivale a incluir créditos o plan de Claude Code.

### NemoClaw (`nemoclaw`)

- **Repo:** https://github.com/NVIDIA/NemoClaw · Apache-2.0 · nivel 3 · 69/100 · recomendado en «Sandboxes para agentes»
- **Qué es:** NVIDIA NemoClaw, stack de referencia open source para ejecutar agentes con más seguridad dentro de sandboxes NVIDIA OpenShell. Licencia Apache-2.0. Tiene ~23k estrellas y está activo.
- **Cuándo elegirlo:** Casos: Estudiar aislamiento para OpenClaw; Comparar políticas de ejecución de agentes.
- **Requisitos:** nivel 3: preparación pesada; Plataforma compatible según prerequisites; OpenShell; agente y proveedor; hardware prerequisites; API de IA: depends; Plataforma compatible según prerequisites; OpenShell; agente y proveedor.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash` — fuente: https://github.com/NVIDIA/NemoClaw/blob/main/docs/get-started/quickstart.mdx
- **Primera prueba propuesta (no ejecutada):** Lee los requisitos y prueba la política con una tarea de consulta en un entorno descartable Éxito: Puedes identificar los permisos de archivos, red e inferencia configurados
- **Combina con:** `openclaw` [21/asistentes], `hermes-agent` [21/asistentes], `deepagents` [3/py], `nemotron` [24/modelos]
- **Alternativas:** `e2b`, `sandbox`
- **Riesgos y avisos:** Alternativas (elige una): sandbox. El prompt para que Claude Code o Codex ayude a instalar es una guía de instalación asistida y no una integración runtime de sus planes.

### agent-desktop (`agent-desktop`)

- **Repo:** https://github.com/vercel-labs/agent-desktop · Apache-2.0 · nivel 2 · 65/100
- **Qué es:** agent-desktop, CLI y biblioteca de Vercel Labs para que un agente use apps de escritorio en macOS, Windows y Linux a través del árbol de accesibilidad del sistema. Licencia Apache-2.0. Tiene ~24k estrellas y está activo.
- **Cuándo elegirlo:** Casos: Inspeccionar una app de escritorio propia; Preparar una prueba de interfaz.
- **Requisitos:** nivel 2: preparación media; Node; permisos de accesibilidad del sistema; cliente de agente opcional; hardware prerequisites; API de IA: no; Node; permisos de accesibilidad del sistema; cliente de agente opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/vercel-labs/agent-desktop/blob/main/README.md

  ```bash
  npm install -g agent-desktop
  agent-desktop status                # platform, permissions, supported surfaces
  agent-desktop permissions --guide   # macOS: walks you through the Accessibility grant
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta status y permissions --guide y obtén una captura de una ventana de prueba sin pulsar controles Éxito: Puedes comprobar plataforma, permisos y referencias de accesibilidad
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `playwright-mcp` [5/servidores]
- **Riesgos y avisos:** Sin alternativas declaradas; enfoque complementario al de computer-use-preview (accesibilidad frente a píxeles). Ofrece skills portables y MCP stdio; algunas órdenes de teclas o botones mantenidos se rechazan hasta disponer de daemon de liberación.

### E2B (`e2b`)

- **Repo:** https://github.com/e2b-dev/E2B · Apache-2.0 · nivel 1 · 65/100 · alternativa en «Sandboxes para agentes»
- **Qué es:** E2B, infraestructura open source para ejecutar código generado por IA en sandboxes aislados en la nube. Licencia Apache-2.0. Es maduro y activo (~15k estrellas).
- **Cuándo elegirlo:** Casos: Ejecutar código aislado de una app; Preparar un entorno temporal para un agente.
- **Requisitos:** nivel 1: preparación sencilla; Node o Python; cuenta E2B y clave; presupuesto de sandbox; hardware prerequisites; API de IA: no; Node o Python; cuenta E2B y clave; presupuesto de sandbox.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i e2b` — fuente: https://github.com/e2b-dev/E2B/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un sandbox de prueba, ejecuta una operación de texto inocua y ciérralo Éxito: Puedes revisar resultado y ciclo de vida del sandbox
- **Combina con:** `smolagents` [3/py], `open-swe` [20/ingenieria], `computer-use-preview`
- **Alternativas:** `nemoclaw`, `sandbox`
- **Riesgos y avisos:** Alternativas (elige una): sandbox. Instalar el SDK no aloja todo E2B en tu equipo ni incluye un modelo de IA.

### sandbox (`sandbox`)

- **Repo:** https://github.com/agent-infra/sandbox · Apache-2.0 · nivel 2 · 52/100 · alternativa en «Sandboxes para agentes»
- **Qué es:** AIO Sandbox, entorno sandbox todo en uno para agentes (navegador, terminal, archivos, VSCode, Jupyter y MCP en un contenedor), de agent-infra. Licencia Apache-2.0. Tiene ~6.3k estrellas (v1.11.0) y artículo asociado.
- **Cuándo elegirlo:** Casos: Probar herramientas de un agente en un contenedor; Consultar una interfaz de navegador aislada.
- **Requisitos:** nivel 2: preparación media; Docker; recursos para navegador; clave de acceso propia; cliente MCP opcional; hardware prerequisites; API de IA: no; Docker; recursos para navegador; clave de acceso propia; cliente MCP opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/agent-infra/sandbox/blob/main/README.md

  ```bash
  # Recommended: Enable API Key authentication (protects all services: API, JupyterLab, VNC)
  # - Supports three methods: X-AIO-API-Key header, Authorization: Bearer header, ?api_key= query parameter
  # - Without SANDBOX_API_KEY, services remain open (backward compatible)
  docker run --security-opt seccomp=unconfined --rm -it \
    -e SANDBOX_API_KEY=your-secret-key \
    -p 127.0.0.1:8080:8080 ghcr.io/agent-infra/sandbox:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Arranca el contenedor limitado a loopback y consulta el contexto o una captura antes de ejecutar comandos Éxito: Puedes acceder al entorno autenticado y reconocer navegador, terminal y archivos
- **Combina con:** `openhands` [20/ingenieria], `browser-use` [32/agentes-web], `deer-flow` [21/research], `computer-use-preview`
- **Alternativas:** `nemoclaw`, `e2b`
- **Riesgos y avisos:** Alternativas (elige una): nemoclaw, e2b. Se quita ecc (sin relación documentada). Riesgo: sin API key, todo queda expuesto. Expone MCP en /mcp; sin SANDBOX_API_KEY los servicios quedan abiertos y el ejemplo usa seccomp unconfined, por lo que no es una garantía absoluta de aislamiento.

### shepherd (`shepherd`)

- **Repo:** https://github.com/shepherd-agents/shepherd · MIT · nivel 2 · 49/100
- **Qué es:** Shepherd, sustrato de ejecución para meta-agentes programables con trazas de ejecución reversibles, de shepherd-agents. Licencia MIT. Está en alfa temprana con APIs cambiantes, tiene ~2.6k estrellas y artículo citado.
- **Cuándo elegirlo:** Casos: Estudiar reproducción de ejecuciones; Comparar una traza con un resultado final.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python 3.11+; entorno compatible; Claude CLI solo para ejemplo con modelo; hardware prerequisites; API de IA: opcional; Python 3.11+; entorno compatible; Claude CLI solo para ejemplo con modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install shepherd-ai` — fuente: https://github.com/shepherd-agents/shepherd/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Empieza por Offline Quickstart para observar una traza reversible sin llamar un modelo Éxito: Puedes inspeccionar estados y bifurcaciones de la demostración
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Es alfa. La reversibilidad afecta al estado capturado por el runtime y no promete deshacer cualquier efecto externo; la demo offline no es un LLM local.

### Agent Protocol (`agent-protocol`)

- **Repo:** https://github.com/langchain-ai/agent-protocol · MIT · nivel 1 · 48/100
- **Qué es:** Agent Protocol, especificación de LangChain de APIs independientes del framework para servir agentes LLM en producción. Licencia MIT. Es una especificación de nicho (~700 estrellas).
- **Cuándo elegirlo:** Casos: Diseñar una API de agentes; Comparar protocolos antes de implementar.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; nociones de HTTP; hardware prerequisites; API de IA: no; Navegador; nociones de HTTP.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/langchain-ai/agent-protocol/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee las rutas threads y runs y dibuja cómo una aplicación inicia y consulta una ejecución Éxito: Puedes distinguir estado del hilo y ejecución del agente
- **Combina con:** `langgraph` [3/py], `langgraphjs` [3/ts], `deepagents` [3/py]
- **Riesgos y avisos:** Sin alternativas declaradas. Es una especificación de API y no MCP ni un servidor instalable; los bloques Hurl ilustran peticiones y no son comandos de terminal normales.

### nodeterm (`nodeterm`)

- **Repo:** https://github.com/eneskirca/nodeterm · BUSL-1.1 · nivel 2 · 48/100
- **Qué es:** nodeterm, gestor de terminales y sesiones de agentes sobre un lienzo infinito, de @eneskirca. Licencia Business Source License 1.1 (no es open source; GitHub muestra NOASSERTION). Tiene ~2.5k estrellas y busca patrocinadores fundadores.
- **Cuándo elegirlo:** Casos: Organizar varias sesiones de código; Asociar sesiones con worktrees.
- **Requisitos:** nivel 2: preparación media; macOS o Linux; tmux según ruta; CLI de agente autenticado; hardware prerequisites; API de IA: opcional; macOS o Linux; tmux según ruta; CLI de agente autenticado.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install --cask nodeterm` — fuente: https://github.com/eneskirca/nodeterm/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un terminal y un nodo de agente para explicar una carpeta de prueba Éxito: Puedes ver sesión, terminal y contexto de proyecto
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal]
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Licencia BUSL: revisa las restricciones de uso. Documenta Claude Code, Codex y Antigravity; la licencia BUSL-1.1 y sus límites no deben presentarse como MIT sin restricciones; local aquí incluye dictado, no….

### Gemini Computer Use (preview) (`computer-use-preview`)

- **Repo:** https://github.com/google-gemini/computer-use-preview · Apache-2.0 · nivel 2 · 45/100
- **Qué es:** Computer Use Preview, implementación de referencia de Google para que Gemini controle un navegador. Licencia Apache-2.0. Tiene ~3.3k estrellas y no cambia desde julio de 2026.
- **Cuándo elegirlo:** Casos: Estudiar automatización visual de navegador; Evaluar tareas de formularios ficticios.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Python; navegador y dependencias; Gemini Developer API o Vertex AI; entorno de prueba; hardware prerequisites; API de IA: sí; Python; navegador y dependencias; Gemini Developer API o Vertex AI; entorno de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/google-gemini/computer-use-preview/blob/main/README.md

  ```bash
  git clone https://github.com/google-gemini/computer-use-preview.git
  cd computer-use-preview
  
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Usa una página de prueba y solicita localizar un elemento sin cuentas personales ni acciones reales Éxito: Puedes comparar la captura y la acción propuesta
- **Combina con:** `playwright` [32/bibliotecas], `sandbox`, `e2b`
- **Alternativas:** `browser-use`, `skyvern`
- **Riesgos y avisos:** Alternativas (elige una): browser-use, skyvern. Es una referencia, no un producto. Es una implementación de referencia y no un servidor genérico que se instala automáticamente en Claude Code, Codex o Antigravity.

### claude-task-master (`claude-task-master`)

- **Repo:** https://github.com/eyaltoledano/claude-task-master · MIT + Commons Clause · nivel 2 · 42/100
- **Qué es:** Taskmaster, sistema de gestión de tareas para desarrollo con IA, de @eyaltoledano y @RalphEcom. Licencia MIT con Commons Clause (no OSI; GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Descomponer un proyecto web; Revisar orden y dependencias de tareas.
- **Requisitos:** nivel 2: preparación media; Node; cliente MCP; proveedor o CLI Claude Code/Codex configurado; PRD ficticio; hardware prerequisites; API de IA: opcional; Node; cliente MCP; proveedor o CLI Claude Code/Codex configurado; PRD ficticio.
- **Instalación (documentada en la fuente; no ejecutada):** `claude mcp add taskmaster-ai -- npx -y task-master-ai` — fuente: https://github.com/eyaltoledano/claude-task-master/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte una especificación corta de prueba en tareas y revisa dependencias antes de ejecutarlas Éxito: Puedes rastrear cada tarea a un requisito
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal]
- **Alternativas:** `spec-kit`
- **Riesgos y avisos:** Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): spec-kit. Actividad reciente baja. Ofrece MCP estándar para el cliente y backends específicos para el modelo; un campo OLLAMA_API_KEY no basta para asegurar inferencia local sin comprobar la….

### Agent Substrate (`agent-substrate`)

- **Repo:** https://github.com/agent-substrate/substrate · Apache-2.0 · nivel 3 · —/100
- **Qué es:** Una plataforma de infraestructura para ejecutar trabajos con estado en Kubernetes.
- **Cuándo elegirlo:** Casos: Comparar dos llamadas al contador de demostración.; Estudiar en un clúster de prueba qué datos se guardan cuando una tarea se suspende.
- **Requisitos:** nivel 3: preparación pesada, despliegue con Kubernetes/Helm; Go, go.mod; hardware prerequisites; API de IA: no; Go, kubectl, Docker y un equipo capaz de ejecutar un clúster local de kind..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/get-started/quickstart.md
- **Primera prueba propuesta (no ejecutada):** Despliega el contador oficial sin cuentas de nube ni secretos reales y haz dos consultas mediante su proxy local. Éxito: El contador aumenta y responde de nuevo tras reanudar la tarea, con el estado de prueba conservado.
- **Riesgos y avisos:** La instalación crea recursos del clúster, controladores y almacenamiento de instantáneas. Usa un clúster de prueba sin credenciales reales ni cargas de….

### Kiri (`kiri`)

- **Repo:** https://github.com/libracoder/kiri · Apache-2.0 · nivel 2 · —/100
- **Qué es:** Un motor con interfaz para contenedores de desarrollo en un equipo personal.
- **Cuándo elegirlo:** Casos: Arrancar un contenedor de demostración sin montar carpetas personales.; Comprobar que un proyecto de ejemplo usa el contexto de Kiri en lugar del de Docker habitual.
- **Requisitos:** nivel 2: preparación media; Rust, Cargo.toml; hardware prerequisites; API de IA: no; En Windows requiere WSL 2; en macOS, macOS 14 o posterior según el README; en Linux, la distribución indicada por el proyecto..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/libracoder/kiri/releases/tag/v0.2.2
- **Primera prueba propuesta (no ejecutada):** En un equipo o entorno de prueba, ejecuta un contenedor de imagen conocida, sin montar archivos del anfitrión ni activar túneles. Éxito: La salida del contenedor es visible y el contexto seleccionado sigue siendo el de Kiri.
- **Riesgos y avisos:** Los siete avisos publicados señalan v0.2.2 como corregida. El motor tiene permisos sobre red y volúmenes; también puede crear una CA para los dominios locales.

### Screen Relay (`screen-relay`)

- **Repo:** https://github.com/vercel-labs/screen-relay · Apache-2.0 · nivel 3 · —/100
- **Qué es:** Una herramienta para transmitir y controlar pantallas de trabajo propias, pensada también para escritorios de prueba.
- **Cuándo elegirlo:** Casos: Mirar la interfaz de una aplicación de prueba en un escritorio vacío.; Capturar una ventana de demostración en un entorno separado.
- **Requisitos:** nivel 3: preparación pesada; C++, Dockerfile, Makefile, package.json; hardware prerequisites; API de IA: no; Docker en una máquina de prueba; Node.js 22 o posterior si eliges la CLI npm en vez de la ruta de contenedor..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/docker.mdx
- **Primera prueba propuesta (no ejecutada):** Abre el visor local con un escritorio vacío. No montes el directorio personal ni conectes cuentas reales. Éxito: El visor muestra el escritorio de prueba en el navegador y deja de estar disponible al cerrar el entorno.
- **Riesgos y avisos:** El visor puede ver pantalla y enviar teclado y ratón. La configuración del tag escucha en loopback por defecto; un bind distinto genera un token.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-22-infra.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Infraestructura: sandboxes, herramientas y protocolos», lee `docs/alexandria/categoria-22-infra.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-22-infra.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
