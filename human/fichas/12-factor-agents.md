[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Guías, cursos y cookbooks

# 🎓 12-Factor Agents

> Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12 Factor Apps.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.2k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo. |
| Coste | Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Ensayo de Dex Horthy (HumanLayer) que resume lo aprendido construyendo agentes para clientes reales: los productos que funcionan son sobre todo software determinista con pasos de LLM bien colocados. Cada factor (controlar tus prompts, tu ventana de contexto y tu flujo de control, pausar y reanudar, contactar a humanos con tool calls, agentes pequeños) tiene su capítulo con diagramas y ejemplos.

## Por qué destaca

Es agnóstico al framework y se ha vuelto una referencia habitual sobre context engineering y diseño de agentes. Ayuda a decidir qué partes conviene programar a mano en vez de dejarlas al bucle del agente.

## Cómo funciona

Es un README con un capítulo en Markdown por factor, diagramas y fragmentos de código, sobre todo en TypeScript; también enlaza la charla del AI Engineer World's Fair.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

1. Abre el material original y elige un capítulo o ejemplo.
2. Revisa los requisitos de ese ejemplo antes de instalar dependencias.
3. Usa las alternativas y recetas para situarlo dentro de tu proyecto.

[Instrucciones originales de instalación](https://github.com/humanlayer/12-factor-agents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar 12-Factor Agents para mi objetivo y necesito pasos guiados. Lee https://github.com/humanlayer/12-factor-agents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Revisar la arquitectura de un agente antes de llevarlo a producción
- Decidir cuándo usar un framework y cuándo código propio
- Diseñar pasos con aprobación humana mediante tool calls

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| vas a construir un agente para clientes reales y quieres principios de diseño antes de elegir framework | buscas tutoriales con código ejecutable paso a paso; mira `agents-towards-production` o `ai-agents-for-beginners` |

**Limitaciones:** Sin cambios desde septiembre de 2025; el contenido es CC BY-SA 4.0 y el código Apache 2.0.

## Stack y modelos

- **Stack:** Markdown, TypeScript (ejemplos)
- **Etiquetas:** `agents` `learning` `prompts` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Context-Engineering](context-engineering.md) | 9.3k | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. |
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [AI SDK (Vercel)](vercel-ai.md) | 28k | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. |

## Enlaces

- 🐙 GitHub: [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/humanlayer/12-factor-agents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
