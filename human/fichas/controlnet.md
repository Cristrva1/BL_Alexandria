# ControlNet

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

DIFERIR

## Para que sirve realmente

ControlNet 1.1 is released. Those new models will be merged to this repo after we make sure that everything is good.

## Que problema resuelve

necesitas control estructural fino de la composición

## Por que tiene valor

Aporta valor en `library` para python, typescript. Stack declarado: python, typescript.

## Cuando usarlo

necesitas control estructural fino de la composición

## Cuando NO usarlo

ya trabajas en SD WebUI ([sd-webui-controlnet](#-sd-webui-controlnet)) o ComfyUI (tienen integración propia) y no necesitas el repo original.

## Tipo de instalacion

deferred

## Stack / tecnologia detectada

python, typescript

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `diffusers`
- `comfyui`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con diffusers, comfyui cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si necesitas control estructural fino de la composición. No debe instalarse por inercia.
