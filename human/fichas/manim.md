[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video programático y con agentes

# 🎞️ Manim (ManimGL)

> Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 96.3k | MIT | Python | 2026-09-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Manim permite describir en código Python escenas con fórmulas LaTeX, gráficas, geometría y transformaciones animadas, y exportarlas a video. Este repo es ManimGL, la versión original que Grant Sanderson usa en 3Blue1Brown; la edición comunitaria (ManimCommunity/manim) es un fork más estable y mejor documentado.

## Por qué destaca

Da una precisión difícil de lograr con un editor: cada objeto y transición se define por código y se puede versionar. Es la herramienta detrás de los videos de 3Blue1Brown y de muchos canales educativos.

## Cómo funciona

Cada escena es una clase Python con objetos matemáticos (Mobjects) y animaciones encadenadas; ManimGL las dibuja con OpenGL en una ventana interactiva y escribe el video con FFmpeg.

## Instalación rápida

`pip install manimgl` (Python 3.10+, con FFmpeg, OpenGL y, si quieres fórmulas, LaTeX; en Linux también Pango). Prueba con `manimgl example_scenes.py OpeningManimExample`.

## Casos de uso

- Animar demostraciones y fórmulas para clases o YouTube
- Visualizar algoritmos o conceptos de machine learning
- Generar videos explicativos a partir de código escrito por un LLM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres animaciones matemáticas o técnicas precisas definidas en código Python | buscas estabilidad y documentación para empezar (usa la edición comunitaria ManimCommunity/manim) o motion graphics de marketing; mira `remotion` o `hyperframes` |

**Limitaciones:** La API cambia entre versiones y no es compatible con la edición comunitaria, así que el código y los tutoriales de una no sirven para la otra.

## Stack y modelos

- **Stack:** Python, OpenGL, FFmpeg, LaTeX
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `video` `dataviz` `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kokoro](kokoro.md) | 10k | Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. |
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |
| [FFmpeg](ffmpeg.md) | 66.9k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |

## Enlaces

- 🐙 GitHub: [3b1b/manim](https://github.com/3b1b/manim)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
