# VoxCPM

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y fluidez muy naturales, con clonación de voz.

## Que problema resuelve

quieres voz muy natural/clonada

## Por que tiene valor

Aporta valor en `runtime` para media, audio. Stack declarado: Python, PyTorch, GPU.

## Cuando usarlo

quieres voz muy natural/clonada

## Cuando NO usarlo

priorizas latencia mínima ([supertonic](#-supertonic)).

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `tts`

## Contra que compite

- `supertonic`

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con tts cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si quieres voz muy natural/clonada. No debe instalarse por inercia.
