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

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Comprueba la resolución y memoria de la tabla antes de generar el ejemplo más pequeño viable
**Qué comprobar:** El clip y sus recursos se pueden comparar con la configuración elegida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `diffusers`, `comfyui`, `wan2gp`
**Alternativas (elige una):** `wan2-2`

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
**Combina con:** `ffmpeg`, `yt-dlp`, `whisperx`, `moviepy`

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
**Alternativas (elige una):** `openmontage`, `videofy-minimal`

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
**Combina con:** `lossless-cut`, `opencut`, `faster-whisper`

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

**Instalación** [?]:

```
Seguir la instalación original: https://aswf-openrv.readthedocs.io/en/latest/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar una entrega de animación; Comparar versiones de un efecto visual
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre dos versiones de una toma y compara fotogramas en el mismo punto
**Qué comprobar:** Puedes observar diferencias de imagen sin desalinear el tiempo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender`, `ffmpeg`, `comfyui`

## `palmier-pro`
role=app · exec=local · setup=medium · mcp=True · prov=— · tags=edicion,ai-video,claude,macos,mcp,seedance2,swift,video-editor

**Qué es:** Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios actuales.
**Stack:** Apple Silicon; macOS 26; binario y licencia de su versión; cliente opcional
**Acceso y costes:**
- API de IA: API de IA opcional. Las versiones posteriores a 0.7.6 son binarias propietarias; agente y modelos tienen costes propios según ruta
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. El código GPL histórico no concede automáticamente la licencia de los binarios actuales; MCP local HTTP está documentado para Claude y Codex
- Coste: El coste depende del proveedor o la ruta. Las versiones posteriores a 0.7.6 son binarias propietarias; agente y modelos tienen costes propios según ruta
- Equipo: Preparación según la ruta elegida. Apple Silicon; macOS 26; binario y licencia de su versión; cliente opcional
**Repo:** https://github.com/palmier-io/palmier-pro

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/palmier-io/palmier-pro/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar cortes con un agente; Revisar una secuencia desde herramientas externas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una copia de un proyecto y consulta su timeline mediante MCP antes de editar
**Qué comprobar:** El agente identifica pistas y clips del proyecto correcto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `ffmpeg`

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
**Combina con:** `comfyui`, `diffusers`, `cosyvoice`, `real-esrgan`
**Alternativas (elige una):** `hunyuanvideo`

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

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/deepbeepmeep/Wan2GP/blob/main/docs/INSTALLATION.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar varios modelos desde una interfaz; Preparar clips locales con una GPU limitada
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige un modelo pequeño admitido y genera un clip corto antes de activar Deepy o Showrunner
**Qué comprobar:** Puedes comprobar memoria, duración y motor de cada tarea
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `wan2-2`, `moviepy`, `lossless-cut`
**Alternativas (elige una):** `comfyui`
