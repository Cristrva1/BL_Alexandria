# 1. Automatizar negocios y comunicación — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `activepieces`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,typescript,docker

**Qué es:** Orquesta tus apps con flujos visuales sin código y conserva el control al alojarlo en tu servidor.
**Stack:** Node.js, TypeScript, self-host/web
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/activepieces/activepieces

**Instalación** [?]: `Seguir la instalación original: https://github.com/activepieces/activepieces/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres reemplazar Zapier con piezas propias en TypeScript
**Evita si:** ya dominas n8n y su ecosistema te basta
**Combina con:** `novu`
**Alternativas (elige una):** `n8n`

## `appsmith`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=ui,automation,typescript,docker

**Qué es:** Arrastra widgets, conéctalos a más de 25 bases de datos o cualquier API y añade lógica en JavaScript. Pensada para equipos que construyen backoffices rápido.
**Stack:** TypeScript, React, Java, MongoDB, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/appsmithorg/appsmith

**Instalación** [?]: `Seguir la instalación original: https://github.com/appsmithorg/appsmith/blob/release/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas herramientas internas con lógica y muchas fuentes de datos
**Evita si:** solo quieres hojas colaborativas; mira `nocodb`
**Combina con:** `n8n`
**Alternativas (elige una):** `tooljet`, `budibase`, `nocodb`

## `awesome-n8n-templates`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=automation,prompts

**Qué es:** Colección de plantillas de n8n para estudiar o importar automatizaciones de servicios y tareas habituales. Cada workflow tiene dependencias y posibles consumos externos que debes revisar antes de activarlo.
**Stack:** JSON de n8n
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/enescingoz/awesome-n8n-templates

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** usas n8n y quieres partir de flujos hechos
**Evita si:** no usas n8n
**Combina con:** `n8n`, `n8n-mcp`, `n8n-skills`

## `baileys`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=whatsapp,chatbot,typescript

**Qué es:** Implementa el protocolo de WhatsApp Web directamente, así que consume muy pocos recursos. Es la base de muchas APIs de WhatsApp, incluida Evolution API.
**Stack:** TypeScript, Node.js, WebSocket
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/WhiskeySockets/Baileys

**Instalación** [?]: `Seguir la instalación original: https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas WhatsApp en código con bajo consumo de recursos
**Evita si:** prefieres una API REST lista; mira `evolution-api`
**Combina con:** `evolution-api`, `n8n`
**Alternativas (elige una):** `whatsapp-web-js`, `waha`

## `botpress`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=chatbot,agents,typescript

**Qué es:** Combina un estudio visual con código para crear agentes que usan bases de conocimiento, herramientas y canales. Su producto principal hoy es cloud; el repo contiene SDK, integraciones y CLI.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/botpress/botpress

**Instalación** [?]: `Seguir la instalación original: https://github.com/botpress/botpress/blob/master/readme.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un agente conversacional multicanal con poco código
**Evita si:** necesitas todo self-host y sin nube; mira `rasa` o `typebot`
**Combina con:** `chatwoot`, `n8n`
**Alternativas (elige una):** `typebot`, `rasa`

## `budibase`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,agents,docker

**Qué es:** Genera apps CRUD, formularios y flujos a partir de bases existentes y ahora añade agentes de IA agnósticos de modelo. Pensada para equipos de operaciones.
**Stack:** TypeScript, Svelte, Node.js, CouchDB, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Budibase/budibase

**Instalación** [?]: `Seguir la instalación original: https://github.com/Budibase/budibase/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres apps internas y agentes en una sola plataforma self-host
**Evita si:** buscas el editor más flexible para backoffices; mira `appsmith`
**Combina con:** `n8n`
**Alternativas (elige una):** `appsmith`, `tooljet`, `nocodb`

## `cal.diy`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=motores,next-auth,nextjs,open-source,postgresql,prisma,t3-stack,tailwindcss

**Qué es:** Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia. Despliega la aplicación de calendario y configura base de datos, disponibilidad e integraciones.
**Stack:** TypeScript, Docker, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/calcom/cal.diy

**Instalación** [?]: `Seguir la instalación original: https://github.com/calcom/cal.diy/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar una agenda autoalojada para uso personal
**Evita si:** solo necesitas una integración sencilla sin operar una plataforma

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

## `evolution-api`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=automation,whatsapp,typescript,docker

**Qué es:** Conecta WhatsApp a tu stack mediante una API REST propia, sin quedar atado a un proveedor cerrado.
**Stack:** Node.js/TypeScript, Fastify, Redis, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/evolution-foundation/evolution-api

**Instalación** [?]: `Seguir la instalación original: https://github.com/evolution-foundation/evolution-api/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** operas WhatsApp en producción con varias instancias
**Evita si:** solo necesitas un bot de prueba o un único script (OpenWA basta)
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `whatsapp-web-js`, `waha`

## `fluxer`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=whatsapp,chatbot,typescript

**Qué es:** Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio. Organiza canales y comunicación de grupos; no es un generador de audio o video.
**Stack:** web/TS
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/fluxerapp/fluxer

**Instalación** [?]: `Seguir la instalación original: https://github.com/fluxerapp/fluxer/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres probar algo nuevo y seguir su evolución
**Evita si:** necesitas estabilidad de producción (API aún en finalización)
**Combina con:** `open-generative-ai`

## `huginn`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,ruby,docker

**Qué es:** Vigila webs, feeds y APIs y dispara acciones cuando algo cambia, todo alojado por ti y sin depender de terceros.
**Stack:** Ruby on Rails, MySQL/PostgreSQL, self-host
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/huginn/huginn

**Instalación** [?]: `Seguir la instalación original: https://github.com/huginn/huginn/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** automatizas tareas orientadas a eventos y valoras la privacidad
**Evita si:** quieres editor visual moderno o IA nativa (n8n)
**Combina con:** `novu`
**Alternativas (elige una):** `n8n`, `node-red`

## `kestra`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,data,java,docker

**Qué es:** Define flujos en YAML con un editor web, cientos de plugins y disparadores por calendario o eventos. Pensado para equipos de datos y plataforma que quieren orquestación como código.
**Stack:** Java, Vue, YAML, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/kestra-io/kestra

**Instalación** [?]: `Seguir la instalación original: https://github.com/kestra-io/kestra/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres workflows declarativos en YAML con UI y control de versiones
**Evita si:** buscas automatizaciones de negocio con nodos visuales; mira `n8n`
**Combina con:** `duckdb`, `superset`
**Alternativas (elige una):** `windmill`, `trigger-dev`

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

## `n8n`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,typescript,docker

**Qué es:** Conecta cualquier app con cualquier otra en tu propio servidor, sin pagar una suscripción mensual por cada flujo.
**Stack:** Node.js, TypeScript, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/n8n-io/n8n

**Instalación** [?]: `Seguir la instalación original: https://github.com/n8n-io/n8n/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres el motor central de automatización con máximo catálogo
**Evita si:** buscas algo minimalista o sin self-host
**Combina con:** `n8n-mcp`, `n8n-skills`, `evolution-api`
**Alternativas (elige una):** `activepieces`, `huginn`, `windmill`, `node-red`

## `n8n-io`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,typescript,docker

**Qué es:** No aporta nada distinto a la ficha principal.
**Stack:** Node.js, TypeScript
**Acceso y costes:**
- API de IA: API: por confirmar. No se ha verificado si la ruta elegida necesita una API de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Ejecución con modelos locales por confirmar. Ejecutar el programa en tu equipo no demuestra que el modelo también sea local.
- Coste: Coste por confirmar. Código disponible no significa servicios, modelos, infraestructura o licencias sin coste.
- Equipo: Requisitos por confirmar. Consultar los requisitos originales de la variante que vayas a usar.
**Repo:** https://github.com/n8n-io/n8n

**Instalación** [?]: `Seguir la instalación original: https://github.com/n8n-io/n8n`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** — **Evita si:** ya usas la ficha n8n (es el mismo proyecto)
**Evita si:** ya usas la ficha n8n (es el mismo proyecto)
**Combina con:** `n8n`

## `n8n-mcp`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,mcp,typescript

**Qué es:** Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. El cliente MCP y la instancia de n8n conservan sus propios requisitos de acceso.
**Stack:** Node.js/TypeScript, MCP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.
- Coste: Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/czlonkowski/n8n-mcp

**Instalación** [?]: `Seguir la instalación original: https://github.com/czlonkowski/n8n-mcp/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** generas flujos n8n con IA y quieres menos alucinaciones de parámetros
**Evita si:** no usas n8n o construyes los flujos a mano
**Combina con:** `n8n`, `n8n-skills`

## `n8n-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,automation

**Qué es:** Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas. La skill no sustituye la instancia de n8n ni las credenciales de los servicios de un workflow.
**Stack:** `SKILL.md`, Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/czlonkowski/n8n-skills

**Instalación** [?]: `Seguir la instalación original: https://github.com/czlonkowski/n8n-skills/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** generas workflows n8n con IA y te cansan los fallos de JSON
**Evita si:** no usas n8n
**Combina con:** `n8n`, `n8n-mcp`

## `nocodb`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=data,automation,docker

**Qué es:** Ofrece vistas de tabla, kanban, galería y formularios sobre PostgreSQL, MySQL o SQLite, con API REST automática. Útil como backoffice rápido para equipos no técnicos.
**Stack:** TypeScript, Vue, Node.js, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/nocodb/nocodb

**Instalación** [?]: `Seguir la instalación original: https://github.com/nocodb/nocodb/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un Airtable propio sobre tu base de datos
**Evita si:** necesitas apps internas con lógica compleja; mira `appsmith`
**Combina con:** `n8n`
**Alternativas (elige una):** `appsmith`, `budibase`

## `node-red`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=automation,javascript,docker

**Qué es:** Conecta dispositivos, APIs y servicios arrastrando nodos en el navegador. Es muy usado en IoT, domótica e industria por su ligereza y su enorme biblioteca de nodos de la comunidad.
**Stack:** JavaScript, Node.js, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/node-red/node-red

**Instalación** [?]: `Seguir la instalación original: https://github.com/node-red/node-red/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** trabajas con IoT o eventos y quieres algo ligero y probado
**Evita si:** necesitas integraciones SaaS y nodos de IA listos; mira `n8n`
**Alternativas (elige una):** `n8n`, `huginn`

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

## `openwa`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=whatsapp,chatbot,typescript

**Qué es:** Envía y recibe mensajes de WhatsApp desde tu propio script con una API sencilla y expresiva.
**Stack:** Node.js, Puppeteer, bindings Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/rmyndharis/OpenWA

**Instalación** [?]: `Seguir la instalación original: https://github.com/rmyndharis/OpenWA/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** desarrollas scripts o bots individuales y quieres arrancar rápido
**Evita si:** necesitas infra multi-instancia o alta disponibilidad (evolution-api)
**Combina con:** `n8n`, `evolution-api`

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

## `rasa`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=chatbot,agents,python

**Qué es:** Permite crear asistentes de texto y voz con control total del diálogo y de los datos. Muy usado en empresas que necesitan bots on-premise y predecibles.
**Stack:** Python, TensorFlow, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/RasaHQ/rasa

**Instalación** [?]: `Seguir la instalación original: https://github.com/RasaHQ/rasa/blob/3.6.x/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas un asistente on-premise con diálogo muy controlado
**Evita si:** quieres algo rápido con LLM y sin entrenar; mira `botpress` o `typebot`
**Combina con:** `chatwoot`
**Alternativas (elige una):** `botpress`

## `self-hosted-ai-starter-kit`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,local,rag,docker

**Qué es:** Kit oficial de n8n que levanta un entorno de IA privado: n8n para orquestar, Ollama para modelos, Qdrant como base vectorial y PostgreSQL. Útil para prototipar agentes y RAG sin enviar datos fuera.
**Stack:** Docker Compose, n8n, Ollama, Qdrant, PostgreSQL
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. La receta incluye Ollama y servicios locales. Las integraciones añadidas a n8n pueden introducir cuentas o APIs externas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/n8n-io/self-hosted-ai-starter-kit

**Instalación** [?]: `Seguir la instalación original: https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un stack de IA local funcionando hoy con n8n
**Evita si:** vas a producción con alta carga; arma tu propio despliegue
**Combina con:** `n8n`, `ollama`, `qdrant`

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

## `tooljet`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=ui,automation,docker

**Qué es:** Construye apps internas arrastrando componentes y conectando bases y APIs, o genéralas describiéndolas con IA. Pensada para equipos de operaciones y TI.
**Stack:** TypeScript, React, Node.js, PostgreSQL
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ToolJet/ToolJet

**Instalación** [?]: `Seguir la instalación original: https://github.com/ToolJet/ToolJet/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres herramientas internas con IA para generarlas
**Evita si:** prefieres un proyecto con licencia más permisiva; mira `appsmith`
**Combina con:** `n8n`
**Alternativas (elige una):** `appsmith`, `budibase`

## `trigger-dev`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,agents,typescript

**Qué es:** Escribe tareas largas o con reintentos en TypeScript dentro de tu app y Trigger.dev las ejecuta, reintenta y monitorea. Ideal para equipos de producto con Next.js o Node que no quieren operar colas.
**Stack:** TypeScript, Node.js, PostgreSQL, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/triggerdotdev/trigger.dev

**Instalación** [?]: `Seguir la instalación original: https://github.com/triggerdotdev/trigger.dev/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu app es TypeScript y necesitas tareas largas confiables sin montar colas
**Evita si:** quieres un editor visual para no programadores; mira `n8n`
**Combina con:** `vercel-ai`, `langfuse`
**Alternativas (elige una):** `windmill`, `kestra`

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

## `typebot`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=chatbot,automation,typescript

**Qué es:** Diseña conversaciones con bloques arrastrables (preguntas, condiciones, integraciones, IA) y publícalas en web o WhatsApp. Pensado para captar leads y formularios conversacionales.
**Stack:** TypeScript, Next.js, PostgreSQL, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/baptisteArno/typebot.io

**Instalación** [?]: `Seguir la instalación original: https://github.com/baptisteArno/typebot.io/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un chatbot guiado sin programar, con buena UX
**Evita si:** necesitas un agente abierto con razonamiento libre; mira `botpress`
**Combina con:** `n8n`, `evolution-api`
**Alternativas (elige una):** `botpress`

## `waha`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=whatsapp,automation,docker

**Qué es:** Expone WhatsApp como API HTTP con webhooks, lista para conectar a n8n o a tu backend. Ofrece motores basados en navegador o en WebSocket.
**Stack:** TypeScript, Go, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/devlikeapro/waha

**Instalación** [?]: `Seguir la instalación original: https://github.com/devlikeapro/waha/blob/core/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres una API REST de WhatsApp lista en minutos
**Evita si:** necesitas multi-instancia avanzada gratis; mira `evolution-api`
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `evolution-api`, `whatsapp-web-js`, `baileys`

## `whatsapp-agentkit`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,automation,python

**Qué es:** Arranca un bot de WhatsApp con IA sin escribir código, a partir de una plantilla guiada.
**Stack:** Node.js/Python, APIs de WhatsApp
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.
- Coste: Consumo de APIs o servicios. La plantilla pide una clave de Anthropic para el bot. Usar Claude Code para construirlo no sustituye la autenticación del bot.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Hainrixz/whatsapp-agentkit

**Instalación** [?]: `Seguir la instalación original: https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres arrancar sin partir de cero y te vale con lo que Claude Code genere
**Evita si:** necesitas control fino del stack o ya tienes el bot hecho
**Combina con:** `evolution-api`, `n8n-mcp`

## `whatsapp-web-js`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=whatsapp,chatbot,javascript

**Qué es:** Permite enviar y recibir mensajes, medios y grupos desde código usando una sesión de WhatsApp Web. Muy usada para bots y prototipos.
**Stack:** JavaScript, Node.js, Puppeteer
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/wwebjs/whatsapp-web.js

**Instalación** [+]: `npm install whatsapp-web.js`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres programar un bot de WhatsApp en Node rápido
**Evita si:** necesitas una API REST multi-sesión lista; mira `evolution-api` o `waha`
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `baileys`, `waha`, `evolution-api`

## `whatsmeow`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=whatsapp,go,golang,whatsapp-web

**Qué es:** Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web. Gestiona la sesión del cliente y permite enviar mensajes, recibir eventos y mantener el estado de la cuenta.
**Stack:** Go, Go modules
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/tulir/whatsmeow

**Instalación** [?]: `Seguir la instalación original: https://github.com/tulir/whatsmeow/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas integrar WhatsApp Web en un servicio escrito en Go
**Evita si:** solo necesitas una integración sencilla sin operar una plataforma
**Combina con:** `n8n`

## `windmill`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,agents,rust,docker

**Qué es:** Convierte scripts de Python, TypeScript, Go o SQL en workflows, endpoints y apps con UI generada. Sirve a equipos técnicos que quieren la flexibilidad del código con la comodidad de un orquestador visual.
**Stack:** Rust, TypeScript, Svelte, PostgreSQL, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/windmill-labs/windmill

**Instalación** [?]: `Seguir la instalación original: https://github.com/windmill-labs/windmill/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu equipo programa y quiere workflows versionados en código
**Evita si:** prefieres arrastrar nodos sin escribir código; mira `n8n`
**Combina con:** `langfuse`
**Alternativas (elige una):** `n8n`, `kestra`, `trigger-dev`
