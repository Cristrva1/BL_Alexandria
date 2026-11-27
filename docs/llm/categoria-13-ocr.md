# Alexandría para agentes · OCR

Categoría 13 «PDF, OCR y procesamiento de documentos» › subcategoría `ocr`. 7 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=13&sub=ocr · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `paddleocr` | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos… | 2 Intermedio | 72 | Apache-2.0 (OSI permisiva) | recomendado |
| `ocrmypdf` | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. | 1 Básico | 65 | MPL-2.0 (OSI copyleft) | sin grupo |
| `tesseract` | Motor de OCR de código abierto que reconoce texto en imágenes y documentos… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | alternativa |
| `surya` | OCR multilingüe y análisis de layout con un VLM de 689M parámetros: orden de… | 3 Avanzado | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `unlimited-ocr` | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. | 3 Avanzado | 62 | MIT (OSI permisiva) | alternativa |
| `pdf-craft` | Herramienta para convertir libros escaneados en PDF a documentos editables… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `olmocr` | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión… | 3 Avanzado | 50 | Apache-2.0 (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### PaddleOCR (`paddleocr`)

- **Repo:** https://github.com/PaddlePaddle/PaddleOCR · Apache-2.0 · nivel 2 · 72/100 · recomendado en «OCR de documentos»
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
- **Combina con:** `tesseract`, `paperless-ngx` [13/gestion], `stirling-pdf` [13/pdf], `pdf-inspector` [13/conversion], `pdfding` [13/pdf]
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

- **Repo:** https://github.com/allenai/olmocr · Apache-2.0 · nivel 3 · 50/100 · alternativa en «OCR de documentos»
- **Qué es:** Kit del Allen Institute for AI (Apache 2.0) para convertir PDF y documentos de imagen en texto limpio. Versión v0.4.27; el último push es de marzo de 2026 y el último modelo anunciado en el README, de octubre de 2025.
- **Cuándo elegirlo:** Casos: Preparar PDFs para entrenamiento documental; Procesar escaneos con un VLM.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python y dependencias del sistema; GPU para inferencia local o proveedor remoto; PDF; hardware prerequisites; API de IA: opcional; Python y dependencias del sistema; GPU para inferencia local o proveedor remoto; PDF.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install olmocr` — fuente: https://github.com/allenai/olmocr/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Convierte unas páginas con texto conocido y revisa orden de lectura y símbolos Éxito: Puedes comparar la salida con la página original y detectar omisiones
- **Combina con:** `vllm` [23/serving], `lightrag` [6/rag], `open-notebook` [8/notebooklm]
- **Alternativas:** `paddleocr`, `tesseract`, `unlimited-ocr`, `docling`
- **Riesgos y avisos:** Alternativas (elige una): paddleocr, docling, unlimited-ocr. Instalar el paquete cliente no proporciona por sí solo GPU ni créditos remotos; comienza con pocas páginas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-13-ocr.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «OCR», lee `docs/alexandria/categoria-13-ocr.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-13-ocr.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
