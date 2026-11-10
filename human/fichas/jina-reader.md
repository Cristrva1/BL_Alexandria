[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🕷️ Jina Reader

> Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 12.2k | Apache-2.0 | TypeScript | 2026-05-22 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Qué es

Pega `https://r.jina.ai/` delante de una URL y obtienes su contenido limpio. También busca en la web con `s.jina.ai`.

## Por qué destaca

La forma más simple de pasar una página a un LLM, sin instalar nada.

## Cómo funciona

Renderiza la página en un navegador, extrae el contenido principal y lo convierte a Markdown.

## Instalación rápida

No se instala: usa `curl https://r.jina.ai/https://ejemplo.com`; con clave de API tienes más cuota.

## Casos de uso

- Pasar artículos a un LLM
- Alimentar un RAG con páginas sueltas
- Lectura web para agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas leer páginas como Markdown al instante | vas a rastrear sitios completos; mira `crawl4ai` o `firecrawl` |

**Limitaciones:** El servicio gratuito tiene límites de uso; el self-host del repo está menos mantenido.

## Stack y modelos

- **Stack:** TypeScript, Puppeteer
- **Modelos / API:** No usa LLM para leer; usa modelos propios para limpieza en algunos modos.
- **Etiquetas:** `scraping` `rag` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [firecrawl](firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |
| [crawl4ai](crawl4ai.md) | 87.2k | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. |

## Enlaces

- 🐙 GitHub: [jina-ai/reader](https://github.com/jina-ai/reader)
- 🌐 Web: <https://jina.ai/reader>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
