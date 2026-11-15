[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# LibreChat vs Open WebUI

| | [LibreChat](../fichas/librechat.md) | [Open WebUI](../fichas/open-webui.md) |
|---|---|---|
| Qué hace | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| ⭐ Estrellas | 46.9k | 158k |
| Elígelo si… | quieres todos los proveedores en un chat con SSO | necesitas un ChatGPT privado para tu equipo |
| Evítalo si… | usas sobre todo modelos locales; mira `open-webui` | solo quieres una app de escritorio individual; mira `jan` |
| Ejecución | 🔀 híbrido | 🏠 local |
| Setup | 🟡 medio | 🟢 fácil |
| Licencia | MIT | Otra (ver repo) |
| Instalación | `git clone https://github.com/danny-avila/LibreChat && cd LibreChat && docker compose up -d` | `docker run -d -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main` |

## Regla práctica

- Elige **LibreChat** si quieres todos los proveedores en un chat con SSO.
- Elige **Open WebUI** si necesitas un ChatGPT privado para tu equipo.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
