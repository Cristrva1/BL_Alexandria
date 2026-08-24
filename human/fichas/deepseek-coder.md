# DeepSeek-Coder

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

DIFERIR

## Para que sirve realmente

DeepSeek Coder is composed of a series of code language models, each trained from scratch on 2T tokens, with a composition of 87% code and 13% natural language in both English and Chinese. We provide various sizes of the code model, ranging from 1B to 33B versions.

## Que problema resuelve

quieres un modelo de código abierto y desplegable on-prem

## Por que tiene valor

Aporta valor en `library` para docker, javascript, python, typescript. Stack declarado: python, typescript, javascript, docker.

## Cuando usarlo

quieres un modelo de código abierto y desplegable on-prem

## Cuando NO usarlo

prefieres APIs comerciales gestionadas o no tienes GPU para servirlo.

## Tipo de instalacion

deferred

## Stack / tecnologia detectada

python, typescript, javascript, docker

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `litellm`
- `codegraph`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con litellm, codegraph cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si quieres un modelo de código abierto y desplegable on-prem. No debe instalarse por inercia.
