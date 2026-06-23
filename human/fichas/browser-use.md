# browser-use

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

biblioteca que da a los LLMs la capacidad de usar navegadores reales con interfaz para modelos de visión, dejando que el agente perciba la pantalla y actúe sin selectores fijos.

## Que problema resuelve

quieres navegación como humano

## Por que tiene valor

Aporta valor en `library` para scraping, browser, agents, video. Stack declarado: Python 3.11+, Rust (core), Playwright.

## Cuando usarlo

quieres navegación como humano

## Cuando NO usarlo

necesitas scripts deterministas ([playwright](#-playwright)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `playwright`
- `gpt-researcher`

## Contra que compite

- `playwright`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con playwright, gpt-researcher cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si quieres navegación como humano. No debe instalarse por inercia.
