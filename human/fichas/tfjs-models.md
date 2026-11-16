[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 📚 tfjs-models

> Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en aplicaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.8k | Apache-2.0 | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección de modelos preentrenados portados a TensorFlow.js, de Google. Licencia Apache-2.0. Tiene ~15k estrellas y está poco activa (último cambio en junio de 2026).

## ¿Qué hace?

Ofrece modelos listos para el navegador o Node: MobileNet, COCO-SSD, detección de pose, manos y landmarks faciales, DeepLab, toxicidad, comandos de voz y otros, para usar directamente o en transfer learning.

## ¿Cómo lo hace?

Se instala por paquete npm (por ejemplo `npm i @tensorflow-models/pose-detection`) o desde unpkg, junto con `@tensorflow/tfjs`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [mediapipe](mediapipe.md) | Runtime alternativo en pose-detection. | Elige el runtime `mediapipe`. |
| [tensorflow](tensorflow.md) | Entrenar en Python y convertir a TF.js. (combinación por arquitectura) | Convierte con tensorflowjs_converter. |
| [three.js](three-js.md) | Interacción 3D a partir de pose o manos. (combinación por arquitectura) | Mapea los keypoints a la escena. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-06-23 · última versión publicada tasks-v0.0.1-alpha.6 (2021-05-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tensorflow/tfjs-models/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API de IA para modelos descargados; descarga, hosting y equipo tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Cada modelo tiene su paquete, guía y licencia; no existe una instalación única que haga funcionar automáticamente toda la colección |
| Coste | Sin pago a un modelo en la ruta básica. No necesita API de IA para modelos descargados; descarga, hosting y equipo tienen costes propios |
| Equipo | Preparación según la ruta elegida. Proyecto JavaScript; modelo específico; navegador o runtime compatible |

Cada modelo tiene su paquete, guía y licencia; no existe una instalación única que haga funcionar automáticamente toda la colección

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto JavaScript
- modelo específico
- navegador o runtime compatible

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/tensorflow/tfjs-models/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar tfjs-models para mi objetivo y necesito pasos guiados. Lee https://github.com/tensorflow/tfjs-models/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige un modelo de clasificación y revisa una predicción sobre una imagen conocida.

**Qué comprobar:** Puedes identificar paquete, pesos y formato de salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar ML en el navegador
- Preparar una demo de landmarks

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar ML en el navegador; Preparar una demo de landmarks | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Cada modelo tiene su paquete, guía y licencia; no existe una instalación única que haga funcionar automáticamente toda la colección

## Stack y modelos

- **Stack:** Proyecto JavaScript; modelo específico; navegador o runtime compatible
- **Etiquetas:** `vision` `library` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [tensorflow/tfjs-models](https://github.com/tensorflow/tfjs-models)
- 🌐 Web: <https://js.tensorflow.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tensorflow/tfjs-models/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
