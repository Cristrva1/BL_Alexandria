[🏠 Inicio](../README.md) › [📊 Analítica & Visualización](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 Apache Superset

> Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 75.5k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Conecta tus bases SQL, crea gráficos y dashboards sin código o con SQL Lab, con control de acceso.

## Por qué destaca

Proyecto Apache maduro, con muchos gráficos y escala empresarial.

## Cómo funciona

Un servidor Flask consulta tus bases vía SQLAlchemy y una app React renderiza dashboards con caché.

## Instalación rápida

`git clone https://github.com/apache/superset && cd superset && docker compose -f docker-compose-image-tag.yml up`.

## Casos de uso

- Dashboards de ventas
- Exploración con SQL
- BI interno sin licencias

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres BI empresarial abierto | buscas algo muy fácil para no técnicos; mira `metabase` |

## Stack y modelos

- **Stack:** Python, React, Docker
- **Modelos / API:** No usa LLM de serie.
- **Etiquetas:** `analytics` `dataviz` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DuckDB](duckdb.md) | 43k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |
| [WrenAI](wrenai.md) | 18.1k | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [metabase](metabase.md) | 50.3k | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |
| [Redash](redash.md) | 28.9k | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. |

## Enlaces

- 🐙 GitHub: [apache/superset](https://github.com/apache/superset)
- 🌐 Web: <https://superset.apache.org/>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
