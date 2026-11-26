[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ PyTorch

> Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 106k | BSD-3-Clause | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; requiere programar con él; necesita GPU; dominio especializado

**Puntuación de calidad** 78/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** BSD-3-Clause. Fuente: [LICENSE](https://github.com/pytorch/pytorch/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

PyTorch, framework de deep learning con tensores acelerados por GPU y autograd dinámico, gobernado por la PyTorch Foundation (Linux Foundation). Licencia de estilo BSD (GitHub muestra NOASSERTION). Es muy madura (~106k estrellas, v2.15.0).

## ¿Qué hace?

Ofrece cálculo de tensores tipo NumPy en GPU, redes neuronales con autograd basado en cinta, ejecución imperativa y compilación (`torch.compile`). Es la base de la mayoría de librerías modernas de modelos.

## ¿Cómo lo hace?

Se instala con binarios por plataforma (pip o conda, con selector CUDA, ROCm o CPU en pytorch.org) o desde el código fuente. Soporta GPU NVIDIA (CUDA), AMD (ROCm), Intel y Jetson.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Modelos preentrenados sobre PyTorch. | Instala PyTorch y luego Transformers. |
| [diffusers](diffusers.md) | Modelos de difusión sobre PyTorch. | Instala Diffusers. |
| [vLLM](vllm.md) | Inferencia en producción construida sobre PyTorch. | Instala vLLM con la versión de PyTorch compatible. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (34). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[4D-Humans](4d-humans.md) · [Accelerate](accelerate.md) · [awesome-machine-learning](awesome-machine-learning.md) · [BentoML](bentoml.md) · [bionemo-recipes](bionemo-recipes.md) · [chaiNNer](chainner.md) · [cosmos](cosmos.md) · [Demucs](demucs.md) · [Detectron2](detectron2.md) · [F5-TTS](f5-tts.md) · [FinGPT](fingpt.md) · [Genesis World](genesis-world.md) · [how-to-train-your-gpt](how-to-train-your-gpt.md) · [JupyterLab](jupyterlab.md) · [Keras 3](keras.md) · [kornia](kornia.md) · [labml.ai Annotated Paper Implementations](annotated-dl-papers.md) · [LLM Course](llm-course.md) · [llm.c](llm-c.md) · [LLMs from Scratch](llms-from-scratch.md) · [LTX-2](ltx-2.md) · [mmpose](mmpose.md) · [nanochat](nanochat.md) · [NeMo Speech](nemo.md) · [pyannote.audio](pyannote-audio.md) · [PyTorch Lightning](pytorch-lightning.md) · [Ray](ray.md) · [TimesFM](timesfm.md) · [torchtune](torchtune.md) · [train-llm-from-scratch](train-llm-from-scratch.md) · [warp](warp.md) · [WHAM](wham.md) · [whisper](whisper.md) · [YuE2](yue.md)

**Notas:** Alternativa (elige una): tensorflow.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.15.0 (2026-10-28) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pytorch/pytorch/blob/main/README.md) · [2](https://pytorch.org/get-started/locally/)</sub>

## Ver similares

Grupo **Frameworks de deep learning**: PyTorch ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [tensorflow](tensorflow.md) ⭐ recomendado | 79 | Si buscas esto: framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. |
| 2 | **PyTorch** (esta ficha) | 78 | Si buscas esto: framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. |
| 3 | [JAX](jax.md) | 65 | Si buscas esto: biblioteca de Google para cómputo numérico de alto rendimiento: NumPy diferenciable, compilación JIT con XLA y vectorización en CPU, GPU y TPU. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de IA para cómputo propio; hardware y nube se pagan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Para principiantes conviene instalar un binario compatible; los comandos de compilar todo el repositorio son para desarrollo del framework |
| Coste | Sin pago a un modelo en la ruta básica. Sin API de IA para cómputo propio; hardware y nube se pagan aparte |
| Equipo | Preparación según la ruta elegida. Python compatible; paquete para CPU o tu GPU; entorno aislado |

Para principiantes conviene instalar un binario compatible; los comandos de compilar todo el repositorio son para desarrollo del framework

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python compatible
- paquete para CPU o tu GPU
- entorno aislado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest
```

Comando copiado literalmente de el README (sección «Using pre-built images»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/pytorch/pytorch/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PyTorch para mi objetivo y necesito pasos guiados. Lee https://github.com/pytorch/pytorch/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa el selector oficial de instalación y realiza una operación pequeña con tensores.

**Qué comprobar:** Puedes comprobar versión, dispositivo y resultado numérico.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender tensores
- Entrenar una red educativa

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender tensores; Entrenar una red educativa | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Para principiantes conviene instalar un binario compatible; los comandos de compilar todo el repositorio son para desarrollo del framework

## Stack y modelos

- **Stack:** Python compatible; paquete para CPU o tu GPU; entorno aislado
- **Etiquetas:** `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [tensorflow](tensorflow.md) | 202k | Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. |
| [JAX](jax.md) | 36.6k | Biblioteca de Google para cómputo numérico de alto rendimiento: NumPy diferenciable, compilación JIT con XLA y vectorización en CPU, GPU y TPU. |

## Enlaces

- 🐙 GitHub: [pytorch/pytorch](https://github.com/pytorch/pytorch)
- 🌐 Web: <https://pytorch.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pytorch/pytorch/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
