[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🧰 MCP TypeScript SDK

> SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.8k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Base de la mayoría de servidores MCP en Node.js, con transportes stdio y HTTP.

## Por qué destaca

SDK oficial y el más usado para servidores MCP en JavaScript.

## Cómo funciona

Clases McpServer y Client gestionan el protocolo; registras herramientas con esquemas Zod.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MCP TypeScript SDK para mi objetivo y necesito pasos guiados. Lee https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Servidor MCP para tu API en Node
- Clientes MCP en apps web
- Herramientas para agentes de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| creas servidores MCP en TypeScript | trabajas en Python; mira `fastmcp` |

## Stack y modelos

- **Stack:** TypeScript, Node.js, Zod
- **Etiquetas:** `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MCP Inspector](mcp-inspector.md) | 11.3k | Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-use](mcp-use.md) | 11k | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |

## Enlaces

- 🐙 GitHub: [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)
- 🌐 Web: <https://ts.sdk.modelcontextprotocol.io/v2>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
