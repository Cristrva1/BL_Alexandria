[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 🔗 graphrag

> Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 36.6k | MIT | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Resuelve las preguntas que requieren conectar entidades dispersas en muchos documentos, donde el RAG clásico falla.

## Por qué destaca

Proyecto de Microsoft Research muy difundido que mejora las respuestas en preguntas que requieren conectar entidades dispersas en muchos documentos. Su enfoque de resumen por comunidades y recuperación local+global es un patrón de referencia en RAG avanzado.

## Cómo funciona

Un LLM extrae entidades y relaciones para construir el grafo, lo resume por comunidades con un LLM y luego responde combinando recuperación local (entidades concretas) y global (temas del corpus) con embeddings.

## Instalación rápida

`pip install graphrag` y luego `graphrag index` / `graphrag query` sobre tu corpus. Requiere claves de un LLM y embeddings; el indexado consume bastantes llamadas.

## Casos de uso

- Preguntas complejas sobre un corpus
- Recuperación que entiende relaciones
- Análisis temático de colecciones grandes de documentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto | un RAG simple basta o el coste de indexado con LLM es prohibitivo |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** Múltiples LLMs + embeddings (OpenAI, Azure, locales); configurable vía settings.yaml.
- **Etiquetas:** `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphify](graphify.md) | 145k | Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos. |
| [mcp-neo4j](mcp-neo4j.md) | 989 | Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud. |
| [turbovec](turbovec.md) | 17.5k | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Graphiti](graphiti.md) | 32.7k | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. |
| [cognee](cognee.md) | 33.2k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |
| [LightRAG](lightrag.md) | 40.6k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. |

## Enlaces

- 🐙 GitHub: [microsoft/graphrag](https://github.com/microsoft/graphrag)
- 🌐 Web: <https://microsoft.github.io/graphrag/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
