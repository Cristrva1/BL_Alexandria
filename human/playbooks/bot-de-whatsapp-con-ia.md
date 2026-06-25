# Bot de WhatsApp con IA

Generado: 2026-06-25T05:05:06.808623+00:00

## Objetivo

atención/ventas automatizada por WhatsApp con un agente LLM.

## Stack sugerido

- `evolution-api`: Open-source REST API for WhatsApp and multi-channel messaging — part of the Evolution Foundation ecosystem.
- `n8n`: n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments.
- `n8n-mcp`: A Model Context Protocol (MCP) server that provides AI assistants with comprehensive access to n8n node documentation, properties, and operations. Deploy in minutes to give Claude and other AI assistants deep knowledge about n8n's 1,845 workflow automation nodes (816 core + 1,029 community).
- `n8n-skills`: Expert Claude Code skills for building flawless n8n workflows using the n8n-mcp MCP server**.
- `chatwoot`: The modern customer support platform, an open-source alternative to Intercom, Zendesk, Salesforce Service Cloud etc.
- `novu`: The open-source communication infrastructure for agents and products.

## Como se conecta

evolution-api recibe/envía mensajes vía webhook; n8n enruta y llama al LLM; chatwoot centraliza cuando entra un agente humano.
