[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 LightRAG

> RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 40.6k | MIT | Python | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Construye un grafo de entidades a partir de tus documentos y consulta en modo local, global o híbrido. Más barato que GraphRAG.

## Por qué destaca

Calidad de RAG con grafo a menor coste y con actualizaciones incrementales.

## Cómo funciona

Extrae entidades y relaciones con un LLM, las indexa en grafo y vectores, y recupera por ambos caminos.

## Instalación rápida

`pip install lightrag-hku` (incluye servidor con UI: `lightrag-server`).

## Casos de uso

- RAG sobre documentación técnica
- Preguntas que cruzan varios documentos
- Alternativa barata a GraphRAG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres RAG con grafo sin el coste de GraphRAG | no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index` |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** Agnóstico, incluido Ollama.
- **Etiquetas:** `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Qdrant](qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [RAGFlow](ragflow.md) | 94k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |
| [PageIndex](pageindex.md) | 40.3k | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. |

## Enlaces

- 🐙 GitHub: [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)
- 🌐 Web: <https://arxiv.org/abs/2410.05779>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
