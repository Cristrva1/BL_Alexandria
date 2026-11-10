[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# AnythingLLM vs Open WebUI

| | [AnythingLLM](../fichas/anything-llm.md) | [Open WebUI](../fichas/open-webui.md) |
|---|---|---|
| Qué hace | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| ⭐ Estrellas | 68.1k | 158k |
| Elígelo si… | quieres RAG privado sin programar | necesitas un ChatGPT privado para tu equipo |
| Evítalo si… | necesitas un pipeline de RAG a medida; mira `llama-index` | solo quieres una app de escritorio individual; mira `jan` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🟢 fácil | 🟢 fácil |
| Licencia | MIT | Otra (ver repo) |
| Instalación | `docker pull mintplexlabs/anythingllm` | `docker run -d -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main` |

## Regla práctica

- Elige **AnythingLLM** si quieres RAG privado sin programar.
- Elige **Open WebUI** si necesitas un ChatGPT privado para tu equipo.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
