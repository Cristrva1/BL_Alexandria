[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# SGLang vs vLLM

| | [SGLang](../fichas/sglang.md) | [vLLM](../fichas/vllm.md) |
|---|---|---|
| Qué hace | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. |
| ⭐ Estrellas | 38.7k | 96.7k |
| Elígelo si… | buscas el máximo rendimiento en servicio de LLM | necesitas servir LLM abiertos a muchos usuarios en GPU |
| Evítalo si… | quieres la opción más documentada; mira `vllm` | solo los usas tú en un portátil; mira `ollama` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🔴 pesado | 🔴 pesado |
| Licencia | Apache-2.0 | Apache-2.0 |
| Instalación | `pip install "sglang[all]"` | `pip install vllm` |

## Regla práctica

- Elige **SGLang** si buscas el máximo rendimiento en servicio de LLM.
- Elige **vLLM** si necesitas servir LLM abiertos a muchos usuarios en GPU.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
