[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Conectar herramientas con MCP

SDKs, servidores, clientes y directorios MCP. Un servidor aporta acciones o datos; el modelo y su acceso pertenecen al cliente que lo utiliza.

24 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [FastMCP](../fichas/fastmcp.md) | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. | Sin API de IA en la ruta básica |
| [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md) | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. | Sin API de IA en la ruta básica |
| [Context7](../fichas/context7.md) | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. | Sin API de IA en la ruta básica |
| [Playwright MCP](../fichas/playwright-mcp.md) | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. | Sin API de IA en la ruta básica |
| [MCP for Beginners](../fichas/mcp-for-beginners.md) | Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python. | Sin API de IA en la ruta básica |

## Secciones

- [SDKs y frameworks para crear MCP](#sdks-y-frameworks-para-crear-mcp) — 6 repos
- [Servidores MCP destacados](#servidores-mcp-destacados) — 13 repos
- [Directorios, clientes y aprendizaje](#directorios-clientes-y-aprendizaje) — 5 repos

## SDKs y frameworks para crear MCP

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FastMCP](../fichas/fastmcp.md) | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. | quieres crear un servidor MCP en Python rápido | Sin API de IA en la ruta básica |
| [MCP TypeScript SDK](../fichas/mcp-typescript-sdk.md) | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. | creas servidores MCP en TypeScript | Sin API de IA en la ruta básica |
| [MCP Python SDK](../fichas/mcp-python-sdk.md) | SDK oficial de Python para crear servidores y clientes del Model Context Protocol. | quieres el SDK oficial con mínima dependencia | Sin API de IA en la ruta básica |
| [MCP Inspector](../fichas/mcp-inspector.md) | Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. | desarrollas un servidor MCP | Sin API de IA en la ruta básica |
| [mcp-use](../fichas/mcp-use.md) | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. | construyes un servidor MCP propio y quieres productividad | Sin API de IA en la ruta básica |
| [LangChain MCP Adapters](../fichas/langchain-mcp-adapters.md) | Puente que convierte herramientas de servidores MCP en herramientas de LangChain y LangGraph. | usas LangGraph y quieres herramientas MCP | Sin API de IA en la ruta básica |

## Servidores MCP destacados

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Context7](../fichas/context7.md) | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. | tu agente de código usa librerías que cambian a menudo | Sin API de IA en la ruta básica |
| [Playwright MCP](../fichas/playwright-mcp.md) | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. | quieres que tu agente use un navegador real | Sin API de IA en la ruta básica |
| [servers](../fichas/servers.md) | Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad. | quieres ejemplos canónicos y plantillas fiables | Sin API de IA en la ruta básica |
| [Chrome DevTools MCP](../fichas/chrome-devtools-mcp.md) | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. | tu agente necesita depurar una web como lo harías en DevTools | Sin API de IA en la ruta básica |
| [GitHub MCP Server](../fichas/github-mcp-server.md) | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. | tu agente trabaja con GitHub | Sin API de IA en la ruta básica |
| [Blender MCP](../fichas/blender-mcp.md) | Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP. | quieres manejar Blender con tu agente | Sin API de IA en la ruta básica |
| [Serena](../fichas/serena.md) | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. | tu agente trabaja en un repo grande y gasta muchos tokens leyendo | Sin API de IA en la ruta básica |
| [Figma Context MCP](../fichas/figma-context-mcp.md) | Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos. | implementas diseños de Figma con un agente de código | Sin API de IA en la ruta básica |
| [unity-mcp](../fichas/unity-mcp.md) | Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity. | buscas esta función: Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity. | Sin API de IA en la ruta básica |
| [GhidraMCP](../fichas/ghidramcp.md) | Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios. | buscas esta función: Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios. | Sin API de IA en la ruta básica |
| [treg](../fichas/treg.md) | Registro y conexión de herramientas para agentes que organiza acceso a servicios, cuentas y credenciales de proveedores. | buscas esta función: Registro y conexión de herramientas para agentes que organiza acceso a servicios, cuentas y credenciales de proveedores. | Sin API de IA en la ruta básica |
| [annas-mcp](../fichas/annas-mcp.md) | Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos. | necesitas integrar búsquedas de documentos en un cliente MCP | Sin API de IA en la ruta básica |
| [mcp-neo4j](../fichas/mcp-neo4j.md) | Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud. | usas Neo4j con IA y quieres que el asistente hable Cypher | Sin API de IA en la ruta básica |

## Directorios, clientes y aprendizaje

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [MCP for Beginners](../fichas/mcp-for-beginners.md) | Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python. | quieres aprender MCP de forma estructurada | Sin API de IA en la ruta básica |
| [public-apis](../fichas/public-apis.md) | Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos. | buscas datos externos y no sabes qué API usar | Sin API de IA en la ruta básica |
| [awesome-mcp-servers](../fichas/awesome-mcp-servers.md) | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. | buscas antes de construir | Sin API de IA en la ruta básica |
| [Awesome MCP Clients](../fichas/awesome-mcp-clients.md) | Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y agentes. | buscas un cliente para tus servidores MCP | Sin API de IA en la ruta básica |
| [mcp](../fichas/mcp.md) | Núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto. | programas MCP a bajo nivel o necesitas conformidad estricta con la spec | Depende de la ruta elegida |

## Recetas relacionadas

- [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md) — Exponer tus datos o herramientas a Claude, ChatGPT, Cursor y otros agentes con Model Context Protocol.
- [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
