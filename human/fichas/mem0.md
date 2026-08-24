# mem0

Generado: 2026-08-24T04:31:34.499362+00:00

## Decision

REFERENCIA

## Para que sirve realmente

mem0 guarda y recupera hechos de usuario entre sesiones. Úsalo cuando el agente necesita memoria a largo plazo, no como base de datos general.

## Que problema resuelve

quieres memoria estándar lista con integraciones amplias

## Por que tiene valor

Aporta valor en `library` para docker, javascript, postgres, python, typescript. Stack declarado: python, typescript, javascript, docker, postgres.

## Cuando usarlo

quieres memoria estándar lista con integraciones amplias

## Cuando NO usarlo

necesitas todo local sin llamadas a API ([mempalace](#-mempalace)) o control total del almacenamiento.

## Tipo de instalacion

reference_only

## Stack / tecnologia detectada

python, typescript, javascript, docker, postgres

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `crewai`
- `langchain`
- `agentmemory`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con crewai, langchain, agentmemory cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si quieres memoria estándar lista con integraciones amplias. No debe instalarse por inercia.
