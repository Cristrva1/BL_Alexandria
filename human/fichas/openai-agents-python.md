[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 OpenAI Agents SDK

> SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.7k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

SDK oficial de OpenAI (MIT) para flujos multiagente, ligero y agnóstico de proveedor. Muy activo (v0.24.0), con versión JS/TS.

## ¿Qué hace?

Ofrece agentes con instrucciones, herramientas, guardrails y handoffs; agentes en sandbox que trabajan en un contenedor durante horizontes largos; agentes de voz y en tiempo real; agentes como herramientas; herramientas de función, MCP y alojadas; sesiones con historial automático, y trazas integradas para ver y depurar ejecuciones. Soporta las API Responses y Chat Completions y más de 100 LLM.

## ¿Cómo lo hace?

Python 3.10+ (`pip install openai-agents`), con extras opcionales para voz (`[voice]`) y sesiones en Redis. Los modelos de otros proveedores se conectan, por ejemplo, mediante LiteLLM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Integración documentada para usar modelos de otros proveedores. | Instala el extra de LiteLLM y configura el modelo. |
| [openai-python](openai-python.md) | Cliente oficial de OpenAI que usa el SDK. | Se instala como dependencia. |
| [langfuse](langfuse.md) | Trazas de código abierto como alternativa al panel de OpenAI (integración oficial). | Instrumenta con el procesador de trazas de Langfuse. |
| [FastMCP](fastmcp.md) | Construir servidores MCP propios que el SDK consume como herramientas (combinación por arquitectura; el SDK documenta MCP). | Servidor MCP primero. |
| [Awesome LLM Apps](awesome-llm-apps.md) | Combinación recíproca: Awesome LLM Apps lo enlaza como «Framework usado por varias plantillas de agentes (citado en el README)». | Orden indicado desde Awesome LLM Apps: Instálalo dentro del entorno de la plantilla que lo use. |
| [Composio](composio.md) | Combinación recíproca: Composio lo enlaza como «Adaptador oficial (`composio-openai-agents`)». | Orden indicado desde Composio: Instala el SDK y el adaptador. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[OpenAI Cookbook](openai-cookbook.md) · [PageIndex](pageindex.md)

**Notas:** Alternativas (elige una): pydantic-ai, langgraph, smolagents, deepagents, adk-python. Las trazas están activadas por defecto y van al panel de OpenAI; se desactivan con `OPENAI_AGENTS_DISABLE_TRACING=1`.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.24.0 (2026-10-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openai/openai-agents-python/blob/main/README.md) · [2](https://openai.github.io/openai-agents-python/models/litellm/) · [3](https://openai.github.io/openai-agents-python/mcp/) · [4](https://langfuse.com/integrations/frameworks/openai-agents) · [5](https://openai.github.io/openai-agents-python/tracing/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El ejemplo usa OPENAI_API_KEY; otros proveedores tienen condiciones propias; Codex no aporta créditos a este SDK |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Es una biblioteca de aplicaciones; la disponibilidad de adaptadores no confirma por sí sola una ruta local completa |
| Coste | El coste depende del proveedor o la ruta. El ejemplo usa OPENAI_API_KEY; otros proveedores tienen condiciones propias; Codex no aporta créditos a este SDK |
| Equipo | Preparación según la ruta elegida. Python y uv; modelo y credenciales |

Es una biblioteca de aplicaciones; la disponibilidad de adaptadores no confirma por sí sola una ruta local completa

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- modelo y credenciales

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv init
uv add openai-agents
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openai/openai-agents-python/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenAI Agents SDK para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/openai-agents-python/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Deriva una consulta a un especialista de facturación ficticio.

**Qué comprobar:** La traza muestra el traspaso y su respuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Enrutar consultas por departamento
- Validar una respuesta antes de aceptarla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Enrutar consultas por departamento; Validar una respuesta antes de aceptarla | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca de aplicaciones; la disponibilidad de adaptadores no confirma por sí sola una ruta local completa

## Stack y modelos

- **Stack:** Python y uv; modelo y credenciales
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pydantic AI](pydantic-ai.md) | 21.2k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. |
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [smolagents](smolagents.md) | 30.4k | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. |
| [Deep Agents](deepagents.md) | 31.3k | Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. |
| [Agent Development Kit (ADK)](adk-python.md) | 22.2k | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. |

## Enlaces

- 🐙 GitHub: [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- 🌐 Web: <https://openai.github.io/openai-agents-python/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openai/openai-agents-python/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
