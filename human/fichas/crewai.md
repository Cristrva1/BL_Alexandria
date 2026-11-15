[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 👥 crewAI

> Framework para orquestar "crews" de agentes con roles y tareas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 60.7k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.

## Por qué destaca

Muy popular por su curva de aprendizaje suave; es de las formas más rápidas de montar un equipo de agentes funcional. Es independiente de LangChain y aporta un modelo mental claro (agentes, tareas, crew) que se lee casi como prosa.

## Cómo funciona

Declaras agentes (rol, meta, herramientas) y tareas, y CrewAI orquesta su ejecución secuencial o jerárquica; está escrito en Python y delega el LLM al proveedor que configures.

## Instalación rápida

`pip install crewai` (o `crewai[tools]` para el set de herramientas integradas). Requiere una clave de API de LLM por entorno.

## Casos de uso

- Avanzar rápido en flujos de agentes
- Prototipos colaborativos
- Pipelines de research/redacción repartidos por rol

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres velocidad y un modelo mental simple de "equipo" | necesitas control de bajo nivel o orquestación muy custom |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** OpenAI, Anthropic, Gemini, locales; agnóstico vía variables de entorno.
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [mem0](mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AutoGen](autogen.md) | 61.8k | Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento. |
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [Agno](agno.md) | 43.1k | Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. |

## Enlaces

- 🐙 GitHub: [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- 🌐 Web: <https://crewai.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
