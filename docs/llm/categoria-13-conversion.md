# Alexandría para agentes · Conversión de documentos para IA

Categoría 13 «PDF, OCR y procesamiento de documentos» › subcategoría `conversion`. 9 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=13&sub=conversion · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `docling` | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON… | 2 Intermedio | 78 | MIT (OSI permisiva) | recomendado |
| `markitdown` | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word… | 2 Intermedio | 70 | MIT (OSI permisiva) | sin grupo |
| `mineru` | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos… | 2 Intermedio | 68 | Apache-2.0 con condiciones adicionales (source-available) | alternativa |
| `xberg` | Motor de extracción de documentos en Rust: texto, tablas y metadatos de más de… | 2 Intermedio | 63 | MIT (OSI permisiva) | alternativa |
| `marker` | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `tika` | Kit de Apache que detecta y extrae texto y metadatos de más de mil tipos de… | 2 Intermedio | 59 | Apache-2.0 (OSI permisiva) | alternativa |
| `unstructured` | ETL open source que transforma documentos complejos en datos estructurados para… | 2 Intermedio | 58 | Apache-2.0 (OSI permisiva) | alternativa |
| `pandoc` | Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y… | 1 Básico | 56 | GPL-2.0 (OSI copyleft) | sin grupo |
| `pdf-inspector` | Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con… | 2 Intermedio | 56 | MIT (OSI permisiva) | sin grupo |

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

### markitdown (`markitdown`)

- **Repo:** https://github.com/microsoft/markitdown · MIT · nivel 2 · 70/100
- **Qué es:** Utilidad Python ligera de Microsoft (MIT) para convertir archivos a Markdown destinado a LLM y análisis de texto. Activa (v0.1.9); el repositorio incluye también un servidor MCP, un complemento de OCR y un complemento de ejemplo.
- **Cuándo elegirlo:** Casos: Preparar documentos Office para consulta; Crear una copia textual de un informe.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python 3.10–3.14; entorno virtual; extras del formato elegido; hardware prerequisites; API de IA: opcional; Python 3.10–3.14; entorno virtual; extras del formato elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install 'markitdown[all]'` — fuente: https://github.com/microsoft/markitdown/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte un DOCX ficticio a Markdown y revisa títulos, listas y tablas Éxito: El texto y el orden se pueden contrastar con el documento
- **Combina con:** `claude-code` [20/terminal], `khoj` [8/workspaces], `pandoc`
- **Riesgos y avisos:** Se retiraron las combinaciones antiguas con ppt-master y open-notebook por falta de relación documentada. Instala los extras necesarios; convertir a Markdown no conserva toda la maquetación del original.

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-13-conversion.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Conversión de documentos para IA», lee `docs/alexandria/categoria-13-conversion.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-13-conversion.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
