[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# HunyuanVideo vs Wan2.2

| | [HunyuanVideo](../fichas/hunyuanvideo.md) | [Wan2.2](../fichas/wan2-2.md) |
|---|---|---|
| Qué hace | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. |
| ⭐ Estrellas | 12.8k | 18.5k |
| Elígelo si… | tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más |
| Evítalo si… | trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente | tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🔴 pesado | 🔴 pesado |
| Licencia | Otra (ver repo) | Apache-2.0 |
| Instalación | `git clone https://github.com/Tencent-Hunyuan/HunyuanVideo` | `git clone https://github.com/Wan-Video/Wan2.2.git && cd Wan2.2 && pip install -r requirements.txt` |

## Regla práctica

- Elige **HunyuanVideo** si tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad.
- Elige **Wan2.2** si quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
