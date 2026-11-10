[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Transcripción (voz a texto)

# 🎯 whisperX

> Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 25.2k | BSD-2-Clause | Python | 2026-10-22 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Convierte la salida "por segmento" de Whisper en timings palabra a palabra con etiqueta de speaker.

## Por qué destaca

Es la opción de referencia cuando los timings finos y el "quién habla" importan, muy usada para subtítulos de reels y entrevistas; combina tres componentes probados en un solo pipeline.

## Cómo funciona

Usa faster-whisper para la transcripción, modelos wav2vec2 (torchaudio) para forzar la alineación fonema/palabra y pyannote para la diarización de hablantes; todo orquestado desde Python.

## Instalación rápida

`pip install whisperx` (requiere PyTorch y, para diarización, un token de Hugging Face con acceso aceptado a los modelos pyannote).

## Casos de uso

- Subtítulos bien ajustados para reels/entrevistas
- Separar hablantes en podcasts
- Exportar SRT/VTT con timings de palabra

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas subtítulos precisos o diarización | te basta texto plano (whisper) o no quieres gestionar tokens de HF |

## Stack y modelos

- **Stack:** Python, faster-whisper, wav2vec2, pyannote
- **Modelos / API:** Local.
- **Etiquetas:** `stt` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 112k | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [NVIDIA NeMo Speech](nemo.md) | 18.7k | Framework de NVIDIA para entrenar y usar modelos de voz: reconocimiento, síntesis y más. |

## Enlaces

- 🐙 GitHub: [m-bain/whisperX](https://github.com/m-bain/whisperX)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
