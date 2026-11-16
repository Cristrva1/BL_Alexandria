[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 🧠 Análisis de repos grandes

> **Objetivo:** Que un agente de código entienda una base de código enorme sin gastar todo su contexto.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [Repomix](../fichas/repomix.md), [Claude Code](../fichas/claude-code.md)

**Prepara:** Un repo propio y una pregunta concreta sobre su código

**Primera prueba propuesta:** Empaqueta solo una parte y pide ubicar una función con referencias

**Qué comprobar:** Puedes abrir los archivos citados y comprobar la explicación

Revisa exclusiones y secretos antes de compartir código; los grafos son otra ampliación y tienen sus propias licencias

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  repomix["Repomix"] --> claude_code["Claude Code"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [Repomix](../fichas/repomix.md) | Empaqueta el repo (o una parte) en un archivo para el LLM | 29.3k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 2 | [codegraph](../fichas/codegraph.md) | Grafo de código pre-indexado que se sincroniza con los cambios | 77.6k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 3 | [GitNexus](../fichas/gitnexus.md) | Explora dependencias y flujos sin servidor | 48.5k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 4 | [graphify](../fichas/graphify.md) | Grafo de conocimiento con código, docs y esquemas | 148k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [Claude Code](../fichas/claude-code.md) | Agente que consulta los índices y edita el código | 156k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |

## 🔌 Cómo se conecta

CodeGraph y graphify construyen índices estructurales que el agente consulta en lugar de leer archivos completos; GitNexus ayuda a recorrer dependencias; Repomix empaqueta solo la parte relevante cuando necesitas pasar código a un chat. Claude Code (o Codex) usa todo eso como contexto barato.

## 🚫 Cuándo NO usar esta receta

Si el repo es pequeño (menos de unas 10.000 líneas), el agente de código con referencias directas a archivos basta.

## 🔁 Variantes

- En lugar de [Repomix](../fichas/repomix.md): [GitNexus](../fichas/gitnexus.md)
- En lugar de [codegraph](../fichas/codegraph.md): [codebase-memory-mcp](../fichas/codebase-memory-mcp.md), [Serena](../fichas/serena.md)
- En lugar de [GitNexus](../fichas/gitnexus.md): [Repomix](../fichas/repomix.md), [codebase-memory-mcp](../fichas/codebase-memory-mcp.md), [Serena](../fichas/serena.md)
- En lugar de [Claude Code](../fichas/claude-code.md): [Codex CLI](../fichas/codex.md), [Gemini CLI](../fichas/gemini-cli.md), [OpenCode](../fichas/opencode.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
