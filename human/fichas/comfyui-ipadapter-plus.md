[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🪞 ComfyUI_IPAdapter_plus

> Conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una o varias imágenes de referencia para transferir estilo o identidad.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 6.2k | GPL-3.0 | Python | 2025-04-14 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Funciona como un "LoRA de una sola imagen": le das un referente y la salida hereda su look.

## Por qué destaca

Es la implementación de referencia de IPAdapter en ComfyUI (de cubiq), un nodo casi imprescindible para mantener coherencia visual entre piezas de una misma campaña o serie.

## Cómo funciona

Inyecta embeddings de imagen de referencia (extraídos vía CLIP vision) en el modelo de difusión sobre PyTorch+GPU durante el sampling de ComfyUI, ponderando la influencia del referente sin reentrenar el modelo base.

## Instalación rápida

Clonar el repo en `custom_nodes/` de ComfyUI (o instalarlo desde ComfyUI Manager) y colocar los modelos IPAdapter y los pesos de CLIP vision en `models/`. Requiere ComfyUI con GPU.

## Casos de uso

- Mantener identidad/estilo entre piezas de una campaña
- Control por referencia visual sin entrenar un LoRA
- Transferir el look de un producto a variantes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas en ComfyUI y necesitas consistencia visual por referencia | no usas ComfyUI o te basta con prompts de estilo |

**Limitaciones:** Depende de pesos IPAdapter específicos (algunos de pago en civitai); la calidad de la transferencia varía mucho según el referente.

## Stack y modelos

- **Stack:** Python, ComfyUI, CLIP vision
- **Modelos / API:** Local (difusión).
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [cubiq/ComfyUI_IPAdapter_plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
