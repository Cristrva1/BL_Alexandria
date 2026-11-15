[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 Wan2.2

> Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 18.5k | Apache-2.0 | Python | 2026-09-21 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Wan2.2 publica pesos y código de inferencia de varios modelos de video: texto a video e imagen a video de 14B (MoE), un modelo híbrido de 5B que genera 720p a 24 fps en una RTX 4090, video guiado por voz (S2V) y animación o sustitución de personajes (Animate). Es la base de muchos flujos de ComfyUI y Diffusers.

## Por qué destaca

Combina calidad cercana a modelos cerrados con licencia Apache 2.0 y un ecosistema amplio: integración oficial en ComfyUI y Diffusers, y herramientas de la comunidad para GPU con poca memoria.

## Cómo funciona

Modelo de difusión con Mixture-of-Experts que reparte el denoising entre expertos según el paso, más un VAE de alta compresión (16x16x4) en el modelo 5B. El prompt se puede ampliar con un LLM Qwen local o por API.

## Instalación rápida

`git clone https://github.com/Wan-Video/Wan2.2.git && cd Wan2.2 && pip install -r requirements.txt` (torch 2.4+); descarga pesos con `huggingface-cli download Wan-AI/Wan2.2-TI2V-5B --local-dir ./Wan2.2-TI2V-5B` y ejecuta `python generate.py --task ti2v-5B`.

## Casos de uso

- Generar clips 720p desde un prompt para anuncios o reels
- Animar la foto de un producto o personaje con imagen a video
- Crear el video de una persona hablando a partir de un audio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más | tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados |

**Limitaciones:** Los modelos de 14B piden unos 80 GB de VRAM sin offload, y el de 5B al menos 24 GB.

## Stack y modelos

- **Stack:** Python, PyTorch, FlashAttention, Diffusers
- **Modelos / API:** Pesos propios en local (T2V/I2V-A14B, TI2V-5B, S2V-14B, Animate-14B); la ampliación opcional del prompt usa Qwen local o la API de DashScope.
- **Etiquetas:** `video` `inference` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |
| [Real-ESRGAN](real-esrgan.md) | 37.4k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |
| [CosyVoice](cosyvoice.md) | 24.4k | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [HunyuanVideo](hunyuanvideo.md) | 12.8k | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. |
| [LTX-Video](ltx-video.md) | 11.4k | Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado. |

## Enlaces

- 🐙 GitHub: [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2)
- 🌐 Web: <https://wan.video>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
