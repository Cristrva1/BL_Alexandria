[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Scraping guiado por LLM

# 🧾 llm-scraper

> Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 7k | MIT | TypeScript | 2026-10-26 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. Popular por su simplicidad: salida tipada y validada sin escribir parsers, integrándose directamente con Playwright y los SDKs de LLM.

## Por qué destaca

Popular por su simplicidad: salida tipada y validada sin escribir parsers, integrándose directamente con Playwright y los SDKs de LLM. El uso de Zod garantiza tipos correctos en tiempo de compilación.

## Cómo funciona

Carga la página con Playwright, la pasa a texto/markdown y pide al LLM que devuelva un objeto conforme al esquema Zod, garantizando tipos correctos y validación en runtime.

## Instalación rápida

`npm i llm-scraper playwright` y la SDK del proveedor de LLM elegido. Requiere Node.js, los binarios de Playwright y una clave de API de LLM.

## Casos de uso

- Extraer datos tipados de sitios
- Automatizar datasets estructurados
- Poblar una API/DB desde páginas sin backend propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres salida tipada y validada en stack TS | prefieres extracción semántica por grafos (Scrapegraph-ai) o trabajas en Python |

## Stack y modelos

- **Stack:** TypeScript, Playwright, Zod
- **Modelos / API:** LLMs vía SDK (OpenAI, Anthropic, etc.); agnóstico vía variables de entorno.
- **Etiquetas:** `scraping` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [firecrawl](firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Maxun](maxun.md) | 18.2k | Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. |

## Enlaces

- 🐙 GitHub: [mishushakov/llm-scraper](https://github.com/mishushakov/llm-scraper)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
