[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🎬 MoviePy

> Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.2k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

MoviePy convierte la edición de video en código Python: abres clips, los recortas, superpones texto o imágenes, mezclas audio y exportas a MP4, WebM o GIF. Es la pieza de ensamblaje habitual en pipelines que generan videos cortos a partir de imágenes, voz sintética y subtítulos.

## Por qué destaca

Es la librería de edición de video más usada en Python, con una API legible y efectos incluidos. La versión 2.0 modernizó la API, aunque rompe la compatibilidad con el código escrito para v1.

## Cómo funciona

Importa fotogramas y audio como arrays de NumPy, aplica efectos y composiciones sobre clips (`VideoFileClip`, `TextClip`, `CompositeVideoClip`) y vuelve a codificar con FFmpeg, que obtiene mediante imageio-ffmpeg.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install moviepy
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/Zulko/moviepy/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MoviePy para mi objetivo y necesito pasos guiados. Lee https://github.com/Zulko/moviepy/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `video` `audio` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [remotion](remotion.md) | 73.2k | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. |
| [HyperFrames](hyperframes.md) | 84.4k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. |

## Enlaces

- 🐙 GitHub: [Zulko/moviepy](https://github.com/Zulko/moviepy)
- 🌐 Web: <https://zulko.github.io/moviepy/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Zulko/moviepy/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
