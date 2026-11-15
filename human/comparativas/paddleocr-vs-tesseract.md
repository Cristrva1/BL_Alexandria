[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# PaddleOCR vs Tesseract

| | [PaddleOCR](../fichas/paddleocr.md) | [Tesseract](../fichas/tesseract.md) |
|---|---|---|
| Qué hace | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. | Motor de OCR open source clásico, con más de 100 idiomas. |
| ⭐ Estrellas | 92.5k | 77.4k |
| Elígelo si… | necesitas OCR preciso y multilingüe | quieres OCR clásico sin GPU |
| Evítalo si… | solo quieres hacer buscables PDFs escaneados; mira `ocrmypdf` | tus documentos tienen layouts complejos; mira `paddleocr` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🟡 medio | 🟢 fácil |
| Licencia | Apache-2.0 | Apache-2.0 |
| Instalación | `pip install paddleocr` | `brew install tesseract` |

## Regla práctica

- Elige **PaddleOCR** si necesitas OCR preciso y multilingüe.
- Elige **Tesseract** si quieres OCR clásico sin GPU.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
