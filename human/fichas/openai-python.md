# openai-python

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

SDK oficial de OpenAI para Python, que expone de forma tipada y cómoda la API (chat, embeddings, imágenes, audio) y es la base habitual para apps que usan sus modelos.

## Que problema resuelve

usas modelos de OpenAI

## Por que tiene valor

Aporta valor en `library` para code, audio. Stack declarado: Python.

## Cuando usarlo

usas modelos de OpenAI

## Cuando NO usarlo

quieres abstracción multi-proveedor ([litellm](06-memoria-llm-ops-observabilidad.md#-litellm)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `litellm`
- `langchain`

## Contra que compite

- `litellm`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con litellm, langchain cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si usas modelos de OpenAI. No debe instalarse por inercia.
