# Bot de WhatsApp con IA

Generado: 2026-06-23T16:56:54.761958+00:00

## Objetivo

atención/ventas automatizada por WhatsApp con un agente LLM.

## Stack sugerido

- `evolution-api`: API REST robusta que actúa como middleware para automatizar WhatsApp y mensajería multicanal, exponiendo el envío/recepción de mensajes a tus aplicaciones.
- `n8n`: plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos.
- `n8n-mcp`: servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n para ayudar a construir y depurar flujos.
- `n8n-skills`: conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando errores al generar su JSON.
- `chatwoot`: plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada.
- `novu`: infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend.

## Como se conecta

evolution-api recibe/envía mensajes vía webhook; n8n enruta y llama al LLM; chatwoot centraliza cuando entra un agente humano.
