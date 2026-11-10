[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Navegadores y automatización web

# 🌐 Lightpanda

> Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 41.8k | AGPL-3.0 | Zig | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Ejecuta JavaScript y es compatible con Puppeteer y Playwright por CDP, usando una fracción de memoria. Ideal para scraping masivo.

## Por qué destaca

Arranque instantáneo y bajo consumo frente a Chrome headless.

## Cómo funciona

Motor de navegador propio en Zig con V8 para JavaScript y un servidor CDP.

## Instalación rápida

Descarga el binario de releases o `docker run -d -p 9222:9222 lightpanda/browser:nightly`.

## Casos de uso

- Scraping a gran escala barato
- Agentes web en servidores pequeños
- Pruebas rápidas por CDP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas muchos navegadores headless con poca memoria | necesitas compatibilidad total con sitios complejos; usa Chrome con `playwright` |

**Limitaciones:** Aún en beta: algunas APIs web no están implementadas.

## Stack y modelos

- **Stack:** Zig, V8
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `browser` `scraping`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Puppeteer](puppeteer.md) | 95.8k | Librería de Google para controlar Chrome y Firefox desde Node.js. |
| [playwright](playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Enlaces

- 🐙 GitHub: [lightpanda-io/browser](https://github.com/lightpanda-io/browser)
- 🌐 Web: <https://lightpanda.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
