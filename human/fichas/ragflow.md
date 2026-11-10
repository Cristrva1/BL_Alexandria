[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 RAGFlow

> Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 94k | Apache-2.0 | Go | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Procesa PDFs, tablas e imágenes con parsing visual, crea bases de conocimiento con citas trazables y añade agentes y workflows.

## Por qué destaca

Su parsing de documentos complejos es de los mejores en RAG open source.

## Cómo funciona

Un parser de layout (DeepDoc) divide documentos en fragmentos con estructura; búsqueda híbrida y reranking alimentan al LLM.

## Instalación rápida

`git clone https://github.com/infiniflow/ragflow && cd ragflow/docker && docker compose up -d`.

## Casos de uso

- Base de conocimiento con citas
- RAG sobre contratos y reportes
- Asistente interno con documentos complejos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tus documentos son complejos y necesitas citas fiables | quieres algo ligero en un portátil; mira `anything-llm` |

**Limitaciones:** Consume bastantes recursos (16 GB de RAM recomendados).

## Stack y modelos

- **Stack:** Go, Python, React, Elasticsearch, Docker
- **Modelos / API:** Agnóstico, incluidos modelos locales.
- **Etiquetas:** `rag` `docs` `agents` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Docling](docling.md) | 70.4k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |
| [LightRAG](lightrag.md) | 40.6k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. |

## Enlaces

- 🐙 GitHub: [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- 🌐 Web: <https://ragflow.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
