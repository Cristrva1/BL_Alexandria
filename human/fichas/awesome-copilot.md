[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Awesome GitHub Copilot

> Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub Copilot.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 41k | MIT | JavaScript | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Repositorio de la organización GitHub que reúne personalizaciones de Copilot aportadas por la comunidad: agentes especializados (algunos conectados a servidores MCP), instrucciones que se aplican por tipo de archivo, skills, plugins y un cookbook de recetas para las APIs de Copilot. Tiene web con búsqueda, un Learning Hub y un llms.txt para agentes.

## Por qué destaca

Es el marketplace que Copilot CLI y VS Code traen registrado por defecto, así que instalar un plugin es un solo comando. También sirve de referencia para escribir instrucciones y agentes de Copilot.

## Cómo funciona

Cada recurso es un archivo Markdown con frontmatter (agentes, instrucciones con patrones de archivo, skills con sus assets) y los plugins agrupan varios para un flujo. Copilot los carga desde el marketplace `awesome-copilot` o copiándolos a tu repo.

## Instalación rápida

`copilot plugin install <plugin>@awesome-copilot`; si tu versión no conoce el marketplace, ejecuta antes `copilot plugin marketplace add github/awesome-copilot`.

## Casos de uso

- Aplicar estándares de código por tipo de archivo en Copilot
- Instalar un plugin de agentes para un flujo de trabajo concreto
- Pasar a un agente el índice llms.txt de recursos de Copilot

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu equipo trabaja con GitHub Copilot en VS Code o Copilot CLI y quiere personalizarlo | usas Claude Code u otro agente; mira `claude-plugins-official` o `antigravity-awesome-skills` |

**Limitaciones:** Los recursos son de terceros: revisa cada agente o plugin antes de instalarlo, como advierte el propio repo.

## Stack y modelos

- **Stack:** Markdown, YAML, JavaScript (web del catálogo)
- **Modelos / API:** Los recursos los ejecuta GitHub Copilot con el modelo que tengas seleccionado (OpenAI, Anthropic, Google, etc.).
- **Etiquetas:** `skills` `coding-agent` `prompts` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [GitHub MCP Server](github-mcp-server.md) | 34.4k | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. |
| [Spec Kit](spec-kit.md) | 149k | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |
| [GitHub CLI](cli.md) | 46.9k | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. |

## Enlaces

- 🐙 GitHub: [github/awesome-copilot](https://github.com/github/awesome-copilot)
- 🌐 Web: <https://awesome-copilot.github.com/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
