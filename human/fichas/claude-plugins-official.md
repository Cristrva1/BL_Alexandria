[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🔌 Claude Code Plugins Directory

> Marketplace oficial de Anthropic con plugins para Claude Code, propios y de socios: comandos, agentes, skills y servidores MCP.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 46.7k | Apache-2.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Directorio curado desde el que Claude Code instala plugins de forma nativa. En `/plugins` están los que mantiene Anthropic (revisión de código y PR, desarrollo de features, diseño frontend, hooks, gestión de CLAUDE.md, skill-creator) y en `/external_plugins` los de socios y comunidad que pasan su revisión (Figma, Atlassian, Cloudflare, Firebase, Context7, Superpowers y cientos más).

## Por qué destaca

Es la fuente oficial: viene integrada en el sistema de plugins de Claude Code y los plugins externos deben cumplir criterios de calidad y seguridad para entrar. Evita copiar archivos a mano.

## Cómo funciona

Cada plugin es una carpeta con `.claude-plugin/plugin.json` y, si los necesita, comandos, agentes, skills y un `.mcp.json` con servidores MCP. Claude Code lee el `marketplace.json` del repo e instala cada plugin por su nombre.

## Instalación rápida

En Claude Code: `/plugin install <plugin>@claude-plugins-official`, o explora el catálogo en `/plugin` > Discover.

## Casos de uso

- Añadir revisión de PR y comandos de commit a Claude Code
- Conectar Claude Code a Figma, Atlassian o Firebase con un plugin
- Usar `example-plugin` como base para publicar el tuyo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas Claude Code y quieres plugins oficiales o de socios que se instalan con un comando | buscas recursos comunitarios o trabajas con otro agente; mira `awesome-claude-code` o `wshobson-agents` |

**Limitaciones:** Anthropic no controla el contenido de los plugins externos ni de sus servidores MCP: revisa cada plugin antes de instalarlo.

## Stack y modelos

- **Stack:** Markdown, JSON, Python, MCP
- **Modelos / API:** Los plugins los ejecuta Claude Code con modelos de Anthropic; algunos añaden servidores MCP de terceros.
- **Etiquetas:** `skills` `coding-agent` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Anthropic Skills](anthropic-skills.md) | 192k | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. |
| [Awesome Claude Code](awesome-claude-code.md) | 57.7k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [wshobson/agents](wshobson-agents.md) | 42.4k | Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- 🌐 Web: <https://code.claude.com/docs/en/plugins>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
