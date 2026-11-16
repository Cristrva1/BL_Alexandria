[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 📚 Ibis

> Biblioteca Python de dataframes portable: escribe la consulta una vez y ejecútala en DuckDB, Polars, ClickHouse, Spark, Postgres o más de 20 motores.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.7k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) con gobierno independiente; su desarrollo lo impulsó durante años Voltron Data. Activa.

## ¿Qué hace?

Ofrece una única API de dataframes que se traduce a más de 20 backends: DuckDB, Polars, DataFusion, PySpark, ClickHouse, Postgres, MySQL, SQLite, BigQuery, Snowflake, Trino, Databricks y otros. Las expresiones son perezosas, se pueden combinar con SQL y se ejecutan en el motor donde están los datos.

## ¿Cómo lo hace?

Se instala como `ibis-framework` con extras por backend. Construye un árbol de expresiones y lo compila a SQL (con SQLGlot) o a la API nativa del backend; DuckDB es el motor local por defecto. Cambiar de backend suele requerir solo cambiar la conexión.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | DuckDB es el backend local por defecto de Ibis. | Instala `ibis-framework[duckdb]`; después conecta con `ibis.duckdb.connect()`. |
| [Polars](polars.md) | Ibis incluye un backend de Polars. | Instala `ibis-framework[polars]`; después usa `ibis.polars.connect()`. |
| [ClickHouse](clickhouse.md) | Ibis incluye un backend de ClickHouse para ejecutar expresiones en un servidor ClickHouse. | Instala `ibis-framework[clickhouse]`; después conecta con `ibis.clickhouse.connect(...)`. |
| [Apache Spark](spark.md) | Ibis incluye un backend de PySpark para ejecutar las mismas expresiones en Spark. | Instala `ibis-framework[pyspark]`; después conecta con una sesión de Spark. |
| [pandas](pandas.md) | Los resultados de Ibis se materializan como DataFrame de pandas con `.to_pandas()`. | Construye la expresión con Ibis; después llama a `.to_pandas()`. |
| [dlt (data load tool)](dlt.md) | Combinación recíproca: dlt (data load tool) lo enlaza como «Las tablas cargadas pueden convertirse en expresiones de Ibis (`to_ibis()`) que dlt compila al SQL del destino». | Orden indicado desde dlt (data load tool): Carga los datos con dlt; después usa `pipeline.dataset().tabla.to_ibis()`. |

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 12.0.0 (2026-02-07) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ibis-project/ibis/blob/main/README.md) · [2](https://ibis-project.org/backends/duckdb/)</sub>

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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
pip install 'ibis-framework[duckdb,examples]'
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/ibis-project/ibis/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ibis para mi objetivo y necesito pasos guiados. Lee https://github.com/ibis-project/ibis/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install 'ibis-framework[duckdb,examples]'` y filtra un conjunto de ejemplo en modo interactivo..

**Qué comprobar:** Obtienes la tabla resultante calculada por DuckDB..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- desarrollar una transformación en local con DuckDB y ejecutarla después en un almacén en la nube
- escribir lógica de datos sin atarse al dialecto SQL de un motor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: desarrollar una transformación en local con DuckDB y ejecutarla después en un almacén en la nube; escribir lógica de datos sin atarse al dialecto SQL de un motor | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, compose.yaml, pyproject.toml
- **Etiquetas:** `data` `python` `dataframe` `sql`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ibis-project/ibis](https://github.com/ibis-project/ibis)
- 🌐 Web: <https://ibis-project.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ibis-project/ibis/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
