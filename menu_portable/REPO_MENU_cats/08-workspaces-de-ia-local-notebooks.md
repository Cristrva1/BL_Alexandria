# 8. Workspaces de IA Local & Notebooks — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ecc`
role=platform · exec=local · setup=heavy · mcp=False · prov=['anthropic', 'google', 'mcp']

**Qué es:** sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura, sirviendo de capa intermedia entre el modelo y tu sistema.
**Stack:** Rust (core), TypeScript, Python, Go
**Repo:** https://github.com/affaan-m/ECC

**Instalación** [~]: `git clone https://github.com/affaan-m/ECC && cd ECC && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** ejecutas agentes con riesgo
**Evita si:** solo haces prompts de chat.
**Combina con:** `openhands`, `sandbox`, `hermes-agent`

## `notebooklm-mcp-cli`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=['anthropic', 'google', 'mcp']

**Qué es:** CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP.
**Stack:** Python, MCP
**Repo:** https://github.com/jacob-bd/notebooklm-mcp-cli

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** integras NotebookLM con tu asistente
**Evita si:** prefieres la API directa ([notebooklm-py](#-notebooklm-py)).
**Combina con:** `notebooklm-py`, `awesome-mcp-servers`
**Alternativas (elige una):** `notebooklm-py`

## `notebooklm-py`
role=library · exec=cloud · setup=easy · mcp=False · prov=['anthropic', 'google', 'mcp']

**Qué es:** API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código.
**Stack:** Python
**Repo:** https://github.com/teng-lin/notebooklm-py

**Instalación** [~]: `pip install notebooklm-py   (o: uv add notebooklm-py)`
_Nombre PyPI puede diferir de 'notebooklm-py'; verifica en pypi.org._

**Elige si:** automatizas el NotebookLM real
**Evita si:** quieres todo local ([open-notebook](#-open-notebook)).
**Combina con:** `notebooklm-mcp-cli`
**Alternativas (elige una):** `open-notebook`

## `odysseus`
role=platform · exec=local · setup=heavy · mcp=False · prov=['mcp', 'local']

**Qué es:** workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado.
**Stack:** Python, React, PostgreSQL
**Repo:** https://github.com/pewdiepie-archdaemon/odysseus

**Instalación** [~]: `git clone https://github.com/pewdiepie-archdaemon/odysseus && cd odysseus && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres operación privada todo-en-uno
**Evita si:** prefieres SaaS gestionado.
**Combina con:** `open-notebook`, `ecc`, `mem0`

## `open-notebook`
role=app · exec=local · setup=medium · mcp=False · prov=['openai', 'anthropic', 'local']

**Qué es:** clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo.
**Stack:** Python (FastAPI), React/Next.js
**Repo:** https://github.com/lfnovo/open-notebook

**Instalación** [~]: `git clone https://github.com/lfnovo/open-notebook && cd open-notebook && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres NotebookLM privado
**Evita si:** prefieres el NotebookLM real automatizado ([notebooklm-py](#-notebooklm-py)).
**Combina con:** `odysseus`, `markitdown`
**Alternativas (elige una):** `notebooklm-py`
