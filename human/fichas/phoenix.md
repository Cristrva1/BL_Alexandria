[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Observabilidad, evaluación y guardrails

# 📡 Phoenix

> Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 12.2k | Otra (ver repo) | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Qué es

Visualiza trazas de agentes y RAG, ejecuta evaluaciones y gestiona datasets y experimentos. Corre en local o en tu servidor.

## Por qué destaca

Basada en estándares abiertos (OpenTelemetry, OpenInference).

## Cómo funciona

Recibe trazas por OTLP desde instrumentaciones automáticas y las muestra con herramientas de evaluación.

## Instalación rápida

`pip install arize-phoenix` y `phoenix serve`, o `docker run -p 6006:6006 arizephoenix/phoenix`.

## Casos de uso

- Depurar un agente paso a paso
- Evaluar respuestas en lote
- Comparar versiones de prompts

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres observabilidad basada en OpenTelemetry | buscas la plataforma más usada; mira `langfuse` |

**Limitaciones:** Licencia Elastic 2.0.

## Stack y modelos

- **Stack:** Python, TypeScript, OpenTelemetry
- **Modelos / API:** No usa LLM salvo para evaluaciones.
- **Etiquetas:** `observability` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [Opik](opik.md) | 23.3k | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. |

## Enlaces

- 🐙 GitHub: [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)
- 🌐 Web: <https://arize.com/docs/phoenix>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
