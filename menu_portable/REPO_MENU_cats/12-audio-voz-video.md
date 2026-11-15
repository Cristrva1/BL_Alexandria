# 12. Audio, Voz & Video — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `audiocraft`
role=library · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** AudioCraft reúne el código de inferencia y entrenamiento de los modelos de audio generativo de Meta: MusicGen (música a partir de texto o melodía), AudioGen (efectos de sonido), MAGNeT, JASCO (música condicionada por acordes y batería), el códec neuronal EnCodec y AudioSeal para marcas de agua. Está orientada a investigación, aunque se usa mucho para crear música de fondo.
**Stack:** Python, PyTorch, EnCodec, Hugging Face Hub
**Repo:** https://github.com/facebookresearch/audiocraft

**Instalación** [~]: `pip install audiocraft   (o: uv add audiocraft)`
_Nombre PyPI puede diferir de 'AudioCraft'; verifica en pypi.org._

**Elige si:** necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio
**Evita si:** necesitas uso comercial (los pesos son CC-BY-NC 4.0) o generar voz hablada; para voz mira `kokoro` o `chatterbox`
**Combina con:** `moviepy`, `remotion`, `ffmpeg`

## `chatterbox`
role=library · exec=local · setup=easy · mcp=False · prov=['local']

**Qué es:** Clona una voz con unos segundos de audio y ajusta la expresividad. Multilingüe y con marca de agua.
**Stack:** Python, PyTorch
**Repo:** https://github.com/resemble-ai/chatterbox

**Instalación** [~]: `pip install chatterbox   (o: uv add chatterbox)`
_Nombre PyPI puede diferir de 'Chatterbox'; verifica en pypi.org._

**Elige si:** quieres clonar voces con calidad alta y licencia libre
**Evita si:** necesitas algo muy ligero en CPU; mira `kokoro`
**Combina con:** `pipecat`
**Alternativas (elige una):** `fish-speech`, `gpt-sovits`, `kokoro`, `luxtts`

## `cosyvoice`
role=library · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Síntesis de voz natural con clonación y control de estilo, también en streaming.
**Stack:** Python, PyTorch
**Repo:** https://github.com/QwenAudio/CosyVoice

**Instalación** [~]: `pip install cosyvoice   (o: uv add cosyvoice)`
_Nombre PyPI puede diferir de 'CosyVoice'; verifica en pypi.org._

**Elige si:** necesitas TTS multilingüe en streaming
**Evita si:** quieres instalación muy simple; mira `kokoro`
**Combina con:** `pipecat`
**Alternativas (elige una):** `fish-speech`, `index-tts`

## `davinci-resolve-mcp`
role=runtime · exec=local · setup=medium · mcp=True · prov=['mcp']

**Qué es:** Expone la API oficial de scripting de DaVinci Resolve como herramientas MCP para Claude, Cursor, Codex y otros clientes. Cubre montaje, organización del media pool, render, marcadores, color, Fusion y Fairlight, y añade análisis de medios que nunca modifica los originales. Incluye un panel de control local en el navegador.
**Stack:** Python, Node.js, DaVinci Resolve Scripting API, ffmpeg
**Repo:** https://github.com/samuelgursky/davinci-resolve-mcp

**Instalación** [~]: `git clone https://github.com/samuelgursky/davinci-resolve-mcp && cd davinci-resolve-mcp && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** editas en DaVinci Resolve y quieres que un agente MCP automatice montaje, render o metadatos
**Evita si:** no usas Resolve o prefieres montar video por código sin editor; mira `moviepy` o `ffmpeg`
**Combina con:** `claude-code`, `ffmpeg`, `whisper`

## `faster-whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Es el mismo modelo de OpenAI, pero con un runtime de inferencia optimizado.
**Stack:** Python, CTranslate2
**Repo:** https://github.com/SYSTRAN/faster-whisper

**Instalación** [~]: `git clone https://github.com/SYSTRAN/faster-whisper && cd faster-whisper && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** el rendimiento, la memoria o el coste de GPU importan
**Evita si:** necesitas alineación/diarización (whisperX) o te basta el CLI oficial
**Combina con:** `whisperx`
**Alternativas (elige una):** `whisper-cpp`

## `ffmpeg`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** FFmpeg es la base multimedia sobre la que se apoyan casi todos los editores, reproductores y pipelines de video. Incluye el CLI `ffmpeg` para convertir, recortar, concatenar, mezclar, quemar subtítulos y transmitir, `ffprobe` para inspeccionar archivos y las librerías libav* para integrarlo en tu propio software.
**Stack:** C, ensamblador (x86/ARM), libavcodec, libavformat, libavfilter
**Repo:** https://github.com/FFmpeg/FFmpeg

**Instalación** [?]: `git clone https://github.com/FFmpeg/FFmpeg (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas convertir, cortar, mezclar o transmitir audio y video desde la línea de comandos o un script
**Evita si:** quieres una interfaz gráfica para cortar sin pérdida (`lossless-cut`) o componer video desde Python con objetos (`moviepy`)
**Combina con:** `whisper`, `yt-dlp`, `moviepy`

## `fish-speech`
role=library · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Clona voces con pocos segundos de audio y genera habla natural en muchos idiomas.
**Stack:** Python, PyTorch
**Repo:** https://github.com/fishaudio/fish-speech

**Instalación** [~]: `pip install fish speech   (o: uv add fish speech)`
_Nombre PyPI puede diferir de 'Fish Speech'; verifica en pypi.org._

**Elige si:** buscas TTS de alta calidad con clonación
**Evita si:** necesitas licencia comercial sin restricciones; mira `chatterbox`
**Alternativas (elige una):** `chatterbox`, `cosyvoice`, `gpt-sovits`

## `gpt-sovits`
role=app · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Entrena una voz con muy pocos datos y sintetiza en varios idiomas. Muy popular entre creadores.
**Stack:** Python, PyTorch, Gradio
**Repo:** https://github.com/RVC-Boss/GPT-SoVITS

**Instalación** [~]: `git clone https://github.com/RVC-Boss/GPT-SoVITS && cd GPT-SoVITS && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres entrenar una voz con pocos datos
**Evita si:** prefieres zero-shot sin entrenar; mira `chatterbox`
**Combina con:** `rvc`
**Alternativas (elige una):** `chatterbox`, `fish-speech`

## `hunyuanvideo`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** HunyuanVideo publica los pesos, la definición en PyTorch y el código de inferencia de un modelo de texto a video de más de 13.000 millones de parámetros, que genera clips de unos 5 segundos (129 fotogramas) en 540p o 720p. Las variantes de imagen a video, avatares guiados por audio y personalización viven en repos aparte.
**Stack:** Python, PyTorch, Diffusers, FlashAttention, xDiT
**Repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo

**Instalación** [~]: `git clone https://github.com/Tencent-Hunyuan/HunyuanVideo && cd HunyuanVideo && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad
**Evita si:** trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente
**Combina con:** `comfyui`, `diffusers`, `real-esrgan`
**Alternativas (elige una):** `wan2-2`, `ltx-video`

## `hyperframes`
role=runtime · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** HyperFrames define cada video como un archivo HTML con atributos de tiempo y pistas, animado con GSAP, CSS, Lottie, Three.js u otras librerías, y lo renderiza a MP4. Incluye CLI para crear, previsualizar y renderizar, un catálogo de unos 450 bloques (transiciones, subtítulos, gráficos, mapas) y skills para que Claude Code, Codex o Cursor produzcan videos a partir de una petición.
**Stack:** TypeScript, Node.js, Puppeteer, FFmpeg, GSAP
**Repo:** https://github.com/heygen-com/hyperframes

**Instalación** [~]: `git clone https://github.com/heygen-com/hyperframes && cd hyperframes && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva
**Evita si:** tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual
**Combina con:** `claude-code`, `gsap`, `kokoro`, `whisperx`
**Alternativas (elige una):** `remotion`, `moviepy`

## `index-tts`
role=library · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Clona voces sin entrenar y permite controlar la duración exacta, útil para doblaje.
**Stack:** Python, PyTorch
**Repo:** https://github.com/index-tts/index-tts

**Instalación** [~]: `pip install indextts   (o: uv add indextts)`
_Nombre PyPI puede diferir de 'IndexTTS'; verifica en pypi.org._

**Elige si:** necesitas controlar duración y emoción de la voz
**Evita si:** buscas licencia totalmente libre; revisa su licencia
**Alternativas (elige una):** `cosyvoice`

## `kokoro`
role=library · exec=local · setup=easy · mcp=False · prov=['local']

**Qué es:** Voces naturales en varios idiomas, incluido el español, rápido incluso en CPU.
**Stack:** Python, PyTorch, JavaScript
**Repo:** https://github.com/hexgrad/kokoro

**Instalación** [~]: `pip install kokoro   (o: uv add kokoro)`
_Nombre PyPI puede diferir de 'Kokoro'; verifica en pypi.org._

**Elige si:** quieres TTS ligero, rápido y con licencia permisiva
**Evita si:** necesitas clonar voces; mira `chatterbox`
**Combina con:** `pipecat`, `whisper-cpp`
**Alternativas (elige una):** `chatterbox`, `tts`, `luxtts`

## `livekit-agents`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** Construye agentes que hablan, escuchan y ven, con detección de turnos y telefonía, desplegables a escala.
**Stack:** Python, Node.js, WebRTC
**Repo:** https://github.com/livekit/agents

**Instalación** [~]: `git clone https://github.com/livekit/agents && cd agents && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas agentes de voz escalables con WebRTC
**Evita si:** quieres algo ligero sin servidor de medios; mira `pipecat`
**Combina con:** `kokoro`
**Alternativas (elige una):** `pipecat`

## `lossless-cut`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** LosslessCut es una interfaz gráfica sobre FFmpeg para recortar y fusionar archivos de video y audio sin recompresión. Sirve para descartar gigas de material de cámara, GoPro o dron, extraer o reemplazar pistas, cambiar de contenedor (MKV a MP4) y editar metadatos o capítulos, en Windows, macOS y Linux.
**Stack:** TypeScript, Electron, React, FFmpeg
**Repo:** https://github.com/mifi/lossless-cut

**Instalación** [~]: `git clone https://github.com/mifi/lossless-cut && cd lossless-cut && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica
**Evita si:** necesitas efectos, transiciones o un montaje con capas; mira `opencut` o, por código, `moviepy`
**Combina con:** `yt-dlp`, `whisperx`, `moviepy`

## `ltx-video`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** LTX-Video es el repositorio de los modelos v0.9.x de Lightricks, un transformer de difusión (DiT) para texto a video, imagen a video, extensión de clips y video a video con condiciones por fotograma clave. Incluye variantes de 2B y 13B, destiladas y FP8, y LoRAs de control de pose, profundidad y bordes. Ya solo se mantiene como legado: los modelos nuevos están en LTX-2.
**Stack:** Python, PyTorch, Diffusers, ComfyUI
**Repo:** https://github.com/Lightricks/LTX-Video

**Instalación** [~]: `git clone https://github.com/Lightricks/LTX-Video && cd LTX-Video && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x
**Evita si:** empiezas un proyecto nuevo; Lightricks recomienda LTX-2.5 (repo Lightricks/LTX-2), o mira `wan2-2` y `wan2gp`
**Combina con:** `comfyui`, `diffusers`, `real-esrgan`
**Alternativas (elige una):** `wan2-2`, `hunyuanvideo`

## `luxtts`
role=library · exec=local · setup=easy · mcp=False · prov=['local']

**Qué es:** Basado en ZipVoice, pensado para clonación rápida y realista con pocos recursos.
**Stack:** Python, PyTorch
**Repo:** https://github.com/ysharma3501/LuxTTS

**Instalación** [~]: `pip install luxtts   (o: uv add luxtts)`
_Nombre PyPI puede diferir de 'LuxTTS'; verifica en pypi.org._

**Elige si:** necesitas TTS con clonación muy rápido
**Evita si:** buscas el proyecto más maduro; mira `chatterbox`
**Combina con:** `litellm`, `cosmos`, `comfyui`
**Alternativas (elige una):** `kokoro`, `chatterbox`

## `manim`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Manim permite describir en código Python escenas con fórmulas LaTeX, gráficas, geometría y transformaciones animadas, y exportarlas a video. Este repo es ManimGL, la versión original que Grant Sanderson usa en 3Blue1Brown; la edición comunitaria (ManimCommunity/manim) es un fork más estable y mejor documentado.
**Stack:** Python, OpenGL, FFmpeg, LaTeX
**Repo:** https://github.com/3b1b/manim

**Instalación** [~]: `pip install manim (manimgl)   (o: uv add manim (manimgl))`
_Nombre PyPI puede diferir de 'Manim (ManimGL)'; verifica en pypi.org._

**Elige si:** quieres animaciones matemáticas o técnicas precisas definidas en código Python
**Evita si:** buscas estabilidad y documentación para empezar (usa la edición comunitaria ManimCommunity/manim) o motion graphics de marketing; mira `remotion` o `hyperframes`
**Combina con:** `kokoro`, `moviepy`, `ffmpeg`

## `moneyprinterturbo`
role=app · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** MoneyPrinterTurbo automatiza la producción de shorts: das un tema o palabras clave y escribe el guion con un LLM, busca clips en Pexels o Pixabay (o usa los tuyos o video generado por IA), genera locución, subtítulos y música, y monta el resultado en 9:16, 16:9 o 1:1. Se usa desde WebUI, API, CLI o pidiéndoselo a un agente con su skill.
**Stack:** Python, Streamlit, FastAPI, MoviePy, faster-whisper
**Repo:** https://github.com/harry0703/MoneyPrinterTurbo

**Instalación** [~]: `git clone https://github.com/harry0703/MoneyPrinterTurbo && cd MoneyPrinterTurbo && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres producir videos cortos narrados a partir de un tema sin editar a mano
**Evita si:** necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage`
**Combina con:** `ollama`, `kokoro`, `faster-whisper`
**Alternativas (elige una):** `openmontage`, `videofy-minimal`

## `moviepy`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** MoviePy convierte la edición de video en código Python: abres clips, los recortas, superpones texto o imágenes, mezclas audio y exportas a MP4, WebM o GIF. Es la pieza de ensamblaje habitual en pipelines que generan videos cortos a partir de imágenes, voz sintética y subtítulos.
**Stack:** Python, NumPy, Pillow, FFmpeg
**Repo:** https://github.com/Zulko/moviepy

**Instalación** [~]: `pip install moviepy   (o: uv add moviepy)`
_Nombre PyPI puede diferir de 'MoviePy'; verifica en pypi.org._

**Elige si:** ensamblas video desde Python y quieres controlar cada clip por código
**Evita si:** prefieres plantillas en React (`remotion`) o en HTML (`hyperframes`), o solo necesitas cortar sin recodificar (`lossless-cut`)
**Combina con:** `whisperx`, `kokoro`, `comfyui`
**Alternativas (elige una):** `remotion`, `hyperframes`

## `nemo`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Incluye modelos de ASR como Parakeet y Canary, que lideran rankings de transcripción, y herramientas para afinarlos.
**Stack:** Python, PyTorch
**Repo:** https://github.com/NVIDIA-NeMo/Speech

**Instalación** [~]: `pip install nvidia nemo speech   (o: uv add nvidia nemo speech)`
_Nombre PyPI puede diferir de 'NVIDIA NeMo Speech'; verifica en pypi.org._

**Elige si:** necesitas ASR de máxima precisión y tienes GPU
**Evita si:** quieres algo simple; mira `faster-whisper`
**Combina con:** `pipecat`
**Alternativas (elige una):** `whisperx`

## `obs-studio`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** OBS Studio captura, compone, codifica, graba y transmite video en Windows, macOS y Linux. Combinas en escenas la pantalla, ventanas, webcam, navegador y archivos multimedia, mezclas el audio con filtros y emites a YouTube, Twitch u otro servicio RTMP, o grabas a disco.
**Stack:** C, C++, Qt, FFmpeg
**Repo:** https://github.com/obsproject/obs-studio

**Instalación** [?]: `git clone https://github.com/obsproject/obs-studio (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas
**Evita si:** lo que necesitas es montar o recortar el video ya grabado; usa `opencut` o `lossless-cut`
**Combina con:** `lossless-cut`, `opencut`, `faster-whisper`
**Alternativas (elige una):** `openscreen`

## `omnivoice-studio`
role=app · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Reúne STT, TTS y dubbing en una sola app sin claves de API.
**Stack:** desktop/Python
**Repo:** https://github.com/debpalash/VoiceStudio

**Instalación** [~]: `git clone https://github.com/debpalash/VoiceStudio && cd VoiceStudio && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres suite de voz completa local (dictado + clonación + dubbing)
**Evita si:** solo necesitas TTS simple por CLI/librería (TTS) o estabilidad de producción
**Combina con:** `whisperx`
**Alternativas (elige una):** `videolingo`

## `opencut`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** OpenCut es un editor de video pensado como alternativa abierta a CapCut: privado (los videos no salen de tu dispositivo), sin funciones de pago y fácil de usar. Hoy se usa la versión clásica en opencut.app mientras el equipo reescribe el proyecto desde cero, con un núcleo en Rust para web, escritorio y móvil.
**Stack:** TypeScript, Rust, WebAssembly, Next.js
**Repo:** https://github.com/OpenCut-app/OpenCut

**Instalación** [~]: `git clone https://github.com/OpenCut-app/OpenCut && cd OpenCut && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut
**Evita si:** necesitas estabilidad o automatización hoy; para montar por código mira `moviepy` o `remotion`, y para cortes sin pérdida `lossless-cut`
**Combina con:** `lossless-cut`, `obs-studio`, `whisperx`

## `openmontage`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Describes el video y el agente investiga, escribe el guion, genera recursos y monta el resultado.
**Stack:** Markdown, Python
**Repo:** https://github.com/calesthio/OpenMontage.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/OpenMontage/). Si necesitas el código: git clone https://github.com/calesthio/OpenMontage.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres producir videos completos con un agente
**Evita si:** solo necesitas editar clips; mira `video-use`
**Combina con:** `remotion`
**Alternativas (elige una):** `remotion-superpowers`, `moneyprinterturbo`

## `openscreen`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** OpenScreen graba una ventana o la pantalla completa con micrófono y audio del sistema, y después te deja pulir la demo: zooms que siguen al cursor, webcam superpuesta, fondos, anotaciones, recorte y velocidad por tramo. Exporta a MP4 o GIF en varias proporciones. El proyecto original está archivado; su continuación activa es getopenscreen/openscreen.
**Stack:** TypeScript, Electron, PixiJS
**Repo:** https://github.com/siddharthvaddem/openscreen

**Instalación** [~]: `git clone https://github.com/siddharthvaddem/openscreen && cd openscreen && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio
**Evita si:** necesitas un proyecto mantenido; usa su continuación getopenscreen/openscreen, o `obs-studio` para grabación y streaming generales
**Combina con:** `lossless-cut`, `opencut`
**Alternativas (elige una):** `obs-studio`

## `pipecat`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** Encadena STT, LLM y TTS con interrupciones y baja latencia, y conecta con teléfono, WebRTC o WhatsApp.
**Stack:** Python
**Repo:** https://github.com/pipecat-ai/pipecat

**Instalación** [~]: `git clone https://github.com/pipecat-ai/pipecat && cd pipecat && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** construyes un agente de voz en Python
**Evita si:** quieres infraestructura WebRTC gestionada; mira `livekit-agents`
**Combina con:** `kokoro`, `whisper-cpp`
**Alternativas (elige una):** `livekit-agents`

## `remotion`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Convierte el video en un artefacto versionable y parametrizable desde tu código frontend.
**Stack:** Node.js, React, Chromium, ffmpeg
**Repo:** https://github.com/remotion-dev/remotion

**Instalación** [~]: `npm install remotion   (o: pnpm add remotion)`
_Nombre npm puede diferir de 'remotion'; verifica en npmjs.com._

**Elige si:** generas video a escala con React y quieres variantes parametrizadas
**Evita si:** trabajas en Python (moviepy) o buscas un editor visual
**Combina con:** `open-generative-ai`
**Alternativas (elige una):** `moviepy`, `hyperframes`

## `remotion-superpowers`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Añade locución con IA, música, footage de stock e imágenes para producir videos en código.
**Stack:** Shell, Markdown
**Repo:** https://github.com/DojoCodingLabs/remotion-superpowers

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Remotion Superpowers/). Si necesitas el código: git clone https://github.com/DojoCodingLabs/remotion-superpowers`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** usas Remotion con un agente y quieres producción completa
**Evita si:** no usas Remotion
**Combina con:** `remotion`, `skills-remotion`
**Alternativas (elige una):** `openmontage`, `video-use`

## `rvc`
role=app · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Cambia la voz de una grabación manteniendo entonación. Muy usado para covers y doblaje.
**Stack:** Python, PyTorch, Gradio
**Repo:** https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

**Instalación** [~]: `git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI && cd Retrieval-based-Voice-Conversion-WebUI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres convertir una voz grabada en otra
**Evita si:** necesitas generar voz desde texto; mira `chatterbox`
**Combina con:** `gpt-sovits`

## `skills-remotion`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Enseñan al agente las buenas prácticas de Remotion: composiciones, animaciones, audio y render.
**Stack:** TypeScript, Markdown
**Repo:** https://github.com/remotion-dev/skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Remotion Agent Skills/). Si necesitas el código: git clone https://github.com/remotion-dev/skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** haces videos con Remotion y un agente
**Evita si:** no usas Remotion
**Combina con:** `remotion`, `remotion-superpowers`

## `supertonic`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Apunta a latencia mínima con privacidad total, sin nube ni llamadas de API.
**Stack:** Python, Rust (ONNX), Node.js, WebGPU
**Repo:** https://github.com/supertone-oss-archive/supertonic

**Instalación** [~]: `git clone https://github.com/supertone-oss-archive/supertonic && cd supertonic && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres voz local en tiempo real y sin nube
**Evita si:** priorizas clonación de máxima fidelidad (VoxCPM) o flexibilidad multi-modelo (TTS)
**Combina con:** `whisperx`, `moviepy`

## `tts`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Reúne en una sola librería modelos como Tacotron, VITS y XTTS, con CLI y API Python.
**Stack:** Python, PyTorch, modelos descargables
**Repo:** https://github.com/coqui-ai/TTS

**Instalación** [~]: `pip install tts   (o: uv add tts)`
_Nombre PyPI puede diferir de 'TTS'; verifica en pypi.org._

**Elige si:** quieres flexibilidad y varios modelos en una librería
**Evita si:** necesitas tiempo real puro (supertonic) o soporte comercial (Coqui está inactivo)
**Combina con:** `whisperx`, `moviepy`
**Alternativas (elige una):** `kokoro`

## `vibevoice`
role=library · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** Genera conversaciones de hasta 90 minutos con cuatro voces distintas, y tiene variantes de baja latencia.
**Stack:** Python, PyTorch
**Repo:** https://github.com/microsoft/VibeVoice

**Instalación** [~]: `pip install vibevoice   (o: uv add vibevoice)`
_Nombre PyPI puede diferir de 'VibeVoice'; verifica en pypi.org._

**Elige si:** quieres generar podcasts o diálogos largos
**Evita si:** solo necesitas frases cortas; mira `kokoro`
**Combina con:** `open-notebook`

## `video-use`
role=skill · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** El agente corta, une, subtitula y ajusta videos a partir de instrucciones en lenguaje natural.
**Stack:** Python, ffmpeg
**Repo:** https://github.com/browser-use/video-use

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/video-use/). Si necesitas el código: git clone https://github.com/browser-use/video-use`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres editar videos pidiéndoselo a tu agente
**Evita si:** quieres una app de edición visual; mira `opencut`
**Combina con:** `ffmpeg`, `claude-code`
**Alternativas (elige una):** `remotion-superpowers`

## `videofy-minimal`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Encadena TTS/STT y montaje en un solo flujo para pasar de texto a reel con lo mínimo.
**Stack:** Python/Node
**Repo:** https://github.com/schibsted/videofy_minimal

**Instalación** [~]: `git clone https://github.com/schibsted/videofy_minimal && cd videofy_minimal && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres reels simples ya, sin montar un pipeline entero
**Evita si:** necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy)
**Combina con:** `whisper`, `supertonic`
**Alternativas (elige una):** `moneyprinterturbo`

## `videolingo`
role=app · exec=hybrid · setup=medium · mcp=False · prov=['openai']

**Qué es:** VideoLingo reúne en una interfaz Streamlit el trabajo de un equipo de subtitulado: descarga el video con yt-dlp, lo transcribe con alineación por palabra, segmenta y traduce los subtítulos con un LLM y, si quieres, genera el doblaje con voz sintética o clonada. Produce archivos SRT y videos subtitulados o doblados.
**Stack:** Python, Streamlit, Qwen3-ASR, yt-dlp, FFmpeg
**Repo:** https://github.com/Huanshere/VideoLingo

**Instalación** [~]: `git clone https://github.com/Huanshere/VideoLingo && cd VideoLingo && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar
**Evita si:** solo necesitas transcribir o subtitular en el idioma original; te basta `whisperx` o `faster-whisper`
**Combina con:** `yt-dlp`, `gpt-sovits`, `whisperx`
**Alternativas (elige una):** `omnivoice-studio`

## `voxcpm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Pertenece a la familia CPM de modelos generativos de OpenBMB.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/OpenBMB/VoxCPM

**Instalación** [~]: `git clone https://github.com/OpenBMB/VoxCPM && cd VoxCPM && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres voz muy natural o clonada y tienes GPU
**Evita si:** priorizas latencia mínima (supertonic) o no tienes GPU
**Combina con:** `tts`

## `wan2-2`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** Wan2.2 publica pesos y código de inferencia de varios modelos de video: texto a video e imagen a video de 14B (MoE), un modelo híbrido de 5B que genera 720p a 24 fps en una RTX 4090, video guiado por voz (S2V) y animación o sustitución de personajes (Animate). Es la base de muchos flujos de ComfyUI y Diffusers.
**Stack:** Python, PyTorch, FlashAttention, Diffusers
**Repo:** https://github.com/Wan-Video/Wan2.2

**Instalación** [~]: `git clone https://github.com/Wan-Video/Wan2.2 && cd Wan2.2 && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más
**Evita si:** tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados
**Combina con:** `comfyui`, `diffusers`, `real-esrgan`, `cosyvoice`
**Alternativas (elige una):** `hunyuanvideo`, `ltx-video`

## `wan2gp`
role=app · exec=local · setup=heavy · mcp=True · prov=['local', 'mcp']

**Qué es:** WanGP, antes Wan2GP, es una interfaz web para ejecutar en tu GPU decenas de modelos generativos abiertos: video (Wan 2.1/2.2, LTX-2, Hunyuan Video), imagen (Flux, Qwen Image), voz y música (Chatterbox, Index TTS, Ace Step) y 3D. Añade cola de trabajos, LoRAs, galerías y un asistente local, Deepy, que planifica y lanza las generaciones por ti.
**Stack:** Python, PyTorch, Gradio, Diffusers, mmgp
**Repo:** https://github.com/deepbeepmeep/Wan2GP

**Instalación** [~]: `git clone https://github.com/deepbeepmeep/Wan2GP && cd Wan2GP && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano
**Evita si:** prefieres construir flujos por nodos con control fino (`comfyui`) o tienes una GPU grande y quieres el código oficial (`wan2-2`)
**Combina con:** `claude-code`, `moviepy`, `lossless-cut`
**Alternativas (elige una):** `comfyui`

## `whisper`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Cubre también identificación de idioma y traducción al inglés en la misma red.
**Stack:** Python 3.9+, PyTorch
**Repo:** https://github.com/openai/whisper

**Instalación** [~]: `git clone https://github.com/openai/whisper && cd whisper && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres la referencia robusta y no te obsesiona la latencia
**Evita si:** necesitas más velocidad (faster-whisper) o timings por palabra (whisperX)
**Combina con:** `whisperx`
**Alternativas (elige una):** `whisper-cpp`

## `whisper-cpp`
role=runtime · exec=local · setup=easy · mcp=False · prov=['local']

**Qué es:** Transcribe voz a texto en local sin Python ni GPU obligatoria, incluso en tiempo real. Base de muchas apps de dictado.
**Stack:** C++, C
**Repo:** https://github.com/ggml-org/whisper.cpp

**Instalación** [?]: `git clone https://github.com/ggml-org/whisper.cpp (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres transcribir en local sin GPU
**Evita si:** necesitas marcas de tiempo por palabra y diarización; mira `whisperx`
**Combina con:** `ffmpeg`
**Alternativas (elige una):** `faster-whisper`, `whisper`

## `whisperx`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Convierte la salida "por segmento" de Whisper en timings palabra a palabra con etiqueta de speaker.
**Stack:** Python, faster-whisper, wav2vec2, pyannote
**Repo:** https://github.com/m-bain/whisperX

**Instalación** [~]: `git clone https://github.com/m-bain/whisperX && cd whisperX && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas subtítulos precisos o diarización
**Evita si:** te basta texto plano (whisper) o no quieres gestionar tokens de HF
**Combina con:** `whisper`, `moviepy`
**Alternativas (elige una):** `nemo`
