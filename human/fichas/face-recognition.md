[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Rostros y retratos animados

# 👤 face_recognition

> Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.9k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

face_recognition, librería Python de reconocimiento facial sobre dlib, de @ageitgey. Licencia MIT. Tiene ~57k estrellas, pero su última release es v1.2.2 (abril de 2018) y el README aún menciona Python 2.7/3.3: está prácticamente sin mantenimiento.

## ¿Qué hace?

Detecta rostros, localiza rasgos faciales y compara caras con una API de alto nivel y una CLI (`face_recognition`, `face_detection`). Trae ejemplos con webcam vía OpenCV.

## ¿Cómo lo hace?

Se instala con `pip install face_recognition`, lo que requiere compilar dlib (con CMake y un compilador). En Windows no está soportado oficialmente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenCV](opencv.md) | Captura de vídeo y dibujo en los ejemplos. | Instala `opencv-python`. |
| [supervision](supervision.md) | Anotar y rastrear detecciones. (combinación por arquitectura) | Convierte las cajas a Detections. |
| [mediapipe](mediapipe.md) | Detección facial moderna y más ligera. (combinación por arquitectura) | Compara antes de adoptar. |

**Notas:** Alternativas (elige una): insightface. Se quita deep-live-cam de las combinaciones. Considera insightface o mediapipe para proyectos nuevos.

Estado en GitHub: activo · último push 2026-06-25 · última versión publicada v1.2.2 (2018-04-02) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ageitgey/face_recognition/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa API remota; compilar dependencias y ejecutar modelos consume equipo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Windows no está oficialmente soportado por esta guía; una similitud no verifica identidad ni sustituye un sistema de autenticación |
| Coste | Sin pago a un modelo en la ruta básica. No usa API remota; compilar dependencias y ejecutar modelos consume equipo |
| Equipo | Preparación según la ruta elegida. Python; dlib y CMake según sistema; fotos propias autorizadas |

Windows no está oficialmente soportado por esta guía; una similitud no verifica identidad ni sustituye un sistema de autenticación

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dlib y CMake según sistema
- fotos propias autorizadas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
pip3 install face_recognition
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ageitgey/face_recognition/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar face_recognition para mi objetivo y necesito pasos guiados. Lee https://github.com/ageitgey/face_recognition/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Localiza rostros en una imagen de prueba y revisa las cajas antes de comparar identidades.

**Qué comprobar:** Puedes comprobar qué región detectó el modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar detección facial
- Comparar dos fotos propias en un laboratorio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar detección facial; Comparar dos fotos propias en un laboratorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Windows no está oficialmente soportado por esta guía; una similitud no verifica identidad ni sustituye un sistema de autenticación

## Stack y modelos

- **Stack:** Python; dlib y CMake según sistema; fotos propias autorizadas
- **Etiquetas:** `image` `vision` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [InsightFace](insightface.md) | 30.2k | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. |

## Enlaces

- 🐙 GitHub: [ageitgey/face_recognition](https://github.com/ageitgey/face_recognition)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ageitgey/face_recognition/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
