# 11. Generación de Imagen & Visión — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `codeformer`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Recupera detalles de caras en fotos de baja calidad con buena fidelidad.
**Stack:** Python, PyTorch
**Repo:** https://github.com/sczhou/CodeFormer

**Instalación** [~]: `pip install codeformer   (o: uv add codeformer)`
_Nombre PyPI puede diferir de 'CodeFormer'; verifica en pypi.org._

**Elige si:** quieres restaurar rostros
**Evita si:** quieres escalar la imagen completa; mira `real-esrgan`
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `gfpgan`

## `comfyui`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Resuelve la composición de flujos de difusión complejos que una UI fija no permite.
**Stack:** Python, GPU, PyTorch, modelos locales
**Repo:** https://github.com/Comfy-Org/ComfyUI

**Instalación** [~]: `git clone https://github.com/Comfy-Org/ComfyUI && cd ComfyUI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres control total y pipelines reproducibles
**Evita si:** buscas simplicidad inmediata (Fooocus)
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `wan2gp`, `sd-webui-forge`

## `comfyui-ipadapter-plus`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Funciona como un "LoRA de una sola imagen": le das un referente y la salida hereda su look.
**Stack:** Python, ComfyUI, CLIP vision
**Repo:** https://github.com/cubiq/ComfyUI_IPAdapter_plus

**Instalación** [~]: `git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus && cd ComfyUI_IPAdapter_plus && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** trabajas en ComfyUI y necesitas consistencia visual por referencia
**Evita si:** no usas ComfyUI o te basta con prompts de estilo
**Combina con:** `comfyui`

## `controlnet`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Resuelve el problema de que el texto por sí solo no controla la composición de la imagen.
**Stack:** Python, PyTorch, difusión, GPU
**Repo:** https://github.com/lllyasviel/ControlNet

**Instalación** [~]: `git clone https://github.com/lllyasviel/ControlNet && cd ControlNet && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas control estructural fino de la composición
**Evita si:** ya trabajas en SD WebUI (sd-webui-controlnet) o ComfyUI (tienen integración propia) y no necesitas el repo original
**Combina con:** `diffusers`, `comfyui`

## `deep-live-cam`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Convierte un cambio de rostro, que normalmente requiere pipeline complejo, en un flujo de "un clic".
**Stack:** Python, PyTorch, ONNX Runtime, GPU
**Repo:** https://github.com/hacksider/Deep-Live-Cam

**Instalación** [~]: `git clone https://github.com/hacksider/Deep-Live-Cam && cd Deep-Live-Cam && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas swap en vivo legítimo con consentimiento
**Evita si:** no puedes garantizar uso ético/consentimiento o no tienes GPU
**Combina con:** `face-recognition`
**Alternativas (elige una):** `facefusion`

## `diffusers`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Es la capa de abstracción que unifica el zoo de modelos de difusión bajo una misma interfaz Python.
**Stack:** Python, PyTorch, Hugging Face Hub
**Repo:** https://github.com/huggingface/diffusers

**Instalación** [~]: `pip install diffusers   (o: uv add diffusers)`
_Nombre PyPI puede diferir de 'diffusers'; verifica en pypi.org._

**Elige si:** programas generación y quieres control total por código
**Evita si:** quieres una UI lista (Fooocus) o grafos nodales (ComfyUI)
**Combina con:** `controlnet`, `cosmos`

## `face-recognition`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Envuelve dlib para que el reconocimiento facial sea trivial desde un script.
**Stack:** Python, dlib
**Repo:** https://github.com/ageitgey/face_recognition

**Instalación** [~]: `pip install face_recognition   (o: uv add face_recognition)`
_Nombre PyPI puede diferir de 'face_recognition'; verifica en pypi.org._

**Elige si:** necesitas reconocimiento facial básico y rápido de implementar
**Evita si:** buscas restauración/animación (GFPGAN/LivePortrait) o precisión de producción (mejor DeepFace/InsightFace)
**Combina con:** `deep-live-cam`
**Alternativas (elige una):** `insightface`

## `facefusion`
role=app · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Herramienta líder para face swap, mejora facial y sincronía labial, con controles de uso responsable.
**Stack:** Python, ONNX, Gradio
**Repo:** https://github.com/facefusion/facefusion

**Instalación** [~]: `git clone https://github.com/facefusion/facefusion && cd facefusion && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas manipulación facial de calidad con consentimiento
**Evita si:** no tienes consentimiento de las personas
**Combina con:** `ffmpeg`
**Alternativas (elige una):** `deep-live-cam`

## `flux`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** Modelos de texto a imagen de alta calidad, con variantes para edición, relleno y control.
**Stack:** Python, PyTorch
**Repo:** https://github.com/black-forest-labs/flux

**Instalación** [~]: `git clone https://github.com/black-forest-labs/flux && cd flux && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres generar imágenes de alta calidad con modelos abiertos
**Evita si:** no tienes GPU potente; usa una API en la nube
**Combina con:** `comfyui`, `diffusers`
**Alternativas (elige una):** `stable-diffusion-webui`

## `fooocus`
role=app · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Es la opción más sencilla para empezar con difusión local.
**Stack:** Python, GPU, PyTorch, modelos SDXL locales
**Repo:** https://github.com/lllyasviel/Fooocus

**Instalación** [~]: `git clone https://github.com/lllyasviel/Fooocus && cd Fooocus && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres resultados ya, sin curva
**Evita si:** necesitas control fino del pipeline (ComfyUI)
**Combina con:** `real-esrgan`

## `gfpgan`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve el problema concreto de las caras "fundidas" que aparecen al reescalar o comprimir fotos.
**Stack:** Python, PyTorch, GPU opcional
**Repo:** https://github.com/TencentARC/GFPGAN

**Instalación** [~]: `git clone https://github.com/TencentARC/GFPGAN && cd GFPGAN && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** restauras rostros borrosos o fundidos
**Evita si:** necesitas upscaling general de la imagen (Real-ESRGAN)
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `codeformer`

## `insightface`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Base de muchas herramientas faciales; ofrece modelos de reconocimiento de última generación.
**Stack:** Python, ONNX
**Repo:** https://github.com/deepinsight/insightface

**Instalación** [~]: `pip install insightface   (o: uv add insightface)`
_Nombre PyPI puede diferir de 'InsightFace'; verifica en pypi.org._

**Elige si:** necesitas reconocimiento facial preciso
**Evita si:** solo quieres detectar caras simples; mira `opencv`
**Combina con:** `facefusion`
**Alternativas (elige una):** `face-recognition`

## `invokeai`
role=app · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Resuelve la fragmentación de herramientas SD reuniendo generación, edición y control en una sola app self-hosted.
**Stack:** Python, PyTorch, React, TypeScript, Docker
**Repo:** https://github.com/invoke-ai/InvokeAI

**Instalación** [~]: `git clone https://github.com/invoke-ai/InvokeAI && cd InvokeAI && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** trabajas creatividad profesional y quieres una app estable con canvas
**Evita si:** solo haces una prueba puntual (Fooocus) o prefieres grafos nodales (ComfyUI)
**Combina con:** `diffusers`, `controlnet`
**Alternativas (elige una):** `krita-ai-diffusion`

## `krita-ai-diffusion`
role=app · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Pinta, selecciona y genera dentro de tu editor de imágenes favorito; usa ComfyUI por debajo.
**Stack:** Python, Krita, ComfyUI
**Repo:** https://github.com/Acly/krita-ai-diffusion

**Instalación** [~]: `git clone https://github.com/Acly/krita-ai-diffusion && cd krita-ai-diffusion && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** ilustras en Krita y quieres IA integrada
**Evita si:** quieres automatizar generación en lote; mira `comfyui`
**Combina con:** `comfyui`
**Alternativas (elige una):** `invokeai`

## `label-studio`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Crea datasets para entrenar o evaluar modelos con interfaces de anotación configurables y preetiquetado con IA.
**Stack:** Python, Django, React
**Repo:** https://github.com/HumanSignal/label-studio

**Instalación** [~]: `git clone https://github.com/HumanSignal/label-studio && cd label-studio && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas crear datasets etiquetados
**Evita si:** solo evalúas prompts; mira `promptfoo`
**Combina con:** `ultralytics`, `sam2`

## `liveportrait`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Convierte una foto en un avatar que sigue las expresiones de un "conductor".
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/KlingAIResearch/LivePortrait

**Instalación** [~]: `git clone https://github.com/KlingAIResearch/LivePortrait && cd LivePortrait && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** animas retratos a partir de una foto
**Evita si:** necesitas swap en vivo (Deep-Live-Cam) o no tienes GPU
**Combina con:** `moviepy`

## `open-generative-ai`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Centraliza la generación visual sin filtros restrictivos ni suscripción.
**Stack:** Python, Node.js
**Repo:** https://github.com/Anil-matcha/Open-Generative-AI

**Instalación** [~]: `git clone https://github.com/Anil-matcha/Open-Generative-AI && cd Open-Generative-AI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un hub de generación multi-modal sin atarte a un SaaS
**Evita si:** ya tienes tu pipeline local (ComfyUI) o necesitas control fino por nodo
**Combina con:** `remotion`

## `opencv`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Procesamiento de imagen y video, detección, calibración de cámaras y más, en C++ y Python.
**Stack:** C++, Python
**Repo:** https://github.com/opencv/opencv

**Instalación** [~]: `pip install opencv   (o: uv add opencv)`
_Nombre PyPI puede diferir de 'OpenCV'; verifica en pypi.org._

**Elige si:** necesitas procesamiento de imagen o video
**Evita si:** necesitas detección de objetos moderna; mira `ultralytics`
**Combina con:** `ultralytics`, `supervision`

## `real-esrgan`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** A diferencia de los upscalers bicúbicos, infiere detalle plausible al ampliar.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/xinntao/Real-ESRGAN

**Instalación** [~]: `git clone https://github.com/xinntao/Real-ESRGAN && cd Real-ESRGAN && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** reescalas imágenes o video a más resolución
**Evita si:** solo necesitas arreglar rostros (GFPGAN) o buscas difusión para reimaginar
**Combina con:** `gfpgan`

## `rembg`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Elimina fondos de fotos de producto o retratos con modelos como U2Net o BiRefNet.
**Stack:** Python, ONNX
**Repo:** https://github.com/danielgatis/rembg

**Instalación** [~]: `pip install rembg   (o: uv add rembg)`
_Nombre PyPI puede diferir de 'rembg'; verifica en pypi.org._

**Elige si:** necesitas quitar fondos en local
**Evita si:** necesitas segmentar objetos específicos; mira `sam2`
**Combina con:** `comfyui`

## `sam2`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Marca un objeto en un fotograma y SAM 2 lo sigue en todo el video. Más rápido que SAM en imágenes.
**Stack:** Python, PyTorch
**Repo:** https://github.com/facebookresearch/sam2

**Instalación** [~]: `pip install sam 2   (o: uv add sam 2)`
_Nombre PyPI puede diferir de 'SAM 2'; verifica en pypi.org._

**Elige si:** necesitas segmentar objetos en video
**Evita si:** solo trabajas con imágenes sueltas; `segment-anything` basta
**Combina con:** `label-studio`, `supervision`
**Alternativas (elige una):** `segment-anything`

## `sd-webui-controlnet`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Lleva el control composicional al flujo de trabajo habitual de la WebUI sin tocar código.
**Stack:** Python, SD WebUI (AUTOMATIC1111), modelos ControlNet
**Repo:** https://github.com/Mikubill/sd-webui-controlnet

**Instalación** [~]: `git clone https://github.com/Mikubill/sd-webui-controlnet && cd sd-webui-controlnet && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** ya usas SD WebUI y quieres ControlNet sin cambiar de entorno
**Evita si:** trabajas en ComfyUI (usa sus propios nodos) o por código (diffusers)
**Combina con:** `stable-diffusion-webui`, `controlnet`

## `sd-webui-forge`
role=app · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Mantiene la interfaz de AUTOMATIC1111 con mejoras de rendimiento y soporte de modelos nuevos como FLUX.
**Stack:** Python, Gradio, PyTorch
**Repo:** https://github.com/lllyasviel/stable-diffusion-webui-forge

**Instalación** [~]: `git clone https://github.com/lllyasviel/stable-diffusion-webui-forge && cd stable-diffusion-webui-forge && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres la WebUI clásica pero más rápida
**Evita si:** prefieres flujos por nodos; mira `comfyui`
**Combina con:** `controlnet`
**Alternativas (elige una):** `stable-diffusion-webui`, `comfyui`

## `segment-anything`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Genera máscaras precisas sin entrenamiento para el objeto que indiques. Su sucesor SAM 2 añade video.
**Stack:** Python, PyTorch
**Repo:** https://github.com/facebookresearch/segment-anything

**Instalación** [~]: `pip install segment anything (sam)   (o: uv add segment anything (sam))`
_Nombre PyPI puede diferir de 'Segment Anything (SAM)'; verifica en pypi.org._

**Elige si:** necesitas segmentar objetos en imágenes
**Evita si:** trabajas con video; mira `sam2`
**Combina con:** `label-studio`
**Alternativas (elige una):** `sam2`

## `stable-diffusion-webui`
role=app · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Es la UI que popularizó la difusión local.
**Stack:** Python, GPU, PyTorch, Gradio, modelos locales
**Repo:** https://github.com/AUTOMATIC1111/stable-diffusion-webui

**Instalación** [~]: `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui && cd stable-diffusion-webui && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres extensiones y comunidad amplia
**Evita si:** prefieres un flujo moderno y limpio (InvokeAI)
**Combina con:** `sd-webui-controlnet`
**Alternativas (elige una):** `sd-webui-forge`, `flux`

## `supervision`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Se conecta a cualquier detector y te da utilidades para dibujar, contar en zonas, seguir objetos y evaluar.
**Stack:** Python
**Repo:** https://github.com/roboflow/supervision

**Instalación** [~]: `pip install supervision   (o: uv add supervision)`
_Nombre PyPI puede diferir de 'supervision'; verifica en pypi.org._

**Elige si:** construyes un proyecto de visión con detectores
**Evita si:** solo necesitas procesar imágenes; mira `opencv`
**Combina con:** `ultralytics`, `opencv`

## `ultralytics`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Entrena un detector con tus datos en pocas líneas y expórtalo a ONNX, TensorRT o móvil.
**Stack:** Python, PyTorch
**Repo:** https://github.com/ultralytics/ultralytics

**Instalación** [~]: `pip install ultralytics yolo   (o: uv add ultralytics yolo)`
_Nombre PyPI puede diferir de 'Ultralytics YOLO'; verifica en pypi.org._

**Elige si:** necesitas detección de objetos práctica
**Evita si:** necesitas licencia permisiva para producto cerrado; revisa su licencia
**Combina con:** `supervision`, `label-studio`
