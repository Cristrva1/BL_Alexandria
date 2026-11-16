[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 🔌 Construir una app o servidor MCP

> **Objetivo:** Exponer tus datos o herramientas a Claude, ChatGPT, Cursor y otros agentes con Model Context Protocol.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [FastMCP](../fichas/fastmcp.md), [MCP Inspector](../fichas/mcp-inspector.md)

**Prepara:** Una acción de solo lectura y datos de prueba

**Primera prueba propuesta:** Expón una herramienta pequeña y compruébala con el inspector

**Qué comprobar:** La entrada y la salida son las esperadas y el cliente puede descubrir la herramienta

Elige Python o TypeScript para construir la misma capa; añade autenticación y permisos según el entorno antes de compartirla

**Otras rutas, no piezas que debas sumar:** [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md)

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  fastmcp["FastMCP"] --> mcp_inspector["MCP Inspector"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [awesome-mcp-servers](../fichas/awesome-mcp-servers.md) | Comprueba primero si ya existe un servidor para tu caso | 97.7k | Filtra por función y sistema operativo y contrasta el README de dos servidores. Comprue… |
| 2 | [FastMCP](../fichas/fastmcp.md) | Framework Python para escribir el servidor en pocas líneas | 28.5k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 3 | [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md) | SDK oficial si tu servidor es TypeScript | 13.8k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 4 | [MCP Inspector](../fichas/mcp-inspector.md) | Prueba y depura el servidor antes de conectarlo | 11.3k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [servers](../fichas/servers.md) | Implementaciones de referencia para copiar patrones | 92k | Elige un servidor de referencia y comprueba sus permisos sobre datos ficticios. Comprue… |
| 6 | [mcp-use](../fichas/mcp-use.md) | Apps MCP y clientes full-stack cuando necesitas UI | 11k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |

## 🔌 Cómo se conecta

Busca en awesome-mcp-servers antes de construir. Si no existe, FastMCP (Python) o el SDK oficial de TypeScript te dan el servidor con poco código; los servidores de referencia muestran cómo modelar tools, recursos y prompts. MCP Inspector valida el servidor antes de conectarlo a Claude Code, Codex o Cursor. mcp-use sirve cuando quieres una app MCP con interfaz propia.

## 🚫 Cuándo NO usar esta receta

Si solo vas a consumir un servidor que ya existe, no construyas uno: instálalo desde su README.

## 🔁 Variantes

- En lugar de [FastMCP](../fichas/fastmcp.md): [MCP Python SDK](../fichas/mcp-python-sdk.md)
- En lugar de [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md): [mcp-use](../fichas/mcp-use.md)
- En lugar de [mcp-use](../fichas/mcp-use.md): [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
