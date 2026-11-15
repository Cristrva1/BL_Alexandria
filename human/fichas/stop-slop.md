[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Escritura y calidad de texto

# 🧹 Stop Slop

> Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 18.8k | MIT | — | 2026-03-17 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Un SKILL.md con tres archivos de referencia (frases a eliminar, estructuras a evitar y ejemplos antes/después) que enseña a Claude o a cualquier LLM a quitar muletillas, contrastes binarios, fragmentos dramáticos, voz pasiva y otros patrones predecibles. Cierra con una rúbrica de cinco dimensiones para decidir si el texto necesita otra vuelta.

## Por qué destaca

Es corto, sin dependencias y portable: funciona como skill de Claude Code, como conocimiento de un proyecto de Claude o pegado en un system prompt. La rúbrica sobre 50 puntos da un criterio concreto para revisar.

## Cómo funciona

El SKILL.md fija reglas de frase (sin aperturas de relleno, sin rayas, sin extremos vagos, voz activa) y remite a los archivos de referencia, que se cargan cuando hacen falta. Cada texto se puntúa en franqueza, ritmo, confianza, autenticidad y densidad.

## Instalación rápida

`git clone https://github.com/hardikpandya/stop-slop ~/.claude/skills/stop-slop`; en otros entornos, pega el contenido de `SKILL.md` en tus instrucciones o en el system prompt.

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
- **Modelos / API:** No llama a un LLM: lo aplica tu agente o el modelo al que le pases el SKILL.md (Claude u otro).
- **Etiquetas:** `skills` `prompts` `docs`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marketing Skills](marketingskills.md) | 59.5k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Humanizer](humanizer.md) | 67.4k | Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA. |

## Enlaces

- 🐙 GitHub: [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
