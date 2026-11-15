[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Crear audio, voz y video

Transcribe, sintetiza voz, edita o genera video. El montaje local y la generación mediante un proveedor son rutas con requisitos diferentes.

50 repos · 7 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Sin API de IA en la ruta básica |
| [Kokoro](../fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | Sin API de IA en la ruta básica |
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | Depende de la ruta elegida |
| [FFmpeg](../fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | Sin API de IA en la ruta básica |
| [MoviePy](../fichas/moviepy.md) | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | Sin API de IA en la ruta básica |
| [HyperFrames](../fichas/hyperframes.md) | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. | Sin API de IA en la ruta básica |
| [Remotion Agent Skills](../fichas/skills-remotion.md) | Skills oficiales de Remotion para que tu agente de código cree videos con React. | Sin API de IA en la ruta básica |
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | Depende de la ruta elegida |
| [Wan2.2](../fichas/wan2-2.md) | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | Sin API de IA en la ruta básica |
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | Sin API de IA en la ruta básica |

## Secciones

- [Transcripción (voz a texto)](#transcripción-voz-a-texto) — 5 repos
- [Síntesis y clonación de voz](#síntesis-y-clonación-de-voz) — 14 repos
- [Agentes de voz en tiempo real](#agentes-de-voz-en-tiempo-real) — 2 repos
- [Edición, grabación y subtítulos](#edición-grabación-y-subtítulos) — 9 repos
- [Video programático y con agentes](#video-programático-y-con-agentes) — 10 repos
- [Video generativo y pipelines automáticos](#video-generativo-y-pipelines-automáticos) — 7 repos
- [Música y audio generativo](#música-y-audio-generativo) — 3 repos

## Transcripción (voz a texto)

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | quieres transcribir en local sin GPU | Sin API de IA en la ruta básica |
| [whisper](../fichas/whisper.md) | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. | quieres la referencia robusta y no te obsesiona la latencia | Sin API de IA en la ruta básica |
| [faster-whisper](../fichas/faster-whisper.md) | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. | el rendimiento, la memoria o el coste de GPU importan | Sin API de IA en la ruta básica |
| [whisperX](../fichas/whisperx.md) | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. | necesitas subtítulos precisos o diarización | Sin API de IA en la ruta básica |
| [NVIDIA NeMo Speech](../fichas/nemo.md) | Framework de NVIDIA para entrenar y usar modelos de voz: reconocimiento, síntesis y más. | necesitas ASR de máxima precisión y tienes GPU | Sin API de IA en la ruta básica |

## Síntesis y clonación de voz

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Kokoro](../fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | quieres TTS ligero, rápido y con licencia permisiva | Sin API de IA en la ruta básica |
| [OmniVoice-Studio](../fichas/omnivoice-studio.md) | Alternativa local y open source a ElevenLabs: clonación, diseño y conversión de voz en una app. | quieres suite de voz completa local (dictado + clonación + dubbing) | Sin API de IA en la ruta básica |
| [GPT-SoVITS](../fichas/gpt-sovits.md) | Clonación de voz y TTS con solo un minuto de audio, con interfaz web para entrenar. | quieres entrenar una voz con pocos datos | Sin API de IA en la ruta básica |
| [VibeVoice](../fichas/vibevoice.md) | Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. | quieres generar podcasts o diálogos largos | Sin API de IA en la ruta básica |
| [TTS](../fichas/tts.md) | Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. | quieres flexibilidad y varios modelos en una librería | Sin API de IA en la ruta básica |
| [VoxCPM](../fichas/voxcpm.md) | Modelo de texto a voz sin tokenizador que clona voces con naturalidad y expresividad alta. | quieres voz muy natural o clonada y tienes GPU | Sin API de IA en la ruta básica |
| [RVC WebUI](../fichas/rvc.md) | Conversión de voz: entrena un modelo con menos de 10 minutos de audio y transforma una voz en otra. | quieres convertir una voz grabada en otra | Sin API de IA en la ruta básica |
| [Fish Speech](../fichas/fish-speech.md) | Sistema de texto a voz open source de alta calidad con clonación de voz multilingüe. | buscas TTS de alta calidad con clonación | Sin API de IA en la ruta básica |
| [Chatterbox](../fichas/chatterbox.md) | Modelo de texto a voz open source de Resemble AI con clonación de voz y control de emoción. | quieres clonar voces con calidad alta y licencia libre | Sin API de IA en la ruta básica |
| [IndexTTS](../fichas/index-tts.md) | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. | necesitas controlar duración y emoción de la voz | Sin API de IA en la ruta básica |
| [CosyVoice](../fichas/cosyvoice.md) | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. | necesitas TTS multilingüe en streaming | Sin API de IA en la ruta básica |
| [supertonic](../fichas/supertonic.md) | Motor de texto a voz que ofrece modelos y ejemplos para sintetizar audio en dispositivos y navegadores compatibles. | quieres voz local en tiempo real y sin nube | Sin API de IA en la ruta básica |
| [edge-tts](../fichas/edge-tts.md) | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. | quieres generar narración sin instalar un modelo de voz local | Sin API de IA en la ruta básica |
| [LuxTTS](../fichas/luxtts.md) | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. | necesitas TTS con clonación muy rápido | Sin API de IA en la ruta básica |

## Agentes de voz en tiempo real

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Pipecat](../fichas/pipecat.md) | Framework open source para agentes de voz y apps multimodales en tiempo real. | construyes un agente de voz en Python | Depende de la ruta elegida |
| [LiveKit Agents](../fichas/livekit-agents.md) | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. | necesitas agentes de voz escalables con WebRTC | Depende de la ruta elegida |

## Edición, grabación y subtítulos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FFmpeg](../fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | necesitas convertir, cortar, mezclar o transmitir audio y video desde la línea de comandos o un script | Sin API de IA en la ruta básica |
| [MoviePy](../fichas/moviepy.md) | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | ensamblas video desde Python y quieres controlar cada clip por código | Sin API de IA en la ruta básica |
| [OpenCut](../fichas/opencut.md) | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. | quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut | Sin API de IA en la ruta básica |
| [OBS Studio](../fichas/obs-studio.md) | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. | necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas | Sin API de IA en la ruta básica |
| [LosslessCut](../fichas/lossless-cut.md) | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. | necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica | Sin API de IA en la ruta básica |
| [OpenScreen](../fichas/openscreen.md) | App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a Screen Studio. | quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio | Sin API de IA en la ruta básica |
| [VideoLingo](../fichas/videolingo.md) | App que subtitula, traduce y dobla videos de forma automática: ASR con timestamps por palabra, traducción con LLM y TTS. | quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar | Depende de la ruta elegida |
| [palmier-pro](../fichas/palmier-pro.md) | Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios actuales. | usas macOS y quieres explorar edición de video asistida por agentes | Depende de la ruta elegida |
| [DaVinci Resolve MCP](../fichas/davinci-resolve-mcp.md) | Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render. | editas en DaVinci Resolve y quieres que un agente MCP automatice montaje, render o metadatos | Sin API de IA en la ruta básica |

## Video programático y con agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [HyperFrames](../fichas/hyperframes.md) | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. | quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva | Sin API de IA en la ruta básica |
| [Remotion Agent Skills](../fichas/skills-remotion.md) | Skills oficiales de Remotion para que tu agente de código cree videos con React. | haces videos con Remotion y un agente | Sin API de IA en la ruta básica |
| [Manim (ManimGL)](../fichas/manim.md) | Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL. | quieres animaciones matemáticas o técnicas precisas definidas en código Python | Sin API de IA en la ruta básica |
| [OpenMontage](../fichas/openmontage.md) | Convierte tu agente de código en un estudio de producción de video completo. | quieres producir videos completos con un agente | Sin API de IA en la ruta básica |
| [remotion](../fichas/remotion.md) | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. | generas video a escala con React y quieres variantes parametrizadas | Sin API de IA en la ruta básica |
| [manim](../fichas/manim-community.md) | Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. | necesitas animaciones matemáticas precisas y reproducibles | Sin API de IA en la ruta básica |
| [video-use](../fichas/video-use.md) | Herramienta para editar videos con agentes de código como Claude Code, de los creadores de browser-use. | quieres editar videos pidiéndoselo a tu agente | Sin API de IA en la ruta básica |
| [rea-video](../fichas/rea-video.md) | Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md. | quieres estudiar o recrear la estructura de un video de referencia | Sin API de IA en la ruta básica |
| [videofy_minimal](../fichas/videofy-minimal.md) | Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. | quieres reels simples ya, sin montar un pipeline entero | API de IA necesaria |
| [Remotion Superpowers](../fichas/remotion-superpowers.md) | Plugin que convierte Remotion en un estudio de video para Claude Code, Codex o Gemini CLI. | usas Remotion con un agente y quieres producción completa | Sin API de IA en la ruta básica |

## Video generativo y pipelines automáticos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | quieres producir videos cortos narrados a partir de un tema sin editar a mano | Depende de la ruta elegida |
| [Wan2.2](../fichas/wan2-2.md) | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más | Sin API de IA en la ruta básica |
| [HunyuanVideo](../fichas/hunyuanvideo.md) | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. | tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | Sin API de IA en la ruta básica |
| [WanGP](../fichas/wan2gp.md) | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. | quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano | Sin API de IA en la ruta básica |
| [LTX-Video](../fichas/ltx-video.md) | Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado. | necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x | Sin API de IA en la ruta básica |
| [short-video-factory](../fichas/short-video-factory.md) | Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. | quieres producir variantes de videos promocionales desde materiales existentes | Depende de la ruta elegida |
| [AI-Youtube-Shorts-Generator](../fichas/ai-youtube-shorts-generator.md) | Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM. | quieres convertir videos largos en una primera selección de shorts | Depende de la ruta elegida |

## Música y audio generativo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [AudioCraft](../fichas/audiocraft.md) | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio | Sin API de IA en la ruta básica |
| [ACE-Step-1.5](../fichas/ace-step-1-5.md) | Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. | necesitas experimentar con generación musical en tu propio equipo | Sin API de IA en la ruta básica |
| [Music-Megathread](../fichas/music-megathread.md) | Directorio de reproductores, herramientas, servicios y otros recursos relacionados con música. | buscas recursos musicales y quieres comparar opciones desde una lista | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
- [Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
