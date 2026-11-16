[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🦾 Mercury Agent

> Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.9k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Mercury, agente personal open source «con alma» (personalidad escrita por el usuario), de cosmicstack-labs. Licencia MIT. Tiene ~4k estrellas.

## ¿Qué hace?

Lee y escribe archivos, ejecuta comandos, trabaja con git y GitHub, investiga en la web y gestiona una agenda, comprobando cada acción con tus reglas de permisos y un presupuesto diario de tokens. Mercury Code actúa como programador en pareja y Mercury Bots como equipo de especialistas programados.

## ¿Cómo lo hace?

Se instala con un instalador de una línea o con `npm i -g @cosmicstack/mercury-agent` (Node 22+), en macOS, Linux, Windows y Android (Termux). Se usa desde TUI, Telegram, Discord, Slack, Signal o un panel web, con DeepSeek, OpenAI, Anthropic, Grok, Ollama, LM Studio o endpoints compatibles.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local documentado. | Configura Ollama Local. |
| [litellm](litellm.md) | Proxy compatible documentado. | Apunta el endpoint compatible con OpenAI al proxy. |
| [SearXNG](searxng.md) | Búsqueda web autoalojada. (combinación por arquitectura) | Expón SearXNG si el agente lo admite. |

**Notas:** Alternativas (elige una): openclaw, hermes-agent. Se quita claude-mem (es un plugin de Claude Code y OpenClaw, no de Mercury).

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.5.2 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md)</sub>

## Ver similares

Grupo **Asistentes personales autónomos**: Mercury Agent ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenClaw](openclaw.md) ⭐ recomendado | 82 | Si buscas esto: asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| 2 | [hermes-agent](hermes-agent.md) | 74 | Si buscas esto: asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados. |
| 3 | **Mercury Agent** (esta ficha) | 49 | Si buscas esto: agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. API, Mercury Cloud o modelos locales según elección; Ollama Cloud no es inferencia local |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El asistente inicia un servicio en segundo plano; revisa su estado antes de añadir canales o ejecución programada |
| Coste | El coste depende del proveedor o la ruta. API, Mercury Cloud o modelos locales según elección; Ollama Cloud no es inferencia local |
| Equipo | Preparación según la ruta elegida. Node 22 o posterior; proveedor u Ollama/LM Studio; perfil de prueba |

El asistente inicia un servicio en segundo plano; revisa su estado antes de añadir canales o ejecución programada

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 22 o posterior
- proveedor u Ollama/LM Studio
- perfil de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm i -g @cosmicstack/mercury-agent
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Mercury Agent para mi objetivo y necesito pasos guiados. Lee https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca mercury, comprueba status y pide una respuesta sobre una nota ficticia sin conectar canales.

**Qué comprobar:** Puedes identificar proveedor, servicio en segundo plano y permisos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un asistente persistente
- Estudiar presupuestos de tokens

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar presupuestos de tokens | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El asistente inicia un servicio en segundo plano; revisa su estado antes de añadir canales o ejecución programada

## Stack y modelos

- **Stack:** Node 22 o posterior; proveedor u Ollama/LM Studio; perfil de prueba
- **Etiquetas:** `agents` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenClaw](openclaw.md) | 394k | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. |
| [hermes-agent](hermes-agent.md) | 263k | Asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados. |

## Enlaces

- 🐙 GitHub: [cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)
- 🌐 Web: <https://mercuryagent.sh/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cosmicstack-labs/mercury-agent/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
