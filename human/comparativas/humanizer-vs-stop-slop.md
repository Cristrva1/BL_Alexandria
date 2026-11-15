[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# Humanizer vs Stop Slop

| | [Humanizer](../fichas/humanizer.md) | [Stop Slop](../fichas/stop-slop.md) |
|---|---|---|
| Qué hace | Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA. | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. |
| ⭐ Estrellas | 69.1k | 18.9k |
| Elígelo si… | publicas textos redactados con IA y quieres que se lean como escritos por una persona | quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt |
| Evítalo si… | quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop` | prefieres una skill que reescriba mostrando su proceso y pueda imitar tu voz; mira `humanizer` |
| Ejecución | 🔀 híbrido | 🔀 híbrido |
| API de IA | Sin API de IA en la ruta básica | Sin API de IA en la ruta básica |
| Coste | Consumo del agente que ya utilizas | Consumo del agente que ya utilizas |
| Modelos locales | La función básica no necesita un modelo | La función básica no necesita un modelo |
| Setup | 🟢 fácil | 🟢 fácil |
| Licencia | MIT | MIT |
| Instalación | `/plugin marketplace add blader/humanizer` | `git clone https://github.com/hardikpandya/stop-slop ~/.claude/skills/stop-slop` |

## Regla práctica

- Elige **Humanizer** si publicas textos redactados con IA y quieres que se lean como escritos por una persona.
- Elige **Stop Slop** si quieres reglas de estilo compactas y portables que puedas usar como skill o dentro de un system prompt.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
