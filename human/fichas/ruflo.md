# ruflo

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). Orquesta swarms de agentes especializados a escala.

## Que problema resuelve

orquestas muchos agentes a escala

## Por que tiene valor

Aporta valor en `platform` para agents, memory. Stack declarado: Rust.

## Cuando usarlo

orquestas muchos agentes a escala

## Cuando NO usarlo

solo necesitas 1-2 agentes.

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `mem0`
- `ecc`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con mem0, ecc cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si orquestas muchos agentes a escala. No debe instalarse por inercia.
