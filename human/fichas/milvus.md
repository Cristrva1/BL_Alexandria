[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Milvus

> Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 46.6k | Apache-2.0 | Go | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Pensada para producción con grandes volúmenes, alta disponibilidad y varios tipos de índices. Tiene una versión ligera para empezar.

## Por qué destaca

Escala horizontal probada en empresas con volúmenes enormes.

## Cómo funciona

Arquitectura distribuida que separa almacenamiento y cómputo, con índices como HNSW, IVF y DiskANN.

## Instalación rápida

`pip install pymilvus` (incluye Milvus Lite) o Docker Compose para el modo standalone.

## Casos de uso

- Búsqueda semántica a gran escala
- Recomendaciones por similitud
- RAG con millones de documentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| esperas volúmenes muy grandes de vectores | tu proyecto es pequeño; mira `chroma` o `qdrant` |

## Stack y modelos

- **Stack:** Go, C++, Kubernetes
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `vector-db` `rag` `go` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |

## Enlaces

- 🐙 GitHub: [milvus-io/milvus](https://github.com/milvus-io/milvus)
- 🌐 Web: <https://milvus.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
