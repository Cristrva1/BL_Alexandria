# Alexandría para agentes · PDF, OCR y procesamiento de documentos

Categoría 13 completa (23 repos, 4 subcategorías). Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=13 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `docling` | conversion | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON… | 2 Intermedio | 78 | MIT (OSI permisiva) | recomendado |
| `mineru` | conversion | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos… | 2 Intermedio | 68 | Apache-2.0 con condiciones adicionales (source-available) | alternativa |
| `markitdown` | conversion | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word… | 2 Intermedio | 67 | MIT (OSI permisiva) | sin grupo |
| `xberg` | conversion | Motor de extracción de documentos en Rust: texto, tablas y metadatos de más de… | 2 Intermedio | 63 | MIT (OSI permisiva) | alternativa |
| `marker` | conversion | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `tika` | conversion | Kit de Apache que detecta y extrae texto y metadatos de más de mil tipos de… | 2 Intermedio | 59 | Apache-2.0 (OSI permisiva) | alternativa |
| `unstructured` | conversion | ETL open source que transforma documentos complejos en datos estructurados para… | 2 Intermedio | 58 | Apache-2.0 (OSI permisiva) | alternativa |
| `pandoc` | conversion | Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y… | 1 Básico | 56 | GPL-2.0 (OSI copyleft) | sin grupo |
| `pdf-inspector` | conversion | Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con… | 2 Intermedio | 56 | MIT (OSI permisiva) | sin grupo |
| `paddleocr` | ocr | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos… | 2 Intermedio | 73 | Apache-2.0 (OSI permisiva) | recomendado |
| `ocrmypdf` | ocr | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | 1 Básico | 65 | MPL-2.0 (OSI copyleft) | sin grupo |
| `tesseract` | ocr | Motor de OCR de código abierto que reconoce texto en imágenes y documentos… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | alternativa |
| `surya` | ocr | OCR multilingüe y análisis de layout con un VLM de 689M parámetros: orden de… | 3 Avanzado | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `unlimited-ocr` | ocr | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. | 3 Avanzado | 62 | MIT (OSI permisiva) | alternativa |
| `pdf-craft` | ocr | Herramienta para convertir libros escaneados en PDF a documentos editables… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `olmocr` | ocr | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión… | 3 Avanzado | 51 | Apache-2.0 (OSI permisiva) | alternativa |
| `stirling-pdf` | pdf | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar… | 1 Básico | 76 | MIT + licencia propietaria (app/proprietary/, app/saas/) (open-core) | recomendado |
| `pdfmathtranslate` | pdf | Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión… | 1 Básico | 68 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `docuseal` | pdf | Aplicación para preparar formularios y gestionar la firma electrónica de… | 3 Avanzado | 62 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `pdfcraft` | pdf | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para… | 1 Básico | 55 | AGPL-3.0 (OSI copyleft) | alternativa |
| `documenso` | pdf | Plataforma abierta de firma electrónica para enviar un PDF a firmantes por… | 3 Avanzado | 53 | AGPL-3.0 (open-core) | sin grupo |
| `paperless-ngx` | gestion | Gestor documental autoalojado para importar, reconocer texto, buscar y archivar… | 2 Intermedio | 79 | GPL-3.0 (OSI copyleft) | sin grupo |
| `pdfding` | gestion | Gestor, visor y editor de PDF autoalojado (AGPL-3.0) con colecciones… | 1 Básico | 45 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Docling (`docling`)

- **Repo:** https://github.com/docling-project/docling · MIT · nivel 2 · 78/100 · recomendado en «Conversión de documentos a Markdown/JSON para IA»
- **Qué es:** Docling, librería y CLI de Python que convierte documentos a formatos listos para IA generativa. Nació en IBM Research y hoy está alojada en LF AI & Data (Linux Foundation). Licencia MIT. Es muy activa (~71k estrellas, v2.150.x).
- **Cuándo elegirlo:** Casos: Preparar documentos para RAG; Extraer tablas antes de un análisis.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python >=3.10; modelos y dependencias del formato; documento de prueba; hardware prerequisites; API de IA: opcional; Python >=3.10; modelos y dependencias del formato; documento de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install docling` — fuente: https://github.com/docling-project/docling/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte un PDF breve con tabla y compara el Markdown y JSON con el original Éxito: Puedes identificar texto, estructura y campos que necesitan corrección
- **Combina con:** `llama-index` [3/py], `haystack` [3/py], `qdrant` [6/vectores], `langchain` [3/py]
- **Alternativas:** `mineru`, `xberg`, `marker`, `tika`, `unstructured`, `olmocr`
- **Riesgos y avisos:** Alternativas (elige una): marker, mineru, unstructured, olmocr. ragflow trae su propio analizador de documentos, por eso se retiró de las combinaciones. MCP es un paquete complementario y convierte localmente por defecto; configura explícitamente cualquier delegación a un servicio remoto.

### MinerU (`mineru`)

- **Repo:** https://github.com/opendatalab/MinerU · Apache-2.0 con condiciones adicionales · nivel 2 · 68/100 · alternativa en «Conversión de documentos a Markdown/JSON para IA»
- **Qué es:** Herramienta de análisis de documentos de OpenDataLab (Shanghai AI Laboratory) que convierte PDF y otros formatos en datos estructurados. Usa la «MinerU Open Source License», basada en Apache 2.0 con condiciones adicionales; muy activa…
- **Cuándo elegirlo:** Casos: Preparar PDFs complejos para un índice; Extraer tablas y fórmulas de un documento propio.
- **Requisitos:** nivel 2: preparación media; Python 3.11–3.14; entorno virtual; modelos y backend del nivel elegido; hardware prerequisites; API de IA: opcional; Python 3.11–3.14; entorno virtual; modelos y backend del nivel elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `uv pip install -U "mineru>=4.0,<5"` — fuente: https://github.com/opendatalab/MinerU/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Procesa un PDF corto con Flash o Basic y compara estructura y tablas antes de usar niveles superiores Éxito: Puedes identificar nivel, backend y origen de la conversión
- **Combina con:** `lightrag` [6/rag], `vllm` [23/serving], `claude-code` [20/terminal]
- **Alternativas:** `docling`, `xberg`, `marker`, `tika`, `unstructured`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): docling, marker. Revisa las condiciones adicionales de su licencia antes de uso comercial. Se retiró ragflow por no estar documentado. La skill ayuda al agente a operar la herramienta; no es un modelo incluido en la suscripción del cliente; la telemetría tiene configuración propia.

### markitdown (`markitdown`)

- **Repo:** https://github.com/microsoft/markitdown · MIT · nivel 2 · 67/100
- **Qué es:** Utilidad Python ligera de Microsoft (MIT) para convertir archivos a Markdown destinado a LLM y análisis de texto. Activa (v0.1.9); el repositorio incluye también un servidor MCP, un complemento de OCR y un complemento de ejemplo.
- **Cuándo elegirlo:** Casos: Preparar documentos Office para consulta; Crear una copia textual de un informe.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python 3.10–3.14; entorno virtual; extras del formato elegido; hardware prerequisites; API de IA: opcional; Python 3.10–3.14; entorno virtual; extras del formato elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install 'markitdown[all]'` — fuente: https://github.com/microsoft/markitdown/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte un DOCX ficticio a Markdown y revisa títulos, listas y tablas Éxito: El texto y el orden se pueden contrastar con el documento
- **Combina con:** `claude-code` [20/terminal], `khoj` [8/workspaces], `pandoc`
- **Riesgos y avisos:** Se retiraron las combinaciones antiguas con ppt-master y open-notebook por falta de relación documentada. Instala los extras necesarios; convertir a Markdown no conserva toda la maquetación del original.

### Xberg (antes Kreuzberg) (`xberg`)

- **Repo:** https://github.com/xberg-io/xberg · MIT · nivel 2 · 63/100 · alternativa en «Conversión de documentos a Markdown/JSON para IA»
- **Qué es:** Motor de inteligencia documental de código abierto (MIT) de xberg-io. Es la nueva iteración de Kreuzberg, reconstruida y renombrada en una línea v1; la API de GitHub redirige el repositorio original a este nombre. Muy activo.
- **Cuándo elegirlo:** Casos: preparar documentos variados (PDF, Office, correos, archivos comprimidos) para un sistema RAG; extraer texto y tablas de escaneos con OCR en lote sin GPU.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Rust, Cargo.toml, composer.json, package.json, pyproject.toml; API de IA: opcional; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install xberg` — fuente: https://github.com/xberg-io/xberg/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install xberg` y extrae el texto de un PDF y un DOCX de prueba. Éxito: Obtienes Markdown limpio con tablas y metadatos de ambos archivos.
- **Combina con:** `claude-code` [20/terminal], `tesseract` [13/ocr], `qdrant` [6/vectores]
- **Alternativas:** `docling`, `mineru`, `marker`, `tika`, `unstructured`
- **Riesgos y avisos:** Alternativas (elige una): tika, unstructured. Proyectos que usaban Kreuzberg deben revisar la migración a la línea v1 de Xberg; la rama Kreuzberg v4 LTS sigue….

### Marker (`marker`)

- **Repo:** https://github.com/datalab-to/marker · Apache-2.0 · nivel 2 · 60/100 · alternativa en «Conversión de documentos a Markdown/JSON para IA»
- **Qué es:** Conversor de documentos de Datalab que produce Markdown, JSON, fragmentos y HTML. El código es Apache 2.0, pero los pesos de los modelos usan una licencia OpenRAIL-M modificada (gratuita para investigación, uso personal y empresas…
- **Cuándo elegirlo:** Casos: Extraer contenido de informes; Preparar documentos escaneados para búsqueda.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; backend Surya con vLLM o llama.cpp según sistema; pesos; PDF de prueba; hardware prerequisites; API de IA: opcional; Python; backend Surya con vLLM o llama.cpp según sistema; pesos; PDF de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install marker-pdf` — fuente: https://github.com/datalab-to/marker/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte un PDF de dos páginas con una tabla y compara texto y columnas Éxito: Puedes localizar errores y decidir si activar la mejora LLM
- **Combina con:** `vllm` [23/serving], `llama-cpp` [8/motores], `pandoc`, `surya` [13/ocr]
- **Alternativas:** `docling`, `mineru`, `xberg`, `tika`, `unstructured`, `pdf-craft`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): docling, mineru, pdf-craft. Se retiró llama-index por no estar documentado en el README actual. Instalar marker-pdf no completa por sí solo el backend de inferencia; verifica requisitos del modelo y su licencia antes de ampliar volumen.

### Apache Tika (`tika`)

- **Repo:** https://github.com/apache/tika · Apache-2.0 · nivel 2 · 59/100 · alternativa en «Conversión de documentos a Markdown/JSON para IA»
- **Qué es:** Proyecto de la Apache Software Foundation (Apache-2.0), referencia histórica en extracción de contenido. Muy maduro; la serie 4.x se orienta a pipelines de agentes.
- **Cuándo elegirlo:** Casos: extraer texto y metadatos de archivos heterogéneos en un pipeline de indexación; alimentar un sistema RAG con Markdown generado desde documentos Office y PDF.
- **Requisitos:** nivel 2: preparación media; Java, pom.xml; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/apache/tika.git` — fuente: https://github.com/apache/tika/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca tika-server con su imagen Docker o JAR y envía un PDF de prueba al endpoint de extracción. Éxito: El servidor devuelve el texto en Markdown y los metadatos del documento.
- **Combina con:** `tesseract` [13/ocr], `paperless-ngx` [13/gestion], `claude-code` [20/terminal]
- **Alternativas:** `docling`, `mineru`, `xberg`, `marker`, `unstructured`
- **Riesgos y avisos:** Alternativas (elige una): xberg, unstructured. Tika incluye subcomponentes con licencias propias (ver LICENSE).

### Unstructured (`unstructured`)

- **Repo:** https://github.com/Unstructured-IO/unstructured · Apache-2.0 · nivel 2 · 58/100 · alternativa en «Conversión de documentos a Markdown/JSON para IA»
- **Qué es:** Biblioteca de código abierto (Apache 2.0) de Unstructured.io para ingerir y preprocesar documentos e imágenes. Muy activa (0.27.x); la empresa ofrece modelos de mayor calidad en su API de pago Transform v2, y según su propia tabla la…
- **Cuándo elegirlo:** Casos: Preparar documentos para una base de conocimiento; Crear un pipeline ETL de archivos.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; extras por formato; herramientas del sistema para PDF o imágenes; hardware prerequisites; API de IA: opcional; Python; extras por formato; herramientas del sistema para PDF o imágenes.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "unstructured[all-docs]"` — fuente: https://github.com/Unstructured-IO/unstructured/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Divide un documento ficticio en elementos y comprueba título, párrafos y tabla Éxito: Los elementos conservan el orden y tipos que necesitas
- **Combina con:** `tesseract` [13/ocr], `langchain` [3/py], `qdrant` [6/vectores]
- **Alternativas:** `docling`, `mineru`, `xberg`, `marker`, `tika`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativa (elige una): docling. Se retiró llama-index por no estar documentado en el README. Instala dependencias del formato; el contenedor y la biblioteca no garantizan por sí solos todas las funciones de la plataforma.

### Pandoc (`pandoc`)

- **Repo:** https://github.com/jgm/pandoc · GPL-2.0 · nivel 1 · 56/100
- **Qué es:** Conversor universal de formatos de marcado de John MacFarlane: una biblioteca Haskell y una herramienta de línea de comandos. GPL-2.0, muy madura y activa (versión 3.14).
- **Cuándo elegirlo:** Casos: Generar documentos desde Markdown; Convertir un libro propio a EPUB.
- **Requisitos:** nivel 1: preparación sencilla; Binario de tu sistema; motor PDF solo si generas PDF; archivo de prueba; hardware prerequisites; API de IA: no; Binario de tu sistema; motor PDF solo si generas PDF; archivo de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://pandoc.org/installing.html
- **Primera prueba propuesta (no ejecutada):** Convierte un Markdown con títulos y tabla a DOCX y revisa el resultado Éxito: Puedes abrir el documento y comprobar estructura y contenido
- **Combina con:** `reveal.js` [31/slides], `markitdown`, `marker`, `ppt-master` [31/slides], `marp` [31/slides], `pdf-craft` [13/ocr]
- **Riesgos y avisos:** Cambiar formato no garantiza conservar cada detalle de diseño; elige plantilla y motor según la salida.

### PDF Inspector (`pdf-inspector`)

- **Repo:** https://github.com/firecrawl/pdf-inspector · MIT · nivel 2 · 56/100
- **Qué es:** Biblioteca en Rust de Firecrawl (MIT) para clasificar PDF y extraer su texto. Muy activa (v1.26.0) y disponible para Rust, CLI, Python, Node y WebAssembly en navegador.
- **Cuándo elegirlo:** Casos: Decidir cuándo hace falta OCR; Extraer texto con posiciones de un PDF.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python para esta ruta; runtime OCR y pesos solo si activas OCR; PDFs de prueba; hardware prerequisites; API de IA: no; Python para esta ruta; runtime OCR y pesos solo si activas OCR; PDFs de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install pdf-inspector` — fuente: https://github.com/firecrawl/pdf-inspector/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clasifica un PDF con texto y otro escaneado y compara el resultado Éxito: Puedes enrutar el escaneado a OCR y extraer el otro sin ese procesamiento
- **Combina con:** `firecrawl` [4/crawlers], `pdfmathtranslate` [13/pdf], `paddleocr` [13/ocr], `ocrmypdf` [13/ocr]
- **Riesgos y avisos:** La instalación base y las funciones OCR no tienen los mismos recursos; la clasificación no verifica exactitud de todo el texto.

### PaddleOCR (`paddleocr`)

- **Repo:** https://github.com/PaddlePaddle/PaddleOCR · Apache-2.0 · nivel 2 · 73/100 · recomendado en «OCR de documentos»
- **Qué es:** Kit de OCR y motor de IA documental de Baidu sobre PaddlePaddle, Apache 2.0. Muy usado (más de 6.000 repositorios dependientes según su insignia) y activo (v3.7.0, último push en septiembre de 2026).
- **Cuándo elegirlo:** Casos: Digitalizar un formulario propio; Extraer texto y estructura de una página escaneada.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python y PaddlePaddle compatibles; modelo y paquete de idioma; imagen de prueba; hardware prerequisites; API de IA: no; Python y PaddlePaddle compatibles; modelo y paquete de idioma; imagen de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install paddleocr` — fuente: https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/installation.md
- **Primera prueba propuesta (no ejecutada):** Reconoce una página con texto y tabla y compara palabras y coordenadas con la imagen Éxito: Puedes medir errores sobre un fragmento conocido
- **Combina con:** `pdf-inspector` [13/conversion], `ragflow` [6/rag], `dify` [3/visual], `vllm` [23/serving]
- **Alternativas:** `tesseract`, `unlimited-ocr`, `olmocr`
- **Riesgos y avisos:** Alternativas (elige una): tesseract, olmocr, unlimited-ocr. Se retiró docling por no estar documentado. Elige OCR clásico, estructura o VLM según la tarea; no todos los pipelines tienen la misma instalación y memoria.

### OCRmyPDF (`ocrmypdf`)

- **Repo:** https://github.com/ocrmypdf/OCRmyPDF · MPL-2.0 · nivel 1 · 65/100
- **Qué es:** Herramienta de línea de comandos de código abierto (MPL-2.0) que añade una capa de texto OCR a PDF escaneados. Muy madura (v17.14) y probada en millones de PDF.
- **Cuándo elegirlo:** Casos: Hacer buscables documentos escaneados; Preparar un archivo histórico propio para indexación.
- **Requisitos:** nivel 1: preparación sencilla; Python; Ghostscript; Tesseract; paquete del idioma; PDF de prueba; hardware prerequisites; API de IA: no; Python; Ghostscript; Tesseract; paquete del idioma; PDF de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install ocrmypdf` — fuente: https://github.com/ocrmypdf/OCRmyPDF/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade OCR a una copia escaneada y busca una palabra que conoces Éxito: Puedes seleccionar y buscar texto manteniendo la imagen de la página
- **Combina con:** `tesseract`, `paperless-ngx` [13/gestion], `stirling-pdf` [13/pdf], `pdf-inspector` [13/conversion], `pdfding` [13/gestion]
- **Riesgos y avisos:** Se retiró docling por no estar documentado. La capa OCR puede contener errores; instala el idioma correcto y conserva el PDF original.

### Tesseract (`tesseract`)

- **Repo:** https://github.com/tesseract-ocr/tesseract · Apache-2.0 · nivel 1 · 64/100 · alternativa en «OCR de documentos»
- **Qué es:** Motor de OCR de código abierto (Apache 2.0) con biblioteca `libtesseract` y programa `tesseract`; nacido en HP y desarrollado después por Google. Hoy lo lidera Stefan Weil y lo mantiene Zdenko Podobny; maduro (5.5.4).
- **Cuándo elegirlo:** Casos: Digitalizar texto de una fotografía propia; Incorporar OCR local a un script.
- **Requisitos:** nivel 1: preparación sencilla; Binario o paquete; datos entrenados del idioma; imagen legible; hardware prerequisites; API de IA: no; Binario o paquete; datos entrenados del idioma; imagen legible.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install tesseract` — fuente: https://tesseract-ocr.github.io/tessdoc/Installation.html
- **Primera prueba propuesta (no ejecutada):** Reconoce una imagen con una frase conocida y cuenta errores del resultado Éxito: Puedes comprobar si idioma, orientación y resolución son adecuados
- **Combina con:** `ocrmypdf`, `paperless-ngx` [13/gestion], `unstructured` [13/conversion], `xberg` [13/conversion], `tika` [13/conversion]
- **Alternativas:** `paddleocr`, `unlimited-ocr`, `olmocr`
- **Riesgos y avisos:** Alternativa (elige una): paddleocr. Para diseños complejos o escritura a mano rinde peor que los modelos VLM. Es un motor OCR con modelos locales, no un LLM conversacional; la calidad depende de la imagen y el idioma configurado.

### Surya (`surya`)

- **Repo:** https://github.com/datalab-to/surya · Apache-2.0 · nivel 3 · 62/100
- **Qué es:** Modelo y biblioteca de OCR de Datalab (autores de marker). El código es Apache-2.0 y los pesos usan una licencia Open Rail-M modificada con límites comerciales. Activo; la versión actual es un VLM único.
- **Cuándo elegirlo:** Casos: digitalizar documentos escaneados en varios idiomas conservando el orden de lectura; extraer tablas de PDF como HTML con celdas combinadas. Evítalo si no tienes el hardware o no aceptas la licencia de los pesos.
- **Requisitos:** nivel 3: preparación media, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install surya-ocr` — fuente: https://github.com/datalab-to/surya/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install surya-ocr` y procesa una página de prueba con OCR y layout. Éxito: Obtienes el texto en orden de lectura y las regiones de layout detectadas.
- **Combina con:** `vllm` [23/serving], `llama-cpp` [8/motores], `marker` [13/conversion]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Para usos comerciales por encima de los umbrales de la licencia de pesos, contacta con Datalab.

### Unlimited-OCR (`unlimited-ocr`)

- **Repo:** https://github.com/baidu/Unlimited-OCR · MIT · nivel 3 · 62/100 · alternativa en «OCR de documentos»
- **Qué es:** Proyecto de investigación de Baidu (MIT) sobre análisis de documentos ultralargos, con la serie de modelos Unlimited OCR. Unlimited OCR 2 se publicó el 27 de octubre de 2026 junto con un artículo y el benchmark MarathonDocBench; no hay…
- **Cuándo elegirlo:** Casos: Estudiar parsing de documentos largos; Comparar un VLM OCR con otro motor.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él, necesita GPU; Python 3.10 y versiones fijadas; GPU grande; pesos y runtime del ejemplo; hardware prerequisites; API de IA: no; Python 3.10 y versiones fijadas; GPU grande; pesos y runtime del ejemplo.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/baidu/Unlimited-OCR/blob/main/README.md

  ```shell
  pip install torch==2.13.0 torchvision pillow transformers==4.52.1 huggingface-hub==0.36.0 \
    tokenizers==0.21.4 addict==2.4.0 einops==0.8.2 easydict==1.13
  ```
- **Primera prueba propuesta (no ejecutada):** Prueba un documento corto antes de procesar uno largo y compara texto y tablas Éxito: Puedes identificar errores y consumo de memoria en tu muestra
- **Combina con:** `sglang` [23/serving], `vllm` [23/serving], `transformers` [24/entrenamiento]
- **Alternativas:** `paddleocr`, `tesseract`, `olmocr`
- **Riesgos y avisos:** Alternativas (elige una): olmocr, paddleocr. Se retiraron litellm, cosmos y comfyui por no tener relación documentada. La prueba del autor usa una NVIDIA A800 de 80 GB; la promesa unlimited describe el método y no recursos ilimitados en cualquier equipo.

### pdf-craft (`pdf-craft`)

- **Repo:** https://github.com/oomol-lab/pdf-craft · MIT · nivel 2 · 58/100
- **Qué es:** Biblioteca Python de código abierto (MIT) de oomol-lab para libros escaneados, artículos y documentos técnicos. Activa (v2.6.7), con servicio oficial en línea.
- **Cuándo elegirlo:** Casos: Crear una versión editable de un escaneo propio; Preparar un EPUB desde material autorizado.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; extra local y modelos para ruta local; proveedor OCR o servicio para ruta remota; hardware prerequisites; API de IA: depends; Python; extra local y modelos para ruta local; proveedor OCR o servicio para ruta remota.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install "pdf-craft[local]"` — fuente: https://github.com/oomol-lab/pdf-craft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte dos páginas escaneadas propias y compara texto y estructura antes de generar un libro completo Éxito: Puedes identificar errores y corregir el orden de lectura
- **Combina con:** `vllm` [23/serving], `pandoc` [13/conversion], `ollama` [8/motores]
- **Alternativas:** `marker`
- **Riesgos y avisos:** Alternativa (elige una): marker. Se retiró unlimited-ocr porque no está documentado como backend. PDF-craft con guion es este conversor Python; no es PDFCraftTool/pdfcraft, la aplicación de herramientas PDF del navegador.

### olmOCR (`olmocr`)

- **Repo:** https://github.com/allenai/olmocr · Apache-2.0 · nivel 3 · 51/100 · alternativa en «OCR de documentos»
- **Qué es:** Kit del Allen Institute for AI (Apache 2.0) para convertir PDF y documentos de imagen en texto limpio. Versión v0.4.27; el último push es de marzo de 2026 y el último modelo anunciado en el README, de octubre de 2025.
- **Cuándo elegirlo:** Casos: Preparar PDFs para entrenamiento documental; Procesar escaneos con un VLM.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python y dependencias del sistema; GPU para inferencia local o proveedor remoto; PDF; hardware prerequisites; API de IA: opcional; Python y dependencias del sistema; GPU para inferencia local o proveedor remoto; PDF.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install olmocr` — fuente: https://github.com/allenai/olmocr/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte unas páginas con texto conocido y revisa orden de lectura y símbolos Éxito: Puedes comparar la salida con la página original y detectar omisiones
- **Combina con:** `vllm` [23/serving], `lightrag` [6/rag], `open-notebook` [8/notebooklm]
- **Alternativas:** `paddleocr`, `tesseract`, `unlimited-ocr`, `docling`
- **Riesgos y avisos:** Alternativas (elige una): paddleocr, docling, unlimited-ocr. Instalar el paquete cliente no proporciona por sí solo GPU ni créditos remotos; comienza con pocas páginas.

### Stirling-PDF (`stirling-pdf`)

- **Repo:** https://github.com/Stirling-Tools/Stirling-PDF · MIT + licencia propietaria (app/proprietary/, app/saas/) · nivel 1 · 76/100 · recomendado en «Suites de herramientas PDF»
- **Qué es:** Plataforma de edición de PDF de código abierto con modelo «open core» de Stirling Tools (licencia mixta; ver LICENSE). Muy activa (v3.3.0), con planes de servidor y Enterprise de pago.
- **Cuándo elegirlo:** Casos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz.
- **Requisitos:** nivel 1: preparación sencilla; Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor; hardware prerequisites; API de IA: no; Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf` — fuente: https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Une dos PDFs de prueba y verifica orden, páginas y metadatos del resultado Éxito: El archivo final se abre y contiene las páginas esperadas
- **Combina con:** `ocrmypdf` [13/ocr], `activepieces` [1/motores], `paperless-ngx` [13/gestion], `docuseal`
- **Alternativas:** `pdfcraft`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): pdfcraft. La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo.

### PDFMathTranslate (`pdfmathtranslate`)

- **Repo:** https://github.com/PDFMathTranslate/PDFMathTranslate · AGPL-3.0 · nivel 1 · 68/100
- **Qué es:** Herramienta de código abierto (AGPL-3.0) para traducir PDF científicos conservando el diseño, también conocida como pdf2zh. Muy activa (v1.9.11) y con servicio público gratuito en línea.
- **Cuándo elegirlo:** Casos: Leer un artículo en otro idioma; Crear una versión bilingüe de documentación propia.
- **Requisitos:** nivel 1: preparación sencilla; Python 3.11–3.12; proveedor de traducción u Ollama; PDF de prueba; hardware prerequisites; API de IA: depends; Python 3.11–3.12; proveedor de traducción u Ollama; PDF de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/PDFMathTranslate/PDFMathTranslate/blob/main/README.md

  ```bash
  pip install uv
     uv tool install --python 3.12 pdf2zh
  ```
- **Primera prueba propuesta (no ejecutada):** Traduce dos páginas con fórmulas y compara texto, nombres y disposición con el original Éxito: Puedes detectar traducciones incorrectas sin confundirlas con cambios de formato
- **Combina con:** `pdf-inspector` [13/conversion], `ollama` [8/motores], `litellm` [23/serving]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. El servicio público en línea procesa tus documentos en servidores ajenos. MCP stdio está documentado; conservar fórmulas y formato es un objetivo, no garantía de traducción técnica correcta.

### docuseal (`docuseal`)

- **Repo:** https://github.com/docusealco/docuseal · AGPL-3.0 · nivel 3 · 62/100
- **Qué es:** Plataforma de código abierto (AGPL-3.0) para rellenar y firmar documentos, de DocuSeal. Activa (3.3.6), con nube de pago y funciones Pro.
- **Cuándo elegirlo:** Casos: Preparar formularios internos de prueba; Evaluar un flujo de firma documental.
- **Requisitos:** nivel 3: preparación pesada; Docker; dominio y correo solo para despliegue real; documento y destinatario ficticios; hardware prerequisites; API de IA: no; Docker; dominio y correo solo para despliegue real; documento y destinatario ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --name docuseal -p 3000:3000 -v.:/data docuseal/docuseal` — fuente: https://github.com/docusealco/docuseal/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una plantilla de prueba con campos de texto y firma y completa una vista de ensayo Éxito: Puedes revisar el documento resultante y la ubicación de los campos
- **Combina con:** `activepieces` [1/motores], `twenty-main` [18/crm], `stirling-pdf`, `pdfcraft`
- **Alternativas:** `documenso`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Para producción usa PostgreSQL en lugar de SQLite y configura SMTP con SPF/DKIM. El ejemplo es para revisar la herramienta con datos de prueba; configura dominio, persistencia y permisos antes de un uso real.

### pdfcraft (`pdfcraft`)

- **Repo:** https://github.com/PDFCraftTool/pdfcraft · AGPL-3.0 · nivel 1 · 55/100 · alternativa en «Suites de herramientas PDF»
- **Qué es:** Suite de herramientas PDF en el navegador de PDFCraftTool, AGPL-3.0, activa con versiones por fecha. Tiene un proyecto hermano de escritorio, LibrePDF (Apache 2.0).
- **Cuándo elegirlo:** Casos: Editar PDFs desde un navegador; Convertir o dividir un documento de prueba.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Navegador moderno; PDFs de prueba; Node solo para self-hosting; hardware prerequisites; API de IA: no; Navegador moderno; PDFs de prueba; Node solo para self-hosting.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull ghcr.io/pdfcrafttool/pdfcraft:latest` — fuente: https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre dos PDFs en la app y combínalos sin usar un servicio externo de conversión Éxito: Puedes descargar el resultado y comprobar páginas y orden
- **Combina con:** `coolify` [22/infraestructura], `docuseal`, `paperless-ngx` [13/gestion]
- **Alternativas:** `stirling-pdf`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativa (elige una): stirling-pdf. Se retiró markitdown por falta de relación. La referencia a Ollama corresponde al proyecto relacionado LibrePDF, no demuestra esa función en PDFCraft web.

### Documenso (`documenso`)

- **Repo:** https://github.com/documenso/documenso · AGPL-3.0 · nivel 3 · 53/100
- **Qué es:** Alternativa de código abierto a DocuSign para gestionar firmas electrónicas de documentos PDF.
- **Cuándo elegirlo:** Casos: Recoger la firma de un acuerdo de prueba entre dos personas de tu equipo; Preparar una plantilla con campos de firma y fecha para reutilizarla. Evítalo si solo necesitas firmar algún PDF suelto y no quieres mantener un servidor con base de datos y correo.
- **Requisitos:** nivel 3: preparación pesada; TypeScript, package.json; hardware prerequisites; API de IA: opcional.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/documenso/documenso/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En la instalación local de desarrollo, crea una cuenta con un correo ficticio y confírmala desde http://localhost:9000. Sube un PDF propio de una página, añade como firmante a «Firmante Ficticio»… Éxito: En http://localhost:9000 abre el correo del firmante y firma. El documento pasa a completado y el PDF descargado…
- **Combina con:** `stirling-pdf`, `paperless-ngx` [13/gestion], `activepieces` [1/motores]
- **Alternativas:** `docuseal`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### paperless-ngx (`paperless-ngx`)

- **Repo:** https://github.com/paperless-ngx/paperless-ngx · GPL-3.0 · nivel 2 · 79/100
- **Qué es:** Sistema de gestión documental de código abierto (GPL-3.0), sucesor oficial de Paperless y Paperless-ng, mantenido por una comunidad. Muy activo (v3.4.2), con demo pública.
- **Cuándo elegirlo:** Casos: Organizar recibos de prueba; Construir un archivo documental buscable.
- **Requisitos:** nivel 2: Docker Compose con script de instalación; Docker o entorno de la guía; directorio persistente; idiomas OCR; documentos ficticios; hardware prerequisites; API de IA: no; Docker o entorno de la guía; directorio persistente; idiomas OCR; documentos ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/paperless-ngx/paperless-ngx/blob/dev/docs/setup.md
- **Primera prueba propuesta (no ejecutada):** Importa un documento de prueba y búscalo por una palabra reconocida y una etiqueta Éxito: Puedes abrir el original y localizarlo con su texto OCR
- **Combina con:** `ocrmypdf` [13/ocr], `tesseract` [13/ocr], `erpnext` [18/crm]
- **Riesgos y avisos:** Para varios usuarios usa la variante con PostgreSQL. La lista de proyectos relacionados está en su wiki. No es solo un conversor PDF: administra un archivo documental persistente; configura retención y copias antes de importar una colección real.

### PdfDing (`pdfding`)

- **Repo:** https://github.com/mrmn2/PdfDing · AGPL-3.0 · nivel 1 · 45/100
- **Qué es:** Gestor, visor y editor de PDF autoalojado (AGPL-3.0), creado por mrmn y financiado por el NGI0 Commons Fund de NLnet. Su repositorio canónico es Codeberg (codeberg.org/mrmn/PdfDing), donde sigue activo con la v1.15.0 del 1 de noviembre de…
- **Cuándo elegirlo:** Casos: Organizar una colección de PDFs; Consultar documentos desde varios dispositivos.
- **Requisitos:** nivel 1: preparación sencilla; Docker o entorno de la guía; volumen para documentos; cuenta de prueba; hardware prerequisites; API de IA: no; Docker o entorno de la guía; volumen para documentos; cuenta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://docs.pdfding.com/getting_started/docker/

  ```bash
  docker run --name pdfding \
      -p 8000:8000 \
      -v sqlite_data:/home/nonroot/pdfding/db -v media:/home/nonroot/pdfding/media \
      -e HOST_NAME=127.0.0.1 -e SECRET_KEY=some_secret \
      -e CSRF_COOKIE_SECURE=FALSE -e SESSION_COOKIE_SECURE=FALSE \
      -d \
      mrmn/pdfding:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Sube un PDF ficticio, añade una etiqueta y continúa su lectura en otra sesión Éxito: Puedes encontrar el documento y su progreso guardado
- **Combina con:** `ocrmypdf` [13/ocr], `paperless-ngx`, `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Fuente canónica: Codeberg. El repositorio de GitHub está archivado y solo se conserva como identidad de la estrella en el catálogo (`gh`, `github_id`); las…. El repositorio de GitHub está archivado desde que el proyecto se mudó a Codeberg; usa Codeberg y docs.pdfding.com como referencia. Sin OCR ni IA integrados.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-13.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «PDF, OCR y procesamiento de documentos», lee `docs/alexandria/categoria-13.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-13.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
