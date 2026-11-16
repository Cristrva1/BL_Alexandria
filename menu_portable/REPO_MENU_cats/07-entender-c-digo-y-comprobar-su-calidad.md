# 7. Entender código y comprobar su calidad — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ast-grep`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=code,security,rust

**Qué es:** CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código.
**Stack:** Node y npm para esta ruta; archivos de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; solo recursos locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Empieza por búsqueda; revisa el diff de una reescritura antes de aplicarla al proyecto entero
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelo ni API; solo recursos locales
- Equipo: Preparación según la ruta elegida. Node y npm para esta ruta; archivos de prueba
**Repo:** https://github.com/ast-grep/ast-grep

**Instalación** [+]:

```
npm install --global @ast-grep/cli
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Migrar llamadas de una API; Aplicar reglas de lint personalizadas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca una llamada por su estructura y revisa los resultados antes de reescribir
**Qué comprobar:** Encuentras la expresión aunque varíe el espaciado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tree-sitter`, `claude-code`, `aider`
**Alternativas (elige una):** `semgrep`

## `biome`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=code,javascript,typescript,rust

**Qué es:** Formateador y linter en un solo binario para JavaScript, TypeScript, JSX, JSON, CSS, GraphQL y más, usable por CLI y LSP.
**Stack:** Rust, Cargo.toml, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/biomejs/biome

**Instalación** [+]:

```
npm install --save-dev --save-exact @biomejs/biome
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: sustituir ESLint y Prettier en un proyecto web por una sola herramienta; formatear y revisar el código que genera un agente antes de abrir un PR
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala `@biomejs/biome` como dependencia de desarrollo y ejecuta `npx @biomejs/biome check --write`.
**Qué comprobar:** Biome formatea y corrige los archivos y lista los problemas restantes.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pre-commit`, `tailwindcss`, `claude-code`

## `cli`
role=app · exec=cloud · setup=easy · mcp=False · prov=— · tags=code,go

**Qué es:** CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal.
**Stack:** Binario gh oficial; cuenta GitHub para operaciones autenticadas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa modelo; GitHub y acciones de la cuenta conservan sus límites y costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Instala gh antes de instalar su skill opcional; los comandos que escriben o publican afectan la cuenta autenticada
- Coste: Sin pago a un modelo en la ruta básica. No usa modelo; GitHub y acciones de la cuenta conservan sus límites y costes
- Equipo: Preparación según la ruta elegida. Binario gh oficial; cuenta GitHub para operaciones autenticadas
**Repo:** https://github.com/cli/cli

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/cli/cli/blob/trunk/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar issues desde terminal; Revisar ejecuciones de Actions
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Autentica tu cuenta y consulta el estado de una pull request de un repositorio de prueba
**Qué comprobar:** Ves el estado que coincide con la interfaz de GitHub
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `github-mcp-server`, `activepieces`, `antigravity-awesome-skills`, `awesome-copilot`

## `codebase-memory-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=code,mcp,memory

**Qué es:** Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes.
**Stack:** Binario para tu sistema; repositorio de prueba; Node 22+ solo para compilar CBM Lens
**Acceso y costes:**
- API de IA: API de IA opcional. La extracción y embeddings locales no requieren API; consultar un modelo u otros proveedores puede añadir consumo
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. Las funciones de hooks y actividad varían por cliente; los binarios ya compilados no necesitan Node para ejecutar Lens
- Coste: El coste depende del proveedor o la ruta. La extracción y embeddings locales no requieren API; consultar un modelo u otros proveedores puede añadir consumo
- Equipo: Preparación según la ruta elegida. Binario para tu sistema; repositorio de prueba; Node 22+ solo para compilar CBM Lens
**Repo:** https://github.com/DeusData/codebase-memory-mcp

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Navegar dependencias de código; Seleccionar pruebas afectadas por un cambio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa un proyecto pequeño y consulta el impacto de cambiar una función
**Qué comprobar:** Puedes abrir las referencias y relaciones del grafo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `repomix`, `codex`
**Alternativas (elige una):** `codegraph`, `gitnexus`, `serena`, `graphify`

## `codegraph`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=code,typescript

**Qué es:** CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo.
**Stack:** Instalador oficial o Node y npm; repositorio de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. El índice básico es local sin API; embeddings opcionales y el agente pueden consumir recursos o servicios según configuración
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: Modelos locales documentados. La compatibilidad con los tres clientes está documentada; comprueba indexación y sincronización antes de confiar en el mapa
- Coste: El coste depende del proveedor o la ruta. El índice básico es local sin API; embeddings opcionales y el agente pueden consumir recursos o servicios según configuración
- Equipo: Preparación según la ruta elegida. Instalador oficial o Node y npm; repositorio de prueba
**Repo:** https://github.com/colbymchenry/codegraph

**Instalación** [+]:

```
npm i -g @colbymchenry/codegraph
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una refactorización; Encontrar rutas de ejecución de un proyecto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa una carpeta y consulta quién llama a una función conocida
**Qué comprobar:** Los resultados identifican definiciones y relaciones comprobables
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `headroom`, `floorplan`
**Alternativas (elige una):** `codebase-memory-mcp`, `serena`, `gitnexus`, `graphify`

## `floorplan`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=codigo,skill,javascript

**Qué es:** Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.
**Stack:** Claude Code o Codex con plugins; proyecto pequeño de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La generación usa el agente anfitrión; el HTML resultante se consulta sin un modelo en ejecución
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El mapa offline no implica generación con IA local; el README cambió y esta ficha conserva la nueva versión de fuente
- Coste: Consumo del agente que ya utilizas. La generación usa el agente anfitrión; el HTML resultante se consulta sin un modelo en ejecución
- Equipo: Preparación según la ruta elegida. Claude Code o Codex con plugins; proyecto pequeño de prueba
**Repo:** https://github.com/haydenschmitty/floorplan

**Instalación** [+]:

```
claude plugin marketplace add haydenschmitty/floorplan
claude plugin install floorplan@floorplan
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar la arquitectura a alguien nuevo; Encontrar dónde se inicia una petición de la interfaz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide un mapa de una app mínima y abre un enlace entre una pantalla y su endpoint
**Qué comprobar:** Puedes contrastar nombres legibles, archivos y conexiones del mapa
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `codegraph`

## `fzf`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=cli,go,terminal

**Qué es:** Buscador difuso de línea de comandos y kit de interfaces de terminal para seleccionar archivos, historial o cualquier lista de forma interactiva.
**Stack:** Go, Dockerfile, Gemfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/junegunn/fzf

**Instalación** [+]:

```
brew install fzf
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: buscar archivos y comandos del historial al instante en la terminal; construir menús interactivos en scripts de shell
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala fzf, activa la integración de tu shell y pulsa CTRL-T para elegir un archivo.
**Qué comprobar:** El selector filtra miles de archivos al escribir y pega la ruta elegida en la línea de comandos.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ripgrep`, `claude-code`, `codex`

## `gitleaks`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,go,cli,code

**Qué es:** Detector de secretos (contraseñas, claves de API, tokens) en repositorios git, archivos y stdin, usable como hook o acción de CI.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/gitleaks/gitleaks

**Instalación** [+]:

```
brew install gitleaks
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: revisar el historial de un repositorio antes de hacerlo público; bloquear commits que contengan claves con un hook pre-commit
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala Gitleaks y ejecútalo sobre un repositorio de prueba con una clave falsa en un commit.
**Qué comprobar:** El informe señala el archivo, la línea y el commit de la clave falsa.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pre-commit`, `semgrep`, `claude-code`
**Alternativas (elige una):** `trufflehog`

## `gitnexus`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=code,typescript

**Qué es:** Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva.
**Stack:** Node 22.18+ en 22.x o 24.11+; repositorio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El análisis no exige modelo; la licencia PolyForm Noncommercial limita uso comercial y ofrece licencia aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El setup detecta los tres clientes; no confundas poder instalarlo con tener permiso de uso comercial
- Coste: El coste depende del proveedor o la ruta. El análisis no exige modelo; la licencia PolyForm Noncommercial limita uso comercial y ofrece licencia aparte
- Equipo: Preparación según la ruta elegida. Node 22.18+ en 22.x o 24.11+; repositorio de prueba
**Repo:** https://github.com/abhigyanpatwari/GitNexus

**Instalación** [+]:

```
# Run from your repository root
npx gitnexus analyze

# Connect your editors once
npx gitnexus setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Entender una base de código nueva; Inspeccionar el alcance de una refactorización
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Analiza una app pequeña y consulta el recorrido entre un endpoint y su función
**Qué comprobar:** El mapa permite localizar los archivos reales y sus conexiones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `opencode`, `codex`, `tools`
**Alternativas (elige una):** `repomix`, `codebase-memory-mcp`, `serena`, `codegraph`, `graphify`

## `graphify`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=— · tags=code,python

**Qué es:** Permite consultar símbolos y relaciones de una base de código desde distintos agentes. El análisis de código es determinista y local; documentos, PDFs, imágenes y video requieren la ruta semántica y sus dependencias. Ofrece adaptadores documentados para Claude Code, Codex y Antigravity.
**Stack:** Python 3.10+; uv o pipx; carpeta de código
**Acceso y costes:**
- API de IA: API de IA opcional. El código se analiza con AST sin LLM; documentos y medios usan el agente, API o backend local configurado
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. El paquete es graphifyy; el soporte Antigravity es explícito; la extracción semántica y la de código no tienen los mismos costes
- Coste: El coste depende del proveedor o la ruta. El código se analiza con AST sin LLM; documentos y medios usan el agente, API o backend local configurado
- Equipo: Preparación según la ruta elegida. Python 3.10+; uv o pipx; carpeta de código
**Repo:** https://github.com/Graphify-Labs/graphify

**Instalación** [+]:

```
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # detects your assistant and registers the skill
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar impacto de un cambio; Relacionar documentación y estructura de código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Indexa primero solo código y consulta qué funciones dependen de un módulo
**Qué comprobar:** Cada relación se puede contrastar con un archivo o símbolo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `tree-sitter`, `ollama`, `graphrag`
**Alternativas (elige una):** `codegraph`, `gitnexus`, `serena`, `codebase-memory-mcp`

## `lazygit`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=cli,go,git,terminal

**Qué es:** Interfaz de terminal sencilla para git: preparar fragmentos o líneas, rebase interactivo, cherry-pick y gestión de ramas con atajos.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/jesseduffield/lazygit

**Instalación** [+]:

```
brew install lazygit
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: revisar y preparar por partes los cambios que hizo un agente antes de confirmarlos; hacer rebases interactivos y deshacer operaciones sin recordar comandos
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala lazygit y ábrelo en un repositorio de prueba con cambios sin confirmar.
**Qué comprobar:** Puedes preparar una sola línea y crear el commit desde la interfaz.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `aider`

## `openai-python`
role=library · exec=cloud · setup=easy · mcp=False · prov=— · tags=code,python

**Qué es:** SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API.
**Stack:** Python 3.10+; entorno virtual; clave de proyecto API
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta OpenAI usa API y facturación de plataforma; la suscripción de Codex o ChatGPT no debe suponerse crédito para este SDK
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Es un cliente oficial de API, no un plugin de Codex; base_url configurable no confirma todas las funciones de servidores locales
- Coste: Consumo de APIs o servicios. La ruta OpenAI usa API y facturación de plataforma; la suscripción de Codex o ChatGPT no debe suponerse crédito para este SDK
- Equipo: Preparación según la ruta elegida. Python 3.10+; entorno virtual; clave de proyecto API
**Repo:** https://github.com/openai/openai-python

**Instalación** [+]:

```
# install from PyPI
pip install openai
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Integrar respuestas de IA en una app Python; Procesar audio o imágenes desde código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Envía una petición breve de ejemplo y revisa respuesta y uso informado
**Qué comprobar:** Obtienes la salida del endpoint y puedes localizar el consumo del proyecto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `vllm`, `langchain`, `openai-agents-python`, `openai-cookbook`

## `pre-commit`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=code,python,cli,git

**Qué es:** Framework para gestionar y ejecutar hooks de git multilenguaje antes de cada commit: linters, formateadores y escáneres declarados en YAML.
**Stack:** Python, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/pre-commit/pre-commit

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/pre-commit/pre-commit/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: obligar a pasar formato, lint y escaneo de secretos antes de cada commit; aplicar las mismas comprobaciones en local y en CI
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala pre-commit, crea un .pre-commit-config.yaml con un hook de formato y ejecuta `pre-commit run --all-files`.
**Qué comprobar:** El hook se instala solo y formatea o señala los archivos del repositorio.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ruff`, `gitleaks`, `trufflehog`, `biome`, `semgrep`, `trivy`

## `repomix`
role=app · exec=local · setup=easy · mcp=True · prov=— · tags=code,coding-agent,typescript

**Qué es:** Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM.
**Stack:** Node.js; repositorio de prueba; filtros de inclusión
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Empaquetar no usa modelo; enviarlo a un agente consume su contexto y presupuesto
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Ofrece MCP stdio y plugins o skills; revisa secretos y archivos excluidos aunque el paquete incluya un detector
- Coste: Sin pago a un modelo en la ruta básica. Empaquetar no usa modelo; enviarlo a un agente consume su contexto y presupuesto
- Equipo: Preparación según la ruta elegida. Node.js; repositorio de prueba; filtros de inclusión
**Repo:** https://github.com/yamadashy/repomix

**Instalación** [+]:

```
npx repomix@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar contexto de código para una consulta; Compartir una muestra reproducible de un proyecto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Empaqueta una carpeta pequeña y abre el resultado antes de entregarlo a una IA
**Qué comprobar:** Puedes comprobar archivos incluidos, tamaño y exclusiones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `tree-sitter`, `markitdown`, `tools`, `codebase-memory-mcp`
**Alternativas (elige una):** `gitnexus`

## `ripgrep`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=cli,rust,code,search

**Qué es:** Búsqueda recursiva de texto por expresiones regulares muy rápida que respeta .gitignore y omite archivos ocultos y binarios.
**Stack:** Rust, Cargo.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/BurntSushi/ripgrep

**Instalación** [+]:

```
brew install ripgrep
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: localizar todas las apariciones de una función en un repositorio grande; buscar texto en miles de archivos de logs o notas en segundos
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala ripgrep y ejecuta `rg` con un patrón en un repositorio.
**Qué comprobar:** Obtienes las coincidencias con archivo y línea, sin resultados de carpetas ignoradas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `fzf`, `claude-code`, `opencode`

## `ruff`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=code,python,rust,cli

**Qué es:** Linter y formateador de Python extremadamente rápido escrito en Rust, compatible con Flake8, isort y Black, con más de 800 reglas.
**Stack:** Rust, Cargo.toml, Dockerfile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/astral-sh/ruff

**Instalación** [+]:

```
pip install ruff
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: sustituir Flake8, isort y Black por una sola herramienta en un proyecto; revisar y corregir el código que genera un agente antes de cada commit
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Ejecuta `uvx ruff check` y `uvx ruff format` en un proyecto Python de prueba.
**Qué comprobar:** Ruff informa de los problemas en segundos y el formateo deja un diff limpio.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pre-commit`, `sonarqube`, `claude-code`

## `sonarqube`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=code,java,security,docker

**Qué es:** Plataforma de inspección continua de calidad y seguridad del código: análisis estático de bugs, vulnerabilidades y mantenibilidad en muchos lenguajes.
**Stack:** Java, build.gradle
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/SonarSource/sonarqube

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/SonarSource/sonarqube/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: vigilar la calidad y seguridad de un repositorio en cada PR; revisar el código generado por IA con reglas consistentes antes de fusionarlo
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Arranca la imagen Docker oficial, crea un proyecto y analiza un repositorio pequeño con el escáner.
**Qué comprobar:** El panel muestra problemas, puntos críticos y la puerta de calidad del proyecto.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ruff`, `claude-code`, `coolify`
**Alternativas (elige una):** `semgrep`

## `swe-bench`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=evaluation,coding-agent,python

**Qué es:** Benchmark para evaluar si los modelos resuelven issues reales de GitHub.
**Stack:** Python; Docker para evaluación; predicciones y tareas elegidas
**Acceso y costes:**
- API de IA: API de IA opcional. El harness no necesita llamar un modelo para evaluar predicciones; generar parches y levantar contenedores sí puede consumir modelos y cómputo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El benchmark no demuestra que un agente resuelva cualquier issue real; usa el conjunto y la versión de tareas correspondientes
- Coste: El coste depende del proveedor o la ruta. El harness no necesita llamar un modelo para evaluar predicciones; generar parches y levantar contenedores sí puede consumir modelos y cómputo
- Equipo: Preparación según la ruta elegida. Python; Docker para evaluación; predicciones y tareas elegidas
**Repo:** https://github.com/SWE-bench/SWE-bench

**Instalación** [+]:

```
git clone git@github.com:SWE-bench/SWE-bench.git
cd SWE-bench
pip install -e .
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar soluciones a issues reproducibles; Estudiar evaluación de agentes de programación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Evalúa una predicción ya preparada sobre una tarea pequeña antes de generar nuevas soluciones
**Qué comprobar:** El informe muestra si las pruebas del entorno aceptan el parche
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openhands`, `aider`, `codex`

## `tree-sitter`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=code,rust

**Qué es:** Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código.
**Stack:** Herramientas y binding del lenguaje elegido; gramática
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere IA ni servicios; compilar gramáticas puede necesitar herramientas nativas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es infraestructura de parsing; no contesta por sí sola preguntas sobre arquitectura o intención del código
- Coste: Sin pago a un modelo en la ruta básica. No requiere IA ni servicios; compilar gramáticas puede necesitar herramientas nativas
- Equipo: Preparación según la ruta elegida. Herramientas y binding del lenguaje elegido; gramática
**Repo:** https://github.com/tree-sitter/tree-sitter

**Instalación** [?]:

```
Seguir la instalación original: https://tree-sitter.github.io/tree-sitter/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un analizador de código; Extraer símbolos para una herramienta de edición
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Analiza un archivo mínimo y observa cómo cambia el árbol tras editar una función
**Qué comprobar:** El árbol refleja el cambio sin interpretar semánticamente todo el programa
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ast-grep`, `aider`, `repomix`, `graphify`

## `trufflehog`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,go,cli,code

**Qué es:** Busca, clasifica, verifica y analiza credenciales filtradas en git, chats, wikis, logs, almacenes de objetos y sistemas de archivos.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/trufflesecurity/trufflehog

**Instalación** [+]:

```
brew install trufflehog
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar los repositorios de una organización en busca de claves activas; revisar buckets o logs exportados antes de compartirlos
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Ejecuta la imagen Docker contra el repositorio de pruebas trufflesecurity/test_keys como indica el README.
**Qué comprobar:** El informe muestra las claves encontradas y si están verificadas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pre-commit`, `semgrep`, `claude-code`
**Alternativas (elige una):** `gitleaks`
