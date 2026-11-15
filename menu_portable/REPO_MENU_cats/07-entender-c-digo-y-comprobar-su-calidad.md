# 7. Entender código y comprobar su calidad — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ast-grep`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=code,security,rust

**Qué es:** Busca y reemplaza código por su estructura (AST), no por texto. Útil para refactors masivos y reglas de lint propias.
**Stack:** Rust, tree-sitter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ast-grep/ast-grep

**Instalación** [?]: `Seguir la instalación original: https://github.com/ast-grep/ast-grep/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas buscar o reescribir código por estructura
**Evita si:** buscas análisis de seguridad con reglas existentes; mira `semgrep`
**Combina con:** `tree-sitter`, `claude-code`
**Alternativas (elige una):** `semgrep`

## `cli`
role=app · exec=cloud · setup=easy · mcp=False · prov=— · tags=code,go

**Qué es:** No es un agente: es la herramienta que los agentes de código usan para abrir PRs, revisar issues o lanzar workflows.
**Stack:** Go
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/cli/cli

**Instalación** [?]: `Seguir la instalación original: https://github.com/cli/cli/blob/trunk/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas con GitHub desde la terminal o con agentes
**Evita si:** usas GitLab u otra forja
**Combina con:** `claude-code`, `github-mcp-server`

## `codebase-memory-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=code,mcp,memory

**Qué es:** Indexa repos en milisegundos y da al agente herramientas MCP para entender arquitectura, dependencias y cambios sin leer archivo por archivo.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/DeusData/codebase-memory-mcp

**Instalación** [?]: `Seguir la instalación original: https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu agente trabaja en repos grandes
**Evita si:** tu repo es pequeño; usa `repomix`
**Combina con:** `claude-code`, `serena`
**Alternativas (elige una):** `codegraph`, `gitnexus`

## `codegraph`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=code,typescript

**Qué es:** Resuelve el coste de contexto de los agentes en repos grandes.
**Stack:** JavaScript/Node.js (binario autónomo)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/colbymchenry/codegraph

**Instalación** [?]: `Seguir la instalación original: https://github.com/colbymchenry/codegraph/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas repos grandes y el contexto del agente es caro
**Evita si:** tu base de código es pequeña y no justifica mantener un índice
**Combina con:** `graphify`, `headroom`
**Alternativas (elige una):** `codebase-memory-mcp`, `serena`

## `deepwiki-open`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,google,local · tags=code,docs,python

**Qué es:** Analiza un repositorio y crea documentación navegable con diagramas y un chat para preguntar sobre el código.
**Stack:** Python, Next.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/AsyncFuncAI/deepwiki-open

**Instalación** [?]: `Seguir la instalación original: https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres documentación automática de un repositorio
**Evita si:** necesitas contexto de librerías externas; mira `context7`
**Combina con:** `ollama`
**Alternativas (elige una):** `context7`

## `defending-code-reference-harness`
role=skill · exec=cloud · setup=medium · mcp=False · prov=anthropic · tags=security,skills,coding-agent

**Qué es:** Implementación de referencia para descubrir y corregir vulnerabilidades de forma autónoma con Claude, basada en experiencia con equipos de seguridad.
**Stack:** Python, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/anthropics/defending-code-reference-harness

**Instalación** [?]: `Seguir la instalación original: https://github.com/anthropics/defending-code-reference-harness/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un flujo de seguridad con agentes probado
**Evita si:** solo necesitas un escáner estático; mira `semgrep`
**Combina con:** `claude-code`, `semgrep`

## `dsh-qa`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=calidad,plugin,javascript

**Qué es:** Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles.
**Stack:** JavaScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
- Otras rutas: Plugin para DeepSeek Harness (DSH). La cuenta, API o modelo se configura en ese anfitrión; no se declara instalación nativa en Claude Code o Codex.
**Repo:** https://github.com/ZSeven-W/dsh-qa

**Instalación** [?]: `Seguir la instalación original: https://github.com/ZSeven-W/dsh-qa/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `floorplan`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=codigo,skill,javascript

**Qué es:** Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.
**Stack:** JavaScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/haydenschmitty/floorplan

**Instalación** [?]: `Seguir la instalación original: https://github.com/haydenschmitty/floorplan/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.
**Evita si:** necesitas un producto autónomo y esta pieza requiere un anfitrión compatible

## `gitnexus`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=code,typescript

**Qué es:** Resuelve el "llegar a un proyecto ajeno y no saber por dónde empezar": lo navegas y lo discutes en vez de leer ficheros sueltos.
**Stack:** web/TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/abhigyanpatwari/GitNexus

**Instalación** [+]: `npm install -g gitnexus`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres entender un repo puntual de forma visual
**Evita si:** necesitas indexar muchos repos a escala (codegraph) o no quieres front web
**Combina con:** `codegraph`
**Alternativas (elige una):** `repomix`, `codebase-memory-mcp`, `serena`

## `graphify`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=— · tags=code,python

**Qué es:** Resuelve el onboarding visual: un índice textual no basta cuando hay relaciones entre archivos.
**Stack:** Python 3.10+, uv/pipx
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Graphify-Labs/graphify

**Instalación** [+]: `pipx install graphify`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres ver conexiones visualmente o auditar un sistema
**Evita si:** solo necesitas índice textual barato (codegraph) o tu proyecto es trivial
**Combina con:** `codegraph`, `graphrag`

## `openai-python`
role=library · exec=cloud · setup=easy · mcp=False · prov=— · tags=code,python

**Qué es:** Resuelve el glue HTTP: no escribes peticiones a mano, usas clientes tipados con streaming.
**Stack:** Python
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. Revisar el plan, créditos, cuotas y facturación del proveedor antes de ejecutar.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/openai/openai-python

**Instalación** [+]: `pip install openai`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** usas modelos de OpenAI desde Python y quieres el cliente oficial
**Evita si:** quieres abstracción multi-proveedor (litellm) o no usas OpenAI
**Combina con:** `litellm`, `langchain`

## `repomix`
role=app · exec=local · setup=easy · mcp=True · prov=— · tags=code,coding-agent,typescript

**Qué es:** Genera un archivo XML, Markdown o texto con la estructura y el código del repo, respetando .gitignore y contando tokens. También funciona como servidor MCP.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/yamadashy/repomix

**Instalación** [+]: `npx repomix`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres dar tu repo completo a un LLM
**Evita si:** el repo es enorme; mira `codebase-memory-mcp` o `serena`
**Combina con:** `claude-code`
**Alternativas (elige una):** `gitnexus`

## `semgrep`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,code

**Qué es:** Encuentra bugs y vulnerabilidades con miles de reglas comunitarias o propias. Muy usado en CI de seguridad.
**Stack:** OCaml, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/semgrep/semgrep

**Instalación** [+]: `pip install semgrep`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres análisis de seguridad en CI
**Evita si:** solo quieres refactors estructurales; mira `ast-grep`
**Combina con:** `defending-code-reference-harness`
**Alternativas (elige una):** `ast-grep`

## `swe-bench`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=evaluation,coding-agent,python

**Qué es:** Da al modelo un repositorio y un issue y comprueba si su parche pasa las pruebas. Es la referencia para medir agentes de código.
**Stack:** Python, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/SWE-bench/SWE-bench

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** necesitas medir agentes de código con un estándar
**Evita si:** solo quieres usar un agente
**Combina con:** `swe-agent`

## `tree-sitter`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=code,rust

**Qué es:** Genera parsers rápidos que actualizan el árbol sintáctico mientras editas. Lo usan editores, Aider, ast-grep y muchas herramientas de código con IA.
**Stack:** Rust, C
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/tree-sitter/tree-sitter

**Instalación** [?]: `Seguir la instalación original: https://github.com/tree-sitter/tree-sitter/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** construyes herramientas que entienden código
**Evita si:** solo necesitas buscar patrones; mira `ast-grep`
**Combina con:** `ast-grep`, `aider`
