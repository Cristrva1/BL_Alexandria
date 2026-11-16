[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 Agent Development Kit (ADK)

> Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 22.2k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Agent Development Kit (ADK) 2.0 de Google (Apache 2.0): framework Python «code-first» para construir, evaluar y desplegar agentes. Muy activo (v2.14.1), con versiones en Java, Kotlin, Go y TypeScript.

## ¿Qué hace?

Tiene un runtime de flujos basado en grafos (enrutamiento, fan-out/fan-in, bucles, reintentos, estado, nodos dinámicos, human-in-the-loop), una Task API para delegar entre agentes, sistemas multiagente jerárquicos, herramientas prediseñadas, funciones, OpenAPI y MCP, agentes sin código (Agent Config) y confirmación de herramientas. Está optimizado para Gemini, pero es agnóstico de modelo y de despliegue.

## ¿Cómo lo hace?

Python 3.11+ (`pip install google-adk`). Incluye ADK Web para desarrollar y se despliega en contenedores, Cloud Run o Agent Runtime en Gemini Enterprise Agent Platform (antes Vertex AI Agent Engine). Otros modelos se conectan, por ejemplo, mediante LiteLLM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Usar modelos no Gemini, incluidos locales (documentado en ADK). | Instala LiteLLM y configura el modelo en el agente. |
| [FastMCP](fastmcp.md) | Servidores MCP propios como herramientas (combinación por arquitectura; ADK documenta herramientas MCP). | Servidor MCP primero. |
| [langfuse](langfuse.md) | Trazas con la integración oficial de Langfuse para Google ADK. | Instrumenta antes de desplegar. |
| [skills](google-skills.md) | Skills oficiales de Google Cloud para que un agente de código despliegue en Cloud Run o Agent Runtime (combinación por arquitectura). | Independientes. |
| [Awesome LLM Apps](awesome-llm-apps.md) | Combinación recíproca: Awesome LLM Apps lo enlaza como «Framework de Google usado en otras plantillas (citado en el README)». | Orden indicado desde Awesome LLM Apps: Instálalo en el entorno de la plantilla correspondiente. |
| [gemini-skills](gemini-skills.md) | Combinación recíproca: gemini-skills lo enlaza como «Construir agentes sobre la API de Gemini con el ADK (combinación por arquitectura)». | Orden indicado desde gemini-skills: Independientes. |

**Notas:** Alternativas (elige una): langgraph, openai-agents-python. Se quitó gemini-cli: no es una integración.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2.14.1 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google/adk-python/blob/main/README.md) · [2](https://google.github.io/adk-docs/agents/models/) · [3](https://google.github.io/adk-docs/tools/mcp-tools/) · [4](https://langfuse.com/integrations/frameworks/google-adk)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Los modelos y servicios se facturan según el proveedor; el SDK no incluye crédito de Antigravity |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Que Google publique ADK no lo convierte en configuración de Antigravity |
| Coste | El coste depende del proveedor o la ruta. Los modelos y servicios se facturan según el proveedor; el SDK no incluye crédito de Antigravity |
| Equipo | Preparación según la ruta elegida. Python 3.11+; entorno virtual; modelo configurado |

Que Google publique ADK no lo convierte en configuración de Antigravity

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11+
- entorno virtual
- modelo configurado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install google-adk
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google/adk-python/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agent Development Kit (ADK) para mi objetivo y necesito pasos guiados. Lee https://github.com/google/adk-python/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta el horario de una tienda ficticia mediante una herramienta del agente.

**Qué comprobar:** El agente devuelve el dato de la herramienta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar información de negocio
- Evaluar la selección de herramientas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar información de negocio; Evaluar la selección de herramientas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Que Google publique ADK no lo convierte en configuración de Antigravity

## Stack y modelos

- **Stack:** Python 3.11+; entorno virtual; modelo configurado
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [OpenAI Agents SDK](openai-agents-python.md) | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |

## Enlaces

- 🐙 GitHub: [google/adk-python](https://github.com/google/adk-python)
- 🌐 Web: <https://google.github.io/adk-docs/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google/adk-python/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
