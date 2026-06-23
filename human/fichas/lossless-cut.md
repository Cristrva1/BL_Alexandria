# lossless-cut

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la calidad original.

## Que problema resuelve

cortas material rápido

## Por que tiene valor

Aporta valor en `app` para media, audio, video. Stack declarado: Node.js/Electron, ffmpeg.

## Cuando usarlo

cortas material rápido

## Cuando NO usarlo

necesitas edición compositiva ([moviepy](#-moviepy)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `moviepy`

## Contra que compite

- `moviepy`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con moviepy cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si cortas material rápido. No debe instalarse por inercia.
