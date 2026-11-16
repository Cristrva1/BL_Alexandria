# Alexandría para agentes · Procesar datos y trabajar con notebooks

Categoría 25 completa (23 repos, 2 subcategorías). Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=25 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `clickhouse` | datos | Base de datos analítica columnar de código abierto para consultas SQL en tiempo… | 2 Intermedio | 80 | Apache-2.0 (OSI permisiva) | sin grupo |
| `pandas` | datos | Biblioteca estándar de Python para analizar y transformar datos tabulares con… | 2 Intermedio | 77 | BSD-3-Clause (OSI permisiva) | recomendado |
| `marimo` | datos | Notebook reactivo de Python que se guarda como script, se versiona en Git y se… | 1 Básico | 76 | Apache-2.0 (OSI permisiva) | recomendado |
| `spark` | datos | Motor unificado de Apache para procesar datos a gran escala en clúster: SQL y… | 3 Avanzado | 76 | Apache-2.0 (OSI permisiva) | sin grupo |
| `arrow` | datos | Formato columnar en memoria y conjunto de bibliotecas multilenguaje para… | 2 Intermedio | 70 | Apache-2.0 (OSI permisiva) | sin grupo |
| `duckdb` | datos | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y… | 2 Intermedio | 68 | MIT (OSI permisiva) | alternativa |
| `polars` | datos | Motor de consultas y DataFrames en Rust con API Python para procesar datos… | 2 Intermedio | 67 | MIT (OSI permisiva) | alternativa |
| `dbt` | datos | Herramienta para transformar datos dentro del almacén con modelos SQL… | 2 Intermedio | 66 | Apache-2.0 (OSI permisiva) | sin grupo |
| `jupyterlab` | datos | Entorno web de Project Jupyter con notebooks, terminal, editor de texto y… | 1 Básico | 66 | BSD-3-Clause (OSI permisiva) | alternativa |
| `dlt` | datos | Biblioteca Python para cargar datos de APIs, bases de datos y archivos en… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `delta-lake` | datos | Capa de almacenamiento con transacciones ACID sobre Parquet para montar un… | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | recomendado |
| `apache-iceberg` | datos | Formato abierto de tablas analíticas de la Apache Software Foundation; este… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `pygwalker` | datos | Convierte un DataFrame de pandas o Polars en una interfaz de exploración visual… | 2 Intermedio | 56 | Apache-2.0 (OSI permisiva) | sin grupo |
| `ibis` | datos | Biblioteca Python de dataframes portable: escribe la consulta una vez y… | 2 Intermedio | 55 | Apache-2.0 (OSI permisiva) | sin grupo |
| `hudi` | datos | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas… | 3 Avanzado | 51 | Apache-2.0 (OSI permisiva) | alternativa |
| `awesome-bigdata` | datos | Directorio curado de frameworks, bases de datos y herramientas de big data… | 1 Básico | 46 | MIT (OSI permisiva) | sin grupo |
| `globalbuildingatlas` | datos | Dataset global y código de procesamiento de edificios con polígonos, alturas y… | 1 Básico | 35 | MIT + Commons Clause (source-available) | sin grupo |
| `streamlit` | apps | Framework para levantar apps internas y prototipos de datos desde Python con… | 2 Intermedio | 76 | Apache-2.0 (OSI permisiva) | recomendado |
| `gradio` | apps | Librería Python para crear y compartir apps web de modelos de ML en minutos. | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | alternativa |
| `reflex` | apps | Framework para crear aplicaciones web completas (frontend y backend) solo con… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | alternativa |
| `dash` | apps | Framework para construir aplicaciones analíticas interactivas en Python… | 2 Intermedio | 69 | MIT (OSI permisiva) | sin grupo |
| `nicegui` | apps | Framework Python para interfaces web en el navegador con botones, gráficos… | 2 Intermedio | 68 | MIT (OSI permisiva) | alternativa |
| `panel` | apps | Framework de HoloViz para dashboards y apps de datos en Python que funcionan… | 2 Intermedio | 55 | BSD-3-Clause (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### ClickHouse (`clickhouse`)

- **Repo:** https://github.com/ClickHouse/ClickHouse · Apache-2.0 · nivel 2 · 80/100
- **Qué es:** Sistema de gestión de bases de datos columnar de código abierto (Apache-2.0) mantenido por ClickHouse Inc., que también vende ClickHouse Cloud. Muy activo, con versiones mensuales; en enero de 2026 la empresa adquirió Langfuse, que usa…
- **Cuándo elegirlo:** Casos: guardar y consultar logs, métricas o eventos de producto con latencias de segundos; servir de motor para dashboards analíticos sobre grandes volúmenes.
- **Requisitos:** nivel 2: preparación media; C++, CMakeLists.txt, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl https://clickhouse.com/ | sh` — fuente: https://github.com/ClickHouse/ClickHouse/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `curl https://clickhouse.com/ | sh` en una máquina de pruebas y consulta un CSV local con `./clickhouse local`. Éxito: Obtienes el resultado de la consulta SQL en la terminal sin levantar un servidor.
- **Combina con:** `langfuse` [23/observabilidad], `grafana` [10/bi], `metabase` [10/bi], `dbt`, `superset` [10/bi], `ibis`
- **Riesgos y avisos:** Alternativa cercana a DuckDB para analítica, pero orientada a servidor y clúster; DuckDB es embebida y local.

### pandas (`pandas`)

- **Repo:** https://github.com/pandas-dev/pandas · BSD-3-Clause · nivel 2 · 77/100 · recomendado en «Procesamiento de datos tabulares»
- **Qué es:** Biblioteca de código abierto (BSD-3-Clause) del proyecto pandas, patrocinado fiscalmente por NumFOCUS. Es la referencia de facto para el análisis de datos tabulares en Python y la base sobre la que se apoyan muchas otras herramientas.
- **Cuándo elegirlo:** Casos: limpiar y cruzar varios CSV o Excel antes de un informe; preparar un conjunto de datos para entrenar un modelo de scikit-learn.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install pandas` — fuente: https://github.com/pandas-dev/pandas/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install pandas`, carga un CSV con `pd.read_csv` y agrupa por una columna con `groupby().sum()`. Éxito: Obtienes un DataFrame resumido que puedes exportar a CSV o Parquet.
- **Combina con:** `jupyterlab`, `duckdb`, `scikit-learn` [24/entrenamiento], `arrow`, `pygwalker`, `reflex` [25/apps]
- **Alternativas:** `duckdb`, `polars`
- **Riesgos y avisos:** Para volúmenes grandes, Polars (alternativa) o DuckDB suelen ser más rápidos y usan menos memoria; pandas sigue siendo la API más compatible con el ecosistema.

### marimo (`marimo`)

- **Repo:** https://github.com/marimo-team/marimo · Apache-2.0 · nivel 1 · 76/100 · recomendado en «Notebooks»
- **Qué es:** marimo, notebook reactivo de Python que se guarda como script `.py`, de marimo-team. Licencia Apache-2.0. Es maduro y activo (~24k estrellas, 0.25.2).
- **Cuándo elegirlo:** Casos: Explorar datos en un notebook; Convertir un análisis en una app.
- **Requisitos:** nivel 1: preparación sencilla; Python; entorno de notebook; CSV pequeño; modelo solo para funciones AI; hardware prerequisites; API de IA: opcional; Python; entorno de notebook; CSV pequeño; modelo solo para funciones AI.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install marimo && marimo tutorial intro` — fuente: https://github.com/marimo-team/marimo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Completa el tutorial intro y modifica una variable para ver qué celdas se recalculan Éxito: Puedes reconocer dependencias reactivas y el archivo Python guardado
- **Combina con:** `duckdb`, `polars`, `ollama` [8/motores]
- **Alternativas:** `jupyterlab`
- **Riesgos y avisos:** Alternativa (elige una): jupyterlab. Documenta pair con Claude Code y Codex; usar un notebook local no implica que el asistente AI también sea local.

### Apache Spark (`spark`)

- **Repo:** https://github.com/apache/spark · Apache-2.0 · nivel 3 · 76/100
- **Qué es:** Motor de procesamiento de datos distribuido de la Apache Software Foundation (Apache-2.0), estándar en big data desde hace más de una década y base de plataformas como Databricks. Muy activo.
- **Cuándo elegirlo:** Casos: procesar terabytes de logs o eventos en un clúster con SQL o PySpark; alimentar un lakehouse con Delta Lake o Iceberg mediante trabajos batch y streaming. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: motor distribuido; en local basta pip, en clúster es avanzado; Scala, pom.xml, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/apache/spark/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala PySpark (`pip install pyspark`) y procesa un CSV local con un DataFrame y una consulta SQL en modo local. Éxito: Obtienes el resultado agregado en la consola sin necesidad de clúster.
- **Combina con:** `delta-lake`, `apache-iceberg`, `hudi`, `pandas`, `arrow`, `dbt`
- **Riesgos y avisos:** Para datos que caben en una máquina, DuckDB o Polars suelen ser más simples y rápidos; Spark compensa en clúster.

### Apache Arrow (`arrow`)

- **Repo:** https://github.com/apache/arrow · Apache-2.0 · nivel 2 · 70/100
- **Qué es:** Proyecto de la Apache Software Foundation (Apache-2.0) que define un formato columnar estándar en memoria y lo implementa en muchos lenguajes. Es infraestructura compartida por pandas, Polars, DuckDB, Spark y muchos otros. Muy activo.
- **Cuándo elegirlo:** Casos: mover datos entre pandas, Polars, DuckDB y Spark sin serializar; leer y escribir Parquet o datasets particionados desde Python.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; C++, compose.yaml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/apache/arrow/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala PyArrow, lee un archivo Parquet con `pyarrow.parquet.read_table` y conviértelo a pandas. Éxito: Obtienes una tabla Arrow y su DataFrame equivalente.
- **Combina con:** `pandas`, `polars`, `duckdb`, `spark`
- **Riesgos y avisos:** Arrow es una pieza de infraestructura: rara vez se usa sola, sino como formato común entre herramientas.

### DuckDB (`duckdb`)

- **Repo:** https://github.com/duckdb/duckdb · MIT · nivel 2 · 68/100 · alternativa en «Procesamiento de datos tabulares»
- **Qué es:** DuckDB, base de datos analítica en proceso (in-process), de la DuckDB Foundation y DuckDB Labs. Licencia MIT. Es muy madura (~43k estrellas, v2.0.0).
- **Cuándo elegirlo:** Casos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; CLI o biblioteca para tu sistema; CSV pequeño; hardware prerequisites; API de IA: no; CLI o biblioteca para tu sistema; CSV pequeño.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://duckdb.org/docs/installation/
- **Primera prueba propuesta (no ejecutada):** Abre un CSV ficticio y consulta el total de registros y una suma por categoría Éxito: Puedes comparar el resultado con las filas originales
- **Combina con:** `marimo`, `superset` [10/bi], `timesfm` [24/modelos], `apache-iceberg`, `delta-lake`
- **Alternativas:** `pandas`, `polars`
- **Riesgos y avisos:** Alternativas (elige una): polars. Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor.

### Polars (`polars`)

- **Repo:** https://github.com/pola-rs/polars · MIT · nivel 2 · 67/100 · alternativa en «Procesamiento de datos tabulares»
- **Qué es:** Polars, motor de consultas y DataFrames escrito en Rust con API de Python (y Rust, Node, R), de pola-rs. Licencia MIT. Es muy madura (~40k estrellas, py-2.1.0).
- **Cuándo elegirlo:** Casos: Transformar tablas; Preparar datos antes de un dashboard.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; CSV pequeño; memoria para los datos; hardware prerequisites; API de IA: no; Python; CSV pequeño; memoria para los datos.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install polars` — fuente: https://github.com/pola-rs/polars/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee un archivo y agrupa por una columna para sumar otra Éxito: Puedes contrastar el resultado con una muestra calculada a mano
- **Combina con:** `marimo`, `timesfm` [24/modelos], `streamlit` [25/apps], `apache-iceberg`, `delta-lake`
- **Alternativas:** `pandas`, `duckdb`
- **Riesgos y avisos:** Alternativas (elige una): duckdb. Es un motor de consultas y DataFrames, no una app de BI; mayor velocidad que otra biblioteca depende del trabajo y configuración.

### dbt (`dbt`)

- **Repo:** https://github.com/dbt-labs/dbt · Apache-2.0 · nivel 2 · 66/100
- **Qué es:** Herramienta de transformación de datos de código abierto (Apache-2.0) de dbt Labs, muy extendida en equipos de analítica ("analytics engineering").
- **Cuándo elegirlo:** Casos: mantener las transformaciones de un almacén analítico como código revisable en Git; añadir pruebas de calidad (únicos, no nulos) a las tablas de un informe.
- **Requisitos:** nivel 2: preparación media; Rust, Cargo.toml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install dbt` — fuente: https://docs.getdbt.com/docs/local/install-dbt?version=2
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de instalación oficial, crea un proyecto con un modelo SELECT simple y ejecútalo con `dbt run` contra una base de pruebas. Éxito: El modelo aparece como tabla o vista en la base y `dbt test` informa de las pruebas.
- **Combina con:** `duckdb`, `clickhouse`, `spark`, `dagster` [1/motores], `airflow` [1/motores]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Los adaptadores comunitarios (dbt-duckdb, dbt-clickhouse, dbt-spark) se documentan para dbt v1; su soporte en v2 no se ha verificado [DATO NO VERIFICADO….

### JupyterLab (`jupyterlab`)

- **Repo:** https://github.com/jupyterlab/jupyterlab · BSD-3-Clause · nivel 1 · 66/100 · alternativa en «Notebooks»
- **Qué es:** Interfaz de nueva generación de Project Jupyter (organización jupyterlab), en TypeScript y Python con licencia BSD-3-Clause. Es el repositorio canónico de la experiencia de notebook de Jupyter; la rama 3 dejó de mantenerse en 2024.
- **Cuándo elegirlo:** Casos: Analizar datos de muestra en un notebook; Documentar un experimento con código y resultados.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; TypeScript, package.json, pyproject.toml; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install jupyterlab` — fuente: https://github.com/jupyterlab/jupyterlab/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un notebook, carga un CSV ficticio y dibuja un gráfico simple Éxito: El notebook guarda código, tabla y gráfico al reabrirlo
- **Combina con:** `pytorch` [24/entrenamiento], `tensorflow` [24/entrenamiento], `duckdb`, `polars`, `apache-iceberg`, `delta-lake`
- **Alternativas:** `marimo`
- **Riesgos y avisos:** Alternativa (elige una): marimo. Los notebooks .ipynb se versionan mal en Git; considera jupytext o marimo si te importa.

### dlt (data load tool) (`dlt`)

- **Repo:** https://github.com/dlt-hub/dlt · Apache-2.0 · nivel 2 · 64/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) de dltHub. Se presenta como "una biblioteca, no una plataforma". Desde marzo de 2026 la empresa ofrece dltHub, una plataforma gestionada con licencia comercial. Activa.
- **Cuándo elegirlo:** Casos: volcar los datos de una API REST paginada en DuckDB para analizarlos; sincronizar tablas de una base SQL a un almacén analítico cada día.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "dlt[duckdb]"` — fuente: https://github.com/dlt-hub/dlt/blob/devel/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install "dlt[duckdb]"`, define una fuente REST pequeña y ejecuta el pipeline con destino DuckDB. Éxito: Obtienes un archivo DuckDB con tablas tipadas creadas por dlt.
- **Combina con:** `duckdb`, `airflow` [1/motores], `ibis`, `marimo`, `dagster` [1/motores]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### Delta Lake (`delta-lake`)

- **Repo:** https://github.com/delta-io/delta · Apache-2.0 · nivel 2 · 63/100 · recomendado en «Formatos de tabla para data lakes»
- **Qué es:** Framework de almacenamiento abierto Delta Lake (organización delta-io), en Scala con licencia Apache-2.0. Este repositorio contiene el conector de Spark, Delta Kernel, conectores y el protocolo; delta-rs es la implementación nativa en…
- **Cuándo elegirlo:** Casos: Añadir transacciones y versiones a archivos Parquet; Recuperar una versión anterior de una tabla.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Scala, Dockerfile, build.sbt; hardware prerequisites; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install delta-spark==4.0.0` — fuente: https://github.com/delta-io/delta/blob/master/docs/src/content/docs/quick-start.mdx
- **Primera prueba propuesta (no ejecutada):** Escribe una tabla Delta local, actualiza unas filas y lee la versión 0 Éxito: La versión 0 muestra los datos originales
- **Combina con:** `duckdb`, `polars`, `jupyterlab`, `spark`
- **Alternativas:** `apache-iceberg`, `hudi`
- **Riesgos y avisos:** Alternativas (elige una): apache-iceberg, hudi. Delta UniForm acerca ambos formatos: Delta puede publicar metadatos Iceberg.

### Apache Iceberg (`apache-iceberg`)

- **Repo:** https://github.com/apache/iceberg · Apache-2.0 · nivel 2 · 62/100 · alternativa en «Formatos de tabla para data lakes»
- **Qué es:** Formato abierto de tablas analíticas, proyecto de primer nivel de la Apache Software Foundation, con licencia Apache-2.0. Este repositorio contiene la biblioteca Java de referencia; hay implementaciones oficiales en Python (PyIceberg), Go…
- **Cuándo elegirlo:** Casos: Compartir una tabla analítica entre varios motores; Consultar un snapshot anterior tras un cambio de esquema.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Java, build.gradle; hardware prerequisites; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/apache/iceberg/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una tabla Iceberg pequeña con PyIceberg, añade una columna y consulta el snapshot previo Éxito: El snapshot anterior conserva el esquema original
- **Combina con:** `duckdb`, `polars`, `jupyterlab`, `spark`
- **Alternativas:** `delta-lake`, `hudi`
- **Riesgos y avisos:** Alternativas (elige una): delta-lake, hudi. Para consultas locales pequeñas suele bastar Parquet con DuckDB; Iceberg aporta valor con varios motores o….

### PyGWalker (`pygwalker`)

- **Repo:** https://github.com/Kanaries/pygwalker · Apache-2.0 · nivel 2 · 56/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) de Kanaries, enlace Python de Graphic Walker. Kanaries ofrece además servicios en la nube y una app de escritorio. Último push en septiembre de 2026.
- **Cuándo elegirlo:** Casos: explorar un conjunto de datos nuevo con gráficos de arrastrar y soltar sin escribir código de visualización; publicar una exploración interactiva de datos dentro de una app de Streamlit.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install pygwalker` — fuente: https://github.com/Kanaries/pygwalker/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install pygwalker` y, en un notebook, ejecuta `pyg.walk(df)` con un DataFrame. Éxito: Aparece una interfaz donde arrastras columnas para crear gráficos.
- **Combina con:** `pandas`, `polars`, `duckdb`, `jupyterlab`, `streamlit` [25/apps]

### Ibis (`ibis`)

- **Repo:** https://github.com/ibis-project/ibis · Apache-2.0 · nivel 2 · 55/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) con gobierno independiente; su desarrollo lo impulsó durante años Voltron Data. Activa.
- **Cuándo elegirlo:** Casos: desarrollar una transformación en local con DuckDB y ejecutarla después en un almacén en la nube; escribir lógica de datos sin atarse al dialecto SQL de un motor.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, compose.yaml, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install 'ibis-framework[duckdb,examples]'` — fuente: https://github.com/ibis-project/ibis/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install 'ibis-framework[duckdb,examples]'` y filtra un conjunto de ejemplo en modo interactivo. Éxito: Obtienes la tabla resultante calculada por DuckDB.
- **Combina con:** `duckdb`, `polars`, `clickhouse`, `spark`, `pandas`, `dlt`

### hudi (`hudi`)

- **Repo:** https://github.com/apache/hudi · Apache-2.0 · nivel 3 · 51/100 · alternativa en «Formatos de tabla para data lakes»
- **Qué es:** Apache Hudi, plataforma de data lakehouse abierta sobre un formato de tabla de alto rendimiento, de la Apache Software Foundation. Licencia Apache-2.0. Es madura (~6.4k estrellas, release-1.2.1).
- **Cuándo elegirlo:** Casos: Estudiar un lakehouse; Preparar ingestión incremental.
- **Requisitos:** nivel 3: preparación pesada; Java y Spark o Flink compatibles; almacenamiento de prueba; datos pequeños; hardware prerequisites; API de IA: no; Java y Spark o Flink compatibles; almacenamiento de prueba; datos pequeños.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/apache/hudi.git && cd hudi` — fuente: https://github.com/apache/hudi/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Inserta registros ficticios y actualiza uno para comparar estado y consulta incremental Éxito: Puedes comprobar la actualización sin reconstruir manualmente toda la tabla
- **Combina con:** `duckdb`, `superset` [10/bi], `awesome-bigdata`, `spark`
- **Alternativas:** `delta-lake`, `apache-iceberg`
- **Riesgos y avisos:** Alternativas (elige una): apache-iceberg, delta-lake. Los comandos para compilar snapshots son para desarrollo; el quickstart de la versión elegida debe coincidir con Spark o Flink instalados.

### awesome-bigdata (`awesome-bigdata`)

- **Repo:** https://github.com/oxnr/awesome-bigdata · MIT · nivel 1 · 46/100
- **Qué es:** Awesome Big Data, lista curada de frameworks, bases de datos y recursos de big data, mantenida por @oxnr desde 2014. Licencia MIT. Tiene ~15k estrellas y recibe contribuciones activas.
- **Cuándo elegirlo:** Casos: Explorar el ecosistema de datos; Comparar motores antes de montar infraestructura.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; problema de datos definido; hardware prerequisites; API de IA: no; Navegador; problema de datos definido.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/oxnr/awesome-bigdata/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Busca una herramienta de streaming y otra de almacenamiento y compara qué función resuelve cada una Éxito: Puedes elegir candidatos complementarios
- **Combina con:** `awesome-dataviz` [10/recursos], `duckdb`, `hudi`
- **Riesgos y avisos:** Sin alternativas declaradas. Recurso, no software. No se instala la colección entera ni se hereda la compatibilidad de sus enlaces.

### GlobalBuildingAtlas (`globalbuildingatlas`)

- **Repo:** https://github.com/zhu-xlab/GlobalBuildingAtlas · MIT + Commons Clause · nivel 1 · 35/100
- **Qué es:** GlobalBuildingAtlas, dataset global de edificios en nivel de detalle LoD1 (polígonos, alturas y modelos 3D) del grupo zhu-xlab (TUM). Tiene licencias mixtas: polígonos ODbL más polígonos, LoD1 y mapas de altura CC BY-NC 4.0 (GitHub muestra…
- **Cuándo elegirlo:** Casos: Explorar edificios en un GIS; Preparar una escena urbana de prueba.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador o GIS; espacio de descarga; zona pequeña; licencia de la capa; hardware prerequisites; API de IA: no; Navegador o GIS; espacio de descarga; zona pequeña; licencia de la capa.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona una zona y distingue polígonos, alturas y LoD1 antes de descargar una capa Éxito: Puedes identificar formato, licencia y escala del dato
- **Combina con:** `three.js` [26/animacion], `duckdb`, `3dviz-pro-max` [27/skills]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Ojo con la parte CC BY-NC para usos comerciales. GBA.ODbLPolygon usa ODbL, mientras otras capas de polígonos, LoD1 y alturas usan CC BY-NC 4.0; no toda la colección permite el mismo uso comercial.

### streamlit (`streamlit`)

- **Repo:** https://github.com/streamlit/streamlit · Apache-2.0 · nivel 2 · 76/100 · recomendado en «Apps web de datos en Python»
- **Qué es:** Streamlit, framework de apps de datos en Python, propiedad de Snowflake. Licencia Apache-2.0. Es muy maduro (~46k estrellas, 1.67.0) y ahora se presenta como «agent-native».
- **Cuándo elegirlo:** Casos: Preparar un dashboard de ventas ficticias; Explorar un simulador de demanda.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; script pequeño; datos ficticios; hardware prerequisites; API de IA: opcional; Python; script pequeño; datos ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install streamlit` — fuente: https://github.com/streamlit/streamlit/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una app con un control y una tabla de ejemplo y comprueba que la interacción actualiza la vista Éxito: Puedes identificar script, estado y resultado
- **Combina con:** `dash`, `polars` [25/datos], `duckdb` [25/datos], `awesome-llm-apps` [19/guias], `pygwalker` [25/datos]
- **Alternativas:** `gradio`, `reflex`, `nicegui`, `panel`
- **Riesgos y avisos:** Alternativas (elige una): gradio. Streamlit skills instala instrucciones para Claude Code y agentes que leen .agents; no convierte la suscripción del agente en backend de cualquier app creada.

### Gradio (`gradio`)

- **Repo:** https://github.com/gradio-app/gradio · Apache-2.0 · nivel 2 · 71/100 · alternativa en «Apps web de datos en Python»
- **Qué es:** Gradio, paquete Python para crear demos y apps web de modelos de ML, APIs o cualquier función, mantenido por Hugging Face. Licencia Apache-2.0. Es muy maduro (~44k estrellas, gradio@6.32.0).
- **Cuándo elegirlo:** Casos: Crear una demo de un modelo; Preparar una herramienta interna de texto.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python 3.10+; función o modelo de prueba; hardware prerequisites; API de IA: opcional; Python 3.10+; función o modelo de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install --upgrade gradio` — fuente: https://github.com/gradio-app/gradio/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una interfaz para una función simple de texto y pruébala localmente antes de compartir un enlace Éxito: Puedes ver la relación entre entrada, función y salida
- **Combina con:** `transformers` [24/entrenamiento], `llama-factory` [24/entrenamiento], `ollama` [8/motores], `rembg` [11/edicion], `f5-tts` [29/tts]
- **Alternativas:** `streamlit`, `reflex`, `nicegui`, `panel`
- **Riesgos y avisos:** Alternativas (elige una): streamlit. Incluye skills para agentes compatibles con .agents y ruta Claude; una URL de compartir expone la app y no sustituye autenticación o alojamiento de producción.

### Reflex (`reflex`)

- **Repo:** https://github.com/reflex-dev/reflex · Apache-2.0 · nivel 2 · 71/100 · alternativa en «Apps web de datos en Python»
- **Qué es:** Framework de código abierto (Apache-2.0) de Reflex Inc. para aplicaciones web full-stack en Python puro. La empresa ofrece además servicios comerciales: AI Builder, alojamiento gestionado y una edición Enterprise.
- **Cuándo elegirlo:** Casos: construir un panel interno o una herramienta con formularios y tablas sin escribir JavaScript; prototipar una app de IA con estado, como un generador de imágenes.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `uv add reflex` — fuente: https://github.com/reflex-dev/reflex/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un proyecto con `uv init`, ejecuta `uv add reflex`, `uv run reflex init` y `uv run reflex run`. Éxito: La app de ejemplo se abre en http://localhost:3000 y se recarga al editar el código.
- **Combina con:** `claude-code` [20/terminal], `pandas` [25/datos], `coolify` [22/infraestructura]
- **Alternativas:** `streamlit`, `gradio`, `nicegui`, `panel`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Es alternativa de Streamlit, Gradio, NiceGUI y Panel: Reflex apunta a apps completas con varias páginas y estado; Streamlit y Gradio a prototipos y demos….

### dash (`dash`)

- **Repo:** https://github.com/plotly/dash · MIT · nivel 2 · 69/100
- **Qué es:** Dash, framework de Plotly para construir apps analíticas web en Python (también R y Julia), sobre Plotly.js, React y Flask. Licencia MIT. Es maduro (~24k estrellas, v4.5.0) y tiene versión comercial (Dash Enterprise).
- **Cuándo elegirlo:** Casos: Crear un tablero interactivo; Comparar escenarios con controles.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; entorno de desarrollo; datos de muestra; hardware prerequisites; API de IA: no; Python; entorno de desarrollo; datos de muestra.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://dash.plotly.com/getting-started
- **Primera prueba propuesta (no ejecutada):** Sigue la app inicial y conecta un selector a un gráfico pequeño Éxito: Puedes comprobar qué callback cambia la figura
- **Combina con:** `streamlit`, `echarts` [10/graficos], `duckdb` [25/datos]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Es un framework Python; el README mezcla ejemplos OSS y funciones Enterprise que no vienen todas con el paquete básico.

### NiceGUI (`nicegui`)

- **Repo:** https://github.com/zauberzeug/nicegui · MIT · nivel 2 · 68/100 · alternativa en «Apps web de datos en Python»
- **Qué es:** Framework de interfaz de código abierto (MIT) creado por Zauberzeug, una empresa alemana de robótica. Activo, con paquetes en PyPI, Docker y conda-forge.
- **Cuándo elegirlo:** Casos: crear un panel de control para un robot o una casa domótica; hacer una pequeña herramienta web para ajustar parámetros de un algoritmo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, docker-compose.yml, package.json, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python3 -m pip install nicegui` — fuente: https://github.com/zauberzeug/nicegui/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `python3 -m pip install nicegui`, escribe un script con `ui.label` y `ui.button` y ejecútalo con `ui.run()`. Éxito: La interfaz se abre en el navegador (puerto 8080) y se recarga al guardar.
- **Combina con:** `leaflet` [10/geoespacial], `echarts` [10/graficos], `three.js` [26/animacion], `pandas` [25/datos]
- **Alternativas:** `streamlit`, `gradio`, `reflex`, `panel`
- **Riesgos y avisos:** Alternativa de Streamlit, Gradio, Panel y Reflex; destaca para control de hardware y robótica por su modelo de eventos.

### Panel (`panel`)

- **Repo:** https://github.com/holoviz/panel · BSD-3-Clause · nivel 2 · 55/100 · alternativa en «Apps web de datos en Python»
- **Qué es:** Framework de código abierto (BSD-3-Clause) del ecosistema HoloViz, respaldado por Anaconda y otros patrocinadores. Activo y maduro.
- **Cuándo elegirlo:** Casos: convertir un análisis de notebook en un dashboard interactivo para el equipo; crear una plataforma interna con varias páginas, tablas editables y autenticación.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install panel` — fuente: https://github.com/holoviz/panel/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install panel`, crea `app.py` con un widget enlazado a un gráfico y ejecútalo con `panel serve app.py --dev`. Éxito: El dashboard se abre en el navegador y responde a los controles.
- **Combina con:** `jupyterlab` [25/datos], `marimo` [25/datos], `claude-code` [20/terminal], `deck.gl` [10/geoespacial], `echarts` [10/graficos]
- **Alternativas:** `streamlit`, `gradio`, `reflex`, `nicegui`
- **Riesgos y avisos:** Panel publica una comparación con Streamlit en su documentación; ambos están agrupados como alternativas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-25.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Procesar datos y trabajar con notebooks», lee `docs/alexandria/categoria-25.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-25.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
