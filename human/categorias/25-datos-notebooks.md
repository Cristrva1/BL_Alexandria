[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Procesar datos y trabajar con notebooks

Motores de consulta, tablas, notebooks y aplicaciones de datos. Empieza por un archivo pequeño y distingue una herramienta de análisis de un catálogo o conjunto de datos de referencia.

23 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [DuckDB](../fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | Sin clave propia de API de IA en la ruta básica |
| [marimo](../fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | API de IA opcional |
| [Gradio](../fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | API de IA opcional |

## Secciones

- [Datos y notebooks](#datos-y-notebooks) — 17 repos
- [Apps de datos en Python](#apps-de-datos-en-python) — 6 repos

## Datos y notebooks

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [DuckDB](../fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | Tu objetivo encaja con estos ejemplos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor | Sin clave propia de API de IA en la ruta básica |
| [marimo](../fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | Tu objetivo encaja con estos ejemplos: Explorar datos en un notebook; Convertir un análisis en una app | API de IA opcional |
| [ClickHouse](../fichas/clickhouse.md) | Base de datos analítica columnar de código abierto para consultas SQL en tiempo real sobre miles de millones de filas, autoalojable o en la nube. | Tu objetivo encaja con estos ejemplos: guardar y consultar logs, métricas o eventos de producto con latencias de segundos; servir de motor para dashboards analíticos sobre grandes volúmenes | Sin clave propia de API de IA en la ruta básica |
| [pandas](../fichas/pandas.md) | Biblioteca estándar de Python para analizar y transformar datos tabulares con DataFrame y Series: limpieza, agrupaciones, uniones, series temporales y E/S. | Tu objetivo encaja con estos ejemplos: limpiar y cruzar varios CSV o Excel antes de un informe; preparar un conjunto de datos para entrenar un modelo de scikit-learn | Sin clave propia de API de IA en la ruta básica |
| [Apache Spark](../fichas/spark.md) | Motor unificado de Apache para procesar datos a gran escala en clúster: SQL y DataFrames, streaming, machine learning (MLlib) y API de pandas sobre Spark. | Tu objetivo encaja con estos ejemplos: procesar terabytes de logs o eventos en un clúster con SQL o PySpark; alimentar un lakehouse con Delta Lake o Iceberg mediante trabajos batch y streaming | Sin clave propia de API de IA en la ruta básica |
| [Polars](../fichas/polars.md) | Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares. | Tu objetivo encaja con estos ejemplos: Transformar tablas; Preparar datos antes de un dashboard | Sin clave propia de API de IA en la ruta básica |
| [Apache Arrow](../fichas/arrow.md) | Formato columnar en memoria y conjunto de bibliotecas multilenguaje para intercambiar y analizar datos sin copias entre procesos y herramientas. | Tu objetivo encaja con estos ejemplos: mover datos entre pandas, Polars, DuckDB y Spark sin serializar; leer y escribir Parquet o datasets particionados desde Python | Sin clave propia de API de IA en la ruta básica |
| [PyGWalker](../fichas/pygwalker.md) | Convierte un DataFrame de pandas o Polars en una interfaz de exploración visual tipo Tableau dentro de Jupyter, Streamlit o marimo, arrastrando campos. | Tu objetivo encaja con estos ejemplos: explorar un conjunto de datos nuevo con gráficos de arrastrar y soltar sin escribir código de visualización; publicar una exploración interactiva de datos dentro de una app de Streamlit | Sin clave propia de API de IA en la ruta básica |
| [JupyterLab](../fichas/jupyterlab.md) | Entorno web de Project Jupyter con notebooks, terminal, editor de texto y explorador de archivos, ampliable mediante extensiones. | Tu objetivo encaja con estos ejemplos: Analizar datos de muestra en un notebook; Documentar un experimento con código y resultados | Sin clave propia de API de IA en la ruta básica |
| [awesome-bigdata](../fichas/awesome-bigdata.md) | Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala. | Tu objetivo encaja con estos ejemplos: Explorar el ecosistema de datos; Comparar motores antes de montar infraestructura | Sin clave propia de API de IA en la ruta básica |
| [dbt](../fichas/dbt.md) | Herramienta para transformar datos dentro del almacén con modelos SQL versionados, pruebas, documentación y dependencias, como se hace con el software. | Tu objetivo encaja con estos ejemplos: mantener las transformaciones de un almacén analítico como código revisable en Git; añadir pruebas de calidad (únicos, no nulos) a las tablas de un informe | Sin clave propia de API de IA en la ruta básica |
| [Apache Iceberg](../fichas/apache-iceberg.md) | Formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java. | Tu objetivo encaja con estos ejemplos: Compartir una tabla analítica entre varios motores; Consultar un snapshot anterior tras un cambio de esquema | Sin clave propia de API de IA en la ruta básica |
| [Delta Lake](../fichas/delta-lake.md) | Capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores. | Tu objetivo encaja con estos ejemplos: Añadir transacciones y versiones a archivos Parquet; Recuperar una versión anterior de una tabla | Sin clave propia de API de IA en la ruta básica |
| [Ibis](../fichas/ibis.md) | Biblioteca Python de dataframes portable: escribe la consulta una vez y ejecútala en DuckDB, Polars, ClickHouse, Spark, Postgres o más de 20 motores. | Tu objetivo encaja con estos ejemplos: desarrollar una transformación en local con DuckDB y ejecutarla después en un almacén en la nube; escribir lógica de datos sin atarse al dialecto SQL de un motor | Sin clave propia de API de IA en la ruta básica |
| [hudi](../fichas/hudi.md) | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. | Tu objetivo encaja con estos ejemplos: Estudiar un lakehouse; Preparar ingestión incremental | Sin clave propia de API de IA en la ruta básica |
| [dlt (data load tool)](../fichas/dlt.md) | Biblioteca Python para cargar datos de APIs, bases de datos y archivos en destinos como DuckDB, Postgres o almacenes en la nube, con esquema y carga incremental. | Tu objetivo encaja con estos ejemplos: volcar los datos de una API REST paginada en DuckDB para analizarlos; sincronizar tablas de una base SQL a un almacén analítico cada día | Sin clave propia de API de IA en la ruta básica |
| [GlobalBuildingAtlas](../fichas/globalbuildingatlas.md) | Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. | Tu objetivo encaja con estos ejemplos: Explorar edificios en un GIS; Preparar una escena urbana de prueba | Sin clave propia de API de IA en la ruta básica |

## Apps de datos en Python

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Gradio](../fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | Tu objetivo encaja con estos ejemplos: Crear una demo de un modelo; Preparar una herramienta interna de texto | API de IA opcional |
| [streamlit](../fichas/streamlit.md) | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. | Tu objetivo encaja con estos ejemplos: Preparar un dashboard de ventas ficticias; Explorar un simulador de demanda | API de IA opcional |
| [Reflex](../fichas/reflex.md) | Framework para crear aplicaciones web completas (frontend y backend) solo con Python, con estado en clases, componentes y despliegue propio o gestionado. | Tu objetivo encaja con estos ejemplos: construir un panel interno o una herramienta con formularios y tablas sin escribir JavaScript; prototipar una app de IA con estado, como un generador de imágenes | Sin clave propia de API de IA en la ruta básica |
| [dash](../fichas/dash.md) | Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. | Tu objetivo encaja con estos ejemplos: Crear un tablero interactivo; Comparar escenarios con controles | Sin clave propia de API de IA en la ruta básica |
| [NiceGUI](../fichas/nicegui.md) | Framework Python para interfaces web en el navegador con botones, gráficos, mapas, tablas y escenas 3D, útil para paneles, robótica y herramientas internas. | Tu objetivo encaja con estos ejemplos: crear un panel de control para un robot o una casa domótica; hacer una pequeña herramienta web para ajustar parámetros de un algoritmo | Sin clave propia de API de IA en la ruta básica |
| [Panel](../fichas/panel.md) | Framework de HoloViz para dashboards y apps de datos en Python que funcionan igual en un notebook y como aplicación web servida con `panel serve`. | Tu objetivo encaja con estos ejemplos: convertir un análisis de notebook en un dashboard interactivo para el equipo; crear una plataforma interna con varias páginas, tablas editables y autenticación | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Analítica de producto con IA](../playbooks/analitica-con-ia.md) — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
