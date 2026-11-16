[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 📚 dlib

> Toolkit C++ con bindings de Python para aprendizaje automático y visión: detección de caras, 68 puntos faciales, seguimiento de objetos y optimización.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.5k | BSL-1.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Toolkit de código abierto (Boost Software License) creado y mantenido por Davis King desde 2002. Clásico y estable, con cambios continuos pero menos frecuentes que en bibliotecas más nuevas.

## ¿Qué hace?

Ofrece algoritmos de aprendizaje automático (SVM, regresión, clustering, redes profundas con su propio módulo), procesamiento de imagen, detección de objetos HOG y CNN, detección de caras, predicción de 68 puntos faciales, reconocimiento facial, seguimiento de objetos, optimización numérica y utilidades de redes e hilos.

## ¿Cómo lo hace?

Biblioteca C++17 que se compila con CMake (con AVX y CUDA opcionales); los bindings de Python se instalan con `pip install dlib`, que compila el código. Los modelos preentrenados se descargan desde dlib.net.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DeepFace](deepface.md) | DeepFace usa dlib como detector facial y como modelo de reconocimiento (`Dlib`). | Instala dlib; después elige el backend `dlib` en DeepFace. |
| [OpenCV](opencv.md) | dlib incluye `cv_image` para trabajar directamente con imágenes de OpenCV en C++, y en Python ambos comparten arrays de NumPy. | Lee los fotogramas con OpenCV; después pásalos a los detectores de dlib. |
| [Claude Code](claude-code.md) | dlib es una biblioteca C++/Python que un agente de código puede integrar y compilar en tu proyecto (combinación por arquitectura). | Instala CMake y dlib; después pide al agente el código de integración. |

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v20.1 (2026-11-14) · licencia declarada BSL-1.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/davisking/dlib/blob/master/README.md) · [2](http://dlib.net)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
pip install dlib
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/davisking/dlib/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dlib para mi objetivo y necesito pasos guiados. Lee https://github.com/davisking/dlib/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install dlib` (necesita CMake y compilador) y ejecuta el ejemplo de detección facial de la carpeta python_examples..

**Qué comprobar:** Obtienes las coordenadas de las caras detectadas en la imagen..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- detectar caras y sus puntos de referencia en fotos para alinear o recortar
- usar un detector rápido en CPU dentro de una aplicación C++

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: detectar caras y sus puntos de referencia en fotos para alinear o recortar; usar un detector rápido en CPU dentro de una aplicación C++ | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt, pyproject.toml, setup.py
- **Etiquetas:** `vision` `cpp` `python` `face`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [davisking/dlib](https://github.com/davisking/dlib)
- 🌐 Web: <http://dlib.net>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/davisking/dlib/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
