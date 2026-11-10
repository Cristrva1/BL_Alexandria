[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 Tesseract

> Motor de OCR open source clásico, con más de 100 idiomas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 77.4k | Apache-2.0 | C++ | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Base de muchas herramientas de OCR, ligero y sin GPU.

## Por qué destaca

Estable, gratuito y disponible en todos los sistemas.

## Cómo funciona

Red LSTM que reconoce líneas de texto en imágenes preprocesadas.

## Instalación rápida

`brew install tesseract` o `apt install tesseract-ocr`.

## Casos de uso

- OCR de imágenes simples
- Base para OCRmyPDF
- Digitalizar documentos sin GPU

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres OCR clásico sin GPU | tus documentos tienen layouts complejos; mira `paddleocr` |

## Stack y modelos

- **Stack:** C++
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `ocr` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OCRmyPDF](ocrmypdf.md) | 35.3k | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PaddleOCR](paddleocr.md) | 92.5k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |

## Enlaces

- 🐙 GitHub: [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- 🌐 Web: <https://tesseract-ocr.github.io/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
