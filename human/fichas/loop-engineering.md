[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 Loop Engineering

> Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.8k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Propone dejar de escribir prompts aislados y diseñar ciclos con objetivo, verificación y puntuación para que el agente itere solo. Incluye starters y herramientas de línea de comandos.

## Por qué destaca

Enfoque práctico y medible: cada bucle termina con una puntuación que guía la siguiente iteración.

## Cómo funciona

Define el objetivo, las comprobaciones y el criterio de parada en archivos que el agente lee y ejecuta en bucle.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/cobusgreyling/loop-engineering/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Loop Engineering para mi objetivo y necesito pasos guiados. Lee https://github.com/cobusgreyling/loop-engineering/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Refactors largos con verificación automática
- Mejorar un prompt con puntuación
- Agentes que iteran hasta pasar tests

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres que tu agente de código itere solo con criterios medibles | solo necesitas una lista de skills; mira `awesome-agent-skills` |

## Stack y modelos

- **Stack:** TypeScript, Markdown
- **Etiquetas:** `coding-agent` `skills` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |

## Enlaces

- 🐙 GitHub: [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)
- 🌐 Web: <https://cobusgreyling.github.io/loop-engineering/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/cobusgreyling/loop-engineering/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
