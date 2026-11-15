[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 💾 agentmemory

> Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 30.3k | Apache-2.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Resuelve el "re-explica todo" al cambiar de asistente: la memoria vive fuera del cliente.

## Por qué destaca

Evita re-explicar el contexto al cambiar de asistente, ofreciendo una memoria compartida poco común entre herramientas de coding. Su exposición vía MCP la hace compatible con cualquier cliente que hable el protocolo, no solo uno concreto.

## Cómo funciona

Se conecta vía MCP para que distintos clientes lean y escriban en el mismo almacén persistente del motor iii, manteniendo el contexto de proyecto/sesión al margen del IDE que uses en cada momento.

## Instalación rápida

Instalación del servidor MCP según el repo y configuración en cada cliente compatible (Claude Code, Cursor, etc.); requiere el motor iii como backend.

## Casos de uso

- Que el agente "recuerde todo" y no re-expliques el contexto
- Memoria multi-cliente vía MCP
- Continuidad de proyecto entre Claude Code y Cursor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| cambias de asistente y quieres una memoria común entre ellos | te basta la memoria nativa de un único cliente o no usas MCP |

## Stack y modelos

- **Stack:** motor iii, MCP
- **Modelos / API:** Cualquier cliente MCP; sin LLM propio.
- **Etiquetas:** `agents` `memory` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [ruflo](ruflo.md) | 81.4k | Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Engram](engram.md) | 7.9k | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. |
| [supermemory](supermemory.md) | 31.6k | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. |
| [claude-mem](claude-mem.md) | 116k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. |

## Enlaces

- 🐙 GitHub: [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)
- 🌐 Web: <https://www.agent-memory.dev/docs>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
