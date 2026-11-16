# 28. Visión artificial, rostros y percepción — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `4d-humans`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de video.
**Stack:** Conda; checkpoint; modelo SMPL neutral con acceso y licencia; equipo adecuado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de IA obligatoria; SMPL, datos y pesos tienen condiciones de acceso y cómputo propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Requiere registrar y descargar SMPL aparte; las cifras de entrenamiento con varias A100 no son requisitos idénticos de una demo ni garantizan precisión métrica
- Coste: El coste depende del proveedor o la ruta. Sin API de IA obligatoria; SMPL, datos y pesos tienen condiciones de acceso y cómputo propios
- Equipo: Preparación según la ruta elegida. Conda; checkpoint; modelo SMPL neutral con acceso y licencia; equipo adecuado
**Repo:** https://github.com/shubham-goel/4D-Humans

**Instalación** [+]:

```
git clone https://github.com/shubham-goel/4D-Humans.git
cd 4D-Humans
conda env create -f environment.yml
conda activate 4D-humans
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar reconstrucción humana 3D; Explorar seguimiento en un clip corto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta la demo con material autorizado y compara reconstrucción con la imagen
**Qué comprobar:** Puedes identificar malla, pose y posibles errores de profundidad
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `wham`, `blender`

## `cvat`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=annotation,vision,dataset,self-hosted

**Qué es:** Plataforma autoalojable para anotar imágenes, vídeo, audio y 3D con equipos, preanotación con modelos y exportación a más de 20 formatos de datasets.
**Stack:** Python, Dockerfile, docker-compose.yml, package.json, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/cvat-ai/cvat

**Instalación** [+]:

```
docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: etiquetar un dataset de detección o segmentación con varias personas; preanotar vídeos con un modelo y corregir solo los errores
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Clona el repositorio y ejecuta `docker compose up -d`; crea un usuario y una tarea con unas pocas imágenes.
**Qué comprobar:** Puedes dibujar cajas o polígonos y exportar las anotaciones en formato COCO o YOLO.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `detectron2`, `mmpose`, `ultralytics`
**Alternativas (elige una):** `label-studio`

## `deep-live-cam`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video.
**Stack:** Python compatible; FFmpeg; modelos ONNX; CPU o GPU según backend; imágenes autorizadas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ejecución local no exige API; hardware y licencias de modelos como InsightFace se revisan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El autor advierte instalación técnica; los pesos de reconocimiento o intercambio pueden tener restricciones no comerciales aunque el código sea accesible
- Coste: Sin pago a un modelo en la ruta básica. La ejecución local no exige API; hardware y licencias de modelos como InsightFace se revisan aparte
- Equipo: Preparación según la ruta elegida. Python compatible; FFmpeg; modelos ONNX; CPU o GPU según backend; imágenes autorizadas
**Repo:** https://github.com/hacksider/Deep-Live-Cam

**Instalación** [+]:

```
git clone --depth 1 https://github.com/hacksider/Deep-Live-Cam.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un efecto facial consentido; Probar un pipeline local de video
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba con imágenes propias o autorizadas y revisa artefactos en una salida corta etiquetada como sintética
**Qué comprobar:** Puedes comparar original y resultado y reconocer errores visibles
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `insightface`, `obs-studio`, `codeformer`
**Alternativas (elige una):** `facefusion`

## `deepface`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=face,python,vision,biometrics

**Qué es:** Biblioteca Python ligera de reconocimiento facial y análisis de atributos (edad, género, emoción) que envuelve modelos como ArcFace, FaceNet o VGG-Face.
**Stack:** Python, Dockerfile, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/serengil/deepface

**Instalación** [+]:

```
pip install deepface
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: verificar si dos fotos propias o autorizadas corresponden a la misma persona; buscar una cara dentro de una carpeta de imágenes con consentimiento de las personas
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install deepface` y ejecuta `DeepFace.verify` con dos imágenes tuyas.
**Qué comprobar:** Obtienes un diccionario con `verified`, la distancia y el umbral usado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `opencv`, `dlib`, `mediapipe`, `ultralytics`, `insightface`

## `detectron2`
role=library · exec=local · setup=hard · mcp=False · prov=— · tags=vision,pytorch,detection,segmentation

**Qué es:** Biblioteca de Meta AI para detección de objetos y segmentación (instancias, panóptica, keypoints) sobre PyTorch, con un zoo de modelos preentrenados.
**Stack:** Python, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/facebookresearch/detectron2

**Instalación** [+]:

```
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: entrenar un detector o segmentador sobre un conjunto de imágenes propio; usar modelos preentrenados de detección como base para investigación
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Sigue la guía de instalación oficial (requiere PyTorch y compilar extensiones) y ejecuta la demo con un modelo del zoo sobre una imagen.
**Qué comprobar:** Obtienes la imagen con cajas y máscaras de los objetos detectados.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `cvat`, `opencv`

## `dlib`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=vision,cpp,python,face

**Qué es:** Toolkit C++ con bindings de Python para aprendizaje automático y visión: detección de caras, 68 puntos faciales, seguimiento de objetos y optimización.
**Stack:** C++, CMakeLists.txt, pyproject.toml, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/davisking/dlib

**Instalación** [+]:

```
pip install dlib
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: detectar caras y sus puntos de referencia en fotos para alinear o recortar; usar un detector rápido en CPU dentro de una aplicación C++
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install dlib` (necesita CMake y compilador) y ejecuta el ejemplo de detección facial de la carpeta python_examples.
**Qué comprobar:** Obtienes las coordenadas de las caras detectadas en la imagen.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `deepface`, `opencv`, `claude-code`

## `easymocap`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imágenes.
**Stack:** Entorno de la demo; cámaras y calibración según método; modelos corporales autorizados
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ejecución propia usa cómputo y modelos o datasets con condiciones separadas; no incluye equipos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La calibración y el número de vistas cambian por pipeline; una demo no prueba precisión de captura con cualquier cámara o escena
- Coste: El coste depende del proveedor o la ruta. La ejecución propia usa cómputo y modelos o datasets con condiciones separadas; no incluye equipos
- Equipo: Preparación según la ruta elegida. Entorno de la demo; cámaras y calibración según método; modelos corporales autorizados
**Repo:** https://github.com/zju3dv/EasyMocap

**Instalación** [?]:

```
Seguir la instalación original: https://chingswy.github.io/easymocap-public-doc/quickstart/quickstart.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar captura multicámara; Explorar reconstrucción de movimiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Empieza por los datos de una demo y revisa correspondencia de cámaras y reconstrucción
**Qué comprobar:** Puedes reconocer qué observaciones sustentan la pose
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openpose`, `mediapipe`, `blender`, `mmpose`

## `facefusion`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=image,video,vision,python

**Qué es:** Plataforma para intercambio y mejora de rostros en imágenes y video.
**Stack:** Sistema compatible; modelos; CPU o GPU; material autorizado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia propia no exige API; instaladores, hardware y modelos tienen condiciones independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La instalación desde fuente requiere conocimientos técnicos; no debe presentarse la disponibilidad del código como permiso comercial de todos los pesos
- Coste: El coste depende del proveedor o la ruta. La inferencia propia no exige API; instaladores, hardware y modelos tienen condiciones independientes
- Equipo: Preparación según la ruta elegida. Sistema compatible; modelos; CPU o GPU; material autorizado
**Repo:** https://github.com/facefusion/facefusion

**Instalación** [+]:

```
git clone https://github.com/facefusion/facefusion
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un efecto facial consentido; Evaluar un flujo local de imagen
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Procesa una imagen de prueba y revisa bordes, color y artefactos antes de pasar a video
**Qué comprobar:** Puedes identificar modelo y limitaciones de la salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `insightface`, `real-esrgan`
**Alternativas (elige una):** `deep-live-cam`

## `insightface`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación.
**Stack:** Python; runtime ONNX; modelos con licencia adecuada; datos autorizados
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Código MIT, pero modelos preentrenados proporcionados para investigación no comercial; uso comercial requiere revisar la licencia correspondiente
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La licencia de código y modelos es distinta incluso en descargas automáticas; el paquete actual ofrece base y GUI con dependencias diferentes
- Coste: El coste depende del proveedor o la ruta. Código MIT, pero modelos preentrenados proporcionados para investigación no comercial; uso comercial requiere revisar la licencia correspondiente
- Equipo: Preparación según la ruta elegida. Python; runtime ONNX; modelos con licencia adecuada; datos autorizados
**Repo:** https://github.com/deepinsight/insightface

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/deepinsight/insightface/blob/master/python-package/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar alineación facial; Evaluar detección en un dataset de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta detección sobre una imagen propia y revisa resultados antes de usar comparaciones
**Qué comprobar:** Puedes identificar modelo, backend y caras detectadas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `facefusion`, `deep-live-cam`, `liveportrait`, `deepface`

## `kornia`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=vision,library,python

**Qué es:** Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en PyTorch.
**Stack:** Python; PyTorch; tensor o imagen de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API remota para operaciones o modelos locales; pesos y cómputo se revisan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es una biblioteca para desarrolladores y sus convenciones geométricas deben comprobarse al combinarla con otros motores
- Coste: Sin pago a un modelo en la ruta básica. Sin API remota para operaciones o modelos locales; pesos y cómputo se revisan aparte
- Equipo: Preparación según la ruta elegida. Python; PyTorch; tensor o imagen de prueba
**Repo:** https://github.com/kornia/kornia

**Instalación** [+]:

```
pip install kornia
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar datos visuales; Estudiar geometría diferenciable
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Aplica una transformación geométrica y compara coordenadas de entrada y salida
**Qué comprobar:** Puedes comprobar convención de ejes y forma del tensor
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `opencv`, `ultralytics`

## `label-studio`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=data,vision,training,docker

**Qué es:** Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video.
**Stack:** Docker o Python compatible; datos de muestra; almacenamiento persistente
**Acceso y costes:**
- API de IA: API de IA opcional. Etiquetado manual sin API de IA; backend de modelos, hosting y ediciones comerciales pueden añadir costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica es anotación humana; no necesita un modelo para empezar y los backends de ML se configuran por separado
- Coste: El coste depende del proveedor o la ruta. Etiquetado manual sin API de IA; backend de modelos, hosting y ediciones comerciales pueden añadir costes
- Equipo: Preparación según la ruta elegida. Docker o Python compatible; datos de muestra; almacenamiento persistente
**Repo:** https://github.com/HumanSignal/label-studio

**Instalación** [+]:

```
docker pull heartexlabs/label-studio:latest
docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un dataset de imágenes; Revisar etiquetas de texto o audio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un proyecto con cinco imágenes y etiqueta una clase antes de añadir preanotación AI
**Qué comprobar:** Puedes exportar anotaciones y comprobar el formato
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ultralytics`, `sam3`, `supervision`
**Alternativas (elige una):** `cvat`

## `liveportrait`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=image,vision,python

**Qué es:** Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas).
**Stack:** Conda; Python 3.10; PyTorch para tu sistema; FFmpeg; pesos; retrato y movimiento autorizados
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta propia no necesita API; hardware, pesos y servicios de demo son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Las alternativas CUDA del README no se instalan todas juntas; Animals mode tiene restricciones en macOS por X-Pose y los modelos externos conservan sus licencias
- Coste: Sin pago a un modelo en la ruta básica. La ruta propia no necesita API; hardware, pesos y servicios de demo son independientes
- Equipo: Preparación según la ruta elegida. Conda; Python 3.10; PyTorch para tu sistema; FFmpeg; pesos; retrato y movimiento autorizados
**Repo:** https://github.com/KlingAIResearch/LivePortrait

**Instalación** [+]:

```
git clone https://github.com/KlingTeam/LivePortrait
cd LivePortrait

# create env using conda
conda create -n LivePortrait python=3.10
conda activate LivePortrait
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una animación consentida de un retrato; Estudiar retargeting facial
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Anima un retrato propio con un clip corto y compara expresión y bordes
**Qué comprobar:** Puedes reconocer movimiento transferido y defectos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `moviepy`, `comfyui`, `insightface`

## `mediapipe`
role=library · exec=local · setup=medium · mcp=False · prov=local · tags=vision,library,c

**Qué es:** Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplicaciones.
**Stack:** Plataforma y SDK elegidos; modelo de tarea; imagen o clip de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ejecución en dispositivo no exige API de modelo alojado; distribución, modelos y hardware tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. MediaPipe Solutions y compilar el Framework son rutas diferentes; elige la tarea antes de preparar todo el entorno
- Coste: Sin pago a un modelo en la ruta básica. La ejecución en dispositivo no exige API de modelo alojado; distribución, modelos y hardware tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Plataforma y SDK elegidos; modelo de tarea; imagen o clip de prueba
**Repo:** https://github.com/google-ai-edge/mediapipe

**Instalación** [?]:

```
Seguir la instalación original: https://developers.google.com/edge/mediapipe/solutions/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una interacción con manos; Prototipar visión en dispositivo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una tarea como landmarks de manos y revisa sus puntos en una muestra
**Qué comprobar:** Puedes distinguir tarea, modelo y SDK
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `opencv`, `tfjs-models`, `three.js`, `easymocap`, `tensorflow`, `deepface`

## `mmpose`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento humano.
**Stack:** Python; PyTorch y dependencias OpenMMLab compatibles; checkpoint
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Inferencia propia sin API de pago; datasets, modelos y GPU tienen condiciones independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La documentación distingue versiones actuales y 0.x; no mezcles configuraciones y dependencias de líneas diferentes
- Coste: Sin pago a un modelo en la ruta básica. Inferencia propia sin API de pago; datasets, modelos y GPU tienen condiciones independientes
- Equipo: Preparación según la ruta elegida. Python; PyTorch y dependencias OpenMMLab compatibles; checkpoint
**Repo:** https://github.com/open-mmlab/mmpose

**Instalación** [+]:

```
git clone https://github.com/open-mmlab/mmpose.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar modelos de pose; Preparar una demo de análisis de movimiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta una demo de pose y revisa articulaciones y confianza en una imagen conocida
**Qué comprobar:** Puedes identificar configuración y resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `opencv`, `easymocap`, `cvat`

## `opencv`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vision,image,cpp,python

**Qué es:** La librería de visión por computadora de referencia, con miles de algoritmos.
**Stack:** Paquete OpenCV para el lenguaje elegido; imagen pequeña
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las operaciones básicas no necesitan modelos ni API; hardware y servicios de una app son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca de visión por computador; no es un único modelo entrenado ni una aplicación de agentes
- Coste: Sin pago a un modelo en la ruta básica. Las operaciones básicas no necesitan modelos ni API; hardware y servicios de una app son independientes
- Equipo: Preparación según la ruta elegida. Paquete OpenCV para el lenguaje elegido; imagen pequeña
**Repo:** https://github.com/opencv/opencv

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/opencv/opencv/blob/5.x/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar imágenes antes de OCR; Estudiar procesamiento visual básico
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga una imagen, cambia su tamaño y guarda una copia para comparar dimensiones
**Qué comprobar:** Puedes comprobar entrada, transformación y salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ultralytics`, `supervision`, `mediapipe`, `mmpose`, `openpose`, `kornia`

## `openpose`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,c

**Qué es:** Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video.
**Stack:** Plataforma compatible; dependencias de compilación; modelos; imagen autorizada
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Uso no comercial bajo su licencia; uso comercial requiere licencia propia; hardware separado
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Detecta keypoints y no mide clínicamente una postura ni garantiza seguimiento sin errores u oclusiones
- Coste: El coste depende del proveedor o la ruta. Uso no comercial bajo su licencia; uso comercial requiere licencia propia; hardware separado
- Equipo: Preparación según la ruta elegida. Plataforma compatible; dependencias de compilación; modelos; imagen autorizada
**Repo:** https://github.com/CMU-Perceptual-Computing-Lab/openpose

**Instalación** [+]:

```
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar estimación de postura; Preparar puntos de movimiento para una demo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Procesa una imagen de muestra y revisa puntos de articulación visibles y ocultos
**Qué comprobar:** Puedes identificar fallos de pose
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `opencv`, `easymocap`, `comfyui`

## `sam3`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=vision,video,python

**Qué es:** Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en imágenes y video todos los objetos que describas con una frase corta.
**Stack:** Python 3.12 o superior; PyTorch 2.7 o superior; GPU con CUDA 12.6 o superior; cuenta de Hugging Face con acceso aprobado a los pesos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API remota; los pesos se descargan desde Hugging Face tras aceptar la licencia SAM
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Se ejecuta en tu equipo con PyTorch y una GPU NVIDIA con CUDA 12.6 o superior
- Coste: Sin pago a un modelo en la ruta básica. Sin pago por uso de un modelo; el coste es tu GPU o una GPU alquilada
- Equipo: GPU o infraestructura especializada. Python 3.12 o superior; PyTorch 2.7 o superior; GPU con CUDA 12.6 o superior; cuenta de Hugging Face con acceso aprobado a los pesos
**Repo:** https://github.com/facebookresearch/sam3

**Instalación** [+]:

```
git clone https://github.com/facebookresearch/sam3.git
cd sam3
pip install -e .
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Recortar todas las personas o productos de una foto con una frase; Seguir un objeto descrito con texto a lo largo de un video
**Evita si:** No tienes una GPU NVIDIA compatible o necesitas una licencia permisiva como Apache; revisa los límites antes de elegirlo
**Primera prueba propuesta:** Escribe «perro» como indicación en una foto con varios perros y revisa las máscaras
**Qué comprobar:** Cada perro aparece con su propia máscara y caja, y puedes ver cuáles faltan o sobran
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `label-studio`, `supervision`, `ultralytics`

## `supervision`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vision,python

**Qué es:** Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir.
**Stack:** Python; imagen y detecciones de prueba; modelo aparte si lo ejecutas
**Acceso y costes:**
- API de IA: API de IA opcional. Las utilidades básicas no exigen API; el ejemplo con Roboflow Inference necesita clave y condiciones del servicio
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Supervision procesa resultados de modelos y no los reemplaza; la compatibilidad depende del adaptador y formato de detecciones
- Coste: El coste depende del proveedor o la ruta. Las utilidades básicas no exigen API; el ejemplo con Roboflow Inference necesita clave y condiciones del servicio
- Equipo: Preparación según la ruta elegida. Python; imagen y detecciones de prueba; modelo aparte si lo ejecutas
**Repo:** https://github.com/roboflow/supervision

**Instalación** [+]:

```
pip install supervision
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Visualizar detecciones; Contar cruces en un video de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Dibuja cajas de detección de muestra y verifica coordenadas y etiquetas
**Qué comprobar:** Puedes comprobar el resultado anotado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ultralytics`, `opencv`, `sam3`, `label-studio`

## `tfjs-models`
role=library · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,library,typescript

**Qué es:** Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en aplicaciones.
**Stack:** Proyecto JavaScript; modelo específico; navegador o runtime compatible
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API de IA para modelos descargados; descarga, hosting y equipo tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Cada modelo tiene su paquete, guía y licencia; no existe una instalación única que haga funcionar automáticamente toda la colección
- Coste: Sin pago a un modelo en la ruta básica. No necesita API de IA para modelos descargados; descarga, hosting y equipo tienen costes propios
- Equipo: Preparación según la ruta elegida. Proyecto JavaScript; modelo específico; navegador o runtime compatible
**Repo:** https://github.com/tensorflow/tfjs-models

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/tensorflow/tfjs-models/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar ML en el navegador; Preparar una demo de landmarks
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige un modelo de clasificación y revisa una predicción sobre una imagen conocida
**Qué comprobar:** Puedes identificar paquete, pesos y formato de salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mediapipe`, `tensorflow`, `three.js`

## `ultralytics`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=vision,training,python

**Qué es:** Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar.
**Stack:** Python; PyTorch; modelo y memoria compatibles; imagen de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Inferencia local sin API obligatoria; AGPL y licencia Enterprise tienen condiciones distintas y hardware aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La licencia se debe revisar para el uso previsto; un modelo rápido o preciso en benchmarks no garantiza igual resultado en tus imágenes
- Coste: El coste depende del proveedor o la ruta. Inferencia local sin API obligatoria; AGPL y licencia Enterprise tienen condiciones distintas y hardware aparte
- Equipo: Preparación según la ruta elegida. Python; PyTorch; modelo y memoria compatibles; imagen de prueba
**Repo:** https://github.com/ultralytics/ultralytics

**Instalación** [+]:

```
pip install ultralytics
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Contar objetos de muestra; Probar segmentación en un prototipo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Detecta objetos en una imagen y revisa dos cajas y sus etiquetas
**Qué comprobar:** Puedes contrastar la detección con el contenido real
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `supervision`, `label-studio`, `opencv`, `kornia`, `sam3`

## `wham`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=vision,model,python

**Qué es:** Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de video.
**Stack:** Entorno de investigación; modelos SMPL y SMPLify con acceso; pesos; video autorizado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Código MIT, con modelos corporales y datasets bajo condiciones independientes; GPU y almacenamiento aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El script de descarga necesita acceso a los modelos externos; MIT del código no concede automáticamente licencia de SMPL o de los datos
- Coste: El coste depende del proveedor o la ruta. Código MIT, con modelos corporales y datasets bajo condiciones independientes; GPU y almacenamiento aparte
- Equipo: Preparación según la ruta elegida. Entorno de investigación; modelos SMPL y SMPLify con acceso; pesos; video autorizado
**Repo:** https://github.com/yohanshin/WHAM

**Instalación** [+]:

```
docker pull yusun9/wham-vitpose-dpvo-cuda11.3-python3.9:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar movimiento humano 3D; Comparar reconstrucción antes y después de refinamiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prepara la demo de un clip corto y revisa trayectoria y articulaciones reconstruidas
**Qué comprobar:** Puedes distinguir estimación visual de una medición real
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `4d-humans`, `blender`, `pytorch`
