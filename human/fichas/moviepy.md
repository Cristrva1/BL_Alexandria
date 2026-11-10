[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🎬 MoviePy

> Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 15.1k | MIT | Python | 2026-08-26 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

MoviePy convierte la edición de video en código Python: abres clips, los recortas, superpones texto o imágenes, mezclas audio y exportas a MP4, WebM o GIF. Es la pieza de ensamblaje habitual en pipelines que generan videos cortos a partir de imágenes, voz sintética y subtítulos.

## Por qué destaca

Es la librería de edición de video más usada en Python, con una API legible y efectos incluidos. La versión 2.0 modernizó la API, aunque rompe la compatibilidad con el código escrito para v1.

## Cómo funciona

Importa fotogramas y audio como arrays de NumPy, aplica efectos y composiciones sobre clips (`VideoFileClip`, `TextClip`, `CompositeVideoClip`) y vuelve a codificar con FFmpeg, que obtiene mediante imageio-ffmpeg.

## Instalación rápida

`pip install moviepy` (Python 3.9+; trae FFmpeg mediante imageio-ffmpeg).

## Casos de uso

- Montar reels con imágenes, voz TTS y subtítulos por script
- Recortar clips y superponer títulos o marcas de agua en lote
- Generar GIFs y videos de demo de forma reproducible

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ensamblas video desde Python y quieres controlar cada clip por código | prefieres plantillas en React (`remotion`) o en HTML (`hyperframes`), o solo necesitas cortar sin recodificar (`lossless-cut`) |

**Limitaciones:** Es más lento que llamar a FFmpeg directamente porque pasa cada fotograma por NumPy, y el código escrito para v1 hay que adaptarlo a v2.

## Stack y modelos

- **Stack:** Python, NumPy, Pillow, FFmpeg
- **Modelos / API:** No usa LLM: compone el material que generan otras herramientas.
- **Etiquetas:** `video` `audio` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |
| [Kokoro](kokoro.md) | 10k | Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. |
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [remotion](remotion.md) | 72.2k | Framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4. |
| [HyperFrames](hyperframes.md) | 82k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. |

## Enlaces

- 🐙 GitHub: [Zulko/moviepy](https://github.com/Zulko/moviepy)
- 🌐 Web: <https://zulko.github.io/moviepy/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
