[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 12. Audio, Voz & Video](12-audio-voz-video.md)

# 📄 13. Documentos & Presentaciones

> Convertir documentos a Markdown/JSON para IA, OCR, herramientas PDF, presentaciones y diagramas.

**23 repos** · 5 subcategorías · ⭐ 1.2M estrellas en total · 🆕 15 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [Docling](../fichas/docling.md) | 70.4k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. | `pip install docling` |
| [PaddleOCR](../fichas/paddleocr.md) | 92.5k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. | `pip install paddleocr` |
| [OCRmyPDF](../fichas/ocrmypdf.md) | 35.3k | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | `brew install ocrmypdf` |
| [Stirling-PDF](../fichas/stirling-pdf.md) | 96.2k | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. | `docker run -d -p 8080:8080 stirlingtools/stirling-pdf` |
| [Slidev](../fichas/slidev.md) | 49.4k | Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. | `npm init slidev@latest` |
| [Mermaid](../fichas/mermaid.md) | 91.1k | Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown. | `npm i mermaid` |

## 🧭 Subcategorías

- [Conversión de documentos para IA](#conversión-de-documentos-para-ia) — 8 repos
- [OCR](#ocr) — 5 repos
- [Herramientas PDF](#herramientas-pdf) — 4 repos
- [Presentaciones](#presentaciones) — 5 repos
- [Diagramas y documentación](#diagramas-y-documentación) — 1 repos

## Conversión de documentos para IA

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Docling](../fichas/docling.md) 🆕 | 70.4k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. | quieres convertir documentos a Markdown con buena estructura | 🟢 |
| [markitdown](../fichas/markitdown.md) | 195k | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. | alimentas LLMs con documentos de formatos variados | 🟢 |
| [MinerU](../fichas/mineru.md) 🆕 | 83.4k | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. | procesas documentos científicos o técnicos complejos | 🟡 |
| [Pandoc](../fichas/pandoc.md) 🆕 | 46.9k | Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos. | necesitas convertir entre formatos de texto | 🟢 |
| [Marker](../fichas/marker.md) 🆕 | 40.8k | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. | conviertes PDFs largos con fórmulas | 🟢 |
| [PDF Inspector](../fichas/pdf-inspector.md) | 20k | Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas. | procesas muchos PDFs y quieres ahorrar OCR | 🟢 |
| [Unstructured](../fichas/unstructured.md) 🆕 | 15.7k | ETL open source que transforma documentos complejos en datos estructurados para LLM. | tienes muchos formatos de documentos distintos | 🟡 |
| [Youtube2Webpage](../fichas/youtube2webpage.md) | 1.5k | Script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado. | quieres video → artículo con transcripción y capturas | 🟢 |

## OCR

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [PaddleOCR](../fichas/paddleocr.md) 🆕 | 92.5k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. | necesitas OCR preciso y multilingüe | 🟡 |
| ⭐ [OCRmyPDF](../fichas/ocrmypdf.md) 🆕 | 35.3k | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | tienes PDFs escaneados que quieres buscar | 🟢 |
| [Tesseract](../fichas/tesseract.md) 🆕 | 77.4k | Motor de OCR open source clásico, con más de 100 idiomas. | quieres OCR clásico sin GPU | 🟢 |
| [Unlimited-OCR](../fichas/unlimited-ocr.md) | 31.1k | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. | procesas documentos muy largos con GPU | 🔴 |
| [olmOCR](../fichas/olmocr.md) 🆕 | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. | procesas grandes volúmenes de PDFs con GPU | 🔴 |

## Herramientas PDF

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Stirling-PDF](../fichas/stirling-pdf.md) 🆕 | 96.2k | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. | quieres un iLovePDF privado | 🟢 |
| [PDFMathTranslate](../fichas/pdfmathtranslate.md) 🆕 | 38.3k | Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe. | traduces PDFs técnicos y quieres conservar el formato | 🟢 |
| [pdfcraft](../fichas/pdfcraft.md) | 9.8k | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. | manipulas PDFs con privacidad y sin instalar nada | 🟢 |
| [PdfDing](../fichas/pdfding.md) | 1.8k | Gestor y visor de PDFs auto-hospedado, ligero, con etiquetas y progreso de lectura. | quieres organizar y leer PDFs en tu servidor | 🟢 |

## Presentaciones

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Slidev](../fichas/slidev.md) 🆕 | 49.4k | Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. | haces presentaciones técnicas y quieres control como código | 🟢 |
| [ppt-master](../fichas/ppt-master.md) | 75.5k | Generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas para abrir y ajustar en Office. | quieres PPTX editable de Office rápido | 🟢 |
| [reveal.js](../fichas/reveal-js.md) | 72.6k | Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. | quieres slides web por código, versionables | 🟢 |
| [Marp](../fichas/marp.md) 🆕 | 12.7k | Ecosistema para crear presentaciones con Markdown simple y exportarlas a PDF, PPTX o HTML. | quieres slides simples en Markdown | 🟢 |
| [Presenton](../fichas/presenton.md) 🆕 | 11.8k | Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. | quieres generar presentaciones de negocio con IA | 🟢 |

## Diagramas y documentación

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Mermaid](../fichas/mermaid.md) 🆕 | 91.1k | Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown. | quieres diagramas como texto | 🟢 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### PaddleOCR, Docling, MinerU, Tesseract, Marker, Unlimited-OCR, olmOCR

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [PaddleOCR](../fichas/paddleocr.md) | 92.5k | necesitas OCR preciso y multilingüe | solo quieres hacer buscables PDFs escaneados; mira `ocrmypdf` |
| [Docling](../fichas/docling.md) | 70.4k | quieres convertir documentos a Markdown con buena estructura | solo tienes PDFs de texto simples; mira `markitdown` |
| [MinerU](../fichas/mineru.md) | 83.4k | procesas documentos científicos o técnicos complejos | quieres algo ligero; mira `markitdown` |
| [Tesseract](../fichas/tesseract.md) | 77.4k | quieres OCR clásico sin GPU | tus documentos tienen layouts complejos; mira `paddleocr` |
| [Marker](../fichas/marker.md) | 40.8k | conviertes PDFs largos con fórmulas | necesitas uso comercial sin licencia; revisa su licencia |
| [Unlimited-OCR](../fichas/unlimited-ocr.md) | 31.1k | procesas documentos muy largos con GPU | necesitas algo probado y ligero; mira `docling` |
| [olmOCR](../fichas/olmocr.md) | 19.8k | procesas grandes volúmenes de PDFs con GPU | no tienes GPU; mira `ocrmypdf` o `tesseract` |

### Stirling-PDF, pdfcraft

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Stirling-PDF](../fichas/stirling-pdf.md) | 96.2k | quieres un iLovePDF privado | solo necesitas OCR; mira `ocrmypdf` |
| [pdfcraft](../fichas/pdfcraft.md) | 9.8k | manipulas PDFs con privacidad y sin instalar nada | necesitas conversión a Markdown para IA (markitdown) o edición de contenido (no solo manipulación de páginas) |

### Slidev, reveal.js, Marp

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Slidev](../fichas/slidev.md) | 49.4k | haces presentaciones técnicas y quieres control como código | necesitas slides para negocio generadas con IA; mira `presenton` |
| [reveal.js](../fichas/reveal-js.md) | 72.6k | quieres slides web por código, versionables | necesitas PPTX editable en Office (ppt-master) o un editor visual de slides |
| [Marp](../fichas/marp.md) | 12.7k | quieres slides simples en Markdown | necesitas interactividad y componentes; mira `slidev` |

### ppt-master, Presenton

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [ppt-master](../fichas/ppt-master.md) | 75.5k | quieres PPTX editable de Office rápido | prefieres slides web por código (reveal.js) o control de diseño pixel-perfect |
| [Presenton](../fichas/presenton.md) | 11.8k | quieres generar presentaciones de negocio con IA | prefieres control total como código; mira `slidev` |

## 🧪 Recetas que usan esta categoría

- [🔎 Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [📊 Documentos → presentaciones](../playbooks/documentos-presentaciones.md) — Pasar informes, PDFs o notas a presentaciones editables o slides web.
- [📎 RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
