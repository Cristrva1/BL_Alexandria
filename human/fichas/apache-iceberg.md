[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 📚 Apache Iceberg

> Formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.4k | Apache-2.0 | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Formato abierto de tablas analíticas, proyecto de primer nivel de la Apache Software Foundation, con licencia Apache-2.0. Este repositorio contiene la biblioteca Java de referencia; hay implementaciones oficiales en Python (PyIceberg), Go, Rust y C++. Versión 1.12.0 (septiembre de 2026), en desarrollo activo.

## ¿Qué hace?

Añade a archivos de datos en almacenamiento de objetos la fiabilidad de una tabla SQL: transacciones, snapshots y viaje en el tiempo, evolución de esquema y particiones sin reescribir datos. Así varios motores (Spark, Trino, Flink, Presto, Hive, Impala) pueden trabajar a la vez sobre las mismas tablas.

## ¿Cómo lo hace?

Mantiene una especificación de metadatos estable (archivos de metadatos, manifiestos y snapshots) sobre datos Parquet, ORC o Avro, y un catálogo (REST, Hive Metastore, Glue…) que apunta a la versión vigente. Se compila con Gradle y Java 17 o 21, y los motores usan los jars `iceberg-spark` o `iceberg-flink` de runtime. Para Python se usa PyIceberg.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | DuckDB lee tablas Iceberg con su extensión oficial `iceberg`. | Instala DuckDB, carga la extensión y consulta una tabla de prueba. |
| [Polars](polars.md) | Polars lee tablas Iceberg con `pl.scan_iceberg` (vía PyIceberg). | Instala Polars con PyIceberg y apunta al catálogo. |
| [JupyterLab](jupyterlab.md) | Explorar tablas con PyIceberg, DuckDB o Spark desde notebooks. (combinación por arquitectura) | Instala JupyterLab en el mismo entorno que PyIceberg. |
| [Apache Spark](spark.md) | Combinación recíproca: Apache Spark lo enlaza como «Iceberg ofrece un runtime para Spark que permite crear y consultar tablas Iceberg con Spark SQL». | Orden indicado desde Apache Spark: Añade el JAR `iceberg-spark-runtime` y configura un catálogo; después usa Spark SQL. |

**Notas:** Alternativas (elige una): delta-lake, hudi. Para consultas locales pequeñas suele bastar Parquet con DuckDB; Iceberg aporta valor con varios motores o escritores concurrentes.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada apache-iceberg-1.12.0 (2026-09-30) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/iceberg/blob/main/README.md) · [2](https://iceberg.apache.org/docs/latest/) · [3](https://duckdb.org/docs/stable/core_extensions/iceberg/overview) · [4](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_iceberg.html)</sub>

## Ver similares

Grupo **Formatos de tabla para data lakes**: Apache Iceberg ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Delta Lake](delta-lake.md) ⭐ recomendado | 63 | Si buscas esto: capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores. |
| 2 | **Apache Iceberg** (esta ficha) | 62 | Si buscas esto: formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java. |
| 3 | [hudi](hudi.md) | 51 | Si buscas esto: plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. |

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
| Equipo | Preparación según la ruta elegida. JVM (Java 17 o 21 para compilar Iceberg; Scala/sbt para Delta) o las bibliotecas de Python y Rust del ecosistema; un motor como Spark, Trino o DuckDB para consultar. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Decide el motor (Spark, Flink, Trino, DuckDB) o la biblioteca (PyIceberg, iceberg-rust) con que vas a leer y escribir tablas.
2. Configura un catálogo y un almacenamiento de prueba según la documentación oficial.
3. Crea una tabla pequeña, haz un cambio de esquema y consulta un snapshot anterior.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/apache/iceberg/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://py.iceberg.apache.org/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Apache Iceberg para mi objetivo y necesito pasos guiados. Lee https://github.com/apache/iceberg/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una tabla Iceberg pequeña con PyIceberg, añade una columna y consulta el snapshot previo.

**Qué comprobar:** El snapshot anterior conserva el esquema original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Compartir una tabla analítica entre varios motores
- Consultar un snapshot anterior tras un cambio de esquema

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Compartir una tabla analítica entre varios motores; Consultar un snapshot anterior tras un cambio de esquema | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Java, build.gradle
- **Etiquetas:** `data` `lakehouse` `table-format` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Delta Lake](delta-lake.md) | 9.1k | Capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores. |
| [hudi](hudi.md) | 6.4k | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. |

## Enlaces

- 🐙 GitHub: [apache/iceberg](https://github.com/apache/iceberg)
- 🌐 Web: <https://iceberg.apache.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/iceberg/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
