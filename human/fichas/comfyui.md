[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🧠 ComfyUI

> Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 146k | GPL-3.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Resuelve la composición de flujos de difusión complejos que una UI fija no permite.

## Por qué destaca

Es la referencia para flujos de difusión avanzados y reproducibles, con una comunidad enorme y un ecosistema de nodos/extensiones muy activo. Su autor (comfyanonymous) lo mantiene con foco en rendimiento y compatibilidad con los modelos más recientes (SDXL, Flux).

## Cómo funciona

Ejecuta modelos de difusión (Stable Diffusion, SDXL, Flux) sobre PyTorch+GPU, encadenando nodos en un grafo visual servido desde una interfaz web local que expone cada paso como bloque configurable.

## Instalación rápida

`git clone` del repo y arranque con `python main.py` (o paquete portable en Windows); requiere descargar checkpoints aparte y una GPU con VRAM decente (8 GB+ recomendado).

## Casos de uso

- Pipeline para generar/transformar/exportar imágenes de campaña
- Composición fina y repetible
- Flujos con ControlNet/IPAdapter encadenados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres control total y pipelines reproducibles | buscas simplicidad inmediata (Fooocus) |

**Limitaciones:** Requiere GPU con VRAM suficiente; los checkpoints pesan varios GB y la curva del grafo de nodos es empinada para nuevos.

## Stack y modelos

- **Stack:** Python, GPU, PyTorch, modelos locales
- **Modelos / API:** Local-first (difusión).
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Real-ESRGAN](real-esrgan.md) | 37.4k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [WanGP](wan2gp.md) | — | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. |
| [Stable Diffusion WebUI Forge](sd-webui-forge.md) | 13.1k | Versión optimizada de la WebUI de Stable Diffusion, más rápida y con menos memoria. |

## Enlaces

- 🐙 GitHub: [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
- 🌐 Web: <https://www.comfy.org/>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
