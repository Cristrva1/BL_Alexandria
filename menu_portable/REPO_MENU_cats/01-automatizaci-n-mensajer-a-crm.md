# 1. Automatización, Mensajería & CRM — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `activepieces`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** href="https://activepieces.com".
**Stack:** javascript/typescript, typescript, javascript, docker
**Repo:** https://github.com/activepieces/activepieces.git

**Instalación** [~]: `git clone https://github.com/activepieces/activepieces.git && cd activepieces && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres target="_blank"
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `appsmith`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Organizations build custom applications like dashboards, admin panels, customer 360, IT automation, and service management tools to help their teams work more efficiently and effectively. Appsmith is an open-source low-code platform that streamlines custom application development, deployment, and maintenance. Learn more on our [website](https://www.appsmith.com?utm_source=github&utm_medium=organic
**Stack:** typescript, javascript, docker, postgres
**Repo:** https://github.com/appsmithorg/appsmith.git

**Instalación** [~]: `git clone https://github.com/appsmithorg/appsmith.git && cd appsmith && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `browser-use`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** 🌤️ Want to skip the setup? Use our cloud for faster, scalable, stealth-enabled browser automation!.
**Stack:** python, typescript, docker
**Repo:** https://github.com/browser-use/browser-use.git

**Instalación** [~]: `git clone https://github.com/browser-use/browser-use.git && cd browser-use && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `budibase`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** AI Agents that run your operations Budibase is an open-source operations platform that saves engineers 100s of hours building Agents, Apps and Automations, securely.
**Stack:** javascript/typescript, typescript, javascript, docker, postgres
**Repo:** https://github.com/Budibase/budibase.git

**Instalación** [~]: `git clone https://github.com/Budibase/budibase.git && cd budibase && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `chatwoot`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** The modern customer support platform, an open-source alternative to Intercom, Zendesk, Salesforce Service Cloud etc.
**Stack:** javascript/typescript, typescript, javascript, docker
**Repo:** https://github.com/chatwoot/chatwoot.git

**Instalación** [~]: `npm install chatwoot   (o: pnpm add chatwoot)`
_Nombre npm puede diferir de 'chatwoot'; verifica en npmjs.com._

**Elige si:** quieres ___
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `evolution-api`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Open-source REST API for WhatsApp and multi-channel messaging — part of the Evolution Foundation ecosystem.
**Stack:** javascript/typescript, typescript, javascript, docker, postgres
**Repo:** https://github.com/evolution-foundation/evolution-api.git

**Instalación** [~]: `git clone https://github.com/evolution-foundation/evolution-api.git && cd evolution-api && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres open-source rest api for whatsapp and multi-channel messaging — part of the evol
**Evita si:** —
**Combina con:** `twenty-main`, `whatsapp-agentkit`, `activepieces`

## `huginn`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Huginn is a system for building agents that perform automated tasks for you online. They can read the web, watch for events, and take actions on your behalf. Huginn's Agents create and consume events, propagating them along a directed graph. Think of it as a hackable version of IFTTT or Zapier on your own server. You always know who has your data. You do.
**Stack:** javascript/typescript, typescript, javascript, docker, postgres
**Repo:** https://github.com/huginn/huginn.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/huginn/). Si necesitas el código: git clone https://github.com/huginn/huginn.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres what is huginn?
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `listmonk`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** listmonk is a standalone, self-hosted, newsletter and mailing list manager. It is fast, feature-rich, and packed into a single binary. It uses a PostgreSQL database as its data store.
**Stack:** typescript, docker, postgres
**Repo:** https://github.com/knadh/listmonk.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/listmonk/). Si necesitas el código: git clone https://github.com/knadh/listmonk.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres listmonk is a standalone, self-hosted, newsletter and mailing list manager. it i
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `mautic`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Open Source Marketing Automation Software.
**Stack:** javascript/typescript, python, typescript, javascript, postgres
**Repo:** https://github.com/mautic/mautic.git

**Instalación** [~]: `git clone https://github.com/mautic/mautic.git && cd mautic && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres open source marketing automation software.
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `n8n`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments.
**Stack:** javascript/typescript, python, typescript, javascript, docker, langchain
**Repo:** https://github.com/n8n-io/n8n.git

**Instalación** [~]: `git clone https://github.com/n8n-io/n8n.git && cd n8n && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres n8n - secure workflow automation for technical teams
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `n8n-io`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments.
**Stack:** javascript/typescript, python, typescript, javascript, docker, langchain
**Repo:** https://github.com/n8n-io/n8n.git

**Instalación** [~]: `git clone https://github.com/n8n-io/n8n.git && cd n8n && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres n8n - secure workflow automation for technical teams
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `n8n-mcp`
role=platform · exec=local · setup=medium · mcp=True · prov=—

**Qué es:** A Model Context Protocol (MCP) server that provides AI assistants with comprehensive access to n8n node documentation, properties, and operations. Deploy in minutes to give Claude and other AI assistants deep knowledge about n8n's 1,845 workflow automation nodes (816 core + 1,029 community).
**Stack:** javascript/typescript, python, typescript, javascript, docker, langchain
**Repo:** https://github.com/czlonkowski/n8n-mcp.git

**Instalación** [~]: `git clone https://github.com/czlonkowski/n8n-mcp.git && cd n8n-mcp && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `novu`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** The open-source communication infrastructure for agents and products.
**Stack:** javascript/typescript, typescript, javascript, react
**Repo:** https://github.com/novuhq/novu.git

**Instalación** [~]: `npm install novu   (o: pnpm add novu)`
_Nombre npm puede diferir de 'novu'; verifica en npmjs.com._

**Elige si:** quieres >
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `openevolve`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** 🧬 The most advanced open-source evolutionary coding agent**.
**Stack:** python, typescript, docker
**Repo:** https://github.com/algorithmicsuperintelligence/openevolve.git

**Instalación** [~]: `pip install openevolve   (o: uv add openevolve)`
_Nombre PyPI puede diferir de 'openevolve'; verifica en pypi.org._

**Elige si:** —
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `whatsapp-agentkit`

## `twenty-main`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Twenty gives technical teams the building blocks for a custom CRM that meets complex business needs and quickly adapts as the business evolves. Twenty is the CRM you build, ship, and version like the rest of your stack.
**Stack:** javascript/typescript, typescript, javascript, react, docker, postgres
**Repo:** —

**Instalación** [~]: `git clone <twenty-main> && cd twenty-main && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres why twenty
**Evita si:** —
**Combina con:** `evolution-api`, `whatsapp-agentkit`, `activepieces`

## `whatsapp-agentkit`
role=directory · exec=cloud · setup=medium · mcp=False · prov=—

**Qué es:** Construye tu propio agente de WhatsApp con inteligencia artificial en menos de 30 minutos. No necesitas saber programar. Claude Code construye todo por ti.
**Stack:** python, typescript, javascript, docker, postgres, fastapi
**Repo:** https://github.com/Hainrixz/whatsapp-agentkit.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/whatsapp-agentkit/). Si necesitas el código: git clone https://github.com/Hainrixz/whatsapp-agentkit.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres agentkit — whatsapp ai agent builder
**Evita si:** —
**Combina con:** `twenty-main`, `evolution-api`, `activepieces`
