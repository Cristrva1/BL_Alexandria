[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Física y simulación

# 🧑‍💻 warp

> Framework de NVIDIA para kernels y simulación física en CPU o GPU; no es un modelo ni un terminal.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.3k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; requiere programar con él

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

NVIDIA Warp, framework Python para simulación, robótica y ML acelerados por GPU. Licencia Apache-2.0. Es maduro (~7.3k estrellas, v1.19.0).

## ¿Qué hace?

Compila con JIT funciones Python normales a kernels eficientes para CPU o GPU. Ofrece primitivas de simulación física, geometría y robótica, y sus kernels son diferenciables, así que se integran en pipelines de ML.

## ¿Cómo lo hace?

Requiere Python 3.11+ y se instala con `pip install warp-lang` (extras `[examples]` para USD). Hay wheels para Windows, Linux y macOS (Apple Silicon solo CPU); la GPU requiere CUDA.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Interoperabilidad de tensores para ML diferenciable. | Convierte arrays con las utilidades de interop. |
| [blender](blender.md) | Visualizar resultados exportados a USD. (combinación por arquitectura) | Importa el USD en Blender. |
| [cosmos](cosmos.md) | Datos de simulación para modelos de mundo. (combinación por arquitectura) | Genera escenas con Warp. |
| [MuJoCo](mujoco.md) | Combinación recíproca: MuJoCo lo enlaza como «MuJoCo Warp (MJWarp), mantenido por Google DeepMind y NVIDIA dentro del proyecto Newton, es una versión de MuJoCo acelerada en GPU con NVIDIA Warp». | Orden indicado desde MuJoCo: Instala MuJoCo Warp (requiere Warp y GPU NVIDIA); después carga tus modelos MJCF. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.19.0 (2026-11-02) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA/warp/blob/main/README.md) · [2](https://nvidia.github.io/warp/stable/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de IA; GPU, energía y servicios de cómputo son costes separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. NVIDIA Warp es un framework de kernels y simulación, no el terminal Warp ni un modelo conversacional; corresponde mejor a simulación y gráficos que a fine-tuning de LLM |
| Coste | Sin pago a un modelo en la ruta básica. Sin API de IA; GPU, energía y servicios de cómputo son costes separados |
| Equipo | Preparación según la ruta elegida. Python 3.11+; CPU o GPU soportada; ejemplo pequeño |

NVIDIA Warp es un framework de kernels y simulación, no el terminal Warp ni un modelo conversacional; corresponde mejor a simulación y gráficos que a fine-tuning de LLM

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11+
- CPU o GPU soportada
- ejemplo pequeño

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (text):**

```
pip install warp-lang
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NVIDIA/warp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar warp para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/warp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una simulación de ejemplo con pocas partículas y revisa su evolución.

**Qué comprobar:** Puedes identificar kernel, dispositivo y estado simulado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar simulación física
- Prototipar cómputo para robótica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar simulación física; Prototipar cómputo para robótica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** NVIDIA Warp es un framework de kernels y simulación, no el terminal Warp ni un modelo conversacional; corresponde mejor a simulación y gráficos que a fine-tuning de LLM

## Stack y modelos

- **Stack:** Python 3.11+; CPU o GPU soportada; ejemplo pequeño
- **Etiquetas:** `entrenamiento` `cuda` `differentiable-programming` `gpu` `gpu-acceleration` `nvidia` `nvidia-warp` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [NVIDIA/warp](https://github.com/NVIDIA/warp)
- 🌐 Web: <https://nvidia.github.io/warp/stable/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA/warp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
