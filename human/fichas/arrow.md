[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 📚 Apache Arrow

> Formato columnar en memoria y conjunto de bibliotecas multilenguaje para intercambiar y analizar datos sin copias entre procesos y herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.3k | Apache-2.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de la Apache Software Foundation (Apache-2.0) que define un formato columnar estándar en memoria y lo implementa en muchos lenguajes. Es infraestructura compartida por pandas, Polars, DuckDB, Spark y muchos otros. Muy activo.

## ¿Qué hace?

Proporciona el formato columnar de Arrow, el formato IPC para pasar datos entre procesos, el protocolo Flight RPC, ADBC para conectar con bases de datos, lectores y escritores de Parquet y CSV, datasets particionados, el motor de consultas Acero y Gandiva (compilador de expresiones con LLVM).

## ¿Cómo lo hace?

El repositorio contiene las bibliotecas de C++, Python (PyArrow), R, Ruby, C/GLib y MATLAB; Go, Java, JavaScript, Rust, Julia, Swift y .NET viven en repositorios aparte. En Python se instala con pip o conda (`pyarrow`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pandas](pandas.md) | pandas usa PyArrow para Parquet y para tipos `ArrowDtype`; `Table.to_pandas()` y `Table.from_pandas()` convierten en ambos sentidos. | Instala `pyarrow` junto a pandas; después convierte con `to_pandas()` o `from_pandas()`. |
| [Polars](polars.md) | Polars usa el formato de memoria de Arrow y convierte a y desde tablas PyArrow con `to_arrow()`/`from_arrow()`. | Instala Polars y PyArrow; después intercambia tablas con `pl.from_arrow()`. |
| [DuckDB](duckdb.md) | DuckDB consulta tablas y datasets de Arrow sin copiarlos y devuelve resultados como Arrow con `.arrow()`. | Instala `duckdb` y `pyarrow`; después consulta la tabla Arrow por su nombre de variable. |
| [Apache Spark](spark.md) | PySpark usa Arrow para convertir DataFrames de Spark a pandas y para UDF vectorizadas. | Instala `pyarrow` en el entorno de PySpark; después activa la optimización Arrow. |

**Notas:** Arrow es una pieza de infraestructura: rara vez se usa sola, sino como formato común entre herramientas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada apache-arrow-26.0.1 (2026-11-03) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/arrow/blob/main/README.md) · [2](https://arrow.apache.org/docs/python/pandas.html) · [3](https://duckdb.org/docs/stable/guides/python/sql_on_arrow)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/apache/arrow/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Apache Arrow para mi objetivo y necesito pasos guiados. Lee https://github.com/apache/arrow/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala PyArrow, lee un archivo Parquet con `pyarrow.parquet.read_table` y conviértelo a pandas..

**Qué comprobar:** Obtienes una tabla Arrow y su DataFrame equivalente..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- mover datos entre pandas, Polars, DuckDB y Spark sin serializar
- leer y escribir Parquet o datasets particionados desde Python

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: mover datos entre pandas, Polars, DuckDB y Spark sin serializar; leer y escribir Parquet o datasets particionados desde Python | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C++, compose.yaml
- **Etiquetas:** `data` `columnar` `python` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [apache/arrow](https://github.com/apache/arrow)
- 🌐 Web: <https://arrow.apache.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/arrow/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
