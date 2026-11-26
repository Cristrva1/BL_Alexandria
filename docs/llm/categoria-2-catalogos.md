# Alexandría para agentes · Catálogos y marketplaces de skills

Categoría 2 «Skills, plugins y métodos para agentes» › subcategoría `catalogos`. 15 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=2&sub=catalogos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `antigravity-awesome-skills` | Biblioteca de skills para varios agentes con selección revisable y distribución… | 1 Básico | 68 | MIT (OSI permisiva) | recomendado |
| `awesome-copilot` | Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y… | 1 Básico | 68 | MIT (OSI permisiva) | sin grupo |
| `claude-plugins-official` | Marketplace oficial de Anthropic con plugins para ampliar las herramientas y… | 1 Básico | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `claude-code-templates` | Reúne componentes para Claude Code con buscador, entre ellos skills, agentes… | 1 Básico | 61 | MIT (OSI permisiva) | sin grupo |
| `google-skills` | Colección de skills para trabajar con productos y tecnologías de Google desde… | 2 Intermedio | 59 | Apache-2.0 (OSI permisiva) | sin grupo |
| `gemini-skills` | Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK… | 1 Básico | 55 | Apache-2.0 (OSI permisiva) | sin grupo |
| `awesome-agent-skills` | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel… | 1 Básico | 54 | MIT (OSI permisiva) | alternativa |
| `anthropic-skills` | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de… | 1 Básico | 52 | — (sin licencia detectada) | sin grupo |
| `awesome-claude-code-subagents` | Reúne perfiles especializados para Claude Code que puedes leer y comparar antes… | 1 Básico | 52 | MIT (OSI permisiva) | sin grupo |
| `wshobson-agents` | Colección de plugins, agentes y skills con adaptadores documentados para Claude… | 1 Básico | 51 | MIT (OSI permisiva) | alternativa |
| `awesome-claude-code` | Lista curada de recursos para Claude Code: skills, plugins, hooks, status… | 1 Básico | 48 | CC-BY-NC-ND-4.0 (source-available) | alternativa |
| `awesome-claude-skills` | Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros… | 1 Básico | 48 | — (sin licencia detectada) | alternativa |
| `plugins` | Especificación y colección oficial de plugins de Cursor para estudiar e… | 1 Básico | 48 | — (sin licencia detectada) | sin grupo |
| `autoskills` | CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un… | 1 Básico | 40 | CC-BY-NC-4.0 (source-available) | sin grupo |
| `awesome-agents` | Directorio de herramientas y proyectos abiertos para construir y operar agentes… | 1 Básico | 39 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Agentic Awesome Skills (AAS) (`antigravity-awesome-skills`)

- **Repo:** https://github.com/sickn33/agentic-awesome-skills · MIT · nivel 1 · 68/100 · recomendado en «Catálogos de skills y plugins para agentes»
- **Qué es:** Agentic Awesome Skills (AAS), antes «Antigravity Awesome Skills», de sickn33 (MIT): biblioteca de más de 2.960 skills instalables y el componente AAS Core. Muy activa (v20.9.0); proyecto comunitario no afiliado a Google.
- **Cuándo elegirlo:** Casos: Añadir una skill de brainstorming a un proyecto; Seleccionar un pequeño conjunto de instrucciones de diseño y seguridad.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); GitHub CLI con gh skill, o la ruta ZIP indicada por la guía;  agente destino; hardware prerequisites; API de IA: no; GitHub CLI con gh skill, o la ruta ZIP indicada por la guía; agente destino.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md

  ```sh
  gh skill preview sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md@v20.8.0
  gh skill install sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md --agent codex --scope user --pin v20.8.0
  ```
- **Primera prueba propuesta (no ejecutada):** Previsualiza una skill concreta y revisa el plan antes de instalarla en un agente Éxito: El destino contiene la skill seleccionada y puedes revisar los archivos añadidos
- **Combina con:** `codex` [20/terminal], `claude-code` [20/terminal], `cli` [7/herramientas], `skillspector` [16/skills], `antigravity-cli` [20/terminal]
- **Alternativas:** `claude-plugins-official`, `awesome-agent-skills`, `wshobson-agents`, `awesome-claude-skills`, `awesome-claude-code`
- **Riesgos y avisos:** Alternativas (elige una): awesome-agent-skills, awesome-claude-skills, wshobson-agents. Con la pausa de npm, desconfía de paquetes AAS recientes en npm. Ahora se llama Agentic Awesome Skills. La publicación npm está pausada: usar GitHub y la guía vigente, no el antiguo instalador npx.

### Awesome GitHub Copilot (`awesome-copilot`)

- **Repo:** https://github.com/github/awesome-copilot · MIT · nivel 1 · 68/100
- **Qué es:** Colección comunitaria alojada por GitHub (MIT) de agentes personalizados, instrucciones, skills, hooks, flujos de trabajo y plugins para GitHub Copilot. Muy activa; tiene web con búsqueda y un Learning Hub.
- **Cuándo elegirlo:** Casos: Añadir instrucciones de equipo al asistente de programación; Estudiar un agente especializado antes de adaptarlo a un proyecto.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); GitHub Copilot y un plugin elegido del catálogo; hardware prerequisites; API de IA: no; GitHub Copilot y un plugin elegido del catálogo.
- **Instalación (documentada en la fuente; no ejecutada):** `copilot plugin install <plugin-name>@awesome-copilot` — fuente: https://github.com/github/awesome-copilot/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sustituye el marcador plugin-name por un plugin listado y consulta sus instrucciones Éxito: Copilot reconoce la personalización seleccionada y puedes ver sus capacidades
- **Combina con:** `github-mcp-server` [5/servidores], `spec-kit` [2/metodologia], `cli` [7/herramientas]
- **Riesgos y avisos:** El destino principal es GitHub Copilot; el comando contiene un marcador que debes sustituir, no ejecutar literalmente.

### Claude Code Plugins Directory (`claude-plugins-official`)

- **Repo:** https://github.com/anthropics/claude-plugins-official · Apache-2.0 · nivel 1 · 62/100 · alternativa en «Catálogos de skills y plugins para agentes»
- **Qué es:** Repositorio de Anthropic (Apache 2.0) con sus propios plugins para Claude y el marketplace `claude-plugins-official` de Claude Code. Está en transición: los envíos de terceros ya se hacen en claude.ai/directory/manage.
- **Cuándo elegirlo:** Casos: Añadir una herramienta de revisión al flujo de desarrollo; Conectar un servicio mediante un plugin publicado en el marketplace oficial.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude Code;  elegir un plugin y revisar sus dependencias; hardware prerequisites; API de IA: no; Claude Code; elegir un plugin y revisar sus dependencias.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://code.claude.com/docs/en/plugins
- **Primera prueba propuesta (no ejecutada):** Busca un plugin del marketplace e instala solo el que corresponde a tu tarea Éxito: El plugin figura instalado y puedes consultar sus comandos o skills
- **Combina con:** `claude-code` [20/terminal], `superpowers` [2/metodologia], `skills` [2/metodologia], `awesome-claude-code`
- **Alternativas:** `antigravity-awesome-skills`, `awesome-agent-skills`, `wshobson-agents`, `awesome-claude-skills`, `awesome-claude-code`
- **Riesgos y avisos:** Alternativa (elige una): wshobson-agents. Se quitaron anthropic-skills y awesome-claude-code: son catálogos paralelos, no integraciones. Es un directorio gestionado por Anthropic; instalar un plugin no implica instalar todos los del repositorio.

### Claude Code Templates (`claude-code-templates`)

- **Repo:** https://github.com/davila7/claude-code-templates · MIT · nivel 1 · 61/100
- **Qué es:** Reúne componentes para Claude Code con buscador, entre ellos skills, agentes, hooks y configuraciones de herramientas.
- **Cuándo elegirlo:** Casos: Comparar dos plantillas de revisión de UI.; Encontrar un componente y revisar su procedencia antes de importarlo.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python, package.json; API de IA: no; Navegador; para una eventual adopción, Claude Code y una carpeta limpia..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://www.aitmpl.com
- **Primera prueba propuesta (no ejecutada):** Navega el catálogo y revisa los archivos y la licencia de una sola skill. Éxito: Puedes explicar qué instalaría y detectar si añade scripts o conexiones.
- **Riesgos y avisos:** Se ficha como referencia. Para su CLI, la publicación 1.29.7 es posterior a la corrección de GHSA-79wm-x847-7cvg; revisa también los otros avisos y cada….

### skills (`google-skills`)

- **Repo:** https://github.com/google/skills · Apache-2.0 · nivel 2 · 59/100
- **Qué es:** Repositorio oficial de Google (Apache 2.0) con Agent Skills para sus productos, sobre todo Google Cloud. Muy activo, sin releases.
- **Cuándo elegirlo:** Casos: Revisar la configuración de un servicio Cloud en un entorno de prueba; Aprender a consultar métricas de Ads sin crear campañas.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente compatible;  elegir una skill del producto de Google que usarás; hardware prerequisites; API de IA: no; Agente compatible; elegir una skill del producto de Google que usarás.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add google/skills` — fuente: https://github.com/google/skills/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala una skill concreta y pide explicar su configuración sin modificar servicios reales Éxito: El agente identifica requisitos, credenciales y acciones del producto correspondiente
- **Combina con:** `gemini-cli` [20/terminal], `gemini-skills`, `adk-python` [3/py], `antigravity-cli` [20/terminal]
- **Riesgos y avisos:** Los tres clientes tienen rutas documentadas; una skill no concede permisos sobre tu cuenta de Google.

### gemini-skills (`gemini-skills`)

- **Repo:** https://github.com/google-gemini/gemini-skills · Apache-2.0 · nivel 1 · 55/100
- **Qué es:** Biblioteca oficial de Google (Apache 2.0) de skills para la API de Gemini, su SDK y la interacción con los modelos. Activa, sin releases.
- **Cuándo elegirlo:** Casos: Revisar cómo integrar el SDK de Gemini en una aplicación; Preparar una llamada multimodal con datos de prueba.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente compatible;  cuenta Gemini solo si el proyecto generado llama su API; hardware prerequisites; API de IA: no; Agente compatible; cuenta Gemini solo si el proyecto generado llama su API.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/google-gemini/gemini-skills/blob/main/README.md

  ```sh
  # Interactively browse and install skills.
  npx skills add google-gemini/gemini-skills --list

  # Install a specific skill (e.g., gemini-api-dev).
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev
  ```
- **Primera prueba propuesta (no ejecutada):** Elige una skill de desarrollo Gemini y pídele preparar un ejemplo sin enviar todavía una petición Éxito: El ejemplo identifica el SDK, la credencial y el punto donde comenzaría el consumo
- **Combina con:** `gemini-cli` [20/terminal], `google-skills`, `adk-python` [3/py]
- **Riesgos y avisos:** Se distingue instalar una skill de disponer de acceso a la API Gemini; Antigravity tiene una ruta documentada.

### Awesome Agent Skills (`awesome-agent-skills`)

- **Repo:** https://github.com/VoltAgent/awesome-agent-skills · MIT · nivel 1 · 54/100 · alternativa en «Catálogos de skills y plugins para agentes»
- **Qué es:** Colección MIT de VoltAgent con skills de agentes oficiales de equipos de desarrollo y de la comunidad, seleccionadas a mano. Muy activa; el README lleva patrocinadores.
- **Cuándo elegirlo:** Casos: Encontrar una skill de Supabase para un proyecto existente; Localizar instrucciones de frontend publicadas por un equipo mantenedor.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador;  identificar el cliente donde usarás el recurso elegido; hardware prerequisites; API de IA: no; Navegador; identificar el cliente donde usarás el recurso elegido.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/VoltAgent/awesome-agent-skills/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre una skill oficial de una tecnología que ya utilices y revisa su instalación Éxito: Puedes distinguir su autor, archivos y destino compatible
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal], `skillspector` [16/skills], `awesome-agents`
- **Alternativas:** `antigravity-awesome-skills`, `claude-plugins-official`, `wshobson-agents`, `awesome-claude-skills`, `awesome-claude-code`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): antigravity-awesome-skills, awesome-claude-skills. Algunas entradas enlazan herramientas de pago o con pagos integrados. El catálogo declara varios clientes, pero la compatibilidad y licencia se revisan por skill, no para todo el directorio en bloque.

### Anthropic Skills (`anthropic-skills`)

- **Repo:** https://github.com/anthropics/skills · — · nivel 1 · 52/100
- **Qué es:** Repositorio oficial de Anthropic con su implementación de skills para Claude: carpetas de instrucciones, scripts y recursos que Claude carga bajo demanda. Muy activo y sin releases.
- **Cuándo elegirlo:** Casos: Extraer campos de un formulario PDF propio; Crear una presentación usando las instrucciones de la skill de diapositivas.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude Code activo;  dependencias de la skill de documentos elegida; hardware prerequisites; API de IA: no; Claude Code activo; dependencias de la skill de documentos elegida.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/anthropics/skills/blob/main/README.md

  ```bash
  /plugin marketplace add anthropics/skills

  /plugin install document-skills@anthropic-agent-skills
  /plugin install example-skills@anthropic-agent-skills
  ```
- **Primera prueba propuesta (no ejecutada):** Pide a la skill PDF identificar campos de un formulario de prueba Éxito: El agente identifica la skill y entrega la lista de campos del PDF
- **Combina con:** `claude-code` [20/terminal], `skillspector` [16/skills], `claude-agent-sdk-python` [3/py], `hello-halo` [21/asistentes], `scientific-agent-skills` [27/dominio], `financial-services` [27/dominio]
- **Riesgos y avisos:** Se quitaron claude-plugins-official y superpowers porque no hay integración documentada. La implementación es para Claude; el estándar abierto no demuestra que todos sus scripts funcionen en otros clientes.

### Awesome Claude Code Subagents (`awesome-claude-code-subagents`)

- **Repo:** https://github.com/VoltAgent/awesome-claude-code-subagents · MIT · nivel 1 · 52/100
- **Qué es:** Reúne perfiles especializados para Claude Code que puedes leer y comparar antes de adoptar uno en tu propio proyecto.
- **Cuándo elegirlo:** Casos: Comparar el perfil de un revisor de accesibilidad y uno de documentación.; Identificar las herramientas declaradas por una plantilla antes de copiarla.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Shell; API de IA: no; Navegador; para una eventual adopción, Claude Code y una carpeta de prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/ed74d115b7fb7026a22a4f816a8e3250f425e3b4/README.md
- **Primera prueba propuesta (no ejecutada):** Abre dos perfiles de una categoría y compara instrucciones, permisos y alcance. Éxito: Puedes explicar qué haría cada perfil y cuál se ajusta a una tarea pequeña.
- **Riesgos y avisos:** Es una colección comunitaria. Revisar cada perfil y sus herramientas antes de instalar; no asumir compatibilidad con otros clientes.

### wshobson/agents (`wshobson-agents`)

- **Repo:** https://github.com/wshobson/agents · MIT · nivel 1 · 51/100 · alternativa en «Catálogos de skills y plugins para agentes»
- **Qué es:** Colección MIT de plugins, agentes, skills y comandos de wshobson para varias herramientas de código con IA. Muy activa, sin releases.
- **Cuándo elegirlo:** Casos: Aplicar patrones de pruebas a un módulo Python; Adaptar el mismo conjunto de agentes a otra herramienta mediante sus generadores.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente destino;  dependencias del plugin seleccionado; hardware prerequisites; API de IA: no; Agente destino; dependencias del plugin seleccionado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/wshobson/agents/blob/main/README.md

  ```text
  /plugin marketplace add wshobson/agents
  /plugin install python-development@claude-code-workflows
  ```
- **Primera prueba propuesta (no ejecutada):** Instala el plugin de desarrollo Python y pide revisar un caso de pruebas pequeño Éxito: El agente encuentra las instrucciones del plugin y propone una revisión sobre ese caso
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal], `plugins`
- **Alternativas:** `antigravity-awesome-skills`, `claude-plugins-official`, `awesome-agent-skills`, `awesome-claude-skills`, `awesome-claude-code`, `agency-agents`
- **Riesgos y avisos:** Alternativas (elige una): claude-plugins-official, antigravity-awesome-skills, agency-agents. Se quitó skillspector porque no hay integración (sigue siendo…. El README documenta generadores distintos por cliente; no basta copiar un formato de configuración a todos.

### Awesome Claude Code (`awesome-claude-code`)

- **Repo:** https://github.com/hesreallyhim/awesome-claude-code · CC-BY-NC-ND-4.0 · nivel 1 · 48/100 · alternativa en «Catálogos de skills y plugins para agentes»
- **Qué es:** Lista curada de recursos para Claude Code (skills, hooks, comandos, flujos, herramientas, documentación) mantenida por hesreallyhim. Muy activa; GitHub marca su licencia como NOASSERTION.
- **Cuándo elegirlo:** Casos: Encontrar ejemplos para personalizar una sesión de Claude Code; Comparar herramientas que muestran el uso del agente.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador;  una necesidad concreta de configuración; hardware prerequisites; API de IA: no; Navegador; una necesidad concreta de configuración.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/hesreallyhim/awesome-claude-code/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Localiza un recurso de hooks o status line y revisa su fuente original Éxito: Identificas su función, mantenimiento y requisitos antes de instalarlo
- **Combina con:** `claude-code` [20/terminal], `claude-plugins-official`, `skillspector` [16/skills]
- **Alternativas:** `antigravity-awesome-skills`, `claude-plugins-official`, `awesome-agent-skills`, `wshobson-agents`, `awesome-claude-skills`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): awesome-claude-skills. Se quitó superpowers porque no hay integración. Es una selección independiente; su nombre y enlaces a Anthropic no la convierten en un marketplace oficial.

### Awesome Claude Skills (`awesome-claude-skills`)

- **Repo:** https://github.com/ComposioHQ/awesome-claude-skills · — · nivel 1 · 48/100 · alternativa en «Catálogos de skills y plugins para agentes»
- **Qué es:** Lista curada de ComposioHQ con más de 1.000 skills y plugins para Claude.ai, Claude Code, Codex y otros agentes. GitHub no detecta licencia, aunque el README muestra una insignia Apache 2.0. Es también un escaparate comercial de Composio.
- **Cuándo elegirlo:** Casos: Encontrar instrucciones para revisar documentos de trabajo; Descubrir un conector para una aplicación que ya usas.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador;  agente compatible solo al utilizar una skill seleccionada; hardware prerequisites; API de IA: no; Navegador; agente compatible solo al utilizar una skill seleccionada.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una skill del listado y abre su archivo o repositorio de origen Éxito: Puedes explicar qué entrada necesita y cómo la instalarías en tu cliente
- **Combina con:** `composio` [22/infra], `claude-code` [20/terminal], `skillspector` [16/skills]
- **Alternativas:** `antigravity-awesome-skills`, `claude-plugins-official`, `awesome-agent-skills`, `wshobson-agents`, `awesome-claude-code`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): awesome-agent-skills, antigravity-awesome-skills, awesome-claude-code. Dar acceso a 1.000 apps amplía mucho lo que el agente puede…. El README distingue la colección del plugin connect-apps; no se atribuye la misma instalación a todos los recursos.

### plugins (`plugins`)

- **Repo:** https://github.com/cursor/plugins · — · nivel 1 · 48/100
- **Qué es:** Repositorio oficial de Cursor con plugins para herramientas de desarrollo, frameworks y productos SaaS. Muy activo; GitHub no detecta licencia de repositorio.
- **Cuándo elegirlo:** Casos: Encontrar una integración de un servicio que ya utiliza tu equipo; Estudiar cómo empaquetar reglas y skills para Cursor.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Cursor;  revisar el plugin concreto y sus credenciales; hardware prerequisites; API de IA: no; Cursor; revisar el plugin concreto y sus credenciales.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/cursor/plugins/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un plugin del catálogo y lee su manifiesto y guía de conexión Éxito: Puedes distinguir sus skills, reglas, servidor MCP y servicios externos
- **Combina con:** `skills` [2/metodologia], `agent-skills` [2/metodologia], `wshobson-agents`
- **Riesgos y avisos:** Sin licencia declarada en la raíz; revisa la de cada plugin de terceros. El manifiesto es de Cursor. No se afirma que todo el plugin pueda copiarse directamente a Claude Code, Codex o Antigravity.

### autoskills (`autoskills`)

- **Repo:** https://github.com/midudev/autoskills · CC-BY-NC-4.0 · nivel 1 · 40/100
- **Qué es:** CLI de midudev que detecta el stack de un proyecto e instala skills de agente seleccionadas. Licencia CC BY-NC 4.0, que no es de código abierto y prohíbe el uso comercial, y que GitHub marca como NOASSERTION. Activo (v0.4.1).
- **Cuándo elegirlo:** Casos: Encontrar skills adecuadas para un proyecto React existente; Revisar qué archivos de skills se incorporarían sin descargarlos todos.
- **Requisitos:** nivel 1: preparación sencilla; Node.js;  un proyecto con sus manifiestos de dependencias; hardware prerequisites; API de IA: no; Node.js; un proyecto con sus manifiestos de dependencias.
- **Instalación (documentada en la fuente; no ejecutada):** `npx autoskills` — fuente: https://github.com/midudev/autoskills/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Revisa la selección que propone para tu stack antes de permitir la instalación Éxito: La lista corresponde a tus tecnologías y queda un registro de las skills instaladas
- **Combina con:** `claude-code` [20/terminal], `skillspector` [16/skills], `codex` [20/terminal]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). La licencia CC BY-NC impide el uso comercial. Se quitó awesome-agent-skills porque no hay integración. Se corrige la API inferida por menciones a tecnologías de autenticación y pagos: no son proveedores requeridos por el CLI.

### awesome-agents (`awesome-agents`)

- **Repo:** https://github.com/kyrolabs/awesome-agents · — · nivel 1 · 39/100
- **Qué es:** Lista curada de kyrolabs con herramientas y productos de código abierto para construir agentes de IA. GitHub no detecta licencia. Activa; ha lanzado una lista hermana, Awesome ADE, sobre entornos de desarrollo agéntico.
- **Cuándo elegirlo:** Casos: Descubrir un asistente personal que trabaja con modelos locales; Encontrar frameworks para estudiar equipos de agentes.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador;  definir qué tarea quieres delegar; hardware prerequisites; API de IA: no; Navegador; definir qué tarea quieres delegar.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/kyrolabs/awesome-agents/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Compara dos proyectos del mismo tipo y abre sus repositorios originales Éxito: Puedes explicar su diferencia y qué infraestructura necesita cada uno
- **Combina con:** `openclaw` [21/asistentes], `hermes-agent` [21/asistentes], `awesome-agent-skills`
- **Riesgos y avisos:** Sin licencia declarada. Muchas entradas son proyectos pequeños que se autopromocionan: verifica la madurez de cada uno. No se hereda la compatibilidad de todos los proyectos citados a la lista que los reúne.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-2-catalogos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Catálogos y marketplaces de skills», lee `docs/alexandria/categoria-2-catalogos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-2-catalogos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
