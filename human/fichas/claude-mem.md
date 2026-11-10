[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 claude-mem

> Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 116k | Apache-2.0 | TypeScript | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Registra lo que hace el agente en cada sesión, lo resume y vuelve a inyectar lo relevante al empezar la siguiente. Evita repetir contexto en proyectos largos.

## Por qué destaca

Uno de los plugins más populares de Claude Code; funciona sin configurar nada.

## Cómo funciona

Hooks capturan las acciones de la sesión, un modelo las comprime y una base local con búsqueda las recupera por MCP.

## Instalación rápida

En Claude Code: `/plugin marketplace add thedotmack/claude-mem` y `/plugin install claude-mem`.

## Casos de uso

- Recordar decisiones de un proyecto
- Retomar trabajo sin re-explicar
- Buscar qué hizo el agente antes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas Claude Code a diario y repites contexto entre sesiones | necesitas memoria para una app propia; mira `mem0` |

## Stack y modelos

- **Stack:** TypeScript, SQLite, Chroma
- **Modelos / API:** Claude para resumir; búsqueda local.
- **Etiquetas:** `memory` `coding-agent` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [superpowers](superpowers.md) | 315k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Engram](engram.md) | 7.9k | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. |
| [agentmemory](agentmemory.md) | 30.3k | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |

## Enlaces

- 🐙 GitHub: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- 🌐 Web: <https://claude-mem.ai>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
