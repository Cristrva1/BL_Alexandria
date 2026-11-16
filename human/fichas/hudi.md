[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🧑‍💻 hudi

> Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.4k | Apache-2.0 | Java | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 51/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Apache Hudi, plataforma de data lakehouse abierta sobre un formato de tabla de alto rendimiento, de la Apache Software Foundation. Licencia Apache-2.0. Es madura (~6.4k estrellas, release-1.2.1).

## ¿Qué hace?

Ingiere, indexa, almacena, sirve y transforma datos en almacenamiento cloud con upserts, borrados, consultas incrementales y time travel. Sus servicios de tabla (compactación, clustering, limpieza) son automáticos.

## ¿Cómo lo hace?

Se integra con Apache Spark y Flink (herramientas de ingestión integradas) y lo consultan motores como Trino, Presto o Hive. Se compila con Maven (`mvn clean package -Dspark3.5 -Dflink2.2`) o se usan los paquetes publicados.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Leer datos del lakehouse para análisis local. (combinación por arquitectura) | Lee los Parquet subyacentes. |
| [Apache Superset](superset.md) | BI sobre tablas Hudi vía un motor SQL. (combinación por arquitectura) | Conecta Superset al motor de consulta. |
| [awesome-bigdata](awesome-bigdata.md) | Mapa del ecosistema alrededor. (combinación por arquitectura) | Consulta la lista. |
| [Apache Spark](spark.md) | Combinación recíproca: Apache Spark lo enlaza como «Hudi se integra con Spark como motor principal de escritura e ingestión incremental». | Orden indicado desde Apache Spark: Añade el bundle de Hudi para Spark; después escribe con `format("hudi")`. |

**Notas:** Alternativas (elige una): apache-iceberg, delta-lake.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada release-1.2.1 (2026-09-24) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/hudi/blob/master/README.md)</sub>

## Ver similares

Grupo **Formatos de tabla para data lakes**: hudi ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Delta Lake](delta-lake.md) ⭐ recomendado | 63 | Si buscas esto: capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores. |
| 2 | [Apache Iceberg](apache-iceberg.md) | 62 | Si buscas esto: formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java. |
| 3 | **hudi** (esta ficha) | 51 | Si buscas esto: plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API de IA; motores, almacenamiento y nube se presupuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Los comandos para compilar snapshots son para desarrollo; el quickstart de la versión elegida debe coincidir con Spark o Flink instalados |
| Coste | Sin pago a un modelo en la ruta básica. No necesita API de IA; motores, almacenamiento y nube se presupuestan aparte |
| Equipo | Preparación según la ruta elegida. Java y Spark o Flink compatibles; almacenamiento de prueba; datos pequeños |

Los comandos para compilar snapshots son para desarrollo; el quickstart de la versión elegida debe coincidir con Spark o Flink instalados

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Java y Spark o Flink compatibles
- almacenamiento de prueba
- datos pequeños

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
git clone https://github.com/apache/hudi.git && cd hudi
```

Comando copiado literalmente de el README (sección «Building Apache Hudi from source»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/apache/hudi/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar hudi para mi objetivo y necesito pasos guiados. Lee https://github.com/apache/hudi/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inserta registros ficticios y actualiza uno para comparar estado y consulta incremental.

**Qué comprobar:** Puedes comprobar la actualización sin reconstruir manualmente toda la tabla.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un lakehouse
- Preparar ingestión incremental

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un lakehouse; Preparar ingestión incremental | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los comandos para compilar snapshots son para desarrollo; el quickstart de la versión elegida debe coincidir con Spark o Flink instalados

## Stack y modelos

- **Stack:** Java y Spark o Flink compatibles; almacenamiento de prueba; datos pequeños
- **Etiquetas:** `datos` `apacheflink` `apachehudi` `apachespark` `bigdata` `data-integration` `datalake` `hudi`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Iceberg](apache-iceberg.md) | 9.4k | Formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java. |
| [Delta Lake](delta-lake.md) | 9.1k | Capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores. |

## Enlaces

- 🐙 GitHub: [apache/hudi](https://github.com/apache/hudi)
- 🌐 Web: <https://hudi.apache.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/hudi/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
