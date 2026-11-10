[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Navegadores y automatización web

# 🎭 playwright-cli

> Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 15.1k | Apache-2.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Resuelve el problema de los árboles de accesibilidad y los JSON de herramientas que inflan el prompt en cada turno.

## Por qué destaca

Alternativa token-eficiente a Playwright MCP, pensada para agentes de código (Claude Code, Cursor, Codex) que necesitan tocar la web sin quemar contexto. Procede del propio ecosistema Playwright de Microsoft, lo que garantiza compatibilidad con su API de automatización.

## Cómo funciona

Envuelve los comandos de Playwright en un CLI que el agente invoca paso a paso (navegar, clickar, leer), devolviendo salidas compactas en lugar de volcar el DOM o el accessibility tree enteros en cada turno.

## Instalación rápida

Parte del ecosistema Playwright; se usa vía `npx playwright`/`npm` dentro del agente de código. Requiere Node.js y los binarios de navegador (`npx playwright install`).

## Casos de uso

- Que un agente automatice el browser de forma token-eficiente
- Alternativa a Playwright MCP cuando el contexto aprieta
- Flujos de login/scraping guiados por un agente de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente vive en CLI y el contexto es un recurso caro | necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP) |

## Stack y modelos

- **Stack:** TypeScript/Node.js, CLI
- **Modelos / API:** Agentes de código (Claude Code, Cursor, Codex); no requiere un LLM propio.
- **Etiquetas:** `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli)
- 🌐 Web: <https://playwright.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
