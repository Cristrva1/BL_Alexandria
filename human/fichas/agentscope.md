[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 📚 AgentScope

> Framework de agentes en Python de origen Alibaba: agentes ReAct, multiagente, herramientas MCP, sandbox, voz en tiempo real y servicio desplegable.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 36.1k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de agentes de código abierto (Apache-2.0) desarrollado por el equipo de AgentScope (origen en Alibaba/Tongyi). La versión 2.0 se presenta como lista para producción; requiere Python 3.11 o superior y tiene desarrollo muy activo.

## ¿Qué hace?

Permite construir agentes que razonan y usan herramientas: agentes ReAct, equipos con líder que delega (TeamPipeline), procedimientos operativos estándar, enrutado de modelos, agentes de voz en tiempo real por WebRTC y un servicio de agentes con historial compartido. Gestiona herramientas Python, servidores MCP y skills, con ejecución aislada local, Docker o en sandbox remoto.

## ¿Cómo lo hace?

Se instala con `uv pip install agentscope` (o desde el código con `uv pip install -e .`); el frontend del servicio usa pnpm. Los modelos se configuran por proveedor (OpenAI, Anthropic, Gemini, DashScope, Ollama, entre otros) y las herramientas MCP se registran en el toolkit. La documentación cubre bloques de construcción, despliegue y trazas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | AgentScope incluye cliente de modelos para Ollama, de modo que los agentes pueden razonar con modelos locales. | Ollama con un modelo descargado; después configura el modelo de Ollama en AgentScope. |
| [FastMCP](fastmcp.md) | El toolkit de AgentScope registra servidores MCP; FastMCP sirve para escribir esos servidores con herramientas propias (combinación por arquitectura). | Escribe y arranca el servidor con FastMCP; después regístralo en el toolkit del agente. |
| [langfuse](langfuse.md) | Las trazas de agentes (OpenTelemetry) pueden enviarse a una plataforma de observabilidad como Langfuse (combinación por arquitectura) [DATO NO VERIFICADO: configuración concreta]. | Langfuse en marcha; después configura el exportador de trazas en AgentScope. |
| [litellm](litellm.md) | Un proxy LiteLLM con API compatible con OpenAI permite cambiar de proveedor sin tocar el código de los agentes (combinación por arquitectura). | LiteLLM primero; después apunta el cliente OpenAI de AgentScope a su URL. |

**Notas:** Alternativas cercanas en el catálogo: crewai, ag2, camel.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.0.12 (2026-11-16) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/agentscope-ai/agentscope/blob/main/README.md) · [2](https://docs.agentscope.io/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
uv pip install agentscope
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/agentscope-ai/agentscope/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AgentScope para mi objetivo y necesito pasos guiados. Lee https://github.com/agentscope-ai/agentscope/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `uv pip install agentscope` y ejecuta el ejemplo de inicio rápido con un modelo configurado..

**Qué comprobar:** El agente responde y usa al menos una herramienta, y puedes ver sus pasos en la salida..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- construir un agente con herramientas MCP y memoria que puedas inspeccionar paso a paso
- orquestar un equipo de agentes con un líder que delega tareas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: construir un agente con herramientas MCP y memoria que puedas inspeccionar paso a paso; orquestar un equipo de agentes con un líder que delega tareas | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `agents` `python` `mcp` `framework`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)
- 🌐 Web: <https://docs.agentscope.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/agentscope-ai/agentscope/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
