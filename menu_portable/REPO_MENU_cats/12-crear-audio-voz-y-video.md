# 12. Crear audio, voz y video — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ace-step-1.5`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=musica,text2music,python

**Qué es:** Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. Combina modelos de generación musical y una interfaz de inferencia para producir audio y personalizar estilos.
**Stack:** Python, Docker, pyproject.toml, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ace-step/ACE-Step-1.5

**Instalación** [?]: `Seguir la instalación original: https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas experimentar con generación musical en tu propio equipo
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa

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

## `audiocraft`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=audio,inference,training,python

**Qué es:** AudioCraft reúne el código de inferencia y entrenamiento de los modelos de audio generativo de Meta: MusicGen (música a partir de texto o melodía), AudioGen (efectos de sonido), MAGNeT, JASCO (música condicionada por acordes y batería), el códec neuronal EnCodec y AudioSeal para marcas de agua. Está orientada a investigación, aunque se usa mucho para crear música de fondo.
**Stack:** Python, PyTorch, EnCodec, Hugging Face Hub
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/facebookresearch/audiocraft

**Instalación** [?]: `Seguir la instalación original: https://github.com/facebookresearch/audiocraft/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio
**Evita si:** necesitas uso comercial (los pesos son CC-BY-NC 4.0) o generar voz hablada; para voz mira `kokoro` o `chatterbox`
**Combina con:** `moviepy`, `remotion`, `ffmpeg`

## `chatterbox`
role=library · exec=local · setup=easy · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Clona una voz con unos segundos de audio y ajusta la expresividad. Multilingüe y con marca de agua.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/resemble-ai/chatterbox

**Instalación** [+]: `pip install chatterbox-tts`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres clonar voces con calidad alta y licencia libre
**Evita si:** necesitas algo muy ligero en CPU; mira `kokoro`
**Combina con:** `pipecat`
**Alternativas (elige una):** `fish-speech`, `gpt-sovits`, `kokoro`, `luxtts`

## `cosyvoice`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Síntesis de voz natural con clonación y control de estilo, también en streaming.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/QwenAudio/CosyVoice

**Instalación** [?]: `Seguir la instalación original: https://github.com/QwenAudio/CosyVoice/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas TTS multilingüe en streaming
**Evita si:** quieres instalación muy simple; mira `kokoro`
**Combina con:** `pipecat`
**Alternativas (elige una):** `fish-speech`, `index-tts`

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

## `edge-tts`
role=library · exec=cloud · setup=easy · mcp=False · prov=— · tags=tts,speech-synthesis,text-to-speech,python

**Qué es:** Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. Envía texto al servicio de voz y guarda el audio y los subtítulos desde Python o la terminal.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta documentada usa un servicio en línea mediante sesión o acceso propio; no implica ejecución local del modelo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Usa un servicio de voz de Microsoft en línea. No pide una API key en su uso documentado, pero no funciona sin conexión ni garantiza disponibilidad futura.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/rany2/edge-tts

**Instalación** [+]: `pip install edge-tts`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres generar narración sin instalar un modelo de voz local
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa
**Combina con:** `moviepy`
**Alternativas (elige una):** `kokoro`

## `faster-whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. Puede reducir requisitos frente a otras implementaciones; mide calidad y rendimiento con tu propio audio.
**Stack:** Python, CTranslate2
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/SYSTRAN/faster-whisper

**Instalación** [+]: `pip install faster-whisper`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** el rendimiento, la memoria o el coste de GPU importan
**Evita si:** necesitas alineación/diarización (whisperX) o te basta el CLI oficial
**Combina con:** `whisperx`
**Alternativas (elige una):** `whisper-cpp`

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

## `fish-speech`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Clona voces con pocos segundos de audio y genera habla natural en muchos idiomas.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/fishaudio/fish-speech

**Instalación** [?]: `Seguir la instalación original: https://github.com/fishaudio/fish-speech/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas TTS de alta calidad con clonación
**Evita si:** necesitas licencia comercial sin restricciones; mira `chatterbox`
**Alternativas (elige una):** `chatterbox`, `cosyvoice`, `gpt-sovits`

## `gpt-sovits`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Entrena una voz con muy pocos datos y sintetiza en varios idiomas. Muy popular entre creadores.
**Stack:** Python, PyTorch, Gradio
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/RVC-Boss/GPT-SoVITS

**Instalación** [?]: `Seguir la instalación original: https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres entrenar una voz con pocos datos
**Evita si:** prefieres zero-shot sin entrenar; mira `chatterbox`
**Combina con:** `rvc`
**Alternativas (elige una):** `chatterbox`, `fish-speech`

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

## `hyperframes`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=video,agents,skills,typescript

**Qué es:** HyperFrames define cada video como un archivo HTML con atributos de tiempo y pistas, animado con GSAP, CSS, Lottie, Three.js u otras librerías, y lo renderiza a MP4. Incluye CLI para crear, previsualizar y renderizar, un catálogo de unos 450 bloques (transiciones, subtítulos, gráficos, mapas) y skills para que Claude Code, Codex o Cursor produzcan videos a partir de una petición.
**Stack:** TypeScript, Node.js, Puppeteer, FFmpeg, GSAP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/heygen-com/hyperframes

**Instalación** [+]: `npx hyperframes init my-video`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva
**Evita si:** tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual
**Combina con:** `claude-code`, `gsap`, `kokoro`, `whisperx`
**Alternativas (elige una):** `remotion`, `moviepy`

## `index-tts`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Clona voces sin entrenar y permite controlar la duración exacta, útil para doblaje.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/index-tts/index-tts

**Instalación** [?]: `Seguir la instalación original: https://github.com/index-tts/index-tts/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas controlar duración y emoción de la voz
**Evita si:** buscas licencia totalmente libre; revisa su licencia
**Alternativas (elige una):** `cosyvoice`

## `kokoro`
role=library · exec=local · setup=easy · mcp=False · prov=local · tags=tts,audio,local

**Qué es:** Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. Comprueba los idiomas, dependencias de audio y condiciones de la variante que utilices.
**Stack:** Python, PyTorch, JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/hexgrad/kokoro

**Instalación** [+]: `pip install kokoro`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres TTS ligero, rápido y con licencia permisiva
**Evita si:** necesitas clonar voces; mira `chatterbox`
**Combina con:** `pipecat`, `whisper-cpp`
**Alternativas (elige una):** `chatterbox`, `tts`, `luxtts`, `edge-tts`

## `livekit-agents`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google · tags=audio,agents,video,python

**Qué es:** Construye agentes que hablan, escuchan y ven, con detección de turnos y telefonía, desplegables a escala.
**Stack:** Python, Node.js, WebRTC
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/livekit/agents

**Instalación** [?]: `Seguir la instalación original: https://github.com/livekit/agents/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas agentes de voz escalables con WebRTC
**Evita si:** quieres algo ligero sin servidor de medios; mira `pipecat`
**Combina con:** `kokoro`
**Alternativas (elige una):** `pipecat`

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

## `luxtts`
role=library · exec=local · setup=easy · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. La velocidad y el consumo de memoria dependen de la variante y del hardware.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ysharma3501/LuxTTS

**Instalación** [?]: `Seguir la instalación original: https://github.com/ysharma3501/LuxTTS/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas TTS con clonación muy rápido
**Evita si:** buscas el proyecto más maduro; mira `chatterbox`
**Combina con:** `litellm`, `cosmos`, `comfyui`
**Alternativas (elige una):** `kokoro`, `chatterbox`

## `manim`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=video,dataviz,learning,python

**Qué es:** Manim permite describir en código Python escenas con fórmulas LaTeX, gráficas, geometría y transformaciones animadas, y exportarlas a video. Este repo es ManimGL, la versión original que Grant Sanderson usa en 3Blue1Brown; la edición comunitaria (ManimCommunity/manim) es un fork más estable y mejor documentado.
**Stack:** Python, OpenGL, FFmpeg, LaTeX
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/3b1b/manim

**Instalación** [+]: `pip install manimgl`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres animaciones matemáticas o técnicas precisas definidas en código Python
**Evita si:** buscas estabilidad y documentación para empezar (usa la edición comunitaria ManimCommunity/manim) o motion graphics de marketing; mira `remotion` o `hyperframes`
**Combina con:** `kokoro`, `moviepy`, `ffmpeg`
**Alternativas (elige una):** `manim-community`

## `manim-community`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=programatico,animations,hacktoberfest,manim,math,python

**Qué es:** Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. Define objetos geométricos y transformaciones en código y renderiza la escena como video.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ManimCommunity/manim

**Instalación** [?]: `Seguir la instalación original: https://github.com/ManimCommunity/manim/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas animaciones matemáticas precisas y reproducibles
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa
**Combina con:** `ffmpeg`
**Alternativas (elige una):** `manim`

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

## `music-megathread`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=musica

**Qué es:** Directorio de reproductores, herramientas, servicios y otros recursos relacionados con música. Agrupa enlaces a proyectos y servicios musicales para explorar alternativas por función.
**Stack:** Recursos y documentación
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/MoonWalker440/Music-Megathread

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas recursos musicales y quieres comparar opciones desde una lista
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa

## `nemo`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=stt,tts,audio,python

**Qué es:** Incluye modelos de ASR como Parakeet y Canary, que lideran rankings de transcripción, y herramientas para afinarlos.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA-NeMo/Speech

**Instalación** [?]: `Seguir la instalación original: https://github.com/NVIDIA-NeMo/Speech/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas ASR de máxima precisión y tienes GPU
**Evita si:** quieres algo simple; mira `faster-whisper`
**Combina con:** `pipecat`
**Alternativas (elige una):** `whisperx`

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

## `omnivoice-studio`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=tts,audio,python

**Qué es:** Reúne STT, TTS y dubbing en una sola app sin claves de API.
**Stack:** desktop/Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/debpalash/VoiceStudio

**Instalación** [?]: `Seguir la instalación original: https://github.com/debpalash/VoiceStudio/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres suite de voz completa local (dictado + clonación + dubbing)
**Evita si:** solo necesitas TTS simple por CLI/librería (TTS) o estabilidad de producción
**Combina con:** `whisperx`
**Alternativas (elige una):** `videolingo`

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

## `openmontage`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=video,coding-agent,skills

**Qué es:** Describes el video y el agente investiga, escribe el guion, genera recursos y monta el resultado.
**Stack:** Markdown, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/OpenMontageInc/OpenMontage

**Instalación** [?]: `Seguir la instalación original: https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres producir videos completos con un agente
**Evita si:** solo necesitas editar clips; mira `video-use`
**Combina con:** `remotion`
**Alternativas (elige una):** `remotion-superpowers`, `moneyprinterturbo`

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

## `pipecat`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google · tags=audio,agents,stt,tts,python

**Qué es:** Encadena STT, LLM y TTS con interrupciones y baja latencia, y conecta con teléfono, WebRTC o WhatsApp.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/pipecat-ai/pipecat

**Instalación** [+]: `pip install pipecat-ai`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** construyes un agente de voz en Python
**Evita si:** quieres infraestructura WebRTC gestionada; mira `livekit-agents`
**Combina con:** `kokoro`, `whisper-cpp`
**Alternativas (elige una):** `livekit-agents`

## `rea-video`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=— · tags=programatico,agent-skills,ai-video,aigc-detection,claude-code,codex,ffmpeg,prompt-engineering

**Qué es:** Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md. Clasifica planos y registra capas, ritmo y técnicas de producción en un formato legible por agentes.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/JuneYaooo/rea-video

**Instalación** [?]: `Seguir la instalación original: https://github.com/JuneYaooo/rea-video/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar o recrear la estructura de un video de referencia
**Evita si:** tu flujo audiovisual actual ya cubre esa etapa
**Combina con:** `remotion`

## `remotion`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=video,typescript

**Qué es:** Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. El render no requiere por sí solo una API de IA; revisa las condiciones de licencia del proyecto.
**Stack:** Node.js, React, Chromium, ffmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. El renderizado de React no requiere una API de IA. Revisar la licencia de Remotion para el tamaño del equipo y el uso comercial.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/remotion-dev/remotion

**Instalación** [+]: `npx create-video@latest`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** generas video a escala con React y quieres variantes parametrizadas
**Evita si:** trabajas en Python (moviepy) o buscas un editor visual
**Combina con:** `open-generative-ai`
**Alternativas (elige una):** `moviepy`, `hyperframes`

## `remotion-superpowers`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,skills,coding-agent

**Qué es:** Añade locución con IA, música, footage de stock e imágenes para producir videos en código.
**Stack:** Shell, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/DojoCodingLabs/remotion-superpowers

**Instalación** [?]: `Seguir la instalación original: https://github.com/DojoCodingLabs/remotion-superpowers/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Remotion con un agente y quieres producción completa
**Evita si:** no usas Remotion
**Combina con:** `remotion`, `skills-remotion`
**Alternativas (elige una):** `openmontage`, `video-use`

## `rvc`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=audio,tts,python

**Qué es:** Cambia la voz de una grabación manteniendo entonación. Muy usado para covers y doblaje.
**Stack:** Python, PyTorch, Gradio
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

**Instalación** [?]: `Seguir la instalación original: https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres convertir una voz grabada en otra
**Evita si:** necesitas generar voz desde texto; mira `chatterbox`
**Combina con:** `gpt-sovits`

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

## `skills-remotion`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,skills

**Qué es:** Enseñan al agente las buenas prácticas de Remotion: composiciones, animaciones, audio y render.
**Stack:** TypeScript, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/remotion-dev/skills

**Instalación** [+]: `npx skills add remotion-dev/skills`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** haces videos con Remotion y un agente
**Evita si:** no usas Remotion
**Combina con:** `remotion`, `remotion-superpowers`

## `supertonic`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=tts,audio

**Qué es:** Motor de texto a voz que ofrece modelos y ejemplos para sintetizar audio en dispositivos y navegadores compatibles. El soporte por idioma, dispositivo y variante debe comprobarse en la documentación actual.
**Stack:** Python, Rust (ONNX), Node.js, WebGPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/supertone-oss-archive/supertonic

**Instalación** [+]: `pip install supertonic`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres voz local en tiempo real y sin nube
**Evita si:** priorizas clonación de máxima fidelidad (VoxCPM) o flexibilidad multi-modelo (TTS)
**Combina con:** `whisperx`, `moviepy`

## `tts`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=tts,audio,python

**Qué es:** Reúne en una sola librería modelos como Tacotron, VITS y XTTS, con CLI y API Python.
**Stack:** Python, PyTorch, modelos descargables
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/coqui-ai/TTS

**Instalación** [+]: `pip install TTS`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres flexibilidad y varios modelos en una librería
**Evita si:** necesitas tiempo real puro (supertonic) o soporte comercial (Coqui está inactivo)
**Combina con:** `whisperx`, `moviepy`
**Alternativas (elige una):** `kokoro`

## `vibevoice`
role=library · exec=local · setup=heavy · mcp=False · prov=local · tags=tts,audio,python

**Qué es:** Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. Elige una variante concreta antes de asumir idiomas, duración, hardware o soporte de tiempo real.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/microsoft/VibeVoice

**Instalación** [?]: `Seguir la instalación original: https://github.com/microsoft/VibeVoice/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres generar podcasts o diálogos largos
**Evita si:** solo necesitas frases cortas; mira `kokoro`
**Combina con:** `open-notebook`

## `video-use`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=video,coding-agent,skills,python

**Qué es:** El agente corta, une, subtitula y ajusta videos a partir de instrucciones en lenguaje natural.
**Stack:** Python, ffmpeg
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/browser-use/video-use

**Instalación** [?]: `Seguir la instalación original: https://github.com/browser-use/video-use/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres editar videos pidiéndoselo a tu agente
**Evita si:** quieres una app de edición visual; mira `opencut`
**Combina con:** `ffmpeg`, `claude-code`
**Alternativas (elige una):** `remotion-superpowers`

## `videofy-minimal`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=video,typescript

**Qué es:** Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. La ruta documentada requiere APIs de OpenAI y ElevenLabs aunque la interfaz y el montaje se ejecuten en tu equipo.
**Stack:** Python/Node
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. El flujo documentado usa OPENAI_API_KEY y ELEVENLABS_API_KEY. La interfaz local no elimina esas llamadas remotas.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/schibsted/videofy_minimal

**Instalación** [?]: `Seguir la instalación original: https://github.com/schibsted/videofy_minimal/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres reels simples ya, sin montar un pipeline entero
**Evita si:** necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy)
**Combina con:** `whisper`, `supertonic`
**Alternativas (elige una):** `moneyprinterturbo`

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

## `voxcpm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=tts,audio,python

**Qué es:** Pertenece a la familia CPM de modelos generativos de OpenBMB.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/OpenBMB/VoxCPM

**Instalación** [+]: `pip install voxcpm`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres voz muy natural o clonada y tienes GPU
**Evita si:** priorizas latencia mínima (supertonic) o no tienes GPU
**Combina con:** `tts`

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

## `whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. El idioma, el tamaño del modelo y la calidad del audio condicionan el resultado.
**Stack:** Python 3.9+, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/openai/whisper

**Instalación** [+]: `pip install -U openai-whisper`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres la referencia robusta y no te obsesiona la latencia
**Evita si:** necesitas más velocidad (faster-whisper) o timings por palabra (whisperX)
**Combina con:** `whisperx`
**Alternativas (elige una):** `whisper-cpp`

## `whisper-cpp`
role=runtime · exec=local · setup=easy · mcp=False · prov=local · tags=stt,audio,local,cpp

**Qué es:** Transcribe voz a texto en local sin Python ni GPU obligatoria, incluso en tiempo real. Base de muchas apps de dictado.
**Stack:** C++, C
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ggml-org/whisper.cpp

**Instalación** [?]: `Seguir la instalación original: https://github.com/ggml-org/whisper.cpp/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres transcribir en local sin GPU
**Evita si:** necesitas marcas de tiempo por palabra y diarización; mira `whisperx`
**Combina con:** `ffmpeg`
**Alternativas (elige una):** `faster-whisper`, `whisper`

## `whisperx`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=stt,audio,python

**Qué es:** Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. Las etapas, modelos y credenciales requeridos cambian según las funciones que actives.
**Stack:** Python, faster-whisper, wav2vec2, pyannote
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/m-bain/whisperX

**Instalación** [+]: `pip install whisperx`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas subtítulos precisos o diarización
**Evita si:** te basta texto plano (whisper) o no quieres gestionar tokens de HF
**Combina con:** `whisper`, `moviepy`
**Alternativas (elige una):** `nemo`
