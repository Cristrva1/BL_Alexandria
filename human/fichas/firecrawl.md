[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🔥 firecrawl

> Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 200k | AGPL-3.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. Se ha vuelto la opción de referencia para alimentar pipelines RAG y agentes con web limpia; muy adoptada y con integración MCP de primera clase.

## Por qué destaca

Se ha vuelto la opción de referencia para alimentar pipelines RAG y agentes con web limpia; muy adoptada y con integración MCP de primera clase. Su salida Markdown/JSON normalizada ahorra el paso de limpiar HTML.

## Cómo funciona

Renderiza la página (incluido JS), normaliza el HTML y lo convierte a Markdown/JSON; expone endpoints scrape/crawl/search/map vía API REST y SDKs, más un servidor MCP para que los agentes lo usen como herramienta.

## Instalación rápida

API hosted con clave (`npm i @mendable/firecrawl-js` o `pip install firecrawl-py`); también self-host con Docker. Requiere una clave de API (gratuita con límite, de pago a escala) o infra para self-host.

## Casos de uso

- Convertir páginas complejas en contexto limpio
- Search + crawl para research
- Alimentar RAG con documentación de sitios dinámicos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| alimentas agentes/RAG con web y quieres salida limpia | solo quieres HTML crudo o el presupuesto de API no encaja |

**Limitaciones:** La API hosted de pago escala por páginas; el self-host requiere operar Redis, workers y Chromium.

## Stack y modelos

- **Stack:** API/SDK (TS/Python), hosted o self-host, Docker
- **Modelos / API:** MCP y agentes; no atado a un proveedor de LLM.
- **Etiquetas:** `scraping` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.6k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |
| [crawl4ai](crawl4ai.md) | 87.2k | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jina Reader](jina-reader.md) | 12.2k | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. |

## Enlaces

- 🐙 GitHub: [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
- 🌐 Web: <https://firecrawl.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
