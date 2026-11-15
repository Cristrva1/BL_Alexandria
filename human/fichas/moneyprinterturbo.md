[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 MoneyPrinterTurbo

> App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 142k | MIT | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

MoneyPrinterTurbo automatiza la producción de shorts: das un tema o palabras clave y escribe el guion con un LLM, busca clips en Pexels o Pixabay (o usa los tuyos o video generado por IA), genera locución, subtítulos y música, y monta el resultado en 9:16, 16:9 o 1:1. Se usa desde WebUI, API, CLI o pidiéndoselo a un agente con su skill.

## Por qué destaca

Cubre todo el flujo de un canal de videos cortos sin editar a mano y es muy configurable: decenas de proveedores de LLM y TTS (incluida Edge TTS, gratuita), generación en lote y publicación directa en TikTok, Instagram y YouTube Shorts.

## Cómo funciona

Python con Streamlit para la WebUI y FastAPI para la API. El LLM genera el guion y los términos de búsqueda, se descargan clips de stock, se sintetiza la voz, los subtítulos salen del TTS o de faster-whisper y MoviePy compone el video.

## Instalación rápida

`pip install mpt` y luego `mpt webui` (Python 3.11+), o `docker compose -f docker-compose.release.yml up`. Añade en la WebUI las claves del LLM y de Pexels o Pixabay.

## Casos de uso

- Producir shorts en lote para TikTok o YouTube Shorts
- Convertir un tema o artículo en un video narrado con subtítulos
- Prototipar formatos de video antes de invertir en edición

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres producir videos cortos narrados a partir de un tema sin editar a mano | necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage` |

**Limitaciones:** El resultado depende del material de stock y del LLM, así que los videos tienden a ser genéricos; revisa derechos y normas de cada plataforma antes de publicar en masa.

## Stack y modelos

- **Stack:** Python, Streamlit, FastAPI, MoviePy, faster-whisper
- **Modelos / API:** Agnóstico: OpenAI, Claude, Gemini, DeepSeek, Qwen, Ollama y gateways compatibles para el guion; TTS de Edge (gratis), Azure, ElevenLabs, Kokoro o Chatterbox, entre otros.
- **Etiquetas:** `video` `automation` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Kokoro](kokoro.md) | 10k | Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. |
| [faster-whisper](faster-whisper.md) | 26.6k | Reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenMontage](openmontage.md) | — | Convierte tu agente de código en un estudio de producción de video completo. |
| [videofy_minimal](videofy-minimal.md) | 656 | Herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo. |

## Enlaces

- 🐙 GitHub: [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
