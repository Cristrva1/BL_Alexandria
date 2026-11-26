# Alexandría para agentes · Calidad, seguridad y benchmarks de código

Categoría 7 «Entender código y comprobar su calidad» › subcategoría `calidad`. 9 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=7&sub=calidad · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `ruff` | Linter y formateador de Python extremadamente rápido escrito en Rust… | 1 Básico | 74 | MIT (OSI permisiva) | sin grupo |
| `biome` | Formateador y linter en un solo binario para JavaScript, TypeScript, JSX, JSON… | 1 Básico | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `open-code-review` | Revisa cambios de código con reglas y un informe guiado, usando su propio… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `gitleaks` | Detector de secretos (contraseñas, claves de API, tokens) en repositorios git… | 1 Básico | 63 | MIT (OSI permisiva) | recomendado |
| `pre-commit` | Framework para gestionar y ejecutar hooks de git multilenguaje antes de cada… | 1 Básico | 62 | MIT (OSI permisiva) | sin grupo |
| `trufflehog` | Busca, clasifica, verifica y analiza credenciales filtradas en git, chats… | 1 Básico | 61 | AGPL-3.0 (OSI copyleft) | alternativa |
| `ast-grep` | CLI en Rust para búsqueda estructural, lint y reescritura de código usando… | 1 Básico | 60 | MIT (OSI permisiva) | sin grupo |
| `sonarqube` | Plataforma de inspección continua de calidad y seguridad del código: análisis… | 2 Intermedio | 57 | LGPL-3.0 (OSI copyleft) | sin grupo |
| `swe-bench` | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. | 3 Avanzado | 52 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-7-calidad.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Calidad, seguridad y benchmarks de código», lee `docs/alexandria/categoria-7-calidad.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-7-calidad.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
