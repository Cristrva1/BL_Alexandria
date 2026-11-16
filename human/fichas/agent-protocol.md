[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ Agent Protocol

> Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 698 | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Agent Protocol, especificación de LangChain de APIs independientes del framework para servir agentes LLM en producción. Licencia MIT. Es una especificación de nicho (~700 estrellas).

## ¿Qué hace?

Define endpoints para runs, threads, store y streaming (Agent Streaming Protocol con esquema CDDL y bindings Python/TypeScript). LangGraph Platform implementa un superconjunto.

## ¿Cómo lo hace?

Incluye la especificación OpenAPI, stubs de servidor en Python (Pydantic V2 y FastAPI) y referencias a la implementación LangGraph.js API.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | LangGraph Platform implementa un superconjunto. | Despliega agentes con LangGraph. |
| [LangGraph.js](langgraphjs.md) | Implementación open source en LangGraph.js API. | Sirve el agente JS con langgraph-api. |
| [Deep Agents](deepagents.md) | Agentes servibles mediante el servidor LangGraph. (combinación por arquitectura) | Expón el agente vía el servidor. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-05 · última versión publicada langchain-protocol==0.0.21 (2026-11-05) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langchain-ai/agent-protocol/blob/main/README.md) · [2](https://langchain-ai.github.io/agent-protocol/api.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Leer la especificación no consume API de IA; una implementación y su alojamiento tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una especificación de API y no MCP ni un servidor instalable; los bloques Hurl ilustran peticiones y no son comandos de terminal normales |
| Coste | Sin pago a un modelo en la ruta básica. Leer la especificación no consume API de IA; una implementación y su alojamiento tienen costes propios |
| Equipo | Preparación según la ruta elegida. Navegador; nociones de HTTP |

Es una especificación de API y no MCP ni un servidor instalable; los bloques Hurl ilustran peticiones y no son comandos de terminal normales

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- nociones de HTTP

1. Lee las rutas threads y runs y dibuja cómo una aplicación inicia y consulta una ejecución.
2. Comprueba: Puedes distinguir estado del hilo y ejecución del agente.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/agent-protocol/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agent Protocol para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/agent-protocol/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee las rutas threads y runs y dibuja cómo una aplicación inicia y consulta una ejecución.

**Qué comprobar:** Puedes distinguir estado del hilo y ejecución del agente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar una API de agentes
- Comparar protocolos antes de implementar

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar una API de agentes; Comparar protocolos antes de implementar | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una especificación de API y no MCP ni un servidor instalable; los bloques Hurl ilustran peticiones y no son comandos de terminal normales

## Stack y modelos

- **Stack:** Navegador; nociones de HTTP
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)
- 🌐 Web: <https://langchain-ai.github.io/agent-protocol/api.html>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/agent-protocol/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
