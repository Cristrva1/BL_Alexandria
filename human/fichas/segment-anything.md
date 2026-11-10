[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Visión por computador

# 👁️ Segment Anything (SAM)

> Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 55.1k | Apache-2.0 | Jupyter Notebook | 2024-09-18 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Genera máscaras precisas sin entrenamiento para el objeto que indiques. Su sucesor SAM 2 añade video.

## Por qué destaca

Cambió la segmentación: funciona con objetos que nunca vio.

## Cómo funciona

Un codificador de imagen y un decodificador de máscaras guiado por puntos o cajas.

## Instalación rápida

`pip install git+https://github.com/facebookresearch/segment-anything.git` y descarga un checkpoint.

## Casos de uso

- Recortar objetos con un clic
- Acelerar anotación de datos
- Edición de imágenes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas segmentar objetos en imágenes | trabajas con video; mira `sam2` |

## Stack y modelos

- **Stack:** Python, PyTorch
- **Modelos / API:** Modelo SAM.
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Label Studio](label-studio.md) | 28.7k | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SAM 2](sam2.md) | 20.1k | Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. |

## Enlaces

- 🐙 GitHub: [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
