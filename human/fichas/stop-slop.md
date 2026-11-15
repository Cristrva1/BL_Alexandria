[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Escritura y calidad de texto

# 🧹 Stop Slop

> Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.9k | MIT | — | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Un SKILL.md con tres archivos de referencia (frases a eliminar, estructuras a evitar y ejemplos antes/después) que enseña a Claude o a cualquier LLM a quitar muletillas, contrastes binarios, fragmentos dramáticos, voz pasiva y otros patrones predecibles. Cierra con una rúbrica de cinco dimensiones para decidir si el texto necesita otra vuelta.

## Por qué destaca

Es corto, sin dependencias y portable: funciona como skill de Claude Code, como conocimiento de un proyecto de Claude o pegado en un system prompt. La rúbrica sobre 50 puntos da un criterio concreto para revisar.

## Cómo funciona

El SKILL.md fija reglas de frase (sin aperturas de relleno, sin rayas, sin extremos vagos, voz activa) y remite a los archivos de referencia, que se cargan cuando hacen falta. Cada texto se puntúa en franqueza, ritmo, confianza, autenticidad y densidad.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/hardikpandya/stop-slop/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stop Slop para mi objetivo y necesito pasos guiados. Lee https://github.com/hardikpandya/stop-slop/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Limpiar muletillas y estructuras cliché de un borrador
- Fijar reglas de estilo en el system prompt de una app
- Puntuar un texto antes de publicarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt | prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer` |

**Limitaciones:** Reglas pensadas para prosa en inglés y algunas muy estrictas (prohíbe todos los adverbios y las rayas); el repo casi no recibe cambios desde marzo de 2026.

## Stack y modelos

- **Stack:** Markdown, SKILL.md
- **Etiquetas:** `skills` `prompts` `docs`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marketing Skills](marketingskills.md) | 60.4k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Humanizer](humanizer.md) | 69.1k | Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA. |

## Enlaces

- 🐙 GitHub: [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/hardikpandya/stop-slop/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
