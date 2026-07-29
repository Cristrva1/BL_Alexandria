# 7. Inteligencia de Código, Datos & Entrenamiento — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `awesome-bigdata`
role=directory · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** A curated list of awesome big data frameworks, resources and other awesomeness. Inspired by awesome-php, awesome-python, awesome-ruby, hadoopecosystemtable & big-data.
**Stack:** python, typescript, javascript, react, docker, postgres
**Repo:** https://github.com/oxnr/awesome-bigdata.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-bigdata/). Si necesitas el código: git clone https://github.com/oxnr/awesome-bigdata.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres awesome big data
**Evita si:** —
**Combina con:** `codegraph`, `gitnexus`, `deepseek-coder`

## `codegraph`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Already installed? Run `codegraph upgrade` to update in place.
**Stack:** javascript/typescript, python, typescript, javascript, react, postgres, fastapi
**Repo:** https://github.com/colbymchenry/codegraph.git

**Instalación** [~]: `pip install codegraph   (o: uv add codegraph)`
_Nombre PyPI puede diferir de 'codegraph'; verifica en pypi.org._

**Elige si:** —
**Evita si:** —
**Combina con:** `gitnexus`, `deepseek-coder`, `llmc`

## `data-science-ipython-notebooks`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** data-science-ipython-notebooks.
**Stack:** python, typescript, postgres
**Repo:** https://github.com/donnemartin/data-science-ipython-notebooks.git

**Instalación** [~]: `pip install data-science-ipython-notebooks   (o: uv add data-science-ipython-notebooks)`
_Nombre PyPI puede diferir de 'data-science-ipython-notebooks'; verifica en pypi.org._

**Elige si:** —
**Evita si:** —
**Combina con:** `codegraph`, `gitnexus`, `deepseek-coder`

## `deepseek-coder`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** 1. Introduction of DeepSeek Coder.
**Stack:** python, typescript, javascript, docker
**Repo:** https://github.com/deepseek-ai/DeepSeek-Coder.git

**Instalación** [~]: `pip install deepseek-coder   (o: uv add deepseek-coder)`
_Nombre PyPI puede diferir de 'DeepSeek-Coder'; verifica en pypi.org._

**Elige si:** quieres 1. introduction of deepseek coder
**Evita si:** —
**Combina con:** `codegraph`, `gitnexus`, `llmc`

## `echarts`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Apache ECharts is a free, powerful charting and visualization library offering easy ways to add intuitive, interactive, and highly customizable charts to your commercial products. It is written in pure JavaScript and based on zrender , which is a whole new lightweight canvas library.
**Stack:** javascript/typescript, typescript, javascript
**Repo:** https://github.com/apache/echarts.git

**Instalación** [~]: `npm install echarts   (o: pnpm add echarts)`
_Nombre npm puede diferir de 'echarts'; verifica en npmjs.com._

**Elige si:** quieres apache echarts
**Evita si:** —
**Combina con:** `codegraph`, `gitnexus`, `deepseek-coder`

## `gitnexus`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** ⚠️ Important Notice:** GitNexus has NO official cryptocurrency, token, or coin. Any token/coin using the GitNexus name on Pump.fun or any other platform is **not affiliated with, endorsed by, or created by** this project or its maintainers. Do not purchase any cryptocurrency claiming association with GitNexus.
**Stack:** javascript/typescript, python, typescript, javascript, react, docker, langchain
**Repo:** https://github.com/abhigyanpatwari/GitNexus.git

**Instalación** [~]: `git clone https://github.com/abhigyanpatwari/GitNexus.git && cd GitNexus && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** —
**Combina con:** `codegraph`, `deepseek-coder`, `llmc`

## `llm.c`
role=app · exec=cloud · setup=heavy · mcp=False · prov=—

**Qué es:** LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython. Current focus is on pretraining, in particular reproducing the GPT-2 and GPT-3 miniseries, along with a parallel PyTorch reference implementation in train_gpt2.py. You'll recognize this file as a slightly tweaked [nanoGPT](https://github.com/karpath.
**Stack:** python, typescript, javascript
**Repo:** https://github.com/karpathy/llm.c.git

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** —
**Evita si:** —
**Combina con:** `codegraph`, `gitnexus`, `deepseek-coder`

## `openai-python`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.9+ application. The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients powered by httpx.
**Stack:** python, typescript, javascript, postgres
**Repo:** https://github.com/openai/openai-python.git

**Instalación** [~]: `git clone https://github.com/openai/openai-python.git && cd openai-python && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres openai python api library
**Evita si:** —
**Combina con:** `codegraph`, `gitnexus`, `deepseek-coder`
