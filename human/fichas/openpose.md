[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 🧩 openpose

> Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.6k | NOASSERTION | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

OpenPose, sistema de CMU que fue el primero en detectar en tiempo real keypoints de cuerpo, manos, cara y pies de varias personas. Licencia académica, gratuita solo para uso no comercial (GitHub muestra NOASSERTION). Tiene ~35k estrellas, pero es histórico: sin cambios desde agosto de 2024 (v1.7.0).

## ¿Qué hace?

Estima hasta 135 keypoints por persona en imágenes y vídeo, con API C++ y Python y una demo.

## ¿Cómo lo hace?

Se compila con CMake en Linux, macOS o Windows, con CUDA y cuDNN para tiempo real, o usando binarios para Windows. Depende de Caffe.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenCV](opencv.md) | Captura y visualización. | Instala OpenCV. |
| [EasyMocap](easymocap.md) | Usa keypoints 2D estilo OpenPose para ajustar SMPL. | Genera los keypoints y pásalos a EasyMocap. |
| [ComfyUI](comfyui.md) | Mapas de pose OpenPose como condición en flujos de imagen. (combinación por arquitectura) | Usa los preprocesadores de pose en ComfyUI. |

**Notas:** Sin alternativas declaradas. Licencia no comercial e inactivo.

Estado en GitHub: activo · último push 2024-08-03 · última versión publicada v1.7.0 (2020-11-17) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Uso no comercial bajo su licencia; uso comercial requiere licencia propia; hardware separado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Detecta keypoints y no mide clínicamente una postura ni garantiza seguimiento sin errores u oclusiones |
| Coste | El coste depende del proveedor o la ruta. Uso no comercial bajo su licencia; uso comercial requiere licencia propia; hardware separado |
| Equipo | Preparación según la ruta elegida. Plataforma compatible; dependencias de compilación; modelos; imagen autorizada |

Detecta keypoints y no mide clínicamente una postura ni garantiza seguimiento sin errores u oclusiones

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Plataforma compatible
- dependencias de compilación
- modelos
- imagen autorizada

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openpose para mi objetivo y necesito pasos guiados. Lee https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Procesa una imagen de muestra y revisa puntos de articulación visibles y ocultos.

**Qué comprobar:** Puedes identificar fallos de pose.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar estimación de postura
- Preparar puntos de movimiento para una demo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar estimación de postura; Preparar puntos de movimiento para una demo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Detecta keypoints y no mide clínicamente una postura ni garantiza seguimiento sin errores u oclusiones

## Stack y modelos

- **Stack:** Plataforma compatible; dependencias de compilación; modelos; imagen autorizada
- **Etiquetas:** `vision` `model` `c`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- 🌐 Web: <https://cmu-perceptual-computing-lab.github.io/openpose>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
