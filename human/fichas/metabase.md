[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 metabase

> Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.3k | NOASSERTION | Clojure | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Metabase, herramienta open source de BI y paneles. La edición open source es AGPL y el repo incluye también código de las ediciones comerciales (GitHub muestra NOASSERTION). Es muy madura (~50k estrellas, v0.65.4).

## ¿Qué hace?

Permite que cualquiera haga preguntas a los datos con un editor visual o SQL, cree paneles y alertas y los comparta o incruste. Se conecta a las bases de datos más comunes y tiene modelos y métricas reutilizables. Metabase Cloud añade soporte, copias y auditoría.

## ¿Cómo lo hace?

Se ejecuta como JAR (Java) o con Docker y necesita una base de aplicación (PostgreSQL recomendado en producción). Hay drivers de la comunidad, como el de DuckDB mantenido por MotherDuck.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Driver de DuckDB mantenido por MotherDuck. | Añade el driver a la carpeta de plugins y crea la conexión. |
| [posthog](posthog.md) | BI sobre datos exportados de PostHog. (combinación por arquitectura) | Sincroniza los datos a una base que lea Metabase. |
| [echarts](echarts.md) | Visualizaciones basadas en ECharts. (combinación por arquitectura) | No requiere instalación aparte. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (9). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Appsmith](appsmith.md) · [Baserow](baserow.md) · [data-analyst-roadmap](data-analyst-roadmap.md) · [ERPNext](erpnext.md) · [Matomo](matomo.md) · [NocoDB](nocodb.md) · [Odoo](odoo.md) · [Teable](teable.md) · [Umami](umami.md)

**Notas:** Alternativas (elige una): superset, redash.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.65.4 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/metabase/metabase/blob/master/README.md) · [2](https://github.com/motherduckdb/metabase_duckdb_driver) · [3](https://www.metabase.com/docs/latest/databases/connections/postgresql)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La edición abierta usa AGPL; ediciones comerciales y Cloud tienen precios; el BI básico no exige LLM |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El repositorio contiene varias ediciones; revisa qué funciones de permisos y embedding incluye tu ruta |
| Coste | El coste depende del proveedor o la ruta. La edición abierta usa AGPL; ediciones comerciales y Cloud tienen precios; el BI básico no exige LLM |
| Equipo | Preparación según la ruta elegida. Ruta Docker o Java según guía; base de prueba; usuario de lectura |

El repositorio contiene varias ediciones; revisa qué funciones de permisos y embedding incluye tu ruta

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Ruta Docker o Java según guía
- base de prueba
- usuario de lectura

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://www.metabase.com/docs/latest/installation-and-operation/installing-metabase)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar metabase para mi objetivo y necesito pasos guiados. Lee https://www.metabase.com/docs/latest/installation-and-operation/installing-metabase. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una pregunta de suma por categoría usando los datos de ejemplo.

**Qué comprobar:** El resultado coincide con las filas y puedes guardarlo en un dashboard.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar ventas sin escribir cada consulta SQL
- Compartir un informe operativo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar ventas sin escribir cada consulta SQL; Compartir un informe operativo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El repositorio contiene varias ediciones; revisa qué funciones de permisos y embedding incluye tu ruta

## Stack y modelos

- **Stack:** Ruta Docker o Java según guía; base de prueba; usuario de lectura
- **Etiquetas:** `analytics` `dataviz` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |
| [Redash](redash.md) | 28.9k | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. |

## Enlaces

- 🐙 GitHub: [metabase/metabase](https://github.com/metabase/metabase)
- 🌐 Web: <https://metabase.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/metabase/metabase/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
