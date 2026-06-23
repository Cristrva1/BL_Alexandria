# supertonic

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU.

## Que problema resuelve

quieres voz local en tiempo real

## Por que tiene valor

Aporta valor en `runtime` para media, browser, audio. Stack declarado: Python, Rust (ONNX/PyTorch), Node.js.

## Cuando usarlo

quieres voz local en tiempo real

## Cuando NO usarlo

priorizas clonación de máxima fidelidad ([VoxCPM](#-voxcpm)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `whisperx`
- `moviepy`

## Contra que compite

- `voxcpm`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con whisperx, moviepy cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si quieres voz local en tiempo real. No debe instalarse por inercia.
