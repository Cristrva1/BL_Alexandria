[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Observabilidad, evaluación y guardrails

# 📡 promptfoo

> CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 27k | MIT | TypeScript | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Defines casos de prueba en YAML y comparas salidas de varios modelos con aserciones. También escanea vulnerabilidades como inyección de prompts.

## Por qué destaca

Muy práctico para CI: evaluación y red teaming en una sola herramienta.

## Cómo funciona

Ejecuta la matriz de prompts por modelos y casos, evalúa con reglas o con un LLM juez y muestra resultados en una web local.

## Instalación rápida

`npx promptfoo@latest init`.

## Casos de uso

- Comparar GPT, Claude y Gemini en tu caso
- Pruebas de regresión de prompts en CI
- Red teaming de un chatbot

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres pruebas automáticas de prompts y seguridad | necesitas observabilidad en producción; mira `langfuse` |

## Stack y modelos

- **Stack:** TypeScript, Node.js
- **Modelos / API:** Agnóstico.
- **Etiquetas:** `evaluation` `security` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepEval](deepeval.md) | 19.4k | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. |
| [Ragas](ragas.md) | 16.3k | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. |
| [DSPy](dspy.md) | 39k | Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. |

## Enlaces

- 🐙 GitHub: [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
- 🌐 Web: <https://promptfoo.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
