[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🧩 Apache Spark

> Motor unificado de Apache para procesar datos a gran escala en clúster: SQL y DataFrames, streaming, machine learning (MLlib) y API de pandas sobre Spark.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 44.5k | Apache-2.0 | Scala | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** hard

**Nivel:** 3 Avanzado — motor distribuido; en local basta pip, en clúster es avanzado · corregido a mano

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de procesamiento de datos distribuido de la Apache Software Foundation (Apache-2.0), estándar en big data desde hace más de una década y base de plataformas como Databricks. Muy activo.

## ¿Qué hace?

Procesa grandes volúmenes en paralelo con Spark SQL y DataFrames, la API de pandas sobre Spark, MLlib para aprendizaje automático, GraphX para grafos y Structured Streaming para flujos. Lee y escribe Parquet, ORC, JSON, JDBC y formatos de tabla como Delta Lake, Iceberg y Hudi.

## ¿Cómo lo hace?

Está escrito en Scala sobre la JVM; el optimizador Catalyst y el motor Tungsten generan planes eficientes. Se ejecuta en modo local o en clúster (standalone, YARN, Kubernetes). PySpark se instala con pip (requiere Java) y usa Apache Arrow para intercambiar datos con pandas. La API de R está marcada como obsoleta.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Delta Lake](delta-lake.md) | Delta Lake nació para Spark: añade transacciones ACID, versiones y MERGE a tablas en almacenamiento de objetos usando Spark como motor. | Añade el paquete `delta-spark` a la sesión de Spark; después lee y escribe con `format("delta")`. |
| [Apache Iceberg](apache-iceberg.md) | Iceberg ofrece un runtime para Spark que permite crear y consultar tablas Iceberg con Spark SQL. | Añade el JAR `iceberg-spark-runtime` y configura un catálogo; después usa Spark SQL. |
| [hudi](hudi.md) | Hudi se integra con Spark como motor principal de escritura e ingestión incremental. | Añade el bundle de Hudi para Spark; después escribe con `format("hudi")`. |
| [pandas](pandas.md) | Spark incluye la API de pandas sobre Spark (`pyspark.pandas`) y convierte DataFrames con `toPandas()`. | Instala PySpark con pandas; después usa `pyspark.pandas` o `toPandas()` en resultados pequeños. |
| [Apache Arrow](arrow.md) | PySpark usa Apache Arrow para acelerar la conversión entre Spark y pandas y las UDF vectorizadas. | Instala `pyarrow`; después activa `spark.sql.execution.arrow.pyspark.enabled`. |
| [dbt](dbt.md) | Combinación recíproca: dbt lo enlaza como «El adaptador dbt-spark ejecuta los modelos dbt como SQL de Spark». | Orden indicado desde dbt: Instala `dbt-spark` con el método de conexión adecuado; después apunta el perfil al clúster. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Ibis](ibis.md)

**Notas:** Para datos que caben en una máquina, DuckDB o Polars suelen ser más simples y rápidos; Spark compensa en clúster.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/spark/blob/master/README.md) · [2](https://spark.apache.org/docs/latest/api/python/user_guide/sql/arrow_pandas.html) · [3](https://docs.delta.io/latest/quick-start.html) · [4](https://iceberg.apache.org/docs/latest/spark-getting-started/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/apache/spark/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Apache Spark para mi objetivo y necesito pasos guiados. Lee https://github.com/apache/spark/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala PySpark (`pip install pyspark`) y procesa un CSV local con un DataFrame y una consulta SQL en modo local..

**Qué comprobar:** Obtienes el resultado agregado en la consola sin necesidad de clúster..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- procesar terabytes de logs o eventos en un clúster con SQL o PySpark
- alimentar un lakehouse con Delta Lake o Iceberg mediante trabajos batch y streaming

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: procesar terabytes de logs o eventos en un clúster con SQL o PySpark; alimentar un lakehouse con Delta Lake o Iceberg mediante trabajos batch y streaming | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Scala, pom.xml, pyproject.toml
- **Etiquetas:** `data` `bigdata` `sql` `streaming`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [apache/spark](https://github.com/apache/spark)
- 🌐 Web: <https://spark.apache.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/spark/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
