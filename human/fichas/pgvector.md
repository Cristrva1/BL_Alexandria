[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 pgvector

> Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 23.6k | Otra (ver repo) | C | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Guarda embeddings en una columna y búscalos con SQL, con índices HNSW o IVFFlat. Evita añadir otra base de datos.

## Por qué destaca

Usa la base que ya tienes; disponible en casi todos los proveedores de PostgreSQL.

## Cómo funciona

Añade el tipo vector y operadores de distancia a PostgreSQL con índices aproximados.

## Instalación rápida

`CREATE EXTENSION vector;` (incluida en muchos servicios; o `docker run pgvector/pgvector:pg17`).

## Casos de uso

- RAG sin servicio extra
- Búsqueda semántica con filtros SQL
- Recomendaciones en una app existente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ya usas PostgreSQL y quieres vectores | tienes volúmenes muy grandes; mira `milvus` |

## Stack y modelos

- **Stack:** C, PostgreSQL
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `vector-db` `postgres` `rag`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |

## Enlaces

- 🐙 GitHub: [pgvector/pgvector](https://github.com/pgvector/pgvector)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
