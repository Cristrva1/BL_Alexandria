[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Transcripción (voz a texto)

# 📝 whisper

> Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 112k | MIT | Python | 2026-08-31 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Cubre también identificación de idioma y traducción al inglés en la misma red.

## Por qué destaca

Es la referencia de facto del STT abierto, base de innumerables forks y servicios de transcripción; su robustez a ruido y acentos lo convirtió en el punto de partida habitual para cualquier pipeline de voz.

## Cómo funciona

Red Transformer encoder-decoder entrenada con audio supervisado a escala; corre sobre PyTorch y procesa el audio en ventanas de 30 s con desplazamiento. La CLI `whisper` genera SRT/VTT/JSON con timestamps.

## Instalación rápida

`pip install -U openai-whisper` (requiere ffmpeg en el sistema y PyTorch). El modelo se descarga al primer uso según `--model` (de `tiny` a `large`).

## Casos de uso

- `whisper grabacion.mp3 --model medium` para SRT con timestamps
- Subtitulado automático de video
- Transcripción de reuniones y podcasts

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres la referencia robusta y no te obsesiona la latencia | necesitas más velocidad (faster-whisper) o timings por palabra (whisperX) |

## Stack y modelos

- **Stack:** Python 3.9+, PyTorch
- **Modelos / API:** Local (modelos tiny→large), sin API de pago.
- **Etiquetas:** `stt` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper.cpp](whisper-cpp.md) | 55.1k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |

## Enlaces

- 🐙 GitHub: [openai/whisper](https://github.com/openai/whisper)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
