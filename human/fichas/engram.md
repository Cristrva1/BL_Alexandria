[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 Engram

> Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 7.9k | MIT | Go | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Da a cualquier agente compatible con MCP una memoria local de decisiones y aprendizajes, sin dependencias pesadas.

## Por qué destaca

Agnóstico de agente, muy ligero y fácil de inspeccionar.

## Cómo funciona

Guarda observaciones en SQLite con búsqueda de texto completo (FTS5) y las expone por MCP, HTTP y CLI.

## Instalación rápida

`brew install gentleman-programming/tap/engram` o binario de releases; luego añádelo como servidor MCP.

## Casos de uso

- Memoria compartida entre Claude Code y Codex
- Registrar decisiones del proyecto
- Buscar soluciones pasadas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres memoria local simple para cualquier agente | solo usas Claude Code y quieres algo automático; mira `claude-mem` |

## Stack y modelos

- **Stack:** Go, SQLite
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `memory` `mcp` `coding-agent` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [OpenCode](opencode.md) | 226k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [claude-mem](claude-mem.md) | 116k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. |
| [agentmemory](agentmemory.md) | 30.3k | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |

## Enlaces

- 🐙 GitHub: [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)
- 🌐 Web: <https://engram.gentlemanprogramming.com/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
