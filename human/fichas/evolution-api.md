# evolution-api

Generado: 2026-06-23T16:56:54.761958+00:00

## Decision

DIFERIR

## Para que sirve realmente

API REST robusta que actúa como middleware para automatizar WhatsApp y mensajería multicanal, exponiendo el envío/recepción de mensajes a tus aplicaciones.

## Que problema resuelve

operas WhatsApp en producción

## Por que tiene valor

Aporta valor en `platform` para automation, whatsapp. Stack declarado: Node.js/TypeScript, Fastify, Redis, Docker.

## Cuando usarlo

operas WhatsApp en producción

## Cuando NO usarlo

solo necesitas un bot de prueba.

## Tipo de instalacion

deferred

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `n8n`
- `chatwoot`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo alto de instalacion o mantenimiento; diferir hasta que sea finalista claro.

## Ideas profesionales

Combinar con n8n, chatwoot cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: diferir. Tiene sentido si operas WhatsApp en producción. No debe instalarse por inercia.
