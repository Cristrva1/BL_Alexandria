# Alexandría para agentes · Entrenar y afinar modelos

Categoría 24 «Modelos abiertos y entrenamiento» › subcategoría `entrenamiento`. 18 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=24&sub=entrenamiento · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `transformers` | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio… | 3 Avanzado | 86 | Apache-2.0 (OSI permisiva) | sin grupo |
| `unsloth` | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a… | 3 Avanzado | 82 | Apache-2.0 (OSI permisiva) | recomendado |
| `tensorflow` | Framework de aprendizaje automático para construir, entrenar y desplegar… | 3 Avanzado | 79 | Apache-2.0 (OSI permisiva) | recomendado |
| `pytorch` | Framework de deep learning con tensores y redes neuronales dinámicas acelerados… | 3 Avanzado | 78 | BSD-3-Clause (OSI permisiva) | alternativa |
| `keras` | API de deep learning multibackend: el mismo código de modelo se ejecuta sobre… | 3 Avanzado | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `scikit-learn` | La biblioteca de machine learning clásico en Python: clasificación, regresión… | 3 Avanzado | 74 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `trl` | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT… | 3 Avanzado | 72 | Apache-2.0 (OSI permisiva) | sin grupo |
| `deepspeed` | Biblioteca de optimización de entrenamiento e inferencia distribuidos de… | 4 Experto | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `peft` | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. | 3 Avanzado | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `verl` | Framework flexible y eficiente de post-entrenamiento por refuerzo para LLM… | 4 Experto | 68 | Apache-2.0 (OSI permisiva) | recomendado |
| `axolotl` | Framework de post-entrenamiento de LLM por configuración YAML: ajuste completo… | 3 Avanzado | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `jax` | Biblioteca de Google para cómputo numérico de alto rendimiento: NumPy… | 3 Avanzado | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `accelerate` | Biblioteca de Hugging Face para ejecutar el mismo código de PyTorch en una GPU… | 3 Avanzado | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `llama-factory` | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web… | 3 Avanzado | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `pytorch-lightning` | Framework que estructura el entrenamiento en PyTorch y lo escala de una GPU a… | 3 Avanzado | 60 | Apache-2.0 (OSI permisiva) | sin grupo |
| `openrlhf` | Framework de RLHF y RL agéntico escalable basado en Ray, vLLM y DeepSpeed: PPO… | 4 Experto | 58 | Apache-2.0 (OSI permisiva) | alternativa |
| `torchtune` | Biblioteca nativa de PyTorch para post-entrenamiento de LLM con recetas de… | 3 Avanzado | 52 | BSD-3-Clause (OSI permisiva) | alternativa |
| `bionemo-recipes` | Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales… | 1 Básico | 37 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Transformers (`transformers`)

- **Repo:** https://github.com/huggingface/transformers · Apache-2.0 · nivel 3 · 86/100
- **Qué es:** Transformers, la librería de definición de modelos de Hugging Face para texto, visión, audio, vídeo y multimodal. Licencia Apache-2.0. Es muy madura (~169k estrellas, v5.23.0).
- **Cuándo elegirlo:** Casos: Clasificar un texto localmente; Probar un modelo de visión.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, dominio especializado; Python; PyTorch; pesos de un modelo; memoria suficiente; hardware prerequisites; API de IA: no; Python; PyTorch; pesos de un modelo; memoria suficiente.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/huggingface/transformers/blob/main/README.md

  ```py
  # pip
  pip install "transformers[torch]"
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta un pipeline de clasificación con un texto breve y revisa sus etiquetas Éxito: Puedes identificar modelo descargado y salida
- **Combina con:** `pytorch`, `peft`, `trl`, `vllm` [23/serving]
- **Riesgos y avisos:** Sin alternativas declaradas. Es una biblioteca de modelos y no un agente de código ni una aplicación lista para todo hardware.

### Unsloth (`unsloth`)

- **Repo:** https://github.com/unslothai/unsloth · Apache-2.0 · nivel 3 · 82/100 · recomendado en «Fine-tuning de LLM»
- **Qué es:** Unsloth, app de escritorio y librería para ejecutar y entrenar modelos en local, de unslothai. Tiene licencia dual: el núcleo es Apache-2.0 y componentes opcionales como la UI de Unsloth Studio son AGPL-3.0.
- **Cuándo elegirlo:** Casos: Probar inferencia local; Preparar un ajuste fino pequeño.
- **Requisitos:** nivel 3: preparación media, dominio especializado; App para tu sistema; modelo que quepa en memoria; GPU según tarea; hardware prerequisites; API de IA: opcional; App para tu sistema; modelo que quepa en memoria; GPU según tarea.
- **Instalación (documentada en la fuente; no ejecutada):** `winget install --id UnslothAI.Unsloth -e` — fuente: https://github.com/unslothai/unsloth/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Carga un modelo pequeño compatible y prueba una pregunta conocida antes de iniciar fine-tuning Éxito: Puedes identificar modelo, formato y memoria utilizada
- **Combina con:** `trl`, `ollama` [8/motores], `llama-cpp` [8/motores], `claude-code` [20/terminal], `llm-course` [19/aprender], `sglang` [23/serving]
- **Alternativas:** `axolotl`, `llama-factory`, `torchtune`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): llama-factory. La AGPL de Studio importa si redistribuyes la UI. Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware.

### tensorflow (`tensorflow`)

- **Repo:** https://github.com/tensorflow/tensorflow · Apache-2.0 · nivel 3 · 79/100 · recomendado en «Frameworks de deep learning»
- **Qué es:** TensorFlow, plataforma open source de aprendizaje automático creada en Google Brain. Licencia Apache-2.0. Es muy madura (~202k estrellas, v2.21.0).
- **Cuándo elegirlo:** Casos: Aprender redes neuronales; Construir un clasificador educativo.
- **Requisitos:** nivel 3: pip install; usarlo exige conocimientos de ML; Python; paquete y sistema compatibles; datos de ejemplo; hardware prerequisites; API de IA: no; Python; paquete y sistema compatibles; datos de ejemplo.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install tensorflow` — fuente: https://github.com/tensorflow/tensorflow/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una operación pequeña con tensores y comprueba el dispositivo antes de entrenar Éxito: Puedes verificar versión y resultado
- **Combina con:** `transformers`, `mediapipe` [28/vision], `marimo` [25/datos], `jupyterlab` [25/datos], `tfjs-models` [28/vision], `keras`
- **Alternativas:** `pytorch`, `jax`
- **Riesgos y avisos:** Alternativa (elige una): pytorch. La instalación CPU y acelerada depende de plataforma y versión; usa el selector y guía oficiales en vez de asumir GPU en cualquier sistema.

### PyTorch (`pytorch`)

- **Repo:** https://github.com/pytorch/pytorch · BSD-3-Clause · nivel 3 · 78/100 · alternativa en «Frameworks de deep learning»
- **Qué es:** PyTorch, framework de deep learning con tensores acelerados por GPU y autograd dinámico, gobernado por la PyTorch Foundation (Linux Foundation). Licencia de estilo BSD (GitHub muestra NOASSERTION). Es muy madura (~106k estrellas, v2.15.0).
- **Cuándo elegirlo:** Casos: Aprender tensores; Entrenar una red educativa.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, necesita GPU, dominio especializado; Python compatible; paquete para CPU o tu GPU; entorno aislado; hardware prerequisites; API de IA: no; Python compatible; paquete para CPU o tu GPU; entorno aislado.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest` — fuente: https://github.com/pytorch/pytorch/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Usa el selector oficial de instalación y realiza una operación pequeña con tensores Éxito: Puedes comprobar versión, dispositivo y resultado numérico
- **Combina con:** `transformers`, `diffusers` [11/modelos], `vllm` [23/serving]
- **Alternativas:** `tensorflow`, `jax`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): tensorflow. Para principiantes conviene instalar un binario compatible; los comandos de compilar todo el repositorio son para desarrollo del framework.

### Keras 3 (`keras`)

- **Repo:** https://github.com/keras-team/keras · Apache-2.0 · nivel 3 · 74/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) creada por François Chollet y mantenida por Google. Muy madura; Keras 3 la convirtió en multibackend.
- **Cuándo elegirlo:** Casos: prototipar una red neuronal con una API sencilla; cambiar de backend sin reescribir el modelo para ganar rendimiento.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, dominio especializado; Python, pyproject.toml, requirements.txt; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install keras --upgrade` — fuente: https://github.com/keras-team/keras/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install keras --upgrade` y un backend (por ejemplo JAX), y entrena el ejemplo MNIST de la documentación. Éxito: El modelo entrena y muestra la precisión por época.
- **Combina con:** `jax`, `pytorch`, `tensorflow`
- **Riesgos y avisos:** Algunas funciones dependen del backend; revisa la compatibilidad antes de cambiarlo.

### scikit-learn (`scikit-learn`)

- **Repo:** https://github.com/scikit-learn/scikit-learn · BSD-3-Clause · nivel 3 · 74/100
- **Qué es:** Biblioteca de código abierto (BSD-3-Clause) desarrollada por una comunidad internacional desde 2007, con apoyo de Inria y patrocinadores. Imprescindible y muy madura.
- **Cuándo elegirlo:** Casos: entrenar y validar un clasificador sobre datos tabulares; construir un pipeline de preprocesado y modelo reproducible.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, dominio especializado; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U scikit-learn` — fuente: https://github.com/scikit-learn/scikit-learn/blob/main/README.rst
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install -U scikit-learn` y entrena un clasificador sobre el conjunto iris incluido. Éxito: Obtienes la precisión del modelo en validación cruzada.
- **Combina con:** `jupyterlab` [25/datos], `mlflow` [23/observabilidad], `ml-for-beginners` [19/aprender], `pandas` [25/datos]
- **Riesgos y avisos:** No está pensado para deep learning ni GPU; para eso usa pytorch o jax.

### TRL (`trl`)

- **Repo:** https://github.com/huggingface/trl · Apache-2.0 · nivel 3 · 72/100
- **Qué es:** TRL, librería de Hugging Face para post-entrenar modelos fundacionales (SFT, GRPO, DPO, reward modeling…). Licencia Apache-2.0. Es madura y muy activa (~20k estrellas, v1.18.0).
- **Cuándo elegirlo:** Casos: Aprender ajuste supervisado; Estudiar DPO o GRPO.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, dominio especializado; Python; Transformers; modelo y datos; GPU según método; hardware prerequisites; API de IA: no; Python; Transformers; modelo y datos; GPU según método.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install trl` — fuente: https://github.com/huggingface/trl/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige el ejemplo SFT y revisa formato de datos antes de probar métodos de recompensa Éxito: Puedes relacionar datos, método y checkpoint
- **Combina con:** `transformers`, `peft`, `unsloth`, `vllm` [23/serving], `llm-course` [19/aprender], `train-llm-from-scratch` [19/aprender]
- **Riesgos y avisos:** Sin alternativas declaradas. SFT, DPO y GRPO son métodos distintos; la disponibilidad de un trainer no garantiza una mejora sin evaluar el resultado.

### DeepSpeed (`deepspeed`)

- **Repo:** https://github.com/deepspeedai/DeepSpeed · Apache-2.0 · nivel 4 · 68/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) creada por Microsoft y ahora bajo la organización deepspeedai, alojada en la LF AI & Data Foundation. Muy madura.
- **Cuándo elegirlo:** Casos: entrenar un modelo que no cabe en una GPU repartiendo estados con ZeRO-3; acelerar un ajuste fino distribuido con Transformers o Accelerate.
- **Requisitos:** nivel 4: preparación pesada, requiere programar con él, dominio especializado; Python, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install deepspeed` — fuente: https://github.com/deepspeedai/DeepSpeed/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install deepspeed` en un entorno con PyTorch y GPU y ejecuta `ds_report` para comprobar la compatibilidad. Éxito: El informe muestra qué operaciones y extensiones están disponibles.
- **Combina con:** `transformers`, `accelerate`, `pytorch-lightning`, `axolotl`, `openrlhf`
- **Riesgos y avisos:** Las extensiones CUDA requieren versiones compatibles de compilador, CUDA y PyTorch.

### PEFT (`peft`)

- **Repo:** https://github.com/huggingface/peft · Apache-2.0 · nivel 3 · 68/100
- **Qué es:** PEFT, librería de Hugging Face para fine-tuning eficiente en parámetros (LoRA y similares). Licencia Apache-2.0. Es madura (~22k estrellas, v0.21.3).
- **Cuándo elegirlo:** Casos: Ajustar un modelo con menos parámetros; Reutilizar un adaptador entrenado.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, dominio especializado; Python; modelo Transformers; dataset; hardware suficiente; hardware prerequisites; API de IA: no; Python; modelo Transformers; dataset; hardware suficiente.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install peft` — fuente: https://github.com/huggingface/peft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Estudia el ejemplo LoRA y comprueba qué parámetros serán entrenables Éxito: Puedes distinguir modelo base de adaptador
- **Combina con:** `transformers`, `trl`, `diffusers` [11/modelos], `llama-factory`, `airllm` [8/motores], `bionemo-recipes`
- **Riesgos y avisos:** Sin alternativas declaradas. Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo.

### verl (`verl`)

- **Repo:** https://github.com/verl-project/verl · Apache-2.0 · nivel 4 · 68/100 · recomendado en «Aprendizaje por refuerzo para LLM»
- **Qué es:** Framework de código abierto (Apache-2.0) iniciado por ByteDance Seed y mantenido ahora por la comunidad verl-project; implementa el artículo HybridFlow. Muy activo.
- **Cuándo elegirlo:** Casos: entrenar un modelo de razonamiento con GRPO sobre problemas verificables; investigar nuevos algoritmos de RL para LLM a escala.
- **Requisitos:** nivel 4: preparación pesada, requiere programar con él, necesita GPU, dominio especializado; Python, pyproject.toml, requirements.txt, setup.py; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --recursive https://github.com/verl-project/verl.git` — fuente: https://github.com/verl-project/verl/blob/main/docs/ascend_tutorial/en/get_start/install_guidance.rst
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de inicio rápido de verl en un nodo con GPU y ejecuta el ejemplo PPO o GRPO pequeño con GSM8K. Éxito: El entrenamiento arranca y registra recompensas por paso.
- **Combina con:** `vllm` [23/serving], `sglang` [23/serving], `ray` [23/serving], `transformers`
- **Alternativas:** `openrlhf`
- **Riesgos y avisos:** Alternativas (elige una): openrlhf. La rama principal cambia rápido; fija versiones.

### Axolotl (`axolotl`)

- **Repo:** https://github.com/axolotl-ai-cloud/axolotl · Apache-2.0 · nivel 3 · 65/100 · alternativa en «Fine-tuning de LLM»
- **Qué es:** Framework de código abierto (Apache-2.0) de Axolotl AI. Muy activo y usado por la comunidad de ajuste fino.
- **Cuándo elegirlo:** Casos: ajustar un modelo abierto con QLoRA a partir de un archivo YAML; entrenar con GRPO o DPO en varias GPU.
- **Requisitos:** nivel 3: fine-tuning por YAML; necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `uv pip install axolotl[deepspeed]` — fuente: https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la instalación con uv del README en una máquina con GPU y lanza uno de los ejemplos de configuración QLoRA pequeños. Éxito: El entrenamiento arranca y guarda el adaptador al final.
- **Combina con:** `deepspeed`, `peft`, `transformers`, `vllm` [23/serving]
- **Alternativas:** `unsloth`, `llama-factory`, `torchtune`
- **Riesgos y avisos:** Alternativas (elige una): llama-factory, unsloth, torchtune.

### JAX (`jax`)

- **Repo:** https://github.com/jax-ml/jax · Apache-2.0 · nivel 3 · 65/100 · alternativa en «Frameworks de deep learning»
- **Qué es:** Biblioteca de código abierto (Apache-2.0) de Google. Muy madura y base de gran parte de la investigación de Google DeepMind.
- **Cuándo elegirlo:** Casos: entrenar modelos o simulaciones científicas en GPU o TPU; calcular derivadas de funciones numéricas complejas.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, dominio especializado; Python, pyproject.toml, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U jax` — fuente: https://github.com/jax-ml/jax/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install -U jax` y calcula el gradiente de una función simple con `jax.grad`. Éxito: Obtienes el valor del gradiente evaluado en el punto indicado.
- **Combina con:** `keras`, `gemma` [24/modelos], `jupyterlab` [25/datos], `mujoco` [26/simulacion]
- **Alternativas:** `tensorflow`, `pytorch`
- **Riesgos y avisos:** Alternativas (elige una): pytorch, tensorflow.

### Accelerate (`accelerate`)

- **Repo:** https://github.com/huggingface/accelerate · Apache-2.0 · nivel 3 · 64/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) de Hugging Face. Muy madura; base del Trainer de Transformers.
- **Cuándo elegirlo:** Casos: convertir un bucle de entrenamiento de PyTorch a multi-GPU sin reescribirlo; lanzar un entrenamiento con DeepSpeed desde un archivo de configuración.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, dominio especializado; Python, pyproject.toml, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install accelerate` — fuente: https://github.com/huggingface/accelerate/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install accelerate`, ejecuta `accelerate config` y lanza un script de ejemplo con `accelerate launch`. Éxito: El script se ejecuta con la configuración elegida.
- **Combina con:** `deepspeed`, `transformers`, `pytorch`
- **Riesgos y avisos:** Para estructurar proyectos grandes, pytorch-lightning aporta más organización.

### LLaMA-Factory (`llama-factory`)

- **Repo:** https://github.com/hiyouga/LlamaFactory · Apache-2.0 · nivel 3 · 60/100 · alternativa en «Fine-tuning de LLM»
- **Qué es:** LlamaFactory, framework para fine-tuning unificado de más de 100 LLM y modelos de visión con CLI e interfaz web sin código, de @hiyouga. Licencia Apache-2.0.
- **Cuándo elegirlo:** Casos: Ajustar un modelo con ejemplos propios; Comparar un adaptador antes de exportarlo.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python; modelo y dataset autorizados; GPU y memoria según configuración; hardware prerequisites; API de IA: no; Python; modelo y dataset autorizados; GPU y memoria según configuración.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/hiyouga/LlamaFactory/blob/main/README.md

  ```bash
  git clone --depth 1 https://github.com/hiyouga/LlamaFactory.git
  cd LlamaFactory
  pip install -e .
  pip install -r requirements/metrics.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Abre la interfaz y revisa un dataset pequeño antes de lanzar un ajuste LoRA Éxito: Puedes identificar modelo base, datos y parámetros de entrenamiento
- **Combina con:** `peft`, `transformers`, `vllm` [23/serving], `sglang` [23/serving], `gradio` [25/apps]
- **Alternativas:** `unsloth`, `axolotl`, `torchtune`
- **Riesgos y avisos:** Alternativas (elige una): unsloth. La interfaz reduce programación pero no elimina requisitos de memoria, licencia o evaluación de datos; no todas las configuraciones caben en un portátil.

### PyTorch Lightning (`pytorch-lightning`)

- **Repo:** https://github.com/Lightning-AI/pytorch-lightning · Apache-2.0 · nivel 3 · 60/100
- **Qué es:** Framework de código abierto (Apache-2.0) de Lightning AI, empresa que ofrece una plataforma en la nube. Muy maduro.
- **Cuándo elegirlo:** Casos: organizar un proyecto de entrenamiento en PyTorch sin código repetitivo; pasar de una GPU a varias con DDP, FSDP o DeepSpeed.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, dominio especializado; Python, pyproject.toml, requirements.txt, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install lightning` — fuente: https://github.com/Lightning-AI/pytorch-lightning/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install lightning` y ejecuta el ejemplo de autoencoder del README. Éxito: El Trainer entrena y muestra métricas por época.
- **Combina con:** `pytorch`, `deepspeed`, `mlflow` [23/observabilidad]
- **Riesgos y avisos:** Añade una capa de abstracción; para scripts sencillos puede bastar accelerate.

### OpenRLHF (`openrlhf`)

- **Repo:** https://github.com/OpenRLHF/OpenRLHF · Apache-2.0 · nivel 4 · 58/100 · alternativa en «Aprendizaje por refuerzo para LLM»
- **Qué es:** Framework de código abierto (Apache-2.0) de la comunidad OpenRLHF. Activo; el README recomienda también Molt (NVIDIA NeMo) como alternativa ligera.
- **Cuándo elegirlo:** Casos: entrenar un modelo con PPO o GRPO a partir de un modelo de recompensa; experimentar con RL para agentes con varios turnos.
- **Requisitos:** nivel 4: preparación pesada, requiere programar con él, necesita GPU, dominio especializado; Python, pyproject.toml, requirements.txt, setup.py; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install openrlhf` — fuente: https://github.com/OpenRLHF/OpenRLHF/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía rápida de OpenRLHF en un entorno con GPU y ejecuta un script de ejemplo de SFT o RM pequeño. Éxito: El entrenamiento arranca y guarda los checkpoints.
- **Combina con:** `ray` [23/serving], `vllm` [23/serving], `deepspeed`
- **Alternativas:** `verl`
- **Riesgos y avisos:** Alternativas (elige una): verl.

### torchtune (`torchtune`)

- **Repo:** https://github.com/meta-pytorch/torchtune · BSD-3-Clause · nivel 3 · 52/100 · alternativa en «Fine-tuning de LLM»
- **Qué es:** Biblioteca de código abierto (BSD-3-Clause) de Meta/PyTorch. Su README avisa de que ya no se mantiene activamente: el desarrollo terminó en 2025. Sigue siendo una referencia útil de recetas en PyTorch puro.
- **Cuándo elegirlo:** Casos: estudiar recetas limpias de ajuste fino en PyTorch puro; reproducir un ajuste LoRA con configuraciones existentes.
- **Requisitos:** nivel 3: recetas de fine-tuning; necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install torchtune` — fuente: https://github.com/meta-pytorch/torchtune/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install torchtune` (junto a torch, torchvision y torchao) y lista las recetas con `tune ls`. Éxito: La CLI muestra las recetas y configuraciones disponibles.
- **Combina con:** `pytorch`, `lm-eval-harness` [23/observabilidad], `transformers`
- **Alternativas:** `unsloth`, `axolotl`, `llama-factory`
- **Riesgos y avisos:** Alternativas (elige una): axolotl, llama-factory, unsloth, todas con mantenimiento activo.

### bionemo-recipes (`bionemo-recipes`)

- **Repo:** https://github.com/NVIDIA-BioNeMo/bionemo-recipes · — · nivel 1 · 37/100
- **Qué es:** BioNeMo Recipes, recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. Licencia Apache-2.0 en LICENSE/license.txt (GitHub no la detecta por la ubicación). Es de nicho (~880 estrellas, v3.0.0).
- **Cuándo elegirlo:** Casos: Estudiar modelos de secuencias biológicas; Reproducir un entrenamiento de investigación.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Conocimientos de biología computacional; Docker; GPU compatible con la receta; datos autorizados; hardware prerequisites; API de IA: no; Conocimientos de biología computacional; Docker; GPU compatible con la receta; datos autorizados.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/NVIDIA-BioNeMo/bionemo-recipes/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Revisa la receta ESM2 y calcula sus requisitos antes de ejecutar un ejemplo educativo pequeño Éxito: Puedes identificar modelo, datos y restricciones de hardware
- **Combina con:** `transformers`, `pytorch`, `peft`
- **Riesgos y avisos:** Sin alternativas declaradas. No es un framework único listo para usar; algunas recetas requieren Hopper o Blackwell y sus resultados no son evidencia clínica.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-24-entrenamiento.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Entrenar y afinar modelos», lee `docs/alexandria/categoria-24-entrenamiento.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-24-entrenamiento.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
