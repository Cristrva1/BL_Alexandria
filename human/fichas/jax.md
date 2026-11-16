[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 JAX

> Biblioteca de Google para cómputo numérico de alto rendimiento: NumPy diferenciable, compilación JIT con XLA y vectorización en CPU, GPU y TPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 36.6k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) de Google. Muy madura y base de gran parte de la investigación de Google DeepMind.

## ¿Qué hace?

Ofrece diferenciación automática en modo directo e inverso, compilación JIT, vectorización automática y paralelismo en varios dispositivos sobre una API tipo NumPy, como base para bibliotecas de redes neuronales (Flax, Optax y otras).

## ¿Cómo lo hace?

Se instala con pip según el hardware (`jax` para CPU, `jax[cuda13]` para GPU NVIDIA, `jax[tpu]` para TPU). Las funciones deben ser puras para transformarse.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Keras 3](keras.md) | Keras 3 puede usar JAX como backend. | Instala JAX; después define KERAS_BACKEND=jax. |
| [Gemma (biblioteca JAX)](gemma.md) | La biblioteca oficial de Gemma está construida sobre JAX. | Instala JAX para tu hardware; después instala gemma. |
| [JupyterLab](jupyterlab.md) | JAX se usa habitualmente en cuadernos para experimentar (combinación por arquitectura). | Instala JAX en el entorno de JupyterLab. |
| [MuJoCo](mujoco.md) | Combinación recíproca: MuJoCo lo enlaza como «MJX (MuJoCo XLA) es una rama de MuJoCo escrita en JAX que permite simular miles de entornos en paralelo en GPU o TPU». | Orden indicado desde MuJoCo: Instala `mujoco-mjx` con JAX; después carga el modelo con `mjx.put_model`. |

**Notas:** Alternativas (elige una): pytorch, tensorflow.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada jax-v0.12.0.1 (2026-10-22) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jax-ml/jax/blob/main/README.md) · [2](https://docs.jax.dev/)</sub>

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
pip install -U jax
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/jax-ml/jax/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar JAX para mi objetivo y necesito pasos guiados. Lee https://github.com/jax-ml/jax/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install -U jax` y calcula el gradiente de una función simple con `jax.grad`..

**Qué comprobar:** Obtienes el valor del gradiente evaluado en el punto indicado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- entrenar modelos o simulaciones científicas en GPU o TPU
- calcular derivadas de funciones numéricas complejas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: entrenar modelos o simulaciones científicas en GPU o TPU; calcular derivadas de funciones numéricas complejas | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml, setup.py
- **Etiquetas:** `ml` `python` `library` `numerical`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PyTorch](pytorch.md) | 106k | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. |
| [tensorflow](tensorflow.md) | 202k | Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. |

## Enlaces

- 🐙 GitHub: [jax-ml/jax](https://github.com/jax-ml/jax)
- 🌐 Web: <https://docs.jax.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jax-ml/jax/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
