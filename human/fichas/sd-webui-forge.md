[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🖼️ Stable Diffusion WebUI Forge

> Versión optimizada de la WebUI de Stable Diffusion, más rápida y con menos memoria.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 13.1k | AGPL-3.0 | Python | 2025-07-31 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Mantiene la interfaz de AUTOMATIC1111 con mejoras de rendimiento y soporte de modelos nuevos como FLUX.

## Por qué destaca

Mejor rendimiento en GPUs modestas con la interfaz conocida.

## Cómo funciona

Backend reescrito para gestión de memoria y nuevos samplers sobre la WebUI de Gradio.

## Instalación rápida

Descarga el paquete de un clic desde los releases o clona y ejecuta `webui-user`.

## Casos de uso

- Generar imágenes en GPUs de 6-8 GB
- Probar FLUX con interfaz clásica
- Flujos con extensiones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres la WebUI clásica pero más rápida | prefieres flujos por nodos; mira `comfyui` |

**Limitaciones:** Licencia AGPL-3.0; actualizaciones irregulares.

## Stack y modelos

- **Stack:** Python, Gradio, PyTorch
- **Modelos / API:** Modelos de Stable Diffusion y FLUX.
- **Etiquetas:** `image` `local` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ControlNet](controlnet.md) | 34.2k | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [stable-diffusion-webui](stable-diffusion-webui.md) | 165k | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. |
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [lllyasviel/stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
