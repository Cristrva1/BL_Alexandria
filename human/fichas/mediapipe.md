[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 📚 mediapipe

> Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplicaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.7k | Apache-2.0 | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MediaPipe, framework de Google AI Edge para ML en dispositivo. Licencia Apache-2.0. Es maduro (~38k estrellas, v1.2.3).

## ¿Qué hace?

Ofrece MediaPipe Tasks (detección y landmarks de cara, manos y pose, segmentación, clasificación, LLM Inference y más) y Model Maker para personalizar modelos. Funciona en Android, iOS, web, escritorio, edge e IoT.

## ¿Cómo lo hace?

Se instala con `pip install mediapipe` o con los SDK de Android, iOS y web. La documentación principal está en developers.google.com/edge/mediapipe; las antiguas «Legacy Solutions» se sustituyeron por Tasks.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenCV](opencv.md) | Captura de vídeo en escritorio. | Lee frames con OpenCV y pásalos a Tasks. |
| [tfjs-models](tfjs-models.md) | Modelos de pose en navegador con backend MediaPipe. | Elige el runtime `mediapipe` en pose-detection. |
| [three.js](three-js.md) | Avatares controlados por landmarks. (combinación por arquitectura) | Mapea landmarks a un esqueleto 3D. |
| [EasyMocap](easymocap.md) | Combinación recíproca: EasyMocap lo enlaza como «Detector de keypoints soportado». | Orden indicado desde EasyMocap: Usa el detector MediaPipe. |
| [tensorflow](tensorflow.md) | Combinación recíproca: tensorflow lo enlaza como «Soluciones de visión sobre modelos TF Lite. (combinación por arquitectura)». | Orden indicado desde tensorflow: Usa modelos TF Lite en MediaPipe. |
| [DeepFace](deepface.md) | Combinación recíproca: DeepFace lo enlaza como «DeepFace puede usar MediaPipe como detector facial». | Orden indicado desde DeepFace: Instala `mediapipe`; después usa `detector_backend="mediapipe"`. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v1.2.3 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-ai-edge/mediapipe/blob/master/README.md) · [2](https://developers.google.com/edge/mediapipe/solutions/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ejecución en dispositivo no exige API de modelo alojado; distribución, modelos y hardware tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. MediaPipe Solutions y compilar el Framework son rutas diferentes; elige la tarea antes de preparar todo el entorno |
| Coste | Sin pago a un modelo en la ruta básica. La ejecución en dispositivo no exige API de modelo alojado; distribución, modelos y hardware tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Plataforma y SDK elegidos; modelo de tarea; imagen o clip de prueba |

MediaPipe Solutions y compilar el Framework son rutas diferentes; elige la tarea antes de preparar todo el entorno

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Plataforma y SDK elegidos
- modelo de tarea
- imagen o clip de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://developers.google.com/edge/mediapipe/solutions/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mediapipe para mi objetivo y necesito pasos guiados. Lee https://developers.google.com/edge/mediapipe/solutions/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una tarea como landmarks de manos y revisa sus puntos en una muestra.

**Qué comprobar:** Puedes distinguir tarea, modelo y SDK.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear una interacción con manos
- Prototipar visión en dispositivo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear una interacción con manos; Prototipar visión en dispositivo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MediaPipe Solutions y compilar el Framework son rutas diferentes; elige la tarea antes de preparar todo el entorno

## Stack y modelos

- **Stack:** Plataforma y SDK elegidos; modelo de tarea; imagen o clip de prueba
- **Etiquetas:** `vision` `library` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe)
- 🌐 Web: <https://ai.google.dev/edge/mediapipe>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-ai-edge/mediapipe/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
