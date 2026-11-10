[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🦗 crawlee

> Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 26.4k | Apache-2.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. Mantenido por Apify, es la referencia de crawling en el ecosistema JavaScript y trae evasión de bloqueos lista de fábrica.

## Por qué destaca

Mantenido por Apify, es la referencia de crawling en el ecosistema JavaScript y trae evasión de bloqueos lista de fábrica. Su unificación HTTP+navegador evita mantener dos stacks separados.

## Cómo funciona

Gestiona una cola de URLs y un pool autoescalable de crawlers (Cheerio para HTTP o Playwright/Puppeteer para navegador), con rotación de proxies y huellas para evitar baneos.

## Instalación rápida

`npm i crawlee` o, para empezar, `npx crawlee create`. Requiere Node.js y, para el modo navegador, los binarios de Playwright/Puppeteer.

## Casos de uso

- Scraping a escala con rotación de proxies
- Colas y reintentos
- Crawlers que combinan HTTP rápido y navegador para JS pesado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| scrapeas con Node y necesitas antibloqueo | trabajas en Python (crawlee-python) o no necesitas evasión |

## Stack y modelos

- **Stack:** Node.js/TypeScript
- **Modelos / API:** N/A (no usa LLM).
- **Etiquetas:** `scraping` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Enlaces

- 🐙 GitHub: [apify/crawlee](https://github.com/apify/crawlee)
- 🌐 Web: <https://crawlee.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
