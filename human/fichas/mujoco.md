[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Física y simulación

# 📚 MuJoCo

> Motor de física de Google DeepMind para simular estructuras articuladas con contacto, estándar en robótica, biomecánica y aprendizaje por refuerzo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.1k | Apache-2.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de física de código abierto (Apache-2.0) mantenido por Google DeepMind, que lo adquirió en 2021 y lo liberó en 2022. Referencia en investigación de robótica y aprendizaje por refuerzo. Muy activo.

## ¿Qué hace?

Simula con rapidez y precisión estructuras articuladas que interactúan con su entorno mediante contactos: robots, cuerpos humanos, manipulación. Incluye un compilador de modelos XML (MJCF), visualización interactiva en escritorio y navegador, funciones de cálculo físico, plugin para Unity y tutoriales en Colab.

## ¿Cómo lo hace?

La biblioteca está en C con estructuras de datos preasignadas para máximo rendimiento. Los bindings de Python (`pip install mujoco`) incluyen el motor. MJX (MuJoCo XLA) lo reimplementa en JAX para ejecutar en GPU/TPU, y MuJoCo Warp (MJWarp, con NVIDIA) lo acelera en GPUs NVIDIA.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [JAX](jax.md) | MJX (MuJoCo XLA) es una rama de MuJoCo escrita en JAX que permite simular miles de entornos en paralelo en GPU o TPU. | Instala `mujoco-mjx` con JAX; después carga el modelo con `mjx.put_model`. |
| [warp](warp.md) | MuJoCo Warp (MJWarp), mantenido por Google DeepMind y NVIDIA dentro del proyecto Newton, es una versión de MuJoCo acelerada en GPU con NVIDIA Warp. | Instala MuJoCo Warp (requiere Warp y GPU NVIDIA); después carga tus modelos MJCF. |
| [Genesis World](genesis-world.md) | Genesis importa modelos MJCF de MuJoCo y lo cita como referencia de dinámica de cuerpos rígidos. | Prepara el modelo MJCF con MuJoCo; después cárgalo en Genesis. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 4.0.1 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-deepmind/mujoco/blob/main/README.md) · [2](https://mujoco.readthedocs.io/en/stable/mjx.html) · [3](https://github.com/google-deepmind/mujoco_warp)</sub>

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
pip install mujoco
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/google-deepmind/mujoco/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MuJoCo para mi objetivo y necesito pasos guiados. Lee https://github.com/google-deepmind/mujoco/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install mujoco`, carga un modelo MJCF de ejemplo y ábrelo con `python -m mujoco.viewer`..

**Qué comprobar:** Ves el modelo simulado en el visor interactivo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- simular un robot o un brazo para probar controladores antes del hardware
- entrenar políticas de aprendizaje por refuerzo en entornos físicos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: simular un robot o un brazo para probar controladores antes del hardware; entrenar políticas de aprendizaje por refuerzo en entornos físicos | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. El código es Apache-2.0; la documentación y los recursos de la carpeta doc usan CC BY 4.0.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt
- **Etiquetas:** `simulation` `robotics` `physics` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)
- 🌐 Web: <https://mujoco.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-deepmind/mujoco/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
