[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 🧩 mmpose

> Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento humano.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.1k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MMPose, toolbox de estimación de pose de OpenMMLab (incluye RTMPose). Licencia Apache-2.0. Tiene ~8k estrellas, pero no cambia desde agosto de 2025 (v1.3.2).

## ¿Qué hace?

Cubre pose 2D y 3D de cuerpo, manos, cara, animales y prendas con numerosos modelos y benchmarks.

## ¿Cómo lo hace?

Requiere PyTorch y la pila OpenMMLab (MMEngine, MMCV, MMDetection), instalada con `mim`. La compatibilidad con versiones recientes de PyTorch puede requerir trabajo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Backend. | Instala una versión compatible. |
| [OpenCV](opencv.md) | Captura y visualización. | Instala OpenCV. |
| [EasyMocap](easymocap.md) | Keypoints 2D como entrada para captura de movimiento. (combinación por arquitectura) | Exporta los keypoints. |
| [CVAT Community](cvat.md) | Combinación recíproca: CVAT Community lo enlaza como «CVAT incluye una función serverless con HRNet32 de MMPose para estimar pose de cuerpo completo». | Orden indicado desde CVAT Community: Despliega CVAT con el componente serverless; después instala la función de MMPose. |

**Notas:** Sin alternativas declaradas. Actividad baja.

Estado en GitHub: activo · último push 2025-08-04 · última versión publicada v1.3.2 (2024-07-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/open-mmlab/mmpose/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Inferencia propia sin API de pago; datasets, modelos y GPU tienen condiciones independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La documentación distingue versiones actuales y 0.x; no mezcles configuraciones y dependencias de líneas diferentes |
| Coste | Sin pago a un modelo en la ruta básica. Inferencia propia sin API de pago; datasets, modelos y GPU tienen condiciones independientes |
| Equipo | Preparación según la ruta elegida. Python; PyTorch y dependencias OpenMMLab compatibles; checkpoint |

La documentación distingue versiones actuales y 0.x; no mezcles configuraciones y dependencias de líneas diferentes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- PyTorch y dependencias OpenMMLab compatibles
- checkpoint

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://mmpose.readthedocs.io/en/latest/installation.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mmpose para mi objetivo y necesito pasos guiados. Lee https://mmpose.readthedocs.io/en/latest/installation.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una demo de pose y revisa articulaciones y confianza en una imagen conocida.

**Qué comprobar:** Puedes identificar configuración y resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar modelos de pose
- Preparar una demo de análisis de movimiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar modelos de pose; Preparar una demo de análisis de movimiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La documentación distingue versiones actuales y 0.x; no mezcles configuraciones y dependencias de líneas diferentes

## Stack y modelos

- **Stack:** Python; PyTorch y dependencias OpenMMLab compatibles; checkpoint
- **Etiquetas:** `vision` `model` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [open-mmlab/mmpose](https://github.com/open-mmlab/mmpose)
- 🌐 Web: <https://mmpose.readthedocs.io/en/latest/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/open-mmlab/mmpose/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
