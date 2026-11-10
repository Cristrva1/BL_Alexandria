# 13. Documentos & Presentaciones — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `docling`
role=library · exec=local · setup=easy · mcp=True · prov=—

**Qué es:** Entiende la estructura del documento (tablas, layout, fórmulas, orden de lectura) y la exporta para RAG y agentes.
**Stack:** Python, PyTorch
**Repo:** https://github.com/docling-project/docling

**Instalación** [~]: `pip install docling   (o: uv add docling)`
_Nombre PyPI puede diferir de 'Docling'; verifica en pypi.org._

**Elige si:** quieres convertir documentos a Markdown con buena estructura
**Evita si:** solo tienes PDFs de texto simples; mira `markitdown`
**Combina con:** `llama-index`, `ragflow`, `qdrant`
**Alternativas (elige una):** `marker`, `mineru`, `unstructured`, `olmocr`

## `marker`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Pensado para libros y papers, con opción de mejorar el resultado usando un LLM.
**Stack:** Python, PyTorch
**Repo:** https://github.com/datalab-to/marker

**Instalación** [~]: `pip install marker   (o: uv add marker)`
_Nombre PyPI puede diferir de 'Marker'; verifica en pypi.org._

**Elige si:** conviertes PDFs largos con fórmulas
**Evita si:** necesitas uso comercial sin licencia; revisa su licencia
**Combina con:** `llama-index`
**Alternativas (elige una):** `docling`, `mineru`

## `markitdown`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Es la puerta de entrada habitual para ingesta de documentos en pipelines RAG.
**Stack:** Python 3.8+
**Repo:** https://github.com/microsoft/markitdown

**Instalación** [~]: `pip install markitdown   (o: uv add markitdown)`
_Nombre PyPI puede diferir de 'markitdown'; verifica en pypi.org._

**Elige si:** alimentas LLMs con documentos de formatos variados
**Evita si:** ya tienes el texto limpio o necesitas fidelidad de layout total (no es un reconstructor de PDF)
**Combina con:** `ppt-master`, `open-notebook`

## `marp`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Escribes Markdown con separadores y obtienes slides limpias; tiene extensión de VS Code.
**Stack:** TypeScript
**Repo:** https://github.com/marp-team/marp

**Instalación** [~]: `git clone https://github.com/marp-team/marp && cd marp && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres slides simples en Markdown
**Evita si:** necesitas interactividad y componentes; mira `slidev`
**Alternativas (elige una):** `slidev`, `reveal.js`

## `mermaid`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** GitHub, Notion y muchos editores lo renderizan de forma nativa; los LLM lo escriben muy bien.
**Stack:** TypeScript
**Repo:** https://github.com/mermaid-js/mermaid

**Instalación** [~]: `npm install mermaid   (o: pnpm add mermaid)`
_Nombre npm puede diferir de 'Mermaid'; verifica en npmjs.com._

**Elige si:** quieres diagramas como texto
**Evita si:** necesitas dibujar a mano alzada; mira `excalidraw`
**Combina con:** `slidev`
**Alternativas (elige una):** `excalidraw`

## `mineru`
role=app · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Muy bueno con papers científicos, tablas y fórmulas; ofrece CLI, API y app de escritorio.
**Stack:** Python, PyTorch
**Repo:** https://github.com/opendatalab/MinerU

**Instalación** [~]: `git clone https://github.com/opendatalab/MinerU && cd MinerU && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** procesas documentos científicos o técnicos complejos
**Evita si:** quieres algo ligero; mira `markitdown`
**Combina con:** `ragflow`
**Alternativas (elige una):** `docling`, `marker`

## `ocrmypdf`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Convierte escaneos en PDF/A buscables manteniendo la imagen original.
**Stack:** Python, Tesseract
**Repo:** https://github.com/ocrmypdf/OCRmyPDF

**Instalación** [~]: `git clone https://github.com/ocrmypdf/OCRmyPDF && cd OCRmyPDF && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tienes PDFs escaneados que quieres buscar
**Evita si:** necesitas extraer estructura; mira `docling`
**Combina con:** `tesseract`, `docling`

## `olmocr`
role=app · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** Pensado para crear datasets de entrenamiento a partir de millones de PDFs, con orden de lectura correcto.
**Stack:** Python, vLLM
**Repo:** https://github.com/allenai/olmocr

**Instalación** [~]: `git clone https://github.com/allenai/olmocr && cd olmocr && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** procesas grandes volúmenes de PDFs con GPU
**Evita si:** no tienes GPU; mira `ocrmypdf` o `tesseract`
**Combina con:** `vllm`
**Alternativas (elige una):** `paddleocr`, `docling`, `unlimited-ocr`

## `paddleocr`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Reconoce texto en más de 80 idiomas y analiza documentos con tablas y layout. Incluye modelos pequeños para dispositivos.
**Stack:** Python, PaddlePaddle
**Repo:** https://github.com/PaddlePaddle/PaddleOCR

**Instalación** [~]: `pip install paddleocr   (o: uv add paddleocr)`
_Nombre PyPI puede diferir de 'PaddleOCR'; verifica en pypi.org._

**Elige si:** necesitas OCR preciso y multilingüe
**Evita si:** solo quieres hacer buscables PDFs escaneados; mira `ocrmypdf`
**Combina con:** `docling`
**Alternativas (elige una):** `tesseract`, `olmocr`, `unlimited-ocr`

## `pandoc`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** La navaja suiza de la conversión de textos: genera Word o PDF desde Markdown y al revés.
**Stack:** Haskell
**Repo:** https://github.com/jgm/pandoc

**Instalación** [?]: `git clone https://github.com/jgm/pandoc (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas convertir entre formatos de texto
**Evita si:** necesitas extraer estructura de PDFs escaneados; mira `docling`
**Combina con:** `markitdown`

## `pdf-inspector`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Detecta si un PDF necesita OCR para enrutarlo al proceso correcto, y extrae texto rápido cuando no hace falta. De Firecrawl.
**Stack:** Rust
**Repo:** https://github.com/firecrawl/pdf-inspector

**Instalación** [?]: `git clone https://github.com/firecrawl/pdf-inspector (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** procesas muchos PDFs y quieres ahorrar OCR
**Evita si:** necesitas la conversión completa a Markdown; mira `docling`
**Combina con:** `ocrmypdf`, `docling`

## `pdfcraft`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Apunta a ser la alternativa local y sin nube a los servicios online de PDF.
**Stack:** web/TS
**Repo:** https://github.com/PDFCraftTool/pdfcraft

**Instalación** [?]: `git clone https://github.com/PDFCraftTool/pdfcraft (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** manipulas PDFs con privacidad y sin instalar nada
**Evita si:** necesitas conversión a Markdown para IA (markitdown) o edición de contenido (no solo manipulación de páginas)
**Combina con:** `markitdown`
**Alternativas (elige una):** `stirling-pdf`

## `pdfding`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Organiza y lee tus PDFs desde cualquier dispositivo. El desarrollo se trasladó a Codeberg.
**Stack:** Python, Django, Docker
**Repo:** https://github.com/mrmn2/PdfDing

**Instalación** [~]: `git clone https://github.com/mrmn2/PdfDing && cd PdfDing && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres organizar y leer PDFs en tu servidor
**Evita si:** necesitas editar PDFs; mira `stirling-pdf`
**Combina con:** `markitdown`, `ppt-master`, `reveal.js`

## `pdfmathtranslate`
role=app · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'google', 'local']

**Qué es:** Ideal para leer artículos científicos en tu idioma sin perder el layout. Admite Google, DeepL, OpenAI, Ollama y más.
**Stack:** Python
**Repo:** https://github.com/PDFMathTranslate/PDFMathTranslate

**Instalación** [~]: `git clone https://github.com/PDFMathTranslate/PDFMathTranslate && cd PDFMathTranslate && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** traduces PDFs técnicos y quieres conservar el formato
**Evita si:** necesitas editar el PDF; mira `stirling-pdf`
**Combina con:** `ollama`

## `ppt-master`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Sustituye el maquetado manual de slides por un borrador estructurado por un LLM.
**Stack:** Python, python-pptx
**Repo:** https://github.com/hugohe3/ppt-master

**Instalación** [~]: `git clone https://github.com/hugohe3/ppt-master && cd ppt-master && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres PPTX editable de Office rápido
**Evita si:** prefieres slides web por código (reveal.js) o control de diseño pixel-perfect
**Combina con:** `markitdown`
**Alternativas (elige una):** `presenton`

## `presenton`
role=app · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'google', 'local']

**Qué es:** Crea presentaciones editables a partir de un prompt o documento, con tus plantillas, y exporta a PPTX o PDF.
**Stack:** TypeScript, Python, Docker
**Repo:** https://github.com/presenton/presenton

**Instalación** [~]: `git clone https://github.com/presenton/presenton && cd presenton && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres generar presentaciones de negocio con IA
**Evita si:** prefieres control total como código; mira `slidev`
**Combina con:** `ollama`
**Alternativas (elige una):** `ppt-master`

## `reveal.js`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Convierte las diapositivas en una página web versionable y reproducible por código.
**Stack:** JavaScript/HTML
**Repo:** https://github.com/hakimel/reveal.js

**Instalación** [~]: `npm install reveal.js   (o: pnpm add reveal.js)`
_Nombre npm puede diferir de 'reveal.js'; verifica en npmjs.com._

**Elige si:** quieres slides web por código, versionables
**Evita si:** necesitas PPTX editable en Office (ppt-master) o un editor visual de slides
**Combina con:** `markitdown`
**Alternativas (elige una):** `slidev`, `marp`

## `slidev`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Escribe tus slides en Markdown y obtén resaltado de código, diagramas, animaciones y exportación a PDF. Los agentes de código lo usan bien.
**Stack:** TypeScript, Vue, Vite
**Repo:** https://github.com/slidevjs/slidev

**Instalación** [~]: `git clone https://github.com/slidevjs/slidev && cd slidev && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** haces presentaciones técnicas y quieres control como código
**Evita si:** necesitas slides para negocio generadas con IA; mira `presenton`
**Combina con:** `mermaid`
**Alternativas (elige una):** `marp`, `reveal.js`

## `stirling-pdf`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Más de 50 herramientas de PDF en el navegador sin enviar archivos a terceros.
**Stack:** Java, TypeScript, Docker
**Repo:** https://github.com/Stirling-Tools/Stirling-PDF

**Instalación** [~]: `git clone https://github.com/Stirling-Tools/Stirling-PDF && cd Stirling-PDF && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un iLovePDF privado
**Evita si:** solo necesitas OCR; mira `ocrmypdf`
**Combina con:** `ocrmypdf`
**Alternativas (elige una):** `pdfcraft`

## `tesseract`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Base de muchas herramientas de OCR, ligero y sin GPU.
**Stack:** C++
**Repo:** https://github.com/tesseract-ocr/tesseract

**Instalación** [?]: `git clone https://github.com/tesseract-ocr/tesseract (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres OCR clásico sin GPU
**Evita si:** tus documentos tienen layouts complejos; mira `paddleocr`
**Combina con:** `ocrmypdf`
**Alternativas (elige una):** `paddleocr`

## `unlimited-ocr`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Extrae texto y estructura de documentos de muchas páginas sin dividirlos, pensado para contexto largo.
**Stack:** Python, PyTorch
**Repo:** https://github.com/baidu/Unlimited-OCR

**Instalación** [~]: `pip install unlimited-ocr   (o: uv add unlimited-ocr)`
_Nombre PyPI puede diferir de 'Unlimited-OCR'; verifica en pypi.org._

**Elige si:** procesas documentos muy largos con GPU
**Evita si:** necesitas algo probado y ligero; mira `docling`
**Combina con:** `litellm`, `cosmos`, `comfyui`
**Alternativas (elige una):** `olmocr`, `paddleocr`

## `unstructured`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Particiona más de 25 tipos de archivo en elementos (títulos, tablas, texto) y los prepara para bases vectoriales.
**Stack:** Python
**Repo:** https://github.com/Unstructured-IO/unstructured

**Instalación** [~]: `pip install unstructured   (o: uv add unstructured)`
_Nombre PyPI puede diferir de 'Unstructured'; verifica en pypi.org._

**Elige si:** tienes muchos formatos de documentos distintos
**Evita si:** solo procesas PDFs; mira `docling`
**Combina con:** `llama-index`
**Alternativas (elige una):** `docling`

## `youtube2webpage`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Convierte una charla en un artículo navegable con contexto visual.
**Stack:** Perl, yt-dlp, ffmpeg
**Repo:** https://github.com/obra/Youtube2Webpage

**Instalación** [?]: `git clone https://github.com/obra/Youtube2Webpage (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres video → artículo con transcripción y capturas
**Evita si:** necesitas edición de video o el contenido no tiene subtítulos
**Combina con:** `whisper`
