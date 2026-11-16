[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Navegadores y automatización web

Navegadores, librerías de pruebas y agentes que interactúan con sitios web. Para leer páginas estáticas consulta extracción web; para operar una interfaz empieza por estas herramientas.

19 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Stagehand](../fichas/stagehand.md) | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | API de IA necesaria |
| [Lightpanda](../fichas/lightpanda.md) | Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome. | API de IA opcional |

## Secciones

- [Automatización y pruebas por código](#automatización-y-pruebas-por-código) — 6 repos
- [Herramientas de navegación para agentes](#herramientas-de-navegación-para-agentes) — 8 repos
- [Navegadores y servidores de ejecución](#navegadores-y-servidores-de-ejecución) — 4 repos
- [Directorios y recursos de navegador](#directorios-y-recursos-de-navegador) — 1 repos

## Automatización y pruebas por código

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [playwright](../fichas/playwright.md) | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. | Tu objetivo encaja con estos ejemplos: Probar un formulario; Crear regresiones de una web | Sin clave propia de API de IA en la ruta básica |
| [Puppeteer](../fichas/puppeteer.md) | Librería de Google para controlar Chrome y Firefox desde Node.js. | Tu objetivo encaja con estos ejemplos: Automatizar una captura; Extraer datos de una página propia | Sin clave propia de API de IA en la ruta básica |
| [Cypress](../fichas/cypress.md) | Framework de pruebas end-to-end y de componentes para todo lo que corre en un navegador, con ejecución interactiva, recarga en vivo y depuración paso a paso. | Tu objetivo encaja con estos ejemplos: probar los flujos críticos de una web (registro, compra) en cada cambio; probar componentes de React, Vue o Angular de forma aislada | Sin clave propia de API de IA en la ruta básica |
| [Selenium](../fichas/selenium.md) | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. | Tu objetivo encaja con estos ejemplos: Automatizar pruebas funcionales; Comparar comportamiento entre navegadores | Sin clave propia de API de IA en la ruta básica |
| [FlareSolverr](../fichas/flaresolverr.md) | Servidor proxy que abre páginas protegidas por Cloudflare o DDoS-GUARD en un Chrome automatizado y devuelve el HTML y las cookies para otros clientes HTTP. | Tu objetivo encaja con estos ejemplos: dar acceso a indexadores (como Prowlarr o Jackett) a sitios propios o autorizados detrás de Cloudflare; obtener cookies válidas para que un scraper autorizado continúe con un cliente HTTP ligero | Sin clave propia de API de IA en la ruta básica |
| [WebdriverIO](../fichas/webdriverio.md) | Framework de automatización de navegadores y apps móviles para Node.js basado en WebDriver, WebDriver BiDi y Appium, con servidor MCP para asistentes de IA. | Tu objetivo encaja con estos ejemplos: probar una web en varios navegadores reales con protocolos estándar; automatizar pruebas de apps iOS y Android con Appium | Sin clave propia de API de IA en la ruta básica |

## Herramientas de navegación para agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Stagehand](../fichas/stagehand.md) | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | Tu objetivo encaja con estos ejemplos: Prototipar extracción estructurada; Automatizar un formulario de prueba | API de IA necesaria |
| [browser-use](../fichas/browser-use.md) | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. | Tu objetivo encaja con estos ejemplos: Extraer información de una web propia; Probar navegación con un agente | API de IA opcional |
| [agent-browser](../fichas/agent-browser.md) | CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. | Tu objetivo encaja con estos ejemplos: Verificar una interfaz; Preparar capturas y consultas de una página | Sin clave propia de API de IA en la ruta básica |
| [Skyvern](../fichas/skyvern.md) | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. | Tu objetivo encaja con estos ejemplos: Automatizar un flujo propio; Evaluar extracción basada en visión | API de IA opcional |
| [Browser Harness](../fichas/browser-harness.md) | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. | Tu objetivo encaja con estos ejemplos: Probar un agente con un browser propio; Inspeccionar una página autenticada de laboratorio | Sin clave propia de API de IA en la ruta básica |
| [playwright-cli](../fichas/playwright-cli.md) | Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. | Tu objetivo encaja con estos ejemplos: Probar un flujo con un agente; Registrar una secuencia de navegación | Sin clave propia de API de IA en la ruta básica |
| [Nanobrowser](../fichas/nanobrowser.md) | Extensión de Chrome con un agente de IA que navega, hace clic y rellena formularios en tu propio navegador, con tu clave de API o un modelo local. | Tu objetivo encaja con estos ejemplos: automatizar tareas repetitivas en webs donde ya tienes la sesión iniciada; investigar y resumir información de varias páginas desde el panel lateral | API de IA opcional |
| [Steel Browser](../fichas/steel-browser.md) | API de navegador autoalojable para agentes y apps: sesiones de Chrome con cookies, proxies, extensiones y repetición, controlables por Puppeteer, Playwright o Selenium. | Tu objetivo encaja con estos ejemplos: dar a un agente de IA un navegador aislado y persistente sin montar infraestructura; extraer páginas o capturas mediante una API REST propia | Sin clave propia de API de IA en la ruta básica |

## Navegadores y servidores de ejecución

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Lightpanda](../fichas/lightpanda.md) | Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome. | Tu objetivo encaja con estos ejemplos: Preparar navegación headless; Explorar un agente con modelo local | API de IA opcional |
| [Ladybird](../fichas/ladybird.md) | Navegador web realmente independiente con motor propio (LibWeb y LibJS) basado en estándares, sin código de Chromium, WebKit ni Gecko; aún en pre-alfa. | Tu objetivo encaja con estos ejemplos: seguir o contribuir al desarrollo de un motor de navegador independiente; probar la compatibilidad de una web con un motor nuevo | Sin clave propia de API de IA en la ruta básica |
| [Servo](../fichas/servo.md) | Motor de navegador escrito en Rust, ligero y paralelo, pensado para incrustar tecnologías web en aplicaciones; prototipo de la Linux Foundation Europe. | Tu objetivo encaja con estos ejemplos: incrustar renderizado web en una aplicación Rust sin depender de Chromium; experimentar con un motor de navegador moderno y seguro en memoria | Sin clave propia de API de IA en la ruta básica |
| [Camoufox](../fichas/camoufox.md) | Navegador basado en Firefox para scraping y agentes que genera una identidad de dispositivo coherente en cada arranque y se controla con Playwright. | Tu objetivo encaja con estos ejemplos: automatizar navegación en sitios propios o autorizados que bloquean navegadores headless; probar cómo responde tu web a distintas huellas de navegador | Sin clave propia de API de IA en la ruta básica |

## Directorios y recursos de navegador

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [awesome-chrome-devtools](../fichas/awesome-chrome-devtools.md) | Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol. | Tu objetivo encaja con estos ejemplos: Encontrar una herramienta de depuración; Explorar clientes de DevTools Protocol | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
