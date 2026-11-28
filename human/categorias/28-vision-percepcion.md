[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Visión artificial, rostros y percepción

Detección, seguimiento, segmentación, rostros y percepción espacial. Distingue el modelo, sus pesos y las herramientas para preparar datos. Comprueba requisitos y permisos sobre las imágenes.

21 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Ultralytics YOLO](../fichas/ultralytics.md) | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. | Sin clave propia de API de IA en la ruta básica |
| [SAM 3](../fichas/sam3.md) | Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en imágenes y video todos los objetos que describas con una frase corta. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Rostros y retratos animados](#rostros-y-retratos-animados) — 5 repos
- [Visión por computador](#visión-por-computador) — 16 repos

## Rostros y retratos animados

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Deep-Live-Cam](../fichas/deep-live-cam.md) | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. | Tu objetivo encaja con estos ejemplos: Estudiar un efecto facial consentido; Probar un pipeline local de video | Sin clave propia de API de IA en la ruta básica |
| [FaceFusion](../fichas/facefusion.md) | Plataforma para intercambio y mejora de rostros en imágenes y video. | Tu objetivo encaja con estos ejemplos: Preparar un efecto facial consentido; Evaluar un flujo local de imagen | Sin clave propia de API de IA en la ruta básica |
| [InsightFace](../fichas/insightface.md) | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. | Tu objetivo encaja con estos ejemplos: Estudiar alineación facial; Evaluar detección en un dataset de prueba | Sin clave propia de API de IA en la ruta básica |
| [DeepFace](../fichas/deepface.md) | Biblioteca Python ligera de reconocimiento facial y análisis de atributos (edad, género, emoción) que envuelve modelos como ArcFace, FaceNet o VGG-Face. | Tu objetivo encaja con estos ejemplos: verificar si dos fotos propias o autorizadas corresponden a la misma persona; buscar una cara dentro de una carpeta de imágenes con consentimiento de las personas | Sin clave propia de API de IA en la ruta básica |
| [LivePortrait](../fichas/liveportrait.md) | Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas). | Tu objetivo encaja con estos ejemplos: Crear una animación consentida de un retrato; Estudiar retargeting facial | Sin clave propia de API de IA en la ruta básica |

## Visión por computador

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Ultralytics YOLO](../fichas/ultralytics.md) | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. | Tu objetivo encaja con estos ejemplos: Contar objetos de muestra; Probar segmentación en un prototipo | Sin clave propia de API de IA en la ruta básica |
| [SAM 3](../fichas/sam3.md) | Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en imágenes y video todos los objetos que describas con una frase corta. | Tu objetivo encaja con estos ejemplos: Recortar todas las personas o productos de una foto con una frase; Seguir un objeto descrito con texto a lo largo de un video | Sin clave propia de API de IA en la ruta básica |
| [OpenCV](../fichas/opencv.md) | La librería de visión por computadora de referencia, con miles de algoritmos. | Tu objetivo encaja con estos ejemplos: Preparar imágenes antes de OCR; Estudiar procesamiento visual básico | Sin clave propia de API de IA en la ruta básica |
| [supervision](../fichas/supervision.md) | Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. | Tu objetivo encaja con estos ejemplos: Visualizar detecciones; Contar cruces en un video de prueba | API de IA opcional |
| [mediapipe](../fichas/mediapipe.md) | Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplicaciones. | Tu objetivo encaja con estos ejemplos: Crear una interacción con manos; Prototipar visión en dispositivo | Sin clave propia de API de IA en la ruta básica |
| [Detectron2](../fichas/detectron2.md) | Biblioteca de Meta AI para detección de objetos y segmentación (instancias, panóptica, keypoints) sobre PyTorch, con un zoo de modelos preentrenados. | Tu objetivo encaja con estos ejemplos: entrenar un detector o segmentador sobre un conjunto de imágenes propio; usar modelos preentrenados de detección como base para investigación | Sin clave propia de API de IA en la ruta básica |
| [openpose](../fichas/openpose.md) | Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video. | Tu objetivo encaja con estos ejemplos: Estudiar estimación de postura; Preparar puntos de movimiento para una demo | Sin clave propia de API de IA en la ruta básica |
| [Label Studio](../fichas/label-studio.md) | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. | Tu objetivo encaja con estos ejemplos: Preparar un dataset de imágenes; Revisar etiquetas de texto o audio | API de IA opcional |
| [CVAT Community](../fichas/cvat.md) | Plataforma autoalojable para anotar imágenes, vídeo, audio y 3D con equipos, preanotación con modelos y exportación a más de 20 formatos de datasets. | Tu objetivo encaja con estos ejemplos: etiquetar un dataset de detección o segmentación con varias personas; preanotar vídeos con un modelo y corregir solo los errores | Sin clave propia de API de IA en la ruta básica |
| [tfjs-models](../fichas/tfjs-models.md) | Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en aplicaciones. | Tu objetivo encaja con estos ejemplos: Probar ML en el navegador; Preparar una demo de landmarks | Sin clave propia de API de IA en la ruta básica |
| [dlib](../fichas/dlib.md) | Toolkit C++ con bindings de Python para aprendizaje automático y visión: detección de caras, 68 puntos faciales, seguimiento de objetos y optimización. | Tu objetivo encaja con estos ejemplos: detectar caras y sus puntos de referencia en fotos para alinear o recortar; usar un detector rápido en CPU dentro de una aplicación C++ | Sin clave propia de API de IA en la ruta básica |
| [kornia](../fichas/kornia.md) | Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en PyTorch. | Tu objetivo encaja con estos ejemplos: Preparar datos visuales; Estudiar geometría diferenciable | Sin clave propia de API de IA en la ruta básica |
| [mmpose](../fichas/mmpose.md) | Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento humano. | Tu objetivo encaja con estos ejemplos: Comparar modelos de pose; Preparar una demo de análisis de movimiento | Sin clave propia de API de IA en la ruta básica |
| [EasyMocap](../fichas/easymocap.md) | Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imágenes. | Tu objetivo encaja con estos ejemplos: Estudiar captura multicámara; Explorar reconstrucción de movimiento | Sin clave propia de API de IA en la ruta básica |
| [4D-Humans](../fichas/4d-humans.md) | Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de video. | Tu objetivo encaja con estos ejemplos: Estudiar reconstrucción humana 3D; Explorar seguimiento en un clip corto | Sin clave propia de API de IA en la ruta básica |
| [WHAM](../fichas/wham.md) | Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de video. | Tu objetivo encaja con estos ejemplos: Estudiar movimiento humano 3D; Comparar reconstrucción antes y después de refinamiento | Sin clave propia de API de IA en la ruta básica |

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
