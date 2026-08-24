# three.js

Generado: 2026-08-24T04:13:47.607813+00:00

## Decision

DIFERIR

## Para que sirve realmente

JavaScript 3D library.

## Que problema resuelve

renderizas 3D en web y quieres control a bajo nivel

## Por que tiene valor

Aporta valor en `library` para javascript, javascript-typescript, typescript. Stack declarado: javascript/typescript, typescript, javascript.

## Cuando usarlo

renderizas 3D en web y quieres control a bajo nivel

## Cuando NO usarlo

trabajas solo 2D o prefieres la ergonomía de React ([react-three-fiber](#-react-three-fiber)).

## Tipo de instalacion

deferred

## Stack / tecnologia detectada

javascript/typescript, typescript, javascript

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `react-three-fiber`
- `gsap`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con react-three-fiber, gsap cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si renderizas 3D en web y quieres control a bajo nivel. No debe instalarse por inercia.
