[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Transcripción (voz a texto)

# 🎙️ whisper.cpp

> Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.2k | MIT | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

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

Transcribe voz a texto en local sin Python ni GPU obligatoria, incluso en tiempo real. Base de muchas apps de dictado.

## Por qué destaca

Rendimiento excelente en hardware común y en Apple Silicon.

## Cómo funciona

Implementa el modelo Whisper sobre ggml con cuantización y aceleración Metal, CUDA o Vulkan.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Compilador o binario compatible, y un modelo Whisper de la variante seleccionada.

1. Elige el binario o la compilación para tu sistema según el README.
2. Prepara un modelo y un audio de muestra en los formatos del ejemplo.
3. Ejecuta la transcripción y mide calidad y tiempo en tu propio equipo.

[Instrucciones originales de instalación](https://github.com/ggml-org/whisper.cpp/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whisper.cpp para mi objetivo y necesito pasos guiados. Lee https://github.com/ggml-org/whisper.cpp/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Transcribir reuniones en local
- Dictado en apps de escritorio
- Subtítulos sin internet

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres transcribir en local sin GPU | necesitas marcas de tiempo por palabra y diarización; mira `whisperx` |

## Stack y modelos

- **Stack:** C++, C
- **Etiquetas:** `stt` `audio` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FFmpeg](ffmpeg.md) | 67.3k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [faster-whisper](faster-whisper.md) | 26.8k | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. |
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |

## Enlaces

- 🐙 GitHub: [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ggml-org/whisper.cpp/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
