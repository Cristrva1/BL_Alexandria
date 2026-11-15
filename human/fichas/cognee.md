[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 cognee

> Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 33.2k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Convierte documentos y conversaciones en un grafo de conocimiento consultable para dar memoria de largo plazo a tus agentes.

## Por qué destaca

Une búsqueda semántica y relaciones del grafo con pocas líneas de código.

## Cómo funciona

Su pipeline cognify extrae entidades y relaciones con un LLM y las guarda en un grafo y una base vectorial.

## Instalación rápida

`pip install cognee`.

## Casos de uso

- Memoria de clientes para un agente
- Grafo de conocimiento de documentos
- RAG con relaciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres memoria basada en grafo con poco esfuerzo | necesitas un grafo temporal en tiempo real; mira `graphiti` |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** Agnóstico, incluidos modelos locales.
- **Etiquetas:** `memory` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [mcp-neo4j](mcp-neo4j.md) | 989 | Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Graphiti](graphiti.md) | 32.7k | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. |
| [mem0](mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [Letta](letta.md) | 25.4k | Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). |

## Enlaces

- 🐙 GitHub: [topoteretes/cognee](https://github.com/topoteretes/cognee)
- 🌐 Web: <https://www.cognee.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
