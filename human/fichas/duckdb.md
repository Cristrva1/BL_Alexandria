[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Datos y notebooks

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
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

El "SQLite de la analítica": sin servidor, embebida en Python, R o Node, y capaz de procesar millones de filas en segundos.

## Por qué destaca

Rendimiento excelente sin infraestructura y SQL directo sobre archivos.

## Cómo funciona

Motor columnar vectorizado que lee formatos de archivo directamente y ejecuta SQL en paralelo.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/duckdb/duckdb/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DuckDB para mi objetivo y necesito pasos guiados. Lee https://github.com/duckdb/duckdb/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
| [Polars](polars.md) | 40.3k | Librería de DataFrames escrita en Rust, mucho más rápida que pandas. |

## Enlaces

- 🐙 GitHub: [duckdb/duckdb](https://github.com/duckdb/duckdb)
- 🌐 Web: <http://www.duckdb.org>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/duckdb/duckdb/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
