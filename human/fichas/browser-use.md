[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Navegadores y automatización web

# 🌐 browser-use

> Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 121k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Resuelve la fragilidad del scraping basado en CSS: el agente "ve" la página como un humano y decide la siguiente acción.

## Por qué destaca

Uno de los proyectos de agentes-web más virales y populares, por permitir automatización robusta guiada por modelos multimodales incluso ante pop-ups y cambios de layout. Su adopción masiva y la opción de cloud gestionado lo consolidan como referencia en navegación agentica.

## Cómo funciona

Controla el navegador con Playwright, extrae el estado de la página (DOM simplificado + capturas) y lo pasa a un LLM con visión que devuelve la siguiente acción de click/escritura/navegación, repitiendo el bucle hasta cumplir el objetivo.

## Instalación rápida

`pip install browser-use` y `playwright install`; requiere clave de un LLM con visión (OpenAI, Anthropic o Google). Para escala/stealth existe cloud gestionado.

## Casos de uso

- Agente que entra a un e-commerce, filtra y compra
- Recuperación ante pop-ups/errores y CAPTCHAs suaves
- Flujos multi-paso donde los selectores cambian entre visitas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres navegación como humano y tolerancia a cambios de UI | necesitas scripts deterministas y baratos (playwright) o no quieres depender de un LLM por paso |

## Stack y modelos

- **Stack:** Python 3.11+, Rust (core), Playwright
- **Modelos / API:** Multimodales con visión (GPT-4o, Claude, Gemini); agnóstico vía variables de entorno.
- **Etiquetas:** `automation` `browser` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [gpt-researcher](gpt-researcher.md) | 30.6k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Gemini Computer Use (preview)](computer-use-preview.md) | 3.3k | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. |
| [Stagehand](stagehand.md) | 26k | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. |
| [Skyvern](skyvern.md) | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. |
| [Playwright MCP](playwright-mcp.md) | 39.4k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |

## Enlaces

- 🐙 GitHub: [browser-use/browser-use](https://github.com/browser-use/browser-use)
- 🌐 Web: <https://browser-use.com>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
