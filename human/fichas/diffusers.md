# diffusers

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

librería de Hugging Face para construir y ejecutar pipelines de modelos de difusión (imagen, video, audio) desde código, con APIs estandarizadas para schedulers y modelos.

## Que problema resuelve

programas generación

## Por que tiene valor

Aporta valor en `library` para image, audio, video. Stack declarado: Python, PyTorch.

## Cuando usarlo

programas generación

## Cuando NO usarlo

quieres una UI lista ([Fooocus](#-fooocus)).

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `controlnet`
- `cosmos`

## Contra que compite

- `fooocus`

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con controlnet, cosmos cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si programas generación. No debe instalarse por inercia.
