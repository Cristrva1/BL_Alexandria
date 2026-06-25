# mcp vs mcp-use

Generado: 2026-06-25T03:39:27.698706+00:00

| Criterio | mcp | mcp-use |
|---|---|---|
| Uso real | núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto. | framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |
| Elegir si | programas MCP a bajo nivel | construyes un servidor MCP propio |
| Evitar si | prefieres un framework de alto nivel ([mcp-use](#-mcp-use)). | solo buscas usar uno ya hecho. |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `mcp` si su caso de uso encaja mejor ahora. Deja `mcp-use` como alternativa, salvo que el proyecto necesite explicitamente ambos.
