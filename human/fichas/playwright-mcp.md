[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Playwright MCP

> Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 39.4k | Apache-2.0 | TypeScript | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Da a tu agente un navegador real controlado por el árbol de accesibilidad, sin depender de capturas. Ideal para pruebas y automatización web.

## Por qué destaca

Oficial, rápido y determinista gracias a usar el árbol de accesibilidad.

## Cómo funciona

Lanza un navegador con Playwright y expone herramientas MCP para navegar, hacer clic, escribir y leer la página.

## Instalación rápida

Añade a tu cliente MCP: `npx @playwright/mcp@latest`.

## Casos de uso

- Agente que prueba tu web
- Rellenar formularios automáticamente
- Extraer datos de páginas dinámicas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres que tu agente use un navegador real | necesitas depurar rendimiento y consola; mira `chrome-devtools-mcp` |

## Stack y modelos

- **Stack:** TypeScript, Playwright
- **Modelos / API:** No usa LLM: lo usa tu agente.
- **Etiquetas:** `mcp` `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [playwright](playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | 55.1k | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. |
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Browser Harness](browser-harness.md) | 19k | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
- 🌐 Web: <https://www.npmjs.com/package/@playwright/mcp>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
