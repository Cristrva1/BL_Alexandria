# 4. Scraping, Búsqueda & Research Web — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `archivebox`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** ▶️ <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Quickstart">Quickstart</a> | <a href="https://demo.archivebox.io">Demo</a> | <a href="https://github.com/ArchiveBox/ArchiveBox">GitHub</a> | <a href="https://github.com/ArchiveBox/ArchiveBox/wiki">Documentation</a> | <a href="#background--motivation">Info & Motivation</a> | <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Web-Archivin
**Stack:** python, typescript, javascript, docker
**Repo:** https://github.com/ArchiveBox/ArchiveBox.git

**Instalación** [~]: `git clone https://github.com/ArchiveBox/ArchiveBox.git && cd ArchiveBox && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres <div align="center" style="text-align: center; width: 100%">
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `browser-use`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic']

**Qué es:** biblioteca que da a los LLMs la capacidad de usar navegadores reales con interfaz para modelos de visión, dejando que el agente perciba la pantalla y actúe sin selectores fijos.
**Stack:** Python 3.11+, Rust (core), Playwright
**Repo:** https://github.com/browser-use/browser-use

**Instalación** [~]: `pip install browser-use   (o: uv add browser-use)`
_Nombre PyPI puede diferir de 'browser-use'; verifica en pypi.org._

**Elige si:** quieres navegación como humano
**Evita si:** necesitas scripts deterministas ([playwright](#-playwright)).
**Combina con:** `playwright`, `gpt-researcher`
**Alternativas (elige una):** `playwright`

## `crawl4ai`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA.
**Stack:** Python
**Repo:** https://github.com/unclecode/crawl4ai

**Instalación** [~]: `pip install crawl4ai   (o: uv add crawl4ai)`
_Nombre PyPI puede diferir de 'crawl4ai'; verifica en pypi.org._

**Elige si:** necesitas volumen barato
**Evita si:** quieres una API hosted simple ([firecrawl](#-firecrawl)).
**Combina con:** `firecrawl`, `gpt-researcher`
**Alternativas (elige una):** `firecrawl`

## `crawlee`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** framework moderno de crawling para Node.js con antibloqueo integrado, unifico scraping de HTTP y de navegador bajo una misma API con colas y reintentos.
**Stack:** Node.js/TypeScript
**Repo:** https://github.com/apify/crawlee

**Instalación** [~]: `npm install crawlee   (o: pnpm add crawlee)`
_Nombre npm puede diferir de 'crawlee'; verifica en npmjs.com._

**Elige si:** scrapeas con Node
**Evita si:** trabajas en Python ([crawlee-python](#-crawlee-python)).
**Combina con:** `playwright`
**Alternativas (elige una):** `crawlee-python`

## `crawlee-python`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python.
**Stack:** Python
**Repo:** https://github.com/apify/crawlee-python

**Instalación** [~]: `pip install crawlee   (o: uv add crawlee)`
_Nombre PyPI puede diferir de 'crawlee-python'; verifica en pypi.org._

**Elige si:** quieres Crawlee en Python
**Evita si:** ya usas scrapy y te basta.
**Combina con:** `scrapy`, `playwright`

## `firecrawl`
role=platform · exec=cloud · setup=medium · mcp=True · prov=['mcp']

**Qué es:** plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript.
**Stack:** API/SDK, hosted o self-host
**Repo:** https://github.com/firecrawl/firecrawl

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** alimentas agentes con web
**Evita si:** solo quieres HTML crudo.
**Combina con:** `gpt-researcher`, `crawl4ai`

## `instaloader`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram.
**Stack:** Python
**Repo:** https://github.com/instaloader/instaloader

**Instalación** [~]: `pip install instaloader   (o: uv add instaloader)`
_Nombre PyPI puede diferir de 'instaloader'; verifica en pypi.org._

**Elige si:** necesitas datos de Instagram
**Evita si:** quieres varias redes ([snscrape](#-snscrape)).
**Combina con:** `snscrape`
**Alternativas (elige una):** `snscrape`

## `llm-scraper`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.
**Stack:** TypeScript
**Repo:** https://github.com/mishushakov/llm-scraper

**Instalación** [~]: `npm install llm-scraper   (o: pnpm add llm-scraper)`
_Nombre npm puede diferir de 'llm-scraper'; verifica en npmjs.com._

**Elige si:** quieres salida tipada
**Evita si:** prefieres extracción semántica por grafos ([Scrapegraph-ai](#-scrapegraph-ai)).
**Combina con:** `playwright`, `firecrawl`
**Alternativas (elige una):** `scrapegraph-ai`

## `normalize.css`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** src="https://necolas.github.io/normalize.css/logo.svg" alt="Normalize Logo" width="80" height="80" align="right"></a>.
**Stack:** javascript/typescript, typescript, javascript
**Repo:** https://github.com/necolas/normalize.css.git

**Instalación** [~]: `npm install normalize.css   (o: pnpm add normalize.css)`
_Nombre npm puede diferir de 'normalize.css'; verifica en npmjs.com._

**Elige si:** —
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `playwright`
role=library · exec=hybrid · setup=medium · mcp=True · prov=['anthropic', 'mcp']

**Qué es:** framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.
**Stack:** Node.js o Python
**Repo:** https://github.com/microsoft/playwright

**Instalación** [~]: `pip install playwright   (o: uv add playwright)`
_Nombre PyPI puede diferir de 'playwright'; verifica en pypi.org._

**Elige si:** necesitas control preciso del browser
**Evita si:** quieres que el agente navegue por visión ([browser-use](#-browser-use)).
**Combina con:** `browser-use`, `crawlee`
**Alternativas (elige una):** `browser-use`

## `playwright-cli`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=['anthropic', 'mcp']

**Qué es:** interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto.
**Stack:** TypeScript/CLI
**Repo:** https://github.com/microsoft/playwright

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/playwright-cli/). Si necesitas el código: git clone https://github.com/microsoft/playwright`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** tu agente vive en CLI
**Evita si:** necesitas estado persistente (usa Playwright MCP).
**Combina con:** `playwright`

## `scrapegraph-ai`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'mcp', 'local']

**Qué es:** framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping.
**Stack:** Python
**Repo:** https://github.com/ScrapeGraphAI/Scrapegraph-ai

**Instalación** [~]: `pip install scrapegraph-ai   (o: uv add scrapegraph-ai)`
_Nombre PyPI puede diferir de 'Scrapegraph-ai'; verifica en pypi.org._

**Elige si:** quieres estructura semántica
**Evita si:** te basta un esquema simple ([llm-scraper](#-llm-scraper)).
**Combina con:** `crawl4ai`, `graphrag`
**Alternativas (elige una):** `llm-scraper`

## `scrapely`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales.
**Stack:** Python
**Repo:** https://github.com/scrapy/scrapely

**Instalación** [~]: `pip install scrapely   (o: uv add scrapely)`
_Nombre PyPI puede diferir de 'scrapely'; verifica en pypi.org._

**Elige si:** prefieres enseñar por ejemplos
**Evita si:** necesitas un crawler completo.
**Combina con:** `scrapy`

## `scrapling`
role=library · exec=local · setup=medium · mcp=False · prov=['mcp']

**Qué es:** librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.
**Stack:** Python
**Repo:** https://github.com/D4Vinci/Scrapling

**Instalación** [~]: `pip install scrapling   (o: uv add scrapling)`
_Nombre PyPI puede diferir de 'Scrapling'; verifica en pypi.org._

**Elige si:** los sitios cambian o te bloquean
**Evita si:** el target es estable y simple.
**Combina con:** `scrapy`

## `scrapy`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala.
**Stack:** Python
**Repo:** https://github.com/scrapy/scrapy

**Instalación** [~]: `pip install scrapy   (o: uv add scrapy)`
_Nombre PyPI puede diferir de 'scrapy'; verifica en pypi.org._

**Elige si:** quieres un crawler sólido y configurable
**Evita si:** buscas salida lista para LLM.
**Combina con:** `scrapely`, `crawlee-python`

## `snscrape`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** scraper de redes sociales (Twitter/X, Reddit, Telegram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves.
**Stack:** Python
**Repo:** https://github.com/JustAnotherArchivist/snscrape

**Instalación** [~]: `pip install snscrape   (o: uv add snscrape)`
_Nombre PyPI puede diferir de 'snscrape'; verifica en pypi.org._

**Elige si:** recolectas varias redes
**Evita si:** solo necesitas Instagram ([instaloader](#-instaloader)).
**Combina con:** `instaloader`
**Alternativas (elige una):** `instaloader`
