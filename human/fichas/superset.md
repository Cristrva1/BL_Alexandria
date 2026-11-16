[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 Apache Superset

> Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 75.5k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Apache Superset, aplicación web de BI de la Apache Software Foundation. Licencia Apache-2.0. Es muy madura (~76k estrellas, 6.1.0).

## ¿Qué hace?

Permite explorar datos sin código o con un IDE SQL, crear gráficos y paneles interactivos y compartirlos. Se conecta a casi cualquier base SQL mediante SQLAlchemy y tiene capa semántica ligera, caché y control de acceso. Ofrece API REST y un framework de extensiones.

## ¿Cómo lo hace?

Se prueba con Docker Compose y se despliega en producción con Kubernetes (Helm) o pip. Está escrito en Python (Flask) con frontend React y requiere una base de metadatos y un driver por cada fuente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | DuckDB y MotherDuck son bases soportadas en la documentación. | Instala el driver de DuckDB y añade la conexión. |
| [WrenAI](wrenai.md) | Capa semántica y text-to-SQL para agentes junto a paneles de Superset. (combinación por arquitectura) | Modela en WrenAI y visualiza en Superset. |
| [echarts](echarts.md) | Superset usa ECharts en muchas visualizaciones. (combinación por arquitectura) | No requiere instalación aparte. |
| [hudi](hudi.md) | Combinación recíproca: hudi lo enlaza como «BI sobre tablas Hudi vía un motor SQL. (combinación por arquitectura)». | Orden indicado desde hudi: Conecta Superset al motor de consulta. |
| [Kestra](kestra.md) | Combinación recíproca: Kestra lo enlaza como «Kestra carga y transforma los datos en el almacén y Superset los visualiza en dashboards (combinación por arquitectura)». | Orden indicado desde Kestra: Primero el almacén de datos, luego Kestra para poblarlo y al final Superset conectado a ese almacén. |
| [deck.gl](deck-gl.md) | Combinación recíproca: deck.gl lo enlaza como «Apache Superset incluye tipos de gráfico basados en deck.gl para datos geoespaciales». | Orden indicado desde deck.gl: Superset con una fuente de datos con coordenadas; después crea un gráfico deck.gl. |

**Notas:** Alternativas (elige una): metabase, redash.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 6.1.0 (2026-05-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/superset/blob/master/README.md) · [2](https://superset.apache.org/user-docs/databases/supported/duckdb)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El BI básico no necesita modelo; servidor, base y consultas pueden generar gasto |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Instala el driver de la base elegida y usa credenciales de lectura para la primera prueba |
| Coste | Sin pago a un modelo en la ruta básica. El BI básico no necesita modelo; servidor, base y consultas pueden generar gasto |
| Equipo | Preparación según la ruta elegida. Entorno del quickstart; motor SQL; driver de conexión; datos ficticios |

Instala el driver de la base elegida y usa credenciales de lectura para la primera prueba

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno del quickstart
- motor SQL
- driver de conexión
- datos ficticios

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://superset.apache.org/docs/quickstart/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Apache Superset para mi objetivo y necesito pasos guiados. Lee https://superset.apache.org/docs/quickstart/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta una tabla de ventas ficticias y crea un gráfico por mes.

**Qué comprobar:** El gráfico coincide con una suma SQL verificable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar métricas de una base SQL
- Compartir un dashboard interno

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar métricas de una base SQL; Compartir un dashboard interno | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instala el driver de la base elegida y usa credenciales de lectura para la primera prueba

## Stack y modelos

- **Stack:** Entorno del quickstart; motor SQL; driver de conexión; datos ficticios
- **Etiquetas:** `analytics` `dataviz` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [metabase](metabase.md) | 50.3k | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |
| [Redash](redash.md) | 28.9k | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. |

## Enlaces

- 🐙 GitHub: [apache/superset](https://github.com/apache/superset)
- 🌐 Web: <https://superset.apache.org/>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/superset/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
