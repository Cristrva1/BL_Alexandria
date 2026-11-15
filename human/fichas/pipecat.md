[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Agentes de voz en tiempo real

# 📞 Pipecat

> Framework open source para agentes de voz y apps multimodales en tiempo real.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 17.2k | BSD-2-Clause | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Encadena STT, LLM y TTS con interrupciones y baja latencia, y conecta con teléfono, WebRTC o WhatsApp.

## Por qué destaca

Muy flexible, con decenas de proveedores de voz y transporte.

## Cómo funciona

Pipelines de frames procesan audio y texto en streaming entre servicios.

## Instalación rápida

`pip install "pipecat-ai[daily,openai,cartesia]"` según tus proveedores.

## Casos de uso

- Agente telefónico de atención
- Asistente de voz en web
- Tutor por voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes un agente de voz en Python | quieres infraestructura WebRTC gestionada; mira `livekit-agents` |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** Agnóstico: OpenAI, Anthropic, Gemini y TTS/STT variados.
- **Etiquetas:** `audio` `agents` `stt` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kokoro](kokoro.md) | 10k | Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. |
| [whisper.cpp](whisper-cpp.md) | 55.1k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LiveKit Agents](livekit-agents.md) | 15.2k | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. |

## Enlaces

- 🐙 GitHub: [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)
- 🌐 Web: <https://pipecat.ai>
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
