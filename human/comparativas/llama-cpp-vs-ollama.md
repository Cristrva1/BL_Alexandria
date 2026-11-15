[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# llama.cpp vs Ollama

| | [llama.cpp](../fichas/llama-cpp.md) | [Ollama](../fichas/ollama.md) |
|---|---|---|
| Qué hace | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| ⭐ Estrellas | 134k | 187k |
| Elígelo si… | quieres el máximo control y rendimiento local | quieres modelos locales funcionando en minutos |
| Evítalo si… | prefieres simplicidad; mira `ollama` | necesitas servir a muchos usuarios con GPU; mira `vllm` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🟡 medio | 🟢 fácil |
| Licencia | MIT | MIT |
| Instalación | `brew install llama.cpp` | `curl -fsSL https://ollama.com/install.sh \| sh` |

## Regla práctica

- Elige **llama.cpp** si quieres el máximo control y rendimiento local.
- Elige **Ollama** si quieres modelos locales funcionando en minutos.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
