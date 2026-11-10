[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 codebase-memory-mcp

> Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 48.4k | MIT | C | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Indexa repos en milisegundos y da al agente herramientas MCP para entender arquitectura, dependencias y cambios sin leer archivo por archivo.

## Por qué destaca

Indexación muy rápida incluso en repos enormes.

## Cómo funciona

Parsea el código a un grafo persistente local y lo expone por MCP e interfaces propias.

## Instalación rápida

Descarga el binario de releases y añádelo como servidor MCP a tu agente.

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
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `code` `mcp` `memory`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Serena](serena.md) | 31.3k | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codegraph](codegraph.md) | 77.3k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |
| [GitNexus](gitnexus.md) | 48.4k | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. |

## Enlaces

- 🐙 GitHub: [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)
- 🌐 Web: <https://deusdata.github.io/codebase-memory-mcp/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
