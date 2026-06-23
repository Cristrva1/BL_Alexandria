# ControlNet

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

método y modelos para condicionar la generación text-to-image con señales externas como poses, bordes, profundidad o mapas de segmentación, fijando la estructura del resultado.

## Que problema resuelve

necesitas control estructural

## Por que tiene valor

Aporta valor en `runtime` para image. Stack declarado: Python, difusión, GPU.

## Cuando usarlo

necesitas control estructural

## Cuando NO usarlo

ya trabajas en SD WebUI ([sd-webui-controlnet](#-sd-webui-controlnet)).

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `diffusers`
- `comfyui`

## Contra que compite

- `sd-webui-controlnet`

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con diffusers, comfyui cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si necesitas control estructural. No debe instalarse por inercia.
