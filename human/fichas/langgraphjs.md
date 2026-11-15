[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks en TypeScript y multi-lenguaje

# 🟦 LangGraph.js

> Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.4k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Lleva el modelo de grafos con estado, checkpoints y human-in-the-loop de LangGraph al ecosistema JavaScript.

## Por qué destaca

Paridad casi completa con la versión Python y despliegue en LangGraph Platform.

## Cómo funciona

Nodos que leen y escriben un estado compartido, ejecutados por un runtime con persistencia.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npm install @langchain/langgraph @langchain/core
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/langchain-ai/langgraphjs/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LangGraph.js para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/langgraphjs/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agentes con aprobación humana en Node
- Flujos multiagente en TS
- Agentes desplegados en LangGraph Platform

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el modelo de LangGraph en TypeScript | buscas una experiencia TS más integrada; mira `mastra` |

## Stack y modelos

- **Stack:** TypeScript, Node.js
- **Etiquetas:** `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Mastra](mastra.md) | 29.5k | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. |
| [AI SDK (Vercel)](vercel-ai.md) | 28k | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. |

## Enlaces

- 🐙 GitHub: [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs)
- 🌐 Web: <https://docs.langchain.com/oss/javascript/langgraph/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/langchain-ai/langgraphjs/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
