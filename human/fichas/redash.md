[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 Redash

> Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.9k | BSD-2-Clause | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; varios servicios con Docker Compose

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Redash, herramienta para consultar fuentes de datos con SQL, visualizar y compartir resultados. Licencia BSD-2-Clause. Es madura (~29k estrellas) y sigue publicando versiones (v26.9.0).

## ¿Qué hace?

Ofrece un editor SQL en el navegador con autocompletado, visualizaciones, paneles, alertas y consultas programadas. Se conecta a bases SQL, NoSQL, APIs y servicios en la nube. Todo se comparte mediante URL.

## ¿Cómo lo hace?

Se autoaloja siguiendo la guía de instalación (Docker, con imágenes preparadas para AWS y GCE). Está escrito en Python con frontend React y requiere PostgreSQL y Redis.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Consultar archivos locales o analíticos con SQL. (combinación por arquitectura) | Configura la fuente de datos correspondiente. |
| [supabase](supabase.md) | Fuente PostgreSQL para consultas y paneles. (combinación por arquitectura) | Conecta con un usuario de solo lectura. |
| [activepieces](activepieces.md) | Disparar flujos a partir de alertas de Redash. (combinación por arquitectura) | Configura un webhook de alerta hacia Activepieces. |

**Notas:** Alternativas (elige una): metabase, superset.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v26.9.0 (2026-09-24) · licencia declarada BSD-2-Clause (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/getredash/redash/blob/master/README.md) · [2](https://redash.io/help/)</sub>

## Ver similares

Grupo **BI y dashboards**: Redash ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Apache Superset](superset.md) ⭐ recomendado | 82 | Si buscas esto: plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |
| 2 | [metabase](metabase.md) | 67 | Si buscas esto: herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |
| 3 | **Redash** (esta ficha) | 57 | Si buscas esto: herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo; servidor, fuentes y ejecución de consultas pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La facilidad de consumir un dashboard no elimina la necesidad de preparar consultas y conexiones correctas |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo; servidor, fuentes y ejecución de consultas pueden costar |
| Equipo | Preparación según la ruta elegida. Servidor según guía; fuente de datos; SQL básico |

La facilidad de consumir un dashboard no elimina la necesidad de preparar consultas y conexiones correctas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor según guía
- fuente de datos
- SQL básico

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker-compose up -d
```

Comando copiado literalmente de la documentación del repositorio (sección «Mail Configuration»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/getredash/redash/blob/master/docs/open-source/setup.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Redash para mi objetivo y necesito pasos guiados. Lee https://github.com/getredash/redash/blob/master/docs/open-source/setup.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una consulta sobre una tabla ficticia y conviértela en una gráfica.

**Qué comprobar:** Puedes revisar consulta, filas y visualización del mismo resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Compartir consultas de negocio
- Crear dashboards a partir de fuentes SQL

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Compartir consultas de negocio; Crear dashboards a partir de fuentes SQL | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La facilidad de consumir un dashboard no elimina la necesidad de preparar consultas y conexiones correctas

## Stack y modelos

- **Stack:** Servidor según guía; fuente de datos; SQL básico
- **Etiquetas:** `analytics` `dataviz` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [metabase](metabase.md) | 50.3k | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |

## Enlaces

- 🐙 GitHub: [getredash/redash](https://github.com/getredash/redash)
- 🌐 Web: <http://redash.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/getredash/redash/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
