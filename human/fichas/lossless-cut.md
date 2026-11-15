[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ LosslessCut

> App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 45.9k | GPL-2.0 | TypeScript | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

LosslessCut es una interfaz gráfica sobre FFmpeg para recortar y fusionar archivos de video y audio sin recompresión. Sirve para descartar gigas de material de cámara, GoPro o dron, extraer o reemplazar pistas, cambiar de contenedor (MKV a MP4) y editar metadatos o capítulos, en Windows, macOS y Linux.

## Por qué destaca

Al copiar los streams en vez de recodificar, los cortes son casi instantáneos y sin pérdida incluso en archivos enormes. Detecta escenas, silencios y fotogramas negros, y ofrece CLI y API HTTP para automatizarlo.

## Cómo funciona

App Electron con React que reproduce con el motor HTML5 de Chromium (o con FFmpeg para formatos no soportados) y exporta desde el archivo original con FFmpeg en modo copia de stream, sin tocar los fotogramas.

## Instalación rápida

Descarga gratis el binario para Windows, macOS o Linux desde GitHub Releases, o instálalo desde Mac App Store, Microsoft Store o Snap Store. Ya incluye FFmpeg.

## Casos de uso

- Recortar horas de grabación de cámara o dron en segundos
- Extraer o reemplazar pistas de audio y subtítulos
- Dividir por escenas o silencios antes de editar un reel

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica | necesitas efectos, transiciones o un montaje con capas; mira `opencut` o, por código, `moviepy` |

**Limitaciones:** Sin recodificar, los cortes solo caen exactos en fotogramas clave, así que el punto de corte puede desplazarse unos fotogramas.

## Stack y modelos

- **Stack:** TypeScript, Electron, React, FFmpeg
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `video` `audio` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [yt-dlp](yt-dlp.md) | 207k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [mifi/lossless-cut](https://github.com/mifi/lossless-cut)
- 🌐 Web: <https://losslesscut.app/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
