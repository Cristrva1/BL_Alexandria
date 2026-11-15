[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# metabase vs Apache Superset

| | [metabase](../fichas/metabase.md) | [Apache Superset](../fichas/superset.md) |
|---|---|---|
| Qué hace | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |
| ⭐ Estrellas | 50.3k | 75.5k |
| Elígelo si… | quieres BI accesible para perfiles no técnicos | quieres BI empresarial abierto |
| Evítalo si… | necesitas analítica de eventos por usuario (posthog) | buscas algo muy fácil para no técnicos; mira `metabase` |
| Ejecución | 🔀 híbrido | 🏠 local |
| Setup | 🟡 medio | 🟡 medio |
| Licencia | Otra (ver repo) | Apache-2.0 |
| Instalación | `docker run metabase/metabase` | `git clone https://github.com/apache/superset && cd superset && docker compose -f docker-compose-image-tag.yml up` |

## Regla práctica

- Elige **metabase** si quieres BI accesible para perfiles no técnicos.
- Elige **Apache Superset** si quieres BI empresarial abierto.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
