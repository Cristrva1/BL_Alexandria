# 7. Inteligencia de Código, Datos & Entrenamiento — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `awesome-bigdata`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala.
**Stack:** Markdown
**Repo:** https://github.com/oxnr/awesome-bigdata

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-bigdata/). Si necesitas el código: git clone https://github.com/oxnr/awesome-bigdata`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** diseñas pipelines de datos grandes
**Evita si:** tu proyecto es pequeño.
**Combina con:** `awesome-dataviz`

## `codegraph`
role=runtime · exec=local · setup=easy · mcp=False · prov=['anthropic', 'google', 'mcp']

**Qué es:** CLI que indexa tu código y da a los asistentes de IA inteligencia semántica 100% local, permitiéndoles entender la estructura y el flujo de un repo sin leer archivo por archivo ni gastar llamadas a herramientas.
**Stack:** JavaScript/Node.js (binario autónomo)
**Repo:** https://github.com/colbymchenry/codegraph

**Instalación** [~]: `git clone https://github.com/colbymchenry/codegraph && cd codegraph && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** trabajas repos grandes
**Evita si:** tu base de código es pequeña.
**Combina con:** `graphify`, `headroom`

## `cosmos`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=['openai']

**Qué es:** plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots.
**Stack:** Python, GPU
**Repo:** https://github.com/NVIDIA/Cosmos

**Instalación** [~]: `git clone https://github.com/NVIDIA/Cosmos && cd Cosmos && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** trabajas IA física/robótica
**Evita si:** haces tareas de texto/UI.
**Combina con:** `diffusers`

## `data-science-ipython-notebooks`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep learning y big data, con ejemplos listos para ejecutar.
**Stack:** Python, Jupyter
**Repo:** https://github.com/donnemartin/data-science-ipython-notebooks

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/data-science-ipython-notebooks/). Si necesitas el código: git clone https://github.com/donnemartin/data-science-ipython-notebooks`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** estudias/consultas DS
**Evita si:** buscas una librería, no ejemplos.
**Combina con:** `dash`, `streamlit`

## `deepseek-coder`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=['openai', 'local']

**Qué es:** familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/deepseek-ai/DeepSeek-Coder

**Instalación** [~]: `git clone https://github.com/deepseek-ai/DeepSeek-Coder && cd DeepSeek-Coder && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un modelo de código abierto
**Evita si:** prefieres APIs comerciales gestionadas.
**Combina con:** `litellm`, `codegraph`

## `gitnexus`
role=app · exec=hybrid · setup=easy · mcp=False · prov=['anthropic', 'google', 'mcp']

**Qué es:** herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva.
**Stack:** web/TS
**Repo:** https://github.com/abhigyanpatwari/GitNexus

**Instalación** [?]: `git clone https://github.com/abhigyanpatwari/GitNexus (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres entender un repo puntual
**Evita si:** necesitas indexar muchos repos ([codegraph](#-codegraph)).
**Combina con:** `codegraph`
**Alternativas (elige una):** `codegraph`

## `graphify`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['anthropic', 'google']

**Qué es:** generador de grafos de conocimiento para proyectos locales que mapea código, PDFs, imágenes y video en diagramas interactivos, revelando cómo se conectan las piezas de un sistema.
**Stack:** Python 3.10+, uv/pipx
**Repo:** https://github.com/safishamsi/graphify

**Instalación** [~]: `git clone https://github.com/safishamsi/graphify && cd graphify && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres ver conexiones visualmente
**Evita si:** solo necesitas índice textual ([codegraph](#-codegraph)).
**Combina con:** `codegraph`, `graphrag`
**Alternativas (elige una):** `codegraph`

## `graphrag`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.
**Stack:** Python
**Repo:** https://github.com/microsoft/graphrag

**Instalación** [~]: `pip install graphrag   (o: uv add graphrag)`
_Nombre PyPI puede diferir de 'graphrag'; verifica en pypi.org._

**Elige si:** tu corpus tiene relaciones ricas
**Evita si:** un RAG simple basta.
**Combina con:** `graphify`, `mcp-neo4j`, `turbovec`

## `how-to-train-your-gpt`
role=directory · exec=local · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción.
**Stack:** Python
**Repo:** https://github.com/raiyanyahya/how-to-train-your-gpt

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/how-to-train-your-gpt/). Si necesitas el código: git clone https://github.com/raiyanyahya/how-to-train-your-gpt`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres una guía explicada
**Evita si:** prefieres solo el código ([nanoGPT](#-nanogpt)).
**Combina con:** `nanogpt`, `nanochat`
**Alternativas (elige una):** `nanogpt`

## `llm.c`
role=app · exec=cloud · setup=heavy · mcp=False · prov=—

**Qué es:** LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython. Current focus is on pretraining, in particular reproducing the [GPT-2](https://github.com/openai/gpt-2) and [GPT-3](https://arxiv.org/abs/2005.14165) miniseries, along with a parallel PyTorch reference implementation in [train_gpt2.py](train_gpt2.py). You'll recognize this file as a slightly tweaked [nanoGPT](https:
**Stack:** python, typescript, javascript
**Repo:** https://github.com/karpathy/llm.c.git

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** —
**Evita si:** —
**Combina con:** `codegraph`, `graphify`, `graphrag`

## `llmc`
role=library · exec=local · setup=heavy · mcp=False · prov=['openai']

**Qué es:** implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo.
**Stack:** C, CUDA
**Repo:** https://github.com/karpathy/llm.c

**Instalación** [?]: `git clone https://github.com/karpathy/llm.c (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres bajo nivel sin abstracciones
**Evita si:** prefieres PyTorch ([nanoGPT](#-nanogpt)).
**Combina con:** `nanogpt`
**Alternativas (elige una):** `nanogpt`

## `nanochat`
role=library · exec=local · setup=medium · mcp=False · prov=['openai']

**Qué es:** pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/karpathy/nanochat

**Instalación** [~]: `pip install nanochat   (o: uv add nanochat)`
_Nombre PyPI puede diferir de 'nanochat'; verifica en pypi.org._

**Elige si:** quieres el pipeline completo
**Evita si:** solo necesitas el core ([nanoGPT](#-nanogpt)).
**Combina con:** `nanogpt`
**Alternativas (elige una):** `nanogpt`

## `nanogpt`
role=library · exec=local · setup=medium · mcp=False · prov=['openai']

**Qué es:** implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/karpathy/nanoGPT

**Instalación** [~]: `pip install nanogpt   (o: uv add nanogpt)`
_Nombre PyPI puede diferir de 'nanoGPT'; verifica en pypi.org._

**Elige si:** quieres entender el entrenamiento
**Evita si:** solo consumes modelos vía API.
**Combina con:** `nanochat`, `llmc`

## `openai-python`
role=library · exec=cloud · setup=easy · mcp=False · prov=['openai']

**Qué es:** SDK oficial de OpenAI para Python, que expone de forma tipada y cómoda la API (chat, embeddings, imágenes, audio) y es la base habitual para apps que usan sus modelos.
**Stack:** Python
**Repo:** https://github.com/openai/openai-python

**Instalación** [~]: `pip install openai   (o: uv add openai)`
_Nombre PyPI puede diferir de 'openai-python'; verifica en pypi.org._

**Elige si:** usas modelos de OpenAI
**Evita si:** quieres abstracción multi-proveedor ([litellm](06-memoria-llm-ops-observabilidad.md#-litellm)).
**Combina con:** `litellm`, `langchain`
**Alternativas (elige una):** `litellm`
