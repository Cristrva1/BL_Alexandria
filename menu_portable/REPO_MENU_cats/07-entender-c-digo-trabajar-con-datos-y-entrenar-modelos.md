# 7. Entender código, trabajar con datos y entrenar modelos — detalle de repos

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

## `awesome-bigdata`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=data

**Qué es:** Resuelve el "qué uso para X a escala": un panorama del stack de datos grandes en un solo vistazo.
**Stack:** Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/oxnr/awesome-bigdata

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** diseñas pipelines de datos grandes y necesitas descubrir el ecosistema
**Evita si:** tu proyecto es pequeño y no justifica herramientas de big data
**Combina con:** `awesome-dataviz`

## `awesome-machine-learning`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=aprender,python

**Qué es:** Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema. Reúne enlaces a implementaciones, cursos y material para comparar herramientas.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/josephmisiti/awesome-machine-learning

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas alternativas de aprendizaje automático en distintos lenguajes
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `bigdata`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=datos,java

**Qué es:** Colección educativa de proyectos de datos con ejercicios de Hive, HDFS, Spark, HBase y sistemas de recomendación. Las carpetas desarrollan problemas de ingestión, análisis y procesamiento distribuido de datos.
**Stack:** Java
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/monsonlee/BigData

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres estudiar ejemplos prácticos del ecosistema de big data
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `bionemo-recipes`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,drug-discovery,gpu,machine-learning,pytorch,python

**Qué es:** Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. Presenta configuraciones de entrenamiento con TransformerEngine y frameworks distribuidos para modelos biológicos.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA-BioNeMo/bionemo-recipes

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** trabajas en entrenamiento de modelos para datos biológicos
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

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

## `cosmos`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=inference

**Qué es:** Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.
**Stack:** Python, GPU (NVIDIA/CUDA)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA/cosmos

**Instalación** [?]: `Seguir la instalación original: https://github.com/NVIDIA/cosmos/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas IA física/robótica y necesitas datos sintéticos
**Evita si:** haces tareas de texto/UI o no tienes GPU para servirlo
**Combina con:** `diffusers`

## `data-science-ipython-notebooks`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=data,python

**Qué es:** Resuelve el "aprender DS con ejemplos reales" sin tener que montarlos tú desde cero.
**Stack:** Python, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/donnemartin/data-science-ipython-notebooks

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** estudias/consultas DS con ejemplos ejecutables
**Evita si:** buscas una librería, no ejemplos, o necesitas material actualizado a las versiones más recientes
**Combina con:** `dash`, `streamlit`

## `deepseek-coder`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=inference,python

**Qué es:** Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia infraestructura.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/deepseek-ai/DeepSeek-Coder

**Instalación** [?]: `Seguir la instalación original: https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un modelo de código abierto y desplegable on-prem
**Evita si:** prefieres APIs comerciales gestionadas o no tienes GPU para servirlo
**Combina con:** `litellm`, `codegraph`

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

## `duckdb`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=data,analytics,cpp

**Qué es:** El "SQLite de la analítica": sin servidor, embebida en Python, R o Node, y capaz de procesar millones de filas en segundos.
**Stack:** C++
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/duckdb/duckdb

**Instalación** [?]: `Seguir la instalación original: https://github.com/duckdb/duckdb/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres SQL analítico rápido sin montar servidores
**Evita si:** necesitas una base transaccional multiusuario; usa PostgreSQL
**Combina con:** `marimo`, `superset`
**Alternativas (elige una):** `polars`

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

## `globalbuildingatlas`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=datos,python

**Qué es:** Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. Publica distintas capas geoespaciales y herramientas para estimar alturas y construir representaciones de edificios.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/zhu-xlab/GlobalBuildingAtlas

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** necesitas geometría de edificios para análisis territorial o visualización urbana
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico
**Combina con:** `three.js`

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

## `how-to-train-your-gpt`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=learning

**Qué es:** Resuelve el "quiero entenderlo con explicación narrada" frente al código desnudo de nanoGPT.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/raiyanyahya/how-to-train-your-gpt

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una guía explicada y narrada
**Evita si:** prefieres solo el código limpio (nanoGPT) o buscas algo productivo
**Combina con:** `nanogpt`, `nanochat`

## `hudi`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=datos,apacheflink,apachehudi,apachespark,bigdata,data-integration,datalake,hudi

**Qué es:** Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. Añade índices, actualizaciones y procesamiento incremental a tablas de un lago de datos.
**Stack:** Java, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/apache/hudi

**Instalación** [?]: `Seguir la instalación original: https://github.com/apache/hudi/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas gestionar cambios y cargas incrementales en un data lake
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `llama-factory`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=training,python

**Qué es:** Soporta LoRA, QLoRA, ajuste completo, DPO y más desde una UI o CLI. Muy usado en investigación e industria.
**Stack:** Python, PyTorch, Gradio
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/hiyouga/LlamaFactory

**Instalación** [?]: `Seguir la instalación original: https://github.com/hiyouga/LlamaFactory/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres muchas técnicas de fine-tuning con UI
**Evita si:** buscas la opción más eficiente en memoria; mira `unsloth`
**Combina con:** `peft`, `transformers`
**Alternativas (elige una):** `unsloth`

## `llm-course`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=learning,training,notebooks

**Qué es:** Tres rutas: fundamentos, científico de LLM (entrenar y afinar) e ingeniero de LLM (apps y despliegue), con recursos y notebooks ejecutables.
**Stack:** Markdown, Jupyter, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mlabonne/llm-course

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres una ruta completa para aprender LLM
**Evita si:** buscas un curso introductorio de apps; mira `generative-ai-for-beginners`
**Combina con:** `unsloth`, `llama-factory`
**Alternativas (elige una):** `llms-from-scratch`, `generative-ai-for-beginners`

## `llm.c`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=learning

**Qué es:** Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framework.
**Stack:** C, CUDA
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/karpathy/llm.c

**Instalación** [?]: `Seguir la instalación original: https://github.com/karpathy/llm.c/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres bajo nivel sin abstracciones y tienes GPU CUDA
**Evita si:** prefieres PyTorch (nanoGPT) o no tienes CUDA
**Combina con:** `nanogpt`

## `llms-from-scratch`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=learning,training,python

**Qué es:** Construyes atención, GPT, preentrenamiento y fine-tuning desde cero, entendiendo cada pieza. Ideal para aprender cómo funcionan por dentro.
**Stack:** Python, PyTorch, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/rasbt/LLMs-from-scratch

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres entender los LLM implementándolos
**Evita si:** solo quieres usar modelos existentes
**Combina con:** `pytorch`
**Alternativas (elige una):** `llm-course`, `nanogpt`

## `machinelearning`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,python

**Qué es:** Ejemplos educativos de algoritmos de machine learning y redes neuronales con Python. Agrupa implementaciones y ejercicios de clasificación, reducción de dimensiones y aprendizaje profundo.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/wepe/MachineLearning

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres explorar implementaciones pequeñas de algoritmos clásicos
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `marimo`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=notebooks,data,python

**Qué es:** Al cambiar una celda se recalculan las dependientes, evitando estados ocultos. Incluye SQL, gráficos interactivos y asistente de IA.
**Stack:** Python, TypeScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/marimo-team/marimo

**Instalación** [+]: `pip install marimo`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres notebooks reproducibles y versionables
**Evita si:** dependes de extensiones de Jupyter
**Combina con:** `duckdb`, `polars`

## `nanochat`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=learning,python

**Qué es:** Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/karpathy/nanochat

**Instalación** [?]: `Seguir la instalación original: https://github.com/karpathy/nanochat/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres el pipeline completo de un chat end-to-end
**Evita si:** solo necesitas el core del modelo (nanoGPT) o un modelo listo para usar
**Combina con:** `nanogpt`

## `nanogpt`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=learning,python

**Qué es:** Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción.
**Stack:** Python, PyTorch, GPU
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/karpathy/nanoGPT

**Instalación** [?]: `Seguir la instalación original: https://github.com/karpathy/nanoGPT/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres entender el entrenamiento de un GPT desde cero
**Evita si:** solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat)
**Combina con:** `nanochat`
**Alternativas (elige una):** `llms-from-scratch`

## `nemotron`
role=directory · exec=local · setup=heavy · mcp=False · prov=local · tags=training,inference

**Qué es:** Reúne guías de entrenamiento, despliegue y casos de uso de los modelos Nemotron, pensados para IA agéntica eficiente.
**Stack:** Python, Jupyter
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA-NeMo/Nemotron

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** usas GPUs NVIDIA y quieres modelos abiertos optimizados
**Evita si:** buscas la forma más simple de correr modelos; mira `ollama`
**Combina con:** `vllm`, `nemoclaw`

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

## `peft`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Adapta modelos grandes entrenando solo una pequeña parte de los parámetros, ahorrando memoria y tiempo.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/peft

**Instalación** [+]: `pip install peft`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** afinas modelos con código propio
**Evita si:** prefieres una herramienta lista; mira `unsloth`
**Combina con:** `transformers`, `trl`

## `polars`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=data,python,rust

**Qué es:** API expresiva con ejecución perezosa y paralela para procesar datos grandes en un solo equipo.
**Stack:** Rust, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/pola-rs/polars

**Instalación** [+]: `pip install polars`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu análisis con pandas es lento
**Evita si:** prefieres SQL; mira `duckdb`
**Combina con:** `marimo`
**Alternativas (elige una):** `duckdb`

## `python-machine-learning-book`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,data-mining,data-science,logistic-regression,machine-learning,machine-learning-algorithms,neural-network,python

**Qué es:** Código de la primera edición del libro Python Machine Learning, con ejemplos de algoritmos y evaluación. Presenta notebooks y scripts que acompañan los capítulos y conceptos del libro.
**Stack:** Jupyter Notebook
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/rasbt/python-machine-learning-book

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres estudiar los ejemplos de la primera edición del libro
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `pytorch`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Base de la mayoría de investigación y modelos abiertos actuales.
**Stack:** Python, C++, CUDA
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/pytorch/pytorch

**Instalación** [?]: `Seguir la instalación original: https://github.com/pytorch/pytorch/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** entrenas o investigas modelos
**Evita si:** solo consumes APIs de LLM
**Combina con:** `transformers`

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

## `tensorflow`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,deep-learning,deep-neural-networks,distributed,machine-learning,ml,neural-network,python

**Qué es:** Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. Define operaciones y modelos y ofrece herramientas de entrenamiento e inferencia en distintos dispositivos.
**Stack:** C++
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/tensorflow/tensorflow

**Instalación** [+]: `pip install tensorflow`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu proyecto necesita el ecosistema TensorFlow para entrenamiento o despliegue
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `timesfm`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=data,analytics,python

**Qué es:** Predice ventas, demanda o tráfico a partir del histórico sin entrenar un modelo propio (zero-shot).
**Stack:** Python, PyTorch, JAX
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/google-research/timesfm

**Instalación** [?]: `Seguir la instalación original: https://github.com/google-research/timesfm/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas pronósticos rápidos sin entrenar modelos
**Evita si:** necesitas explicabilidad estadística clásica
**Combina con:** `polars`, `duckdb`

## `train-llm-from-scratch`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=aprender,gemini,large-language-models,llm,openai,training,transformers,python

**Qué es:** Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación. Implementa un Transformer y recorre preparación de datos, entrenamiento y ajuste del modelo.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/FareedKhan-dev/train-llm-from-scratch

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres entender el entrenamiento de un LLM mediante una implementación completa
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico

## `transformers`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=training,inference,python

**Qué es:** Da acceso a cientos de miles de modelos con una API común para inferencia y entrenamiento. Es la base del ecosistema de modelos abiertos.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/transformers

**Instalación** [?]: `Seguir la instalación original: https://github.com/huggingface/transformers/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas con modelos abiertos en Python
**Evita si:** solo quieres chatear con un modelo local; mira `ollama`
**Combina con:** `peft`, `trl`, `pytorch`

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

## `trl`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=training,python

**Qué es:** Ofrece entrenadores listos para ajuste supervisado y por preferencias, usados para alinear modelos.
**Stack:** Python, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/trl

**Instalación** [+]: `pip install trl`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas SFT o RL sobre modelos abiertos
**Evita si:** quieres algo sin código; mira `llama-factory`
**Combina con:** `transformers`, `peft`, `unsloth`

## `unsloth`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=training,local,python

**Qué es:** Afina modelos como Qwen, Llama o Gemma en una sola GPU y expórtalos a GGUF u Ollama. Ofrece notebooks gratuitos y una interfaz local.
**Stack:** Python, Triton, PyTorch
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/unslothai/unsloth

**Instalación** [?]: `Seguir la instalación original: https://github.com/unslothai/unsloth/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres afinar un LLM con pocos recursos
**Evita si:** necesitas muchas técnicas y una UI de entrenamiento; mira `llama-factory`
**Combina con:** `ollama`, `trl`
**Alternativas (elige una):** `llama-factory`

## `warp`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=entrenamiento,cuda,differentiable-programming,gpu,gpu-acceleration,nvidia,nvidia-warp,python

**Qué es:** Framework de NVIDIA que compila funciones de Python en kernels para simulación física y cálculo en CPU o GPU. Compila funciones especializadas y aporta primitivas de geometría, física y diferenciación.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/NVIDIA/warp

**Instalación** [+]: `pip install warp-lang`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres escribir simulaciones o kernels de cálculo acelerado desde Python
**Evita si:** necesitas una aplicación lista para usuarios sin trabajo técnico
