[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🧑‍🤝‍🧑 multica

> Workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.1k | NOASSERTION | Go | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Multica, workspace para asignar trabajo a agentes de programación como si fueran compañeros de equipo, de multica-ai, escrito en Go. Es source-available: «Multica License», Apache-2.0 con condiciones adicionales sobre servicios alojados, integración comercial y marca. Tiene ~56k estrellas.

## ¿Qué hace?

Los agentes reciben issues, informan del progreso, señalan bloqueos y devuelven el resultado para revisión. Admite squads mixtos de personas y agentes, skills reutilizables y runtimes propios mediante un daemon.

## ¿Cómo lo hace?

Se autoaloja con Docker Compose o Helm usando imágenes de GHCR, y usa las CLIs de agente que ya tienes (Claude Code, Codex, Cursor, Copilot, Kimi, OpenCode). Tiene telemetría anónima de despliegue que se puede desactivar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Runtime de agente soportado. | Instala Claude Code en el runtime. |
| [Codex CLI](codex.md) | Runtime de agente soportado. | Instala Codex en el runtime. |
| [OpenCode](opencode.md) | Runtime de agente soportado. | Instala OpenCode en el runtime. |
| [andrej-karpathy-skills](andrej-karpathy-skills.md) | Combinación recíproca: andrej-karpathy-skills lo enlaza como «Plataforma del mismo autor para gestionar agentes con skills reutilizables (combinación por arquitectura)». | Orden indicado desde andrej-karpathy-skills: Independientes. |

**Notas:** Alternativa (elige una): paperclip. Se quitan ruflo y chatwoot (sin relación documentada). La licencia no es OSI.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.9.0 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/multica-ai/multica/blob/main/README.md) · [2](https://multica.ai/docs/agents)</sub>

## Ver similares

Grupo **Paneles para coordinar equipos de agentes**: multica ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [paperclip](paperclip.md) ⭐ recomendado | 67 | Si buscas esto: servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. |
| 2 | **multica** (esta ficha) | 56 | Si buscas esto: workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Usa las cuentas de los agentes y alojamiento propio o servicio; no incluye créditos |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Se declara source-available con licencia Multica que añade condiciones a Apache; no debe resumirse como Apache puro ni como una garantía de sustituir empleados |
| Coste | El coste depende del proveedor o la ruta. Usa las cuentas de los agentes y alojamiento propio o servicio; no incluye créditos |
| Equipo | Preparación según la ruta elegida. Un CLI de agente instalado y autenticado; Docker si autoalojas servidor |

Se declara source-available con licencia Multica que añade condiciones a Apache; no debe resumirse como Apache puro ni como una garantía de sustituir empleados

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un CLI de agente instalado y autenticado
- Docker si autoalojas servidor

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/multica-ai/multica/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar multica para mi objetivo y necesito pasos guiados. Lee https://github.com/multica-ai/multica/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Asigna una tarea de explicación a un agente en un proyecto de prueba antes de crear automatizaciones.

**Qué comprobar:** Puedes ver tarea, sesión y resultado atribuibles al agente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar trabajo entre agentes
- Revisar entregas en un espacio compartido

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar trabajo entre agentes; Revisar entregas en un espacio compartido | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se declara source-available con licencia Multica que añade condiciones a Apache; no debe resumirse como Apache puro ni como una garantía de sustituir empleados

## Stack y modelos

- **Stack:** Un CLI de agente instalado y autenticado; Docker si autoalojas servidor
- **Etiquetas:** `agents` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [paperclip](paperclip.md) | 114k | Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. |

## Enlaces

- 🐙 GitHub: [multica-ai/multica](https://github.com/multica-ai/multica)
- 🌐 Web: <https://multica.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/multica-ai/multica/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
