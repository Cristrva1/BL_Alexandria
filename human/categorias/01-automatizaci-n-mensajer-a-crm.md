[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Automatizar procesos y crear herramientas internas

Motores de flujos, ecosistema n8n y aplicaciones internas. Elige el motor del proceso y conecta después sus fuentes de datos, canales y modelos.

15 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [n8n](../fichas/n8n.md) | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. | API de IA opcional |
| [Self-hosted AI Starter Kit](../fichas/self-hosted-ai-starter-kit.md) | Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos. | Sin clave propia de API de IA en la ruta básica |
| [NocoDB](../fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Motores de workflow y automatización](#motores-de-workflow-y-automatización) — 7 repos
- [Ecosistema n8n](#ecosistema-n8n) — 4 repos
- [Apps internas y bases de datos no-code](#apps-internas-y-bases-de-datos-no-code) — 4 repos

## Motores de workflow y automatización

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [n8n](../fichas/n8n.md) | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. | Tu objetivo encaja con estos ejemplos: Un formulario de contacto genera un registro para seguimiento comercial; Un flujo resume documentos con Ollama en lugar de una API remota | API de IA opcional |
| [huginn](../fichas/huginn.md) | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". | Tu objetivo encaja con estos ejemplos: Vigilar novedades de un sitio que publica una fuente RSS; Transformar un webhook entrante en un evento para otros agentes | Sin clave propia de API de IA en la ruta básica |
| [Kestra](../fichas/kestra.md) | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. | Tu objetivo encaja con estos ejemplos: Programar una importación diaria de archivos con reintentos; Combinar tareas de datos con una consulta a un modelo Ollama | API de IA opcional |
| [activepieces](../fichas/activepieces.md) | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. | Tu objetivo encaja con estos ejemplos: Pasar respuestas de un formulario a una aplicación de negocio; Solicitar aprobación humana antes de continuar una automatización | API de IA opcional |
| [Node-RED](../fichas/node-red.md) | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. | Tu objetivo encaja con estos ejemplos: Mostrar lecturas de un sensor recibidas por MQTT; Convertir un webhook en una secuencia de acciones | Sin clave propia de API de IA en la ruta básica |
| [Windmill](../fichas/windmill.md) | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. | Tu objetivo encaja con estos ejemplos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente | API de IA opcional |
| [Trigger.dev](../fichas/trigger-dev.md) | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. | Tu objetivo encaja con estos ejemplos: Procesar en segundo plano un archivo subido por un usuario; Reintentar una tarea de generación cuando falla el proveedor | API de IA opcional |

## Ecosistema n8n

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Self-hosted AI Starter Kit](../fichas/self-hosted-ai-starter-kit.md) | Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos. | Tu objetivo encaja con estos ejemplos: Probar un asistente local que responde preguntas sobre material de ejemplo; Explorar cómo se conectan n8n, Ollama y una base vectorial | Sin clave propia de API de IA en la ruta básica |
| [Awesome n8n Templates](../fichas/awesome-n8n-templates.md) | Colección de plantillas de n8n para estudiar o importar automatizaciones de servicios y tareas habituales. | Tu objetivo encaja con estos ejemplos: Estudiar una plantilla que clasifica correo con Ollama; Adaptar una alerta de precio que avisa por Telegram | Depende de la ruta elegida |
| [n8n-mcp](../fichas/n8n-mcp.md) | Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. | Tu objetivo encaja con estos ejemplos: Investigar por qué falló una ejecución de un flujo propio; Preparar y validar un flujo de prueba con ayuda del agente | Sin clave propia de API de IA en la ruta básica |
| [n8n-skills](../fichas/n8n-skills.md) | Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas. | Tu objetivo encaja con estos ejemplos: Corregir una expresión que no encuentra un campo de entrada; Elegir nodos y validar un flujo antes de activarlo | Sin clave propia de API de IA en la ruta básica |

## Apps internas y bases de datos no-code

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [NocoDB](../fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | Tu objetivo encaja con estos ejemplos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular | Sin clave propia de API de IA en la ruta básica |
| [Appsmith](../fichas/appsmith.md) | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. | Tu objetivo encaja con estos ejemplos: Preparar un panel para que soporte consulte expedientes; Construir un formulario interno que actualiza datos mediante una API | API de IA opcional |
| [ToolJet](../fichas/tooljet.md) | Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. | Tu objetivo encaja con estos ejemplos: Crear un panel interno para consultar pedidos y su estado; Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP | API de IA opcional |
| [Budibase](../fichas/budibase.md) | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. | Tu objetivo encaja con estos ejemplos: Registrar solicitudes internas y seguir su estado; Montar un proceso que combina formulario, automatización y agente de IA | API de IA opcional |

## Recetas relacionadas

- [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md) — Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
