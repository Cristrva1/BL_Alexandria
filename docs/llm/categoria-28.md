# Alexandría para agentes · Visión artificial, rostros y percepción

Categoría 28 completa (21 repos, 2 subcategorías). Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=28 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `deep-live-cam` | rostros | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen… | 3 Avanzado | 75 | AGPL-3.0 (OSI copyleft) | recomendado |
| `deepface` | rostros | Biblioteca Python ligera de reconocimiento facial y análisis de atributos… | 3 Avanzado | 70 | MIT (OSI permisiva) | sin grupo |
| `facefusion` | rostros | Plataforma para intercambio y mejora de rostros en imágenes y video. | 2 Intermedio | 56 | OpenRAIL-AS (source-available) | alternativa |
| `insightface` | rostros | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. | 2 Intermedio | 54 | — (sin licencia detectada) | sin grupo |
| `liveportrait` | rostros | Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento… | 3 Avanzado | 50 | MIT (source-available) | sin grupo |
| `ultralytics` | vision | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de… | 2 Intermedio | 88 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `supervision` | vision | Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y… | 2 Intermedio | 78 | MIT (OSI permisiva) | sin grupo |
| `mediapipe` | vision | Herramientas de aprendizaje automático para tareas de visión y procesamiento de… | 2 Intermedio | 76 | Apache-2.0 (OSI permisiva) | sin grupo |
| `kornia` | vision | Biblioteca de visión por computador para incorporar geometría, transformaciones… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `opencv` | vision | La librería de visión por computadora de referencia, con miles de algoritmos. | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `label-studio` | vision | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. | 1 Básico | 71 | Apache-2.0 (OSI permisiva) | recomendado |
| `cvat` | vision | Plataforma autoalojable para anotar imágenes, vídeo, audio y 3D con equipos… | 2 Intermedio | 68 | MIT (OSI permisiva) | alternativa |
| `detectron2` | vision | Biblioteca de Meta AI para detección de objetos y segmentación (instancias… | 4 Experto | 67 | Apache-2.0 (OSI permisiva) | sin grupo |
| `dlib` | vision | Toolkit C++ con bindings de Python para aprendizaje automático y visión… | 3 Avanzado | 60 | BSL-1.0 (OSI permisiva) | sin grupo |
| `tfjs-models` | vision | Colección de modelos preparados para TensorFlow.js que permite integrar tareas… | 3 Avanzado | 59 | Apache-2.0 (OSI permisiva) | sin grupo |
| `mmpose` | vision | Herramientas y modelos de estimación de pose, incluidos RTMPose y otras… | 3 Avanzado | 56 | Apache-2.0 (OSI permisiva) | sin grupo |
| `sam3` | vision | Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en… | 3 Avanzado | 52 | SAM License (source-available) | sin grupo |
| `openpose` | vision | Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y… | 3 Avanzado | 48 | Licencia académica no comercial (source-available) | sin grupo |
| `4d-humans` | vision | Implementación de investigación para reconstruir y seguir personas en 3D a… | 3 Avanzado | 47 | MIT (OSI permisiva) | sin grupo |
| `wham` | vision | Implementación de investigación para reconstruir movimiento humano… | 3 Avanzado | 39 | MIT (OSI permisiva) | sin grupo |
| `easymocap` | vision | Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir… | 3 Avanzado | 38 | Project Registration License v1.0 (source-available) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Deep-Live-Cam (`deep-live-cam`)

- **Repo:** https://github.com/hacksider/Deep-Live-Cam · AGPL-3.0 · nivel 3 · 75/100 · recomendado en «Intercambio de rostros»
- **Qué es:** Deep-Live-Cam, herramienta de intercambio de rostros (face swap) y deepfake en tiempo real a partir de una sola imagen, de @hacksider. Licencia AGPL-3.0.
- **Cuándo elegirlo:** Casos: Estudiar un efecto facial consentido; Probar un pipeline local de video.
- **Requisitos:** nivel 3: preparación pesada; Python compatible; FFmpeg; modelos ONNX; CPU o GPU según backend; imágenes autorizadas; hardware prerequisites; API de IA: no; Python compatible; FFmpeg; modelos ONNX; CPU o GPU según backend; imágenes autorizadas.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --depth 1 https://github.com/hacksider/Deep-Live-Cam.git` — fuente: https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Prueba con imágenes propias o autorizadas y revisa artefactos en una salida corta etiquetada como sintética Éxito: Puedes comparar original y resultado y reconocer errores visibles
- **Combina con:** `insightface`, `obs-studio` [12/edicion], `codeformer` [11/edicion]
- **Alternativas:** `facefusion`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): facefusion. Riesgo ético y legal alto (suplantación). El autor advierte instalación técnica; los pesos de reconocimiento o intercambio pueden tener restricciones no comerciales aunque el código sea accesible.

### DeepFace (`deepface`)

- **Repo:** https://github.com/serengil/deepface · MIT · nivel 3 · 70/100
- **Qué es:** Biblioteca de código abierto (MIT) creada por Sefik Ilkin Serengil. Muy popular y activa; su autor ofrece además una API gestionada (deepface.dev).
- **Cuándo elegirlo:** Casos: verificar si dos fotos propias o autorizadas corresponden a la misma persona; buscar una cara dentro de una carpeta de imágenes con consentimiento de las personas.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, necesita GPU; Python, Dockerfile, setup.py; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install deepface` — fuente: https://github.com/serengil/deepface/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install deepface` y ejecuta `DeepFace.verify` con dos imágenes tuyas. Éxito: Obtienes un diccionario con `verified`, la distancia y el umbral usado.
- **Combina con:** `opencv` [28/vision], `dlib` [28/vision], `mediapipe` [28/vision], `ultralytics` [28/vision], `insightface`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Úsalo solo con imágenes propias o con consentimiento; la estimación de atributos como el origen étnico es sensible y puede tener sesgos.

### FaceFusion (`facefusion`)

- **Repo:** https://github.com/facefusion/facefusion · OpenRAIL-AS · nivel 2 · 56/100 · alternativa en «Intercambio de rostros»
- **Qué es:** FaceFusion, plataforma de manipulación facial (intercambio y mejora de rostros) para imágenes y vídeo. Licencia OpenRAIL-AS (GitHub muestra NOASSERTION). Tiene ~31k estrellas y está activa (3.9.2).
- **Cuándo elegirlo:** Casos: Preparar un efecto facial consentido; Evaluar un flujo local de imagen.
- **Requisitos:** nivel 2: preparación media; Sistema compatible; modelos; CPU o GPU; material autorizado; hardware prerequisites; API de IA: no; Sistema compatible; modelos; CPU o GPU; material autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/facefusion/facefusion` — fuente: https://docs.facefusion.io/installation
- **Primera prueba propuesta (no ejecutada):** Procesa una imagen de prueba y revisa bordes, color y artefactos antes de pasar a video Éxito: Puedes identificar modelo y limitaciones de la salida
- **Combina con:** `ffmpeg` [12/edicion], `insightface`, `real-esrgan` [11/edicion]
- **Alternativas:** `deep-live-cam`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): deep-live-cam. Riesgo ético y legal; licencia RAIL con restricciones de uso. La instalación desde fuente requiere conocimientos técnicos; no debe presentarse la disponibilidad del código como permiso comercial de todos los pesos.

### InsightFace (`insightface`)

- **Repo:** https://github.com/deepinsight/insightface · — · nivel 2 · 54/100
- **Qué es:** InsightFace, proyecto de análisis facial 2D y 3D mantenido por Jia Guo y Jiankang Deng. El código es MIT, pero los datos de entrenamiento y los modelos entrenados con ellos son solo para investigación no comercial; GitHub no detecta…
- **Cuándo elegirlo:** Casos: Estudiar alineación facial; Evaluar detección en un dataset de prueba.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; runtime ONNX; modelos con licencia adecuada; datos autorizados; hardware prerequisites; API de IA: no; Python; runtime ONNX; modelos con licencia adecuada; datos autorizados.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/deepinsight/insightface/blob/master/python-package/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta detección sobre una imagen propia y revisa resultados antes de usar comparaciones Éxito: Puedes identificar modelo, backend y caras detectadas
- **Combina con:** `facefusion`, `deep-live-cam`, `liveportrait`, `deepface`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Los pesos no permiten uso comercial. La licencia de código y modelos es distinta incluso en descargas automáticas; el paquete actual ofrece base y GUI con dependencias diferentes.

### LivePortrait (`liveportrait`)

- **Repo:** https://github.com/KlingAIResearch/LivePortrait · MIT · nivel 3 · 50/100
- **Qué es:** LivePortrait, sistema de animación de retratos con control de stitching y retargeting, del Kuaishou Visual Generation and Interaction Center (KlingAIResearch).
- **Cuándo elegirlo:** Casos: Crear una animación consentida de un retrato; Estudiar retargeting facial.
- **Requisitos:** nivel 3: preparación pesada; Conda; Python 3.10; PyTorch para tu sistema; FFmpeg; pesos; retrato y movimiento autorizados; hardware prerequisites; API de IA: no; Conda; Python 3.10; PyTorch para tu sistema; FFmpeg; pesos; retrato y movimiento autorizados.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md

  ```bash
  git clone https://github.com/KlingTeam/LivePortrait
  cd LivePortrait
  
  # create env using conda
  conda create -n LivePortrait python=3.10
  conda activate LivePortrait
  ```
- **Primera prueba propuesta (no ejecutada):** Anima un retrato propio con un clip corto y compara expresión y bordes Éxito: Puedes reconocer movimiento transferido y defectos
- **Combina con:** `moviepy` [30/motores], `comfyui` [11/interfaces], `insightface`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Las alternativas CUDA del README no se instalan todas juntas; Animals mode tiene restricciones en macOS por X-Pose y los modelos externos conservan sus….

### Ultralytics YOLO (`ultralytics`)

- **Repo:** https://github.com/ultralytics/ultralytics · AGPL-3.0 · nivel 2 · 88/100
- **Qué es:** Ultralytics, paquete con los modelos YOLO para detección, segmentación, clasificación, pose y OBB. Licencia AGPL-3.0, con licencia Enterprise de pago para uso comercial cerrado. Es muy activo (~63k estrellas, v8.4.215).
- **Cuándo elegirlo:** Casos: Contar objetos de muestra; Probar segmentación en un prototipo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; PyTorch; modelo y memoria compatibles; imagen de prueba; hardware prerequisites; API de IA: no; Python; PyTorch; modelo y memoria compatibles; imagen de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install ultralytics` — fuente: https://github.com/ultralytics/ultralytics/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Detecta objetos en una imagen y revisa dos cajas y sus etiquetas Éxito: Puedes contrastar la detección con el contenido real
- **Combina con:** `supervision`, `label-studio`, `opencv`, `kornia`, `sam3`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. La AGPL obliga a publicar el código de servicios que lo usen, salvo con licencia Enterprise. La licencia se debe revisar para el uso previsto; un modelo rápido o preciso en benchmarks no garantiza igual resultado en tus imágenes.

### supervision (`supervision`)

- **Repo:** https://github.com/roboflow/supervision · MIT · nivel 2 · 78/100
- **Qué es:** supervision, herramientas reutilizables de visión por computador de Roboflow. Licencia MIT. Es madura y muy activa (~52k estrellas, 0.31.7).
- **Cuándo elegirlo:** Casos: Visualizar detecciones; Contar cruces en un video de prueba.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; imagen y detecciones de prueba; modelo aparte si lo ejecutas; hardware prerequisites; API de IA: opcional; Python; imagen y detecciones de prueba; modelo aparte si lo ejecutas.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install supervision` — fuente: https://github.com/roboflow/supervision/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Dibuja cajas de detección de muestra y verifica coordenadas y etiquetas Éxito: Puedes comprobar el resultado anotado
- **Combina con:** `ultralytics`, `opencv`, `sam3`, `label-studio`
- **Riesgos y avisos:** Sin alternativas declaradas. Supervision procesa resultados de modelos y no los reemplaza; la compatibilidad depende del adaptador y formato de detecciones.

### mediapipe (`mediapipe`)

- **Repo:** https://github.com/google-ai-edge/mediapipe · Apache-2.0 · nivel 2 · 76/100
- **Qué es:** MediaPipe, framework de Google AI Edge para ML en dispositivo. Licencia Apache-2.0. Es maduro (~38k estrellas, v1.2.3).
- **Cuándo elegirlo:** Casos: Crear una interacción con manos; Prototipar visión en dispositivo.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Plataforma y SDK elegidos; modelo de tarea; imagen o clip de prueba; hardware prerequisites; API de IA: no; Plataforma y SDK elegidos; modelo de tarea; imagen o clip de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://developers.google.com/edge/mediapipe/solutions/
- **Primera prueba propuesta (no ejecutada):** Elige una tarea como landmarks de manos y revisa sus puntos en una muestra Éxito: Puedes distinguir tarea, modelo y SDK
- **Combina con:** `opencv`, `tfjs-models`, `three.js` [26/animacion], `easymocap`, `tensorflow` [24/entrenamiento], `deepface` [28/rostros]
- **Riesgos y avisos:** Sin alternativas declaradas. MediaPipe Solutions y compilar el Framework son rutas diferentes; elige la tarea antes de preparar todo el entorno.

### kornia (`kornia`)

- **Repo:** https://github.com/kornia/kornia · Apache-2.0 · nivel 2 · 74/100
- **Qué es:** Kornia, biblioteca de visión por computador diferenciable sobre PyTorch. Licencia Apache-2.0. Es madura (~12k estrellas, v0.9.1).
- **Cuándo elegirlo:** Casos: Preparar datos visuales; Estudiar geometría diferenciable.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; PyTorch; tensor o imagen de prueba; hardware prerequisites; API de IA: no; Python; PyTorch; tensor o imagen de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install kornia` — fuente: https://github.com/kornia/kornia/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Aplica una transformación geométrica y compara coordenadas de entrada y salida Éxito: Puedes comprobar convención de ejes y forma del tensor
- **Combina con:** `pytorch` [24/entrenamiento], `opencv`, `ultralytics`
- **Riesgos y avisos:** Sin alternativas declaradas. Es una biblioteca para desarrolladores y sus convenciones geométricas deben comprobarse al combinarla con otros motores.

### OpenCV (`opencv`)

- **Repo:** https://github.com/opencv/opencv · Apache-2.0 · nivel 2 · 74/100
- **Qué es:** OpenCV, la biblioteca open source de visión por computador de referencia, gestionada por OpenCV.org. Licencia Apache-2.0. Es muy madura (~92k estrellas, 5.1.0).
- **Cuándo elegirlo:** Casos: Preparar imágenes antes de OCR; Estudiar procesamiento visual básico.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Paquete OpenCV para el lenguaje elegido; imagen pequeña; hardware prerequisites; API de IA: no; Paquete OpenCV para el lenguaje elegido; imagen pequeña.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/opencv/opencv/blob/5.x/README.md
- **Primera prueba propuesta (no ejecutada):** Carga una imagen, cambia su tamaño y guarda una copia para comparar dimensiones Éxito: Puedes comprobar entrada, transformación y salida
- **Combina con:** `ultralytics`, `supervision`, `mediapipe`, `mmpose`, `openpose`, `kornia`
- **Riesgos y avisos:** Sin alternativas declaradas. Es una biblioteca de visión por computador; no es un único modelo entrenado ni una aplicación de agentes.

### Label Studio (`label-studio`)

- **Repo:** https://github.com/HumanSignal/label-studio · Apache-2.0 · nivel 1 · 71/100 · recomendado en «Etiquetado de datos para visión»
- **Qué es:** Label Studio, herramienta open source de etiquetado de datos, de HumanSignal. Licencia Apache-2.0. Es madura (~29k estrellas, 1.23.2) y tiene edición Enterprise de pago.
- **Cuándo elegirlo:** Casos: Preparar un dataset de imágenes; Revisar etiquetas de texto o audio.
- **Requisitos:** nivel 1: preparación sencilla; Docker o Python compatible; datos de muestra; almacenamiento persistente; hardware prerequisites; API de IA: opcional; Docker o Python compatible; datos de muestra; almacenamiento persistente.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/HumanSignal/label-studio/blob/develop/README.md

  ```bash
  docker pull heartexlabs/label-studio:latest
  docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un proyecto con cinco imágenes y etiqueta una clase antes de añadir preanotación AI Éxito: Puedes exportar anotaciones y comprobar el formato
- **Combina con:** `ultralytics`, `sam3`, `supervision`
- **Alternativas:** `cvat`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. La función básica es anotación humana; no necesita un modelo para empezar y los backends de ML se configuran por separado.

### CVAT Community (`cvat`)

- **Repo:** https://github.com/cvat-ai/cvat · MIT · nivel 2 · 68/100 · alternativa en «Etiquetado de datos para visión»
- **Qué es:** Edición comunitaria, autoalojable y de código abierto (MIT) de CVAT, una de las herramientas de anotación de datos más usadas en visión por computador desde 2018. Es la base de CVAT Online y CVAT Enterprise (comerciales). Muy activa.
- **Cuándo elegirlo:** Casos: etiquetar un dataset de detección o segmentación con varias personas; preanotar vídeos con un modelo y corregir solo los errores.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Python, Dockerfile, docker-compose.yml, package.json, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/cvat-ai/cvat/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio y ejecuta `docker compose up -d`; crea un usuario y una tarea con unas pocas imágenes. Éxito: Puedes dibujar cajas o polígonos y exportar las anotaciones en formato COCO o YOLO.
- **Combina con:** `detectron2`, `mmpose`, `ultralytics`
- **Alternativas:** `label-studio`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativa de Label Studio: CVAT está más especializado en visión (vídeo, pistas y 3D); Label Studio cubre más tipos de datos generales.

### Detectron2 (`detectron2`)

- **Repo:** https://github.com/facebookresearch/detectron2 · Apache-2.0 · nivel 4 · 67/100
- **Qué es:** Biblioteca de investigación de código abierto (Apache-2.0) de Facebook AI Research (Meta), sucesora de Detectron y maskrcnn-benchmark. Muy citada, pero con mantenimiento bajo: la última versión publicada es v0.6 (2021) y el último push es…
- **Cuándo elegirlo:** Casos: entrenar un detector o segmentador sobre un conjunto de imágenes propio; usar modelos preentrenados de detección como base para investigación.
- **Requisitos:** nivel 4: preparación difícil, requiere programar con él, necesita GPU; Python, setup.py; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'` — fuente: https://github.com/facebookresearch/detectron2/blob/main/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de instalación oficial (requiere PyTorch y compilar extensiones) y ejecuta la demo con un modelo del zoo sobre una imagen. Éxito: Obtienes la imagen con cajas y máscaras de los objetos detectados.
- **Combina con:** `pytorch` [24/entrenamiento], `cvat`, `opencv`
- **Riesgos y avisos:** Para detección en producción, Ultralytics (YOLO) suele ser más sencillo; Detectron2 sigue siendo útil en investigación y segmentación avanzada.

### dlib (`dlib`)

- **Repo:** https://github.com/davisking/dlib · BSL-1.0 · nivel 3 · 60/100
- **Qué es:** Toolkit de código abierto (Boost Software License) creado y mantenido por Davis King desde 2002. Clásico y estable, con cambios continuos pero menos frecuentes que en bibliotecas más nuevas.
- **Cuándo elegirlo:** Casos: detectar caras y sus puntos de referencia en fotos para alinear o recortar; usar un detector rápido en CPU dentro de una aplicación C++.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, necesita GPU; C++, CMakeLists.txt, pyproject.toml, setup.py; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install dlib` — fuente: https://github.com/davisking/dlib/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install dlib` (necesita CMake y compilador) y ejecuta el ejemplo de detección facial de la carpeta python_examples. Éxito: Obtienes las coordenadas de las caras detectadas en la imagen.
- **Combina con:** `deepface` [28/rostros], `opencv`, `claude-code` [20/terminal]
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia.

### tfjs-models (`tfjs-models`)

- **Repo:** https://github.com/tensorflow/tfjs-models · Apache-2.0 · nivel 3 · 59/100
- **Qué es:** Colección de modelos preentrenados portados a TensorFlow.js, de Google. Licencia Apache-2.0. Tiene ~15k estrellas y está poco activa (último cambio en junio de 2026).
- **Cuándo elegirlo:** Casos: Probar ML en el navegador; Preparar una demo de landmarks.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él; Proyecto JavaScript; modelo específico; navegador o runtime compatible; hardware prerequisites; API de IA: no; Proyecto JavaScript; modelo específico; navegador o runtime compatible.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/tensorflow/tfjs-models/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Elige un modelo de clasificación y revisa una predicción sobre una imagen conocida Éxito: Puedes identificar paquete, pesos y formato de salida
- **Combina con:** `mediapipe`, `tensorflow` [24/entrenamiento], `three.js` [26/animacion]
- **Riesgos y avisos:** Sin alternativas declaradas. Cada modelo tiene su paquete, guía y licencia; no existe una instalación única que haga funcionar automáticamente toda la colección.

### mmpose (`mmpose`)

- **Repo:** https://github.com/open-mmlab/mmpose · Apache-2.0 · nivel 3 · 56/100
- **Qué es:** MMPose, toolbox de estimación de pose de OpenMMLab (incluye RTMPose). Licencia Apache-2.0. Tiene ~8k estrellas, pero no cambia desde agosto de 2025 (v1.3.2).
- **Cuándo elegirlo:** Casos: Comparar modelos de pose; Preparar una demo de análisis de movimiento.
- **Requisitos:** nivel 3: preparación pesada; Python; PyTorch y dependencias OpenMMLab compatibles; checkpoint; hardware prerequisites; API de IA: no; Python; PyTorch y dependencias OpenMMLab compatibles; checkpoint.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/open-mmlab/mmpose.git` — fuente: https://github.com/open-mmlab/mmpose/blob/main/docs/en/installation.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una demo de pose y revisa articulaciones y confianza en una imagen conocida Éxito: Puedes identificar configuración y resultado
- **Combina con:** `pytorch` [24/entrenamiento], `opencv`, `easymocap`, `cvat`
- **Riesgos y avisos:** Sin alternativas declaradas. Actividad baja. La documentación distingue versiones actuales y 0.x; no mezcles configuraciones y dependencias de líneas diferentes.

### SAM 3 (`sam3`)

- **Repo:** https://github.com/facebookresearch/sam3 · SAM License · nivel 3 · 52/100
- **Qué es:** SAM 3 (Segment Anything with Concepts), modelo de Meta Superintelligence Labs para detectar, segmentar y seguir objetos en imágenes y vídeo a partir de conceptos. Licencia «SAM License» propia (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Recortar todas las personas o productos de una foto con una frase; Seguir un objeto descrito con texto a lo largo de un video. Evítalo si No tienes una GPU NVIDIA compatible o necesitas una licencia permisiva como Apache; revisa los límites antes de elegirlo.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él, necesita GPU; Python 3.12 o superior; PyTorch 2.7 o superior; GPU con CUDA 12.6 o superior; cuenta de Hugging Face con acceso aprobado a los pesos; hardware gpu; API de IA: no; Python 3.12 o superior; PyTorch 2.7 o superior; GPU con CUDA 12.6 o superior; acceso aprobado a los pesos en Hugging Face.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/facebookresearch/sam3/blob/main/README.md

  ```bash
  git clone https://github.com/facebookresearch/sam3.git
  cd sam3
  pip install -e .
  ```
- **Primera prueba propuesta (no ejecutada):** Escribe «perro» como indicación en una foto con varios perros y revisa las máscaras Éxito: Cada perro aparece con su propia máscara y caja, y puedes ver cuáles faltan o sobran
- **Combina con:** `label-studio`, `supervision`, `ultralytics`
- **Riesgos y avisos:** Sin alternativas declaradas. Pesos con acceso restringido. Los pesos se descargan solo tras aprobarse la solicitud en Hugging Face; requiere GPU con CUDA y la licencia SAM tiene condiciones propias.

### openpose (`openpose`)

- **Repo:** https://github.com/CMU-Perceptual-Computing-Lab/openpose · Licencia académica no comercial · nivel 3 · 48/100
- **Qué es:** OpenPose, sistema de CMU que fue el primero en detectar en tiempo real keypoints de cuerpo, manos, cara y pies de varias personas. Licencia académica, gratuita solo para uso no comercial (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Estudiar estimación de postura; Preparar puntos de movimiento para una demo.
- **Requisitos:** nivel 3: preparación pesada; Plataforma compatible; dependencias de compilación; modelos; imagen autorizada; hardware prerequisites; API de IA: no; Plataforma compatible; dependencias de compilación; modelos; imagen autorizada.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose` — fuente: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/jetson_tx/installation_jetson_tx1.md
- **Primera prueba propuesta (no ejecutada):** Procesa una imagen de muestra y revisa puntos de articulación visibles y ocultos Éxito: Puedes identificar fallos de pose
- **Combina con:** `opencv`, `easymocap`, `comfyui` [11/interfaces]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Licencia no comercial e inactivo. Detecta keypoints y no mide clínicamente una postura ni garantiza seguimiento sin errores u oclusiones.

### 4D-Humans (`4d-humans`)

- **Repo:** https://github.com/shubham-goel/4D-Humans · MIT · nivel 3 · 47/100
- **Qué es:** 4DHumans (HMR 2.0), implementación del artículo «Humans in 4D: Reconstructing and Tracking Humans with Transformers» (UC Berkeley). Licencia MIT. Es código de investigación (~1.7k estrellas) sin cambios desde febrero de 2026.
- **Cuándo elegirlo:** Casos: Estudiar reconstrucción humana 3D; Explorar seguimiento en un clip corto.
- **Requisitos:** nivel 3: preparación pesada; Conda; checkpoint; modelo SMPL neutral con acceso y licencia; equipo adecuado; hardware prerequisites; API de IA: no; Conda; checkpoint; modelo SMPL neutral con acceso y licencia; equipo adecuado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/shubham-goel/4D-Humans/blob/main/README.md

  ```bash
  git clone https://github.com/shubham-goel/4D-Humans.git
  cd 4D-Humans
  conda env create -f environment.yml
  conda activate 4D-humans
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta la demo con material autorizado y compara reconstrucción con la imagen Éxito: Puedes identificar malla, pose y posibles errores de profundidad
- **Combina con:** `pytorch` [24/entrenamiento], `wham`, `blender` [26/creacion-3d]
- **Riesgos y avisos:** Sin alternativas declaradas. Código de investigación. Requiere registrar y descargar SMPL aparte; las cifras de entrenamiento con varias A100 no son requisitos idénticos de una demo ni garantizan precisión métrica.

### WHAM (`wham`)

- **Repo:** https://github.com/yohanshin/WHAM · MIT · nivel 3 · 39/100
- **Qué es:** WHAM, implementación de investigación para reconstruir humanos en 3D anclados al mundo con movimiento preciso a partir de vídeo, de @yohanshin. Licencia MIT. Tiene ~1.2k estrellas y no cambia desde abril de 2024.
- **Cuándo elegirlo:** Casos: Estudiar movimiento humano 3D; Comparar reconstrucción antes y después de refinamiento.
- **Requisitos:** nivel 3: preparación pesada; Entorno de investigación; modelos SMPL y SMPLify con acceso; pesos; video autorizado; hardware prerequisites; API de IA: no; Entorno de investigación; modelos SMPL y SMPLify con acceso; pesos; video autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull yusun9/wham-vitpose-dpvo-cuda11.3-python3.9:latest` — fuente: https://github.com/yohanshin/WHAM/blob/main/docs/DOCKER.md
- **Primera prueba propuesta (no ejecutada):** Prepara la demo de un clip corto y revisa trayectoria y articulaciones reconstruidas Éxito: Puedes distinguir estimación visual de una medición real
- **Combina con:** `4d-humans`, `blender` [26/creacion-3d], `pytorch` [24/entrenamiento]
- **Riesgos y avisos:** Sin alternativas declaradas. Código de investigación inactivo. El script de descarga necesita acceso a los modelos externos; MIT del código no concede automáticamente licencia de SMPL o de los datos.

### EasyMocap (`easymocap`)

- **Repo:** https://github.com/zju3dv/EasyMocap · Project Registration License v1.0 · nivel 3 · 38/100
- **Qué es:** EasyMocap, toolbox open source de captura de movimiento sin marcadores y síntesis de nuevas vistas desde vídeo RGB, del grupo ZJU3DV (Universidad de Zhejiang).
- **Cuándo elegirlo:** Casos: Estudiar captura multicámara; Explorar reconstrucción de movimiento.
- **Requisitos:** nivel 3: preparación pesada; Entorno de la demo; cámaras y calibración según método; modelos corporales autorizados; hardware prerequisites; API de IA: no; Entorno de la demo; cámaras y calibración según método; modelos corporales autorizados.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://chingswy.github.io/easymocap-public-doc/quickstart/quickstart.html
- **Primera prueba propuesta (no ejecutada):** Empieza por los datos de una demo y revisa correspondencia de cámaras y reconstrucción Éxito: Puedes reconocer qué observaciones sustentan la pose
- **Combina con:** `openpose`, `mediapipe`, `blender` [26/creacion-3d], `mmpose`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Revisa la licencia PRL antes de redistribuir. La calibración y el número de vistas cambian por pipeline; una demo no prueba precisión de captura con cualquier cámara o escena.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-28.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Visión artificial, rostros y percepción», lee `docs/alexandria/categoria-28.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-28.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
