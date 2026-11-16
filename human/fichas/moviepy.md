[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 🎬 MoviePy

> Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.2k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MoviePy, librería Python para editar vídeo por código, de @Zulko. Licencia MIT. Es madura (~15k estrellas, v2.2.1); la v2.0 introdujo cambios incompatibles y la v1 ya no se mantiene.

## ¿Qué hace?

Corta, concatena, inserta títulos, compone, aplica efectos y procesa audio y vídeo, incluido GIF. Es flexible pero más lenta que usar FFmpeg directamente.

## ¿Cómo lo hace?

Requiere Python 3.9+ y se instala con `pip install moviepy`; usa FFmpeg (incluido vía imageio-ffmpeg o uno personalizado). Funciona en Windows, macOS y Linux.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [whisperX](whisperx.md) | Subtítulos con marcas por palabra. (combinación por arquitectura) | Genera SRT y móntalo con TextClip. |
| [Kokoro](kokoro.md) | Narración local. (combinación por arquitectura) | Genera el audio y añádelo como AudioFileClip. |
| [FFmpeg](ffmpeg.md) | Motor de lectura y escritura. | Viene vía imageio-ffmpeg o usa el del sistema. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (8). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[AudioCraft](audiocraft.md) · [edge-tts](edge-tts.md) · [faster-whisper](faster-whisper.md) · [LivePortrait](liveportrait.md) · [LosslessCut](lossless-cut.md) · [LuxTTS](luxtts.md) · [Manim (ManimGL)](manim.md) · [WanGP](wan2gp.md)

**Notas:** Alternativas (elige una): remotion, hyperframes. Se quita comfyui de las combinaciones (sin relación directa).

Estado en GitHub: activo · último push 2026-08-26 · última versión publicada v2.2.1 (2025-05-21) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Zulko/moviepy/blob/master/README.md)</sub>

## Ver similares

Grupo **Video y escenas por código**: MoviePy ocupa la posición 4 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [HyperFrames](hyperframes.md) ⭐ recomendado | 73 | Si quieres que un agente componga video desde HTML con HeyGen HyperFrames. |
| 2 | [remotion](remotion.md) | 68 | Si sabes React y quieres generar videos programáticos con calidad de producción (revisa su licencia). |
| 3 | [Motion Canvas](motion-canvas.md) | 56 | Si haces animaciones explicativas en TypeScript con editor en tiempo real. |
| 4 | **MoviePy** (esta ficha) | 54 | Si editas video desde Python (cortes, composición, texto) sin interfaz. |
| 5 | [Revideo](revideo.md) | 51 | Si quieres renderizar videos desde código TypeScript como API o servicio. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El montaje no requiere modelo; renderizar consume CPU, memoria y disco; medios y fuentes tienen licencias propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. v2 cambia APIs como subclipped y with_volume_scaled; los ejemplos v1 no son intercambiables |
| Coste | Sin pago a un modelo en la ruta básica. El montaje no requiere modelo; renderizar consume CPU, memoria y disco; medios y fuentes tienen licencias propias |
| Equipo | Preparación según la ruta elegida. Python; FFmpeg según instalación; fuente tipográfica para títulos; video de prueba |

v2 cambia APIs como subclipped y with_volume_scaled; los ejemplos v1 no son intercambiables

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- FFmpeg según instalación
- fuente tipográfica para títulos
- video de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://zulko.github.io/moviepy/getting_started/install.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MoviePy para mi objetivo y necesito pasos guiados. Lee https://zulko.github.io/moviepy/getting_started/install.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Recorta diez segundos y superpone un título usando el ejemplo v2.

**Qué comprobar:** El render conserva duración y audio y muestra el título.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar variantes de un video
- Componer clips y rótulos desde Python

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar variantes de un video; Componer clips y rótulos desde Python | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** v2 cambia APIs como subclipped y with_volume_scaled; los ejemplos v1 no son intercambiables

## Stack y modelos

- **Stack:** Python; FFmpeg según instalación; fuente tipográfica para títulos; video de prueba
- **Etiquetas:** `video` `audio` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [remotion](remotion.md) | 73.2k | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. |
| [HyperFrames](hyperframes.md) | 84.4k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. |

## Enlaces

- 🐙 GitHub: [Zulko/moviepy](https://github.com/Zulko/moviepy)
- 🌐 Web: <https://zulko.github.io/moviepy/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Zulko/moviepy/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
