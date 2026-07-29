# 5. MCP & Conectividad — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `awesome-mcp-clients`
role=directory · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** A curated list of awesome Model Context Protocol (MCP) clients.
**Stack:** python, typescript, javascript, react, docker, postgres, langchain
**Repo:** https://github.com/punkpeye/awesome-mcp-clients.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-mcp-clients/). Si necesitas el código: git clone https://github.com/punkpeye/awesome-mcp-clients.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`

## `claude-plugins-official`
role=platform · exec=cloud · setup=medium · mcp=False · prov=—

**Qué es:** A curated directory of high-quality plugins for Claude Code.
**Stack:** typescript
**Repo:** https://github.com/anthropics/claude-plugins-official.git

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `n8n-skills`, `mcp`, `servers`

## `github-mcp-server`
role=platform · exec=local · setup=medium · mcp=True · prov=—

**Qué es:** The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read repositories and code files, manage issues and PRs, analyze code, and automate workflows. All through natural language interactions.
**Stack:** python, typescript, javascript, react, docker
**Repo:** https://github.com/github/github-mcp-server.git

**Instalación** [~]: `git clone https://github.com/github/github-mcp-server.git && cd github-mcp-server && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`

## `graphify`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** 🇺🇸 English | 🇨🇳 简体中文 | 🇯🇵 日本語 | 🇰🇷 한국어 | 🇩🇪 Deutsch | 🇫🇷 Français | 🇪🇸 Español | 🇮🇳 <a href="docs/translatio.
**Stack:** python, typescript, javascript, docker, postgres, whisper
**Repo:** https://github.com/safishamsi/graphify.git

**Instalación** [~]: `pip install graphify   (o: uv add graphify)`
_Nombre PyPI puede diferir de 'graphify'; verifica en pypi.org._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`

## `mcp`
role=directory · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** This repository contains a list of Google's official Model Context Protocol (MCP) servers, guidance on how to deploy MCP servers to Google Cloud, and examples to get started.
**Stack:** typescript, postgres
**Repo:** https://github.com/google/mcp.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/mcp/). Si necesitas el código: git clone https://github.com/google/mcp.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `servers`

## `mcp-neo4j`
role=directory · exec=local · setup=medium · mcp=True · prov=—

**Qué es:** These MCP servers are a part of the Neo4j Labs program. They are developed and maintained by the Neo4j Field GenAI team and welcome contributions from the larger developer community. These servers are frequently updated with new and experimental features, but are not supported by the Neo4j product team.
**Stack:** typescript
**Repo:** https://github.com/neo4j-contrib/mcp-neo4j.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/mcp-neo4j/). Si necesitas el código: git clone https://github.com/neo4j-contrib/mcp-neo4j.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`

## `metabase`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** The easiest way to get started with Metabase is to sign up for a free trial of Metabase Cloud.
**Stack:** javascript/typescript, typescript, javascript, react, docker, postgres
**Repo:** https://github.com/metabase/metabase.git

**Instalación** [~]: `git clone https://github.com/metabase/metabase.git && cd metabase && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`

## `n8n-skills`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Expert Claude Code skills for building flawless n8n workflows using the n8n-mcp MCP server**.
**Stack:** python, typescript, javascript, docker, postgres, langchain
**Repo:** https://github.com/czlonkowski/n8n-skills.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/n8n-skills/). Si necesitas el código: git clone https://github.com/czlonkowski/n8n-skills.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `mcp`, `servers`

## `notebooklm-mcp-cli`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** Programmatic access to Google NotebookLM** — via command-line interface (CLI) or Model Context Protocol (MCP) server.
**Stack:** python, typescript, react, postgres
**Repo:** https://github.com/jacob-bd/notebooklm-mcp-cli.git

**Instalación** [~]: `git clone https://github.com/jacob-bd/notebooklm-mcp-cli.git && cd notebooklm-mcp-cli && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`

## `opencut`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** OpenCut is being rewritten from the ground up.** What's coming:.
**Stack:** typescript
**Repo:** https://github.com/OpenCut-app/OpenCut.git

**Instalación** [~]: `git clone https://github.com/OpenCut-app/OpenCut.git && cd OpenCut && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`

## `public-apis`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** The Public APIs repository is manually curated by community members like you and folks working at APILayer. It includes an extensive list of public APIs from many domains that you can use for your own products. Consider it a treasure trove of APIs well-managed by the community over the years.
**Stack:** python, typescript, javascript, react, docker, postgres
**Repo:** https://github.com/public-apis/public-apis.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/public-apis/). Si necesitas el código: git clone https://github.com/public-apis/public-apis.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`

## `servers`
role=directory · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** This repository is a collection of *reference implementations* for the Model Context Protocol (MCP), as well as references to community-built servers and additional resources.
**Stack:** javascript/typescript, python, typescript, javascript, postgres
**Repo:** https://github.com/modelcontextprotocol/servers.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/servers/). Si necesitas el código: git clone https://github.com/modelcontextprotocol/servers.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `claude-plugins-official`, `n8n-skills`, `mcp`
