# metabase

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL.

## Que problema resuelve

quieres BI accesible

## Por que tiene valor

Aporta valor en `platform` para dataviz. Stack declarado: Java/Clojure, BD, web.

## Cuando usarlo

quieres BI accesible

## Cuando NO usarlo

necesitas analítica de eventos ([posthog](#-posthog)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `posthog`
- `echarts`

## Contra que compite

- `posthog`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con posthog, echarts cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si quieres BI accesible. No debe instalarse por inercia.
