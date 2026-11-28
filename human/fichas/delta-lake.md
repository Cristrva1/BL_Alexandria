[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 📚 Delta Lake

> Capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.1k | Apache-2.0 | Scala | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de almacenamiento abierto Delta Lake (organización delta-io), en Scala con licencia Apache-2.0. Este repositorio contiene el conector de Spark, Delta Kernel, conectores y el protocolo; delta-rs es la implementación nativa en Rust/Python. Versión v4.4.1 (octubre de 2026), activo.

## ¿Qué hace?

Da transacciones ACID, serializabilidad, versiones y viaje en el tiempo a tablas guardadas como Parquet, para construir un «lakehouse» que leen y escriben Spark, Flink, Trino, PrestoDB y Hive. UniForm permite además leer tablas Delta como Iceberg.

## ¿Cómo lo hace?

Registra cada cambio en un log de transacciones (`_delta_log`) definido en PROTOCOL.md. Requiere un almacenamiento con visibilidad atómica, exclusión mutua y listados consistentes. Se usa desde Spark con `delta-spark` (Scala, Java o Python) siguiendo la guía rápida, desde Delta Standalone o Kernel en la JVM, o sin JVM con delta-rs.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | DuckDB lee tablas Delta con su extensión oficial `delta`. | Instala DuckDB y carga la extensión `delta`. |
| [Polars](polars.md) | Polars lee y escribe tablas Delta (`pl.scan_delta`, `write_delta`) mediante deltalake (delta-rs). | Instala Polars con el paquete `deltalake`. |
| [JupyterLab](jupyterlab.md) | Explorar tablas Delta con PySpark, delta-rs o DuckDB desde notebooks. (combinación por arquitectura) | Instala JupyterLab en el entorno con PySpark o deltalake. |
| [Apache Spark](spark.md) | Combinación recíproca: Apache Spark lo enlaza como «Delta Lake nació para Spark: añade transacciones ACID, versiones y MERGE a tablas en almacenamiento de objetos usando Spark como motor». | Orden indicado desde Apache Spark: Añade el paquete `delta-spark` a la sesión de Spark; después lee y escribe con `format("delta")`. |

**Notas:** Alternativas (elige una): apache-iceberg, hudi. Delta UniForm acerca ambos formatos: Delta puede publicar metadatos Iceberg.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v4.4.1 (2026-10-05) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/delta-io/delta/blob/master/README.md) · [2](https://docs.delta.io/latest/quick-start.html) · [3](https://docs.delta.io/latest/delta-uniform.html) · [4](https://duckdb.org/docs/stable/core_extensions/delta) · [5](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_delta.html)</sub>

## Ver similares

Grupo **Formatos de tabla para data lakes**: Delta Lake ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Delta Lake** (esta ficha) ⭐ recomendado | 61 | Si buscas esto: capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores. |
| 2 | [Apache Iceberg](apache-iceberg.md) | 61 | Si buscas esto: formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java. |
| 3 | [hudi](hudi.md) | 50 | Si buscas esto: plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. |

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

1. Sigue la guía rápida oficial con Spark (Scala, Java o Python) o usa delta-rs si no quieres JVM.
2. Escribe una tabla de prueba en un directorio local y lee su historial.
3. Prueba una actualización y una consulta de una versión anterior antes de usar almacenamiento en la nube.

**Entrada documentada (bash):**

```
pip install delta-spark==4.0.0
```

Comando copiado literalmente de la documentación del repositorio (sección «Python»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/delta-io/delta/blob/master/docs/src/content/docs/quick-start.mdx)

[Abrir la web o descarga indicada por el autor](https://docs.delta.io/latest/quick-start.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Delta Lake para mi objetivo y necesito pasos guiados. Lee https://github.com/delta-io/delta/blob/master/docs/src/content/docs/quick-start.mdx. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Escribe una tabla Delta local, actualiza unas filas y lee la versión 0.

**Qué comprobar:** La versión 0 muestra los datos originales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir transacciones y versiones a archivos Parquet
- Recuperar una versión anterior de una tabla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir transacciones y versiones a archivos Parquet; Recuperar una versión anterior de una tabla | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Scala, Dockerfile, build.sbt
- **Etiquetas:** `data` `lakehouse` `table-format` `scala`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Iceberg](apache-iceberg.md) | 9.4k | Formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java. |
| [hudi](hudi.md) | 6.4k | Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. |

## Enlaces

- 🐙 GitHub: [delta-io/delta](https://github.com/delta-io/delta)
- 🌐 Web: <https://delta.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/delta-io/delta/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
