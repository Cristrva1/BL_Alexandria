# playwright

Generado: 2026-06-26T07:47:33.067156+00:00

## Decision

REFERENCIA

## Para que sirve realmente

Playwright is a framework for web automation and testing. It drives Chromium, Firefox, and WebKit with a single API — in your tests, in your scripts, and as a tool for AI agents.

## Que problema resuelve

necesitas control preciso y reproducible del browser

## Por que tiene valor

Aporta valor en `runtime` para automation, javascript, javascript-typescript, postgres, python, typescript. Stack declarado: javascript/typescript, python, typescript, javascript, postgres.

## Cuando usarlo

necesitas control preciso y reproducible del browser

## Cuando NO usarlo

quieres que el agente navegue por visión ([browser-use](#-browser-use)) o no necesitas un navegador real.

## Tipo de instalacion

reference_only

## Stack / tecnologia detectada

javascript/typescript, python, typescript, javascript, postgres

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `browser-use`
- `crawlee`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con browser-use, crawlee cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si necesitas control preciso y reproducible del browser. No debe instalarse por inercia.
