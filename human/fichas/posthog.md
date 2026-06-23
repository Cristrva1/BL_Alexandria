# posthog

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite.

## Que problema resuelve

quieres entender el uso real

## Por que tiene valor

Aporta valor en `platform` para dataviz. Stack declarado: Python/Node, self-host o cloud.

## Cuando usarlo

quieres entender el uso real

## Cuando NO usarlo

solo necesitas BI sobre una BD ([metabase](#-metabase)).

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `metabase`

## Contra que compite

- `metabase`

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con metabase cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si quieres entender el uso real. No debe instalarse por inercia.
