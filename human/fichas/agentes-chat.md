[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🖥️ agentes-chat

> Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.4k | AGPL-3.0 | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

agentes.chat, alternativa autoalojada a Slack donde trabajan juntos personas y agentes de IA, de Codari Global, LLC. Licencia AGPL-3.0, con licencia comercial y CLA. Es muy reciente (noviembre de 2026, ~1.5k estrellas) y tiene app de escritorio.

## ¿Qué hace?

Los agentes son miembros del workspace, con rol, responsable y presupuesto, y piden aprobación para acciones sensibles (merges, despliegues). Usan Claude, ChatGPT/Codex, Gemini, Grok u OpenRouter, herramientas MCP, y tienen su propio ordenador y navegador.

## ¿Cómo lo hace?

Se instala con un comando en un servidor Linux; la única dependencia es Postgres. También hay versión Cloud de pago con el mismo código.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Herramienta de trabajo de los agentes. | Conecta tu cuenta de Claude. |
| [Codex CLI](codex.md) | Herramienta de trabajo de los agentes. | Conecta Codex. |
| [GitHub MCP Server](github-mcp-server.md) | Conector MCP por URL. (combinación por arquitectura) | Añade el servidor desde el panel de la organización. |

**Notas:** Sin alternativas declaradas. Proyecto muy joven.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada desktop-v0.8.10 (2026-11-15) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/agentes-chat/agentes-chat/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Autoalojado AGPL, Cloud de pago y licencia comercial alternativa; API o cuentas de agentes por separado |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Claude Code puede usarse en computadora conectada; la ruta Codex está todavía en pruebas y no se presenta como verificación de producción |
| Coste | El coste depende del proveedor o la ruta. Autoalojado AGPL, Cloud de pago y licencia comercial alternativa; API o cuentas de agentes por separado |
| Equipo | Preparación según la ruta elegida. Docker Compose y PostgreSQL; proveedor o computadora conectada; equipo de prueba |

Claude Code puede usarse en computadora conectada; la ruta Codex está todavía en pruebas y no se presenta como verificación de producción

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker Compose y PostgreSQL
- proveedor o computadora conectada
- equipo de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/agentes-chat/agentes-chat/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar agentes-chat para mi objetivo y necesito pasos guiados. Lee https://github.com/agentes-chat/agentes-chat/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un canal de prueba y pide al agente una respuesta sin conectar acciones externas.

**Qué comprobar:** Puedes revisar conversación, herramientas permitidas y aprobaciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evaluar un espacio de colaboración con agentes
- Organizar consultas en canales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evaluar un espacio de colaboración con agentes; Organizar consultas en canales | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude Code puede usarse en computadora conectada; la ruta Codex está todavía en pruebas y no se presenta como verificación de producción

## Stack y modelos

- **Stack:** Docker Compose y PostgreSQL; proveedor o computadora conectada; equipo de prueba
- **Etiquetas:** `asistentes` `agent` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [agentes-chat/agentes-chat](https://github.com/agentes-chat/agentes-chat)
- 🌐 Web: <https://agentes.chat>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/agentes-chat/agentes-chat/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
