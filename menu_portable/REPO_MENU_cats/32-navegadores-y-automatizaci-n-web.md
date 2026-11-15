# 32. Navegadores y automatización web — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agent-browser`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=navegador,rust

**Qué es:** CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. Mantiene una sesión de navegador y permite abrir páginas, inspeccionarlas y actuar por referencias desde la terminal.
**Stack:** Rust, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/vercel-labs/agent-browser

**Instalación** [+]: `npm install -g agent-browser`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas navegación programable con salidas compactas para un agente
**Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente
**Combina con:** `codex`
**Alternativas (elige una):** `playwright-cli`

## `awesome-chrome-devtools`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=navegador,awesome,awesome-list

**Qué es:** Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol. Agrupa depuradores, visores de trazas y clientes del protocolo para localizar una herramienta adecuada.
**Stack:** Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ChromeDevTools/awesome-chrome-devtools

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas utilidades para depurar o automatizar Chrome
**Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente

## `browser-harness`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=browser,coding-agent,python

**Qué es:** Conecta el agente a tu navegador por CDP con un arnés pequeño y editable. Útil cuando necesitas libertad total y tus cuentas ya abiertas.
**Stack:** Python, CDP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/browser-use/browser-harness

**Instalación** [?]: `Seguir la instalación original: https://github.com/browser-use/browser-harness/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente debe usar tu navegador real con sesión
**Evita si:** necesitas aislamiento; mira `playwright-mcp`
**Combina con:** `claude-code`, `codex`
**Alternativas (elige una):** `playwright-mcp`, `chrome-devtools-mcp`

## `browser-use`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,browser,python

**Qué es:** Resuelve la fragilidad del scraping basado en CSS: el agente "ve" la página como un humano y decide la siguiente acción.
**Stack:** Python 3.11+, Rust (core), Playwright
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/browser-use/browser-use

**Instalación** [?]: `Seguir la instalación original: https://github.com/browser-use/browser-use/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres navegación como humano y tolerancia a cambios de UI
**Evita si:** necesitas scripts deterministas y baratos (playwright) o no quieres depender de un LLM por paso
**Combina con:** `playwright`, `gpt-researcher`
**Alternativas (elige una):** `computer-use-preview`, `stagehand`, `skyvern`, `playwright-mcp`

## `camofox-browser`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=— · tags=navegador,ai-agent,anti-bot,antidetect-browser,automation,bot-detection,browser-automation,cloudflare-bypass

**Qué es:** Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes. Expone un navegador derivado de Firefox mediante herramientas y endpoints de automatización.
**Stack:** JavaScript, Docker, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/jo-inc/camofox-browser

**Instalación** [?]: `Seguir la instalación original: https://github.com/jo-inc/camofox-browser/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas evaluar una alternativa de navegador automatizado para agentes
**Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente

## `lightpanda`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=browser,scraping

**Qué es:** Ejecuta JavaScript y es compatible con Puppeteer y Playwright por CDP, usando una fracción de memoria. Ideal para scraping masivo.
**Stack:** Zig, V8
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/lightpanda-io/browser

**Instalación** [?]: `Seguir la instalación original: https://github.com/lightpanda-io/browser/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas muchos navegadores headless con poca memoria
**Evita si:** necesitas compatibilidad total con sitios complejos; usa Chrome con `playwright`
**Combina con:** `puppeteer`, `playwright`

## `playwright`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,browser,typescript

**Qué es:** Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. Se ha convertido en el estándar moderno de automatización de browser, desplazando a Selenium/Puppeteer por su fiabilidad y su auto-espera de elementos.
**Stack:** Node.js o Python (también Java/.NET)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/playwright

**Instalación** [?]: `Seguir la instalación original: https://github.com/microsoft/playwright/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas control preciso y reproducible del browser
**Evita si:** quieres que el agente navegue por visión (browser-use) o no necesitas un navegador real
**Combina con:** `browser-use`, `crawlee`
**Alternativas (elige una):** `puppeteer`, `selenium`

## `playwright-cli`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=browser,typescript

**Qué es:** Resuelve el problema de los árboles de accesibilidad y los JSON de herramientas que inflan el prompt en cada turno.
**Stack:** TypeScript/Node.js, CLI
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/playwright-cli

**Instalación** [?]: `Seguir la instalación original: https://github.com/microsoft/playwright-cli/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente vive en CLI y el contexto es un recurso caro
**Evita si:** necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP)
**Combina con:** `playwright`, `browser-use`
**Alternativas (elige una):** `agent-browser`

## `puppeteer`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=browser,scraping,typescript

**Qué es:** Automatiza navegación, capturas, PDFs y pruebas. Es la base de muchas herramientas de scraping.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/puppeteer/puppeteer

**Instalación** [+]: `npm i puppeteer`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** trabajas en Node y quieres controlar Chrome
**Evita si:** necesitas varios navegadores y pruebas E2E; mira `playwright`
**Combina con:** `lightpanda`
**Alternativas (elige una):** `playwright`, `selenium`

## `selenium`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=browser,java,python

**Qué es:** Estándar W3C WebDriver, muy usado en pruebas empresariales con Selenium Grid para paralelizar.
**Stack:** Java, Python, C#, JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/SeleniumHQ/selenium

**Instalación** [?]: `Seguir la instalación original: https://github.com/SeleniumHQ/selenium/blob/trunk/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu equipo ya usa Selenium o necesitas muchos lenguajes
**Evita si:** empiezas de cero; mira `playwright`
**Alternativas (elige una):** `playwright`, `puppeteer`

## `skyvern`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic · tags=browser,automation,python

**Qué es:** Completa formularios, compras o descargas en sitios que nunca vio, entendiendo la página con visión. Incluye UI, API y workflows.
**Stack:** Python, Playwright, React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Skyvern-AI/skyvern

**Instalación** [+]: `pip install skyvern`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** automatizas portales web que cambian a menudo
**Evita si:** necesitas scraping masivo y barato; mira `crawl4ai`
**Combina con:** `n8n`
**Alternativas (elige una):** `browser-use`, `stagehand`, `computer-use-preview`

## `stagehand`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic · tags=browser,agents,typescript

**Qué es:** Usa `act`, `extract` y `observe` para que la IA haga lo difícil y tu código lo predecible. Basado en Playwright.
**Stack:** TypeScript, Playwright
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/browserbase/stagehand

**Instalación** [?]: `Seguir la instalación original: https://github.com/browserbase/stagehand/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres automatización web robusta con un toque de IA en TS
**Evita si:** quieres que un agente navegue solo; mira `browser-use`
**Combina con:** `mastra`, `playwright`
**Alternativas (elige una):** `browser-use`, `skyvern`
