[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🗃️ DuckDB

> Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 43.1k | MIT | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa LLM ni API de IA; servicios Cloud o almacenamiento remoto tienen sus condiciones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor |
| Coste | Sin pago a un modelo en la ruta básica. No usa LLM ni API de IA; servicios Cloud o almacenamiento remoto tienen sus condiciones |
| Equipo | Preparación según la ruta elegida. CLI o biblioteca para tu sistema; CSV pequeño |

Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor

## Qué puedes hacer con él

Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL.

## Por qué destaca

Usos propuestos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor.

## Cómo funciona

Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- CLI o biblioteca para tu sistema
- CSV pequeño

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://duckdb.org/docs/installation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DuckDB para mi objetivo y necesito pasos guiados. Lee https://duckdb.org/docs/installation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un CSV ficticio y consulta el total de registros y una suma por categoría.

**Qué comprobar:** Puedes comparar el resultado con las filas originales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar ventas de muestra
- Consultar Parquet sin desplegar un servidor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar ventas de muestra; Consultar Parquet sin desplegar un servidor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Para usar DuckDB instala su CLI o paquete; CMake y compilador del README son para desarrollar el motor

## Stack y modelos

- **Stack:** CLI o biblioteca para tu sistema; CSV pequeño
- **Etiquetas:** `data` `analytics` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [marimo](marimo.md) | 23.6k | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. |
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Polars](polars.md) | 40.3k | Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares. |

## Enlaces

- 🐙 GitHub: [duckdb/duckdb](https://github.com/duckdb/duckdb)
- 🌐 Web: <http://www.duckdb.org>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/duckdb/duckdb/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
