# 4. Scraping, Búsqueda & Research Web — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `archivebox`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** ▶️ Quickstart | Demo | GitHub | Documentation | Info & Motivation | Communi.
**Stack:** python, typescript, javascript, docker, postgres
**Repo:** https://github.com/ArchiveBox/ArchiveBox.git

**Instalación** [~]: `git clone https://github.com/ArchiveBox/ArchiveBox.git && cd ArchiveBox && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres ▶️ <a href="https://github.com/archivebox/archivebox/wiki/quickstart">quickstart
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `crawl4ai`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** 🚀 Crawl4AI Cloud API — Closed Beta (Launching Soon) Reliable, large-scale web extraction, now built to be _**drastically more cost-effective**_ than any of the existing solutions.
**Stack:** python, typescript, javascript, react, docker, postgres, fastapi
**Repo:** https://github.com/unclecode/crawl4ai.git

**Instalación** [~]: `git clone https://github.com/unclecode/crawl4ai.git && cd crawl4ai && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres 🚀🤖 crawl4ai: open-source llm friendly web crawler & scraper.
**Evita si:** —
**Combina con:** `firecrawl`, `scrapy`, `crawlee`

## `crawlee`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Crawlee covers your crawling and scraping end-to-end and **helps you build reliable scrapers. Fast.**.
**Stack:** javascript/typescript, python, typescript, javascript, react, docker
**Repo:** https://github.com/apify/crawlee.git

**Instalación** [~]: `git clone https://github.com/apify/crawlee.git && cd crawlee && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres crawlee covers your crawling and scraping end-to-end and **helps you build relia
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `crawlee-python`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Crawlee covers your crawling and scraping end-to-end and **helps you build reliable scrapers. Fast.**.
**Stack:** python, typescript, javascript, react
**Repo:** https://github.com/apify/crawlee-python.git

**Instalación** [~]: `pip install crawlee   (o: uv add crawlee)`
_Nombre PyPI puede diferir de 'crawlee-python'; verifica en pypi.org._

**Elige si:** quieres crawlee covers your crawling and scraping end-to-end and **helps you build relia
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `firecrawl`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** src="https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/firecrawl_logo.png".
**Stack:** python, typescript, javascript, docker
**Repo:** https://github.com/firecrawl/firecrawl.git

**Instalación** [~]: `pip install firecrawl   (o: uv add firecrawl)`
_Nombre PyPI puede diferir de 'firecrawl'; verifica en pypi.org._

**Elige si:** quieres src="https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/firecrawl_lo
**Evita si:** —
**Combina con:** `crawl4ai`, `scrapy`, `crawlee`

## `how-to-train-your-gpt`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** A guide to building a world-class language model from absolute scratch. Taught like you're five. Built like you're an engineer.*.
**Stack:** python, typescript
**Repo:** https://github.com/raiyanyahya/how-to-train-your-gpt.git

**Instalación** [~]: `git clone https://github.com/raiyanyahya/how-to-train-your-gpt.git && cd how-to-train-your-gpt && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres 🧠 how to train your gpt
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `instaloader`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** .. |pypi| image:: https://img.shields.io/pypi/v/instaloader.svg :alt: Instaloader PyPI Project Page :target: https://pypi.org/project/instaloader/.
**Stack:** python, typescript
**Repo:** https://github.com/instaloader/instaloader.git

**Instalación** [~]: `pip install instaloader   (o: uv add instaloader)`
_Nombre PyPI puede diferir de 'instaloader'; verifica en pypi.org._

**Elige si:** quieres .. image:: https://raw.githubusercontent.com/instaloader/instaloader/master/docs/logo_head
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `llm-scraper`
role=platform · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** LLM Scraper is a TypeScript library that allows you to extract structured data from **any** webpage using LLMs.
**Stack:** javascript/typescript, typescript, javascript
**Repo:** https://github.com/mishushakov/llm-scraper.git

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres llm scraper
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `motion`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** An open source animation library for JavaScript, React and Vue.
**Stack:** javascript/typescript, typescript, javascript, react
**Repo:** https://github.com/motiondivision/motion.git

**Instalación** [~]: `git clone https://github.com/motiondivision/motion.git && cd motion && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres <img width="35" height="35" alt="motion logo" src="https://github.com/user-attachments/ass
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `normalize.css`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** src="https://necolas.github.io/normalize.css/logo.svg" alt="Normalize Logo" width="80" height="80" align="right"> .
**Stack:** javascript/typescript, typescript, javascript
**Repo:** https://github.com/necolas/normalize.css.git

**Instalación** [~]: `npm install normalize.css   (o: pnpm add normalize.css)`
_Nombre npm puede diferir de 'normalize.css'; verifica en npmjs.com._

**Elige si:** —
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `odysseus`
role=skill · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** A self-hosted AI workspace for chat, agents, research, documents, email, notes, calendar, and local model workflows.
**Stack:** python, typescript, javascript, docker, postgres
**Repo:** https://github.com/pewdiepie-archdaemon/odysseus.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/odysseus/). Si necesitas el código: git clone https://github.com/pewdiepie-archdaemon/odysseus.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres a self-hosted ai workspace for chat, agents, research, documents, email, notes,
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `scrapegraph-ai`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** 🕷️ ScrapeGraphAI: You Only Scrape Once.
**Stack:** python, typescript, javascript, docker, langchain
**Repo:** https://github.com/ScrapeGraphAI/Scrapegraph-ai.git

**Instalación** [~]: `git clone https://github.com/ScrapeGraphAI/Scrapegraph-ai.git && cd Scrapegraph-ai && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres 🚀 **looking for an even faster and simpler way to scrape at scale (only 5 lines of code)?*
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `scrapely`
role=library · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** .. image:: https://api.travis-ci.org/scrapy/scrapely.svg?branch=master :target: https://travis-ci.org/scrapy/scrapely.
**Stack:** python, typescript, javascript
**Repo:** https://github.com/scrapy/scrapely.git

**Instalación** [~]: `pip install scrapely   (o: uv add scrapely)`
_Nombre PyPI puede diferir de 'scrapely'; verifica en pypi.org._

**Elige si:** quieres ========
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`

## `scrapy`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** :target: https://scrapy.org.
**Stack:** python
**Repo:** https://github.com/scrapy/scrapy.git

**Instalación** [~]: `pip install scrapy   (o: uv add scrapy)`
_Nombre PyPI puede diferir de 'scrapy'; verifica en pypi.org._

**Elige si:** quieres .. |logo| image:: https://raw.githubusercontent.com/scrapy/scrapy/master/docs/_static/logo
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `crawlee`

## `snscrape`
role=directory · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.
**Stack:** python, typescript
**Repo:** https://github.com/JustAnotherArchivist/snscrape.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/snscrape/). Si necesitas el código: git clone https://github.com/JustAnotherArchivist/snscrape.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** —
**Evita si:** —
**Combina con:** `firecrawl`, `crawl4ai`, `scrapy`
