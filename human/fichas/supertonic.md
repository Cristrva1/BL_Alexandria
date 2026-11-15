[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Síntesis y clonación de voz

# 🔊 supertonic

> Motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 13.8k | MIT | Swift | 2026-09-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

> ⚠️ Archivado en GitHub: ya no recibe cambios.

## Qué es

Apunta a latencia mínima con privacidad total, sin nube ni llamadas de API.

## Por qué destaca

Logra latencia muy baja con privacidad total al no depender de la nube, atractivo para voz en tiempo real y asistentes on-device; sus modelos se publican gratis en Hugging Face.

## Cómo funciona

Ejecuta modelos ONNX acelerados por WebGPU desde el navegador o por Rust/Python en escritorio, con inferencia optimizada para mantener el tiempo de primer audio bajo.

## Instalación rápida

Clonar el repo y seguir el ejemplo Node/Python, o probar la demo WebGPU (no hay paquete único oficial). Requiere un navegador/entorno con WebGPU o runtime ONNX adecuado.

## Casos de uso

- Respuesta por voz en tiempo real
- Locuciones de anuncios local
- Asistentes on-device sin enviar audio a la nube

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres voz local en tiempo real y sin nube | priorizas clonación de máxima fidelidad (VoxCPM) o flexibilidad multi-modelo (TTS) |

## Stack y modelos

- **Stack:** Python, Rust (ONNX), Node.js, WebGPU
- **Modelos / API:** Modelos propios de Hugging Face, gratis.
- **Etiquetas:** `tts` `audio`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [supertone-oss-archive/supertonic](https://github.com/supertone-oss-archive/supertonic)
- 🌐 Web: <https://huggingface.co/spaces/Supertone/supertonic-3>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
