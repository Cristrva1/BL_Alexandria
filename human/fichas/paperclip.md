[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🕸️ paperclip

> Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 114k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Paperclip, servidor Node.js con interfaz React para orquestar equipos de agentes de IA como si fueran una empresa. Licencia MIT. Creado en marzo de 2026, ya tiene ~114k estrellas; hay lista de espera para un servicio cloud.

## ¿Qué hace?

Defines objetivos de negocio, «contratas» agentes con roles (CEO, CTO…), apruebas la estrategia y fijas presupuestos. Incluye organigramas, gobernanza, seguimiento de tokens y costes por agente o proyecto, y conectores (GitHub, Notion, Railway, MCP).

## ¿Cómo lo hace?

Se inicia con `npx paperclipai@latest onboard --yes` o se prueba con `npx paperclipai test-drive` y una clave de proveedor. Funciona con OpenClaw, Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Hermes y otros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenClaw](openclaw.md) | Harness soportado. | Registra OpenClaw como agente. |
| [Claude Code](claude-code.md) | Harness soportado. | Instala Claude Code y asígnalo. |
| [Codex CLI](codex.md) | Harness soportado (`--harness codex`). | Instala Codex y asígnalo. |
| [hermes-agent](hermes-agent.md) | Harness soportado. | Registra Hermes vía su gateway. |

**Notas:** Alternativa (elige una): multica. Conviene vigilar el gasto con presupuestos.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2026.1106.0 (2026-11-06) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/paperclipai/paperclip/blob/master/README.md) · [2](https://docs.paperclip.ing/connectors/)</sub>

## Ver similares

Grupo **Paneles para coordinar equipos de agentes**: paperclip ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **paperclip** (esta ficha) ⭐ recomendado | 67 | Si buscas esto: servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. |
| 2 | [multica](multica.md) | 56 | Si buscas esto: workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Usa modelos y agentes propios; servidor, proveedores y servicios conectados tienen costes independientes |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El panel organiza trabajo y no constituye por sí solo una empresa autónoma; las integraciones Claude y Codex dependen de sus adaptadores y cuentas |
| Coste | El coste depende del proveedor o la ruta. Usa modelos y agentes propios; servidor, proveedores y servicios conectados tienen costes independientes |
| Equipo | Preparación según la ruta elegida. Node 24.11+; pnpm 9.15+ para desarrollo; agentes configurados; proyecto de prueba |

El panel organiza trabajo y no constituye por sí solo una empresa autónoma; las integraciones Claude y Codex dependen de sus adaptadores y cuentas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 24.11+
- pnpm 9.15+ para desarrollo
- agentes configurados
- proyecto de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.paperclip.ing/reference/cli/installation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar paperclip para mi objetivo y necesito pasos guiados. Lee https://docs.paperclip.ing/reference/cli/installation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una tarea de explicación para un agente y revisa historial y presupuesto antes de activar heartbeats.

**Qué comprobar:** Puedes atribuir una ejecución a su tarea, agente y coste registrado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar tareas de varios agentes
- Auditar una propuesta antes de aprobarla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar tareas de varios agentes; Auditar una propuesta antes de aprobarla | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El panel organiza trabajo y no constituye por sí solo una empresa autónoma; las integraciones Claude y Codex dependen de sus adaptadores y cuentas

## Stack y modelos

- **Stack:** Node 24.11+; pnpm 9.15+ para desarrollo; agentes configurados; proyecto de prueba
- **Etiquetas:** `asistentes` `acpx` `agent-orchestration` `agent-skills` `agentic-ai` `ai-agents` `ai-engineering` `ai-governance`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [multica](multica.md) | 56.1k | Workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias. |

## Enlaces

- 🐙 GitHub: [paperclipai/paperclip](https://github.com/paperclipai/paperclip)
- 🌐 Web: <https://paperclip.ing>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/paperclipai/paperclip/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
