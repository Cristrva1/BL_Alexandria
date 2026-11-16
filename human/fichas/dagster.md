[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 📚 Dagster

> Orquestador de datos orientado a activos: declaras tablas, modelos o informes como funciones Python y Dagster los mantiene actualizados con linaje.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.4k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Orquestador de pipelines de datos de Dagster Labs (Apache-2.0), con oferta comercial gestionada (Dagster+). Proyecto maduro; el README indica soporte oficial de Python 3.9 a 3.14.

## ¿Qué hace?

Gestiona activos de datos (tablas, conjuntos de datos, modelos de ML, informes) a lo largo de todo el ciclo: desarrollo local, tests, staging y producción. Programa materializaciones, rastrea linaje y metadatos, detecta activos desactualizados e integra herramientas como dbt, DuckDB, Snowflake o Spark mediante bibliotecas propias.

## ¿Cómo lo hace?

Los activos se declaran como funciones Python decoradas y sus dependencias se deducen de los parámetros. Se instala con `uv add dagster dagster-webserver dagster-dg-cli` y se arranca la interfaz en local; en producción usa una base PostgreSQL, un daemon de programación y ejecutores sobre procesos, Docker o Kubernetes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Dagster mantiene una integración oficial con DuckDB (dagster-duckdb) para guardar y leer activos como tablas DuckDB. | Instala dagster-duckdb; después configura el recurso o el IO manager de DuckDB en las definiciones. |
| [Polars](polars.md) | Existe la integración dagster-polars para manejar DataFrames de Polars como activos con IO managers en Parquet o Delta. | Instala dagster-polars; después declara los activos que devuelven DataFrames de Polars. |
| [MLflow](mlflow.md) | Dagster puede materializar modelos como activos mientras MLflow registra parámetros y métricas de entrenamiento (combinación por arquitectura). | Servidor de MLflow primero; después activos de Dagster que usen su cliente. |
| [Claude Code](claude-code.md) | Las definiciones son Python y la CLI dg permite crear y validar proyectos, lo que facilita que un agente de código los genere y pruebe (combinación por arquitectura). | Proyecto Dagster local; después pide al agente activos nuevos y valídalos con la CLI. |
| [dbt](dbt.md) | Combinación recíproca: dbt lo enlaza como «La biblioteca dagster-dbt carga los modelos de un proyecto dbt como assets de Dagster para orquestarlos y monitorizarlos». | Orden indicado desde dbt: Instala `dagster-dbt`; después carga el proyecto dbt con `@dbt_assets`. |
| [dlt (data load tool)](dlt.md) | Combinación recíproca: dlt (data load tool) lo enlaza como «La biblioteca dagster-dlt carga los recursos de dlt como assets de Dagster». | Orden indicado desde dlt (data load tool): Instala `dagster-dlt`; después declara los assets con `@dlt_assets`. |

**Notas:** Alternativas (elige una): airflow, prefect, kestra.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada 1.13.30 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dagster-io/dagster/blob/master/README.md) · [2](https://docs.dagster.io/integrations/libraries/duckdb) · [3](https://docs.dagster.io/integrations/libraries/polars)</sub>

## Ver similares

Grupo **Orquestadores de workflows de datos y tareas**: Dagster ocupa la posición 6 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Apache Airflow](airflow.md) ⭐ recomendado | 81 | Si necesitas el estándar de la industria para pipelines por lotes con un ecosistema enorme de operadores. |
| 2 | [Kestra](kestra.md) | 80 | Si prefieres definir flujos en YAML con interfaz web y disparadores por eventos. |
| 3 | [Prefect](prefect.md) | 68 | Si quieres convertir funciones Python en flujos observables con muy poco código. |
| 4 | [Trigger.dev](trigger-dev.md) | 68 | Si trabajas en TypeScript y quieres tareas de fondo largas sin gestionar colas. |
| 5 | [Windmill](windmill.md) | 61 | Si quieres scripts en varios lenguajes convertidos en flujos y apps internas rápidas. |
| 6 | **Dagster** (esta ficha) | 57 | Si piensas en activos de datos (tablas, modelos) con linaje y pruebas. |

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
uv add dagster dagster-webserver dagster-dg-cli
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/dagster-io/dagster/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Dagster para mi objetivo y necesito pasos guiados. Lee https://github.com/dagster-io/dagster/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `uv add dagster dagster-webserver dagster-dg-cli`, define dos activos dependientes y materialízalos desde la interfaz..

**Qué comprobar:** La interfaz muestra el grafo de activos y ambos aparecen materializados con sus metadatos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- mantener al día un conjunto de tablas analíticas con dependencias y linaje visibles
- probar pipelines de datos con tests unitarios antes de llevarlos a producción

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: mantener al día un conjunto de tablas analíticas con dependencias y linaje visibles; probar pipelines de datos con tests unitarios antes de llevarlos a producción | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `automation` `data` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Airflow](airflow.md) | 47.5k | Orquestador de workflows de la Apache Software Foundation: DAGs en Python con planificador, workers, reintentos e interfaz de monitorización. |
| [Prefect](prefect.md) | 24.2k | Framework de orquestación en Python: convierte scripts en flujos con decoradores, reintentos, caché, programación y servidor de monitorización. |
| [Kestra](kestra.md) | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. |

## Enlaces

- 🐙 GitHub: [dagster-io/dagster](https://github.com/dagster-io/dagster)
- 🌐 Web: <https://dagster.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dagster-io/dagster/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
