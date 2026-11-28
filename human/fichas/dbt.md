[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🖥️ dbt

> Herramienta para transformar datos dentro del almacén con modelos SQL versionados, pruebas, documentación y dependencias, como se hace con el software.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.2k | Apache-2.0 | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de transformación de datos de código abierto (Apache-2.0) de dbt Labs, muy extendida en equipos de analítica ("analytics engineering"). La rama main contiene dbt v2.0, una reescritura en Rust distribuida como binario autocontenido; dbt v1 (Python) se mantiene en la rama `1.latest`. Existe además una plataforma comercial (dbt platform).

## ¿Qué hace?

Permite escribir transformaciones como sentencias SELECT ("modelos") que se apoyan unas en otras; dbt las convierte en tablas y vistas del almacén en el orden correcto, ejecuta pruebas de datos, gestiona semillas e instantáneas y genera documentación y un grafo de linaje. La v2 parsea y compila más rápido, es más estricta y produce artefactos en Parquet.

## ¿Cómo lo hace?

Compila SQL con plantillas Jinja y resuelve dependencias con `ref()`/`source()`; se conecta al almacén mediante adaptadores o drivers (DuckDB, Postgres, Snowflake, BigQuery, Spark, ClickHouse…). La v2 se instala como un único binario (macOS y Linux x86-64/ARM, Windows x86-64); la v1 con pip y el adaptador correspondiente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | El adaptador dbt-duckdb permite ejecutar proyectos dbt sobre DuckDB local, ideal para desarrollo y almacenes pequeños. | Instala dbt (v1) con `dbt-duckdb`; después configura el perfil con la ruta del archivo .duckdb. |
| [ClickHouse](clickhouse.md) | ClickHouse mantiene el adaptador oficial dbt-clickhouse para materializar modelos en ClickHouse. | Instala `dbt-clickhouse`; después configura el perfil con el host de ClickHouse. |
| [Apache Spark](spark.md) | El adaptador dbt-spark ejecuta los modelos dbt como SQL de Spark. | Instala `dbt-spark` con el método de conexión adecuado; después apunta el perfil al clúster. |
| [Dagster](dagster.md) | La biblioteca dagster-dbt carga los modelos de un proyecto dbt como assets de Dagster para orquestarlos y monitorizarlos. | Instala `dagster-dbt`; después carga el proyecto dbt con `@dbt_assets`. |
| [Apache Airflow](airflow.md) | Airflow se usa habitualmente para programar ejecuciones de dbt (por ejemplo con Astronomer Cosmos u operadores Bash). | Instala dbt en el entorno de Airflow; después crea un DAG que ejecute `dbt build`. |

**Notas:** Los adaptadores comunitarios (dbt-duckdb, dbt-clickhouse, dbt-spark) se documentan para dbt v1; su soporte en v2 no se ha verificado [DATO NO VERIFICADO: compatibilidad de adaptadores con v2]. La orquestación con Airflow es una combinación por arquitectura (Cosmos es un proyecto externo).

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.12.7 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dbt-labs/dbt/blob/main/README.md) · [2](https://docs.getdbt.com/docs/core/connect-data-platform/duckdb-setup) · [3](https://github.com/ClickHouse/dbt-clickhouse) · [4](https://docs.dagster.io/integrations/libraries/dbt)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (bash):**

```
python -m pip install dbt
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Install dbt​»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://docs.getdbt.com/docs/local/install-dbt?version=2)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dbt para mi objetivo y necesito pasos guiados. Lee https://docs.getdbt.com/docs/local/install-dbt?version=2. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la guía de instalación oficial, crea un proyecto con un modelo SELECT simple y ejecútalo con `dbt run` contra una base de pruebas..

**Qué comprobar:** El modelo aparece como tabla o vista en la base y `dbt test` informa de las pruebas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- mantener las transformaciones de un almacén analítico como código revisable en Git
- añadir pruebas de calidad (únicos, no nulos) a las tablas de un informe

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: mantener las transformaciones de un almacén analítico como código revisable en Git; añadir pruebas de calidad (únicos, no nulos) a las tablas de un informe | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La rama main es dbt v2 (reescritura en Rust); la implementación Python v1 sigue en la rama 1.latest. Revisa qué adaptadores admite cada versión.

## Stack y modelos

- **Stack:** Rust, Cargo.toml, pyproject.toml
- **Etiquetas:** `data` `sql` `etl` `analytics`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [dbt-labs/dbt](https://github.com/dbt-labs/dbt)
- 🌐 Web: <https://getdbt.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dbt-labs/dbt/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
