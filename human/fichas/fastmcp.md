[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🧰 FastMCP

> La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 28.4k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Convierte funciones Python en herramientas MCP con un decorador y añade autenticación, composición de servidores y cliente de pruebas. Su versión 1 se integró en el SDK oficial.

## Por qué destaca

Es la librería más usada para crear servidores MCP en Python.

## Cómo funciona

Decoradores registran tools, resources y prompts; el servidor los expone por stdio o HTTP según el protocolo MCP.

## Instalación rápida

`pip install fastmcp` (o `uv add fastmcp`).

## Casos de uso

- Exponer tu API interna como MCP
- Herramientas propias para Claude Code
- Servidores MCP con OAuth

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres crear un servidor MCP en Python rápido | trabajas en TypeScript; mira `mcp-typescript-sdk` |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** No usa LLM: lo consumen los clientes MCP.
- **Etiquetas:** `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MCP Inspector](mcp-inspector.md) | 11.3k | Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. |
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MCP Python SDK](mcp-python-sdk.md) | 24.8k | SDK oficial de Python para crear servidores y clientes del Model Context Protocol. |

## Enlaces

- 🐙 GitHub: [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)
- 🌐 Web: <https://gofastmcp.com>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
