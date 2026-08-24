# playwright-cli

Generado: 2026-08-24T04:13:47.607813+00:00

## Decision

REFERENCIA

## Para que sirve realmente

Playwright CLI with SKILLS.

## Que problema resuelve

tu agente vive en CLI y el contexto es un recurso caro

## Por que tiene valor

Aporta valor en `skill` para javascript, javascript-typescript, python, typescript. Stack declarado: javascript/typescript, python, typescript, javascript.

## Cuando usarlo

tu agente vive en CLI y el contexto es un recurso caro

## Cuando NO usarlo

necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP).

## Tipo de instalacion

reference_only

## Stack / tecnologia detectada

javascript/typescript, python, typescript, javascript

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `playwright`
- `browser-use`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo de ruido: leer y seleccionar, no instalar catalogos completos.

## Ideas profesionales

Combinar con playwright, browser-use cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si tu agente vive en CLI y el contexto es un recurso caro. No debe instalarse por inercia.
