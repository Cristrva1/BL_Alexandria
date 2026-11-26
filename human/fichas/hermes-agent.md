[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# ☤ hermes-agent

> Asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 263k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Hermes Agent, agente de Nous Research que se mejora a sí mismo. Licencia MIT. Es muy activo (~264k estrellas) y tiene versión de escritorio.

## ¿Qué hace?

Tiene un bucle de aprendizaje: crea skills a partir de la experiencia, las mejora con el uso y mantiene memoria curada con búsqueda FTS5 entre sesiones. Atiende por TUI, Telegram, Discord, Slack, WhatsApp y Signal desde un único gateway, programa automatizaciones con cron, lanza subagentes y se conecta a MCP.

## ¿Cómo lo hace?

Se instala con `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`, que instala Python 3.14, Node y otras dependencias, o con PowerShell o MSIX. Funciona con Nous Portal, OpenRouter, OpenAI o endpoints propios, en seis backends de terminal (local, Docker, SSH, Modal, Daytona, Vercel Sandbox). Puede importar configuración y memoria de OpenClaw, Claude Code, Codex o Cursor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [NemoClaw](nemoclaw.md) | Ejecutar Hermes con más aislamiento en el stack de NVIDIA. | Instala NemoClaw y lanza Hermes dentro. |
| [Ollama](ollama.md) | Endpoint propio con modelos locales. (combinación por arquitectura) | Configura el endpoint compatible con OpenAI. |
| [ECC](ecc.md) | Skills y configuración reutilizables. (combinación por arquitectura) | Importa las skills que apliquen. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (13). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[agentmemory](agentmemory.md) · [awesome-agents](awesome-agents.md) · [book-to-skill](book-to-skill.md) · [dsh-noema](dsh-noema.md) · [gods-eye-view](gods-eye-view.md) · [Hermes Desktop](hermes-desktop.md) · [hermes-agent-self-evolution](hermes-agent-self-evolution.md) · [Letta](letta.md) · [magnitude](magnitude.md) · [osiris](osiris.md) · [paperclip](paperclip.md) · [superpowers](superpowers.md) · [video-use](video-use.md)

**Notas:** Alternativas (elige una): openclaw, mercury-agent.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.23.1 (2026-11-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NousResearch/hermes-agent/blob/main/README.md) · [2](https://hermes-agent.nousresearch.com/docs/integrations/providers)</sub>

## Ver similares

Grupo **Asistentes personales autónomos**: hermes-agent ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenClaw](openclaw.md) ⭐ recomendado | 83 | Si buscas esto: asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| 2 | **hermes-agent** (esta ficha) | 74 | Si buscas esto: asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados. |
| 3 | [Mercury Agent](mercury-agent.md) | 49 | Si buscas esto: agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. API, Portal por suscripción o endpoint local según configuración; documenta también ruta ChatGPT/Codex |
| Claude Code | Referencia para la herramienta; no es una integración |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Importar ajustes e historial de Claude Code no equivale a usar su plan como motor; las herramientas de búsqueda, voz e imagen tienen proveedores separados |
| Coste | El coste depende del proveedor o la ruta. API, Portal por suscripción o endpoint local según configuración; documenta también ruta ChatGPT/Codex |
| Equipo | Preparación según la ruta elegida. Equipo compatible; proveedor o endpoint local; perfil de prueba |

Importar ajustes e historial de Claude Code no equivale a usar su plan como motor; las herramientas de búsqueda, voz e imagen tienen proveedores separados

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Equipo compatible
- proveedor o endpoint local
- perfil de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Comando copiado literalmente de el README (sección «Linux, macOS, WSL2»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/NousResearch/hermes-agent/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar hermes-agent para mi objetivo y necesito pasos guiados. Lee https://github.com/NousResearch/hermes-agent/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un perfil nuevo y pide recordar una nota ficticia antes de importar historial.

**Qué comprobar:** Puedes comprobar la nota guardada y el proveedor usado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evaluar memoria de un asistente
- Comparar un modelo local con Nous Portal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evaluar memoria de un asistente; Comparar un modelo local con Nous Portal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Importar ajustes e historial de Claude Code no equivale a usar su plan como motor; las herramientas de búsqueda, voz e imagen tienen proveedores separados

## Stack y modelos

- **Stack:** Equipo compatible; proveedor o endpoint local; perfil de prueba
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenClaw](openclaw.md) | 394k | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| [Mercury Agent](mercury-agent.md) | 3.9k | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. |

## Enlaces

- 🐙 GitHub: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 🌐 Web: <https://hermes-agent.nousresearch.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NousResearch/hermes-agent/blob/main/README.md)
- [Fuente 2](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
