[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 6. Memoria, RAG & LLM Ops](06-memoria-rag-llm-ops.md) · [8. IA Local: Modelos, Chats & Workspaces ➡️](08-ia-local-modelos-chats-workspaces.md)

# 🧑‍💻 7. Inteligencia de Código, Datos & Entrenamiento

> Entender y empaquetar codebases para agentes, calidad de código, entrenar y afinar modelos, modelos abiertos y herramientas de datos.

**44 repos** · 7 subcategorías · ⭐ 1.9M estrellas en total · 🆕 44 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [Repomix](../fichas/repomix.md) | 29.3k | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | `npx repomix` |
| [Semgrep](../fichas/semgrep.md) | 17.7k | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | `pip install semgrep` |
| [Unsloth](../fichas/unsloth.md) | 79.5k | Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI. | `pip install unsloth` |
| [LLM Course](../fichas/llm-course.md) | 85.1k | Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. | No se instala: abre el repo y sigue la ruta que te interese. |
| [TimesFM](../fichas/timesfm.md) | 35.5k | Modelo fundacional de Google Research para pronosticar series de tiempo sin entrenamiento previo. | `pip install timesfm` |
| [GitHub CLI](../fichas/cli.md) | 47k | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | `brew install gh` |
| [DuckDB](../fichas/duckdb.md) | 43.1k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | `pip install duckdb` |
| [marimo](../fichas/marimo.md) | 23.6k | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | `pip install marimo` |

## 🧭 Subcategorías

- [Entender y empaquetar código para agentes](#entender-y-empaquetar-código-para-agentes) — 7 repos
- [Calidad, seguridad y benchmarks de código](#calidad-seguridad-y-benchmarks-de-código) — 4 repos
- [Entrenar y afinar modelos](#entrenar-y-afinar-modelos) — 9 repos
- [Aprender LLMs desde cero](#aprender-llms-desde-cero) — 10 repos
- [Modelos abiertos y fundacionales](#modelos-abiertos-y-fundacionales) — 4 repos
- [CLIs y SDKs de desarrollo](#clis-y-sdks-de-desarrollo) — 2 repos
- [Datos y notebooks](#datos-y-notebooks) — 8 repos

## Entender y empaquetar código para agentes

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Repomix](../fichas/repomix.md) 🆕 | 29.3k | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | quieres dar tu repo completo a un LLM | 🟢 |
| [graphify](../fichas/graphify.md) 🆕 | 148k | Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos. | quieres ver conexiones visualmente o auditar un sistema | 🟡 |
| [codegraph](../fichas/codegraph.md) 🆕 | 77.6k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. | trabajas repos grandes y el contexto del agente es caro | 🟢 |
| [codebase-memory-mcp](../fichas/codebase-memory-mcp.md) 🆕 | 48.6k | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. | tu agente trabaja en repos grandes | 🟢 |
| [GitNexus](../fichas/gitnexus.md) 🆕 | 48.5k | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. | quieres entender un repo puntual de forma visual | 🟢 |
| [tree-sitter](../fichas/tree-sitter.md) 🆕 | 27.5k | Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. | construyes herramientas que entienden código | 🟡 |
| [DeepWiki Open](../fichas/deepwiki-open.md) 🆕 | 18.4k | Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki. | quieres documentación automática de un repositorio | 🟡 |

## Calidad, seguridad y benchmarks de código

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Semgrep](../fichas/semgrep.md) 🆕 | 17.7k | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | quieres análisis de seguridad en CI | 🟢 |
| [ast-grep](../fichas/ast-grep.md) 🆕 | 16.6k | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. | necesitas buscar o reescribir código por estructura | 🟢 |
| [Defending Code Reference Harness](../fichas/defending-code-reference-harness.md) 🆕 | 7.8k | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades. | quieres un flujo de seguridad con agentes probado | 🟡 |
| [SWE-bench](../fichas/swe-bench.md) 🆕 | 6.2k | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. | necesitas medir agentes de código con un estándar | 🔴 |

## Entrenar y afinar modelos

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Unsloth](../fichas/unsloth.md) 🆕 | 79.5k | Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI. | quieres afinar un LLM con pocos recursos | 🟡 |
| [tensorflow](../fichas/tensorflow.md) 🆕 | 202k | Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. | tu proyecto necesita el ecosistema TensorFlow para entrenamiento o despliegue | 🔴 |
| [Transformers](../fichas/transformers.md) 🆕 | 169k | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. | trabajas con modelos abiertos en Python | 🟢 |
| [PyTorch](../fichas/pytorch.md) 🆕 | 106k | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. | entrenas o investigas modelos | 🟡 |
| [LLaMA-Factory](../fichas/llama-factory.md) 🆕 | 76k | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. | quieres muchas técnicas de fine-tuning con UI | 🟡 |
| [PEFT](../fichas/peft.md) 🆕 | 21.9k | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. | afinas modelos con código propio | 🟡 |
| [TRL](../fichas/trl.md) 🆕 | 19.7k | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. | necesitas SFT o RL sobre modelos abiertos | 🟡 |
| [warp](../fichas/warp.md) 🆕 | 7.3k | Framework de NVIDIA que compila funciones de Python en kernels para simulación física y cálculo en CPU o GPU. | quieres escribir simulaciones o kernels de cálculo acelerado desde Python | 🔴 |
| [bionemo-recipes](../fichas/bionemo-recipes.md) 🆕 | 877 | Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. | trabajas en entrenamiento de modelos para datos biológicos | 🔴 |

## Aprender LLMs desde cero

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [LLM Course](../fichas/llm-course.md) 🆕 | 85.1k | Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. | quieres una ruta completa para aprender LLM | 🟢 |
| [LLMs from Scratch](../fichas/llms-from-scratch.md) 🆕 | 108k | Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. | quieres entender los LLM implementándolos | 🟡 |
| [awesome-machine-learning](../fichas/awesome-machine-learning.md) 🆕 | 74.8k | Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema. | buscas alternativas de aprendizaje automático en distintos lenguajes | 🟢 |
| [nanoGPT](../fichas/nanogpt.md) 🆕 | 64.8k | Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. | quieres entender el entrenamiento de un GPT desde cero | 🟡 |
| [nanochat](../fichas/nanochat.md) 🆕 | 60.6k | Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. | quieres el pipeline completo de un chat end-to-end | 🟡 |
| [llm.c](../fichas/llm-c.md) 🆕 | 31.5k | Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo. | quieres bajo nivel sin abstracciones y tienes GPU CUDA | 🔴 |
| [train-llm-from-scratch](../fichas/train-llm-from-scratch.md) 🆕 | 13.2k | Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación. | quieres entender el entrenamiento de un LLM mediante una implementación completa | 🔴 |
| [python-machine-learning-book](../fichas/python-machine-learning-book.md) 🆕 | 12.7k | Código de la primera edición del libro Python Machine Learning, con ejemplos de algoritmos y evaluación. | quieres estudiar los ejemplos de la primera edición del libro | 🟡 |
| [MachineLearning](../fichas/machinelearning.md) 🆕 | 5.8k | Ejemplos educativos de algoritmos de machine learning y redes neuronales con Python. | quieres explorar implementaciones pequeñas de algoritmos clásicos | 🟡 |
| [how-to-train-your-gpt](../fichas/how-to-train-your-gpt.md) 🆕 | 4.2k | Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción. | quieres una guía explicada y narrada | 🟢 |

## Modelos abiertos y fundacionales

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [TimesFM](../fichas/timesfm.md) 🆕 | 35.5k | Modelo fundacional de Google Research para pronosticar series de tiempo sin entrenamiento previo. | necesitas pronósticos rápidos sin entrenar modelos | 🟡 |
| [DeepSeek-Coder](../fichas/deepseek-coder.md) 🆕 | 24.4k | Familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software. | quieres un modelo de código abierto y desplegable on-prem | 🔴 |
| [cosmos](../fichas/cosmos.md) 🆕 | 12.4k | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. | trabajas IA física/robótica y necesitas datos sintéticos | 🔴 |
| [Nemotron (NVIDIA)](../fichas/nemotron.md) 🆕 | 2.3k | Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. | usas GPUs NVIDIA y quieres modelos abiertos optimizados | 🔴 |

## CLIs y SDKs de desarrollo

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [GitHub CLI](../fichas/cli.md) 🆕 | 47k | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | trabajas con GitHub desde la terminal o con agentes | 🟢 |
| [openai-python](../fichas/openai-python.md) 🆕 | 32.2k | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. | usas modelos de OpenAI desde Python y quieres el cliente oficial | 🟢 |

## Datos y notebooks

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [DuckDB](../fichas/duckdb.md) 🆕 | 43.1k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | quieres SQL analítico rápido sin montar servidores | 🟢 |
| ⭐ [marimo](../fichas/marimo.md) 🆕 | 23.6k | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | quieres notebooks reproducibles y versionables | 🟢 |
| [Polars](../fichas/polars.md) 🆕 | 40.3k | Librería de DataFrames escrita en Rust, mucho más rápida que pandas. | tu análisis con pandas es lento | 🟢 |
| [data-science-ipython-notebooks](../fichas/data-science-ipython-notebooks.md) 🆕 | 29.4k | Gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep learning y big data, con ejemplos listos para ejecutar. | estudias/consultas DS con ejemplos ejecutables | 🟢 |
| [awesome-bigdata](../fichas/awesome-bigdata.md) 🆕 | 14.7k | Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala. | diseñas pipelines de datos grandes y necesitas descubrir el ecosistema | 🟢 |
| [hudi](../fichas/hudi.md) 🆕 | 6.4k | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. | necesitas gestionar cambios y cargas incrementales en un data lake | 🔴 |
| [GlobalBuildingAtlas](../fichas/globalbuildingatlas.md) 🆕 | 2.3k | Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. | necesitas geometría de edificios para análisis territorial o visualización urbana | 🔴 |
| [BigData](../fichas/bigdata.md) 🆕 | 642 | Colección educativa de proyectos de datos con ejercicios de Hive, HDFS, Spark, HBase y sistemas de recomendación. | quieres estudiar ejemplos prácticos del ecosistema de big data | 🔴 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### Repomix, codegraph, codebase-memory-mcp, GitNexus

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Repomix](../fichas/repomix.md) | 29.3k | quieres dar tu repo completo a un LLM | el repo es enorme; mira `codebase-memory-mcp` o `serena` |
| [codegraph](../fichas/codegraph.md) | 77.6k | trabajas repos grandes y el contexto del agente es caro | tu base de código es pequeña y no justifica mantener un índice |
| [codebase-memory-mcp](../fichas/codebase-memory-mcp.md) | 48.6k | tu agente trabaja en repos grandes | tu repo es pequeño; usa `repomix` |
| [GitNexus](../fichas/gitnexus.md) | 48.5k | quieres entender un repo puntual de forma visual | necesitas indexar muchos repos a escala (codegraph) o no quieres front web |

### Semgrep, ast-grep

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Semgrep](../fichas/semgrep.md) | 17.7k | quieres análisis de seguridad en CI | solo quieres refactors estructurales; mira `ast-grep` |
| [ast-grep](../fichas/ast-grep.md) | 16.6k | necesitas buscar o reescribir código por estructura | buscas análisis de seguridad con reglas existentes; mira `semgrep` |

### Unsloth, LLaMA-Factory

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Unsloth](../fichas/unsloth.md) | 79.5k | quieres afinar un LLM con pocos recursos | necesitas muchas técnicas y una UI de entrenamiento; mira `llama-factory` |
| [LLaMA-Factory](../fichas/llama-factory.md) | 76k | quieres muchas técnicas de fine-tuning con UI | buscas la opción más eficiente en memoria; mira `unsloth` |

### LLM Course, LLMs from Scratch, nanoGPT

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [LLM Course](../fichas/llm-course.md) | 85.1k | quieres una ruta completa para aprender LLM | buscas un curso introductorio de apps; mira `generative-ai-for-beginners` |
| [LLMs from Scratch](../fichas/llms-from-scratch.md) | 108k | quieres entender los LLM implementándolos | solo quieres usar modelos existentes |
| [nanoGPT](../fichas/nanogpt.md) | 64.8k | quieres entender el entrenamiento de un GPT desde cero | solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat) |

### DuckDB, Polars

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [DuckDB](../fichas/duckdb.md) | 43.1k | quieres SQL analítico rápido sin montar servidores | necesitas una base transaccional multiusuario; usa PostgreSQL |
| [Polars](../fichas/polars.md) | 40.3k | tu análisis con pandas es lento | prefieres SQL; mira `duckdb` |

## 🧪 Recetas que usan esta categoría

- [🧠 Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md) — Que un agente de código entienda una base de código enorme sin gastar todo su contexto.
- [📊 Analítica de producto con IA](../playbooks/analitica-con-ia.md) — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
