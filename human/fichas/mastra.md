[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks en TypeScript y multi-lenguaje

# 🟦 Mastra

> Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.5k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework en TypeScript para aplicaciones y agentes de IA, de Mastra. Doble licencia: Apache 2.0 para el núcleo y Mastra Enterprise License (código visible pero no libre) en los directorios `ee/`; GitHub lo marca NOASSERTION. Muy activo (@mastra/core 1.83.0).

## ¿Qué hace?

Ofrece enrutamiento de modelos a más de 40 proveedores, agentes autónomos con herramientas, un motor de flujos basado en grafos, human-in-the-loop con suspensión y reanudación, gestión de contexto (historial, memoria de trabajo y semántica, RAG), autoría de servidores MCP, evals y observabilidad integradas.

## ¿Cómo lo hace?

Node/TypeScript. Se crea con `npm create mastra@latest` y se integra en apps React, Next.js o Node o como endpoints independientes. Mastra Studio (`localhost:4111`) sirve para construir y probar agentes y flujos. Para interfaces se integra con AI SDK UI de Vercel y CopilotKit.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [CopilotKit](copilotkit.md) | Interfaz de asistente en la web (integración documentada por CopilotKit y citada en el README). | Crea el backend Mastra y conecta CopilotKit en el frontend. |
| [langfuse](langfuse.md) | Trazas con la integración oficial de Langfuse para Mastra. | Configura el exportador en la observabilidad de Mastra. |
| [Ollama](ollama.md) | Modelos locales a través del enrutamiento de proveedores (combinación por arquitectura) [DATO NO VERIFICADO: proveedor exacto]. | Ollama primero. |
| [Composio](composio.md) | Combinación recíproca: Composio lo enlaza como «Adaptador de proveedor». | Orden indicado desde Composio: Instala el adaptador de Mastra. |
| [OpenBot](openbot.md) | Combinación recíproca: OpenBot lo enlaza como «Incluye un agente de ejemplo de Mastra (`agent-mastra`) conectable por AG-UI». | Orden indicado desde OpenBot: Arranca OpenBot y conecta el agente Mastra. |

**Notas:** Alternativas (elige una): langgraphjs, vercel-ai. Las funciones de `ee/` requieren licencia comercial para producción.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada @mastra/core@1.83.0 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mastra-ai/mastra/blob/main/README.md) · [2](https://docs.copilotkit.ai/mastra) · [3](https://langfuse.com/integrations/frameworks/mastra) · [4](https://mastra.ai/docs/observability/overview)</sub>

## Ver similares

Grupo **Frameworks de agentes en TypeScript**: Mastra ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [AI SDK (Vercel)](vercel-ai.md) ⭐ recomendado | 67 | Si buscas esto: toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. |
| 2 | **Mastra** (esta ficha) | 65 | Si buscas esto: framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. |
| 3 | [LangGraph.js](langgraphjs.md) | 60 | Si buscas esto: versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El framework base es Apache-2.0; nube, modelos y partes con otra licencia tienen condiciones separadas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. No copies el bloque de prompt del README como comando de terminal; el instalador es npm create mastra |
| Coste | El coste depende del proveedor o la ruta. El framework base es Apache-2.0; nube, modelos y partes con otra licencia tienen condiciones separadas |
| Equipo | Preparación según la ruta elegida. Node.js y npm; proveedor elegido |

No copies el bloque de prompt del README como comando de terminal; el instalador es npm create mastra

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js y npm
- proveedor elegido

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
npm create mastra@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mastra-ai/mastra/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Mastra para mi objetivo y necesito pasos guiados. Lee https://github.com/mastra-ai/mastra/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un proyecto y añade una herramienta que devuelva el precio de un producto ficticio.

**Qué comprobar:** Puedes probar el agente y ver la herramienta usada en sus trazas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir un agente a una app TypeScript
- Pausar y reanudar un flujo de aprobación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir un agente a una app TypeScript; Pausar y reanudar un flujo de aprobación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No copies el bloque de prompt del README como comando de terminal; el instalador es npm create mastra

## Stack y modelos

- **Stack:** Node.js y npm; proveedor elegido
- **Etiquetas:** `agents` `rag` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph.js](langgraphjs.md) | 3.4k | Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. |
| [AI SDK (Vercel)](vercel-ai.md) | 28k | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. |

## Enlaces

- 🐙 GitHub: [mastra-ai/mastra](https://github.com/mastra-ai/mastra)
- 🌐 Web: <https://mastra.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mastra-ai/mastra/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
