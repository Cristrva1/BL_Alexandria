[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Chrome DevTools MCP

> Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.3k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Chrome DevTools para agentes: servidor MCP y CLI del equipo de Chrome DevTools para controlar e inspeccionar un Chrome real. Licencia Apache-2.0. Es muy popular (~57k estrellas, v1.13.0).

## ¿Qué hace?

Permite a agentes como Antigravity, Claude, Cursor o Copilot automatizar el navegador, depurar (consola, red), analizar rendimiento con trazas e inspeccionar páginas en vivo. Expone el contenido del navegador al cliente MCP, así que no debe usarse con datos sensibles. Solo soporta oficialmente Google Chrome y Chrome for Testing.

## ¿Cómo lo hace?

Se añade con `npx -y chrome-devtools-mcp@latest`, como extensión de Gemini CLI o como plugin de otros agentes. Google recopila estadísticas de uso por defecto; se desactivan con `--no-usage-statistics` o con las variables `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` o `CI`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Depuración y automatización de Chrome desde el agente. | Registra el servidor MCP con `--no-usage-statistics` si no quieres telemetría. |
| [Gemini CLI](gemini-cli.md) | Instalación como extensión oficial de Gemini CLI. | Ejecuta `gemini extensions install` con la URL del repo. |
| [MCP Inspector](mcp-inspector.md) | Explorar las herramientas del servidor. (combinación por arquitectura) | Conecta el Inspector al servidor. |
| [Puppeteer](puppeteer.md) | Combinación recíproca: Puppeteer lo enlaza como «MCP para agentes basado en DevTools». | Orden indicado desde Puppeteer: Úsalo para depurar desde el agente. |
| [agent-browser](agent-browser.md) | Combinación recíproca: agent-browser lo enlaza como «Depuración profunda complementaria. (combinación por arquitectura)». | Orden indicado desde agent-browser: Úsalo para rendimiento y red. |
| [awesome-chrome-devtools](awesome-chrome-devtools.md) | Combinación recíproca: awesome-chrome-devtools lo enlaza como «MCP para agentes del mismo ecosistema. (combinación por arquitectura)». | Orden indicado desde awesome-chrome-devtools: Instálalo si usas agentes. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Front-End-Checklist](front-end-checklist.md)

**Notas:** Alternativas (elige una): playwright-mcp, browser-harness. Telemetría activada por defecto.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada chrome-devtools-mcp-v1.13.0 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md)</sub>

## Ver similares

Grupo **Servidores MCP de navegador**: Chrome DevTools MCP ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Chrome DevTools MCP** (esta ficha) ⭐ recomendado | 72 | Si buscas esto: servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. |
| 2 | [Playwright MCP](playwright-mcp.md) | 62 | Si buscas esto: servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La herramienta no incluye un modelo; consume el agente y el equipo; estadísticas de uso se habilitan por defecto |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. MCP y CLI con skill son rutas diferentes; la recogida de métricas tiene una opción de exclusión documentada |
| Coste | Consumo del agente que ya utilizas. La herramienta no incluye un modelo; consume el agente y el equipo; estadísticas de uso se habilitan por defecto |
| Equipo | Preparación según la ruta elegida. Node.js LTS; npm; Chrome estable; cliente MCP |

MCP y CLI con skill son rutas diferentes; la recogida de métricas tiene una opción de exclusión documentada

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js LTS
- npm
- Chrome estable
- cliente MCP

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Chrome DevTools MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre tu app local y pide revisar errores de consola y una petición de red.

**Qué comprobar:** El informe identifica el error y la petición que puedes reproducir.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diagnosticar una pantalla que falla
- Inspeccionar rendimiento de una página propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diagnosticar una pantalla que falla; Inspeccionar rendimiento de una página propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP y CLI con skill son rutas diferentes; la recogida de métricas tiene una opción de exclusión documentada

## Stack y modelos

- **Stack:** Node.js LTS; npm; Chrome estable; cliente MCP
- **Etiquetas:** `mcp` `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Playwright MCP](playwright-mcp.md) | 39.7k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |
| [Browser Harness](browser-harness.md) | 19.1k | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. |

## Enlaces

- 🐙 GitHub: [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- 🌐 Web: <https://developer.chrome.com/docs/devtools/agents>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
