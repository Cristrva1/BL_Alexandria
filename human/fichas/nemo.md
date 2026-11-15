[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Transcripción (voz a texto)

# 🎙️ NVIDIA NeMo Speech

> Framework de NVIDIA para entrenar y usar modelos de voz: reconocimiento, síntesis y más.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 18.7k | Apache-2.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Qué es

Incluye modelos de ASR como Parakeet y Canary, que lideran rankings de transcripción, y herramientas para afinarlos.

## Por qué destaca

Modelos de reconocimiento de voz de primer nivel y abiertos.

## Cómo funciona

Colección de modelos y recetas sobre PyTorch Lightning optimizadas para GPUs NVIDIA.

## Instalación rápida

`pip install "nemo_toolkit[asr]"`.

## Casos de uso

- Transcripción de alta precisión
- Afinar ASR con tu vocabulario
- Investigación en voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas ASR de máxima precisión y tienes GPU | quieres algo simple; mira `faster-whisper` |

**Limitaciones:** Pesado de instalar; requiere GPU para entrenar.

## Stack y modelos

- **Stack:** Python, PyTorch
- **Modelos / API:** Modelos propios (Parakeet, Canary).
- **Etiquetas:** `stt` `tts` `audio` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pipecat](pipecat.md) | 17.2k | Framework open source para agentes de voz y apps multimodales en tiempo real. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |

## Enlaces

- 🐙 GitHub: [NVIDIA-NeMo/Speech](https://github.com/NVIDIA-NeMo/Speech)
- 🌐 Web: <https://docs.nvidia.com/nemo/speech/nightly/index.html>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
