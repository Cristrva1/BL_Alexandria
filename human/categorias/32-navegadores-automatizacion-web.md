[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Navegadores y automatización web

Navegadores, librerías de pruebas y agentes que interactúan con sitios web. Para leer páginas estáticas consulta extracción web; para operar una interfaz empieza por estas herramientas.

12 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Stagehand](../fichas/stagehand.md) | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | API de IA necesaria |

## Secciones

- [Automatización y pruebas por código](#automatización-y-pruebas-por-código) — 3 repos
- [Herramientas de navegación para agentes](#herramientas-de-navegación-para-agentes) — 6 repos
- [Navegadores y servidores de ejecución](#navegadores-y-servidores-de-ejecución) — 2 repos
- [Directorios y recursos de navegador](#directorios-y-recursos-de-navegador) — 1 repos

## Automatización y pruebas por código

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [playwright](../fichas/playwright.md) | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. | Tu objetivo encaja con estos ejemplos: Probar un formulario; Crear regresiones de una web | Sin clave propia de API de IA en la ruta básica |
| [Puppeteer](../fichas/puppeteer.md) | Librería de Google para controlar Chrome y Firefox desde Node.js. | Tu objetivo encaja con estos ejemplos: Automatizar una captura; Extraer datos de una página propia | Sin clave propia de API de IA en la ruta básica |
| [Selenium](../fichas/selenium.md) | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. | Tu objetivo encaja con estos ejemplos: Automatizar pruebas funcionales; Comparar comportamiento entre navegadores | Sin clave propia de API de IA en la ruta básica |

## Herramientas de navegación para agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Stagehand](../fichas/stagehand.md) | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | Tu objetivo encaja con estos ejemplos: Prototipar extracción estructurada; Automatizar un formulario de prueba | API de IA necesaria |
| [browser-use](../fichas/browser-use.md) | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. | Tu objetivo encaja con estos ejemplos: Extraer información de una web propia; Probar navegación con un agente | API de IA opcional |
| [agent-browser](../fichas/agent-browser.md) | CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. | Tu objetivo encaja con estos ejemplos: Verificar una interfaz; Preparar capturas y consultas de una página | Sin clave propia de API de IA en la ruta básica |
| [Skyvern](../fichas/skyvern.md) | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. | Tu objetivo encaja con estos ejemplos: Automatizar un flujo propio; Evaluar extracción basada en visión | API de IA opcional |
| [Browser Harness](../fichas/browser-harness.md) | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. | Tu objetivo encaja con estos ejemplos: Probar un agente con un browser propio; Inspeccionar una página autenticada de laboratorio | Sin clave propia de API de IA en la ruta básica |
| [playwright-cli](../fichas/playwright-cli.md) | Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. | Tu objetivo encaja con estos ejemplos: Probar un flujo con un agente; Registrar una secuencia de navegación | Sin clave propia de API de IA en la ruta básica |

## Navegadores y servidores de ejecución

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Lightpanda](../fichas/lightpanda.md) | Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome. | Tu objetivo encaja con estos ejemplos: Preparar navegación headless; Explorar un agente con modelo local | API de IA opcional |
| [camofox-browser](../fichas/camofox-browser.md) | Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes. | Tu objetivo encaja con estos ejemplos: Probar automatización de una web propia; Evaluar una herramienta de navegación para agentes | Sin clave propia de API de IA en la ruta básica |

## Directorios y recursos de navegador

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [awesome-chrome-devtools](../fichas/awesome-chrome-devtools.md) | Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol. | Tu objetivo encaja con estos ejemplos: Encontrar una herramienta de depuración; Explorar clientes de DevTools Protocol | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
