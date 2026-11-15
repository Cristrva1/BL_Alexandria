[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 LangGraph

> Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 45k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

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

## Qué puedes hacer con él

Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming.

## Por qué destaca

Usos propuestos: Pausar una devolución hasta su revisión; Retomar una investigación interrumpida.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [crewAI](crewai.md) | 60.9k | Framework para orquestar "crews" de agentes con roles y tareas. |
| [OpenAI Agents SDK](openai-agents-python.md) | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |
| [Pydantic AI](pydantic-ai.md) | 21.2k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. |
| [LangGraph Supervisor](langgraph-supervisor-py.md) | 1.7k | Librería archivada para crear un agente supervisor que coordina a otros agentes en LangGraph. |
| [Agent Development Kit (ADK)](adk-python.md) | 22.2k | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. |

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
