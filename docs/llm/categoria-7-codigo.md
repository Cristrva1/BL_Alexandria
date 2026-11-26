# Alexandría para agentes · Entender y empaquetar código para agentes

Categoría 7 «Entender código y comprobar su calidad» › subcategoría `codigo`. 7 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=7&sub=codigo · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `graphify` | CLI y skill que convierten código y documentos en un grafo consultable; el… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `codegraph` | CLI que indexa tu código en local para que los asistentes de IA entiendan… | 1 Básico | 66 | MIT (OSI permisiva) | alternativa |
| `tree-sitter` | Sistema de parsing incremental para herramientas de programación, base de… | 2 Intermedio | 60 | MIT (OSI permisiva) | sin grupo |
| `codebase-memory-mcp` | Motor local de inteligencia de código que conecta código, docs e… | 1 Básico | 58 | MIT (OSI permisiva) | alternativa |
| `floorplan` | Herramienta para que Claude o Codex genere un mapa interactivo y explicado de… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `repomix` | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | 1 Básico | 53 | MIT (OSI permisiva) | alternativa |
| `gitnexus` | Herramienta visual para explorar y entender repositorios Git, mostrando… | 1 Básico | 51 | PolyForm-Noncommercial-1.0.0 (source-available) | alternativa |

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-7-codigo.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Entender y empaquetar código para agentes», lee `docs/alexandria/categoria-7-codigo.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-7-codigo.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
