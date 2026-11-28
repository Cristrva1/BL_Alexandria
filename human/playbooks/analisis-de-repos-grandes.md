[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 🧠 Análisis de repos grandes

> **Objetivo:** Que un agente de código entienda una base de código enorme sin gastar todo su contexto.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [Repomix](../fichas/repomix.md), [Claude Code](../fichas/claude-code.md)

**Prepara:** Un repo propio y una pregunta concreta sobre su código

**Primera prueba propuesta:** Empaqueta solo una parte y pide ubicar una función con referencias

**Qué comprobar:** Puedes abrir los archivos citados y comprobar la explicación

Revisa las exclusiones y los secretos antes de compartir archivos. Usa el índice o visor que responda a tu pregunta y revisa su licencia.

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  repomix["Repomix"] --> claude_code["Claude Code"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [Repomix](../fichas/repomix.md) | Empaqueta el repo (o una parte) en un archivo para el LLM | 29.3k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 2 | [codegraph](../fichas/codegraph.md) | Índice principal para consultar símbolos y llamadas a medida que cambia el código | 77.6k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 3 | [codebase-memory-mcp](../fichas/codebase-memory-mcp.md) | Ampliación para revisar el impacto de cambios de Git y abrir el visor local CBM Lens en beta | 48.6k | `curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh \| bash` |
| 4 | [GitNexus](../fichas/gitnexus.md) | Referencia opcional para explorar flujos y renombrados. El visor se conecta a gitnexus serve. Licencia PolyForm Noncommercial 1.0.0 | 48.5k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [graphify](../fichas/graphify.md) | Grafo de conocimiento con código, docs y esquemas | 148k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 6 | [Claude Code](../fichas/claude-code.md) | Agente que consulta los índices y edita el código | 156k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |

## 🔌 Cómo se conecta

Empieza con Repomix para empaquetar una parte del repositorio y dársela al agente. Añade CodeGraph para consultas repetidas de símbolos y llamadas. Codebase Memory MCP ayuda a revisar el impacto de cambios en Git. Graphify incorpora documentación al grafo. GitNexus queda como referencia opcional para explorar flujos y previsualizar renombrados con el índice del CLI.

## 🚫 Cuándo NO usar esta receta

Si el agente ya puede responder con referencias a unos pocos archivos, empieza con esos archivos directamente.

## 🔁 Variantes

- En lugar de [codegraph](../fichas/codegraph.md): [codebase-memory-mcp](../fichas/codebase-memory-mcp.md), [Serena](../fichas/serena.md), [graphify](../fichas/graphify.md)
- En lugar de [codebase-memory-mcp](../fichas/codebase-memory-mcp.md): [codegraph](../fichas/codegraph.md), [Serena](../fichas/serena.md), [graphify](../fichas/graphify.md)
- En lugar de [graphify](../fichas/graphify.md): [codegraph](../fichas/codegraph.md), [Serena](../fichas/serena.md), [codebase-memory-mcp](../fichas/codebase-memory-mcp.md)
- En lugar de [Claude Code](../fichas/claude-code.md): [Codex CLI](../fichas/codex.md), [Gemini CLI](../fichas/gemini-cli.md), [OpenCode](../fichas/opencode.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
