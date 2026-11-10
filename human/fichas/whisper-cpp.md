[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Transcripción (voz a texto)

# 🎙️ whisper.cpp

> Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 55.1k | MIT | C++ | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Transcribe voz a texto en local sin Python ni GPU obligatoria, incluso en tiempo real. Base de muchas apps de dictado.

## Por qué destaca

Rendimiento excelente en hardware común y en Apple Silicon.

## Cómo funciona

Implementa el modelo Whisper sobre ggml con cuantización y aceleración Metal, CUDA o Vulkan.

## Instalación rápida

`brew install whisper-cpp` o compila con `cmake`; descarga un modelo con el script incluido.

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
- **Modelos / API:** Modelos Whisper.
- **Etiquetas:** `stt` `audio` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FFmpeg](ffmpeg.md) | 66.9k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [faster-whisper](faster-whisper.md) | 26.6k | Reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. |
| [whisper](whisper.md) | 112k | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |

## Enlaces

- 🐙 GitHub: [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
