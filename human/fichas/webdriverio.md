[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Automatización y pruebas por código

# 📚 WebdriverIO

> Framework de automatización de navegadores y apps móviles para Node.js basado en WebDriver, WebDriver BiDi y Appium, con servidor MCP para asistentes de IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.9k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de código abierto (MIT) de la OpenJS Foundation, mantenido por la comunidad. Muy activo.

## ¿Qué hace?

Automatiza navegadores y apps móviles para pruebas end-to-end, unitarias y de componentes en el navegador, con soporte de Mocha, Jasmine y Cucumber, servicios (Appium, DevTools, nubes como Sauce Labs o BrowserStack), reporters y un servidor MCP (`@wdio/mcp`) para que asistentes de IA controlen navegadores y apps.

## ¿Cómo lo hace?

Paquetes Node.js en un monorepo: `webdriver` implementa los protocolos W3C WebDriver y WebDriver BiDi, `webdriverio` ofrece la API de alto nivel y `@wdio/cli` el test runner. Se configura con el asistente `create-wdio`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | El servidor MCP oficial `@wdio/mcp` permite a asistentes de IA automatizar navegadores y apps móviles con WebdriverIO. | Añade `@wdio/mcp` como servidor MCP del agente; después pide la automatización. |
| [Steel Browser](steel-browser.md) | Steel expone sesiones compatibles con el protocolo WebDriver a las que puede conectarse un cliente estándar como WebdriverIO (combinación por arquitectura). | Arranca Steel y crea una sesión con `isSelenium`; después apunta WebdriverIO a ese endpoint. |
| [Ladybird](ladybird.md) | Ladybird incluye un servicio WebDriver al que pueden conectarse clientes estándar como WebdriverIO para probar el motor (combinación por arquitectura). | Compila Ladybird con su servicio WebDriver; después configura WebdriverIO para conectarse a él. |
| [Servo](servo.md) | Servo incluye un servidor WebDriver al que pueden conectarse clientes estándar como WebdriverIO (combinación por arquitectura). | Arranca Servo con WebDriver activado; después conecta WebdriverIO a su puerto. |

**Notas:** Alternativa de Cypress, Playwright, Selenium y Puppeteer; destaca por usar protocolos estándar y cubrir apps móviles.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v10.2.0 (2026-11-06) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/webdriverio/webdriverio/blob/main/README.md) · [2](https://github.com/webdriverio/mcp) · [3](https://webdriver.io/docs/gettingstarted)</sub>

## Ver similares

Grupo **Automatización de navegador y pruebas E2E**: WebdriverIO ocupa la posición 4 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [playwright](playwright.md) ⭐ recomendado | 78 | Si empiezas hoy: pruebas E2E y automatización multi-navegador con la mejor experiencia. |
| 2 | [Puppeteer](puppeteer.md) | 72 | Si solo necesitas Chrome/Firefox desde Node.js para scraping o capturas. |
| 3 | [Cypress](cypress.md) | 65 | Si haces pruebas de componentes y E2E de frontend dentro del navegador. |
| 4 | **WebdriverIO** (esta ficha) | 60 | Si quieres WebDriver y móvil (Appium) desde un mismo framework en Node.js. |
| 5 | [Selenium](selenium.md) | 60 | Si necesitas el estándar W3C WebDriver, muchos lenguajes o grids existentes. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/webdriverio/webdriverio/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WebdriverIO para mi objetivo y necesito pasos guiados. Lee https://github.com/webdriverio/webdriverio/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un proyecto ejecuta el asistente `npm init wdio@latest .` y lanza la prueba de ejemplo..

**Qué comprobar:** Ves el navegador abrirse y la prueba pasar en la terminal..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- probar una web en varios navegadores reales con protocolos estándar
- automatizar pruebas de apps iOS y Android con Appium

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: probar una web en varios navegadores reales con protocolos estándar; automatizar pruebas de apps iOS y Android con Appium | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `testing` `e2e` `webdriver` `mobile`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Cypress](cypress.md) | 51k | Framework de pruebas end-to-end y de componentes para todo lo que corre en un navegador, con ejecución interactiva, recarga en vivo y depuración paso a paso. |
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [Selenium](selenium.md) | 34.6k | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. |
| [Puppeteer](puppeteer.md) | 95.8k | Librería de Google para controlar Chrome y Firefox desde Node.js. |

## Enlaces

- 🐙 GitHub: [webdriverio/webdriverio](https://github.com/webdriverio/webdriverio)
- 🌐 Web: <http://webdriver.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/webdriverio/webdriverio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
