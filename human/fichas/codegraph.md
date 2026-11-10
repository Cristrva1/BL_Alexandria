[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 📊 codegraph

> CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 77.3k | MIT | TypeScript | 2026-11-01 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Resuelve el coste de contexto de los agentes en repos grandes.

## Por qué destaca

Convierte repos enormes en algo navegable para la IA con coste casi nulo; muy valorado en flujos de agentes de código por su ahorro real de tokens y tool calls. Su acoplamiento con Claude Code, Gemini y Cursor sin modelo propio lo hace fácil de adoptar.

## Cómo funciona

Construye un índice semántico local del repositorio (símbolos, referencias, flujo) que el asistente consulta vía comandos; se acopla a Claude Code, Gemini y Cursor sin necesidad de un modelo propio ni de enviar código a la nube.

## Instalación rápida

`npm install -g codegraph` (binario autónomo de Node.js) y luego `codegraph index .`. Requiere Node.js; el índice se regenera al cambiar el código.

## Casos de uso

- `codegraph index .` para que el asistente entienda el flujo sin leer archivo por archivo
- Onboarding de IA en monorepos grandes
- Reducir tool calls en revisiones de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas repos grandes y el contexto del agente es caro | tu base de código es pequeña y no justifica mantener un índice |

## Stack y modelos

- **Stack:** JavaScript/Node.js (binario autónomo)
- **Modelos / API:** No requiere IA; se acopla a Claude Code, Gemini, Cursor.
- **Etiquetas:** `code` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphify](graphify.md) | 145k | Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos. |
| [headroom](headroom.md) | 79.3k | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codebase-memory-mcp](codebase-memory-mcp.md) | 48.4k | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. |
| [Serena](serena.md) | 31.3k | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. |

## Enlaces

- 🐙 GitHub: [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)
- 🌐 Web: <https://colbymchenry.github.io/codegraph/>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
