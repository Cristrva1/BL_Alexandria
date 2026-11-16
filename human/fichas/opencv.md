[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 👁️ OpenCV

> La librería de visión por computadora de referencia, con miles de algoritmos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 91.6k | Apache-2.0 | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

OpenCV, la biblioteca open source de visión por computador de referencia, gestionada por OpenCV.org. Licencia Apache-2.0. Es muy madura (~92k estrellas, 5.1.0).

## ¿Qué hace?

Ofrece miles de algoritmos de procesamiento de imagen, vídeo, calibración, características, detección, seguimiento y un módulo DNN para inferencia. Los módulos extra están en opencv_contrib.

## ¿Cómo lo hace?

Se instala en Python con `pip install opencv-python` (o `-contrib`, o `-headless` para servidores), o se compila con CMake para C++. La documentación de la rama 5.x está en docs.opencv.org/5.x.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ultralytics YOLO](ultralytics.md) | Fuente de fotogramas para YOLO. | Lee vídeo con OpenCV y pasa los frames. |
| [supervision](supervision.md) | Dibujo y anotación sobre imágenes OpenCV. | Usa los anotadores sobre arrays NumPy. |
| [mediapipe](mediapipe.md) | Captura con OpenCV y análisis con MediaPipe. (combinación por arquitectura) | Convierte BGR a RGB antes. |
| [mmpose](mmpose.md) | Combinación recíproca: mmpose lo enlaza como «Captura y visualización». | Orden indicado desde mmpose: Instala OpenCV. |
| [openpose](openpose.md) | Combinación recíproca: openpose lo enlaza como «Captura y visualización». | Orden indicado desde openpose: Instala OpenCV. |
| [kornia](kornia.md) | Combinación recíproca: kornia lo enlaza como «Preprocesado clásico fuera del grafo. (combinación por arquitectura)». | Orden indicado desde kornia: Combina según necesidad. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[DeepFace](deepface.md) · [Detectron2](detectron2.md) · [dlib](dlib.md) · [Frigate NVR](frigate.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 5.1.0 (2026-11-06) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/opencv/opencv/blob/5.x/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las operaciones básicas no necesitan modelos ni API; hardware y servicios de una app son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una biblioteca de visión por computador; no es un único modelo entrenado ni una aplicación de agentes |
| Coste | Sin pago a un modelo en la ruta básica. Las operaciones básicas no necesitan modelos ni API; hardware y servicios de una app son independientes |
| Equipo | Preparación según la ruta elegida. Paquete OpenCV para el lenguaje elegido; imagen pequeña |

Es una biblioteca de visión por computador; no es un único modelo entrenado ni una aplicación de agentes

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Paquete OpenCV para el lenguaje elegido
- imagen pequeña

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/opencv/opencv/blob/5.x/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenCV para mi objetivo y necesito pasos guiados. Lee https://github.com/opencv/opencv/blob/5.x/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga una imagen, cambia su tamaño y guarda una copia para comparar dimensiones.

**Qué comprobar:** Puedes comprobar entrada, transformación y salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar imágenes antes de OCR
- Estudiar procesamiento visual básico

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar imágenes antes de OCR; Estudiar procesamiento visual básico | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca de visión por computador; no es un único modelo entrenado ni una aplicación de agentes

## Stack y modelos

- **Stack:** Paquete OpenCV para el lenguaje elegido; imagen pequeña
- **Etiquetas:** `vision` `image` `cpp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [opencv/opencv](https://github.com/opencv/opencv)
- 🌐 Web: <https://opencv.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/opencv/opencv/blob/5.x/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
