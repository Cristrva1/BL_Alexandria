[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Visión por computador

# 👁️ SAM 2

> Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 20.1k | Apache-2.0 | Jupyter Notebook | 2026-05-30 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Marca un objeto en un fotograma y SAM 2 lo sigue en todo el video. Más rápido que SAM en imágenes.

## Por qué destaca

Segmentación de video interactiva de alta calidad.

## Cómo funciona

Arquitectura con memoria en streaming que propaga máscaras entre fotogramas.

## Instalación rápida

Clona el repo, `pip install -e .` y descarga los checkpoints.

## Casos de uso

- Rotoscopía de video
- Seguimiento de objetos
- Anotar datasets de video

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas segmentar objetos en video | solo trabajas con imágenes sueltas; `segment-anything` basta |

## Stack y modelos

- **Stack:** Python, PyTorch
- **Modelos / API:** Modelo SAM 2.
- **Etiquetas:** `vision` `video` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Label Studio](label-studio.md) | 28.7k | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. |
| [supervision](supervision.md) | 51.6k | Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Segment Anything (SAM)](segment-anything.md) | 55.1k | Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja. |

## Enlaces

- 🐙 GitHub: [facebookresearch/sam2](https://github.com/facebookresearch/sam2)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
