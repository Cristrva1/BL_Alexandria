[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 11. Generación de Imagen & Visión](11-generaci-n-de-imagen-visi-n.md) · [13. Documentos & Presentaciones ➡️](13-documentos-presentaciones.md)

# 🎬 12. Audio, Voz & Video

> Transcripción, síntesis y clonación de voz, agentes de voz, edición y subtítulos, video programático, video generativo y música.

**42 repos** · 7 subcategorías · ⭐ 1.6M estrellas en total · 🆕 18 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | 55.1k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | `brew install whisper-cpp` |
| [Kokoro](../fichas/kokoro.md) | 10k | Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. | `pip install kokoro soundfile` |
| [Pipecat](../fichas/pipecat.md) | 17.2k | Framework open source para agentes de voz y apps multimodales en tiempo real. | `pip install "pipecat-ai[daily,openai,cartesia]"` |
| [FFmpeg](../fichas/ffmpeg.md) | 66.9k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | `brew install ffmpeg` |
| [MoviePy](../fichas/moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | `pip install moviepy` |
| [HyperFrames](../fichas/hyperframes.md) | 82k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. | `npx hyperframes init my-video` |
| [Remotion Agent Skills](../fichas/skills-remotion.md) | 6.8k | Skills oficiales de Remotion para que tu agente de código cree videos con React. | `npx skills add remotion-dev/skills` |
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | 142k | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | `pip install mpt` |
| [Wan2.2](../fichas/wan2-2.md) | 18.5k | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | `git clone https://github.com/Wan-Video/Wan2.2.git && cd Wan2.2 && pip install -r requirements.txt` |
| [AudioCraft](../fichas/audiocraft.md) | 23.8k | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | `python -m pip install 'torch==2.1.0'` |

## 🧭 Subcategorías

- [Transcripción (voz a texto)](#transcripción-voz-a-texto) — 5 repos
- [Síntesis y clonación de voz](#síntesis-y-clonación-de-voz) — 13 repos
- [Agentes de voz en tiempo real](#agentes-de-voz-en-tiempo-real) — 2 repos
- [Edición, grabación y subtítulos](#edición-grabación-y-subtítulos) — 8 repos
- [Video programático y con agentes](#video-programático-y-con-agentes) — 8 repos
- [Video generativo y pipelines automáticos](#video-generativo-y-pipelines-automáticos) — 5 repos
- [Música y audio generativo](#música-y-audio-generativo) — 1 repos

## Transcripción (voz a texto)

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [whisper.cpp](../fichas/whisper-cpp.md) 🆕 | 55.1k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | quieres transcribir en local sin GPU | 🟢 |
| [whisper](../fichas/whisper.md) | 112k | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. | quieres la referencia robusta y no te obsesiona la latencia | 🟡 |
| [faster-whisper](../fichas/faster-whisper.md) | 26.6k | Reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. | el rendimiento, la memoria o el coste de GPU importan | 🟡 |
| [whisperX](../fichas/whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. | necesitas subtítulos precisos o diarización | 🟡 |
| [NVIDIA NeMo Speech](../fichas/nemo.md) | 18.7k | Framework de NVIDIA para entrenar y usar modelos de voz: reconocimiento, síntesis y más. | necesitas ASR de máxima precisión y tienes GPU | 🔴 |

## Síntesis y clonación de voz

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Kokoro](../fichas/kokoro.md) 🆕 | 10k | Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. | quieres TTS ligero, rápido y con licencia permisiva | 🟢 |
| [OmniVoice-Studio](../fichas/omnivoice-studio.md) | 107k | Alternativa local y open source a ElevenLabs: clonación, diseño y conversión de voz en una app. | quieres suite de voz completa local (dictado + clonación + dubbing) | 🟡 |
| [GPT-SoVITS](../fichas/gpt-sovits.md) 🆕 | 64.7k | Clonación de voz y TTS con solo un minuto de audio, con interfaz web para entrenar. | quieres entrenar una voz con pocos datos | 🟡 |
| [VibeVoice](../fichas/vibevoice.md) | 56.9k | Modelos de voz de frontera de Microsoft para podcasts largos con varios hablantes y tiempo real. | quieres generar podcasts o diálogos largos | 🔴 |
| [TTS](../fichas/tts.md) | 46.2k | Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. | quieres flexibilidad y varios modelos en una librería | 🟡 |
| [VoxCPM](../fichas/voxcpm.md) | 42.2k | Modelo de texto a voz sin tokenizador que clona voces con naturalidad y expresividad alta. | quieres voz muy natural o clonada y tienes GPU | 🔴 |
| [RVC WebUI](../fichas/rvc.md) 🆕 | 39.1k | Conversión de voz: entrena un modelo con menos de 10 minutos de audio y transforma una voz en otra. | quieres convertir una voz grabada en otra | 🟡 |
| [Fish Speech](../fichas/fish-speech.md) 🆕 | 33.7k | Sistema de texto a voz open source de alta calidad con clonación de voz multilingüe. | buscas TTS de alta calidad con clonación | 🟡 |
| [Chatterbox](../fichas/chatterbox.md) 🆕 | 27.7k | Modelo de texto a voz open source de Resemble AI con clonación de voz y control de emoción. | quieres clonar voces con calidad alta y licencia libre | 🟢 |
| [IndexTTS](../fichas/index-tts.md) 🆕 | 25k | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. | necesitas controlar duración y emoción de la voz | 🟡 |
| [CosyVoice](../fichas/cosyvoice.md) 🆕 | 24.4k | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. | necesitas TTS multilingüe en streaming | 🟡 |
| [supertonic](../fichas/supertonic.md) | 13.8k | Motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU. | quieres voz local en tiempo real y sin nube | 🟡 |
| [LuxTTS](../fichas/luxtts.md) | 5.5k | Modelo de TTS ligero con clonación de voz que genera audio hasta 150 veces más rápido que tiempo real. | necesitas TTS con clonación muy rápido | 🟢 |

## Agentes de voz en tiempo real

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Pipecat](../fichas/pipecat.md) 🆕 | 17.2k | Framework open source para agentes de voz y apps multimodales en tiempo real. | construyes un agente de voz en Python | 🟡 |
| [LiveKit Agents](../fichas/livekit-agents.md) 🆕 | 15.2k | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. | necesitas agentes de voz escalables con WebRTC | 🟡 |

## Edición, grabación y subtítulos

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [FFmpeg](../fichas/ffmpeg.md) | 66.9k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | necesitas convertir, cortar, mezclar o transmitir audio y video desde la línea de comandos o un script | 🟢 |
| ⭐ [MoviePy](../fichas/moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | ensamblas video desde Python y quieres controlar cada clip por código | 🟢 |
| [OpenCut](../fichas/opencut.md) | 98k | Editor de video libre con línea de tiempo, alternativa a CapCut, que funciona en el navegador y procesa en tu equipo. | quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut | 🟡 |
| [OBS Studio](../fichas/obs-studio.md) 🆕 | 79.3k | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. | necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas | 🟢 |
| [LosslessCut](../fichas/lossless-cut.md) | 45.9k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. | necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica | 🟢 |
| [OpenScreen](../fichas/openscreen.md) | 40k | App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a Screen Studio. | quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio | 🟢 |
| [VideoLingo](../fichas/videolingo.md) 🆕 | 19.1k | App que subtitula, traduce y dobla videos de forma automática: ASR con timestamps por palabra, traducción con LLM y TTS. | quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar | 🟡 |
| [DaVinci Resolve MCP](../fichas/davinci-resolve-mcp.md) | 4k | Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render. | editas en DaVinci Resolve y quieres que un agente MCP automatice montaje, render o metadatos | 🟡 |

## Video programático y con agentes

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [HyperFrames](../fichas/hyperframes.md) | 82k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. | quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva | 🟢 |
| ⭐ [Remotion Agent Skills](../fichas/skills-remotion.md) | 6.8k | Skills oficiales de Remotion para que tu agente de código cree videos con React. | haces videos con Remotion y un agente | 🟢 |
| [Manim (ManimGL)](../fichas/manim.md) 🆕 | 96.3k | Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL. | quieres animaciones matemáticas o técnicas precisas definidas en código Python | 🟡 |
| [remotion](../fichas/remotion.md) | 72.2k | Framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4. | generas video a escala con React y quieres variantes parametrizadas | 🟡 |
| [video-use](../fichas/video-use.md) | 30.8k | Herramienta para editar videos con agentes de código como Claude Code, de los creadores de browser-use. | quieres editar videos pidiéndoselo a tu agente | 🟢 |
| [videofy_minimal](../fichas/videofy-minimal.md) | 656 | Herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo. | quieres reels simples ya, sin montar un pipeline entero | 🟢 |
| [Remotion Superpowers](../fichas/remotion-superpowers.md) | 164 | Plugin que convierte Remotion en un estudio de video para Claude Code, Codex o Gemini CLI. | usas Remotion con un agente y quieres producción completa | 🟢 |
| [OpenMontage](../fichas/openmontage.md) | — | Convierte tu agente de código en un estudio de producción de video completo. | quieres producir videos completos con un agente | 🟡 |

## Video generativo y pipelines automáticos

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) 🆕 | 142k | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. | quieres producir videos cortos narrados a partir de un tema sin editar a mano | 🟡 |
| ⭐ [Wan2.2](../fichas/wan2-2.md) 🆕 | 18.5k | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. | quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más | 🔴 |
| [HunyuanVideo](../fichas/hunyuanvideo.md) 🆕 | 12.8k | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. | tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | 🔴 |
| [LTX-Video](../fichas/ltx-video.md) 🆕 | 11.4k | Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado. | necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x | 🔴 |
| [WanGP](../fichas/wan2gp.md) | — | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. | quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano | 🔴 |

## Música y audio generativo

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [AudioCraft](../fichas/audiocraft.md) 🆕 | 23.8k | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. | necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio | 🟡 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### whisper.cpp, whisper, faster-whisper

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [whisper.cpp](../fichas/whisper-cpp.md) | 55.1k | quieres transcribir en local sin GPU | necesitas marcas de tiempo por palabra y diarización; mira `whisperx` |
| [whisper](../fichas/whisper.md) | 112k | quieres la referencia robusta y no te obsesiona la latencia | necesitas más velocidad (faster-whisper) o timings por palabra (whisperX) |
| [faster-whisper](../fichas/faster-whisper.md) | 26.6k | el rendimiento, la memoria o el coste de GPU importan | necesitas alineación/diarización (whisperX) o te basta el CLI oficial |

### whisperX, NVIDIA NeMo Speech

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [whisperX](../fichas/whisperx.md) | 25.2k | necesitas subtítulos precisos o diarización | te basta texto plano (whisper) o no quieres gestionar tokens de HF |
| [NVIDIA NeMo Speech](../fichas/nemo.md) | 18.7k | necesitas ASR de máxima precisión y tienes GPU | quieres algo simple; mira `faster-whisper` |

### Kokoro, GPT-SoVITS, TTS, Fish Speech, Chatterbox, IndexTTS, CosyVoice

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Kokoro](../fichas/kokoro.md) | 10k | quieres TTS ligero, rápido y con licencia permisiva | necesitas clonar voces; mira `chatterbox` |
| [GPT-SoVITS](../fichas/gpt-sovits.md) | 64.7k | quieres entrenar una voz con pocos datos | prefieres zero-shot sin entrenar; mira `chatterbox` |
| [TTS](../fichas/tts.md) | 46.2k | quieres flexibilidad y varios modelos en una librería | necesitas tiempo real puro (supertonic) o soporte comercial (Coqui está inactivo) |
| [Fish Speech](../fichas/fish-speech.md) | 33.7k | buscas TTS de alta calidad con clonación | necesitas licencia comercial sin restricciones; mira `chatterbox` |
| [Chatterbox](../fichas/chatterbox.md) | 27.7k | quieres clonar voces con calidad alta y licencia libre | necesitas algo muy ligero en CPU; mira `kokoro` |
| [IndexTTS](../fichas/index-tts.md) | 25k | necesitas controlar duración y emoción de la voz | buscas licencia totalmente libre; revisa su licencia |
| [CosyVoice](../fichas/cosyvoice.md) | 24.4k | necesitas TTS multilingüe en streaming | quieres instalación muy simple; mira `kokoro` |

### OmniVoice-Studio, VideoLingo

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [OmniVoice-Studio](../fichas/omnivoice-studio.md) | 107k | quieres suite de voz completa local (dictado + clonación + dubbing) | solo necesitas TTS simple por CLI/librería (TTS) o estabilidad de producción |
| [VideoLingo](../fichas/videolingo.md) | 19.1k | quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar | solo necesitas transcribir o subtitular en el idioma original; te basta `whisperx` o `faster-whisper` |

### Pipecat, LiveKit Agents

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Pipecat](../fichas/pipecat.md) | 17.2k | construyes un agente de voz en Python | quieres infraestructura WebRTC gestionada; mira `livekit-agents` |
| [LiveKit Agents](../fichas/livekit-agents.md) | 15.2k | necesitas agentes de voz escalables con WebRTC | quieres algo ligero sin servidor de medios; mira `pipecat` |

### HyperFrames, MoviePy, remotion

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [HyperFrames](../fichas/hyperframes.md) | 82k | quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva | tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual |
| [MoviePy](../fichas/moviepy.md) | 15.1k | ensamblas video desde Python y quieres controlar cada clip por código | prefieres plantillas en React (`remotion`) o en HTML (`hyperframes`), o solo necesitas cortar sin recodificar (`lossless-cut`) |
| [remotion](../fichas/remotion.md) | 72.2k | generas video a escala con React y quieres variantes parametrizadas | trabajas en Python (moviepy) o buscas un editor visual |

### OBS Studio, OpenScreen

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [OBS Studio](../fichas/obs-studio.md) | 79.3k | necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas | lo que necesitas es montar o recortar el video ya grabado; usa `opencut` o `lossless-cut` |
| [OpenScreen](../fichas/openscreen.md) | 40k | quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio | necesitas un proyecto mantenido; usa su continuación getopenscreen/openscreen, o `obs-studio` para grabación y streaming generales |

### MoneyPrinterTurbo, video-use, videofy_minimal, Remotion Superpowers, OpenMontage

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | 142k | quieres producir videos cortos narrados a partir de un tema sin editar a mano | necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage` |
| [video-use](../fichas/video-use.md) | 30.8k | quieres editar videos pidiéndoselo a tu agente | quieres una app de edición visual; mira `opencut` |
| [videofy_minimal](../fichas/videofy-minimal.md) | 656 | quieres reels simples ya, sin montar un pipeline entero | necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy) |
| [Remotion Superpowers](../fichas/remotion-superpowers.md) | 164 | usas Remotion con un agente y quieres producción completa | no usas Remotion |
| [OpenMontage](../fichas/openmontage.md) | — | quieres producir videos completos con un agente | solo necesitas editar clips; mira `video-use` |

### Wan2.2, HunyuanVideo, LTX-Video

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Wan2.2](../fichas/wan2-2.md) | 18.5k | quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más | tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados |
| [HunyuanVideo](../fichas/hunyuanvideo.md) | 12.8k | tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente |
| [LTX-Video](../fichas/ltx-video.md) | 11.4k | necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x | empiezas un proyecto nuevo; Lightricks recomienda LTX-2.5 (repo Lightricks/LTX-2), o mira `wan2-2` y `wan2gp` |

## 🧪 Recetas que usan esta categoría

- [🎬 Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
- [📞 Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
