[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Física y simulación

# 📚 Genesis World

> Plataforma de simulación para IA física y robótica con motor multifísica unificado (rígidos, FEM, MPM, fluidos), render fotorrealista y paralelismo masivo en GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.2k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** hard

**Nivel:** 3 Avanzado — pip install; simulación física con GPU · corregido a mano

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de simulación de código abierto (Apache-2.0), antes llamada Genesis, que nació como proyecto académico en diciembre de 2024 y ahora cuenta con el apoyo de la empresa Genesis AI. Muy activa (Genesis World 1.0).

## ¿Qué hace?

Simula robótica e IA física con un motor multifísica unificado (cuerpos rígidos, FEM, MPM, partículas PBD/SPH, IPC) en una misma escena; importa URDF, MJCF, OBJ, GLB y USD; ofrece sensores, controladores, entornos paralelos y heterogéneos, GUI integrada y renderizado fotorrealista para generar datos.

## ¿Cómo lo hace?

Se instala con pip (Python 3.12–3.14) después de instalar PyTorch. El compilador Quadrants traduce kernels de Python a CUDA, AMD ROCm, Apple Metal, Vulkan, x86 y ARM64, con diferenciación automática. Los renderizadores (Nyx, Luisa, Pyrender) se conectan como sensores de cámara.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Genesis requiere PyTorch instalado y expone los estados de la simulación como tensores para entrenar políticas. | Instala PyTorch para tu plataforma; después `pip install genesis-world`. |
| [MuJoCo](mujoco.md) | Genesis importa modelos MJCF (el formato de MuJoCo) y cita MuJoCo como referencia para su dinámica de cuerpos rígidos. | Prepara o descarga el modelo MJCF; después cárgalo como entidad en Genesis. |
| [blender](blender.md) | Genesis importa mallas OBJ, GLB y USD que puedes crear o preparar en Blender (combinación por arquitectura). | Modela o limpia el objeto en Blender y expórtalo a GLB; después añádelo a la escena de Genesis. |

**Notas:** Simulador cercano a MuJoCo e Isaac; Genesis prioriza multifísica y paralelismo en GPU.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.4.6 (2026-11-08) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/README.md) · [2](https://genesis-world.readthedocs.io)</sub>

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
pip install genesis-world
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Genesis World para mi objetivo y necesito pasos guiados. Lee https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala PyTorch y después `pip install genesis-world`; ejecuta el ejemplo `examples/rigid/single_franka.py`..

**Qué comprobar:** Se simula un brazo Franka en una escena con visor..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- entrenar políticas de robots con miles de entornos paralelos en GPU
- generar datos sintéticos de manipulación con cuerpos rígidos y deformables

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: entrenar políticas de robots con miles de entornos paralelos en GPU; generar datos sintéticos de manipulación con cuerpos rígidos y deformables | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `simulation` `robotics` `physics` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Genesis-Embodied-AI/genesis-world](https://github.com/Genesis-Embodied-AI/genesis-world)
- 🌐 Web: <https://genesis-world.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
