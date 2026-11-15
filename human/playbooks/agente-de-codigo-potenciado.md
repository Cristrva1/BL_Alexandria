[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 🛠️ Agente de código potenciado

> **Objetivo:** Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [Claude Code](../fichas/claude-code.md), [superpowers](../fichas/superpowers.md)

**Prepara:** Un repo de prueba y una tarea pequeña

**Primera prueba propuesta:** Añade una metodología al agente y pide un cambio con su comprobación

**Qué comprobar:** Puedes revisar el diff y el resultado de la comprobación

La ruta mínima usa Claude Code; compara la compatibilidad de cada complemento antes de adaptarla a Codex o Antigravity

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  claude_code["Claude Code"] --> superpowers["superpowers"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [Claude Code](../fichas/claude-code.md) | Agente de código en la terminal (o Codex / opencode) | 156k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 2 | [superpowers](../fichas/superpowers.md) | Metodología: planificar, probar y revisar antes de dar por hecho | 318k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 3 | [Context7](../fichas/context7.md) | Documentación actualizada de librerías vía MCP | 64.8k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 4 | [Serena](../fichas/serena.md) | Búsqueda y edición semántica del código vía MCP | 31.4k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [claude-mem](../fichas/claude-mem.md) | Memoria persistente entre sesiones | 117k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 6 | [SkillSpector](../fichas/skillspector.md) | Audita skills de terceros antes de instalarlas | 26.1k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |

## 🔌 Cómo se conecta

Superpowers obliga al agente a planificar, escribir pruebas y revisar; Context7 le pasa la documentación vigente de cada librería; Serena le da navegación semántica del código en lugar de leer archivos enteros; claude-mem conserva decisiones entre sesiones. SkillSpector revisa cualquier skill nueva antes de instalarla.

## 🚫 Cuándo NO usar esta receta

Si solo haces cambios pequeños y puntuales, el agente tal cual basta: cada pieza añade contexto y configuración.

## 🔁 Variantes

- En lugar de [Claude Code](../fichas/claude-code.md): [Codex CLI](../fichas/codex.md), [Gemini CLI](../fichas/gemini-cli.md), [OpenCode](../fichas/opencode.md)
- En lugar de [superpowers](../fichas/superpowers.md): [Agent Skills (Addy Osmani)](../fichas/agent-skills.md)
- En lugar de [Context7](../fichas/context7.md): [DeepWiki Open](../fichas/deepwiki-open.md)
- En lugar de [Serena](../fichas/serena.md): [codegraph](../fichas/codegraph.md), [GitNexus](../fichas/gitnexus.md)
- En lugar de [claude-mem](../fichas/claude-mem.md): [Engram](../fichas/engram.md), [agentmemory](../fichas/agentmemory.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
