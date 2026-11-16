[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# ⚙️ Apache Airflow

> Orquestador de workflows de la Apache Software Foundation: DAGs en Python con planificador, workers, reintentos e interfaz de monitorización.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47.5k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 81/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de orquestación de workflows de la Apache Software Foundation (Apache-2.0), creada en Airbnb en 2014 y proyecto de nivel superior de Apache. Muy madura y usada en producción por miles de organizaciones; la serie 3.x es la actual.

## ¿Qué hace?

Permite definir, programar y monitorizar flujos de trabajo como código: cada DAG declara tareas y dependencias, y Airflow las ejecuta por calendario, eventos o activos de datos, con reintentos, backfills, alertas y una interfaz web con logs y estado. Sus paquetes de proveedores conectan con nubes, bases de datos y servicios externos.

## ¿Cómo lo hace?

Escrito en Python; se instala con pip usando los archivos de constraints oficiales, o con la imagen Docker y el chart de Helm. Necesita una base de metadatos (PostgreSQL o MySQL en producción), un scheduler, el servidor de API e interfaz y un ejecutor (local, Celery o Kubernetes). Cada versión declara las versiones de Python y Kubernetes soportadas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Una tarea de Airflow puede ejecutar transformaciones con DuckDB sobre Parquet o CSV sin levantar un almacén de datos (combinación por arquitectura). | Instala duckdb en el entorno de los workers; después llama a DuckDB desde una tarea Python. |
| [Polars](polars.md) | Las tareas Python del DAG pueden usar Polars para transformar lotes grandes en memoria antes de cargarlos (combinación por arquitectura). | Añade polars a la imagen o al entorno de los workers; luego úsalo dentro de las tareas. |
| [Grafana](grafana.md) | Airflow publica métricas por StatsD u OpenTelemetry que se pueden visualizar en Grafana a través de Prometheus u otro backend (combinación por arquitectura). | Configura las métricas de Airflow y el exportador o colector; después añade la fuente de datos y el panel en Grafana. |
| [MLflow](mlflow.md) | Airflow programa los pasos de entrenamiento y evaluación y MLflow registra parámetros, métricas y modelos de cada ejecución (combinación por arquitectura). | Servidor de MLflow primero; después tareas de Airflow que usen su cliente con MLFLOW_TRACKING_URI. |
| [Claude Code](claude-code.md) | Los DAGs son Python normal: un agente de código puede escribirlos y probarlos con `airflow dags test` en un entorno de desarrollo (combinación por arquitectura). | Entorno de Airflow de pruebas; después pide al agente el DAG y pruébalo antes de desplegarlo. |
| [dbt](dbt.md) | Combinación recíproca: dbt lo enlaza como «Airflow se usa habitualmente para programar ejecuciones de dbt (por ejemplo con Astronomer Cosmos u operadores Bash)». | Orden indicado desde dbt: Instala dbt en el entorno de Airflow; después crea un DAG que ejecute `dbt build`. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[dlt (data load tool)](dlt.md)

**Notas:** Alternativas (elige una): prefect, dagster, kestra. Instalar sin el archivo de constraints suele romper dependencias.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 3.4.0 (2026-11-06) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/airflow/blob/main/README.md) · [2](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html) · [3](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html)</sub>

## Ver similares

Grupo **Orquestadores de workflows de datos y tareas**: Apache Airflow ocupa la posición 1 de 6 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Apache Airflow** (esta ficha) ⭐ recomendado | 81 | Si necesitas el estándar de la industria para pipelines por lotes con un ecosistema enorme de operadores. |
| 2 | [Kestra](kestra.md) | 80 | Si prefieres definir flujos en YAML con interfaz web y disparadores por eventos. |
| 3 | [Prefect](prefect.md) | 68 | Si quieres convertir funciones Python en flujos observables con muy poco código. |
| 4 | [Trigger.dev](trigger-dev.md) | 68 | Si trabajas en TypeScript y quieres tareas de fondo largas sin gestionar colas. |
| 5 | [Windmill](windmill.md) | 61 | Si quieres scripts en varios lenguajes convertidos en flujos y apps internas rápidas. |
| 6 | [Dagster](dagster.md) | 57 | Si piensas en activos de datos (tablas, modelos) con linaje y pruebas. |

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
pip install 'apache-airflow==3.4.0' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.4.0/constraints-3.10.txt"
```

Comando copiado literalmente de el README (sección «Installing from PyPI»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/apache/airflow/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Apache Airflow para mi objetivo y necesito pasos guiados. Lee https://github.com/apache/airflow/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Levanta un entorno local de pruebas siguiendo la guía oficial y ejecuta un DAG de ejemplo con dos tareas dependientes..

**Qué comprobar:** El DAG aparece en la interfaz, ambas tareas terminan en verde y puedes leer sus logs..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- programar un ETL diario que descarga, transforma y carga datos en un almacén
- coordinar entrenamientos y despliegues de modelos con dependencias y reintentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: programar un ETL diario que descarga, transforma y carga datos en un almacén; coordinar entrenamientos y despliegues de modelos con dependencias y reintentos | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, Dockerfile, pyproject.toml
- **Etiquetas:** `automation` `data` `python` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Prefect](prefect.md) | 24.2k | Framework de orquestación en Python: convierte scripts en flujos con decoradores, reintentos, caché, programación y servidor de monitorización. |
| [Dagster](dagster.md) | 16.4k | Orquestador de datos orientado a activos: declaras tablas, modelos o informes como funciones Python y Dagster los mantiene actualizados con linaje. |
| [Kestra](kestra.md) | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. |

## Enlaces

- 🐙 GitHub: [apache/airflow](https://github.com/apache/airflow)
- 🌐 Web: <https://airflow.apache.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/airflow/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
