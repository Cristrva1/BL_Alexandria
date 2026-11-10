[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🔍 Real-ESRGAN

> Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 37.4k | BSD-3-Clause | Python | 2024-08-06 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

A diferencia de los upscalers bicúbicos, infiere detalle plausible al ampliar.

## Por qué destaca

Es uno de los upscalers open-source más usados y citados (del grupo de Xintao Wang), con resultados sólidos en fotos y arte, e integrado como opción nativa en SD WebUI, ComfyUI y muchas UIs.

## Cómo funciona

Emplea una red GAN práctica sobre PyTorch+GPU entrenada con un pipeline de degradaciones sintéticas (blur + ruido + compresión) para inferir detalle al ampliar la imagen; ofrece modelos específicos para anime vs. foto.

## Instalación rápida

`pip install realesrgan` o ejecutable portable; los modelos preentrenados se descargan al primer uso. GPU recomendada (también hay build CPU).

## Casos de uso

- Reescalar creativos antiguos
- Mejorar detalle de assets comprimidos
- Upscaling de frames de video en pipelines

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| reescalas imágenes o video a más resolución | solo necesitas arreglar rostros (GFPGAN) o buscas difusión para reimaginar |

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Modelos / API:** Modelos locales.
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [GFPGAN](gfpgan.md) | 37.7k | Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. |

## Enlaces

- 🐙 GitHub: [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
