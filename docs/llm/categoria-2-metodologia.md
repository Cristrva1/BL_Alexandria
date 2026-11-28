# Alexandría para agentes · Metodologías y harness para agentes de código

Categoría 2 «Skills, plugins y métodos para agentes» › subcategoría `metodologia`. 18 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=2&sub=metodologia · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `spec-kit` | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. | 1 Básico | 76 | MIT (OSI permisiva) | recomendado |
| `ponytail` | Skill que hace que tu agente de código piense como un senior minimalista: el… | 1 Básico | 74 | MIT (OSI permisiva) | sin grupo |
| `ecc` | Sistema de skills, hooks y configuración para agentes de código, con rutas… | 2 Intermedio | 72 | MIT (OSI permisiva) | recomendado |
| `elephant-goldfish-model` | Plugin con instrucciones para diseñar y revisar software con agentes mediante… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `gstack` | Conjunto de skills y herramientas para organizar planificación, implementación… | 2 Intermedio | 66 | MIT (OSI permisiva) | alternativa |
| `agent-skills` | Colección de Addy Osmani con skills de ingeniería para especificar, planificar… | 1 Básico | 64 | MIT (OSI permisiva) | alternativa |
| `book-to-skill` | Herramientas para convertir un libro técnico en PDF en una skill que un agente… | 2 Intermedio | 64 | MIT (OSI permisiva) | sin grupo |
| `skills` | Skills de ingeniería de Matt Pocock para trabajar sobre requisitos, diseño… | 1 Básico | 62 | MIT (OSI permisiva) | sin grupo |
| `superpowers` | Metodología completa de desarrollo para agentes construida sobre skills… | 1 Básico | 59 | MIT (OSI permisiva) | alternativa |
| `bmad-method` | Metodología ágil con agentes especializados (analista, PM, arquitecto, dev)… | 1 Básico | 58 | MIT (OSI permisiva) | alternativa |
| `codex-plugin-cc` | Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y… | 1 Básico | 56 | Apache-2.0 (OSI permisiva) | sin grupo |
| `claude-token-efficient` | Instrucciones para reducir la verbosidad de Claude Code y medir el coste de… | 1 Básico | 47 | MIT (OSI permisiva) | sin grupo |
| `andrej-karpathy-skills` | Instrucciones para declarar supuestos, simplificar cambios y comprobar… | 1 Básico | 46 | — (sin licencia detectada) | sin grupo |
| `shadcn-improve` | Organiza una auditoría de código en un plan que un modelo diferente puede… | 2 Intermedio | 45 | MIT (OSI permisiva) | sin grupo |
| `agent-toolkit` | Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code… | 1 Básico | 43 | MIT (OSI permisiva) | sin grupo |
| `humans-md-plugins` | Carga preferencias de trabajo de un archivo HUMANS.md al iniciar una sesión en… | 2 Intermedio | 43 | Apache-2.0 (OSI permisiva) | sin grupo |
| `grok-plugin-claude-code` | Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante… | 1 Básico | 34 | MIT (OSI permisiva) | sin grupo |
| `claude-code-hooks-mastery` | Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar… | 1 Básico | 31 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Spec Kit (`spec-kit`)

- **Repo:** https://github.com/github/spec-kit · MIT · nivel 1 · 76/100 · recomendado en «Desarrollo guiado por especificaciones»
- **Qué es:** Kit de código abierto de GitHub (MIT) que da a los agentes de código procesos estructurados, plantillas reutilizables y resultados documentados. Muy activo (v1.4.0).
- **Cuándo elegirlo:** Casos: Especificar una función con requisitos y criterios de aceptación; Mantener un flujo común en un equipo que usa agentes diferentes.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Python y uv según la guía;  un agente con integración soportada; hardware prerequisites; API de IA: no; Python y uv según la guía; un agente con integración soportada.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/github/spec-kit.git` — fuente: https://github.github.io/spec-kit/install/air-gapped.html
- **Primera prueba propuesta (no ejecutada):** Inicializa un proyecto de prueba y selecciona su integración antes de crear una especificación Éxito: El proyecto contiene el scaffolding y los comandos o skills de ese agente
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal], `awesome-copilot` [2/catalogos], `elephant-goldfish-model`
- **Alternativas:** `bmad-method`, `claude-task-master`
- **Riesgos y avisos:** Alternativas (elige una): bmad-method, claude-task-master. La guía actual usa integration y claves claude, codex y agy; no reutilizar comandos de versiones antiguas sin comprobarlos.

### Ponytail (`ponytail`)

- **Repo:** https://github.com/DietrichGebert/ponytail · MIT · nivel 1 · 74/100
- **Qué es:** Skill de DietrichGebert (MIT) que hace que el agente escriba solo el código necesario. Activa (v5.3.3); sus benchmarks son del propio proyecto.
- **Cuándo elegirlo:** Casos: Revisar deuda técnica y detectar código que se puede eliminar; Evaluar alternativas sencillas antes de crear una abstracción nueva.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente compatible;  proyecto donde comparar un cambio pequeño; hardware prerequisites; API de IA: no; Agente compatible; proyecto donde comparar un cambio pequeño.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/DietrichGebert/ponytail/blob/main/README.md

  ```bash
  /plugin marketplace add DietrichGebert/ponytail

  /plugin install ponytail@ponytail
  ```
- **Primera prueba propuesta (no ejecutada):** Solicita resolver un problema reutilizando el código existente antes de añadir funciones Éxito: La propuesta explica qué reutiliza y presenta un diff limitado
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `andrej-karpathy-skills`
- **Riesgos y avisos:** Se quitó superpowers porque no hay integración. Codex tiene hooks propios; los adaptadores de solo instrucciones no ofrecen todos los comandos ni la banda de estado.

### ECC (`ecc`)

- **Repo:** https://github.com/affaan-m/ECC · MIT · nivel 2 · 72/100 · recomendado en «Metodologías y harness para agentes de código»
- **Qué es:** ECC, de affaan-m, se presenta como un «sistema operativo de harness» para agentes (MIT). Es open core: el producto ECC Pro es una GitHub App de pago para repositorios privados.
- **Cuándo elegirlo:** Casos: Configurar convenciones, skills y comprobaciones para un equipo; Probar una mejora de contexto sin activar todos los componentes.
- **Requisitos:** nivel 2: preparación pesada, se instala dentro de un agente (skill, plugin o MCP); Node.js compatible;  Git y cliente que elegirá el instalador; hardware prerequisites; API de IA: no; Node.js compatible; Git y cliente que elegirá el instalador.
- **Instalación (documentada en la fuente; no ejecutada):** `npx ecc-universal@2.2.3 setup` — fuente: https://github.com/affaan-m/ECC/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta la configuración guiada en una carpeta de prueba y revisa el destino antes de confirmar Éxito: El informe muestra los componentes y archivos preparados para el cliente elegido
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal], `gemini-cli` [20/terminal], `claude-code-hooks-mastery`, `hermes-agent` [21/asistentes]
- **Alternativas:** `gstack`, `agent-skills`, `superpowers`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): superpowers, gstack. El README pide instalar solo desde canales oficiales: el repositorio y sus paquetes npm verificados. Ahora el repositorio es ECC. Hay rutas nativas para Claude Code y Codex y adaptadores de capacidad limitada para otros clientes.

### elephant-goldfish-model (`elephant-goldfish-model`)

- **Repo:** https://github.com/google/elephant-goldfish-model · Apache-2.0 · nivel 2 · 68/100
- **Qué es:** EGM, plugin de código abierto de Google (Apache 2.0) para asistentes de IA, que separa diseñar con contexto de revisar con ojos frescos. Muy reciente (v0.1.1).
- **Cuándo elegirlo:** Casos: Documentar alternativas para una funcionalidad antes de elegir una; Revisar una especificación con un contexto de lectura renovado.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Cliente compatible;  una propuesta o documento propio para revisar; hardware prerequisites; API de IA: no; Cliente compatible; una propuesta o documento propio para revisar.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/google/elephant-goldfish-model/blob/main/README.md

  ```sh
  claude plugin marketplace add google/elephant-goldfish-model
  claude plugin install egm@egm
  ```
- **Primera prueba propuesta (no ejecutada):** Plantea una decisión de diseño y pide una revisión con una perspectiva nueva Éxito: Obtienes un brief y observaciones que puedes contrastar con el contexto inicial
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `spec-kit`
- **Riesgos y avisos:** El repositorio de Google declara que no es un producto con soporte oficial; cada host tiene una guía propia.

### gstack (`gstack`)

- **Repo:** https://github.com/garrytan/gstack · MIT · nivel 2 · 66/100 · alternativa en «Metodologías y harness para agentes de código»
- **Qué es:** «Fábrica de software» de código abierto (MIT) de Garry Tan, presidente y CEO de Y Combinator, que convierte Claude Code y otros agentes en un equipo de ingeniería virtual. Muy activo (v1.99.4.0), con canal estable y releases frecuentes.
- **Cuándo elegirlo:** Casos: Preparar una revisión de producto antes de implementar; Abrir un navegador de prueba para revisar una interfaz propia.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Git, Bun y cliente autenticado;  en Windows revisar Git Bash o WSL y Node.js; hardware prerequisites; API de IA: no; Git, Bun y cliente autenticado; en Windows revisar Git Bash o WSL y Node.js.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/garrytan/gstack/blob/main/README.md

  ```bash
  git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
  cd ~/gstack && ./setup --host auto      # or: ./setup --host codex
  ./setup --status                         # one row per install: host, tier, scope, version, path
  ```
- **Primera prueba propuesta (no ejecutada):** Consulta el estado de instalación y prueba una revisión o planificación sobre un cambio pequeño Éxito: El estado indica el host y puedes revisar el resultado de la skill elegida
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal]
- **Alternativas:** `ecc`, `agent-skills`, `superpowers`
- **Riesgos y avisos:** Alternativas (elige una): superpowers, ecc. Los hosts Codex y Antigravity aparecen como experimentales y con comprobaciones advisory; no se equiparan a la ruta completa de Claude Code.

### Agent Skills (Addy Osmani) (`agent-skills`)

- **Repo:** https://github.com/addyosmani/agent-skills · MIT · nivel 1 · 64/100 · alternativa en «Metodologías y harness para agentes de código»
- **Qué es:** Skills de ingeniería de Addy Osmani (MIT) para agentes de código, centradas en procesos de nivel producción. Activas (0.6.16).
- **Cuándo elegirlo:** Casos: Preparar una especificación antes de escribir una funcionalidad; Revisar un diff con criterios de calidad y pruebas.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Node.js y un agente compatible;  instalar solo las skills necesarias; hardware prerequisites; API de IA: no; Node.js y un agente compatible; instalar solo las skills necesarias.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/addyosmani/agent-skills/blob/main/README.md

  ```bash
  npx skills add addyosmani/agent-skills            # install all 25 skills
  npx skills add addyosmani/agent-skills --list     # browse before installing
  ```
- **Primera prueba propuesta (no ejecutada):** Pide una revisión de calidad sobre un cambio pequeño del proyecto Éxito: La revisión aplica los criterios de la skill y señala archivos concretos
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal], `plugins` [2/catalogos]
- **Alternativas:** `ecc`, `gstack`, `superpowers`
- **Riesgos y avisos:** Alternativa (elige una): superpowers. Antigravity tiene una guía propia y limitaciones de comandos en algunas versiones; usa las skills subyacentes cuando corresponda.

### book-to-skill (`book-to-skill`)

- **Repo:** https://github.com/virgiliojr94/book-to-skill · MIT · nivel 2 · 64/100
- **Qué es:** Skill de virgiliojr94 (MIT) que convierte libros técnicos, carpetas de documentos o colecciones de fuentes en una skill de agente unificada. Activa (v1.4.0).
- **Cuándo elegirlo:** Casos: Preparar una guía de consulta a partir de documentación interna; Convertir notas técnicas propias en instrucciones reutilizables del agente.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente con Agent Skills;  un documento propio o autorizado de pocas páginas; hardware prerequisites; API de IA: no; Agente con Agent Skills; un documento propio o autorizado de pocas páginas.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/virgiliojr94/book-to-skill/blob/master/README.md

  ```bash
  # One command, any host — via the cross-agent skills CLI:
  npx skills add virgiliojr94/book-to-skill
  ```
- **Primera prueba propuesta (no ejecutada):** Convierte un extracto técnico propio en una skill y revisa el SKILL.md generado Éxito: La skill resume el ámbito, conserva referencias y responde una pregunta sobre ese extracto
- **Combina con:** `docling` [13/conversion], `claude-code` [20/terminal], `hermes-agent` [21/asistentes]
- **Riesgos y avisos:** Convierte solo libros cuyos derechos tengas: la skill generada contiene el contenido del libro. La portabilidad corresponde al estándar Agent Skills; empieza con material propio y revisa qué contenido puede redistribuirse.

### skills (`skills`)

- **Repo:** https://github.com/mattpocock/skills · MIT · nivel 1 · 62/100
- **Qué es:** Skills de agente de Matt Pocock (MIT) para «ingeniería real, no vibe coding»: pequeñas, adaptables y combinables. Activas (v1.3.2).
- **Cuándo elegirlo:** Casos: Revisar requisitos de una función antes de implementarla; Organizar una refactorización pequeña con un plan revisable.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude Code o Codex;  carpeta de prueba para la primera skill; hardware prerequisites; API de IA: no; Claude Code o Codex; carpeta de prueba para la primera skill.
- **Instalación (documentada en la fuente; no ejecutada):** `claude plugin install mattpocock-skills@claude-plugins-official` — fuente: https://github.com/mattpocock/skills/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una skill de ingeniería e invócala sobre una tarea acotada Éxito: El agente aplica la skill y produce el artefacto que esa tarea pide
- **Combina con:** `claude-code` [20/terminal], `claude-plugins-official` [2/catalogos], `codex` [20/terminal], `plugins` [2/catalogos]
- **Riesgos y avisos:** Se quitó awesome-agent-skills: es un catálogo, no una integración. El README actual ya documenta plugins para Claude Code y Codex; se corrige la ficha que los dejaba sin documentar.

### superpowers (`superpowers`)

- **Repo:** https://github.com/obra/superpowers · MIT · nivel 1 · 59/100 · alternativa en «Metodologías y harness para agentes de código»
- **Qué es:** Metodología completa de desarrollo para agentes de código de Jesse Vincent y Prime Radiant (MIT), basada en skills combinables. Muy activa (v7.0.2); Prime Radiant ofrece soporte comercial.
- **Cuándo elegirlo:** Casos: Dividir una funcionalidad en tareas que se puedan verificar; Trabajar con pruebas y revisión antes de cerrar un cambio.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Cliente compatible;  proyecto pequeño o carpeta de prueba; hardware prerequisites; API de IA: no; Cliente compatible; proyecto pequeño o carpeta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `/plugin install superpowers@claude-plugins-official` — fuente: https://github.com/obra/superpowers/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Describe una mejora sencilla y revisa la fase de definición y planificación Éxito: El agente muestra una propuesta acotada antes de cambiar archivos
- **Combina con:** `claude-plugins-official` [2/catalogos], `codex` [20/terminal], `gemini-cli` [20/terminal], `hermes-agent` [21/asistentes], `claude-code` [20/terminal]
- **Alternativas:** `ecc`, `gstack`, `agent-skills`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): agent-skills, ecc, gstack. Se quitaron awesome-claude-code y agent-toolkit porque no hay integración. Claude Code, Codex y Antigravity tienen rutas de instalación propias en el README.

### BMAD Method (`bmad-method`)

- **Repo:** https://github.com/bmad-code-org/BMAD-METHOD · MIT · nivel 1 · 58/100 · alternativa en «Desarrollo guiado por especificaciones»
- **Qué es:** BMad Method es un marco de «desarrollo ágil dirigido por IA» de bmad-code-org. El README declara licencia MIT, aunque GitHub la marca como NOASSERTION.
- **Cuándo elegirlo:** Casos: Convertir una idea de producto en un primer cambio acotado; Revisar requisitos y decisiones antes de implementar una función.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Node.js, Git y uv;  cliente compatible con Agent Skills; hardware prerequisites; API de IA: no; Node.js, Git y uv; cliente compatible con Agent Skills.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md

  ```bash
  npx skills add bmad-code-org/BMAD-METHOD/skills/core-tools --skill '*'
  npx skills add bmad-code-org/BMAD-METHOD/skills/method --skill '*'
  ```
- **Primera prueba propuesta (no ejecutada):** Instala los módulos de la ruta elegida y pide configurar una primera mejora pequeña Éxito: El agente identifica el método y deja un plan o artefacto de trabajo revisable
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `skillspector` [16/skills]
- **Alternativas:** `spec-kit`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): spec-kit. Usa la v6.12 si necesitas estabilidad. El README distingue la versión estable del preview V7. Los comandos seleccionados son del preview: pueden cambiar y no deben mezclarse con la guía estable.

### codex-plugin-cc (`codex-plugin-cc`)

- **Repo:** https://github.com/openai/codex-plugin-cc · Apache-2.0 · nivel 1 · 56/100
- **Qué es:** Plugin oficial de OpenAI (Apache 2.0) para usar Codex desde Claude Code. Versión v1.0.6; último cambio en julio de 2026.
- **Cuándo elegirlo:** Casos: Pedir una segunda revisión de un cambio desde Claude Code; Delegar una tarea acotada a Codex manteniendo el contexto principal.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude Code;  Codex CLI autenticado y acceso a su cuenta; hardware prerequisites; API de IA: opcional; Claude Code; Codex CLI autenticado y acceso a su cuenta.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/openai/codex-plugin-cc/blob/main/README.md

  ```bash
  /plugin marketplace add openai/codex-plugin-cc

  /plugin install codex@openai-codex
  ```
- **Primera prueba propuesta (no ejecutada):** Pide revisar un diff pequeño mediante el comando del plugin y examina su informe Éxito: La delegación devuelve una revisión atribuible al proceso de Codex
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `grok-plugin-claude-code`
- **Riesgos y avisos:** No es una skill que se instala dentro de Codex: es un puente desde Claude Code hacia el CLI de Codex.

### claude-token-efficient (`claude-token-efficient`)

- **Repo:** https://github.com/drona23/claude-token-efficient · MIT · nivel 1 · 47/100
- **Qué es:** Un archivo `CLAUDE.md` de drona23 (MIT) para que Claude responda de forma concisa y gaste menos tokens. Sin releases; último cambio en junio de 2026.
- **Cuándo elegirlo:** Casos: Reducir respuestas repetitivas en una sesión larga; Mantener un estilo de comunicación conciso para tareas de código.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude Code;  copia revisable de las instrucciones del proyecto; hardware prerequisites; API de IA: no; Claude Code; copia revisable de las instrucciones del proyecto.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/drona23/claude-token-efficient/blob/main/README.md

  ```bash
  git clone https://github.com/drona23/claude-token-efficient
  cp claude-token-efficient/profiles/CLAUDE.coding.md your-project/CLAUDE.md
  ```
- **Primera prueba propuesta (no ejecutada):** Aplica un perfil en una carpeta de prueba y pide una respuesta breve con criterios concretos Éxito: Puedes comparar extensión y claridad sin perder la información necesaria
- **Combina con:** `claude-code` [20/terminal], `andrej-karpathy-skills`, `claude-code-usage-monitor` [23/observabilidad]
- **Riesgos y avisos:** Los resultados con modelos locales se declaran sin probar; no se presentan como compatibilidad validada.

### andrej-karpathy-skills (`andrej-karpathy-skills`)

- **Repo:** https://github.com/multica-ai/andrej-karpathy-skills · — · nivel 1 · 46/100
- **Qué es:** Un solo archivo `CLAUDE.md`, con plugin de Claude Code, basado en las observaciones de Andrej Karpathy sobre los fallos de los LLM al programar. Lo mantiene multica-ai, cuyo autor promociona su plataforma Multica.
- **Cuándo elegirlo:** Casos: Evitar una refactorización amplia para corregir un fallo pequeño; Hacer explícitas dudas y criterios de éxito antes de programar.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude Code;  revisar las instrucciones que ya existen en el proyecto; hardware prerequisites; API de IA: no; Claude Code; revisar las instrucciones que ya existen en el proyecto.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md

  ```bash
  /plugin marketplace add forrestchang/andrej-karpathy-skills

  /plugin install andrej-karpathy-skills@karpathy-skills
  ```
- **Primera prueba propuesta (no ejecutada):** Pide un cambio pequeño y observa si declara supuestos y limita el alcance Éxito: La propuesta identifica lo que cambiará y cómo comprobar el resultado
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `multica` [21/asistentes], `claude-token-efficient`, `ponytail`
- **Riesgos y avisos:** Sin licencia declarada. Se quitaron awesome-claude-code y context-engineering porque no hay integración. Son principios inspirados en observaciones de Karpathy, no un proyecto publicado por él ni una garantía de calidad.

### Improve de shadcn (`shadcn-improve`)

- **Repo:** https://github.com/shadcn/improve · MIT · nivel 2 · 45/100
- **Qué es:** Organiza una auditoría de código en un plan que un modelo diferente puede implementar después de una revisión humana.
- **Cuándo elegirlo:** Casos: Separar el análisis de un formulario y su corrección.; Convertir un diagnóstico de rendimiento en tareas verificables. Evítalo si no usas un agente compatible con skills.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); API de IA: no; Un agente con soporte de skills y un repositorio desechable o una copia de prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/shadcn/improve/blob/cac56e1ebd3c279aa9153616cfeac7b174ab90f9/README.md
- **Primera prueba propuesta (no ejecutada):** Revisa un módulo pequeño con la skill y solicita solo el plan, sin aplicar cambios. Éxito: El plan nombra archivos, cambios propuestos y una forma de comprobarlos.
- **Riesgos y avisos:** Los modelos se pagan o limitan por el anfitrión; el proyecto no incluye un modelo ni promete ahorro fijo.

### agent-toolkit (`agent-toolkit`)

- **Repo:** https://github.com/softaworks/agent-toolkit · MIT · nivel 1 · 43/100
- **Qué es:** Skills «con opinión» de @leonardocouy (Softaworks), con licencia MIT y en formato Agent Skills, pensadas para ganar eficiencia en Claude Code. Sin releases; último cambio en marzo de 2026.
- **Cuándo elegirlo:** Casos: Aclarar una petición ambigua antes de programar; Documentar el contrato entre frontend y backend.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Node.js;  agente compatible y una skill escogida; hardware prerequisites; API de IA: no; Node.js; agente compatible y una skill escogida.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add softaworks/agent-toolkit` — fuente: https://github.com/softaworks/agent-toolkit/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona una skill de requisitos y úsala con una descripción breve de una función Éxito: Recibes preguntas o un documento de requisitos que puedes corregir
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `skillspector` [16/skills]
- **Riesgos y avisos:** Se quitó superpowers porque no hay integración. La ruta skills CLI es portable; el marketplace y sus comandos propios pertenecen a Claude Code.

### HUMANS.md Plugins (`humans-md-plugins`)

- **Repo:** https://github.com/cmdai-hq/humans-md-plugins · Apache-2.0 · nivel 2 · 43/100
- **Qué es:** Carga preferencias de trabajo de un archivo HUMANS.md al iniciar una sesión en asistentes compatibles con el plugin.
- **Cuándo elegirlo:** Casos: Pedir que el agente avise antes de modificar archivos de configuración.; Reutilizar preferencias de comunicación entre dos clientes compatibles. Evítalo si no usas un agente compatible con skills.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); JavaScript, package.json; API de IA: no; Node.js 22.18 o posterior según el README, un anfitrión compatible y perfil de prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://humansmd.dev/
- **Primera prueba propuesta (no ejecutada):** Crea un perfil con una sola preferencia ficticia y abre una nueva sesión. Éxito: El agente puede leer y explicar esa preferencia sin cargar notas reales.
- **Riesgos y avisos:** El autor indica pruebas solo en macOS. El proveedor del agente puede procesar el perfil; no guardes contraseñas ni datos sensibles.

### grok-plugin-claude-code (`grok-plugin-claude-code`)

- **Repo:** https://github.com/zachdunn/grok-plugin-claude-code · MIT · nivel 1 · 34/100
- **Qué es:** Plugin no oficial de zachdunn (MIT) para Claude Code que delega tareas en Grok CLI de xAI. Versión v0.2.0; último cambio en junio de 2026.
- **Cuándo elegirlo:** Casos: Solicitar una segunda opinión sobre un cambio pequeño usando Grok; Delegar una tarea acotada desde una sesión de Claude Code.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude Code;  Grok CLI instalado y autenticado;  Node.js; hardware prerequisites; API de IA: unconfirmed; Claude Code; Grok CLI instalado y autenticado; Node.js.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md

  ```text
  /plugin marketplace add zachdunn/grok-plugin-claude-code
  /plugin install grok-cc@grok-plugin-claude-code
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta la comprobación setup del plugin antes de delegar una tarea de prueba Éxito: El diagnóstico confirma que puede localizar y utilizar el CLI de Grok
- **Combina con:** `claude-code` [20/terminal], `codex-plugin-cc`, `codex` [20/terminal]
- **Riesgos y avisos:** Se elimina la falsa compatibilidad con Codex: se menciona como inspiración. La forma de cobro y API de Grok no queda resuelta por el README.

### claude-code-hooks-mastery (`claude-code-hooks-mastery`)

- **Repo:** https://github.com/disler/claude-code-hooks-mastery · — · nivel 1 · 31/100
- **Qué es:** Repositorio didáctico de disler (IndyDevDan) para dominar los hooks de Claude Code, con subagentes, estilos de salida y líneas de estado. Sin licencia declarada; último cambio en marzo de 2026.
- **Cuándo elegirlo:** Casos: Registrar cuándo empieza y termina una sesión de trabajo; Comprender un control que revisa una acción antes de ejecutarla.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Claude Code y uv;  revisar solo un ejemplo de hook y sus dependencias; hardware prerequisites; API de IA: opcional; Claude Code y uv; revisar solo un ejemplo de hook y sus dependencias.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/disler/claude-code-hooks-mastery/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Estudia un hook sencillo de sesión y adapta una comprobación en una carpeta de prueba Éxito: El hook produce el evento o registro esperado al activar esa fase de la sesión
- **Combina con:** `claude-code` [20/terminal], `ecc`, `claude-code-router` [23/serving]
- **Riesgos y avisos:** Sin licencia: úsalo como referencia didáctica. Se distingue el material de aprendizaje de un plugin automático; no hace falta activar todos los ejemplos ni sus servicios opcionales.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-2-metodologia.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Metodologías y harness para agentes de código», lee `docs/alexandria/categoria-2-metodologia.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-2-metodologia.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
