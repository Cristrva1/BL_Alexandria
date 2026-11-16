# 4. Buscar, extraer y monitorear información web — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agent-reach`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=scraping,research,python

**Qué es:** CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs.
**Stack:** Agente con terminal; uv; sesiones de sitios solo cuando corresponda
**Acceso y costes:**
- API de IA: API de IA opcional. Varias rutas no usan claves; transcripción puede requerir Groq u OpenAI y otros canales usan servicios, sesiones o proxies
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Compatibilidad por confirmar
- Modelos locales: La función básica no necesita un modelo. El paquete homónimo de PyPI no es este proyecto; usa la dirección GitHub del instalador oficial
- Coste: El coste depende del proveedor o la ruta. Varias rutas no usan claves; transcripción puede requerir Groq u OpenAI y otros canales usan servicios, sesiones o proxies
- Equipo: Preparación según la ruta elegida. Agente con terminal; uv; sesiones de sitios solo cuando corresponda
**Repo:** https://github.com/Panniantong/Agent-Reach

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Leer una discusión pública para investigación; Obtener transcripciones de un video permitido
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lista los canales y lee un README público de GitHub antes de añadir canales opcionales
**Qué comprobar:** Puedes distinguir canales disponibles, autenticados y experimentales
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `last30days-skill`

## `archivebox`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=scraping,data,python,docker

**Qué es:** Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios.
**Stack:** Docker o dependencias nativas; directorio persistente; espacio en disco
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; almacenamiento, navegador y servidor son recursos propios
- Claude Code: Compatibilidad por confirmar
- Codex: Compatibilidad por confirmar
- Antigravity: Compatibilidad por confirmar
- Modelos locales: La función básica no necesita un modelo. El README menciona herramientas MCP pero falta confirmar aquí su configuración por cliente; los archivos no garantizan capturar toda web dinámica
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo; almacenamiento, navegador y servidor son recursos propios
- Equipo: Preparación según la ruta elegida. Docker o dependencias nativas; directorio persistente; espacio en disco
**Repo:** https://github.com/ArchiveBox/ArchiveBox

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ArchiveBox/ArchiveBox/wiki/Quickstart
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preservar documentación que cambia; Crear una biblioteca de fuentes de una investigación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Archiva una página propia y abre las copias HTML y captura desde el panel
**Qué comprobar:** La captura conserva la URL y se puede consultar después
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `yt-dlp`

## `awesome-web-scraping`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=crawlers,captcha-bypass,captcha-recaptcha,crawler,crawling,crawling-framework,crawling-python,crawling-tool

**Qué es:** Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos.
**Stack:** Navegador; lenguaje o formato objetivo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer la lista no cuesta API; servicios enlazados pueden ser comerciales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No se instala el directorio entero ni hereda compatibilidad de las herramientas que enumera
- Coste: Sin pago a un modelo en la ruta básica. Leer la lista no cuesta API; servicios enlazados pueden ser comerciales
- Equipo: Preparación según la ruta elegida. Navegador; lenguaje o formato objetivo
**Repo:** https://github.com/lorien/awesome-web-scraping

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar un parser para Python; Encontrar herramientas de extracción para JavaScript
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige la lista de tu lenguaje y compara dos bibliotecas por mantenimiento y salida
**Qué comprobar:** Obtienes dos candidatos con sus repositorios originales
Revisión documental individual; instalación no ejecutada por Alexandría.

## `changedetection`
role=app · exec=local · setup=easy · mcp=True · prov=— · tags=scraping,notifications,python,docker

**Qué es:** Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más.
**Stack:** Docker; URL a vigilar; canal de aviso opcional
**Acceso y costes:**
- API de IA: API de IA opcional. Las comparaciones clásicas no necesitan LLM; filtros semánticos usan API o modelo local; SaaS y proxies tienen condiciones propias
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. MCP requiere versión que lo incluya; su acceso al historial no acredita que el agente haya observado cambios futuros
- Coste: El coste depende del proveedor o la ruta. Las comparaciones clásicas no necesitan LLM; filtros semánticos usan API o modelo local; SaaS y proxies tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Docker; URL a vigilar; canal de aviso opcional
**Repo:** https://github.com/dgtlmoon/changedetection.io

**Instalación** [+]:

```
docker run -d --restart always -p "127.0.0.1:5000:5000" -v datastore-volume:/datastore --name changedetection.io docker.io/dgtlmoon/changedetection.io
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Detectar cambios de precio permitidos; Monitorear avisos de una página
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Vigila un texto en una página propia y modifícalo una vez para revisar la diferencia
**Qué comprobar:** El historial identifica el cambio concreto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`

## `crawl4ai`
role=library · exec=local · setup=medium · mcp=True · prov=— · tags=scraping,python

**Qué es:** Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA.
**Stack:** Python; dependencias de navegador; clave Cloud solo para servicio alojado
**Acceso y costes:**
- API de IA: API de IA opcional. Cloud tiene créditos y límites; self-hosting necesita recursos; la extracción LLM puede usar Ollama o una API
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. La lectura básica no necesita modelo; no confundas la clave del servicio de crawling con una clave del proveedor LLM
- Coste: El coste depende del proveedor o la ruta. Cloud tiene créditos y límites; self-hosting necesita recursos; la extracción LLM puede usar Ollama o una API
- Equipo: Preparación según la ruta elegida. Python; dependencias de navegador; clave Cloud solo para servicio alojado
**Repo:** https://github.com/unclecode/crawl4ai

**Instalación** [+]:

```
pip install -U crawl4ai
crawl4ai-setup        # installs the browser, once
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar artículos para RAG; Extraer datos estructurados con un modelo local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte una página de prueba a Markdown y después extrae dos campos sin LLM
**Qué comprobar:** Puedes comparar texto y campos con la página
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `firecrawl`, `gpt-researcher`
**Alternativas (elige una):** `jina-reader`

## `crawlee`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=scraping,typescript

**Qué es:** Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos.
**Stack:** Node.js >=22.13; npm; navegador si eliges Playwright
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no exige IA ni Apify Cloud; proxies y alojamiento son opcionales de pago
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El generador ofrece plantillas; elige HTTP para HTML sencillo y navegador cuando sea necesario
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no exige IA ni Apify Cloud; proxies y alojamiento son opcionales de pago
- Equipo: Preparación según la ruta elegida. Node.js >=22.13; npm; navegador si eliges Playwright
**Repo:** https://github.com/apify/crawlee

**Instalación** [+]:

```
npx crawlee create my-crawler
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Rastrear una documentación propia; Extraer datos de páginas con JavaScript
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un crawler con límite pequeño y recoge títulos de tres páginas de prueba
**Qué comprobar:** La cola termina y guarda un registro por página
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `playwright`

## `crawlee-python`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=scraping,python

**Qué es:** Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python.
**Stack:** Python; entorno virtual; navegador si eliges Playwright
**Acceso y costes:**
- API de IA: API de IA opcional. El crawling básico no necesita LLM; la extracción con Pydantic AI o Stagehand y proveedores externos puede costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. No atribuyas las necesidades de los módulos de IA a la ruta básica de scraping
- Coste: El coste depende del proveedor o la ruta. El crawling básico no necesita LLM; la extracción con Pydantic AI o Stagehand y proveedores externos puede costar
- Equipo: Preparación según la ruta elegida. Python; entorno virtual; navegador si eliges Playwright
**Repo:** https://github.com/apify/crawlee-python

**Instalación** [+]:

```
python -m pip install 'crawlee[all]'
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Recopilar documentos públicos; Crear un crawler con reintentos y exportación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Recoge enlaces de tres páginas con una cola acotada y guarda sus títulos
**Qué comprobar:** Se controlan duplicados y obtienes los tres registros esperados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `scrapy`, `playwright`

## `defuddle`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=crawlers,library,typescript

**Qué es:** Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable.
**Stack:** Node.js; archivo HTML de prueba o página pública
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La extracción básica no necesita API ni modelo; el contenido y alojamiento son costes externos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Puede perder información en diseños poco habituales; compara una muestra antes de procesar muchas páginas
- Coste: Sin pago a un modelo en la ruta básica. La extracción básica no necesita API ni modelo; el contenido y alojamiento son costes externos
- Equipo: Preparación según la ruta elegida. Node.js; archivo HTML de prueba o página pública
**Repo:** https://github.com/kepano/defuddle

**Instalación** [+]:

```
npm install defuddle
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar artículos para lectura; Limpiar HTML antes de indexarlo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Extrae Markdown de un artículo con menú y comprueba qué texto conserva
**Qué comprobar:** El resultado prioriza el artículo y elimina navegación irrelevante
Revisión documental individual; instalación no ejecutada por Alexandría.

## `firecrawl`
role=platform · exec=cloud · setup=medium · mcp=True · prov=— · tags=scraping,typescript,docker

**Qué es:** Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript.
**Stack:** Node.js; cuenta Firecrawl para la ruta alojada; cliente elegido
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta alojada consume créditos de Firecrawl; el agente tiene sus propios límites; self-hosting tiene infraestructura y funciones distintas
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Hay CLI, skill y MCP stdio; compatibilidad MCP no significa que la suscripción del cliente pague Firecrawl
- Coste: El coste depende del proveedor o la ruta. La ruta alojada consume créditos de Firecrawl; el agente tiene sus propios límites; self-hosting tiene infraestructura y funciones distintas
- Equipo: Preparación según la ruta elegida. Node.js; cuenta Firecrawl para la ruta alojada; cliente elegido
**Repo:** https://github.com/firecrawl/firecrawl

**Instalación** [+]:

```
npx -y firecrawl-cli@latest init --all --browser
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar páginas para un buscador documental; Crear un mapa de URLs de una web propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Extrae título y contenido de una página pública de prueba y revisa el Markdown
**Qué comprobar:** Se conserva el contenido principal con la URL de origen
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gpt-researcher`, `crawl4ai`
**Alternativas (elige una):** `jina-reader`

## `instaloader`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vision,scraping,python

**Qué es:** Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram.
**Stack:** Python; espacio en disco; sesión propia para contenido que la requiera
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa un modelo ni requiere API de IA; la cuenta y la plataforma imponen límites
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Contenido privado exige acceso autorizado; que el código no cobre no garantiza que Instagram permita todas las operaciones
- Coste: Sin pago a un modelo en la ruta básica. No usa un modelo ni requiere API de IA; la cuenta y la plataforma imponen límites
- Equipo: Preparación según la ruta elegida. Python; espacio en disco; sesión propia para contenido que la requiera
**Repo:** https://github.com/instaloader/instaloader

**Instalación** [+]:

```
pip3 install instaloader
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Respaldar publicaciones propias; Actualizar una colección autorizada sin repetir todo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Descarga una publicación propia y compara archivo, descripción y metadatos
**Qué comprobar:** La carpeta contiene los medios y datos esperados
Revisión documental individual; instalación no ejecutada por Alexandría.

## `jina-reader`
role=platform · exec=cloud · setup=easy · mcp=False · prov=— · tags=scraping,rag,typescript

**Qué es:** Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai.
**Stack:** Navegador para servicio público; Docker solo para self-hosting
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El servicio público tiene cupos y modalidades con clave; self-hosting usa recursos y puede necesitar activos con licencia propia
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El contenedor básico no tiene caché ni control de tasa; localhost usa el puerto HTTP/1.1 del ejemplo
- Coste: El coste depende del proveedor o la ruta. El servicio público tiene cupos y modalidades con clave; self-hosting usa recursos y puede necesitar activos con licencia propia
- Equipo: Preparación según la ruta elegida. Navegador para servicio público; Docker solo para self-hosting
**Repo:** https://github.com/jina-ai/reader

**Instalación** [+]:

```
docker run --rm -p 3000:8081 ghcr.io/jina-ai/reader:oss
# then: curl http://localhost:3000/https://example.com
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un artículo a texto para consulta; Preparar una página para un índice documental
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Antepon r.jina.ai a una URL pública y compara el texto devuelto con la página
**Qué comprobar:** Obtienes contenido legible con su dirección de origen
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `llama-index`
**Alternativas (elige una):** `firecrawl`, `crawl4ai`

## `last30days-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=research,skills,python

**Qué es:** Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días.
**Stack:** Agente compatible; dependencias de los canales; credenciales solo donde se indiquen
**Acceso y costes:**
- API de IA: API de IA opcional. Algunas fuentes son públicas; otras consumen APIs o créditos; además usa el agente anfitrión
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. No todas las fuentes están activas ni disponibles sin clave; compatibilidad por Agent Skills y no por compartir proveedor LLM
- Coste: El coste depende del proveedor o la ruta. Algunas fuentes son públicas; otras consumen APIs o créditos; además usa el agente anfitrión
- Equipo: Preparación según la ruta elegida. Agente compatible; dependencias de los canales; credenciales solo donde se indiquen
**Repo:** https://github.com/mvanhorn/last30days-skill

**Instalación** [+]:

```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una reunión sobre una empresa; Revisar novedades de una herramienta
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Investiga un tema concreto y exige fechas, enlaces y distinción entre opinión y evidencia
**Qué comprobar:** Puedes abrir las fuentes y verificar que corresponden al periodo solicitado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `agent-reach`
**Alternativas (elige una):** `social-media-research-skills`

## `llm-scraper`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=scraping,typescript

**Qué es:** Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.
**Stack:** Node.js; Playwright; esquema Zod; modelo elegido
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El modelo puede ser Ollama local o un proveedor API; no es gratis por instalar la biblioteca
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Instala el adaptador del proveedor además de llm-scraper y descarga el navegador de Playwright
- Coste: El coste depende del proveedor o la ruta. El modelo puede ser Ollama local o un proveedor API; no es gratis por instalar la biblioteca
- Equipo: Preparación según la ruta elegida. Node.js; Playwright; esquema Zod; modelo elegido
**Repo:** https://github.com/mishushakov/llm-scraper

**Instalación** [+]:

```
npm i zod playwright llm-scraper
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer campos sin escribir selectores específicos; Normalizar información de páginas similares
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Define nombre, precio y moneda y extrae un producto ficticio de una página de prueba
**Qué comprobar:** El objeto respeta el esquema y coincide con la página
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `playwright`, `firecrawl`
**Alternativas (elige una):** `maxun`

## `maxun`
role=platform · exec=local · setup=medium · mcp=True · prov=— · tags=scraping,automation,typescript

**Qué es:** Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción.
**Stack:** Docker; cuenta local; modelo solo para funciones AI
**Acceso y costes:**
- API de IA: API de IA opcional. La extracción grabada no exige LLM; Cloud, proxies y modelos se pagan según ruta; Ollama sirve para funciones AI locales
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. MCP admite HTTP y stdio; la clave de Maxun autoriza el servicio y no sustituye credenciales de modelos
- Coste: El coste depende del proveedor o la ruta. La extracción grabada no exige LLM; Cloud, proxies y modelos se pagan según ruta; Ollama sirve para funciones AI locales
- Equipo: Preparación según la ruta elegida. Docker; cuenta local; modelo solo para funciones AI
**Repo:** https://github.com/getmaxun/maxun

**Instalación** [?]:

```
Seguir la instalación original: https://docs.maxun.dev/installation/docker
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un listado en datos consultables; Monitorear cambios de un catálogo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Graba un robot que recoge nombres y precios de una página de prueba
**Qué comprobar:** El robot devuelve filas que puedes repetir y comparar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`
**Alternativas (elige una):** `scrapegraph-ai`, `llm-scraper`

## `scrapegraph-ai`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=scraping,python

**Qué es:** Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping.
**Stack:** Python; Playwright; modelo Ollama o proveedor remoto
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La ruta local documentada evita API de pago; proveedores remotos y servicio comercial se cobran por separado
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. El MCP compañero scrapegraph-mcp usa el servicio ScrapeGraph con clave propia; la biblioteca local y el servicio no comparten necesariamente costes o requisitos
- Coste: El coste depende del proveedor o la ruta. La ruta local documentada evita API de pago; proveedores remotos y servicio comercial se cobran por separado
- Equipo: Preparación según la ruta elegida. Python; Playwright; modelo Ollama o proveedor remoto
**Repo:** https://github.com/ScrapeGraphAI/Scrapegraph-ai

**Instalación** [+]:

```
pip install scrapegraphai

# IMPORTANT (for fetching websites content)
playwright install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer fichas de productos; Transformar artículos en registros estructurados
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Describe dos campos de una página de prueba y revisa el JSON extraído
**Qué comprobar:** Los campos coinciden con el contenido y faltan datos que no están en la página
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `crawl4ai`, `graphrag`
**Alternativas (elige una):** `maxun`

## `scrapling`
role=library · exec=local · setup=medium · mcp=True · prov=— · tags=automation,scraping,python

**Qué es:** Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.
**Stack:** Python 3.10+; navegadores del paquete; extra ai para MCP
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El motor no necesita LLM; proxies y servicios de terceros son opcionales y pueden costar
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. La instalación base solo trae parser; MCP requiere scrapling[ai]; los tres clientes admiten sus transportes estándar sin prueba de instalación aquí
- Coste: Sin pago a un modelo en la ruta básica. El motor no necesita LLM; proxies y servicios de terceros son opcionales y pueden costar
- Equipo: Preparación según la ruta elegida. Python 3.10+; navegadores del paquete; extra ai para MCP
**Repo:** https://github.com/D4Vinci/Scrapling

**Instalación** [+]:

```
pip install "scrapling[fetchers]"

    scrapling install           # normal install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Recopilar un catálogo público permitido; Extraer texto para un índice de búsqueda
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Extrae nombre y precio de tres productos de una página de prueba mediante selectores
**Qué comprobar:** Obtienes tres registros que coinciden con el HTML
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `scrapy`

## `scrapy`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=scraping,python

**Qué es:** Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala.
**Stack:** Python 3.11+; entorno virtual; conocimientos básicos de selectores
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelos; servidor, proxies y almacenamiento pueden generar gasto
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un framework de desarrollo, no una app de conversación ni una garantía de acceso a cualquier web
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelos; servidor, proxies y almacenamiento pueden generar gasto
- Equipo: Preparación según la ruta elegida. Python 3.11+; entorno virtual; conocimientos básicos de selectores
**Repo:** https://github.com/scrapy/scrapy

**Instalación** [+]:

```
pip install scrapy
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Recopilar listados públicos permitidos; Programar extracción repetible con pipelines
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un spider para una página propia con tres productos y exporta sus nombres
**Qué comprobar:** El archivo de salida contiene exactamente los tres productos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `crawlee-python`

## `searxng`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=search,research,python,docker

**Qué es:** Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes.
**Stack:** Servidor o Docker; configuración de motores de búsqueda
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere LLM; el servidor y ciertos motores o servicios pueden tener costes y límites
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La privacidad del metabuscador no vuelve locales las consultas enviadas a motores externos
- Coste: Sin pago a un modelo en la ruta básica. No requiere LLM; el servidor y ciertos motores o servicios pueden tener costes y límites
- Equipo: Preparación según la ruta elegida. Servidor o Docker; configuración de motores de búsqueda
**Repo:** https://github.com/searxng/searxng

**Instalación** [?]:

```
Seguir la instalación original: https://docs.searxng.org/admin/installation.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir búsqueda a una herramienta de investigación; Disponer de un metabuscador propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Realiza una búsqueda y compara las fuentes de dos resultados
**Qué comprobar:** Ves resultados agregados y puedes abrir su origen
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gpt-researcher`, `open-webui`, `vane`

## `vane`
role=app · exec=local · setup=easy · mcp=False · prov=openai,local · tags=search,research,local,typescript

**Qué es:** Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica).
**Stack:** Docker; modelo local accesible o clave de proveedor
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El contenedor incluye SearxNG; el modelo puede ser local o API de pago; alojamiento y hardware siguen siendo costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Antes llamado Perplexica; búsqueda web privada no significa que los sitios externos no reciban consultas
- Coste: El coste depende del proveedor o la ruta. El contenedor incluye SearxNG; el modelo puede ser local o API de pago; alojamiento y hardware siguen siendo costes
- Equipo: Preparación según la ruta elegida. Docker; modelo local accesible o clave de proveedor
**Repo:** https://github.com/ItzCrazyKns/Vane

**Instalación** [+]:

```
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Investigar un tema con citas; Consultar la web usando Ollama
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca una pregunta de actualidad sencilla y abre las referencias antes de aceptar el resumen
**Qué comprobar:** La respuesta muestra enlaces que apoyan sus afirmaciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `searxng`, `ollama`
**Alternativas (elige una):** `gpt-researcher`

## `yt-dlp`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,scraping,python

**Qué es:** Descargador de audio y video por línea de comandos compatible con miles de sitios.
**Stack:** Binario oficial o Python compatible; FFmpeg para unir y convertir medios
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere IA; acceso al contenido y servicios externos pueden tener sus propios costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El comando nightly del README instala versiones preliminares; empieza con la ruta estable y respeta permisos de uso
- Coste: Sin pago a un modelo en la ruta básica. No requiere IA; acceso al contenido y servicios externos pueden tener sus propios costes
- Equipo: Preparación según la ruta elegida. Binario oficial o Python compatible; FFmpeg para unir y convertir medios
**Repo:** https://github.com/yt-dlp/yt-dlp

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/yt-dlp/yt-dlp/wiki/Installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Respaldar videos propios; Obtener medios permitidos para edición
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta formatos de un video propio y descarga una versión que puedas reproducir
**Qué comprobar:** El archivo conserva audio y video y se abre en un reproductor
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisperx`, `ffmpeg`, `fabric`
