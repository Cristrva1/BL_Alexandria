[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 📚 servers

> Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 91.9k | Otra (ver repo) | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

## Qué es

Resuelve la falta de ejemplos canónicos: muestra cómo se construye un servidor MCP correcto, paso a paso.

## Por qué destaca

Es la fuente canónica y didáctica para entender cómo se construye un servidor MCP, respaldada por los mantenedores del propio protocolo. Incluye ejemplos prácticos (filesystem, fetch, git, etc.) que sirven de plantilla para los tuyos.

## Cómo funciona

Cada subdirectorio es un servidor MCP de ejemplo (filesystem, fetch, git…) que se ejecuta con `npx` y se conecta a un cliente compatible mediante el protocolo MCP sobre stdio o HTTP.

## Instalación rápida

Ejecutar un servidor del repo con `npx` (p. ej. `npx -y @modelcontextprotocol/server-filesystem /ruta`) y añadirlo a la config del cliente MCP. Requiere Node.js para los servers TS.

## Casos de uso

- Aprender a construir un servidor MCP
- Plantillas para arrancar el tuyo
- Ejemplos educativos de features (tools, resources, prompts)

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres ejemplos canónicos y plantillas fiables | buscas soluciones listas para producción (son demos educativas, no hardening) |

## Stack y modelos

- **Stack:** TypeScript/Python
- **Modelos / API:** Clientes MCP (Claude, Cursor, etc.); sin LLM propio.
- **Etiquetas:** `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-use](mcp-use.md) | 10.9k | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | 97.6k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |

## Enlaces

- 🐙 GitHub: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- 🌐 Web: <https://modelcontextprotocol.io>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
