[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🕸️ nodeterm

> Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.5k | NOASSERTION | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

nodeterm, gestor de terminales y sesiones de agentes sobre un lienzo infinito, de @eneskirca. Licencia Business Source License 1.1 (no es open source; GitHub muestra NOASSERTION). Tiene ~2.5k estrellas y busca patrocinadores fundadores.

## ¿Qué hace?

Coloca terminales reales como nodos arrastrables en un lienzo con zoom, y cada proyecto funciona además como tablero tipo Trello de sesiones de Claude Code en vivo. Está pensado para personas con TDAH o flujos de trabajo dispersos.

## ¿Cómo lo hace?

Hay app de escritorio para macOS, Linux y Windows (beta), con `brew install --cask nodeterm`, edición servidor autoalojada para usarlo desde el navegador y app compañera para iOS.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Sesiones de Claude Code integradas en el tablero. | Instala Claude Code y añade nodos de sesión. |
| [Codex CLI](codex.md) | Otro agente de terminal en un nodo. (combinación por arquitectura) | Abre Codex en un nodo de terminal. |
| [OpenCode](opencode.md) | Otro agente de terminal en un nodo. (combinación por arquitectura) | Abre OpenCode en un nodo de terminal. |

**Notas:** Sin alternativas declaradas. Licencia BUSL: revisa las restricciones de uso.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.5.1 (2026-11-06) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/eneskirca/nodeterm/blob/main/README.md) · [2](https://nodeterm.dev/docs)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El gestor usa cuentas de los agentes; dictado local Whisper y funciones AI opcionales tienen requisitos separados |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. Documenta Claude Code, Codex y Antigravity; la licencia BUSL-1.1 y sus límites no deben presentarse como MIT sin restricciones; local aquí incluye dictado, no todo agente |
| Coste | El coste depende del proveedor o la ruta. El gestor usa cuentas de los agentes; dictado local Whisper y funciones AI opcionales tienen requisitos separados |
| Equipo | Preparación según la ruta elegida. macOS o Linux; tmux según ruta; CLI de agente autenticado |

Documenta Claude Code, Codex y Antigravity; la licencia BUSL-1.1 y sus límites no deben presentarse como MIT sin restricciones; local aquí incluye dictado, no todo agente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- macOS o Linux
- tmux según ruta
- CLI de agente autenticado

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/eneskirca/nodeterm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar nodeterm para mi objetivo y necesito pasos guiados. Lee https://github.com/eneskirca/nodeterm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un terminal y un nodo de agente para explicar una carpeta de prueba.

**Qué comprobar:** Puedes ver sesión, terminal y contexto de proyecto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar varias sesiones de código
- Asociar sesiones con worktrees

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar varias sesiones de código; Asociar sesiones con worktrees | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code, Codex y Antigravity; la licencia BUSL-1.1 y sus límites no deben presentarse como MIT sin restricciones; local aquí incluye dictado, no todo agente

## Stack y modelos

- **Stack:** macOS o Linux; tmux según ruta; CLI de agente autenticado
- **Etiquetas:** `infra` `adhd` `agent-orchestration` `ai-agents` `canvas` `claude-code` `codex` `coding-agents`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [eneskirca/nodeterm](https://github.com/eneskirca/nodeterm)
- 🌐 Web: <https://nodeterm.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/eneskirca/nodeterm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
