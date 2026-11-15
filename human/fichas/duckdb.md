[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Datos y notebooks

# 🗃️ DuckDB

> Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 43k | MIT | C++ | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

El "SQLite de la analítica": sin servidor, embebida en Python, R o Node, y capaz de procesar millones de filas en segundos.

## Por qué destaca

Rendimiento excelente sin infraestructura y SQL directo sobre archivos.

## Cómo funciona

Motor columnar vectorizado que lee formatos de archivo directamente y ejecuta SQL en paralelo.

## Instalación rápida

`pip install duckdb` o `brew install duckdb`.

## Casos de uso

- Analizar CSV grandes con SQL
- Pipelines de datos locales
- Backend analítico de dashboards

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres SQL analítico rápido sin montar servidores | necesitas una base transaccional multiusuario; usa PostgreSQL |

## Stack y modelos

- **Stack:** C++
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `data` `analytics` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [marimo](marimo.md) | 23.5k | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. |
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Polars](polars.md) | 40.3k | Librería de DataFrames escrita en Rust, mucho más rápida que pandas. |

## Enlaces

- 🐙 GitHub: [duckdb/duckdb](https://github.com/duckdb/duckdb)
- 🌐 Web: <http://www.duckdb.org>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
