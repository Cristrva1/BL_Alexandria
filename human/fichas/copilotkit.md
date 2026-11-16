[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 🪄 CopilotKit

> Stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.7k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Stack open source (MIT) para poner agentes de IA frente a usuarios reales en React, de CopilotKit, el equipo creador del protocolo AG-UI. Es muy activo (v1.88.0). Tiene un producto de pago, CopilotKit Intelligence, que añade memoria entre sesiones y aprendizaje continuo.

## ¿Qué hace?

Conecta un agente ya construido en cualquier framework con una interfaz de chat, UI generativa, estado compartido entre agente y app, y human-in-the-loop. Soporta AG-UI 1.0, A2UI y MCP Apps. Tiene integraciones documentadas con LangGraph, Mastra, CrewAI, Google ADK, AG2, Agno, LlamaIndex, Strands y Microsoft Agent Framework, entre otros.

## ¿Cómo lo hace?

Paquetes npm (`@copilotkit/react-core`, `@copilotkit/runtime`), un asistente de onboarding que puede ejecutar un agente de programación (`npx copilotkit@latest onboard start`) y plantillas (`npx copilotkit@latest create`). El runtime se despliega en tu backend y la UI va en React.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Backend de agente con integración oficial documentada. | Despliega el grafo y conecta CopilotKit a su endpoint. |
| [Mastra](mastra.md) | Agentes TypeScript con integración oficial documentada. | Configura Mastra y registra el agente en el runtime de CopilotKit. |
| [Microsoft Agent Framework](agent-framework.md) | Agentes de Microsoft Agent Framework con integración documentada. | Expón el agente y conéctalo vía AG-UI. |
| [crewAI](crewai.md) | Equipos de agentes CrewAI con integración documentada. | Despliega el crew y conéctalo al runtime. |
| [OpenBot](openbot.md) | OpenBot, la plataforma de compañeros de IA de CopilotKit, está construida sobre CopilotKit y AG-UI. | Parte de OpenBot si quieres un espacio de trabajo completo en vez de componentes sueltos. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[claude-quickstarts](claude-quickstarts.md) · [LangGraph.js](langgraphjs.md) · [OpenDots](opendots.md) · [OpenUI](openui.md)

**Notas:** Alternativas (elige una): assistant-ui.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.88.0 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CopilotKit/CopilotKit/blob/main/README.md) · [2](https://docs.copilotkit.ai/agentic-protocols/ag-ui) · [3](https://docs.copilotkit.ai/mastra) · [4](https://docs.copilotkit.ai/langgraph) · [5](https://docs.copilotkit.ai/microsoft-agent-framework) · [6](https://docs.copilotkit.ai/crewai-crews)</sub>

## Ver similares

Grupo **Componentes de chat y copilotos para React**: CopilotKit ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **CopilotKit** (esta ficha) ⭐ recomendado | 70 | Si buscas esto: stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI. |
| 2 | [assistant-ui](assistant-ui.md) | 62 | Si buscas esto: librería React y TypeScript para interfaces de chat con IA de calidad producción. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La interfaz y el protocolo no incluyen inferencia; backend, modelos y servicios gestionados se presupuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El prompt de onboarding ayuda a un agente a instalar; no demuestra que el plan de Claude Code o Codex ejecute el backend del producto |
| Coste | El coste depende del proveedor o la ruta. La interfaz y el protocolo no incluyen inferencia; backend, modelos y servicios gestionados se presupuestan aparte |
| Equipo | Preparación según la ruta elegida. Node; framework compatible; backend de agente; proveedor del modelo |

El prompt de onboarding ayuda a un agente a instalar; no demuestra que el plan de Claude Code o Codex ejecute el backend del producto

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- framework compatible
- backend de agente
- proveedor del modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx copilotkit@latest create
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/CopilotKit/CopilotKit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CopilotKit para mi objetivo y necesito pasos guiados. Lee https://github.com/CopilotKit/CopilotKit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una app de ejemplo y una acción que lea un dato ficticio de la interfaz.

**Qué comprobar:** El agente recibe el contexto y devuelve una acción que puedes revisar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir asistencia contextual a una app
- Mostrar componentes generados a partir de respuestas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir asistencia contextual a una app; Mostrar componentes generados a partir de respuestas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El prompt de onboarding ayuda a un agente a instalar; no demuestra que el plan de Claude Code o Codex ejecute el backend del producto

## Stack y modelos

- **Stack:** Node; framework compatible; backend de agente; proveedor del modelo
- **Etiquetas:** `ui` `agents` `react` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [assistant-ui](assistant-ui.md) | 13.2k | Librería React y TypeScript para interfaces de chat con IA de calidad producción. |

## Enlaces

- 🐙 GitHub: [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)
- 🌐 Web: <https://docs.copilotkit.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CopilotKit/CopilotKit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
