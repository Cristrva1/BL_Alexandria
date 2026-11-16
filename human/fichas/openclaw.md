[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🦾 OpenClaw

> Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 394k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

OpenClaw, asistente de IA personal open source que corre en tu equipo y atiende en tus canales de chat. Licencia MIT. Lo desarrolla la OpenClaw Foundation, una organización 501(c)(3) independiente, y es el repo con más estrellas del catálogo (~395k).

## ¿Qué hace?

Atiende por Discord, iMessage, Slack, Teams, Telegram, WhatsApp y más de 20 canales, además de apps nativas. El estado, la memoria y las credenciales se quedan en tu hardware, y los modelos y harnesses de agente (Claude, Codex, modelos locales) son plugins intercambiables.

## ¿Cómo lo hace?

Se instala con `curl -fsSL https://openclaw.ai/install.sh | bash` o PowerShell, o con `npm install -g openclaw@latest` (Node 24.16+ o 26.1+; se recomiendan las versiones con parches de seguridad). También hay rutas con Docker y Nix, y el instalador lanza el onboarding.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [NemoClaw](nemoclaw.md) | Stack de NVIDIA para ejecutar OpenClaw con más aislamiento. | Instala NemoClaw y lanza OpenClaw dentro. |
| [claude-mem](claude-mem.md) | Plugin de memoria persistente para gateways OpenClaw. | Instala claude-mem con su comando para OpenClaw. |
| [Claude Code](claude-code.md) | Harness de agente como plugin. | Configura Claude como harness. |
| [Ollama](ollama.md) | Modelos locales como plugin. (combinación por arquitectura) | Configura un proveedor local. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (10). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Agent-Reach](agent-reach.md) · [awesome-agents](awesome-agents.md) · [cognee](cognee.md) · [Letta](letta.md) · [OpenMAIC](openmaic.md) · [OpenViking](openviking.md) · [paperclip](paperclip.md) · [Qwen Code](qwen-code.md) · [signal-cli](signal-cli.md) · [Vibe-Trading](vibe-trading.md)

**Notas:** Alternativas (elige una): hermes-agent, mercury-agent. Superficie de ataque amplia (canales y credenciales): conviene aislarlo.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2026.11.4 (2026-11-16) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openclaw/openclaw/blob/main/README.md) · [2](https://docs.openclaw.ai/install)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Modelos locales, API y harnesses con cuentas tienen costes distintos; los canales también pueden cobrar |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La interfaz y memoria locales no mantienen locales los prompts enviados a proveedores; el backend Claude CLI usa el ejecutable autenticado y Codex tiene su propio harness |
| Coste | El coste depende del proveedor o la ruta. Modelos locales, API y harnesses con cuentas tienen costes distintos; los canales también pueden cobrar |
| Equipo | Preparación según la ruta elegida. Node compatible o instalador; proveedor o harness; canal de prueba opcional |

La interfaz y memoria locales no mantienen locales los prompts enviados a proveedores; el backend Claude CLI usa el ejecutable autenticado y Codex tiene su propio harness

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node compatible o instalador
- proveedor o harness
- canal de prueba opcional

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openclaw/openclaw/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenClaw para mi objetivo y necesito pasos guiados. Lee https://github.com/openclaw/openclaw/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Completa onboarding y consulta gateway status y dashboard antes de conectar mensajería.

**Qué comprobar:** Puedes identificar estado, proveedor y permisos del Gateway.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un asistente personal
- Conectar un agente a un canal propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un asistente personal; Conectar un agente a un canal propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La interfaz y memoria locales no mantienen locales los prompts enviados a proveedores; el backend Claude CLI usa el ejecutable autenticado y Codex tiene su propio harness

## Stack y modelos

- **Stack:** Node compatible o instalador; proveedor o harness; canal de prueba opcional
- **Etiquetas:** `agents` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [hermes-agent](hermes-agent.md) | 263k | Asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados. |
| [Mercury Agent](mercury-agent.md) | 3.9k | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. |

## Enlaces

- 🐙 GitHub: [openclaw/openclaw](https://github.com/openclaw/openclaw)
- 🌐 Web: <https://openclaw.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openclaw/openclaw/blob/main/README.md)
- [Fuente 2](https://docs.openclaw.ai/gateway/cli-backends)
- [Fuente 3](https://docs.openclaw.ai/concepts/model-providers)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
