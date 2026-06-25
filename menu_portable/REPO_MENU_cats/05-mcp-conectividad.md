# 5. MCP & Conectividad — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `awesome-mcp-clients`
role=directory · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** A curated list of awesome Model Context Protocol (MCP) clients.
**Stack:** python, typescript, javascript, docker
**Repo:** https://github.com/punkpeye/awesome-mcp-clients.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-mcp-clients/). Si necesitas el código: git clone https://github.com/punkpeye/awesome-mcp-clients.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `mcp`, `mcp-use`, `servers`

## `awesome-mcp-servers`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=['anthropic', 'mcp']

**Qué es:** directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar.
**Stack:** Markdown
**Repo:** https://github.com/punkpeye/awesome-mcp-servers

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-mcp-servers/). Si necesitas el código: git clone https://github.com/punkpeye/awesome-mcp-servers`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas antes de construir
**Evita si:** ya sabes que necesitas uno a medida.
**Combina con:** `mcp-use`, `servers`

## `github-mcp-server`
role=platform · exec=local · setup=medium · mcp=True · prov=—

**Qué es:** The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read repositories and code files, manage issues and PRs, analyze code, and automate workflows. All through natural language interactions.
**Stack:** typescript, docker
**Repo:** https://github.com/github/github-mcp-server.git

**Instalación** [~]: `git clone https://github.com/github/github-mcp-server.git && cd github-mcp-server && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas exponer herramientas o contexto a agentes vía MCP
**Evita si:** prefieres conexiones directas sin protocolo estándar
**Combina con:** `mcp`, `mcp-use`, `servers`

## `mcp`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['google', 'mcp']

**Qué es:** núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto.
**Stack:** TS/Python
**Repo:** https://github.com/modelcontextprotocol/modelcontextprotocol

**Instalación** [~]: `pip install mcp   (o: uv add mcp)`
_Nombre PyPI puede diferir de 'mcp'; verifica en pypi.org._

**Elige si:** programas MCP a bajo nivel
**Evita si:** prefieres un framework de alto nivel ([mcp-use](#-mcp-use)).
**Combina con:** `mcp-use`, `servers`
**Alternativas (elige una):** `mcp-use`

## `mcp-neo4j`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=['anthropic', 'google', 'mcp']

**Qué es:** conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud.
**Stack:** Python, Docker
**Repo:** https://github.com/neo4j-contrib/mcp-neo4j

**Instalación** [~]: `git clone https://github.com/neo4j-contrib/mcp-neo4j && cd mcp-neo4j && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** usas Neo4j con IA
**Evita si:** no trabajas con grafos.
**Combina con:** `graphrag`, `awesome-mcp-servers`

## `mcp-use`
role=library · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'anthropic', 'mcp']

**Qué es:** framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable.
**Stack:** TypeScript o Python
**Repo:** https://github.com/mcp-use/mcp-use

**Instalación** [~]: `pip install mcp-use   (o: uv add mcp-use)`
_Nombre PyPI puede diferir de 'mcp-use'; verifica en pypi.org._

**Elige si:** construyes un servidor MCP propio
**Evita si:** solo buscas usar uno ya hecho.
**Combina con:** `mcp`, `awesome-mcp-servers`

## `n8n-mcp`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=['openai', 'anthropic', 'mcp']

**Qué es:** servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n para ayudar a construir y depurar flujos.
**Stack:** Node.js/TypeScript, MCP
**Repo:** https://github.com/czlonkowski/n8n-mcp

**Instalación** [~]: `git clone https://github.com/czlonkowski/n8n-mcp && cd n8n-mcp && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** generas flujos n8n con IA
**Evita si:** no usas n8n.
**Combina con:** `n8n`, `n8n-skills`

## `public-apis`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos.
**Stack:** Markdown
**Repo:** https://github.com/public-apis/public-apis

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/public-apis/). Si necesitas el código: git clone https://github.com/public-apis/public-apis`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas datos externos
**Evita si:** ya tienes tus fuentes definidas.
**Combina con:** `n8n`, `firecrawl`

## `servers`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=['anthropic', 'mcp']

**Qué es:** colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad.
**Stack:** TS/Python
**Repo:** https://github.com/modelcontextprotocol/servers

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/servers/). Si necesitas el código: git clone https://github.com/modelcontextprotocol/servers`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres ejemplos canónicos
**Evita si:** buscas soluciones listas para prod (son demos).
**Combina con:** `mcp-use`, `awesome-mcp-servers`
