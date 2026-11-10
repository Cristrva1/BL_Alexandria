# 7. Inteligencia de Código, Datos & Entrenamiento — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ast-grep`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Busca y reemplaza código por su estructura (AST), no por texto. Útil para refactors masivos y reglas de lint propias.
**Stack:** Rust, tree-sitter
**Repo:** https://github.com/ast-grep/ast-grep

**Instalación** [?]: `git clone https://github.com/ast-grep/ast-grep (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas buscar o reescribir código por estructura
**Evita si:** buscas análisis de seguridad con reglas existentes; mira `semgrep`
**Combina con:** `tree-sitter`, `claude-code`
**Alternativas (elige una):** `semgrep`

## `awesome-bigdata`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el "qué uso para X a escala": un panorama del stack de datos grandes en un solo vistazo.
**Stack:** Markdown
**Repo:** https://github.com/oxnr/awesome-bigdata

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-bigdata/). Si necesitas el código: git clone https://github.com/oxnr/awesome-bigdata`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** diseñas pipelines de datos grandes y necesitas descubrir el ecosistema
**Evita si:** tu proyecto es pequeño y no justifica herramientas de big data
**Combina con:** `awesome-dataviz`

## `cli`
role=app · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** No es un agente: es la herramienta que los agentes de código usan para abrir PRs, revisar issues o lanzar workflows.
**Stack:** Go
**Repo:** https://github.com/cli/cli

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** trabajas con GitHub desde la terminal o con agentes
**Evita si:** usas GitLab u otra forja
**Combina con:** `claude-code`, `github-mcp-server`

## `codebase-memory-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Indexa repos en milisegundos y da al agente herramientas MCP para entender arquitectura, dependencias y cambios sin leer archivo por archivo.
**Stack:** C
**Repo:** https://github.com/DeusData/codebase-memory-mcp

**Instalación** [?]: `git clone https://github.com/DeusData/codebase-memory-mcp (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** tu agente trabaja en repos grandes
**Evita si:** tu repo es pequeño; usa `repomix`
**Combina con:** `claude-code`, `serena`
**Alternativas (elige una):** `codegraph`, `gitnexus`

## `codegraph`
role=runtime · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el coste de contexto de los agentes en repos grandes.
**Stack:** JavaScript/Node.js (binario autónomo)
**Repo:** https://github.com/colbymchenry/codegraph

**Instalación** [~]: `git clone https://github.com/colbymchenry/codegraph && cd codegraph && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** trabajas repos grandes y el contexto del agente es caro
**Evita si:** tu base de código es pequeña y no justifica mantener un índice
**Combina con:** `graphify`, `headroom`
**Alternativas (elige una):** `codebase-memory-mcp`, `serena`

## `cosmos`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.
**Stack:** Python, GPU (NVIDIA/CUDA)
**Repo:** https://github.com/NVIDIA/cosmos

**Instalación** [~]: `git clone https://github.com/NVIDIA/cosmos && cd cosmos && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** trabajas IA física/robótica y necesitas datos sintéticos
**Evita si:** haces tareas de texto/UI o no tienes GPU para servirlo
**Combina con:** `diffusers`

## `data-science-ipython-notebooks`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el "aprender DS con ejemplos reales" sin tener que montarlos tú desde cero.
**Stack:** Python, Jupyter
**Repo:** https://github.com/donnemartin/data-science-ipython-notebooks

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/data-science-ipython-notebooks/). Si necesitas el código: git clone https://github.com/donnemartin/data-science-ipython-notebooks`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** estudias/consultas DS con ejemplos ejecutables
**Evita si:** buscas una librería, no ejemplos, o necesitas material actualizado a las versiones más recientes
**Combina con:** `dash`, `streamlit`

## `deepseek-coder`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia infraestructura.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/deepseek-ai/DeepSeek-Coder

**Instalación** [~]: `git clone https://github.com/deepseek-ai/DeepSeek-Coder && cd DeepSeek-Coder && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un modelo de código abierto y desplegable on-prem
**Evita si:** prefieres APIs comerciales gestionadas o no tienes GPU para servirlo
**Combina con:** `litellm`, `codegraph`

## `deepwiki-open`
role=app · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'google', 'local']

**Qué es:** Analiza un repositorio y crea documentación navegable con diagramas y un chat para preguntar sobre el código.
**Stack:** Python, Next.js
**Repo:** https://github.com/AsyncFuncAI/deepwiki-open

**Instalación** [~]: `git clone https://github.com/AsyncFuncAI/deepwiki-open && cd deepwiki-open && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres documentación automática de un repositorio
**Evita si:** necesitas contexto de librerías externas; mira `context7`
**Combina con:** `ollama`
**Alternativas (elige una):** `context7`

## `defending-code-reference-harness`
role=skill · exec=cloud · setup=medium · mcp=False · prov=['anthropic']

**Qué es:** Implementación de referencia para descubrir y corregir vulnerabilidades de forma autónoma con Claude, basada en experiencia con equipos de seguridad.
**Stack:** Python, Markdown
**Repo:** https://github.com/anthropics/defending-code-reference-harness

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Defending Code Reference Harness/). Si necesitas el código: git clone https://github.com/anthropics/defending-code-reference-harness`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres un flujo de seguridad con agentes probado
**Evita si:** solo necesitas un escáner estático; mira `semgrep`
**Combina con:** `claude-code`, `semgrep`

## `duckdb`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** El "SQLite de la analítica": sin servidor, embebida en Python, R o Node, y capaz de procesar millones de filas en segundos.
**Stack:** C++
**Repo:** https://github.com/duckdb/duckdb

**Instalación** [?]: `git clone https://github.com/duckdb/duckdb (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres SQL analítico rápido sin montar servidores
**Evita si:** necesitas una base transaccional multiusuario; usa PostgreSQL
**Combina con:** `marimo`, `superset`
**Alternativas (elige una):** `polars`

## `gitnexus`
role=app · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el "llegar a un proyecto ajeno y no saber por dónde empezar": lo navegas y lo discutes en vez de leer ficheros sueltos.
**Stack:** web/TypeScript
**Repo:** https://github.com/abhigyanpatwari/GitNexus

**Instalación** [~]: `git clone https://github.com/abhigyanpatwari/GitNexus && cd GitNexus && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres entender un repo puntual de forma visual
**Evita si:** necesitas indexar muchos repos a escala (codegraph) o no quieres front web
**Combina con:** `codegraph`
**Alternativas (elige una):** `repomix`, `codebase-memory-mcp`, `serena`

## `graphify`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve el onboarding visual: un índice textual no basta cuando hay relaciones entre archivos.
**Stack:** Python 3.10+, uv/pipx
**Repo:** https://github.com/Graphify-Labs/graphify

**Instalación** [~]: `git clone https://github.com/Graphify-Labs/graphify && cd graphify && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres ver conexiones visualmente o auditar un sistema
**Evita si:** solo necesitas índice textual barato (codegraph) o tu proyecto es trivial
**Combina con:** `codegraph`, `graphrag`

## `how-to-train-your-gpt`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el "quiero entenderlo con explicación narrada" frente al código desnudo de nanoGPT.
**Stack:** Python, PyTorch
**Repo:** https://github.com/raiyanyahya/how-to-train-your-gpt

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/how-to-train-your-gpt/). Si necesitas el código: git clone https://github.com/raiyanyahya/how-to-train-your-gpt`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres una guía explicada y narrada
**Evita si:** prefieres solo el código limpio (nanoGPT) o buscas algo productivo
**Combina con:** `nanogpt`, `nanochat`

## `llama-factory`
role=app · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Soporta LoRA, QLoRA, ajuste completo, DPO y más desde una UI o CLI. Muy usado en investigación e industria.
**Stack:** Python, PyTorch, Gradio
**Repo:** https://github.com/hiyouga/LlamaFactory

**Instalación** [~]: `git clone https://github.com/hiyouga/LlamaFactory && cd LlamaFactory && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres muchas técnicas de fine-tuning con UI
**Evita si:** buscas la opción más eficiente en memoria; mira `unsloth`
**Combina con:** `peft`, `transformers`
**Alternativas (elige una):** `unsloth`

## `llm-course`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Tres rutas: fundamentos, científico de LLM (entrenar y afinar) e ingeniero de LLM (apps y despliegue), con recursos y notebooks ejecutables.
**Stack:** Markdown, Jupyter, Python
**Repo:** https://github.com/mlabonne/llm-course

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/LLM Course/). Si necesitas el código: git clone https://github.com/mlabonne/llm-course`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres una ruta completa para aprender LLM
**Evita si:** buscas un curso introductorio de apps; mira `generative-ai-for-beginners`
**Combina con:** `unsloth`, `llama-factory`
**Alternativas (elige una):** `llms-from-scratch`, `generative-ai-for-beginners`

## `llm.c`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framework.
**Stack:** C, CUDA
**Repo:** https://github.com/karpathy/llm.c

**Instalación** [?]: `git clone https://github.com/karpathy/llm.c (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres bajo nivel sin abstracciones y tienes GPU CUDA
**Evita si:** prefieres PyTorch (nanoGPT) o no tienes CUDA
**Combina con:** `nanogpt`

## `llms-from-scratch`
role=directory · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Construyes atención, GPT, preentrenamiento y fine-tuning desde cero, entendiendo cada pieza. Ideal para aprender cómo funcionan por dentro.
**Stack:** Python, PyTorch, Jupyter
**Repo:** https://github.com/rasbt/LLMs-from-scratch

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/LLMs from Scratch/). Si necesitas el código: git clone https://github.com/rasbt/LLMs-from-scratch`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres entender los LLM implementándolos
**Evita si:** solo quieres usar modelos existentes
**Combina con:** `pytorch`
**Alternativas (elige una):** `llm-course`, `nanogpt`

## `marimo`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Al cambiar una celda se recalculan las dependientes, evitando estados ocultos. Incluye SQL, gráficos interactivos y asistente de IA.
**Stack:** Python, TypeScript
**Repo:** https://github.com/marimo-team/marimo

**Instalación** [~]: `git clone https://github.com/marimo-team/marimo && cd marimo && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres notebooks reproducibles y versionables
**Evita si:** dependes de extensiones de Jupyter
**Combina con:** `duckdb`, `polars`

## `nanochat`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/karpathy/nanochat

**Instalación** [~]: `pip install nanochat   (o: uv add nanochat)`
_Nombre PyPI puede diferir de 'nanochat'; verifica en pypi.org._

**Elige si:** quieres el pipeline completo de un chat end-to-end
**Evita si:** solo necesitas el core del modelo (nanoGPT) o un modelo listo para usar
**Combina con:** `nanogpt`

## `nanogpt`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción.
**Stack:** Python, PyTorch, GPU
**Repo:** https://github.com/karpathy/nanoGPT

**Instalación** [~]: `pip install nanogpt   (o: uv add nanogpt)`
_Nombre PyPI puede diferir de 'nanoGPT'; verifica en pypi.org._

**Elige si:** quieres entender el entrenamiento de un GPT desde cero
**Evita si:** solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat)
**Combina con:** `nanochat`
**Alternativas (elige una):** `llms-from-scratch`

## `nemotron`
role=directory · exec=local · setup=heavy · mcp=False · prov=['local']

**Qué es:** Reúne guías de entrenamiento, despliegue y casos de uso de los modelos Nemotron, pensados para IA agéntica eficiente.
**Stack:** Python, Jupyter
**Repo:** https://github.com/NVIDIA-NeMo/Nemotron

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Nemotron (NVIDIA)/). Si necesitas el código: git clone https://github.com/NVIDIA-NeMo/Nemotron`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** usas GPUs NVIDIA y quieres modelos abiertos optimizados
**Evita si:** buscas la forma más simple de correr modelos; mira `ollama`
**Combina con:** `vllm`, `nemoclaw`

## `openai-python`
role=library · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el glue HTTP: no escribes peticiones a mano, usas clientes tipados con streaming.
**Stack:** Python
**Repo:** https://github.com/openai/openai-python

**Instalación** [~]: `pip install openai   (o: uv add openai)`
_Nombre PyPI puede diferir de 'openai-python'; verifica en pypi.org._

**Elige si:** usas modelos de OpenAI desde Python y quieres el cliente oficial
**Evita si:** quieres abstracción multi-proveedor (litellm) o no usas OpenAI
**Combina con:** `litellm`, `langchain`

## `peft`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Adapta modelos grandes entrenando solo una pequeña parte de los parámetros, ahorrando memoria y tiempo.
**Stack:** Python, PyTorch
**Repo:** https://github.com/huggingface/peft

**Instalación** [~]: `pip install peft   (o: uv add peft)`
_Nombre PyPI puede diferir de 'PEFT'; verifica en pypi.org._

**Elige si:** afinas modelos con código propio
**Evita si:** prefieres una herramienta lista; mira `unsloth`
**Combina con:** `transformers`, `trl`

## `polars`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** API expresiva con ejecución perezosa y paralela para procesar datos grandes en un solo equipo.
**Stack:** Rust, Python
**Repo:** https://github.com/pola-rs/polars

**Instalación** [~]: `pip install polars   (o: uv add polars)`
_Nombre PyPI puede diferir de 'Polars'; verifica en pypi.org._

**Elige si:** tu análisis con pandas es lento
**Evita si:** prefieres SQL; mira `duckdb`
**Combina con:** `marimo`
**Alternativas (elige una):** `duckdb`

## `pytorch`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Base de la mayoría de investigación y modelos abiertos actuales.
**Stack:** Python, C++, CUDA
**Repo:** https://github.com/pytorch/pytorch

**Instalación** [~]: `pip install pytorch   (o: uv add pytorch)`
_Nombre PyPI puede diferir de 'PyTorch'; verifica en pypi.org._

**Elige si:** entrenas o investigas modelos
**Evita si:** solo consumes APIs de LLM
**Combina con:** `transformers`

## `repomix`
role=app · exec=local · setup=easy · mcp=True · prov=—

**Qué es:** Genera un archivo XML, Markdown o texto con la estructura y el código del repo, respetando .gitignore y contando tokens. También funciona como servidor MCP.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/yamadashy/repomix

**Instalación** [~]: `git clone https://github.com/yamadashy/repomix && cd repomix && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres dar tu repo completo a un LLM
**Evita si:** el repo es enorme; mira `codebase-memory-mcp` o `serena`
**Combina con:** `claude-code`
**Alternativas (elige una):** `gitnexus`

## `semgrep`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Encuentra bugs y vulnerabilidades con miles de reglas comunitarias o propias. Muy usado en CI de seguridad.
**Stack:** OCaml, Python
**Repo:** https://github.com/semgrep/semgrep

**Instalación** [~]: `git clone https://github.com/semgrep/semgrep && cd semgrep && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres análisis de seguridad en CI
**Evita si:** solo quieres refactors estructurales; mira `ast-grep`
**Combina con:** `defending-code-reference-harness`
**Alternativas (elige una):** `ast-grep`

## `swe-bench`
role=directory · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Da al modelo un repositorio y un issue y comprueba si su parche pasa las pruebas. Es la referencia para medir agentes de código.
**Stack:** Python, Docker
**Repo:** https://github.com/SWE-bench/SWE-bench

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/SWE-bench/). Si necesitas el código: git clone https://github.com/SWE-bench/SWE-bench`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas medir agentes de código con un estándar
**Evita si:** solo quieres usar un agente
**Combina con:** `swe-agent`

## `timesfm`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Predice ventas, demanda o tráfico a partir del histórico sin entrenar un modelo propio (zero-shot).
**Stack:** Python, PyTorch, JAX
**Repo:** https://github.com/google-research/timesfm

**Instalación** [~]: `pip install timesfm   (o: uv add timesfm)`
_Nombre PyPI puede diferir de 'TimesFM'; verifica en pypi.org._

**Elige si:** necesitas pronósticos rápidos sin entrenar modelos
**Evita si:** necesitas explicabilidad estadística clásica
**Combina con:** `polars`, `duckdb`

## `transformers`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Da acceso a cientos de miles de modelos con una API común para inferencia y entrenamiento. Es la base del ecosistema de modelos abiertos.
**Stack:** Python, PyTorch
**Repo:** https://github.com/huggingface/transformers

**Instalación** [~]: `pip install transformers   (o: uv add transformers)`
_Nombre PyPI puede diferir de 'Transformers'; verifica en pypi.org._

**Elige si:** trabajas con modelos abiertos en Python
**Evita si:** solo quieres chatear con un modelo local; mira `ollama`
**Combina con:** `peft`, `trl`, `pytorch`

## `tree-sitter`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Genera parsers rápidos que actualizan el árbol sintáctico mientras editas. Lo usan editores, Aider, ast-grep y muchas herramientas de código con IA.
**Stack:** Rust, C
**Repo:** https://github.com/tree-sitter/tree-sitter

**Instalación** [?]: `git clone https://github.com/tree-sitter/tree-sitter (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** construyes herramientas que entienden código
**Evita si:** solo necesitas buscar patrones; mira `ast-grep`
**Combina con:** `ast-grep`, `aider`

## `trl`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Ofrece entrenadores listos para ajuste supervisado y por preferencias, usados para alinear modelos.
**Stack:** Python, PyTorch
**Repo:** https://github.com/huggingface/trl

**Instalación** [~]: `pip install trl   (o: uv add trl)`
_Nombre PyPI puede diferir de 'TRL'; verifica en pypi.org._

**Elige si:** necesitas SFT o RL sobre modelos abiertos
**Evita si:** quieres algo sin código; mira `llama-factory`
**Combina con:** `transformers`, `peft`, `unsloth`

## `unsloth`
role=app · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Afina modelos como Qwen, Llama o Gemma en una sola GPU y expórtalos a GGUF u Ollama. Ofrece notebooks gratuitos y una interfaz local.
**Stack:** Python, Triton, PyTorch
**Repo:** https://github.com/unslothai/unsloth

**Instalación** [~]: `git clone https://github.com/unslothai/unsloth && cd unsloth && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres afinar un LLM con pocos recursos
**Evita si:** necesitas muchas técnicas y una UI de entrenamiento; mira `llama-factory`
**Combina con:** `ollama`, `trl`
**Alternativas (elige una):** `llama-factory`
