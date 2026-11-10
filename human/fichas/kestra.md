[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Kestra

> Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 30.2k | Apache-2.0 | Java | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Define flujos en YAML con un editor web, cientos de plugins y disparadores por calendario o eventos. Pensado para equipos de datos y plataforma que quieren orquestación como código.

## Por qué destaca

Une el enfoque declarativo de infraestructura con una UI completa; escala bien y tiene muchos plugins.

## Cómo funciona

Un servidor Java guarda los flujos YAML y reparte tareas a workers; cada tarea es un plugin (scripts, SQL, APIs, contenedores).

## Instalación rápida

`docker run --pull=always -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock kestra/kestra:latest server local`.

## Casos de uso

- Pipelines ETL programados
- Orquestar dbt, Airbyte y scripts
- Procesos de negocio con aprobaciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres workflows declarativos en YAML con UI y control de versiones | buscas automatizaciones de negocio con nodos visuales; mira `n8n` |

**Limitaciones:** Funciones de equipo como RBAC y SSO son de la edición Enterprise.

## Stack y modelos

- **Stack:** Java, Vue, YAML, Docker
- **Modelos / API:** Agnóstico: plugins para OpenAI, Ollama y otros.
- **Etiquetas:** `automation` `data` `java` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DuckDB](duckdb.md) | 43k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Windmill](windmill.md) | 18.5k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Trigger.dev](trigger-dev.md) | 16.7k | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. |

## Enlaces

- 🐙 GitHub: [kestra-io/kestra](https://github.com/kestra-io/kestra)
- 🌐 Web: <https://go.kestra.io/home>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
