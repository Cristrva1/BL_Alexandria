[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Música y audio generativo

# 🎵 AudioCraft

> Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 23.8k | MIT | Jupyter Notebook | 2026-03-03 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

AudioCraft reúne el código de inferencia y entrenamiento de los modelos de audio generativo de Meta: MusicGen (música a partir de texto o melodía), AudioGen (efectos de sonido), MAGNeT, JASCO (música condicionada por acordes y batería), el códec neuronal EnCodec y AudioSeal para marcas de agua. Está orientada a investigación, aunque se usa mucho para crear música de fondo.

## Por qué destaca

Es la referencia abierta en generación de música por texto, con modelos de varios tamaños en Hugging Face y código de entrenamiento para crear o ajustar los tuyos.

## Cómo funciona

MusicGen es un transformer autorregresivo que genera los tokens discretos de EnCodec condicionado por texto (y opcionalmente por una melodía); después EnCodec o Multi Band Diffusion los decodifican a audio.

## Instalación rápida

`python -m pip install 'torch==2.1.0'` y luego `python -m pip install -U audiocraft` (Python 3.9). Conviene tener ffmpeg instalado; los modelos se descargan de Hugging Face al primer uso.

## Casos de uso

- Generar música de fondo original para videos o podcasts
- Crear efectos de sonido (lluvia, tráfico, pasos) desde texto
- Investigar o ajustar modelos de audio generativo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas generar música o efectos de sonido por texto en local, o investigar modelos de audio | necesitas uso comercial (los pesos son CC-BY-NC 4.0) o generar voz hablada; para voz mira `kokoro` o `chatterbox` |

**Limitaciones:** Los pesos tienen licencia CC-BY-NC 4.0, sin uso comercial, y el proyecto tiene poca actividad reciente y dependencias fijadas a PyTorch 2.1.

## Stack y modelos

- **Stack:** Python, PyTorch, EnCodec, Hugging Face Hub
- **Modelos / API:** Modelos propios de Meta en local (MusicGen, AudioGen, MAGNeT, JASCO), descargados de Hugging Face.
- **Etiquetas:** `audio` `inference` `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |
| [remotion](remotion.md) | 72.2k | Framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4. |
| [FFmpeg](ffmpeg.md) | 66.9k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |

## Enlaces

- 🐙 GitHub: [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
