[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Faiss

> Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 41.3k | MIT | C++ | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Base de muchas bases vectoriales; ideal para investigación o cuando quieres índices en memoria sin servidor.

## Por qué destaca

Rendimiento de referencia y gran variedad de índices, también en GPU.

## Cómo funciona

Implementa índices exactos y aproximados (IVF, HNSW, PQ) en C++ con bindings de Python.

## Instalación rápida

`pip install faiss-cpu` (o `faiss-gpu`).

## Casos de uso

- Búsqueda de vecinos en memoria
- Experimentos de recuperación
- Deduplicar imágenes por embeddings

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas índices vectoriales en memoria y máximo control | quieres persistencia y API listas; mira `qdrant` |

## Stack y modelos

- **Stack:** C++, Python, CUDA
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `vector-db` `python` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Transformers](transformers.md) | 169k | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |

## Enlaces

- 🐙 GitHub: [facebookresearch/faiss](https://github.com/facebookresearch/faiss)
- 🌐 Web: <https://faiss.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
