[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🕷️ crawl4ai

> Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 87.2k | Apache-2.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. Una de las alternativas open-source más populares a las APIs de pago; gratuita, self-host y muy activa en la comunidad de scraping para LLMs.

## Por qué destaca

Una de las alternativas open-source más populares a las APIs de pago; gratuita, self-host y muy activa en la comunidad de scraping para LLMs. Su salida Markdown/JSON limpia compite directamente con firecrawl sin coste de API.

## Cómo funciona

Usa Playwright para controlar un navegador headless, ejecuta el render asíncrono y limpia el resultado a Markdown/JSON con estrategias de extracción configurables (incluido LLM-extraction opcional).

## Instalación rápida

`pip install crawl4ai` seguido de `crawl4ai-setup` para instalar los navegadores de Playwright. Requiere Chromium (lo instala el setup) y, para LLM-extraction, una clave de proveedor.

## Casos de uso

- Pipeline que recolecta muchas páginas para análisis
- Salida lista para IA
- Alternativa self-host a firecrawl a escala

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas volumen barato y self-host | quieres una API hosted simple sin operar navegadores (firecrawl) |

## Stack y modelos

- **Stack:** Python, Playwright
- **Modelos / API:** Agnóstico; la extracción con LLM es opcional y configurable por entorno.
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📦 **Dependencia del proyecto** — instálalo dentro de cada proyecto que lo use

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [firecrawl](firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |
| [gpt-researcher](gpt-researcher.md) | 30.6k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jina Reader](jina-reader.md) | 12.2k | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. |

## Enlaces

- 🐙 GitHub: [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- 🌐 Web: <https://crawl4ai.com/?ref=github-about>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
