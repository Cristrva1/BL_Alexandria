[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Rostros y retratos animados

# 📚 DeepFace

> Biblioteca Python ligera de reconocimiento facial y análisis de atributos (edad, género, emoción) que envuelve modelos como ArcFace, FaceNet o VGG-Face.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.7k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 3 Avanzado — preparación sencilla; requiere programar con él; necesita GPU

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (MIT) creada por Sefik Ilkin Serengil. Muy popular y activa; su autor ofrece además una API gestionada (deepface.dev).

## ¿Qué hace?

Verifica si dos caras son de la misma persona, busca una cara en una base de imágenes, extrae embeddings faciales y estima edad, género, emoción y origen étnico aparentes. Incluye detección facial con varios backends (OpenCV, SSD, Dlib, MTCNN, RetinaFace, MediaPipe, YOLO, YuNet, CenterFace), API REST y gRPC, y análisis en tiempo real con cámara.

## ¿Cómo lo hace?

Se instala con pip; usa ONNX Runtime por defecto o TensorFlow/PyTorch con extras. Descarga los pesos de cada modelo al primer uso. Funciona en CPU; la GPU acelera el análisis por lotes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenCV](opencv.md) | OpenCV es el detector facial por defecto de DeepFace y se usa para leer imágenes y vídeo. | Instala DeepFace (incluye OpenCV); después elige `detector_backend="opencv"`. |
| [dlib](dlib.md) | DeepFace incluye Dlib como detector facial y como modelo de reconocimiento. | Instala `dlib`; después usa `detector_backend="dlib"` o `model_name="Dlib"`. |
| [mediapipe](mediapipe.md) | DeepFace puede usar MediaPipe como detector facial. | Instala `mediapipe`; después usa `detector_backend="mediapipe"`. |
| [Ultralytics YOLO](ultralytics.md) | Los detectores YOLO (yolov8, yolov11, yolov12) de DeepFace usan Ultralytics. | Instala `ultralytics`; después usa por ejemplo `detector_backend="yolov11n"`. |
| [InsightFace](insightface.md) | El modelo de reconocimiento Buffalo_L que envuelve DeepFace procede de InsightFace. | Instala DeepFace; después usa `model_name="Buffalo_L"` (revisa la licencia de los pesos de InsightFace). |

**Notas:** Úsalo solo con imágenes propias o con consentimiento; la estimación de atributos como el origen étnico es sensible y puede tener sesgos.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.0.105 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/serengil/deepface/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
pip install deepface
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/serengil/deepface/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepFace para mi objetivo y necesito pasos guiados. Lee https://github.com/serengil/deepface/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install deepface` y ejecuta `DeepFace.verify` con dos imágenes tuyas..

**Qué comprobar:** Obtienes un diccionario con `verified`, la distancia y el umbral usado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- verificar si dos fotos propias o autorizadas corresponden a la misma persona
- buscar una cara dentro de una carpeta de imágenes con consentimiento de las personas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: verificar si dos fotos propias o autorizadas corresponden a la misma persona; buscar una cara dentro de una carpeta de imágenes con consentimiento de las personas | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Reconocimiento facial: tratar datos biométricos está regulado (p. ej. RGPD o LFPDPPP) y requiere base legal o consentimiento. Algunos modelos envueltos tienen licencias propias.

## Stack y modelos

- **Stack:** Python, Dockerfile, setup.py
- **Etiquetas:** `face` `python` `vision` `biometrics`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [serengil/deepface](https://github.com/serengil/deepface)
- 🌐 Web: <https://www.youtube.com/watch?v=WnUVYQP4h44&list=PLsS_1RYmYQQFdWqxQggXHynP1rqaYXv_E>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/serengil/deepface/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
