[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🌊 Flowise

> Builder visual drag-and-drop para pipelines LLM.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 55.6k | Otra (ver repo) | TypeScript | 2026-08-13 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

> ⚠️ Archivado en GitHub: ya no recibe cambios.

## Qué es

Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible.

## Por qué destaca

Muy adoptado para prototipar flujos LLM en minutos sin escribir código. Al estar basado en LangChain.js, hereda sus conectores y se instala con un solo comando de npm.

## Cómo funciona

Cada nodo encapsula un componente (LLM, retriever, tool, memoria); el grafo se ejecuta en un backend Node.js y se sirve por API o widget. Persiste credenciales y conversaciones en SQLite/PostgreSQL.

## Instalación rápida

`npm install -g flowise && npx flowise start` o vía Docker. Requiere Node.js y las claves de los proveedores de LLM que uses.

## Casos de uso

- Prototipar un flujo LLM rápido
- Demos sin código
- Widget de chat embebible en una web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un prototipo visual ya, en stack JS | necesitas plataforma completa con RAG/observabilidad (dify) |

## Stack y modelos

- **Stack:** Node.js/TypeScript, React
- **Modelos / API:** Múltiples; agnóstico vía LangChain.js.
- **Etiquetas:** `automation` `agents` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sim](sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. |
| [AutoGPT](autogpt.md) | 188k | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. |

## Enlaces

- 🐙 GitHub: [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- 🌐 Web: <https://flowiseai.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
