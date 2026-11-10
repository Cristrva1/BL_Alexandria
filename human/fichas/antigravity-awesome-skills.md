[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Agentic Awesome Skills

> Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 49.5k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Antes llamada Antigravity Awesome Skills, reúne miles de skills por dominio (desarrollo, seguridad, DevOps, datos, marketing) instalables en Claude Code, Codex, Cursor, Gemini CLI, Kiro, OpenCode y otros agentes. Incluye bundles por rol, plugins temáticos y AAS Core, un MCP local para que el agente busque en el catálogo y elija skills antes de instalarlas.

## Por qué destaca

Destaca por volumen y por su instalador, que filtra por categoría, nivel de riesgo o lista exacta de ids. Con AAS Core el agente consulta el catálogo bajo demanda en lugar de cargar miles de skills en su contexto.

## Cómo funciona

Cada skill vive en `skills/<nombre>/SKILL.md` y un índice JSON describe el catálogo. El CLI de npm copia la selección a la carpeta de skills de cada agente y AAS Core expone el catálogo como servidor MCP local con vista previa del plan.

## Instalación rápida

`npx agentic-awesome-skills --claude` (o `--codex`, `--cursor`, `--gemini`, `--path ./mis-skills`); añade `--skills <ids> --dry-run` para previsualizar. En Claude Code también: `/plugin marketplace add sickn33/agentic-awesome-skills`.

## Casos de uso

- Instalar solo las skills de un dominio con filtros de categoría
- Dejar que Codex o Claude elijan skills a través del MCP AAS Core
- Dar el mismo set de skills a varios agentes de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres cubrir muchos dominios con skills ya escritas y trabajas con uno o varios agentes de código | prefieres pocas skills oficiales y revisadas; mira `anthropic-skills` o `awesome-agent-skills` |

**Limitaciones:** La calidad varía entre skills de terceros y algunas dependen de servicios externos de pago; revísalas antes de instalarlas (por ejemplo con `skillspector`).

## Stack y modelos

- **Stack:** Markdown, JavaScript (Node.js 22+), Python, MCP
- **Modelos / API:** No llama a un LLM: las skills las ejecuta tu agente de código (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, etc.).
- **Etiquetas:** `skills` `coding-agent` `mcp` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SkillSpector](skillspector.md) | 25.2k | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. |
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Agent Skills](awesome-agent-skills.md) | 37k | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. |
| [Awesome Claude Skills](awesome-claude-skills.md) | 79.2k | Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps. |
| [wshobson/agents](wshobson-agents.md) | 42.4k | Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot. |

## Enlaces

- 🐙 GitHub: [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)
- 🌐 Web: <https://aaskills.tech/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
