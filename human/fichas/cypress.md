[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Automatización y pruebas por código

# 📚 Cypress

> Framework de pruebas end-to-end y de componentes para todo lo que corre en un navegador, con ejecución interactiva, recarga en vivo y depuración paso a paso.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Framework de pruebas de código abierto (MIT) de Cypress.io, uno de los más usados en pruebas de front-end. Muy activo. La empresa ofrece Cypress Cloud como servicio comercial.

## ¿Qué hace?

Ejecuta pruebas end-to-end y de componentes en Chrome, Edge, Electron, Firefox y WebKit (experimental), con viaje en el tiempo por los pasos, esperas automáticas, intercepción de red, capturas, grabación de vídeo y depuración con las herramientas del navegador. Incluye funciones de IA como Cypress Studio y `cy.prompt`.

## ¿Cómo lo hace?

Se instala como dependencia de desarrollo con npm, yarn o pnpm; la app de escritorio (Electron) lanza el navegador y ejecuta las pruebas en el mismo bucle que la aplicación. Graba vídeos con FFmpeg incluido. Cypress Cloud recibe resultados si conectas el proyecto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Storybook](storybook.md) | La documentación de Storybook explica cómo reutilizar historias de componentes en pruebas end-to-end con Cypress. | Publica o arranca Storybook; después visita las historias desde las pruebas de Cypress. |
| [Claude Code](claude-code.md) | Cypress Cloud MCP y el plugin `cypress` (con las Cypress AI Skills) dan a Claude Code acceso a los resultados de las pruebas; requiere cuenta de Cypress Cloud. | Conecta el proyecto a Cypress Cloud; después instala el plugin `cypress` en Claude Code. |
| [FFmpeg](ffmpeg.md) | Cypress graba vídeos de las ejecuciones con FFmpeg, que incluye como dependencia. | No requiere instalación aparte; activa `video: true` en la configuración. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v16.3.0 (2026-11-10) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cypress-io/cypress/blob/develop/README.md) · [2](https://storybook.js.org/docs/writing-tests/integrations/stories-in-end-to-end-tests) · [3](https://docs.cypress.io/cloud/integrations/cloud-mcp) · [4](https://github.com/cypress-io/cypress/blob/develop/packages/server/package.json)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
npm install cypress --save-dev
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/cypress-io/cypress/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Cypress para mi objetivo y necesito pasos guiados. Lee https://github.com/cypress-io/cypress/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un proyecto web ejecuta `npm install cypress --save-dev` y `npx cypress open`; crea una prueba de ejemplo..

**Qué comprobar:** Ves la prueba ejecutándose paso a paso en el navegador..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- probar los flujos críticos de una web (registro, compra) en cada cambio
- probar componentes de React, Vue o Angular de forma aislada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: probar los flujos críticos de una web (registro, compra) en cada cambio; probar componentes de React, Vue o Angular de forma aislada | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Cypress es MIT; Cypress Cloud (grabación, paralelización, Test Replay, Cloud MCP) es un servicio con planes de pago.

## Stack y modelos

- **Stack:** TypeScript, docker-compose.yml, package.json
- **Etiquetas:** `testing` `e2e` `javascript` `browser`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [WebdriverIO](webdriverio.md) | 9.9k | Framework de automatización de navegadores y apps móviles para Node.js basado en WebDriver, WebDriver BiDi y Appium, con servidor MCP para asistentes de IA. |
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [Selenium](selenium.md) | 34.6k | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. |
| [Puppeteer](puppeteer.md) | 95.8k | Librería de Google para controlar Chrome y Firefox desde Node.js. |

## Enlaces

- 🐙 GitHub: [cypress-io/cypress](https://github.com/cypress-io/cypress)
- 🌐 Web: <https://cypress.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cypress-io/cypress/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
