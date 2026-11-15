# 4. Buscar y extraer información web — detalle de repos

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

## `agent-reach`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=scraping,research,python

**Qué es:** Un solo comando para que el agente lea y busque en redes y plataformas populares, incluidas chinas como Bilibili y XiaoHongShu.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Panniantong/Agent-Reach

**Instalación** [?]: `Seguir la instalación original: https://github.com/Panniantong/Agent-Reach/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente necesita leer redes sociales sin APIs de pago
**Evita si:** necesitas datos con garantías de términos de servicio
**Combina con:** `claude-code`, `last30days-skill`
**Alternativas (elige una):** `snscrape`

## `archivebox`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=scraping,data,python,docker

**Qué es:** Le das URLs, marcadores o historial y guarda copias completas para siempre. Útil para investigación y preservación de fuentes.
**Stack:** Python, Django, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ArchiveBox/ArchiveBox

**Instalación** [+]: `pip install archivebox`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres conservar copias fieles de páginas web
**Evita si:** solo necesitas el texto para un LLM; mira `jina-reader`
**Combina con:** `yt-dlp`

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

## `awesome-web-scraping`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=crawlers,captcha-bypass,captcha-recaptcha,crawler,crawling,crawling-framework,crawling-python,crawling-tool

**Qué es:** Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos. Organiza opciones por lenguaje y función para investigar alternativas de extracción.
**Stack:** JavaScript, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/lorien/awesome-web-scraping

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres comparar librerías de scraping antes de elegir tu stack
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

## `changedetection`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=scraping,notifications,python,docker

**Qué es:** Vigila precios, stock, documentación o cualquier texto de una página y te avisa cuando cambia. Admite navegador real para sitios con JavaScript.
**Stack:** Python, Playwright, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/dgtlmoon/changedetection.io

**Instalación** [?]: `Seguir la instalación original: https://github.com/dgtlmoon/changedetection.io/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres alertas cuando cambia una página
**Evita si:** necesitas extraer datos estructurados; mira `maxun`
**Combina con:** `n8n`

## `crawl4ai`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=scraping,python

**Qué es:** Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. Una de las alternativas open-source más populares a las APIs de pago; gratuita, self-host y muy activa en la comunidad de scraping para LLMs.
**Stack:** Python, Playwright
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/unclecode/crawl4ai

**Instalación** [+]: `pip install crawl4ai`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas volumen barato y self-host
**Evita si:** quieres una API hosted simple sin operar navegadores (firecrawl)
**Combina con:** `firecrawl`, `gpt-researcher`
**Alternativas (elige una):** `jina-reader`

## `crawlee`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=scraping,typescript

**Qué es:** Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. Mantenido por Apify, es la referencia de crawling en el ecosistema JavaScript y trae evasión de bloqueos lista de fábrica.
**Stack:** Node.js/TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/apify/crawlee

**Instalación** [+]: `npx crawlee create`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** scrapeas con Node y necesitas antibloqueo
**Evita si:** trabajas en Python (crawlee-python) o no necesitas evasión
**Combina con:** `playwright`

## `crawlee-python`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=scraping,python

**Qué es:** Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. Acerca las ventajas del Crawlee de Node a quienes ya viven en Python, con respaldo oficial de Apify y adopción en crecimiento.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/apify/crawlee-python

**Instalación** [?]: `Seguir la instalación original: https://github.com/apify/crawlee-python/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres Crawlee en Python con antibloqueo
**Evita si:** ya usas scrapy y te basta, o no necesitas evasión
**Combina con:** `scrapy`, `playwright`

## `firecrawl`
role=platform · exec=cloud · setup=medium · mcp=True · prov=— · tags=scraping,typescript,docker

**Qué es:** Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. Se ha vuelto la opción de referencia para alimentar pipelines RAG y agentes con web limpia; muy adoptada y con integración MCP de primera clase.
**Stack:** API/SDK (TS/Python), hosted o self-host, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/firecrawl/firecrawl

**Instalación** [+]: `pip install firecrawl`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** alimentas agentes/RAG con web y quieres salida limpia
**Evita si:** solo quieres HTML crudo o el presupuesto de API no encaja
**Combina con:** `gpt-researcher`, `crawl4ai`
**Alternativas (elige una):** `jina-reader`

## `instaloader`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vision,scraping,python

**Qué es:** Resuelve el archivado masivo de Instagram sin recurrir a APIs oficiales de pago ni herramientas manuales.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/instaloader/instaloader

**Instalación** [?]: `Seguir la instalación original: https://github.com/instaloader/instaloader/blob/master/README.rst`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas datos de Instagram de forma fiable
**Evita si:** quieres varias redes a la vez (snscrape) o el contenido requiere API oficial por ToS
**Combina con:** `snscrape`

## `jina-reader`
role=platform · exec=cloud · setup=easy · mcp=False · prov=— · tags=scraping,rag,typescript

**Qué es:** Pega `https://r.jina.ai/` delante de una URL y obtienes su contenido limpio. También busca en la web con `s.jina.ai`.
**Stack:** TypeScript, Puppeteer
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/jina-ai/reader

**Instalación** [?]: `Seguir la instalación original: https://github.com/jina-ai/reader/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas leer páginas como Markdown al instante
**Evita si:** vas a rastrear sitios completos; mira `crawl4ai` o `firecrawl`
**Combina con:** `n8n`, `llama-index`
**Alternativas (elige una):** `firecrawl`, `crawl4ai`

## `last30days-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=research,skills,python

**Qué es:** Busca lo que la gente está diciendo ahora sobre un tema y lo resume con fuentes. Prioriza señales reales como votos, likes y apuestas.
**Stack:** Python, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mvanhorn/last30days-skill

**Instalación** [?]: `Seguir la instalación original: https://github.com/mvanhorn/last30days-skill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres saber qué se dice ahora sobre un tema
**Evita si:** necesitas un informe académico; mira `storm`
**Combina con:** `claude-code`, `agent-reach`
**Alternativas (elige una):** `social-media-research-skills`

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

## `llm-scraper`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=scraping,typescript

**Qué es:** Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. Popular por su simplicidad: salida tipada y validada sin escribir parsers, integrándose directamente con Playwright y los SDKs de LLM.
**Stack:** TypeScript, Playwright, Zod
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/mishushakov/llm-scraper

**Instalación** [?]: `Seguir la instalación original: https://github.com/mishushakov/llm-scraper/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres salida tipada y validada en stack TS
**Evita si:** prefieres extracción semántica por grafos (Scrapegraph-ai) o trabajas en Python
**Combina con:** `playwright`, `firecrawl`
**Alternativas (elige una):** `maxun`

## `maxun`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=scraping,automation,typescript

**Qué es:** Grabas lo que quieres extraer haciendo clic en la página y Maxun crea un robot que lo repite, con paginación y programación. Ideal para equipos sin programadores.
**Stack:** TypeScript, Playwright, PostgreSQL, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/getmaxun/maxun

**Instalación** [?]: `Seguir la instalación original: https://github.com/getmaxun/maxun/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres extraer datos web sin programar
**Evita si:** programas y prefieres librerías; mira `crawl4ai` o `scrapy`
**Combina con:** `n8n`
**Alternativas (elige una):** `scrapegraph-ai`, `llm-scraper`

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

## `scrapegraph-ai`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=scraping,python

**Qué es:** Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. Muy popular por permitir scraping "by prompt", combinando extracción con razonamiento del modelo y soporte para múltiples proveedores.
**Stack:** Python, LangChain/LangGraph, Playwright
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ScrapeGraphAI/Scrapegraph-ai

**Instalación** [+]: `pip install scrapegraphai`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres estructura semántica "by prompt" en Python
**Evita si:** te basta un esquema simple (llm-scraper) o el coste de LLM por página es alto
**Combina con:** `crawl4ai`, `graphrag`
**Alternativas (elige una):** `maxun`

## `scrapely`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=scraping

**Qué es:** Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales. Pieza histórica del ecosistema Scrapy; nicho y poco activa hoy, pero útil cuando se quiere extraer "por demostración" en lugar de programar selectores.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/scrapy/scrapely

**Instalación** [+]: `pip install scrapely`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** prefieres enseñar por ejemplos y el sitio es homogéneo
**Evita si:** necesitas un crawler completo o el proyecto exige mantenimiento activo
**Combina con:** `scrapy`

## `scrapling`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=automation,scraping,python

**Qué es:** Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. Proyecto en alza por su enfoque "auto-reparable" de selectores, que evita reescribir scrapers cada vez que el sitio se actualiza.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/D4Vinci/Scrapling

**Instalación** [+]: `pip install scrapling`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** los sitios cambian o te bloquean a menudo
**Evita si:** el target es estable y simple, o no necesitas stealth
**Combina con:** `scrapy`

## `scrapy`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=scraping,python

**Qué es:** Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. Estándar de facto del scraping en Python desde hace más de una década, con enorme ecosistema de extensiones y base instalada masiva.
**Stack:** Python (Twisted)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/scrapy/scrapy

**Instalación** [+]: `pip install scrapy`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres un crawler sólido y configurable a escala
**Evita si:** buscas salida lista para LLM o algo puntual sin curva de framework
**Combina con:** `scrapely`, `crawlee-python`

## `scrapydweb`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=crawlers,dashboard,log-analysis,log-parsing,scrapy,scrapy-log-analysis,scrapy-visualization,scrapyd

**Qué es:** Panel web para administrar clústeres de Scrapyd y consultar trabajos, logs y estadísticas de Scrapy. Conecta servidores Scrapyd y centraliza despliegues, tareas programadas y seguimiento de crawls.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/my8100/scrapydweb

**Instalación** [+]: `pip install scrapydweb`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** operas varios spiders de Scrapy y necesitas un panel de administración
**Evita si:** la fuente ya ofrece una API o un archivo de datos suficiente
**Combina con:** `scrapy`

## `searxng`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=search,research,python,docker

**Qué es:** Combina resultados de más de 70 servicios sin rastrearte. Muchos agentes de investigación lo usan como API de búsqueda gratuita y propia.
**Stack:** Python, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/searxng/searxng

**Instalación** [?]: `Seguir la instalación original: https://github.com/searxng/searxng/blob/master/README.rst`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tus agentes necesitan buscar en la web sin coste por consulta
**Evita si:** necesitas resultados con SLA comercial
**Combina con:** `gpt-researcher`, `open-webui`, `vane`

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

## `snscrape`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=scraping,python

**Qué es:** Resuelve la recolección histórica de datos sociales cuando las APIs de pago no son viables o no existen.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/JustAnotherArchivist/snscrape

**Instalación** [?]: `Seguir la instalación original: https://github.com/JustAnotherArchivist/snscrape/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** recolectas varias redes y no te sirve una API oficial
**Evita si:** solo necesitas Instagram (instaloader) o la plataforma ya bloqueó el acceso no oficial
**Combina con:** `instaloader`
**Alternativas (elige una):** `agent-reach`

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

## `vane`
role=app · exec=local · setup=easy · mcp=False · prov=openai,local · tags=search,research,local,typescript

**Qué es:** Busca en la web con SearXNG y responde con citas usando modelos locales o en la nube. Incluye modos de enfoque para académico, YouTube o Reddit.
**Stack:** TypeScript, Next.js, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ItzCrazyKns/Vane

**Instalación** [?]: `Seguir la instalación original: https://github.com/ItzCrazyKns/Vane/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un buscador con respuestas citadas auto-hospedado
**Evita si:** necesitas informes largos; mira `gpt-researcher`
**Combina con:** `searxng`, `ollama`
**Alternativas (elige una):** `gpt-researcher`

## `yt-dlp`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,scraping,python

**Qué es:** Descarga videos, audios, subtítulos y metadatos de YouTube y miles de plataformas. Base de muchos pipelines de transcripción.
**Stack:** Python, ffmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/yt-dlp/yt-dlp

**Instalación** [?]: `Seguir la instalación original: https://github.com/yt-dlp/yt-dlp/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas bajar audio o video de la web
**Evita si:** solo necesitas metadatos sociales; mira `instaloader`
**Combina con:** `whisperx`, `ffmpeg`, `fabric`
