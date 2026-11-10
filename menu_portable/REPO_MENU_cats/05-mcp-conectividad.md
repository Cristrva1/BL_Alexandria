# 5. MCP & Conectividad — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `awesome-mcp-clients`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Ayuda a elegir dónde usar tus servidores MCP: chats de escritorio, editores, CLIs y plataformas.
**Stack:** Markdown
**Repo:** https://github.com/punkpeye/awesome-mcp-clients

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Awesome MCP Clients/). Si necesitas el código: git clone https://github.com/punkpeye/awesome-mcp-clients`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas un cliente para tus servidores MCP
**Evita si:** buscas servidores; mira `awesome-mcp-servers`
**Combina con:** `awesome-mcp-servers`

## `awesome-mcp-servers`
role=directory · exec=hybrid · setup=easy · mcp=True · prov=—

**Qué es:** Resuelve el "¿ya existe un servidor para X?" antes de que construyas el tuyo desde cero.
**Stack:** Markdown
**Repo:** https://github.com/punkpeye/awesome-mcp-servers

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-mcp-servers/). Si necesitas el código: git clone https://github.com/punkpeye/awesome-mcp-servers`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas antes de construir
**Evita si:** ya sabes que necesitas uno a medida y no te vale ninguno listado
**Combina con:** `mcp-use`, `servers`

## `blender-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Crea y modifica escenas, objetos y materiales hablando con tu asistente. Útil para prototipos 3D rápidos.
**Stack:** Python, Blender
**Repo:** https://github.com/ahujasid/mcp-for-blender

**Instalación** [~]: `git clone https://github.com/ahujasid/mcp-for-blender && cd mcp-for-blender && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres manejar Blender con tu agente
**Evita si:** no trabajas en 3D
**Combina con:** `claude-code`

## `chrome-devtools-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Tu agente de código puede abrir páginas, leer errores de consola, inspeccionar peticiones y medir rendimiento para depurar de verdad.
**Stack:** TypeScript, Puppeteer
**Repo:** https://github.com/ChromeDevTools/chrome-devtools-mcp

**Instalación** [~]: `git clone https://github.com/ChromeDevTools/chrome-devtools-mcp && cd chrome-devtools-mcp && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** tu agente necesita depurar una web como lo harías en DevTools
**Evita si:** solo quieres automatizar navegación; mira `playwright-mcp`
**Combina con:** `claude-code`
**Alternativas (elige una):** `playwright-mcp`, `browser-harness`

## `context7`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Evita que el modelo invente APIs viejas: busca la documentación vigente de la librería que estás usando y la inyecta en el prompt.
**Stack:** TypeScript
**Repo:** https://github.com/upstash/context7

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** tu agente de código usa librerías que cambian a menudo
**Evita si:** trabajas sin conexión a internet
**Combina con:** `claude-code`, `cline`, `opencode`
**Alternativas (elige una):** `deepwiki-open`

## `fastmcp`
role=library · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Convierte funciones Python en herramientas MCP con un decorador y añade autenticación, composición de servidores y cliente de pruebas. Su versión 1 se integró en el SDK oficial.
**Stack:** Python
**Repo:** https://github.com/PrefectHQ/fastmcp

**Instalación** [~]: `pip install fastmcp   (o: uv add fastmcp)`
_Nombre PyPI puede diferir de 'FastMCP'; verifica en pypi.org._

**Elige si:** quieres crear un servidor MCP en Python rápido
**Evita si:** trabajas en TypeScript; mira `mcp-typescript-sdk`
**Combina con:** `mcp-inspector`, `claude-code`
**Alternativas (elige una):** `mcp-python-sdk`

## `figma-context-mcp`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Simplifica la respuesta de la API de Figma y da al agente solo lo relevante (estructura, estilos, medidas) para convertir un diseño en código.
**Stack:** TypeScript
**Repo:** https://github.com/GLips/Figma-Context-MCP

**Instalación** [~]: `git clone https://github.com/GLips/Figma-Context-MCP && cd Figma-Context-MCP && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** implementas diseños de Figma con un agente de código
**Evita si:** no usas Figma
**Combina con:** `claude-code`, `ui`, `tailwindcss`

## `github-mcp-server`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Conecta asistentes y agentes con la plataforma GitHub: repositorios, issues, pull requests, Actions y seguridad.
**Stack:** Go, Docker
**Repo:** https://github.com/github/github-mcp-server

**Instalación** [~]: `git clone https://github.com/github/github-mcp-server && cd github-mcp-server && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** tu agente trabaja con GitHub
**Evita si:** usas otra forja como GitLab
**Combina con:** `claude-code`, `codex`

## `langchain-mcp-adapters`
role=library · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Permite que tus agentes de LangGraph usen cualquier servidor MCP sin escribir adaptadores. El repo está archivado y su función se integró en LangChain.
**Stack:** Python, LangChain
**Repo:** https://github.com/langchain-ai/langchain-mcp-adapters

**Instalación** [~]: `pip install langchain mcp adapters   (o: uv add langchain mcp adapters)`
_Nombre PyPI puede diferir de 'LangChain MCP Adapters'; verifica en pypi.org._

**Elige si:** usas LangGraph y quieres herramientas MCP
**Evita si:** no usas LangChain
**Combina con:** `langgraph`, `langchain`
**Alternativas (elige una):** `mcp-use`

## `mcp`
role=library · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** Resuelve la fragmentación: cada integración de IA dejaba de ser ad-hoc y pasa a hablar un protocolo común.
**Stack:** TypeScript/Python
**Repo:** https://github.com/google/mcp

**Instalación** [~]: `pip install mcp   (o: uv add mcp)`
_Nombre PyPI puede diferir de 'mcp'; verifica en pypi.org._

**Elige si:** programas MCP a bajo nivel o necesitas conformidad estricta con la spec
**Evita si:** prefieres un framework de alto nivel que abstraiga el protocolo (mcp-use)
**Combina con:** `mcp-use`, `servers`

## `mcp-for-beginners`
role=directory · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Explica los fundamentos del Model Context Protocol, seguridad y despliegue con ejercicios por lenguaje. Disponible en varios idiomas.
**Stack:** Markdown, Python, TypeScript, C#, Java
**Repo:** https://github.com/microsoft/mcp-for-beginners

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/MCP for Beginners/). Si necesitas el código: git clone https://github.com/microsoft/mcp-for-beginners`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres aprender MCP de forma estructurada
**Evita si:** ya construyes servidores MCP; ve directo a `fastmcp`
**Combina con:** `fastmcp`, `mcp-inspector`

## `mcp-inspector`
role=app · exec=local · setup=easy · mcp=True · prov=—

**Qué es:** Conéctate a cualquier servidor MCP, lista sus herramientas y recursos y lánzalos a mano para ver respuestas y errores.
**Stack:** TypeScript, React
**Repo:** https://github.com/modelcontextprotocol/inspector

**Instalación** [~]: `git clone https://github.com/modelcontextprotocol/inspector && cd inspector && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** desarrollas un servidor MCP
**Evita si:** solo usas servidores ya hechos
**Combina con:** `fastmcp`, `mcp-typescript-sdk`

## `mcp-neo4j`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** Resuelve el acceso natural a grafos desde un LLM: el asistente consulta y escribe Cypher sin que tú escribas el glue a mano.
**Stack:** Python, Docker
**Repo:** https://github.com/neo4j-contrib/mcp-neo4j

**Instalación** [~]: `git clone https://github.com/neo4j-contrib/mcp-neo4j && cd mcp-neo4j && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** usas Neo4j con IA y quieres que el asistente hable Cypher
**Evita si:** no trabajas con grafos o tu base es relacional pura
**Combina con:** `graphrag`, `awesome-mcp-servers`

## `mcp-python-sdk`
role=library · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Implementación de referencia del protocolo en Python, con la API FastMCP integrada para servidores sencillos.
**Stack:** Python
**Repo:** https://github.com/modelcontextprotocol/python-sdk

**Instalación** [~]: `pip install mcp python sdk   (o: uv add mcp python sdk)`
_Nombre PyPI puede diferir de 'MCP Python SDK'; verifica en pypi.org._

**Elige si:** quieres el SDK oficial con mínima dependencia
**Evita si:** quieres funciones extra como auth y composición; mira `fastmcp`
**Combina con:** `mcp-inspector`
**Alternativas (elige una):** `fastmcp`

## `mcp-typescript-sdk`
role=library · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Base de la mayoría de servidores MCP en Node.js, con transportes stdio y HTTP.
**Stack:** TypeScript, Node.js, Zod
**Repo:** https://github.com/modelcontextprotocol/typescript-sdk

**Instalación** [~]: `npm install mcp typescript sdk   (o: pnpm add mcp typescript sdk)`
_Nombre npm puede diferir de 'MCP TypeScript SDK'; verifica en npmjs.com._

**Elige si:** creas servidores MCP en TypeScript
**Evita si:** trabajas en Python; mira `fastmcp`
**Combina con:** `mcp-inspector`
**Alternativas (elige una):** `mcp-use`

## `mcp-use`
role=library · exec=hybrid · setup=medium · mcp=True · prov=—

**Qué es:** Resuelve el salto del SDK base (verboso) a algo productivo: registro de tools, inspector y despliegue incluidos.
**Stack:** TypeScript o Python, React (apps)
**Repo:** https://github.com/mcp-use/mcp-use

**Instalación** [~]: `pip install mcp-use   (o: uv add mcp-use)`
_Nombre PyPI puede diferir de 'mcp-use'; verifica en pypi.org._

**Elige si:** construyes un servidor MCP propio y quieres productividad
**Evita si:** solo buscas usar uno ya hecho (awesome-mcp-servers) o necesitas control a nivel spec
**Combina con:** `mcp`, `awesome-mcp-servers`
**Alternativas (elige una):** `langchain-mcp-adapters`, `mcp-typescript-sdk`

## `playwright-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** Da a tu agente un navegador real controlado por el árbol de accesibilidad, sin depender de capturas. Ideal para pruebas y automatización web.
**Stack:** TypeScript, Playwright
**Repo:** https://github.com/microsoft/playwright-mcp

**Instalación** [~]: `git clone https://github.com/microsoft/playwright-mcp && cd playwright-mcp && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres que tu agente use un navegador real
**Evita si:** necesitas depurar rendimiento y consola; mira `chrome-devtools-mcp`
**Combina con:** `claude-code`, `playwright`
**Alternativas (elige una):** `chrome-devtools-mcp`, `browser-use`, `browser-harness`

## `public-apis`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el descubrimiento: en un solo lugar tienes URLs, autenticación y HTTPS de cada API en lugar de buscarlas una a una.
**Stack:** Markdown
**Repo:** https://github.com/public-apis/public-apis

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/public-apis/). Si necesitas el código: git clone https://github.com/public-apis/public-apis`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas datos externos y no sabes qué API usar
**Evita si:** ya tienes tus fuentes definidas o necesitas SLA empresarial (son APIs públicas, sin garantías)
**Combina con:** `n8n`, `firecrawl`

## `serena`
role=runtime · exec=local · setup=easy · mcp=True · prov=['mcp']

**Qué es:** En vez de leer archivos enteros, el agente busca símbolos, referencias y edita a nivel de función usando servidores de lenguaje. Ahorra tokens en repos grandes.
**Stack:** Python, LSP
**Repo:** https://github.com/oraios/serena

**Instalación** [~]: `git clone https://github.com/oraios/serena && cd serena && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tu agente trabaja en un repo grande y gasta muchos tokens leyendo
**Evita si:** tu proyecto es pequeño
**Combina con:** `claude-code`, `codex`
**Alternativas (elige una):** `codegraph`, `gitnexus`

## `servers`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve la falta de ejemplos canónicos: muestra cómo se construye un servidor MCP correcto, paso a paso.
**Stack:** TypeScript/Python
**Repo:** https://github.com/modelcontextprotocol/servers

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/servers/). Si necesitas el código: git clone https://github.com/modelcontextprotocol/servers`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres ejemplos canónicos y plantillas fiables
**Evita si:** buscas soluciones listas para producción (son demos educativas, no hardening)
**Combina con:** `mcp-use`, `awesome-mcp-servers`
