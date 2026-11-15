[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Kestra

> Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.2k | Apache-2.0 | Java | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Define flujos en YAML con un editor web, cientos de plugins y disparadores por calendario o eventos. Pensado para equipos de datos y plataforma que quieren orquestación como código.

## Por qué destaca

Une el enfoque declarativo de infraestructura con una UI completa; escala bien y tiene muchos plugins.

## Cómo funciona

Un servidor Java guarda los flujos YAML y reparte tareas a workers; cada tarea es un plugin (scripts, SQL, APIs, contenedores).

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/kestra-io/kestra/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kestra para mi objetivo y necesito pasos guiados. Lee https://github.com/kestra-io/kestra/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `automation` `data` `java` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DuckDB](duckdb.md) | 43.1k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Windmill](windmill.md) | 18.6k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Trigger.dev](trigger-dev.md) | 16.8k | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. |

## Enlaces

- 🐙 GitHub: [kestra-io/kestra](https://github.com/kestra-io/kestra)
- 🌐 Web: <https://go.kestra.io/home>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/kestra-io/kestra/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
