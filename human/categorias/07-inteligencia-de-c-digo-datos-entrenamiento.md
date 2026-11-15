[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Entender código, trabajar con datos y entrenar modelos

Herramientas para analizar código, procesar datos, aprender machine learning y entrenar modelos. Separa los ejemplos de aprendizaje de las librerías que integras.

47 repos · 7 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Repomix](../fichas/repomix.md) | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | Sin API de IA en la ruta básica |
| [Semgrep](../fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | Sin API de IA en la ruta básica |
| [Unsloth](../fichas/unsloth.md) | Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI. | Sin API de IA en la ruta básica |
| [LLM Course](../fichas/llm-course.md) | Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. | Sin API de IA en la ruta básica |
| [TimesFM](../fichas/timesfm.md) | Modelo fundacional de Google Research para pronosticar series de tiempo sin entrenamiento previo. | Sin API de IA en la ruta básica |
| [GitHub CLI](../fichas/cli.md) | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | Sin API de IA en la ruta básica |
| [DuckDB](../fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | Sin API de IA en la ruta básica |
| [marimo](../fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | Sin API de IA en la ruta básica |

## Secciones

- [Entender y empaquetar código para agentes](#entender-y-empaquetar-código-para-agentes) — 8 repos
- [Calidad, seguridad y benchmarks de código](#calidad-seguridad-y-benchmarks-de-código) — 5 repos
- [Entrenar y afinar modelos](#entrenar-y-afinar-modelos) — 9 repos
- [Aprender LLMs desde cero](#aprender-llms-desde-cero) — 10 repos
- [Modelos abiertos y fundacionales](#modelos-abiertos-y-fundacionales) — 5 repos
- [CLIs y SDKs de desarrollo](#clis-y-sdks-de-desarrollo) — 2 repos
- [Datos y notebooks](#datos-y-notebooks) — 8 repos

## Entender y empaquetar código para agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Repomix](../fichas/repomix.md) | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | quieres dar tu repo completo a un LLM | Sin API de IA en la ruta básica |
| [graphify](../fichas/graphify.md) | Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos. | quieres ver conexiones visualmente o auditar un sistema | API de IA opcional |
| [codegraph](../fichas/codegraph.md) | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. | trabajas repos grandes y el contexto del agente es caro | Sin API de IA en la ruta básica |
| [codebase-memory-mcp](../fichas/codebase-memory-mcp.md) | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. | tu agente trabaja en repos grandes | Sin API de IA en la ruta básica |
| [GitNexus](../fichas/gitnexus.md) | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. | quieres entender un repo puntual de forma visual | Sin API de IA en la ruta básica |
| [tree-sitter](../fichas/tree-sitter.md) | Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. | construyes herramientas que entienden código | Sin API de IA en la ruta básica |
| [DeepWiki Open](../fichas/deepwiki-open.md) | Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki. | quieres documentación automática de un repositorio | Depende de la ruta elegida |
| [floorplan](../fichas/floorplan.md) | Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto. | buscas esta función: Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto. | Sin API de IA en la ruta básica |

## Calidad, seguridad y benchmarks de código

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Semgrep](../fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | quieres análisis de seguridad en CI | Sin API de IA en la ruta básica |
| [ast-grep](../fichas/ast-grep.md) | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. | necesitas buscar o reescribir código por estructura | Sin API de IA en la ruta básica |
| [Defending Code Reference Harness](../fichas/defending-code-reference-harness.md) | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades. | quieres un flujo de seguridad con agentes probado | Sin API de IA en la ruta básica |
| [SWE-bench](../fichas/swe-bench.md) | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. | necesitas medir agentes de código con un estándar | Sin API de IA en la ruta básica |
| [dsh-qa](../fichas/dsh-qa.md) | Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles. | buscas esta función: Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles. | Sin API de IA en la ruta básica |

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

## Aprender LLMs desde cero

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [LLM Course](../fichas/llm-course.md) | Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. | quieres una ruta completa para aprender LLM | Sin API de IA en la ruta básica |
| [LLMs from Scratch](../fichas/llms-from-scratch.md) | Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. | quieres entender los LLM implementándolos | Sin API de IA en la ruta básica |
| [awesome-machine-learning](../fichas/awesome-machine-learning.md) | Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema. | buscas alternativas de aprendizaje automático en distintos lenguajes | Sin API de IA en la ruta básica |
| [nanoGPT](../fichas/nanogpt.md) | Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. | quieres entender el entrenamiento de un GPT desde cero | Sin API de IA en la ruta básica |
| [nanochat](../fichas/nanochat.md) | Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. | quieres el pipeline completo de un chat end-to-end | Sin API de IA en la ruta básica |
| [llm.c](../fichas/llm-c.md) | Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo. | quieres bajo nivel sin abstracciones y tienes GPU CUDA | Sin API de IA en la ruta básica |
| [train-llm-from-scratch](../fichas/train-llm-from-scratch.md) | Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación. | quieres entender el entrenamiento de un LLM mediante una implementación completa | Sin API de IA en la ruta básica |
| [python-machine-learning-book](../fichas/python-machine-learning-book.md) | Código de la primera edición del libro Python Machine Learning, con ejemplos de algoritmos y evaluación. | quieres estudiar los ejemplos de la primera edición del libro | Sin API de IA en la ruta básica |
| [MachineLearning](../fichas/machinelearning.md) | Ejemplos educativos de algoritmos de machine learning y redes neuronales con Python. | quieres explorar implementaciones pequeñas de algoritmos clásicos | Sin API de IA en la ruta básica |
| [how-to-train-your-gpt](../fichas/how-to-train-your-gpt.md) | Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción. | quieres una guía explicada y narrada | Sin API de IA en la ruta básica |

## Modelos abiertos y fundacionales

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [TimesFM](../fichas/timesfm.md) | Modelo fundacional de Google Research para pronosticar series de tiempo sin entrenamiento previo. | necesitas pronósticos rápidos sin entrenar modelos | Sin API de IA en la ruta básica |
| [laya](../fichas/laya.md) | Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados. | buscas esta función: Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados. | Sin API de IA en la ruta básica |
| [DeepSeek-Coder](../fichas/deepseek-coder.md) | Familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software. | quieres un modelo de código abierto y desplegable on-prem | Sin API de IA en la ruta básica |
| [cosmos](../fichas/cosmos.md) | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. | trabajas IA física/robótica y necesitas datos sintéticos | Sin API de IA en la ruta básica |
| [Nemotron (NVIDIA)](../fichas/nemotron.md) | Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. | usas GPUs NVIDIA y quieres modelos abiertos optimizados | Sin API de IA en la ruta básica |

## CLIs y SDKs de desarrollo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [GitHub CLI](../fichas/cli.md) | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | trabajas con GitHub desde la terminal o con agentes | Sin API de IA en la ruta básica |
| [openai-python](../fichas/openai-python.md) | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. | usas modelos de OpenAI desde Python y quieres el cliente oficial | API de IA necesaria |

## Datos y notebooks

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [DuckDB](../fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | quieres SQL analítico rápido sin montar servidores | Sin API de IA en la ruta básica |
| [marimo](../fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | quieres notebooks reproducibles y versionables | Sin API de IA en la ruta básica |
| [Polars](../fichas/polars.md) | Librería de DataFrames escrita en Rust, mucho más rápida que pandas. | tu análisis con pandas es lento | Sin API de IA en la ruta básica |
| [data-science-ipython-notebooks](../fichas/data-science-ipython-notebooks.md) | Gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep learning y big data, con ejemplos listos para ejecutar. | estudias/consultas DS con ejemplos ejecutables | Sin API de IA en la ruta básica |
| [awesome-bigdata](../fichas/awesome-bigdata.md) | Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala. | diseñas pipelines de datos grandes y necesitas descubrir el ecosistema | Sin API de IA en la ruta básica |
| [hudi](../fichas/hudi.md) | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. | necesitas gestionar cambios y cargas incrementales en un data lake | Depende de la ruta elegida |
| [GlobalBuildingAtlas](../fichas/globalbuildingatlas.md) | Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. | necesitas geometría de edificios para análisis territorial o visualización urbana | Sin API de IA en la ruta básica |
| [BigData](../fichas/bigdata.md) | Colección educativa de proyectos de datos con ejercicios de Hive, HDFS, Spark, HBase y sistemas de recomendación. | quieres estudiar ejemplos prácticos del ecosistema de big data | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md) — Que un agente de código entienda una base de código enorme sin gastar todo su contexto.
- [Analítica de producto con IA](../playbooks/analitica-con-ia.md) — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
