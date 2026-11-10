[🏠 Inicio](../README.md) › [📊 Analítica & Visualización](../categorias/10-anal-tica-visualizaci-n.md) › Analítica web y de producto

# 📈 posthog

> Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 40.7k | Otra (ver repo) | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Cubre todo el ciclo de medición de producto sin integrar varias herramientas.

## Por qué destaca

Referente open source de analítica de producto, autohospedable y muy adoptado por equipos que quieren evitar el lock-in de herramientas SaaS. Su licencia MIT y la amplitud de funciones (replay, flags, A/B tests) lo hacen competitivo frente a Amplitude/Mixpanel.

## Cómo funciona

Instrumentas eventos con su SDK (JS/Python/etc.) que se ingieren en su backend, y exploras todo desde su panel web con funnels, grabaciones de sesión y experimentos.

## Instalación rápida

`docker compose` para self-host, o SDK vía `npm i posthog-js` / `pip install posthog` apuntando al cloud. El self-host requiere ClickHouse y recursos no triviales.

## Casos de uso

- Medir conversiones antes/después de cambios
- Funnels y session replay para diagnosticar fricción
- Feature flags y A/B tests controlados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres entender el uso real y el comportamiento de usuarios | solo necesitas BI sobre una BD estática (metabase) |

## Stack y modelos

- **Stack:** Python/Node, ClickHouse, self-host o cloud
- **Modelos / API:** Complementa apps instrumentadas con agentes.
- **Etiquetas:** `analytics` `python` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [metabase](metabase.md) | 50.3k | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |

## Enlaces

- 🐙 GitHub: [PostHog/posthog](https://github.com/PostHog/posthog)
- 🌐 Web: <https://posthog.com>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
