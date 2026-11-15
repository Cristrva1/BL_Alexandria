[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video programático y con agentes

# 📲 videofy_minimal

> Herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 656 | Apache-2.0 | TypeScript | 2026-03-13 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Encadena TTS/STT y montaje en un solo flujo para pasar de texto a reel con lo mínimo.

## Por qué destaca

Prioriza la simplicidad para pasar de texto a reel rápido; es un proyecto pequeño y experimental, conviene revisar su estado antes de usarlo en serio.

## Cómo funciona

Combina TTS/STT y un montador de video local para sincronizar narración, texto y fondos en un clip corto, orquestando los pasos sin depender de servicios externos.

## Instalación rápida

Clonar el repo e instalar dependencias Python/Node según el README (sin paquete publicado). Requiere los modelos TTS/STT que el proyecto utilice.

## Casos de uso

- Transformar noticias/contenido en reels
- Video corto rápido sin pipeline complejo
- Prototipos de texto-a-video local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres reels simples ya, sin montar un pipeline entero | necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy) |

**Limitaciones:** Proyecto pequeño y experimental; valida mantenimiento y calidad antes de depender de él.

## Stack y modelos

- **Stack:** Python/Node
- **Modelos / API:** Local + TTS/STT.
- **Etiquetas:** `video` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 112k | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |
| [supertonic](supertonic.md) | 13.8k | Motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoneyPrinterTurbo](moneyprinterturbo.md) | 142k | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. |

## Enlaces

- 🐙 GitHub: [schibsted/videofy_minimal](https://github.com/schibsted/videofy_minimal)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
