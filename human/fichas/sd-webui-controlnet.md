# sd-webui-controlnet

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI, con preprocesadores para poses, bordes, profundidad y más.

## Que problema resuelve

ya usas SD WebUI

## Por que tiene valor

Aporta valor en `runtime` para image. Stack declarado: Python, SD WebUI, modelos ControlNet.

## Cuando usarlo

ya usas SD WebUI

## Cuando NO usarlo

trabajas en ComfyUI o por código.

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `stable-diffusion-webui`
- `controlnet`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con stable-diffusion-webui, controlnet cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si ya usas SD WebUI. No debe instalarse por inercia.
