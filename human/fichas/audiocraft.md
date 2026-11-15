[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Música y audio generativo

# 🎵 AudioCraft

> Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.9k | MIT | Jupyter Notebook | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

AudioCraft reúne el código de inferencia y entrenamiento de los modelos de audio generativo de Meta: MusicGen (música a partir de texto o melodía), AudioGen (efectos de sonido), MAGNeT, JASCO (música condicionada por acordes y batería), el códec neuronal EnCodec y AudioSeal para marcas de agua. Está orientada a investigación, aunque se usa mucho para crear música de fondo.

## Por qué destaca

Es la referencia abierta en generación de música por texto, con modelos de varios tamaños en Hugging Face y código de entrenamiento para crear o ajustar los tuyos.

## Cómo funciona

MusicGen es un transformer autorregresivo que genera los tokens discretos de EnCodec condicionado por texto (y opcionalmente por una melodía); después EnCodec o Multi Band Diffusion los decodifican a audio.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/facebookresearch/audiocraft/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AudioCraft para mi objetivo y necesito pasos guiados. Lee https://github.com/facebookresearch/audiocraft/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `audio` `inference` `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |
| [remotion](remotion.md) | 73.2k | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. |
| [FFmpeg](ffmpeg.md) | 67.3k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |

## Enlaces

- 🐙 GitHub: [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/facebookresearch/audiocraft/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
