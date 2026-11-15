[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🐍 scrapy

> Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 65.3k | BSD-3-Clause | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. Estándar de facto del scraping en Python desde hace más de una década, con enorme ecosistema de extensiones y base instalada masiva.

## Por qué destaca

Estándar de facto del scraping en Python desde hace más de una década, con enorme ecosistema de extensiones y base instalada masiva. Su robustez y extensibilidad lo mantienen vigente pese a su edad.

## Cómo funciona

Define spiders que emiten requests asíncronas sobre el motor Twisted, procesa respuestas con selectores (CSS/XPath) y pasa los items por pipelines de limpieza/almacenamiento.

## Instalación rápida

`pip install scrapy`; el comando `scrapy startproject` genera el andamiaje del proyecto. Requiere Python y, según el target, rotación de proxies/headers para evitar bloqueos.

## Casos de uso

- Spiders robustos
- Pipelines de extracción a gran escala
- Feeds estructurados (JSON/CSV) hacia un data warehouse

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un crawler sólido y configurable a escala | buscas salida lista para LLM o algo puntual sin curva de framework |

## Stack y modelos

- **Stack:** Python (Twisted)
- **Modelos / API:** N/A (no usa LLM).
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [scrapely](scrapely.md) | 1.9k | Librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales. |
| [crawlee-python](crawlee-python.md) | 9.7k | Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. |

## Enlaces

- 🐙 GitHub: [scrapy/scrapy](https://github.com/scrapy/scrapy)
- 🌐 Web: <https://scrapy.org>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
