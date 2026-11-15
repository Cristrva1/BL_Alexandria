[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ Agent Protocol

> Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 697 | MIT | Python | 2026-11-05 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## Qué es

Define cómo se ejecuta un agente, cómo recibe entradas y cómo guarda su estado, sin atarse a un framework. Es una especificación, no un runtime.

## Por qué destaca

Facilita que clientes y herramientas hablen con agentes distintos por la misma API.

## Cómo funciona

Un documento OpenAPI describe endpoints de runs, threads y store que cualquier servidor de agentes puede implementar.

## Instalación rápida

No se instala: lee la especificación OpenAPI e impleméntala en tu servidor.

## Casos de uso

- Estandarizar la API de tus agentes
- Conectar una UI genérica a varios agentes
- Diseñar plataformas de agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| diseñas una plataforma que sirve agentes de distintos frameworks | solo necesitas construir un agente |

## Stack y modelos

- **Stack:** OpenAPI, Python
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |

## Enlaces

- 🐙 GitHub: [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)
- 🌐 Web: <https://langchain-ai.github.io/agent-protocol/api.html>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
