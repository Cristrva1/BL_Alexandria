[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 LTX-Video

> Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 11.4k | Apache-2.0 | Python | 2026-11-02 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

LTX-Video es el repositorio de los modelos v0.9.x de Lightricks, un transformer de difusión (DiT) para texto a video, imagen a video, extensión de clips y video a video con condiciones por fotograma clave. Incluye variantes de 2B y 13B, destiladas y FP8, y LoRAs de control de pose, profundidad y bordes. Ya solo se mantiene como legado: los modelos nuevos están en LTX-2.

## Por qué destaca

Destacó por su velocidad: las versiones destiladas generan clips HD en segundos y hay variantes que caben en GPU de 8 GB. Tiene integración oficial con ComfyUI y Diffusers.

## Cómo funciona

DiT que trabaja sobre un VAE de video muy comprimido y acepta varias condiciones (imágenes o videos en fotogramas concretos) en una misma generación; un pipeline multiescala combina el modelo 13B con su versión destilada.

## Instalación rápida

`git clone https://github.com/Lightricks/LTX-Video.git && cd LTX-Video && python -m pip install -e .[inference]` y después `python inference.py --prompt ...`; para la mejor calidad, el equipo recomienda su flujo de ComfyUI.

## Casos de uso

- Animar una imagen fija para un anuncio o un reel
- Extender un clip existente hacia delante o hacia atrás
- Prototipar planos con control de pose o de profundidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas reproducir resultados o mantener flujos existentes con los modelos LTX-Video v0.9.x | empiezas un proyecto nuevo; Lightricks recomienda LTX-2.5 (repo Lightricks/LTX-2), o mira `wan2-2` y `wan2gp` |

**Limitaciones:** El repositorio ya no tiene desarrollo activo, y según el propio equipo el script de inferencia da peor calidad que su flujo de ComfyUI.

## Stack y modelos

- **Stack:** Python, PyTorch, Diffusers, ComfyUI
- **Modelos / API:** Modelos LTX-Video v0.9.x en local (2B y 13B, destilados y FP8); no usa API externa.
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
| [HunyuanVideo](hunyuanvideo.md) | 12.8k | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. |

## Enlaces

- 🐙 GitHub: [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video)
- 🌐 Web: <https://ltx.io/model>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
