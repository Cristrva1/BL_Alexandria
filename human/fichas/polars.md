[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🗃️ Polars

> Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.3k | MIT | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Polars, motor de consultas y DataFrames escrito en Rust con API de Python (y Rust, Node, R), de pola-rs. Licencia MIT. Es muy madura (~40k estrellas, py-2.1.0).

## ¿Qué hace?

Procesa datos tabulares con ejecución lazy y optimizador de consultas, multihilo, vectorizado y en streaming para datos mayores que la memoria. Opcionalmente acelera consultas en GPU NVIDIA y lee los formatos más comunes.

## ¿Cómo lo hace?

Se instala con `pip install polars` (hay feature flags para extras) o se compila con Rust y maturin.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [marimo](marimo.md) | Visualización interactiva de DataFrames en notebooks. | Instala marimo y muestra el DataFrame. |
| [TimesFM](timesfm.md) | Preparar series para pronóstico. (combinación por arquitectura) | Limpia los datos con Polars. |
| [streamlit](streamlit.md) | Apps de datos sobre DataFrames de Polars. (combinación por arquitectura) | Muestra el DataFrame en Streamlit. |
| [Apache Iceberg](apache-iceberg.md) | Polars lee tablas Iceberg con `pl.scan_iceberg` (vía PyIceberg). | Instala PyIceberg junto a Polars. |
| [Delta Lake](delta-lake.md) | Polars lee y escribe tablas Delta (`pl.scan_delta`, `write_delta`) mediante deltalake. | Instala el paquete `deltalake` junto a Polars. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (11). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Apache Airflow](airflow.md) · [Apache Arrow](arrow.md) · [Colly](colly.md) · [Dagster](dagster.md) · [Ibis](ibis.md) · [JupyterLab](jupyterlab.md) · [LanceDB](lancedb.md) · [nautilus_trader](nautilus-trader.md) · [Prefect](prefect.md) · [PyGWalker](pygwalker.md) · [Windmill](windmill.md)

**Notas:** Alternativas (elige una): duckdb.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada py-2.1.0 (2026-10-25) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pola-rs/polars/blob/main/README.md) · [2](https://docs.pola.rs/user-guide/installation/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de IA; cómputo y alojamiento propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un motor de consultas y DataFrames, no una app de BI; mayor velocidad que otra biblioteca depende del trabajo y configuración |
| Coste | Sin pago a un modelo en la ruta básica. Sin API de IA; cómputo y alojamiento propios |
| Equipo | Preparación según la ruta elegida. Python; CSV pequeño; memoria para los datos |

Es un motor de consultas y DataFrames, no una app de BI; mayor velocidad que otra biblioteca depende del trabajo y configuración

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- CSV pequeño
- memoria para los datos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
pip install polars
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/pola-rs/polars/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Polars para mi objetivo y necesito pasos guiados. Lee https://github.com/pola-rs/polars/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee un archivo y agrupa por una columna para sumar otra.

**Qué comprobar:** Puedes contrastar el resultado con una muestra calculada a mano.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Transformar tablas
- Preparar datos antes de un dashboard

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Transformar tablas; Preparar datos antes de un dashboard | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un motor de consultas y DataFrames, no una app de BI; mayor velocidad que otra biblioteca depende del trabajo y configuración

## Stack y modelos

- **Stack:** Python; CSV pequeño; memoria para los datos
- **Etiquetas:** `data` `python` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DuckDB](duckdb.md) | 43.1k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |
| [pandas](pandas.md) | 50.5k | Biblioteca estándar de Python para analizar y transformar datos tabulares con DataFrame y Series: limpieza, agrupaciones, uniones, series temporales y E/S. |

## Enlaces

- 🐙 GitHub: [pola-rs/polars](https://github.com/pola-rs/polars)
- 🌐 Web: <https://docs.pola.rs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pola-rs/polars/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
