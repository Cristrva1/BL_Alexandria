[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🩹 Scrapling

> Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 101k | BSD-3-Clause | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. Proyecto en alza por su enfoque "auto-reparable" de selectores, que evita reescribir scrapers cada vez que el sitio se actualiza.

## Por qué destaca

Proyecto en alza por su enfoque "auto-reparable" de selectores, que evita reescribir scrapers cada vez que el sitio se actualiza. Sus fetchers sigilosos imitan navegadores reales para sortear bloqueos.

## Cómo funciona

Rastrea atributos y posiciones de los elementos para reencontrarlos tras cambios en el DOM, con fetchers sigilosos (Camoufox/Playwright) que imitan navegadores reales para evadir detección.

## Instalación rápida

`pip install scrapling` (con `scrapling install` para los navegadores del modo sigiloso). Requiere Python y, para el modo stealth, los binarios de navegador que instala el subcomando.

## Casos de uso

- Páginas que cambian de estructura
- Evadir bloqueos sin reescribir selectores
- Scraping resiliente sobre sitios volátiles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| los sitios cambian o te bloquean a menudo | el target es estable y simple, o no necesitas stealth |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** N/A (no usa LLM).
- **Etiquetas:** `automation` `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [scrapy](scrapy.md) | 65.3k | Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. |

## Enlaces

- 🐙 GitHub: [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
- 🌐 Web: <https://scrapling.readthedocs.io/en/latest/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
