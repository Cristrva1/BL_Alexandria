[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🖼️ stable-diffusion-webui

> Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 165k | AGPL-3.0 | Python | 2026-03-02 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

## Qué es

Es la UI que popularizó la difusión local.

## Por qué destaca

Fue la UI que popularizó SD y mantiene una de las comunidades y catálogos de plugins más grandes del ecosistema. Su madurez y la cantidad de extensiones (ControlNet, ADetailer, ReActor) la hacen muy versátil.

## Cómo funciona

Levanta un servidor Gradio que orquesta modelos de difusión sobre PyTorch+GPU, con pestañas y scripts para cada modo de generación y un sistema de extensiones instalables desde la propia UI.

## Instalación rápida

`git clone` y ejecutar `webui-user.bat` (Windows) o `webui.sh` (Linux/Mac); el script crea el entorno e instala dependencias automáticamente. Requiere GPU con VRAM decente y checkpoints descargados aparte.

## Casos de uso

- Probar estilos rápido desde una UI
- Usar el enorme ecosistema de extensiones
- Inpainting y img2img sin montar pipeline

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres extensiones y comunidad amplia | prefieres un flujo moderno y limpio (InvokeAI) |

**Limitaciones:** Requiere GPU con VRAM suficiente; la base de código es veterana y el flujo es menos limpio que alternativas modernas como InvokeAI.

## Stack y modelos

- **Stack:** Python, GPU, PyTorch, Gradio, modelos locales
- **Modelos / API:** Local-first (difusión).
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [sd-webui-controlnet](sd-webui-controlnet.md) | 17.8k | Extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI (AUTOMATIC1111), con preprocesadores para poses, bordes, profundidad y más. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stable Diffusion WebUI Forge](sd-webui-forge.md) | 13.1k | Versión optimizada de la WebUI de Stable Diffusion, más rápida y con menos memoria. |
| [FLUX](flux.md) | 26.1k | Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes. |

## Enlaces

- 🐙 GitHub: [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
