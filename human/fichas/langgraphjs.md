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
| API de IA | API de IA opcional. El grafo no necesita necesariamente un modelo; los nodos LLM, alojamiento y observabilidad pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Ollama está documentado mediante @langchain/ollama; revisa que el modelo soporte las herramientas necesarias |
| Coste | El coste depende del proveedor o la ruta. El grafo no necesita necesariamente un modelo; los nodos LLM, alojamiento y observabilidad pueden costar |
| Equipo | Preparación según la ruta elegida. Node.js; TypeScript; modelo solo para nodos LLM |

Ollama está documentado mediante @langchain/ollama; revisa que el modelo soporte las herramientas necesarias

## Qué puedes hacer con él

Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador.

## Por qué destaca

Usos propuestos: Controlar aprobación de una solicitud; Reanudar un agente en una app JavaScript.

## Cómo funciona

Ollama está documentado mediante @langchain/ollama; revisa que el modelo soporte las herramientas necesarias

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- TypeScript
- modelo solo para nodos LLM

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install @langchain/langgraph @langchain/core
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/langgraphjs/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LangGraph.js para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/langgraphjs/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Monta un grafo que clasifica una solicitud y espera revisión antes de continuar.

**Qué comprobar:** Se conserva el estado y se ve el siguiente paso.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Controlar aprobación de una solicitud
- Reanudar un agente en una app JavaScript

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Controlar aprobación de una solicitud; Reanudar un agente en una app JavaScript | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ollama está documentado mediante @langchain/ollama; revisa que el modelo soporte las herramientas necesarias

## Stack y modelos

- **Stack:** Node.js; TypeScript; modelo solo para nodos LLM
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/langgraphjs/blob/main/README.md)
- [Fuente 2](https://docs.langchain.com/oss/javascript/integrations/chat/ollama)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
