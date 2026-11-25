# Alexandría para agentes · Buscar, extraer y monitorear información web

Categoría 4 completa (28 repos, 4 subcategorías). Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=4 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `scrapy` | crawlers | Framework clásico y maduro de scraping y crawling en Python, con arquitectura… | 2 Intermedio | 77 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `crawl4ai` | crawlers | Librería open-source de crawling y extracción web a gran escala con foco en… | 2 Intermedio | 72 | Apache-2.0 (OSI permisiva) | recomendado |
| `firecrawl` | crawlers | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a… | 2 Intermedio | 71 | AGPL-3.0 (OSI copyleft) | alternativa |
| `scrapling` | crawlers | Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de… | 2 Intermedio | 69 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `crawlee-python` | crawlers | Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y… | 2 Intermedio | 66 | Apache-2.0 (OSI permisiva) | recomendado |
| `katana` | crawlers | Crawler web de ProjectDiscovery en Go, en modo estándar o headless, con… | 1 Básico | 66 | MIT (OSI permisiva) | sin grupo |
| `crawlee` | crawlers | Framework moderno de crawling para Node.js con antibloqueo integrado, que… | 2 Intermedio | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `defuddle` | crawlers | Biblioteca para extraer el contenido principal de una página y convertirlo en… | 2 Intermedio | 57 | MIT (OSI permisiva) | sin grupo |
| `colly` | crawlers | Framework de scraping y crawling para Go: callbacks por selector, límites por… | 2 Intermedio | 53 | Apache-2.0 (OSI permisiva) | sin grupo |
| `jina-reader` | crawlers | Servicio que convierte cualquier URL en Markdown listo para LLM con solo… | 1 Básico | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `awesome-web-scraping` | crawlers | Directorio de bibliotecas, herramientas y recursos para scraping web y… | 1 Básico | 48 | CC-BY-4.0 (OSI permisiva) | sin grupo |
| `maxun` | llm | Plataforma sin código para convertir sitios web en APIs y hojas de datos… | 2 Intermedio | 70 | AGPL-3.0 (OSI copyleft) | alternativa |
| `scrapegraph-ai` | llm | Framework de scraping en Python basado en grafos potenciado por LLM, donde… | 2 Intermedio | 70 | MIT (OSI permisiva) | recomendado |
| `llm-scraper` | llm | Librería TypeScript que convierte cualquier página web en datos estructurados… | 2 Intermedio | 47 | MIT (OSI permisiva) | alternativa |
| `last30days-skill` | busqueda | Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket… | 1 Básico | 73 | MIT (OSI permisiva) | sin grupo |
| `rsshub` | busqueda | Generador de feeds RSS para miles de webs y redes sin RSS propio; instancia… | 1 Básico | 73 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `changedetection` | busqueda | Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más. | 1 Básico | 70 | Apache-2.0 (OSI permisiva) | sin grupo |
| `searxng` | busqueda | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal… | 1 Básico | 69 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `agent-reach` | busqueda | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube… | 1 Básico | 67 | MIT (OSI permisiva) | sin grupo |
| `archivebox` | busqueda | Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y… | 1 Básico | 66 | MIT (OSI permisiva) | sin grupo |
| `freshrss` | busqueda | Agregador de noticias RSS autoalojado, ligero y multiusuario, con API para apps… | 1 Básico | 65 | AGPL-3.0 (OSI copyleft) | recomendado |
| `miniflux` | busqueda | Lector de feeds minimalista y rápido en Go sobre PostgreSQL, con privacidad… | 1 Básico | 58 | Apache-2.0 (OSI permisiva) | alternativa |
| `wallabag` | busqueda | Aplicación autoalojada para guardar páginas web y leerlas más tarde sin… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `vane` | busqueda | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity… | 1 Básico | 57 | MIT (OSI permisiva) | sin grupo |
| `yt-dlp` | social | Descargador de audio y video por línea de comandos compatible con miles de… | 1 Básico | 80 | Unlicense (OSI permisiva) | sin grupo |
| `spotdl` | social | CLI que toma listas y canciones de Spotify, busca coincidencias en YouTube y… | 1 Básico | 64 | MIT (OSI permisiva) | sin grupo |
| `instaloader` | social | Herramienta y librería Python para descargar fotos, videos, stories, leyendas y… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `gallery-dl` | social | Programa de línea de comandos para descargar galerías y colecciones de imágenes… | 1 Básico | 53 | GPL-2.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### scrapy (`scrapy`)

- **Repo:** https://github.com/scrapy/scrapy · BSD-3-Clause · nivel 2 · 77/100
- **Qué es:** Framework de crawling y scraping rápido y de alto nivel para Python, mantenido por Zyte. Licencia BSD-3-Clause. Es el estándar veterano del sector (~65k estrellas, 2.20.0).
- **Cuándo elegirlo:** Casos: Recopilar listados públicos permitidos; Programar extracción repetible con pipelines.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python 3.11+; entorno virtual; conocimientos básicos de selectores; hardware prerequisites; API de IA: no; Python 3.11+; entorno virtual; conocimientos básicos de selectores.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install scrapy` — fuente: https://github.com/scrapy/scrapy/blob/master/README.rst
- **Primera prueba propuesta (no ejecutada):** Crea un spider para una página propia con tres productos y exporta sus nombres Éxito: El archivo de salida contiene exactamente los tres productos
- **Combina con:** `playwright` [32/bibliotecas], `scrapling`, `defuddle`, `awesome-web-scraping`, `flaresolverr` [32/bibliotecas]
- **Riesgos y avisos:** Sin alternativas declaradas. Se quita la combinación con crawlee-python por ser frameworks equivalentes. Es un framework de desarrollo, no una app de conversación ni una garantía de acceso a cualquier web.

### crawl4ai (`crawl4ai`)

- **Repo:** https://github.com/unclecode/crawl4ai · Apache-2.0 · nivel 2 · 72/100 · recomendado en «Crawlers que entregan contenido listo para LLM»
- **Qué es:** Crawl4AI, crawler y extractor web orientado a IA de @unclecode. Licencia Apache-2.0. Es muy popular (~87k estrellas, v0.9.5). Este repositorio es el motor de Crawl4AI Cloud, un servicio de pago; se puede usar como librería Python o como…
- **Cuándo elegirlo:** Casos: Preparar artículos para RAG; Extraer datos estructurados con un modelo local.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; dependencias de navegador; clave Cloud solo para servicio alojado; hardware prerequisites; API de IA: opcional; Python; dependencias de navegador; clave Cloud solo para servicio alojado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/unclecode/crawl4ai/blob/main/README.md

  ```bash
  pip install -U crawl4ai
  crawl4ai-setup        # installs the browser, once
  ```
- **Primera prueba propuesta (no ejecutada):** Convierte una página de prueba a Markdown y después extrae dos campos sin LLM Éxito: Puedes comparar texto y campos con la página
- **Combina con:** `ollama` [8/motores], `qdrant` [6/vectores], `litellm` [23/serving], `tools` [0/hub]
- **Alternativas:** `firecrawl`, `jina-reader`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): jina-reader. firecrawl cumple una función parecida. gpt-researcher no trae un scraper de Crawl4AI (su carpeta de scrapers incluye…. La lectura básica no necesita modelo; no confundas la clave del servicio de crawling con una clave del proveedor LLM.

### firecrawl (`firecrawl`)

- **Repo:** https://github.com/firecrawl/firecrawl · AGPL-3.0 · nivel 2 · 71/100 · alternativa en «Crawlers que entregan contenido listo para LLM»
- **Qué es:** API para buscar, extraer e interactuar con la web a escala, pensada como «API de contexto» para agentes de IA, de Firecrawl. Licencia AGPL-3.0, con servicio alojado de pago. Es muy popular y activo (~202k estrellas, v2.11.0).
- **Cuándo elegirlo:** Casos: Preparar páginas para un buscador documental; Crear un mapa de URLs de una web propia.
- **Requisitos:** nivel 2: preparación media; Node.js; cuenta Firecrawl para la ruta alojada; cliente elegido; hardware prerequisites; API de IA: opcional; Node.js; cuenta Firecrawl para la ruta alojada; cliente elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `npx -y firecrawl-cli@latest init --all --browser` — fuente: https://github.com/firecrawl/firecrawl/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Extrae título y contenido de una página pública de prueba y revisa el Markdown Éxito: Se conserva el contenido principal con la URL de origen
- **Combina con:** `activepieces` [1/motores], `claude-code` [20/terminal], `gpt-researcher` [21/research]
- **Alternativas:** `crawl4ai`, `jina-reader`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): jina-reader. Se quita la combinación con crawl4ai por solaparse como crawler. Hay CLI, skill y MCP stdio; compatibilidad MCP no significa que la suscripción del cliente pague Firecrawl.

### Scrapling (`scrapling`)

- **Repo:** https://github.com/D4Vinci/Scrapling · BSD-3-Clause · nivel 2 · 69/100
- **Qué es:** Framework de web scraping en Python con peticiones HTTP rápidas, navegadores sigilosos, parsing potente y crawling concurrente, creado por @D4Vinci. Licencia BSD-3-Clause.
- **Cuándo elegirlo:** Casos: Recopilar un catálogo público permitido; Extraer texto para un índice de búsqueda.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python 3.10+; navegadores del paquete; extra ai para MCP; hardware prerequisites; API de IA: no; Python 3.10+; navegadores del paquete; extra ai para MCP.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/D4Vinci/Scrapling/blob/main/README.md

  ```bash
  pip install "scrapling[fetchers]"
      
      scrapling install           # normal install
  ```
- **Primera prueba propuesta (no ejecutada):** Extrae nombre y precio de tres productos de una página de prueba mediante selectores Éxito: Obtienes tres registros que coinciden con el HTML
- **Combina con:** `claude-code` [20/terminal], `scrapy`, `defuddle`
- **Riesgos y avisos:** Sin alternativas declaradas. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales. La instalación base solo trae parser; MCP requiere scrapling[ai]; los tres clientes admiten sus transportes estándar sin prueba de instalación aquí.

### crawlee-python (`crawlee-python`)

- **Repo:** https://github.com/apify/crawlee-python · Apache-2.0 · nivel 2 · 66/100 · recomendado en «Crawlee (Node.js y Python)»
- **Qué es:** Versión en Python de Crawlee, la librería de scraping y automatización de navegadores de Apify. Licencia Apache-2.0. Es activa (~10k estrellas, v1.11.2).
- **Cuándo elegirlo:** Casos: Recopilar documentos públicos; Crear un crawler con reintentos y exportación.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; entorno virtual; navegador si eliges Playwright; hardware prerequisites; API de IA: opcional; Python; entorno virtual; navegador si eliges Playwright.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install 'crawlee[all]'` — fuente: https://github.com/apify/crawlee-python/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Recoge enlaces de tres páginas con una cola acotada y guarda sus títulos Éxito: Se controlan duplicados y obtienes los tres registros esperados
- **Combina con:** `playwright` [32/bibliotecas], `scrapegraph-ai` [4/llm], `qdrant` [6/vectores], `flaresolverr` [32/bibliotecas], `camoufox` [32/motores-web]
- **Alternativas:** `crawlee`
- **Riesgos y avisos:** Sin alternativas declaradas. Se quita la combinación con scrapy por ser frameworks equivalentes. Respeta los términos de uso y robots.txt de cada sitio y la…. No atribuyas las necesidades de los módulos de IA a la ruta básica de scraping.

### Katana (`katana`)

- **Repo:** https://github.com/projectdiscovery/katana · MIT · nivel 1 · 66/100
- **Qué es:** Crawler de código abierto (MIT) de ProjectDiscovery, el equipo de nuclei y subfinder. Muy activo y orientado a reconocimiento de seguridad.
- **Cuándo elegirlo:** Casos: descubrir los endpoints de una aplicación propia antes de una auditoría autorizada; mapear rutas generadas por JavaScript en un sitio de pruebas.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install github.com/projectdiscovery/katana/cmd/katana@latest` — fuente: https://github.com/projectdiscovery/katana/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta la imagen Docker oficial contra el sitio de ejemplo books.toscrape.com que usa el README. Éxito: Katana lista las URLs descubiertas sin errores.
- **Combina con:** `mitmproxy` [16/pruebas], `duckdb` [25/datos], `claude-code` [20/terminal], `theharvester` [10/osint], `nuclei` [16/pruebas], `subfinder` [16/reconocimiento]
- **Riesgos y avisos:** Herramienta de reconocimiento: define siempre el alcance permitido antes de ejecutarla.

### crawlee (`crawlee`)

- **Repo:** https://github.com/apify/crawlee · Apache-2.0 · nivel 2 · 65/100 · alternativa en «Crawlee (Node.js y Python)»
- **Qué es:** Librería de web scraping y automatización de navegadores para Node.js, de Apify. Licencia Apache-2.0. Es madura y activa (~26k estrellas, v3.18.2).
- **Cuándo elegirlo:** Casos: Rastrear una documentación propia; Extraer datos de páginas con JavaScript.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node.js >=22.13; npm; navegador si eliges Playwright; hardware prerequisites; API de IA: no; Node.js >=22.13; npm; navegador si eliges Playwright.
- **Instalación (documentada en la fuente; no ejecutada):** `npx crawlee create my-crawler` — fuente: https://github.com/apify/crawlee/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un crawler con límite pequeño y recoge títulos de tres páginas de prueba Éxito: La cola termina y guarda un registro por página
- **Combina con:** `playwright` [32/bibliotecas], `defuddle`, `llm-scraper` [4/llm], `awesome-web-scraping`, `camoufox` [32/motores-web]
- **Alternativas:** `crawlee-python`
- **Riesgos y avisos:** Sin alternativas declaradas. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales. El generador ofrece plantillas; elige HTTP para HTML sencillo y navegador cuando sea necesario.

### defuddle (`defuddle`)

- **Repo:** https://github.com/kepano/defuddle · MIT · nivel 2 · 57/100
- **Qué es:** Librería y CLI que extrae el contenido principal de páginas web, de @kepano. Licencia MIT. Es activa (~10k estrellas, 0.19.6) y el propio README avisa de que sigue en desarrollo.
- **Cuándo elegirlo:** Casos: Preparar artículos para lectura; Limpiar HTML antes de indexarlo.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node.js; archivo HTML de prueba o página pública; hardware prerequisites; API de IA: no; Node.js; archivo HTML de prueba o página pública.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install defuddle` — fuente: https://github.com/kepano/defuddle/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Extrae Markdown de un artículo con menú y comprueba qué texto conserva Éxito: El resultado prioriza el artículo y elimina navegación irrelevante
- **Combina con:** `obsidian-clipper` [15/notas], `obsidian-skills` [15/notas], `crawlee`, `claude-obsidian` [15/notas], `scrapling`, `scrapy`
- **Riesgos y avisos:** Sin alternativas declaradas. En desarrollo: la salida puede cambiar entre versiones. Puede perder información en diseños poco habituales; compara una muestra antes de procesar muchas páginas.

### Colly (`colly`)

- **Repo:** https://github.com/gocolly/colly · Apache-2.0 · nivel 2 · 53/100
- **Qué es:** Biblioteca de scraping de código abierto (Apache-2.0) para Go, mantenida por la comunidad gocolly. Madura y estable en su versión v2; actividad moderada.
- **Cuándo elegirlo:** Casos: escribir un rastreador rápido que extraiga datos estructurados de un sitio; archivar páginas de un dominio respetando límites de velocidad.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Go, go.mod; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/gocolly/colly/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un módulo Go, añade Colly v2 y ejecuta uno de los ejemplos del repositorio contra un sitio de prueba. Éxito: El programa visita las páginas y escribe los campos extraídos en la salida.
- **Combina con:** `duckdb` [25/datos], `polars` [25/datos], `claude-code` [20/terminal]
- **Riesgos y avisos:** Alternativas cercanas en el catálogo: scrapy (Python), crawlee (Node/Python).

### Jina Reader (`jina-reader`)

- **Repo:** https://github.com/jina-ai/reader · Apache-2.0 · nivel 1 · 52/100 · alternativa en «Crawlers que entregan contenido listo para LLM»
- **Qué es:** Reader, de Jina AI: convierte cualquier URL en entrada apta para LLM y busca en la web. Licencia Apache-2.0. Es popular (~12k estrellas, sin releases) y el código abierto se resincronizó con el SaaS en abril de 2026 sin la capa de…
- **Cuándo elegirlo:** Casos: Convertir un artículo a texto para consulta; Preparar una página para un índice documental.
- **Requisitos:** nivel 1: preparación sencilla; Navegador para servicio público; Docker solo para self-hosting; hardware prerequisites; API de IA: no; Navegador para servicio público; Docker solo para self-hosting.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/jina-ai/reader/blob/main/README.md

  ```bash
  docker run --rm -p 3000:8081 ghcr.io/jina-ai/reader:oss
  # then: curl http://localhost:3000/https://example.com
  ```
- **Primera prueba propuesta (no ejecutada):** Antepon r.jina.ai a una URL pública y compara el texto devuelto con la página Éxito: Obtienes contenido legible con su dirección de origen
- **Combina con:** `activepieces` [1/motores], `open-webui` [8/chats], `llama-index` [3/py]
- **Alternativas:** `crawl4ai`, `firecrawl`
- **Riesgos y avisos:** Alternativas (elige una): firecrawl, crawl4ai. El contenedor básico no tiene caché ni control de tasa; localhost usa el puerto HTTP/1.1 del ejemplo.

### awesome-web-scraping (`awesome-web-scraping`)

- **Repo:** https://github.com/lorien/awesome-web-scraping · CC-BY-4.0 · nivel 1 · 48/100
- **Qué es:** Lista de paquetes, servicios y manuales de web scraping, de @lorien. GitHub muestra licencia NOASSERTION. Es una lista veterana (~8k estrellas) que se sigue actualizando.
- **Cuándo elegirlo:** Casos: Buscar un parser para Python; Encontrar herramientas de extracción para JavaScript.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; lenguaje o formato objetivo; hardware prerequisites; API de IA: no; Navegador; lenguaje o formato objetivo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/lorien/awesome-web-scraping/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Elige la lista de tu lenguaje y compara dos bibliotecas por mantenimiento y salida Éxito: Obtienes dos candidatos con sus repositorios originales
- **Combina con:** `scrapy`, `crawlee`, `firecrawl`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. No se instala el directorio entero ni hereda compatibilidad de las herramientas que enumera.

### Maxun (`maxun`)

- **Repo:** https://github.com/getmaxun/maxun · AGPL-3.0 · nivel 2 · 70/100 · alternativa en «Scraping guiado por LLM»
- **Qué es:** Plataforma open source de datos web para scraping, crawling, búsqueda, monitorización y extracción con IA, de getmaxun. Licencia AGPL-3.0. Es activa (~18k estrellas) pero joven (v0.1.0) y muestra patrocinadores de proxies.
- **Cuándo elegirlo:** Casos: Convertir un listado en datos consultables; Monitorear cambios de un catálogo.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker; cuenta local; modelo solo para funciones AI; hardware prerequisites; API de IA: opcional; Docker; cuenta local; modelo solo para funciones AI.
- **Instalación (documentada en la fuente; no ejecutada):** `docker-compose up -d` — fuente: https://github.com/getmaxun/maxun/blob/develop/SETUP.md
- **Primera prueba propuesta (no ejecutada):** Graba un robot que recoge nombres y precios de una página de prueba Éxito: El robot devuelve filas que puedes repetir y comparar
- **Combina con:** `claude-code` [20/terminal], `activepieces` [1/motores], `changedetection` [4/busqueda]
- **Alternativas:** `scrapegraph-ai`, `llm-scraper`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): scrapegraph-ai, llm-scraper. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales. MCP admite HTTP y stdio; la clave de Maxun autoriza el servicio y no sustituye credenciales de modelos.

### Scrapegraph-ai (`scrapegraph-ai`)

- **Repo:** https://github.com/ScrapeGraphAI/Scrapegraph-ai · MIT · nivel 2 · 70/100 · recomendado en «Scraping guiado por LLM»
- **Qué es:** Librería Python de scraping con LLM y grafos, de ScrapeGraphAI. Licencia MIT. Es popular (~33k estrellas, v2.3.1) y el README promociona en primer plano su API comercial.
- **Cuándo elegirlo:** Casos: Extraer fichas de productos; Transformar artículos en registros estructurados.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; Playwright; modelo Ollama o proveedor remoto; hardware prerequisites; API de IA: depends; Python; Playwright; modelo Ollama o proveedor remoto.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/README.md

  ```bash
  pip install scrapegraphai
  
  # IMPORTANT (for fetching websites content)
  playwright install
  ```
- **Primera prueba propuesta (no ejecutada):** Describe dos campos de una página de prueba y revisa el JSON extraído Éxito: Los campos coinciden con el contenido y faltan datos que no están en la página
- **Combina con:** `ollama` [8/motores], `playwright` [32/bibliotecas], `graphrag` [6/rag], `crawlee-python` [4/crawlers]
- **Alternativas:** `maxun`, `llm-scraper`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): maxun. Se quita la combinación con crawl4ai por solaparse. Respeta los términos de uso y robots.txt de cada sitio y la normativa de…. El MCP compañero scrapegraph-mcp usa el servicio ScrapeGraph con clave propia; la biblioteca local y el servicio no comparten necesariamente costes o requisitos.

### llm-scraper (`llm-scraper`)

- **Repo:** https://github.com/mishushakov/llm-scraper · MIT · nivel 2 · 47/100 · alternativa en «Scraping guiado por LLM»
- **Qué es:** Librería TypeScript para extraer datos estructurados de cualquier página web con LLM, de @mishushakov. Licencia MIT. Es estable (~7k estrellas, sin releases) y su versión 2.0 usa el Vercel AI SDK 6.
- **Cuándo elegirlo:** Casos: Extraer campos sin escribir selectores específicos; Normalizar información de páginas similares.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node.js; Playwright; esquema Zod; modelo elegido; hardware prerequisites; API de IA: depends; Node.js; Playwright; esquema Zod; modelo elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i zod playwright llm-scraper` — fuente: https://github.com/mishushakov/llm-scraper/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Define nombre, precio y moneda y extrae un producto ficticio de una página de prueba Éxito: El objeto respeta el esquema y coincide con la página
- **Combina con:** `playwright` [32/bibliotecas], `vercel-ai` [3/ts], `ollama` [8/motores], `crawlee` [4/crawlers]
- **Alternativas:** `scrapegraph-ai`, `maxun`
- **Riesgos y avisos:** Alternativas (elige una): maxun. Se quita la combinación con firecrawl por no estar documentada. Respeta los términos de uso y robots.txt de cada sitio y la…. Instala el adaptador del proveedor además de llm-scraper y descarga el navegador de Playwright.

### last30days (`last30days-skill`)

- **Repo:** https://github.com/mvanhorn/last30days-skill · MIT · nivel 1 · 73/100
- **Qué es:** Skill de investigación que resume lo ocurrido en los últimos 30 días sobre un tema a partir de señales sociales (votos, likes, mercados de predicción), de @mvanhorn. Licencia MIT. Es muy popular y activa (~68k estrellas, v4.0.5).
- **Cuándo elegirlo:** Casos: Preparar una reunión sobre una empresa; Revisar novedades de una herramienta.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; dependencias de los canales; credenciales solo donde se indiquen; hardware prerequisites; API de IA: opcional; Agente compatible; dependencias de los canales; credenciales solo donde se indiquen.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/mvanhorn/last30days-skill/blob/main/README.md

  ```bash
  /plugin marketplace add mvanhorn/last30days-skill
  /plugin install last30days
  ```
- **Primera prueba propuesta (no ejecutada):** Investiga un tema concreto y exige fechas, enlaces y distinción entre opinión y evidencia Éxito: Puedes abrir las fuentes y verificar que corresponden al periodo solicitado
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `agent-reach`
- **Alternativas:** `social-media-research-skills`
- **Riesgos y avisos:** Alternativas (elige una): social-media-research-skills. Investigar a personas concretas exige cuidado con la privacidad. No todas las fuentes están activas ni disponibles sin clave; compatibilidad por Agent Skills y no por compartir proveedor LLM.

### RSSHub (`rsshub`)

- **Repo:** https://github.com/DIYgod/RSSHub · AGPL-3.0 · nivel 1 · 73/100
- **Qué es:** Red y servidor de feeds RSS de código abierto (AGPL-3.0) creado por DIYgod y mantenido por una comunidad amplia. Muy usado (más de 5.000 instancias según el proyecto) y en desarrollo continuo.
- **Cuándo elegirlo:** Casos: seguir canales, perfiles o webs sin RSS desde tu lector de feeds; alimentar un flujo de monitorización de fuentes con feeds uniformes.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d --name rsshub -p 1200:1200 diygod/rsshub` — fuente: https://docs.rsshub.app/deploy/
- **Primera prueba propuesta (no ejecutada):** Despliega RSSHub con Docker según su documentación y abre una ruta de ejemplo en el navegador. Éxito: La ruta devuelve un feed RSS válido que tu lector puede suscribir.
- **Combina con:** `freshrss`, `miniflux`, `activepieces` [1/motores], `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La instancia pública puede limitar peticiones; para uso intensivo conviene autoalojarla.

### changedetection.io (`changedetection`)

- **Repo:** https://github.com/dgtlmoon/changedetection.io · Apache-2.0 · nivel 1 · 70/100
- **Qué es:** Monitor autoalojado de cambios en páginas web (changedetection.io), de @dgtlmoon. Licencia Apache-2.0. Es maduro y activo (~36k estrellas, 0.70.3) y tiene versión alojada de pago.
- **Cuándo elegirlo:** Casos: Detectar cambios de precio permitidos; Monitorear avisos de una página.
- **Requisitos:** nivel 1: preparación sencilla; Docker; URL a vigilar; canal de aviso opcional; hardware prerequisites; API de IA: opcional; Docker; URL a vigilar; canal de aviso opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/dgtlmoon/changedetection.io/blob/master/README.md

  ```bash
  docker run -d --restart always -p "127.0.0.1:5000:5000" -v datastore-volume:/datastore --name changedetection.io docker.io/dgtlmoon/changedetection.io
  ```
- **Primera prueba propuesta (no ejecutada):** Vigila un texto en una página propia y modifícalo una vez para revisar la diferencia Éxito: El historial identifica el cambio concreto
- **Combina con:** `ollama` [8/motores], `claude-code` [20/terminal], `activepieces` [1/motores], `archivebox`, `cloud-mail` [18/marketing], `huginn` [1/motores]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Respeta los términos de uso de cada plataforma y la privacidad de las personas. MCP requiere versión que lo incluya; su acceso al historial no acredita que el agente haya observado cambios futuros.

### SearXNG (`searxng`)

- **Repo:** https://github.com/searxng/searxng · AGPL-3.0 · nivel 1 · 69/100
- **Qué es:** Metabuscador libre que agrega resultados de muchos motores sin rastrear ni perfilar al usuario. Licencia AGPL-3.0-or-later. Es un proyecto comunitario maduro y activo (~40k estrellas; publica desde la rama principal, sin releases en…
- **Cuándo elegirlo:** Casos: Añadir búsqueda a una herramienta de investigación; Disponer de un metabuscador propio.
- **Requisitos:** nivel 1: preparación sencilla; Servidor o Docker; configuración de motores de búsqueda; hardware prerequisites; API de IA: no; Servidor o Docker; configuración de motores de búsqueda.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.searxng.org/admin/installation.html
- **Primera prueba propuesta (no ejecutada):** Realiza una búsqueda y compara las fuentes de dos resultados Éxito: Ves resultados agregados y puedes abrir su origen
- **Combina con:** `gpt-researcher` [21/research], `open-webui` [8/chats], `vane`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. No expongas tu instancia sin limitación de peticiones. La privacidad del metabuscador no vuelve locales las consultas enviadas a motores externos.

### Agent-Reach (`agent-reach`)

- **Repo:** https://github.com/Panniantong/Agent-Reach · MIT · nivel 1 · 67/100
- **Qué es:** Herramienta para que agentes de IA de línea de comandos busquen y lean plataformas a las que no llegan solos (X, Reddit, YouTube, Xiaohongshu y otras), de @Panniantong. Licencia MIT.
- **Cuándo elegirlo:** Casos: Leer una discusión pública para investigación; Obtener transcripciones de un video permitido.
- **Requisitos:** nivel 1: preparación sencilla; Agente con terminal; uv; sesiones de sitios solo cuando corresponda; hardware prerequisites; API de IA: opcional; Agente con terminal; uv; sesiones de sitios solo cuando corresponda.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip` — fuente: https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md
- **Primera prueba propuesta (no ejecutada):** Lista los canales y lee un README público de GitHub antes de añadir canales opcionales Éxito: Puedes distinguir canales disponibles, autenticados y experimentales
- **Combina con:** `claude-code` [20/terminal], `openclaw` [21/asistentes], `last30days-skill`
- **Riesgos y avisos:** Sin alternativas declaradas. Instala solo desde GitHub (hay un paquete homónimo en PyPI que no es este). El paquete homónimo de PyPI no es este proyecto; usa la dirección GitHub del instalador oficial.

### ArchiveBox (`archivebox`)

- **Repo:** https://github.com/ArchiveBox/ArchiveBox · MIT · nivel 1 · 66/100
- **Qué es:** Aplicación autoalojada para archivar sitios web en varios formatos. Licencia MIT. Es madura y activa (~29k estrellas, v0.9.77).
- **Cuándo elegirlo:** Casos: Preservar documentación que cambia; Crear una biblioteca de fuentes de una investigación.
- **Requisitos:** nivel 1: preparación sencilla; Docker o dependencias nativas; directorio persistente; espacio en disco; hardware prerequisites; API de IA: no; Docker o dependencias nativas; directorio persistente; espacio en disco.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install archivebox` — fuente: https://github.com/ArchiveBox/ArchiveBox/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Archiva una página propia y abre las copias HTML y captura desde el panel Éxito: La captura conserva la URL y se puede consultar después
- **Combina con:** `yt-dlp` [4/social], `changedetection`, `karakeep` [15/notas], `instaloader` [4/social]
- **Riesgos y avisos:** Sin alternativas declaradas. Desactiva el envío a archive.org si archivas páginas privadas. El README menciona herramientas MCP pero falta confirmar aquí su configuración por cliente; los archivos no garantizan capturar toda web dinámica.

### FreshRSS (`freshrss`)

- **Repo:** https://github.com/FreshRSS/FreshRSS · AGPL-3.0 · nivel 1 · 65/100 · recomendado en «Lectores RSS auto-hospedados»
- **Qué es:** Agregador RSS autoalojado de código abierto (AGPL-3.0) mantenido por la comunidad FreshRSS. Proyecto maduro y traducido a más de 20 idiomas.
- **Cuándo elegirlo:** Casos: centralizar en tu servidor los feeds de noticias y blogs que sigues; seguir webs sin RSS con reglas de extracción XPath.
- **Requisitos:** nivel 1: preparación sencilla; PHP, composer.json, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/FreshRSS/FreshRSS/blob/edge/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega FreshRSS con Docker, importa un archivo OPML pequeño y actualiza los feeds. Éxito: Los artículos aparecen en la interfaz y un cliente móvil compatible puede sincronizarlos.
- **Combina con:** `rsshub`, `wallabag`, `coolify` [22/infraestructura]
- **Alternativas:** `miniflux`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): miniflux.

### Miniflux (`miniflux`)

- **Repo:** https://github.com/miniflux/v2 · Apache-2.0 · nivel 1 · 58/100 · alternativa en «Lectores RSS auto-hospedados»
- **Qué es:** Lector de feeds de código abierto (Apache-2.0) creado por Frédéric Guillot. Proyecto maduro, deliberadamente minimalista y «opinionated».
- **Cuándo elegirlo:** Casos: leer feeds sin rastreadores en una instancia propia ligera; enviar artículos automáticamente a un servicio de lectura o notas.
- **Requisitos:** nivel 1: preparación sencilla; Go, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/miniflux/v2/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Miniflux con PostgreSQL según la guía, importa un OPML y lee un artículo. Éxito: Los feeds se actualizan, la búsqueda devuelve resultados y no aparecen píxeles de seguimiento.
- **Combina con:** `rsshub`, `wallabag`, `coolify` [22/infraestructura]
- **Alternativas:** `freshrss`
- **Riesgos y avisos:** Alternativas (elige una): freshrss.

### wallabag (`wallabag`)

- **Repo:** https://github.com/wallabag/wallabag · MIT · nivel 2 · 58/100
- **Qué es:** Aplicación «leer más tarde» de código abierto (MIT) mantenida por la comunidad wallabag desde 2013. Madura, con apps oficiales para Android e iOS y servicio alojado (wallabag.it) aparte.
- **Cuándo elegirlo:** Casos: guardar artículos para leerlos sin conexión en el móvil; archivar lecturas con etiquetas y anotaciones en tu propio servidor.
- **Requisitos:** nivel 2: preparación media; PHP, compose.yaml, composer.json, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/wallabag/wallabag.git` — fuente: https://github.com/wallabag/wallabag/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala wallabag con Docker o según su documentación y guarda un artículo desde la extensión del navegador. Éxito: El artículo aparece limpio en la lista de lectura y se puede exportar.
- **Combina con:** `freshrss`, `miniflux`, `coolify` [22/infraestructura]
- **Riesgos y avisos:** Alternativa cercana en el catálogo: karakeep (marcadores con IA).

### Vane (`vane`)

- **Repo:** https://github.com/ItzCrazyKns/Vane · MIT · nivel 1 · 57/100
- **Qué es:** Motor de respuestas con IA centrado en la privacidad que se ejecuta en tu propio equipo, de @ItzCrazyKns. Licencia MIT. Es popular (~38k estrellas, v1.12.2) y su último cambio es de septiembre de 2026.
- **Cuándo elegirlo:** Casos: Investigar un tema con citas; Consultar la web usando Ollama.
- **Requisitos:** nivel 1: preparación sencilla; Docker; modelo local accesible o clave de proveedor; hardware prerequisites; API de IA: depends; Docker; modelo local accesible o clave de proveedor.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest` — fuente: https://github.com/ItzCrazyKns/Vane/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Busca una pregunta de actualidad sencilla y abre las referencias antes de aceptar el resumen Éxito: La respuesta muestra enlaces que apoyan sus afirmaciones
- **Combina con:** `searxng`, `ollama` [8/motores], `markitdown` [13/conversion]
- **Alternativas:** `gpt-researcher`
- **Riesgos y avisos:** Alternativas (elige una): gpt-researcher. Antes llamado Perplexica; búsqueda web privada no significa que los sitios externos no reciban consultas.

### yt-dlp (`yt-dlp`)

- **Repo:** https://github.com/yt-dlp/yt-dlp · Unlicense · nivel 1 · 80/100
- **Qué es:** Descargador de audio y vídeo por línea de comandos con soporte para miles de sitios, fork de youtube-dl. El código del repositorio es Unlicense, pero los ejecutables publicados incluyen código GPLv3+ o ISC.
- **Cuándo elegirlo:** Casos: Respaldar videos propios; Obtener medios permitidos para edición.
- **Requisitos:** nivel 1: preparación sencilla; Binario oficial o Python compatible; FFmpeg para unir y convertir medios; hardware prerequisites; API de IA: no; Binario oficial o Python compatible; FFmpeg para unir y convertir medios.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "yt-dlp[default,curl-cffi]"` — fuente: https://github.com/yt-dlp/yt-dlp/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta formatos de un video propio y descarga una versión que puedas reproducir Éxito: El archivo conserva audio y video y se abre en un reproductor
- **Combina con:** `ffmpeg` [12/edicion], `whisperx` [29/stt], `fabric` [19/prompts]
- **Riesgos y avisos:** Sin alternativas declaradas. Descargar contenido protegido puede infringir derechos de autor o términos de uso. El comando nightly del README instala versiones preliminares; empieza con la ruta estable y respeta permisos de uso.

### spotDL (`spotdl`)

- **Repo:** https://github.com/spotDL/spotify-downloader · MIT · nivel 1 · 64/100
- **Qué es:** Descargador de música de línea de comandos de código abierto (MIT) mantenido por la comunidad spotDL; versión 4 estable y activa.
- **Cuándo elegirlo:** Casos: conservar una copia local de listas de reproducción propias; etiquetar automáticamente archivos de audio con metadatos de Spotify.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install spotdl` — fuente: https://github.com/spotDL/spotify-downloader/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install spotdl`, prepara FFmpeg y descarga una canción con su URL. Éxito: El archivo de audio queda en la carpeta con título, artista y carátula incrustados.
- **Combina con:** `ffmpeg` [12/edicion], `yt-dlp`, `syncthing` [15/archivos]
- **Riesgos y avisos:** La coincidencia en YouTube no siempre es exacta: revisa versiones en vivo o remezclas.

### instaloader (`instaloader`)

- **Repo:** https://github.com/instaloader/instaloader · MIT · nivel 2 · 58/100
- **Qué es:** Herramienta Python para descargar fotos, vídeos y metadatos de Instagram. Licencia MIT. Es madura (~14k estrellas, v4.16) y muestra un patrocinador de APIs sociales.
- **Cuándo elegirlo:** Casos: Respaldar publicaciones propias; Actualizar una colección autorizada sin repetir todo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; espacio en disco; sesión propia para contenido que la requiera; hardware prerequisites; API de IA: no; Python; espacio en disco; sesión propia para contenido que la requiera.
- **Instalación (documentada en la fuente; no ejecutada):** `pip3 install instaloader` — fuente: https://github.com/instaloader/instaloader/blob/master/README.rst
- **Primera prueba propuesta (no ejecutada):** Descarga una publicación propia y compara archivo, descripción y metadatos Éxito: La carpeta contiene los medios y datos esperados
- **Combina con:** `archivebox` [4/busqueda], `whisper` [29/stt], `yt-dlp`
- **Riesgos y avisos:** Sin alternativas declaradas. Respeta los términos de uso de cada plataforma y la privacidad de las personas. Contenido privado exige acceso autorizado; que el código no cobre no garantiza que Instagram permita todas las operaciones.

### gallery-dl (`gallery-dl`)

- **Repo:** https://github.com/mikf/gallery-dl · GPL-2.0 · nivel 1 · 53/100
- **Qué es:** Herramienta de línea de comandos de código abierto (GPL-2.0) creada por Mike Fährmann y mantenida durante años. El README anuncia que el desarrollo activo se ha trasladado a Codeberg; GitHub sigue recibiendo cambios.
- **Cuándo elegirlo:** Casos: archivar una colección propia de imágenes con metadatos y nombres ordenados; descargar un conjunto de imágenes públicas para un dataset con permiso de uso.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml, requirements.txt, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install gallery-dl` — fuente: https://github.com/mikf/gallery-dl/blob/master/README.rst
- **Primera prueba propuesta (no ejecutada):** Instala gallery-dl (pip, Homebrew o binario) y descarga una galería pública pequeña a una carpeta de prueba. Éxito: Las imágenes quedan en disco con la estructura de carpetas y nombres configurada.
- **Combina con:** `yt-dlp`, `ffmpeg` [12/edicion], `real-esrgan` [11/edicion], `upscayl` [11/edicion]
- **Riesgos y avisos:** Repositorio canónico de desarrollo: Codeberg (mikf/gallery-dl); GitHub se mantiene como espejo con actividad.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-4.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Buscar, extraer y monitorear información web», lee `docs/alexandria/categoria-4.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-4.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
