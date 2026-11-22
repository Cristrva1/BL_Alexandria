# Alexandría para agentes · Crawlers y extracción para IA

Categoría 4 «Buscar, extraer y monitorear información web» › subcategoría `crawlers`. 11 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=4&sub=crawlers · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `scrapy` | Framework clásico y maduro de scraping y crawling en Python, con arquitectura… | 2 Intermedio | 77 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `crawl4ai` | Librería open-source de crawling y extracción web a gran escala con foco en… | 2 Intermedio | 72 | Apache-2.0 (OSI permisiva) | recomendado |
| `firecrawl` | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a… | 2 Intermedio | 71 | AGPL-3.0 (OSI copyleft) | alternativa |
| `scrapling` | Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de… | 2 Intermedio | 69 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `crawlee-python` | Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y… | 2 Intermedio | 66 | Apache-2.0 (OSI permisiva) | recomendado |
| `katana` | Crawler web de ProjectDiscovery en Go, en modo estándar o headless, con… | 1 Básico | 66 | MIT (OSI permisiva) | sin grupo |
| `crawlee` | Framework moderno de crawling para Node.js con antibloqueo integrado, que… | 2 Intermedio | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `defuddle` | Biblioteca para extraer el contenido principal de una página y convertirlo en… | 2 Intermedio | 57 | MIT (OSI permisiva) | sin grupo |
| `colly` | Framework de scraping y crawling para Go: callbacks por selector, límites por… | 2 Intermedio | 53 | Apache-2.0 (OSI permisiva) | sin grupo |
| `jina-reader` | Servicio que convierte cualquier URL en Markdown listo para LLM con solo… | 1 Básico | 52 | Apache-2.0 (OSI permisiva) | alternativa |
| `awesome-web-scraping` | Directorio de bibliotecas, herramientas y recursos para scraping web y… | 1 Básico | 48 | CC-BY-4.0 (OSI permisiva) | sin grupo |

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-4-crawlers.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Crawlers y extracción para IA», lee `docs/alexandria/categoria-4-crawlers.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-4-crawlers.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
