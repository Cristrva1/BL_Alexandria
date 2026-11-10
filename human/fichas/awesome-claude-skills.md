[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Awesome Claude Skills

> Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 79.2k | — | Python | 2026-09-18 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## Qué es

Recopilación de skills por áreas (documentos, desarrollo, datos, marketing, escritura, multimedia, productividad, seguridad) que enlaza skills oficiales de Anthropic y de la comunidad, y aloja algunas propias. Incluye el plugin connect-apps, que usa Composio para que Claude envíe correos, cree issues o publique en Slack.

## Por qué destaca

Cubre tareas de negocio y productividad además de programación, y explica bien la diferencia entre una skill y un MCP. Su plugin de Composio añade acciones reales en apps externas, algo que las skills solas no dan.

## Cómo funciona

Es un README por categorías con enlaces a cada skill, más algunas carpetas de skills dentro del propio repo. El plugin connect-apps se carga en Claude Code y delega la autenticación y las llamadas a la plataforma de Composio.

## Instalación rápida

No se instala entero: copia la carpeta de la skill que quieras a `~/.claude/skills/`. Para el plugin de apps: `claude --plugin-dir ./connect-apps-plugin` y luego `/connect-apps:setup` con tu API key de Composio.

## Casos de uso

- Encontrar skills de documentos, datos o marketing para Claude
- Conectar Claude a Gmail, Slack o GitHub mediante Composio
- Ver ejemplos de skills de comunidad antes de crear la tuya

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas Claude para tareas de negocio además de código y quieres skills ordenadas por área de trabajo | solo quieres skills de procedencia oficial; mira `anthropic-skills` o `awesome-agent-skills` |

**Limitaciones:** Mezcla skills de terceros de calidad desigual y promociona Composio; el plugin de apps requiere cuenta y API key de Composio.

## Stack y modelos

- **Stack:** Markdown, Python, Composio (plugin connect-apps)
- **Modelos / API:** Pensada para Claude (Claude.ai, Claude Code y la API); muchas skills también funcionan en Codex, Cursor o Gemini CLI.
- **Etiquetas:** `skills` `automation` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Composio](composio.md) | 31k | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. |
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [SkillSpector](skillspector.md) | 25.2k | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Agent Skills](awesome-agent-skills.md) | 37k | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. |
| [Agentic Awesome Skills](antigravity-awesome-skills.md) | 49.5k | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. |
| [Awesome Claude Code](awesome-claude-code.md) | 57.7k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |

## Enlaces

- 🐙 GitHub: [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
