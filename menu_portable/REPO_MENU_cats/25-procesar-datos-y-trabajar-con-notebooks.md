# 25. Procesar datos y trabajar con notebooks — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `apache-iceberg`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=data,lakehouse,table-format,java

**Qué es:** Formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java.
**Stack:** Java, build.gradle
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Preparación según la ruta elegida. JVM (Java 17 o 21 para compilar Iceberg; Scala/sbt para Delta) o las bibliotecas de Python y Rust del ecosistema; un motor como Spark, Trino o DuckDB para consultar.
**Repo:** https://github.com/apache/iceberg

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/apache/iceberg/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir una tabla analítica entre varios motores; Consultar un snapshot anterior tras un cambio de esquema
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Crea una tabla Iceberg pequeña con PyIceberg, añade una columna y consulta el snapshot previo
**Qué comprobar:** El snapshot anterior conserva el esquema original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `duckdb`, `polars`, `jupyterlab`
**Alternativas (elige una):** `delta-lake`, `hudi`

## `awesome-bigdata`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=data

**Qué es:** Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala.
**Stack:** Navegador; problema de datos definido
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El directorio no usa API; cada proyecto o servicio tiene coste, licencia y requisitos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No se instala la colección entera ni se hereda la compatibilidad de sus enlaces
- Coste: Sin pago a un modelo en la ruta básica. El directorio no usa API; cada proyecto o servicio tiene coste, licencia y requisitos propios
- Equipo: Preparación según la ruta elegida. Navegador; problema de datos definido
**Repo:** https://github.com/oxnr/awesome-bigdata

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar el ecosistema de datos; Comparar motores antes de montar infraestructura
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca una herramienta de streaming y otra de almacenamiento y compara qué función resuelve cada una
**Qué comprobar:** Puedes elegir candidatos complementarios
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `awesome-dataviz`, `duckdb`, `hudi`

## `dash`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=automation,ui,python

**Qué es:** Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos.
**Stack:** Python; entorno de desarrollo; datos de muestra
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Dash OSS no exige API de IA; Dash Enterprise, hosting y fuentes de datos son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un framework Python; el README mezcla ejemplos OSS y funciones Enterprise que no vienen todas con el paquete básico
- Coste: El coste depende del proveedor o la ruta. Dash OSS no exige API de IA; Dash Enterprise, hosting y fuentes de datos son independientes
- Equipo: Preparación según la ruta elegida. Python; entorno de desarrollo; datos de muestra
**Repo:** https://github.com/plotly/dash

**Instalación** [?]:

```
Seguir la instalación original: https://dash.plotly.com/getting-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un tablero interactivo; Comparar escenarios con controles
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue la app inicial y conecta un selector a un gráfico pequeño
**Qué comprobar:** Puedes comprobar qué callback cambia la figura
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `streamlit`, `echarts`, `duckdb`

## `delta-lake`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=data,lakehouse,table-format,scala

**Qué es:** Capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores.
**Stack:** Scala, Dockerfile, build.sbt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Preparación según la ruta elegida. JVM (Java 17 o 21 para compilar Iceberg; Scala/sbt para Delta) o las bibliotecas de Python y Rust del ecosistema; un motor como Spark, Trino o DuckDB para consultar.
**Repo:** https://github.com/delta-io/delta

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/delta-io/delta/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir transacciones y versiones a archivos Parquet; Recuperar una versión anterior de una tabla
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Escribe una tabla Delta local, actualiza unas filas y lee la versión 0
**Qué comprobar:** La versión 0 muestra los datos originales
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `duckdb`, `polars`, `jupyterlab`
**Alternativas (elige una):** `apache-iceberg`, `hudi`

## `duckdb`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=data,analytics,cpp

**Qué es:** Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL.
**Stack:** CLI o biblioteca para tu sistema; CSV pequeño
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa LLM ni API de IA; servicios Cloud o almacenamiento remoto tienen sus condiciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor
- Coste: Sin pago a un modelo en la ruta básica. No usa LLM ni API de IA; servicios Cloud o almacenamiento remoto tienen sus condiciones
- Equipo: Preparación según la ruta elegida. CLI o biblioteca para tu sistema; CSV pequeño
**Repo:** https://github.com/duckdb/duckdb

**Instalación** [?]:

```
Seguir la instalación original: https://duckdb.org/docs/installation/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un CSV ficticio y consulta el total de registros y una suma por categoría
**Qué comprobar:** Puedes comparar el resultado con las filas originales
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `marimo`, `superset`, `timesfm`, `apache-iceberg`, `delta-lake`
**Alternativas (elige una):** `polars`

## `globalbuildingatlas`
role=directory · exec=local · setup=heavy · mcp=False · prov=— · tags=datos,python

**Qué es:** Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1.
**Stack:** Navegador o GIS; espacio de descarga; zona pequeña; licencia de la capa
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa API de IA para consultar datos; descarga, almacenamiento y procesamiento tienen costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. GBA.ODbLPolygon usa ODbL, mientras otras capas de polígonos, LoD1 y alturas usan CC BY-NC 4.0; no toda la colección permite el mismo uso comercial
- Coste: Sin pago a un modelo en la ruta básica. No usa API de IA para consultar datos; descarga, almacenamiento y procesamiento tienen costes
- Equipo: Preparación según la ruta elegida. Navegador o GIS; espacio de descarga; zona pequeña; licencia de la capa
**Repo:** https://github.com/zhu-xlab/GlobalBuildingAtlas

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar edificios en un GIS; Preparar una escena urbana de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Selecciona una zona y distingue polígonos, alturas y LoD1 antes de descargar una capa
**Qué comprobar:** Puedes identificar formato, licencia y escala del dato
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `duckdb`, `3dviz-pro-max`

## `gradio`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,python

**Qué es:** Librería Python para crear y compartir apps web de modelos de ML en minutos.
**Stack:** Python 3.10+; función o modelo de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. La interfaz básica no necesita API; modelo, servicio y alojamiento elegidos pueden cobrar
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. Incluye skills para agentes compatibles con .agents y ruta Claude; una URL de compartir expone la app y no sustituye autenticación o alojamiento de producción
- Coste: El coste depende del proveedor o la ruta. La interfaz básica no necesita API; modelo, servicio y alojamiento elegidos pueden cobrar
- Equipo: Preparación según la ruta elegida. Python 3.10+; función o modelo de prueba
**Repo:** https://github.com/gradio-app/gradio

**Instalación** [+]:

```
pip install --upgrade gradio
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una demo de un modelo; Preparar una herramienta interna de texto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una interfaz para una función simple de texto y pruébala localmente antes de compartir un enlace
**Qué comprobar:** Puedes ver la relación entre entrada, función y salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `llama-factory`, `ollama`, `rembg`
**Alternativas (elige una):** `streamlit`

## `hudi`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=datos,apacheflink,apachehudi,apachespark,bigdata,data-integration,datalake,hudi

**Qué es:** Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos.
**Stack:** Java y Spark o Flink compatibles; almacenamiento de prueba; datos pequeños
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API de IA; motores, almacenamiento y nube se presupuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Los comandos para compilar snapshots son para desarrollo; el quickstart de la versión elegida debe coincidir con Spark o Flink instalados
- Coste: Sin pago a un modelo en la ruta básica. No necesita API de IA; motores, almacenamiento y nube se presupuestan aparte
- Equipo: Preparación según la ruta elegida. Java y Spark o Flink compatibles; almacenamiento de prueba; datos pequeños
**Repo:** https://github.com/apache/hudi

**Instalación** [?]:

```
Seguir la instalación original: https://hudi.apache.org/docs/quick-start-guide.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un lakehouse; Preparar ingestión incremental
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inserta registros ficticios y actualiza uno para comparar estado y consulta incremental
**Qué comprobar:** Puedes comprobar la actualización sin reconstruir manualmente toda la tabla
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `duckdb`, `superset`, `awesome-bigdata`
**Alternativas (elige una):** `apache-iceberg`, `delta-lake`

## `jupyterlab`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=notebooks,data,python,typescript

**Qué es:** Entorno web de Project Jupyter con notebooks, terminal, editor de texto y explorador de archivos, ampliable mediante extensiones.
**Stack:** TypeScript, package.json, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. Sin coste de modelo. Las extensiones de IA (p. ej. Jupyter AI) se configuran aparte con sus proveedores.
- Equipo: Equipo normal; revisar dependencias. Python con pip, conda o mamba; los kernels y extensiones añaden sus propias dependencias.
**Repo:** https://github.com/jupyterlab/jupyterlab

**Instalación** [+]:

```
pip install jupyterlab
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Analizar datos de muestra en un notebook; Documentar un experimento con código y resultados
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Crea un notebook, carga un CSV ficticio y dibuja un gráfico simple
**Qué comprobar:** El notebook guarda código, tabla y gráfico al reabrirlo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pytorch`, `tensorflow`, `duckdb`, `polars`, `apache-iceberg`, `delta-lake`
**Alternativas (elige una):** `marimo`

## `marimo`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=notebooks,data,python

**Qué es:** Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app.
**Stack:** Python; entorno de notebook; CSV pequeño; modelo solo para funciones AI
**Acceso y costes:**
- API de IA: API de IA opcional. Notebook básico sin API; AI opcional con claves o modelos locales y marimo pair con su agente
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Documenta pair con Claude Code y Codex; usar un notebook local no implica que el asistente AI también sea local
- Coste: El coste depende del proveedor o la ruta. Notebook básico sin API; AI opcional con claves o modelos locales y marimo pair con su agente
- Equipo: Preparación según la ruta elegida. Python; entorno de notebook; CSV pequeño; modelo solo para funciones AI
**Repo:** https://github.com/marimo-team/marimo

**Instalación** [+]:

```
pip install marimo && marimo tutorial intro
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar datos en un notebook; Convertir un análisis en una app
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Completa el tutorial intro y modifica una variable para ver qué celdas se recalculan
**Qué comprobar:** Puedes reconocer dependencias reactivas y el archivo Python guardado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `duckdb`, `polars`, `ollama`
**Alternativas (elige una):** `jupyterlab`

## `polars`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=data,python,rust

**Qué es:** Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares.
**Stack:** Python; CSV pequeño; memoria para los datos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Sin API de IA; cómputo y alojamiento propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un motor de consultas y DataFrames, no una app de BI; mayor velocidad que otra biblioteca depende del trabajo y configuración
- Coste: Sin pago a un modelo en la ruta básica. Sin API de IA; cómputo y alojamiento propios
- Equipo: Preparación según la ruta elegida. Python; CSV pequeño; memoria para los datos
**Repo:** https://github.com/pola-rs/polars

**Instalación** [+]:

```
pip install polars
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Transformar tablas; Preparar datos antes de un dashboard
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee un archivo y agrupa por una columna para sumar otra
**Qué comprobar:** Puedes contrastar el resultado con una muestra calculada a mano
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `marimo`, `timesfm`, `streamlit`, `apache-iceberg`, `delta-lake`
**Alternativas (elige una):** `duckdb`

## `streamlit`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,dataviz,python

**Qué es:** Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS.
**Stack:** Python; script pequeño; datos ficticios
**Acceso y costes:**
- API de IA: API de IA opcional. La app básica no necesita LLM; AI, hosting y fuentes de datos tienen costes separados
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. streamlit skills instala instrucciones para Claude Code y agentes que leen .agents; no convierte la suscripción del agente en backend de cualquier app creada
- Coste: El coste depende del proveedor o la ruta. La app básica no necesita LLM; AI, hosting y fuentes de datos tienen costes separados
- Equipo: Preparación según la ruta elegida. Python; script pequeño; datos ficticios
**Repo:** https://github.com/streamlit/streamlit

**Instalación** [+]:

```
pip install streamlit
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un dashboard de ventas ficticias; Explorar un simulador de demanda
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una app con un control y una tabla de ejemplo y comprueba que la interacción actualiza la vista
**Qué comprobar:** Puedes identificar script, estado y resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `dash`, `polars`, `duckdb`, `awesome-llm-apps`
**Alternativas (elige una):** `gradio`
