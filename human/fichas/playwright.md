[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Navegadores y automatización web

# 🎭 playwright

> Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 99.7k | Apache-2.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. Se ha convertido en el estándar moderno de automatización de browser, desplazando a Selenium/Puppeteer por su fiabilidad y su auto-espera de elementos.

## Por qué destaca

Se ha convertido en el estándar moderno de automatización de browser, desplazando a Selenium/Puppeteer por su fiabilidad y su auto-espera de elementos. Microsoft lo mantiene y tiene bindings para Node.js, Python, Java y .NET.

## Cómo funciona

Lanza navegadores reales en modo headless o con UI y los controla por protocolo (CDP), con waits automáticos, interceptación de red y captura de DOM/screenshots/traces.

## Instalación rápida

`npm i playwright` o `pip install playwright`, seguido de `playwright install` para los navegadores. Requiere descargar los binarios de Chromium/Firefox/WebKit (~varios cientos de MB).

## Casos de uso

- Testing E2E
- Scraping dinámico
- Scripting reproducible

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas control preciso y reproducible del browser | quieres que el agente navegue por visión (browser-use) o no necesitas un navegador real |

## Stack y modelos

- **Stack:** Node.js o Python (también Java/.NET)
- **Modelos / API:** Se integra con MCP y agentes; no usa LLM por sí mismo.
- **Etiquetas:** `automation` `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [crawlee](crawlee.md) | 26.4k | Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Puppeteer](puppeteer.md) | 95.8k | Librería de Google para controlar Chrome y Firefox desde Node.js. |
| [Selenium](selenium.md) | 34.6k | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright](https://github.com/microsoft/playwright)
- 🌐 Web: <https://playwright.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
