[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Transcripción (voz a texto)

# ⚡ faster-whisper

> Reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 26.6k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Es el mismo modelo de OpenAI, pero con un runtime de inferencia optimizado.

## Por qué destaca

Es la versión preferida en producción por su relación velocidad/calidad y su bajo consumo; muy adoptada en pipelines y servidores de transcripción (WhisperX la usa internamente).

## Cómo funciona

Ejecuta los mismos modelos Whisper convertidos al runtime CTranslate2, con cuantización int8/float16 que acelera tanto CPU como GPU y reduce la VRAM necesaria frente al Whisper original.

## Instalación rápida

`pip install faster-whisper` (necesita ffmpeg). El modelo se descarga al primer uso; en GPU requiere drivers CUDA compatibles con CTranslate2.

## Casos de uso

- Procesar lotes de audio/video con menos latencia
- Transcripción en producción/servidor
- Reducir coste de GPU manteniendo calidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| el rendimiento, la memoria o el coste de GPU importan | necesitas alineación/diarización (whisperX) o te basta el CLI oficial |

## Stack y modelos

- **Stack:** Python, CTranslate2
- **Modelos / API:** Modelos Whisper locales.
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

- 🐙 GitHub: [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
