[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ VideoLingo

> App que subtitula, traduce y dobla videos de forma automática: ASR con timestamps por palabra, traducción con LLM y TTS.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 19.1k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

VideoLingo reúne en una interfaz Streamlit el trabajo de un equipo de subtitulado: descarga el video con yt-dlp, lo transcribe con alineación por palabra, segmenta y traduce los subtítulos con un LLM y, si quieres, genera el doblaje con voz sintética o clonada. Produce archivos SRT y videos subtitulados o doblados.

## Por qué destaca

Cuida el subtítulo, no solo la transcripción: corta frases con NLP y LLM, mantiene un glosario para traducir con coherencia y revisa la traducción. Incluye una API HTTP local para usarlo desde agentes o scripts.

## Cómo funciona

Pipeline Python por etapas con caché y reanudación: Qwen3-ASR con ForcedAligner en local (MLX en Apple Silicon), un LLM compatible con OpenAI para segmentar y traducir, y TTS intercambiable (GPT-SoVITS, Edge TTS, OpenAI, Fish Audio, F5-TTS).

## Instalación rápida

`git clone https://github.com/Huanshere/VideoLingo.git && cd VideoLingo && uv run start.py` (en Windows, `OneKeyStart.bat`). Luego configura URL, clave y modelo del LLM en la barra lateral.

## Casos de uso

- Subtitular en español videos de YouTube en inglés
- Doblar tutoriales a otro idioma con voz clonada
- Generar subtítulos bilingües para cursos o entrevistas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres subtitular, traducir o doblar videos de punta a punta con una interfaz y sin programar | solo necesitas transcribir o subtitular en el idioma original; te basta `whisperx` o `faster-whisper` |

**Limitaciones:** El doblaje no asigna voces distintas por hablante, la traducción consume tokens de una API de LLM y, si clonas una voz, necesitas el consentimiento de su dueño.

## Stack y modelos

- **Stack:** Python, Streamlit, Qwen3-ASR, yt-dlp, FFmpeg
- **Modelos / API:** Requiere un LLM con API compatible con OpenAI que devuelva JSON estructurado; ASR local (Qwen3-ASR) o en la nube (ElevenLabs, MAI-Transcribe) y TTS local o en la nube.
- **Etiquetas:** `video` `stt` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [yt-dlp](yt-dlp.md) | 207k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |
| [GPT-SoVITS](gpt-sovits.md) | 64.7k | Clonación de voz y TTS con solo un minuto de audio, con interfaz web para entrenar. |
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OmniVoice-Studio](omnivoice-studio.md) | 107k | Alternativa local y open source a ElevenLabs: clonación, diseño y conversión de voz en una app. |

## Enlaces

- 🐙 GitHub: [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo)
- 🌐 Web: <https://docs.videolingo.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
