# litellm

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.

## Que problema resuelve

trabajas con múltiples modelos

## Por que tiene valor

Aporta valor en `library` para llmops. Stack declarado: Python.

## Cuando usarlo

trabajas con múltiples modelos

## Cuando NO usarlo

usas un único proveedor fijo.

## Tipo de instalacion

reference_only

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

Veredicto: referencia. Tiene sentido si trabajas con múltiples modelos. No debe instalarse por inercia.
