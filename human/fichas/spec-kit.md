[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧭 Spec Kit

> Kit de GitHub para desarrollo guiado por especificaciones con agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 150k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Te guía para escribir especificación, plan y tareas antes de que el agente programe. Funciona con Copilot, Claude Code, Gemini CLI y otros.

## Por qué destaca

Respaldo oficial de GitHub y un flujo simple que mejora mucho la calidad del código generado.

## Cómo funciona

El CLI `specify` crea plantillas y comandos (/specify, /plan, /tasks) que tu agente ejecuta por fases.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/github/spec-kit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Spec Kit para mi objetivo y necesito pasos guiados. Lee https://github.com/github/spec-kit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Arrancar un proyecto nuevo con especificación
- Dividir una función grande en tareas
- Alinear a varios agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres que el agente siga una especificación antes de programar | buscas roles completos de equipo ágil; mira `bmad-method` |

## Stack y modelos

- **Stack:** Python, Markdown
- **Etiquetas:** `coding-agent` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [Gemini CLI](gemini-cli.md) | 109k | Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [BMAD Method](bmad-method.md) | 55.4k | Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. |

## Enlaces

- 🐙 GitHub: [github/spec-kit](https://github.com/github/spec-kit)
- 🌐 Web: <https://github.github.com/spec-kit/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/github/spec-kit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
