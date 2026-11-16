[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🕷️ crawl4ai

> Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 87.4k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Crawler y extractor web de código abierto (Apache 2.0) orientado a IA. Se usa como librería Python, como servidor Docker propio o a través del servicio de pago Crawl4AI Cloud.

## ¿Qué hace?

Convierte páginas en Markdown limpio para RAG, extrae JSON estructurado y procesa muchas URLs. La versión Cloud añade búsqueda web (`/search`, `/serp`, `/answer`) y un servidor MCP alojado.

## ¿Cómo lo hace?

Controla navegadores reales con Playwright (`crawl4ai-setup` instala el navegador) desde `AsyncWebCrawler`. Quita menús y pies de página con filtros de poda, BM25 o un LLM, fragmenta páginas largas y puede ordenar fragmentos por similitud coseno. Extrae datos con esquemas CSS/XPath sin LLM o con `LLMExtractionStrategy`, que acepta cualquier proveedor soportado por LiteLLM, incluido Ollama.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelo local para la extracción con LLM, sin enviar el contenido a una API de pago. | Ollama con el modelo descargado antes de lanzar la extracción. |
| [Qdrant](qdrant.md) | El Markdown fragmentado se convierte en embeddings y se guarda en Qdrant para buscarlo en un RAG (combinación por arquitectura). | Independientes; necesitas además un modelo de embeddings. |
| [n8n](n8n.md) | Un flujo de n8n puede llamar al servidor Docker de Crawl4AI con un nodo HTTP para rastrear páginas de forma programada (combinación por arquitectura). | Levanta el servidor Docker de Crawl4AI y luego crea el flujo. |

**Notas:** firecrawl y jina-reader cumplen una función parecida: elige uno. gpt-researcher no trae un scraper de Crawl4AI (su carpeta de scrapers incluye Firecrawl, BeautifulSoup y navegador), por eso se retiró de las combinaciones.

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/unclecode/crawl4ai/blob/main/README.md) · [2](https://api.github.com/repos/assafelovic/gpt-researcher/contents/gpt_researcher/scraper)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Cloud tiene créditos y límites; self-hosting necesita recursos; la extracción LLM puede usar Ollama o una API |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. La lectura básica no necesita modelo; no confundas la clave del servicio de crawling con una clave del proveedor LLM |
| Coste | El coste depende del proveedor o la ruta. Cloud tiene créditos y límites; self-hosting necesita recursos; la extracción LLM puede usar Ollama o una API |
| Equipo | Preparación según la ruta elegida. Python; dependencias de navegador; clave Cloud solo para servicio alojado |

La lectura básica no necesita modelo; no confundas la clave del servicio de crawling con una clave del proveedor LLM

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dependencias de navegador
- clave Cloud solo para servicio alojado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install -U crawl4ai
crawl4ai-setup        # installs the browser, once
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/unclecode/crawl4ai/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar crawl4ai para mi objetivo y necesito pasos guiados. Lee https://github.com/unclecode/crawl4ai/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte una página de prueba a Markdown y después extrae dos campos sin LLM.

**Qué comprobar:** Puedes comparar texto y campos con la página.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar artículos para RAG
- Extraer datos estructurados con un modelo local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar artículos para RAG; Extraer datos estructurados con un modelo local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La lectura básica no necesita modelo; no confundas la clave del servicio de crawling con una clave del proveedor LLM

## Stack y modelos

- **Stack:** Python; dependencias de navegador; clave Cloud solo para servicio alojado
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📦 **Dependencia del proyecto** — instálalo dentro de cada proyecto que lo use

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jina Reader](jina-reader.md) | 12.3k | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. |

## Enlaces

- 🐙 GitHub: [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- 🌐 Web: <https://crawl4ai.com/?ref=github-about>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/unclecode/crawl4ai/blob/main/README.md)
- [Fuente 2](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
