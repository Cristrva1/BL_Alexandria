# 20. Programar con agentes de código — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `aider`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,local · tags=coding-agent,python

**Qué es:** Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos.
**Stack:** Python; Git; proveedor o modelo local; repositorio de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. APIs remotas por consumo o modelos locales según configuración; no aporta créditos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Sus modelos de ejemplo incluyen versiones antiguas; la presencia de Claude en la lista no implica una suscripción Claude Code
- Coste: El coste depende del proveedor o la ruta. APIs remotas por consumo o modelos locales según configuración; no aporta créditos
- Equipo: Preparación según la ruta elegida. Python; Git; proveedor o modelo local; repositorio de prueba
**Repo:** https://github.com/Aider-AI/aider

**Instalación** [+]:

```
python -m pip install aider-install
aider-install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Corregir una función pequeña; Programar en pareja desde terminal
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una copia de un proyecto y pide una explicación antes de aceptar cambios y commits
**Qué comprobar:** Puedes revisar archivos incluidos y cualquier diff propuesto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `ollama`, `tree-sitter`
**Alternativas (elige una):** `opencode`, `cline`

## `antigravity-cli`
role=app · exec=hybrid · setup=easy · mcp=True · prov=google · tags=coding,agents,cli,google

**Qué es:** Agente de programación de Google para la terminal (agy), con subagentes, MCP y skills; se distribuye en binarios, sin código fuente.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Inicia sesión con una cuenta de Google (o un proyecto de GCP para empresa); no pide una clave de API propia en la ruta básica.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Acceso oficial con sesión del plan
- Modelos locales: Modelo local no documentado. No documenta modelos locales.
- Coste: El coste depende del proveedor o la ruta. Los límites dependen de la cuenta y el plan de Google. Google recoge datos de interacción por defecto (desactivable en ajustes).
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/google-antigravity/antigravity-cli

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/google-antigravity/antigravity-cli/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Pedir cambios a un proyecto desde la terminal o por SSH; Delegar tareas paralelas en subagentes
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Inicia agy en un proyecto de prueba y pide renombrar una función con su prueba
**Qué comprobar:** El cambio aparece en el diff y pediste permiso antes de ejecutar comandos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `google-skills`, `antigravity-awesome-skills`, `engram`, `context7`
**Alternativas (elige una):** `gemini-cli`, `claude-code`, `codex`

## `claude-code`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=anthropic,mcp · tags=coding-agent,agents,mcp,typescript

**Qué es:** Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio.
**Stack:** Equipo compatible; terminal; cuenta de Claude o proveedor elegido; carpeta de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. El cliente oficial admite suscripción o cuenta Console según ruta; Ollama documenta modelos locales y nube separada
- Claude Code: Acceso oficial con sesión del plan
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local procede de la integración de Ollama y necesita modelos compatibles con herramientas; las funciones y el acceso no son idénticos a Claude alojado
- Coste: El coste depende del proveedor o la ruta. El cliente oficial admite suscripción o cuenta Console según ruta; Ollama documenta modelos locales y nube separada
- Equipo: Preparación según la ruta elegida. Equipo compatible; terminal; cuenta de Claude o proveedor elegido; carpeta de prueba
**Repo:** https://github.com/anthropics/claude-code

**Instalación** [+]:

```
winget install Anthropic.ClaudeCode
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Entender código sin editar; Preparar una propuesta de corrección
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala el CLI para tu sistema, comprueba la versión y pide explicar un archivo sin modificarlo
**Qué comprobar:** Puedes revisar el archivo citado y la configuración de acceso
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `superpowers`, `anthropic-skills`, `claude-mem`, `context7`
**Alternativas (elige una):** `codex`, `gemini-cli`, `opencode`, `goose`, `antigravity-cli`

## `cline`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=coding-agent,agents,typescript

**Qué es:** Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo.
**Stack:** Node para CLI o editor compatible; proveedor o Ollama; proyecto de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. API o servicios del proveedor según elección; Ollama y LM Studio permiten inferencia local
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Cline es su propio agente; soportar modelos Claude u OpenAI no equivale a usar una suscripción de Claude Code o Codex
- Coste: El coste depende del proveedor o la ruta. API o servicios del proveedor según elección; Ollama y LM Studio permiten inferencia local
- Equipo: Preparación según la ruta elegida. Node para CLI o editor compatible; proveedor o Ollama; proyecto de prueba
**Repo:** https://github.com/cline/cline

**Instalación** [+]:

```
npm i -g cline
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar un error de código; Comparar una propuesta antes de editar
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa Plan mode para pedir un diagnóstico de un archivo antes de pasar a Act
**Qué comprobar:** Puedes revisar el plan y los permisos solicitados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `context7`, `playwright-mcp`
**Alternativas (elige una):** `aider`

## `codex`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=openai,mcp · tags=coding-agent,agents,rust

**Qué es:** Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source.
**Stack:** Node o binario adecuado; terminal; proyecto de prueba; cuenta o backend local
**Acceso y costes:**
- API de IA: API de IA opcional. Acceso oficial con plan de ChatGPT elegible o API con facturación separada; Ollama documenta la ruta --oss local
- Claude Code: Integración no documentada
- Codex: Acceso oficial con sesión del plan
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El CLI corre en tu equipo pero el modelo puede ser remoto; --oss distingue la inferencia local y los servicios de búsqueda pueden seguir siendo externos
- Coste: El coste depende del proveedor o la ruta. Acceso oficial con plan de ChatGPT elegible o API con facturación separada; Ollama documenta la ruta --oss local
- Equipo: Preparación según la ruta elegida. Node o binario adecuado; terminal; proyecto de prueba; cuenta o backend local
**Repo:** https://github.com/openai/codex

**Instalación** [+]:

```
# Install using npm
npm install -g @openai/codex
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un proyecto; Preparar un cambio y revisar su diff
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala el CLI, inicia sesión por la ruta elegida y solicita una explicación sin cambios
**Qué comprobar:** Puedes comprobar los archivos usados y el alcance de la propuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `agent-skills`, `spec-kit`, `context7`, `t3code`
**Alternativas (elige una):** `claude-code`, `gemini-cli`, `opencode`, `antigravity-cli`

## `deepseek-harness`
role=app · exec=hybrid · setup=medium · mcp=True · prov=deepseek,anthropic,openai,local · tags=agents,coding,plugins,typescript

**Qué es:** Harness de agentes de DeepSeek en vista previa, con arquitectura de plugins, Web UI local y proveedores de modelos configurables.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Necesita un proveedor: clave de DeepSeek, un proveedor de terceros incluido (Anthropic, OpenAI, Kimi, GLM) o una API propia compatible.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La guía de proveedores admite una API personalizada para un servidor autoalojado; el harness no incluye modelos.
- Coste: El coste depende del proveedor o la ruta. El consumo se paga al proveedor elegido. Un servidor local consume tu hardware.
- Equipo: Equipo normal; revisar dependencias. Node.js para `npx`; pnpm para ejecutar desde el código. Preferible una VM o contenedor desechable según su aviso de seguridad.
**Repo:** https://github.com/deepseek-ai/deepseek-harness

**Instalación** [+]:

```
npx @deepseek-ai/dsh web
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un harness de agentes extensible por plugins; Comparar proveedores de modelos desde una misma Web UI
**Evita si:** necesitas una herramienta estable y auditada para datos sensibles
**Primera prueba propuesta:** Abre la Web UI en una VM o contenedor, configura un proveedor y pide un resumen de un archivo ficticio
**Qué comprobar:** El resumen aparece y el registro de la sesión muestra el proveedor elegido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `dsh-noema`, `engram`, `agentmemory`, `litellm`, `ollama`

## `gemini-cli`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=google,mcp · tags=coding-agent,agents,typescript

**Qué es:** Agente de terminal de Google. Su aviso actual diferencia el acceso empresarial de Gemini Code Assist, Antigravity CLI para usuarios individuales y Gemini API CLI para llamadas sin estado. Revisa esa distinción antes de instalar o asumir una cuota gratuita.
**Stack:** Node; acceso empresarial Code Assist o credenciales admitidas; proyecto de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. El README actual lo destina a Code Assist Standard o Enterprise y rutas API o Vertex heredadas; no promete cuota individual gratuita
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Referencia para la herramienta; no es una integración
- Modelos locales: Modelo local no documentado. El acceso individual y Google AI Pro o Ultra se remiten a Antigravity CLI, un producto separado; sustituye la descripción antigua de cuota gratuita
- Coste: El coste depende del proveedor o la ruta. El README actual lo destina a Code Assist Standard o Enterprise y rutas API o Vertex heredadas; no promete cuota individual gratuita
- Equipo: Preparación según la ruta elegida. Node; acceso empresarial Code Assist o credenciales admitidas; proyecto de prueba
**Repo:** https://github.com/google-gemini/gemini-cli

**Instalación** [+]:

```
# Using npx (no installation required)
npx @google/gemini-cli
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un agente empresarial de Google; Planificar una migración de CLI
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee primero el aviso de acceso y comprueba si corresponde este CLI empresarial o Antigravity CLI
**Qué comprobar:** Puedes elegir el producto de Google apropiado antes de instalar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `stitch-skills`, `context7`, `mcp`
**Alternativas (elige una):** `claude-code`, `codex`, `opencode`, `antigravity-cli`

## `goose`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=coding-agent,agents,mcp,rust

**Qué es:** Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM.
**Stack:** CLI o app; proveedor o agente ACP autenticado; proyecto de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Documenta API, modelos locales Ollama y agentes ACP con cuentas Claude, ChatGPT o Gemini; aplican límites del servicio elegido
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los proveedores y extensiones tienen requisitos diferentes; la integración ACP no incluye créditos ni garantiza todas las funciones de cada agente
- Coste: El coste depende del proveedor o la ruta. Documenta API, modelos locales Ollama y agentes ACP con cuentas Claude, ChatGPT o Gemini; aplican límites del servicio elegido
- Equipo: Preparación según la ruta elegida. CLI o app; proveedor o agente ACP autenticado; proyecto de prueba
**Repo:** https://github.com/aaif-goose/goose

**Instalación** [?]:

```
Seguir la instalación original: https://goose-docs.ai/docs/getting-started/installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar una tarea de desarrollo; Comparar agentes conectados por ACP
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un proveedor y solicita resumir una carpeta pequeña antes de añadir extensiones
**Qué comprobar:** Puedes reconocer herramientas y contexto usados en la respuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `playwright-mcp`, `github-mcp-server`
**Alternativas (elige una):** `opencode`, `claude-code`, `open-interpreter`

## `mimo-code`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=coding,ai,ai-agents,cli,mimo,mimo-code,typescript

**Qué es:** Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente.
**Stack:** Terminal; cuenta o proveedor admitido; carpeta de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Documenta MiMo OAuth, Codex Plus o Pro e importación de autenticación Claude Code además de API; los términos y límites dependen de cada servicio
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Son adaptadores de terceros y la importación de credenciales no demuestra autorización universal del proveedor; no se confirma una ruta local en este README
- Coste: El coste depende del proveedor o la ruta. Documenta MiMo OAuth, Codex Plus o Pro e importación de autenticación Claude Code además de API; los términos y límites dependen de cada servicio
- Equipo: Preparación según la ruta elegida. Terminal; cuenta o proveedor admitido; carpeta de prueba
**Repo:** https://github.com/XiaomiMiMo/MiMo-Code

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente de terminal; Estudiar memoria y herramientas del proyecto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el primer inicio y comprueba proveedor y modelo antes de pedir explicar un archivo
**Qué comprobar:** Puedes identificar la ruta de autenticación y revisar la respuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `headroom`, `rtk`, `context7`
**Alternativas (elige una):** `opencode`

## `open-interpreter`
role=runtime · exec=local · setup=easy · mcp=False · prov=openai,local · tags=coding-agent,local,rust

**Qué es:** Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos.
**Stack:** Terminal; instalador del sistema; proveedor configurado; carpeta de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor elegido define autenticación y coste; llamar abierto a un modelo no acredita que la inferencia se haga localmente
- Claude Code: Referencia para la herramienta; no es una integración
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La versión actual está escrita en Rust y deriva de Codex; su compatibilidad con el SDK mediante override no implica acceso al plan de Codex; la versión Python tiene otra continuación
- Coste: El coste depende del proveedor o la ruta. El proveedor elegido define autenticación y coste; llamar abierto a un modelo no acredita que la inferencia se haga localmente
- Equipo: Preparación según la ruta elegida. Terminal; instalador del sistema; proveedor configurado; carpeta de prueba
**Repo:** https://github.com/openinterpreter/openinterpreter

**Instalación** [?]:

```
Seguir la instalación original: https://www.openinterpreter.com/docs/terminal/install
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un agente con distintos harnesses; Reutilizar un cliente del SDK de Codex
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Arranca interpreter y revisa modelo y harness antes de pedir una explicación de código
**Qué comprobar:** Puedes identificar proveedor y permisos sin ejecutar cambios
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `e2b`, `context7`
**Alternativas (elige una):** `goose`

## `open-swe`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=anthropic,openai · tags=coding-agent,agents,python

**Qué es:** Robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisables.
**Stack:** Managed Deep Agents para despliegue actual; repositorio y permisos de prueba; servicios integrados
**Acceso y costes:**
- API de IA: API de IA necesaria. El despliegue tal como está requiere Managed Deep Agents y servicios asociados; adaptar a otro runtime requiere trabajo adicional
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El proyecto se presenta actualmente como Robin construido sobre Deep Agents; MIT cubre su código y no concede acceso a todos los servicios
- Coste: Consumo de APIs o servicios. El despliegue tal como está requiere Managed Deep Agents y servicios asociados; adaptar a otro runtime requiere trabajo adicional
- Equipo: Preparación según la ruta elegida. Managed Deep Agents para despliegue actual; repositorio y permisos de prueba; servicios integrados
**Repo:** https://github.com/langchain-ai/open-swe

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/langchain-ai/open-swe/blob/main/docs/INSTALLATION.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una fábrica interna de cambios; Estudiar un agente asíncrono con revisión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee el flujo de issue a PR y prueba un issue ficticio sin habilitar entregas automáticas
**Qué comprobar:** Puedes inspeccionar planificación, sandbox y validación por separado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `deepagents`, `langgraph`, `e2b`
**Alternativas (elige una):** `openhands`

## `opencode`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=coding-agent,agents,typescript

**Qué es:** Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales.
**Stack:** Node para npm; repositorio de prueba; cuenta de proveedor o Ollama
**Acceso y costes:**
- API de IA: API de IA opcional. Admite proveedores por API, ChatGPT Plus o Pro mediante su adaptador y modelos locales con Ollama, LM Studio o vLLM
- Claude Code: Integración no documentada
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El paquete actual es @opencode/cli; no confundir con el antiguo opencode-ai archivado; la integración ChatGPT no convierte el proyecto en un cliente oficial de Codex
- Coste: El coste depende del proveedor o la ruta. Admite proveedores por API, ChatGPT Plus o Pro mediante su adaptador y modelos locales con Ollama, LM Studio o vLLM
- Equipo: Preparación según la ruta elegida. Node para npm; repositorio de prueba; cuenta de proveedor o Ollama
**Repo:** https://github.com/anomalyco/opencode

**Instalación** [+]:

```
npm i -g @opencode/cli@latest      # or bun/pnpm/yarn
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comprender un repositorio nuevo; Planificar una corrección pequeña
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una copia de un proyecto en modo plan y pide que explique su estructura
**Qué comprobar:** Obtienes una explicación contrastable antes de permitir ediciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `opencode-manager`, `t3code`
**Alternativas (elige una):** `claude-code`, `codex`, `goose`, `gemini-cli`, `aider`, `mimo-code`

## `opencode-manager`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=coding,agent,typescript

**Qué es:** Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil.
**Stack:** Docker Compose v2 o entorno de desarrollo; OpenCode; proveedor configurado
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Alojamiento y modelo de OpenCode se pagan o ejecutan según configuración; el panel no incorpora créditos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Este panel es para OpenCode; no se deduce compatibilidad directa con Claude Code o Codex por usar tecnologías similares
- Coste: El coste depende del proveedor o la ruta. Alojamiento y modelo de OpenCode se pagan o ejecutan según configuración; el panel no incorpora créditos
- Equipo: Preparación según la ruta elegida. Docker Compose v2 o entorno de desarrollo; OpenCode; proveedor configurado
**Repo:** https://github.com/chriswritescode-dev/opencode-manager

**Instalación** [?]:

```
Seguir la instalación original: https://opencodemanager.app/docs/getting-started/installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Gestionar sesiones desde el navegador; Consultar un proyecto desde el móvil
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una sesión en un repositorio de ejemplo y revisa cambios sin programar tareas todavía
**Qué comprobar:** Puedes reconocer la sesión, terminal y estado Git
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `opencode`, `ollama`, `coolify`
**Alternativas (elige una):** `t3code`

## `opencursor`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=coding,agent,ai,code,coder,cursor,extension,ide

**Qué es:** Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos.
**Stack:** VS Code; extensión o VSIX; cuenta, API u Ollama/llama.cpp; proyecto de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Admite cuentas de Claude Code, Codex y Antigravity por flujos del proyecto, API y modelos locales; costes y cuotas son externos
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. Es una extensión independiente; las rutas de cuenta no la convierten en producto oficial de esos proveedores y los servicios de embeddings pueden ser distintos del modelo
- Coste: El coste depende del proveedor o la ruta. Admite cuentas de Claude Code, Codex y Antigravity por flujos del proyecto, API y modelos locales; costes y cuotas son externos
- Equipo: Preparación según la ruta elegida. VS Code; extensión o VSIX; cuenta, API u Ollama/llama.cpp; proyecto de prueba
**Repo:** https://github.com/PawanOsman/OpenCursor

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/PawanOsman/OpenCursor/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Trabajar con un agente dentro de VS Code; Comparar inferencia local con cuenta remota
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala la extensión y usa un modelo local o cuenta para explicar un archivo antes de permitir comandos
**Qué comprobar:** Puedes revisar contexto enviado, modelo y diff propuesto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `llama-cpp`, `context7`

## `openhands`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,automation,typescript,docker

**Qué es:** Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP.
**Stack:** Node 24 o posterior; uv; repositorio de prueba; agente autenticado; Docker según backend
**Acceso y costes:**
- API de IA: API de IA opcional. Canvas usa el proveedor o plan del agente y la infraestructura elegida; ejecutar localmente la interfaz no elimina la facturación del modelo
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El README actual presenta Agent Canvas con OpenHands, Claude Code, Codex y agentes ACP; la receta de Docker limita el puerto al equipo local
- Coste: El coste depende del proveedor o la ruta. Canvas usa el proveedor o plan del agente y la infraestructura elegida; ejecutar localmente la interfaz no elimina la facturación del modelo
- Equipo: Preparación según la ruta elegida. Node 24 o posterior; uv; repositorio de prueba; agente autenticado; Docker según backend
**Repo:** https://github.com/OpenHands/OpenHands

**Instalación** [+]:

```
npm install -g @openhands/agent-canvas
agent-canvas
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Centralizar sesiones de agentes; Preparar una automatización de ingeniería
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Arranca Agent Canvas y crea una sesión que solo examine un proyecto de ejemplo
**Qué comprobar:** Puedes reconocer agente, backend y permisos de la sesión
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `sandbox`, `ecc`
**Alternativas (elige una):** `open-swe`

## `openidea`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=coding,app,typescript

**Qué es:** Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes.
**Stack:** Instalador para tu sistema; proyecto pequeño
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El editor básico no necesita API de IA; servicios o plugins externos pueden tener condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un IDE independiente en Rust y la API de plugins está en preview; los benchmarks del autor no son una garantía de igual rendimiento en tu equipo
- Coste: Sin pago a un modelo en la ruta básica. El editor básico no necesita API de IA; servicios o plugins externos pueden tener condiciones propias
- Equipo: Preparación según la ruta elegida. Instalador para tu sistema; proyecto pequeño
**Repo:** https://github.com/l0ng-ai/openidea

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/l0ng-ai/openidea/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar código con atajos tipo IntelliJ; Probar un editor nativo con plugins
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un proyecto de ejemplo y usa buscar en todo para localizar una función
**Qué comprobar:** Puedes navegar al archivo y reconocer sus referencias
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `opencode`, `claude-code`, `aider`

## `t3code`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,ui,typescript

**Qué es:** Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina.
**Stack:** Un agente instalado y autenticado; equipo que permanezca disponible; proyecto de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto dice no revender tokens; usa las cuentas y cuotas de los agentes ya configurados
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. Documenta Claude Code, Codex y Antigravity entre sus proveedores; acceso remoto requiere configuración propia y no ejecuta los agentes en el teléfono
- Coste: El coste depende del proveedor o la ruta. El proyecto dice no revender tokens; usa las cuentas y cuotas de los agentes ya configurados
- Equipo: Preparación según la ruta elegida. Un agente instalado y autenticado; equipo que permanezca disponible; proyecto de prueba
**Repo:** https://github.com/pingdotgg/t3code

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Controlar una sesión desde otro dispositivo; Comparar trabajo de Claude Code y Codex
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un agente local y pide explicar un archivo; revisa sus permisos desde la interfaz
**Qué comprobar:** La sesión refleja el agente y puedes comprobar el archivo consultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`
**Alternativas (elige una):** `opencode-manager`
