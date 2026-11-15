# 11. Generar y editar imágenes con IA — detalle de repos

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
