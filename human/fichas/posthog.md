[🏠 Inicio](../README.md) › [📊 Analizar datos, crear dashboards y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Analítica web y de producto

# 📈 posthog

> Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.8k | NOASSERTION | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Cubre todo el ciclo de medición de producto sin integrar varias herramientas.

## Por qué destaca

Referente open source de analítica de producto, autohospedable y muy adoptado por equipos que quieren evitar el lock-in de herramientas SaaS. Su licencia MIT y la amplitud de funciones (replay, flags, A/B tests) lo hacen competitivo frente a Amplitude/Mixpanel.

## Cómo funciona

Instrumentas eventos con su SDK (JS/Python/etc.) que se ingieren en su backend, y exploras todo desde su panel web con funnels, grabaciones de sesión y experimentos.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/PostHog/posthog/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar posthog para mi objetivo y necesito pasos guiados. Lee https://github.com/PostHog/posthog/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/PostHog/posthog/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
