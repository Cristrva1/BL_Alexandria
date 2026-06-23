# playwright-cli

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto.

## Que problema resuelve

tu agente vive en CLI

## Por que tiene valor

Aporta valor en `skill` para scraping, browser, agents, skills, context. Stack declarado: TypeScript/CLI.

## Cuando usarlo

tu agente vive en CLI

## Cuando NO usarlo

necesitas estado persistente (usa Playwright MCP).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `playwright`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo de ruido: leer y seleccionar, no instalar catalogos completos.

## Ideas profesionales

Combinar con playwright cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si tu agente vive en CLI. No debe instalarse por inercia.
