[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧭 Agent Skills (Addy Osmani)

> Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 118k | MIT | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skills de ingeniería de Addy Osmani (MIT) para agentes de código, centradas en procesos de nivel producción. Activas (0.6.16).

## ¿Qué hace?

25 skills y 9 comandos que cubren el ciclo de desarrollo: `/spec`, `/plan`, `/build`, `/test`, `/constraints`, `/review`, `/webperf`, `/code-simplify` y `/ship`. Incluyen revisión en cinco ejes, entrevista de requisitos y TDD obligatorio.

## ¿Cómo lo hace?

Se instalan con `npx skills add addyosmani/agent-skills` (todas o `--skill` por separado), como plugin de Claude Code (`/plugin marketplace add addyosmani/agent-skills`) o a mano en Cursor (`.cursor/skills` y reglas `.mdc`) y Gemini CLI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial; los comandos se instalan con su espacio de nombres. | Usa la forma con espacio de nombres si choca con `/review`. |
| [Codex CLI](codex.md) | Instalable con skills CLI. | `npx skills add addyosmani/agent-skills`. |
| [Gemini CLI](gemini-cli.md) | Guía de instalación documentada. | Sigue la sección de Gemini CLI. |
| [plugins](plugins.md) | Combinación recíproca: plugins lo enlaza como «Skills de ingeniería con guía de instalación para Cursor». | Orden indicado desde plugins: Sigue la sección de Cursor. |

**Notas:** Alternativa (elige una): superpowers.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 0.6.16 (2026-11-14) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/addyosmani/agent-skills/blob/main/README.md)</sub>

## Ver similares

Grupo **Metodologías y harness para agentes de código**: Agent Skills (Addy Osmani) ocupa la posición 3 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ECC](ecc.md) ⭐ recomendado | 72 | Si quieres un sistema completo de skills, hooks y configuración adaptable a varios agentes. |
| 2 | [gstack](gstack.md) | 66 | Si quieres el flujo de planificar, implementar, revisar y probar que usa Garry Tan con Claude Code. |
| 3 | **Agent Skills (Addy Osmani)** (esta ficha) | 64 | Si quieres skills de ingeniería portables en el formato Agent Skills. |
| 4 | [superpowers](superpowers.md) | 59 | Si quieres que el agente siga TDD, planificación y revisión de forma disciplinada. |
| 5 | [SuperClaude_Framework](superclaude-framework.md) | 49 | Si quieres comandos y personas para Claude Code organizados por fase. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El repositorio aporta instrucciones; el modelo se factura por el acceso del agente |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Antigravity tiene una guía propia y limitaciones de comandos en algunas versiones; usa las skills subyacentes cuando corresponda |
| Coste | Consumo del agente que ya utilizas. El repositorio aporta instrucciones; el modelo se factura por el acceso del agente |
| Equipo | Preparación según la ruta elegida. Node.js y un agente compatible;  instalar solo las skills necesarias |

Antigravity tiene una guía propia y limitaciones de comandos en algunas versiones; usa las skills subyacentes cuando corresponda

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js y un agente compatible
-  instalar solo las skills necesarias

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add addyosmani/agent-skills            # install all 25 skills
npx skills add addyosmani/agent-skills --list     # browse before installing
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/addyosmani/agent-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agent Skills (Addy Osmani) para mi objetivo y necesito pasos guiados. Lee https://github.com/addyosmani/agent-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide una revisión de calidad sobre un cambio pequeño del proyecto.

**Qué comprobar:** La revisión aplica los criterios de la skill y señala archivos concretos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una especificación antes de escribir una funcionalidad
- Revisar un diff con criterios de calidad y pruebas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una especificación antes de escribir una funcionalidad; Revisar un diff con criterios de calidad y pruebas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Antigravity tiene una guía propia y limitaciones de comandos en algunas versiones; usa las skills subyacentes cuando corresponda

## Stack y modelos

- **Stack:** Node.js y un agente compatible;  instalar solo las skills necesarias
- **Etiquetas:** `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |

## Enlaces

- 🐙 GitHub: [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- 🌐 Web: <https://skills.addy.ie>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/addyosmani/agent-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
