[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › Directorios, clientes y aprendizaje

# 🧩 mcp

> Núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 4.7k | Apache-2.0 | — | 2026-08-17 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Resuelve la fragmentación: cada integración de IA dejaba de ser ad-hoc y pasa a hablar un protocolo común.

## Por qué destaca

Es el protocolo de referencia del ecosistema, adoptado por Claude, Cursor, ChatGPT y muchos otros clientes, lo que lo convierte en la base sobre la que se construye todo lo demás. Su respaldo por Anthropic y la gobernanza abierta le dan tracción real frente a alternativas propietarias.

## Cómo funciona

Define el protocolo MCP (mensajes JSON-RPC 2.0 entre cliente y servidor sobre stdio o HTTP/SSE) y ofrece SDKs en TypeScript y Python para implementar servidores que exponen tools, resources y prompts conformes.

## Instalación rápida

`npm install @modelcontextprotocol/sdk` o `pip install mcp` según el lenguaje; requiere un cliente MCP (Claude Desktop, Cursor, etc.) para conectar.

## Casos de uso

- Base de interoperabilidad para tu app de IA
- Construir servidores/clientes conforme al estándar
- Exponer herramientas internas a cualquier asistente compatible

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| programas MCP a bajo nivel o necesitas conformidad estricta con la spec | prefieres un framework de alto nivel que abstraiga el protocolo (mcp-use) |

## Stack y modelos

- **Stack:** TypeScript/Python
- **Modelos / API:** Clientes MCP (Claude, Cursor, ChatGPT); agnóstico respecto al LLM.
- **Etiquetas:** `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-use](mcp-use.md) | 10.9k | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |
| [servers](servers.md) | 91.9k | Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad. |

## Enlaces

- 🐙 GitHub: [google/mcp](https://github.com/google/mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
