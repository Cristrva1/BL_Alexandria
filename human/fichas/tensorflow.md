[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🧑‍💻 tensorflow

> Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 202k | Apache-2.0 | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## ¿Qué es?

TensorFlow, plataforma open source de aprendizaje automático creada en Google Brain. Licencia Apache-2.0. Es muy madura (~202k estrellas, v2.21.0).

## ¿Qué hace?

Permite construir, entrenar y desplegar modelos con APIs estables en Python y C++, además de un ecosistema de herramientas (Keras, TF Lite/LiteRT, TF Serving, TensorBoard). Hoy pierde peso frente a PyTorch en investigación.

## ¿Cómo lo hace?

Se instala con `pip install tensorflow` (o `tensorflow-cpu`) y tiene imágenes Docker. Soporta GPU NVIDIA con CUDA en Linux.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Algunos modelos tienen variante TF (el soporte se ha ido reduciendo). (combinación por arquitectura) | Comprueba el soporte del modelo. |
| [mediapipe](mediapipe.md) | Soluciones de visión sobre modelos TF Lite. (combinación por arquitectura) | Usa modelos TF Lite en MediaPipe. |
| [marimo](marimo.md) | Experimentación en notebooks reactivos. (combinación por arquitectura) | Instala marimo en el mismo entorno. |
| [JupyterLab](jupyterlab.md) | Combinación recíproca: JupyterLab lo enlaza como «Experimentar con modelos de TensorFlow paso a paso en notebooks. (combinación por arquitectura)». | Orden indicado desde JupyterLab: Instala TensorFlow en el entorno del kernel. |
| [tfjs-models](tfjs-models.md) | Combinación recíproca: tfjs-models lo enlaza como «Entrenar en Python y convertir a TF.js. (combinación por arquitectura)». | Orden indicado desde tfjs-models: Convierte con tensorflowjs_converter. |
| [Keras 3](keras.md) | Combinación recíproca: Keras 3 lo enlaza como «TensorFlow es uno de los backends de Keras 3». | Orden indicado desde Keras 3: Instala TensorFlow; después define KERAS_BACKEND=tensorflow. |

**Notas:** Alternativa (elige una): pytorch.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.21.0 (2026-03-06) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tensorflow/tensorflow/blob/master/README.md) · [2](https://www.tensorflow.org/install)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API obligatoria para ejecución propia; hardware y nube independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La instalación CPU y acelerada depende de plataforma y versión; usa el selector y guía oficiales en vez de asumir GPU en cualquier sistema |
| Coste | Sin pago a un modelo en la ruta básica. Sin API obligatoria para ejecución propia; hardware y nube independientes |
| Equipo | Preparación según la ruta elegida. Python; paquete y sistema compatibles; datos de ejemplo |

La instalación CPU y acelerada depende de plataforma y versión; usa el selector y guía oficiales en vez de asumir GPU en cualquier sistema

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- paquete y sistema compatibles
- datos de ejemplo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
pip install tensorflow
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/tensorflow/tensorflow/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar tensorflow para mi objetivo y necesito pasos guiados. Lee https://github.com/tensorflow/tensorflow/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una operación pequeña con tensores y comprueba el dispositivo antes de entrenar.

**Qué comprobar:** Puedes verificar versión y resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender redes neuronales
- Construir un clasificador educativo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender redes neuronales; Construir un clasificador educativo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación CPU y acelerada depende de plataforma y versión; usa el selector y guía oficiales en vez de asumir GPU en cualquier sistema

## Stack y modelos

- **Stack:** Python; paquete y sistema compatibles; datos de ejemplo
- **Etiquetas:** `entrenamiento` `deep-learning` `deep-neural-networks` `distributed` `machine-learning` `ml` `neural-network` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PyTorch](pytorch.md) | 106k | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. |
| [JAX](jax.md) | 36.6k | Biblioteca de Google para cómputo numérico de alto rendimiento: NumPy diferenciable, compilación JIT con XLA y vectorización en CPU, GPU y TPU. |

## Enlaces

- 🐙 GitHub: [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)
- 🌐 Web: <https://tensorflow.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tensorflow/tensorflow/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
