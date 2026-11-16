[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🕸️ agent-desktop

> CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.8k | Apache-2.0 | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

agent-desktop, CLI y biblioteca de Vercel Labs para que un agente use apps de escritorio en macOS, Windows y Linux a través del árbol de accesibilidad del sistema. Licencia Apache-2.0. Tiene ~24k estrellas y está activo.

## ¿Qué hace?

Lee el árbol de accesibilidad de una app y lo devuelve como JSON, con una referencia para cada elemento accionable; así el agente actúa sin capturas de pantalla ni comparación de píxeles. Incluye sesiones, sandboxes y trazas. El README advierte que los snapshots pueden contener datos privados.

## ¿Cómo lo hace?

Se instala con `npm install -g agent-desktop` (con binarios nativos x64 y ARM64) o `brew install agent-desktop`. En macOS requiere el permiso de Accesibilidad. Se expone como servidor MCP (`agent-desktop mcp`) o como skill (`npx skills add …`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Instalable como skill o MCP. | Añade la skill o el servidor MCP. |
| [Codex CLI](codex.md) | Cliente MCP stdio. (combinación por arquitectura) | Añade `agent-desktop mcp` a la configuración. |
| [Playwright MCP](playwright-mcp.md) | Complemento para la parte web. (combinación por arquitectura) | Usa Playwright MCP en el navegador y agent-desktop en apps nativas. |

**Notas:** Sin alternativas declaradas; enfoque complementario al de computer-use-preview (accesibilidad frente a píxeles).

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.3.1 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vercel-labs/agent-desktop/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El CLI y MCP no necesitan un LLM propio; el agente que los controle usa su modelo o plan |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Ofrece skills portables y MCP stdio; algunas órdenes de teclas o botones mantenidos se rechazan hasta disponer de daemon de liberación |
| Coste | Sin pago a un modelo en la ruta básica. El CLI y MCP no necesitan un LLM propio; el agente que los controle usa su modelo o plan |
| Equipo | Preparación según la ruta elegida. Node; permisos de accesibilidad del sistema; cliente de agente opcional |

Ofrece skills portables y MCP stdio; algunas órdenes de teclas o botones mantenidos se rechazan hasta disponer de daemon de liberación

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- permisos de accesibilidad del sistema
- cliente de agente opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install -g agent-desktop
agent-desktop status                # platform, permissions, supported surfaces
agent-desktop permissions --guide   # macOS: walks you through the Accessibility grant
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/vercel-labs/agent-desktop/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar agent-desktop para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel-labs/agent-desktop/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta status y permissions --guide y obtén una captura de una ventana de prueba sin pulsar controles.

**Qué comprobar:** Puedes comprobar plataforma, permisos y referencias de accesibilidad.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Inspeccionar una app de escritorio propia
- Preparar una prueba de interfaz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Inspeccionar una app de escritorio propia; Preparar una prueba de interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ofrece skills portables y MCP stdio; algunas órdenes de teclas o botones mantenidos se rechazan hasta disponer de daemon de liberación

## Stack y modelos

- **Stack:** Node; permisos de accesibilidad del sistema; cliente de agente opcional
- **Etiquetas:** `infra` `accessibility` `accessibility-api` `ai-agents` `automation` `cli` `computer-use` `computer-use-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)
- 🌐 Web: <https://agent-browser.dev/desktop>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vercel-labs/agent-desktop/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
