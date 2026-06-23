# agentmemory

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes.

## Que problema resuelve

cambias de asistente y quieres una memoria común

## Por que tiene valor

Aporta valor en `library` para llmops, memory, agents. Stack declarado: motor iii.

## Cuando usarlo

cambias de asistente y quieres una memoria común

## Cuando NO usarlo

te basta la memoria nativa del cliente.

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `mem0`
- `ruflo`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con mem0, ruflo cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si cambias de asistente y quieres una memoria común. No debe instalarse por inercia.
