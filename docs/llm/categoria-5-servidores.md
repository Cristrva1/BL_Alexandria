# Alexandría para agentes · Servidores MCP destacados

Categoría 5 «Conectar herramientas con MCP» › subcategoría `servidores`. 17 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=5&sub=servidores · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `servers` | Colección oficial de implementaciones de referencia de servidores MCP mantenida… | 1 Básico | 79 | Apache-2.0 (en transición desde MIT) (OSI permisiva) | sin grupo |
| `context7` | Servidor MCP que trae documentación actualizada y por versión de librerías al… | 1 Básico | 75 | MIT (OSI permisiva) | sin grupo |
| `chrome-devtools-mcp` | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red… | 1 Básico | 72 | Apache-2.0 (OSI permisiva) | recomendado |
| `github-mcp-server` | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen… | 1 Básico | 68 | MIT (OSI permisiva) | sin grupo |
| `ha-mcp` | Conecta Home Assistant con un asistente mediante MCP para consultar entidades y… | 2 Intermedio | 68 | MIT (OSI permisiva) | sin grupo |
| `unity-mcp` | Servidor MCP que permite a un asistente operar escenas, scripts y recursos… | 2 Intermedio | 66 | MIT (OSI permisiva) | sin grupo |
| `serena` | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un… | 1 Básico | 65 | GPL-3.0-or-later (SolidLSP: MIT) (open-core) | sin grupo |
| `mcp-toolbox` | Servidor MCP de Google para bases de datos: herramientas genéricas listas y un… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `playwright-mcp` | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar… | 1 Básico | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `aws-mcp` | Colección oficial de AWS Labs con decenas de servidores MCP para documentación… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | sin grupo |
| `neo4j-mcp` | Servidor MCP oficial de Neo4j para que un asistente lea el esquema de un grafo… | 2 Intermedio | 60 | GPL-3.0 (OSI copyleft) | recomendado |
| `blender-mcp` | Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP. | 1 Básico | 59 | MIT (OSI permisiva) | sin grupo |
| `figma-context-mcp` | Servidor MCP que entrega a los agentes de código el layout de tus diseños de… | 1 Básico | 54 | MIT (OSI permisiva) | sin grupo |
| `mcp-neo4j` | Servidores experimentales de Neo4j Labs para consultar grafos, memoria y… | 2 Intermedio | 52 | MIT (OSI permisiva) | alternativa |
| `claude-context` | Permite que asistentes busquen funciones y conceptos por significado en una… | 2 Intermedio | 48 | MIT (OSI permisiva) | sin grupo |
| `ghidramcp` | Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y… | 2 Intermedio | 42 | Apache-2.0 (OSI permisiva) | sin grupo |
| `annas-mcp` | Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's… | 2 Intermedio | 27 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-5-servidores.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Servidores MCP destacados», lee `docs/alexandria/categoria-5-servidores.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-5-servidores.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
