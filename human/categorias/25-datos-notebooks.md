[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Procesar datos y trabajar con notebooks

Motores de consulta, tablas, notebooks y aplicaciones de datos. Empieza por un archivo pequeño y distingue una herramienta de análisis de un catálogo o conjunto de datos de referencia.

11 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [DuckDB](../fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | Sin API de IA en la ruta básica |
| [marimo](../fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | Sin API de IA en la ruta básica |
| [Gradio](../fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | Sin API de IA en la ruta básica |

## Secciones

- [Datos y notebooks](#datos-y-notebooks) — 8 repos
- [Apps de datos en Python](#apps-de-datos-en-python) — 3 repos

## Datos y notebooks

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [DuckDB](../fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | quieres SQL analítico rápido sin montar servidores | Sin API de IA en la ruta básica |
| [marimo](../fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | quieres notebooks reproducibles y versionables | Sin API de IA en la ruta básica |
| [Polars](../fichas/polars.md) | Librería de DataFrames escrita en Rust, mucho más rápida que pandas. | tu análisis con pandas es lento | Sin API de IA en la ruta básica |
| [data-science-ipython-notebooks](../fichas/data-science-ipython-notebooks.md) | Gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep learning y big data, con ejemplos listos para ejecutar. | estudias/consultas DS con ejemplos ejecutables | Sin API de IA en la ruta básica |
| [awesome-bigdata](../fichas/awesome-bigdata.md) | Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala. | diseñas pipelines de datos grandes y necesitas descubrir el ecosistema | Sin API de IA en la ruta básica |
| [hudi](../fichas/hudi.md) | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. | necesitas gestionar cambios y cargas incrementales en un data lake | Depende de la ruta elegida |
| [GlobalBuildingAtlas](../fichas/globalbuildingatlas.md) | Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. | necesitas geometría de edificios para análisis territorial o visualización urbana | Sin API de IA en la ruta básica |
| [BigData](../fichas/bigdata.md) | Colección educativa de proyectos de datos con ejercicios de Hive, HDFS, Spark, HBase y sistemas de recomendación. | quieres estudiar ejemplos prácticos del ecosistema de big data | Sin API de IA en la ruta básica |

## Apps de datos en Python

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Gradio](../fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | quieres una demo web de tu modelo rápido | Sin API de IA en la ruta básica |
| [streamlit](../fichas/streamlit.md) | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. | quieres una UI de datos al vuelo y prototipos rápidos | Sin API de IA en la ruta básica |
| [dash](../fichas/dash.md) | Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. | quieres dashboards productivos en Python con control del frontend | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Analítica de producto con IA](../playbooks/analitica-con-ia.md) — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
