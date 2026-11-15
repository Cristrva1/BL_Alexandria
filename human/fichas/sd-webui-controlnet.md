[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🧩 sd-webui-controlnet

> Extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI (AUTOMATIC1111), con preprocesadores para poses, bordes, profundidad y más.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 17.8k | GPL-3.0 | Python | 2024-08-12 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Lleva el control composicional al flujo de trabajo habitual de la WebUI sin tocar código.

## Por qué destaca

Es la forma estándar de usar ControlNet dentro del ecosistema AUTOMATIC1111, con panel propio y soporte para múltiples unidades de control simultáneas; muy popular entre quienes ya viven en esa UI.

## Cómo funciona

Se instala como extensión de la WebUI y añade un panel que aplica modelos ControlNet sobre la difusión PyTorch+GPU del propio WebUI, encadenando preprocesador (genera el mapa) + modelo de control (inyecta la condición).

## Instalación rápida

Desde la pestaña Extensions de la WebUI (instalar por URL del repo) o `git clone` en `extensions/`; descargar luego los modelos ControlNet a `models/ControlNet`. Requiere la WebUI ya funcionando con GPU.

## Casos de uso

- Afinar creativos en SD WebUI con poses/sketches/mapas
- Combinar varios ControlNet a la vez (pose + depth)
- Iterar composición sin salir de la UI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ya usas SD WebUI y quieres ControlNet sin cambiar de entorno | trabajas en ComfyUI (usa sus propios nodos) o por código (diffusers) |

## Stack y modelos

- **Stack:** Python, SD WebUI (AUTOMATIC1111), modelos ControlNet
- **Modelos / API:** Local (difusión).
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [stable-diffusion-webui](stable-diffusion-webui.md) | 165k | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. |
| [ControlNet](controlnet.md) | 34.2k | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. |

## Enlaces

- 🐙 GitHub: [Mikubill/sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
