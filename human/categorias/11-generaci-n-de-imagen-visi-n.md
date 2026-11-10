[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 10. Analítica & Visualización](10-anal-tica-visualizaci-n.md) · [12. Audio, Voz & Video ➡️](12-audio-voz-video.md)

# 🖼️ 11. Generación de Imagen & Visión

> Interfaces de difusión, modelos y control, restauración y upscaling, rostros y visión por computador.

**27 repos** · 6 subcategorías · ⭐ 1.2M estrellas en total · 🆕 13 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [stable-diffusion-webui](../fichas/stable-diffusion-webui.md) | 165k | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. | `git clone` |
| [FLUX](../fichas/flux.md) | 26.1k | Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes. | `pip install -e ".[all]"` |
| [rembg](../fichas/rembg.md) | 25.4k | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | `pip install "rembg[cpu,cli]"` |
| [Deep-Live-Cam](../fichas/deep-live-cam.md) | 97.9k | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. | `git clone` |
| [Ultralytics YOLO](../fichas/ultralytics.md) | 63.3k | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. | `pip install ultralytics` |
| [SAM 2](../fichas/sam2.md) | 20.1k | Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. | `pip install -e .` |
| [Open-Generative-AI](../fichas/open-generative-ai.md) | 33.8k | Plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes. | `git clone` |

## 🧭 Subcategorías

- [Interfaces para generar imágenes](#interfaces-para-generar-imágenes) — 6 repos
- [Modelos, librerías y control](#modelos-librerías-y-control) — 5 repos
- [Restauración, upscaling y edición](#restauración-upscaling-y-edición) — 4 repos
- [Rostros y retratos animados](#rostros-y-retratos-animados) — 5 repos
- [Visión por computador](#visión-por-computador) — 6 repos
- [Suites generativas todo-en-uno](#suites-generativas-todo-en-uno) — 1 repos

## Interfaces para generar imágenes

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [stable-diffusion-webui](../fichas/stable-diffusion-webui.md) | 165k | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. | quieres extensiones y comunidad amplia | 🔴 |
| [ComfyUI](../fichas/comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | quieres control total y pipelines reproducibles | 🔴 |
| [Fooocus](../fichas/fooocus.md) | 53.9k | Herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes. | quieres resultados ya, sin curva | 🟡 |
| [InvokeAI](../fichas/invokeai.md) | 29.1k | Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. | trabajas creatividad profesional y quieres una app estable con canvas | 🔴 |
| [Stable Diffusion WebUI Forge](../fichas/sd-webui-forge.md) 🆕 | 13.1k | Versión optimizada de la WebUI de Stable Diffusion, más rápida y con menos memoria. | quieres la WebUI clásica pero más rápida | 🟡 |
| [Krita AI Diffusion](../fichas/krita-ai-diffusion.md) 🆕 | 10.9k | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. | ilustras en Krita y quieres IA integrada | 🟡 |

## Modelos, librerías y control

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [FLUX](../fichas/flux.md) 🆕 | 26.1k | Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes. | quieres generar imágenes de alta calidad con modelos abiertos | 🔴 |
| [diffusers](../fichas/diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. | programas generación y quieres control total por código | 🔴 |
| [ControlNet](../fichas/controlnet.md) | 34.2k | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. | necesitas control estructural fino de la composición | 🔴 |
| [sd-webui-controlnet](../fichas/sd-webui-controlnet.md) | 17.8k | Extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI (AUTOMATIC1111), con preprocesadores para poses, bordes, profundidad y más. | ya usas SD WebUI y quieres ControlNet sin cambiar de entorno | 🔴 |
| [ComfyUI_IPAdapter_plus](../fichas/comfyui-ipadapter-plus.md) | 6.2k | Conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una o varias imágenes de referencia para transferir estilo o identidad. | trabajas en ComfyUI y necesitas consistencia visual por referencia | 🔴 |

## Restauración, upscaling y edición

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [rembg](../fichas/rembg.md) 🆕 | 25.4k | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | necesitas quitar fondos en local | 🟢 |
| [GFPGAN](../fichas/gfpgan.md) | 37.7k | Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. | restauras rostros borrosos o fundidos | 🟡 |
| [Real-ESRGAN](../fichas/real-esrgan.md) | 37.4k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. | reescalas imágenes o video a más resolución | 🟡 |
| [CodeFormer](../fichas/codeformer.md) 🆕 | 18.2k | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. | quieres restaurar rostros | 🟡 |

## Rostros y retratos animados

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Deep-Live-Cam](../fichas/deep-live-cam.md) | 97.9k | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. | necesitas swap en vivo legítimo con consentimiento | 🔴 |
| [face_recognition](../fichas/face-recognition.md) | 56.9k | Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud. | necesitas reconocimiento facial básico y rápido de implementar | 🟡 |
| [FaceFusion](../fichas/facefusion.md) 🆕 | 30.6k | Plataforma para intercambio y mejora de rostros en imágenes y video. | necesitas manipulación facial de calidad con consentimiento | 🟡 |
| [InsightFace](../fichas/insightface.md) 🆕 | 30.2k | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. | necesitas reconocimiento facial preciso | 🟡 |
| [LivePortrait](../fichas/liveportrait.md) | 19.4k | Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas). | animas retratos a partir de una foto | 🔴 |

## Visión por computador

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Ultralytics YOLO](../fichas/ultralytics.md) 🆕 | 63.3k | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. | necesitas detección de objetos práctica | 🟢 |
| ⭐ [SAM 2](../fichas/sam2.md) 🆕 | 20.1k | Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. | necesitas segmentar objetos en video | 🟡 |
| [OpenCV](../fichas/opencv.md) 🆕 | 91.5k | La librería de visión por computadora de referencia, con miles de algoritmos. | necesitas procesamiento de imagen o video | 🟢 |
| [Segment Anything (SAM)](../fichas/segment-anything.md) 🆕 | 55.1k | Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja. | necesitas segmentar objetos en imágenes | 🟡 |
| [supervision](../fichas/supervision.md) 🆕 | 51.6k | Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. | construyes un proyecto de visión con detectores | 🟢 |
| [Label Studio](../fichas/label-studio.md) 🆕 | 28.7k | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. | necesitas crear datasets etiquetados | 🟢 |

## Suites generativas todo-en-uno

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Open-Generative-AI](../fichas/open-generative-ai.md) | 33.8k | Plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes. | quieres un hub de generación multi-modal sin atarte a un SaaS | 🟡 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### stable-diffusion-webui, FLUX, ComfyUI, Stable Diffusion WebUI Forge

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [stable-diffusion-webui](../fichas/stable-diffusion-webui.md) | 165k | quieres extensiones y comunidad amplia | prefieres un flujo moderno y limpio (InvokeAI) |
| [FLUX](../fichas/flux.md) | 26.1k | quieres generar imágenes de alta calidad con modelos abiertos | no tienes GPU potente; usa una API en la nube |
| [ComfyUI](../fichas/comfyui.md) | 146k | quieres control total y pipelines reproducibles | buscas simplicidad inmediata (Fooocus) |
| [Stable Diffusion WebUI Forge](../fichas/sd-webui-forge.md) | 13.1k | quieres la WebUI clásica pero más rápida | prefieres flujos por nodos; mira `comfyui` |

### InvokeAI, Krita AI Diffusion

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [InvokeAI](../fichas/invokeai.md) | 29.1k | trabajas creatividad profesional y quieres una app estable con canvas | solo haces una prueba puntual (Fooocus) o prefieres grafos nodales (ComfyUI) |
| [Krita AI Diffusion](../fichas/krita-ai-diffusion.md) | 10.9k | ilustras en Krita y quieres IA integrada | quieres automatizar generación en lote; mira `comfyui` |

### GFPGAN, CodeFormer

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [GFPGAN](../fichas/gfpgan.md) | 37.7k | restauras rostros borrosos o fundidos | necesitas upscaling general de la imagen (Real-ESRGAN) |
| [CodeFormer](../fichas/codeformer.md) | 18.2k | quieres restaurar rostros | quieres escalar la imagen completa; mira `real-esrgan` |

### Deep-Live-Cam, FaceFusion

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Deep-Live-Cam](../fichas/deep-live-cam.md) | 97.9k | necesitas swap en vivo legítimo con consentimiento | no puedes garantizar uso ético/consentimiento o no tienes GPU |
| [FaceFusion](../fichas/facefusion.md) | 30.6k | necesitas manipulación facial de calidad con consentimiento | no tienes consentimiento de las personas |

### face_recognition, InsightFace

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [face_recognition](../fichas/face-recognition.md) | 56.9k | necesitas reconocimiento facial básico y rápido de implementar | buscas restauración/animación (GFPGAN/LivePortrait) o precisión de producción (mejor DeepFace/InsightFace) |
| [InsightFace](../fichas/insightface.md) | 30.2k | necesitas reconocimiento facial preciso | solo quieres detectar caras simples; mira `opencv` |

### SAM 2, Segment Anything (SAM)

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [SAM 2](../fichas/sam2.md) | 20.1k | necesitas segmentar objetos en video | solo trabajas con imágenes sueltas; `segment-anything` basta |
| [Segment Anything (SAM)](../fichas/segment-anything.md) | 55.1k | necesitas segmentar objetos en imágenes | trabajas con video; mira `sam2` |

## 🧪 Recetas que usan esta categoría

- [🎬 Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
- [📈 Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
