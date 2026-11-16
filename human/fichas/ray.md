[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 📚 Ray

> Motor de cómputo distribuido para IA: escala Python de un portátil a un clúster, con bibliotecas para datos, entrenamiento, ajuste, RL y serving.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 44.3k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Framework de código abierto (Apache-2.0) creado en UC Berkeley y mantenido por Anyscale, que ofrece una plataforma gestionada. Muy maduro y usado a gran escala.

## ¿Qué hace?

Ejecuta Python distribuido con tareas y actores y ofrece bibliotecas para datos escalables, entrenamiento distribuido, ajuste de hiperparámetros, aprendizaje por refuerzo y serving programable con autoescalado.

## ¿Cómo lo hace?

Se instala con pip (extras por biblioteca); los clústeres se lanzan en nubes, máquinas propias o Kubernetes con KubeRay. Incluye panel de observabilidad.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | vLLM usa Ray para el serving distribuido en varios nodos. | Monta un clúster de Ray; después lanza vLLM con el backend distribuido de Ray. |
| [PyTorch](pytorch.md) | Ray Train distribuye entrenamientos de PyTorch. | Instala `ray[train]`; después envuelve el bucle de entrenamiento con TorchTrainer. |
| [verl](verl.md) | verl orquesta su entrenamiento por refuerzo sobre Ray. | Instala Ray en el clúster; después lanza los trabajos de verl. |
| [OpenRLHF](openrlhf.md) | OpenRLHF se basa en la arquitectura distribuida Ray + vLLM. | Monta el clúster de Ray; después lanza los trabajos de OpenRLHF. |

**Notas:** Para un solo equipo, la complejidad de Ray puede no compensar.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada ray-2.60.0 (2026-11-04) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ray-project/ray/blob/master/README.md) · [2](https://docs.ray.io/) · [3](https://docs.vllm.ai/en/latest/serving/parallelism_scaling.html)</sub>

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
pip install ray
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/ray-project/ray/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ray para mi objetivo y necesito pasos guiados. Lee https://github.com/ray-project/ray/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install ray` y paraleliza una función con `@ray.remote` en tu equipo..

**Qué comprobar:** Las tareas se ejecutan en paralelo y el panel de Ray muestra su progreso..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- paralelizar un procesamiento de datos o entrenamiento en varias máquinas
- servir modelos con autoescalado mediante Ray Serve

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: paralelizar un procesamiento de datos o entrenamiento en varias máquinas; servir modelos con autoescalado mediante Ray Serve | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `distributed` `python` `serving` `ml`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ray-project/ray](https://github.com/ray-project/ray)
- 🌐 Web: <https://ray.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ray-project/ray/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
