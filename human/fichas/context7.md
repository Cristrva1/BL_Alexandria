# context7

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

REFERENCIA

## Para que sirve realmente

Context7 evita que el modelo alucine APIs viejas: trae docs versionadas al contexto. Instálalo como servidor MCP en el agente de código.

## Que problema resuelve

necesitas exponer herramientas o contexto a agentes vía MCP

## Por que tiene valor

Aporta valor en `runtime` para mcp, docs, agents. Stack declarado: javascript/typescript, typescript, javascript, react.

## Cuando usarlo

necesitas exponer herramientas o contexto a agentes vía MCP

## Cuando NO usarlo

prefieres conexiones directas sin protocolo estándar

## Tipo de instalacion

reference_only

## Stack / tecnologia detectada

javascript/typescript, typescript, javascript, react

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
