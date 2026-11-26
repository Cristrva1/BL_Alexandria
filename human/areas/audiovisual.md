[Áreas](../areas.md) · [Inicio](../README.md)

# Producción audiovisual

Encuentra las piezas para producir imágenes, audio y video: desde una voz o un subtítulo hasta un anuncio completo.

120 repos únicos · 11 subcategorías. [Ver en el explorador](../../docs/index.html#/area/audiovisual).

## Opciones para empezar

[FFmpeg](../fichas/ffmpeg.md), [whisper](../fichas/whisper.md), [remotion](../fichas/remotion.md)

Son opciones para comparar. No es necesario instalar todas.

## Subcategorías

### Video: edición, grabación y subtítulos

Montar material existente, capturar pantalla y preparar subtítulos.

[Explorar 14 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-video-edicion)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Concat](../fichas/concat.md) | Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP. | Sin clave propia de API de IA en la ruta básica |
| [DaVinci Resolve MCP](../fichas/davinci-resolve-mcp.md) | Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render. | Sin clave propia de API de IA en la ruta básica |
| [FFmpeg](../fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | Sin clave propia de API de IA en la ruta básica |
| [HandBrake](../fichas/handbrake.md) | Transcodificador de vídeo libre para Linux, macOS y Windows con interfaz gráfica, CLI, presets por dispositivo y colas de trabajo. | Sin clave propia de API de IA en la ruta básica |
| [Kdenlive](../fichas/kdenlive.md) | Editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz. | Sin clave propia de API de IA en la ruta básica |
| [LosslessCut](../fichas/lossless-cut.md) | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. | Sin clave propia de API de IA en la ruta básica |
| [OBS Studio](../fichas/obs-studio.md) | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. | Sin clave propia de API de IA en la ruta básica |
| [OpenCut](../fichas/opencut.md) | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. | Sin clave propia de API de IA en la ruta básica |
| [OpenRV](../fichas/openrv.md) | Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual. | Sin clave propia de API de IA en la ruta básica |
| [pysubs2](../fichas/pysubs2.md) | Convierte formatos de subtítulos y ajusta sus tiempos en lote desde Python o la terminal, sin cambiar el video ni usar una API de IA. | Sin clave propia de API de IA en la ruta básica |
| [rea-video](../fichas/rea-video.md) | Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md. | API de IA opcional |
| [Shotcut](../fichas/shotcut.md) | Editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz. | Sin clave propia de API de IA en la ruta básica |
| [video-use](../fichas/video-use.md) | Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe. | API de IA necesaria |
| [VideoLingo](../fichas/videolingo.md) | App para reconocer voz, traducir subtítulos y preparar doblaje, con ASR local por defecto y proveedores configurables por etapa. | Depende de la ruta elegida |

### Video: generación con IA

Crear clips y organizar flujos de video generativo.

[Explorar 8 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-video-ia)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [AI-Youtube-Shorts-Generator](../fichas/ai-youtube-shorts-generator.md) | Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM. | API de IA necesaria |
| [HunyuanVideo](../fichas/hunyuanvideo.md) | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. | Sin clave propia de API de IA en la ruta básica |
| [HunyuanVideo 1.5](../fichas/hunyuanvideo-1-5.md) | Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más. | API de IA opcional |
| [LTX-2](../fichas/ltx-2.md) | Código oficial de inferencia y entrenamiento LoRA de LTX-2 y LTX-2.5, modelo DiT de Lightricks que genera vídeo con audio sincronizado. | Sin clave propia de API de IA en la ruta básica |
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | Depende de la ruta elegida |
| [short-video-factory](../fichas/short-video-factory.md) | Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. | Depende de la ruta elegida |
| [Wan2.2](../fichas/wan2-2.md) | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | API de IA opcional |
| [WanGP](../fichas/wan2gp.md) | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. | API de IA opcional |

### Video: código y motion graphics

Crear escenas, animaciones y piezas audiovisuales mediante código o agentes.

[Explorar 26 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-video-codigo)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [brag](../fichas/brag.md) | Skills para que un agente convierta un proyecto o sitio en un video breve de lanzamiento con composición y música. | API de IA opcional |
| [claude-animated-shorts](../fichas/claude-animated-shorts.md) | Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion. | Sin clave propia de API de IA en la ruta básica |
| [FFmpeg Skill](../fichas/ffmpeg-skill.md) | Da a agentes herramientas locales de FFmpeg para recortar, reencuadrar, normalizar audio y exportar video con pasos trazables. | Sin clave propia de API de IA en la ruta básica |
| [huashu-motion](../fichas/huashu-motion.md) | Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión visual. | Sin clave propia de API de IA en la ruta básica |
| [HyperFrames](../fichas/hyperframes.md) | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. | API de IA opcional |
| [HyperFrames Launches](../fichas/hyperframes-launches.md) | Publica composiciones con código usadas en videos de lanzamiento de HeyGen para estudiar cómo se montan escenas y animaciones. | Sin clave propia de API de IA en la ruta básica |
| [lemo-opuscar](../fichas/lemo-opuscar.md) | Biblioteca de estilos para video por código orientada a Claude,con licencias diferentes para código,guías y medios. | API de IA opcional |
| [manim](../fichas/manim-community.md) | Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. | Sin clave propia de API de IA en la ruta básica |
| [Manim (ManimGL)](../fichas/manim.md) | Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL. | Sin clave propia de API de IA en la ruta básica |
| [mediabunny](../fichas/mediabunny.md) | Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web. | Sin clave propia de API de IA en la ruta básica |
| [Motion Canvas](../fichas/motion-canvas.md) | Biblioteca TypeScript para crear animaciones y vídeos explicativos con código, con editor en tiempo real que sincroniza animaciones con una pista de voz. | Sin clave propia de API de IA en la ruta básica |
| [motion-design-skill](../fichas/motion-design-skill.md) | Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interfaces. | Sin clave propia de API de IA en la ruta básica |
| [motionmaxxing](../fichas/motionmaxxing.md) | Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código. | API de IA opcional |
| [MoviePy](../fichas/moviepy.md) | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | Sin clave propia de API de IA en la ruta básica |
| [openfilm](../fichas/openfilm.md) | Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos. | API de IA opcional |
| [OpenMontage](../fichas/openmontage.md) | Pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales. | API de IA opcional |
| [Papermorph](../fichas/papermorph.md) | Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visuales. | API de IA opcional |
| [rea-video](../fichas/rea-video.md) | Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md. | API de IA opcional |
| [remotion](../fichas/remotion.md) | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. | API de IA opcional |
| [Remotion Agent Skills](../fichas/skills-remotion.md) | Skills oficiales de Remotion para que tu agente de código cree videos con React. | API de IA opcional |
| [Remotion Superpowers](../fichas/remotion-superpowers.md) | Orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa. | API de IA necesaria |
| [Revideo](../fichas/revideo.md) | Motor TypeScript para crear vídeos con código y renderizarlos sin interfaz desde una API, con reproductor React para previsualizar escenas en el navegador. | Sin clave propia de API de IA en la ruta básica |
| [srt-whiteboard-animation](../fichas/srt-whiteboard-animation.md) | Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos SRT. | Sin clave propia de API de IA en la ruta básica |
| [video-shotcraft](../fichas/video-shotcraft.md) | Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de sonido. | API de IA opcional |
| [video-use](../fichas/video-use.md) | Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe. | API de IA necesaria |
| [videofy_minimal](../fichas/videofy-minimal.md) | Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. | API de IA necesaria |

### Voz: narración, síntesis y clonación

Convertir texto en voz y preparar locuciones en los idiomas compatibles.

[Explorar 13 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-voz)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [CosyVoice](../fichas/cosyvoice.md) | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. | Sin clave propia de API de IA en la ruta básica |
| [edge-tts](../fichas/edge-tts.md) | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. | Sin clave propia de API de IA en la ruta básica |
| [ElevenLabs (SDK de Python)](../fichas/elevenlabs-python.md) | SDK oficial de Python para la API de pago de ElevenLabs: voz sintética, clonación, transcripción, música y agentes de voz. | API de IA necesaria |
| [F5-TTS](../fichas/f5-tts.md) | Síntesis de voz con clonación a partir de pocos segundos de audio de referencia, basada en flow matching con Diffusion Transformer; incluye app Gradio y CLI. | Sin clave propia de API de IA en la ruta básica |
| [Fish Speech](../fichas/fish-speech.md) | Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante. | Sin clave propia de API de IA en la ruta básica |
| [GPT-SoVITS](../fichas/gpt-sovits.md) | Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos. | Sin clave propia de API de IA en la ruta básica |
| [IndexTTS](../fichas/index-tts.md) | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. | Sin clave propia de API de IA en la ruta básica |
| [Kokoro](../fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | Sin clave propia de API de IA en la ruta básica |
| [LuxTTS](../fichas/luxtts.md) | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. | Sin clave propia de API de IA en la ruta básica |
| [RVC WebUI](../fichas/rvc.md) | Interfaz y herramientas para convertir una grabación a otra voz mediante modelos locales. | Sin clave propia de API de IA en la ruta básica |
| [VibeVoice](../fichas/vibevoice.md) | Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. | Sin clave propia de API de IA en la ruta básica |
| [VoiceStudio](../fichas/omnivoice-studio.md) | App local de voz con modelos descargables,edición AGPL y una oferta comercial separada. | Sin clave propia de API de IA en la ruta básica |
| [VoxCPM](../fichas/voxcpm.md) | VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación de voz. | Sin clave propia de API de IA en la ruta básica |

### Transcripción: audio a texto

Transcribir, alinear y aprovechar grabaciones de voz.

[Explorar 8 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-transcripcion)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Buzz](../fichas/buzz.md) | Transcribe grabaciones y exporta subtítulos en una aplicación de escritorio que puede usar Whisper en tu propio equipo. | API de IA opcional |
| [faster-whisper](../fichas/faster-whisper.md) | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. | Sin clave propia de API de IA en la ruta básica |
| [NeMo Speech](../fichas/nemo.md) | Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento. | Sin clave propia de API de IA en la ruta básica |
| [sherpa-onnx](../fichas/sherpa-onnx.md) | Motor de voz offline con ONNX Runtime: reconocimiento, síntesis, VAD, diarización e identificación de hablante en móvil, embebido, escritorio y servidor. | Sin clave propia de API de IA en la ruta básica |
| [VibeVoice](../fichas/vibevoice.md) | Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. | Sin clave propia de API de IA en la ruta básica |
| [whisper](../fichas/whisper.md) | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. | Sin clave propia de API de IA en la ruta básica |
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Sin clave propia de API de IA en la ruta básica |
| [whisperX](../fichas/whisperx.md) | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. | Sin clave propia de API de IA en la ruta básica |

### Audio: limpieza, música y sonido

Limpiar grabaciones, ajustar sonido y trabajar con música.

[Explorar 10 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-audio)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [ACE-Step-1.5](../fichas/ace-step-1-5.md) | Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. | Sin clave propia de API de IA en la ruta básica |
| [Audacity](../fichas/audacity.md) | Editor y grabador de audio multipista libre para Windows, macOS y Linux, con efectos, análisis y plugins, incluidos plugins de IA locales de Intel. | Sin clave propia de API de IA en la ruta básica |
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | Sin clave propia de API de IA en la ruta básica |
| [Demucs](../fichas/demucs.md) | Modelo de separación de fuentes musicales (voz, batería, bajo y resto) con Hybrid Transformer; continuación mantenida por su autor tras archivarse el repo de Meta. | Sin clave propia de API de IA en la ruta básica |
| [earshot](../fichas/earshot.md) | Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP. | API de IA opcional |
| [pyannote.audio](../fichas/pyannote-audio.md) | Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos preentrenados y un servicio premium opcional. | API de IA opcional |
| [rnnoise](../fichas/rnnoise.md) | Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente. | Sin clave propia de API de IA en la ruta básica |
| [rubberband](../fichas/rubberband.md) | Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas. | Sin clave propia de API de IA en la ruta básica |
| [Ultimate Vocal Remover (UVR)](../fichas/ultimate-vocal-remover.md) | Aplicación de escritorio para separar voz e instrumentos de canciones con modelos de IA (MDX-Net, VR, Demucs), sin necesidad de programar. | Sin clave propia de API de IA en la ruta básica |
| [YuE2](../fichas/yue.md) | Modelo abierto de generación de canciones completas (voz y acompañamiento) a partir de letra y estilo, con partitura editable, covers y una skill para agentes. | Sin clave propia de API de IA en la ruta básica |

### Voz: agentes en tiempo real

Construir conversaciones por audio con procesamiento y respuesta en directo.

[Explorar 4 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-conversacion)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [dograh](../fichas/dograh.md) | Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables. | Depende de la ruta elegida |
| [LiveKit Agents](../fichas/livekit-agents.md) | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. | API de IA opcional |
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | API de IA opcional |
| [TEN Framework](../fichas/ten-framework.md) | Framework para agentes de voz conversacionales en tiempo real, con grafo de extensiones (ASR, LLM, TTS, VAD, turnos), diseñador visual y ejemplos listos. | API de IA necesaria |

### Imagen: generación y edición

Generar imágenes, ampliar, recortar o restaurar fotografías.

[Explorar 13 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-imagen)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [chaiNNer](../fichas/chainner.md) | Interfaz por nodos para encadenar procesamiento de imágenes con IA y clásico: escalado, restauración, conversión y lotes, en Windows, macOS y Linux. | Sin clave propia de API de IA en la ruta básica |
| [CodeFormer](../fichas/codeformer.md) | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. | Sin clave propia de API de IA en la ruta básica |
| [ComfyUI](../fichas/comfyui.md) | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | API de IA opcional |
| [Creative Architect](../fichas/creative-architect.md) | Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video. | API de IA opcional |
| [diffusers](../fichas/diffusers.md) | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. | Sin clave propia de API de IA en la ruta básica |
| [FLUX.2](../fichas/flux2.md) | Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágenes, con variantes rápidas para GPU domésticas. | API de IA opcional |
| [ImageMagick](../fichas/imagemagick.md) | Convierte, redimensiona y prepara imágenes desde la terminal. Puedes generar miniaturas y variantes web en tu equipo sin un modelo de IA. | Sin clave propia de API de IA en la ruta básica |
| [InvokeAI](../fichas/invokeai.md) | Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. | Sin clave propia de API de IA en la ruta básica |
| [Krita AI Diffusion](../fichas/krita-ai-diffusion.md) | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. | API de IA opcional |
| [logo-design-skill](../fichas/logo-design-skill.md) | Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de diseño. | Sin clave propia de API de IA en la ruta básica |
| [Real-ESRGAN](../fichas/real-esrgan.md) | Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos. | Sin clave propia de API de IA en la ruta básica |
| [rembg](../fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | API de IA opcional |
| [Upscayl](../fichas/upscayl.md) | Aplicación de escritorio libre para ampliar y mejorar imágenes con IA (Real-ESRGAN sobre NCNN Vulkan) en Linux, macOS y Windows. | Sin clave propia de API de IA en la ruta básica |

### Avatares, rostros y personajes

Animación de retratos y herramientas para personajes.

[Explorar 7 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-personajes)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [claude-animated-shorts](../fichas/claude-animated-shorts.md) | Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion. | Sin clave propia de API de IA en la ruta básica |
| [Deep-Live-Cam](../fichas/deep-live-cam.md) | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. | Sin clave propia de API de IA en la ruta básica |
| [DeepFace](../fichas/deepface.md) | Biblioteca Python ligera de reconocimiento facial y análisis de atributos (edad, género, emoción) que envuelve modelos como ArcFace, FaceNet o VGG-Face. | Sin clave propia de API de IA en la ruta básica |
| [FaceFusion](../fichas/facefusion.md) | Plataforma para intercambio y mejora de rostros en imágenes y video. | Sin clave propia de API de IA en la ruta básica |
| [genjutsu](../fichas/genjutsu.md) | Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple. | Sin clave propia de API de IA en la ruta básica |
| [InsightFace](../fichas/insightface.md) | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. | Sin clave propia de API de IA en la ruta básica |
| [LivePortrait](../fichas/liveportrait.md) | Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas). | Sin clave propia de API de IA en la ruta básica |

### Modelado y animación 3D

Crear objetos, escenas y recursos tridimensionales.

[Explorar 14 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-3d)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [3dviz-pro-max](../fichas/3dviz-pro-max.md) | Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código. | Sin clave propia de API de IA en la ruta básica |
| [awesome-cad](../fichas/awesome-cad.md) | Directorio de programas, bibliotecas y recursos de diseño asistido por computadora organizados por especialidad. | Sin clave propia de API de IA en la ruta básica |
| [Bevy](../fichas/bevy.md) | Motor de juegos en Rust basado en datos y en el patrón ECS, libre (MIT o Apache-2.0), modular y con funciones 2D y 3D para juegos y simulaciones. | Sin clave propia de API de IA en la ruta básica |
| [blender](../fichas/blender.md) | Código de Blender, la aplicación para modelar, animar, renderizar y editar escenas y contenido tridimensional. | Sin clave propia de API de IA en la ruta básica |
| [Blender MCP](../fichas/blender-mcp.md) | Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP. | API de IA opcional |
| [blender-skills](../fichas/blender-skills.md) | Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexiones MCP. | Sin clave propia de API de IA en la ruta básica |
| [filament](../fichas/filament.md) | Motor de renderizado físicamente basado para integrar gráficos 3D en aplicaciones móviles, web y de escritorio. | Sin clave propia de API de IA en la ruta básica |
| [FreeCAD](../fichas/freecad.md) | Modelador CAD 3D paramétrico libre para diseño de producto, ingeniería mecánica y arquitectura (BIM), con planos técnicos, FEM, CAM y Python. | Sin clave propia de API de IA en la ruta básica |
| [Godot Engine](../fichas/godot.md) | Motor de videojuegos 2D y 3D libre (MIT) con editor integrado, scripting en GDScript o C# y exportación a escritorio, móvil, web y consolas. | Sin clave propia de API de IA en la ruta básica |
| [meshoptimizer](../fichas/meshoptimizer.md) | Biblioteca para optimizar geometría y reducir el coste de almacenar y renderizar mallas tridimensionales. | Sin clave propia de API de IA en la ruta básica |
| [Open Reality](../fichas/openreality.md) | Convierte video propio en escenas 3D consultables y ofrece herramientas MCP para trabajar con la reconstrucción desde un asistente. | Sin clave propia de API de IA en la ruta básica |
| [OpenSCAD](../fichas/openscad.md) | CAD 3D por código: describes la pieza en un lenguaje de script y OpenSCAD la compila a un sólido exportable (STL, 3MF), ideal para piezas paramétricas. | Sin clave propia de API de IA en la ruta básica |
| [ozz-animation](../fichas/ozz-animation.md) | Biblioteca C++ y herramientas para preparar y reproducir animación esquelética dentro de motores y aplicaciones. | Sin clave propia de API de IA en la ruta básica |
| [video2threejs](../fichas/video2threejs.md) | Explica con un caso cómo reconstruir la apariencia de un video como una escena navegable en Three.js. | Sin clave propia de API de IA en la ruta básica |

### Física y simulación

Simular cuerpos,colisiones y sistemas físicos.

[Explorar 7 repos](../../docs/index.html#/explorar?area=audiovisual&topic=av-simulacion)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Genesis World](../fichas/genesis-world.md) | Plataforma de simulación para IA física y robótica con motor multifísica unificado (rígidos, FEM, MPM, fluidos), render fotorrealista y paralelismo masivo en GPU. | Sin clave propia de API de IA en la ruta básica |
| [MotionBricks](../fichas/motionbricks.md) | Genera movimiento de personajes a partir de poses y objetivos mediante modelos locales y una escena de demostración. | Sin clave propia de API de IA en la ruta básica |
| [MuJoCo](../fichas/mujoco.md) | Motor de física de Google DeepMind para simular estructuras articuladas con contacto, estándar en robótica, biomecánica y aprendizaje por refuerzo. | Sin clave propia de API de IA en la ruta básica |
| [planck.js](../fichas/planck-js.md) | Motor de física 2D para simular cuerpos, colisiones y uniones dentro de juegos o aplicaciones JavaScript. | Sin clave propia de API de IA en la ruta básica |
| [react-three-rapier](../fichas/react-three-rapier.md) | Integración del motor de física Rapier con React Three Fiber para añadir simulación a escenas tridimensionales. | Sin clave propia de API de IA en la ruta básica |
| [Robotics for Antigravity](../fichas/robotics-antigravity-plugin.md) | Añade a Antigravity instrucciones para crear, probar y observar escenas de robótica con flujos como la simulación en MuJoCo. | Depende de la ruta elegida |
| [warp](../fichas/warp.md) | Framework de NVIDIA para kernels y simulación física en CPU o GPU; no es un modelo ni un terminal. | Sin clave propia de API de IA en la ruta básica |

La revisión de documentación no equivale a una instalación probada. Consulta cada ficha para acceso, coste, equipo y pasos de arranque.
