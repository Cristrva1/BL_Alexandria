[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# headroom vs rtk

| | [headroom](../fichas/headroom.md) | [rtk](../fichas/rtk.md) |
|---|---|---|
| Qué hace | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. |
| ⭐ Estrellas | 79.7k | 86.6k |
| Elígelo si… | te quedas sin contexto en sesiones largas | tu agente consume demasiado contexto leyendo salidas extensas de terminal |
| Evítalo si… | tus prompts ya caben holgados o la pérdida de detalle por resumen es inaceptable | el coste operativo supera el volumen de uso del proyecto |
| Ejecución | 🔀 híbrido | 🏠 local |
| API de IA | API de IA opcional | API de IA opcional |
| Coste | El coste depende del proveedor o la ruta | El coste depende del proveedor o la ruta |
| Modelos locales | La función básica no necesita un modelo | La función básica no necesita un modelo |
| Setup | 🟢 fácil | 🟢 fácil |
| Licencia | Apache-2.0 | Apache-2.0 |
| Instalación | Instalación según el repo (`pip`/`npm`); requiere un LLM para la condensación (o modo l… | `git clone https://github.com/rtk-ai/rtk.git` |

## Regla práctica

- Elige **headroom** si te quedas sin contexto en sesiones largas.
- Elige **rtk** si tu agente consume demasiado contexto leyendo salidas extensas de terminal.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
