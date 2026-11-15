[🏠 Inicio](../README.md) › [📊 Analítica & Visualización](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 metabase

> Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 50.3k | Otra (ver repo) | Clojure | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Apunta a perfiles no técnicos que necesitan reporting propio.

## Por qué destaca

De las plataformas BI open source más populares por su facilidad de uso y su editor visual de consultas accesible para perfiles no técnicos. Su despliegue como JAR o contenedor lo hace muy portable.

## Cómo funciona

Se conecta a tu BD (Postgres, MySQL, BigQuery, etc.), define preguntas mediante un constructor visual o SQL nativo, y las agrupa en dashboards interactivos servidos por web.

## Instalación rápida

`docker run metabase/metabase`, o JAR ejecutable con Java. Requiere una BD de aplicación (H2 por defecto, recomendado Postgres/MySQL para producción).

## Casos de uso

- Tableros de marketing/ventas sin escribir SQL
- Reporting de negocio sobre tu BD existente
- Exploración ad-hoc por perfiles no técnicos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres BI accesible para perfiles no técnicos | necesitas analítica de eventos por usuario (posthog) |

## Stack y modelos

- **Stack:** Java/Clojure, BD, web
- **Modelos / API:** N/A.
- **Etiquetas:** `analytics` `dataviz` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [posthog](posthog.md) | 40.7k | Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. |
| [echarts](echarts.md) | 67.7k | Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |
| [Redash](redash.md) | 28.9k | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. |

## Enlaces

- 🐙 GitHub: [metabase/metabase](https://github.com/metabase/metabase)
- 🌐 Web: <https://metabase.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
