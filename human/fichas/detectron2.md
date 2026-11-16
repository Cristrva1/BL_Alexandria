[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 📚 Detectron2

> Biblioteca de Meta AI para detección de objetos y segmentación (instancias, panóptica, keypoints) sobre PyTorch, con un zoo de modelos preentrenados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** hard

## ¿Qué es?

Biblioteca de investigación de código abierto (Apache-2.0) de Facebook AI Research (Meta), sucesora de Detectron y maskrcnn-benchmark. Muy citada, pero con mantenimiento bajo: la última versión publicada es v0.6 (2021) y el último push es de octubre de 2026.

## ¿Qué hace?

Proporciona algoritmos de detección y segmentación: detección de objetos, segmentación de instancias, semántica y panóptica, keypoints, DensePose, cajas rotadas, PointRend, DeepLab, ViTDet y MViTv2, con un zoo de modelos preentrenados y proyectos de investigación construidos encima.

## ¿Cómo lo hace?

Está escrita en Python sobre PyTorch con extensiones C++/CUDA que se compilan al instalar. Usa configuraciones declarativas (YACS o LazyConfig) y permite exportar modelos a TorchScript para despliegue.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Detectron2 está construida sobre PyTorch y requiere una versión compatible instalada antes. | Instala PyTorch con CUDA; después compila Detectron2 siguiendo la guía oficial. |
| [CVAT Community](cvat.md) | CVAT incluye una función serverless con RetinaNet de Detectron2 para preanotar imágenes automáticamente. | Despliega CVAT con soporte serverless (Nuclio); después activa la función de Detectron2. |
| [OpenCV](opencv.md) | La demo de Detectron2 usa OpenCV para leer imágenes, vídeo o cámara y dibujar resultados. | Instala OpenCV junto a Detectron2; después ejecuta `demo/demo.py`. |

**Notas:** Para detección en producción, Ultralytics (YOLO) suele ser más sencillo; Detectron2 sigue siendo útil en investigación y segmentación avanzada.

Estado en GitHub: activo · último push 2026-10-27 · última versión publicada v0.6 (2021-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/facebookresearch/detectron2/blob/main/README.md) · [2](https://detectron2.readthedocs.io/tutorials/install.html) · [3](https://github.com/cvat-ai/cvat/blob/develop/README.md)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/facebookresearch/detectron2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Detectron2 para mi objetivo y necesito pasos guiados. Lee https://github.com/facebookresearch/detectron2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la guía de instalación oficial (requiere PyTorch y compilar extensiones) y ejecuta la demo con un modelo del zoo sobre una imagen..

**Qué comprobar:** Obtienes la imagen con cajas y máscaras de los objetos detectados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- entrenar un detector o segmentador sobre un conjunto de imágenes propio
- usar modelos preentrenados de detección como base para investigación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: entrenar un detector o segmentador sobre un conjunto de imágenes propio; usar modelos preentrenados de detección como base para investigación | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Mantenimiento bajo: la última versión publicada es v0.6 (noviembre de 2021) y los cambios recientes son esporádicos; para proyectos nuevos valora alternativas más activas.

## Stack y modelos

- **Stack:** Python, setup.py
- **Etiquetas:** `vision` `pytorch` `detection` `segmentation`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [facebookresearch/detectron2](https://github.com/facebookresearch/detectron2)
- 🌐 Web: <https://detectron2.readthedocs.io/en/latest/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/facebookresearch/detectron2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
