# graphrag

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.

## Que problema resuelve

tu corpus tiene relaciones ricas

## Por que tiene valor

Aporta valor en `library` para code, rag, graph. Stack declarado: Python.

## Cuando usarlo

tu corpus tiene relaciones ricas

## Cuando NO usarlo

un RAG simple basta.

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `graphify`
- `mcp-neo4j`
- `turbovec`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con graphify, mcp-neo4j, turbovec cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si tu corpus tiene relaciones ricas. No debe instalarse por inercia.
