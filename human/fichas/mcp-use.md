[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🛠️ mcp-use

> Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 10.9k | MIT | TypeScript | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Resuelve el salto del SDK base (verboso) a algo productivo: registro de tools, inspector y despliegue incluidos.

## Por qué destaca

Abstrae el protocolo en una capa de alto nivel con SDK, inspector y documentación, lo que acorta el camino de la idea a producción frente a usar el SDK base. Su enfoque fullstack (TS y Python) y la integración con clientes como ChatGPT/Claude le dan versatilidad.

## Cómo funciona

Envuelve el protocolo MCP exponiendo APIs de alto nivel para registrar tools/resources y conectar con clientes (Claude, ChatGPT), gestionando el ciclo de vida del servidor y el despliegue sin que toques JSON-RPC a mano.

## Instalación rápida

`npm install mcp-use` o `pip install mcp-use` según el stack; requiere un cliente MCP para probar el resultado.

## Casos de uso

- Exponer datos/herramientas internas vía MCP
- Pasar de local a app desplegable
- Prototipar un servidor con inspector antes de producción

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes un servidor MCP propio y quieres productividad | solo buscas usar uno ya hecho (awesome-mcp-servers) o necesitas control a nivel spec |

## Stack y modelos

- **Stack:** TypeScript o Python, React (apps)
- **Modelos / API:** ChatGPT, Claude y agentes MCP; agnóstico vía variables de entorno.
- **Etiquetas:** `automation` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp](mcp.md) | 4.7k | Núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | 97.6k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangChain MCP Adapters](langchain-mcp-adapters.md) | 3.6k | Puente que convierte herramientas de servidores MCP en herramientas de LangChain y LangGraph. |
| [MCP TypeScript SDK](mcp-typescript-sdk.md) | 13.7k | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. |

## Enlaces

- 🐙 GitHub: [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)
- 🌐 Web: <https://manufact.com>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
