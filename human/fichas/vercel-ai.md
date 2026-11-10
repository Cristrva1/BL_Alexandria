[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks en TypeScript y multi-lenguaje

# 🟦 AI SDK (Vercel)

> Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 27.9k | Otra (ver repo) | TypeScript | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Unifica la llamada a decenas de proveedores con una API común y trae hooks de React para chat con streaming. Es la base de muchos frameworks de agentes en TS.

## Por qué destaca

API de proveedores unificada y hooks de UI muy usados; mantenida por Vercel.

## Cómo funciona

Funciones como generateText y streamText llaman al proveedor elegido; los hooks useChat conectan el streaming con la UI.

## Instalación rápida

`npm i ai` más el proveedor, p. ej. `npm i @ai-sdk/openai`.

## Casos de uso

- Chat con streaming en Next.js
- Llamadas a herramientas tipadas
- Cambiar de proveedor sin reescribir

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes una app web con IA en TypeScript | necesitas agentes complejos con memoria y workflows; mira `mastra` |

## Stack y modelos

- **Stack:** TypeScript, React, Next.js
- **Modelos / API:** Agnóstico: OpenAI, Anthropic, Google, Ollama y más.
- **Etiquetas:** `agents` `ui` `typescript` `react`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ui](ui.md) | 128k | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. |
| [assistant-ui](assistant-ui.md) | 13k | Librería React y TypeScript para interfaces de chat con IA de calidad producción. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph.js](langgraphjs.md) | 3.4k | Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. |
| [Mastra](mastra.md) | 29.4k | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. |

## Enlaces

- 🐙 GitHub: [vercel/ai](https://github.com/vercel/ai)
- 🌐 Web: <https://ai-sdk.dev>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
