[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Observabilidad, evaluación y guardrails

# 📡 Ragas

> Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 16.3k | Apache-2.0 | Python | 2026-02-24 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Mide fidelidad, relevancia del contexto y calidad de respuestas, y genera conjuntos de prueba a partir de tus documentos.

## Por qué destaca

Referencia en métricas de RAG y generación de tests sintéticos.

## Cómo funciona

Usa un LLM juez y embeddings para calcular métricas sobre preguntas, contextos y respuestas.

## Instalación rápida

`pip install ragas`.

## Casos de uso

- Medir calidad de un RAG
- Generar preguntas de prueba
- Comparar configuraciones de recuperación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| evalúas un sistema RAG | necesitas red teaming de seguridad; mira `promptfoo` |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** OpenAI por defecto; otros vía LangChain.
- **Etiquetas:** `evaluation` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepEval](deepeval.md) | 19.4k | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. |
| [promptfoo](promptfoo.md) | 27k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. |

## Enlaces

- 🐙 GitHub: [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas)
- 🌐 Web: <https://docs.ragas.io>
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
