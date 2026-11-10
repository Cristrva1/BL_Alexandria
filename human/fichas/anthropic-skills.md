[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Anthropic Skills

> Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 192k | — | Python | 2026-11-06 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Repositorio de Anthropic con skills listas para Claude Code, Claude.ai y la API: creativas, técnicas (pruebas de apps web, creación de servidores MCP) y empresariales, más las skills de docx, pptx, xlsx y PDF que Claude usa para generar archivos. Incluye la especificación del estándar Agent Skills y una plantilla para crear las tuyas.

## Por qué destaca

Es la implementación de referencia del formato SKILL.md, publicada por quien definió el estándar. Las skills de documentos son las que Claude usa en producción, así que sirven de modelo para skills complejas.

## Cómo funciona

Cada skill es una carpeta con un SKILL.md (frontmatter YAML con nombre y descripción, más instrucciones) y a veces scripts. Claude ve la descripción y carga el contenido completo solo cuando la tarea lo pide.

## Instalación rápida

En Claude Code: `/plugin marketplace add anthropics/skills` y luego `/plugin install document-skills@anthropic-agent-skills` (o `example-skills@anthropic-agent-skills`).

## Casos de uso

- Crear y editar docx, pptx, xlsx y PDF desde Claude Code
- Generar un servidor MCP con la skill mcp-builder
- Escribir tus propias skills partiendo de skill-creator o la plantilla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres skills oficiales de Anthropic o un ejemplo de referencia para escribir las tuyas | buscas volumen o skills de comunidad para varios agentes; mira `awesome-agent-skills` o `antigravity-awesome-skills` |

**Limitaciones:** Son skills de demostración y las de documentos (docx, pdf, pptx, xlsx) son source-available, no open source.

## Stack y modelos

- **Stack:** Markdown, YAML, Python, JavaScript
- **Modelos / API:** No llama a un LLM por sí mismo: las skills las ejecuta Claude (Claude Code, Claude.ai o la API de Claude).
- **Etiquetas:** `skills` `docs` `pdf` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Claude Code Plugins Directory](claude-plugins-official.md) | 46.7k | Marketplace oficial de Anthropic con plugins para Claude Code, propios y de socios: comandos, agentes, skills y servidores MCP. |
| [superpowers](superpowers.md) | 315k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |

## Enlaces

- 🐙 GitHub: [anthropics/skills](https://github.com/anthropics/skills)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
