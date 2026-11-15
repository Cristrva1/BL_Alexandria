[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 Apache Superset

> Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 75.5k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

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

## Qué puedes hacer con él

Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau.

## Por qué destaca

Usos propuestos: Explorar métricas de una base SQL; Compartir un dashboard interno.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DuckDB](duckdb.md) | 43.1k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |
| [WrenAI](wrenai.md) | 18.2k | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. |

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
