# 18. CRM, ventas y marketing — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `chatwoot`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=automation,crm,ruby,docker

**Qué es:** Reúne WhatsApp, email, web chat y redes en una sola bandeja, con paso a un humano cuando el bot no basta. Alternativa abierta a Intercom o Zendesk.
**Stack:** Ruby on Rails, Vue.js, PostgreSQL, Redis, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/chatwoot/chatwoot

**Instalación** [?]: `Seguir la instalación original: https://github.com/chatwoot/chatwoot/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** das soporte por varios canales y necesitas handoff humano
**Evita si:** solo necesitas enviar mensajes salientes (evolution-api)
**Combina con:** `evolution-api`, `novu`

## `cloud-mail`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=marketing,server,javascript

**Qué es:** Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/maillab/cloud-mail

**Instalación** [?]: `Seguir la instalación original: https://github.com/maillab/cloud-mail/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `compai-crm`
role=platform · exec=cloud · setup=heavy · mcp=False · prov=— · tags=crm,typescript

**Qué es:** CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia. Un agente trabaja sobre una cola y un presupuesto de investigación y mantiene la información del CRM.
**Stack:** TypeScript, Docker, Node.js
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. El README permite prescindir de fuentes externas de investigación. Confirmar por separado el agente y proveedor que ejecutará las tareas.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/trycompai/crm

**Instalación** [?]: `Seguir la instalación original: https://github.com/trycompai/crm/blob/release/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar un CRM donde el agente organiza el seguimiento
**Evita si:** solo necesitas una integración sencilla sin operar una plataforma

## `erpnext`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=crm,python

**Qué es:** Cubre la operación completa de una empresa sin licencias de pago. Muy usado por pymes y en manufactura y distribución.
**Stack:** Python, Frappe, MariaDB, JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/frappe/erpnext

**Instalación** [?]: `Seguir la instalación original: https://github.com/frappe/erpnext/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un ERP completo y totalmente libre
**Evita si:** buscas el mayor ecosistema de módulos; mira `odoo`
**Combina con:** `n8n`, `metabase`
**Alternativas (elige una):** `odoo`

## `listmonk`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,email,go,docker

**Qué es:** Envía newsletters y campañas a miles de suscriptores desde un solo binario ligero que consume muy pocos recursos.
**Stack:** Go, PostgreSQL, self-host
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/knadh/listmonk

**Instalación** [?]: `Seguir la instalación original: https://github.com/knadh/listmonk/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres email marketing simple, rápido y propio
**Evita si:** necesitas nurturing avanzado o scoring de leads (mautic)
**Combina con:** `mautic`, `n8n`

## `mautic`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=automation,email,php

**Qué es:** Nutre leads por email con reglas y segmentos automáticos, sin ceder los datos de tus clientes a un SaaS.
**Stack:** PHP/Symfony, MySQL, self-host
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mautic/mautic

**Instalación** [?]: `Seguir la instalación original: https://github.com/mautic/mautic/blob/7.x/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas automatización de marketing seria y soberana
**Evita si:** te basta una newsletter simple (listmonk)
**Combina con:** `listmonk`, `marketingskills`

## `novu`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,email,typescript

**Qué es:** Envía notificaciones por email, SMS, push y chat desde una sola API, sin integrar y mantener cada proveedor por separado.
**Stack:** Node.js, TypeScript, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/novuhq/novu

**Instalación** [?]: `Seguir la instalación original: https://github.com/novuhq/novu/blob/next/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** envías notificaciones por varios canales y quieres un único backend
**Evita si:** solo necesitas email (listmonk)
**Combina con:** `chatwoot`, `activepieces`

## `odoo`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=crm,python,postgres

**Qué es:** Integra CRM, ventas, facturación, inventario, RR. HH. y sitio web en una sola plataforma modular. La usan pymes y grandes empresas en todo el mundo.
**Stack:** Python, PostgreSQL, JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/odoo/odoo

**Instalación** [?]: `Seguir la instalación original: https://github.com/odoo/odoo/blob/20.0/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas un ERP completo con CRM integrado
**Evita si:** solo quieres un CRM ligero; mira `twenty-main`
**Combina con:** `n8n`, `metabase`
**Alternativas (elige una):** `erpnext`

## `open-seo`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=marketing,server,typescript

**Qué es:** Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio.
**Stack:** TypeScript, compose.yaml, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función principal conecta servicios externos; sus claves no equivalen necesariamente a una API de un modelo de lenguaje.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. OpenSEO autoalojado necesita una clave de DataForSEO y su consumo se paga al proveedor. La modalidad alojada tiene condiciones propias.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/every-app/open-seo

**Instalación** [?]: `Seguir la instalación original: https://github.com/every-app/open-seo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `postiz-app`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=marketing,server,typescript

**Qué es:** Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/gitroomhq/postiz-app

**Instalación** [?]: `Seguir la instalación original: https://github.com/gitroomhq/postiz-app/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `sellbird`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=marketing,agent,python

**Qué es:** Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes.
**Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El README documenta usar una cuenta o sesión del agente, además de las otras rutas que admita el producto.
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. El razonamiento usa tu plan de Claude Code o Codex; correo, búsqueda de contactos, verificación de direcciones y otros servicios tienen requisitos y posibles tarifas propios.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ethanplusai/sellbird

**Instalación** [?]: `Seguir la instalación original: https://github.com/ethanplusai/sellbird/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `twenty-main`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=automation,crm,typescript,docker

**Qué es:** La premisa es tratar el CRM como una pieza más de tu stack: lo construyes, lo despliegas y lo versionas igual que el código.
**Stack:** TypeScript, React, NestJS, PostgreSQL, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/twentyhq/twenty

**Instalación** [?]: `Seguir la instalación original: https://github.com/twentyhq/twenty/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un CRM que se adapte 1:1 a tu negocio y vivir en self-host
**Evita si:** buscas algo plug-and-play gestionado o no quieres operar PostgreSQL y Docker
**Combina con:** `evolution-api`, `n8n`
