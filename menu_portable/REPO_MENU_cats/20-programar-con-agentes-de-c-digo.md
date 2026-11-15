# 20. Programar con agentes de código — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `aider`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,local · tags=coding-agent,python

**Qué es:** Le pides cambios en lenguaje natural y Aider edita los archivos y confirma cada cambio en Git. Funciona con casi cualquier modelo.
**Stack:** Python, tree-sitter, Git
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/Aider-AI/aider

**Instalación** [?]: `Seguir la instalación original: https://github.com/Aider-AI/aider/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un agente sencillo que trabaje con Git paso a paso
**Evita si:** necesitas autonomía en tareas largas; mira `claude-code`
**Combina con:** `ollama`, `litellm`
**Alternativas (elige una):** `opencode`, `cline`, `continue`

## `claude-code`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=anthropic,mcp · tags=coding-agent,agents,mcp,typescript

**Qué es:** Lee y edita archivos, ejecuta comandos, hace commits y abre PRs a partir de instrucciones en lenguaje natural. Se extiende con skills, plugins, subagentes, hooks y servidores MCP.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: API de IA opcional. Puede utilizarse con sesión del plan compatible o con API key; no son la misma facturación.
- Claude Code: Acceso oficial con sesión del plan
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/claude-code

**Instalación** [+]: `winget install Anthropic.ClaudeCode`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres el agente de código más capaz para tareas largas en tu repo
**Evita si:** necesitas un agente totalmente abierto y multi-modelo; mira `opencode`
**Combina con:** `superpowers`, `anthropic-skills`, `claude-mem`, `context7`
**Alternativas (elige una):** `codex`, `gemini-cli`, `opencode`, `goose`

## `cline`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=coding-agent,agents,typescript

**Qué es:** Planifica, edita archivos, ejecuta comandos y usa el navegador pidiendo aprobación en cada paso. Admite MCP y casi cualquier proveedor.
**Stack:** TypeScript, VS Code API
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/cline/cline

**Instalación** [+]: `npm i -g cline`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres un agente dentro de VS Code con control de cada paso
**Evita si:** trabajas solo en terminal; mira `opencode`
**Combina con:** `context7`, `playwright-mcp`
**Alternativas (elige una):** `continue`, `aider`

## `codex`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=openai,mcp · tags=coding-agent,agents,rust

**Qué es:** Lee tu repositorio, propone y aplica cambios y ejecuta comandos dentro de un sandbox. Usa AGENTS.md para el contexto del proyecto y admite MCP.
**Stack:** Rust, TypeScript
**Acceso y costes:**
- API de IA: API de IA opcional. Puede utilizarse con sesión del plan compatible o con API key; no son la misma facturación.
- Claude Code: Integración no documentada
- Codex: Acceso oficial con sesión del plan
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/openai/codex

**Instalación** [+]: `npm install -g @openai/codex`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** usas ChatGPT u OpenAI y quieres un agente abierto en terminal
**Evita si:** trabajas con Claude como modelo principal; mira `claude-code`
**Combina con:** `agent-skills`, `spec-kit`, `context7`
**Alternativas (elige una):** `claude-code`, `gemini-cli`, `opencode`

## `continue`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,local · tags=coding-agent,typescript

**Qué es:** Integra chat, edición y autocompletado en el IDE con cualquier modelo, y permite ejecutar comprobaciones de IA en los PRs.
**Stack:** TypeScript, Kotlin
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/continuedev/continue

**Instalación** [?]: `Seguir la instalación original: https://github.com/continuedev/continue/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres autocompletado y chat en el IDE con modelos a elección
**Evita si:** buscas un agente autónomo para tareas largas; mira `cline`
**Combina con:** `ollama`
**Alternativas (elige una):** `cline`, `aider`

## `dsh-android`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=coding,plugin,typescript

**Qué es:** Plugin de DeepSeek Harness para operar un emulador o dispositivo Android y revisar aplicaciones desde el agente.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
- Otras rutas: Plugin para DeepSeek Harness (DSH). La cuenta, API o modelo se configura en ese anfitrión; no se declara instalación nativa en Claude Code o Codex.
**Repo:** https://github.com/ZSeven-W/dsh-android

**Instalación** [?]: `Seguir la instalación original: https://github.com/ZSeven-W/dsh-android/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plugin de DeepSeek Harness para operar un emulador o dispositivo Android y revisar aplicaciones desde el agente.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `dsh-game-studio`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=coding,plugin,typescript

**Qué es:** Plugin de DeepSeek Harness para preparar y probar juegos pequeños con una interfaz de trabajo dentro del agente.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
- Otras rutas: Plugin para DeepSeek Harness (DSH). La cuenta, API o modelo se configura en ese anfitrión; no se declara instalación nativa en Claude Code o Codex.
**Repo:** https://github.com/ZSeven-W/dsh-game-studio

**Instalación** [?]: `Seguir la instalación original: https://github.com/ZSeven-W/dsh-game-studio/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plugin de DeepSeek Harness para preparar y probar juegos pequeños con una interfaz de trabajo dentro del agente.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `dsh-ios`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=coding,plugin,typescript

**Qué es:** Plugin de DeepSeek Harness para desarrollar y operar aplicaciones en simuladores iOS o dispositivos compatibles.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
- Otras rutas: Plugin para DeepSeek Harness (DSH). La cuenta, API o modelo se configura en ese anfitrión; no se declara instalación nativa en Claude Code o Codex.
**Repo:** https://github.com/ZSeven-W/dsh-ios

**Instalación** [?]: `Seguir la instalación original: https://github.com/ZSeven-W/dsh-ios/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plugin de DeepSeek Harness para desarrollar y operar aplicaciones en simuladores iOS o dispositivos compatibles.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `gemini-cli`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=google,mcp · tags=coding-agent,agents,typescript

**Qué es:** Programa, investiga y automatiza tareas desde la terminal con contexto de millones de tokens y búsqueda de Google integrada. Admite MCP y extensiones.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
- Otras rutas: El README documenta acceso con una cuenta de Google mediante OAuth y rutas con API key. Consultar las cuotas del método elegido.
**Repo:** https://github.com/google-gemini/gemini-cli

**Instalación** [+]: `npx @google/gemini-cli`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres un agente de terminal potente con cuota gratuita
**Evita si:** buscas el agente con mejor desempeño en tareas largas; mira `claude-code`
**Combina con:** `stitch-skills`, `context7`
**Alternativas (elige una):** `claude-code`, `codex`, `opencode`

## `goose`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=coding-agent,agents,mcp,rust

**Qué es:** Funciona como app de escritorio o CLI y va más allá del código: automatiza tareas de desarrollo y de sistema con extensiones MCP. Nacido en Block.
**Stack:** Rust, TypeScript, Electron
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
- Otras rutas: El README también documenta proveedores ACP para utilizar acceso de Gemini, además de APIs y modelos locales.
**Repo:** https://github.com/aaif-goose/goose

**Instalación** [?]: `Seguir la instalación original: https://github.com/aaif-goose/goose/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un agente abierto con app de escritorio y MCP
**Evita si:** solo programas en terminal y quieres el más usado; mira `opencode`
**Combina con:** `playwright-mcp`, `github-mcp-server`
**Alternativas (elige una):** `opencode`, `claude-code`, `open-interpreter`

## `mimo-code`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=coding,ai,ai-agents,cli,mimo,mimo-code,typescript

**Qué es:** Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente. Mantiene el contexto del proyecto y usa herramientas para ejecutar tareas de desarrollo desde una conversación.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
- Otras rutas: El README documenta acceso al proveedor Xiaomi MiMo con OAuth o configuración del proveedor. No equivale a usar un plan de Claude o Codex.
**Repo:** https://github.com/XiaomiMiMo/MiMo-Code

**Instalación** [?]: `Seguir la instalación original: https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres evaluar el agente de código del ecosistema Xiaomi MiMo
**Evita si:** un flujo determinista resuelve el problema sin un agente

## `open-interpreter`
role=runtime · exec=local · setup=easy · mcp=False · prov=openai,local · tags=coding-agent,local,rust

**Qué es:** Ejecuta código y comandos en tu máquina para cumplir tareas descritas en lenguaje natural. Su versión actual se enfoca en modelos abiertos.
**Stack:** Rust, Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/openinterpreter/openinterpreter

**Instalación** [?]: `Seguir la instalación original: https://github.com/openinterpreter/openinterpreter/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un agente que ejecute código usando modelos abiertos
**Evita si:** buscas un agente maduro para repos grandes; mira `opencode`
**Combina con:** `ollama`, `e2b`
**Alternativas (elige una):** `goose`

## `open-swe`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=anthropic,openai · tags=coding-agent,agents,python

**Qué es:** Trabaja en segundo plano a partir de issues o mensajes, planifica, programa en un sandbox y abre PRs. Inspirado en los agentes internos de empresas como Stripe o Ramp.
**Stack:** Python, LangGraph, TypeScript
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/langchain-ai/open-swe

**Instalación** [?]: `Seguir la instalación original: https://github.com/langchain-ai/open-swe/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres construir el agente de código interno de tu empresa
**Evita si:** solo quieres un agente para tu terminal; mira `claude-code`
**Combina con:** `langgraph`, `e2b`
**Alternativas (elige una):** `openhands`, `swe-agent`

## `openclaude`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=coding,ai,ai-agent,ai-tools,cli,typescript

**Qué es:** Agente de código abierto para terminal que conecta proveedores remotos y modelos locales con herramientas y MCP. Mantiene una conversación de desarrollo con streaming, comandos y herramientas sobre el workspace.
**Stack:** TypeScript, Docker, Node.js
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Twigpine/openclaude

**Instalación** [+]: `npm install -g @twigpine/openclaude@latest`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres evaluar un agente de terminal compatible con varios backends
**Evita si:** un flujo determinista resuelve el problema sin un agente

## `opencode`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=coding-agent,agents,typescript

**Qué es:** Ofrece una TUI cuidada, modo cliente-servidor, LSP y agentes configurables. Sirve si quieres un agente libre de proveedor.
**Stack:** TypeScript, Go, Bun
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/anomalyco/opencode

**Instalación** [?]: `Seguir la instalación original: https://github.com/anomalyco/opencode/blob/dev/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un agente de código abierto y multi-modelo
**Evita si:** prefieres la experiencia oficial de un proveedor; mira `claude-code` o `codex`
**Combina con:** `ollama`, `litellm`, `awesome-agent-skills`
**Alternativas (elige una):** `claude-code`, `codex`, `goose`, `gemini-cli`, `aider`

## `opencode-legacy`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=coding,ai,claude,code,llm,openai,go

**Qué es:** Agente de código en Go del antiguo proyecto opencode-ai, archivado y continuado bajo el nombre Crush. Conserva una interfaz de terminal y el historial del agente original para consulta.
**Stack:** Go, Go modules
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/opencode-ai/opencode

**Instalación** [?]: `Seguir la instalación original: https://github.com/opencode-ai/opencode/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas estudiar la implementación histórica de OpenCode en Go
**Evita si:** un flujo determinista resuelve el problema sin un agente

## `opencode-manager`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=coding,agent,typescript

**Qué es:** Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil.
**Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El agente o la pasarela necesita un proveedor. Comprueba en su configuración la ruta de sesión, API o modelo elegida.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. El código de la aplicación no incluye el consumo de su proveedor. Comprueba plan, cuotas, infraestructura y servicios conectados.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/chriswritescode-dev/opencode-manager

**Instalación** [?]: `Seguir la instalación original: https://github.com/chriswritescode-dev/opencode-manager/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `opencursor`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=coding,agent,ai,code,coder,cursor,extension,ide

**Qué es:** Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos. Integra conversación y acciones sobre el workspace con proveedores remotos o locales y herramientas MCP.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/PawanOsman/OpenCursor

**Instalación** [?]: `Seguir la instalación original: https://github.com/PawanOsman/OpenCursor/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres evaluar un agente de código integrado en VS Code
**Evita si:** un flujo determinista resuelve el problema sin un agente

## `openhands`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,automation,typescript,docker

**Qué es:** El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.
**Stack:** Python/TS, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/OpenHands/OpenHands

**Instalación** [?]: `Seguir la instalación original: https://github.com/OpenHands/OpenHands/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un agente que "haga", no solo hable
**Evita si:** solo necesitas chat/RAG o no puedes correr Docker
**Combina con:** `ecc`, `sandbox`
**Alternativas (elige una):** `open-swe`, `swe-agent`

## `openidea`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=coding,app,typescript

**Qué es:** Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes.
**Stack:** TypeScript, Cargo.toml, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/l0ng-ai/openidea

**Instalación** [?]: `Seguir la instalación original: https://github.com/l0ng-ai/openidea/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `swe-agent`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic · tags=coding-agent,evaluation,python

**Qué es:** Resuelve issues reales con el modelo que elijas y sirve como base de investigación en agentes de software. También tiene usos en ciberseguridad y retos de programación.
**Stack:** Python, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/SWE-agent/SWE-agent

**Instalación** [?]: `Seguir la instalación original: https://github.com/SWE-agent/SWE-agent/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** investigas o automatizas la resolución de issues
**Evita si:** quieres un asistente diario en tu terminal; mira `claude-code`
**Combina con:** `swe-bench`, `litellm`
**Alternativas (elige una):** `openhands`, `open-swe`

## `t3code`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,ui,typescript

**Qué es:** No sustituye al agente: orquesta Claude Code, Codex y otros desde una UI cómoda, también en el móvil. Útil para lanzar y revisar sesiones a distancia.
**Stack:** TypeScript, Electron, React Native
**Acceso y costes:**
- API de IA: API de IA opcional. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
- Otras rutas: El README lista otros agentes y adaptadores ACP. T3 Code coordina esos agentes; cada uno conserva su autenticación y sus límites.
**Repo:** https://github.com/pingdotgg/t3code

**Instalación** [+]: `npx t3@latest`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** usas varios agentes de código y quieres controlarlos desde una UI
**Evita si:** solo usas un agente en la terminal
**Combina con:** `claude-code`, `codex`, `opencode`
