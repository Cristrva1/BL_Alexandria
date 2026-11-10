# 8. IA Local: Modelos, Chats & Workspaces — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `anything-llm`
role=app · exec=local · setup=easy · mcp=True · prov=['openai', 'anthropic', 'local']

**Qué es:** Organiza documentos en espacios de trabajo, crea RAG sin configurar nada y añade agentes con herramientas. Escritorio o Docker multiusuario.
**Stack:** JavaScript, Node.js, React
**Repo:** https://github.com/Mintplex-Labs/anything-llm

**Instalación** [~]: `git clone https://github.com/Mintplex-Labs/anything-llm && cd anything-llm && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres RAG privado sin programar
**Evita si:** necesitas un pipeline de RAG a medida; mira `llama-index`
**Combina con:** `ollama`
**Alternativas (elige una):** `open-webui`, `khoj`, `private-gpt`

## `cherry-studio`
role=app · exec=hybrid · setup=easy · mcp=True · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Chatea con decenas de proveedores y modelos locales, usa asistentes predefinidos, MCP y base de conocimiento desde una sola app.
**Stack:** TypeScript, Electron, React
**Repo:** https://github.com/CherryHQ/cherry-studio

**Instalación** [~]: `git clone https://github.com/CherryHQ/cherry-studio && cd cherry-studio && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres una app de escritorio multi-proveedor completa
**Evita si:** solo quieres modelos locales simples; mira `jan`
**Combina con:** `ollama`
**Alternativas (elige una):** `jan`, `lobehub`

## `exo`
role=runtime · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Une Macs, PCs o teléfonos en un clúster que comparte la carga de un modelo que no cabría en uno solo.
**Stack:** Python, MLX
**Repo:** https://github.com/exo-explore/exo

**Instalación** [~]: `git clone https://github.com/exo-explore/exo && cd exo && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tienes varios equipos y quieres correr un modelo grande
**Evita si:** un solo equipo te basta; mira `ollama`
**Combina con:** `open-webui`

## `hermes-desktop`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Para quien quiere usar Hermes Agent como aplicación y no solo desde la terminal.
**Stack:** TypeScript, Electron
**Repo:** https://github.com/fathah/hermes-desktop

**Instalación** [~]: `git clone https://github.com/fathah/hermes-desktop && cd hermes-desktop && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** usas Hermes Agent y prefieres una app de escritorio
**Evita si:** no usas Hermes
**Combina con:** `hermes-agent`

## `jan`
role=app · exec=local · setup=easy · mcp=False · prov=['local', 'openai']

**Qué es:** Descarga modelos y chatea en local con privacidad total, o conecta APIs en la nube si quieres. Incluye servidor local compatible con OpenAI.
**Stack:** Rust, TypeScript, Tauri
**Repo:** https://github.com/janhq/jan

**Instalación** [~]: `git clone https://github.com/janhq/jan && cd jan && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un ChatGPT local en tu escritorio
**Evita si:** necesitas multiusuario; mira `open-webui`
**Combina con:** `ollama`
**Alternativas (elige una):** `cherry-studio`, `textgen`

## `khoj`
role=app · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** Busca en tus documentos y en internet, crea agentes personalizados, programa resúmenes y hace investigación profunda. Accesible desde web, Obsidian, Emacs o WhatsApp.
**Stack:** Python, Django, Next.js
**Repo:** https://github.com/khoj-ai/khoj

**Instalación** [~]: `git clone https://github.com/khoj-ai/khoj && cd khoj && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un asistente sobre tus notas personales
**Evita si:** necesitas una plataforma de equipo; mira `anything-llm`
**Combina con:** `ollama`
**Alternativas (elige una):** `anything-llm`, `surfsense`

## `librechat`
role=app · exec=hybrid · setup=medium · mcp=True · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Une OpenAI, Anthropic, Google, Azure, OpenRouter y modelos locales con agentes, artifacts, búsqueda y control de usuarios.
**Stack:** TypeScript, React, Node.js, MongoDB
**Repo:** https://github.com/LibreChat-AI/LibreChat

**Instalación** [~]: `git clone https://github.com/LibreChat-AI/LibreChat && cd LibreChat && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres todos los proveedores en un chat con SSO
**Evita si:** usas sobre todo modelos locales; mira `open-webui`
**Combina con:** `litellm`, `ollama`
**Alternativas (elige una):** `open-webui`, `lobehub`

## `llama-cpp`
role=runtime · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Base de Ollama, LM Studio y muchas apps. Incluye un servidor compatible con OpenAI y herramientas para cuantizar modelos GGUF.
**Stack:** C++, C, CUDA, Metal
**Repo:** https://github.com/ggml-org/llama.cpp

**Instalación** [?]: `git clone https://github.com/ggml-org/llama.cpp (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres el máximo control y rendimiento local
**Evita si:** prefieres simplicidad; mira `ollama`
**Combina con:** `open-webui`
**Alternativas (elige una):** `ollama`, `llamafile`, `localai`

## `llamafile`
role=runtime · exec=local · setup=easy · mcp=False · prov=['local']

**Qué es:** Empaqueta modelo y motor en un ejecutable que funciona en Windows, macOS y Linux sin instalar nada. Proyecto de Mozilla.
**Stack:** C++, Cosmopolitan
**Repo:** https://github.com/mozilla-ai/llamafile

**Instalación** [?]: `git clone https://github.com/mozilla-ai/llamafile (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres repartir un modelo que funcione con doble clic
**Evita si:** vas a cambiar de modelos a menudo; mira `ollama`
**Alternativas (elige una):** `ollama`, `llama-cpp`

## `llmfit`
role=library · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve la elección subjetiva de modelo: la conviertes en un flujo objetivo y reproducible con métricas.
**Stack:** Go/Python
**Repo:** https://github.com/AlexsJones/llmfit

**Instalación** [~]: `pip install llmfit   (o: uv add llmfit)`
_Nombre PyPI puede diferir de 'llmfit'; verifica en pypi.org._

**Elige si:** necesitas elegir modelo con datos y reproducibilidad
**Evita si:** ya tienes el modelo decidido o tu caso no justifica un harness de evaluación
**Combina con:** `litellm`, `langfuse`

## `lobehub`
role=app · exec=hybrid · setup=easy · mcp=True · prov=['openai', 'anthropic', 'google', 'local']

**Qué es:** Antes LobeChat: chat elegante con agentes, plugins, base de conocimiento y despliegue en un clic. Ahora añade agentes que trabajan en tus chats de equipo.
**Stack:** TypeScript, Next.js
**Repo:** https://github.com/lobehub/lobehub

**Instalación** [~]: `git clone https://github.com/lobehub/lobehub && cd lobehub && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres un chat bonito y extensible con agentes
**Evita si:** necesitas el máximo control empresarial; mira `librechat`
**Combina con:** `ollama`
**Alternativas (elige una):** `open-webui`, `librechat`, `cherry-studio`

## `localai`
role=runtime · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** Sustituye la API de OpenAI por una propia que corre modelos abiertos de muchos tipos. Útil para apps que ya hablan con OpenAI.
**Stack:** Go, C++, Docker
**Repo:** https://github.com/mudler/LocalAI

**Instalación** [~]: `git clone https://github.com/mudler/LocalAI && cd LocalAI && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres una API tipo OpenAI local para varias modalidades
**Evita si:** solo necesitas chat local simple; mira `ollama`
**Combina con:** `anything-llm`
**Alternativas (elige una):** `ollama`, `llama-cpp`

## `notebooklm-mcp-cli`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=—

**Qué es:** Convierte NotebookLM en una herramienta invocable por asistentes.
**Stack:** Python, MCP
**Repo:** https://github.com/jacob-bd/gemini-notebook-mcp-cli

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** integras NotebookLM con tu asistente MCP
**Evita si:** prefieres la API directa en scripts (notebooklm-py)
**Combina con:** `notebooklm-py`, `awesome-mcp-servers`

## `notebooklm-py`
role=library · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Cubre el vacío de automatización que la interfaz web oficial no ofrece.
**Stack:** Python
**Repo:** https://github.com/teng-lin/notebooklm-py

**Instalación** [~]: `pip install notebooklm-py   (o: uv add notebooklm-py)`
_Nombre PyPI puede diferir de 'notebooklm-py'; verifica en pypi.org._

**Elige si:** automatizas el NotebookLM real y aceptas el riesgo de API no oficial
**Evita si:** quieres todo local (open-notebook)
**Combina con:** `notebooklm-mcp-cli`

## `odysseus`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Sustituye la dispersión entre varios SaaS por un único panel que tú controlas.
**Stack:** Python, React, PostgreSQL
**Repo:** https://github.com/odysseus-dev/odysseus

**Instalación** [~]: `git clone https://github.com/odysseus-dev/odysseus && cd odysseus && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres operación privada todo-en-uno y aceptas operar la infra
**Evita si:** prefieres SaaS gestionado sin mantenimiento
**Combina con:** `open-notebook`, `ecc`, `mem0`

## `ollama`
role=runtime · exec=local · setup=easy · mcp=False · prov=['local']

**Qué es:** Un comando para bajar y ejecutar modelos como Qwen, Gemma, DeepSeek o gpt-oss. Casi todas las apps de IA local lo soportan.
**Stack:** Go, C++
**Repo:** https://github.com/ollama/ollama

**Instalación** [?]: `git clone https://github.com/ollama/ollama (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres modelos locales funcionando en minutos
**Evita si:** necesitas servir a muchos usuarios con GPU; mira `vllm`
**Combina con:** `open-webui`, `n8n`, `anything-llm`
**Alternativas (elige una):** `llama-cpp`, `localai`, `llamafile`

## `open-notebook`
role=app · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve el envío de documentos sensibles a la nube que implica el NotebookLM oficial.
**Stack:** Python (FastAPI), React/Next.js
**Repo:** https://github.com/lfnovo/open-notebook

**Instalación** [~]: `git clone https://github.com/lfnovo/open-notebook && cd open-notebook && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres NotebookLM privado y sin cuotas
**Evita si:** prefieres el NotebookLM real automatizado (notebooklm-py)
**Combina con:** `odysseus`, `markitdown`
**Alternativas (elige una):** `deeptutor`, `surfsense`

## `open-webui`
role=app · exec=local · setup=easy · mcp=True · prov=['openai', 'local']

**Qué es:** Da a tu equipo un chat privado con usuarios, documentos, búsqueda web, herramientas y modelos locales o en la nube.
**Stack:** Python, Svelte, Docker
**Repo:** https://github.com/open-webui/open-webui

**Instalación** [~]: `git clone https://github.com/open-webui/open-webui && cd open-webui && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas un ChatGPT privado para tu equipo
**Evita si:** solo quieres una app de escritorio individual; mira `jan`
**Combina con:** `ollama`, `searxng`, `litellm`
**Alternativas (elige una):** `librechat`, `lobehub`, `anything-llm`, `textgen`

## `private-gpt`
role=platform · exec=local · setup=medium · mcp=False · prov=['local', 'openai']

**Qué es:** Ofrece una API lista para construir apps de IA sin que los datos salgan de tu entorno. Funciona con cualquier motor compatible con OpenAI.
**Stack:** Python, FastAPI
**Repo:** https://github.com/zylon-ai/private-gpt

**Instalación** [~]: `git clone https://github.com/zylon-ai/private-gpt && cd private-gpt && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** construyes un producto de IA que no puede enviar datos fuera
**Evita si:** quieres una app lista para usuarios finales; mira `anything-llm`
**Combina con:** `ollama`, `qdrant`
**Alternativas (elige una):** `anything-llm`

## `surfsense`
role=app · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'local']

**Qué es:** Conecta tus fuentes (archivos, Slack, Notion, GitHub, web) y conversa con ellas con citas, genera podcasts y reportes. Puede funcionar sin conexión.
**Stack:** Python, FastAPI, Next.js, PostgreSQL
**Repo:** https://github.com/MODSetter/SurfSense

**Instalación** [~]: `git clone https://github.com/MODSetter/SurfSense && cd SurfSense && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres un NotebookLM propio y con más fuentes
**Evita si:** solo quieres el NotebookLM de Google por código; mira `notebooklm-py`
**Combina con:** `ollama`
**Alternativas (elige una):** `open-notebook`, `khoj`

## `textgen`
role=app · exec=local · setup=medium · mcp=False · prov=['local']

**Qué es:** La clásica "oobabooga": carga modelos en muchos formatos y backends, con chat, modo notebook y entrenamiento LoRA.
**Stack:** Python, Gradio
**Repo:** https://github.com/oobabooga/textgen

**Instalación** [~]: `git clone https://github.com/oobabooga/textgen && cd textgen && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres experimentar con muchos backends locales
**Evita si:** quieres algo sencillo; mira `jan` u `ollama`
**Alternativas (elige una):** `jan`, `open-webui`
