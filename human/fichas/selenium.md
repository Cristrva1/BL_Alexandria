[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Automatización y pruebas por código

# 🌐 Selenium

> Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.6k | Apache-2.0 | Java | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Selenium, proyecto paraguas de automatización de navegadores e infraestructura de la especificación W3C WebDriver, de SeleniumHQ. Licencia Apache-2.0. Es el veterano del sector (repo desde 2013, ~35k estrellas, 4.52).

## ¿Qué hace?

Controla todos los navegadores principales con WebDriver para pruebas y automatización, y escala con Selenium Grid.

## ¿Cómo lo hace?

Tiene bindings para Java, Python, C#, Ruby y JavaScript, y Selenium Manager gestiona los drivers automáticamente. El repo se construye con Bazel.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [mitmproxy](mitmproxy.md) | Inspección de tráfico en pruebas. (combinación por arquitectura) | Configura el proxy en el navegador. |
| [activepieces](activepieces.md) | Orquestar scripts de automatización. (combinación por arquitectura) | Lanza los scripts desde flujos de Activepieces. |
| [Claude Code](claude-code.md) | Generar y mantener pruebas. (combinación por arquitectura) | Pide al agente las pruebas WebDriver. |
| [FlareSolverr](flaresolverr.md) | Combinación recíproca: FlareSolverr lo enlaza como «FlareSolverr usa Selenium con undetected-chromedriver para controlar Chrome internamente». | Orden indicado desde FlareSolverr: Ejecuta FlareSolverr con Docker (incluye Selenium y Chrome); después llama a su API. |
| [Steel Browser](steel-browser.md) | Combinación recíproca: Steel Browser lo enlaza como «Steel crea sesiones compatibles con el protocolo WebDriver de Selenium con la opción `isSelenium`». | Orden indicado desde Steel Browser: Arranca Steel y crea la sesión con `isSelenium: true`; después conecta tu cliente de Selenium. |
| [Ladybird](ladybird.md) | Combinación recíproca: Ladybird lo enlaza como «Ladybird incluye un servicio WebDriver al que pueden conectarse clientes de Selenium para automatizar pruebas (combinación por arquitectura)». | Orden indicado desde Ladybird: Compila Ladybird con su servicio WebDriver; después conecta Selenium a ese endpoint. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Servo](servo.md)

**Notas:** Alternativas (elige una): playwright, puppeteer.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada selenium-4.52.0 (2026-10-29) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SeleniumHQ/selenium/blob/trunk/README.md) · [2](https://www.selenium.dev/documentation/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelos ni API de IA; infraestructura o servicios de pruebas Cloud se costean aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El README raíz está dirigido a contribuidores; para utilizar Selenium sigue el manual de usuario y no cambies políticas de Windows para compilar todo el proyecto |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelos ni API de IA; infraestructura o servicios de pruebas Cloud se costean aparte |
| Equipo | Preparación según la ruta elegida. Lenguaje y bindings elegidos; navegador compatible; app de prueba |

El README raíz está dirigido a contribuidores; para utilizar Selenium sigue el manual de usuario y no cambies políticas de Windows para compilar todo el proyecto

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Lenguaje y bindings elegidos
- navegador compatible
- app de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://selenium.dev/documentation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Selenium para mi objetivo y necesito pasos guiados. Lee https://selenium.dev/documentation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una página de prueba y verifica un elemento mediante WebDriver.

**Qué comprobar:** Puedes comprobar que la sesión controla el navegador correcto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar pruebas funcionales
- Comparar comportamiento entre navegadores

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar pruebas funcionales; Comparar comportamiento entre navegadores | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README raíz está dirigido a contribuidores; para utilizar Selenium sigue el manual de usuario y no cambies políticas de Windows para compilar todo el proyecto

## Stack y modelos

- **Stack:** Lenguaje y bindings elegidos; navegador compatible; app de prueba
- **Etiquetas:** `browser` `java` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [Puppeteer](puppeteer.md) | 95.8k | Librería de Google para controlar Chrome y Firefox desde Node.js. |
| [Cypress](cypress.md) | 51k | Framework de pruebas end-to-end y de componentes para todo lo que corre en un navegador, con ejecución interactiva, recarga en vivo y depuración paso a paso. |
| [WebdriverIO](webdriverio.md) | 9.9k | Framework de automatización de navegadores y apps móviles para Node.js basado en WebDriver, WebDriver BiDi y Appium, con servidor MCP para asistentes de IA. |

## Enlaces

- 🐙 GitHub: [SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium)
- 🌐 Web: <https://selenium.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SeleniumHQ/selenium/blob/trunk/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
