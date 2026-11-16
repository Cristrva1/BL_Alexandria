[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 verl

> Framework flexible y eficiente de post-entrenamiento por refuerzo para LLM (HybridFlow): PPO, GRPO y otros algoritmos con FSDP/Megatron y vLLM/SGLang.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.2k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Nivel:** 4 Experto — preparación pesada; requiere programar con él; necesita GPU; dominio especializado

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de código abierto (Apache-2.0) iniciado por ByteDance Seed y mantenido ahora por la comunidad verl-project; implementa el artículo HybridFlow. Muy activo.

## ¿Qué hace?

Permite construir flujos de post-entrenamiento por refuerzo (PPO, GRPO y variantes) con pocas líneas, mapeo flexible de modelos a GPU, integración con infraestructura existente y entrenamiento de modelos grandes, multimodales y agentes con herramientas.

## ¿Cómo lo hace?

Paquete Python sobre PyTorch y Ray; usa FSDP o Megatron-LM para entrenar y vLLM, SGLang o Hugging Face para generar. Requiere varias GPU para modelos medianos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | verl usa vLLM como motor de generación de muestras (rollout). | Instala la versión de vLLM compatible; después selecciónalo como rollout. |
| [SGLang](sglang.md) | SGLang es otro motor de rollout soportado por verl. | Instala SGLang compatible; después selecciónalo en la configuración. |
| [Ray](ray.md) | verl orquesta su flujo de entrenamiento sobre Ray. | Monta el clúster de Ray; después lanza los trabajos. |
| [Transformers](transformers.md) | verl es compatible con modelos de Hugging Face Transformers. | Indica el modelo del Hub en la configuración. |

**Notas:** Alternativas (elige una): openrlhf. La rama principal cambia rápido; fija versiones.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.9.1 (2026-09-20) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/verl-project/verl/blob/main/README.md) · [2](https://verl-project.github.io)</sub>

## Ver similares

Grupo **Aprendizaje por refuerzo para LLM**: verl ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **verl** (esta ficha) ⭐ recomendado | 68 | Si buscas esto: framework flexible y eficiente de post-entrenamiento por refuerzo para LLM (HybridFlow): PPO, GRPO y otros algoritmos con FSDP/Megatron y vLLM/SGLang. |
| 2 | [OpenRLHF](openrlhf.md) | 58 | Si buscas esto: framework de RLHF y RL agéntico escalable basado en Ray, vLLM y DeepSpeed: PPO, REINFORCE++, GRPO, RLOO y entrenamiento asíncrono. |

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

**Entrada documentada (bash):**

```
git clone --recursive https://github.com/verl-project/verl.git
```

Comando copiado literalmente de la documentación del repositorio (sección «USE_MEGATRON=0 bash verl/scripts/install_vllm_mcore_npu.sh»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/verl-project/verl/blob/main/docs/ascend_tutorial/en/get_start/install_guidance.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar verl para mi objetivo y necesito pasos guiados. Lee https://github.com/verl-project/verl/blob/main/docs/ascend_tutorial/en/get_start/install_guidance.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la guía de inicio rápido de verl en un nodo con GPU y ejecuta el ejemplo PPO o GRPO pequeño con GSM8K..

**Qué comprobar:** El entrenamiento arranca y registra recompensas por paso..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- entrenar un modelo de razonamiento con GRPO sobre problemas verificables
- investigar nuevos algoritmos de RL para LLM a escala

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: entrenar un modelo de razonamiento con GRPO sobre problemas verificables; investigar nuevos algoritmos de RL para LLM a escala | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml, requirements.txt, setup.py
- **Etiquetas:** `training` `python` `rl` `gpu`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenRLHF](openrlhf.md) | 10.2k | Framework de RLHF y RL agéntico escalable basado en Ray, vLLM y DeepSpeed: PPO, REINFORCE++, GRPO, RLOO y entrenamiento asíncrono. |

## Enlaces

- 🐙 GitHub: [verl-project/verl](https://github.com/verl-project/verl)
- 🌐 Web: <https://verl-project.github.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/verl-project/verl/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
