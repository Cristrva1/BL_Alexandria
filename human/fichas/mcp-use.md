[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🛠️ mcp-use

> Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

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

Resuelve el salto del SDK base (verboso) a algo productivo: registro de tools, inspector y despliegue incluidos.

## Por qué destaca

Abstrae el protocolo en una capa de alto nivel con SDK, inspector y documentación, lo que acorta el camino de la idea a producción frente a usar el SDK base. Su enfoque fullstack (TS y Python) y la integración con clientes como ChatGPT/Claude le dan versatilidad.

## Cómo funciona

Envuelve el protocolo MCP exponiendo APIs de alto nivel para registrar tools/resources y conectar con clientes (Claude, ChatGPT), gestionando el ciclo de vida del servidor y el despliegue sin que toques JSON-RPC a mano.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/mcp-use/mcp-use/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mcp-use para mi objetivo y necesito pasos guiados. Lee https://github.com/mcp-use/mcp-use/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `automation` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp](mcp.md) | 4.7k | Núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | 97.7k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangChain MCP Adapters](langchain-mcp-adapters.md) | 3.6k | Puente que convierte herramientas de servidores MCP en herramientas de LangChain y LangGraph. |
| [MCP TypeScript SDK](mcp-typescript-sdk.md) | 13.8k | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. |

## Enlaces

- 🐙 GitHub: [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)
- 🌐 Web: <https://manufact.com>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/mcp-use/mcp-use/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
