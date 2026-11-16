[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Interfaces para gestionar sesiones

# 🖥️ opencode-manager

> Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.1k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 44/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OpenCode Manager, centro de mando web autoalojado para OpenCode, de @chriswritescode-dev. Licencia MIT. Tiene ~1k estrellas y está activo.

## ¿Qué hace?

Reúne en una app web, usable desde escritorio y móvil, las sesiones de OpenCode, git, una terminal y tareas programadas. Incluye la CLI `ocm`.

## ¿Cómo lo hace?

Requiere Docker con Compose v2. Se instala con `curl -fsSL https://opencodemanager.app/install | sh`, que lo arranca en http://localhost:5003 y pide crear una cuenta de administrador. Es un workspace pnpm: backend con Bun y Hono, frontend con React y Vite.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenCode](opencode.md) | Agente que gestiona. | Instala OpenCode y luego el gestor. |
| [Ollama](ollama.md) | Modelos locales para las sesiones de OpenCode. (combinación por arquitectura) | Configura Ollama como proveedor en OpenCode. |
| [coolify](coolify.md) | Desplegar el contenedor en un servidor propio. (combinación por arquitectura) | Despliega con Compose desde Coolify. |

**Notas:** Alternativa (elige una): t3code.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.1.0 (2026-10-26) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/chriswritescode-dev/opencode-manager/blob/main/README.md) · [2](https://opencodemanager.app/docs/getting-started/installation)</sub>

## Ver similares

Grupo **Gestores de sesiones de agentes de código**: opencode-manager ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [T3 Code](t3code.md) ⭐ recomendado | 72 | Si buscas esto: interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. |
| 2 | **opencode-manager** (esta ficha) | 44 | Si buscas esto: interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Alojamiento y modelo de OpenCode se pagan o ejecutan según configuración; el panel no incorpora créditos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Este panel es para OpenCode; no se deduce compatibilidad directa con Claude Code o Codex por usar tecnologías similares |
| Coste | El coste depende del proveedor o la ruta. Alojamiento y modelo de OpenCode se pagan o ejecutan según configuración; el panel no incorpora créditos |
| Equipo | Preparación según la ruta elegida. Docker Compose v2 o entorno de desarrollo; OpenCode; proveedor configurado |

Este panel es para OpenCode; no se deduce compatibilidad directa con Claude Code o Codex por usar tecnologías similares

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker Compose v2 o entorno de desarrollo
- OpenCode
- proveedor configurado

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://opencodemanager.app/docs/getting-started/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar opencode-manager para mi objetivo y necesito pasos guiados. Lee https://opencodemanager.app/docs/getting-started/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una sesión en un repositorio de ejemplo y revisa cambios sin programar tareas todavía.

**Qué comprobar:** Puedes reconocer la sesión, terminal y estado Git.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Gestionar sesiones desde el navegador
- Consultar un proyecto desde el móvil

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Gestionar sesiones desde el navegador; Consultar un proyecto desde el móvil | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Este panel es para OpenCode; no se deduce compatibilidad directa con Claude Code o Codex por usar tecnologías similares

## Stack y modelos

- **Stack:** Docker Compose v2 o entorno de desarrollo; OpenCode; proveedor configurado
- **Etiquetas:** `coding` `agent` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [T3 Code](t3code.md) | 60.6k | Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. |

## Enlaces

- 🐙 GitHub: [chriswritescode-dev/opencode-manager](https://github.com/chriswritescode-dev/opencode-manager)
- 🌐 Web: <https://opencodemanager.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/chriswritescode-dev/opencode-manager/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
