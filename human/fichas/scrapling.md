# Scrapling

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.

## Que problema resuelve

los sitios cambian o te bloquean

## Por que tiene valor

Aporta valor en `library` para scraping. Stack declarado: Python.

## Cuando usarlo

los sitios cambian o te bloquean

## Cuando NO usarlo

el target es estable y simple.

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `scrapy`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con scrapy cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si los sitios cambian o te bloquean. No debe instalarse por inercia.
