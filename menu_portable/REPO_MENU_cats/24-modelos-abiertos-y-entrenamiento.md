# 24. Modelos abiertos y entrenamiento — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `bionemo-recipes`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,drug-discovery,gpu,machine-learning,pytorch,python

**Qué es:** Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. Presenta configuraciones de entrenamiento con TransformerEngine y frameworks distribuidos para modelos biológicos.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA-BioNeMo/bionemo-recipes

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** trabajas en entrenamiento de modelos para datos biológicos
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `cosmos`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=inference

**Qué es:** Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.
**Stack:** Python, GPU (NVIDIA/CUDA)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA/cosmos

**Instalación** [?]: `Seguir la instalación original: https://github.com/NVIDIA/cosmos/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas IA física/robótica y necesitas datos sintéticos
**Evita si:** haces tareas de texto/UI o no tienes GPU para servirlo
**Combina con:** `diffusers`

## `deepseek-coder`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=inference,python

**Qué es:** Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia infraestructura.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/deepseek-ai/DeepSeek-Coder

**Instalación** [?]: `Seguir la instalación original: https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un modelo de código abierto y desplegable on-prem
**Evita si:** prefieres APIs comerciales gestionadas o no tienes GPU para servirlo
**Combina con:** `litellm`, `codegraph`

## `kimi-k2-7-code`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=local · tags=kimi,moonshot,modelo,programacion,pesos-abiertos,huggingface

**Qué es:** Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face.
**Stack:** Pesos del modelo; vLLM, SGLang o KTransformers
**Acceso y costes:**
- API de IA: API de IA opcional. La ficha oficial ofrece una API de Moonshot y alternativas de inferencia con pesos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. Se documenta inferencia con vLLM, SGLang o KTransformers. Comprueba la variante y la guía antes de descargar.
- Coste: El coste depende del proveedor o la ruta. API e infraestructura tienen costes según la ruta; disponer de pesos no equivale a cómputo gratuito.
- Equipo: GPU o infraestructura especializada. Modelo de gran tamaño: requiere preparación y hardware especializado; no se recomienda descargarlo sin revisar la guía.
**Repo:** https://huggingface.co/moonshotai/Kimi-K2.7-Code

**Instalación** [?]: `Seguir la instalación original: https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** puedes evaluar una API o administrar inferencia de un modelo grande
**Evita si:** buscas un chat local sencillo para un portátil o acceso ya cubierto por tu plan de otro proveedor

## `laya`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=modelos,model,python

**Qué es:** Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados.
**Stack:** Python, Dockerfile, compose.yaml, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/NandhaKishorM/laya

**Instalación** [+]: `python -m pip install laya`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `llama-factory`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=training,python

**Qué es:** Soporta LoRA, QLoRA, ajuste completo, DPO y más desde una UI o CLI. Muy usado en investigación e industria.
**Stack:** Python, PyTorch, Gradio
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/hiyouga/LlamaFactory

**Instalación** [?]: `Seguir la instalación original: https://github.com/hiyouga/LlamaFactory/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres muchas técnicas de fine-tuning con UI
**Evita si:** buscas la opción más eficiente en memoria; mira `unsloth`
**Combina con:** `peft`, `transformers`
**Alternativas (elige una):** `unsloth`

## `nemotron`
role=directory · exec=local · setup=heavy · mcp=False · prov=local · tags=training,inference

**Qué es:** Reúne guías de entrenamiento, despliegue y casos de uso de los modelos Nemotron, pensados para IA agéntica eficiente.
**Stack:** Python, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA-NeMo/Nemotron

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** usas GPUs NVIDIA y quieres modelos abiertos optimizados
**Evita si:** buscas la forma más simple de correr modelos; mira `ollama`
**Combina con:** `vllm`, `nemoclaw`

## `peft`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Adapta modelos grandes entrenando solo una pequeña parte de los parámetros, ahorrando memoria y tiempo.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/peft

**Instalación** [+]: `pip install peft`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** afinas modelos con código propio
**Evita si:** prefieres una herramienta lista; mira `unsloth`
**Combina con:** `transformers`, `trl`

## `pytorch`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Base de la mayoría de investigación y modelos abiertos actuales.
**Stack:** Python, C++, CUDA
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/pytorch/pytorch

**Instalación** [?]: `Seguir la instalación original: https://github.com/pytorch/pytorch/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** entrenas o investigas modelos
**Evita si:** solo consumes APIs de LLM
**Combina con:** `transformers`

## `tensorflow`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,deep-learning,deep-neural-networks,distributed,machine-learning,ml,neural-network,python

**Qué es:** Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. Define operaciones y modelos y ofrece herramientas de entrenamiento e inferencia en distintos dispositivos.
**Stack:** C++
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/tensorflow/tensorflow

**Instalación** [+]: `pip install tensorflow`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu proyecto necesita el ecosistema TensorFlow para entrenamiento o despliegue
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `timesfm`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=data,analytics,python

**Qué es:** Predice ventas, demanda o tráfico a partir del histórico sin entrenar un modelo propio (zero-shot).
**Stack:** Python, PyTorch, JAX
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/google-research/timesfm

**Instalación** [?]: `Seguir la instalación original: https://github.com/google-research/timesfm/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas pronósticos rápidos sin entrenar modelos
**Evita si:** necesitas explicabilidad estadística clásica
**Combina con:** `polars`, `duckdb`

## `transformers`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=training,inference,python

**Qué es:** Da acceso a cientos de miles de modelos con una API común para inferencia y entrenamiento. Es la base del ecosistema de modelos abiertos.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/transformers

**Instalación** [?]: `Seguir la instalación original: https://github.com/huggingface/transformers/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas con modelos abiertos en Python
**Evita si:** solo quieres chatear con un modelo local; mira `ollama`
**Combina con:** `peft`, `trl`, `pytorch`

## `trl`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Ofrece entrenadores listos para ajuste supervisado y por preferencias, usados para alinear modelos.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/trl

**Instalación** [+]: `pip install trl`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas SFT o RL sobre modelos abiertos
**Evita si:** quieres algo sin código; mira `llama-factory`
**Combina con:** `transformers`, `peft`, `unsloth`

## `unsloth`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=training,local,python

**Qué es:** Afina modelos como Qwen, Llama o Gemma en una sola GPU y expórtalos a GGUF u Ollama. Ofrece notebooks gratuitos y una interfaz local.
**Stack:** Python, Triton, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/unslothai/unsloth

**Instalación** [?]: `Seguir la instalación original: https://github.com/unslothai/unsloth/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres afinar un LLM con pocos recursos
**Evita si:** necesitas muchas técnicas y una UI de entrenamiento; mira `llama-factory`
**Combina con:** `ollama`, `trl`
**Alternativas (elige una):** `llama-factory`

## `warp`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,cuda,differentiable-programming,gpu,gpu-acceleration,nvidia,nvidia-warp,python

**Qué es:** Framework de NVIDIA que compila funciones de Python en kernels para simulación física y cálculo en CPU o GPU. Compila funciones especializadas y aporta primitivas de geometría, física y diferenciación.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA/warp

**Instalación** [+]: `pip install warp-lang`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres escribir simulaciones o kernels de cálculo acelerado desde Python
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico
