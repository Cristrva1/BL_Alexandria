# Alexandría para agentes · Conectar herramientas con MCP

Categoría 5 completa (27 repos, 3 subcategorías). Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=5 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `fastmcp` | sdk | La forma rápida y pythónica de crear servidores y clientes MCP, con auth… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `mcp-inspector` | sdk | Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. | 1 Básico | 68 | Apache-2.0 (en transición desde MIT) (OSI permisiva) | sin grupo |
| `mcp-use` | sdk | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o… | 2 Intermedio | 64 | MIT (OSI permisiva) | recomendado |
| `mcp-python-sdk` | sdk | SDK oficial de Python para crear servidores y clientes del Model Context… | 2 Intermedio | 62 | MIT (OSI permisiva) | alternativa |
| `mcp-typescript-sdk` | sdk | SDK oficial de TypeScript para crear servidores y clientes del Model Context… | 2 Intermedio | 60 | Apache-2.0 (en transición desde MIT) (OSI permisiva) | alternativa |
| `servers` | servidores | Colección oficial de implementaciones de referencia de servidores MCP mantenida… | 1 Básico | 79 | Apache-2.0 (en transición desde MIT) (OSI permisiva) | sin grupo |
| `context7` | servidores | Servidor MCP que trae documentación actualizada y por versión de librerías al… | 1 Básico | 75 | MIT (OSI permisiva) | sin grupo |
| `chrome-devtools-mcp` | servidores | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red… | 1 Básico | 72 | Apache-2.0 (OSI permisiva) | recomendado |
| `github-mcp-server` | servidores | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen… | 1 Básico | 68 | MIT (OSI permisiva) | sin grupo |
| `ha-mcp` | servidores | Conecta Home Assistant con un asistente mediante MCP para consultar entidades y… | 2 Intermedio | 68 | MIT (OSI permisiva) | sin grupo |
| `unity-mcp` | servidores | Servidor MCP que permite a un asistente operar escenas, scripts y recursos… | 2 Intermedio | 66 | MIT (OSI permisiva) | sin grupo |
| `serena` | servidores | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un… | 1 Básico | 65 | GPL-3.0-or-later (SolidLSP: MIT) (open-core) | sin grupo |
| `mcp-toolbox` | servidores | Servidor MCP de Google para bases de datos: herramientas genéricas listas y un… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `playwright-mcp` | servidores | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar… | 1 Básico | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `aws-mcp` | servidores | Colección oficial de AWS Labs con decenas de servidores MCP para documentación… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | sin grupo |
| `neo4j-mcp` | servidores | Servidor MCP oficial de Neo4j para que un asistente lea el esquema de un grafo… | 2 Intermedio | 60 | GPL-3.0 (OSI copyleft) | recomendado |
| `blender-mcp` | servidores | Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP. | 1 Básico | 59 | MIT (OSI permisiva) | sin grupo |
| `figma-context-mcp` | servidores | Servidor MCP que entrega a los agentes de código el layout de tus diseños de… | 1 Básico | 54 | MIT (OSI permisiva) | sin grupo |
| `mcp-neo4j` | servidores | Servidores experimentales de Neo4j Labs para consultar grafos, memoria y… | 2 Intermedio | 52 | MIT (OSI permisiva) | alternativa |
| `claude-context` | servidores | Permite que asistentes busquen funciones y conceptos por significado en una… | 2 Intermedio | 48 | MIT (OSI permisiva) | sin grupo |
| `ghidramcp` | servidores | Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y… | 2 Intermedio | 42 | Apache-2.0 (OSI permisiva) | sin grupo |
| `annas-mcp` | servidores | Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's… | 2 Intermedio | 27 | — (sin licencia detectada) | sin grupo |
| `public-apis` | directorios | Directorio masivo y muy popular que lista por categorías miles de APIs públicas… | 1 Básico | 73 | MIT (OSI permisiva) | sin grupo |
| `awesome-mcp-servers` | directorios | Directorio curado de la comunidad que cataloga por categorías cientos de… | 1 Básico | 67 | MIT (OSI permisiva) | sin grupo |
| `mcp-for-beginners` | directorios | Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java… | 1 Básico | 59 | MIT (OSI permisiva) | sin grupo |
| `awesome-mcp-clients` | directorios | Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y… | 1 Básico | 42 | MIT (OSI permisiva) | sin grupo |
| `mcp` | directorios | Directorio de servidores MCP oficiales de Google, ejemplos y orientación para… | 1 Básico | 39 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### FastMCP (`fastmcp`)

- **Repo:** https://github.com/PrefectHQ/fastmcp · Apache-2.0 · nivel 2 · 74/100 · recomendado en «SDKs de MCP en Python»
- **Qué es:** Framework Python para construir servidores, clientes y aplicaciones interactivas del Model Context Protocol, hecho por Prefect. Licencia Apache-2.0.
- **Cuándo elegirlo:** Casos: Exponer una función de inventario como herramienta; Probar autenticación de un servidor propio.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python y uv; proyecto de prueba; hardware prerequisites; API de IA: no; Python y uv; proyecto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add fastmcp` — fuente: https://github.com/PrefectHQ/fastmcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Copia la herramienta add del ejemplo y solicita sumar dos números con un cliente MCP Éxito: La herramienta devuelve la suma esperada
- **Combina con:** `claude-code` [20/terminal], `mcp-inspector`, `pydantic-ai` [3/py]
- **Alternativas:** `mcp-python-sdk`
- **Riesgos y avisos:** Alternativas (elige una): mcp-python-sdk. Es un framework para construir servidores y clientes, no un servidor de negocio ya configurado.

### MCP Inspector (`mcp-inspector`)

- **Repo:** https://github.com/modelcontextprotocol/inspector · Apache-2.0 (en transición desde MIT) · nivel 1 · 68/100
- **Qué es:** Herramienta oficial para inspeccionar servidores del Model Context Protocol. El proyecto MCP está pasando de MIT a Apache-2.0 (GitHub muestra NOASSERTION). Es activa (~11k estrellas, 2.15.0).
- **Cuándo elegirlo:** Casos: Depurar un esquema MCP; Reproducir un fallo de una herramienta.
- **Requisitos:** nivel 1: preparación sencilla; Node ^22.23.4 o ^24.22.1 o >=26.12.1; servidor MCP de prueba; hardware prerequisites; API de IA: no; Node ^22.23.4 o ^24.22.1 o >=26.12.1; servidor MCP de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npx @modelcontextprotocol/inspector                   # web UI (default)` — fuente: https://github.com/modelcontextprotocol/inspector/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un servidor local, lista herramientas y llama una con datos ficticios Éxito: Puedes inspeccionar argumentos, respuesta y errores sin un agente de IA
- **Combina con:** `fastmcp`, `mcp-typescript-sdk`, `mcp-python-sdk`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Trata los secretos que guarda como credenciales. Las instrucciones CLAUDE.md del repositorio sirven para contribuir al código; no hacen del Inspector un plugin de Claude Code.

### mcp-use (`mcp-use`)

- **Repo:** https://github.com/mcp-use/mcp-use · MIT · nivel 2 · 64/100 · recomendado en «SDKs de MCP en TypeScript»
- **Qué es:** Framework TypeScript para construir, probar y publicar servidores MCP, plugins de ChatGPT y conectores de Claude, de mcp-use. Licencia MIT. Es activo (~11k estrellas, mcp-use@2.12.4).
- **Cuándo elegirlo:** Casos: Construir una herramienta con interfaz embebida; Desplegar un servidor MCP para una app propia.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node.js; plantilla elegida; Python solo para su ruta correspondiente; hardware prerequisites; API de IA: opcional; Node.js; plantilla elegida; Python solo para su ruta correspondiente.
- **Instalación (documentada en la fuente; no ejecutada):** `npx -y create-mcp-use-app@latest` — fuente: https://github.com/mcp-use/mcp-use/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera una app MCP de ejemplo y prueba su herramienta desde el inspector incluido Éxito: Puedes ver una respuesta y la interfaz asociada si el cliente admite MCP Apps
- **Combina con:** `claude-code` [20/terminal], `awesome-mcp-servers` [5/directorios], `mcp` [5/directorios], `servers` [5/servidores]
- **Alternativas:** `mcp-typescript-sdk`
- **Riesgos y avisos:** Alternativas (elige una): mcp-typescript-sdk. MCP Apps con widgets requiere capacidades del cliente adicionales a las de un servidor MCP de texto.

### MCP Python SDK (`mcp-python-sdk`)

- **Repo:** https://github.com/modelcontextprotocol/python-sdk · MIT · nivel 2 · 62/100 · alternativa en «SDKs de MCP en Python»
- **Qué es:** SDK oficial en Python del Model Context Protocol. Licencia MIT (el proyecto MCP está migrando a Apache-2.0). Es muy usado (~25k estrellas, v2.3.0).
- **Cuándo elegirlo:** Casos: Conectar una función Python a MCP; Servir un recurso de texto desde una aplicación.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python 3.11+; uv; directorio de proyecto; hardware prerequisites; API de IA: no; Python 3.11+; uv; directorio de proyecto.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add "mcp[cli]"      # or: pip install "mcp[cli]"` — fuente: https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Implementa el servidor add del ejemplo y comprueba su esquema con Inspector Éxito: Una llamada con dos enteros devuelve su suma
- **Combina con:** `mcp-inspector`, `pydantic-ai` [3/py], `claude-code` [20/terminal], `mcp-for-beginners` [5/directorios]
- **Alternativas:** `fastmcp`
- **Riesgos y avisos:** Alternativas (elige una): fastmcp. La documentación revisada usa MCPServer y ofrece migración v2; no confundas este SDK con FastMCP independiente.

### MCP TypeScript SDK (`mcp-typescript-sdk`)

- **Repo:** https://github.com/modelcontextprotocol/typescript-sdk · Apache-2.0 (en transición desde MIT) · nivel 2 · 60/100 · alternativa en «SDKs de MCP en TypeScript»
- **Qué es:** SDK oficial en TypeScript del Model Context Protocol. La rama principal es la v2 estable (v2.4.0), que implementa la especificación MCP 2026-07-28.
- **Cuándo elegirlo:** Casos: Construir un servidor MCP en TypeScript; Crear un cliente que enumere herramientas.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node.js; TypeScript; gestor de paquetes; hardware prerequisites; API de IA: no; Node.js; TypeScript; gestor de paquetes.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @modelcontextprotocol/server` — fuente: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el ejemplo v2 para exponer una herramienta y llámala desde Inspector Éxito: Ves el esquema y una respuesta válida de la herramienta
- **Combina con:** `mcp-inspector`, `vercel-ai` [3/ts], `claude-code` [20/terminal]
- **Alternativas:** `mcp-use`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): mcp-use. La rama revisada es v2 con paquetes server y client separados; no mezcles imports de tutoriales v1.

### servers (`servers`)

- **Repo:** https://github.com/modelcontextprotocol/servers · Apache-2.0 (en transición desde MIT) · nivel 1 · 79/100
- **Qué es:** Repositorio oficial de servidores de referencia del Model Context Protocol. El proyecto MCP está pasando de MIT a Apache-2.0 (GitHub muestra NOASSERTION). Es muy popular (~92k estrellas, v2.4.0).
- **Cuándo elegirlo:** Casos: Aprender cómo se implementa memoria MCP; Estudiar acceso a un repositorio Git de prueba.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; Node o Python según el servidor elegido; hardware prerequisites; API de IA: no; Navegador; Node o Python según el servidor elegido.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/modelcontextprotocol/servers/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige un servidor de referencia y comprueba sus permisos sobre datos ficticios Éxito: Entiendes qué herramientas expone y qué datos puede modificar
- **Combina con:** `mcp-inspector` [5/sdk], `mcp-use` [5/sdk], `awesome-mcp-servers` [5/directorios], `opendots` [21/asistentes]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. No son para producción, según el propio README. Los autores los presentan como implementaciones educativas de referencia, no servicios listos para producción.

### Context7 (`context7`)

- **Repo:** https://github.com/upstash/context7 · MIT · nivel 1 · 75/100
- **Qué es:** Context7, servicio de Upstash que da a los agentes documentación actualizada y ejemplos de código de librerías. Licencia MIT para el repo; el servicio es alojado y requiere clave. Es muy popular (~65k estrellas).
- **Cuándo elegirlo:** Casos: Consultar APIs recientes durante programación; Evitar mezclar instrucciones de versiones distintas.
- **Requisitos:** nivel 1: preparación sencilla; Node.js >=22.13; cliente MCP; clave Context7 recomendada; hardware prerequisites; API de IA: no; Node.js >=22.13; cliente MCP; clave Context7 recomendada.
- **Instalación (documentada en la fuente; no ejecutada):** `npx ctx7 setup` — fuente: https://github.com/upstash/context7/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Pide documentación de una versión concreta y contrasta el ejemplo devuelto con la fuente Éxito: El agente identifica la biblioteca y la versión consultada
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `cline` [20/editor]
- **Riesgos y avisos:** Sin alternativas declaradas. Las consultas salen hacia el servicio de Upstash. Conectar documentación actual no acredita que todo ejemplo sea válido para la versión instalada en tu proyecto.

### Chrome DevTools MCP (`chrome-devtools-mcp`)

- **Repo:** https://github.com/ChromeDevTools/chrome-devtools-mcp · Apache-2.0 · nivel 1 · 72/100 · recomendado en «Servidores MCP de navegador»
- **Qué es:** Chrome DevTools para agentes: servidor MCP y CLI del equipo de Chrome DevTools para controlar e inspeccionar un Chrome real. Licencia Apache-2.0. Es muy popular (~57k estrellas, v1.13.0).
- **Cuándo elegirlo:** Casos: Diagnosticar una pantalla que falla; Inspeccionar rendimiento de una página propia.
- **Requisitos:** nivel 1: preparación sencilla; Node.js LTS; npm; Chrome estable; cliente MCP; hardware prerequisites; API de IA: no; Node.js LTS; npm; Chrome estable; cliente MCP.
- **Instalación (documentada en la fuente; no ejecutada):** `/plugin marketplace add ChromeDevTools/chrome-devtools-mcp` — fuente: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre tu app local y pide revisar errores de consola y una petición de red Éxito: El informe identifica el error y la petición que puedes reproducir
- **Combina con:** `claude-code` [20/terminal], `gemini-cli` [20/terminal], `mcp-inspector` [5/sdk], `puppeteer` [32/bibliotecas], `agent-browser` [32/agentes-web], `awesome-chrome-devtools` [32/recursos-web]
- **Alternativas:** `playwright-mcp`, `browser-harness`
- **Riesgos y avisos:** Alternativas (elige una): playwright-mcp, browser-harness. Telemetría activada por defecto. MCP y CLI con skill son rutas diferentes; la recogida de métricas tiene una opción de exclusión documentada.

### GitHub MCP Server (`github-mcp-server`)

- **Repo:** https://github.com/github/github-mcp-server · MIT · nivel 1 · 68/100
- **Qué es:** Servidor MCP oficial de GitHub que conecta herramientas de IA con la plataforma. Licencia MIT. Es muy activo (~35k estrellas, v2.1.0).
- **Cuándo elegirlo:** Casos: Explorar una base de código; Revisar el estado de una pull request.
- **Requisitos:** nivel 1: preparación sencilla; Cuenta GitHub; cliente MCP; token con permisos adecuados o autenticación remota; hardware prerequisites; API de IA: no; Cuenta GitHub; cliente MCP; token con permisos adecuados o autenticación remota.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/github/github-mcp-server/blob/main/README.md

  ```text
  claude mcp add github -e GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_PAT -- docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server
  ```
- **Primera prueba propuesta (no ejecutada):** Lista archivos y lee un README de un repositorio público antes de habilitar herramientas de escritura Éxito: El agente devuelve contenidos y enlaces del repositorio elegido
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `strix` [16/agentes], `agentes-chat` [21/asistentes], `awesome-copilot` [2/catalogos], `cli` [7/herramientas]
- **Riesgos y avisos:** Sin alternativas declaradas. Usa el modo de solo lectura cuando no necesites escribir. Empieza con el conjunto de herramientas y permisos de lectura necesario; no copies tokens de ejemplo como credenciales reales.

### Home Assistant MCP (`ha-mcp`)

- **Repo:** https://github.com/homeassistant-ai/ha-mcp · MIT · nivel 2 · 68/100
- **Qué es:** Conecta Home Assistant con un asistente mediante MCP para consultar entidades y trabajar con automatizaciones de domótica.
- **Cuándo elegirlo:** Casos: Consultar qué sensores aparecen en el demo.; Revisar como borrador la automatización de una luz virtual. Evítalo si necesitas un producto autónomo y esta pieza requiere un cliente MCP.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: no; Home Assistant compatible o el demo oficial, y un cliente MCP de prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://homeassistant-ai.github.io/ha-mcp/
- **Primera prueba propuesta (no ejecutada):** Inicia con el demo y pide una consulta sin cambios sobre una entidad ficticia. Éxito: La herramienta devuelve el estado de la entidad sin accionar dispositivos.
- **Combina con:** `home-assistant` [15/domotica]
- **Riesgos y avisos:** Hay avisos públicos: el release revisado v9.2.0 es posterior a los pisos publicados para el paquete.

### unity-mcp (`unity-mcp`)

- **Repo:** https://github.com/CoplayDev/unity-mcp · MIT · nivel 2 · 66/100
- **Qué es:** MCP for Unity, puente entre asistentes de IA y el editor de Unity, de Coplay (patrocinado y mantenido por Aura). Licencia MIT. Es activo (~16k estrellas, v10.3.0).
- **Cuándo elegirlo:** Casos: Bocetar escenas de una demo; Ejecutar pruebas del proyecto desde un agente.
- **Requisitos:** nivel 2: preparación media; Unity 2021.3 LTS a 6.x; Python 3.10+ mediante uv; cliente MCP; hardware prerequisites; API de IA: no; Unity 2021.3 LTS a 6.x; Python 3.10+ mediante uv; cliente MCP.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/CoplayDev/unity-mcp/blob/beta/README.md
- **Primera prueba propuesta (no ejecutada):** En un proyecto vacío pide crear un cubo en el origen con un Rigidbody Éxito: El cubo aparece y puedes inspeccionar el componente en Unity
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `blender` [26/creacion-3d], `blender-mcp`
- **Riesgos y avisos:** Sin alternativas declaradas. Usa control de versiones: el agente puede modificar escenas y scripts. Instala el paquete desde Package Manager y configura el cliente; guarda una copia del proyecto antes de automatizar ediciones.

### Serena (`serena`)

- **Repo:** https://github.com/oraios/serena · GPL-3.0-or-later (SolidLSP: MIT) · nivel 1 · 65/100
- **Qué es:** Serena, un kit de herramientas de código semántico para agentes («el IDE de tu agente»), de Oraios AI. La aplicación es GPL-3.0-or-later y el componente SolidLSP es MIT (GitHub muestra NOASSERTION). Es muy activa (~31k estrellas, v2.1.0).
- **Cuándo elegirlo:** Casos: Navegar una base de código grande; Refactorizar un símbolo con contexto semántico.
- **Requisitos:** nivel 1: preparación sencilla; uv; servidor de lenguaje del proyecto; repositorio de prueba; hardware prerequisites; API de IA: no; uv; servidor de lenguaje del proyecto; repositorio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install -p 3.13 serena-agent` — fuente: https://github.com/oraios/serena/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Pide localizar una función por símbolo y enumera sus referencias antes de editar Éxito: El agente identifica la definición y usos reales
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `context7`, `superclaude-framework` [2/metodologia]
- **Alternativas:** `codegraph`, `gitnexus`, `codebase-memory-mcp`, `graphify`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): codegraph, gitnexus, codebase-memory-mcp, graphify. El autor desaconseja marketplaces con instalaciones antiguas; configura el comando de lanzamiento oficial y el backend adecuado.

### MCP Toolbox for Databases (`mcp-toolbox`)

- **Repo:** https://github.com/googleapis/mcp-toolbox · Apache-2.0 · nivel 2 · 64/100
- **Qué es:** Servidor MCP de código abierto (Apache-2.0) mantenido por Google (organización googleapis). El repositorio se llamaba genai-toolbox y se renombró a mcp-toolbox; publica versiones frecuentes y SDK oficiales.
- **Cuándo elegirlo:** Casos: consultar y explorar el esquema de una base PostgreSQL desde tu agente de código; dar a un agente en producción consultas parametrizadas en lugar de SQL libre. Evítalo si necesitas un producto autónomo y esta pieza requiere un cliente MCP.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Go, Dockerfile, go.mod; API de IA: no; Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta..
- **Instalación (documentada en la fuente; no ejecutada):** `brew install mcp-toolbox` — fuente: https://github.com/googleapis/mcp-toolbox/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Prepara un tools.yaml contra una base de prueba, arranca el servidor y regístralo en tu cliente MCP. Éxito: El cliente lista las herramientas y una consulta de solo lectura devuelve filas de la base de prueba.
- **Combina con:** `claude-code` [20/terminal], `gemini-cli` [20/terminal], `codex` [20/terminal], `langchain` [3/py], `llama-index` [3/py]
- **Riesgos y avisos:** Usa credenciales de solo lectura en las primeras pruebas: las herramientas genéricas pueden ejecutar SQL arbitrario.

### Playwright MCP (`playwright-mcp`)

- **Repo:** https://github.com/microsoft/playwright-mcp · Apache-2.0 · nivel 1 · 63/100 · alternativa en «Servidores MCP de navegador»
- **Qué es:** Servidor MCP oficial de Microsoft que da a los LLM automatización de navegador con Playwright. Licencia Apache-2.0. Es muy popular y activo (~40k estrellas, v0.0.85, aún 0.x).
- **Cuándo elegirlo:** Casos: Probar una navegación de tu app; Inspeccionar un formulario de desarrollo.
- **Requisitos:** nivel 1: preparación sencilla; Node.js; npm; cliente MCP; navegador de prueba; hardware prerequisites; API de IA: no; Node.js; npm; cliente MCP; navegador de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `claude mcp add playwright npx @playwright/mcp@latest` — fuente: https://github.com/microsoft/playwright-mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre una página local con un formulario ficticio y comprueba sus campos antes de rellenarla Éxito: La instantánea accesible identifica campos y el resultado de la acción
- **Combina con:** `claude-code` [20/terminal], `playwright` [32/bibliotecas], `mcp-inspector` [5/sdk]
- **Alternativas:** `chrome-devtools-mcp`, `browser-use`, `browser-harness`
- **Riesgos y avisos:** Alternativas (elige una): chrome-devtools-mcp, browser-use, browser-harness. El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies.

### MCP servers for AWS (`aws-mcp`)

- **Repo:** https://github.com/awslabs/mcp · Apache-2.0 · nivel 2 · 60/100
- **Qué es:** Conjunto de servidores MCP de código abierto (Apache-2.0) publicado por AWS Labs. Muy activo; desde mayo de 2026 AWS recomienda para producción el Agent Toolkit for AWS, presentado como sucesor, aunque este repositorio sigue funcionando y…
- **Cuándo elegirlo:** Casos: consultar la documentación actualizada de AWS desde tu agente de código; revisar y generar plantillas de CloudFormation o CDK con validación de seguridad. Evítalo si necesitas un producto autónomo y esta pieza requiere un cliente MCP.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python; API de IA: no; Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta..
- **Instalación (documentada en la fuente; no ejecutada):** `claude mcp add aws-api uvx awslabs.aws-api-mcp-server@latest` — fuente: https://github.com/awslabs/mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura el servidor de documentación de AWS con uvx en tu cliente MCP y pregunta por un servicio concreto. Éxito: El agente devuelve fragmentos de la documentación oficial con su enlace.
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `mcp-inspector` [5/sdk]
- **Riesgos y avisos:** Empieza por servidores de solo lectura (documentación) y usa permisos IAM mínimos. Para producción, AWS recomienda el Agent Toolkit for AWS.

### Neo4j MCP (oficial) (`neo4j-mcp`)

- **Repo:** https://github.com/neo4j/mcp · GPL-3.0 · nivel 2 · 60/100 · recomendado en «Servidores MCP de Neo4j»
- **Qué es:** Servidor MCP oficial de Neo4j (organización neo4j, Neo4j Sweden AB), escrito en Go. Licencia GPL-3.0 según LICENSE.txt y NOTICE.txt (GitHub muestra NOASSERTION); si se usa con Aura o con las ediciones comerciales de Neo4j, pasa a regirse…
- **Cuándo elegirlo:** Casos: Preguntar en lenguaje natural por el esquema de un grafo de prueba; Consultar relaciones con Cypher de solo lectura desde el agente. Evítalo si necesitas un producto autónomo y esta pieza requiere un cliente MCP y una base Neo4j.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Go, Dockerfile, go.mod; hardware prerequisites; API de IA: no; Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install neo4j-mcp-server` — fuente: https://github.com/neo4j/mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta el servidor en modo solo lectura a una base Neo4j de prueba y pide al agente que describa su esquema Éxito: El agente lista etiquetas y relaciones que coinciden con las de la base
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `graphiti` [6/memoria], `cognee` [6/memoria]
- **Alternativas:** `mcp-neo4j`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativa (elige una): mcp-neo4j. Es el servidor oficial; mcp-neo4j son los servidores experimentales de Neo4j Labs.

### Blender MCP (`blender-mcp`)

- **Repo:** https://github.com/ahujasid/mcp-for-blender · MIT · nivel 1 · 59/100
- **Qué es:** MCP for Blender (antes blender-mcp), integración de terceros que conecta Blender con cualquier LLM, creada por @ahujasid. Licencia MIT. Es muy popular (~35k estrellas) y no está hecha por la Blender Foundation; el paquete PyPI pasó a…
- **Cuándo elegirlo:** Casos: Bocetar una escena 3D; Automatizar ajustes de objetos y materiales.
- **Requisitos:** nivel 1: preparación sencilla; Blender >=3; uv; cliente MCP; escena de prueba; hardware prerequisites; API de IA: opcional; Blender >=3; uv; cliente MCP; escena de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ahujasid/mcp-for-blender/blob/main/README.md

  ```powershell
  winget install --id=astral-sh.uv -e
  uvx mcp-for-blender setup
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un cubo y cambia su material en una escena vacía Éxito: Puedes ver el objeto y el material en Blender
- **Combina con:** `claude-code` [20/terminal], `blender` [26/creacion-3d], `unity-mcp`, `blender-skills` [27/skills], `dream-loop` [27/skills], `chatdev` [3/py]
- **Riesgos y avisos:** Sin alternativas declaradas. Revisa los ajustes de telemetría y el uso de servicios 3D de terceros. El paquete actual es mcp-for-blender; plugin comunitario sin afiliación con Blender Foundation.

### Figma Context MCP (`figma-context-mcp`)

- **Repo:** https://github.com/GLips/Figma-Context-MCP · MIT · nivel 1 · 54/100
- **Qué es:** Framelink MCP for Figma, servidor que da a los agentes de programación acceso a los datos de Figma, de @GLips. Licencia MIT. Es popular (~16k estrellas, v0.13.2).
- **Cuándo elegirlo:** Casos: Implementar una tarjeta a partir de un diseño; Consultar tipografía y espaciado de una pantalla.
- **Requisitos:** nivel 1: preparación sencilla; Node.js; token Figma; archivo de diseño accesible; cliente MCP; hardware prerequisites; API de IA: no; Node.js; token Figma; archivo de diseño accesible; cliente MCP.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/GLips/Figma-Context-MCP/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Solicita los datos de un frame pequeño y compara dimensiones y textos con Figma Éxito: El agente obtiene información del frame correcto
- **Combina con:** `claude-code` [20/terminal], `ui` [9/componentes], `tailwindcss` [9/estilos], `design-dna` [27/skills]
- **Riesgos y avisos:** Sin alternativas declaradas. El token de Figma da acceso a tus archivos: guárdalo como secreto. La configuración Windows utiliza un lanzador distinto; el token Figma no es una clave de IA.

### mcp-neo4j (`mcp-neo4j`)

- **Repo:** https://github.com/neo4j-contrib/mcp-neo4j · MIT · nivel 2 · 52/100 · alternativa en «Servidores MCP de Neo4j»
- **Qué es:** Servidores MCP de Neo4j Labs, mantenidos por el equipo Field GenAI de Neo4j. Licencia MIT. Son experimentales (~1k estrellas, mcp-neo4j-cypher-v0.6.0) y el README remite al servidor MCP oficial de producto (neo4j/mcp).
- **Cuándo elegirlo:** Casos: Consultar relaciones en un grafo; Estudiar memoria de entidades entre sesiones.
- **Requisitos:** nivel 2: preparación media; Neo4j; credenciales; APOC para inspección de esquema; servidor elegido; hardware prerequisites; API de IA: no; Neo4j; credenciales; APOC para inspección de esquema; servidor elegido.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta el esquema de un grafo ficticio y revisa una consulta Cypher de lectura Éxito: Obtienes etiquetas y relaciones que coinciden con la base de prueba
- **Combina con:** `claude-code` [20/terminal], `graphrag` [6/rag], `graphiti` [6/memoria]
- **Alternativas:** `neo4j-mcp`
- **Riesgos y avisos:** Alternativa (elige una): neo4j-mcp. Para producción, valora el servidor oficial neo4j/mcp (neo4j-mcp). El servidor Cypher puede escribir: limita permisos. Son servidores Neo4j Labs experimentales sin SLA del equipo de producto; el producto oficial Neo4j MCP es otro repositorio.

### Claude Context (`claude-context`)

- **Repo:** https://github.com/zilliztech/claude-context · MIT · nivel 2 · 48/100
- **Qué es:** Permite que asistentes busquen funciones y conceptos por significado en una base de código a través de un conector MCP.
- **Cuándo elegirlo:** Casos: Encontrar archivos relacionados con la autenticación en un proyecto de ejemplo.; Indexar una biblioteca ficticia y comprobar qué resultado devuelve por función. Evítalo si necesitas un producto autónomo y esta pieza requiere un cliente MCP.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP), requiere clave de API; TypeScript, package.json; API de IA: sí; Node.js 20+, un cliente MCP, base vectorial y una configuración de embeddings según el proveedor escogido..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/zilliztech/claude-context/blob/64a87f9b31b0c983f731c91242322562ffd91c7d/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un índice de prueba sobre código público e intenta encontrar una función conocida. Éxito: La búsqueda devuelve el archivo y fragmento esperado, y puedes comprobar el proveedor de embeddings utilizado.
- **Riesgos y avisos:** Los embeddings y almacenamiento pueden ser servicios externos. La cuenta del cliente no cubre esos cargos; no enviar código sensible sin revisar destino y….

### GhidraMCP (`ghidramcp`)

- **Repo:** https://github.com/LaurieWired/GhidraMCP · Apache-2.0 · nivel 2 · 42/100
- **Qué es:** GhidraMCP, servidor MCP y plugin que permite a los LLM hacer ingeniería inversa autónoma con Ghidra, de @LaurieWired. Licencia Apache-2.0. Es popular (~12k estrellas, versión 2.0).
- **Cuándo elegirlo:** Casos: Documentar funciones de un binario propio; Estudiar llamadas en un ejecutable de laboratorio.
- **Requisitos:** nivel 2: preparación media; Ghidra y su plugin; uv; binario propio de prueba; hardware prerequisites; API de IA: no; Ghidra y su plugin; uv; binario propio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP ghidra-mcp --ghidra-server http://127.0.0.1:8080/` — fuente: https://github.com/LaurieWired/GhidraMCP/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Carga un programa de prueba y pide enumerar funciones sin modificar el análisis Éxito: Obtienes nombres y ubicaciones verificables en Ghidra
- **Combina con:** `ghidra` [16/reversing], `claude-code` [20/terminal], `angr` [16/reversing], `awesome-ai-reverse-engineering` [16/referencias]
- **Riesgos y avisos:** Sin alternativas declaradas. Analiza solo software que tengas derecho a analizar. La integración de los clientes se basa en stdio o HTTP documentados; esta revisión no prueba su instalación ni el análisis de binarios.

### annas-mcp (`annas-mcp`)

- **Repo:** https://github.com/iosifache/annas-mcp · — · nivel 2 · 27/100
- **Qué es:** Servidor MCP y CLI para buscar y descargar libros y artículos de Anna's Archive, de @iosifache. El repo no tiene licencia en GitHub. Es pequeño (~1k estrellas, v0.1) y su último cambio es de junio de 2026.
- **Cuándo elegirlo:** Casos: Localizar un documento de dominio público; Estudiar una interfaz de búsqueda documental MCP.
- **Requisitos:** nivel 2: preparación media; Binario oficial para tu sistema; cliente MCP; clave solo para descargas; hardware prerequisites; API de IA: no; Binario oficial para tu sistema; cliente MCP; clave solo para descargas.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/iosifache/annas-mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Busca un documento que puedas utilizar legalmente y revisa los metadatos antes de descargar Éxito: La búsqueda muestra título y origen sin necesitar clave de descarga
- **Combina con:** `claude-code` [20/terminal], `markitdown` [13/conversion], `docling` [13/conversion]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo legal: descargar obras protegidas puede infringir derechos de autor según tu país. Sin licencia declarada. Configura la ruta absoluta del binario y del directorio de descargas; la herramienta no concede derechos sobre los documentos.

### public-apis (`public-apis`)

- **Repo:** https://github.com/public-apis/public-apis · MIT · nivel 1 · 73/100
- **Qué es:** Lista colectiva de APIs gratuitas para software y desarrollo web. Licencia MIT. Es uno de los repos más populares de GitHub (~499k estrellas) y está patrocinado por APILayer, cuyo anuncio encabeza el README.
- **Cuándo elegirlo:** Casos: Encontrar datos de clima para una demo; Comparar APIs públicas de geocodificación.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; necesidad concreta de datos; hardware prerequisites; API de IA: no; Navegador; necesidad concreta de datos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/public-apis/public-apis/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una API y verifica autenticación, HTTPS, límites y licencia en su sitio oficial Éxito: Sabes qué datos devuelve y si podrás usarlos en tu proyecto
- **Combina con:** `activepieces` [1/motores], `firecrawl` [4/crawlers], `claude-code` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Parte del contenido destacado es publicidad del patrocinador. El nombre CodeX de un compilador enlazado no es OpenAI Codex; no hereda compatibilidad con agentes.

### awesome-mcp-servers (`awesome-mcp-servers`)

- **Repo:** https://github.com/punkpeye/awesome-mcp-servers · MIT · nivel 1 · 67/100
- **Qué es:** Lista curada de servidores MCP de @punkpeye (vinculada a Glama). Licencia MIT. Es muy popular (~98k estrellas) y su README empieza con un anuncio.
- **Cuándo elegirlo:** Casos: Buscar una conexión a archivos propios; Encontrar un servidor para una base de datos.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; cliente y tarea elegidos; hardware prerequisites; API de IA: no; Navegador; cliente y tarea elegidos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/punkpeye/awesome-mcp-servers/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Filtra por función y sistema operativo y contrasta el README de dos servidores Éxito: Tienes dos candidatos con transporte, permisos y credenciales identificados
- **Combina con:** `awesome-mcp-clients`, `servers` [5/servidores], `mcp-use` [5/sdk]
- **Riesgos y avisos:** Sin alternativas declaradas. Lista sin auditoría de seguridad. Es un directorio comunitario; sus enlaces y etiquetas no equivalen a una auditoría ni a compatibilidad uniforme.

### MCP for Beginners (`mcp-for-beginners`)

- **Repo:** https://github.com/microsoft/mcp-for-beginners · MIT · nivel 1 · 59/100
- **Qué es:** Curso de Microsoft para aprender Model Context Protocol con ejemplos prácticos en C#, Java, JavaScript, Rust, Python y TypeScript. Licencia MIT. Es popular (~18k estrellas, sin releases) y tiene más de 50 traducciones automáticas.
- **Cuándo elegirlo:** Casos: Aprender conceptos MCP desde cero; Comparar un servidor Python con otro TypeScript.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; lenguaje elegido para los ejercicios; hardware prerequisites; API de IA: no; Navegador; lenguaje elegido para los ejercicios.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/microsoft/mcp-for-beginners.git` — fuente: https://github.com/microsoft/mcp-for-beginners/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee la introducción y completa un ejercicio de herramienta con entrada y salida pequeñas Éxito: Puedes explicar el papel del host, cliente y servidor
- **Combina con:** `mcp-python-sdk` [5/sdk], `fastmcp` [5/sdk], `mcp-inspector` [5/sdk], `ai-agents-for-beginners` [19/guias], `generative-ai-for-beginners` [19/guias]
- **Riesgos y avisos:** Sin alternativas declaradas. No necesitas ejecutar todos los lenguajes ni desplegar todos los ejemplos para empezar.

### Awesome MCP Clients (`awesome-mcp-clients`)

- **Repo:** https://github.com/punkpeye/awesome-mcp-clients · MIT · nivel 1 · 42/100
- **Qué es:** Lista curada de clientes MCP de @punkpeye. Licencia MIT. Es pequeña (~7k estrellas) y poco activa (último cambio en junio de 2026); el propio README remite a glama.ai/mcp/clients para la lista más actual.
- **Cuándo elegirlo:** Casos: Encontrar una interfaz para herramientas MCP; Comparar clientes con modelos locales.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; preferencias de sistema y modelo; hardware prerequisites; API de IA: no; Navegador; preferencias de sistema y modelo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/punkpeye/awesome-mcp-clients/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Compara dos clientes por transportes MCP, autenticación y modelos admitidos Éxito: Puedes elegir un cliente cuyo sistema y conexiones encajen con tu caso
- **Combina con:** `awesome-mcp-servers`, `claude-code` [20/terminal], `cline` [20/editor]
- **Riesgos y avisos:** Sin alternativas declaradas. Posiblemente desactualizada frente a Glama. Un cliente descrito como basado en Claude Code no es necesariamente el producto oficial ni comparte sus condiciones.

### Google MCP (`mcp`)

- **Repo:** https://github.com/google/mcp · Apache-2.0 · nivel 1 · 39/100
- **Qué es:** Repositorio de Google con la lista de sus servidores MCP oficiales, guías para desplegar servidores en Google Cloud y ejemplos. Licencia Apache-2.0. Es pequeño (~5k estrellas) y su último cambio es de agosto de 2026.
- **Cuándo elegirlo:** Casos: Conectar un servicio Google a un agente; Aprender a alojar un servidor MCP en Cloud Run.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; servicio Google objetivo; hardware prerequisites; API de IA: no; Navegador; servicio Google objetivo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/google/mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige un servidor oficial Google y consulta su autenticación antes de desplegar Éxito: Distingues servicio gestionado, ejemplo y despliegue en Cloud Run
- **Combina con:** `gemini-cli` [20/terminal], `mcp-use` [5/sdk], `mcp-inspector` [5/sdk]
- **Riesgos y avisos:** Sin alternativas declaradas. Cuidado con los permisos IAM que concedes a agentes. Este repositorio es google/mcp: catálogo y ejemplos Google, no el núcleo de la especificación Model Context Protocol.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-5.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Conectar herramientas con MCP», lee `docs/alexandria/categoria-5.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-5.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
