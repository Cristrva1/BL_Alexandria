# open-design

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

editor/workspace de diseño colaborativo asistido por IA que genera, maqueta y anima interfaces a partir de instrucciones en lenguaje natural; alternativa libre a Claude Design Artifacts.

## Que problema resuelve

generas UI desde texto

## Por que tiene valor

Aporta valor en `app` para ui. Stack declarado: TypeScript/React, Tauri (Rust).

## Cuando usarlo

generas UI desde texto

## Cuando NO usarlo

prefieres editar sobre tu código ([plasmic](#-plasmic)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `tailwindcss`
- `heroui`

## Contra que compite

- `plasmic`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con tailwindcss, heroui cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si generas UI desde texto. No debe instalarse por inercia.
