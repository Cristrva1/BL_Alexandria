[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🩹 rembg

> Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 25.4k | MIT | Python | 2026-11-06 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Elimina fondos de fotos de producto o retratos con modelos como U2Net o BiRefNet.

## Por qué destaca

Sencilla, rápida y sin servicios externos.

## Cómo funciona

Modelos de segmentación ONNX generan una máscara del sujeto principal.

## Instalación rápida

`pip install "rembg[cpu,cli]"` y `rembg i entrada.png salida.png`.

## Casos de uso

- Fotos de producto con fondo blanco
- Recortes para diseño
- Procesos en lote

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas quitar fondos en local | necesitas segmentar objetos específicos; mira `sam2` |

## Stack y modelos

- **Stack:** Python, ONNX
- **Modelos / API:** Modelos propios de segmentación.
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [danielgatis/rembg](https://github.com/danielgatis/rembg)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
