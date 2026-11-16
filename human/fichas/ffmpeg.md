[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ FFmpeg

> Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 67.3k | NOASSERTION | C | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

FFmpeg, conjunto de librerías y herramientas para procesar contenido multimedia. Licencia mayoritariamente LGPL con componentes opcionales GPL (GitHub muestra NOASSERTION). Es infraestructura fundamental (~67k estrellas en el espejo de GitHub).

## ¿Qué hace?

Convierte, corta, filtra, codifica, decodifica y transmite audio, vídeo y subtítulos. Lo forman libavcodec, libavformat, libavfilter, libavdevice, libswresample, libswscale y libavutil, y las herramientas `ffmpeg`, `ffplay` y `ffprobe`. Casi todas las herramientas de vídeo y audio con IA dependen de él.

## ¿Cómo lo hace?

Se instala con paquetes del sistema o binarios precompilados, o se compila con `./configure` eligiendo códecs. Los parches se envían al Forgejo del proyecto (code.ffmpeg.org) o a la lista ffmpeg-devel, no por pull requests de GitHub.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [whisper](whisper.md) | Whisper requiere FFmpeg para leer audio. | Instala FFmpeg antes de Whisper. |
| [yt-dlp](yt-dlp.md) | yt-dlp usa FFmpeg para unir y convertir formatos. | Instala FFmpeg en el PATH. |
| [MoviePy](moviepy.md) | MoviePy usa FFmpeg para leer y escribir vídeo. | Se instala con imageio-ffmpeg o usa el del sistema. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (43). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ACE-Step-1.5](ace-step-1-5.md) · [AI-Youtube-Shorts-Generator](ai-youtube-shorts-generator.md) · [Arcads AI Video Skill Pack](arcads-claude-code.md) · [AudioCraft](audiocraft.md) · [Concat](concat.md) · [CosyVoice](cosyvoice.md) · [DaVinci Resolve MCP](davinci-resolve-mcp.md) · [earshot](earshot.md) · [edge-tts](edge-tts.md) · [FaceFusion](facefusion.md) · [Fish Speech](fish-speech.md) · [gallery-dl](gallery-dl.md) · [GPT-SoVITS](gpt-sovits.md) · [HandBrake](handbrake.md) · [IndexTTS](index-tts.md) · [Jellyfin](jellyfin.md) · [Kdenlive](kdenlive.md) · [lemo-opuscar](lemo-opuscar.md) · [LosslessCut](lossless-cut.md) · [LTX-2](ltx-2.md) · [Manim (ManimGL)](manim.md) · [manim](manim-community.md) · [mediabunny](mediabunny.md) · [motionmaxxing](motionmaxxing.md) · [OpenMontage](openmontage.md) · [OpenRV](openrv.md) · [pencil](pencil.md) · [pyannote.audio](pyannote-audio.md) · [rea-video](rea-video.md) · [rnnoise](rnnoise.md) · [rubberband](rubberband.md) · [RVC WebUI](rvc.md) · [short-video-factory](short-video-factory.md) · [Shotcut](shotcut.md) · [spotDL](spotdl.md) · [taste-skill](taste-skill.md) · [Trigger.dev](trigger-dev.md) · [video-use](video-use.md) · [videofy_minimal](videofy-minimal.md) · [VideoLingo](videolingo.md) · [VoiceStudio](omnivoice-studio.md) · [VoxCPM](voxcpm.md) · [whisper.cpp](whisper-cpp.md)

**Notas:** Sin alternativas declaradas. Al distribuir binarios, revisa si incluyen componentes GPL o códecs con patentes.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FFmpeg/FFmpeg/blob/master/README.md) · [2](https://ffmpeg.org/documentation.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa IA ni API; codecs y componentes del build pueden tener licencias distintas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Descarga un build para tu sistema o sigue la compilación; el repositorio GitHub es un espejo de la fuente oficial |
| Coste | Sin pago a un modelo en la ruta básica. No usa IA ni API; codecs y componentes del build pueden tener licencias distintas |
| Equipo | Preparación según la ruta elegida. Binario apropiado al sistema; archivo de video propio; espacio de salida |

Descarga un build para tu sistema o sigue la compilación; el repositorio GitHub es un espejo de la fuente oficial

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario apropiado al sistema
- archivo de video propio
- espacio de salida

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://ffmpeg.org/download.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FFmpeg para mi objetivo y necesito pasos guiados. Lee https://ffmpeg.org/download.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte una copia de un video breve y comprueba duración, audio y formato con ffprobe.

**Qué comprobar:** La salida se reproduce y conserva las pistas esperadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir un video para una plataforma
- Extraer audio de una grabación propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir un video para una plataforma; Extraer audio de una grabación propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Descarga un build para tu sistema o sigue la compilación; el repositorio GitHub es un espejo de la fuente oficial

## Stack y modelos

- **Stack:** Binario apropiado al sistema; archivo de video propio; espacio de salida
- **Etiquetas:** `video` `audio` `automation` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)
- 🌐 Web: <https://ffmpeg.org/>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FFmpeg/FFmpeg/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
