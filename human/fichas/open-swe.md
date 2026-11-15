[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 Open SWE

> Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 11.2k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Trabaja en segundo plano a partir de issues o mensajes, planifica, programa en un sandbox y abre PRs. Inspirado en los agentes internos de empresas como Stripe o Ramp.

## Por qué destaca

Base abierta y extensible sobre LangGraph para quien quiere su propio agente de ingeniería.

## Cómo funciona

Un grafo de LangGraph coordina planificador y programador; el código se ejecuta en sandboxes remotos y el resultado llega como PR.

## Instalación rápida

Clona el repo y sigue la guía de despliegue en LangGraph Platform con tus claves.

## Casos de uso

- Agente que resuelve issues y abre PRs
- Bot interno de ingeniería en Slack
- Tareas largas en segundo plano

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres construir el agente de código interno de tu empresa | solo quieres un agente para tu terminal; mira `claude-code` |

## Stack y modelos

- **Stack:** Python, LangGraph, TypeScript
- **Modelos / API:** Anthropic u OpenAI configurables.
- **Etiquetas:** `coding-agent` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [E2B](e2b.md) | 14.8k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenHands](openhands.md) | 93.1k | Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). |
| [SWE-agent](swe-agent.md) | 20.8k | Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo. |

## Enlaces

- 🐙 GitHub: [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe)
- 🌐 Web: <https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
