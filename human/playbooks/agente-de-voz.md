[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 📞 Agente de voz en tiempo real

> **Objetivo:** Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

## 🗺️ Cómo fluye

```mermaid
flowchart LR
  Usuario["Usuario"] -->|audio| pipecat["Pipecat"]
  pipecat["Pipecat"] -->|STT| faster_whisper["faster-whisper"]
  faster_whisper["faster-whisper"] -->|texto| litellm["litellm"]
  litellm["litellm"] -->|respuesta| kokoro["Kokoro"]
  kokoro["Kokoro"] -->|TTS| pipecat["Pipecat"]
  pipecat["Pipecat"] -->|voz| Usuario["Usuario"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [Pipecat](../fichas/pipecat.md) | Orquesta la conversación: turnos, interrupciones y pipeline | 17.2k | `pip install "pipecat-ai[daily,openai,cartesia]"` |
| 2 | [faster-whisper](../fichas/faster-whisper.md) | Transcripción rápida (voz a texto) | 26.6k | `pip install faster-whisper` |
| 3 | [litellm](../fichas/litellm.md) | Acceso al LLM que decide la respuesta | 63k | `pip install litellm` |
| 4 | [Kokoro](../fichas/kokoro.md) | Voz sintética ligera (texto a voz) | 10k | `pip install kokoro soundfile` |
| 5 | [LiveKit Agents](../fichas/livekit-agents.md) | Alternativa con transporte WebRTC y telefonía integrados | 15.2k | `pip install "livekit-agents[openai,silero,deepgram]"` |

## 🔌 Cómo se conecta

Pipecat encadena transporte de audio, detección de voz, STT, LLM y TTS con manejo de interrupciones. faster-whisper transcribe, el LLM (vía LiteLLM) decide qué decir y Kokoro lo sintetiza. LiveKit Agents es la alternativa si quieres WebRTC y telefonía SIP resueltos de serie.

## 🚫 Cuándo NO usar esta receta

Si te basta con dictado o transcripción sin respuesta hablada, usa solo Whisper o faster-whisper. Si no quieres operar infraestructura, un servicio gestionado de voz es más rápido de lanzar.

## 🔁 Variantes

- En lugar de [Pipecat](../fichas/pipecat.md): [LiveKit Agents](../fichas/livekit-agents.md)
- En lugar de [faster-whisper](../fichas/faster-whisper.md): [whisper.cpp](../fichas/whisper-cpp.md)
- En lugar de [Kokoro](../fichas/kokoro.md): [Chatterbox](../fichas/chatterbox.md), [TTS](../fichas/tts.md), [LuxTTS](../fichas/luxtts.md)
- En lugar de [LiveKit Agents](../fichas/livekit-agents.md): [Pipecat](../fichas/pipecat.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
