[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🎚️ OmniVoice-Studio

> Alternativa local y open source a ElevenLabs: clonación, diseño y conversión de voz en una app.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 111k | AGPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

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

Reúne STT, TTS y dubbing en una sola app sin claves de API.

## Por qué destaca

Combina dictado, clonación y dubbing en una sola app de escritorio sin nube ni API keys, algo poco común; está en beta activa y es un proyecto pequeño y poco conocido, conviene validarlo antes de depender de él.

## Cómo funciona

Envuelve modelos locales de STT y TTS en una interfaz de escritorio Python que orquesta transcripción, síntesis y reemplazo de audio en el video, manteniendo todo on-device.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/debpalash/VoiceStudio/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OmniVoice-Studio para mi objetivo y necesito pasos guiados. Lee https://github.com/debpalash/VoiceStudio/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [VideoLingo](videolingo.md) | 19.3k | App que subtitula, traduce y dobla videos de forma automática: ASR con timestamps por palabra, traducción con LLM y TTS. |

## Enlaces

- 🐙 GitHub: [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- 🌐 Web: <https://voicestudio.sh>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/debpalash/VoiceStudio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
