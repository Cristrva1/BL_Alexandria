[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Automatización y pruebas por código

# 🎭 playwright

> Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 100k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 79/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Playwright, framework de automatización y pruebas web de Microsoft. Licencia Apache-2.0. Es maduro y estándar en la industria (~100k estrellas, v1.65.1).

## ¿Qué hace?

Controla Chromium, Firefox y WebKit con una sola API para pruebas end-to-end (Playwright Test), scripts de automatización y como herramienta para agentes (CLI y MCP).

## ¿Cómo lo hace?

Se instala con `npm init playwright@latest` (pruebas), `npm i playwright` (librería) o `npm i -g @playwright/cli@latest` (agentes). También tiene bindings para Python, .NET y Java.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Playwright MCP](playwright-mcp.md) | Servidor MCP oficial. | Añade el MCP al agente. |
| [playwright-cli](playwright-cli.md) | CLI con skills para agentes. | Instala la CLI global. |
| [Lightpanda](lightpanda.md) | Navegador headless alternativo vía CDP. | Conecta Playwright al CDP de Lightpanda. |
| [crawlee](crawlee.md) | Crawlee usa Playwright como uno de sus motores de navegador. | Instala crawlee junto con playwright. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (19). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ai-website-cloner-template](ai-website-cloner-template.md) · [Camoufox](camoufox.md) · [crawlee-python](crawlee-python.md) · [diagram-design](diagram-design.md) · [Gemini Computer Use (preview)](computer-use-preview.md) · [llm-scraper](llm-scraper.md) · [Locust](locust.md) · [mitmproxy](mitmproxy.md) · [OpenManus](openmanus.md) · [Scrapegraph-ai](scrapegraph-ai.md) · [scrapy](scrapy.md) · [screenshot-to-code](screenshot-to-code.md) · [Skyvern](skyvern.md) · [Slidev](slidev.md) · [Steel Browser](steel-browser.md) · [Storybook](storybook.md) · [Trigger.dev](trigger-dev.md) · [UI SDK (Vercel)](ui-sdk.md) · [ZAP (Zed Attack Proxy)](zaproxy.md)

**Notas:** Alternativas (elige una): puppeteer, selenium.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.65.1 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/playwright/blob/main/README.md) · [2](https://playwright.dev/)</sub>

## Ver similares

Grupo **Automatización de navegador y pruebas E2E**: playwright ocupa la posición 1 de 5 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **playwright** (esta ficha) ⭐ recomendado | 79 | Si empiezas hoy: pruebas E2E y automatización multi-navegador con la mejor experiencia. |
| 2 | [Puppeteer](puppeteer.md) | 72 | Si solo necesitas Chrome/Firefox desde Node.js para scraping o capturas. |
| 3 | [Cypress](cypress.md) | 65 | Si haces pruebas de componentes y E2E de frontend dentro del navegador. |
| 4 | [WebdriverIO](webdriverio.md) | 60 | Si quieres WebDriver y móvil (Appium) desde un mismo framework en Node.js. |
| 5 | [Selenium](selenium.md) | 60 | Si necesitas el estándar W3C WebDriver, muchos lenguajes o grids existentes. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Los tests y control básico no necesitan API de IA; agente y servicios de browser Cloud son independientes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor |
| Coste | Sin pago a un modelo en la ruta básica. Los tests y control básico no necesitan API de IA; agente y servicios de browser Cloud son independientes |
| Equipo | Preparación según la ruta elegida. Node; navegadores descargados; aplicación de prueba |

El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- navegadores descargados
- aplicación de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm i -D @playwright/test
npx playwright install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/playwright/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar playwright para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/playwright/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Escribe un test que abra una página local y compruebe un título.

**Qué comprobar:** Puedes distinguir fallo de aserción y fallo de arranque del navegador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un formulario
- Crear regresiones de una web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un formulario; Crear regresiones de una web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor

## Stack y modelos

- **Stack:** Node; navegadores descargados; aplicación de prueba
- **Etiquetas:** `automation` `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Puppeteer](puppeteer.md) | 95.8k | Librería de Google para controlar Chrome y Firefox desde Node.js. |
| [Selenium](selenium.md) | 34.6k | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. |
| [Cypress](cypress.md) | 51k | Framework de pruebas end-to-end y de componentes para todo lo que corre en un navegador, con ejecución interactiva, recarga en vivo y depuración paso a paso. |
| [WebdriverIO](webdriverio.md) | 9.9k | Framework de automatización de navegadores y apps móviles para Node.js basado en WebDriver, WebDriver BiDi y Appium, con servidor MCP para asistentes de IA. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright](https://github.com/microsoft/playwright)
- 🌐 Web: <https://playwright.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/playwright/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
