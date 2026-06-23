# sandbox

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado.

## Que problema resuelve

quieres aislar la ejecución de agentes

## Por que tiene valor

Aporta valor en `platform` para llmops, browser, mcp, agents. Stack declarado: Docker/web.

## Cuando usarlo

quieres aislar la ejecución de agentes

## Cuando NO usarlo

te basta correr local sin sandbox.

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `openhands`
- `ecc`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con openhands, ecc cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si quieres aislar la ejecución de agentes. No debe instalarse por inercia.
