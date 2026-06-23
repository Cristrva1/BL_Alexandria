# novu

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

REFERENCIA

## Para que sirve realmente

infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend.

## Que problema resuelve

envías notificaciones por varios canales

## Por que tiene valor

Aporta valor en `platform` para automation, email, notifications. Stack declarado: Node.js, TypeScript, Docker.

## Cuando usarlo

envías notificaciones por varios canales

## Cuando NO usarlo

solo necesitas email ([listmonk](#-listmonk)).

## Tipo de instalacion

reference_only

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `chatwoot`
- `activepieces`

## Contra que compite

- `listmonk`

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con chatwoot, activepieces cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si envías notificaciones por varios canales. No debe instalarse por inercia.
