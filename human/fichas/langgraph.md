[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 LangGraph

> Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 44.7k | MIT | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Modela agentes y flujos multiagente como grafos de nodos con estado compartido y checkpoints. Pensado para agentes de producción que deben ser controlables y recuperables.

## Por qué destaca

Estándar de facto para agentes controlables en Python, usado en producción por muchas empresas.

## Cómo funciona

Cada nodo lee y escribe un estado tipado; un runtime ejecuta el grafo, guarda checkpoints y permite pausar para aprobación humana.

## Instalación rápida

`pip install -U langgraph`.

## Casos de uso

- Agentes con aprobación humana
- Flujos multiagente con supervisor
- Agentes de larga duración recuperables

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas agentes con estado, control fino y persistencia | quieres algo mínimo para un agente simple; mira `smolagents` |

## Stack y modelos

- **Stack:** Python, LangChain
- **Modelos / API:** Agnóstico: cualquier modelo de LangChain.
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [crewAI](crewai.md) | 60.7k | Framework para orquestar "crews" de agentes con roles y tareas. |
| [OpenAI Agents SDK](openai-agents-python.md) | 30.6k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |
| [Pydantic AI](pydantic-ai.md) | 21.1k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. |
| [LangGraph Supervisor](langgraph-supervisor-py.md) | 1.7k | Librería archivada para crear un agente supervisor que coordina a otros agentes en LangGraph. |
| [Agent Development Kit (ADK)](adk-python.md) | 22.2k | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. |

## Enlaces

- 🐙 GitHub: [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- 🌐 Web: <https://docs.langchain.com/oss/python/langgraph/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
