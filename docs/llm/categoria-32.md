# Alexandría para agentes · Navegadores y automatización web

Categoría 32 completa (20 repos, 4 subcategorías). Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=32 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `playwright` | bibliotecas | Framework de Microsoft para automatización y testing de navegadores Chromium… | 2 Intermedio | 78 | Apache-2.0 (OSI permisiva) | recomendado |
| `puppeteer` | bibliotecas | Librería de Google para controlar Chrome y Firefox desde Node.js. | 2 Intermedio | 72 | Apache-2.0 (OSI permisiva) | alternativa |
| `cypress` | bibliotecas | Framework de pruebas end-to-end y de componentes para todo lo que corre en un… | 2 Intermedio | 65 | MIT (OSI permisiva) | alternativa |
| `selenium` | bibliotecas | Framework veterano de automatización de navegadores con soporte para casi todos… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `webdriverio` | bibliotecas | Framework de automatización de navegadores y apps móviles para Node.js basado… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `flaresolverr` | bibliotecas | Servidor proxy que abre páginas protegidas por Cloudflare o DDoS-GUARD en un… | 1 Básico | 58 | MIT (OSI permisiva) | sin grupo |
| `browser-use` | agentes-web | Librería Python para que los LLM usen un navegador real y actúen en páginas sin… | 2 Intermedio | 73 | MIT (OSI permisiva) | recomendado |
| `agent-browser` | agentes-web | CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias… | 1 Básico | 63 | Apache-2.0 (OSI permisiva) | recomendado |
| `stagehand` | agentes-web | SDK de Browserbase para automatizar el navegador mezclando código con acciones… | 2 Intermedio | 61 | MIT (OSI permisiva) | alternativa |
| `browser-harness` | agentes-web | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu… | 1 Básico | 60 | MIT (OSI permisiva) | alternativa |
| `skyvern` | agentes-web | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. | 2 Intermedio | 60 | AGPL-3.0 (OSI copyleft) | alternativa |
| `nanobrowser` | agentes-web | Extensión de Chrome con un agente de IA que navega, hace clic y rellena… | 1 Básico | 59 | Apache-2.0 (OSI permisiva) | sin grupo |
| `playwright-cli` | agentes-web | Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les… | 1 Básico | 57 | Apache-2.0 (OSI permisiva) | alternativa |
| `steel-browser` | agentes-web | API de navegador autoalojable para agentes y apps: sesiones de Chrome con… | 2 Intermedio | 56 | Apache-2.0 (OSI permisiva) | sin grupo |
| `ladybird` | motores-web | Navegador web realmente independiente con motor propio (LibWeb y LibJS) basado… | 4 Experto | 72 | BSD-2-Clause (OSI permisiva) | recomendado |
| `lightpanda` | motores-web | Navegador headless escrito en Zig para IA y automatización, mucho más ligero… | 1 Básico | 70 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `servo` | motores-web | Motor de navegador escrito en Rust, ligero y paralelo, pensado para incrustar… | 4 Experto | 58 | MPL-2.0 (OSI copyleft) | alternativa |
| `camoufox` | motores-web | Navegador basado en Firefox para scraping y agentes que genera una identidad de… | 2 Intermedio | 48 | MPL-2.0 (navegador) y MIT (paquetes de Python) (OSI copyleft) | sin grupo |
| `kitesurf` | motores-web | Explora un motor experimental para renderizar páginas en Workers y obtener… | 3 Avanzado | — | Apache-2.0 | sin grupo |
| `awesome-chrome-devtools` | recursos-web | Directorio de herramientas, clientes y recursos del ecosistema de Chrome… | 1 Básico | 43 | CC0-1.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### playwright (`playwright`)

- **Repo:** https://github.com/microsoft/playwright · Apache-2.0 · nivel 2 · 78/100 · recomendado en «Automatización de navegador y pruebas E2E»
- **Qué es:** Playwright, framework de automatización y pruebas web de Microsoft. Licencia Apache-2.0. Es maduro y estándar en la industria (~100k estrellas, v1.65.1).
- **Cuándo elegirlo:** Casos: Probar un formulario; Crear regresiones de una web.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node; navegadores descargados; aplicación de prueba; hardware prerequisites; API de IA: no; Node; navegadores descargados; aplicación de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/microsoft/playwright/blob/main/README.md

  ```bash
  npm i -D @playwright/test
  npx playwright install
  ```
- **Primera prueba propuesta (no ejecutada):** Escribe un test que abra una página local y compruebe un título Éxito: Puedes distinguir fallo de aserción y fallo de arranque del navegador
- **Combina con:** `playwright-mcp` [5/servidores], `playwright-cli` [32/agentes-web], `lightpanda` [32/motores-web], `crawlee` [4/crawlers]
- **Alternativas:** `puppeteer`, `cypress`, `webdriverio`, `selenium`
- **Riesgos y avisos:** Alternativas (elige una): puppeteer, selenium. El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor.

### Puppeteer (`puppeteer`)

- **Repo:** https://github.com/puppeteer/puppeteer · Apache-2.0 · nivel 2 · 72/100 · alternativa en «Automatización de navegador y pruebas E2E»
- **Qué es:** Puppeteer, librería JavaScript para controlar Chrome o Firefox mediante el protocolo DevTools o WebDriver BiDi, mantenida por el equipo de Chrome. Licencia Apache-2.0. Es madura (~96k estrellas).
- **Cuándo elegirlo:** Casos: Automatizar una captura; Extraer datos de una página propia.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node; Chrome compatible o navegador propio con puppeteer-core; página de prueba; hardware prerequisites; API de IA: no; Node; Chrome compatible o navegador propio con puppeteer-core; página de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i puppeteer # Downloads compatible Chrome during installation.` — fuente: https://github.com/puppeteer/puppeteer/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre una página de prueba y consulta su título o captura antes de añadir interacciones Éxito: Puedes comprobar navegador y salida obtenida
- **Combina con:** `lightpanda` [32/motores-web], `chrome-devtools-mcp` [5/servidores], `awesome-chrome-devtools` [32/recursos-web], `nanobrowser` [32/agentes-web], `steel-browser` [32/agentes-web]
- **Alternativas:** `playwright`, `cypress`, `webdriverio`, `selenium`
- **Riesgos y avisos:** Alternativas (elige una): playwright, selenium. Puppeteer descarga Chrome y puppeteer-core no; el MCP recomendado es chrome-devtools-mcp, un proyecto compañero que se configura aparte.

### Cypress (`cypress`)

- **Repo:** https://github.com/cypress-io/cypress · MIT · nivel 2 · 65/100 · alternativa en «Automatización de navegador y pruebas E2E»
- **Qué es:** Framework de pruebas de código abierto (MIT) de Cypress.io, uno de los más usados en pruebas de front-end. Muy activo. La empresa ofrece Cypress Cloud como servicio comercial.
- **Cuándo elegirlo:** Casos: probar los flujos críticos de una web (registro, compra) en cada cambio; probar componentes de React, Vue o Angular de forma aislada.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, docker-compose.yml, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install cypress --save-dev` — fuente: https://github.com/cypress-io/cypress/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** En un proyecto web ejecuta `npm install cypress --save-dev` y `npx cypress open`; crea una prueba de ejemplo. Éxito: Ves la prueba ejecutándose paso a paso en el navegador.
- **Combina con:** `storybook` [9/componentes], `claude-code` [20/terminal], `ffmpeg` [12/edicion]
- **Alternativas:** `playwright`, `puppeteer`, `webdriverio`, `selenium`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### Selenium (`selenium`)

- **Repo:** https://github.com/SeleniumHQ/selenium · Apache-2.0 · nivel 2 · 60/100 · alternativa en «Automatización de navegador y pruebas E2E»
- **Qué es:** Selenium, proyecto paraguas de automatización de navegadores e infraestructura de la especificación W3C WebDriver, de SeleniumHQ. Licencia Apache-2.0. Es el veterano del sector (repo desde 2013, ~35k estrellas, 4.52).
- **Cuándo elegirlo:** Casos: Automatizar pruebas funcionales; Comparar comportamiento entre navegadores.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Lenguaje y bindings elegidos; navegador compatible; app de prueba; hardware prerequisites; API de IA: no; Lenguaje y bindings elegidos; navegador compatible; app de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://selenium.dev/documentation/
- **Primera prueba propuesta (no ejecutada):** Abre una página de prueba y verifica un elemento mediante WebDriver Éxito: Puedes comprobar que la sesión controla el navegador correcto
- **Combina con:** `mitmproxy` [16/pruebas], `activepieces` [1/motores], `claude-code` [20/terminal], `flaresolverr`, `steel-browser` [32/agentes-web], `ladybird` [32/motores-web]
- **Alternativas:** `playwright`, `puppeteer`, `cypress`, `webdriverio`
- **Riesgos y avisos:** Alternativas (elige una): playwright, puppeteer. El README raíz está dirigido a contribuidores; para utilizar Selenium sigue el manual de usuario y no cambies políticas de Windows para compilar todo el….

### WebdriverIO (`webdriverio`)

- **Repo:** https://github.com/webdriverio/webdriverio · MIT · nivel 2 · 60/100 · alternativa en «Automatización de navegador y pruebas E2E»
- **Qué es:** Proyecto de código abierto (MIT) de la OpenJS Foundation, mantenido por la comunidad. Muy activo.
- **Cuándo elegirlo:** Casos: probar una web en varios navegadores reales con protocolos estándar; automatizar pruebas de apps iOS y Android con Appium.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/webdriverio/webdriverio/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En un proyecto ejecuta el asistente `npm init wdio@latest .` y lanza la prueba de ejemplo. Éxito: Ves el navegador abrirse y la prueba pasar en la terminal.
- **Combina con:** `claude-code` [20/terminal], `steel-browser` [32/agentes-web], `ladybird` [32/motores-web], `servo` [32/motores-web]
- **Alternativas:** `playwright`, `puppeteer`, `cypress`, `selenium`
- **Riesgos y avisos:** Alternativa de Cypress, Playwright, Selenium y Puppeteer; destaca por usar protocolos estándar y cubrir apps móviles.

### FlareSolverr (`flaresolverr`)

- **Repo:** https://github.com/FlareSolverr/FlareSolverr · MIT · nivel 1 · 58/100
- **Qué es:** Servidor de código abierto (MIT) mantenido por la comunidad (ngosang y colaboradores), muy usado junto a indexadores multimedia. Activo, aunque depende de que Cloudflare no cambie sus desafíos.
- **Cuándo elegirlo:** Casos: dar acceso a indexadores (como Prowlarr o Jackett) a sitios propios o autorizados detrás de Cloudflare; obtener cookies válidas para que un scraper autorizado continúe con un cliente HTTP….
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, docker-compose.yml, package.json, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d --name=flaresolverr -p 127.0.0.1:8191:8191 -e LOG_LEVEL=info --restart unless-stopped ghcr.io/flaresolverr/flaresolverr:latest` — fuente: https://github.com/FlareSolverr/FlareSolverr/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el contenedor con Docker y envía un POST a `http://localhost:8191/v1` con `cmd: request.get` y una URL autorizada. Éxito: Obtienes el HTML de la página y las cookies de la sesión.
- **Combina con:** `selenium`, `scrapy` [4/crawlers], `crawlee-python` [4/crawlers]

### browser-use (`browser-use`)

- **Repo:** https://github.com/browser-use/browser-use · MIT · nivel 2 · 73/100 · recomendado en «Agentes que navegan la web»
- **Qué es:** Browser Use, agente de navegador open source de browser-use. La librería Python es MIT; la inferencia y los navegadores alojados son de pago. Es muy popular (~121k estrellas, v1.0.6).
- **Cuándo elegirlo:** Casos: Extraer información de una web propia; Probar navegación con un agente.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python y uv; Chrome o browser Cloud; agente o proveedor; perfil de prueba; hardware prerequisites; API de IA: opcional; Python y uv; Chrome o browser Cloud; agente o proveedor; perfil de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add 'browser-use==1.0.6'` — fuente: https://github.com/browser-use/browser-use/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un navegador de prueba y solicita leer una página sin enviar formularios ni usar cuentas personales Éxito: Puedes revisar pestaña, contexto y resultado
- **Combina con:** `claude-code` [20/terminal], `ollama` [8/motores], `pydantic-ai` [3/py], `sandbox` [22/infra], `openmanus` [3/py], `steel-browser`
- **Alternativas:** `stagehand`, `skyvern`, `browser-harness`, `computer-use-preview`, `playwright-mcp`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): computer-use-preview, stagehand, skyvern, playwright-mcp, browser-harness. La versión actual integra browser-harness y registra skills para Claude/Codex y MCP; una sesión con cookies puede actuar con los permisos de esa cuenta.

### agent-browser (`agent-browser`)

- **Repo:** https://github.com/vercel-labs/agent-browser · Apache-2.0 · nivel 1 · 63/100 · recomendado en «CLIs de navegador para agentes»
- **Qué es:** agent-browser, CLI nativa en Rust para que agentes controlen un navegador comando a comando, de Vercel Labs. Licencia Apache-2.0. Creado en enero de 2026, tiene ~52k estrellas (v0.43.0).
- **Cuándo elegirlo:** Casos: Verificar una interfaz; Preparar capturas y consultas de una página.
- **Requisitos:** nivel 1: preparación sencilla; Node; Chrome for Testing o navegador configurado; agente opcional; hardware prerequisites; API de IA: no; Node; Chrome for Testing o navegador configurado; agente opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/vercel-labs/agent-browser/blob/main/README.md

  ```bash
  npm install -g agent-browser
  agent-browser install           # download Chrome for Testing (first time only)
  ```
- **Primera prueba propuesta (no ejecutada):** Abre una página propia y consulta el árbol de accesibilidad antes de actuar Éxito: Puedes identificar referencias de elementos y cambios tras una acción
- **Combina con:** `claude-code` [20/terminal], `lightpanda` [32/motores-web], `chrome-devtools-mcp` [5/servidores]
- **Alternativas:** `playwright-cli`
- **Riesgos y avisos:** Alternativas (elige una): playwright-cli. Incluye skill portable y MCP stdio; descargar el browser es un paso separado y el perfil de pruebas evita mezclar sesiones personales.

### Stagehand (`stagehand`)

- **Repo:** https://github.com/browserbase/stagehand · MIT · nivel 2 · 61/100 · alternativa en «Agentes que navegan la web»
- **Qué es:** Stagehand, SDK para agentes de navegador de Browserbase. Licencia MIT. Es maduro y activo (~26k estrellas, v3.x).
- **Cuándo elegirlo:** Casos: Prototipar extracción estructurada; Automatizar un formulario de prueba.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él, requiere clave de API; Node o Python; modelo y navegador según ruta; clave Browserbase para MCP hospedado; sitio de prueba; hardware prerequisites; API de IA: sí; Node o Python; modelo y navegador según ruta; clave Browserbase para MCP hospedado; sitio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pnpm add @browserbasehq/stagehand 'zod@~4.4.3'` — fuente: https://github.com/browserbase/stagehand/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Extrae dos campos de una página propia y contrasta la estructura con el contenido visible Éxito: Puedes comprobar datos y acciones del navegador
- **Combina con:** `claude-code` [20/terminal], `lightpanda` [32/motores-web], `firecrawl` [4/crawlers], `steel-browser`
- **Alternativas:** `browser-use`, `skyvern`, `browser-harness`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): browser-use, skyvern. La nube de Browserbase es de pago. El MCP remoto documentado necesita cuenta y clave Browserbase; usar Claude Code o Codex para programar no aporta créditos de navegación.

### Browser Harness (`browser-harness`)

- **Repo:** https://github.com/browser-use/browser-harness · MIT · nivel 1 · 60/100 · alternativa en «Agentes que navegan la web»
- **Qué es:** Browser Harness, harness con el que Claude Code, Codex o Cursor usan tu Chrome real con tu sesión iniciada, de browser-use. Licencia MIT. Creado en abril de 2026 (~19k estrellas, v0.1.13); ahora es el motor de Browser Use y se recomienda…
- **Cuándo elegirlo:** Casos: Probar un agente con un browser propio; Inspeccionar una página autenticada de laboratorio.
- **Requisitos:** nivel 1: preparación sencilla; Browser Use CLI actual; Chrome y perfil de prueba; cliente agente; hardware prerequisites; API de IA: no; Browser Use CLI actual; Chrome y perfil de prueba; cliente agente.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/browser-use/browser-harness/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un perfil de prueba y solicita solo leer el título de una página Éxito: Puedes identificar qué navegador y sesión expone al agente
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal]
- **Alternativas:** `browser-use`, `stagehand`, `skyvern`, `playwright-mcp`, `chrome-devtools-mcp`
- **Riesgos y avisos:** Alternativas (elige una): playwright-mcp, chrome-devtools-mcp, browser-use. Riesgo: acceso del agente a sesiones autenticadas. Ahora es el motor de Browser Use y el README recomienda su CLI; conectar una sesión autenticada concede acceso a lo que esa sesión puede hacer.

### Skyvern (`skyvern`)

- **Repo:** https://github.com/Skyvern-AI/skyvern · AGPL-3.0 · nivel 2 · 60/100 · alternativa en «Agentes que navegan la web»
- **Qué es:** Skyvern, automatización de flujos web con LLMs y visión por computador, de Skyvern-AI. Licencia AGPL-3.0, con versión cloud gestionada. Tiene ~23k estrellas (v1.0.58).
- **Cuándo elegirlo:** Casos: Automatizar un flujo propio; Evaluar extracción basada en visión.
- **Requisitos:** nivel 2: preparación media; Python; browser; proveedor o modelo local Ollama; flujo de prueba; hardware prerequisites; API de IA: opcional; Python; browser; proveedor o modelo local Ollama; flujo de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "skyvern[server]"` — fuente: https://github.com/Skyvern-AI/skyvern/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Define una tarea de lectura de página y revisa acciones y extracción antes de permitir envíos Éxito: Puedes contrastar los pasos con la web
- **Combina con:** `playwright` [32/bibliotecas], `ollama` [8/motores], `activepieces` [1/motores]
- **Alternativas:** `browser-use`, `stagehand`, `browser-harness`, `computer-use-preview`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): browser-use, stagehand, computer-use-preview. Telemetría activa por defecto. Usa LLM y visión; evitar selectores frágiles no garantiza funcionar sin errores en todos los sitios.

### Nanobrowser (`nanobrowser`)

- **Repo:** https://github.com/nanobrowser/nanobrowser · Apache-2.0 · nivel 1 · 59/100
- **Qué es:** Extensión de código abierto (Apache-2.0), gratuita y alternativa abierta a agentes web comerciales. Muy activa.
- **Cuándo elegirlo:** Casos: automatizar tareas repetitivas en webs donde ya tienes la sesión iniciada; investigar y resumir información de varias páginas desde el panel lateral. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; TypeScript, package.json; hardware model_dependent; API de IA: opcional; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/nanobrowser/nanobrowser.git` — fuente: https://github.com/nanobrowser/nanobrowser/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Nanobrowser desde la Chrome Web Store, configura una clave de API o Ollama y pide una tarea sencilla en el panel lateral. Éxito: El agente abre las páginas y realiza la tarea en una pestaña propia.
- **Combina con:** `ollama` [8/motores], `llama-cpp` [8/motores], `vllm` [23/serving], `puppeteer` [32/bibliotecas]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Con modelos locales, el README recomienda tareas simples y un contexto de 16k tokens o más.

### playwright-cli (`playwright-cli`)

- **Repo:** https://github.com/microsoft/playwright-cli · Apache-2.0 · nivel 1 · 57/100 · alternativa en «CLIs de navegador para agentes»
- **Qué es:** Playwright CLI, CLI de Playwright con skills para agentes de código, de Microsoft. Licencia Apache-2.0. Tiene ~15k estrellas (v0.1.x).
- **Cuándo elegirlo:** Casos: Probar un flujo con un agente; Registrar una secuencia de navegación.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Node; navegador; agente con shell; aplicación de prueba; hardware prerequisites; API de IA: no; Node; navegador; agente con shell; aplicación de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/microsoft/playwright-cli/blob/main/README.md

  ```bash
  npm install -g @playwright/cli@latest
  playwright-cli --help
  ```
- **Primera prueba propuesta (no ejecutada):** Instala sus skills y abre una página de prueba para obtener snapshot antes de pulsar un control Éxito: Puedes usar referencias del snapshot y comprobar el resultado
- **Combina con:** `playwright` [32/bibliotecas], `claude-code` [20/terminal], `playwright-mcp` [5/servidores]
- **Alternativas:** `agent-browser`
- **Riesgos y avisos:** Alternativas (elige una): agent-browser. Los hosts compatibles pueden leer las skills instaladas; control por CLI y MCP son superficies distintas y las sesiones deben separarse al trabajar en paralelo.

### Steel Browser (`steel-browser`)

- **Repo:** https://github.com/steel-dev/steel-browser · Apache-2.0 · nivel 2 · 56/100
- **Qué es:** Proyecto de código abierto (Apache-2.0) de Steel, la base autoalojable de su servicio comercial Steel Cloud. Muy activo.
- **Cuándo elegirlo:** Casos: dar a un agente de IA un navegador aislado y persistente sin montar infraestructura; extraer páginas o capturas mediante una API REST propia.
- **Requisitos:** nivel 2: preparación media; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 3000:3000 -p 9223:9223 ghcr.io/steel-dev/steel-browser` — fuente: https://github.com/steel-dev/steel-browser/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el contenedor con Docker y abre la interfaz en `http://localhost:3000/ui` o llama a la API en el puerto 3000. Éxito: Puedes crear una sesión y conectar Puppeteer o Playwright a ella.
- **Combina con:** `puppeteer` [32/bibliotecas], `playwright` [32/bibliotecas], `selenium` [32/bibliotecas], `browser-use`, `stagehand`, `webdriverio` [32/bibliotecas]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### Ladybird (`ladybird`)

- **Repo:** https://github.com/LadybirdBrowser/ladybird · BSD-2-Clause · nivel 4 · 72/100 · recomendado en «Motores de navegador independientes»
- **Qué es:** Navegador de código abierto (BSD-2-Clause) desarrollado por Ladybird Browser Initiative, organización sin ánimo de lucro, a partir de componentes de SerenityOS. Muy popular y activo; está en pre-alfa.
- **Cuándo elegirlo:** Casos: seguir o contribuir al desarrollo de un motor de navegador independiente; probar la compatibilidad de una web con un motor nuevo.
- **Requisitos:** nivel 4: preparación difícil; Rust, CMakeLists.txt, Cargo.toml, pyproject.toml, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/LadybirdBrowser/ladybird/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de compilación (`Documentation/BuildInstructionsLadybird.md`) en Linux o macOS y ejecuta el navegador. Éxito: Abres páginas con un motor independiente, todavía con fallos.
- **Combina con:** `selenium` [32/bibliotecas], `webdriverio` [32/bibliotecas], `ffmpeg` [12/edicion]
- **Alternativas:** `servo`
- **Riesgos y avisos:** Alternativa de Servo como motor de navegador independiente.

### Lightpanda (`lightpanda`)

- **Repo:** https://github.com/lightpanda-io/browser · AGPL-3.0 · nivel 1 · 70/100
- **Qué es:** Lightpanda, navegador headless escrito desde cero en Zig para agentes de IA y automatización; no es un fork de Chromium ni de WebKit. Licencia AGPL-3.0. Tiene ~42k estrellas (v1.0.4).
- **Cuándo elegirlo:** Casos: Preparar navegación headless; Explorar un agente con modelo local.
- **Requisitos:** nivel 1: preparación sencilla; Binario compatible o Docker; agente o proveedor opcional; sitio de prueba; hardware prerequisites; API de IA: opcional; Binario compatible o Docker; agente o proveedor opcional; sitio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install lightpanda-io/browser/lightpanda` — fuente: https://github.com/lightpanda-io/browser/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una consulta simple sin LLM y compara el DOM con la página esperada Éxito: Puedes identificar la sesión y el resultado antes de probar autonomía
- **Combina con:** `puppeteer` [32/bibliotecas], `playwright` [32/bibliotecas], `stagehand` [32/agentes-web], `agent-browser` [32/agentes-web], `awesome-chrome-devtools` [32/recursos-web]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. La cobertura de APIs web aún es menor que la de Chromium. Telemetría activa por defecto. Ofrece MCP stdio y HTTP; su compatibilidad con páginas no es idéntica a un navegador completo y menor consumo no garantiza funcionar en toda web.

### Servo (`servo`)

- **Repo:** https://github.com/servo/servo · MPL-2.0 · nivel 4 · 58/100 · alternativa en «Motores de navegador independientes»
- **Qué es:** Motor de navegador de código abierto (MPL-2.0) iniciado por Mozilla y alojado ahora en Linux Foundation Europe. Muy activo; sigue considerándose un prototipo. Su política prohíbe contribuciones generadas con modelos de lenguaje.
- **Cuándo elegirlo:** Casos: incrustar renderizado web en una aplicación Rust sin depender de Chromium; experimentar con un motor de navegador moderno y seguro en memoria. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 4: preparación difícil, necesita GPU; Rust, Cargo.toml, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/servo/servo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Rust y las dependencias del sistema según el README y ejecuta `./mach build` y `./mach run https://servo.org`. Éxito: Abres una web con el navegador de demostración de Servo.
- **Combina con:** `selenium` [32/bibliotecas], `webdriverio` [32/bibliotecas], `mitmproxy` [16/pruebas]
- **Alternativas:** `ladybird`
- **Riesgos y avisos:** Alternativa de Ladybird como motor independiente; Servo se orienta más a incrustar que a ser un navegador completo.

### Camoufox (`camoufox`)

- **Repo:** https://github.com/daijro/camoufox · MPL-2.0 (navegador) y MIT (paquetes de Python) · nivel 2 · 48/100
- **Qué es:** Navegador antidetección de código abierto creado por daijro. El navegador es MPL-2.0 y los paquetes de lanzamiento de Python son MIT. Muy activo; el propio README avisa de que está en desarrollo.
- **Cuándo elegirlo:** Casos: automatizar navegación en sitios propios o autorizados que bloquean navegadores headless; probar cómo responde tu web a distintas huellas de navegador.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; C; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U "camoufox[geoip]"` — fuente: https://github.com/daijro/camoufox/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install -U "camoufox[geoip]"`, descarga el navegador con su comando `fetch` y abre una página con el ejemplo del README. Éxito: Obtienes un objeto `Browser` de Playwright normal controlando Camoufox.
- **Combina con:** `playwright` [32/bibliotecas], `crawlee-python` [4/crawlers], `crawlee` [4/crawlers]

### Kitesurf (`kitesurf`)

- **Repo:** https://github.com/cloudflare/kitesurf · Apache-2.0 · nivel 3 · —/100
- **Qué es:** Explora un motor experimental para renderizar páginas en Workers y obtener capturas desde código o herramientas compatibles.
- **Cuándo elegirlo:** Casos: Capturar una página estática de prueba.; Comparar cómo se renderiza un componente en un entorno aislado. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: preparación pesada; TypeScript, Cargo.toml, package.json; hardware model_dependent; API de IA: no; Contenedor local para el ejemplo o Cloudflare Workers con los servicios que indique su guía..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://kitesurf.dev/
- **Primera prueba propuesta (no ejecutada):** Usa el ejemplo local enlazado y abre una página de prueba sin cuentas ni cookies. Éxito: Se obtiene una captura o HTML del ejemplo y puedes compararlo con tu navegador.
- **Riesgos y avisos:** El motor es experimental. Workers y Dynamic Workers pueden requerir planes de Cloudflare; la demo local no exige cuenta.

### awesome-chrome-devtools (`awesome-chrome-devtools`)

- **Repo:** https://github.com/ChromeDevTools/awesome-chrome-devtools · CC0-1.0 · nivel 1 · 43/100
- **Qué es:** Awesome Chrome DevTools, lista curada de herramientas y recursos del ecosistema Chrome DevTools y del protocolo CDP, mantenida en la organización ChromeDevTools. Licencia CC0-1.0. Existe desde 2016 (~7k estrellas).
- **Cuándo elegirlo:** Casos: Encontrar una herramienta de depuración; Explorar clientes de DevTools Protocol.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; necesidad de depuración o automatización; hardware prerequisites; API de IA: no; Navegador; necesidad de depuración o automatización.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ChromeDevTools/awesome-chrome-devtools/blob/master/readme.md
- **Primera prueba propuesta (no ejecutada):** Escoge una herramienta de CDP y revisa su repositorio y función antes de instalar Éxito: Puedes distinguir protocolo, cliente y extensión
- **Combina con:** `puppeteer` [32/bibliotecas], `chrome-devtools-mcp` [5/servidores], `lightpanda` [32/motores-web]
- **Riesgos y avisos:** Sin alternativas declaradas. Un directorio que enlaza servidores MCP no es por sí mismo un servidor ni una integración con un agente.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-32.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Navegadores y automatización web», lee `docs/alexandria/categoria-32.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-32.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
