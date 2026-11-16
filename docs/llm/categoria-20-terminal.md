# Alexandría para agentes · Agentes de terminal

Categoría 20 «Programar con agentes de código» › subcategoría `terminal`. 11 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=20&sub=terminal · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `opencode` | Agente de código open source para la terminal, compatible con más de 75… | 1 Básico | 82 | MIT (OSI permisiva) | recomendado |
| `deepseek-harness` | Harness de agentes de DeepSeek en vista previa, con arquitectura de plugins… | 2 Intermedio | 74 | MIT (OSI permisiva) | sin grupo |
| `codex` | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open… | 1 Básico | 71 | Apache-2.0 (OSI permisiva) | alternativa |
| `gemini-cli` | CLI de Google orientado actualmente a Code Assist empresarial; el README remite… | 1 Básico | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `qwen-code` | Agente de código de terminal del equipo Qwen, multiprotocolo (OpenAI… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | alternativa |
| `goose` | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y… | 1 Básico | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `claude-code` | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y… | 1 Básico | 58 | — (propietaria) | alternativa |
| `open-interpreter` | Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con… | 1 Básico | 57 | Apache-2.0 (OSI permisiva) | sin grupo |
| `mimo-code` | Asistente de código de Xiaomi MiMo para la terminal con herramientas de… | 2 Intermedio | 50 | MIT (OSI permisiva) | alternativa |
| `aider` | Programación en pareja con IA en la terminal que edita tu repo y hace commits… | 1 Básico | 49 | Apache-2.0 (OSI permisiva) | alternativa |
| `antigravity-cli` | Agente de programación de Google para la terminal (agy), con subagentes, MCP y… | 1 Básico | 27 | Propietaria (sin licencia en el repositorio) (propietaria) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OpenCode (`opencode`)

- **Repo:** https://github.com/anomalyco/opencode · MIT · nivel 1 · 82/100 · recomendado en «Agentes de programación en terminal»
- **Qué es:** OpenCode, agente de programación open source para la terminal, de Anomaly (organización anomalyco). Licencia MIT. Es uno de los repos más populares del catálogo (~227k estrellas, v1.19.5).
- **Cuándo elegirlo:** Casos: Comprender un repositorio nuevo; Planificar una corrección pequeña.
- **Requisitos:** nivel 1: preparación sencilla; Node para npm; repositorio de prueba; cuenta de proveedor o Ollama; hardware prerequisites; API de IA: opcional; Node para npm; repositorio de prueba; cuenta de proveedor o Ollama.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i -g @opencode/cli@latest      # or bun/pnpm/yarn` — fuente: https://github.com/anomalyco/opencode/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Abre una copia de un proyecto en modo plan y pide que explique su estructura Éxito: Obtienes una explicación contrastable antes de permitir ediciones
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `opencode-manager` [20/sesiones], `t3code` [20/sesiones]
- **Alternativas:** `codex`, `gemini-cli`, `qwen-code`, `goose`, `claude-code`, `mimo-code`, `aider`, `antigravity-cli`
- **Riesgos y avisos:** Alternativas (elige una): claude-code, codex, goose, gemini-cli, aider, mimo-code. El paquete actual es @opencode/cli; no confundir con el antiguo opencode-ai archivado; la integración ChatGPT no convierte el proyecto en un cliente oficial de….

### DeepSeek Harness (DSH) (`deepseek-harness`)

- **Repo:** https://github.com/deepseek-ai/deepseek-harness · MIT · nivel 2 · 74/100
- **Qué es:** Harness de agentes de código abierto de DeepSeek AI (deepseek-ai/deepseek-harness, comando `dsh`), en TypeScript con licencia MIT. Está en «developer preview»: el README avisa de cambios incompatibles y SAFETY.md indica que no ha pasado…
- **Cuándo elegirlo:** Casos: Probar un harness de agentes extensible por plugins; Comparar proveedores de modelos desde una misma Web UI. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: depends.
- **Instalación (documentada en la fuente; no ejecutada):** `npx @deepseek-ai/dsh web` — fuente: https://github.com/deepseek-ai/deepseek-harness/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la Web UI en una VM o contenedor, configura un proveedor y pide un resumen de un archivo ficticio Éxito: El resumen aparece y el registro de la sesión muestra el proveedor elegido
- **Combina con:** `dsh-noema` [6/memoria], `engram` [6/memoria], `agentmemory` [6/memoria], `litellm` [23/serving], `ollama` [8/motores]
- **Riesgos y avisos:** Es distinto de los modelos DeepSeek: el harness no incluye modelo y puede usar otros proveedores. Vista previa sin auditoría: no lo uses como único control de….

### Codex CLI (`codex`)

- **Repo:** https://github.com/openai/codex · Apache-2.0 · nivel 1 · 71/100 · alternativa en «Agentes de programación en terminal»
- **Qué es:** Codex CLI, agente de programación de OpenAI que se ejecuta en local, escrito en Rust. Licencia Apache-2.0. Es muy activo (~135k estrellas, rust-v0.169.0).
- **Cuándo elegirlo:** Casos: Explorar un proyecto; Preparar un cambio y revisar su diff.
- **Requisitos:** nivel 1: preparación sencilla; Node o binario adecuado; terminal; proyecto de prueba; cuenta o backend local; hardware prerequisites; API de IA: opcional; Node o binario adecuado; terminal; proyecto de prueba; cuenta o backend local.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/openai/codex/blob/main/README.md

  ```shell
  # Install using npm
  npm install -g @openai/codex
  ```
- **Primera prueba propuesta (no ejecutada):** Instala el CLI, inicia sesión por la ruta elegida y solicita una explicación sin cambios Éxito: Puedes comprobar los archivos usados y el alcance de la propuesta
- **Combina con:** `agent-skills` [2/metodologia], `spec-kit` [2/metodologia], `context7` [5/servidores], `t3code` [20/sesiones]
- **Alternativas:** `opencode`, `gemini-cli`, `qwen-code`, `goose`, `claude-code`, `mimo-code`, `aider`, `antigravity-cli`
- **Riesgos y avisos:** Alternativas (elige una): claude-code, gemini-cli, opencode, antigravity-cli. El CLI corre en tu equipo pero el modelo puede ser remoto; --oss distingue la inferencia local y los servicios de búsqueda pueden seguir siendo externos.

### Gemini CLI (`gemini-cli`)

- **Repo:** https://github.com/google-gemini/gemini-cli · Apache-2.0 · nivel 1 · 65/100 · alternativa en «Agentes de programación en terminal»
- **Qué es:** Gemini CLI, agente de terminal de Google. Licencia Apache-2.0. Tiene ~109k estrellas (v0.68.0), pero su README indica que desde el 18 de junio de 2026 está orientado solo a licencias Gemini Code Assist Standard/Enterprise y Code Assist for…
- **Cuándo elegirlo:** Casos: Estudiar un agente empresarial de Google; Planificar una migración de CLI.
- **Requisitos:** nivel 1: preparación sencilla; Node; acceso empresarial Code Assist o credenciales admitidas; proyecto de prueba; hardware prerequisites; API de IA: opcional; Node; acceso empresarial Code Assist o credenciales admitidas; proyecto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/google-gemini/gemini-cli/blob/main/README.md

  ```bash
  # Using npx (no installation required)
  npx @google/gemini-cli
  ```
- **Primera prueba propuesta (no ejecutada):** Lee primero el aviso de acceso y comprueba si corresponde este CLI empresarial o Antigravity CLI Éxito: Puedes elegir el producto de Google apropiado antes de instalar
- **Combina con:** `stitch-skills` [27/skills], `context7` [5/servidores], `mcp` [5/directorios]
- **Alternativas:** `opencode`, `codex`, `qwen-code`, `goose`, `claude-code`, `mimo-code`, `aider`, `antigravity-cli`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): claude-code, codex, opencode, antigravity-cli. Para uso individual, Google remite a Antigravity CLI (antigravity-cli). El acceso individual y Google AI Pro o Ultra se remiten a Antigravity CLI, un producto separado; sustituye la descripción antigua de cuota gratuita.

### Qwen Code (`qwen-code`)

- **Repo:** https://github.com/QwenLM/qwen-code · Apache-2.0 · nivel 1 · 64/100 · alternativa en «Agentes de programación en terminal»
- **Qué es:** Agente de código de código abierto (Apache-2.0) del equipo Qwen de Alibaba, derivado de Gemini CLI. Muy activo.
- **Cuándo elegirlo:** Casos: pedir desde la terminal cambios y pruebas en un repositorio; usar un modelo local o de Qwen como agente de código sin depender de un único proveedor. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, Dockerfile, package.json; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g @qwen-code/qwen-code@latest` — fuente: https://github.com/QwenLM/qwen-code/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `npm install -g @qwen-code/qwen-code@latest`, configura un proveedor y pídele que resuma tu repositorio. Éxito: El agente lee el código y devuelve un resumen con los módulos principales.
- **Combina con:** `zed` [20/editor], `ollama` [8/motores], `vllm` [23/serving], `openclaw` [21/asistentes]
- **Alternativas:** `opencode`, `codex`, `gemini-cli`, `goose`, `claude-code`, `mimo-code`, `aider`, `antigravity-cli`
- **Riesgos y avisos:** Alternativas (elige una): gemini-cli, del que deriva.

### goose (`goose`)

- **Repo:** https://github.com/aaif-goose/goose · Apache-2.0 · nivel 1 · 62/100 · alternativa en «Agentes de programación en terminal»
- **Qué es:** goose, agente de IA open source de propósito general (escritorio, CLI y API) escrito en Rust, ahora bajo la organización aaif-goose y con métricas de salud de la Linux Foundation. Licencia Apache-2.0.
- **Cuándo elegirlo:** Casos: Automatizar una tarea de desarrollo; Comparar agentes conectados por ACP.
- **Requisitos:** nivel 1: preparación sencilla; CLI o app; proveedor o agente ACP autenticado; proyecto de prueba; hardware prerequisites; API de IA: opcional; CLI o app; proveedor o agente ACP autenticado; proyecto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash` — fuente: https://github.com/aaif-goose/goose/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un proveedor y solicita resumir una carpeta pequeña antes de añadir extensiones Éxito: Puedes reconocer herramientas y contexto usados en la respuesta
- **Combina con:** `ollama` [8/motores], `playwright-mcp` [5/servidores], `github-mcp-server` [5/servidores]
- **Alternativas:** `opencode`, `codex`, `gemini-cli`, `qwen-code`, `claude-code`, `mimo-code`, `aider`, `antigravity-cli`, `open-interpreter`
- **Riesgos y avisos:** Alternativas (elige una): opencode, claude-code, open-interpreter. Los proveedores y extensiones tienen requisitos diferentes; la integración ACP no incluye créditos ni garantiza todas las funciones de cada agente.

### Claude Code (`claude-code`)

- **Repo:** https://github.com/anthropics/claude-code · — · nivel 1 · 58/100 · alternativa en «Agentes de programación en terminal»
- **Qué es:** Claude Code, agente de programación de Anthropic para la terminal, el IDE y la web. Es software propietario: el repo contiene documentación, plugins y seguimiento de issues, y el uso se rige por los Términos Comerciales de Anthropic…
- **Cuándo elegirlo:** Casos: Entender código sin editar; Preparar una propuesta de corrección.
- **Requisitos:** nivel 1: preparación sencilla; Equipo compatible; terminal; cuenta de Claude o proveedor elegido; carpeta de prueba; hardware prerequisites; API de IA: opcional; Equipo compatible; terminal; cuenta de Claude o proveedor elegido; carpeta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `winget install Anthropic.ClaudeCode` — fuente: https://github.com/anthropics/claude-code/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala el CLI para tu sistema, comprueba la versión y pide explicar un archivo sin modificarlo Éxito: Puedes revisar el archivo citado y la configuración de acceso
- **Combina con:** `superpowers` [2/metodologia], `anthropic-skills` [2/catalogos], `claude-mem` [6/memoria], `context7` [5/servidores]
- **Alternativas:** `opencode`, `codex`, `gemini-cli`, `qwen-code`, `goose`, `mimo-code`, `aider`, `antigravity-cli`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): codex, gemini-cli, opencode, goose, antigravity-cli. No es open source. La ruta local procede de la integración de Ollama y necesita modelos compatibles con herramientas; las funciones y el acceso no son idénticos a Claude alojado.

### Open Interpreter (`open-interpreter`)

- **Repo:** https://github.com/openinterpreter/openinterpreter · Apache-2.0 · nivel 1 · 57/100
- **Qué es:** Open Interpreter, ahora reescrito en Rust a partir de Codex como agente de programación optimizado para modelos de bajo coste. Licencia Apache-2.0.
- **Cuándo elegirlo:** Casos: Probar un agente con distintos harnesses; Reutilizar un cliente del SDK de Codex.
- **Requisitos:** nivel 1: preparación sencilla; Terminal; instalador del sistema; proveedor configurado; carpeta de prueba; hardware prerequisites; API de IA: depends; Terminal; instalador del sistema; proveedor configurado; carpeta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://www.openinterpreter.com/install | sh` — fuente: https://github.com/openinterpreter/openinterpreter/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca interpreter y revisa modelo y harness antes de pedir una explicación de código Éxito: Puedes identificar proveedor y permisos sin ejecutar cambios
- **Combina con:** `ollama` [8/motores], `e2b` [22/infra], `context7` [5/servidores]
- **Alternativas:** `goose`
- **Riesgos y avisos:** Alternativas (elige una): goose. La descripción antigua (intérprete Python local) ya no corresponde a este repo. La versión actual está escrita en Rust y deriva de Codex; su compatibilidad con el SDK mediante override no implica acceso al plan de Codex; la versión Python….

### MiMo-Code (`mimo-code`)

- **Repo:** https://github.com/XiaomiMiMo/MiMo-Code · MIT · nivel 2 · 50/100 · alternativa en «Agentes de programación en terminal»
- **Qué es:** MiMoCode, asistente de programación para terminal de Xiaomi MiMo, construido como fork de OpenCode. Licencia MIT. Tiene ~14k estrellas (v0.1.17).
- **Cuándo elegirlo:** Casos: Probar un asistente de terminal; Estudiar memoria y herramientas del proyecto.
- **Requisitos:** nivel 2: preparación media; Terminal; cuenta o proveedor admitido; carpeta de prueba; hardware prerequisites; API de IA: opcional; Terminal; cuenta o proveedor admitido; carpeta de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el primer inicio y comprueba proveedor y modelo antes de pedir explicar un archivo Éxito: Puedes identificar la ruta de autenticación y revisar la respuesta
- **Combina con:** `headroom` [23/tokens], `rtk` [23/tokens], `context7` [5/servidores]
- **Alternativas:** `opencode`, `codex`, `gemini-cli`, `qwen-code`, `goose`, `claude-code`, `aider`, `antigravity-cli`
- **Riesgos y avisos:** Alternativa (elige una): opencode. Son adaptadores de terceros y la importación de credenciales no demuestra autorización universal del proveedor; no se confirma una ruta local en este README.

### Aider (`aider`)

- **Repo:** https://github.com/Aider-AI/aider · Apache-2.0 · nivel 1 · 49/100 · alternativa en «Agentes de programación en terminal»
- **Qué es:** Aider, programación en pareja con IA en la terminal, de Aider-AI. Licencia Apache-2.0. Es maduro (~50k estrellas, v0.86.0), pero su último cambio es de mayo de 2026.
- **Cuándo elegirlo:** Casos: Corregir una función pequeña; Programar en pareja desde terminal.
- **Requisitos:** nivel 1: preparación sencilla; Python; Git; proveedor o modelo local; repositorio de prueba; hardware prerequisites; API de IA: opcional; Python; Git; proveedor o modelo local; repositorio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Aider-AI/aider/blob/main/README.md

  ```bash
  python -m pip install aider-install
  aider-install
  ```
- **Primera prueba propuesta (no ejecutada):** Abre una copia de un proyecto y pide una explicación antes de aceptar cambios y commits Éxito: Puedes revisar archivos incluidos y cualquier diff propuesto
- **Combina con:** `litellm` [23/serving], `ollama` [8/motores], `tree-sitter` [7/codigo], `ast-grep` [7/calidad], `openidea` [20/editor], `swe-bench` [7/calidad]
- **Alternativas:** `opencode`, `codex`, `gemini-cli`, `qwen-code`, `goose`, `claude-code`, `mimo-code`, `antigravity-cli`, `cline`
- **Riesgos y avisos:** Alternativas (elige una): opencode, cline. Actividad reciente baja. Sus modelos de ejemplo incluyen versiones antiguas; la presencia de Claude en la lista no implica una suscripción Claude Code.

### Antigravity CLI (`antigravity-cli`)

- **Repo:** https://github.com/google-antigravity/antigravity-cli · Propietaria (sin licencia en el repositorio) · nivel 1 · 27/100 · alternativa en «Agentes de programación en terminal»
- **Qué es:** CLI oficial de Google Antigravity (`agy`), producto propietario. El repositorio google-antigravity/antigravity-cli solo contiene README, CHANGELOG, ejemplos y releases con binarios; no publica código fuente ni licencia.
- **Cuándo elegirlo:** Casos: Pedir cambios a un proyecto desde la terminal o por SSH; Delegar tareas paralelas en subagentes.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/google-antigravity/antigravity-cli/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Inicia agy en un proyecto de prueba y pide renombrar una función con su prueba Éxito: El cambio aparece en el diff y pediste permiso antes de ejecutar comandos
- **Combina con:** `google-skills` [2/catalogos], `antigravity-awesome-skills` [2/catalogos], `engram` [6/memoria], `context7` [5/servidores]
- **Alternativas:** `opencode`, `codex`, `gemini-cli`, `qwen-code`, `goose`, `claude-code`, `mimo-code`, `aider`
- **Riesgos y avisos:** Alternativas (elige una): gemini-cli, claude-code, codex. Google remite a Antigravity CLI a las cuentas gratuitas y Google AI Pro/Ultra que antes usaban Gemini….

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-20-terminal.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Agentes de terminal», lee `docs/alexandria/categoria-20-terminal.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-20-terminal.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
