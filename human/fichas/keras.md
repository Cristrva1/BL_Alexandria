[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 Keras 3

> API de deep learning multibackend: el mismo código de modelo se ejecuta sobre JAX, TensorFlow o PyTorch (y OpenVINO para inferencia).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 64.4k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) creada por François Chollet y mantenida por Google. Muy madura; Keras 3 la convirtió en multibackend.

## ¿Qué hace?

Permite definir, entrenar y desplegar modelos de visión, lenguaje, audio y series temporales con una API sencilla, eligiendo el backend más rápido para cada arquitectura, y se completa con KerasHub para modelos preentrenados.

## ¿Cómo lo hace?

Se instala con pip junto al backend elegido (JAX, TensorFlow o PyTorch); el backend se fija con la variable KERAS_BACKEND.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [JAX](jax.md) | Keras 3 puede usar JAX como backend, a menudo el más rápido. | Instala JAX; después define KERAS_BACKEND=jax. |
| [PyTorch](pytorch.md) | Keras 3 puede ejecutarse sobre PyTorch. | Instala PyTorch; después define KERAS_BACKEND=torch. |
| [tensorflow](tensorflow.md) | TensorFlow es uno de los backends de Keras 3. | Instala TensorFlow; después define KERAS_BACKEND=tensorflow. |

**Notas:** Algunas funciones dependen del backend; revisa la compatibilidad antes de cambiarlo.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v3.12.4 (2026-07-29) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/keras-team/keras/blob/master/README.md) · [2](https://keras.io/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

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
pip install keras --upgrade
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/keras-team/keras/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Keras 3 para mi objetivo y necesito pasos guiados. Lee https://github.com/keras-team/keras/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install keras --upgrade` y un backend (por ejemplo JAX), y entrena el ejemplo MNIST de la documentación..

**Qué comprobar:** El modelo entrena y muestra la precisión por época..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- prototipar una red neuronal con una API sencilla
- cambiar de backend sin reescribir el modelo para ganar rendimiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: prototipar una red neuronal con una API sencilla; cambiar de backend sin reescribir el modelo para ganar rendimiento | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml, requirements.txt
- **Etiquetas:** `ml` `python` `library` `deep-learning`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [keras-team/keras](https://github.com/keras-team/keras)
- 🌐 Web: <http://keras.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/keras-team/keras/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
