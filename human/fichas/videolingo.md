[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ VideoLingo

> App que subtitula, traduce y dobla videos de forma automática: ASR con timestamps por palabra, traducción con LLM y TTS.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.3k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

VideoLingo reúne en una interfaz Streamlit el trabajo de un equipo de subtitulado: descarga el video con yt-dlp, lo transcribe con alineación por palabra, segmenta y traduce los subtítulos con un LLM y, si quieres, genera el doblaje con voz sintética o clonada. Produce archivos SRT y videos subtitulados o doblados.

## Por qué destaca

Cuida el subtítulo, no solo la transcripción: corta frases con NLP y LLM, mantiene un glosario para traducir con coherencia y revisa la traducción. Incluye una API HTTP local para usarlo desde agentes o scripts.

## Cómo funciona

Pipeline Python por etapas con caché y reanudación: Qwen3-ASR con ForcedAligner en local (MLX en Apple Silicon), un LLM compatible con OpenAI para segmentar y traducir, y TTS intercambiable (GPT-SoVITS, Edge TTS, OpenAI, Fish Audio, F5-TTS).

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/Huanshere/VideoLingo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar VideoLingo para mi objetivo y necesito pasos guiados. Lee https://github.com/Huanshere/VideoLingo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `video` `stt` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [yt-dlp](yt-dlp.md) | 208k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |
| [GPT-SoVITS](gpt-sovits.md) | 65.1k | Clonación de voz y TTS con solo un minuto de audio, con interfaz web para entrenar. |
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OmniVoice-Studio](omnivoice-studio.md) | 111k | Alternativa local y open source a ElevenLabs: clonación, diseño y conversión de voz en una app. |

## Enlaces

- 🐙 GitHub: [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo)
- 🌐 Web: <https://docs.videolingo.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Huanshere/VideoLingo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
