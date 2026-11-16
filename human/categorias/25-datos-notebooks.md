[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Procesar datos y trabajar con notebooks

Motores de consulta, tablas, notebooks y aplicaciones de datos. Empieza por un archivo pequeño y distingue una herramienta de análisis de un catálogo o conjunto de datos de referencia.

9 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [DuckDB](../fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | Sin clave propia de API de IA en la ruta básica |
| [marimo](../fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | API de IA opcional |
| [Gradio](../fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | API de IA opcional |

## Secciones

- [Datos y notebooks](#datos-y-notebooks) — 6 repos
- [Apps de datos en Python](#apps-de-datos-en-python) — 3 repos

## Datos y notebooks

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [DuckDB](../fichas/duckdb.md) | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | Tu objetivo encaja con estos ejemplos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor | Sin clave propia de API de IA en la ruta básica |
| [marimo](../fichas/marimo.md) | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. | Tu objetivo encaja con estos ejemplos: Explorar datos en un notebook; Convertir un análisis en una app | API de IA opcional |
| [Polars](../fichas/polars.md) | Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares. | Tu objetivo encaja con estos ejemplos: Transformar tablas; Preparar datos antes de un dashboard | Sin clave propia de API de IA en la ruta básica |
| [awesome-bigdata](../fichas/awesome-bigdata.md) | Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala. | Tu objetivo encaja con estos ejemplos: Explorar el ecosistema de datos; Comparar motores antes de montar infraestructura | Sin clave propia de API de IA en la ruta básica |
| [hudi](../fichas/hudi.md) | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. | Tu objetivo encaja con estos ejemplos: Estudiar un lakehouse; Preparar ingestión incremental | Sin clave propia de API de IA en la ruta básica |
| [GlobalBuildingAtlas](../fichas/globalbuildingatlas.md) | Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. | Tu objetivo encaja con estos ejemplos: Explorar edificios en un GIS; Preparar una escena urbana de prueba | Sin clave propia de API de IA en la ruta básica |

## Apps de datos en Python

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Gradio](../fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | Tu objetivo encaja con estos ejemplos: Crear una demo de un modelo; Preparar una herramienta interna de texto | API de IA opcional |
| [streamlit](../fichas/streamlit.md) | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. | Tu objetivo encaja con estos ejemplos: Preparar un dashboard de ventas ficticias; Explorar un simulador de demanda | API de IA opcional |
| [dash](../fichas/dash.md) | Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. | Tu objetivo encaja con estos ejemplos: Crear un tablero interactivo; Comparar escenarios con controles | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Analítica de producto con IA](../playbooks/analitica-con-ia.md) — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
