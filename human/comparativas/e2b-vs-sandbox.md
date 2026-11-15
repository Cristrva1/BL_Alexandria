[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# E2B vs sandbox

| | [E2B](../fichas/e2b.md) | [sandbox](../fichas/sandbox.md) |
|---|---|---|
| Qué hace | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |
| ⭐ Estrellas | 14.8k | 6.3k |
| Elígelo si… | tu agente ejecuta código y necesitas aislarlo | quieres aislar la ejecución de agentes y reproducibilidad |
| Evítalo si… | solo necesitas ejecutar código localmente de confianza | te basta correr local sin sandbox o no puedes asumir el overhead de Docker |
| Ejecución | ☁️ cloud/API | 🔀 híbrido |
| Setup | 🟢 fácil | 🟡 medio |
| Licencia | Apache-2.0 | Apache-2.0 |
| Instalación | `pip install e2b-code-interpreter` | `docker run` |

## Regla práctica

- Elige **E2B** si tu agente ejecuta código y necesitas aislarlo.
- Elige **sandbox** si quieres aislar la ejecución de agentes y reproducibilidad.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
