# Alexandría para agentes · Infraestructura, despliegue y herramientas para agentes

Categoría 22 completa (32 repos, 4 subcategorías). Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=22 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `composio` | infra | Plataforma con más de 1000 integraciones con autenticación gestionada para que… | 1 Básico | 74 | MIT (OSI permisiva) | sin grupo |
| `nemoclaw` | infra | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de… | 3 Avanzado | 69 | Apache-2.0 (OSI permisiva) | recomendado |
| `agent-desktop` | infra | CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y… | 2 Intermedio | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `e2b` | infra | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y… | 1 Básico | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `sandbox` | infra | Entorno sandbox all-in-one para agentes que reúne navegador, terminal… | 2 Intermedio | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `shepherd` | infra | Capa de ejecución que registra acciones y estado de un agente para permitir… | 2 Intermedio | 49 | MIT (OSI permisiva) | sin grupo |
| `agent-protocol` | infra | Especificación de LangChain para exponer cualquier agente con una API estándar… | 1 Básico | 48 | MIT (OSI permisiva) | sin grupo |
| `nodeterm` | infra | Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con… | 2 Intermedio | 48 | BUSL-1.1 (source-available) | sin grupo |
| `computer-use-preview` | infra | Implementación de referencia de Google para que Gemini vea la pantalla y opere… | 2 Intermedio | 45 | Apache-2.0 (OSI permisiva) | sin grupo |
| `claude-task-master` | infra | Sistema de gestión de tareas con IA que prepara y organiza trabajo de… | 2 Intermedio | 42 | MIT + Commons Clause (source-available) | sin grupo |
| `agent-substrate` | infra | Aloja tareas con estado en Kubernetes y permite probar cómo se suspenden y… | 3 Avanzado | — | Apache-2.0 | sin grupo |
| `kiri` | infra | Ejecuta contenedores de desarrollo y permite verlos desde una aplicación de… | 2 Intermedio | — | Apache-2.0 | sin grupo |
| `screen-relay` | infra | Muestra en el navegador un escritorio de prueba para ver una aplicación gráfica… | 3 Avanzado | — | Apache-2.0 | sin grupo |
| `freedomain` | recursos | Recursos de registro de dominios y aprendizaje práctico de DNS publicados por… | 1 Básico | 57 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `free-for-dev` | recursos | Directorio de servicios de infraestructura y desarrollo que ofrecen planes o… | 1 Básico | 47 | — (sin licencia detectada) | sin grupo |
| `headscale` | redes | Implementación abierta y autoalojada del servidor de control de Tailscale para… | 2 Intermedio | 69 | BSD-3-Clause (OSI permisiva) | recomendado |
| `frp` | redes | Proxy inverso rápido para exponer servidores locales detrás de NAT o… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `netbird` | redes | Red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso… | 2 Intermedio | 63 | BSD-3-Clause + AGPL-3.0 (management, signal, relay) (OSI copyleft) | alternativa |
| `wg-easy` | redes | La forma más sencilla de ejecutar WireGuard VPN con interfaz web para gestionar… | 2 Intermedio | 63 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `masterdnsvpn` | redes | Implementación en Go de un túnel que transporta tráfico TCP mediante consultas… | 2 Intermedio | 55 | MIT (OSI permisiva) | sin grupo |
| `pangolin` | redes | Controla qué personas pueden entrar a aplicaciones propias mediante un proxy y… | 3 Avanzado | — | NOASSERTION | sin grupo |
| `tailcat` | redes | Conecta dos equipos propios para el intercambio temporal de datos mediante un… | 2 Intermedio | — | BSD-3-Clause | sin grupo |
| `supabase` | infraestructura | Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras… | 3 Avanzado | 76 | Apache-2.0 (OSI permisiva) | recomendado |
| `coolify` | infraestructura | Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `appwrite` | infraestructura | Plataforma de backend abierta orientada a agentes y desarrolladores… | 2 Intermedio | 73 | BSD-3-Clause (OSI permisiva) | alternativa |
| `uptime-kuma` | infraestructura | Monitor de disponibilidad autoalojado y fácil de usar: comprueba webs y… | 1 Básico | 72 | MIT (OSI permisiva) | sin grupo |
| `caddy` | infraestructura | Servidor web y proxy inverso extensible con HTTPS automático por defecto… | 2 Intermedio | 70 | Apache-2.0 (OSI permisiva) | recomendado |
| `traefik` | infraestructura | Proxy inverso y balanceador de carga dinámico para contenedores y… | 2 Intermedio | 70 | MIT (OSI permisiva) | alternativa |
| `dokploy` | infraestructura | Plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku… | 2 Intermedio | 67 | Apache-2.0 + licencia propietaria (/proprietary) (open-core) | alternativa |
| `portainer` | infraestructura | Interfaz web ligera para gestionar contenedores en Docker, Swarm, Podman… | 1 Básico | 66 | Zlib (OSI permisiva) | sin grupo |
| `casaos` | infraestructura | Entorno para administrar un servidor personal, instalar aplicaciones y… | 1 Básico | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `libretranslate` | infraestructura | Traduce texto con una interfaz web y una API que puedes alojar en tu equipo… | 3 Avanzado | — | AGPL-3.0 | sin grupo |

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

### FreeDomain (`freedomain`)

- **Repo:** https://github.com/DigitalPlatDev/FreeDomain · AGPL-3.0 · nivel 1 · 57/100
- **Qué es:** DigitalPlat FreeDomain, servicio de registro gratuito de subdominios con guías de DNS. El repo contiene información pública y tutoriales; el código de la aplicación está en DigitalPlatDev/Domain-OSS. Licencia AGPL-3.0.
- **Cuándo elegirlo:** Casos: Aprender DNS; Evaluar un dominio para un proyecto personal.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; nombre de dominio de prueba; hardware prerequisites; API de IA: no; Navegador; nombre de dominio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/DigitalPlatDev/FreeDomain/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee las condiciones de registro y dibuja registros DNS para un sitio ficticio sin cambiar dominios activos Éxito: Puedes distinguir registro, DNS y alojamiento
- **Combina con:** `coolify` [22/infraestructura], `free-for-dev`, `masterdnsvpn` [22/redes]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. Recuento de estrellas inusual y canal comprometido: conviene precaución. No se instala un dominio con este README ni se promete disponibilidad o renovación perpetua de cualquier nombre.

### free-for-dev (`free-for-dev`)

- **Repo:** https://github.com/ripienaar/free-for-dev · — · nivel 1 · 47/100
- **Qué es:** free-for.dev, lista curada de servicios SaaS, PaaS e IaaS con niveles gratuitos para desarrolladores de infraestructura, iniciada por @ripienaar. GitHub no detecta licencia.
- **Cuándo elegirlo:** Casos: Encontrar infraestructura para una demo; Comparar niveles gratuitos.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; necesidad y presupuesto; hardware prerequisites; API de IA: no; Navegador; necesidad y presupuesto.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ripienaar/free-for-dev/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Elige un servicio de alojamiento y comprueba sus límites y condiciones en la web del proveedor antes de crear una cuenta Éxito: Puedes distinguir plan gratuito, cuotas y extras de pago
- **Combina con:** `freedomain`, `supabase` [22/infraestructura], `coolify` [22/infraestructura], `masterdnsvpn` [22/redes]
- **Riesgos y avisos:** Sin alternativas declaradas. Recurso, no software. Es un directorio de servicios as-a-Service, no software autoalojado ni una garantía permanente de gratuidad.

### Headscale (`headscale`)

- **Repo:** https://github.com/juanfont/headscale · BSD-3-Clause · nivel 2 · 69/100 · recomendado en «Redes privadas tipo mesh (WireGuard)»
- **Qué es:** Servidor de control de código abierto (BSD-3-Clause) mantenido por la comunidad (Juan Font, Kristoffer Dalby y otros). Maduro; alcance deliberadamente acotado a una sola tailnet para uso personal o pequeñas organizaciones.
- **Cuándo elegirlo:** Casos: conectar tus equipos y servidores en una red privada sin depender del servicio de Tailscale; dar acceso remoto a una red doméstica o de laboratorio.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/juanfont/headscale/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Headscale en un servidor siguiendo su documentación, crea un usuario y registra un cliente de Tailscale con `--login-server`. Éxito: El dispositivo aparece en `headscale nodes list` y alcanza a otros nodos.
- **Combina con:** `caddy` [22/infraestructura], `grafana` [10/bi], `uptime-kuma` [22/infraestructura]
- **Alternativas:** `netbird`
- **Riesgos y avisos:** Alternativas (elige una): netbird. No es un producto oficial de Tailscale.

### frp (`frp`)

- **Repo:** https://github.com/fatedier/frp · Apache-2.0 · nivel 2 · 64/100
- **Qué es:** Proxy inverso de código abierto (Apache-2.0) creado por fatedier. Muy popular y maduro; el README anuncia una arquitectura v2 en desarrollo.
- **Cuándo elegirlo:** Casos: acceder por SSH a un equipo de casa detrás de NAT; publicar temporalmente un servicio web local usando tu propio VPS.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/fatedier/frp/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** En un VPS propio arranca frps y en tu equipo frpc con un proxy TCP para SSH, siguiendo el ejemplo del README. Éxito: Puedes conectar por SSH al equipo local a través del puerto del VPS.
- **Combina con:** `caddy` [22/infraestructura], `uptime-kuma` [22/infraestructura], `home-assistant` [15/domotica]
- **Riesgos y avisos:** Alternativas cercanas: headscale o netbird si prefieres una red privada en lugar de publicar servicios.

### NetBird (`netbird`)

- **Repo:** https://github.com/netbirdio/netbird · BSD-3-Clause + AGPL-3.0 (management, signal, relay) · nivel 2 · 63/100 · alternativa en «Redes privadas tipo mesh (WireGuard)»
- **Qué es:** Plataforma de red de código abierto de NetBird GmbH. El repositorio es BSD-3-Clause salvo management/, signal/ y relay/, que son AGPL-3.0. Muy activa, con nube de pago.
- **Cuándo elegirlo:** Casos: conectar servidores y equipos remotos sin abrir puertos; dar acceso a la red interna con SSO y políticas por grupo.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://pkgs.netbird.io/install.sh | sh` — fuente: https://docs.netbird.io/get-started/install/linux
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de autoalojamiento rápido de NetBird en un VPS y conecta dos dispositivos con el cliente. Éxito: Ambos dispositivos aparecen en el panel y se alcanzan por la red privada.
- **Combina con:** `grafana` [10/bi], `uptime-kuma` [22/infraestructura], `coolify` [22/infraestructura]
- **Alternativas:** `headscale`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): headscale.

### WireGuard Easy (`wg-easy`)

- **Repo:** https://github.com/wg-easy/wg-easy · AGPL-3.0 · nivel 2 · 63/100
- **Qué es:** Proyecto de código abierto (AGPL-3.0) de la comunidad wg-easy. Maduro y activo; no está afiliado a WireGuard.
- **Cuándo elegirlo:** Casos: montar una VPN para acceder a tu red de casa desde el móvil; gestionar clientes de WireGuard sin editar archivos a mano.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo docker compose up / down` — fuente: https://github.com/wg-easy/wg-easy/blob/master/docs/content/getting-started.md
- **Primera prueba propuesta (no ejecutada):** Despliega wg-easy con Docker Compose según su documentación, crea un cliente y escanea el QR con la app de WireGuard. Éxito: El cliente se conecta y aparece activo en el panel.
- **Combina con:** `grafana` [10/bi], `caddy` [22/infraestructura], `pi-hole` [15/privacidad], `portainer` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Para redes malladas con muchos nodos, headscale o netbird encajan mejor.

### MasterDnsVPN (`masterdnsvpn`)

- **Repo:** https://github.com/masterking32/MasterDnsVPN · MIT · nivel 2 · 55/100
- **Qué es:** MasterDnsVPN, proyecto de investigación en Go para transportar tráfico TCP mediante consultas y respuestas DNS, de @masterking32. Licencia MIT. Tiene ~7.3k estrellas y existe una versión legacy en Python.
- **Cuándo elegirlo:** Casos: Estudiar transporte sobre DNS; Probar conectividad en un laboratorio.
- **Requisitos:** nivel 2: preparación media; Servidor y dominio propios; control DNS; cliente compatible; red de laboratorio; hardware prerequisites; API de IA: no; Servidor y dominio propios; control DNS; cliente compatible; red de laboratorio.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD

  ```bash
  docker run -d --name masterdnsvpn --restart unless-stopped -e DOMAIN=v.example.com -v $(pwd)/data:/data -p 53:53/tcp -p 53:53/udp ghcr.io/masterking32/masterdnsvpn:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Revisa la delegación DNS y prepara una prueba entre equipos propios antes de sustituir una conexión habitual Éxito: Puedes identificar servidor, resolver y túnel y comprobar conectividad básica
- **Combina con:** `freedomain` [22/recursos], `free-for-dev` [22/recursos], `casaos` [22/infraestructura]
- **Riesgos y avisos:** Sin alternativas declaradas. Herramienta de doble uso con implicaciones legales según el país; no se probó. Es un túnel DNS con requisitos de red y no una app de IA; velocidad y resistencia a pérdida dependen de la red y de los resolvers.

### Pangolin Community Edition (`pangolin`)

- **Repo:** https://github.com/fosrl/pangolin · NOASSERTION · nivel 3 · —/100
- **Qué es:** Una plataforma para dar acceso identificado a aplicaciones y servicios propios.
- **Cuándo elegirlo:** Casos: Comprobar el acceso de una cuenta de prueba a una web ficticia.; Comparar qué ven dos cuentas con roles distintos.
- **Requisitos:** nivel 3: preparación pesada; TypeScript, Dockerfile, Makefile, compose.yaml, package.json; hardware prerequisites; API de IA: no; Servidor Linux de prueba, Docker, configuración de DNS y TLS según la guía, y una cuenta inicial de administración..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.pangolin.net/self-host/quick-install
- **Primera prueba propuesta (no ejecutada):** Configura un recurso web de ejemplo con autenticación; prueba una cuenta autorizada y otra sin acceso. Éxito: La cuenta autorizada abre la web de ejemplo y a la otra se le deniega el acceso.
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. GitHub no identifica la licencia (NOASSERTION): confírmala en el archivo LICENSE/COPYING. Los 15 avisos publicados del servidor indican correcciones hasta 1.27.0; el tag 1.27.1 desciende de esa versión.

### Tailcat (`tailcat`)

- **Repo:** https://github.com/tailscale/tailcat · BSD-3-Clause · nivel 2 · —/100
- **Qué es:** Una herramienta experimental de terminal para unir dos extremos bajo control de la misma persona.
- **Cuándo elegirlo:** Casos: Enviar una línea de texto ficticio entre dos equipos propios.; Comprobar si un laboratorio de red local consigue una conexión directa o vía relé.
- **Requisitos:** nivel 2: preparación media; Go, Makefile, go.mod; hardware prerequisites; API de IA: no; Dos equipos propios, una distribución compatible y conectividad entre los extremos o a través del relé..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Elige solo el ejemplo de texto entre terminales; cierra ambas instancias tras recibir la línea. Éxito: La misma línea aparece en la otra terminal sin exponer directorios ni servicios.
- **Riesgos y avisos:** GHSA-w496-344h-g2vv afecta al modo de recepción de 0.4.0 y se corrigió en 0.5.0; 0.7.0 incluye cambios posteriores.

### supabase (`supabase`)

- **Repo:** https://github.com/supabase/supabase · Apache-2.0 · nivel 3 · 76/100 · recomendado en «Backends como servicio auto-hospedados»
- **Qué es:** Supabase, plataforma de desarrollo sobre PostgreSQL que ofrece funciones similares a Firebase con herramientas open source. Licencia Apache-2.0. Es muy madura (~115k estrellas) y tiene servicio alojado y opción de autoalojamiento.
- **Cuándo elegirlo:** Casos: Preparar un backend para una web; Conectar un agente a un esquema de prueba.
- **Requisitos:** nivel 3: preparación pesada; Proyecto de prueba o entorno local; cuenta para Cloud; cliente MCP opcional; hardware prerequisites; API de IA: no; Proyecto de prueba o entorno local; cuenta para Cloud; cliente MCP opcional.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://supabase.com/docs/guides/getting-started
- **Primera prueba propuesta (no ejecutada):** Crea datos ficticios en un proyecto de desarrollo y consulta su estructura con permisos de solo lectura Éxito: Puedes comprobar tablas y acceso sin tocar datos de producción
- **Combina con:** `pgvector` [6/vectores], `activepieces` [1/motores], `coolify`
- **Alternativas:** `appwrite`
- **Riesgos y avisos:** Sin alternativas declaradas. El MCP oficial sirve a clientes compatibles; funciones alojadas, locales y confirmaciones interactivas varían y no deben asumirse idénticas.

### coolify (`coolify`)

- **Repo:** https://github.com/coollabsio/coolify · Apache-2.0 · nivel 2 · 74/100 · recomendado en «Paneles de auto-hospedaje y PaaS propios»
- **Qué es:** Coolify, plataforma autoalojada para desplegar aplicaciones, bases de datos y servicios en tus propios servidores, de coollabsio. Licencia Apache-2.0. Es muy popular (~66k estrellas), activa y financiada por patrocinios.
- **Cuándo elegirlo:** Casos: Alojar una demo web; Administrar despliegues en servidor propio.
- **Requisitos:** nivel 2: instalador de una línea; después hay que configurar dominios y despliegues; Servidor compatible; Docker; dominio opcional; aplicación de prueba; hardware prerequisites; API de IA: no; Servidor compatible; Docker; dominio opcional; aplicación de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash` — fuente: https://github.com/coollabsio/coolify/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega una página estática de prueba y revisa logs antes de añadir bases de datos reales Éxito: Puedes abrir el sitio y reconocer su servicio y registros
- **Combina con:** `supabase`, `activepieces` [1/motores], `windmill` [1/motores], `freedomain` [22/recursos]
- **Alternativas:** `dokploy`, `casaos`
- **Riesgos y avisos:** Alternativa (elige una): casaos. Un patrocinador que menciona Claude Code no acredita una integración del producto con ese agente.

### Appwrite (`appwrite`)

- **Repo:** https://github.com/appwrite/appwrite · BSD-3-Clause · nivel 2 · 73/100 · alternativa en «Backends como servicio auto-hospedados»
- **Qué es:** Plataforma de backend de código abierto (BSD-3-Clause) de Appwrite, que ofrece también una nube gestionada. Muy popular y activa.
- **Cuándo elegirlo:** Casos: dar backend completo a una app web o móvil sin escribir servidor; dejar que un agente de código opere un proyecto de backend vía MCP.
- **Requisitos:** nivel 2: preparación media; TypeScript, Cargo.toml, Dockerfile, composer.json, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/appwrite/appwrite/blob/main/README.md

  ```bash
  docker run -it --rm --publish 127.0.0.1:20080:20080 --volume /var/run/docker.sock:/var/run/docker.sock --volume "$(pwd)"/appwrite:/usr/src/code/appwrite:rw --entrypoint="install" appwrite/appwrite:2.7.2
  ```
- **Primera prueba propuesta (no ejecutada):** Lanza Appwrite con el `docker run` del README, crea un proyecto y un usuario de prueba. Éxito: El panel muestra el proyecto con autenticación y base de datos listas.
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `coolify`
- **Alternativas:** `supabase`
- **Riesgos y avisos:** Alternativas (elige una): supabase.

### Uptime Kuma (`uptime-kuma`)

- **Repo:** https://github.com/louislam/uptime-kuma · MIT · nivel 1 · 72/100
- **Qué es:** Herramienta de monitorización de código abierto (MIT) creada por Louis Lam. Uno de los proyectos autoalojados más populares; activa.
- **Cuándo elegirlo:** Casos: recibir un aviso en Telegram cuando tu web o servidor cae; publicar una página de estado de tus servicios.
- **Requisitos:** nivel 1: preparación sencilla; JavaScript, compose.yaml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2` — fuente: https://github.com/louislam/uptime-kuma/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Uptime Kuma con el `docker run` del README, añade un monitor HTTP para una web propia y configura una notificación. Éxito: El panel muestra el monitor en verde y el historial de tiempos de respuesta.
- **Combina con:** `grafana` [10/bi], `coolify`, `caddy`
- **Riesgos y avisos:** No sustituye a una monitorización completa de métricas y registros.

### Caddy (`caddy`)

- **Repo:** https://github.com/caddyserver/caddy · Apache-2.0 · nivel 2 · 70/100 · recomendado en «Proxies inversos con HTTPS automático»
- **Qué es:** Servidor web de código abierto (Apache-2.0) creado por Matt Holt y patrocinado por empresas. Muy maduro.
- **Cuándo elegirlo:** Casos: publicar tus servicios autoalojados con HTTPS sin gestionar certificados; servir una web estática o hacer de proxy inverso con pocas líneas.
- **Requisitos:** nivel 2: servidor web: hay que escribir un Caddyfile; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone "https://github.com/caddyserver/caddy.git"` — fuente: https://github.com/caddyserver/caddy/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Caddy y ejecuta `caddy reverse-proxy --from localhost:8443 --to localhost:8080` sobre un servicio local. Éxito: Caddy sirve el servicio por HTTPS con un certificado local automático.
- **Combina con:** `coolify`, `uptime-kuma`, `headscale` [22/redes], `frp` [22/redes], `synapse` [17/comunidades], `wg-easy` [22/redes]
- **Alternativas:** `traefik`
- **Riesgos y avisos:** Alternativas (elige una): traefik.

### Traefik Proxy (`traefik`)

- **Repo:** https://github.com/traefik/traefik · MIT · nivel 2 · 70/100 · alternativa en «Proxies inversos con HTTPS automático»
- **Qué es:** Proxy inverso de código abierto (MIT) de Traefik Labs, que vende productos comerciales aparte. Muy maduro.
- **Cuándo elegirlo:** Casos: publicar contenedores Docker con dominios y HTTPS mediante etiquetas; balancear tráfico entre servicios en Kubernetes.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/traefik/traefik` — fuente: https://github.com/traefik/traefik/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Traefik con Docker y el proveedor de Docker activado, y lanza un contenedor whoami con etiquetas de ruta. Éxito: El servicio responde en el dominio configurado sin reiniciar Traefik.
- **Combina con:** `coolify`, `dokploy`, `crowdsec` [16/deteccion], `grafana` [10/bi], `portainer`, `coraza` [16/deteccion]
- **Alternativas:** `caddy`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): caddy.

### Dokploy (`dokploy`)

- **Repo:** https://github.com/Dokploy/dokploy · Apache-2.0 + licencia propietaria (/proprietary) · nivel 2 · 67/100 · alternativa en «Paneles de auto-hospedaje y PaaS propios»
- **Qué es:** PaaS autoalojable de Dokploy Technology, Inc. La licencia es Apache-2.0 salvo el contenido bajo /proprietary (LICENSE_PROPRIETARY). Muy activo; ofrece Dokploy Cloud de pago.
- **Cuándo elegirlo:** Casos: desplegar tus aplicaciones y bases de datos en un VPS propio con interfaz web; levantar con un clic plantillas como Plausible o Cal.com.
- **Requisitos:** nivel 2: preparación media; TypeScript, Dockerfile, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSL https://dokploy.com/install.sh | bash` — fuente: https://github.com/Dokploy/dokploy/blob/canary/README.md
- **Primera prueba propuesta (no ejecutada):** En un VPS de pruebas ejecuta el instalador oficial (`curl -sSL https://dokploy.com/install.sh | bash`) y despliega una aplicación de ejemplo. Éxito: La aplicación queda accesible a través de Traefik desde el panel.
- **Combina con:** `traefik`, `uptime-kuma`, `supabase`
- **Alternativas:** `coolify`, `casaos`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): coolify. Instalar con `curl | bash` ejecuta un script remoto con privilegios: revísalo antes.

### Portainer CE (`portainer`)

- **Repo:** https://github.com/portainer/portainer · Zlib · nivel 1 · 66/100
- **Qué es:** Gestor de contenedores de código abierto (zlib) de Portainer.io. La Community Edition es gratuita y la Business Edition añade funciones de pago sobre la misma base. Muy maduro.
- **Cuándo elegirlo:** Casos: administrar los contenedores de tu homelab desde el navegador; desplegar stacks de Docker Compose con interfaz gráfica.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, go.mod, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/portainer/portainer/blob/release/2.45/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Portainer CE con Docker según su guía, crea el usuario administrador y revisa los contenedores locales. Éxito: El panel lista los contenedores con su estado y registros.
- **Combina con:** `traefik`, `uptime-kuma`, `wg-easy` [22/redes]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Dar a Portainer acceso al socket de Docker equivale a acceso de administrador al host.

### CasaOS (`casaos`)

- **Repo:** https://github.com/IceWhaleTech/CasaOS · Apache-2.0 · nivel 1 · 52/100 · alternativa en «Paneles de auto-hospedaje y PaaS propios»
- **Qué es:** CasaOS, sistema para nube personal sobre Docker, de IceWhaleTech (ZimaSpace). Licencia Apache-2.0. Tiene ~38k estrellas, pero su última release es v0.4.15 (diciembre de 2024), aunque el repo sigue recibiendo cambios.
- **Cuándo elegirlo:** Casos: Organizar servicios domésticos; Explorar un servidor personal.
- **Requisitos:** nivel 1: instalador de una línea con panel web; Servidor Linux compatible; disco y red; respaldo del equipo antes de instalar; hardware prerequisites; API de IA: no; Servidor Linux compatible; disco y red; respaldo del equipo antes de instalar.
- **Instalación (documentada en la fuente; no ejecutada):** `wget -qO- https://get.casaos.io | sudo bash` — fuente: https://github.com/IceWhaleTech/CasaOS/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta compatibilidad y prueba el panel en un equipo de laboratorio antes de instalar apps Éxito: Puedes identificar almacenamiento y una app de prueba
- **Combina con:** `nextcloud-server` [15/archivos], `adguardhome` [15/privacidad], `activepieces` [1/motores], `masterdnsvpn` [22/redes]
- **Alternativas:** `coolify`, `dokploy`
- **Riesgos y avisos:** Alternativa (elige una): coolify. Ritmo de releases lento. La instalación modifica el servidor y debe seguir requisitos del autor; las apps de su catálogo tienen condiciones independientes.

### LibreTranslate (`libretranslate`)

- **Repo:** https://github.com/LibreTranslate/LibreTranslate · AGPL-3.0 · nivel 3 · —/100
- **Qué es:** Un servicio de traducción que ofrece una interfaz web y una API HTTP para aplicaciones.
- **Cuándo elegirlo:** Casos: Traducir un borrador de una ficha entre español e inglés sin enviarla a un proveedor de LLM.; Conectar una aplicación interna a una instancia de traducción administrada por tu equipo.
- **Requisitos:** nivel 3: preparación media, necesita GPU; Python, docker-compose.yml, pyproject.toml; hardware prerequisites; API de IA: no; Entorno Python compatible con la versión elegida o Docker.; Conexión para descargar paquetes y modelos de idiomas; espacio para los idiomas seleccionados..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install libretranslate` — fuente: https://docs.libretranslate.com/guides/installation/
- **Primera prueba propuesta (no ejecutada):** Abre la interfaz de una instancia local, elige inglés a español y escribe «Good morning». Éxito: La interfaz muestra la traducción al español; el navegador sigue conectado a tu propia instancia.
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. En un despliegue de red, configurar autenticación y límites; el endpoint MCP de ejemplo envía texto a la instancia alojada.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-22.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Infraestructura, despliegue y herramientas para agentes», lee `docs/alexandria/categoria-22.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-22.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
