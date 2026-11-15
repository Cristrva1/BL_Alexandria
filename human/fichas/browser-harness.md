[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Navegadores y automatización web

# 🌐 Browser Harness

> Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 19k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Conecta el agente a tu navegador por CDP con un arnés pequeño y editable. Útil cuando necesitas libertad total y tus cuentas ya abiertas.

## Por qué destaca

De los creadores de browser-use; se configura con un solo prompt.

## Cómo funciona

Habla con Chrome por el protocolo DevTools y expone comandos simples que el agente invoca.

## Instalación rápida

Sigue el README: pide a tu agente que lo instale con el prompt indicado.

## Casos de uso

- Automatizar tareas en webs donde ya estás logueado
- Pruebas manuales asistidas
- Investigación con tu sesión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente debe usar tu navegador real con sesión | necesitas aislamiento; mira `playwright-mcp` |

**Limitaciones:** El agente actúa con tus cuentas reales: supervisa lo que hace.

## Stack y modelos

- **Stack:** Python, CDP
- **Modelos / API:** Usa el modelo de tu agente.
- **Etiquetas:** `browser` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Playwright MCP](playwright-mcp.md) | 39.4k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | 55.1k | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. |

## Enlaces

- 🐙 GitHub: [browser-use/browser-harness](https://github.com/browser-use/browser-harness)
- 🌐 Web: <https://browser-harness.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
