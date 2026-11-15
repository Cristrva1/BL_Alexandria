[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Scraping guiado por LLM

# 🧠 Maxun

> Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 18.2k | AGPL-3.0 | TypeScript | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Grabas lo que quieres extraer haciendo clic en la página y Maxun crea un robot que lo repite, con paginación y programación. Ideal para equipos sin programadores.

## Por qué destaca

Alternativa abierta a herramientas como Browse AI, auto-hospedable.

## Cómo funciona

Un grabador en el navegador captura acciones y selectores; un ejecutor con Playwright las repite y guarda los datos.

## Instalación rápida

Self-host con `docker compose up -d` siguiendo el README.

## Casos de uso

- Monitorear precios de la competencia
- Extraer listados a Google Sheets
- APIs de sitios sin API

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres extraer datos web sin programar | programas y prefieres librerías; mira `crawl4ai` o `scrapy` |

**Limitaciones:** Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** TypeScript, Playwright, PostgreSQL, Docker
- **Modelos / API:** Opcionalmente usa LLM para extracción.
- **Etiquetas:** `scraping` `automation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Scrapegraph-ai](scrapegraph-ai.md) | 32.7k | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. |
| [llm-scraper](llm-scraper.md) | 7k | Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. |

## Enlaces

- 🐙 GitHub: [getmaxun/maxun](https://github.com/getmaxun/maxun)
- 🌐 Web: <https://www.maxun.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
