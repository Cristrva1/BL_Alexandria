[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Escritura y calidad de texto

# 🧑 Humanizer

> Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 67.4k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Detecta 26 patrones típicos de la prosa de LLM (contrastes tipo 'no es X, es Y', cierres dramáticos, tríadas forzadas, frases de falsa profundidad, importancia inflada) y reescribe el texto sin cambiar lo que dice. Puede imitar tu estilo si le das una muestra y, sobre un archivo, solo toca la prosa: no el código, los datos ni el frontmatter.

## Por qué destaca

Parte de una fuente pública (la guía 'Signs of AI writing' de los editores de Wikipedia) y muestra su trabajo: primera reescritura, crítica de lo que aún suena artificial y versión final. No añade datos que no estuvieran en el original.

## Cómo funciona

El SKILL.md ordena los patrones por fuerza: los cinco primeros justifican un cambio con una sola aparición y los débiles solo cuentan si se acumulan. El agente marca las señales, redacta, contrasta el borrador con los patrones y las afirmaciones originales y entrega.

## Instalación rápida

En Claude Code: `/plugin marketplace add blader/humanizer` y `/plugin install humanizer@humanizer`; en otros agentes: `npx skills add blader/humanizer --global --agent '*'`.

## Casos de uso

- Quitar el tono IA de un post o un anuncio de producto
- Reescribir documentación generada sin perder los datos
- Ajustar un borrador a tu propia voz con una muestra

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| publicas textos redactados con IA y quieres que se lean como escritos por una persona | quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop` |

**Limitaciones:** Sus patrones y ejemplos están pensados para prosa en inglés, y no busca engañar a los detectores de IA, que siguen marcando la mayoría de sus salidas.

## Stack y modelos

- **Stack:** Markdown, SKILL.md
- **Modelos / API:** No llama a un LLM: la ejecuta tu agente (Claude Code, Codex, Claude.ai, Gemini CLI, Copilot, Windsurf, etc.).
- **Etiquetas:** `skills` `prompts` `docs`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marketing Skills](marketingskills.md) | 59.5k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stop Slop](stop-slop.md) | 18.8k | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. |

## Enlaces

- 🐙 GitHub: [blader/humanizer](https://github.com/blader/humanizer)
- 🌐 Web: <https://skills.sh/blader/humanizer>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
