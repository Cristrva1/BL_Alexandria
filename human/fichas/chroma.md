[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Chroma

> Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 29.7k | Apache-2.0 | Rust | 2026-11-07 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Se usa embebida en tu script Python o como servidor, con embeddings automáticos. Perfecta para prototipos de RAG.

## Por qué destaca

Cero configuración: `pip install` y ya puedes guardar y buscar.

## Cómo funciona

Núcleo en Rust con índices HNSW y metadatos; corre en proceso o como servidor cliente-servidor.

## Instalación rápida

`pip install chromadb`.

## Casos de uso

- Prototipo de RAG en un notebook
- Memoria simple para un agente
- Búsqueda semántica local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| empiezas con RAG y quieres lo más simple | necesitas gran escala y filtros complejos; mira `qdrant` o `milvus` |

## Stack y modelos

- **Stack:** Rust, Python, TypeScript
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `vector-db` `rag` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [pgvector](pgvector.md) | 23.6k | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. |
| [Milvus](milvus.md) | 46.6k | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. |
| [Faiss](faiss.md) | 41.3k | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. |

## Enlaces

- 🐙 GitHub: [chroma-core/chroma](https://github.com/chroma-core/chroma)
- 🌐 Web: <https://www.trychroma.com/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
