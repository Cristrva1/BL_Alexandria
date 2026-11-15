[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Skills de dominio: marketing, SEO y negocio

# 🏢 The Agency (agency-agents)

> Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 168k | MIT | Shell | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Plantillas de subagente en Markdown agrupadas por divisiones, como una agencia completa: ingeniería, diseño, paid media, ventas, marketing, producto, testing, seguridad, soporte, finanzas, videojuegos y más. Cada agente define identidad, misión, flujo de trabajo, entregables con ejemplos y métricas de éxito, y hay runbooks que arman equipos para escenarios como un MVP o una campaña.

## Por qué destaca

Cada agente es un rol concreto con proceso y entregables, no un prompt genérico, y los scripts lo adaptan a más de una docena de herramientas. Puedes instalar solo las divisiones que vayas a usar.

## Cómo funciona

Los agentes son archivos `.md` por división; `convert.sh` genera el formato de cada herramienta e `install.sh` los copia a su carpeta (por ejemplo `~/.claude/agents/`). También hay una app de escritorio que instala y actualiza el roster.

## Instalación rápida

`git clone https://github.com/msitarzewski/agency-agents && cd agency-agents && ./scripts/install.sh --tool claude-code --division engineering,marketing`, o la app de escritorio (`brew install --cask msitarzewski/agency-agents/agency-agents`).

## Casos de uso

- Activar un agente de marketing o paid media en Claude Code
- Montar un equipo de agentes para un MVP con un runbook
- Usar los mismos roles en Cursor, Codex o Gemini CLI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres roles de negocio y técnicos ya definidos (marketing, ventas, producto, ingeniería) para tu agente de código | solo necesitas skills de marketing y growth; mira `marketingskills` |

**Limitaciones:** Son definiciones de rol en Markdown que no ejecutan nada por sí solas; además OpenCode solo registra unos 119 agentes, así que conviene instalar por divisiones.

## Stack y modelos

- **Stack:** Markdown, Bash, Python
- **Modelos / API:** No llama a un LLM: los agentes los ejecuta tu herramienta (Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Aider, etc.).
- **Etiquetas:** `agents` `prompts` `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marketing Skills](marketingskills.md) | 59.5k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |
| [GEO-SEO Claude](geo-seo-claude.md) | 11.6k | Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF. |
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [wshobson/agents](wshobson-agents.md) | 42.4k | Marketplace de 94 plugins con más de 200 subagentes, 185 skills y 105 comandos para Claude Code, Codex, Cursor, OpenCode y Copilot. |

## Enlaces

- 🐙 GitHub: [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
