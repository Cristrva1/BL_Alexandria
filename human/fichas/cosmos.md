# cosmos

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

DIFERIR

## Para que sirve realmente

Colección NVIDIA Cosmos para modelos de mundo y video. Setup pesado: GPU y checkpoints. No es un editor de imagen ligero.

## Que problema resuelve

trabajas IA física/robótica y necesitas datos sintéticos

## Por que tiene valor

Aporta valor en `runtime` para docker, postgres, python, typescript. Stack declarado: python, typescript, docker, postgres.

## Cuando usarlo

trabajas IA física/robótica y necesitas datos sintéticos

## Cuando NO usarlo

haces tareas de texto/UI o no tienes GPU para servirlo.

## Tipo de instalacion

deferred

## Stack / tecnologia detectada

python, typescript, docker, postgres

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `diffusers`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con diffusers cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si trabajas IA física/robótica y necesitas datos sintéticos. No debe instalarse por inercia.
