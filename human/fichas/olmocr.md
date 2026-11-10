[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 olmOCR

> Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 19.8k | Apache-2.0 | Python | 2026-03-25 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

## Qué es

Pensado para crear datasets de entrenamiento a partir de millones de PDFs, con orden de lectura correcto.

## Por qué destaca

Calidad alta y coste por página muy bajo en lotes grandes.

## Cómo funciona

Un VLM afinado lee cada página como imagen y produce texto lineal; se sirve con vLLM.

## Instalación rápida

`pip install olmocr` (requiere GPU NVIDIA).

## Casos de uso

- Convertir archivos de PDFs masivos
- Crear datasets de texto
- OCR de alta calidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| procesas grandes volúmenes de PDFs con GPU | no tienes GPU; mira `ocrmypdf` o `tesseract` |

**Limitaciones:** Requiere GPU con bastante memoria.

## Stack y modelos

- **Stack:** Python, vLLM
- **Modelos / API:** Modelo propio olmOCR.
- **Etiquetas:** `ocr` `pdf` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [vLLM](vllm.md) | 96.7k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PaddleOCR](paddleocr.md) | 92.5k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |
| [Docling](docling.md) | 70.4k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |
| [Unlimited-OCR](unlimited-ocr.md) | 31.1k | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. |

## Enlaces

- 🐙 GitHub: [allenai/olmocr](https://github.com/allenai/olmocr)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
