# graphrag

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

DIFERIR

## Para que sirve realmente

👉 Microsoft Research Blog Post 👉 Read the docs 👉 GraphRAG Arxiv.

## Que problema resuelve

tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto

## Por que tiene valor

Aporta valor en `library` para python, typescript. Stack declarado: python, typescript.

## Cuando usarlo

tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto

## Cuando NO usarlo

un RAG simple basta o el coste de indexado con LLM es prohibitivo.

## Tipo de instalacion

deferred

## Stack / tecnologia detectada

python, typescript

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `graphify`
- `mcp-neo4j`
- `turbovec`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con graphify, mcp-neo4j, turbovec cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto. No debe instalarse por inercia.
