[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 3. Frameworks & Orquestación de Agentes](03-frameworks-orquestaci-n-de-agentes.md) · [5. MCP & Conectividad ➡️](05-mcp-conectividad.md)

# 🕷️ 4. Scraping, Búsqueda & Research Web

> Crawlers que entregan Markdown para IA, scraping guiado por LLM, navegadores automatizados, buscadores y redes sociales.

**29 repos** · 5 subcategorías · ⭐ 1.6M estrellas en total · 🆕 11 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [firecrawl](../fichas/firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. | `npm i @mendable/firecrawl-js` |
| [Scrapegraph-ai](../fichas/scrapegraph-ai.md) | 32.7k | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. | `pip install scrapegraphai` |
| [Stagehand](../fichas/stagehand.md) | 26k | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | `npx create-browser-app` |
| [SearXNG](../fichas/searxng.md) | 39.4k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. | `docker run -d -p 8080:8080 searxng/searxng` |
| [yt-dlp](../fichas/yt-dlp.md) | 207k | Descargador de audio y video por línea de comandos compatible con miles de sitios. | `pip install yt-dlp` |

## 🧭 Subcategorías

- [Crawlers y extracción para IA](#crawlers-y-extracción-para-ia) — 8 repos
- [Scraping guiado por LLM](#scraping-guiado-por-llm) — 3 repos
- [Navegadores y automatización web](#navegadores-y-automatización-web) — 9 repos
- [Búsqueda, monitoreo y research web](#búsqueda-monitoreo-y-research-web) — 6 repos
- [Redes sociales y descarga de medios](#redes-sociales-y-descarga-de-medios) — 3 repos

## Crawlers y extracción para IA

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [firecrawl](../fichas/firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. | alimentas agentes/RAG con web y quieres salida limpia | 🟡 |
| [Scrapling](../fichas/scrapling.md) | 101k | Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. | los sitios cambian o te bloquean a menudo | 🟡 |
| [crawl4ai](../fichas/crawl4ai.md) | 87.2k | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. | necesitas volumen barato y self-host | 🟡 |
| [scrapy](../fichas/scrapy.md) | 65.3k | Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. | quieres un crawler sólido y configurable a escala | 🟡 |
| [crawlee](../fichas/crawlee.md) | 26.4k | Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. | scrapeas con Node y necesitas antibloqueo | 🟡 |
| [Jina Reader](../fichas/jina-reader.md) 🆕 | 12.2k | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. | necesitas leer páginas como Markdown al instante | 🟢 |
| [crawlee-python](../fichas/crawlee-python.md) | 9.7k | Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. | quieres Crawlee en Python con antibloqueo | 🟡 |
| [scrapely](../fichas/scrapely.md) | 1.9k | Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales. | prefieres enseñar por ejemplos y el sitio es homogéneo | 🟢 |

## Scraping guiado por LLM

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Scrapegraph-ai](../fichas/scrapegraph-ai.md) | 32.7k | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. | quieres estructura semántica "by prompt" en Python | 🟡 |
| [Maxun](../fichas/maxun.md) 🆕 | 18.2k | Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. | quieres extraer datos web sin programar | 🟡 |
| [llm-scraper](../fichas/llm-scraper.md) | 7k | Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. | quieres salida tipada y validada en stack TS | 🟢 |

## Navegadores y automatización web

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Stagehand](../fichas/stagehand.md) 🆕 | 26k | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. | quieres automatización web robusta con un toque de IA en TS | 🟢 |
| [browser-use](../fichas/browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. | quieres navegación como humano y tolerancia a cambios de UI | 🟡 |
| [playwright](../fichas/playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. | necesitas control preciso y reproducible del browser | 🟡 |
| [Puppeteer](../fichas/puppeteer.md) 🆕 | 95.8k | Librería de Google para controlar Chrome y Firefox desde Node.js. | trabajas en Node y quieres controlar Chrome | 🟢 |
| [Lightpanda](../fichas/lightpanda.md) 🆕 | 41.8k | Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome. | necesitas muchos navegadores headless con poca memoria | 🟢 |
| [Selenium](../fichas/selenium.md) 🆕 | 34.6k | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. | tu equipo ya usa Selenium o necesitas muchos lenguajes | 🟡 |
| [Skyvern](../fichas/skyvern.md) 🆕 | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. | automatizas portales web que cambian a menudo | 🟡 |
| [Browser Harness](../fichas/browser-harness.md) | 19k | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. | tu agente debe usar tu navegador real con sesión | 🟢 |
| [playwright-cli](../fichas/playwright-cli.md) | 15.1k | Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. | tu agente vive en CLI y el contexto es un recurso caro | 🟢 |

## Búsqueda, monitoreo y research web

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [SearXNG](../fichas/searxng.md) 🆕 | 39.4k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. | tus agentes necesitan buscar en la web sin coste por consulta | 🟢 |
| [Agent-Reach](../fichas/agent-reach.md) | 111k | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. | tu agente necesita leer redes sociales sin APIs de pago | 🟢 |
| [last30days](../fichas/last30days-skill.md) | 67.2k | Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días. | quieres saber qué se dice ahora sobre un tema | 🟢 |
| [Vane](../fichas/vane.md) 🆕 | 38.1k | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). | quieres un buscador con respuestas citadas auto-hospedado | 🟢 |
| [changedetection.io](../fichas/changedetection.md) 🆕 | 35.7k | Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más. | quieres alertas cuando cambia una página | 🟢 |
| [ArchiveBox](../fichas/archivebox.md) | 29k | Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios. | quieres conservar copias fieles de páginas web | 🟢 |

## Redes sociales y descarga de medios

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [yt-dlp](../fichas/yt-dlp.md) 🆕 | 207k | Descargador de audio y video por línea de comandos compatible con miles de sitios. | necesitas bajar audio o video de la web | 🟢 |
| [instaloader](../fichas/instaloader.md) | 13.8k | Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram. | necesitas datos de Instagram de forma fiable | 🟢 |
| [snscrape](../fichas/snscrape.md) | 5.5k | Scraper de redes sociales (Twitter/X, Reddit, Telegram, Instagram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves. | recolectas varias redes y no te sirve una API oficial | 🟢 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### firecrawl, crawl4ai, Jina Reader

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [firecrawl](../fichas/firecrawl.md) | 200k | alimentas agentes/RAG con web y quieres salida limpia | solo quieres HTML crudo o el presupuesto de API no encaja |
| [crawl4ai](../fichas/crawl4ai.md) | 87.2k | necesitas volumen barato y self-host | quieres una API hosted simple sin operar navegadores (firecrawl) |
| [Jina Reader](../fichas/jina-reader.md) | 12.2k | necesitas leer páginas como Markdown al instante | vas a rastrear sitios completos; mira `crawl4ai` o `firecrawl` |

### Scrapegraph-ai, Maxun, llm-scraper

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Scrapegraph-ai](../fichas/scrapegraph-ai.md) | 32.7k | quieres estructura semántica "by prompt" en Python | te basta un esquema simple (llm-scraper) o el coste de LLM por página es alto |
| [Maxun](../fichas/maxun.md) | 18.2k | quieres extraer datos web sin programar | programas y prefieres librerías; mira `crawl4ai` o `scrapy` |
| [llm-scraper](../fichas/llm-scraper.md) | 7k | quieres salida tipada y validada en stack TS | prefieres extracción semántica por grafos (Scrapegraph-ai) o trabajas en Python |

### Stagehand, browser-use, Skyvern

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Stagehand](../fichas/stagehand.md) | 26k | quieres automatización web robusta con un toque de IA en TS | quieres que un agente navegue solo; mira `browser-use` |
| [browser-use](../fichas/browser-use.md) | 121k | quieres navegación como humano y tolerancia a cambios de UI | necesitas scripts deterministas y baratos (playwright) o no quieres depender de un LLM por paso |
| [Skyvern](../fichas/skyvern.md) | 23.4k | automatizas portales web que cambian a menudo | necesitas scraping masivo y barato; mira `crawl4ai` |

### playwright, Puppeteer, Selenium

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [playwright](../fichas/playwright.md) | 99.7k | necesitas control preciso y reproducible del browser | quieres que el agente navegue por visión (browser-use) o no necesitas un navegador real |
| [Puppeteer](../fichas/puppeteer.md) | 95.8k | trabajas en Node y quieres controlar Chrome | necesitas varios navegadores y pruebas E2E; mira `playwright` |
| [Selenium](../fichas/selenium.md) | 34.6k | tu equipo ya usa Selenium o necesitas muchos lenguajes | empiezas de cero; mira `playwright` |

### Agent-Reach, snscrape

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Agent-Reach](../fichas/agent-reach.md) | 111k | tu agente necesita leer redes sociales sin APIs de pago | necesitas datos con garantías de términos de servicio |
| [snscrape](../fichas/snscrape.md) | 5.5k | recolectas varias redes y no te sirve una API oficial | solo necesitas Instagram (instaloader) o la plataforma ya bloqueó el acceso no oficial |

## 🧪 Recetas que usan esta categoría

- [🔎 Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [🏠 Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.
- [🦙 ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
