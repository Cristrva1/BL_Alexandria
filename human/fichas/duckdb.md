[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🗃️ DuckDB

> Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 43.1k | MIT | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

DuckDB, base de datos analítica en proceso (in-process), de la DuckDB Foundation y DuckDB Labs. Licencia MIT. Es muy madura (~43k estrellas, v2.0.0).

## ¿Qué hace?

Ejecuta SQL analítico muy rápido dentro de tu aplicación y lee y escribe CSV, Parquet, JSON y formatos lakehouse (Iceberg, Delta, DuckLake). Puede adjuntar y consultar en sitio otras bases de datos como Postgres, MySQL o SQLite.

## ¿Cómo lo hace?

Hay CLI independiente y clientes para Python, R, Java, Node, Rust, Go, WebAssembly y más. Las extensiones del núcleo vienen incluidas y las comunitarias se cargan bajo demanda. La instalación por plataforma está en duckdb.org.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [marimo](marimo.md) | Celdas SQL nativas sobre DuckDB. | Instala marimo y escribe celdas SQL. |
| [Apache Superset](superset.md) | Dashboards sobre DuckDB. (combinación por arquitectura) | Conecta DuckDB como base de datos. |
| [TimesFM](timesfm.md) | Preparar series temporales para pronóstico. (combinación por arquitectura) | Extrae las series con SQL. |
| [Apache Iceberg](apache-iceberg.md) | DuckDB lee tablas Apache Iceberg con su extensión oficial `iceberg`. | Carga la extensión y consulta una tabla de prueba. |
| [Delta Lake](delta-lake.md) | DuckDB lee tablas Delta Lake con su extensión oficial `delta`. | Carga la extensión `delta` y apunta al directorio de la tabla. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (32). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Apache Airflow](airflow.md) · [Apache Arrow](arrow.md) · [awesome-bigdata](awesome-bigdata.md) · [Chart.js](chart-js.md) · [Colly](colly.md) · [Dagster](dagster.md) · [dash](dash.md) · [data-analyst-roadmap](data-analyst-roadmap.md) · [dbt](dbt.md) · [dlt (data load tool)](dlt.md) · [Evidence](evidence.md) · [GlobalBuildingAtlas](globalbuildingatlas.md) · [Grist](grist-core.md) · [hudi](hudi.md) · [Ibis](ibis.md) · [JupyterLab](jupyterlab.md) · [Katana](katana.md) · [Kestra](kestra.md) · [LanceDB](lancedb.md) · [Maigret](maigret.md) · [metabase](metabase.md) · [pandas](pandas.md) · [Prefect](prefect.md) · [PyGWalker](pygwalker.md) · [QGIS](qgis.md) · [Recon-ng](recon-ng.md) · [Redash](redash.md) · [Sherlock](sherlock.md) · [streamlit](streamlit.md) · [uPlot](uplot.md) · [Windmill](windmill.md) · [WrenAI](wrenai.md)

**Notas:** Alternativas (elige una): polars.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v2.0.0 (2026-10-21) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/duckdb/duckdb/blob/main/README.md) · [2](https://duckdb.org/docs/installation/)</sub>

## Ver similares

Grupo **Procesamiento de datos tabulares**: DuckDB ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [pandas](pandas.md) ⭐ recomendado | 77 | Si buscas esto: biblioteca estándar de Python para analizar y transformar datos tabulares con DataFrame y Series: limpieza, agrupaciones, uniones, series temporales y E/S. |
| 2 | **DuckDB** (esta ficha) | 68 | Si buscas esto: base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |
| 3 | [Polars](polars.md) | 67 | Si buscas esto: motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa LLM ni API de IA; servicios Cloud o almacenamiento remoto tienen sus condiciones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor |
| Coste | Sin pago a un modelo en la ruta básica. No usa LLM ni API de IA; servicios Cloud o almacenamiento remoto tienen sus condiciones |
| Equipo | Preparación según la ruta elegida. CLI o biblioteca para tu sistema; CSV pequeño |

Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- CLI o biblioteca para tu sistema
- CSV pequeño

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://duckdb.org/docs/installation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DuckDB para mi objetivo y necesito pasos guiados. Lee https://duckdb.org/docs/installation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un CSV ficticio y consulta el total de registros y una suma por categoría.

**Qué comprobar:** Puedes comparar el resultado con las filas originales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar ventas de muestra
- Consultar Parquet sin desplegar un servidor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor

## Stack y modelos

- **Stack:** CLI o biblioteca para tu sistema; CSV pequeño
- **Etiquetas:** `data` `analytics` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Polars](polars.md) | 40.3k | Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares. |

## Enlaces

- 🐙 GitHub: [duckdb/duckdb](https://github.com/duckdb/duckdb)
- 🌐 Web: <http://www.duckdb.org>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/duckdb/duckdb/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
