[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ CosyVoice

> Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.4k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Síntesis de voz natural con clonación y control de estilo, también en streaming.

## Por qué destaca

Muy buena calidad y soporte de streaming de baja latencia.

## Cómo funciona

Modelo de lenguaje para tokens de voz y un modelo de flujo para generar el audio.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CosyVoice para mi objetivo y necesito pasos guiados. Lee https://github.com/QwenAudio/CosyVoice/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- TTS en streaming para agentes
- Clonación de voz multilingüe
- Servicios de voz propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas TTS multilingüe en streaming | quieres instalación muy simple; mira `kokoro` |

## Stack y modelos

- **Stack:** Python, PyTorch
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pipecat](pipecat.md) | 17.3k | Framework open source para agentes de voz y apps multimodales en tiempo real. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Fish Speech](fish-speech.md) | 33.7k | Sistema de texto a voz open source de alta calidad con clonación de voz multilingüe. |
| [IndexTTS](index-tts.md) | 25.1k | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. |

## Enlaces

- 🐙 GitHub: [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice)
- 🌐 Web: <https://funaudiollm.github.io/cosyvoice3>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
