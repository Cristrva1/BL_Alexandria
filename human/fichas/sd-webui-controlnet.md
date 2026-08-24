# sd-webui-controlnet

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

REFERENCIA

## Para que sirve realmente

The WebUI extension for ControlNet and other injection-based SD controls.

## Que problema resuelve

ya usas SD WebUI y quieres ControlNet sin cambiar de entorno

## Por que tiene valor

Aporta valor en `library` para frontend, postgres, python, typescript, vision. Stack declarado: python, typescript, postgres.

## Cuando usarlo

ya usas SD WebUI y quieres ControlNet sin cambiar de entorno

## Cuando NO usarlo

trabajas en ComfyUI (usa sus propios nodos) o por código ([diffusers](#-diffusers)).

## Tipo de instalacion

reference_only

## Stack / tecnologia detectada

python, typescript, postgres

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `stable-diffusion-webui`
- `controlnet`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con stable-diffusion-webui, controlnet cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si ya usas SD WebUI y quieres ControlNet sin cambiar de entorno. No debe instalarse por inercia.
