[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# DuckDB vs Polars

| | [DuckDB](../fichas/duckdb.md) | [Polars](../fichas/polars.md) |
|---|---|---|
| Qué hace | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. | Librería de DataFrames escrita en Rust, mucho más rápida que pandas. |
| ⭐ Estrellas | 43k | 40.3k |
| Elígelo si… | quieres SQL analítico rápido sin montar servidores | tu análisis con pandas es lento |
| Evítalo si… | necesitas una base transaccional multiusuario; usa PostgreSQL | prefieres SQL; mira `duckdb` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🟢 fácil | 🟢 fácil |
| Licencia | MIT | MIT |
| Instalación | `pip install duckdb` | `pip install polars` |

## Regla práctica

- Elige **DuckDB** si quieres SQL analítico rápido sin montar servidores.
- Elige **Polars** si tu análisis con pandas es lento.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
