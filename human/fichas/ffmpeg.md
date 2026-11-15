[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ FFmpeg

> Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 67.3k | NOASSERTION | C | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

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

FFmpeg es la base multimedia sobre la que se apoyan casi todos los editores, reproductores y pipelines de video. Incluye el CLI `ffmpeg` para convertir, recortar, concatenar, mezclar, quemar subtítulos y transmitir, `ffprobe` para inspeccionar archivos y las librerías libav* para integrarlo en tu propio software.

## Por qué destaca

Es el estándar de facto: soporta prácticamente todos los códecs, contenedores y protocolos (RTMP, HLS, RTSP) y lo usan por dentro herramientas como OBS, LosslessCut, MoviePy o Remotion.

## Cómo funciona

Las librerías libavcodec, libavformat y libavfilter decodifican, procesan con un grafo de filtros y vuelven a codificar; el CLI encadena entradas, filtros y salidas en un solo comando. Admite aceleración por hardware (NVENC, QSV, VideoToolbox).

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/FFmpeg/FFmpeg/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FFmpeg para mi objetivo y necesito pasos guiados. Lee https://github.com/FFmpeg/FFmpeg/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `video` `audio` `automation` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |
| [yt-dlp](yt-dlp.md) | 208k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)
- 🌐 Web: <https://ffmpeg.org/>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/FFmpeg/FFmpeg/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
