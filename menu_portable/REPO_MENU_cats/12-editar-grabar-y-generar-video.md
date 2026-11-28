# 12. Editar, grabar y generar video — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ai-youtube-shorts-generator`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=generativo,2short-ai-alternative,ai-clip-generator,ai-clipping,auto-clip,auto-crop,highlight-detection,klap-alternative

**Qué es:** Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM.
**Stack:** Python; FFmpeg y dependencias locales si eliges ese modo; clave LLM; video autorizado
**Acceso y costes:**
- API de IA: API de IA necesaria. El modo API usa MuAPI; el modo local procesa medios en tu equipo pero conserva llamadas OpenAI o Gemini para ranking
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Local no significa todo offline; las puntuaciones de viralidad son heurísticas del proyecto y no predicen vistas
- Coste: El coste depende del proveedor o la ruta. El modo API usa MuAPI; el modo local procesa medios en tu equipo pero conserva llamadas OpenAI o Gemini para ranking
- Equipo: Preparación según la ruta elegida. Python; FFmpeg y dependencias locales si eliges ese modo; clave LLM; video autorizado
**Repo:** https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator

**Instalación** [+]:

```
git clone https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator.git
   cd AI-Youtube-Shorts-Generator

pip install -r requirements.txt
   # Only if you plan to use --mode local:
   pip install -r requirements-local.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Obtener clips de un tutorial propio; Comparar criterios de selección de momentos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Procesa un video propio corto y revisa los fragmentos propuestos antes de exportar
**Qué comprobar:** Puedes corregir puntos de corte, subtítulos y encuadre
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `faster-whisper`, `yt-dlp`, `ffmpeg`

## `cap`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=grabar pantalla,edición de video,tutoriales,enlaces para compartir

**Qué es:** Graba pantalla, cámara y micrófono, edita el video en tu equipo con fondos, zoom y recortes, y expórtalo o compártelo con un enlace.
**Stack:** Rust, Cargo.toml, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El modo Studio graba y exporta en el equipo. El modo Instant, los enlaces compartidos y Cap AI usan la nube de Cap o un servidor propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Grabar y editar no necesita un modelo de IA. Las notas de la 0.6.3 describen una transcripción en el equipo con modelos que se descargan aparte; no se comprobó en el plan gratuito.
- Coste: Sin pago a un modelo en la ruta básica. Gratis para uso personal. La licencia de escritorio para uso comercial y Cap Pro, con nube, funciones de IA y enlaces ilimitados, son de pago según la página de precios consultada el 27 de noviembre de 2026.
- Equipo: Equipo normal; revisar dependencias. macOS 13.1 o posterior recomendado, Windows, o Linux con glibc 2.39 o posterior. Ubuntu 22.04 no está soportado.
**Repo:** https://github.com/CapSoftware/Cap

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/CapSoftware/Cap/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Grabar un tutorial corto sobre una hoja de cálculo propia y exportarlo en MP4; Mostrar a un compañero cómo aparece un fallo en tu propia aplicación con una grabación editada
**Evita si:** necesitas transmitir en directo con escenas y varias fuentes, o vas a grabar para un uso comercial sin pagar la licencia.
**Primera prueba propuesta:** En el modo Studio, sin iniciar sesión, graba 15 segundos de una ventana con un documento de prueba propio mientras dices una frase al micrófono
**Qué comprobar:** Al detener la grabación se abre el editor. Exporta a MP4, abre el archivo en tu reproductor y comprueba que se ve la ventana y se oye la frase
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `lossless-cut`, `handbrake`
**Alternativas (elige una):** `obs-studio`

## `concat`
role=app · exec=local · setup=medium · mcp=True · prov=— · tags=edicion,app,rust

**Qué es:** Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP.
**Stack:** Distribución compatible; clip propio; modelos opcionales descargados; permisos de automatización para MCP
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La edición y modelos locales no necesitan API; AGPL y licencia comercial para ciertos usos cerrados tienen condiciones distintas
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Está en beta; MCP puede usar la ventana o un proceso separado y sus modos tienen límites distintos al editar el mismo proyecto
- Coste: El coste depende del proveedor o la ruta. La edición y modelos locales no necesitan API; AGPL y licencia comercial para ciertos usos cerrados tienen condiciones distintas
- Equipo: Preparación según la ruta elegida. Distribución compatible; clip propio; modelos opcionales descargados; permisos de automatización para MCP
**Repo:** https://github.com/jub0t/Concat

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/jub0t/Concat/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Editar un video sin subir el material; Automatizar una variante de montaje mediante MCP
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Recorta una copia de un clip y añade subtítulos locales antes de exportar
**Qué comprobar:** Puedes revisar texto, puntos de corte y archivo final
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ffmpeg`, `yt-dlp`

## `davinci-resolve-mcp`
role=runtime · exec=local · setup=medium · mcp=True · prov=mcp · tags=video,mcp,agents,python

**Qué es:** Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render.
**Stack:** Resolve >=18.5; Python 64 bits; FFmpeg; Studio o puente interno para edición gratuita
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El conector no incluye un modelo; Studio tiene licencia propia y la edición gratuita necesita otra ruta; el agente mantiene sus límites
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Studio permite scripting externo Local; la edición gratuita usa un puente interno documentado; instalar MCP no activa por sí solo Resolve
- Coste: El coste depende del proveedor o la ruta. El conector no incluye un modelo; Studio tiene licencia propia y la edición gratuita necesita otra ruta; el agente mantiene sus límites
- Equipo: Preparación según la ruta elegida. Resolve >=18.5; Python 64 bits; FFmpeg; Studio o puente interno para edición gratuita
**Repo:** https://github.com/samuelgursky/davinci-resolve-mcp

**Instalación** [+]:

```
npx davinci-resolve-mcp setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar material desde un agente; Preparar ajustes de render con revisión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** En un proyecto de prueba consulta el media pool y añade un marcador antes de automatizar montaje
**Qué comprobar:** El marcador aparece en el clip o timeline esperado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ffmpeg`, `whisper`

## `ffmpeg`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,automation,cpp

**Qué es:** Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato.
**Stack:** Binario apropiado al sistema; archivo de video propio; espacio de salida
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa IA ni API; codecs y componentes del build pueden tener licencias distintas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Descarga un build para tu sistema o sigue la compilación; el repositorio GitHub es un espejo de la fuente oficial
- Coste: Sin pago a un modelo en la ruta básica. No usa IA ni API; codecs y componentes del build pueden tener licencias distintas
- Equipo: Preparación según la ruta elegida. Binario apropiado al sistema; archivo de video propio; espacio de salida
**Repo:** https://github.com/FFmpeg/FFmpeg

**Instalación** [?]:

```
Seguir la instalación original: https://ffmpeg.org/download.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un video para una plataforma; Extraer audio de una grabación propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte una copia de un video breve y comprueba duración, audio y formato con ffprobe
**Qué comprobar:** La salida se reproduce y conserva las pistas esperadas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `whisper`, `yt-dlp`, `moviepy`

## `handbrake`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,c,app

**Qué es:** Transcodificador de vídeo libre para Linux, macOS y Windows con interfaz gráfica, CLI, presets por dispositivo y colas de trabajo.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/HandBrake/HandBrake

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/HandBrake/HandBrake/blob/master/README.markdown
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: convertir grabaciones de cámara o pantalla a MP4 compatibles con móviles y webs; reducir el tamaño de una videoteca manteniendo la calidad
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala HandBrake, abre un vídeo corto y conviértelo con un preset de 1080p.
**Qué comprobar:** Obtienes un MP4 reproducible en el móvil con menor tamaño que el original.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `obs-studio`, `lossless-cut`, `jellyfin`

## `hunyuanvideo`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=video,inference,local,python

**Qué es:** Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia.
**Stack:** Python 3.10.9 y PyTorch según ruta; GPU grande; pesos y licencia
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API remota; hardware y almacenamiento son importantes y los pesos tienen licencia Hunyuan propia
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta original cita 45 GB VRAM para 544x960x129 y 60 GB para 720x1280x129; no es una instalación ligera para cualquier laptop
- Coste: El coste depende del proveedor o la ruta. No exige API remota; hardware y almacenamiento son importantes y los pesos tienen licencia Hunyuan propia
- Equipo: Preparación según la ruta elegida. Python 3.10.9 y PyTorch según ruta; GPU grande; pesos y licencia
**Repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo

**Instalación** [+]:

```
docker pull hunyuanvideo/hunyuanvideo:cuda_12
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Comprueba la resolución y memoria de la tabla antes de generar el ejemplo más pequeño viable
**Qué comprobar:** El clip y sus recursos se pueden comparar con la configuración elegida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `diffusers`, `comfyui`, `wan2gp`
**Alternativas (elige una):** `wan2-2`, `hunyuanvideo-1-5`

## `hunyuanvideo-1-5`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=local · tags=video,inference,local,python

**Qué es:** Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más.
**Stack:** Python, requirements.txt
**Acceso y costes:**
- API de IA: API de IA opcional. La reescritura de prompts usa un endpoint vLLM opcional; si no se configura, el pipeline genera sin reescritura remota.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Inferencia local con pesos descargados de Hugging Face, sujeta a la Tencent Hunyuan Community License.
- Coste: El coste depende del proveedor o la ruta. Sin pago por llamada en la ruta local; consume GPU. La licencia excluye la UE, el Reino Unido y Corea del Sur.
- Equipo: GPU o infraestructura especializada. GPU NVIDIA con CUDA y al menos 14 GB de VRAM con offloading; Linux y Python 3.10 o superior.
**Repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5

**Instalación** [+]:

```
git clone https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Generar un clip corto desde texto con GPU de consumo; Animar una imagen fija en 480p
**Evita si:** no tienes una GPU NVIDIA con memoria suficiente o te afecta la exclusión territorial de la licencia
**Primera prueba propuesta:** Genera un clip de pocos segundos en 480p con offloading activado
**Qué comprobar:** El video se guarda y anotas tiempo y VRAM usados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`, `wan2gp`, `vllm`
**Alternativas (elige una):** `hunyuanvideo`, `wan2-2`

## `kdenlive`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,cpp,app,edicion

**Qué es:** Editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/KDE/kdenlive

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/KDE/kdenlive/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: montar vídeos con varias pistas, efectos y corrección de color; subtitular automáticamente entrevistas o tutoriales
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala Kdenlive desde kdenlive.org, crea un proyecto, añade clips a la línea de tiempo y renderiza un MP4.
**Qué comprobar:** El render termina y el archivo reproduce el montaje.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `whisper`, `obs-studio`
**Alternativas (elige una):** `shotcut`, `opencut`

## `libass`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=subtítulos,ass,ssa,renderizado,c

**Qué es:** Dibuja subtítulos ASS y SSA con estilos, posiciones y tiempos en programas de video, bibliotecas multimedia y reproductores compatibles.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El programa lee subtítulos locales y escribe un PNG.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Dibuja texto por reglas de tipografía y estilos. Funciona sin un modelo de IA.
- Coste: Sin pago a un modelo en la ruta básica. Biblioteca ISC, sin pago obligatorio para compilar o ejecutar el ejemplo local.
- Equipo: Equipo normal; revisar dependencias. Equipo de uso general con Linux y herramientas de compilación. Para generar el PNG necesitas libpng y fuentes disponibles para el texto.
**Repo:** https://github.com/libass/libass

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/libass/libass/releases/tag/0.17.5
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Necesitas dibujar subtítulos ASS o SSA con estilos y posiciones desde una biblioteca o una integración.
**Evita si:** Prefieres editar o sincronizar subtítulos desde una interfaz gráfica.
**Primera prueba propuesta:** En una compilación Autotools con el programa de prueba habilitado, ejecuta ./test/test subtitulo.png muestra.ass 1.0 con una línea ASS propia activa durante el segundo 1
**Qué comprobar:** Abre subtitulo.png. La imagen muestra el texto con el estilo del archivo y la línea original se conserva
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `pysubs2`

## `lossless-cut`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,ui,typescript

**Qué es:** App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad.
**Stack:** Distribución para tu sistema; archivo compatible; espacio de salida
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Los ejecutables manuales se ofrecen gratis; tiendas pueden cobrar para apoyar el proyecto; no usa modelo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Los cortes sin recodificar dependen de fotogramas clave y del contenedor; no prometas precisión idéntica a un render completo
- Coste: El coste depende del proveedor o la ruta. Los ejecutables manuales se ofrecen gratis; tiendas pueden cobrar para apoyar el proyecto; no usa modelo
- Equipo: Preparación según la ruta elegida. Distribución para tu sistema; archivo compatible; espacio de salida
**Repo:** https://github.com/mifi/lossless-cut

**Instalación** [?]:

```
Seguir la instalación original: https://losslesscut.app/docs/getting-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Quitar una parte de una grabación; Separar o unir medios compatibles
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Marca dos puntos de un video propio y exporta el segmento sin recodificar
**Qué comprobar:** Compruebas duración, comienzo, final y pistas del clip
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `yt-dlp`, `whisperx`, `moviepy`, `obs-studio`, `opencut`

## `ltx-2`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=video,python,model,local

**Qué es:** Código oficial de inferencia y entrenamiento LoRA de LTX-2 y LTX-2.5, modelo DiT de Lightricks que genera vídeo con audio sincronizado.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/Lightricks/LTX-2

**Instalación** [+]:

```
git clone https://github.com/Lightricks/LTX-2.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: generar clips cortos con audio a partir de texto o una imagen en una GPU propia; entrenar un LoRA de estilo o personaje para el modelo
**Evita si:** no tienes el hardware o no aceptas la licencia de los pesos
**Primera prueba propuesta:** Clona el repositorio, instala las dependencias, descarga los pesos de LTX-2.5 y ejecuta la DistilledPipeline con un prompt corto.
**Qué comprobar:** Se genera un clip de vídeo con audio en la carpeta de salida sin agotar la VRAM.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`, `ffmpeg`, `pytorch`

## `moneyprinterturbo`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google,local · tags=video,automation,tts,python

**Qué es:** App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso.
**Stack:** Python; FFmpeg; proveedores de guion, voz e imágenes; material propio o autorizado
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Guion, voz, stock e imagen pueden consumir servicios distintos; ofrece imagen SDXL local y una ruta Codex/ChatGPT sujeta a elegibilidad y límites de cuenta
- Claude Code: Integración no documentada
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El adaptador Codex es del proyecto y no instala el CLI ni promete cobertura de cualquier modelo o cuenta; la imagen local no vuelve local todo el flujo
- Coste: El coste depende del proveedor o la ruta. Guion, voz, stock e imagen pueden consumir servicios distintos; ofrece imagen SDXL local y una ruta Codex/ChatGPT sujeta a elegibilidad y límites de cuenta
- Equipo: Preparación según la ruta elegida. Python; FFmpeg; proveedores de guion, voz e imágenes; material propio o autorizado
**Repo:** https://github.com/harry0703/MoneyPrinterTurbo

**Instalación** [+]:

```
python -m pip install mpt
mpt webui
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un borrador de video de producto; Generar variantes de un tutorial propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un video corto de prueba con un guion revisado y comprueba voz, clips y subtítulos
**Qué comprobar:** Puedes rastrear el origen de cada recurso y corregir el resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `faster-whisper`, `kokoro`, `ollama`
**Alternativas (elige una):** `openmontage`, `videofy-minimal`, `short-video-factory`

## `obs-studio`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,ui,cpp

**Qué es:** App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real.
**Stack:** Instalador oficial; permisos de captura; micrófono opcional; disco
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa un modelo ni necesita API de IA; streaming, almacenamiento y equipos son costes externos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Prueba el archivo antes de una sesión larga; seleccionar una fuente no acredita que capture el audio deseado
- Coste: Sin pago a un modelo en la ruta básica. No usa un modelo ni necesita API de IA; streaming, almacenamiento y equipos son costes externos
- Equipo: Preparación según la ruta elegida. Instalador oficial; permisos de captura; micrófono opcional; disco
**Repo:** https://github.com/obsproject/obs-studio

**Instalación** [?]:

```
Seguir la instalación original: https://obsproject.com/download
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Grabar una explicación de pantalla; Preparar escenas para una transmisión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una escena con pantalla y micrófono y graba veinte segundos
**Qué comprobar:** El archivo tiene imagen, audio y niveles aceptables
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `lossless-cut`, `opencut`, `faster-whisper`, `rnnoise`, `deep-live-cam`, `rvc`
**Alternativas (elige una):** `cap`

## `opencut`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=video,ui,typescript,rust

**Qué es:** Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe.
**Stack:** Navegador para versión clásica o herramientas de la nueva rama; clip de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La edición básica no exige IA; hosting y recursos propios son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El proyecto se reescribe; la versión clásica web y la rama principal no tienen necesariamente las mismas funciones ni instalación
- Coste: Sin pago a un modelo en la ruta básica. La edición básica no exige IA; hosting y recursos propios son independientes
- Equipo: Preparación según la ruta elegida. Navegador para versión clásica o herramientas de la nueva rama; clip de prueba
**Repo:** https://github.com/OpenCut-app/OpenCut

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/OpenCut-app/OpenCut/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar una alternativa de edición abierta; Estudiar la arquitectura de un editor con plugins
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba un corte corto en la versión disponible y revisa qué funciones pertenecen a la reescritura
**Qué comprobar:** Puedes exportar o identificar con claridad qué parte aún no está disponible
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `lossless-cut`, `obs-studio`, `whisperx`
**Alternativas (elige una):** `shotcut`, `kdenlive`

## `openrv`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=edicion,app,c

**Qué es:** Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual.
**Stack:** Build compatible o herramientas de compilación; secuencia o video de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo ni API; compilación, almacenamiento y componentes de terceros tienen requisitos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una herramienta de revisión y reproducción, no un generador de escenas ni un editor de montaje completo
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo ni API; compilación, almacenamiento y componentes de terceros tienen requisitos propios
- Equipo: Preparación según la ruta elegida. Build compatible o herramientas de compilación; secuencia o video de prueba
**Repo:** https://github.com/AcademySoftwareFoundation/OpenRV

**Instalación** [+]:

```
git clone --recursive https://github.com/AcademySoftwareFoundation/OpenRV.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar una entrega de animación; Comparar versiones de un efecto visual
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre dos versiones de una toma y compara fotogramas en el mismo punto
**Qué comprobar:** Puedes observar diferencias de imagen sin desalinear el tiempo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender`, `ffmpeg`, `comfyui`

## `pysubs2`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=subtítulos,srt,webvtt,python

**Qué es:** Convierte formatos de subtítulos y ajusta sus tiempos en lote desde Python o la terminal, sin cambiar el video ni usar una API de IA.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Carga y transformación de archivos de subtítulos en Python.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La ruta básica procesa los datos en tu equipo sin un modelo.
- Coste: Sin pago a un modelo en la ruta básica. Código MIT. La tarea de ejemplo se ejecuta con herramientas gratuitas en tu equipo.
- Equipo: Equipo normal; revisar dependencias. Python 3.12 o posterior. La distribución comprobada declara cero dependencias de ejecución.
**Repo:** https://github.com/tkarabela/pysubs2

**Instalación** [+]:

```
pip install pysubs2
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un archivo ASS de edición a SRT para compartirlo con un reproductor.; Corregir un desfase constante de los subtítulos en varios clips propios.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Convierte una copia de un ASS de dos líneas a SRT siguiendo el ejemplo del README fijado.
**Qué comprobar:** Abre el SRT y comprueba que conserva las dos líneas y sus tiempos.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `short-video-factory`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=generativo,ai,automatic,automation,clipping,cross-platform,desktop,linux

**Qué es:** Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos.
**Stack:** App de escritorio; proveedores de guion y voz; clips e imágenes propios
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La app integra varios servicios; modelos, voces y recursos pueden tener créditos o suscripción propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma aquí una ruta completamente local ni que la suscripción de un agente pague las funciones de generación
- Coste: El coste depende del proveedor o la ruta. La app integra varios servicios; modelos, voces y recursos pueden tener créditos o suscripción propios
- Equipo: Preparación según la ruta elegida. App de escritorio; proveedores de guion y voz; clips e imágenes propios
**Repo:** https://github.com/YILS-LIN/short-video-factory

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/YILS-LIN/short-video-factory/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un borrador de producto; Preparar variantes de un anuncio propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Monta un borrador corto con un texto y tres clips ficticios o propios y revisa cada escena
**Qué comprobar:** El video exportado coincide con guion, voz y subtítulos corregidos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `edge-tts`, `ffmpeg`, `ollama`
**Alternativas (elige una):** `moneyprinterturbo`

## `shotcut`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,cpp,app,edicion

**Qué es:** Editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/mltframework/shotcut

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/mltframework/shotcut/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: editar vídeos de YouTube o cursos con cortes, transiciones y títulos; generar subtítulos automáticos a partir del audio de un vídeo
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala Shotcut desde shotcut.org, importa dos clips, córtalos en la línea de tiempo y exporta un MP4.
**Qué comprobar:** El MP4 exportado reproduce los dos clips con el corte aplicado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `whisper-cpp`, `obs-studio`
**Alternativas (elige una):** `kdenlive`, `opencut`

## `videolingo`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai · tags=video,stt,tts,python

**Qué es:** Combina reconocimiento de voz, alineación, traducción, segmentación y doblaje. La ruta revisada utiliza Qwen3-ASR y ForcedAligner localmente por defecto; traducción y TTS tienen requisitos y costes distintos según proveedor.
**Stack:** Python y uv; FFmpeg y modelos según ruta; LLM con salida JSON; video propio
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. ASR local y algunos TTS no requieren API; traducción y servicios de voz dependen del proveedor; cada etapa puede consumir por separado
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El reconocimiento local actual usa Qwen3-ASR y ForcedAligner por defecto; no se debe seguir describiendo todo el pipeline como WhisperX
- Coste: El coste depende del proveedor o la ruta. ASR local y algunos TTS no requieren API; traducción y servicios de voz dependen del proveedor; cada etapa puede consumir por separado
- Equipo: Preparación según la ruta elegida. Python y uv; FFmpeg y modelos según ruta; LLM con salida JSON; video propio
**Repo:** https://github.com/Huanshere/VideoLingo

**Instalación** [+]:

```
git clone https://github.com/Huanshere/VideoLingo.git && cd VideoLingo
uv run start.py
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Subtitular un tutorial propio; Preparar una traducción de una demostración
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Procesa un clip corto con voz clara y revisa transcripción, traducción y tiempos antes de doblar
**Qué comprobar:** Los subtítulos coinciden con las palabras y puedes corregir errores antes de exportar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `yt-dlp`, `gpt-sovits`, `ffmpeg`
**Alternativas (elige una):** `omnivoice-studio`

## `wan2-2`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=video,inference,local,python

**Qué es:** Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0.
**Stack:** Python y PyTorch >=2.4; GPU; pesos y disco según variante
**Acceso y costes:**
- API de IA: API de IA opcional. Inferencia local usa hardware; expansión de prompts puede llamar DashScope; pesos y descargas tienen licencias propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El ejemplo 5B cita al menos 24 GB VRAM; otros ejemplos 14B citan 80 GB; no extrapoles esos mínimos a interfaces optimizadas de terceros
- Coste: El coste depende del proveedor o la ruta. Inferencia local usa hardware; expansión de prompts puede llamar DashScope; pesos y descargas tienen licencias propias
- Equipo: Preparación según la ruta elegida. Python y PyTorch >=2.4; GPU; pesos y disco según variante
**Repo:** https://github.com/Wan-Video/Wan2.2

**Instalación** [+]:

```
git clone https://github.com/Wan-Video/Wan2.2.git
cd Wan2.2

# Ensure torch >= 2.4.0
# If the installation of `flash_attn` fails, try installing the other packages first and install `flash_attn` last
pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una escena desde texto; Animar una imagen propia con un modelo local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige primero el modelo TI2V-5B y la ruta de memoria documentada y genera un clip breve
**Qué comprobar:** Puedes identificar pesos, tamaño, duración y recursos de la ejecución
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`, `diffusers`, `cosyvoice`, `real-esrgan`, `wan2gp`
**Alternativas (elige una):** `hunyuanvideo`, `hunyuanvideo-1-5`

## `wan2gp`
role=app · exec=local · setup=heavy · mcp=True · prov=local,mcp · tags=video,image,tts,local,python

**Qué es:** App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas.
**Stack:** GPU compatible; Python y PyTorch según guía; pesos del modelo elegido
**Acceso y costes:**
- API de IA: API de IA opcional. La app se ofrece sin cuota local; proveedores remotos de Deepy, modelos y recursos de búsqueda pueden costar
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Documenta Claude Code y Codex como proveedores remotos auxiliares; que algunos modelos quepan en 4 GB no garantiza que todos lo hagan
- Coste: El coste depende del proveedor o la ruta. La app se ofrece sin cuota local; proveedores remotos de Deepy, modelos y recursos de búsqueda pueden costar
- Equipo: Preparación según la ruta elegida. GPU compatible; Python y PyTorch según guía; pesos del modelo elegido
**Repo:** https://github.com/deepbeepmeep/WanGP

**Instalación** [+]:

```
git clone https://github.com/deepbeepmeep/WanGP.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar varios modelos desde una interfaz; Preparar clips locales con una GPU limitada
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige un modelo pequeño admitido y genera un clip corto antes de activar Deepy o Showrunner
**Qué comprobar:** Puedes comprobar memoria, duración y motor de cada tarea
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `wan2-2`, `moviepy`, `lossless-cut`, `hunyuanvideo-1-5`, `hunyuanvideo`
**Alternativas (elige una):** `comfyui`
