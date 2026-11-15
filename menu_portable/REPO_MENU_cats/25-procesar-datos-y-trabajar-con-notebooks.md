# 25. Procesar datos y trabajar con notebooks — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

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

## `dash`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=automation,ui,python

**Qué es:** Cubre el caso de dashboards productivos en Python sin salir del lenguaje.
**Stack:** Python, Plotly, Flask, web
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/plotly/dash

**Instalación** [?]: `Seguir la instalación original: https://github.com/plotly/dash/blob/dev/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres dashboards productivos en Python con control del frontend
**Evita si:** prefieres prototipos ultrarrápidos (streamlit)
**Combina con:** `streamlit`, `echarts`

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

## `gradio`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,python

**Qué es:** Envuelve una función Python en una interfaz web con entradas y salidas de texto, imagen, audio o chat. Base de Hugging Face Spaces.
**Stack:** Python, Svelte
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/gradio-app/gradio

**Instalación** [+]: `pip install --upgrade gradio`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres una demo web de tu modelo rápido
**Evita si:** construyes una app de datos con varias páginas; mira `streamlit`
**Combina con:** `transformers`
**Alternativas (elige una):** `streamlit`

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

## `streamlit`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,dataviz,python

**Qué es:** Convierte un script de datos en una app web interactiva casi al instante.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/streamlit/streamlit

**Instalación** [+]: `pip install streamlit`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres una UI de datos al vuelo y prototipos rápidos
**Evita si:** necesitas una app productiva con control fino del frontend (dash)
**Combina con:** `dash`, `data-science-ipython-notebooks`
**Alternativas (elige una):** `gradio`
