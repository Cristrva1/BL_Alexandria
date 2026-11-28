[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 💪 superpowers

> Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 318k | MIT | Shell | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Metodología completa de desarrollo para agentes de código de Jesse Vincent y Prime Radiant (MIT), basada en skills combinables. Muy activa (v7.0.2); Prime Radiant ofrece soporte comercial.

## ¿Qué hace?

Antes de programar, el agente pregunta qué quieres conseguir, redacta una especificación en partes legibles, pide aprobación, crea un plan, aísla el trabajo en git worktrees y ejecuta tareas con subagentes y revisión (`subagent-driven-development`), con TDD. Su componente visual opcional carga el logo de Prime Radiant desde su web por defecto, e incluye la versión instalada: es telemetría mínima que, según el README, no envía detalles del proyecto ni de los prompts.

## ¿Cómo lo hace?

Skills más instrucciones iniciales y hooks de sesión. Se instala por separado en cada herramienta: Claude Code (`/plugin install superpowers@claude-plugins-official`), Codex, Cursor, Gemini CLI (`gemini extensions install`), Copilot CLI, OpenCode, Hermes Agent y otros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code Plugins Directory](claude-plugins-official.md) | Disponible en el marketplace oficial. | Instala desde ese marketplace. |
| [Codex CLI](codex.md) | Instalación documentada (app y CLI). | Sigue la sección de Codex. |
| [Gemini CLI](gemini-cli.md) | Extensión de Gemini CLI. | `gemini extensions install https://github.com/obra/superpowers`. |
| [hermes-agent](hermes-agent.md) | Instalación documentada para Hermes Agent. | Reinicia la sesión tras instalar para activar los hooks. |
| [Claude Code](claude-code.md) | Combinación recíproca: Claude Code lo enlaza como «Biblioteca de skills y flujos para Claude Code». | Orden indicado desde Claude Code: Instala el plugin desde su marketplace. |

**Notas:** Alternativas (elige una): agent-skills, ecc, gstack. Se quitaron awesome-claude-code y agent-toolkit porque no hay integración. La telemetría se desactiva con `SUPERPOWERS_DISABLE_TELEMETRY`; también respeta `DISABLE_TELEMETRY` de Claude Code.

Estado en GitHub: activo · último push 2026-11-03 · última versión publicada v7.0.2 (2026-11-03) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/obra/superpowers/blob/main/README.md)</sub>

## Ver similares

Grupo **Metodologías y harness para agentes de código**: superpowers ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ECC](ecc.md) ⭐ recomendado | 70 | Si quieres un sistema completo de skills, hooks y configuración adaptable a varios agentes. |
| 2 | [gstack](gstack.md) | 64 | Si quieres el flujo de planificar, implementar, revisar y probar que usa Garry Tan con Claude Code. |
| 3 | [Agent Skills (Addy Osmani)](agent-skills.md) | 61 | Si quieres skills de ingeniería portables en el formato Agent Skills. |
| 4 | **superpowers** (esta ficha) | 57 | Si quieres que el agente siga TDD, planificación y revisión de forma disciplinada. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La metodología usa el acceso del agente anfitrión; sus benchmarks no son una promesa de ahorro para tu proyecto |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Claude Code, Codex y Antigravity tienen rutas de instalación propias en el README |
| Coste | Consumo del agente que ya utilizas. La metodología usa el acceso del agente anfitrión; sus benchmarks no son una promesa de ahorro para tu proyecto |
| Equipo | Preparación según la ruta elegida. Cliente compatible;  proyecto pequeño o carpeta de prueba |

Claude Code, Codex y Antigravity tienen rutas de instalación propias en el README

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cliente compatible
-  proyecto pequeño o carpeta de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
/plugin install superpowers@claude-plugins-official
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/obra/superpowers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar superpowers para mi objetivo y necesito pasos guiados. Lee https://github.com/obra/superpowers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Describe una mejora sencilla y revisa la fase de definición y planificación.

**Qué comprobar:** El agente muestra una propuesta acotada antes de cambiar archivos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Dividir una funcionalidad en tareas que se puedan verificar
- Trabajar con pruebas y revisión antes de cerrar un cambio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Dividir una funcionalidad en tareas que se puedan verificar; Trabajar con pruebas y revisión antes de cerrar un cambio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude Code, Codex y Antigravity tienen rutas de instalación propias en el README

## Stack y modelos

- **Stack:** Cliente compatible;  proyecto pequeño o carpeta de prueba
- **Etiquetas:** `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agent Skills (Addy Osmani)](agent-skills.md) | 118k | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. |
| [ECC](ecc.md) | 303k | Sistema de skills, hooks y configuración para agentes de código, con rutas nativas y adaptadores cuya capacidad varía según el cliente. |
| [gstack](gstack.md) | 142k | Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code. |

## Enlaces

- 🐙 GitHub: [obra/superpowers](https://github.com/obra/superpowers)
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/obra/superpowers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
