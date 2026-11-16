# 13. PDF, OCR y procesamiento de documentos — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `docling`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=docs,pdf,ocr,python

**Qué es:** Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA.
**Stack:** Python >=3.10; modelos y dependencias del formato; documento de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta local no requiere modelo remoto; VLM, servicios y despliegues gestionados pueden tener costes y licencias propias
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. MCP es un paquete complementario y convierte localmente por defecto; configura explícitamente cualquier delegación a un servicio remoto
- Coste: El coste depende del proveedor o la ruta. La ruta local no requiere modelo remoto; VLM, servicios y despliegues gestionados pueden tener costes y licencias propias
- Equipo: Preparación según la ruta elegida. Python >=3.10; modelos y dependencias del formato; documento de prueba
**Repo:** https://github.com/docling-project/docling

**Instalación** [+]:

```
pip install docling
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar documentos para RAG; Extraer tablas antes de un análisis
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte un PDF breve con tabla y compara el Markdown y JSON con el original
**Qué comprobar:** Puedes identificar texto, estructura y campos que necesitan corrección
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `llama-index`, `ragflow`, `qdrant`
**Alternativas (elige una):** `marker`, `mineru`, `unstructured`, `olmocr`

## `docuseal`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=pdf,server,ruby

**Qué es:** Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio.
**Stack:** Docker; dominio y correo solo para despliegue real; documento y destinatario ficticios
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El núcleo AGPL añade términos; Pro, Cloud y servicios de correo tienen condiciones propias; no exige LLM
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El ejemplo es para revisar la herramienta con datos de prueba; configura dominio, persistencia y permisos antes de un uso real
- Coste: El coste depende del proveedor o la ruta. El núcleo AGPL añade términos; Pro, Cloud y servicios de correo tienen condiciones propias; no exige LLM
- Equipo: Preparación según la ruta elegida. Docker; dominio y correo solo para despliegue real; documento y destinatario ficticios
**Repo:** https://github.com/docusealco/docuseal

**Instalación** [+]:

```
docker run --name docuseal -p 3000:3000 -v.:/data docuseal/docuseal
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar formularios internos de prueba; Evaluar un flujo de firma documental
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una plantilla de prueba con campos de texto y firma y completa una vista de ensayo
**Qué comprobar:** Puedes revisar el documento resultante y la ubicación de los campos
Revisión documental individual; instalación no ejecutada por Alexandría.

## `marker`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=docs,pdf,python

**Qué es:** Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código.
**Stack:** Python; backend Surya con vLLM o llama.cpp según sistema; pesos; PDF de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Código Apache-2.0; pesos con licencia modificada y condiciones comerciales según organización; LLM opcional puede usar proveedores de pago
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Instalar marker-pdf no completa por sí solo el backend de inferencia; verifica requisitos del modelo y su licencia antes de ampliar volumen
- Coste: El coste depende del proveedor o la ruta. Código Apache-2.0; pesos con licencia modificada y condiciones comerciales según organización; LLM opcional puede usar proveedores de pago
- Equipo: Preparación según la ruta elegida. Python; backend Surya con vLLM o llama.cpp según sistema; pesos; PDF de prueba
**Repo:** https://github.com/datalab-to/marker

**Instalación** [+]:

```
pip install marker-pdf
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer contenido de informes; Preparar documentos escaneados para búsqueda
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte un PDF de dos páginas con una tabla y compara texto y columnas
**Qué comprobar:** Puedes localizar errores y decidir si activar la mejora LLM
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `llama-index`
**Alternativas (elige una):** `docling`, `mineru`, `pdf-craft`

## `markitdown`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=docs,python

**Qué es:** Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman.
**Stack:** Python 3.10–3.14; entorno virtual; extras del formato elegido
**Acceso y costes:**
- API de IA: API de IA opcional. La extracción básica es offline; Azure, descripciones LLM y otras extensiones pueden enviar datos y consumir servicios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Instala los extras necesarios; convertir a Markdown no conserva toda la maquetación del original
- Coste: El coste depende del proveedor o la ruta. La extracción básica es offline; Azure, descripciones LLM y otras extensiones pueden enviar datos y consumir servicios
- Equipo: Preparación según la ruta elegida. Python 3.10–3.14; entorno virtual; extras del formato elegido
**Repo:** https://github.com/microsoft/markitdown

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/microsoft/markitdown/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar documentos Office para consulta; Crear una copia textual de un informe
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte un DOCX ficticio a Markdown y revisa títulos, listas y tablas
**Qué comprobar:** El texto y el orden se pueden contrastar con el documento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ppt-master`, `open-notebook`

## `mineru`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=docs,pdf,ocr,python

**Qué es:** Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes.
**Stack:** Python 3.11–3.14; entorno virtual; modelos y backend del nivel elegido
**Acceso y costes:**
- API de IA: API de IA opcional. Los niveles locales usan CPU o GPU según backend; remoto requiere autorización explícita y puede costar; licencia MinerU añade condiciones
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. La skill ayuda al agente a operar la herramienta; no es un modelo incluido en la suscripción del cliente; la telemetría tiene configuración propia
- Coste: El coste depende del proveedor o la ruta. Los niveles locales usan CPU o GPU según backend; remoto requiere autorización explícita y puede costar; licencia MinerU añade condiciones
- Equipo: Preparación según la ruta elegida. Python 3.11–3.14; entorno virtual; modelos y backend del nivel elegido
**Repo:** https://github.com/opendatalab/MinerU

**Instalación** [+]:

```
uv pip install -U "mineru>=4.0,<5"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar PDFs complejos para un índice; Extraer tablas y fórmulas de un documento propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Procesa un PDF corto con Flash o Basic y compara estructura y tablas antes de usar niveles superiores
**Qué comprobar:** Puedes identificar nivel, backend y origen de la conversión
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ragflow`
**Alternativas (elige una):** `docling`, `marker`

## `ocrmypdf`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=ocr,pdf,python

**Qué es:** Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos.
**Stack:** Python; Ghostscript; Tesseract; paquete del idioma; PDF de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita LLM ni API; procesamiento y paquetes locales consumen recursos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La capa OCR puede contener errores; instala el idioma correcto y conserva el PDF original
- Coste: Sin pago a un modelo en la ruta básica. No necesita LLM ni API; procesamiento y paquetes locales consumen recursos
- Equipo: Preparación según la ruta elegida. Python; Ghostscript; Tesseract; paquete del idioma; PDF de prueba
**Repo:** https://github.com/ocrmypdf/OCRmyPDF

**Instalación** [?]:

```
Seguir la instalación original: https://ocrmypdf.readthedocs.io/en/latest/installation.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Hacer buscables documentos escaneados; Preparar un archivo histórico propio para indexación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade OCR a una copia escaneada y busca una palabra que conoces
**Qué comprobar:** Puedes seleccionar y buscar texto manteniendo la imagen de la página
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tesseract`, `docling`

## `olmocr`
role=app · exec=local · setup=heavy · mcp=False · prov=local · tags=ocr,pdf,python

**Qué es:** Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala.
**Stack:** Python y dependencias del sistema; GPU para inferencia local o proveedor remoto; PDF
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta local necesita GPU; endpoints alojados cobran según proveedor; guardar resultados también consume espacio
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Instalar el paquete cliente no proporciona por sí solo GPU ni créditos remotos; comienza con pocas páginas
- Coste: El coste depende del proveedor o la ruta. La ruta local necesita GPU; endpoints alojados cobran según proveedor; guardar resultados también consume espacio
- Equipo: Preparación según la ruta elegida. Python y dependencias del sistema; GPU para inferencia local o proveedor remoto; PDF
**Repo:** https://github.com/allenai/olmocr

**Instalación** [+]:

```
pip install olmocr
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar PDFs para entrenamiento documental; Procesar escaneos con un VLM
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte unas páginas con texto conocido y revisa orden de lectura y símbolos
**Qué comprobar:** Puedes comparar la salida con la página original y detectar omisiones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`
**Alternativas (elige una):** `paddleocr`, `docling`, `unlimited-ocr`

## `paddleocr`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ocr,docs,python

**Qué es:** Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA.
**Stack:** Python y PaddlePaddle compatibles; modelo y paquete de idioma; imagen de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta local no exige API; GPU, modelos y servicios opcionales tienen requisitos y condiciones propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Elige OCR clásico, estructura o VLM según la tarea; no todos los pipelines tienen la misma instalación y memoria
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no exige API; GPU, modelos y servicios opcionales tienen requisitos y condiciones propios
- Equipo: Preparación según la ruta elegida. Python y PaddlePaddle compatibles; modelo y paquete de idioma; imagen de prueba
**Repo:** https://github.com/PaddlePaddle/PaddleOCR

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/installation.en.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Digitalizar un formulario propio; Extraer texto y estructura de una página escaneada
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Reconoce una página con texto y tabla y compara palabras y coordenadas con la imagen
**Qué comprobar:** Puedes medir errores sobre un fragmento conocido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `docling`
**Alternativas (elige una):** `tesseract`, `olmocr`, `unlimited-ocr`

## `pandoc`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=docs

**Qué es:** Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos.
**Stack:** Binario de tu sistema; motor PDF solo si generas PDF; archivo de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere IA; motores PDF, fuentes y herramientas complementarias tienen sus condiciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Cambiar formato no garantiza conservar cada detalle de diseño; elige plantilla y motor según la salida
- Coste: Sin pago a un modelo en la ruta básica. No requiere IA; motores PDF, fuentes y herramientas complementarias tienen sus condiciones
- Equipo: Preparación según la ruta elegida. Binario de tu sistema; motor PDF solo si generas PDF; archivo de prueba
**Repo:** https://github.com/jgm/pandoc

**Instalación** [?]:

```
Seguir la instalación original: https://pandoc.org/installing.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Generar documentos desde Markdown; Convertir un libro propio a EPUB
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte un Markdown con títulos y tabla a DOCX y revisa el resultado
**Qué comprobar:** Puedes abrir el documento y comprobar estructura y contenido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `markitdown`

## `paperless-ngx`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=gestion,server,python

**Qué es:** Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados.
**Stack:** Docker o entorno de la guía; directorio persistente; idiomas OCR; documentos ficticios
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta básica usa OCR local sin API de IA; servidor, almacenamiento y copias requieren recursos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No es solo un conversor PDF: administra un archivo documental persistente; configura retención y copias antes de importar una colección real
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica usa OCR local sin API de IA; servidor, almacenamiento y copias requieren recursos
- Equipo: Preparación según la ruta elegida. Docker o entorno de la guía; directorio persistente; idiomas OCR; documentos ficticios
**Repo:** https://github.com/paperless-ngx/paperless-ngx

**Instalación** [?]:

```
Seguir la instalación original: https://docs.paperless-ngx.com/setup/#installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar recibos de prueba; Construir un archivo documental buscable
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Importa un documento de prueba y búscalo por una palabra reconocida y una etiqueta
**Qué comprobar:** Puedes abrir el original y localizarlo con su texto OCR
Revisión documental individual; instalación no ejecutada por Alexandría.

## `pdf-craft`
role=library · exec=hybrid · setup=medium · mcp=False · prov=local · tags=ocr,library,python

**Qué es:** Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento.
**Stack:** Python; extra local y modelos para ruta local; proveedor OCR o servicio para ruta remota
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Ofrece servicio remoto y extra local; proveedores, hardware y pesos tienen condiciones separadas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. PDF-craft con guion es este conversor Python; no es PDFCraftTool/pdfcraft, la aplicación de herramientas PDF del navegador
- Coste: El coste depende del proveedor o la ruta. Ofrece servicio remoto y extra local; proveedores, hardware y pesos tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. Python; extra local y modelos para ruta local; proveedor OCR o servicio para ruta remota
**Repo:** https://github.com/oomol-lab/pdf-craft

**Instalación** [+]:

```
python -m pip install "pdf-craft[local]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una versión editable de un escaneo propio; Preparar un EPUB desde material autorizado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte dos páginas escaneadas propias y compara texto y estructura antes de generar un libro completo
**Qué comprobar:** Puedes identificar errores y corregir el orden de lectura
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `unlimited-ocr`
**Alternativas (elige una):** `marker`

## `pdf-inspector`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=pdf,docs,rust

**Qué es:** Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas.
**Stack:** Python para esta ruta; runtime OCR y pesos solo si activas OCR; PDFs de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La extracción básica no exige API; OCR selectivo usa modelo local y requiere dependencias adicionales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La instalación base y las funciones OCR no tienen los mismos recursos; la clasificación no verifica exactitud de todo el texto
- Coste: Sin pago a un modelo en la ruta básica. La extracción básica no exige API; OCR selectivo usa modelo local y requiere dependencias adicionales
- Equipo: Preparación según la ruta elegida. Python para esta ruta; runtime OCR y pesos solo si activas OCR; PDFs de prueba
**Repo:** https://github.com/firecrawl/pdf-inspector

**Instalación** [+]:

```
pip install pdf-inspector
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Decidir cuándo hace falta OCR; Extraer texto con posiciones de un PDF
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Clasifica un PDF con texto y otro escaneado y compara el resultado
**Qué comprobar:** Puedes enrutar el escaneado a OCR y extraer el otro sin ese procesamiento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ocrmypdf`, `docling`

## `pdfcraft`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pdf,typescript

**Qué es:** Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada.
**Stack:** Navegador moderno; PDFs de prueba; Node solo para self-hosting
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las herramientas del navegador no requieren modelo; hosting propio y productos enlazados tienen condiciones aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La referencia a Ollama corresponde al proyecto relacionado LibrePDF, no demuestra esa función en PDFCraft web
- Coste: Sin pago a un modelo en la ruta básica. Las herramientas del navegador no requieren modelo; hosting propio y productos enlazados tienen condiciones aparte
- Equipo: Preparación según la ruta elegida. Navegador moderno; PDFs de prueba; Node solo para self-hosting
**Repo:** https://github.com/PDFCraftTool/pdfcraft

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Editar PDFs desde un navegador; Convertir o dividir un documento de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre dos PDFs en la app y combínalos sin usar un servicio externo de conversión
**Qué comprobar:** Puedes descargar el resultado y comprobar páginas y orden
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `markitdown`
**Alternativas (elige una):** `stirling-pdf`

## `pdfding`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pdf,docker

**Qué es:** Gestor y visor de PDFs auto-hospedado, ligero, con etiquetas y progreso de lectura.
**Stack:** Docker o entorno de la guía; volumen para documentos; cuenta de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El gestor básico no requiere IA; servidor y almacenamiento son recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El desarrollo se ha trasladado a Codeberg; sigue el enlace canónico y la documentación antes de usar instrucciones GitHub antiguas
- Coste: Sin pago a un modelo en la ruta básica. El gestor básico no requiere IA; servidor y almacenamiento son recursos propios
- Equipo: Preparación según la ruta elegida. Docker o entorno de la guía; volumen para documentos; cuenta de prueba
**Repo:** https://codeberg.org/mrmn/PdfDing

**Instalación** [?]:

```
Seguir la instalación original: https://docs.pdfding.com/getting_started/docker/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una colección de PDFs; Consultar documentos desde varios dispositivos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sube un PDF ficticio, añade una etiqueta y continúa su lectura en otra sesión
**Qué comprobar:** Puedes encontrar el documento y su progreso guardado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `markitdown`, `ppt-master`, `reveal.js`

## `pdfmathtranslate`
role=app · exec=hybrid · setup=easy · mcp=True · prov=openai,google,local · tags=pdf,docs,python

**Qué es:** Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe.
**Stack:** Python 3.11–3.12; proveedor de traducción u Ollama; PDF de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El coste depende del traductor; puede usar servicios remotos o modelo Ollama; el procesamiento y modelos locales requieren recursos
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. MCP stdio está documentado; conservar fórmulas y formato es un objetivo, no garantía de traducción técnica correcta
- Coste: El coste depende del proveedor o la ruta. El coste depende del traductor; puede usar servicios remotos o modelo Ollama; el procesamiento y modelos locales requieren recursos
- Equipo: Preparación según la ruta elegida. Python 3.11–3.12; proveedor de traducción u Ollama; PDF de prueba
**Repo:** https://github.com/PDFMathTranslate/PDFMathTranslate

**Instalación** [+]:

```
pip install uv
   uv tool install --python 3.12 pdf2zh
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Leer un artículo en otro idioma; Crear una versión bilingüe de documentación propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Traduce dos páginas con fórmulas y compara texto, nombres y disposición con el original
**Qué comprobar:** Puedes detectar traducciones incorrectas sin confundirlas con cambios de formato
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`

## `stirling-pdf`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pdf,docker

**Qué es:** Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs.
**Stack:** Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El proyecto es open-core; Server y Enterprise tienen planes; la operación PDF básica no exige modelo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo
- Coste: El coste depende del proveedor o la ruta. El proyecto es open-core; Server y Enterprise tienen planes; la operación PDF básica no exige modelo
- Equipo: Preparación según la ruta elegida. Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor
**Repo:** https://github.com/Stirling-Tools/Stirling-PDF

**Instalación** [+]:

```
docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Une dos PDFs de prueba y verifica orden, páginas y metadatos del resultado
**Qué comprobar:** El archivo final se abre y contiene las páginas esperadas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ocrmypdf`
**Alternativas (elige una):** `pdfcraft`

## `tesseract`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=ocr,cpp

**Qué es:** Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma.
**Stack:** Binario o paquete; datos entrenados del idioma; imagen legible
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API; modelos de idioma y procesamiento son locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es un motor OCR con modelos locales, no un LLM conversacional; la calidad depende de la imagen y el idioma configurado
- Coste: Sin pago a un modelo en la ruta básica. No requiere API; modelos de idioma y procesamiento son locales
- Equipo: Preparación según la ruta elegida. Binario o paquete; datos entrenados del idioma; imagen legible
**Repo:** https://github.com/tesseract-ocr/tesseract

**Instalación** [?]:

```
Seguir la instalación original: https://tesseract-ocr.github.io/tessdoc/Installation.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Digitalizar texto de una fotografía propia; Incorporar OCR local a un script
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Reconoce una imagen con una frase conocida y cuenta errores del resultado
**Qué comprobar:** Puedes comprobar si idioma, orientación y resolución son adecuados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ocrmypdf`
**Alternativas (elige una):** `paddleocr`

## `unlimited-ocr`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=ocr,docs,python

**Qué es:** Modelo de Baidu para parsear documentos largos de una sola pasada con visión.
**Stack:** Python 3.10 y versiones fijadas; GPU grande; pesos y runtime del ejemplo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API remota; el entorno y pesos usan recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La prueba del autor usa una NVIDIA A800 de 80 GB; la promesa unlimited describe el método y no recursos ilimitados en cualquier equipo
- Coste: Sin pago a un modelo en la ruta básica. No exige API remota; el entorno y pesos usan recursos propios
- Equipo: Preparación según la ruta elegida. Python 3.10 y versiones fijadas; GPU grande; pesos y runtime del ejemplo
**Repo:** https://github.com/baidu/Unlimited-OCR

**Instalación** [+]:

```
pip install torch==2.13.0 torchvision pillow transformers==4.52.1 huggingface-hub==0.36.0 \
  tokenizers==0.21.4 addict==2.4.0 einops==0.8.2 easydict==1.13
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar parsing de documentos largos; Comparar un VLM OCR con otro motor
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba un documento corto antes de procesar uno largo y compara texto y tablas
**Qué comprobar:** Puedes identificar errores y consumo de memoria en tu muestra
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `cosmos`, `comfyui`
**Alternativas (elige una):** `olmocr`, `paddleocr`

## `unstructured`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=docs,data,python

**Qué es:** ETL open source que transforma documentos complejos en datos estructurados para LLM.
**Stack:** Python; extras por formato; herramientas del sistema para PDF o imágenes
**Acceso y costes:**
- API de IA: API de IA opcional. La biblioteca local y la plataforma gestionada son rutas distintas; partición, enriquecimiento y modelos externos pueden consumir servicios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Instala dependencias del formato; el contenedor y la biblioteca no garantizan por sí solos todas las funciones de la plataforma
- Coste: El coste depende del proveedor o la ruta. La biblioteca local y la plataforma gestionada son rutas distintas; partición, enriquecimiento y modelos externos pueden consumir servicios
- Equipo: Preparación según la ruta elegida. Python; extras por formato; herramientas del sistema para PDF o imágenes
**Repo:** https://github.com/Unstructured-IO/unstructured

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Unstructured-IO/unstructured/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar documentos para una base de conocimiento; Crear un pipeline ETL de archivos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Divide un documento ficticio en elementos y comprueba título, párrafos y tabla
**Qué comprobar:** Los elementos conservan el orden y tipos que necesitas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `llama-index`
**Alternativas (elige una):** `docling`
