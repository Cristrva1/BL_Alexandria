# 24. Modelos abiertos y entrenamiento — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

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
**Combina con:** `diffusers`

## `deepseek-coder`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=inference,python

**Qué es:** Familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software.
**Stack:** Python; modelo y tokenizer; equipo según tamaño y cuantización
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Inferencia propia sin API obligatoria; hardware y licencia de pesos separados del código MIT
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es una familia de modelos y no el IDE DeepSeek ni una integración nativa con Claude Code, Codex o Antigravity
- Coste: Sin pago a un modelo en la ruta básica. Inferencia propia sin API obligatoria; hardware y licencia de pesos separados del código MIT
- Equipo: Preparación según la ruta elegida. Python; modelo y tokenizer; equipo según tamaño y cuantización
**Repo:** https://github.com/deepseek-ai/DeepSeek-Coder

**Instalación** [+]:

```
pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar generación de código local; Comparar variantes de un modelo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga una variante que quepa en tu equipo y pide completar una función de prueba
**Qué comprobar:** Puedes revisar la salida y probarla con entradas conocidas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `codegraph`

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
**Combina con:** `peft`, `transformers`
**Alternativas (elige una):** `unsloth`

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

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar modelos abiertos de NVIDIA; Preparar un pipeline guiado de adaptación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una receta y usa su guía para identificar datos, checkpoint y recursos antes de ejecutarla
**Qué comprobar:** Puedes diferenciar entrenamiento, adaptación e inferencia
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vllm`, `nemoclaw`

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
**Combina con:** `transformers`, `trl`

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

**Instalación** [?]:

```
Seguir la instalación original: https://pytorch.org/get-started/locally/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender tensores; Entrenar una red educativa
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa el selector oficial de instalación y realiza una operación pequeña con tensores
**Qué comprobar:** Puedes comprobar versión, dispositivo y resultado numérico
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`

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
**Combina con:** `polars`, `duckdb`

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
**Combina con:** `peft`, `trl`, `pytorch`

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
**Combina con:** `transformers`, `peft`, `unsloth`

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
**Combina con:** `ollama`, `trl`
**Alternativas (elige una):** `llama-factory`
