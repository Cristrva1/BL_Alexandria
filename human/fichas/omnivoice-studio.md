[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Síntesis y clonación de voz

# 🎚️ OmniVoice-Studio

> Alternativa local y open source a ElevenLabs: clonación, diseño y conversión de voz en una app.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 107k | AGPL-3.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Reúne STT, TTS y dubbing en una sola app sin claves de API.

## Por qué destaca

Combina dictado, clonación y dubbing en una sola app de escritorio sin nube ni API keys, algo poco común; está en beta activa y es un proyecto pequeño y poco conocido, conviene validarlo antes de depender de él.

## Cómo funciona

Envuelve modelos locales de STT y TTS en una interfaz de escritorio Python que orquesta transcripción, síntesis y reemplazo de audio en el video, manteniendo todo on-device.

## Instalación rápida

Clonar el repo e instalar dependencias Python según el README (sin paquete publicado); el README recomienda correr desde fuente por estar en beta.

## Casos de uso

- Dictado de escritorio sin nube
- Doblar videos a otros idiomas
- Clonar voz sin API keys

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres suite de voz completa local (dictado + clonación + dubbing) | solo necesitas TTS simple por CLI/librería (TTS) o estabilidad de producción |

**Limitaciones:** Beta activa: cosas pueden romperse entre releases; proyecto pequeño, valida mantenimiento antes de adoptarlo.

## Stack y modelos

- **Stack:** desktop/Python
- **Modelos / API:** Modelos locales.
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [VideoLingo](videolingo.md) | 19.1k | App que subtitula, traduce y dobla videos de forma automática: ASR con timestamps por palabra, traducción con LLM y TTS. |

## Enlaces

- 🐙 GitHub: [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- 🌐 Web: <https://voicestudio.sh>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
