[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# ⚙️ ClickHouse

> Base de datos analítica columnar de código abierto para consultas SQL en tiempo real sobre miles de millones de filas, autoalojable o en la nube.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51k | Apache-2.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 79/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema de gestión de bases de datos columnar de código abierto (Apache-2.0) mantenido por ClickHouse Inc., que también vende ClickHouse Cloud. Muy activo, con versiones mensuales; en enero de 2026 la empresa adquirió Langfuse, que usa ClickHouse como almacén analítico.

## ¿Qué hace?

Ejecuta consultas analíticas (OLAP) muy rápidas sobre grandes volúmenes: agregaciones, ventanas, joins y funciones especializadas para series temporales, logs y eventos. Lee y escribe muchos formatos (CSV, Parquet, JSON) y tablas externas (S3, Iceberg, Delta), y replica y fragmenta datos en clúster.

## ¿Cómo lo hace?

Servidor C++ con almacenamiento columnar comprimido, ejecución vectorizada y motores de tabla de la familia MergeTree. Se instala con el script oficial, paquetes o Docker; `clickhouse-local` permite consultar archivos sin servidor. Requiere más operación que una base embebida como DuckDB.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langfuse](langfuse.md) | Langfuse v3 usa ClickHouse como almacén analítico de trazas y observaciones en sus despliegues autoalojados. | Despliega ClickHouse (o usa el incluido en el chart/compose de Langfuse); después configura Langfuse con su URL. |
| [Grafana](grafana.md) | El plugin oficial de ClickHouse para Grafana permite construir paneles con consultas SQL a ClickHouse. | Instala el plugin grafana-clickhouse-datasource; después añade ClickHouse como fuente de datos. |
| [metabase](metabase.md) | Metabase incluye un driver de ClickHouse para explorar y crear dashboards sobre sus tablas. | Levanta ClickHouse; después añádelo como base de datos en Metabase. |
| [dbt](dbt.md) | ClickHouse mantiene el adaptador dbt-clickhouse para transformar datos con modelos dbt. | Instala `dbt-clickhouse`; después configura el perfil con el host de ClickHouse. |
| [Apache Superset](superset.md) | Superset se conecta a ClickHouse mediante el conector SQLAlchemy `clickhouse-connect`. | Instala `clickhouse-connect` en Superset; después añade la base con su URI. |
| [Ibis](ibis.md) | Combinación recíproca: Ibis lo enlaza como «Ibis incluye un backend de ClickHouse para ejecutar expresiones en un servidor ClickHouse». | Orden indicado desde Ibis: Instala `ibis-framework[clickhouse]`; después conecta con `ibis.clickhouse.connect(...)`. |

**Notas:** Alternativa cercana a DuckDB para analítica, pero orientada a servidor y clúster; DuckDB es embebida y local.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v26.9.29.5-stable (2026-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ClickHouse/ClickHouse/blob/master/README.md) · [2](https://langfuse.com/self-hosting) · [3](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability) · [4](https://github.com/grafana/clickhouse-datasource) · [5](https://github.com/ClickHouse/dbt-clickhouse) · [6](https://clickhouse.com/docs/integrations/superset)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
curl https://clickhouse.com/ | sh
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/ClickHouse/ClickHouse/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ClickHouse para mi objetivo y necesito pasos guiados. Lee https://github.com/ClickHouse/ClickHouse/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `curl https://clickhouse.com/ | sh` en una máquina de pruebas y consulta un CSV local con `./clickhouse local`..

**Qué comprobar:** Obtienes el resultado de la consulta SQL en la terminal sin levantar un servidor..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- guardar y consultar logs, métricas o eventos de producto con latencias de segundos
- servir de motor para dashboards analíticos sobre grandes volúmenes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: guardar y consultar logs, métricas o eventos de producto con latencias de segundos; servir de motor para dashboards analíticos sobre grandes volúmenes | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. ClickHouse Cloud es un servicio de pago; el servidor de este repositorio es Apache-2.0. Revisa el script de instalación antes de ejecutarlo.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt, pyproject.toml
- **Etiquetas:** `database` `sql` `analytics` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)
- 🌐 Web: <https://clickhouse.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ClickHouse/ClickHouse/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
