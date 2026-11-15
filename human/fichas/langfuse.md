[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Observabilidad, evaluación y guardrails

# 📡 langfuse

> Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 37.3k | Otra (ver repo) | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Resuelve la opacidad: ves qué prompt, qué modelo, qué coste y qué salida tuvo cada paso de tu pipeline.

## Por qué destaca

Es una de las plataformas de LLM observability de referencia, con self-host y cloud e integraciones con los frameworks más usados (LangChain, OpenAI SDK, LiteLLM, CrewAI). Su soporte de OpenTelemetry la hace compatible con instrumentación existente.

## Cómo funciona

Instrumentas tu app con sus SDKs (o vía OpenTelemetry) para enviar trazas, costos y evaluaciones a un backend con UI de análisis, permitiendo seguir el árbol completo de una petición de agente paso a paso.

## Instalación rápida

Docker Compose para self-host (Postgres + backend + frontend) o cuenta cloud; SDKs vía `pip`/`npm`. El self-host requiere mantener PostgreSQL.

## Casos de uso

- Ver el detalle de cada llamada/agente
- Evaluar prompts y medir costos
- Depurar flujos multi-paso de agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| operas agentes en serio y necesitas trazas/costes/eval | haces prototipos triviales o no quieres operar el backend |

## Stack y modelos

- **Stack:** TypeScript, Docker, PostgreSQL, self-host/cloud
- **Modelos / API:** SDKs para múltiples frameworks; agnóstico respecto al LLM.
- **Etiquetas:** `automation` `observability` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [ag2](ag2.md) | 5.1k | Framework maduro para sistemas multiagente con patrones de colaboración (heredero directo de AutoGen). |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Phoenix](phoenix.md) | 12.2k | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. |
| [Opik](opik.md) | 23.3k | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. |
| [MLflow](mlflow.md) | 28.7k | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. |

## Enlaces

- 🐙 GitHub: [langfuse/langfuse](https://github.com/langfuse/langfuse)
- 🌐 Web: <https://langfuse.com>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
