[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# Chrome DevTools MCP vs Playwright MCP

| | [Chrome DevTools MCP](../fichas/chrome-devtools-mcp.md) | [Playwright MCP](../fichas/playwright-mcp.md) |
|---|---|---|
| Qué hace | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |
| ⭐ Estrellas | 55.1k | 39.4k |
| Elígelo si… | tu agente necesita depurar una web como lo harías en DevTools | quieres que tu agente use un navegador real |
| Evítalo si… | solo quieres automatizar navegación; mira `playwright-mcp` | necesitas depurar rendimiento y consola; mira `chrome-devtools-mcp` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🟢 fácil | 🟢 fácil |
| Licencia | Apache-2.0 | Apache-2.0 |
| Instalación | `npx chrome-devtools-mcp@latest` | `npx @playwright/mcp@latest` |

## Regla práctica

- Elige **Chrome DevTools MCP** si tu agente necesita depurar una web como lo harías en DevTools.
- Elige **Playwright MCP** si quieres que tu agente use un navegador real.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
