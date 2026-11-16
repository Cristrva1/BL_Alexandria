[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🎨 gstack

> Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 142k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

«Fábrica de software» de código abierto (MIT) de Garry Tan, presidente y CEO de Y Combinator, que convierte Claude Code y otros agentes en un equipo de ingeniería virtual. Muy activo (v1.99.4.0), con canal estable y releases frecuentes.

## ¿Qué hace?

Asigna roles especializados: un CEO que replantea el producto (`/office-hours` escribe un documento de diseño), un jefe de ingeniería que fija la arquitectura, un diseñador contra el «AI slop», un revisor que busca bugs que pasan CI (`/review`), QA que abre un navegador real y reproduce bugs (`/qa`), y `/autoplan` y `/ship` para revisar planes y publicar con tests y revisión.

## ¿Cómo lo hace?

Se clona en `~/.claude/skills/gstack` y se ejecuta `./setup`, que requiere Claude Code, Git y Bun 1.4.2+. Claude Code tiene soporte completo, con hooks que bloquean pasos indebidos. Codex CLI, OpenCode y Cursor tienen soporte experimental (`--host codex|opencode|cursor`), donde las reglas solo son orientativas. Algunas funciones usan Codex CLI con sesión iniciada como segunda opinión.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Host con soporte completo (`--host claude`). | Instala Bun antes de `./setup`. |
| [Codex CLI](codex.md) | Host experimental y segunda opinión documentada. | Codex CLI con sesión iniciada. |
| [OpenCode](opencode.md) | Host experimental (`--host opencode`). | `./setup --host opencode`. |

**Notas:** Alternativas (elige una): superclaude-framework, superpowers, ecc.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.99.4.0 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/garrytan/gstack/blob/main/README.md)</sub>

## Ver similares

Grupo **Metodologías y harness para agentes de código**: gstack ocupa la posición 2 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ECC](ecc.md) ⭐ recomendado | 72 | Si quieres un sistema completo de skills, hooks y configuración adaptable a varios agentes. |
| 2 | **gstack** (esta ficha) | 66 | Si quieres el flujo de planificar, implementar, revisar y probar que usa Garry Tan con Claude Code. |
| 3 | [Agent Skills (Addy Osmani)](agent-skills.md) | 63 | Si quieres skills de ingeniería portables en el formato Agent Skills. |
| 4 | [superpowers](superpowers.md) | 62 | Si quieres que el agente siga TDD, planificación y revisión de forma disciplinada. |
| 5 | [SuperClaude_Framework](superclaude-framework.md) | 49 | Si quieres comandos y personas para Claude Code organizados por fase. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Se consumen los agentes que intervienen; algunas rutas piden otro CLI autenticado para la revisión cruzada |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Los hosts Codex y Antigravity aparecen como experimentales y con comprobaciones advisory; no se equiparan a la ruta completa de Claude Code |
| Coste | El coste depende del proveedor o la ruta. Se consumen los agentes que intervienen; algunas rutas piden otro CLI autenticado para la revisión cruzada |
| Equipo | Preparación según la ruta elegida. Git, Bun y cliente autenticado;  en Windows revisar Git Bash o WSL y Node.js |

Los hosts Codex y Antigravity aparecen como experimentales y con comprobaciones advisory; no se equiparan a la ruta completa de Claude Code

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Git, Bun y cliente autenticado
-  en Windows revisar Git Bash o WSL y Node.js

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host auto      # or: ./setup --host codex
./setup --status                         # one row per install: host, tier, scope, version, path
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/garrytan/gstack/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar gstack para mi objetivo y necesito pasos guiados. Lee https://github.com/garrytan/gstack/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta el estado de instalación y prueba una revisión o planificación sobre un cambio pequeño.

**Qué comprobar:** El estado indica el host y puedes revisar el resultado de la skill elegida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una revisión de producto antes de implementar
- Abrir un navegador de prueba para revisar una interfaz propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una revisión de producto antes de implementar; Abrir un navegador de prueba para revisar una interfaz propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los hosts Codex y Antigravity aparecen como experimentales y con comprobaciones advisory; no se equiparan a la ruta completa de Claude Code

## Stack y modelos

- **Stack:** Git, Bun y cliente autenticado;  en Windows revisar Git Bash o WSL y Node.js
- **Etiquetas:** `metodologia` `skill` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SuperClaude_Framework](superclaude-framework.md) | 23.9k | Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code. |
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |
| [ECC](ecc.md) | 303k | Sistema de skills, hooks y configuración para agentes de código, con rutas nativas y adaptadores cuya capacidad varía según el cliente. |

## Enlaces

- 🐙 GitHub: [garrytan/gstack](https://github.com/garrytan/gstack)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/garrytan/gstack/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
