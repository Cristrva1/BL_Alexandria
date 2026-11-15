[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 4. Scraping, Búsqueda & Research Web](04-scraping-b-squeda-research-web.md) · [6. Memoria, RAG & LLM Ops ➡️](06-memoria-rag-llm-ops.md)

# 🔌 5. MCP & Conectividad

> SDKs para crear servidores MCP, servidores destacados (navegador, GitHub, diseño, 3D), directorios y APIs públicas.

**20 repos** · 3 subcategorías · ⭐ 1.1M estrellas en total · 🆕 10 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [FastMCP](../fichas/fastmcp.md) | 28.4k | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. | `pip install fastmcp` |
| [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md) | 13.7k | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. | `npm install @modelcontextprotocol/sdk` |
| [Context7](../fichas/context7.md) | 64.5k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. | `npx -y @upstash/context7-mcp` |
| [Playwright MCP](../fichas/playwright-mcp.md) | 39.4k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. | `npx @playwright/mcp@latest` |
| [MCP for Beginners](../fichas/mcp-for-beginners.md) | 17.6k | Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python. | No se instala: abre el repo y sigue las lecciones. |

## 🧭 Subcategorías

- [SDKs y frameworks para crear MCP](#sdks-y-frameworks-para-crear-mcp) — 6 repos
- [Servidores MCP destacados](#servidores-mcp-destacados) — 9 repos
- [Directorios, clientes y aprendizaje](#directorios-clientes-y-aprendizaje) — 5 repos

## SDKs y frameworks para crear MCP

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [FastMCP](../fichas/fastmcp.md) 🆕 | 28.4k | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. | quieres crear un servidor MCP en Python rápido | 🟢 |
| ⭐ [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md) 🆕 | 13.7k | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. | creas servidores MCP en TypeScript | 🟢 |
| [MCP Python SDK](../fichas/mcp-python-sdk.md) 🆕 | 24.8k | SDK oficial de Python para crear servidores y clientes del Model Context Protocol. | quieres el SDK oficial con mínima dependencia | 🟢 |
| [MCP Inspector](../fichas/mcp-inspector.md) 🆕 | 11.3k | Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. | desarrollas un servidor MCP | 🟢 |
| [mcp-use](../fichas/mcp-use.md) | 10.9k | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. | construyes un servidor MCP propio y quieres productividad | 🟡 |
| [LangChain MCP Adapters](../fichas/langchain-mcp-adapters.md) | 3.6k | Puente que convierte herramientas de servidores MCP en herramientas de LangChain y LangGraph. | usas LangGraph y quieres herramientas MCP | 🟢 |

## Servidores MCP destacados

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Context7](../fichas/context7.md) | 64.5k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. | tu agente de código usa librerías que cambian a menudo | 🟢 |
| ⭐ [Playwright MCP](../fichas/playwright-mcp.md) 🆕 | 39.4k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. | quieres que tu agente use un navegador real | 🟢 |
| [servers](../fichas/servers.md) | 91.9k | Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad. | quieres ejemplos canónicos y plantillas fiables | 🟡 |
| [Chrome DevTools MCP](../fichas/chrome-devtools-mcp.md) 🆕 | 55.1k | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. | tu agente necesita depurar una web como lo harías en DevTools | 🟢 |
| [GitHub MCP Server](../fichas/github-mcp-server.md) | 34.4k | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. | tu agente trabaja con GitHub | 🟢 |
| [Blender MCP](../fichas/blender-mcp.md) 🆕 | 33.9k | Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP. | quieres manejar Blender con tu agente | 🟢 |
| [Serena](../fichas/serena.md) 🆕 | 31.3k | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. | tu agente trabaja en un repo grande y gasta muchos tokens leyendo | 🟢 |
| [Figma Context MCP](../fichas/figma-context-mcp.md) 🆕 | 16.2k | Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos. | implementas diseños de Figma con un agente de código | 🟢 |
| [mcp-neo4j](../fichas/mcp-neo4j.md) | 989 | Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud. | usas Neo4j con IA y quieres que el asistente hable Cypher | 🟡 |

## Directorios, clientes y aprendizaje

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [MCP for Beginners](../fichas/mcp-for-beginners.md) 🆕 | 17.6k | Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python. | quieres aprender MCP de forma estructurada | 🟢 |
| [public-apis](../fichas/public-apis.md) | 498k | Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos. | buscas datos externos y no sabes qué API usar | 🟢 |
| [awesome-mcp-servers](../fichas/awesome-mcp-servers.md) | 97.6k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. | buscas antes de construir | 🟢 |
| [Awesome MCP Clients](../fichas/awesome-mcp-clients.md) | 6.6k | Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y agentes. | buscas un cliente para tus servidores MCP | 🟢 |
| [mcp](../fichas/mcp.md) | 4.7k | Núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto. | programas MCP a bajo nivel o necesitas conformidad estricta con la spec | 🟡 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### FastMCP, MCP Python SDK

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [FastMCP](../fichas/fastmcp.md) | 28.4k | quieres crear un servidor MCP en Python rápido | trabajas en TypeScript; mira `mcp-typescript-sdk` |
| [MCP Python SDK](../fichas/mcp-python-sdk.md) | 24.8k | quieres el SDK oficial con mínima dependencia | quieres funciones extra como auth y composición; mira `fastmcp` |

### MCP TypeScript SDK, mcp-use, LangChain MCP Adapters

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md) | 13.7k | creas servidores MCP en TypeScript | trabajas en Python; mira `fastmcp` |
| [mcp-use](../fichas/mcp-use.md) | 10.9k | construyes un servidor MCP propio y quieres productividad | solo buscas usar uno ya hecho (awesome-mcp-servers) o necesitas control a nivel spec |
| [LangChain MCP Adapters](../fichas/langchain-mcp-adapters.md) | 3.6k | usas LangGraph y quieres herramientas MCP | no usas LangChain |

### Playwright MCP, Chrome DevTools MCP

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Playwright MCP](../fichas/playwright-mcp.md) | 39.4k | quieres que tu agente use un navegador real | necesitas depurar rendimiento y consola; mira `chrome-devtools-mcp` |
| [Chrome DevTools MCP](../fichas/chrome-devtools-mcp.md) | 55.1k | tu agente necesita depurar una web como lo harías en DevTools | solo quieres automatizar navegación; mira `playwright-mcp` |

## 🧪 Recetas que usan esta categoría

- [🔌 Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md) — Exponer tus datos o herramientas a Claude, ChatGPT, Cursor y otros agentes con Model Context Protocol.
- [🛠️ Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
