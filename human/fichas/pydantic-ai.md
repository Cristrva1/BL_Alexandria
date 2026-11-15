[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 Pydantic AI

> Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 21.1k | MIT | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Construye agentes con salidas validadas, herramientas tipadas e inyección de dependencias, al estilo FastAPI. Incluye evaluación y observabilidad con Logfire.

## Por qué destaca

Ergonomía muy pythónica y validación estricta de salidas, de los autores de Pydantic.

## Cómo funciona

Define agentes con modelos Pydantic para entradas y salidas; el runtime valida cada respuesta y reintenta si no cumple.

## Instalación rápida

`pip install pydantic-ai`.

## Casos de uso

- Extraer datos estructurados fiables
- Agentes en backends FastAPI
- Herramientas tipadas para LLM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres agentes tipados y validados en Python | necesitas grafos complejos con persistencia; mira `langgraph` |

## Stack y modelos

- **Stack:** Python, Pydantic
- **Modelos / API:** Agnóstico: OpenAI, Anthropic, Gemini, Ollama y más.
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [FastMCP](fastmcp.md) | 28.4k | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenAI Agents SDK](openai-agents-python.md) | 30.6k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |
| [smolagents](smolagents.md) | 30.3k | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. |
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |

## Enlaces

- 🐙 GitHub: [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- 🌐 Web: <https://pydantic.dev/pydantic-ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
