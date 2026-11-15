[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Observabilidad, evaluación y guardrails

# 📡 Opik

> Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 23.3k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Traza llamadas, ejecuta evaluaciones automáticas y monitorea producción con paneles. Incluye optimizador de prompts.

## Por qué destaca

Completa y open source, con buen rendimiento en volúmenes grandes.

## Cómo funciona

SDKs envían trazas a un backend con ClickHouse; la UI muestra trazas, métricas y experimentos.

## Instalación rápida

Clona el repo y ejecuta `./opik.sh` (Docker), o usa su cloud; `pip install opik`.

## Casos de uso

- Monitorear un agente en producción
- Evaluar con LLM juez
- Optimizar prompts

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres observabilidad y evaluación en un solo producto abierto | prefieres la opción más extendida; mira `langfuse` |

## Stack y modelos

- **Stack:** Python, Java, TypeScript, ClickHouse
- **Modelos / API:** Agnóstico.
- **Etiquetas:** `observability` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [Phoenix](phoenix.md) | 12.2k | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. |

## Enlaces

- 🐙 GitHub: [comet-ml/opik](https://github.com/comet-ml/opik)
- 🌐 Web: <https://www.comet.com/docs/opik/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
