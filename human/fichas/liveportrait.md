# LivePortrait

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen.

## Que problema resuelve

animas retratos

## Por que tiene valor

Aporta valor en `runtime` para image, video. Stack declarado: Python, GPU.

## Cuando usarlo

animas retratos

## Cuando NO usarlo

necesitas swap en vivo ([Deep-Live-Cam](#-deep-live-cam)).

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `moviepy`

## Contra que compite

- `deep-live-cam`

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con moviepy cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si animas retratos. No debe instalarse por inercia.
