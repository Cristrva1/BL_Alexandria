[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Scraping guiado por LLM

# 🕸️ Scrapegraph-ai

> Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 32.8k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Librería Python de scraping con LLM y grafos, de ScrapeGraphAI. Licencia MIT. Es popular (~33k estrellas, v2.3.1) y el README promociona en primer plano su API comercial.

## ¿Qué hace?

Describes en lenguaje natural qué datos quieres y la librería construye un pipeline (grafo) que descarga la página o documento y extrae la información estructurada con un LLM. Tiene grafos para una página, para varias páginas, para resultados de búsqueda y para generar un script Python de scraping. Funciona con OpenAI, Groq, Azure, Gemini y otros, o con modelos locales vía Ollama.

## ¿Cómo lo hace?

Se instala con `pip install scrapegraphai` y `playwright install` para la descarga de páginas. Se configura el modelo en un diccionario (`ollama/llama3.2`, etc.). Hay un servidor MCP y conectores de bajo código como Pipedream o Zapier vinculados a la API de pago.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales soportados de forma nativa. | Instala Ollama, descarga el modelo y apúntalo en la configuración. |
| [playwright](playwright.md) | Descarga y renderizado de páginas. | Ejecuta `playwright install` tras instalar la librería. |
| [graphrag](graphrag.md) | Construir un grafo de conocimiento con los datos extraídos. (combinación por arquitectura) | Exporta los resultados como documentos para GraphRAG. |
| [crawlee-python](crawlee-python.md) | Combinación recíproca: crawlee-python lo enlaza como «Extraer datos con LLM a partir de las páginas recogidas. (combinación por arquitectura)». | Orden indicado desde crawlee-python: Recoge con Crawlee y pasa el HTML a ScrapeGraphAI. |

**Notas:** Alternativas (elige una): maxun. Se quita la combinación con crawl4ai por solaparse. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales.

Estado en GitHub: activo · último push 2026-10-06 · última versión publicada v2.3.1 (2026-10-06) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/README.md) · [2](https://docs.scrapegraphai.com/introduction)</sub>

## Ver similares

Grupo **Scraping guiado por LLM**: Scrapegraph-ai ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Scrapegraph-ai** (esta ficha) ⭐ recomendado | 70 | Si buscas esto: framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. |
| 2 | [Maxun](maxun.md) | 70 | Si buscas esto: plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. |
| 3 | [llm-scraper](llm-scraper.md) | 47 | Si buscas esto: librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La ruta local documentada evita API de pago; proveedores remotos y servicio comercial se cobran por separado |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El MCP compañero scrapegraph-mcp usa el servicio ScrapeGraph con clave propia; la biblioteca local y el servicio no comparten necesariamente costes o requisitos |
| Coste | El coste depende del proveedor o la ruta. La ruta local documentada evita API de pago; proveedores remotos y servicio comercial se cobran por separado |
| Equipo | Preparación según la ruta elegida. Python; Playwright; modelo Ollama o proveedor remoto |

El MCP compañero scrapegraph-mcp usa el servicio ScrapeGraph con clave propia; la biblioteca local y el servicio no comparten necesariamente costes o requisitos

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Playwright
- modelo Ollama o proveedor remoto

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install scrapegraphai

# IMPORTANT (for fetching websites content)
playwright install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Scrapegraph-ai para mi objetivo y necesito pasos guiados. Lee https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Describe dos campos de una página de prueba y revisa el JSON extraído.

**Qué comprobar:** Los campos coinciden con el contenido y faltan datos que no están en la página.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Extraer fichas de productos
- Transformar artículos en registros estructurados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Extraer fichas de productos; Transformar artículos en registros estructurados | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP compañero scrapegraph-mcp usa el servicio ScrapeGraph con clave propia; la biblioteca local y el servicio no comparten necesariamente costes o requisitos

## Stack y modelos

- **Stack:** Python; Playwright; modelo Ollama o proveedor remoto
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Maxun](maxun.md) | 18.4k | Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. |

## Enlaces

- 🐙 GitHub: [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)
- 🌐 Web: <https://scrapegraphai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/README.md)
- [Fuente 2](https://github.com/ScrapeGraphAI/scrapegraph-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
