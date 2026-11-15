# 13. PDF, OCR y procesamiento de documentos — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `docling`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=docs,pdf,ocr,python

**Qué es:** Entiende la estructura del documento (tablas, layout, fórmulas, orden de lectura) y la exporta para RAG y agentes.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/docling-project/docling

**Instalación** [+]: `pip install docling`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres convertir documentos a Markdown con buena estructura
**Evita si:** solo tienes PDFs de texto simples; mira `markitdown`
**Combina con:** `llama-index`, `ragflow`, `qdrant`
**Alternativas (elige una):** `marker`, `mineru`, `unstructured`, `olmocr`

## `docuseal`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=pdf,server,ruby

**Qué es:** Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio.
**Stack:** Ruby, Dockerfile, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/docusealco/docuseal

**Instalación** [?]: `Seguir la instalación original: https://github.com/docusealco/docuseal/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `marker`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=docs,pdf,python

**Qué es:** Pensado para libros y papers, con opción de mejorar el resultado usando un LLM.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/datalab-to/marker

**Instalación** [+]: `pip install marker-pdf`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** conviertes PDFs largos con fórmulas
**Evita si:** necesitas uso comercial sin licencia; revisa su licencia
**Combina con:** `llama-index`
**Alternativas (elige una):** `docling`, `mineru`, `pdf-craft`

## `markitdown`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=docs,python

**Qué es:** Es la puerta de entrada habitual para ingesta de documentos en pipelines RAG.
**Stack:** Python 3.8+
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/markitdown

**Instalación** [+]: `pip install markitdown`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** alimentas LLMs con documentos de formatos variados
**Evita si:** ya tienes el texto limpio o necesitas fidelidad de layout total (no es un reconstructor de PDF)
**Combina con:** `ppt-master`, `open-notebook`

## `mineru`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=docs,pdf,ocr,python

**Qué es:** Muy bueno con papers científicos, tablas y fórmulas; ofrece CLI, API y app de escritorio.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/opendatalab/MinerU

**Instalación** [?]: `Seguir la instalación original: https://github.com/opendatalab/MinerU/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** procesas documentos científicos o técnicos complejos
**Evita si:** quieres algo ligero; mira `markitdown`
**Combina con:** `ragflow`
**Alternativas (elige una):** `docling`, `marker`

## `ocrmypdf`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=ocr,pdf,python

**Qué es:** Convierte escaneos en PDF/A buscables manteniendo la imagen original.
**Stack:** Python, Tesseract
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ocrmypdf/OCRmyPDF

**Instalación** [?]: `Seguir la instalación original: https://github.com/ocrmypdf/OCRmyPDF/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tienes PDFs escaneados que quieres buscar
**Evita si:** necesitas extraer estructura; mira `docling`
**Combina con:** `tesseract`, `docling`

## `olmocr`
role=app · exec=local · setup=heavy · mcp=False · prov=local · tags=ocr,pdf,python

**Qué es:** Pensado para crear datasets de entrenamiento a partir de millones de PDFs, con orden de lectura correcto.
**Stack:** Python, vLLM
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/allenai/olmocr

**Instalación** [+]: `pip install olmocr`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** procesas grandes volúmenes de PDFs con GPU
**Evita si:** no tienes GPU; mira `ocrmypdf` o `tesseract`
**Combina con:** `vllm`
**Alternativas (elige una):** `paddleocr`, `docling`, `unlimited-ocr`

## `paddleocr`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ocr,docs,python

**Qué es:** Reconoce texto en más de 80 idiomas y analiza documentos con tablas y layout. Incluye modelos pequeños para dispositivos.
**Stack:** Python, PaddlePaddle
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/PaddlePaddle/PaddleOCR

**Instalación** [?]: `Seguir la instalación original: https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas OCR preciso y multilingüe
**Evita si:** solo quieres hacer buscables PDFs escaneados; mira `ocrmypdf`
**Combina con:** `docling`
**Alternativas (elige una):** `tesseract`, `olmocr`, `unlimited-ocr`

## `pandoc`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=docs

**Qué es:** La navaja suiza de la conversión de textos: genera Word o PDF desde Markdown y al revés.
**Stack:** Haskell
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/jgm/pandoc

**Instalación** [?]: `Seguir la instalación original: https://github.com/jgm/pandoc/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas convertir entre formatos de texto
**Evita si:** necesitas extraer estructura de PDFs escaneados; mira `docling`
**Combina con:** `markitdown`

## `paperless-ngx`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=gestion,server,python

**Qué es:** Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados.
**Stack:** Python, Dockerfile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/paperless-ngx/paperless-ngx

**Instalación** [?]: `Seguir la instalación original: https://github.com/paperless-ngx/paperless-ngx/blob/dev/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `pdf-craft`
role=library · exec=hybrid · setup=medium · mcp=False · prov=local · tags=ocr,library,python

**Qué es:** Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/oomol-lab/pdf-craft

**Instalación** [+]: `python -m pip install pdf-craft`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Combina con:** `unlimited-ocr`
**Alternativas (elige una):** `marker`

## `pdf-inspector`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=pdf,docs,rust

**Qué es:** Detecta si un PDF necesita OCR para enrutarlo al proceso correcto, y extrae texto rápido cuando no hace falta. De Firecrawl.
**Stack:** Rust
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/firecrawl/pdf-inspector

**Instalación** [+]: `pip install pdf-inspector`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** procesas muchos PDFs y quieres ahorrar OCR
**Evita si:** necesitas la conversión completa a Markdown; mira `docling`
**Combina con:** `ocrmypdf`, `docling`

## `pdfcraft`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pdf,typescript

**Qué es:** Apunta a ser la alternativa local y sin nube a los servicios online de PDF.
**Stack:** web/TS
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/PDFCraftTool/pdfcraft

**Instalación** [?]: `Seguir la instalación original: https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** manipulas PDFs con privacidad y sin instalar nada
**Evita si:** necesitas conversión a Markdown para IA (markitdown) o edición de contenido (no solo manipulación de páginas)
**Combina con:** `markitdown`
**Alternativas (elige una):** `stirling-pdf`

## `pdfding`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pdf,docker

**Qué es:** Organiza y lee tus PDFs desde cualquier dispositivo. El desarrollo se trasladó a Codeberg.
**Stack:** Python, Django, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mrmn2/PdfDing

**Instalación** [?]: `Seguir la instalación original: https://github.com/mrmn2/PdfDing/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres organizar y leer PDFs en tu servidor
**Evita si:** necesitas editar PDFs; mira `stirling-pdf`
**Combina con:** `markitdown`, `ppt-master`, `reveal.js`

## `pdfmathtranslate`
role=app · exec=hybrid · setup=easy · mcp=False · prov=openai,google,local · tags=pdf,docs,python

**Qué es:** Ideal para leer artículos científicos en tu idioma sin perder el layout. Admite Google, DeepL, OpenAI, Ollama y más.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/PDFMathTranslate/PDFMathTranslate

**Instalación** [+]: `pip install pdf2zh`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** traduces PDFs técnicos y quieres conservar el formato
**Evita si:** necesitas editar el PDF; mira `stirling-pdf`
**Combina con:** `ollama`

## `stirling-pdf`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pdf,docker

**Qué es:** Más de 50 herramientas de PDF en el navegador sin enviar archivos a terceros.
**Stack:** Java, TypeScript, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Stirling-Tools/Stirling-PDF

**Instalación** [?]: `Seguir la instalación original: https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un iLovePDF privado
**Evita si:** solo necesitas OCR; mira `ocrmypdf`
**Combina con:** `ocrmypdf`
**Alternativas (elige una):** `pdfcraft`

## `tesseract`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=ocr,cpp

**Qué es:** Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma. La precisión depende del idioma, el escaneo y la preparación de la imagen.
**Stack:** C++
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/tesseract-ocr/tesseract

**Instalación** [?]: `Seguir la instalación original: https://github.com/tesseract-ocr/tesseract/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres OCR clásico sin GPU
**Evita si:** tus documentos tienen layouts complejos; mira `paddleocr`
**Combina con:** `ocrmypdf`
**Alternativas (elige una):** `paddleocr`

## `unlimited-ocr`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=ocr,docs,python

**Qué es:** Extrae texto y estructura de documentos de muchas páginas sin dividirlos, pensado para contexto largo.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/baidu/Unlimited-OCR

**Instalación** [?]: `Seguir la instalación original: https://github.com/baidu/Unlimited-OCR/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** procesas documentos muy largos con GPU
**Evita si:** necesitas algo probado y ligero; mira `docling`
**Combina con:** `litellm`, `cosmos`, `comfyui`
**Alternativas (elige una):** `olmocr`, `paddleocr`

## `unstructured`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=docs,data,python

**Qué es:** Particiona más de 25 tipos de archivo en elementos (títulos, tablas, texto) y los prepara para bases vectoriales.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/Unstructured-IO/unstructured

**Instalación** [+]: `pip install "unstructured[all-docs]"`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tienes muchos formatos de documentos distintos
**Evita si:** solo procesas PDFs; mira `docling`
**Combina con:** `llama-index`
**Alternativas (elige una):** `docling`

## `youtube2webpage`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=docs,javascript

**Qué es:** Convierte una charla en un artículo navegable con contexto visual.
**Stack:** Perl, yt-dlp, ffmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/obra/Youtube2Webpage

**Instalación** [?]: `Seguir la instalación original: https://github.com/obra/Youtube2Webpage/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres video → artículo con transcripción y capturas
**Evita si:** necesitas edición de video o el contenido no tiene subtítulos
**Combina con:** `whisper`
