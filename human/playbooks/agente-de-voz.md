[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 📞 Agente de voz en tiempo real

> **Objetivo:** Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [Pipecat](../fichas/pipecat.md), [faster-whisper](../fichas/faster-whisper.md), [Kokoro](../fichas/kokoro.md)

**Prepara:** Micrófono, auriculares y un modelo de conversación configurado

**Primera prueba propuesta:** Prueba una frase corta de entrada, respuesta y reproducción

**Qué comprobar:** La transcripción y la voz de salida corresponden a la conversación

Configura también el LLM; transcripción y voz locales no hacen local todo el flujo ni incluyen telefonía

**Otras rutas, no piezas que debas sumar:** [LiveKit Agents](../fichas/livekit-agents.md)

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  pipecat["Pipecat"] --> faster_whisper["faster-whisper"]
  faster_whisper["faster-whisper"] --> kokoro["Kokoro"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [Pipecat](../fichas/pipecat.md) | Orquesta la conversación: turnos, interrupciones y pipeline | 17.3k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 2 | [faster-whisper](../fichas/faster-whisper.md) | Transcripción rápida (voz a texto) | 26.8k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 3 | [litellm](../fichas/litellm.md) | Acceso al LLM que decide la respuesta | 63.3k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 4 | [Kokoro](../fichas/kokoro.md) | Voz sintética ligera (texto a voz) | 10.1k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 5 | [LiveKit Agents](../fichas/livekit-agents.md) | Alternativa con transporte WebRTC y telefonía integrados | 15.2k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |

## 🔌 Cómo se conecta

Pipecat encadena transporte de audio, detección de voz, STT, LLM y TTS con manejo de interrupciones. faster-whisper transcribe, el LLM (vía LiteLLM) decide qué decir y Kokoro lo sintetiza. LiveKit Agents es la alternativa si quieres WebRTC y telefonía SIP resueltos de serie.

## 🚫 Cuándo NO usar esta receta

Si te basta con dictado o transcripción sin respuesta hablada, usa solo Whisper o faster-whisper. Si no quieres operar infraestructura, un servicio gestionado de voz es más rápido de lanzar.

## 🔁 Variantes

- En lugar de [Pipecat](../fichas/pipecat.md): [LiveKit Agents](../fichas/livekit-agents.md)
- En lugar de [faster-whisper](../fichas/faster-whisper.md): [whisper.cpp](../fichas/whisper-cpp.md)
- En lugar de [Kokoro](../fichas/kokoro.md): [LuxTTS](../fichas/luxtts.md), [edge-tts](../fichas/edge-tts.md)
- En lugar de [LiveKit Agents](../fichas/livekit-agents.md): [Pipecat](../fichas/pipecat.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
