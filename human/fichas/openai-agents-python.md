[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 OpenAI Agents SDK

> SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 30.6k | MIT | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Define agentes con instrucciones y herramientas, pasa el control entre ellos y añade validaciones. Funciona con modelos de OpenAI y otros compatibles.

## Por qué destaca

Pocas abstracciones, buena documentación y trazas listas en el panel de OpenAI.

## Cómo funciona

Un bucle ejecuta al agente, llama herramientas o transfiere a otro agente, y registra cada paso como traza.

## Instalación rápida

`pip install openai-agents`.

## Casos de uso

- Agentes de soporte con traspasos
- Flujos con guardrails de entrada y salida
- Agentes de voz en tiempo real

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas OpenAI y quieres agentes multiagente con poco código | necesitas control de estado avanzado; mira `langgraph` |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** OpenAI por defecto; otros vía LiteLLM.
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [openai-python](openai-python.md) | 32.1k | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. |
| [FastMCP](fastmcp.md) | 28.4k | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pydantic AI](pydantic-ai.md) | 21.1k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. |
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [smolagents](smolagents.md) | 30.3k | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. |
| [Deep Agents](deepagents.md) | 31.2k | Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. |
| [Agent Development Kit (ADK)](adk-python.md) | 22.2k | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. |

## Enlaces

- 🐙 GitHub: [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- 🌐 Web: <https://openai.github.io/openai-agents-python/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
