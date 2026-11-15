[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 codebase-memory-mcp

> Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 48.6k | MIT | C | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Indexa repos en milisegundos y da al agente herramientas MCP para entender arquitectura, dependencias y cambios sin leer archivo por archivo.

## Por qué destaca

Indexación muy rápida incluso en repos enormes.

## Cómo funciona

Parsea el código a un grafo persistente local y lo expone por MCP e interfaces propias.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

[Instrucciones originales de instalación](https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar codebase-memory-mcp para mi objetivo y necesito pasos guiados. Lee https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Entender un repo grande con un agente
- Analizar impacto de cambios
- Memoria de arquitectura

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente trabaja en repos grandes | tu repo es pequeño; usa `repomix` |

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `code` `mcp` `memory`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Serena](serena.md) | 31.4k | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codegraph](codegraph.md) | 77.6k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |
| [GitNexus](gitnexus.md) | 48.5k | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. |

## Enlaces

- 🐙 GitHub: [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)
- 🌐 Web: <https://deusdata.github.io/codebase-memory-mcp/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
