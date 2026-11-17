# 24. Modelos abiertos y entrenamiento — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `accelerate`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=training,python,pytorch

**Qué es:** Biblioteca de Hugging Face para ejecutar el mismo código de PyTorch en una GPU, varias, TPU o con DeepSpeed y FSDP, con precisión mixta, cambiando pocas líneas.
**Stack:** Python, pyproject.toml, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/huggingface/accelerate

**Instalación** [+]:

```
pip install accelerate
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: convertir un bucle de entrenamiento de PyTorch a multi-GPU sin reescribirlo; lanzar un entrenamiento con DeepSpeed desde un archivo de configuración
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install accelerate`, ejecuta `accelerate config` y lanza un script de ejemplo con `accelerate launch`.
**Qué comprobar:** El script se ejecuta con la configuración elegida.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `deepspeed`, `transformers`, `pytorch`

## `axolotl`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=training,python,llm,gpu

**Qué es:** Framework de post-entrenamiento de LLM por configuración YAML: ajuste completo, LoRA/QLoRA, DPO/GRPO, multimodal y entrenamiento distribuido.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/axolotl-ai-cloud/axolotl

**Instalación** [+]:

```
uv pip install axolotl[deepspeed]
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: ajustar un modelo abierto con QLoRA a partir de un archivo YAML; entrenar con GRPO o DPO en varias GPU
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Sigue la instalación con uv del README en una máquina con GPU y lanza uno de los ejemplos de configuración QLoRA pequeños.
**Qué comprobar:** El entrenamiento arranca y guarda el adaptador al final.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `deepspeed`, `peft`, `transformers`, `vllm`
**Alternativas (elige una):** `torchtune`, `llama-factory`, `unsloth`

## `bionemo-recipes`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,drug-discovery,gpu,machine-learning,pytorch,python

**Qué es:** Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala.
**Stack:** Conocimientos de biología computacional; Docker; GPU compatible con la receta; datos autorizados
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API para las recetas propias; GPUs, almacenamiento y datasets tienen condiciones independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No es un framework único listo para usar; algunas recetas requieren Hopper o Blackwell y sus resultados no son evidencia clínica
- Coste: El coste depende del proveedor o la ruta. No necesita API para las recetas propias; GPUs, almacenamiento y datasets tienen condiciones independientes
- Equipo: Preparación según la ruta elegida. Conocimientos de biología computacional; Docker; GPU compatible con la receta; datos autorizados
**Repo:** https://github.com/NVIDIA-BioNeMo/bionemo-recipes

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar modelos de secuencias biológicas; Reproducir un entrenamiento de investigación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa la receta ESM2 y calcula sus requisitos antes de ejecutar un ejemplo educativo pequeño
**Qué comprobar:** Puedes identificar modelo, datos y restricciones de hardware
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `pytorch`, `peft`

## `cosmos`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=inference

**Qué es:** Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots.
**Stack:** GPU compatible; entorno de la receta; acceso aprobado a pesos restringidos; token HF de lectura
**Acceso y costes:**
- API de IA: API de IA opcional. Demo y servicios alojados tienen condiciones propias; ejecución propia necesita GPU y licencias de modelos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Autenticarse en Hugging Face no concede por sí solo acceso al repositorio gated de Guardrail; las escenas generadas no prueban fidelidad física ni aptitud para controlar robots
- Coste: El coste depende del proveedor o la ruta. Demo y servicios alojados tienen condiciones propias; ejecución propia necesita GPU y licencias de modelos
- Equipo: Preparación según la ruta elegida. GPU compatible; entorno de la receta; acceso aprobado a pesos restringidos; token HF de lectura
**Repo:** https://github.com/NVIDIA/cosmos

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/NVIDIA/cosmos/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar datos sintéticos para robótica; Estudiar generación de escenas físicas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta una demo o ejecuta una receta pequeña y compara el video con su condicionamiento
**Qué comprobar:** Puedes reconocer entrada, modelo y salida generada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `diffusers`, `pytorch`, `nemotron`, `warp`

## `deepseek-v3`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=llm,inference,python

**Qué es:** Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su API compatible con OpenAI o en servidores con varias GPU.
**Stack:** API: cuenta en platform.deepseek.com; local: servidor con varias GPU y un motor como SGLang o vLLM
**Acceso y costes:**
- API de IA: API de IA opcional. API de pago compatible con OpenAI en platform.deepseek.com; la ruta local no usa API pero necesita infraestructura de varias GPU
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Pesos abiertos en Hugging Face; se sirven con SGLang, vLLM, LMDeploy o TensorRT-LLM en servidores con varias GPU
- Coste: El coste depende del proveedor o la ruta. La API se paga por uso; la ruta local evita ese pago pero exige hardware de centro de datos
- Equipo: GPU o infraestructura especializada. API: cuenta en platform.deepseek.com; local: servidor con varias GPU y un motor como SGLang o vLLM
**Repo:** https://github.com/deepseek-ai/DeepSeek-V3

**Instalación** [+]:

```
git clone https://github.com/deepseek-ai/DeepSeek-V3.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar un modelo abierto potente a un agente mediante la API de DeepSeek; Estudiar cómo se sirve un modelo MoE grande con vLLM o SGLang
**Evita si:** Quieres correr un modelo en un equipo doméstico; elige un modelo pequeño con Ollama y revisa los límites antes de elegirlo
**Primera prueba propuesta:** Envía una petición de prueba a la API de DeepSeek desde un cliente compatible con OpenAI y pide completar una función corta
**Qué comprobar:** Recibes la respuesta y ves en tu panel el consumo de esa llamada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `sglang`, `vllm`, `litellm`, `tensorrt-llm`

## `deepspeed`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=training,python,gpu,distributed

**Qué es:** Biblioteca de optimización de entrenamiento e inferencia distribuidos de Microsoft: ZeRO, paralelismo y descarga a CPU/NVMe para modelos enormes.
**Stack:** Python, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/deepspeedai/DeepSpeed

**Instalación** [+]:

```
pip install deepspeed
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: entrenar un modelo que no cabe en una GPU repartiendo estados con ZeRO-3; acelerar un ajuste fino distribuido con Transformers o Accelerate
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install deepspeed` en un entorno con PyTorch y GPU y ejecuta `ds_report` para comprobar la compatibilidad.
**Qué comprobar:** El informe muestra qué operaciones y extensiones están disponibles.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `accelerate`, `pytorch-lightning`, `axolotl`, `openrlhf`

## `gemma`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=model,python,jax,llm

**Qué es:** Biblioteca oficial de Google DeepMind para usar y ajustar los modelos de pesos abiertos Gemma en JAX: muestreo, multimodal, LoRA y ajuste fino.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/google-deepmind/gemma

**Instalación** [+]:

```
pip install gemma
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: chatear con un modelo Gemma en Python con JAX; ajustar Gemma con LoRA en GPU o TPU
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala JAX para tu hardware y después `pip install gemma`; ejecuta el ejemplo de muestreo con un checkpoint pequeño.
**Qué comprobar:** El modelo responde al prompt de ejemplo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `jax`, `jupyterlab`, `lm-eval-harness`

## `jax`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ml,python,library,numerical

**Qué es:** Biblioteca de Google para cómputo numérico de alto rendimiento: NumPy diferenciable, compilación JIT con XLA y vectorización en CPU, GPU y TPU.
**Stack:** Python, pyproject.toml, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/jax-ml/jax

**Instalación** [+]:

```
pip install -U jax
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: entrenar modelos o simulaciones científicas en GPU o TPU; calcular derivadas de funciones numéricas complejas
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install -U jax` y calcula el gradiente de una función simple con `jax.grad`.
**Qué comprobar:** Obtienes el valor del gradiente evaluado en el punto indicado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `keras`, `gemma`, `jupyterlab`, `mujoco`
**Alternativas (elige una):** `pytorch`, `tensorflow`

## `keras`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ml,python,library,deep-learning

**Qué es:** API de deep learning multibackend: el mismo código de modelo se ejecuta sobre JAX, TensorFlow o PyTorch (y OpenVINO para inferencia).
**Stack:** Python, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/keras-team/keras

**Instalación** [+]:

```
pip install keras --upgrade
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: prototipar una red neuronal con una API sencilla; cambiar de backend sin reescribir el modelo para ganar rendimiento
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install keras --upgrade` y un backend (por ejemplo JAX), y entrena el ejemplo MNIST de la documentación.
**Qué comprobar:** El modelo entrena y muestra la precisión por época.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `jax`, `pytorch`, `tensorflow`

## `kimi-k2-7-code`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=local · tags=kimi,moonshot,modelo,programacion,pesos-abiertos,huggingface

**Qué es:** Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face.
**Stack:** Servicio Moonshot o infraestructura de inferencia adecuada; licencia Modified MIT; proyecto de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. API por consumo o infraestructura propia considerable; pesos y código usan Modified MIT con condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es una ficha de pesos en Hugging Face, no un repositorio Git ni el CLI Kimi; mencionar Codex o Claude en benchmarks no prueba integración con esos planes
- Coste: El coste depende del proveedor o la ruta. API por consumo o infraestructura propia considerable; pesos y código usan Modified MIT con condiciones propias
- Equipo: Preparación según la ruta elegida. Servicio Moonshot o infraestructura de inferencia adecuada; licencia Modified MIT; proyecto de prueba
**Repo:** https://huggingface.co/moonshotai/Kimi-K2.7-Code

**Instalación** [?]:

```
Seguir la instalación original: https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar generación de código; Estudiar uso de herramientas con un modelo abierto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa la guía de despliegue o API y evalúa una función pequeña con tests conocidos
**Qué comprobar:** Puedes identificar modelo, proveedor y resultado comprobado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `sglang`, `opencode`

## `laya`
role=runtime · exec=local · setup=heavy · mcp=True · prov=local · tags=modelos,model,python

**Qué es:** Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados.
**Stack:** Python 3.10+; pesos del checkpoint para inferencia real; memoria del modelo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta propia no necesita API de pago; primera descarga de pesos requiere red y el modelo consume recursos
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Ofrece MCP stdio opcional; el ejemplo offline sin descarga es routing y no demuestra que se haya cargado un modelo; las probabilidades requieren evaluación propia
- Coste: Sin pago a un modelo en la ruta básica. La ruta propia no necesita API de pago; primera descarga de pesos requiere red y el modelo consume recursos
- Equipo: Preparación según la ruta elegida. Python 3.10+; pesos del checkpoint para inferencia real; memoria del modelo
**Repo:** https://github.com/NandhaKishorM/laya

**Instalación** [+]:

```
python -m pip install laya
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar consultas por intención; Elegir una opción estructurada
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba una decisión entre categorías de soporte y comprueba si usas routing offline o inferencia con pesos
**Qué comprobar:** Puedes distinguir una regla de enrutamiento de una predicción del modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `llama-index`, `crewai`

## `llama-factory`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=training,python

**Qué es:** Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código.
**Stack:** Python; modelo y dataset autorizados; GPU y memoria según configuración
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API de modelo remota; cómputo, almacenamiento y acceso a pesos son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La interfaz reduce programación pero no elimina requisitos de memoria, licencia o evaluación de datos; no todas las configuraciones caben en un portátil
- Coste: Sin pago a un modelo en la ruta básica. No exige API de modelo remota; cómputo, almacenamiento y acceso a pesos son independientes
- Equipo: Preparación según la ruta elegida. Python; modelo y dataset autorizados; GPU y memoria según configuración
**Repo:** https://github.com/hiyouga/LlamaFactory

**Instalación** [+]:

```
git clone --depth 1 https://github.com/hiyouga/LlamaFactory.git
cd LlamaFactory
pip install -e .
pip install -r requirements/metrics.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar un modelo con ejemplos propios; Comparar un adaptador antes de exportarlo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre la interfaz y revisa un dataset pequeño antes de lanzar un ajuste LoRA
**Qué comprobar:** Puedes identificar modelo base, datos y parámetros de entrenamiento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `peft`, `transformers`, `vllm`, `sglang`, `gradio`
**Alternativas (elige una):** `unsloth`, `axolotl`, `torchtune`

## `nemotron`
role=directory · exec=local · setup=heavy · mcp=False · prov=local · tags=training,inference

**Qué es:** Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos.
**Stack:** Navegador; modelo o receta elegida; GPU según tarea; Claude Code solo para plugin
**Acceso y costes:**
- API de IA: API de IA opcional. Consultar es gratuito; modelos locales requieren hardware y proveedores remotos tienen sus condiciones; plugin usa el plan del agente
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es un centro de recursos con modelos y recetas distintas; el plugin nemotron-customize es para Claude Code y no implica compatibilidad automática de toda receta
- Coste: El coste depende del proveedor o la ruta. Consultar es gratuito; modelos locales requieren hardware y proveedores remotos tienen sus condiciones; plugin usa el plan del agente
- Equipo: Preparación según la ruta elegida. Navegador; modelo o receta elegida; GPU según tarea; Claude Code solo para plugin
**Repo:** https://github.com/NVIDIA-NeMo/Nemotron

**Instalación** [+]:

```
/plugin marketplace add NVIDIA-NeMo/Nemotron
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar modelos abiertos de NVIDIA; Preparar un pipeline guiado de adaptación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una receta y usa su guía para identificar datos, checkpoint y recursos antes de ejecutarla
**Qué comprobar:** Puedes diferenciar entrenamiento, adaptación e inferencia
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `nemoclaw`, `claude-code`, `nemo`, `cosmos`

## `openrlhf`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=training,python,rl,gpu

**Qué es:** Framework de RLHF y RL agéntico escalable basado en Ray, vLLM y DeepSpeed: PPO, REINFORCE++, GRPO, RLOO y entrenamiento asíncrono.
**Stack:** Python, pyproject.toml, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/OpenRLHF/OpenRLHF

**Instalación** [+]:

```
pip install openrlhf
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: entrenar un modelo con PPO o GRPO a partir de un modelo de recompensa; experimentar con RL para agentes con varios turnos
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Sigue la guía rápida de OpenRLHF en un entorno con GPU y ejecuta un script de ejemplo de SFT o RM pequeño.
**Qué comprobar:** El entrenamiento arranca y guarda los checkpoints.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ray`, `vllm`, `deepspeed`
**Alternativas (elige una):** `verl`

## `peft`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA.
**Stack:** Python; modelo Transformers; dataset; hardware suficiente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de modelo alojado; entrenar y almacenar pesos requiere cómputo propio o alquilado
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo
- Coste: Sin pago a un modelo en la ruta básica. Sin API de modelo alojado; entrenar y almacenar pesos requiere cómputo propio o alquilado
- Equipo: Preparación según la ruta elegida. Python; modelo Transformers; dataset; hardware suficiente
**Repo:** https://github.com/huggingface/peft

**Instalación** [+]:

```
pip install peft
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar un modelo con menos parámetros; Reutilizar un adaptador entrenado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Estudia el ejemplo LoRA y comprueba qué parámetros serán entrenables
**Qué comprobar:** Puedes distinguir modelo base de adaptador
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `trl`, `diffusers`, `llama-factory`, `airllm`, `bionemo-recipes`

## `pytorch`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU.
**Stack:** Python compatible; paquete para CPU o tu GPU; entorno aislado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de IA para cómputo propio; hardware y nube se pagan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Para principiantes conviene instalar un binario compatible; los comandos de compilar todo el repositorio son para desarrollo del framework
- Coste: Sin pago a un modelo en la ruta básica. Sin API de IA para cómputo propio; hardware y nube se pagan aparte
- Equipo: Preparación según la ruta elegida. Python compatible; paquete para CPU o tu GPU; entorno aislado
**Repo:** https://github.com/pytorch/pytorch

**Instalación** [+]:

```
docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender tensores; Entrenar una red educativa
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa el selector oficial de instalación y realiza una operación pequeña con tensores
**Qué comprobar:** Puedes comprobar versión, dispositivo y resultado numérico
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `diffusers`, `vllm`
**Alternativas (elige una):** `tensorflow`, `jax`

## `pytorch-lightning`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=training,python,pytorch

**Qué es:** Framework que estructura el entrenamiento en PyTorch y lo escala de una GPU a miles sin cambiar el código, con Lightning Fabric para control experto.
**Stack:** Python, pyproject.toml, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Lightning-AI/pytorch-lightning

**Instalación** [+]:

```
pip install lightning
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: organizar un proyecto de entrenamiento en PyTorch sin código repetitivo; pasar de una GPU a varias con DDP, FSDP o DeepSpeed
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install lightning` y ejecuta el ejemplo de autoencoder del README.
**Qué comprobar:** El Trainer entrena y muestra métricas por época.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `deepspeed`, `mlflow`

## `scikit-learn`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ml,python,library,data

**Qué es:** La biblioteca de machine learning clásico en Python: clasificación, regresión, clustering, reducción de dimensión, selección de modelos y preprocesado.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/scikit-learn/scikit-learn

**Instalación** [+]:

```
pip install -U scikit-learn
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: entrenar y validar un clasificador sobre datos tabulares; construir un pipeline de preprocesado y modelo reproducible
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install -U scikit-learn` y entrena un clasificador sobre el conjunto iris incluido.
**Qué comprobar:** Obtienes la precisión del modelo en validación cruzada.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `jupyterlab`, `mlflow`, `ml-for-beginners`, `pandas`

## `tensorflow`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,deep-learning,deep-neural-networks,distributed,machine-learning,ml,neural-network,python

**Qué es:** Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos.
**Stack:** Python; paquete y sistema compatibles; datos de ejemplo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API obligatoria para ejecución propia; hardware y nube independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La instalación CPU y acelerada depende de plataforma y versión; usa el selector y guía oficiales en vez de asumir GPU en cualquier sistema
- Coste: Sin pago a un modelo en la ruta básica. Sin API obligatoria para ejecución propia; hardware y nube independientes
- Equipo: Preparación según la ruta elegida. Python; paquete y sistema compatibles; datos de ejemplo
**Repo:** https://github.com/tensorflow/tensorflow

**Instalación** [+]:

```
pip install tensorflow
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender redes neuronales; Construir un clasificador educativo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta una operación pequeña con tensores y comprueba el dispositivo antes de entrenar
**Qué comprobar:** Puedes verificar versión y resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `mediapipe`, `marimo`, `jupyterlab`, `tfjs-models`, `keras`
**Alternativas (elige una):** `pytorch`, `jax`

## `timesfm`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=data,analytics,python

**Qué es:** Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por versión.
**Stack:** Python; serie numérica ordenada; backend PyTorch o MLX; pesos permitidos
**Acceso y costes:**
- API de IA: API de IA opcional. Inferencia propia consume hardware; Cloud cobra por servicio; pesos 3.0 tienen restricciones no comerciales y no productivas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Código y pesos hasta 2.5 son Apache; pesos 3.0 autoalojados no permiten uso comercial o productivo, que sí se ofrece mediante servicios Google autorizados
- Coste: El coste depende del proveedor o la ruta. Inferencia propia consume hardware; Cloud cobra por servicio; pesos 3.0 tienen restricciones no comerciales y no productivas
- Equipo: Preparación según la ruta elegida. Python; serie numérica ordenada; backend PyTorch o MLX; pesos permitidos
**Repo:** https://github.com/google-research/timesfm

**Instalación** [+]:

```
# Install TimesFM with PyTorch
pip install timesfm[torch]
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar demanda con series temporales; Comparar un baseline de pronóstico
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pronostica un tramo reservado de una serie de ejemplo y compáralo con datos que no diste al modelo
**Qué comprobar:** Puedes medir error fuera de la muestra
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `polars`, `duckdb`, `pytorch`

## `torchtune`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=training,python,pytorch,llm

**Qué es:** Biblioteca nativa de PyTorch para post-entrenamiento de LLM con recetas de ajuste completo, LoRA/QLoRA, DPO y destilación; ya sin mantenimiento activo.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/meta-pytorch/torchtune

**Instalación** [+]:

```
pip install torchtune
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: estudiar recetas limpias de ajuste fino en PyTorch puro; reproducir un ajuste LoRA con configuraciones existentes
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install torchtune` (junto a torch, torchvision y torchao) y lista las recetas con `tune ls`.
**Qué comprobar:** La CLI muestra las recetas y configuraciones disponibles.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `lm-eval-harness`, `transformers`
**Alternativas (elige una):** `axolotl`, `llama-factory`, `unsloth`

## `transformers`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=training,inference,python

**Qué es:** Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación.
**Stack:** Python; PyTorch; pesos de un modelo; memoria suficiente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API para inferencia descargada; modelos restringidos pueden pedir acceso y cada peso tiene licencia
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es una biblioteca de modelos y no un agente de código ni una aplicación lista para todo hardware
- Coste: Sin pago a un modelo en la ruta básica. No necesita API para inferencia descargada; modelos restringidos pueden pedir acceso y cada peso tiene licencia
- Equipo: Preparación según la ruta elegida. Python; PyTorch; pesos de un modelo; memoria suficiente
**Repo:** https://github.com/huggingface/transformers

**Instalación** [+]:

```
# pip
pip install "transformers[torch]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar un texto localmente; Probar un modelo de visión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta un pipeline de clasificación con un texto breve y revisa sus etiquetas
**Qué comprobar:** Puedes identificar modelo descargado y salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `peft`, `trl`, `vllm`

## `trl`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más.
**Stack:** Python; Transformers; modelo y datos; GPU según método
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Entrenamiento propio sin API obligatoria; cómputo y posibles modelos de recompensa tienen costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. SFT, DPO y GRPO son métodos distintos; la disponibilidad de un trainer no garantiza una mejora sin evaluar el resultado
- Coste: Sin pago a un modelo en la ruta básica. Entrenamiento propio sin API obligatoria; cómputo y posibles modelos de recompensa tienen costes
- Equipo: Preparación según la ruta elegida. Python; Transformers; modelo y datos; GPU según método
**Repo:** https://github.com/huggingface/trl

**Instalación** [+]:

```
pip install trl
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender ajuste supervisado; Estudiar DPO o GRPO
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige el ejemplo SFT y revisa formato de datos antes de probar métodos de recompensa
**Qué comprobar:** Puedes relacionar datos, método y checkpoint
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `peft`, `unsloth`, `vllm`, `llm-course`, `train-llm-from-scratch`

## `unsloth`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=training,local,python

**Qué es:** App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales.
**Stack:** App para tu sistema; modelo que quepa en memoria; GPU según tarea
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta local no exige API de pago; hardware, modelos y conexiones Cloud o ChatGPT tienen costes o cuotas propios
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware
- Coste: El coste depende del proveedor o la ruta. La ruta local no exige API de pago; hardware, modelos y conexiones Cloud o ChatGPT tienen costes o cuotas propios
- Equipo: Preparación según la ruta elegida. App para tu sistema; modelo que quepa en memoria; GPU según tarea
**Repo:** https://github.com/unslothai/unsloth

**Instalación** [+]:

```
winget install --id UnslothAI.Unsloth -e
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar inferencia local; Preparar un ajuste fino pequeño
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un modelo pequeño compatible y prueba una pregunta conocida antes de iniciar fine-tuning
**Qué comprobar:** Puedes identificar modelo, formato y memoria utilizada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `trl`, `ollama`, `llama-cpp`, `claude-code`, `llm-course`, `sglang`
**Alternativas (elige una):** `llama-factory`, `axolotl`, `torchtune`

## `verl`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=training,python,rl,gpu

**Qué es:** Framework flexible y eficiente de post-entrenamiento por refuerzo para LLM (HybridFlow): PPO, GRPO y otros algoritmos con FSDP/Megatron y vLLM/SGLang.
**Stack:** Python, pyproject.toml, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/verl-project/verl

**Instalación** [+]:

```
git clone --recursive https://github.com/verl-project/verl.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: entrenar un modelo de razonamiento con GRPO sobre problemas verificables; investigar nuevos algoritmos de RL para LLM a escala
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Sigue la guía de inicio rápido de verl en un nodo con GPU y ejecuta el ejemplo PPO o GRPO pequeño con GSM8K.
**Qué comprobar:** El entrenamiento arranca y registra recompensas por paso.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `sglang`, `ray`, `transformers`
**Alternativas (elige una):** `openrlhf`
