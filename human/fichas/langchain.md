[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🦜 langchain

> Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas).

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 149k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.

## Por qué destaca

Estándar de facto del ecosistema LLM, con la comunidad e integraciones más grandes del sector. Su valor está en future-proofing: cambiar de modelo o vector store suele ser mover un parámetro, no reescribir código.

## Cómo funciona

Encadena componentes (prompts, modelos, retrievers, tools) en pipelines o agentes; disponible en Python y JS/TS, con LangGraph para grafos cíclicos con estado.

## Instalación rápida

`pip install langchain` o `npm install langchain`. Requiere la clave del proveedor de LLM que vayas a usar (OpenAI, Anthropic, etc.).

## Casos de uso

- Orquestar LLM + herramientas + memoria
- Base de casi cualquier app de IA
- RAG sobre documentos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres la base estándar con máximas integraciones | prefieres mínima abstracción o un solo proveedor sin cambiar |

## Stack y modelos

- **Stack:** Python/JS/TS
- **Modelos / API:** Prácticamente todos (OpenAI, Anthropic, Google, locales vía Ollama).
- **Etiquetas:** `agents` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [Haystack](haystack.md) | 27k | Framework de deepset para pipelines de RAG y agentes listos para producción. |
| [Semantic Kernel](semantic-kernel.md) | 28.8k | SDK de Microsoft para integrar LLM en apps de C#, Python y Java con plugins y planificación. |

## Enlaces

- 🐙 GitHub: [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- 🌐 Web: <https://docs.langchain.com/langchain/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
