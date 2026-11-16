[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Buscar, extraer y monitorear información web

Buscadores, crawlers, extracción y seguimiento de páginas o redes. Para hacer clic y operar interfaces utiliza la sala de navegadores y automatización web.

28 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [firecrawl](../fichas/firecrawl.md) | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. | API de IA opcional |
| [Scrapegraph-ai](../fichas/scrapegraph-ai.md) | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. | Depende de la ruta elegida |
| [SearXNG](../fichas/searxng.md) | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. | Sin clave propia de API de IA en la ruta básica |
| [yt-dlp](../fichas/yt-dlp.md) | Descargador de audio y video por línea de comandos compatible con miles de sitios. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Crawlers y extracción para IA](#crawlers-y-extracción-para-ia) — 11 repos
- [Scraping guiado por LLM](#scraping-guiado-por-llm) — 3 repos
- [Búsqueda, monitoreo y research web](#búsqueda-monitoreo-y-research-web) — 10 repos
- [Redes sociales y descarga de medios](#redes-sociales-y-descarga-de-medios) — 4 repos

## Crawlers y extracción para IA

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [firecrawl](../fichas/firecrawl.md) | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. | Tu objetivo encaja con estos ejemplos: Preparar páginas para un buscador documental; Crear un mapa de URLs de una web propia | API de IA opcional |
| [Scrapling](../fichas/scrapling.md) | Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. | Tu objetivo encaja con estos ejemplos: Recopilar un catálogo público permitido; Extraer texto para un índice de búsqueda | Sin clave propia de API de IA en la ruta básica |
| [crawl4ai](../fichas/crawl4ai.md) | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. | Tu objetivo encaja con estos ejemplos: Preparar artículos para RAG; Extraer datos estructurados con un modelo local | API de IA opcional |
| [scrapy](../fichas/scrapy.md) | Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. | Tu objetivo encaja con estos ejemplos: Recopilar listados públicos permitidos; Programar extracción repetible con pipelines | Sin clave propia de API de IA en la ruta básica |
| [crawlee](../fichas/crawlee.md) | Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. | Tu objetivo encaja con estos ejemplos: Rastrear una documentación propia; Extraer datos de páginas con JavaScript | Sin clave propia de API de IA en la ruta básica |
| [Colly](../fichas/colly.md) | Framework de scraping y crawling para Go: callbacks por selector, límites por dominio, caché, cookies y ejecución paralela. | Tu objetivo encaja con estos ejemplos: escribir un rastreador rápido que extraiga datos estructurados de un sitio; archivar páginas de un dominio respetando límites de velocidad | Sin clave propia de API de IA en la ruta básica |
| [Katana](../fichas/katana.md) | Crawler web de ProjectDiscovery en Go, en modo estándar o headless, con análisis de JavaScript, control de alcance y salida JSON. | Tu objetivo encaja con estos ejemplos: descubrir los endpoints de una aplicación propia antes de una auditoría autorizada; mapear rutas generadas por JavaScript en un sitio de pruebas | Sin clave propia de API de IA en la ruta básica |
| [Jina Reader](../fichas/jina-reader.md) | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. | Tu objetivo encaja con estos ejemplos: Convertir un artículo a texto para consulta; Preparar una página para un índice documental | Sin clave propia de API de IA en la ruta básica |
| [defuddle](../fichas/defuddle.md) | Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable. | Tu objetivo encaja con estos ejemplos: Preparar artículos para lectura; Limpiar HTML antes de indexarlo | Sin clave propia de API de IA en la ruta básica |
| [crawlee-python](../fichas/crawlee-python.md) | Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. | Tu objetivo encaja con estos ejemplos: Recopilar documentos públicos; Crear un crawler con reintentos y exportación | API de IA opcional |
| [awesome-web-scraping](../fichas/awesome-web-scraping.md) | Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos. | Tu objetivo encaja con estos ejemplos: Buscar un parser para Python; Encontrar herramientas de extracción para JavaScript | Sin clave propia de API de IA en la ruta básica |

## Scraping guiado por LLM

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Scrapegraph-ai](../fichas/scrapegraph-ai.md) | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. | Tu objetivo encaja con estos ejemplos: Extraer fichas de productos; Transformar artículos en registros estructurados | Depende de la ruta elegida |
| [Maxun](../fichas/maxun.md) | Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. | Tu objetivo encaja con estos ejemplos: Convertir un listado en datos consultables; Monitorear cambios de un catálogo | API de IA opcional |
| [llm-scraper](../fichas/llm-scraper.md) | Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. | Tu objetivo encaja con estos ejemplos: Extraer campos sin escribir selectores específicos; Normalizar información de páginas similares | Depende de la ruta elegida |

## Búsqueda, monitoreo y research web

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [SearXNG](../fichas/searxng.md) | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. | Tu objetivo encaja con estos ejemplos: Añadir búsqueda a una herramienta de investigación; Disponer de un metabuscador propio | Sin clave propia de API de IA en la ruta básica |
| [Agent-Reach](../fichas/agent-reach.md) | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. | Tu objetivo encaja con estos ejemplos: Leer una discusión pública para investigación; Obtener transcripciones de un video permitido | API de IA opcional |
| [last30days](../fichas/last30days-skill.md) | Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días. | Tu objetivo encaja con estos ejemplos: Preparar una reunión sobre una empresa; Revisar novedades de una herramienta | API de IA opcional |
| [RSSHub](../fichas/rsshub.md) | Generador de feeds RSS para miles de webs y redes sin RSS propio; instancia pública o autoalojada con Docker. | Tu objetivo encaja con estos ejemplos: seguir canales, perfiles o webs sin RSS desde tu lector de feeds; alimentar un flujo de monitorización de fuentes con feeds uniformes | Sin clave propia de API de IA en la ruta básica |
| [Vane](../fichas/vane.md) | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). | Tu objetivo encaja con estos ejemplos: Investigar un tema con citas; Consultar la web usando Ollama | Depende de la ruta elegida |
| [changedetection.io](../fichas/changedetection.md) | Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más. | Tu objetivo encaja con estos ejemplos: Detectar cambios de precio permitidos; Monitorear avisos de una página | API de IA opcional |
| [ArchiveBox](../fichas/archivebox.md) | Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios. | Tu objetivo encaja con estos ejemplos: Preservar documentación que cambia; Crear una biblioteca de fuentes de una investigación | Sin clave propia de API de IA en la ruta básica |
| [FreshRSS](../fichas/freshrss.md) | Agregador de noticias RSS autoalojado, ligero y multiusuario, con API para apps móviles, WebSub, extracción por XPath y extensiones. | Tu objetivo encaja con estos ejemplos: centralizar en tu servidor los feeds de noticias y blogs que sigues; seguir webs sin RSS con reglas de extracción XPath | Sin clave propia de API de IA en la ruta básica |
| [wallabag](../fichas/wallabag.md) | Aplicación autoalojada para guardar páginas web y leerlas más tarde sin distracciones, con apps móviles y extensión de navegador. | Tu objetivo encaja con estos ejemplos: guardar artículos para leerlos sin conexión en el móvil; archivar lecturas con etiquetas y anotaciones en tu propio servidor | Sin clave propia de API de IA en la ruta básica |
| [Miniflux](../fichas/miniflux.md) | Lector de feeds minimalista y rápido en Go sobre PostgreSQL, con privacidad, búsqueda de texto completo y más de 25 integraciones. | Tu objetivo encaja con estos ejemplos: leer feeds sin rastreadores en una instancia propia ligera; enviar artículos automáticamente a un servicio de lectura o notas | Sin clave propia de API de IA en la ruta básica |

## Redes sociales y descarga de medios

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [yt-dlp](../fichas/yt-dlp.md) | Descargador de audio y video por línea de comandos compatible con miles de sitios. | Tu objetivo encaja con estos ejemplos: Respaldar videos propios; Obtener medios permitidos para edición | Sin clave propia de API de IA en la ruta básica |
| [spotDL](../fichas/spotdl.md) | CLI que toma listas y canciones de Spotify, busca coincidencias en YouTube y las descarga con carátula, letras y metadatos. | Tu objetivo encaja con estos ejemplos: conservar una copia local de listas de reproducción propias; etiquetar automáticamente archivos de audio con metadatos de Spotify | Sin clave propia de API de IA en la ruta básica |
| [gallery-dl](../fichas/gallery-dl.md) | Programa de línea de comandos para descargar galerías y colecciones de imágenes de muchos sitios, con nombres de archivo configurables. | Tu objetivo encaja con estos ejemplos: archivar una colección propia de imágenes con metadatos y nombres ordenados; descargar un conjunto de imágenes públicas para un dataset con permiso de uso | Sin clave propia de API de IA en la ruta básica |
| [instaloader](../fichas/instaloader.md) | Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram. | Tu objetivo encaja con estos ejemplos: Respaldar publicaciones propias; Actualizar una colección autorizada sin repetir todo | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Preparar chat, documentos y memoria con rutas locales, comprobando por separado modelos, herramientas y conexiones externas.
- [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
