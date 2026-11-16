[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 📂 claude-code-hooks-mastery

> Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de trabajo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4k | — | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## ¿Qué es?

Repositorio didáctico de disler (IndyDevDan) para dominar los hooks de Claude Code, con subagentes, estilos de salida y líneas de estado. Sin licencia declarada; último cambio en marzo de 2026.

## ¿Qué hace?

Muestra el ciclo de vida y los payloads de todos los hooks, el control de flujo con códigos de error, un análisis a fondo de `UserPromptSubmit`, subagentes, un sistema de validación por equipos, una colección de estilos de salida y líneas de estado personalizadas, con ejemplos como avisos de voz.

## ¿Cómo lo hace?

Los hooks son scripts Python de un solo archivo ejecutados con uv (dependencias declaradas en el propio script, sin gestionar entornos). Requiere uv y Claude Code; opcionalmente usa ElevenLabs (con su servidor MCP), OpenAI y Anthropic para voz y LLM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Los hooks se configuran en `.claude/settings.json`. | Copia los hooks que necesites y revísalos: se ejecutan con tus permisos. |
| [ECC](ecc.md) | Marco que también usa hooks; sirve de ejemplo de producción (combinación por arquitectura). | No mezcles hooks de ambos sin revisar los conflictos. |
| [claude-code-router](claude-code-router.md) | Enrutar Claude Code a otros modelos mientras experimentas con hooks (combinación por arquitectura). | Independientes. |

**Notas:** Sin licencia: úsalo como referencia didáctica.

Estado en GitHub: activo · último push 2026-03-04 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/disler/claude-code-hooks-mastery/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los hooks deterministas no necesitan un modelo adicional; los ejemplos de voz o mensajes inteligentes pueden usar APIs u Ollama |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Se distingue el material de aprendizaje de un plugin automático; no hace falta activar todos los ejemplos ni sus servicios opcionales |
| Coste | El coste depende del proveedor o la ruta. Los hooks deterministas no necesitan un modelo adicional; los ejemplos de voz o mensajes inteligentes pueden usar APIs u Ollama |
| Equipo | Preparación según la ruta elegida. Claude Code y uv;  revisar solo un ejemplo de hook y sus dependencias |

Se distingue el material de aprendizaje de un plugin automático; no hace falta activar todos los ejemplos ni sus servicios opcionales

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code y uv
-  revisar solo un ejemplo de hook y sus dependencias

1. Estudia un hook sencillo de sesión y adapta una comprobación en una carpeta de prueba.
2. Comprueba: El hook produce el evento o registro esperado al activar esa fase de la sesión.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/disler/claude-code-hooks-mastery/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-code-hooks-mastery para mi objetivo y necesito pasos guiados. Lee https://github.com/disler/claude-code-hooks-mastery/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Estudia un hook sencillo de sesión y adapta una comprobación en una carpeta de prueba.

**Qué comprobar:** El hook produce el evento o registro esperado al activar esa fase de la sesión.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Registrar cuándo empieza y termina una sesión de trabajo
- Comprender un control que revisa una acción antes de ejecutarla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Registrar cuándo empieza y termina una sesión de trabajo; Comprender un control que revisa una acción antes de ejecutarla | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se distingue el material de aprendizaje de un plugin automático; no hace falta activar todos los ejemplos ni sus servicios opcionales

## Stack y modelos

- **Stack:** Claude Code y uv;  revisar solo un ejemplo de hook y sus dependencias
- **Etiquetas:** `metodologia` `reference` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/disler/claude-code-hooks-mastery/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
