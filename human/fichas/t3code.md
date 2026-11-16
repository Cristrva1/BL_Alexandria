[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Interfaces para gestionar sesiones

# 👨‍💻 T3 Code

> Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.6k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

T3 Code, plano de control open source para agentes de programación, de ping.gg. Licencia MIT. Es muy popular (~62k estrellas, v0.1.9).

## ¿Qué hace?

Ejecuta los agentes en tu máquina y les da una interfaz común en escritorio, web, iOS y Android: empiezas un hilo en el ordenador y apruebas el siguiente paso desde el móvil. Funciona con Claude Code, Codex, Cursor, OpenCode, Grok Build, Antigravity, Kiro y cualquier agente ACP, usando tus suscripciones.

## ¿Cómo lo hace?

Se instala con `brew install --cask t3-code` o las descargas por plataforma, o se prueba con `npx t3@latest`. Puede exponerse a agentes externos por MCP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente soportado. | Instala Claude Code y ábrelo desde T3 Code. |
| [Codex CLI](codex.md) | Agente soportado. | Instala Codex y selecciónalo. |
| [OpenCode](opencode.md) | Agente soportado. | Instala OpenCode y selecciónalo. |

**Notas:** Alternativa (elige una): opencode-manager.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.1.9 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pingdotgg/t3code/blob/main/README.md)</sub>

## Ver similares

Grupo **Gestores de sesiones de agentes de código**: T3 Code ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **T3 Code** (esta ficha) ⭐ recomendado | 72 | Si buscas esto: interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. |
| 2 | [opencode-manager](opencode-manager.md) | 44 | Si buscas esto: interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto dice no revender tokens; usa las cuentas y cuotas de los agentes ya configurados |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelo local no documentado. Documenta Claude Code, Codex y Antigravity entre sus proveedores; acceso remoto requiere configuración propia y no ejecuta los agentes en el teléfono |
| Coste | El coste depende del proveedor o la ruta. El proyecto dice no revender tokens; usa las cuentas y cuotas de los agentes ya configurados |
| Equipo | Preparación según la ruta elegida. Un agente instalado y autenticado; equipo que permanezca disponible; proyecto de prueba |

Documenta Claude Code, Codex y Antigravity entre sus proveedores; acceso remoto requiere configuración propia y no ejecuta los agentes en el teléfono

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente instalado y autenticado
- equipo que permanezca disponible
- proyecto de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar T3 Code para mi objetivo y necesito pasos guiados. Lee https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un agente local y pide explicar un archivo; revisa sus permisos desde la interfaz.

**Qué comprobar:** La sesión refleja el agente y puedes comprobar el archivo consultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Controlar una sesión desde otro dispositivo
- Comparar trabajo de Claude Code y Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Controlar una sesión desde otro dispositivo; Comparar trabajo de Claude Code y Codex | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code, Codex y Antigravity entre sus proveedores; acceso remoto requiere configuración propia y no ejecuta los agentes en el teléfono

## Stack y modelos

- **Stack:** Un agente instalado y autenticado; equipo que permanezca disponible; proyecto de prueba
- **Etiquetas:** `coding-agent` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [opencode-manager](opencode-manager.md) | 1.1k | Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil. |

## Enlaces

- 🐙 GitHub: [pingdotgg/t3code](https://github.com/pingdotgg/t3code)
- 🌐 Web: <https://t3.codes>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pingdotgg/t3code/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
