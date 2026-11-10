# 4. Scraping, Búsqueda & Research Web — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agent-reach`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Un solo comando para que el agente lea y busque en redes y plataformas populares, incluidas chinas como Bilibili y XiaoHongShu.
**Stack:** Python
**Repo:** https://github.com/Panniantong/Agent-Reach

**Instalación** [~]: `git clone https://github.com/Panniantong/Agent-Reach && cd Agent-Reach && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tu agente necesita leer redes sociales sin APIs de pago
**Evita si:** necesitas datos con garantías de términos de servicio
**Combina con:** `claude-code`, `last30days-skill`
**Alternativas (elige una):** `snscrape`

## `archivebox`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Le das URLs, marcadores o historial y guarda copias completas para siempre. Útil para investigación y preservación de fuentes.
**Stack:** Python, Django, Docker
**Repo:** https://github.com/ArchiveBox/ArchiveBox

**Instalación** [~]: `git clone https://github.com/ArchiveBox/ArchiveBox && cd ArchiveBox && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres conservar copias fieles de páginas web
**Evita si:** solo necesitas el texto para un LLM; mira `jina-reader`
**Combina con:** `yt-dlp`

## `browser-harness`
role=runtime · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Conecta el agente a tu navegador por CDP con un arnés pequeño y editable. Útil cuando necesitas libertad total y tus cuentas ya abiertas.
**Stack:** Python, CDP
**Repo:** https://github.com/browser-use/browser-harness

**Instalación** [~]: `git clone https://github.com/browser-use/browser-harness && cd browser-harness && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tu agente debe usar tu navegador real con sesión
**Evita si:** necesitas aislamiento; mira `playwright-mcp`
**Combina con:** `claude-code`, `codex`
**Alternativas (elige una):** `playwright-mcp`, `chrome-devtools-mcp`

## `browser-use`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve la fragilidad del scraping basado en CSS: el agente "ve" la página como un humano y decide la siguiente acción.
**Stack:** Python 3.11+, Rust (core), Playwright
**Repo:** https://github.com/browser-use/browser-use

**Instalación** [~]: `pip install browser-use   (o: uv add browser-use)`
_Nombre PyPI puede diferir de 'browser-use'; verifica en pypi.org._

**Elige si:** quieres navegación como humano y tolerancia a cambios de UI
**Evita si:** necesitas scripts deterministas y baratos (playwright) o no quieres depender de un LLM por paso
**Combina con:** `playwright`, `gpt-researcher`
**Alternativas (elige una):** `computer-use-preview`, `stagehand`, `skyvern`, `playwright-mcp`

## `changedetection`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Vigila precios, stock, documentación o cualquier texto de una página y te avisa cuando cambia. Admite navegador real para sitios con JavaScript.
**Stack:** Python, Playwright, Docker
**Repo:** https://github.com/dgtlmoon/changedetection.io

**Instalación** [~]: `git clone https://github.com/dgtlmoon/changedetection.io && cd changedetection.io && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres alertas cuando cambia una página
**Evita si:** necesitas extraer datos estructurados; mira `maxun`
**Combina con:** `n8n`

## `crawl4ai`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. Una de las alternativas open-source más populares a las APIs de pago; gratuita, self-host y muy activa en la comunidad de scraping para LLMs.
**Stack:** Python, Playwright
**Repo:** https://github.com/unclecode/crawl4ai

**Instalación** [~]: `pip install crawl4ai   (o: uv add crawl4ai)`
_Nombre PyPI puede diferir de 'crawl4ai'; verifica en pypi.org._

**Elige si:** necesitas volumen barato y self-host
**Evita si:** quieres una API hosted simple sin operar navegadores (firecrawl)
**Combina con:** `firecrawl`, `gpt-researcher`
**Alternativas (elige una):** `jina-reader`

## `crawlee`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. Mantenido por Apify, es la referencia de crawling en el ecosistema JavaScript y trae evasión de bloqueos lista de fábrica.
**Stack:** Node.js/TypeScript
**Repo:** https://github.com/apify/crawlee

**Instalación** [~]: `npm install crawlee   (o: pnpm add crawlee)`
_Nombre npm puede diferir de 'crawlee'; verifica en npmjs.com._

**Elige si:** scrapeas con Node y necesitas antibloqueo
**Evita si:** trabajas en Python (crawlee-python) o no necesitas evasión
**Combina con:** `playwright`

## `crawlee-python`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. Acerca las ventajas del Crawlee de Node a quienes ya viven en Python, con respaldo oficial de Apify y adopción en crecimiento.
**Stack:** Python
**Repo:** https://github.com/apify/crawlee-python

**Instalación** [~]: `pip install crawlee   (o: uv add crawlee)`
_Nombre PyPI puede diferir de 'crawlee-python'; verifica en pypi.org._

**Elige si:** quieres Crawlee en Python con antibloqueo
**Evita si:** ya usas scrapy y te basta, o no necesitas evasión
**Combina con:** `scrapy`, `playwright`

## `firecrawl`
role=platform · exec=cloud · setup=medium · mcp=True · prov=—

**Qué es:** Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. Se ha vuelto la opción de referencia para alimentar pipelines RAG y agentes con web limpia; muy adoptada y con integración MCP de primera clase.
**Stack:** API/SDK (TS/Python), hosted o self-host, Docker
**Repo:** https://github.com/firecrawl/firecrawl

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** alimentas agentes/RAG con web y quieres salida limpia
**Evita si:** solo quieres HTML crudo o el presupuesto de API no encaja
**Combina con:** `gpt-researcher`, `crawl4ai`
**Alternativas (elige una):** `jina-reader`

## `instaloader`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el archivado masivo de Instagram sin recurrir a APIs oficiales de pago ni herramientas manuales.
**Stack:** Python
**Repo:** https://github.com/instaloader/instaloader

**Instalación** [~]: `pip install instaloader   (o: uv add instaloader)`
_Nombre PyPI puede diferir de 'instaloader'; verifica en pypi.org._

**Elige si:** necesitas datos de Instagram de forma fiable
**Evita si:** quieres varias redes a la vez (snscrape) o el contenido requiere API oficial por ToS
**Combina con:** `snscrape`

## `jina-reader`
role=platform · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Pega `https://r.jina.ai/` delante de una URL y obtienes su contenido limpio. También busca en la web con `s.jina.ai`.
**Stack:** TypeScript, Puppeteer
**Repo:** https://github.com/jina-ai/reader

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** necesitas leer páginas como Markdown al instante
**Evita si:** vas a rastrear sitios completos; mira `crawl4ai` o `firecrawl`
**Combina con:** `n8n`, `llama-index`
**Alternativas (elige una):** `firecrawl`, `crawl4ai`

## `last30days-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Busca lo que la gente está diciendo ahora sobre un tema y lo resume con fuentes. Prioriza señales reales como votos, likes y apuestas.
**Stack:** Python, Markdown
**Repo:** https://github.com/mvanhorn/last30days-skill

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/last30days/). Si necesitas el código: git clone https://github.com/mvanhorn/last30days-skill`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres saber qué se dice ahora sobre un tema
**Evita si:** necesitas un informe académico; mira `storm`
**Combina con:** `claude-code`, `agent-reach`

## `lightpanda`
role=runtime · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Ejecuta JavaScript y es compatible con Puppeteer y Playwright por CDP, usando una fracción de memoria. Ideal para scraping masivo.
**Stack:** Zig, V8
**Repo:** https://github.com/lightpanda-io/browser

**Instalación** [?]: `git clone https://github.com/lightpanda-io/browser (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas muchos navegadores headless con poca memoria
**Evita si:** necesitas compatibilidad total con sitios complejos; usa Chrome con `playwright`
**Combina con:** `puppeteer`, `playwright`

## `llm-scraper`
role=library · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. Popular por su simplicidad: salida tipada y validada sin escribir parsers, integrándose directamente con Playwright y los SDKs de LLM.
**Stack:** TypeScript, Playwright, Zod
**Repo:** https://github.com/mishushakov/llm-scraper

**Instalación** [~]: `npm install llm-scraper   (o: pnpm add llm-scraper)`
_Nombre npm puede diferir de 'llm-scraper'; verifica en npmjs.com._

**Elige si:** quieres salida tipada y validada en stack TS
**Evita si:** prefieres extracción semántica por grafos (Scrapegraph-ai) o trabajas en Python
**Combina con:** `playwright`, `firecrawl`
**Alternativas (elige una):** `maxun`

## `maxun`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Grabas lo que quieres extraer haciendo clic en la página y Maxun crea un robot que lo repite, con paginación y programación. Ideal para equipos sin programadores.
**Stack:** TypeScript, Playwright, PostgreSQL, Docker
**Repo:** https://github.com/getmaxun/maxun

**Instalación** [~]: `git clone https://github.com/getmaxun/maxun && cd maxun && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres extraer datos web sin programar
**Evita si:** programas y prefieres librerías; mira `crawl4ai` o `scrapy`
**Combina con:** `n8n`
**Alternativas (elige una):** `scrapegraph-ai`, `llm-scraper`

## `playwright`
role=library · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. Se ha convertido en el estándar moderno de automatización de browser, desplazando a Selenium/Puppeteer por su fiabilidad y su auto-espera de elementos.
**Stack:** Node.js o Python (también Java/.NET)
**Repo:** https://github.com/microsoft/playwright

**Instalación** [~]: `pip install playwright   (o: uv add playwright)`
_Nombre PyPI puede diferir de 'playwright'; verifica en pypi.org._

**Elige si:** necesitas control preciso y reproducible del browser
**Evita si:** quieres que el agente navegue por visión (browser-use) o no necesitas un navegador real
**Combina con:** `browser-use`, `crawlee`
**Alternativas (elige una):** `puppeteer`, `selenium`

## `playwright-cli`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el problema de los árboles de accesibilidad y los JSON de herramientas que inflan el prompt en cada turno.
**Stack:** TypeScript/Node.js, CLI
**Repo:** https://github.com/microsoft/playwright-cli

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/playwright-cli/). Si necesitas el código: git clone https://github.com/microsoft/playwright-cli`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** tu agente vive en CLI y el contexto es un recurso caro
**Evita si:** necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP)
**Combina con:** `playwright`, `browser-use`

## `puppeteer`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Automatiza navegación, capturas, PDFs y pruebas. Es la base de muchas herramientas de scraping.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/puppeteer/puppeteer

**Instalación** [~]: `npm install puppeteer   (o: pnpm add puppeteer)`
_Nombre npm puede diferir de 'Puppeteer'; verifica en npmjs.com._

**Elige si:** trabajas en Node y quieres controlar Chrome
**Evita si:** necesitas varios navegadores y pruebas E2E; mira `playwright`
**Combina con:** `lightpanda`
**Alternativas (elige una):** `playwright`, `selenium`

## `scrapegraph-ai`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. Muy popular por permitir scraping "by prompt", combinando extracción con razonamiento del modelo y soporte para múltiples proveedores.
**Stack:** Python, LangChain/LangGraph, Playwright
**Repo:** https://github.com/ScrapeGraphAI/Scrapegraph-ai

**Instalación** [~]: `pip install scrapegraph-ai   (o: uv add scrapegraph-ai)`
_Nombre PyPI puede diferir de 'Scrapegraph-ai'; verifica en pypi.org._

**Elige si:** quieres estructura semántica "by prompt" en Python
**Evita si:** te basta un esquema simple (llm-scraper) o el coste de LLM por página es alto
**Combina con:** `crawl4ai`, `graphrag`
**Alternativas (elige una):** `maxun`

## `scrapely`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales. Pieza histórica del ecosistema Scrapy; nicho y poco activa hoy, pero útil cuando se quiere extraer "por demostración" en lugar de programar selectores.
**Stack:** Python
**Repo:** https://github.com/scrapy/scrapely

**Instalación** [~]: `pip install scrapely   (o: uv add scrapely)`
_Nombre PyPI puede diferir de 'scrapely'; verifica en pypi.org._

**Elige si:** prefieres enseñar por ejemplos y el sitio es homogéneo
**Evita si:** necesitas un crawler completo o el proyecto exige mantenimiento activo
**Combina con:** `scrapy`

## `scrapling`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. Proyecto en alza por su enfoque "auto-reparable" de selectores, que evita reescribir scrapers cada vez que el sitio se actualiza.
**Stack:** Python
**Repo:** https://github.com/D4Vinci/Scrapling

**Instalación** [~]: `pip install scrapling   (o: uv add scrapling)`
_Nombre PyPI puede diferir de 'Scrapling'; verifica en pypi.org._

**Elige si:** los sitios cambian o te bloquean a menudo
**Evita si:** el target es estable y simple, o no necesitas stealth
**Combina con:** `scrapy`

## `scrapy`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. Estándar de facto del scraping en Python desde hace más de una década, con enorme ecosistema de extensiones y base instalada masiva.
**Stack:** Python (Twisted)
**Repo:** https://github.com/scrapy/scrapy

**Instalación** [~]: `pip install scrapy   (o: uv add scrapy)`
_Nombre PyPI puede diferir de 'scrapy'; verifica en pypi.org._

**Elige si:** quieres un crawler sólido y configurable a escala
**Evita si:** buscas salida lista para LLM o algo puntual sin curva de framework
**Combina con:** `scrapely`, `crawlee-python`

## `searxng`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Combina resultados de más de 70 servicios sin rastrearte. Muchos agentes de investigación lo usan como API de búsqueda gratuita y propia.
**Stack:** Python, Docker
**Repo:** https://github.com/searxng/searxng

**Instalación** [~]: `git clone https://github.com/searxng/searxng && cd searxng && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** tus agentes necesitan buscar en la web sin coste por consulta
**Evita si:** necesitas resultados con SLA comercial
**Combina con:** `gpt-researcher`, `open-webui`, `vane`

## `selenium`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Estándar W3C WebDriver, muy usado en pruebas empresariales con Selenium Grid para paralelizar.
**Stack:** Java, Python, C#, JavaScript
**Repo:** https://github.com/SeleniumHQ/selenium

**Instalación** [~]: `pip install selenium   (o: uv add selenium)`
_Nombre PyPI puede diferir de 'Selenium'; verifica en pypi.org._

**Elige si:** tu equipo ya usa Selenium o necesitas muchos lenguajes
**Evita si:** empiezas de cero; mira `playwright`
**Alternativas (elige una):** `playwright`, `puppeteer`

## `skyvern`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic']

**Qué es:** Completa formularios, compras o descargas en sitios que nunca vio, entendiendo la página con visión. Incluye UI, API y workflows.
**Stack:** Python, Playwright, React
**Repo:** https://github.com/Skyvern-AI/skyvern

**Instalación** [~]: `git clone https://github.com/Skyvern-AI/skyvern && cd skyvern && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** automatizas portales web que cambian a menudo
**Evita si:** necesitas scraping masivo y barato; mira `crawl4ai`
**Combina con:** `n8n`
**Alternativas (elige una):** `browser-use`, `stagehand`, `computer-use-preview`

## `snscrape`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve la recolección histórica de datos sociales cuando las APIs de pago no son viables o no existen.
**Stack:** Python
**Repo:** https://github.com/JustAnotherArchivist/snscrape

**Instalación** [~]: `pip install snscrape   (o: uv add snscrape)`
_Nombre PyPI puede diferir de 'snscrape'; verifica en pypi.org._

**Elige si:** recolectas varias redes y no te sirve una API oficial
**Evita si:** solo necesitas Instagram (instaloader) o la plataforma ya bloqueó el acceso no oficial
**Combina con:** `instaloader`
**Alternativas (elige una):** `agent-reach`

## `stagehand`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic']

**Qué es:** Usa `act`, `extract` y `observe` para que la IA haga lo difícil y tu código lo predecible. Basado en Playwright.
**Stack:** TypeScript, Playwright
**Repo:** https://github.com/browserbase/stagehand

**Instalación** [~]: `npm install stagehand   (o: pnpm add stagehand)`
_Nombre npm puede diferir de 'Stagehand'; verifica en npmjs.com._

**Elige si:** quieres automatización web robusta con un toque de IA en TS
**Evita si:** quieres que un agente navegue solo; mira `browser-use`
**Combina con:** `mastra`, `playwright`
**Alternativas (elige una):** `browser-use`, `skyvern`

## `vane`
role=app · exec=local · setup=easy · mcp=False · prov=['openai', 'local']

**Qué es:** Busca en la web con SearXNG y responde con citas usando modelos locales o en la nube. Incluye modos de enfoque para académico, YouTube o Reddit.
**Stack:** TypeScript, Next.js, Docker
**Repo:** https://github.com/ItzCrazyKns/Vane

**Instalación** [~]: `git clone https://github.com/ItzCrazyKns/Vane && cd Vane && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un buscador con respuestas citadas auto-hospedado
**Evita si:** necesitas informes largos; mira `gpt-researcher`
**Combina con:** `searxng`, `ollama`
**Alternativas (elige una):** `gpt-researcher`

## `yt-dlp`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Descarga videos, audios, subtítulos y metadatos de YouTube y miles de plataformas. Base de muchos pipelines de transcripción.
**Stack:** Python, ffmpeg
**Repo:** https://github.com/yt-dlp/yt-dlp

**Instalación** [~]: `git clone https://github.com/yt-dlp/yt-dlp && cd yt-dlp && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas bajar audio o video de la web
**Evita si:** solo necesitas metadatos sociales; mira `instaloader`
**Combina con:** `whisperx`, `ffmpeg`, `fabric`
