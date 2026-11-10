[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ FFmpeg

> Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 66.9k | Otra (ver repo) | C | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

FFmpeg es la base multimedia sobre la que se apoyan casi todos los editores, reproductores y pipelines de video. Incluye el CLI `ffmpeg` para convertir, recortar, concatenar, mezclar, quemar subtítulos y transmitir, `ffprobe` para inspeccionar archivos y las librerías libav* para integrarlo en tu propio software.

## Por qué destaca

Es el estándar de facto: soporta prácticamente todos los códecs, contenedores y protocolos (RTMP, HLS, RTSP) y lo usan por dentro herramientas como OBS, LosslessCut, MoviePy o Remotion.

## Cómo funciona

Las librerías libavcodec, libavformat y libavfilter decodifican, procesan con un grafo de filtros y vuelven a codificar; el CLI encadena entradas, filtros y salidas en un solo comando. Admite aceleración por hardware (NVENC, QSV, VideoToolbox).

## Instalación rápida

`brew install ffmpeg` (macOS) o `sudo apt install ffmpeg` (Linux); en Windows, descarga un binario desde ffmpeg.org.

## Casos de uso

- Convertir y comprimir videos para redes con un solo comando
- Extraer el audio de un video antes de transcribirlo
- Quemar subtítulos SRT y concatenar clips en un pipeline

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas convertir, cortar, mezclar o transmitir audio y video desde la línea de comandos o un script | quieres una interfaz gráfica para cortar sin pérdida (`lossless-cut`) o componer video desde Python con objetos (`moviepy`) |

**Limitaciones:** La sintaxis de filtros tiene una curva de aprendizaje alta, y algunos componentes opcionales (x264, x265) son GPL, lo que cambia las condiciones de redistribución.

## Stack y modelos

- **Stack:** C, ensamblador (x86/ARM), libavcodec, libavformat, libavfilter
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `video` `audio` `automation` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 112k | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |
| [yt-dlp](yt-dlp.md) | 207k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)
- 🌐 Web: <https://ffmpeg.org/>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
