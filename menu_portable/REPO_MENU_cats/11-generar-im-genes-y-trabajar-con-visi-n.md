# 11. Generar imágenes y trabajar con visión — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `codeformer`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=image,vision,python

**Qué es:** Recupera detalles de caras en fotos de baja calidad con buena fidelidad.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/sczhou/CodeFormer

**Instalación** [?]: `Seguir la instalación original: https://github.com/sczhou/CodeFormer/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres restaurar rostros
**Evita si:** quieres escalar la imagen completa; mira `real-esrgan`
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `gfpgan`

## `comfyui`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=image,python

**Qué es:** Resuelve la composición de flujos de difusión complejos que una UI fija no permite.
**Stack:** Python, GPU, PyTorch, modelos locales
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Comfy-Org/ComfyUI

**Instalación** [?]: `Seguir la instalación original: https://github.com/Comfy-Org/ComfyUI/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres control total y pipelines reproducibles
**Evita si:** buscas simplicidad inmediata (Fooocus)
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `wan2gp`, `sd-webui-forge`

## `comfyui-ipadapter-plus`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=image,python

**Qué es:** Funciona como un "LoRA de una sola imagen": le das un referente y la salida hereda su look.
**Stack:** Python, ComfyUI, CLIP vision
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/cubiq/ComfyUI_IPAdapter_plus

**Instalación** [?]: `Seguir la instalación original: https://github.com/cubiq/ComfyUI_IPAdapter_plus/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas en ComfyUI y necesitas consistencia visual por referencia
**Evita si:** no usas ComfyUI o te basta con prompts de estilo
**Combina con:** `comfyui`

## `controlnet`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=image,python

**Qué es:** Resuelve el problema de que el texto por sí solo no controla la composición de la imagen.
**Stack:** Python, PyTorch, difusión, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/lllyasviel/ControlNet

**Instalación** [?]: `Seguir la instalación original: https://github.com/lllyasviel/ControlNet/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas control estructural fino de la composición
**Evita si:** ya trabajas en SD WebUI (sd-webui-controlnet) o ComfyUI (tienen integración propia) y no necesitas el repo original
**Combina con:** `diffusers`, `comfyui`

## `deep-live-cam`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Convierte un cambio de rostro, que normalmente requiere pipeline complejo, en un flujo de "un clic".
**Stack:** Python, PyTorch, ONNX Runtime, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/hacksider/Deep-Live-Cam

**Instalación** [?]: `Seguir la instalación original: https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas swap en vivo legítimo con consentimiento
**Evita si:** no puedes garantizar uso ético/consentimiento o no tienes GPU
**Combina con:** `face-recognition`
**Alternativas (elige una):** `facefusion`

## `diffusers`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=image,python

**Qué es:** Es la capa de abstracción que unifica el zoo de modelos de difusión bajo una misma interfaz Python.
**Stack:** Python, PyTorch, Hugging Face Hub
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/diffusers

**Instalación** [?]: `Seguir la instalación original: https://github.com/huggingface/diffusers/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** programas generación y quieres control total por código
**Evita si:** quieres una UI lista (Fooocus) o grafos nodales (ComfyUI)
**Combina con:** `controlnet`, `cosmos`

## `face-recognition`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=image,vision,python

**Qué es:** Envuelve dlib para que el reconocimiento facial sea trivial desde un script.
**Stack:** Python, dlib
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ageitgey/face_recognition

**Instalación** [?]: `Seguir la instalación original: https://github.com/ageitgey/face_recognition/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas reconocimiento facial básico y rápido de implementar
**Evita si:** buscas restauración/animación (GFPGAN/LivePortrait) o precisión de producción (mejor DeepFace/InsightFace)
**Combina con:** `deep-live-cam`
**Alternativas (elige una):** `insightface`

## `facefusion`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=image,video,vision,python

**Qué es:** Herramienta líder para face swap, mejora facial y sincronía labial, con controles de uso responsable.
**Stack:** Python, ONNX, Gradio
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/facefusion/facefusion

**Instalación** [?]: `Seguir la instalación original: https://github.com/facefusion/facefusion/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas manipulación facial de calidad con consentimiento
**Evita si:** no tienes consentimiento de las personas
**Combina con:** `ffmpeg`
**Alternativas (elige una):** `deep-live-cam`

## `flux`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=image,python

**Qué es:** Modelos de texto a imagen de alta calidad, con variantes para edición, relleno y control.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/black-forest-labs/flux

**Instalación** [?]: `Seguir la instalación original: https://github.com/black-forest-labs/flux/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres generar imágenes de alta calidad con modelos abiertos
**Evita si:** no tienes GPU potente; usa una API en la nube
**Combina con:** `comfyui`, `diffusers`
**Alternativas (elige una):** `stable-diffusion-webui`

## `fooocus`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=image,python

**Qué es:** Es la opción más sencilla para empezar con difusión local.
**Stack:** Python, GPU, PyTorch, modelos SDXL locales
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/lllyasviel/Fooocus

**Instalación** [?]: `Seguir la instalación original: https://github.com/lllyasviel/Fooocus/blob/main/readme.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres resultados ya, sin curva
**Evita si:** necesitas control fino del pipeline (ComfyUI)
**Combina con:** `real-esrgan`

## `gfpgan`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=image,python

**Qué es:** Resuelve el problema concreto de las caras "fundidas" que aparecen al reescalar o comprimir fotos.
**Stack:** Python, PyTorch, GPU opcional
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/TencentARC/GFPGAN

**Instalación** [?]: `Seguir la instalación original: https://github.com/TencentARC/GFPGAN/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** restauras rostros borrosos o fundidos
**Evita si:** necesitas upscaling general de la imagen (Real-ESRGAN)
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `codeformer`

## `insightface`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Base de muchas herramientas faciales; ofrece modelos de reconocimiento de última generación.
**Stack:** Python, ONNX
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/deepinsight/insightface

**Instalación** [?]: `Seguir la instalación original: https://github.com/deepinsight/insightface/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas reconocimiento facial preciso
**Evita si:** solo quieres detectar caras simples; mira `opencv`
**Combina con:** `facefusion`
**Alternativas (elige una):** `face-recognition`

## `invokeai`
role=app · exec=local · setup=heavy · mcp=False · prov=— · tags=image,typescript

**Qué es:** Resuelve la fragmentación de herramientas SD reuniendo generación, edición y control en una sola app self-hosted.
**Stack:** Python, PyTorch, React, TypeScript, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/invoke-ai/InvokeAI

**Instalación** [?]: `Seguir la instalación original: https://github.com/invoke-ai/InvokeAI/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas creatividad profesional y quieres una app estable con canvas
**Evita si:** solo haces una prueba puntual (Fooocus) o prefieres grafos nodales (ComfyUI)
**Combina con:** `diffusers`, `controlnet`
**Alternativas (elige una):** `krita-ai-diffusion`

## `krita-ai-diffusion`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=image,design,python

**Qué es:** Pinta, selecciona y genera dentro de tu editor de imágenes favorito; usa ComfyUI por debajo.
**Stack:** Python, Krita, ComfyUI
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Acly/krita-ai-diffusion

**Instalación** [?]: `Seguir la instalación original: https://github.com/Acly/krita-ai-diffusion/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** ilustras en Krita y quieres IA integrada
**Evita si:** quieres automatizar generación en lote; mira `comfyui`
**Combina con:** `comfyui`
**Alternativas (elige una):** `invokeai`

## `label-studio`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=data,vision,training,docker

**Qué es:** Crea datasets para entrenar o evaluar modelos con interfaces de anotación configurables y preetiquetado con IA.
**Stack:** Python, Django, React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/HumanSignal/label-studio

**Instalación** [+]: `pip install label-studio`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas crear datasets etiquetados
**Evita si:** solo evalúas prompts; mira `promptfoo`
**Combina con:** `ultralytics`, `sam2`

## `liveportrait`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=image,vision,python

**Qué es:** Convierte una foto en un avatar que sigue las expresiones de un "conductor".
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/KlingAIResearch/LivePortrait

**Instalación** [?]: `Seguir la instalación original: https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** animas retratos a partir de una foto
**Evita si:** necesitas swap en vivo (Deep-Live-Cam) o no tienes GPU
**Combina con:** `moviepy`

## `open-generative-ai`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=image,video,javascript

**Qué es:** Estudio abierto de generación de imagen y video que utiliza modelos ofrecidos mediante servicios de MuAPI. El código de la interfaz está disponible; las generaciones y otras modalidades del servicio tienen requisitos y tarifas propios.
**Stack:** Python, Node.js
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. La aplicación utiliza MuAPI para generar medios. El código abierto no incluye el consumo de ese servicio.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Anil-matcha/Open-Generative-AI

**Instalación** [?]: `Seguir la instalación original: https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un hub de generación multi-modal sin atarte a un SaaS
**Evita si:** ya tienes tu pipeline local (ComfyUI) o necesitas control fino por nodo
**Combina con:** `remotion`

## `opencv`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vision,image,cpp,python

**Qué es:** Procesamiento de imagen y video, detección, calibración de cámaras y más, en C++ y Python.
**Stack:** C++, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/opencv/opencv

**Instalación** [?]: `Seguir la instalación original: https://github.com/opencv/opencv/blob/5.x/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas procesamiento de imagen o video
**Evita si:** necesitas detección de objetos moderna; mira `ultralytics`
**Combina con:** `ultralytics`, `supervision`

## `real-esrgan`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=image,python

**Qué es:** A diferencia de los upscalers bicúbicos, infiere detalle plausible al ampliar.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/xinntao/Real-ESRGAN

**Instalación** [?]: `Seguir la instalación original: https://github.com/xinntao/Real-ESRGAN/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** reescalas imágenes o video a más resolución
**Evita si:** solo necesitas arreglar rostros (GFPGAN) o buscas difusión para reimaginar
**Combina con:** `gfpgan`

## `rembg`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=image,python

**Qué es:** Elimina fondos de fotos de producto o retratos con modelos como U2Net o BiRefNet.
**Stack:** Python, ONNX
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/danielgatis/rembg

**Instalación** [?]: `Seguir la instalación original: https://github.com/danielgatis/rembg/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas quitar fondos en local
**Evita si:** necesitas segmentar objetos específicos; mira `sam2`
**Combina con:** `comfyui`

## `ruview`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=sensores,claude,claude-code,esp32,firmware,home-assistant,home-automation,iot

**Qué es:** Proyecto de detección espacial que experimenta con señales WiFi para estimar presencia y movimiento. Procesa señales de radio y conecta componentes de detección con paneles y sistemas de domótica.
**Stack:** Rust, pyproject.toml
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ruvnet/RuView

**Instalación** [?]: `Seguir la instalación original: https://github.com/ruvnet/RuView/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres investigar percepción mediante radiofrecuencia y sensores WiFi
**Evita si:** no dispones de datos o hardware compatibles con el proyecto

## `sam2`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=vision,video,python

**Qué es:** Marca un objeto en un fotograma y SAM 2 lo sigue en todo el video. Más rápido que SAM en imágenes.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/facebookresearch/sam2

**Instalación** [?]: `Seguir la instalación original: https://github.com/facebookresearch/sam2/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas segmentar objetos en video
**Evita si:** solo trabajas con imágenes sueltas; `segment-anything` basta
**Combina con:** `label-studio`, `supervision`
**Alternativas (elige una):** `segment-anything`

## `sd-webui-controlnet`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Lleva el control composicional al flujo de trabajo habitual de la WebUI sin tocar código.
**Stack:** Python, SD WebUI (AUTOMATIC1111), modelos ControlNet
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Mikubill/sd-webui-controlnet

**Instalación** [?]: `Seguir la instalación original: https://github.com/Mikubill/sd-webui-controlnet/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** ya usas SD WebUI y quieres ControlNet sin cambiar de entorno
**Evita si:** trabajas en ComfyUI (usa sus propios nodos) o por código (diffusers)
**Combina con:** `stable-diffusion-webui`, `controlnet`

## `sd-webui-forge`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=image,local,python

**Qué es:** Mantiene la interfaz de AUTOMATIC1111 con mejoras de rendimiento y soporte de modelos nuevos como FLUX.
**Stack:** Python, Gradio, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/lllyasviel/stable-diffusion-webui-forge

**Instalación** [?]: `Seguir la instalación original: https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres la WebUI clásica pero más rápida
**Evita si:** prefieres flujos por nodos; mira `comfyui`
**Combina con:** `controlnet`
**Alternativas (elige una):** `stable-diffusion-webui`, `comfyui`

## `segment-anything`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Genera máscaras precisas sin entrenamiento para el objeto que indiques. Su sucesor SAM 2 añade video.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/facebookresearch/segment-anything

**Instalación** [?]: `Seguir la instalación original: https://github.com/facebookresearch/segment-anything/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas segmentar objetos en imágenes
**Evita si:** trabajas con video; mira `sam2`
**Combina con:** `label-studio`
**Alternativas (elige una):** `sam2`

## `stable-diffusion-webui`
role=app · exec=local · setup=heavy · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Es la UI que popularizó la difusión local.
**Stack:** Python, GPU, PyTorch, Gradio, modelos locales
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/AUTOMATIC1111/stable-diffusion-webui

**Instalación** [?]: `Seguir la instalación original: https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres extensiones y comunidad amplia
**Evita si:** prefieres un flujo moderno y limpio (InvokeAI)
**Combina con:** `sd-webui-controlnet`
**Alternativas (elige una):** `sd-webui-forge`, `flux`

## `supervision`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vision,python

**Qué es:** Se conecta a cualquier detector y te da utilidades para dibujar, contar en zonas, seguir objetos y evaluar.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/roboflow/supervision

**Instalación** [+]: `pip install supervision`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** construyes un proyecto de visión con detectores
**Evita si:** solo necesitas procesar imágenes; mira `opencv`
**Combina con:** `ultralytics`, `opencv`

## `ultralytics`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vision,training,python

**Qué es:** Entrena un detector con tus datos en pocas líneas y expórtalo a ONNX, TensorRT o móvil.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ultralytics/ultralytics

**Instalación** [+]: `pip install ultralytics`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas detección de objetos práctica
**Evita si:** necesitas licencia permisiva para producto cerrado; revisa su licencia
**Combina con:** `supervision`, `label-studio`
