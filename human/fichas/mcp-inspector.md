[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🧰 MCP Inspector

> Herramienta oficial para probar y depurar servidores MCP desde una interfaz web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.3k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

Conéctate a cualquier servidor MCP, lista sus herramientas y recursos y lánzalos a mano para ver respuestas y errores.

## Por qué destaca

Es la forma estándar de depurar un servidor MCP antes de conectarlo a un agente.

## Cómo funciona

Un proxy local habla con el servidor por stdio o HTTP y una UI web muestra cada mensaje del protocolo.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npx @modelcontextprotocol/inspector
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/modelcontextprotocol/inspector/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MCP Inspector para mi objetivo y necesito pasos guiados. Lee https://github.com/modelcontextprotocol/inspector/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Depurar un servidor MCP nuevo
- Probar herramientas sin agente
- Ver los mensajes del protocolo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| desarrollas un servidor MCP | solo usas servidores ya hechos |

## Stack y modelos

- **Stack:** TypeScript, React
- **Etiquetas:** `mcp` `evaluation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FastMCP](fastmcp.md) | 28.5k | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. |
| [MCP TypeScript SDK](mcp-typescript-sdk.md) | 13.8k | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. |

## Enlaces

- 🐙 GitHub: [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)
- 🌐 Web: <https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/modelcontextprotocol/inspector/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
