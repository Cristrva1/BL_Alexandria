[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 Agno

> Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 43.2k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de agentes «autogestionada» (Apache 2.0) de Agno. Muy activa (v3.2.0).

## ¿Qué hace?

Permite crear agentes con los SDK de Agno, Claude Agent o Codex, combinarlos en equipos y flujos, y ejecutarlos como servicios duraderos en AgentOS: autenticación, roles, reanudación y repetición, aprobaciones humanas, programación y ejecución duradera. Company OS asigna responsabilidades, proyectos y rutinas a agentes. Los agentes se exponen por API REST, como servidor MCP (Claude, ChatGPT) o en Slack.

## ¿Cómo lo hace?

Python. Usa PostgreSQL para conversaciones, memoria y actividad, y ofrece plantillas para desplegar en tu nube (Docker, Railway…). El README propone arrancar dando una plantilla a un agente de código. La interfaz AgentOS UI (os.agno.com) inspecciona trazas y conocimiento.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [claude-agent-sdk-python](claude-agent-sdk-python.md) | SDK soportado para construir agentes que AgentOS sirve. | Instala Agno y el SDK de Claude Agent en el mismo entorno. |
| [Qdrant](qdrant.md) | Almacén vectorial para la base de conocimiento (documentado por Agno). | Qdrant primero; configúralo en el knowledge del agente. |
| [mem0](mem0.md) | Memoria externa con integración documentada por Mem0. | Opcional: Agno ya trae memoria propia sobre PostgreSQL. |
| [500-AI-Agents-Projects](500-ai-agents-projects.md) | Combinación recíproca: 500-AI-Agents-Projects lo enlaza como «Framework usado en muchos de los agentes listados». | Orden indicado desde 500-AI-Agents-Projects: Instálalo según el requirements del ejemplo. |

**Notas:** Alternativas (elige una): crewai, langgraph. AgentOS UI es un servicio alojado por Agno: revisa qué datos ve.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.2.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/agno-agi/agno/blob/main/README.md) · [2](https://docs.agno.com/knowledge/vector-stores/qdrant/overview) · [3](https://docs.mem0.ai/integrations/agno)</sub>

## Ver similares

Grupo **Frameworks de agentes en Python**: Agno ocupa la posición 7 de 8 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [LangGraph](langgraph.md) ⭐ recomendado | 72 | Si necesitas flujos con estado, ciclos, checkpoints y control fino del grafo en producción. |
| 2 | [crewAI](crewai.md) | 72 | Si piensas en equipos de agentes con roles y tareas y quieres arrancar rápido. |
| 3 | [Deep Agents](deepagents.md) | 70 | Si quieres agentes de largo recorrido con planificación, subagentes y sistema de archivos sobre LangGraph. |
| 4 | [OpenAI Agents SDK](openai-agents-python.md) | 67 | Si usas la API de OpenAI y quieres handoffs, guardrails y trazas oficiales. |
| 5 | [Pydantic AI](pydantic-ai.md) | 66 | Si quieres salidas tipadas y validadas con Pydantic y un estilo cercano a FastAPI. |
| 6 | [Agent Development Kit (ADK)](adk-python.md) | 65 | Si despliegas en Google Cloud/Vertex o usas Gemini y quieres el kit oficial de Google. |
| 7 | **Agno** (esta ficha) | 61 | Si quieres un runtime de agentes con memoria, conocimiento y equipos listo para servir por API. |
| 8 | [smolagents](smolagents.md) | 55 | Si quieres agentes mínimos que escriben código Python como acciones, de Hugging Face. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El MCP de documentación no requiere autenticación; plataforma, nube y modelos pueden costar; los ingenieros Claude/Codex usan claves API |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. MCP HTTP accesible desde los tres clientes; no significa que sus planes paguen los agentes desplegados |
| Coste | El coste depende del proveedor o la ruta. El MCP de documentación no requiere autenticación; plataforma, nube y modelos pueden costar; los ingenieros Claude/Codex usan claves API |
| Equipo | Preparación según la ruta elegida. Python; plantilla; PostgreSQL; proveedor de modelos |

MCP HTTP accesible desde los tres clientes; no significa que sus planes paguen los agentes desplegados

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- plantilla
- PostgreSQL
- proveedor de modelos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.agno.com/agent-platform/overview)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agno para mi objetivo y necesito pasos guiados. Lee https://docs.agno.com/agent-platform/overview. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta el MCP de documentación y pide que explique el montaje de la plataforma local.

**Qué comprobar:** El agente consulta la guía y enumera servicios y credenciales necesarios.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Servir un agente mediante una API
- Investigar fallos mediante trazas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Servir un agente mediante una API; Investigar fallos mediante trazas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP HTTP accesible desde los tres clientes; no significa que sus planes paguen los agentes desplegados

## Stack y modelos

- **Stack:** Python; plantilla; PostgreSQL; proveedor de modelos
- **Etiquetas:** `agents` `memory` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [crewAI](crewai.md) | 60.9k | Framework para orquestar "crews" de agentes con roles y tareas. |
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |

## Enlaces

- 🐙 GitHub: [agno-agi/agno](https://github.com/agno-agi/agno)
- 🌐 Web: <https://docs.agno.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/agno-agi/agno/blob/main/README.md)
- [Fuente 2](https://docs.agno.com/coding-agents)
- [Fuente 3](https://docs.agno.com/agent-platform/coding-agents)
- [Fuente 4](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
