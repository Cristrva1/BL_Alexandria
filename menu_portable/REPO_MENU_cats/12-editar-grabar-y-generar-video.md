# 12. Editar, grabar y generar video — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ai-youtube-shorts-generator`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=generativo,2short-ai-alternative,ai-clip-generator,ai-clipping,auto-clip,auto-crop,highlight-detection,klap-alternative

**Qué es:** Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM. Transcribe, puntúa segmentos y recorta el video a formato vertical para producir clips cortos.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator

**Instalación** [?]: `Seguir la instalación original: https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres convertir videos largos en una primera selección de shorts
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa
**Combina con:** `ffmpeg`

## `concat`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=edicion,app,rust

**Qué es:** Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP.
**Stack:** Rust
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/jub0t/Concat

**Instalación** [?]: `Seguir la instalación original: https://github.com/jub0t/Concat/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `davinci-resolve-mcp`
role=runtime · exec=local · setup=medium · mcp=True · prov=mcp · tags=video,mcp,agents,python

**Qué es:** Expone la API oficial de scripting de DaVinci Resolve como herramientas MCP para Claude, Cursor, Codex y otros clientes. Cubre montaje, organización del media pool, render, marcadores, color, Fusion y Fairlight, y añade análisis de medios que nunca modifica los originales. Incluye un panel de control local en el navegador.
**Stack:** Python, Node.js, DaVinci Resolve Scripting API, ffmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: Consumo del agente que ya utilizas. Necesita DaVinci Resolve instalado y su API de scripting; algunas funciones dependen de la edición de Resolve.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/samuelgursky/davinci-resolve-mcp

**Instalación** [?]: `Seguir la instalación original: https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** editas en DaVinci Resolve y quieres que un agente MCP automatice montaje, render o metadatos
**Evita si:** no usas Resolve o prefieres montar video por código sin editor; mira `moviepy` o `ffmpeg`
**Combina con:** `claude-code`, `ffmpeg`, `whisper`

## `ffmpeg`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,automation,cpp

**Qué es:** FFmpeg es la base multimedia sobre la que se apoyan casi todos los editores, reproductores y pipelines de video. Incluye el CLI `ffmpeg` para convertir, recortar, concatenar, mezclar, quemar subtítulos y transmitir, `ffprobe` para inspeccionar archivos y las librerías libav* para integrarlo en tu propio software.
**Stack:** C, ensamblador (x86/ARM), libavcodec, libavformat, libavfilter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/FFmpeg/FFmpeg

**Instalación** [?]: `Seguir la instalación original: https://github.com/FFmpeg/FFmpeg/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas convertir, cortar, mezclar o transmitir audio y video desde la línea de comandos o un script
**Evita si:** quieres una interfaz gráfica para cortar sin pérdida (`lossless-cut`) o componer video desde Python con objetos (`moviepy`)
**Combina con:** `whisper`, `yt-dlp`, `moviepy`

## `hunyuanvideo`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=video,inference,local,python

**Qué es:** HunyuanVideo publica los pesos, la definición en PyTorch y el código de inferencia de un modelo de texto a video de más de 13.000 millones de parámetros, que genera clips de unos 5 segundos (129 fotogramas) en 540p o 720p. Las variantes de imagen a video, avatares guiados por audio y personalización viven en repos aparte.
**Stack:** Python, PyTorch, Diffusers, FlashAttention, xDiT
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo

**Instalación** [?]: `Seguir la instalación original: https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad
**Evita si:** trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente
**Combina con:** `comfyui`, `diffusers`, `real-esrgan`
**Alternativas (elige una):** `wan2-2`, `ltx-video`

## `hypit`
role=skill · exec=local · setup=medium · mcp=False · prov=local · tags=generativo,skill,typescript

**Qué es:** Skills para agentes que organizan generación y edición de videos mediante modelos, servicios y recursos configurables.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: API de IA opcional. Las instrucciones se usan en el agente. El README permite configurar la generación con HypiHub, APIs propias o modelos locales; cada ruta se prepara aparte.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. El autor menciona modelos locales como una ruta de generación. Confirma la compatibilidad de cada etapa y los recursos necesarios.
- Coste: El coste depende del proveedor o la ruta. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/hypit-ai/hypit

**Instalación** [+]: `npx skills add hypit-ai/hypit -g`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Skills para agentes que organizan generación y edición de videos mediante modelos, servicios y recursos configurables.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `lossless-cut`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,ui,typescript

**Qué es:** LosslessCut es una interfaz gráfica sobre FFmpeg para recortar y fusionar archivos de video y audio sin recompresión. Sirve para descartar gigas de material de cámara, GoPro o dron, extraer o reemplazar pistas, cambiar de contenedor (MKV a MP4) y editar metadatos o capítulos, en Windows, macOS y Linux.
**Stack:** TypeScript, Electron, React, FFmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mifi/lossless-cut

**Instalación** [?]: `Seguir la instalación original: https://github.com/mifi/lossless-cut/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica
**Evita si:** necesitas efectos, transiciones o un montaje con capas; mira `opencut` o, por código, `moviepy`
**Combina con:** `yt-dlp`, `whisperx`, `moviepy`

## `ltx-video`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=video,inference,local,python

**Qué es:** LTX-Video es el repositorio de los modelos v0.9.x de Lightricks, un transformer de difusión (DiT) para texto a video, imagen a video, extensión de clips y video a video con condiciones por fotograma clave. Incluye variantes de 2B y 13B, destiladas y FP8, y LoRAs de control de pose, profundidad y bordes. Ya solo se mantiene como legado: los modelos nuevos están en LTX-2.
**Stack:** Python, PyTorch, Diffusers, ComfyUI
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Lightricks/LTX-Video

**Instalación** [?]: `Seguir la instalación original: https://github.com/Lightricks/LTX-Video/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x
**Evita si:** empiezas un proyecto nuevo; Lightricks recomienda LTX-2.5 (repo Lightricks/LTX-2), o mira `wan2-2` y `wan2gp`
**Combina con:** `comfyui`, `diffusers`, `real-esrgan`
**Alternativas (elige una):** `wan2-2`, `hunyuanvideo`

## `mediabunny`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=edicion,library,typescript

**Qué es:** Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Vanilagy/mediabunny

**Instalación** [+]: `npm install mediabunny`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `moneyprinterturbo`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google,local · tags=video,automation,tts,python

**Qué es:** MoneyPrinterTurbo automatiza la producción de shorts: das un tema o palabras clave y escribe el guion con un LLM, busca clips en Pexels o Pixabay (o usa los tuyos o video generado por IA), genera locución, subtítulos y música, y monta el resultado en 9:16, 16:9 o 1:1. Se usa desde WebUI, API, CLI o pidiéndoselo a un agente con su skill.
**Stack:** Python, Streamlit, FastAPI, MoviePy, faster-whisper
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/harry0703/MoneyPrinterTurbo

**Instalación** [?]: `Seguir la instalación original: https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres producir videos cortos narrados a partir de un tema sin editar a mano
**Evita si:** necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage`
**Combina con:** `ollama`, `kokoro`, `faster-whisper`
**Alternativas (elige una):** `openmontage`, `videofy-minimal`

## `moviepy`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,automation,python

**Qué es:** MoviePy convierte la edición de video en código Python: abres clips, los recortas, superpones texto o imágenes, mezclas audio y exportas a MP4, WebM o GIF. Es la pieza de ensamblaje habitual en pipelines que generan videos cortos a partir de imágenes, voz sintética y subtítulos.
**Stack:** Python, NumPy, Pillow, FFmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Zulko/moviepy

**Instalación** [+]: `pip install moviepy`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** ensamblas video desde Python y quieres controlar cada clip por código
**Evita si:** prefieres plantillas en React (`remotion`) o en HTML (`hyperframes`), o solo necesitas cortar sin recodificar (`lossless-cut`)
**Combina con:** `whisperx`, `kokoro`, `comfyui`
**Alternativas (elige una):** `remotion`, `hyperframes`

## `obs-studio`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,audio,ui,cpp

**Qué es:** OBS Studio captura, compone, codifica, graba y transmite video en Windows, macOS y Linux. Combinas en escenas la pantalla, ventanas, webcam, navegador y archivos multimedia, mezclas el audio con filtros y emites a YouTube, Twitch u otro servicio RTMP, o grabas a disco.
**Stack:** C, C++, Qt, FFmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/obsproject/obs-studio

**Instalación** [?]: `Seguir la instalación original: https://github.com/obsproject/obs-studio/blob/master/README.rst`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas
**Evita si:** lo que necesitas es montar o recortar el video ya grabado; usa `opencut` o `lossless-cut`
**Combina con:** `lossless-cut`, `opencut`, `faster-whisper`
**Alternativas (elige una):** `openscreen`

## `opencut`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=video,ui,typescript,rust

**Qué es:** Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. El README diferencia opencut.app y opencut-classic de la reescritura en curso; comprueba qué versión necesitas antes de compilar.
**Stack:** TypeScript, Rust, WebAssembly, Next.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/OpenCut-app/OpenCut

**Instalación** [?]: `Seguir la instalación original: https://github.com/OpenCut-app/OpenCut/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut
**Evita si:** necesitas estabilidad o automatización hoy; para montar por código mira `moviepy` o `remotion`, y para cortes sin pérdida `lossless-cut`
**Combina con:** `lossless-cut`, `obs-studio`, `whisperx`

## `openrv`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=edicion,app,c

**Qué es:** Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/AcademySoftwareFoundation/OpenRV

**Instalación** [?]: `Seguir la instalación original: https://github.com/AcademySoftwareFoundation/OpenRV/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `openscreen`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,ui,typescript

**Qué es:** OpenScreen graba una ventana o la pantalla completa con micrófono y audio del sistema, y después te deja pulir la demo: zooms que siguen al cursor, webcam superpuesta, fondos, anotaciones, recorte y velocidad por tramo. Exporta a MP4 o GIF en varias proporciones. El proyecto original está archivado; su continuación activa es getopenscreen/openscreen.
**Stack:** TypeScript, Electron, PixiJS
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/siddharthvaddem/openscreen

**Instalación** [?]: `Seguir la instalación original: https://github.com/siddharthvaddem/openscreen/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio
**Evita si:** necesitas un proyecto mantenido; usa su continuación getopenscreen/openscreen, o `obs-studio` para grabación y streaming generales
**Combina con:** `lossless-cut`, `opencut`
**Alternativas (elige una):** `obs-studio`

## `palmier-pro`
role=app · exec=local · setup=medium · mcp=True · prov=— · tags=edicion,ai-video,claude,macos,mcp,seedance2,swift,video-editor

**Qué es:** Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios actuales. Permite trabajar con una línea de tiempo y enlazar agentes mediante MCP en las versiones que lo incorporan.
**Stack:** Swift
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Las versiones actuales distribuyen binarios propietarios; el código abierto conservado es histórico. Las funciones de IA pueden tener servicios adicionales.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/palmier-io/palmier-pro

**Instalación** [?]: `Seguir la instalación original: https://github.com/palmier-io/palmier-pro/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas macOS y quieres explorar edición de video asistida por agentes
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa

## `pencil`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=edicion,app,c

**Qué es:** Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/pencil2d/pencil

**Instalación** [?]: `Seguir la instalación original: https://github.com/pencil2d/pencil/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `short-video-factory`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=generativo,ai,automatic,automation,clipping,cross-platform,desktop,linux

**Qué es:** Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. Encadena generación de texto y voz con montaje automático en una interfaz de escritorio.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/YILS-LIN/short-video-factory

**Instalación** [?]: `Seguir la instalación original: https://github.com/YILS-LIN/short-video-factory/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres producir variantes de videos promocionales desde materiales existentes
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa

## `videolingo`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai · tags=video,stt,tts,python

**Qué es:** VideoLingo reúne en una interfaz Streamlit el trabajo de un equipo de subtitulado: descarga el video con yt-dlp, lo transcribe con alineación por palabra, segmenta y traduce los subtítulos con un LLM y, si quieres, genera el doblaje con voz sintética o clonada. Produce archivos SRT y videos subtitulados o doblados.
**Stack:** Python, Streamlit, Qwen3-ASR, yt-dlp, FFmpeg
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/Huanshere/VideoLingo

**Instalación** [?]: `Seguir la instalación original: https://github.com/Huanshere/VideoLingo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar
**Evita si:** solo necesitas transcribir o subtitular en el idioma original; te basta `whisperx` o `faster-whisper`
**Combina con:** `yt-dlp`, `gpt-sovits`, `whisperx`
**Alternativas (elige una):** `omnivoice-studio`

## `wan2-2`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=video,inference,local,python

**Qué es:** Wan2.2 publica pesos y código de inferencia de varios modelos de video: texto a video e imagen a video de 14B (MoE), un modelo híbrido de 5B que genera 720p a 24 fps en una RTX 4090, video guiado por voz (S2V) y animación o sustitución de personajes (Animate). Es la base de muchos flujos de ComfyUI y Diffusers.
**Stack:** Python, PyTorch, FlashAttention, Diffusers
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Wan-Video/Wan2.2

**Instalación** [?]: `Seguir la instalación original: https://github.com/Wan-Video/Wan2.2/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más
**Evita si:** tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados
**Combina con:** `comfyui`, `diffusers`, `real-esrgan`, `cosyvoice`
**Alternativas (elige una):** `hunyuanvideo`, `ltx-video`

## `wan2gp`
role=app · exec=local · setup=heavy · mcp=True · prov=local,mcp · tags=video,image,tts,local,python

**Qué es:** WanGP, antes Wan2GP, es una interfaz web para ejecutar en tu GPU decenas de modelos generativos abiertos: video (Wan 2.1/2.2, LTX-2, Hunyuan Video), imagen (Flux, Qwen Image), voz y música (Chatterbox, Index TTS, Ace Step) y 3D. Añade cola de trabajos, LoRAs, galerías y un asistente local, Deepy, que planifica y lanza las generaciones por ti.
**Stack:** Python, PyTorch, Gradio, Diffusers, mmgp
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/deepbeepmeep/WanGP

**Instalación** [?]: `Seguir la instalación original: https://github.com/deepbeepmeep/WanGP/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano
**Evita si:** prefieres construir flujos por nodos con control fino (`comfyui`) o tienes una GPU grande y quieres el código oficial (`wan2-2`)
**Combina con:** `claude-code`, `moviepy`, `lossless-cut`
**Alternativas (elige una):** `comfyui`
