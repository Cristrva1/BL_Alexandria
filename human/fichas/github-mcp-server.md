[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 GitHub MCP Server

> Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 34.4k | MIT | Go | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Conecta asistentes y agentes con la plataforma GitHub: repositorios, issues, pull requests, Actions y seguridad.

## Por qué destaca

Oficial y mantenido por GitHub, con un servidor remoto listo para usar.

## Cómo funciona

Un servidor Go expone herramientas MCP que llaman a la API de GitHub con tu token u OAuth.

## Instalación rápida

Usa el servidor remoto `https://api.githubcopilot.com/mcp/` o `docker run -i ghcr.io/github/github-mcp-server` con tu token.

## Casos de uso

- Triage de issues con un agente
- Revisar PRs automáticamente
- Consultar el estado de Actions

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente trabaja con GitHub | usas otra forja como GitLab |

## Stack y modelos

- **Stack:** Go, Docker
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `mcp` `code` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Enlaces

- 🐙 GitHub: [github/github-mcp-server](https://github.com/github/github-mcp-server)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
