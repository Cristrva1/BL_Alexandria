[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Síntesis y clonación de voz

# 🎙️ TTS

> Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 46.2k | MPL-2.0 | Python | 2024-08-16 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Reúne en una sola librería modelos como Tacotron, VITS y XTTS, con CLI y API Python.

## Por qué destaca

Es uno de los kits TTS abiertos más completos y reutilizados; aunque Coqui cerró, su código y modelos (XTTSv2, 16+ idiomas) siguen siendo referencia comunitaria y se mantienen vía fork `coqui-tts`.

## Cómo funciona

Librería Python que carga modelos sobre PyTorch y expone CLI (`tts`) y API para generar o clonar voz; XTTS permite clonación zero-shot a partir de unos segundos de referencia.

## Instalación rápida

`pip install TTS` (o `coqui-tts`, el fork mantenido). Requiere PyTorch; la clonación con XTTS mejora con GPU.

## Casos de uso

- Locuciones automáticas para anuncios/demos
- Clonación de voz zero-shot
- Base para apps de voz multilingües

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres flexibilidad y varios modelos en una librería | necesitas tiempo real puro (supertonic) o soporte comercial (Coqui está inactivo) |

**Limitaciones:** El proyecto original de Coqui está inactivo; usa el fork `coqui-tts` para fixes; revisar licencia de XTTS antes de uso comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, modelos descargables
- **Modelos / API:** Local.
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kokoro](kokoro.md) | 10k | Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. |

## Enlaces

- 🐙 GitHub: [coqui-ai/TTS](https://github.com/coqui-ai/TTS)
- 🌐 Web: <http://coqui.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
