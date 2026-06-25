# 1. Automatización, Mensajería & CRM — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `activepieces`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=['openai', 'anthropic', 'mcp']

**Qué es:** plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y piezas reutilizables.
**Stack:** Node.js, TypeScript, self-host/web
**Repo:** https://github.com/activepieces/activepieces

**Instalación** [~]: `git clone https://github.com/activepieces/activepieces && cd activepieces && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres reemplazar Zapier con piezas propias
**Evita si:** ya dominas n8n.
**Combina con:** `n8n`, `novu`

## `appsmith`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Organizations build custom applications like dashboards, admin panels, customer 360, IT automation, and service management tools to help their teams work more efficiently and effectively. Appsmith is an open-source low-code platform that streamlines custom application development, deployment, and maintenance. Learn more on our [website](https://www.appsmith.com?utm_source=github&utm_medium=organic
**Stack:** typescript, docker, postgres
**Repo:** https://github.com/appsmithorg/appsmith.git

**Instalación** [~]: `git clone https://github.com/appsmithorg/appsmith.git && cd appsmith && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** —

## `budibase`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** AI Agents that run your operations Budibase is an open-source operations platform that saves engineers 100s of hours building Agents, Apps and Automations, securely.
**Stack:** javascript/typescript, typescript, javascript, docker, postgres
**Repo:** https://github.com/Budibase/budibase.git

**Instalación** [~]: `git clone https://github.com/Budibase/budibase.git && cd budibase && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** —

## `chatwoot`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada.
**Stack:** Ruby on Rails, Node.js, PostgreSQL, Redis, Docker
**Repo:** https://github.com/chatwoot/chatwoot

**Instalación** [~]: `git clone https://github.com/chatwoot/chatwoot && cd chatwoot && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** das soporte por varios canales
**Evita si:** solo necesitas enviar mensajes salientes.
**Combina con:** `evolution-api`, `novu`

## `evolution-api`
role=platform · exec=local · setup=heavy · mcp=False · prov=['openai']

**Qué es:** API REST robusta que actúa como middleware para automatizar WhatsApp y mensajería multicanal, exponiendo el envío/recepción de mensajes a tus aplicaciones.
**Stack:** Node.js/TypeScript, Fastify, Redis, Docker
**Repo:** https://github.com/EvolutionAPI/evolution-api

**Instalación** [~]: `git clone https://github.com/EvolutionAPI/evolution-api && cd evolution-api && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** operas WhatsApp en producción
**Evita si:** solo necesitas un bot de prueba.
**Combina con:** `n8n`, `chatwoot`

## `huginn`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú".
**Stack:** Ruby, Node.js, BD, self-host
**Repo:** https://github.com/huginn/huginn

**Instalación** [~]: `git clone https://github.com/huginn/huginn && cd huginn && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** automatizas tareas orientadas a eventos
**Evita si:** quieres editor visual amigable.
**Combina con:** `n8n`, `novu`

## `listmonk`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS.
**Stack:** Go, PostgreSQL, self-host
**Repo:** https://github.com/knadh/listmonk

**Instalación** [?]: `git clone https://github.com/knadh/listmonk (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres email marketing simple y propio
**Evita si:** necesitas nurturing avanzado ([mautic](#-mautic)).
**Combina con:** `mautic`, `n8n`
**Alternativas (elige una):** `mautic`

## `mautic`
role=platform · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo.
**Stack:** PHP, MySQL, self-host
**Repo:** https://github.com/mautic/mautic

**Instalación** [?]: `git clone https://github.com/mautic/mautic (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas automatización de marketing seria
**Evita si:** te basta una newsletter simple ([listmonk](#-listmonk)).
**Combina con:** `listmonk`, `marketingskills`
**Alternativas (elige una):** `listmonk`

## `n8n`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos.
**Stack:** Node.js, Docker
**Repo:** https://github.com/n8n-io/n8n

**Instalación** [~]: `git clone https://github.com/n8n-io/n8n && cd n8n && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres el motor central de automatización
**Evita si:** buscas algo minimalista.
**Combina con:** `n8n-mcp`, `n8n-skills`, `evolution-api`

## `n8n-io`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** copia local del repositorio oficial de n8n (mismo proyecto que [n8n](#-n8n)), mantenida como referencia o espejo del código fuente.
**Stack:** Node.js
**Repo:** https://github.com/n8n-io/n8n

**Instalación** [~]: `git clone https://github.com/n8n-io/n8n && cd n8n && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** —
**Evita si:** ya usas la ficha [n8n](#-n8n) (es el mismo proyecto).
**Combina con:** `n8n`
**Alternativas (elige una):** `n8n`

## `novu`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['anthropic']

**Qué es:** infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend.
**Stack:** Node.js, TypeScript, Docker
**Repo:** https://github.com/novuhq/novu

**Instalación** [~]: `git clone https://github.com/novuhq/novu && cd novu && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** envías notificaciones por varios canales
**Evita si:** solo necesitas email ([listmonk](#-listmonk)).
**Combina con:** `chatwoot`, `activepieces`
**Alternativas (elige una):** `listmonk`

## `openwa`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraestructura pesada.
**Stack:** Python, JavaScript/Node.js
**Repo:** https://github.com/open-wa/wa-automate-nodejs

**Instalación** [~]: `pip install openwa   (o: uv add openwa)`
_Nombre PyPI puede diferir de 'OpenWA'; verifica en pypi.org._

**Elige si:** desarrollas scripts independientes
**Evita si:** necesitas infra multi-instancia.
**Combina con:** `n8n`, `evolution-api`

## `twenty-main`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** CRM open-source orientado a desarrolladores, alternativa moderna y personalizable a Salesforce/HubSpot que modela tu negocio mediante objetos y campos propios.
**Stack:** TypeScript, React, NestJS, PostgreSQL, Docker
**Repo:** https://github.com/twentyhq/twenty

**Instalación** [~]: `git clone https://github.com/twentyhq/twenty && cd twenty && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres un CRM que se adapte 1:1 a tu negocio
**Evita si:** buscas algo plug-and-play sin self-host.
**Combina con:** `evolution-api`, `n8n`

## `whatsapp-agentkit`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de programar, partiendo de preguntas sobre tu negocio.
**Stack:** Node.js/Python, APIs de WhatsApp
**Repo:** https://github.com/Hainrixz/whatsapp-agentkit

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/whatsapp-agentkit/). Si necesitas el código: git clone https://github.com/Hainrixz/whatsapp-agentkit`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres arrancar sin partir de cero
**Evita si:** necesitas control fino del stack.
**Combina con:** `evolution-api`, `n8n-mcp`
