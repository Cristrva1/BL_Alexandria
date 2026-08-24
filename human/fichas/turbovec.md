# turbovec

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

REFERENCIA

## Para que sirve realmente

A 10 million document corpus takes 31 GB of RAM as float32. turbovec fits it in 4 GB - and searches it faster than FAISS..

## Que problema resuelve

necesitas vector search veloz y embebido sin desplegar una DB

## Por que tiene valor

Aporta valor en `directory` para automation, langchain, python, typescript. Stack declarado: python, typescript, langchain.

## Cuando usarlo

necesitas vector search veloz y embebido sin desplegar una DB

## Cuando NO usarlo

ya usas una vector DB completa con persistencia y escalado horizontal.

## Tipo de instalacion

reference_only

## Stack / tecnologia detectada

python, typescript, langchain

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `mem0`
- `graphrag`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con mem0, graphrag cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si necesitas vector search veloz y embebido sin desplegar una DB. No debe instalarse por inercia.
