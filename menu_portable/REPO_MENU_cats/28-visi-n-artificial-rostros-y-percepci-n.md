# 28. Visión artificial, rostros y percepción — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `4d-humans`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de video.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/shubham-goel/4D-Humans

**Instalación** [?]: `Seguir la instalación original: https://github.com/shubham-goel/4D-Humans/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de video.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

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

## `easymocap`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imágenes.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/zju3dv/EasyMocap

**Instalación** [?]: `Seguir la instalación original: https://github.com/zju3dv/EasyMocap/blob/master/Readme.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imágenes.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

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

## `kornia`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=vision,library,python

**Qué es:** Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en PyTorch.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/kornia/kornia

**Instalación** [?]: `Seguir la instalación original: https://github.com/kornia/kornia/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en PyTorch.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

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

## `mediapipe`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=vision,library,c

**Qué es:** Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplicaciones.
**Stack:** C++, Dockerfile, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/google-ai-edge/mediapipe

**Instalación** [?]: `Seguir la instalación original: https://github.com/google-ai-edge/mediapipe/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplicaciones.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `mmpose`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento humano.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/open-mmlab/mmpose

**Instalación** [?]: `Seguir la instalación original: https://github.com/open-mmlab/mmpose/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento humano.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

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

## `openpose`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,c

**Qué es:** Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video.
**Stack:** C++, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/CMU-Perceptual-Computing-Lab/openpose

**Instalación** [?]: `Seguir la instalación original: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

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

## `tfjs-models`
role=library · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,library,typescript

**Qué es:** Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en aplicaciones.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/tensorflow/tfjs-models

**Instalación** [?]: `Seguir la instalación original: https://github.com/tensorflow/tfjs-models/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en aplicaciones.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

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

## `videopose3d`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Implementación de investigación para estimar pose humana 3D desde trayectorias de puntos 2D en secuencias de video.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/facebookresearch/VideoPose3D

**Instalación** [?]: `Seguir la instalación original: https://github.com/facebookresearch/VideoPose3D/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Implementación de investigación para estimar pose humana 3D desde trayectorias de puntos 2D en secuencias de video.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `wham`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de video.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/yohanshin/WHAM

**Instalación** [?]: `Seguir la instalación original: https://github.com/yohanshin/WHAM/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de video.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución
