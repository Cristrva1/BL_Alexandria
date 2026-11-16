[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 Grafana

> Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 77.9k | AGPL-3.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Puntuación de calidad** 80/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Grafana, plataforma open source de visualización y observabilidad de Grafana Labs. Licencia AGPL-3.0-only con excepciones Apache-2.0. Es muy madura (~78k estrellas, v13.3.1).

## ¿Qué hace?

Consulta, visualiza y alerta sobre métricas, logs y trazas estén donde estén, con paneles dinámicos y variables. Permite explorar datos ad hoc, alertas unificadas y mezclar fuentes en un mismo panel. Se amplía con plugins de fuentes de datos y paneles.

## ¿Cómo lo hace?

Se instala con paquetes, Docker o Helm, o se usa en Grafana Cloud. Está escrito en Go y TypeScript y usa SQLite, MySQL o PostgreSQL para su configuración.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langfuse](langfuse.md) | Paneles operativos sobre métricas de apps LLM. (combinación por arquitectura) | Expón métricas de Langfuse a una fuente compatible y crea paneles. |
| [supabase](supabase.md) | Fuente PostgreSQL nativa para paneles sobre Supabase. | Añade la conexión Postgres de Supabase como fuente. |
| [Umami](umami.md) | Panel sobre la base PostgreSQL de Umami. (combinación por arquitectura) | Añade la base de Umami como fuente. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (21). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Apache Airflow](airflow.md) · [ClickHouse](clickhouse.md) · [CrowdSec](crowdsec.md) · [freqtrade](freqtrade.md) · [Headscale](headscale.md) · [hummingbot](hummingbot.md) · [k6](k6.md) · [Locust](locust.md) · [Matomo](matomo.md) · [NetBird](netbird.md) · [Node-RED](node-red.md) · [open-sol-bot](open-sol-bot.md) · [OpenLLMetry](openllmetry.md) · [Pi-hole](pi-hole.md) · [Plausible Analytics](plausible.md) · [Synapse](synapse.md) · [Temporal](temporal.md) · [Traefik Proxy](traefik.md) · [uPlot](uplot.md) · [Uptime Kuma](uptime-kuma.md) · [WireGuard Easy](wg-easy.md)

**Notas:** Sin alternativas declaradas. AGPL: ofrecerlo modificado como servicio obliga a publicar cambios.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v13.3.1 (2026-11-10) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/grafana/grafana/blob/main/README.md) · [2](https://grafana.com/docs/grafana/latest/datasources/postgres/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El dashboard básico no usa LLM; Cloud, Enterprise, almacenamiento y fuentes tienen planes y consumo propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Grafana visualiza fuentes existentes; no recopila automáticamente todos los datos de tus sistemas |
| Coste | El coste depende del proveedor o la ruta. El dashboard básico no usa LLM; Cloud, Enterprise, almacenamiento y fuentes tienen planes y consumo propios |
| Equipo | Preparación según la ruta elegida. Servidor o cuenta Cloud; fuente de métricas; permisos de consulta |

Grafana visualiza fuentes existentes; no recopila automáticamente todos los datos de tus sistemas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor o cuenta Cloud
- fuente de métricas
- permisos de consulta

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Grafana para mi objetivo y necesito pasos guiados. Lee https://grafana.com/docs/grafana/latest/setup-grafana/installation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta una fuente de prueba y grafica una métrica con un rango temporal explícito.

**Qué comprobar:** El panel coincide con la consulta y cambia al ajustar el periodo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Observar consumo de un servicio
- Compartir métricas de una operación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Observar consumo de un servicio; Compartir métricas de una operación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Grafana visualiza fuentes existentes; no recopila automáticamente todos los datos de tus sistemas

## Stack y modelos

- **Stack:** Servidor o cuenta Cloud; fuente de métricas; permisos de consulta
- **Etiquetas:** `observability` `dataviz` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [grafana/grafana](https://github.com/grafana/grafana)
- 🌐 Web: <https://grafana.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/grafana/grafana/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
