[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Rostros y retratos animados

# 👤 face_recognition

> Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 56.9k | MIT | Python | 2026-06-25 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Envuelve dlib para que el reconocimiento facial sea trivial desde un script.

## Por qué destaca

Es de las librerías de reconocimiento facial más populares y accesibles, ideal para prototipos por su API mínima (`face_locations`, `face_encodings`, `compare_faces`); muy usada como referencia didáctica.

## Cómo funciona

Envuelve los modelos de dlib (detector HOG/CNN y embeddings faciales de 128 dimensiones) para comparar rostros por distancia entre vectores; el umbral de distancia decide si dos caras son la misma persona.

## Instalación rápida

`pip install face_recognition` (requiere dlib y, en Windows, herramientas de compilación de C++/CMake). El modelo CNN para mayor precisión necesita GPU.

## Casos de uso

- Detectar/identificar rostros en imágenes
- Etiquetado automático de álbumes
- Comparar identidad entre dos fotos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas reconocimiento facial básico y rápido de implementar | buscas restauración/animación (GFPGAN/LivePortrait) o precisión de producción (mejor DeepFace/InsightFace) |

**Limitaciones:** La instalación de dlib es frágil en Windows; el modelo por defecto (HOG) es menos preciso que alternativas modernas; el repo recibe mantenimiento esporádico.

## Stack y modelos

- **Stack:** Python, dlib
- **Modelos / API:** Modelos locales.
- **Etiquetas:** `image` `vision` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Deep-Live-Cam](deep-live-cam.md) | 97.9k | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [InsightFace](insightface.md) | 30.2k | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. |

## Enlaces

- 🐙 GitHub: [ageitgey/face_recognition](https://github.com/ageitgey/face_recognition)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
