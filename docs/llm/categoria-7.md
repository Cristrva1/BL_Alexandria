# Alexandría para agentes · Entender código y comprobar su calidad

Categoría 7 completa (26 repos, 3 subcategorías). Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=7 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `graphify` | codigo | CLI y skill que convierten código y documentos en un grafo consultable; el… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `codegraph` | codigo | CLI que indexa tu código en local para que los asistentes de IA entiendan… | 1 Básico | 66 | MIT (OSI permisiva) | alternativa |
| `tree-sitter` | codigo | Sistema de parsing incremental para herramientas de programación, base de… | 2 Intermedio | 60 | MIT (OSI permisiva) | sin grupo |
| `codebase-memory-mcp` | codigo | Motor local de inteligencia de código que conecta código, docs e… | 1 Básico | 58 | MIT (OSI permisiva) | alternativa |
| `floorplan` | codigo | Herramienta para que Claude o Codex genere un mapa interactivo y explicado de… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `repomix` | codigo | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | 1 Básico | 53 | MIT (OSI permisiva) | alternativa |
| `gitnexus` | codigo | Herramienta visual para explorar y entender repositorios Git, mostrando… | 1 Básico | 51 | PolyForm-Noncommercial-1.0.0 (source-available) | alternativa |
| `ruff` | calidad | Linter y formateador de Python extremadamente rápido escrito en Rust… | 1 Básico | 74 | MIT (OSI permisiva) | sin grupo |
| `biome` | calidad | Formateador y linter en un solo binario para JavaScript, TypeScript, JSX, JSON… | 1 Básico | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `open-code-review` | calidad | Revisa cambios de código con reglas y un informe guiado, usando su propio… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `gitleaks` | calidad | Detector de secretos (contraseñas, claves de API, tokens) en repositorios git… | 1 Básico | 63 | MIT (OSI permisiva) | recomendado |
| `pre-commit` | calidad | Framework para gestionar y ejecutar hooks de git multilenguaje antes de cada… | 1 Básico | 62 | MIT (OSI permisiva) | sin grupo |
| `trufflehog` | calidad | Busca, clasifica, verifica y analiza credenciales filtradas en git, chats… | 1 Básico | 61 | AGPL-3.0 (OSI copyleft) | alternativa |
| `ast-grep` | calidad | CLI en Rust para búsqueda estructural, lint y reescritura de código usando… | 1 Básico | 60 | MIT (OSI permisiva) | sin grupo |
| `sonarqube` | calidad | Plataforma de inspección continua de calidad y seguridad del código: análisis… | 2 Intermedio | 57 | LGPL-3.0 (OSI copyleft) | sin grupo |
| `swe-bench` | calidad | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. | 3 Avanzado | 52 | MIT (OSI permisiva) | sin grupo |
| `openai-python` | herramientas | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes… | 2 Intermedio | 75 | Apache-2.0 (OSI permisiva) | sin grupo |
| `cli` | herramientas | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la… | 1 Básico | 74 | MIT (OSI permisiva) | sin grupo |
| `lazygit` | herramientas | Interfaz de terminal sencilla para git: preparar fragmentos o líneas, rebase… | 1 Básico | 72 | MIT (OSI permisiva) | sin grupo |
| `fzf` | herramientas | Buscador difuso de línea de comandos y kit de interfaces de terminal para… | 1 Básico | 68 | MIT (OSI permisiva) | sin grupo |
| `requests-cache` | herramientas | Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas… | 2 Intermedio | 59 | BSD-2-Clause (OSI permisiva) | sin grupo |
| `apscheduler` | herramientas | Programa funciones Python para un horario, un intervalo o una fecha concreta… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `npkill` | herramientas | Muestra cuánto espacio ocupan carpetas generadas por herramientas de desarrollo… | 1 Básico | 58 | MIT (OSI permisiva) | sin grupo |
| `hishel` | herramientas | Añade caché a peticiones HTTP de Python con políticas de expiración y… | 2 Intermedio | 53 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `ripgrep` | herramientas | Búsqueda recursiva de texto por expresiones regulares muy rápida que respeta… | 1 Básico | 52 | Unlicense (OSI permisiva) | sin grupo |
| `pybreaker` | herramientas | Protege una integración Python con un interruptor que pausa llamadas tras… | 2 Intermedio | 43 | BSD-3-Clause (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### graphify (`graphify`)

- **Repo:** https://github.com/Graphify-Labs/graphify · Apache-2.0 · nivel 2 · 74/100 · recomendado en «Mapas e índices de código para agentes»
- **Qué es:** Graphify, CLI y skill que convierte código y documentos en un grafo de conocimiento consultable, de Graphify Labs. Licencia Apache-2.0. Tiene un recuento de estrellas excepcionalmente alto (~149k), publica muy a menudo (v0.9.111) y ofrece…
- **Cuándo elegirlo:** Casos: Explorar impacto de un cambio; Relacionar documentación y estructura de código.
- **Requisitos:** nivel 2: preparación media; Python 3.10+; uv o pipx; carpeta de código; hardware prerequisites; API de IA: opcional; Python 3.10+; uv o pipx; carpeta de código.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Graphify-Labs/graphify/blob/v8/README.md

  ```bash
  uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
  graphify install               # detects your assistant and registers the skill
  ```
- **Primera prueba propuesta (no ejecutada):** Indexa primero solo código y consulta qué funciones dependen de un módulo Éxito: Cada relación se puede contrastar con un archivo o símbolo
- **Combina con:** `claude-code` [20/terminal], `tree-sitter`, `ollama` [8/motores], `graphrag` [6/rag]
- **Alternativas:** `codegraph`, `codebase-memory-mcp`, `repomix`, `gitnexus`, `serena`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): codegraph, gitnexus, serena, codebase-memory-mcp. Ojo con paquetes PyPI de nombre parecido. El paquete es graphifyy; el soporte Antigravity es explícito; la extracción semántica y la de código no tienen los mismos costes.

### codegraph (`codegraph`)

- **Repo:** https://github.com/colbymchenry/codegraph · MIT · nivel 1 · 66/100 · alternativa en «Mapas e índices de código para agentes»
- **Qué es:** CodeGraph, CLI que indexa el código en local para dar contexto semántico a asistentes de IA, de @colbymchenry. Licencia MIT. Es muy popular (~78k estrellas, v1.6.2) y prepara una plataforma alojada.
- **Cuándo elegirlo:** Casos: Preparar una refactorización; Encontrar rutas de ejecución de un proyecto.
- **Requisitos:** nivel 1: preparación sencilla; Instalador oficial o Node y npm; repositorio de prueba; hardware prerequisites; API de IA: opcional; Instalador oficial o Node y npm; repositorio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i -g @colbymchenry/codegraph` — fuente: https://github.com/colbymchenry/codegraph/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Indexa una carpeta y consulta quién llama a una función conocida Éxito: Los resultados identifican definiciones y relaciones comprobables
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `headroom` [23/tokens], `floorplan`
- **Alternativas:** `graphify`, `codebase-memory-mcp`, `repomix`, `gitnexus`, `serena`
- **Riesgos y avisos:** Alternativas (elige una): codebase-memory-mcp, serena, gitnexus, graphify. Telemetría anónima activada. La compatibilidad con los tres clientes está documentada; comprueba indexación y sincronización antes de confiar en el mapa.

### tree-sitter (`tree-sitter`)

- **Repo:** https://github.com/tree-sitter/tree-sitter · MIT · nivel 2 · 60/100
- **Qué es:** Tree-sitter, generador de parsers y librería de parsing incremental. Licencia MIT. Es infraestructura madura (~27k estrellas, v0.27.2) usada por muchos editores y herramientas.
- **Cuándo elegirlo:** Casos: Construir un analizador de código; Extraer símbolos para una herramienta de edición.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Herramientas y binding del lenguaje elegido; gramática; hardware prerequisites; API de IA: no; Herramientas y binding del lenguaje elegido; gramática.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://tree-sitter.github.io/tree-sitter/
- **Primera prueba propuesta (no ejecutada):** Analiza un archivo mínimo y observa cómo cambia el árbol tras editar una función Éxito: El árbol refleja el cambio sin interpretar semánticamente todo el programa
- **Combina con:** `ast-grep` [7/calidad], `aider` [20/terminal], `repomix`, `graphify`
- **Riesgos y avisos:** Sin alternativas declaradas. Es infraestructura de parsing; no contesta por sí sola preguntas sobre arquitectura o intención del código.

### codebase-memory-mcp (`codebase-memory-mcp`)

- **Repo:** https://github.com/DeusData/codebase-memory-mcp · MIT · nivel 1 · 58/100 · alternativa en «Mapas e índices de código para agentes»
- **Qué es:** codebase-memory-mcp, motor local de inteligencia de código para agentes vía MCP, de DeusData. Licencia MIT. Es muy activo (~49k estrellas, v0.12.1).
- **Cuándo elegirlo:** Casos: Navegar dependencias de código; Seleccionar pruebas afectadas por un cambio.
- **Requisitos:** nivel 1: preparación sencilla; Binario para tu sistema; repositorio de prueba; Node 22+ solo para compilar CBM Lens; hardware prerequisites; API de IA: opcional; Binario para tu sistema; repositorio de prueba; Node 22+ solo para compilar CBM Lens.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash` — fuente: https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Indexa un proyecto pequeño y consulta el impacto de cambiar una función Éxito: Puedes abrir las referencias y relaciones del grafo
- **Combina con:** `claude-code` [20/terminal], `repomix`, `codex` [20/terminal]
- **Alternativas:** `graphify`, `codegraph`, `repomix`, `gitnexus`, `serena`
- **Riesgos y avisos:** Alternativas (elige una): codegraph, gitnexus, serena, graphify. Revisa el script de instalación antes de ejecutarlo. Las funciones de hooks y actividad varían por cliente; los binarios ya compilados no necesitan Node para ejecutar Lens.

### floorplan (`floorplan`)

- **Repo:** https://github.com/haydenschmitty/floorplan · MIT · nivel 2 · 58/100
- **Qué es:** Floorplan, plugin para Claude Code y Codex que dibuja un mapa interactivo de una aplicación, de @haydenschmitty. Licencia MIT. Es reciente (~5k estrellas, floorplan--v0.10.0).
- **Cuándo elegirlo:** Casos: Explicar la arquitectura a alguien nuevo; Encontrar dónde se inicia una petición de la interfaz.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude Code o Codex con plugins; proyecto pequeño de prueba; hardware prerequisites; API de IA: no; Claude Code o Codex con plugins; proyecto pequeño de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/haydenschmitty/floorplan/blob/main/README.md

  ```bash
  claude plugin marketplace add haydenschmitty/floorplan
  claude plugin install floorplan@floorplan
  ```
- **Primera prueba propuesta (no ejecutada):** Pide un mapa de una app mínima y abre un enlace entre una pantalla y su endpoint Éxito: Puedes contrastar nombres legibles, archivos y conexiones del mapa
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `codegraph`
- **Riesgos y avisos:** Sin alternativas declaradas. El mapa offline no implica generación con IA local; el README cambió y esta ficha conserva la nueva versión de fuente.

### Repomix (`repomix`)

- **Repo:** https://github.com/yamadashy/repomix · MIT · nivel 1 · 53/100 · alternativa en «Mapas e índices de código para agentes»
- **Qué es:** Repomix, herramienta para empaquetar un repositorio en un único archivo apto para LLM, de @yamadashy. Licencia MIT. Es madura y muy usada (~29k estrellas, v1.19.0) y tiene patrocinadores destacados en el README.
- **Cuándo elegirlo:** Casos: Preparar contexto de código para una consulta; Compartir una muestra reproducible de un proyecto.
- **Requisitos:** nivel 1: preparación sencilla; Node.js; repositorio de prueba; filtros de inclusión; hardware prerequisites; API de IA: no; Node.js; repositorio de prueba; filtros de inclusión.
- **Instalación (documentada en la fuente; no ejecutada):** `npx repomix@latest` — fuente: https://github.com/yamadashy/repomix/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Empaqueta una carpeta pequeña y abre el resultado antes de entregarlo a una IA Éxito: Puedes comprobar archivos incluidos, tamaño y exclusiones
- **Combina con:** `claude-code` [20/terminal], `tree-sitter`, `markitdown` [13/conversion], `codebase-memory-mcp`
- **Alternativas:** `graphify`, `codegraph`, `codebase-memory-mcp`, `gitnexus`
- **Riesgos y avisos:** Alternativas (elige una): gitnexus. Ofrece MCP stdio y plugins o skills; revisa secretos y archivos excluidos aunque el paquete incluya un detector.

### GitNexus (`gitnexus`)

- **Repo:** https://github.com/abhigyanpatwari/GitNexus · PolyForm-Noncommercial-1.0.0 · nivel 1 · 51/100 · alternativa en «Mapas e índices de código para agentes»
- **Qué es:** GitNexus, indexador de código en grafo con herramientas MCP, CLI y explorador web, de @abhigyanpatwari. Licencia PolyForm Noncommercial 1.0.0, con licencia comercial aparte (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Entender una base de código nueva; Inspeccionar el alcance de una refactorización.
- **Requisitos:** nivel 1: preparación sencilla; Node 22.18+ en 22.x o 24.11+; repositorio de prueba; hardware prerequisites; API de IA: no; Node 22.18+ en 22.x o 24.11+; repositorio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/abhigyanpatwari/GitNexus/blob/main/README.md

  ```bash
  # Run from your repository root
  npx gitnexus analyze

  # Connect your editors once
  npx gitnexus setup
  ```
- **Primera prueba propuesta (no ejecutada):** Analiza una app pequeña y consulta el recorrido entre un endpoint y su función Éxito: El mapa permite localizar los archivos reales y sus conexiones
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `codex` [20/terminal]
- **Alternativas:** `graphify`, `codegraph`, `codebase-memory-mcp`, `repomix`, `serena`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): repomix, codebase-memory-mcp, serena, codegraph, graphify. La licencia no comercial impide usarlo en empresas sin licencia de pago. El setup detecta los tres clientes; no confundas poder instalarlo con tener permiso de uso comercial.

### Ruff (`ruff`)

- **Repo:** https://github.com/astral-sh/ruff · MIT · nivel 1 · 74/100
- **Qué es:** Linter y formateador de código abierto (MIT) desarrollado por Astral, la empresa de uv. Estándar de facto en el ecosistema Python, usado por proyectos como FastAPI, pandas o Apache Airflow.
- **Cuándo elegirlo:** Casos: sustituir Flake8, isort y Black por una sola herramienta en un proyecto; revisar y corregir el código que genera un agente antes de cada commit.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install ruff` — fuente: https://github.com/astral-sh/ruff/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta `uvx ruff check` y `uvx ruff format` en un proyecto Python de prueba. Éxito: Ruff informa de los problemas en segundos y el formateo deja un diff limpio.
- **Combina con:** `pre-commit`, `sonarqube`, `claude-code` [20/terminal]
- **Riesgos y avisos:** Ruff no hace comprobación de tipos: combínalo con un verificador de tipos si lo necesitas.

### Biome (`biome`)

- **Repo:** https://github.com/biomejs/biome · Apache-2.0 · nivel 1 · 71/100
- **Qué es:** Cadena de herramientas de código abierto (doble licencia MIT o Apache-2.0) mantenida por la comunidad Biome, sucesora de Rome. Muy activa y adoptada en proyectos web.
- **Cuándo elegirlo:** Casos: sustituir ESLint y Prettier en un proyecto web por una sola herramienta; formatear y revisar el código que genera un agente antes de abrir un PR.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install --save-dev --save-exact @biomejs/biome` — fuente: https://github.com/biomejs/biome/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala `@biomejs/biome` como dependencia de desarrollo y ejecuta `npx @biomejs/biome check --write`. Éxito: Biome formatea y corrige los archivos y lista los problemas restantes.
- **Combina con:** `pre-commit`, `tailwindcss` [9/estilos], `claude-code` [20/terminal]
- **Riesgos y avisos:** Algunos plugins de ESLint no tienen equivalente en Biome: revisa las reglas que necesitas antes de migrar.

### Open Code Review (`open-code-review`)

- **Repo:** https://github.com/alibaba/open-code-review · Apache-2.0 · nivel 2 · 71/100
- **Qué es:** Una herramienta de revisión defensiva de código para cambios propios antes de fusionarlos.
- **Cuándo elegirlo:** Casos: Revisar condiciones de error en un cambio de ejemplo.; Preparar una lista de comprobaciones para una PR de un proyecto propio. Evítalo si no usas un agente compatible con skills.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Go, Makefile, go.mod, package.json; hardware prerequisites; API de IA: opcional; Git 2.41 o superior, la CLI ocr y un cliente apropiado para la ruta delegada..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/skills/open-code-review-delegate/SKILL.md
- **Primera prueba propuesta (no ejecutada):** Pide que revise un cambio ficticio de un proyecto propio, sin permitir escrituras ni cargar un repositorio de origen desconocido. Éxito: El informe nombra archivos, hallazgos y comprobaciones sin modificar el proyecto de ejemplo.
- **Riesgos y avisos:** GHSA-wwg6-qfxw-xffj afecta versiones anteriores a 1.11.1; el tag 1.14.1 incluye la corrección. Usa solo repositorios propios o de confianza.

### Gitleaks (`gitleaks`)

- **Repo:** https://github.com/gitleaks/gitleaks · MIT · nivel 1 · 63/100 · recomendado en «Detección de secretos en repos»
- **Qué es:** Herramienta de detección de secretos de código abierto (MIT) creada por Zachary Rice. Muy usada; el README indica que está completa en funciones y que las versiones futuras serán solo parches de seguridad, mientras el autor se centra en…
- **Cuándo elegirlo:** Casos: revisar el historial de un repositorio antes de hacerlo público; bloquear commits que contengan claves con un hook pre-commit.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install gitleaks` — fuente: https://github.com/gitleaks/gitleaks/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Gitleaks y ejecútalo sobre un repositorio de prueba con una clave falsa en un commit. Éxito: El informe señala el archivo, la línea y el commit de la clave falsa.
- **Combina con:** `pre-commit`, `semgrep` [16/defensa], `claude-code` [20/terminal]
- **Alternativas:** `trufflehog`
- **Riesgos y avisos:** Alternativas (elige una): trufflehog. Sucesor declarado por el autor: Betterleaks.

### pre-commit (`pre-commit`)

- **Repo:** https://github.com/pre-commit/pre-commit · MIT · nivel 1 · 62/100
- **Qué es:** Framework de hooks de git de código abierto (MIT) mantenido por Anthony Sottile y la comunidad pre-commit desde 2014. Muy maduro y ampliamente adoptado.
- **Cuándo elegirlo:** Casos: obligar a pasar formato, lint y escaneo de secretos antes de cada commit; aplicar las mismas comprobaciones en local y en CI.
- **Requisitos:** nivel 1: preparación sencilla; Python, setup.py; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/pre-commit/pre-commit/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala pre-commit, crea un .pre-commit-config.yaml con un hook de formato y ejecuta `pre-commit run --all-files`. Éxito: El hook se instala solo y formatea o señala los archivos del repositorio.
- **Combina con:** `ruff`, `gitleaks`, `trufflehog`, `biome`, `semgrep` [16/defensa], `trivy` [16/nube-contenedores]
- **Riesgos y avisos:** Los hooks se descargan de repositorios externos: fija revisiones y revisa su origen.

### TruffleHog (`trufflehog`)

- **Repo:** https://github.com/trufflesecurity/trufflehog · AGPL-3.0 · nivel 1 · 61/100 · alternativa en «Detección de secretos en repos»
- **Qué es:** Herramienta de código abierto (AGPL-3.0) de Truffle Security, que financia el proyecto con una edición Enterprise de monitorización continua. Muy activa.
- **Cuándo elegirlo:** Casos: auditar los repositorios de una organización en busca de claves activas; revisar buckets o logs exportados antes de compartirlos.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install trufflehog` — fuente: https://github.com/trufflesecurity/trufflehog/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta la imagen Docker contra el repositorio de pruebas trufflesecurity/test_keys como indica el README. Éxito: El informe muestra las claves encontradas y si están verificadas.
- **Combina con:** `pre-commit`, `semgrep` [16/defensa], `claude-code` [20/terminal]
- **Alternativas:** `gitleaks`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): gitleaks.

### ast-grep (`ast-grep`)

- **Repo:** https://github.com/ast-grep/ast-grep · MIT · nivel 1 · 60/100
- **Qué es:** ast-grep (sg), CLI en Rust para búsqueda estructural, lint y reescritura de código, de @HerringtonDarkholme. Licencia MIT. Es activa (~17k estrellas, 0.51.2).
- **Cuándo elegirlo:** Casos: Migrar llamadas de una API; Aplicar reglas de lint personalizadas.
- **Requisitos:** nivel 1: preparación sencilla; Node y npm para esta ruta; archivos de prueba; hardware prerequisites; API de IA: no; Node y npm para esta ruta; archivos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install --global @ast-grep/cli` — fuente: https://github.com/ast-grep/ast-grep/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Busca una llamada por su estructura y revisa los resultados antes de reescribir Éxito: Encuentras la expresión aunque varíe el espaciado
- **Combina con:** `tree-sitter` [7/codigo], `claude-code` [20/terminal], `aider` [20/terminal]
- **Alternativas:** `semgrep`
- **Riesgos y avisos:** Alternativas (elige una): semgrep. Empieza por búsqueda; revisa el diff de una reescritura antes de aplicarla al proyecto entero.

### SonarQube Community Build (`sonarqube`)

- **Repo:** https://github.com/SonarSource/sonarqube · LGPL-3.0 · nivel 2 · 57/100
- **Qué es:** Código de SonarQube Community Build, la edición gratuita y de código abierto (LGPL-3.0) de la plataforma de SonarSource. Proyecto muy maduro; las ediciones superiores son comerciales.
- **Cuándo elegirlo:** Casos: vigilar la calidad y seguridad de un repositorio en cada PR; revisar el código generado por IA con reglas consistentes antes de fusionarlo.
- **Requisitos:** nivel 2: preparación media; Java, build.gradle; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/SonarSource/sonarqube/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca la imagen Docker oficial, crea un proyecto y analiza un repositorio pequeño con el escáner. Éxito: El panel muestra problemas, puntos críticos y la puerta de calidad del proyecto.
- **Combina con:** `ruff`, `claude-code` [20/terminal], `coolify` [22/infraestructura]
- **Alternativas:** `semgrep`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): semgrep.

### SWE-bench (`swe-bench`)

- **Repo:** https://github.com/SWE-bench/SWE-bench · MIT · nivel 3 · 52/100
- **Qué es:** SWE-bench, benchmark para evaluar si los modelos resuelven issues reales de GitHub, presentado en ICLR 2024 (oral) y ampliado con SWE-bench Multimodal (ICLR 2025). Licencia MIT.
- **Cuándo elegirlo:** Casos: Comparar soluciones a issues reproducibles; Estudiar evaluación de agentes de programación.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él; Python; Docker para evaluación; predicciones y tareas elegidas; hardware prerequisites; API de IA: opcional; Python; Docker para evaluación; predicciones y tareas elegidas.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/SWE-bench/SWE-bench/blob/main/README.md

  ```bash
  git clone git@github.com:SWE-bench/SWE-bench.git
  cd SWE-bench
  pip install -e .
  ```
- **Primera prueba propuesta (no ejecutada):** Evalúa una predicción ya preparada sobre una tarea pequeña antes de generar nuevas soluciones Éxito: El informe muestra si las pruebas del entorno aceptan el parche
- **Combina con:** `openhands` [20/ingenieria], `aider` [20/terminal], `codex` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Muy exigente en disco y CPU. El benchmark no demuestra que un agente resuelva cualquier issue real; usa el conjunto y la versión de tareas correspondientes.

### openai-python (`openai-python`)

- **Repo:** https://github.com/openai/openai-python · Apache-2.0 · nivel 2 · 75/100
- **Qué es:** SDK oficial de OpenAI para Python. Licencia Apache-2.0. Es madura y muy activa (~32k estrellas, v3.51.0) y se genera a partir de la especificación OpenAPI de OpenAI.
- **Cuándo elegirlo:** Casos: Integrar respuestas de IA en una app Python; Procesar audio o imágenes desde código.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él, requiere clave de API; Python 3.10+; entorno virtual; clave de proyecto API; hardware prerequisites; API de IA: sí; Python 3.10+; entorno virtual; clave de proyecto API.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/openai/openai-python/blob/main/README.md

  ```sh
  # install from PyPI
  pip install openai
  ```
- **Primera prueba propuesta (no ejecutada):** Envía una petición breve de ejemplo y revisa respuesta y uso informado Éxito: Obtienes la salida del endpoint y puedes localizar el consumo del proyecto
- **Combina con:** `litellm` [23/serving], `vllm` [23/serving], `langchain` [3/py], `openai-agents-python` [3/py], `openai-cookbook` [19/guias]
- **Riesgos y avisos:** Sin alternativas declaradas. Es un cliente oficial de API, no un plugin de Codex; base_url configurable no confirma todas las funciones de servidores locales.

### GitHub CLI (`cli`)

- **Repo:** https://github.com/cli/cli · MIT · nivel 1 · 74/100
- **Qué es:** GitHub CLI (`gh`), la herramienta oficial de GitHub para la terminal. Licencia MIT. Es madura y muy activa (~47k estrellas, v2.104.0).
- **Cuándo elegirlo:** Casos: Consultar issues desde terminal; Revisar ejecuciones de Actions.
- **Requisitos:** nivel 1: preparación sencilla; Binario gh oficial; cuenta GitHub para operaciones autenticadas; hardware prerequisites; API de IA: no; Binario gh oficial; cuenta GitHub para operaciones autenticadas.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/cli/cli.git gh-cli` — fuente: https://github.com/cli/cli/blob/trunk/docs/install_source.md
- **Primera prueba propuesta (no ejecutada):** Autentica tu cuenta y consulta el estado de una pull request de un repositorio de prueba Éxito: Ves el estado que coincide con la interfaz de GitHub
- **Combina con:** `claude-code` [20/terminal], `github-mcp-server` [5/servidores], `activepieces` [1/motores], `antigravity-awesome-skills` [2/catalogos], `awesome-copilot` [2/catalogos]
- **Riesgos y avisos:** Sin alternativas declaradas. Limita los scopes del token que uses con agentes. Instala gh antes de instalar su skill opcional; los comandos que escriben o publican afectan la cuenta autenticada.

### lazygit (`lazygit`)

- **Repo:** https://github.com/jesseduffield/lazygit · MIT · nivel 1 · 72/100
- **Qué es:** Interfaz de terminal para git de código abierto (MIT) creada por Jesse Duffield y mantenida con la comunidad y patrocinadores. Muy popular y activa.
- **Cuándo elegirlo:** Casos: revisar y preparar por partes los cambios que hizo un agente antes de confirmarlos; hacer rebases interactivos y deshacer operaciones sin recordar comandos.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install lazygit` — fuente: https://github.com/jesseduffield/lazygit/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala lazygit y ábrelo en un repositorio de prueba con cambios sin confirmar. Éxito: Puedes preparar una sola línea y crear el commit desde la interfaz.
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `aider` [20/terminal]
- **Riesgos y avisos:** Lazygit ejecuta comandos git reales: las operaciones destructivas (reset, force push) siguen siendo destructivas.

### fzf (`fzf`)

- **Repo:** https://github.com/junegunn/fzf · MIT · nivel 1 · 68/100
- **Qué es:** Buscador difuso de propósito general de código abierto (MIT) creado y mantenido por Junegunn Choi desde 2013. Muy maduro y extendido.
- **Cuándo elegirlo:** Casos: buscar archivos y comandos del historial al instante en la terminal; construir menús interactivos en scripts de shell.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Gemfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install fzf` — fuente: https://github.com/junegunn/fzf/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala fzf, activa la integración de tu shell y pulsa CTRL-T para elegir un archivo. Éxito: El selector filtra miles de archivos al escribir y pega la ruta elegida en la línea de comandos.
- **Combina con:** `ripgrep`, `claude-code` [20/terminal], `codex` [20/terminal]
- **Riesgos y avisos:** Es una herramienta de uso diario: no requiere servidor ni configuración para empezar.

### Requests Cache (`requests-cache`)

- **Repo:** https://github.com/requests-cache/requests-cache · BSD-2-Clause · nivel 2 · 59/100
- **Qué es:** Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas y reducir viajes repetidos a un servicio HTTP.
- **Cuándo elegirlo:** Casos: Evitar repetir la descarga de una lista pública durante pruebas.; Medir cuántas veces una tarea de ejemplo vuelve a consultar el servidor.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, docker-compose.yml, pyproject.toml; API de IA: no; Python y una aplicación que use requests; SQLite disponible para un ejemplo local..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://requests-cache.readthedocs.io/
- **Primera prueba propuesta (no ejecutada):** Configura una sesión de caché en un ejemplo con dos lecturas de la misma página de prueba. Éxito: La primera lectura consulta el servidor y la siguiente puede reutilizar la respuesta guardada.
- **Riesgos y avisos:** Expira la caché según los datos y evita almacenar respuestas con credenciales o información privada.

### APScheduler (`apscheduler`)

- **Repo:** https://github.com/agronholm/apscheduler · MIT · nivel 2 · 58/100
- **Qué es:** Programa funciones Python para un horario, un intervalo o una fecha concreta dentro de una aplicación propia.
- **Cuándo elegirlo:** Casos: Actualizar un dato local cada minuto.; Programar un recordatorio interno una vez al día.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, docker-compose.yml, pyproject.toml; API de IA: no; Python y una versión estable 3.x conforme a su guía..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://apscheduler.readthedocs.io/en/3.x/userguide.html
- **Primera prueba propuesta (no ejecutada):** Sigue la guía 3.x y programa una función de prueba que imprima la hora. Éxito: La función se ejecuta en el intervalo elegido y deja una marca visible.
- **Riesgos y avisos:** Haz la primera prueba solo con el almacén en memoria. GHSA-2r6w-vc63-g3hx afecta a los almacenes persistentes de 3.x y no indica parche; las preversiones….

### npkill (`npkill`)

- **Repo:** https://github.com/voidcosmos/npkill · MIT · nivel 1 · 58/100
- **Qué es:** Muestra cuánto espacio ocupan carpetas generadas por herramientas de desarrollo y permite revisarlas antes de eliminar residuos.
- **Cuándo elegirlo:** Casos: Medir el tamaño de node_modules en un proyecto de ejemplo.; Revisar sin borrar los residuos de un directorio de pruebas.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, package.json; API de IA: no; Node.js/npm para la distribución oficial y una carpeta de prueba sin datos importantes..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://npkill.js.org
- **Primera prueba propuesta (no ejecutada):** Usa el modo documentado de simulación dentro de la carpeta de prueba, sin confirmar eliminaciones. Éxito: Ves una lista de candidatos y los archivos del ejemplo siguen presentes.
- **Riesgos y avisos:** Una eliminación real puede ser irreversible. Verifica la ruta y el modo antes de confirmar; no barrer todo el disco para la primera prueba.

### Hishel (`hishel`)

- **Repo:** https://github.com/karpetrosyan/hishel · BSD-3-Clause · nivel 2 · 53/100
- **Qué es:** Añade caché a peticiones HTTP de Python con políticas de expiración y adaptadores de almacenamiento reutilizables.
- **Cuándo elegirlo:** Casos: Evitar pedir varias veces un catálogo público de prueba.; Probar una política de expiración con respuestas de un servidor local.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, package.json, pyproject.toml; API de IA: no; Python y el cliente HTTP soportado por el adaptador elegido..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://hishel.com
- **Primera prueba propuesta (no ejecutada):** Crea dos consultas iguales al ejemplo de prueba usando el adaptador de la guía. Éxito: La segunda consulta se sirve de la caché cuando las reglas lo permiten.
- **Riesgos y avisos:** No compartas una caché que contenga respuestas privadas entre usuarios. El tráfico remoto conserva sus propias cuotas.

### ripgrep (`ripgrep`)

- **Repo:** https://github.com/BurntSushi/ripgrep · Unlicense · nivel 1 · 52/100
- **Qué es:** Herramienta de búsqueda de código abierto con doble licencia MIT o Unlicense, creada por Andrew Gallant (BurntSushi). Muy madura; la usan editores como VS Code y muchos agentes de código.
- **Cuándo elegirlo:** Casos: localizar todas las apariciones de una función en un repositorio grande; buscar texto en miles de archivos de logs o notas en segundos.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install ripgrep` — fuente: https://github.com/BurntSushi/ripgrep/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala ripgrep y ejecuta `rg` con un patrón en un repositorio. Éxito: Obtienes las coincidencias con archivo y línea, sin resultados de carpetas ignoradas.
- **Combina con:** `fzf`, `claude-code` [20/terminal], `opencode` [20/terminal]
- **Riesgos y avisos:** Es la herramienta de búsqueda que asumen muchos agentes de terminal; conviene tenerla instalada.

### PyBreaker (`pybreaker`)

- **Repo:** https://github.com/danielfm/pybreaker · BSD-3-Clause · nivel 2 · 43/100
- **Qué es:** Protege una integración Python con un interruptor que pausa llamadas tras varios fallos y después permite comprobar si volvió el servicio.
- **Cuándo elegirlo:** Casos: Evitar que una integración lenta bloquee todos los trabajos.; Probar cómo se recupera un cliente tras una caída ficticia.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno Python con una función ficticia que pueda fallar..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/danielfm/pybreaker/blob/2b0b965fcfc7705ca9a776c614ea6cb3ec3fe783/README.rst
- **Primera prueba propuesta (no ejecutada):** Configura un ejemplo con una función local que falle repetidamente. Éxito: El interruptor abre y deja de invocar la función hasta el periodo de recuperación.
- **Riesgos y avisos:** Redis es opcional para guardar el estado compartido; no sirve por sí solo para reintentos ni para definir tiempos de espera.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-7.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Entender código y comprobar su calidad», lee `docs/alexandria/categoria-7.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-7.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
