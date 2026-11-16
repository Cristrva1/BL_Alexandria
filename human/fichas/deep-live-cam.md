[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Rostros y retratos animados

# 🎭 Deep-Live-Cam

> Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 98.1k | AGPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Puntuación de calidad** 75/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Deep-Live-Cam, herramienta de intercambio de rostros (face swap) y deepfake en tiempo real a partir de una sola imagen, de @hacksider. Licencia AGPL-3.0. Tiene ~98k estrellas y versión 2.8, y vende una versión precompilada «Ultimate» (quickstart) en deeplivecam.net.

## ¿Qué hace?

Sustituye rostros en webcam o vídeo en tiempo real con un clic. El README incluye un descargo ético y un filtro integrado contra contenido inapropiado, y pide consentimiento y etiquetar los deepfakes.

## ¿Cómo lo hace?

La instalación manual requiere conocimientos técnicos: Python (el README menciona 3.14), `pip install -r requirements.txt` y descargar los modelos ONNX `inswapper_128_fp16` y `gfpgan-1024` de Hugging Face. Soporta CUDA, CoreML (Apple Silicon) y otros proveedores de ONNX Runtime.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [InsightFace](insightface.md) | Modelo de intercambio (inswapper) y análisis facial. | Viene como dependencia. |
| [OBS Studio](obs-studio.md) | Emitir la cámara virtual. (combinación por arquitectura) | Captura la salida en OBS. |
| [CodeFormer](codeformer.md) | Restaurar rostros en vídeo procesado offline. (combinación por arquitectura) | Aplica sobre los fotogramas. |

**Notas:** Alternativas (elige una): facefusion. Riesgo ético y legal alto (suplantación).

Estado en GitHub: activo · último push 2026-11-08 · última versión publicada 2.8 (2026-10-22) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md)</sub>

## Ver similares

Grupo **Intercambio de rostros**: Deep-Live-Cam ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Deep-Live-Cam** (esta ficha) ⭐ recomendado | 75 | Si buscas esto: herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. |
| 2 | [FaceFusion](facefusion.md) | 56 | Si buscas esto: plataforma para intercambio y mejora de rostros en imágenes y video. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ejecución local no exige API; hardware y licencias de modelos como InsightFace se revisan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El autor advierte instalación técnica; los pesos de reconocimiento o intercambio pueden tener restricciones no comerciales aunque el código sea accesible |
| Coste | Sin pago a un modelo en la ruta básica. La ejecución local no exige API; hardware y licencias de modelos como InsightFace se revisan aparte |
| Equipo | Preparación según la ruta elegida. Python compatible; FFmpeg; modelos ONNX; CPU o GPU según backend; imágenes autorizadas |

El autor advierte instalación técnica; los pesos de reconocimiento o intercambio pueden tener restricciones no comerciales aunque el código sea accesible

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python compatible
- FFmpeg
- modelos ONNX
- CPU o GPU según backend
- imágenes autorizadas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
git clone --depth 1 https://github.com/hacksider/Deep-Live-Cam.git
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Deep-Live-Cam para mi objetivo y necesito pasos guiados. Lee https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba con imágenes propias o autorizadas y revisa artefactos en una salida corta etiquetada como sintética.

**Qué comprobar:** Puedes comparar original y resultado y reconocer errores visibles.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un efecto facial consentido
- Probar un pipeline local de video

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un efecto facial consentido; Probar un pipeline local de video | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor advierte instalación técnica; los pesos de reconocimiento o intercambio pueden tener restricciones no comerciales aunque el código sea accesible

## Stack y modelos

- **Stack:** Python compatible; FFmpeg; modelos ONNX; CPU o GPU según backend; imágenes autorizadas
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FaceFusion](facefusion.md) | 30.7k | Plataforma para intercambio y mejora de rostros en imágenes y video. |

## Enlaces

- 🐙 GitHub: [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
- 🌐 Web: <https://deeplivecam.net/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
