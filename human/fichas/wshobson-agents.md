[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ wshobson/agents

> Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 42.4k | MIT | Python | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Colección de Seth Hobson que agrupa subagentes especialistas, skills y comandos en plugins por área: desarrollo Python y JavaScript, revisión de código, testing, infraestructura, seguridad y más. Se escribe una sola vez en formato de plugin de Claude Code y unos adaptadores generan las versiones para Codex, Cursor, OpenCode, Antigravity CLI, GitHub Copilot y Pi.

## Por qué destaca

Instalas solo el plugin que necesitas en lugar de cientos de archivos sueltos y mantienes el mismo set en varios agentes. Incluye `plugin-eval` para puntuar skills con chequeos estáticos.

## Cómo funciona

Cada plugin de `plugins/` agrupa agentes (con alias de modelo como opus o sonnet), skills y comandos en Markdown. Los marketplaces nativos apuntan a esa fuente y adaptadores en Python generan el formato de cada herramienta.

## Instalación rápida

En Claude Code: `/plugin marketplace add wshobson/agents` y `/plugin install python-development@claude-code-workflows`. Solo una skill: `npx skills add wshobson/agents --skill <skill>`.

## Casos de uso

- Añadir subagentes de Python o TypeScript a Claude Code
- Lanzar un escaneo de seguridad con un comando del plugin
- Compartir el mismo set de agentes entre Claude Code y Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres subagentes y comandos especializados por lenguaje o área, instalables plugin a plugin | solo quieres plugins oficiales de Anthropic y socios; mira `claude-plugins-official` |

**Limitaciones:** Las funciones dependen de la herramienta: Codex, Copilot u OpenCode reciben versiones generadas con menos capacidades que Claude Code.

## Stack y modelos

- **Stack:** Markdown, Python (uv), Make
- **Modelos / API:** Los ejecuta tu agente de código; los subagentes usan alias de modelos Claude (opus, sonnet, haiku) que se traducen a cada herramienta.
- **Etiquetas:** `skills` `coding-agent` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [SkillSpector](skillspector.md) | 25.2k | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code Plugins Directory](claude-plugins-official.md) | 46.7k | Marketplace oficial de Anthropic con plugins para Claude Code, propios y de socios: comandos, agentes, skills y servidores MCP. |
| [Agentic Awesome Skills](antigravity-awesome-skills.md) | 49.5k | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. |
| [The Agency (agency-agents)](agency-agents.md) | 168k | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. |

## Enlaces

- 🐙 GitHub: [wshobson/agents](https://github.com/wshobson/agents)
- 🌐 Web: <https://sethhobson.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
