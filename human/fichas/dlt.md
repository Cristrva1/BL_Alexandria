[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 📚 dlt (data load tool)

> Biblioteca Python para cargar datos de APIs, bases de datos y archivos en destinos como DuckDB, Postgres o almacenes en la nube, con esquema y carga incremental.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.1k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) de dltHub. Se presenta como "una biblioteca, no una plataforma". Desde marzo de 2026 la empresa ofrece dltHub, una plataforma gestionada con licencia comercial. Activa.

## ¿Qué hace?

Carga datos desde fuentes desordenadas (APIs REST, bases SQL, archivos locales o en la nube, DataFrames y tablas Arrow) a conjuntos tipados y estructurados en más de 20 destinos: DuckDB, Postgres, BigQuery, Snowflake, Redshift, Databricks, sistemas de archivos y otros. Gestiona paginación, inferencia y evolución del esquema, normalización de JSON anidado y cargas incrementales.

## ¿Cómo lo hace?

Se instala con pip o uv con extras por destino. Un pipeline se define en Python con fuentes y recursos (generadores) y se ejecuta con `pipeline.run()`; después se accede a los datos como pandas, Arrow o expresiones de Ibis. Funciona en un notebook, una función serverless, un DAG de Airflow o un agente de código.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | DuckDB es el destino local más usado de dlt (`destination="duckdb"`). | Instala `dlt[duckdb]`; después ejecuta el pipeline con destino DuckDB. |
| [Apache Airflow](airflow.md) | dlt se ejecuta dentro de DAGs de Airflow; su documentación incluye una guía de despliegue en Airflow. | Instala dlt en el entorno de Airflow; después llama al pipeline desde una tarea del DAG. |
| [Ibis](ibis.md) | Las tablas cargadas pueden convertirse en expresiones de Ibis (`to_ibis()`) que dlt compila al SQL del destino. | Carga los datos con dlt; después usa `pipeline.dataset().tabla.to_ibis()`. |
| [marimo](marimo.md) | dlt documenta cómo visualizar los datos cargados en notebooks marimo. | Instala marimo; después abre el dataset del pipeline en un notebook. |
| [Dagster](dagster.md) | La biblioteca dagster-dlt carga los recursos de dlt como assets de Dagster. | Instala `dagster-dlt`; después declara los assets con `@dlt_assets`. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.32.0 (2026-10-29) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dlt-hub/dlt/blob/devel/README.md) · [2](https://dlthub.com/docs/walkthroughs/deploy-a-pipeline/deploy-with-airflow-composer) · [3](https://docs.dagster.io/integrations/libraries/dlt)</sub>

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
pip install "dlt[duckdb]"
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/dlt-hub/dlt/blob/devel/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dlt (data load tool) para mi objetivo y necesito pasos guiados. Lee https://github.com/dlt-hub/dlt/blob/devel/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install "dlt[duckdb]"`, define una fuente REST pequeña y ejecuta el pipeline con destino DuckDB..

**Qué comprobar:** Obtienes un archivo DuckDB con tablas tipadas creadas por dlt..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- volcar los datos de una API REST paginada en DuckDB para analizarlos
- sincronizar tablas de una base SQL a un almacén analítico cada día

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: volcar los datos de una API REST paginada en DuckDB para analizarlos; sincronizar tablas de una base SQL a un almacén analítico cada día | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. dlt es Apache-2.0; dltHub (plataforma gestionada y el extra `dlt[hub]`) es un producto comercial con licencia propia.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `data` `etl` `python` `pipeline`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [dlt-hub/dlt](https://github.com/dlt-hub/dlt)
- 🌐 Web: <https://dlthub.com/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dlt-hub/dlt/blob/devel/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
