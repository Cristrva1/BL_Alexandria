[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Modelos abiertos y entrenamiento

Modelos, bibliotecas de entrenamiento y ajuste fino. Revisa la licencia de los pesos, la memoria necesaria y la opción de inferencia antes de descargar o entrenar.

25 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Unsloth](../fichas/unsloth.md) | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales. | API de IA opcional |
| [TimesFM](../fichas/timesfm.md) | Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por versión. | API de IA opcional |

## Secciones

- [Entrenar y afinar modelos](#entrenar-y-afinar-modelos) — 18 repos
- [Modelos abiertos y fundacionales](#modelos-abiertos-y-fundacionales) — 7 repos

## Entrenar y afinar modelos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Unsloth](../fichas/unsloth.md) | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales. | Tu objetivo encaja con estos ejemplos: Probar inferencia local; Preparar un ajuste fino pequeño | API de IA opcional |
| [tensorflow](../fichas/tensorflow.md) | Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. | Tu objetivo encaja con estos ejemplos: Aprender redes neuronales; Construir un clasificador educativo | Sin clave propia de API de IA en la ruta básica |
| [Transformers](../fichas/transformers.md) | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. | Tu objetivo encaja con estos ejemplos: Clasificar un texto localmente; Probar un modelo de visión | Sin clave propia de API de IA en la ruta básica |
| [PyTorch](../fichas/pytorch.md) | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. | Tu objetivo encaja con estos ejemplos: Aprender tensores; Entrenar una red educativa | Sin clave propia de API de IA en la ruta básica |
| [LLaMA-Factory](../fichas/llama-factory.md) | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. | Tu objetivo encaja con estos ejemplos: Ajustar un modelo con ejemplos propios; Comparar un adaptador antes de exportarlo | Sin clave propia de API de IA en la ruta básica |
| [scikit-learn](../fichas/scikit-learn.md) | La biblioteca de machine learning clásico en Python: clasificación, regresión, clustering, reducción de dimensión, selección de modelos y preprocesado. | Tu objetivo encaja con estos ejemplos: entrenar y validar un clasificador sobre datos tabulares; construir un pipeline de preprocesado y modelo reproducible | Sin clave propia de API de IA en la ruta básica |
| [Keras 3](../fichas/keras.md) | API de deep learning multibackend: el mismo código de modelo se ejecuta sobre JAX, TensorFlow o PyTorch (y OpenVINO para inferencia). | Tu objetivo encaja con estos ejemplos: prototipar una red neuronal con una API sencilla; cambiar de backend sin reescribir el modelo para ganar rendimiento | Sin clave propia de API de IA en la ruta básica |
| [DeepSpeed](../fichas/deepspeed.md) | Biblioteca de optimización de entrenamiento e inferencia distribuidos de Microsoft: ZeRO, paralelismo y descarga a CPU/NVMe para modelos enormes. | Tu objetivo encaja con estos ejemplos: entrenar un modelo que no cabe en una GPU repartiendo estados con ZeRO-3; acelerar un ajuste fino distribuido con Transformers o Accelerate | Sin clave propia de API de IA en la ruta básica |
| [JAX](../fichas/jax.md) | Biblioteca de Google para cómputo numérico de alto rendimiento: NumPy diferenciable, compilación JIT con XLA y vectorización en CPU, GPU y TPU. | Tu objetivo encaja con estos ejemplos: entrenar modelos o simulaciones científicas en GPU o TPU; calcular derivadas de funciones numéricas complejas | Sin clave propia de API de IA en la ruta básica |
| [PyTorch Lightning](../fichas/pytorch-lightning.md) | Framework que estructura el entrenamiento en PyTorch y lo escala de una GPU a miles sin cambiar el código, con Lightning Fabric para control experto. | Tu objetivo encaja con estos ejemplos: organizar un proyecto de entrenamiento en PyTorch sin código repetitivo; pasar de una GPU a varias con DDP, FSDP o DeepSpeed | Sin clave propia de API de IA en la ruta básica |
| [verl](../fichas/verl.md) | Framework flexible y eficiente de post-entrenamiento por refuerzo para LLM (HybridFlow): PPO, GRPO y otros algoritmos con FSDP/Megatron y vLLM/SGLang. | Tu objetivo encaja con estos ejemplos: entrenar un modelo de razonamiento con GRPO sobre problemas verificables; investigar nuevos algoritmos de RL para LLM a escala | Sin clave propia de API de IA en la ruta básica |
| [PEFT](../fichas/peft.md) | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. | Tu objetivo encaja con estos ejemplos: Ajustar un modelo con menos parámetros; Reutilizar un adaptador entrenado | Sin clave propia de API de IA en la ruta básica |
| [TRL](../fichas/trl.md) | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. | Tu objetivo encaja con estos ejemplos: Aprender ajuste supervisado; Estudiar DPO o GRPO | Sin clave propia de API de IA en la ruta básica |
| [Axolotl](../fichas/axolotl.md) | Framework de post-entrenamiento de LLM por configuración YAML: ajuste completo, LoRA/QLoRA, DPO/GRPO, multimodal y entrenamiento distribuido. | Tu objetivo encaja con estos ejemplos: ajustar un modelo abierto con QLoRA a partir de un archivo YAML; entrenar con GRPO o DPO en varias GPU | Sin clave propia de API de IA en la ruta básica |
| [OpenRLHF](../fichas/openrlhf.md) | Framework de RLHF y RL agéntico escalable basado en Ray, vLLM y DeepSpeed: PPO, REINFORCE++, GRPO, RLOO y entrenamiento asíncrono. | Tu objetivo encaja con estos ejemplos: entrenar un modelo con PPO o GRPO a partir de un modelo de recompensa; experimentar con RL para agentes con varios turnos | Sin clave propia de API de IA en la ruta básica |
| [Accelerate](../fichas/accelerate.md) | Biblioteca de Hugging Face para ejecutar el mismo código de PyTorch en una GPU, varias, TPU o con DeepSpeed y FSDP, con precisión mixta, cambiando pocas líneas. | Tu objetivo encaja con estos ejemplos: convertir un bucle de entrenamiento de PyTorch a multi-GPU sin reescribirlo; lanzar un entrenamiento con DeepSpeed desde un archivo de configuración | Sin clave propia de API de IA en la ruta básica |
| [torchtune](../fichas/torchtune.md) | Biblioteca nativa de PyTorch para post-entrenamiento de LLM con recetas de ajuste completo, LoRA/QLoRA, DPO y destilación; ya sin mantenimiento activo. | Tu objetivo encaja con estos ejemplos: estudiar recetas limpias de ajuste fino en PyTorch puro; reproducir un ajuste LoRA con configuraciones existentes | Sin clave propia de API de IA en la ruta básica |
| [bionemo-recipes](../fichas/bionemo-recipes.md) | Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. | Tu objetivo encaja con estos ejemplos: Estudiar modelos de secuencias biológicas; Reproducir un entrenamiento de investigación | Sin clave propia de API de IA en la ruta básica |

## Modelos abiertos y fundacionales

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [TimesFM](../fichas/timesfm.md) | Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por versión. | Tu objetivo encaja con estos ejemplos: Estudiar demanda con series temporales; Comparar un baseline de pronóstico | API de IA opcional |
| [DeepSeek-V3](../fichas/deepseek-v3.md) | Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su API compatible con OpenAI o en servidores con varias GPU. | Tu objetivo encaja con estos ejemplos: Conectar un modelo abierto potente a un agente mediante la API de DeepSeek; Estudiar cómo se sirve un modelo MoE grande con vLLM o SGLang | API de IA opcional |
| [laya](../fichas/laya.md) | Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados. | Tu objetivo encaja con estos ejemplos: Clasificar consultas por intención; Elegir una opción estructurada | Sin clave propia de API de IA en la ruta básica |
| [cosmos](../fichas/cosmos.md) | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. | Tu objetivo encaja con estos ejemplos: Explorar datos sintéticos para robótica; Estudiar generación de escenas físicas | API de IA opcional |
| [Gemma (biblioteca JAX)](../fichas/gemma.md) | Biblioteca oficial de Google DeepMind para usar y ajustar los modelos de pesos abiertos Gemma en JAX: muestreo, multimodal, LoRA y ajuste fino. | Tu objetivo encaja con estos ejemplos: chatear con un modelo Gemma en Python con JAX; ajustar Gemma con LoRA en GPU o TPU | Sin clave propia de API de IA en la ruta básica |
| [Nemotron (NVIDIA)](../fichas/nemotron.md) | Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. | Tu objetivo encaja con estos ejemplos: Explorar modelos abiertos de NVIDIA; Preparar un pipeline guiado de adaptación | API de IA opcional |
| [Kimi K2.7 Code](../fichas/kimi-k2-7-code.md) | Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face. | Tu objetivo encaja con estos ejemplos: Comparar generación de código; Estudiar uso de herramientas con un modelo abierto | API de IA opcional |

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
