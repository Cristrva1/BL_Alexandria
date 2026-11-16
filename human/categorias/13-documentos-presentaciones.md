[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# PDF, OCR y procesamiento de documentos

Extracción de texto, OCR, conversión y gestión de PDF. Empieza por el formato de entrada y comprueba con una muestra si conserva el contenido que necesitas.

22 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Docling](../fichas/docling.md) | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. | API de IA opcional |
| [PaddleOCR](../fichas/paddleocr.md) | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. | Sin clave propia de API de IA en la ruta básica |
| [OCRmyPDF](../fichas/ocrmypdf.md) | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | Sin clave propia de API de IA en la ruta básica |
| [Stirling-PDF](../fichas/stirling-pdf.md) | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Conversión de documentos para IA](#conversión-de-documentos-para-ia) — 9 repos
- [OCR](#ocr) — 7 repos
- [Herramientas PDF](#herramientas-pdf) — 5 repos
- [Gestión y archivo de documentos](#gestión-y-archivo-de-documentos) — 1 repos

## Conversión de documentos para IA

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Docling](../fichas/docling.md) | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. | Tu objetivo encaja con estos ejemplos: Preparar documentos para RAG; Extraer tablas antes de un análisis | API de IA opcional |
| [markitdown](../fichas/markitdown.md) | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. | Tu objetivo encaja con estos ejemplos: Preparar documentos Office para consulta; Crear una copia textual de un informe | API de IA opcional |
| [MinerU](../fichas/mineru.md) | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. | Tu objetivo encaja con estos ejemplos: Preparar PDFs complejos para un índice; Extraer tablas y fórmulas de un documento propio | API de IA opcional |
| [Pandoc](../fichas/pandoc.md) | Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos. | Tu objetivo encaja con estos ejemplos: Generar documentos desde Markdown; Convertir un libro propio a EPUB | Sin clave propia de API de IA en la ruta básica |
| [Marker](../fichas/marker.md) | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. | Tu objetivo encaja con estos ejemplos: Extraer contenido de informes; Preparar documentos escaneados para búsqueda | API de IA opcional |
| [PDF Inspector](../fichas/pdf-inspector.md) | Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas. | Tu objetivo encaja con estos ejemplos: Decidir cuándo hace falta OCR; Extraer texto con posiciones de un PDF | Sin clave propia de API de IA en la ruta básica |
| [Unstructured](../fichas/unstructured.md) | ETL open source que transforma documentos complejos en datos estructurados para LLM. | Tu objetivo encaja con estos ejemplos: Preparar documentos para una base de conocimiento; Crear un pipeline ETL de archivos | API de IA opcional |
| [Xberg (antes Kreuzberg)](../fichas/xberg.md) | Motor de extracción de documentos en Rust: texto, tablas y metadatos de más de 100 formatos, con OCR, transcripción, embeddings y MCP. | Tu objetivo encaja con estos ejemplos: preparar documentos variados (PDF, Office, correos, archivos comprimidos) para un sistema RAG; extraer texto y tablas de escaneos con OCR en lote sin GPU | API de IA opcional |
| [Apache Tika](../fichas/tika.md) | Kit de Apache que detecta y extrae texto y metadatos de más de mil tipos de archivo; desde 4.0 emite Markdown pensado para LLM y RAG. | Tu objetivo encaja con estos ejemplos: extraer texto y metadatos de archivos heterogéneos en un pipeline de indexación; alimentar un sistema RAG con Markdown generado desde documentos Office y PDF | API de IA opcional |

## OCR

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [PaddleOCR](../fichas/paddleocr.md) | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. | Tu objetivo encaja con estos ejemplos: Digitalizar un formulario propio; Extraer texto y estructura de una página escaneada | Sin clave propia de API de IA en la ruta básica |
| [OCRmyPDF](../fichas/ocrmypdf.md) | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | Tu objetivo encaja con estos ejemplos: Hacer buscables documentos escaneados; Preparar un archivo histórico propio para indexación | Sin clave propia de API de IA en la ruta básica |
| [Tesseract](../fichas/tesseract.md) | Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma. | Tu objetivo encaja con estos ejemplos: Digitalizar texto de una fotografía propia; Incorporar OCR local a un script | Sin clave propia de API de IA en la ruta básica |
| [Unlimited-OCR](../fichas/unlimited-ocr.md) | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. | Tu objetivo encaja con estos ejemplos: Estudiar parsing de documentos largos; Comparar un VLM OCR con otro motor | Sin clave propia de API de IA en la ruta básica |
| [Surya](../fichas/surya.md) | OCR multilingüe y análisis de layout con un VLM de 689M parámetros: orden de lectura, tablas en HTML y más de 90 idiomas. | Tu objetivo encaja con estos ejemplos: digitalizar documentos escaneados en varios idiomas conservando el orden de lectura; extraer tablas de PDF como HTML con celdas combinadas | Sin clave propia de API de IA en la ruta básica |
| [olmOCR](../fichas/olmocr.md) | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. | Tu objetivo encaja con estos ejemplos: Preparar PDFs para entrenamiento documental; Procesar escaneos con un VLM | API de IA opcional |
| [pdf-craft](../fichas/pdf-craft.md) | Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento. | Tu objetivo encaja con estos ejemplos: Crear una versión editable de un escaneo propio; Preparar un EPUB desde material autorizado | Depende de la ruta elegida |

## Herramientas PDF

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Stirling-PDF](../fichas/stirling-pdf.md) | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. | Tu objetivo encaja con estos ejemplos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz | Sin clave propia de API de IA en la ruta básica |
| [PDFMathTranslate](../fichas/pdfmathtranslate.md) | Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe. | Tu objetivo encaja con estos ejemplos: Leer un artículo en otro idioma; Crear una versión bilingüe de documentación propia | Depende de la ruta elegida |
| [docuseal](../fichas/docuseal.md) | Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio. | Tu objetivo encaja con estos ejemplos: Preparar formularios internos de prueba; Evaluar un flujo de firma documental | Sin clave propia de API de IA en la ruta básica |
| [pdfcraft](../fichas/pdfcraft.md) | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. | Tu objetivo encaja con estos ejemplos: Editar PDFs desde un navegador; Convertir o dividir un documento de prueba | Sin clave propia de API de IA en la ruta básica |
| [PdfDing](../fichas/pdfding.md) | Gestor, visor y editor de PDF autoalojado (AGPL-3.0) con colecciones, etiquetas, anotaciones y progreso de lectura; se desarrolla en Codeberg. | Tu objetivo encaja con estos ejemplos: Organizar una colección de PDFs; Consultar documentos desde varios dispositivos | Sin clave propia de API de IA en la ruta básica |

## Gestión y archivo de documentos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [paperless-ngx](../fichas/paperless-ngx.md) | Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados. | Tu objetivo encaja con estos ejemplos: Organizar recibos de prueba; Construir un archivo documental buscable | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [Documentos → presentaciones](../playbooks/documentos-presentaciones.md) — Pasar informes, PDFs o notas a presentaciones editables o slides web.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
