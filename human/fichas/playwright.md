# playwright

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.

## Que problema resuelve

necesitas control preciso del browser

## Por que tiene valor

Aporta valor en `library` para scraping, browser, automation. Stack declarado: Node.js o Python.

## Cuando usarlo

necesitas control preciso del browser

## Cuando NO usarlo

quieres que el agente navegue por visión ([browser-use](#-browser-use)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `browser-use`
- `crawlee`

## Contra que compite

- `browser-use`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con browser-use, crawlee cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si necesitas control preciso del browser. No debe instalarse por inercia.
