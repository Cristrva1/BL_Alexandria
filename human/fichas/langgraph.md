[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 LangGraph

> Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 45k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## ¿Qué es?

Framework de orquestación de bajo nivel (MIT) de LangChain Inc. para construir, gestionar y desplegar agentes con estado y de larga duración. Es maduro y muy activo (1.2.22), y lo usan en producción empresas como Klarna, Replit o Elastic, según el README.

## ¿Qué hace?

Modela agentes y flujos como grafos con estado y ofrece ejecución duradera (los agentes sobreviven a fallos y retoman donde se quedaron), human-in-the-loop (inspeccionar y modificar el estado en cualquier punto) y memoria a corto y largo plazo. No impone prompts ni arquitectura. Para empezar más rápido, el propio README remite a Deep Agents, construido encima.

## ¿Cómo lo hace?

Biblioteca Python (`pip install -U langgraph`), con equivalente en JS/TS (LangGraph.js). Funciona sola o con componentes de LangChain. Para depuración, evaluación y despliegue se integra con LangSmith y LangSmith Deployment, servicios comerciales de la misma empresa.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langchain](langchain.md) | Componentes de modelos, herramientas e integraciones que se usan dentro de los nodos del grafo. | Instala langgraph y añade solo los paquetes de integración de LangChain que necesites. |
| [Deep Agents](deepagents.md) | Harness de alto nivel construido sobre LangGraph. | Empieza con deepagents si no necesitas controlar el grafo a bajo nivel. |
| [langfuse](langfuse.md) | Trazas y evaluación de código abierto mediante la integración oficial de Langfuse con LangChain/LangGraph. | Langfuse (cloud o autoalojado) primero; añade su callback handler a las ejecuciones. |
| [mem0](mem0.md) | Memoria a largo plazo para agentes de LangGraph (integración documentada por Mem0). | Configura Mem0 y úsalo desde un nodo o herramienta. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (25). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[12-Factor Agents](12-factor-agents.md) · [500-AI-Agents-Projects](500-ai-agents-projects.md) · [Agent Protocol](agent-protocol.md) · [agentic-rag-for-dummies](agentic-rag-for-dummies.md) · [Agents Towards Production](agents-towards-production.md) · [assistant-ui](assistant-ui.md) · [AutoHedge](autohedge.md) · [awesome-LangGraph](awesome-langgraph.md) · [Composio](composio.md) · [CopilotKit](copilotkit.md) · [deer-flow](deer-flow.md) · [Graphiti](graphiti.md) · [Hugging Face Agents Course](agents-course.md) · [LangGraph.js](langgraphjs.md) · [laya](laya.md) · [novu](novu.md) · [Open SWE](open-swe.md) · [OpenBot](openbot.md) · [OpenUI](openui.md) · [Opik](opik.md) · [Phoenix](phoenix.md) · [python-telegram-bot](python-telegram-bot.md) · [QuantHarness](quantharness.md) · [Temporal](temporal.md) · [TradingAgents](tradingagents.md)

**Notas:** Alternativas (elige una): crewai, openai-agents-python, pydantic-ai, adk-python, agno.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 1.2.22 (2026-11-14) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langchain-ai/langgraph/blob/main/README.md) · [2](https://langfuse.com/integrations/frameworks/langchain) · [3](https://docs.mem0.ai/integrations/langgraph)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El grafo admite funciones sin LLM; los modelos, LangSmith y el alojamiento pueden costar aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Ollama se configura mediante la integración LangChain; no es un plugin del editor |
| Coste | El coste depende del proveedor o la ruta. El grafo admite funciones sin LLM; los modelos, LangSmith y el alojamiento pueden costar aparte |
| Equipo | Preparación según la ruta elegida. Python y entorno virtual; modelo solo para nodos LLM |

Ollama se configura mediante la integración LangChain; no es un plugin del editor

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y entorno virtual
- modelo solo para nodos LLM

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install -U langgraph
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/langgraph/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LangGraph para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/langgraph/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un grafo que guarda un pedido y se detiene para revisión humana.

**Qué comprobar:** Puedes inspeccionar el estado y reanudar el pedido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Pausar una devolución hasta su revisión
- Retomar una investigación interrumpida

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Pausar una devolución hasta su revisión; Retomar una investigación interrumpida | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ollama se configura mediante la integración LangChain; no es un plugin del editor

## Stack y modelos

- **Stack:** Python y entorno virtual; modelo solo para nodos LLM
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [crewAI](crewai.md) | 60.9k | Framework para orquestar "crews" de agentes con roles y tareas. |
| [OpenAI Agents SDK](openai-agents-python.md) | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |
| [Pydantic AI](pydantic-ai.md) | 21.2k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. |
| [Agent Development Kit (ADK)](adk-python.md) | 22.2k | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. |
| [Agno](agno.md) | 43.2k | Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. |

## Enlaces

- 🐙 GitHub: [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- 🌐 Web: <https://docs.langchain.com/oss/python/langgraph/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/langgraph/blob/main/README.md)
- [Fuente 2](https://docs.langchain.com/oss/python/integrations/chat/ollama)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
