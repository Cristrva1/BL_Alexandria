# stable-diffusion-webui

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador.

## Que problema resuelve

quieres extensiones y comunidad

## Por que tiene valor

Aporta valor en `app` para image, browser. Stack declarado: Python, GPU, modelos locales.

## Cuando usarlo

quieres extensiones y comunidad

## Cuando NO usarlo

prefieres flujo moderno/limpio ([InvokeAI](#-invokeai)).

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `sd-webui-controlnet`

## Contra que compite

- `invokeai`

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con sd-webui-controlnet cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si quieres extensiones y comunidad. No debe instalarse por inercia.
