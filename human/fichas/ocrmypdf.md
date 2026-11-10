[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 OCRmyPDF

> Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 35.3k | MPL-2.0 | Python | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Convierte escaneos en PDF/A buscables manteniendo la imagen original.

## Por qué destaca

Simple, fiable y muy usado en archivos y despachos.

## Cómo funciona

Usa Tesseract para reconocer texto y lo coloca como capa invisible sobre cada página.

## Instalación rápida

`brew install ocrmypdf` o `apt install ocrmypdf`; luego `ocrmypdf entrada.pdf salida.pdf`.

## Casos de uso

- Hacer buscables documentos escaneados
- Archivo digital en PDF/A
- Preparar escaneos para RAG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tienes PDFs escaneados que quieres buscar | necesitas extraer estructura; mira `docling` |

## Stack y modelos

- **Stack:** Python, Tesseract
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `ocr` `pdf` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Tesseract](tesseract.md) | 77.4k | Motor de OCR open source clásico, con más de 100 idiomas. |
| [Docling](docling.md) | 70.4k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Enlaces

- 🐙 GitHub: [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)
- 🌐 Web: <http://ocrmypdf.readthedocs.io/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
