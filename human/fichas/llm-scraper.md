# llm-scraper

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.

## Que problema resuelve

quieres salida tipada

## Por que tiene valor

Aporta valor en `library` para scraping. Stack declarado: TypeScript.

## Cuando usarlo

quieres salida tipada

## Cuando NO usarlo

prefieres extracción semántica por grafos ([Scrapegraph-ai](#-scrapegraph-ai)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `playwright`
- `firecrawl`

## Contra que compite

- `scrapegraph-ai`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con playwright, firecrawl cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si quieres salida tipada. No debe instalarse por inercia.
