[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Generar imágenes y trabajar con visión

Generación, restauración, detección, segmentación y etiquetado de imágenes. Revisa por separado la licencia de los pesos y el hardware del modelo.

28 repos · 7 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [stable-diffusion-webui](../fichas/stable-diffusion-webui.md) | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. | Sin API de IA en la ruta básica |
| [FLUX](../fichas/flux.md) | Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes. | Sin API de IA en la ruta básica |
| [rembg](../fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | Sin API de IA en la ruta básica |
| [Deep-Live-Cam](../fichas/deep-live-cam.md) | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. | Sin API de IA en la ruta básica |
| [Ultralytics YOLO](../fichas/ultralytics.md) | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. | Sin API de IA en la ruta básica |
| [SAM 2](../fichas/sam2.md) | Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. | Sin API de IA en la ruta básica |
| [Open-Generative-AI](../fichas/open-generative-ai.md) | Estudio abierto de generación de imagen y video que utiliza modelos ofrecidos mediante servicios de MuAPI. | API de IA necesaria |

## Secciones

- [Interfaces para generar imágenes](#interfaces-para-generar-imágenes) — 6 repos
- [Modelos, librerías y control](#modelos-librerías-y-control) — 5 repos
- [Restauración, upscaling y edición](#restauración-upscaling-y-edición) — 4 repos
- [Rostros y retratos animados](#rostros-y-retratos-animados) — 5 repos
- [Visión por computador](#visión-por-computador) — 6 repos
- [Suites generativas todo-en-uno](#suites-generativas-todo-en-uno) — 1 repos
- [Sensores y percepción espacial](#sensores-y-percepción-espacial) — 1 repos

## Interfaces para generar imágenes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [stable-diffusion-webui](../fichas/stable-diffusion-webui.md) | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. | quieres extensiones y comunidad amplia | Sin API de IA en la ruta básica |
| [ComfyUI](../fichas/comfyui.md) | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | quieres control total y pipelines reproducibles | Sin API de IA en la ruta básica |
| [Fooocus](../fichas/fooocus.md) | Herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes. | quieres resultados ya, sin curva | Sin API de IA en la ruta básica |
| [InvokeAI](../fichas/invokeai.md) | Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. | trabajas creatividad profesional y quieres una app estable con canvas | Sin API de IA en la ruta básica |
| [Stable Diffusion WebUI Forge](../fichas/sd-webui-forge.md) | Versión optimizada de la WebUI de Stable Diffusion, más rápida y con menos memoria. | quieres la WebUI clásica pero más rápida | Sin API de IA en la ruta básica |
| [Krita AI Diffusion](../fichas/krita-ai-diffusion.md) | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. | ilustras en Krita y quieres IA integrada | Sin API de IA en la ruta básica |

## Modelos, librerías y control

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FLUX](../fichas/flux.md) | Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes. | quieres generar imágenes de alta calidad con modelos abiertos | Sin API de IA en la ruta básica |
| [diffusers](../fichas/diffusers.md) | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. | programas generación y quieres control total por código | Sin API de IA en la ruta básica |
| [ControlNet](../fichas/controlnet.md) | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. | necesitas control estructural fino de la composición | Sin API de IA en la ruta básica |
| [sd-webui-controlnet](../fichas/sd-webui-controlnet.md) | Extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI (AUTOMATIC1111), con preprocesadores para poses, bordes, profundidad y más. | ya usas SD WebUI y quieres ControlNet sin cambiar de entorno | Sin API de IA en la ruta básica |
| [ComfyUI_IPAdapter_plus](../fichas/comfyui-ipadapter-plus.md) | Conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una o varias imágenes de referencia para transferir estilo o identidad. | trabajas en ComfyUI y necesitas consistencia visual por referencia | Sin API de IA en la ruta básica |

## Restauración, upscaling y edición

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [rembg](../fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | necesitas quitar fondos en local | Sin API de IA en la ruta básica |
| [GFPGAN](../fichas/gfpgan.md) | Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. | restauras rostros borrosos o fundidos | Sin API de IA en la ruta básica |
| [Real-ESRGAN](../fichas/real-esrgan.md) | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. | reescalas imágenes o video a más resolución | Sin API de IA en la ruta básica |
| [CodeFormer](../fichas/codeformer.md) | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. | quieres restaurar rostros | Sin API de IA en la ruta básica |

## Rostros y retratos animados

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Deep-Live-Cam](../fichas/deep-live-cam.md) | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. | necesitas swap en vivo legítimo con consentimiento | Sin API de IA en la ruta básica |
| [face_recognition](../fichas/face-recognition.md) | Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud. | necesitas reconocimiento facial básico y rápido de implementar | Sin API de IA en la ruta básica |
| [FaceFusion](../fichas/facefusion.md) | Plataforma para intercambio y mejora de rostros en imágenes y video. | necesitas manipulación facial de calidad con consentimiento | Sin API de IA en la ruta básica |
| [InsightFace](../fichas/insightface.md) | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. | necesitas reconocimiento facial preciso | Sin API de IA en la ruta básica |
| [LivePortrait](../fichas/liveportrait.md) | Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas). | animas retratos a partir de una foto | Sin API de IA en la ruta básica |

## Visión por computador

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Ultralytics YOLO](../fichas/ultralytics.md) | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. | necesitas detección de objetos práctica | Sin API de IA en la ruta básica |
| [SAM 2](../fichas/sam2.md) | Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. | necesitas segmentar objetos en video | Sin API de IA en la ruta básica |
| [OpenCV](../fichas/opencv.md) | La librería de visión por computadora de referencia, con miles de algoritmos. | necesitas procesamiento de imagen o video | Sin API de IA en la ruta básica |
| [Segment Anything (SAM)](../fichas/segment-anything.md) | Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja. | necesitas segmentar objetos en imágenes | Sin API de IA en la ruta básica |
| [supervision](../fichas/supervision.md) | Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. | construyes un proyecto de visión con detectores | Sin API de IA en la ruta básica |
| [Label Studio](../fichas/label-studio.md) | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. | necesitas crear datasets etiquetados | Sin API de IA en la ruta básica |

## Suites generativas todo-en-uno

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Open-Generative-AI](../fichas/open-generative-ai.md) | Estudio abierto de generación de imagen y video que utiliza modelos ofrecidos mediante servicios de MuAPI. | quieres un hub de generación multi-modal sin atarte a un SaaS | API de IA necesaria |

## Sensores y percepción espacial

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [RuView](../fichas/ruview.md) | Proyecto de detección espacial que experimenta con señales WiFi para estimar presencia y movimiento. | quieres investigar percepción mediante radiofrecuencia y sensores WiFi | Depende de la ruta elegida |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
- [Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
