[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Scraping guiado por LLM

# 🕸️ Scrapegraph-ai

> Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 32.7k | MIT | Python | 2026-10-06 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. Muy popular por permitir scraping "by prompt", combinando extracción con razonamiento del modelo y soporte para múltiples proveedores.

## Por qué destaca

Muy popular por permitir scraping "by prompt", combinando extracción con razonamiento del modelo y soporte para múltiples proveedores. Su filosofía "You Only Scrape Once" resume el valor: una descripción, un grafo.

## Cómo funciona

Construye un grafo dirigido de nodos (fetch, parse, generación con LLM) que recorre la página y produce el resultado estructurado pedido, usando LangGraph por debajo.

## Instalación rápida

`pip install scrapegraphai` más `playwright install` para el render dinámico. Requiere una clave de proveedor de LLM y los binarios de Playwright.

## Casos de uso

- Extracción semántica de sitios
- Datasets útiles para IA
- Scraping sin selectores, solo describiendo los campos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres estructura semántica "by prompt" en Python | te basta un esquema simple (llm-scraper) o el coste de LLM por página es alto |

## Stack y modelos

- **Stack:** Python, LangChain/LangGraph, Playwright
- **Modelos / API:** Múltiples LLMs (OpenAI, Anthropic, locales vía Ollama); agnóstico vía variables de entorno.
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [crawl4ai](crawl4ai.md) | 87.2k | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Maxun](maxun.md) | 18.2k | Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. |

## Enlaces

- 🐙 GitHub: [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)
- 🌐 Web: <https://scrapegraphai.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
