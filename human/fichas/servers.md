[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 📚 servers

> Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 92k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo. |
| Coste | Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la falta de ejemplos canónicos: muestra cómo se construye un servidor MCP correcto, paso a paso.

## Por qué destaca

Es la fuente canónica y didáctica para entender cómo se construye un servidor MCP, respaldada por los mantenedores del propio protocolo. Incluye ejemplos prácticos (filesystem, fetch, git, etc.) que sirven de plantilla para los tuyos.

## Cómo funciona

Cada subdirectorio es un servidor MCP de ejemplo (filesystem, fetch, git…) que se ejecuta con `npx` y se conecta a un cliente compatible mediante el protocolo MCP sobre stdio o HTTP.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

1. Abre el material original y elige un capítulo o ejemplo.
2. Revisa los requisitos de ese ejemplo antes de instalar dependencias.
3. Usa las alternativas y recetas para situarlo dentro de tu proyecto.

[Instrucciones originales de instalación](https://github.com/modelcontextprotocol/servers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar servers para mi objetivo y necesito pasos guiados. Lee https://github.com/modelcontextprotocol/servers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-use](mcp-use.md) | 11k | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | 97.7k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |

## Enlaces

- 🐙 GitHub: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- 🌐 Web: <https://modelcontextprotocol.io>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/modelcontextprotocol/servers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
