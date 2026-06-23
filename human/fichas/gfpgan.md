# GFPGAN

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

algoritmo de restauración facial que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados.

## Que problema resuelve

restauras rostros

## Por que tiene valor

Aporta valor en `runtime` para image, training. Stack declarado: Python, PyTorch, GPU opcional.

## Cuando usarlo

restauras rostros

## Cuando NO usarlo

necesitas upscaling general ([Real-ESRGAN](#-real-esrgan)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `real-esrgan`

## Contra que compite

- `real-esrgan`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con real-esrgan cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si restauras rostros. No debe instalarse por inercia.
