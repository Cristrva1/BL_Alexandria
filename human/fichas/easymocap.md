[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 🧩 EasyMocap

> Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imágenes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5k | NOASSERTION | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

EasyMocap, toolbox open source de captura de movimiento sin marcadores y síntesis de nuevas vistas desde vídeo RGB, del grupo ZJU3DV (Universidad de Zhejiang). Licencia «Project Registration License (PRL) v1.0» propia (GitHub muestra NOASSERTION). Tiene ~5k estrellas y está poco activo (v0.1).

## ¿Qué hace?

Ajusta modelos SMPL, SMPL+H, SMPL-X y MANO para capturar cuerpo, manos y cara desde una o varias cámaras, con múltiples demos. Incluye trabajos de síntesis de vistas presentados en SIGGRAPH 2022.

## ¿Cómo lo hace?

Se instala desde el repo con PyTorch. Necesita detectores de keypoints 2D (OpenPose, HRNet o MediaPipe, este último soportado desde 2021) y los modelos SMPL, que requieren registro.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [openpose](openpose.md) | Detector de keypoints 2D de entrada. | Genera los keypoints con OpenPose. |
| [mediapipe](mediapipe.md) | Detector de keypoints soportado. | Usa el detector MediaPipe. |
| [blender](blender.md) | Visualizar y animar las mallas. (combinación por arquitectura) | Importa el resultado. |

**Notas:** Sin alternativas declaradas. Revisa la licencia PRL antes de redistribuir.

Estado en GitHub: activo · último push 2026-09-15 · última versión publicada v0.1 (2021-03-29) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zju3dv/EasyMocap/blob/master/Readme.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ejecución propia usa cómputo y modelos o datasets con condiciones separadas; no incluye equipos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La calibración y el número de vistas cambian por pipeline; una demo no prueba precisión de captura con cualquier cámara o escena |
| Coste | El coste depende del proveedor o la ruta. La ejecución propia usa cómputo y modelos o datasets con condiciones separadas; no incluye equipos |
| Equipo | Preparación según la ruta elegida. Entorno de la demo; cámaras y calibración según método; modelos corporales autorizados |

La calibración y el número de vistas cambian por pipeline; una demo no prueba precisión de captura con cualquier cámara o escena

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno de la demo
- cámaras y calibración según método
- modelos corporales autorizados

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://chingswy.github.io/easymocap-public-doc/quickstart/quickstart.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar EasyMocap para mi objetivo y necesito pasos guiados. Lee https://chingswy.github.io/easymocap-public-doc/quickstart/quickstart.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Empieza por los datos de una demo y revisa correspondencia de cámaras y reconstrucción.

**Qué comprobar:** Puedes reconocer qué observaciones sustentan la pose.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar captura multicámara
- Explorar reconstrucción de movimiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar captura multicámara; Explorar reconstrucción de movimiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La calibración y el número de vistas cambian por pipeline; una demo no prueba precisión de captura con cualquier cámara o escena

## Stack y modelos

- **Stack:** Entorno de la demo; cámaras y calibración según método; modelos corporales autorizados
- **Etiquetas:** `vision` `model` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [zju3dv/EasyMocap](https://github.com/zju3dv/EasyMocap)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zju3dv/EasyMocap/blob/master/Readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
