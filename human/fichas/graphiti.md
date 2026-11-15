[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 Graphiti

> Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 32.7k | Apache-2.0 | Python | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Actualiza el grafo con cada nuevo dato sin recalcular todo y guarda cuándo era válido cada hecho. Ideal para memoria de agentes que cambia.

## Por qué destaca

Manejo de tiempo y actualizaciones incrementales que otros grafos no ofrecen.

## Cómo funciona

Extrae entidades y relaciones con un LLM, las fusiona en Neo4j u otra base de grafos y consulta con búsqueda híbrida.

## Instalación rápida

`pip install graphiti-core` (requiere Neo4j o FalkorDB).

## Casos de uso

- Memoria de agentes que evoluciona
- Historial de relaciones con clientes
- Grafos con validez temporal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas memoria que cambie con el tiempo y se pueda consultar | solo quieres RAG sobre documentos estáticos; mira `lightrag` |

## Stack y modelos

- **Stack:** Python, Neo4j
- **Modelos / API:** OpenAI, Anthropic y otros.
- **Etiquetas:** `memory` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-neo4j](mcp-neo4j.md) | 989 | Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [cognee](cognee.md) | 33.2k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |

## Enlaces

- 🐙 GitHub: [getzep/graphiti](https://github.com/getzep/graphiti)
- 🌐 Web: <https://help.getzep.com/graphiti>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
