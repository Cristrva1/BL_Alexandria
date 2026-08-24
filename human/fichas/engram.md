# engram

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

REFERENCIA

## Para que sirve realmente

Engram da a cualquier agente compatible con MCP una memoria local (o cloud) en un solo binario, sin dependencias pesadas.

## Que problema resuelve

necesitas exponer herramientas o contexto a agentes vía MCP

## Por que tiene valor

Aporta valor en `runtime` para memory, mcp, agents. Stack declarado: python, typescript, javascript, docker, postgres.

## Cuando usarlo

necesitas exponer herramientas o contexto a agentes vía MCP

## Cuando NO usarlo

prefieres conexiones directas sin protocolo estándar

## Tipo de instalacion

reference_only

## Stack / tecnologia detectada

python, typescript, javascript, docker, postgres

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `claude-plugins-official`
- `n8n-skills`
- `mcp`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con claude-plugins-official, n8n-skills, mcp cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si necesitas exponer herramientas o contexto a agentes vía MCP. No debe instalarse por inercia.
