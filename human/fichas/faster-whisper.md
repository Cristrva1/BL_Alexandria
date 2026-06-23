# faster-whisper

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión.

## Que problema resuelve

el rendimiento importa

## Por que tiene valor

Aporta valor en `runtime` para media, memory, audio. Stack declarado: Python, CTranslate2.

## Cuando usarlo

el rendimiento importa

## Cuando NO usarlo

necesitas alineación/diarización ([whisperX](#-whisperx)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `whisperx`

## Contra que compite

- `whisperx`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con whisperx cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si el rendimiento importa. No debe instalarse por inercia.
