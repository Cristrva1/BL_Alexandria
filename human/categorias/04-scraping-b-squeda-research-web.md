[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Buscar y extraer información web

Buscadores, crawlers y navegadores. Usa un crawler para extraer páginas, un navegador para interactuar y un agente para investigar con un modelo.

35 repos · 5 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [firecrawl](../fichas/firecrawl.md) | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. | Depende de la ruta elegida |
| [Scrapegraph-ai](../fichas/scrapegraph-ai.md) | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. | Sin API de IA en la ruta básica |
| [Stagehand](../fichas/stagehand.md) | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | Depende de la ruta elegida |
| [SearXNG](../fichas/searxng.md) | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. | Sin API de IA en la ruta básica |
| [yt-dlp](../fichas/yt-dlp.md) | Descargador de audio y video por línea de comandos compatible con miles de sitios. | Sin API de IA en la ruta básica |

## Secciones

- [Crawlers y extracción para IA](#crawlers-y-extracción-para-ia) — 11 repos
- [Scraping guiado por LLM](#scraping-guiado-por-llm) — 3 repos
- [Navegadores y automatización web](#navegadores-y-automatización-web) — 12 repos
- [Búsqueda, monitoreo y research web](#búsqueda-monitoreo-y-research-web) — 6 repos
- [Redes sociales y descarga de medios](#redes-sociales-y-descarga-de-medios) — 3 repos

## Crawlers y extracción para IA

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [firecrawl](../fichas/firecrawl.md) | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. | alimentas agentes/RAG con web y quieres salida limpia | Depende de la ruta elegida |
| [Scrapling](../fichas/scrapling.md) | Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. | los sitios cambian o te bloquean a menudo | Sin API de IA en la ruta básica |
| [crawl4ai](../fichas/crawl4ai.md) | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. | necesitas volumen barato y self-host | API de IA opcional |
| [scrapy](../fichas/scrapy.md) | Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. | quieres un crawler sólido y configurable a escala | Sin API de IA en la ruta básica |
| [crawlee](../fichas/crawlee.md) | Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. | scrapeas con Node y necesitas antibloqueo | Sin API de IA en la ruta básica |
| [Jina Reader](../fichas/jina-reader.md) | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. | necesitas leer páginas como Markdown al instante | Depende de la ruta elegida |
| [defuddle](../fichas/defuddle.md) | Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable. | buscas esta función: Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable. | Sin API de IA en la ruta básica |
| [crawlee-python](../fichas/crawlee-python.md) | Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. | quieres Crawlee en Python con antibloqueo | Sin API de IA en la ruta básica |
| [awesome-web-scraping](../fichas/awesome-web-scraping.md) | Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos. | quieres comparar librerías de scraping antes de elegir tu stack | Sin API de IA en la ruta básica |
| [scrapydweb](../fichas/scrapydweb.md) | Panel web para administrar clústeres de Scrapyd y consultar trabajos, logs y estadísticas de Scrapy. | operas varios spiders de Scrapy y necesitas un panel de administración | Sin API de IA en la ruta básica |
| [scrapely](../fichas/scrapely.md) | Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales. | prefieres enseñar por ejemplos y el sitio es homogéneo | Sin API de IA en la ruta básica |

## Scraping guiado por LLM

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Scrapegraph-ai](../fichas/scrapegraph-ai.md) | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. | quieres estructura semántica "by prompt" en Python | Sin API de IA en la ruta básica |
| [Maxun](../fichas/maxun.md) | Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. | quieres extraer datos web sin programar | Depende de la ruta elegida |
| [llm-scraper](../fichas/llm-scraper.md) | Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. | quieres salida tipada y validada en stack TS | Sin API de IA en la ruta básica |

## Navegadores y automatización web

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Stagehand](../fichas/stagehand.md) | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | quieres automatización web robusta con un toque de IA en TS | Depende de la ruta elegida |
| [browser-use](../fichas/browser-use.md) | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. | quieres navegación como humano y tolerancia a cambios de UI | Depende de la ruta elegida |
| [playwright](../fichas/playwright.md) | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. | necesitas control preciso y reproducible del browser | Sin API de IA en la ruta básica |
| [Puppeteer](../fichas/puppeteer.md) | Librería de Google para controlar Chrome y Firefox desde Node.js. | trabajas en Node y quieres controlar Chrome | Sin API de IA en la ruta básica |
| [agent-browser](../fichas/agent-browser.md) | CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. | necesitas navegación programable con salidas compactas para un agente | Sin API de IA en la ruta básica |
| [Lightpanda](../fichas/lightpanda.md) | Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome. | necesitas muchos navegadores headless con poca memoria | Sin API de IA en la ruta básica |
| [Selenium](../fichas/selenium.md) | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. | tu equipo ya usa Selenium o necesitas muchos lenguajes | Sin API de IA en la ruta básica |
| [Skyvern](../fichas/skyvern.md) | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. | automatizas portales web que cambian a menudo | Sin API de IA en la ruta básica |
| [Browser Harness](../fichas/browser-harness.md) | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. | tu agente debe usar tu navegador real con sesión | Sin API de IA en la ruta básica |
| [playwright-cli](../fichas/playwright-cli.md) | Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. | tu agente vive en CLI y el contexto es un recurso caro | Sin API de IA en la ruta básica |
| [camofox-browser](../fichas/camofox-browser.md) | Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes. | necesitas evaluar una alternativa de navegador automatizado para agentes | Sin API de IA en la ruta básica |
| [awesome-chrome-devtools](../fichas/awesome-chrome-devtools.md) | Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol. | buscas utilidades para depurar o automatizar Chrome | Sin API de IA en la ruta básica |

## Búsqueda, monitoreo y research web

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [SearXNG](../fichas/searxng.md) | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. | tus agentes necesitan buscar en la web sin coste por consulta | Sin API de IA en la ruta básica |
| [Agent-Reach](../fichas/agent-reach.md) | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. | tu agente necesita leer redes sociales sin APIs de pago | Depende de la ruta elegida |
| [last30days](../fichas/last30days-skill.md) | Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días. | quieres saber qué se dice ahora sobre un tema | Sin API de IA en la ruta básica |
| [Vane](../fichas/vane.md) | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). | quieres un buscador con respuestas citadas auto-hospedado | Sin API de IA en la ruta básica |
| [changedetection.io](../fichas/changedetection.md) | Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más. | quieres alertas cuando cambia una página | API de IA opcional |
| [ArchiveBox](../fichas/archivebox.md) | Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios. | quieres conservar copias fieles de páginas web | API de IA opcional |

## Redes sociales y descarga de medios

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [yt-dlp](../fichas/yt-dlp.md) | Descargador de audio y video por línea de comandos compatible con miles de sitios. | necesitas bajar audio o video de la web | Sin API de IA en la ruta básica |
| [instaloader](../fichas/instaloader.md) | Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram. | necesitas datos de Instagram de forma fiable | Sin API de IA en la ruta básica |
| [snscrape](../fichas/snscrape.md) | Scraper de redes sociales (Twitter/X, Reddit, Telegram, Instagram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves. | recolectas varias redes y no te sirve una API oficial | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.
- [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
