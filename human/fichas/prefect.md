[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 📚 Prefect

> Framework de orquestación en Python: convierte scripts en flujos con decoradores, reintentos, caché, programación y servidor de monitorización.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.2k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Framework de orquestación de workflows de Prefect Technologies (Apache-2.0), con servidor autoalojable y una nube comercial (Prefect Cloud). Proyecto maduro en su serie 3.x; requiere Python 3.11 o superior según el README.

## ¿Qué hace?

Eleva scripts de Python a flujos de producción: programación, caché, reintentos, concurrencia, lógica condicional, automatizaciones por eventos y seguimiento de cada ejecución. Sirve para pipelines de datos, tareas de ML y cualquier proceso que deba ejecutarse de forma fiable.

## ¿Cómo lo hace?

Se instala con `pip install -U prefect` o `uv add prefect`; los flujos son funciones Python decoradas con `@flow` y `@task`. El servidor (`prefect server start`) ofrece interfaz y API; los despliegues se ejecutan mediante workers sobre procesos, Docker o Kubernetes. El README enlaza guías para conectar agentes mediante plugins o MCP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Las tareas de Prefect pueden transformar archivos con DuckDB y pasar resultados entre pasos sin un almacén externo (combinación por arquitectura). | Instala duckdb en el entorno del flujo; después úsalo dentro de las tareas. |
| [Polars](polars.md) | Polars acelera las transformaciones en memoria dentro de tareas de Prefect (combinación por arquitectura). | Añade polars al entorno del worker; luego llámalo en las tareas. |
| [Claude Code](claude-code.md) | Prefect documenta guías para conectar agentes de código mediante plugins o MCP y gestionar flujos desde la CLI. | Prefect instalado y servidor accesible; después sigue la guía de agentes de Prefect para Claude Code. |
| [MLflow](mlflow.md) | Prefect orquesta entrenamientos y evaluaciones mientras MLflow registra métricas y modelos (combinación por arquitectura). | Servidor de MLflow primero; después tareas de Prefect con su cliente. |

**Notas:** Alternativas (elige una): airflow, dagster, kestra.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 3.9.3 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/PrefectHQ/prefect/blob/main/README.md) · [2](https://www.prefect.io/agents)</sub>

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
pip install -U prefect
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/PrefectHQ/prefect/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Prefect para mi objetivo y necesito pasos guiados. Lee https://github.com/PrefectHQ/prefect/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install -U prefect`, ejecuta el ejemplo de estrellas de GitHub del README y abre el servidor local..

**Qué comprobar:** El flujo y sus tareas aparecen como completados en la interfaz con sus logs..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- convertir un script de ingesta en un flujo con reintentos y ejecución programada
- encadenar pasos de datos o ML con dependencias dinámicas y observabilidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: convertir un script de ingesta en un flujo con reintentos y ejecución programada; encadenar pasos de datos o ML con dependencias dinámicas y observabilidad | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, Dockerfile, pyproject.toml
- **Etiquetas:** `automation` `data` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Airflow](airflow.md) | 47.5k | Orquestador de workflows de la Apache Software Foundation: DAGs en Python con planificador, workers, reintentos e interfaz de monitorización. |
| [Dagster](dagster.md) | 16.4k | Orquestador de datos orientado a activos: declaras tablas, modelos o informes como funciones Python y Dagster los mantiene actualizados con linaje. |
| [Kestra](kestra.md) | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. |

## Enlaces

- 🐙 GitHub: [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect)
- 🌐 Web: <https://prefect.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/PrefectHQ/prefect/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
