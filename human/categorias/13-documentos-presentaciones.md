[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# PDF, OCR y procesamiento de documentos

Extracción de texto, OCR, conversión y gestión de PDF. Empieza por el formato de entrada y comprueba con una muestra si conserva el contenido que necesitas.

20 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Docling](../fichas/docling.md) | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. | API de IA opcional |
| [PaddleOCR](../fichas/paddleocr.md) | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. | Sin API de IA en la ruta básica |
| [OCRmyPDF](../fichas/ocrmypdf.md) | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | Sin API de IA en la ruta básica |
| [Stirling-PDF](../fichas/stirling-pdf.md) | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. | Sin API de IA en la ruta básica |

## Secciones

- [Conversión de documentos para IA](#conversión-de-documentos-para-ia) — 8 repos
- [OCR](#ocr) — 6 repos
- [Herramientas PDF](#herramientas-pdf) — 5 repos
- [Gestión y archivo de documentos](#gestión-y-archivo-de-documentos) — 1 repos

## Conversión de documentos para IA

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Docling](../fichas/docling.md) | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. | quieres convertir documentos a Markdown con buena estructura | API de IA opcional |
| [markitdown](../fichas/markitdown.md) | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. | alimentas LLMs con documentos de formatos variados | API de IA opcional |
| [MinerU](../fichas/mineru.md) | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. | procesas documentos científicos o técnicos complejos | Sin API de IA en la ruta básica |
| [Pandoc](../fichas/pandoc.md) | Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos. | necesitas convertir entre formatos de texto | Sin API de IA en la ruta básica |
| [Marker](../fichas/marker.md) | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. | conviertes PDFs largos con fórmulas | API de IA opcional |
| [PDF Inspector](../fichas/pdf-inspector.md) | Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas. | procesas muchos PDFs y quieres ahorrar OCR | Sin API de IA en la ruta básica |
| [Unstructured](../fichas/unstructured.md) | ETL open source que transforma documentos complejos en datos estructurados para LLM. | tienes muchos formatos de documentos distintos | Depende de la ruta elegida |
| [Youtube2Webpage](../fichas/youtube2webpage.md) | Script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado. | quieres video → artículo con transcripción y capturas | Sin API de IA en la ruta básica |

## OCR

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [PaddleOCR](../fichas/paddleocr.md) | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. | necesitas OCR preciso y multilingüe | Sin API de IA en la ruta básica |
| [OCRmyPDF](../fichas/ocrmypdf.md) | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | tienes PDFs escaneados que quieres buscar | Sin API de IA en la ruta básica |
| [Tesseract](../fichas/tesseract.md) | Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma. | quieres OCR clásico sin GPU | Sin API de IA en la ruta básica |
| [Unlimited-OCR](../fichas/unlimited-ocr.md) | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. | procesas documentos muy largos con GPU | Sin API de IA en la ruta básica |
| [olmOCR](../fichas/olmocr.md) | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. | procesas grandes volúmenes de PDFs con GPU | Sin API de IA en la ruta básica |
| [pdf-craft](../fichas/pdf-craft.md) | Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento. | buscas esta función: Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento. | API de IA opcional |

## Herramientas PDF

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Stirling-PDF](../fichas/stirling-pdf.md) | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. | quieres un iLovePDF privado | Sin API de IA en la ruta básica |
| [PDFMathTranslate](../fichas/pdfmathtranslate.md) | Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe. | traduces PDFs técnicos y quieres conservar el formato | Depende de la ruta elegida |
| [docuseal](../fichas/docuseal.md) | Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio. | buscas esta función: Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio. | Sin API de IA en la ruta básica |
| [pdfcraft](../fichas/pdfcraft.md) | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. | manipulas PDFs con privacidad y sin instalar nada | Sin API de IA en la ruta básica |
| [PdfDing](../fichas/pdfding.md) | Gestor y visor de PDFs auto-hospedado, ligero, con etiquetas y progreso de lectura. | quieres organizar y leer PDFs en tu servidor | Sin API de IA en la ruta básica |

## Gestión y archivo de documentos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [paperless-ngx](../fichas/paperless-ngx.md) | Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados. | buscas esta función: Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados. | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [Documentos → presentaciones](../playbooks/documentos-presentaciones.md) — Pasar informes, PDFs o notas a presentaciones editables o slides web.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
