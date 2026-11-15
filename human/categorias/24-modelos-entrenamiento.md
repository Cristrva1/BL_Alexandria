[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Modelos abiertos y entrenamiento

Modelos, bibliotecas de entrenamiento y ajuste fino. Revisa la licencia de los pesos, la memoria necesaria y la opción de inferencia antes de descargar o entrenar.

15 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Unsloth](../fichas/unsloth.md) | Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI. | Sin API de IA en la ruta básica |
| [TimesFM](../fichas/timesfm.md) | Modelo fundacional de Google Research para pronosticar series de tiempo sin entrenamiento previo. | Sin API de IA en la ruta básica |

## Secciones

- [Entrenar y afinar modelos](#entrenar-y-afinar-modelos) — 9 repos
- [Modelos abiertos y fundacionales](#modelos-abiertos-y-fundacionales) — 6 repos

## Entrenar y afinar modelos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Unsloth](../fichas/unsloth.md) | Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI. | quieres afinar un LLM con pocos recursos | Sin API de IA en la ruta básica |
| [tensorflow](../fichas/tensorflow.md) | Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. | tu proyecto necesita el ecosistema TensorFlow para entrenamiento o despliegue | Sin API de IA en la ruta básica |
| [Transformers](../fichas/transformers.md) | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. | trabajas con modelos abiertos en Python | Sin API de IA en la ruta básica |
| [PyTorch](../fichas/pytorch.md) | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. | entrenas o investigas modelos | Sin API de IA en la ruta básica |
| [LLaMA-Factory](../fichas/llama-factory.md) | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. | quieres muchas técnicas de fine-tuning con UI | Sin API de IA en la ruta básica |
| [PEFT](../fichas/peft.md) | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. | afinas modelos con código propio | Sin API de IA en la ruta básica |
| [TRL](../fichas/trl.md) | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. | necesitas SFT o RL sobre modelos abiertos | Sin API de IA en la ruta básica |
| [warp](../fichas/warp.md) | Framework de NVIDIA que compila funciones de Python en kernels para simulación física y cálculo en CPU o GPU. | quieres escribir simulaciones o kernels de cálculo acelerado desde Python | Sin API de IA en la ruta básica |
| [bionemo-recipes](../fichas/bionemo-recipes.md) | Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. | trabajas en entrenamiento de modelos para datos biológicos | Sin API de IA en la ruta básica |

## Modelos abiertos y fundacionales

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [TimesFM](../fichas/timesfm.md) | Modelo fundacional de Google Research para pronosticar series de tiempo sin entrenamiento previo. | necesitas pronósticos rápidos sin entrenar modelos | Sin API de IA en la ruta básica |
| [laya](../fichas/laya.md) | Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados. | buscas esta función: Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados. | Sin API de IA en la ruta básica |
| [DeepSeek-Coder](../fichas/deepseek-coder.md) | Familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software. | quieres un modelo de código abierto y desplegable on-prem | Sin API de IA en la ruta básica |
| [cosmos](../fichas/cosmos.md) | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. | trabajas IA física/robótica y necesitas datos sintéticos | Sin API de IA en la ruta básica |
| [Nemotron (NVIDIA)](../fichas/nemotron.md) | Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. | usas GPUs NVIDIA y quieres modelos abiertos optimizados | Sin API de IA en la ruta básica |
| [Kimi K2.7 Code](../fichas/kimi-k2-7-code.md) | Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face. | puedes evaluar una API o administrar inferencia de un modelo grande | API de IA opcional |

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
