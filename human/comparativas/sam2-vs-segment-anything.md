[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# SAM 2 vs Segment Anything (SAM)

| | [SAM 2](../fichas/sam2.md) | [Segment Anything (SAM)](../fichas/segment-anything.md) |
|---|---|---|
| Qué hace | Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. | Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja. |
| ⭐ Estrellas | 20.1k | 55.1k |
| Elígelo si… | necesitas segmentar objetos en video | necesitas segmentar objetos en imágenes |
| Evítalo si… | solo trabajas con imágenes sueltas; `segment-anything` basta | trabajas con video; mira `sam2` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🟡 medio | 🟡 medio |
| Licencia | Apache-2.0 | Apache-2.0 |
| Instalación | `pip install -e .` | `pip install git+https://github.com/facebookresearch/segment-anything.git` |

## Regla práctica

- Elige **SAM 2** si necesitas segmentar objetos en video.
- Elige **Segment Anything (SAM)** si necesitas segmentar objetos en imágenes.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
