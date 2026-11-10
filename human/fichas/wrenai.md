[🏠 Inicio](../README.md) › [📊 Analítica & Visualización](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 WrenAI

> BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 18.1k | Otra (ver repo) | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Define tu modelo de datos una vez y los usuarios (o agentes) preguntan en lenguaje natural para obtener SQL, gráficos y respuestas.

## Por qué destaca

La capa semántica reduce errores frente al text-to-SQL directo.

## Cómo funciona

Un motor semántico (MDL) describe tablas y métricas; el LLM genera SQL contra ese modelo con RAG.

## Instalación rápida

Descarga el lanzador de releases o usa Docker Compose del repo.

## Casos de uso

- Preguntar a la base de ventas
- Dashboards generados con IA
- Agentes con acceso a datos de negocio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres text-to-SQL confiable para el negocio | solo analizas un CSV; mira `pandas-ai` |

**Limitaciones:** Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** Python, TypeScript, Rust
- **Modelos / API:** Agnóstico.
- **Etiquetas:** `analytics` `data` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |
| [DuckDB](duckdb.md) | 43k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PandasAI](pandas-ai.md) | 23.9k | Librería para conversar con tus datos (SQL, CSV, Parquet) usando LLM. |

## Enlaces

- 🐙 GitHub: [Canner/WrenAI](https://github.com/Canner/WrenAI)
- 🌐 Web: <https://www.getwren.ai/en/open-core>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
