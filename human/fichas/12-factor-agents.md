[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Guías, cursos y cookbooks

# 🎓 12-Factor Agents

> Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12 Factor Apps.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 27.1k | Otra (ver repo) | TypeScript | 2025-09-21 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## Qué es

Ensayo de Dex Horthy (HumanLayer) que resume lo aprendido construyendo agentes para clientes reales: los productos que funcionan son sobre todo software determinista con pasos de LLM bien colocados. Cada factor (controlar tus prompts, tu ventana de contexto y tu flujo de control, pausar y reanudar, contactar a humanos con tool calls, agentes pequeños) tiene su capítulo con diagramas y ejemplos.

## Por qué destaca

Es agnóstico al framework y se ha vuelto una referencia habitual sobre context engineering y diseño de agentes. Ayuda a decidir qué partes conviene programar a mano en vez de dejarlas al bucle del agente.

## Cómo funciona

Es un README con un capítulo en Markdown por factor, diagramas y fragmentos de código, sobre todo en TypeScript; también enlaza la charla del AI Engineer World's Fair.

## Instalación rápida

No se instala: abre el repo y lee los factores en orden (empieza por el factor 3 si te interesa el context engineering).

## Casos de uso

- Revisar la arquitectura de un agente antes de llevarlo a producción
- Decidir cuándo usar un framework y cuándo código propio
- Diseñar pasos con aprobación humana mediante tool calls

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework | buscas tutoriales con código ejecutable paso a paso; mira `agents-towards-production` o `ai-agents-for-beginners` |

**Limitaciones:** Sin cambios desde septiembre de 2025; el contenido es CC BY-SA 4.0 y el código Apache 2.0.

## Stack y modelos

- **Stack:** Markdown, TypeScript (ejemplos)
- **Modelos / API:** No usa LLM: es una guía; los principios aplican a cualquier proveedor.
- **Etiquetas:** `agents` `learning` `prompts` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Context-Engineering](context-engineering.md) | 9.3k | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. |
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [AI SDK (Vercel)](vercel-ai.md) | 27.9k | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. |

## Enlaces

- 🐙 GitHub: [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
