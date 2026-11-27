# Alexandría para agentes · Automatización y pruebas por código

Categoría 32 «Navegadores y automatización web» › subcategoría `bibliotecas`. 6 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=32&sub=bibliotecas · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `playwright` | Framework de Microsoft para automatización y testing de navegadores Chromium… | 2 Intermedio | 79 | Apache-2.0 (OSI permisiva) | recomendado |
| `puppeteer` | Librería de Google para controlar Chrome y Firefox desde Node.js. | 2 Intermedio | 72 | Apache-2.0 (OSI permisiva) | alternativa |
| `cypress` | Framework de pruebas end-to-end y de componentes para todo lo que corre en un… | 2 Intermedio | 65 | MIT (OSI permisiva) | alternativa |
| `selenium` | Framework veterano de automatización de navegadores con soporte para casi todos… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `webdriverio` | Framework de automatización de navegadores y apps móviles para Node.js basado… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `flaresolverr` | Servidor proxy que abre páginas protegidas por Cloudflare o DDoS-GUARD en un… | 1 Básico | 55 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### playwright (`playwright`)

- **Repo:** https://github.com/microsoft/playwright · Apache-2.0 · nivel 2 · 79/100 · recomendado en «Automatización de navegador y pruebas E2E»
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

- **Repo:** https://github.com/FlareSolverr/FlareSolverr · MIT · nivel 1 · 55/100
- **Qué es:** Servidor de código abierto (MIT) mantenido por la comunidad (ngosang y colaboradores), muy usado junto a indexadores multimedia. Activo, aunque depende de que Cloudflare no cambie sus desafíos.
- **Cuándo elegirlo:** Casos: dar acceso a indexadores (como Prowlarr o Jackett) a sitios propios o autorizados detrás de Cloudflare; obtener cookies válidas para que un scraper autorizado continúe con un cliente HTTP….
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, docker-compose.yml, package.json, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d --name=flaresolverr -p 127.0.0.1:8191:8191 -e LOG_LEVEL=info --restart unless-stopped ghcr.io/flaresolverr/flaresolverr:latest` — fuente: https://github.com/FlareSolverr/FlareSolverr/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el contenedor con Docker y envía un POST a `http://localhost:8191/v1` con `cmd: request.get` y una URL autorizada. Éxito: Obtienes el HTML de la página y las cookies de la sesión.
- **Combina con:** `selenium`, `scrapy` [4/crawlers], `crawlee-python` [4/crawlers]

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-32-bibliotecas.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Automatización y pruebas por código», lee `docs/alexandria/categoria-32-bibliotecas.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-32-bibliotecas.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
