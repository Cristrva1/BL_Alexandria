[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# llama.cpp vs Ollama

| | [llama.cpp](../fichas/llama-cpp.md) | [Ollama](../fichas/ollama.md) |
|---|---|---|
| Qué hace | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| ⭐ Estrellas | 135k | 187k |
| Elígelo si… | Tu objetivo encaja con estos ejemplos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo | Tu objetivo encaja con estos ejemplos: Probar un LLM local; Conectar un modelo local a Codex CLI |
| Evítalo si… | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| Ejecución | 🏠 local | 🏠 local |
| API de IA | Sin clave propia de API de IA en la ruta básica | API de IA opcional |
| Coste | Sin pago a un modelo en la ruta básica | El coste depende del proveedor o la ruta |
| Modelos locales | Modelos locales documentados | Modelos locales documentados |
| Setup | 🟡 medio | 🟢 fácil |
| Licencia | MIT | MIT |
| Instalación | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |

## Regla práctica

- Elige **llama.cpp** si Tu objetivo encaja con estos ejemplos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo.
- Elige **Ollama** si Tu objetivo encaja con estos ejemplos: Probar un LLM local; Conectar un modelo local a Codex CLI.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
