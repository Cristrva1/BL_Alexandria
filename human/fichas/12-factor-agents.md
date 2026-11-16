[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 12-Factor Agents

> Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12 Factor Apps.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.2k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Guía de 12 principios para construir aplicaciones con LLM fiables, escrita por Dex (HumanLayer) a imagen de las '12 Factor Apps'. El código es Apache 2.0 y el contenido CC BY-SA 4.0 (GitHub lo marca NOASSERTION). Es un texto de referencia estable; último push en septiembre de 2025.

## ¿Qué hace?

Defiende que los agentes en producción son sobre todo software determinista con LLMs en puntos concretos. Sus principios incluyen controlar los prompts, la ventana de contexto (factor 3, la base de la 'ingeniería de contexto') y el flujo de control, tratar las herramientas como salidas estructuradas, unificar estado de ejecución y de negocio, poder pausar y reanudar, contactar con humanos mediante herramientas y construir agentes pequeños y enfocados. Es crítica con depender de frameworks opacos.

## ¿Cómo lo hace?

Es contenido Markdown con ejemplos de código (TypeScript, entre otros) y una charla del AI Engineer World's Fair. Hay una discusión abierta para crear `npx/uvx create-12-factor-agent`, aún no publicado. No requiere instalación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Context-Engineering](context-engineering.md) | Profundiza en el factor 3 (gestionar la ventana de contexto). (combinación por arquitectura) | Lee primero los 12 factores y luego la guía de contexto. |
| [LangGraph](langgraph.md) | Framework de bajo nivel que permite aplicar los principios (control del flujo, pausar y reanudar) sin ocultar los prompts. (combinación por arquitectura) | Diseña con los 12 factores y usa LangGraph solo donde aporte estado duradero. |
| [AI SDK (Vercel)](vercel-ai.md) | Biblioteca ligera para aplicar los factores en TypeScript manteniendo el control de prompts y bucle. (combinación por arquitectura) | Implementa el bucle propio con generateText/tools. |
| [awesome-harness-engineering](awesome-harness-engineering.md) | Combinación recíproca: awesome-harness-engineering lo enlaza como «Principios concretos de diseño de harnesses fiables. (combinación por arquitectura)». | Orden indicado desde awesome-harness-engineering: Lee los 12 factores como base y usa la lista para ampliar. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2025-09-21 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/humanlayer/12-factor-agents/blob/main/README.md) · [2](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La guía no necesita API; implementar sus ideas sí puede usar modelos de pago o locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El bloque de pseudocódigo es ilustrativo y no un instalador ejecutable; la licencia de contenido es CC BY-SA |
| Coste | Sin pago a un modelo en la ruta básica. La guía no necesita API; implementar sus ideas sí puede usar modelos de pago o locales |
| Equipo | Preparación según la ruta elegida. Navegador; flujo de agente dibujado |

El bloque de pseudocódigo es ilustrativo y no un instalador ejecutable; la licencia de contenido es CC BY-SA

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- flujo de agente dibujado

1. Aplica el principio de controlar el flujo a un agente imaginario de soporte y señala dónde pedir intervención humana.
2. Comprueba: Obtienes un diagrama con pasos deterministas y decisiones del modelo.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/humanlayer/12-factor-agents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar 12-Factor Agents para mi objetivo y necesito pasos guiados. Lee https://github.com/humanlayer/12-factor-agents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Aplica el principio de controlar el flujo a un agente imaginario de soporte y señala dónde pedir intervención humana.

**Qué comprobar:** Obtienes un diagrama con pasos deterministas y decisiones del modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar un diseño antes de programar
- Estudiar recuperación de errores en agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar un diseño antes de programar; Estudiar recuperación de errores en agentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El bloque de pseudocódigo es ilustrativo y no un instalador ejecutable; la licencia de contenido es CC BY-SA

## Stack y modelos

- **Stack:** Navegador; flujo de agente dibujado
- **Etiquetas:** `agents` `learning` `prompts` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/humanlayer/12-factor-agents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
