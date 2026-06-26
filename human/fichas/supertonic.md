# supertonic

Generado: 2026-06-26T07:47:33.067156+00:00

## Decision

DIFERIR

## Para que sirve realmente

Supertonic** is a lightning-fast, on-device multilingual text-to-speech system designed for local inference with minimal overhead. Powered by ONNX Runtime, it runs entirely on your device—no cloud, no API calls, no privacy concerns.

## Que problema resuelve

quieres voz local en tiempo real y sin nube

## Por que tiene valor

Aporta valor en `library` para javascript, multimedia, python, typescript. Stack declarado: python, typescript, javascript.

## Cuando usarlo

quieres voz local en tiempo real y sin nube

## Cuando NO usarlo

priorizas clonación de máxima fidelidad ([VoxCPM](#-voxcpm)) o flexibilidad multi-modelo ([TTS](#-tts)).

## Tipo de instalacion

deferred

## Stack / tecnologia detectada

python, typescript, javascript

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `whisperx`
- `moviepy`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con whisperx, moviepy cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si quieres voz local en tiempo real y sin nube. No debe instalarse por inercia.
