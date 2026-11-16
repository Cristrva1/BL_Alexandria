[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Rostros y retratos animados

# 🙂 FaceFusion

> Plataforma para intercambio y mejora de rostros en imágenes y video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.7k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

FaceFusion, plataforma de manipulación facial (intercambio y mejora de rostros) para imágenes y vídeo. Licencia OpenRAIL-AS (GitHub muestra NOASSERTION). Tiene ~31k estrellas y está activa (3.9.2).

## ¿Qué hace?

Intercambia rostros, mejora caras y fotogramas, sincroniza labios y aplica otros procesadores mediante UI o CLI (`python facefusion.py [commands]`). Incluye controles de contenido.

## ¿Cómo lo hace?

La instalación requiere conocimientos técnicos según el propio README (docs.facefusion.io) y usa Python, ONNX Runtime con aceleración CUDA, ROCm, CoreML u OpenVINO, y FFmpeg.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Procesamiento de vídeo. | Instala FFmpeg en el sistema. |
| [InsightFace](insightface.md) | Modelos de análisis facial del ecosistema. (combinación por arquitectura) | Usados en los procesadores. |
| [Real-ESRGAN](real-esrgan.md) | Escalar fotogramas tras el procesado. (combinación por arquitectura) | Aplica después. |

**Notas:** Alternativas (elige una): deep-live-cam. Riesgo ético y legal; licencia RAIL con restricciones de uso.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada 3.9.2 (2026-10-26) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/facefusion/facefusion/blob/master/README.md) · [2](https://docs.facefusion.io/installation)</sub>

## Ver similares

Grupo **Intercambio de rostros**: FaceFusion ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Deep-Live-Cam](deep-live-cam.md) ⭐ recomendado | 75 | Si buscas esto: herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. |
| 2 | **FaceFusion** (esta ficha) | 56 | Si buscas esto: plataforma para intercambio y mejora de rostros en imágenes y video. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia propia no exige API; instaladores, hardware y modelos tienen condiciones independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La instalación desde fuente requiere conocimientos técnicos; no debe presentarse la disponibilidad del código como permiso comercial de todos los pesos |
| Coste | El coste depende del proveedor o la ruta. La inferencia propia no exige API; instaladores, hardware y modelos tienen condiciones independientes |
| Equipo | Preparación según la ruta elegida. Sistema compatible; modelos; CPU o GPU; material autorizado |

La instalación desde fuente requiere conocimientos técnicos; no debe presentarse la disponibilidad del código como permiso comercial de todos los pesos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Sistema compatible
- modelos
- CPU o GPU
- material autorizado

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.facefusion.io/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FaceFusion para mi objetivo y necesito pasos guiados. Lee https://docs.facefusion.io/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Procesa una imagen de prueba y revisa bordes, color y artefactos antes de pasar a video.

**Qué comprobar:** Puedes identificar modelo y limitaciones de la salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un efecto facial consentido
- Evaluar un flujo local de imagen

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un efecto facial consentido; Evaluar un flujo local de imagen | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación desde fuente requiere conocimientos técnicos; no debe presentarse la disponibilidad del código como permiso comercial de todos los pesos

## Stack y modelos

- **Stack:** Sistema compatible; modelos; CPU o GPU; material autorizado
- **Etiquetas:** `image` `video` `vision` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Deep-Live-Cam](deep-live-cam.md) | 98.1k | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. |

## Enlaces

- 🐙 GitHub: [facefusion/facefusion](https://github.com/facefusion/facefusion)
- 🌐 Web: <https://facefusion.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/facefusion/facefusion/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
