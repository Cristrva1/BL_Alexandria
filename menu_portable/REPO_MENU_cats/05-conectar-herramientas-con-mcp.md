# 5. Conectar herramientas con MCP — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `annas-mcp`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=— · tags=servidores,annas-archive,cli,mcp-server,go

**Qué es:** Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos. Expone búsquedas y descargas como herramientas MCP y permite seleccionar espejos disponibles.
**Stack:** Go, Go modules
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: El coste depende del proveedor o la ruta. El proyecto documenta requisitos de acceso a la API de Anna's Archive; no asumir acceso ilimitado por conectar un cliente MCP.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/iosifache/annas-mcp

**Instalación** [?]: `Seguir la instalación original: https://github.com/iosifache/annas-mcp/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas integrar búsquedas de documentos en un cliente MCP
**Evita si:** una conexión directa cubre el caso sin añadir infraestructura
**Combina con:** `markitdown`

## `awesome-mcp-clients`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=mcp

**Qué es:** Ayuda a elegir dónde usar tus servidores MCP: chats de escritorio, editores, CLIs y plataformas.
**Stack:** Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/punkpeye/awesome-mcp-clients

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas un cliente para tus servidores MCP
**Evita si:** buscas servidores; mira `awesome-mcp-servers`
**Combina con:** `awesome-mcp-servers`

## `awesome-mcp-servers`
role=directory · exec=hybrid · setup=easy · mcp=True · prov=— · tags=automation,mcp

**Qué es:** Resuelve el "¿ya existe un servidor para X?" antes de que construyas el tuyo desde cero.
**Stack:** Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/punkpeye/awesome-mcp-servers

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas antes de construir
**Evita si:** ya sabes que necesitas uno a medida y no te vale ninguno listado
**Combina con:** `mcp-use`, `servers`

## `blender-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,design,python

**Qué es:** Crea y modifica escenas, objetos y materiales hablando con tu asistente. Útil para prototipos 3D rápidos.
**Stack:** Python, Blender
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: El coste depende del proveedor o la ruta. Controlar Blender y generar modelos en servicios externos son rutas distintas: los proveedores de generación pueden cobrar.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ahujasid/mcp-for-blender

**Instalación** [+]: `uvx blender-mcp`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres manejar Blender con tu agente
**Evita si:** no trabajas en 3D
**Combina con:** `claude-code`

## `chrome-devtools-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,browser,typescript

**Qué es:** Tu agente de código puede abrir páginas, leer errores de consola, inspeccionar peticiones y medir rendimiento para depurar de verdad.
**Stack:** TypeScript, Puppeteer
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ChromeDevTools/chrome-devtools-mcp

**Instalación** [?]: `Seguir la instalación original: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente necesita depurar una web como lo harías en DevTools
**Evita si:** solo quieres automatizar navegación; mira `playwright-mcp`
**Combina con:** `claude-code`
**Alternativas (elige una):** `playwright-mcp`, `browser-harness`

## `context7`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=mcp · tags=mcp,docs,typescript

**Qué es:** Evita que el modelo invente APIs viejas: busca la documentación vigente de la librería que estás usando y la inyecta en el prompt.
**Stack:** TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: El coste depende del proveedor o la ruta. El cliente MCP usa su propio modelo. Context7 recomienda una API key y aplica límites o planes al servicio de documentación.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/upstash/context7

**Instalación** [?]: `Seguir la instalación original: https://github.com/upstash/context7/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente de código usa librerías que cambian a menudo
**Evita si:** trabajas sin conexión a internet
**Combina con:** `claude-code`, `cline`, `opencode`
**Alternativas (elige una):** `deepwiki-open`

## `fastmcp`
role=library · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,python

**Qué es:** Convierte funciones Python en herramientas MCP con un decorador y añade autenticación, composición de servidores y cliente de pruebas. Su versión 1 se integró en el SDK oficial.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/PrefectHQ/fastmcp

**Instalación** [+]: `uv add fastmcp`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres crear un servidor MCP en Python rápido
**Evita si:** trabajas en TypeScript; mira `mcp-typescript-sdk`
**Combina con:** `mcp-inspector`, `claude-code`
**Alternativas (elige una):** `mcp-python-sdk`

## `figma-context-mcp`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=mcp · tags=mcp,design,ui,typescript

**Qué es:** Simplifica la respuesta de la API de Figma y da al agente solo lo relevante (estructura, estilos, medidas) para convertir un diseño en código.
**Stack:** TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: El coste depende del proveedor o la ruta. Requiere credenciales y acceso al archivo de Figma. La clave de Figma no es una clave de un LLM.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/GLips/Figma-Context-MCP

**Instalación** [?]: `Seguir la instalación original: https://github.com/GLips/Figma-Context-MCP/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** implementas diseños de Figma con un agente de código
**Evita si:** no usas Figma
**Combina con:** `claude-code`, `ui`, `tailwindcss`

## `free-for-dev`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=recursos,awesome-list,free-for-developers,html

**Qué es:** Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. Agrupa servicios por capacidad para comparar opciones antes de configurar un proyecto.
**Stack:** HTML
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ripienaar/free-for-dev

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas servicios de desarrollo con un nivel gratuito disponible
**Evita si:** una conexión directa cubre el caso sin añadir infraestructura

## `freedomain`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=recursos,digitalplat,dns,dns-tutorial,documentation,domain,domain-platform,domain-registration

**Qué es:** Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. Reúne instrucciones para registrar un dominio, configurar nameservers y conectar un proyecto.
**Stack:** Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/DigitalPlatDev/FreeDomain

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres aprender el flujo de dominios y DNS con sus recursos de referencia
**Evita si:** una conexión directa cubre el caso sin añadir infraestructura

## `github-mcp-server`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=mcp · tags=mcp,code,go

**Qué es:** Conecta asistentes y agentes con la plataforma GitHub: repositorios, issues, pull requests, Actions y seguridad.
**Stack:** Go, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: El coste depende del proveedor o la ruta. Requiere autenticación y permisos de GitHub. La IA que decide las acciones pertenece al cliente MCP.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/github/github-mcp-server

**Instalación** [?]: `Seguir la instalación original: https://github.com/github/github-mcp-server/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente trabaja con GitHub
**Evita si:** usas otra forja como GitLab
**Combina con:** `claude-code`, `codex`

## `langchain-mcp-adapters`
role=library · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,agents,python

**Qué es:** Permite que tus agentes de LangGraph usen cualquier servidor MCP sin escribir adaptadores. El repo está archivado y su función se integró en LangChain.
**Stack:** Python, LangChain
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/langchain-ai/langchain-mcp-adapters

**Instalación** [+]: `pip install langchain-mcp-adapters`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** usas LangGraph y quieres herramientas MCP
**Evita si:** no usas LangChain
**Combina con:** `langgraph`, `langchain`
**Alternativas (elige una):** `mcp-use`

## `masterdnsvpn`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=redes,dns,dns-client,dns-proxy,dns-server,dns-tunnel,dns-tunneling,dnstt

**Qué es:** Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. Coordina cliente y servidor con retransmisión y selección de resolvers para enlaces con restricciones.
**Stack:** Go, Go modules
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/masterking32/MasterDnsVPN

**Instalación** [?]: `Seguir la instalación original: https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar transporte de red sobre DNS en un entorno de pruebas
**Evita si:** una conexión directa cubre el caso sin añadir infraestructura

## `mcp`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=mcp

**Qué es:** Resuelve la fragmentación: cada integración de IA dejaba de ser ad-hoc y pasa a hablar un protocolo común.
**Stack:** TypeScript/Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/google/mcp

**Instalación** [?]: `Seguir la instalación original: https://github.com/google/mcp/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** programas MCP a bajo nivel o necesitas conformidad estricta con la spec
**Evita si:** prefieres un framework de alto nivel que abstraiga el protocolo (mcp-use)
**Combina con:** `mcp-use`, `servers`

## `mcp-for-beginners`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=mcp,learning

**Qué es:** Explica los fundamentos del Model Context Protocol, seguridad y despliegue con ejercicios por lenguaje. Disponible en varios idiomas.
**Stack:** Markdown, Python, TypeScript, C#, Java
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/mcp-for-beginners

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres aprender MCP de forma estructurada
**Evita si:** ya construyes servidores MCP; ve directo a `fastmcp`
**Combina con:** `fastmcp`, `mcp-inspector`

## `mcp-inspector`
role=app · exec=local · setup=easy · mcp=True · prov=— · tags=mcp,evaluation,typescript

**Qué es:** Conéctate a cualquier servidor MCP, lista sus herramientas y recursos y lánzalos a mano para ver respuestas y errores.
**Stack:** TypeScript, React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/modelcontextprotocol/inspector

**Instalación** [+]: `npx @modelcontextprotocol/inspector`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** desarrollas un servidor MCP
**Evita si:** solo usas servidores ya hechos
**Combina con:** `fastmcp`, `mcp-typescript-sdk`

## `mcp-neo4j`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=— · tags=mcp,python

**Qué es:** Resuelve el acceso natural a grafos desde un LLM: el asistente consulta y escribe Cypher sin que tú escribas el glue a mano.
**Stack:** Python, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/neo4j-contrib/mcp-neo4j

**Instalación** [?]: `Seguir la instalación original: https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Neo4j con IA y quieres que el asistente hable Cypher
**Evita si:** no trabajas con grafos o tu base es relacional pura
**Combina con:** `graphrag`, `awesome-mcp-servers`

## `mcp-python-sdk`
role=library · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,python

**Qué es:** Implementación de referencia del protocolo en Python, con la API FastMCP integrada para servidores sencillos.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/modelcontextprotocol/python-sdk

**Instalación** [+]: `pip install "mcp[cli]"`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres el SDK oficial con mínima dependencia
**Evita si:** quieres funciones extra como auth y composición; mira `fastmcp`
**Combina con:** `mcp-inspector`
**Alternativas (elige una):** `fastmcp`

## `mcp-typescript-sdk`
role=library · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,typescript

**Qué es:** Base de la mayoría de servidores MCP en Node.js, con transportes stdio y HTTP.
**Stack:** TypeScript, Node.js, Zod
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/modelcontextprotocol/typescript-sdk

**Instalación** [?]: `Seguir la instalación original: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** creas servidores MCP en TypeScript
**Evita si:** trabajas en Python; mira `fastmcp`
**Combina con:** `mcp-inspector`
**Alternativas (elige una):** `mcp-use`

## `mcp-use`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,mcp,typescript

**Qué es:** Resuelve el salto del SDK base (verboso) a algo productivo: registro de tools, inspector y despliegue incluidos.
**Stack:** TypeScript o Python, React (apps)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mcp-use/mcp-use

**Instalación** [?]: `Seguir la instalación original: https://github.com/mcp-use/mcp-use/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** construyes un servidor MCP propio y quieres productividad
**Evita si:** solo buscas usar uno ya hecho (awesome-mcp-servers) o necesitas control a nivel spec
**Combina con:** `mcp`, `awesome-mcp-servers`
**Alternativas (elige una):** `langchain-mcp-adapters`, `mcp-typescript-sdk`

## `playwright-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,browser,typescript

**Qué es:** Da a tu agente un navegador real controlado por el árbol de accesibilidad, sin depender de capturas. Ideal para pruebas y automatización web.
**Stack:** TypeScript, Playwright
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/playwright-mcp

**Instalación** [+]: `npx @playwright/mcp@latest`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres que tu agente use un navegador real
**Evita si:** necesitas depurar rendimiento y consola; mira `chrome-devtools-mcp`
**Combina con:** `claude-code`, `playwright`
**Alternativas (elige una):** `chrome-devtools-mcp`, `browser-use`, `browser-harness`

## `public-apis`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=mcp,python

**Qué es:** Resuelve el descubrimiento: en un solo lugar tienes URLs, autenticación y HTTPS de cada API en lugar de buscarlas una a una.
**Stack:** Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/public-apis/public-apis

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas datos externos y no sabes qué API usar
**Evita si:** ya tienes tus fuentes definidas o necesitas SLA empresarial (son APIs públicas, sin garantías)
**Combina con:** `n8n`, `firecrawl`

## `serena`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,coding-agent,code,python

**Qué es:** En vez de leer archivos enteros, el agente busca símbolos, referencias y edita a nivel de función usando servidores de lenguaje. Ahorra tokens en repos grandes.
**Stack:** Python, LSP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/oraios/serena

**Instalación** [?]: `Seguir la instalación original: https://github.com/oraios/serena/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente trabaja en un repo grande y gasta muchos tokens leyendo
**Evita si:** tu proyecto es pequeño
**Combina con:** `claude-code`, `codex`
**Alternativas (elige una):** `codegraph`, `gitnexus`

## `servers`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=— · tags=mcp,typescript

**Qué es:** Resuelve la falta de ejemplos canónicos: muestra cómo se construye un servidor MCP correcto, paso a paso.
**Stack:** TypeScript/Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/modelcontextprotocol/servers

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres ejemplos canónicos y plantillas fiables
**Evita si:** buscas soluciones listas para producción (son demos educativas, no hardening)
**Combina con:** `mcp-use`, `awesome-mcp-servers`
