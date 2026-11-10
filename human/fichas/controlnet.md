[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🧭 ControlNet

> Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 34.2k | Apache-2.0 | Python | 2024-02-25 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Resuelve el problema de que el texto por sí solo no controla la composición de la imagen.

## Por qué destaca

Revolucionó el control de la difusión al permitir guiar la composición sin perder calidad; es trabajo de referencia de Lvmin Zhang (lllyasviel) ampliamente citado y adoptado, con versiones 1.0/1.1 y modelos para múltiples condiciones.

## Cómo funciona

Añade una red paralela entrenable ("zero convolution") a un modelo de difusión sobre PyTorch+GPU que inyecta la condición (mapa de control) en cada paso de denoising del U-Net; el modelo base queda congelado durante el fine-tuning.

## Instalación rápida

`git clone` del repo y entorno con sus dependencias; descargar los pesos de ControlNet además del modelo base de Stable Diffusion. Requiere GPU NVIDIA y disco para varios pares de pesos.

## Casos de uso

- Guiar creativos con siluetas/poses/layouts
- Control compositivo preciso a partir de un boceto o depth map
- Mantener pose entre variantes de un personaje

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas control estructural fino de la composición | ya trabajas en SD WebUI (sd-webui-controlnet) o ComfyUI (tienen integración propia) y no necesitas el repo original |

**Limitaciones:** GPU obligatoria; cada tipo de control requiere su par de pesos; el repo original es más de investigación que de producto.

## Stack y modelos

- **Stack:** Python, PyTorch, difusión, GPU
- **Modelos / API:** Local (Stable Diffusion).
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [lllyasviel/ControlNet](https://github.com/lllyasviel/ControlNet)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
