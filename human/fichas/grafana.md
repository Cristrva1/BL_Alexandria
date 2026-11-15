[🏠 Inicio](../README.md) › [📊 Analítica & Visualización](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 Grafana

> Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 77.8k | AGPL-3.0 | TypeScript | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Qué es

Crea dashboards y alertas sobre Prometheus, Loki, bases SQL y decenas de fuentes. Estándar en monitoreo.

## Por qué destaca

El estándar de facto para dashboards de monitoreo.

## Cómo funciona

Un servidor Go consulta las fuentes por plugins y un frontend React dibuja paneles y alertas.

## Instalación rápida

`docker run -d -p 3000:3000 grafana/grafana`.

## Casos de uso

- Monitorear servidores y APIs
- Alertas de métricas
- Dashboards de costos de LLM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas monitoreo y alertas en tiempo real | buscas BI de negocio; mira `superset` o `metabase` |

**Limitaciones:** Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** Go, TypeScript, Docker
- **Modelos / API:** No usa LLM de serie.
- **Etiquetas:** `observability` `dataviz` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Enlaces

- 🐙 GitHub: [grafana/grafana](https://github.com/grafana/grafana)
- 🌐 Web: <https://grafana.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
