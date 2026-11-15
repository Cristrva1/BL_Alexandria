[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Observabilidad, evaluación y guardrails

# 📡 DeepEval

> Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 19.4k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Escribe pruebas para tus apps de LLM con métricas como fidelidad, relevancia o alucinación, e intégralas en tu CI.

## Por qué destaca

Experiencia tipo pytest muy familiar y muchas métricas de investigación.

## Cómo funciona

Cada métrica usa un LLM juez o reglas para puntuar casos de prueba que defines en Python.

## Instalación rápida

`pip install -U deepeval`.

## Casos de uso

- Pruebas unitarias de un RAG
- Detectar alucinaciones
- Evaluar agentes en CI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres tests de LLM en Python como pytest | prefieres configurar en YAML y comparar modelos; mira `promptfoo` |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** OpenAI por defecto; otros jueces configurables.
- **Etiquetas:** `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ragas](ragas.md) | 16.3k | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. |
| [promptfoo](promptfoo.md) | 27k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. |

## Enlaces

- 🐙 GitHub: [confident-ai/deepeval](https://github.com/confident-ai/deepeval)
- 🌐 Web: <https://deepeval.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
