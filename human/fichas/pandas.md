[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 📚 pandas

> Biblioteca estándar de Python para analizar y transformar datos tabulares con DataFrame y Series: limpieza, agrupaciones, uniones, series temporales y E/S.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.5k | BSD-3-Clause | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Biblioteca de código abierto (BSD-3-Clause) del proyecto pandas, patrocinado fiscalmente por NumFOCUS. Es la referencia de facto para el análisis de datos tabulares en Python y la base sobre la que se apoyan muchas otras herramientas. Muy activa.

## ¿Qué hace?

Ofrece las estructuras DataFrame y Series para cargar, limpiar, transformar y resumir datos: manejo de valores faltantes, alineación por etiquetas, agrupaciones (split-apply-combine), uniones, pivotes, índices jerárquicos, series temporales (rangos de fechas, ventanas móviles) y lectura/escritura de CSV, Excel, bases de datos SQL, Parquet y HDF5.

## ¿Cómo lo hace?

Se instala con `pip install pandas` o desde conda-forge. Está escrita en Python, Cython y C sobre NumPy; desde la versión 2 puede usar tipos respaldados por PyArrow. Trabaja en memoria en un solo proceso, por lo que para datos mayores que la RAM conviene delegar en DuckDB, Polars o Spark.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [JupyterLab](jupyterlab.md) | Entorno habitual para explorar DataFrames de pandas de forma interactiva, con su representación en tabla. | Instala JupyterLab y pandas en el mismo entorno; después importa pandas en un notebook. |
| [DuckDB](duckdb.md) | DuckDB consulta DataFrames de pandas con SQL directamente (por nombre de variable) y devuelve resultados como DataFrame con `.df()`. | Instala `duckdb` junto a pandas; después ejecuta `duckdb.sql("SELECT ... FROM df").df()`. |
| [scikit-learn](scikit-learn.md) | scikit-learn acepta DataFrames de pandas como entrada y puede devolver salidas en pandas con `set_output(transform="pandas")`. | Prepara los datos con pandas; después pásalos a los estimadores de scikit-learn. |
| [Apache Arrow](arrow.md) | pandas usa PyArrow para leer y escribir Parquet y para los tipos `ArrowDtype` respaldados por Arrow. | Instala `pyarrow`; después usa `pd.read_parquet` o `dtype_backend="pyarrow"`. |
| [PyGWalker](pygwalker.md) | PyGWalker convierte un DataFrame de pandas en una interfaz visual de exploración tipo Tableau dentro del notebook. | Instala `pygwalker`; después llama a `pyg.walk(df)` con tu DataFrame. |
| [Reflex](reflex.md) | Combinación recíproca: Reflex lo enlaza como «El componente `rx.data_table` acepta un DataFrame de pandas para mostrar datos en una tabla». | Orden indicado desde Reflex: Instala pandas en el proyecto; después pasa el DataFrame a `rx.data_table(data=df)`. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (3). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Apache Spark](spark.md) · [Ibis](ibis.md) · [NiceGUI](nicegui.md)

**Notas:** Para volúmenes grandes, Polars (alternativa) o DuckDB suelen ser más rápidos y usan menos memoria; pandas sigue siendo la API más compatible con el ecosistema.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.1.1 (2026-11-04) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pandas-dev/pandas/blob/main/README.md) · [2](https://pandas.pydata.org/docs/user_guide/pyarrow.html) · [3](https://duckdb.org/docs/stable/guides/python/sql_on_pandas)</sub>

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
pip install pandas
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/pandas-dev/pandas/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pandas para mi objetivo y necesito pasos guiados. Lee https://github.com/pandas-dev/pandas/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install pandas`, carga un CSV con `pd.read_csv` y agrupa por una columna con `groupby().sum()`..

**Qué comprobar:** Obtienes un DataFrame resumido que puedes exportar a CSV o Parquet..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- limpiar y cruzar varios CSV o Excel antes de un informe
- preparar un conjunto de datos para entrenar un modelo de scikit-learn

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: limpiar y cruzar varios CSV o Excel antes de un informe; preparar un conjunto de datos para entrenar un modelo de scikit-learn | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `data` `python` `dataframe` `analytics`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Polars](polars.md) | 40.3k | Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares. |

## Enlaces

- 🐙 GitHub: [pandas-dev/pandas](https://github.com/pandas-dev/pandas)
- 🌐 Web: <https://pandas.pydata.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pandas-dev/pandas/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
