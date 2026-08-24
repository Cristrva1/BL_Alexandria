# litellm

Generado: 2026-08-24T04:13:47.607813+00:00

## Decision

USAR AHORA

## Para que sirve realmente

LiteLLM is an open source AI Gateway that gives you a single, unified interface to call 100+ LLM providers — OpenAI, Anthropic, Gemini, Bedrock, Azure, and more — using the OpenAI format.

## Que problema resuelve

trabajas con múltiples modelos o quieres fallback/control de costos

## Por que tiene valor

Aporta valor en `platform` para docker, javascript, postgres, python, typescript. Stack declarado: python, typescript, javascript, docker, postgres.

## Cuando usarlo

trabajas con múltiples modelos o quieres fallback/control de costos

## Cuando NO usarlo

usas un único proveedor fijo y no necesitas abstracción.

## Tipo de instalacion

local_project

## Stack / tecnologia detectada

python, typescript, javascript, docker, postgres

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `langchain`
- `langfuse`
- `llm-council`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con langchain, langfuse, llm-council cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: usar ahora. Tiene sentido si trabajas con múltiples modelos o quieres fallback/control de costos. No debe instalarse por inercia.
