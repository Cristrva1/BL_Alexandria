# Alexandría para agentes · Scraping guiado por LLM

Categoría 4 «Buscar, extraer y monitorear información web» › subcategoría `llm`. 3 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=4&sub=llm · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `maxun` | Plataforma sin código para convertir sitios web en APIs y hojas de datos… | 2 Intermedio | 70 | AGPL-3.0 (OSI copyleft) | alternativa |
| `scrapegraph-ai` | Framework de scraping en Python basado en grafos potenciado por LLM, donde… | 2 Intermedio | 70 | MIT (OSI permisiva) | recomendado |
| `llm-scraper` | Librería TypeScript que convierte cualquier página web en datos estructurados… | 2 Intermedio | 47 | MIT (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-4-llm.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Scraping guiado por LLM», lee `docs/alexandria/categoria-4-llm.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-4-llm.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
