[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 HunyuanVideo

> Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 12.8k | Otra (ver repo) | Python | 2026-10-08 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

HunyuanVideo publica los pesos, la definición en PyTorch y el código de inferencia de un modelo de texto a video de más de 13.000 millones de parámetros, que genera clips de unos 5 segundos (129 fotogramas) en 540p o 720p. Las variantes de imagen a video, avatares guiados por audio y personalización viven en repos aparte.

## Por qué destaca

Al publicarse fue el modelo de video abierto más grande, con calidad comparable a modelos cerrados en evaluaciones humanas. Tiene soporte nativo en ComfyUI y Diffusers, pesos FP8 y versiones cuantizadas de la comunidad.

## Cómo funciona

Transformer de difusión que trabaja en un espacio latente comprimido por un VAE causal 3D; el prompt se codifica con un LLM multimodal en lugar de CLIP o T5. Admite inferencia paralela en varias GPU con xDiT.

## Instalación rápida

`git clone https://github.com/Tencent-Hunyuan/HunyuanVideo`, entorno conda con Python 3.10, PyTorch con CUDA y `pip install -r requirements.txt`; luego descarga los pesos de Hugging Face (tencent/HunyuanVideo).

## Casos de uso

- Generar planos cinematográficos a partir de un prompt
- Crear b-roll para videos sin rodar ni comprar material de stock
- Investigar o ajustar modelos de video con pesos abiertos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente |

**Limitaciones:** Necesita entre 45 y 60 GB de VRAM, y su licencia Tencent Hunyuan Community excluye la UE, el Reino Unido y Corea del Sur.

## Stack y modelos

- **Stack:** Python, PyTorch, Diffusers, FlashAttention, xDiT
- **Modelos / API:** Modelos propios en local (HunyuanVideo con codificador de texto MLLM); no usa API externa.
- **Etiquetas:** `video` `inference` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |
| [Real-ESRGAN](real-esrgan.md) | 37.4k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Wan2.2](wan2-2.md) | 18.5k | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. |
| [LTX-Video](ltx-video.md) | 11.4k | Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado. |

## Enlaces

- 🐙 GitHub: [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo)
- 🌐 Web: <https://aivideo.hunyuan.tencent.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
