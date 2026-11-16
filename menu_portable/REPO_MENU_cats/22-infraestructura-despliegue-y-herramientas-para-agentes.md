# 22. Infraestructura, despliegue y herramientas para agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agent-desktop`
role=app · exec=local · setup=medium · mcp=True · prov=— · tags=infra,accessibility,accessibility-api,ai-agents,automation,cli,computer-use,computer-use-agent

**Qué es:** CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio.
**Stack:** Node; permisos de accesibilidad del sistema; cliente de agente opcional
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El CLI y MCP no necesitan un LLM propio; el agente que los controle usa su modelo o plan
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Ofrece skills portables y MCP stdio; algunas órdenes de teclas o botones mantenidos se rechazan hasta disponer de daemon de liberación
- Coste: Sin pago a un modelo en la ruta básica. El CLI y MCP no necesitan un LLM propio; el agente que los controle usa su modelo o plan
- Equipo: Preparación según la ruta elegida. Node; permisos de accesibilidad del sistema; cliente de agente opcional
**Repo:** https://github.com/vercel-labs/agent-desktop

**Instalación** [+]:

```
npm install -g agent-desktop
agent-desktop status                # platform, permissions, supported surfaces
agent-desktop permissions --guide   # macOS: walks you through the Accessibility grant
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Inspeccionar una app de escritorio propia; Preparar una prueba de interfaz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta status y permissions --guide y obtén una captura de una ventana de prueba sin pulsar controles
**Qué comprobar:** Puedes comprobar plataforma, permisos y referencias de accesibilidad
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `playwright-mcp`

## `agent-protocol`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=agents,python

**Qué es:** Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado.
**Stack:** Navegador; nociones de HTTP
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer la especificación no consume API de IA; una implementación y su alojamiento tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una especificación de API y no MCP ni un servidor instalable; los bloques Hurl ilustran peticiones y no son comandos de terminal normales
- Coste: Sin pago a un modelo en la ruta básica. Leer la especificación no consume API de IA; una implementación y su alojamiento tienen costes propios
- Equipo: Preparación según la ruta elegida. Navegador; nociones de HTTP
**Repo:** https://github.com/langchain-ai/agent-protocol

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una API de agentes; Comparar protocolos antes de implementar
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee las rutas threads y runs y dibuja cómo una aplicación inicia y consulta una ejecución
**Qué comprobar:** Puedes distinguir estado del hilo y ejecución del agente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `langgraphjs`, `deepagents`

## `casaos`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=infraestructura,server,go

**Qué es:** Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos.
**Stack:** Servidor Linux compatible; disco y red; respaldo del equipo antes de instalar
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API de IA; equipo, discos y energía se pagan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La instalación modifica el servidor y debe seguir requisitos del autor; las apps de su catálogo tienen condiciones independientes
- Coste: Sin pago a un modelo en la ruta básica. No necesita API de IA; equipo, discos y energía se pagan aparte
- Equipo: Preparación según la ruta elegida. Servidor Linux compatible; disco y red; respaldo del equipo antes de instalar
**Repo:** https://github.com/IceWhaleTech/CasaOS

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/IceWhaleTech/CasaOS/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar servicios domésticos; Explorar un servidor personal
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta compatibilidad y prueba el panel en un equipo de laboratorio antes de instalar apps
**Qué comprobar:** Puedes identificar almacenamiento y una app de prueba
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nextcloud-server`, `adguardhome`, `activepieces`
**Alternativas (elige una):** `coolify`

## `claude-task-master`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=infra,agent,javascript

**Qué es:** Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP.
**Stack:** Node; cliente MCP; proveedor o CLI Claude Code/Codex configurado; PRD ficticio
**Acceso y costes:**
- API de IA: API de IA opcional. Admite proveedores API y rutas por CLI Claude Code o Codex con sus cuentas; investigación y fallback pueden usar otros proveedores
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. Ofrece MCP estándar para el cliente y backends específicos para el modelo; un campo OLLAMA_API_KEY no basta para asegurar inferencia local sin comprobar la configuración
- Coste: El coste depende del proveedor o la ruta. Admite proveedores API y rutas por CLI Claude Code o Codex con sus cuentas; investigación y fallback pueden usar otros proveedores
- Equipo: Preparación según la ruta elegida. Node; cliente MCP; proveedor o CLI Claude Code/Codex configurado; PRD ficticio
**Repo:** https://github.com/eyaltoledano/claude-task-master

**Instalación** [+]:

```
claude mcp add taskmaster-ai -- npx -y task-master-ai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Descomponer un proyecto web; Revisar orden y dependencias de tareas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte una especificación corta de prueba en tareas y revisa dependencias antes de ejecutarlas
**Qué comprobar:** Puedes rastrear cada tarea a un requisito
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`
**Alternativas (elige una):** `spec-kit`

## `composio`
role=platform · exec=cloud · setup=easy · mcp=True · prov=openai,anthropic,mcp · tags=agents,mcp,automation,typescript

**Qué es:** Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales.
**Stack:** Cuenta Composio; CLI o SDK; cuenta externa de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La conexión no necesita un LLM propio en su ruta básica; Composio requiere autenticación y su servicio y apps externas tienen condiciones de uso
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El CLI ofrece una superficie local para Claude Code; el SDK de Claude Agent no equivale a incluir créditos o plan de Claude Code
- Coste: Consumo de APIs o servicios. La conexión no necesita un LLM propio en su ruta básica; Composio requiere autenticación y su servicio y apps externas tienen condiciones de uso
- Equipo: Preparación según la ruta elegida. Cuenta Composio; CLI o SDK; cuenta externa de prueba
**Repo:** https://github.com/ComposioHQ/composio

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ComposioHQ/composio/blob/next/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar un agente a un CRM; Explorar herramientas de consulta de un servicio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca una herramienta de consulta y revisa sus permisos antes de enlazar una cuenta
**Qué comprobar:** Puedes identificar acción, aplicación y alcance de autorización
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openai-agents-python`, `langgraph`, `mastra`, `claude-code`

## `computer-use-preview`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=google · tags=browser,agents,python

**Qué es:** Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web.
**Stack:** Python; navegador y dependencias; Gemini Developer API o Vertex AI; entorno de prueba
**Acceso y costes:**
- API de IA: API de IA necesaria. Requiere Gemini API o Vertex con sus credenciales y consumo; no lo cubre por defecto una suscripción de un agente de código
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Es una implementación de referencia y no un servidor genérico que se instala automáticamente en Claude Code, Codex o Antigravity
- Coste: Consumo de APIs o servicios. Requiere Gemini API o Vertex con sus credenciales y consumo; no lo cubre por defecto una suscripción de un agente de código
- Equipo: Preparación según la ruta elegida. Python; navegador y dependencias; Gemini Developer API o Vertex AI; entorno de prueba
**Repo:** https://github.com/google-gemini/computer-use-preview

**Instalación** [+]:

```
git clone https://github.com/google-gemini/computer-use-preview.git
cd computer-use-preview

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar automatización visual de navegador; Evaluar tareas de formularios ficticios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa una página de prueba y solicita localizar un elemento sin cuentas personales ni acciones reales
**Qué comprobar:** Puedes comparar la captura y la acción propuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `playwright`, `sandbox`, `e2b`
**Alternativas (elige una):** `browser-use`, `skyvern`

## `coolify`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=infraestructura,server,php

**Qué es:** Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios.
**Stack:** Servidor compatible; Docker; dominio opcional; aplicación de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Self-host abierto requiere servidores y mantenimiento; Cloud es un servicio de pago separado
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Un patrocinador que menciona Claude Code no acredita una integración del producto con ese agente
- Coste: El coste depende del proveedor o la ruta. Self-host abierto requiere servidores y mantenimiento; Cloud es un servicio de pago separado
- Equipo: Preparación según la ruta elegida. Servidor compatible; Docker; dominio opcional; aplicación de prueba
**Repo:** https://github.com/coollabsio/coolify

**Instalación** [?]:

```
Seguir la instalación original: https://coolify.io/docs/installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Alojar una demo web; Administrar despliegues en servidor propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Despliega una página estática de prueba y revisa logs antes de añadir bases de datos reales
**Qué comprobar:** Puedes abrir el sitio y reconocer su servicio y registros
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `supabase`, `activepieces`, `windmill`, `freedomain`
**Alternativas (elige una):** `casaos`

## `e2b`
role=platform · exec=cloud · setup=easy · mcp=False · prov=— · tags=agents,security,python

**Qué es:** Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas.
**Stack:** Node o Python; cuenta E2B y clave; presupuesto de sandbox
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API de IA para crear el entorno pero sí clave del servicio E2B; cómputo y tiempo del sandbox se facturan según plan
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Instalar el SDK no aloja todo E2B en tu equipo ni incluye un modelo de IA
- Coste: Consumo de APIs o servicios. No necesita API de IA para crear el entorno pero sí clave del servicio E2B; cómputo y tiempo del sandbox se facturan según plan
- Equipo: Preparación según la ruta elegida. Node o Python; cuenta E2B y clave; presupuesto de sandbox
**Repo:** https://github.com/e2b-dev/E2B

**Instalación** [+]:

```
npm i e2b
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Ejecutar código aislado de una app; Preparar un entorno temporal para un agente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un sandbox de prueba, ejecuta una operación de texto inocua y ciérralo
**Qué comprobar:** Puedes revisar resultado y ciclo de vida del sandbox
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `smolagents`, `open-swe`, `computer-use-preview`
**Alternativas (elige una):** `sandbox`

## `free-for-dev`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=recursos,awesome-list,free-for-developers,html

**Qué es:** Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos.
**Stack:** Navegador; necesidad y presupuesto
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La lista no cobra API; los proveedores cambian sus cuotas y pueden pedir tarjeta o cobrar excesos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un directorio de servicios as-a-Service, no software autoalojado ni una garantía permanente de gratuidad
- Coste: Sin pago a un modelo en la ruta básica. La lista no cobra API; los proveedores cambian sus cuotas y pueden pedir tarjeta o cobrar excesos
- Equipo: Preparación según la ruta elegida. Navegador; necesidad y presupuesto
**Repo:** https://github.com/ripienaar/free-for-dev

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar infraestructura para una demo; Comparar niveles gratuitos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige un servicio de alojamiento y comprueba sus límites y condiciones en la web del proveedor antes de crear una cuenta
**Qué comprobar:** Puedes distinguir plan gratuito, cuotas y extras de pago
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `freedomain`, `supabase`, `coolify`

## `freedomain`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=recursos,digitalplat,dns,dns-tutorial,documentation,domain,domain-platform,domain-registration

**Qué es:** Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat.
**Stack:** Navegador; nombre de dominio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El recurso describe opciones gratuitas sujetas a políticas, disponibilidad y elegibilidad; alojamiento no está incluido
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No se instala un dominio con este README ni se promete disponibilidad o renovación perpetua de cualquier nombre
- Coste: Sin pago a un modelo en la ruta básica. El recurso describe opciones gratuitas sujetas a políticas, disponibilidad y elegibilidad; alojamiento no está incluido
- Equipo: Preparación según la ruta elegida. Navegador; nombre de dominio de prueba
**Repo:** https://github.com/DigitalPlatDev/FreeDomain

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender DNS; Evaluar un dominio para un proyecto personal
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee las condiciones de registro y dibuja registros DNS para un sitio ficticio sin cambiar dominios activos
**Qué comprobar:** Puedes distinguir registro, DNS y alojamiento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `coolify`, `free-for-dev`, `masterdnsvpn`

## `masterdnsvpn`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=redes,dns,dns-client,dns-proxy,dns-server,dns-tunnel,dns-tunneling,dnstt

**Qué es:** Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS.
**Stack:** Servidor y dominio propios; control DNS; cliente compatible; red de laboratorio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa IA; servidor, dominio y ancho de banda tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un túnel DNS con requisitos de red y no una app de IA; velocidad y resistencia a pérdida dependen de la red y de los resolvers
- Coste: Sin pago a un modelo en la ruta básica. No usa IA; servidor, dominio y ancho de banda tienen costes propios
- Equipo: Preparación según la ruta elegida. Servidor y dominio propios; control DNS; cliente compatible; red de laboratorio
**Repo:** https://github.com/masterking32/MasterDnsVPN

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar transporte sobre DNS; Probar conectividad en un laboratorio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa la delegación DNS y prepara una prueba entre equipos propios antes de sustituir una conexión habitual
**Qué comprobar:** Puedes identificar servidor, resolver y túnel y comprobar conectividad básica
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `freedomain`, `free-for-dev`, `casaos`

## `nemoclaw`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=agents,security,typescript

**Qué es:** Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes.
**Stack:** Plataforma compatible según prerequisites; OpenShell; agente y proveedor
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Infraestructura e inferencia gestionada tienen requisitos y costes propios; no incluye acceso universal gratuito
- Claude Code: Referencia para la herramienta; no es una integración
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El prompt para que Claude Code o Codex ayude a instalar es una guía de instalación asistida y no una integración runtime de sus planes
- Coste: El coste depende del proveedor o la ruta. Infraestructura e inferencia gestionada tienen requisitos y costes propios; no incluye acceso universal gratuito
- Equipo: Preparación según la ruta elegida. Plataforma compatible según prerequisites; OpenShell; agente y proveedor
**Repo:** https://github.com/NVIDIA/NemoClaw

**Instalación** [?]:

```
Seguir la instalación original: https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/get-started/quickstart
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar aislamiento para OpenClaw; Comparar políticas de ejecución de agentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee los requisitos y prueba la política con una tarea de consulta en un entorno descartable
**Qué comprobar:** Puedes identificar los permisos de archivos, red e inferencia configurados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openclaw`, `hermes-agent`, `deepagents`, `nemotron`
**Alternativas (elige una):** `sandbox`

## `nodeterm`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=infra,adhd,agent-orchestration,ai-agents,canvas,claude-code,codex,coding-agents

**Qué es:** Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto.
**Stack:** macOS o Linux; tmux según ruta; CLI de agente autenticado
**Acceso y costes:**
- API de IA: API de IA opcional. El gestor usa cuentas de los agentes; dictado local Whisper y funciones AI opcionales tienen requisitos separados
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. Documenta Claude Code, Codex y Antigravity; la licencia BUSL-1.1 y sus límites no deben presentarse como MIT sin restricciones; local aquí incluye dictado, no todo agente
- Coste: El coste depende del proveedor o la ruta. El gestor usa cuentas de los agentes; dictado local Whisper y funciones AI opcionales tienen requisitos separados
- Equipo: Preparación según la ruta elegida. macOS o Linux; tmux según ruta; CLI de agente autenticado
**Repo:** https://github.com/eneskirca/nodeterm

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/eneskirca/nodeterm/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar varias sesiones de código; Asociar sesiones con worktrees
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un terminal y un nodo de agente para explicar una carpeta de prueba
**Qué comprobar:** Puedes ver sesión, terminal y contexto de proyecto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`

## `sandbox`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=— · tags=agents,automation,python,docker

**Qué es:** Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado.
**Stack:** Docker; recursos para navegador; clave de acceso propia; cliente MCP opcional
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El contenedor básico no necesita LLM; equipo, hosting y modelos del agente se pagan o configuran aparte
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Expone MCP en /mcp; sin SANDBOX_API_KEY los servicios quedan abiertos y el ejemplo usa seccomp unconfined, por lo que no es una garantía absoluta de aislamiento
- Coste: Sin pago a un modelo en la ruta básica. El contenedor básico no necesita LLM; equipo, hosting y modelos del agente se pagan o configuran aparte
- Equipo: Preparación según la ruta elegida. Docker; recursos para navegador; clave de acceso propia; cliente MCP opcional
**Repo:** https://github.com/agent-infra/sandbox

**Instalación** [+]:

```
# Recommended: Enable API Key authentication (protects all services: API, JupyterLab, VNC)
# - Supports three methods: X-AIO-API-Key header, Authorization: Bearer header, ?api_key= query parameter
# - Without SANDBOX_API_KEY, services remain open (backward compatible)
docker run --security-opt seccomp=unconfined --rm -it \
  -e SANDBOX_API_KEY=your-secret-key \
  -p 127.0.0.1:8080:8080 ghcr.io/agent-infra/sandbox:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar herramientas de un agente en un contenedor; Consultar una interfaz de navegador aislada
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Arranca el contenedor limitado a loopback y consulta el contexto o una captura antes de ejecutar comandos
**Qué comprobar:** Puedes acceder al entorno autenticado y reconocer navegador, terminal y archivos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openhands`, `browser-use`, `deer-flow`
**Alternativas (elige una):** `nemoclaw`, `e2b`

## `shepherd`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=infra,framework,python

**Qué es:** Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos.
**Stack:** Python 3.11+; entorno compatible; Claude CLI solo para ejemplo con modelo
**Acceso y costes:**
- API de IA: API de IA opcional. El ejemplo offline no necesita API; el ejemplo Claude usa suscripción o clave API y el entorno consume recursos
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La reversibilidad afecta al estado capturado por el runtime y no promete deshacer cualquier efecto externo; la demo offline no es un LLM local
- Coste: El coste depende del proveedor o la ruta. El ejemplo offline no necesita API; el ejemplo Claude usa suscripción o clave API y el entorno consume recursos
- Equipo: Preparación según la ruta elegida. Python 3.11+; entorno compatible; Claude CLI solo para ejemplo con modelo
**Repo:** https://github.com/shepherd-agents/shepherd

**Instalación** [+]:

```
pip install shepherd-ai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar reproducción de ejecuciones; Comparar una traza con un resultado final
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Empieza por Offline Quickstart para observar una traza reversible sin llamar un modelo
**Qué comprobar:** Puedes inspeccionar estados y bifurcaciones de la demostración
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`

## `supabase`
role=platform · exec=local · setup=heavy · mcp=True · prov=— · tags=infraestructura,server,typescript

**Qué es:** Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones.
**Stack:** Proyecto de prueba o entorno local; cuenta para Cloud; cliente MCP opcional
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La base no exige LLM; Cloud, almacenamiento, cómputo y extras tienen planes y cuotas; self-host requiere infraestructura
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El MCP oficial sirve a clientes compatibles; funciones alojadas, locales y confirmaciones interactivas varían y no deben asumirse idénticas
- Coste: El coste depende del proveedor o la ruta. La base no exige LLM; Cloud, almacenamiento, cómputo y extras tienen planes y cuotas; self-host requiere infraestructura
- Equipo: Preparación según la ruta elegida. Proyecto de prueba o entorno local; cuenta para Cloud; cliente MCP opcional
**Repo:** https://github.com/supabase/supabase

**Instalación** [?]:

```
Seguir la instalación original: https://supabase.com/docs/guides/getting-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un backend para una web; Conectar un agente a un esquema de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea datos ficticios en un proyecto de desarrollo y consulta su estructura con permisos de solo lectura
**Qué comprobar:** Puedes comprobar tablas y acceso sin tocar datos de producción
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pgvector`, `activepieces`, `coolify`
