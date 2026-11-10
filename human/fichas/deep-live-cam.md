[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Rostros y retratos animados

# 🎭 Deep-Live-Cam

> Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 97.9k | AGPL-3.0 | Python | 2026-11-08 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Convierte un cambio de rostro, que normalmente requiere pipeline complejo, en un flujo de "un clic".

## Por qué destaca

Es de los proyectos de swap en vivo más conocidos por su facilidad de uso (una sola imagen de origen y arrancar); incluye chequeos contra contenido inapropiado (NSFW/real) para desincentivar usos problemáticos.

## Cómo funciona

Combina detección facial (insightface/face_swapper) y reenactment sobre PyTorch+GPU (con backend ONNX Runtime o CUDA) para reemplazar el rostro fotograma a fotograma en un flujo en directo desde la webcam o un archivo.

## Instalación rápida

`git clone`, instalar dependencias y proveedores de GPU (p. ej. ONNX Runtime con CUDA Execution Provider); descargar los modelos de swap indicados. Requiere GPU NVIDIA para tiempo real fluido.

## Casos de uso

- Animar personajes
- Contenido creativo con rostro (uso responsable y consentido)
- Prototipos de presentadores virtuales en vivo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas swap en vivo legítimo con consentimiento | no puedes garantizar uso ético/consentimiento o no tienes GPU |

**Limitaciones:** Uso responsable obligatorio: deepfakes de personas sin consentimiento pueden ser ilegales y violar ToS; GPU requerida para tiempo real; revisar licencia antes de uso comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, ONNX Runtime, GPU
- **Modelos / API:** Modelos locales.
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [face_recognition](face-recognition.md) | 56.9k | Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FaceFusion](facefusion.md) | 30.6k | Plataforma para intercambio y mejora de rostros en imágenes y video. |

## Enlaces

- 🐙 GitHub: [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
- 🌐 Web: <https://deeplivecam.net/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
