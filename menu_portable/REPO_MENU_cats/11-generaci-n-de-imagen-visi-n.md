# 11. Generación de Imagen & Visión — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `comfyui`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** motor local modular para crear pipelines visuales de generación con IA mediante un grafo de nodos, donde cada paso (carga de modelo, sampling, postproceso) es un bloque conectable y reutilizable.
**Stack:** Python, GPU, modelos locales
**Repo:** https://github.com/comfyanonymous/ComfyUI

**Instalación** [~]: `git clone https://github.com/comfyanonymous/ComfyUI && cd ComfyUI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres control total
**Evita si:** buscas simplicidad ([Fooocus](#-fooocus)).
**Combina con:** `comfyui-ipadapter-plus`, `real-esrgan`
**Alternativas (elige una):** `fooocus`

## `comfyui-ipadapter-plus`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una imagen de referencia para transferir estilo o identidad.
**Stack:** Python, ComfyUI
**Repo:** https://github.com/cubiq/ComfyUI_IPAdapter_plus

**Instalación** [~]: `git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus && cd ComfyUI_IPAdapter_plus && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** trabajas en ComfyUI y necesitas consistencia
**Evita si:** no usas ComfyUI.
**Combina con:** `comfyui`

## `controlnet`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** método y modelos para condicionar la generación text-to-image con señales externas como poses, bordes, profundidad o mapas de segmentación, fijando la estructura del resultado.
**Stack:** Python, difusión, GPU
**Repo:** https://github.com/lllyasviel/ControlNet

**Instalación** [~]: `git clone https://github.com/lllyasviel/ControlNet && cd ControlNet && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas control estructural
**Evita si:** ya trabajas en SD WebUI ([sd-webui-controlnet](#-sd-webui-controlnet)).
**Combina con:** `diffusers`, `comfyui`
**Alternativas (elige una):** `sd-webui-controlnet`

## `deep-live-cam`
role=runtime · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video con salvaguardas de uso.
**Stack:** Python, GPU
**Repo:** https://github.com/hacksider/Deep-Live-Cam

**Instalación** [~]: `git clone https://github.com/hacksider/Deep-Live-Cam && cd Deep-Live-Cam && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas swap en vivo legítimo
**Evita si:** no puedes garantizar uso ético/consentimiento.
**Combina con:** `face-recognition`

## `diffusers`
role=library · exec=local · setup=heavy · mcp=False · prov=['anthropic', 'local']

**Qué es:** librería de Hugging Face para construir y ejecutar pipelines de modelos de difusión (imagen, video, audio) desde código, con APIs estandarizadas para schedulers y modelos.
**Stack:** Python, PyTorch
**Repo:** https://github.com/huggingface/diffusers

**Instalación** [~]: `pip install diffusers   (o: uv add diffusers)`
_Nombre PyPI puede diferir de 'diffusers'; verifica en pypi.org._

**Elige si:** programas generación
**Evita si:** quieres una UI lista ([Fooocus](#-fooocus)).
**Combina con:** `controlnet`, `cosmos`
**Alternativas (elige una):** `fooocus`

## `face-recognition`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** librería de Python sencilla para detección y reconocimiento facial, con una API de alto nivel para localizar, comparar e identificar caras en imágenes.
**Stack:** Python, dlib
**Repo:** https://github.com/ageitgey/face_recognition

**Instalación** [~]: `pip install face_recognition   (o: uv add face_recognition)`
_Nombre PyPI puede diferir de 'face_recognition'; verifica en pypi.org._

**Elige si:** necesitas reconocimiento facial básico
**Evita si:** buscas restauración/animación.
**Combina con:** `deep-live-cam`

## `fluxer`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop; su API y self-host aún están en finalización.
**Stack:** web/TS
**Repo:** https://github.com/fluxerapp/fluxer

**Instalación** [?]: `git clone https://github.com/fluxerapp/fluxer (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres probar algo nuevo
**Evita si:** necesitas estabilidad de producción (API aún en finalización).
**Combina con:** `open-generative-ai`

## `fooocus`
role=app · exec=local · setup=medium · mcp=False · prov=['openai', 'local']

**Qué es:** herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes.
**Stack:** Python, GPU, modelos locales
**Repo:** https://github.com/lllyasviel/Fooocus

**Instalación** [~]: `git clone https://github.com/lllyasviel/Fooocus && cd Fooocus && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres resultados ya
**Evita si:** necesitas control fino ([ComfyUI](#-comfyui)).
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `comfyui`

## `gfpgan`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** algoritmo de restauración facial que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados.
**Stack:** Python, PyTorch, GPU opcional
**Repo:** https://github.com/TencentARC/GFPGAN

**Instalación** [~]: `git clone https://github.com/TencentARC/GFPGAN && cd GFPGAN && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** restauras rostros
**Evita si:** necesitas upscaling general ([Real-ESRGAN](#-real-esrgan)).
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `real-esrgan`

## `invokeai`
role=app · exec=local · setup=heavy · mcp=False · prov=['openai', 'local']

**Qué es:** suite profesional y unificada para Stable Diffusion que combina una UI pulida con canvas, capas, inpainting y gestión de modelos y workflows.
**Stack:** Python, GPU, modelos locales
**Repo:** https://github.com/invoke-ai/InvokeAI

**Instalación** [~]: `git clone https://github.com/invoke-ai/InvokeAI && cd InvokeAI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** trabajas creatividad profesional
**Evita si:** solo haces una prueba puntual ([Fooocus](#-fooocus)).
**Combina con:** `diffusers`, `controlnet`
**Alternativas (elige una):** `fooocus`

## `liveportrait`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen.
**Stack:** Python, GPU
**Repo:** https://github.com/KwaiVGI/LivePortrait

**Instalación** [~]: `git clone https://github.com/KwaiVGI/LivePortrait && cd LivePortrait && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** animas retratos
**Evita si:** necesitas swap en vivo ([Deep-Live-Cam](#-deep-live-cam)).
**Combina con:** `moviepy`
**Alternativas (elige una):** `deep-live-cam`

## `nemo`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Checkout our [HuggingFace🤗 collection](https://huggingface.co/collections/nvidia/nemotron-speech) for the latest open weight checkpoints and demos!.
**Stack:** python, typescript
**Repo:** https://github.com/NVIDIA-NeMo/NeMo.git

**Instalación** [~]: `git clone https://github.com/NVIDIA-NeMo/NeMo.git && cd NeMo && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres **nvidia nemo speech**
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `comfyui`, `stable-diffusion-webui`, `fooocus`

## `open-generative-ai`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'google', 'mcp']

**Qué es:** plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes.
**Stack:** Python, Node.js
**Repo:** https://github.com/Anil-matcha/Open-Generative-AI

**Instalación** [~]: `git clone https://github.com/Anil-matcha/Open-Generative-AI && cd Open-Generative-AI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un hub de generación
**Evita si:** ya tienes tu pipeline local ([ComfyUI](#-comfyui)).
**Combina con:** `remotion`
**Alternativas (elige una):** `comfyui`

## `real-esrgan`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** herramienta de superresolución y restauración para imágenes reales que reescala y limpia material de baja calidad sin rehacerlo.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/xinntao/Real-ESRGAN

**Instalación** [~]: `git clone https://github.com/xinntao/Real-ESRGAN && cd Real-ESRGAN && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** reescalas imágenes
**Evita si:** solo necesitas arreglar rostros ([GFPGAN](#-gfpgan)).
**Combina con:** `gfpgan`
**Alternativas (elige una):** `gfpgan`

## `sd-webui-controlnet`
role=runtime · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI, con preprocesadores para poses, bordes, profundidad y más.
**Stack:** Python, SD WebUI, modelos ControlNet
**Repo:** https://github.com/Mikubill/sd-webui-controlnet

**Instalación** [~]: `git clone https://github.com/Mikubill/sd-webui-controlnet && cd sd-webui-controlnet && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** ya usas SD WebUI
**Evita si:** trabajas en ComfyUI o por código.
**Combina con:** `stable-diffusion-webui`, `controlnet`

## `stable-diffusion-webui`
role=app · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador.
**Stack:** Python, GPU, modelos locales
**Repo:** https://github.com/AUTOMATIC1111/stable-diffusion-webui

**Instalación** [~]: `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui && cd stable-diffusion-webui && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres extensiones y comunidad
**Evita si:** prefieres flujo moderno/limpio ([InvokeAI](#-invokeai)).
**Combina con:** `sd-webui-controlnet`
**Alternativas (elige una):** `invokeai`
