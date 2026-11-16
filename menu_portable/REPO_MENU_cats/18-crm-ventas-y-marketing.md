# 18. CRM, ventas y marketing — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `cal.diy`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=motores,next-auth,nextjs,open-source,postgresql,prisma,t3-stack,tailwindcss

**Qué es:** Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia.
**Stack:** Node.js y Yarn según el proyecto;  PostgreSQL;  Docker para el entorno de desarrollo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere licencia Cal.com ni un LLM en la ruta comunitaria; servidor y correo siguen siendo gastos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El autor la recomienda para uso personal y no productivo. Se mueve de motores de workflows a agendas y reservas
- Coste: Sin pago a un modelo en la ruta básica. No requiere licencia Cal.com ni un LLM en la ruta comunitaria; servidor y correo siguen siendo gastos propios
- Equipo: Preparación según la ruta elegida. Node.js y Yarn según el proyecto;  PostgreSQL;  Docker para el entorno de desarrollo
**Repo:** https://github.com/calcom/cal.diy

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/calcom/cal.diy/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Experimentar con una agenda personal autoalojada; Probar la duración y disponibilidad de distintos tipos de cita
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un evento personal de prueba y abre su página de reserva
**Qué comprobar:** Puedes elegir una franja disponible y revisar la reserva creada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `twenty-main`, `botpress`

## `chatwoot`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=automation,crm,ruby,docker

**Qué es:** Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada.
**Stack:** Cuenta o servidor; canal de prueba; proveedor solo para funciones AI
**Acceso y costes:**
- API de IA: API de IA opcional. Community, Cloud y Enterprise tienen condiciones distintas; canales y funciones AI pueden consumir servicios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El helpdesk no incluye por sí solo la facturación de WhatsApp ni modelos; configura cada integración por separado
- Coste: El coste depende del proveedor o la ruta. Community, Cloud y Enterprise tienen condiciones distintas; canales y funciones AI pueden consumir servicios
- Equipo: Preparación según la ruta elegida. Cuenta o servidor; canal de prueba; proveedor solo para funciones AI
**Repo:** https://github.com/chatwoot/chatwoot

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/chatwoot/chatwoot/blob/develop/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una mesa de soporte; Comparar atención humana y asistencia AI
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una bandeja de ensayo y recorre una conversación ficticia con etiquetas y asignación
**Qué comprobar:** Puedes seguir estado, agente asignado e historial de la conversación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `evolution-api`, `n8n`, `firecrawl`

## `cloud-mail`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=marketing,server,javascript

**Qué es:** Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio.
**Stack:** Cuenta Cloudflare; dominio propio; Workers y almacenamiento de la guía; canal de envío
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere LLM para correo básico; dominio, Workers, almacenamiento y proveedor de envío tienen cuotas y costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No es una app totalmente local: se apoya en servicios Cloudflare y en la configuración del dominio
- Coste: El coste depende del proveedor o la ruta. No requiere LLM para correo básico; dominio, Workers, almacenamiento y proveedor de envío tienen cuotas y costes propios
- Equipo: Preparación según la ruta elegida. Cuenta Cloudflare; dominio propio; Workers y almacenamiento de la guía; canal de envío
**Repo:** https://github.com/maillab/cloud-mail

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/maillab/cloud-mail/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar correo sobre Workers; Gestionar buzones de un dominio de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Despliega un entorno de prueba y comprueba recepción con un buzón propio antes de usar correo real
**Qué comprobar:** Puedes identificar dónde se guarda el mensaje y qué servicio lo entrega
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `open-seo`, `changedetection`

## `compai-crm`
role=platform · exec=cloud · setup=heavy · mcp=False · prov=— · tags=crm,typescript

**Qué es:** CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia.
**Stack:** Bun; PostgreSQL; OAuth Google o Microsoft para login; AI Gateway para agentes fuera de Vercel
**Acceso y costes:**
- API de IA: API de IA opcional. Fuentes de enriquecimiento son opcionales; el modelo del agente usa Vercel AI Gateway con OIDC en Vercel o clave fuera; sin clave escrita no significa sin consumo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El agente es un despliegue propio; OAuth de correo no sustituye autenticación y presupuesto del modelo; la configuración incluye telemetría desactivable
- Coste: El coste depende del proveedor o la ruta. Fuentes de enriquecimiento son opcionales; el modelo del agente usa Vercel AI Gateway con OIDC en Vercel o clave fuera; sin clave escrita no significa sin consumo
- Equipo: Preparación según la ruta elegida. Bun; PostgreSQL; OAuth Google o Microsoft para login; AI Gateway para agentes fuera de Vercel
**Repo:** https://github.com/trycompai/crm

**Instalación** [+]:

```
git clone https://github.com/trycompai/crm.git && cd crm
cp .env.example .env          # then fill in the values below
bun install

docker compose up -d          # Postgres on :5432

bun run db:deploy             # apply migrations
bun run db:seed               # optional: a believable pipeline to look at
bun run dev
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un CRM con investigación de contactos; Organizar tareas con evidencia de su origen
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga datos ficticios y revisa qué fuentes de enriquecimiento y modelo están configurados antes de conectar correo
**Qué comprobar:** Puedes distinguir funciones CRM, lectura de historial y llamadas a proveedores externos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `sellbird`, `cal.diy`, `n8n`

## `erpnext`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=crm,python

**Qué es:** ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura.
**Stack:** Docker; servicios Frappe; datos de negocio ficticios; permisos de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El ERP abierto no necesita LLM; hosting, soporte, implementación y servicios externos se presupuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. pwd.yml es un entorno de evaluación; no equivale a configurar una instalación de producción con respaldos y credenciales propias
- Coste: El coste depende del proveedor o la ruta. El ERP abierto no necesita LLM; hosting, soporte, implementación y servicios externos se presupuestan aparte
- Equipo: Preparación según la ruta elegida. Docker; servicios Frappe; datos de negocio ficticios; permisos de prueba
**Repo:** https://github.com/frappe/erpnext

**Instalación** [+]:

```
git clone https://github.com/frappe/frappe_docker
cd frappe_docker

docker compose -f pwd.yml up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar inventario y ventas; Estudiar un ERP con datos de muestra
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa la demo Docker y crea un artículo y una oportunidad ficticios antes de configurar una empresa real
**Qué comprobar:** Puedes inspeccionar módulos y flujo de documentos de la demo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `metabase`, `paperless-ngx`
**Alternativas (elige una):** `odoo`

## `listmonk`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,email,go,docker

**Qué es:** Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS.
**Stack:** Docker; PostgreSQL; SMTP de ensayo; lista ficticia
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El gestor AGPL no necesita modelo; SMTP, entrega, servidor y dominio pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No incluye un servicio de entrega de correo gratuito por instalarlo; configura el proveedor y prueba con tu propio destinatario
- Coste: El coste depende del proveedor o la ruta. El gestor AGPL no necesita modelo; SMTP, entrega, servidor y dominio pueden costar
- Equipo: Preparación según la ruta elegida. Docker; PostgreSQL; SMTP de ensayo; lista ficticia
**Repo:** https://github.com/knadh/listmonk

**Instalación** [+]:

```
# Download the compose file to the current directory.
curl -LO https://github.com/knadh/listmonk/raw/master/docker-compose.yml

# Run the services in the background.
docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Gestionar una newsletter propia; Evaluar segmentación de una lista de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una lista de prueba y revisa el preview de una campaña antes de un envío de ensayo propio
**Qué comprobar:** Puedes comprobar plantilla, destinatario y estado del trabajo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `novu`, `postiz-app`

## `mautic`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=automation,email,php

**Qué es:** Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo.
**Stack:** Servidor y versión compatibles; SMTP; contactos ficticios; colas y tareas según guía
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita LLM para automatización; hosting, correo y servicios conectados tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Las campañas pueden ejecutar acciones y envíos; una plantilla dibujada no demuestra que cron, colas y entrega estén configurados
- Coste: El coste depende del proveedor o la ruta. No necesita LLM para automatización; hosting, correo y servicios conectados tienen costes propios
- Equipo: Preparación según la ruta elegida. Servidor y versión compatibles; SMTP; contactos ficticios; colas y tareas según guía
**Repo:** https://github.com/mautic/mautic

**Instalación** [?]:

```
Seguir la instalación original: https://docs.mautic.org/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar segmentación de audiencias; Prototipar una secuencia de marketing
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Diseña una campaña de prueba con un contacto ficticio y revisa condiciones y acciones antes de activarla
**Qué comprobar:** Puedes explicar qué evento dispara cada paso del flujo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `marketingskills`, `posthog`

## `novu`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,email,typescript

**Qué es:** Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend.
**Stack:** Proyecto de notificaciones; credenciales del canal; destino propio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La infraestructura no necesita un modelo para notificar; proveedores de canal, Cloud y módulos Enterprise tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Novu conecta agentes y productos a canales; no es el agente ni incluye el modelo que toma decisiones
- Coste: El coste depende del proveedor o la ruta. La infraestructura no necesita un modelo para notificar; proveedores de canal, Cloud y módulos Enterprise tienen costes propios
- Equipo: Preparación según la ruta elegida. Proyecto de notificaciones; credenciales del canal; destino propio de prueba
**Repo:** https://github.com/novuhq/novu

**Instalación** [?]:

```
Seguir la instalación original: https://docs.novu.co/platform/quickstart
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir una bandeja de notificaciones a una app; Coordinar avisos de email y chat
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Define un evento ficticio y comprueba su preview y entrega en un canal de ensayo
**Qué comprobar:** Puedes rastrear evento, plantilla y estado de entrega
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vercel-ai`, `langgraph`, `listmonk`

## `odoo`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=crm,python,postgres

**Qué es:** Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web.
**Stack:** Edición y versión elegidas; servidor y PostgreSQL; negocio ficticio
**Acceso y costes:**
- API de IA: API de IA opcional. Community, Enterprise y alojamiento tienen condiciones distintas; apps y servicios AI pueden añadir costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La edición determina módulos y licencia; instalar el repositorio Community no incluye todas las funciones comerciales
- Coste: El coste depende del proveedor o la ruta. Community, Enterprise y alojamiento tienen condiciones distintas; apps y servicios AI pueden añadir costes
- Equipo: Preparación según la ruta elegida. Edición y versión elegidas; servidor y PostgreSQL; negocio ficticio
**Repo:** https://github.com/odoo/odoo

**Instalación** [?]:

```
Seguir la instalación original: https://www.odoo.com/documentation/master/administration/install/install.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar un CRM para un negocio; Estudiar cómo se conectan ventas e inventario
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un contacto y una oportunidad ficticios y recorre sus etapas sin emitir documentos reales
**Qué comprobar:** Puedes comprobar campos, etapas y permisos del flujo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `metabase`, `botpress`
**Alternativas (elige una):** `erpnext`

## `open-seo`
role=platform · exec=local · setup=heavy · mcp=True · prov=— · tags=marketing,server,typescript

**Qué es:** Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio.
**Stack:** Cuenta o despliegue; DataForSEO; cliente MCP opcional; dominio propio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige modelo propio para consultar datos; DataForSEO cobra por uso y hosting o plan alojado tienen condiciones propias
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El plugin Codex agrupa MCP y skills; MCP HTTP también conecta otros clientes; el agente mantiene sus propios límites
- Coste: El coste depende del proveedor o la ruta. No exige modelo propio para consultar datos; DataForSEO cobra por uso y hosting o plan alojado tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Cuenta o despliegue; DataForSEO; cliente MCP opcional; dominio propio de prueba
**Repo:** https://github.com/every-app/open-seo

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/every-app/open-seo/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Investigar palabras clave de una web propia; Preparar una revisión técnica SEO
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta una métrica de un dominio propio y revisa origen, fecha y coste de la solicitud
**Qué comprobar:** Puedes identificar qué datos devuelve DataForSEO y qué interpreta el agente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `coolify`, `geo-seo-claude`

## `postiz-app`
role=platform · exec=hybrid · setup=heavy · mcp=True · prov=— · tags=marketing,server,typescript

**Qué es:** Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA.
**Stack:** Cuenta Cloud o self-host con PostgreSQL y Redis; apps de plataforma; modelos solo para AI
**Acceso y costes:**
- API de IA: API de IA opcional. Cloud incluye cuotas de AI por plan; self-hosting usa claves propias y recursos; redes pueden exigir aprobaciones y permisos adicionales
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. MCP y CLI están incluidos por ambas rutas; clonar el código no obtiene automáticamente credenciales aprobadas de cada red
- Coste: El coste depende del proveedor o la ruta. Cloud incluye cuotas de AI por plan; self-hosting usa claves propias y recursos; redes pueden exigir aprobaciones y permisos adicionales
- Equipo: Preparación según la ruta elegida. Cuenta Cloud o self-host con PostgreSQL y Redis; apps de plataforma; modelos solo para AI
**Repo:** https://github.com/gitroomhq/postiz-app

**Instalación** [?]:

```
Seguir la instalación original: https://docs.postiz.com/quickstart
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar un calendario de contenido; Evaluar generación asistida de borradores
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prepara una publicación ficticia en borrador y revisa preview, canal y horario sin programarla
**Qué comprobar:** Puedes comprobar contenido y cuenta de destino antes de publicar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `claude-code`, `coolify`

## `sellbird`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=marketing,agent,python

**Qué es:** Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes.
**Stack:** Python 3.13; Claude Code o Codex CLI autenticado; SMTP y fuentes solo según la prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa tu plan Claude o ChatGPT mediante CLI según el proyecto; fuentes pagadas, verificación y correo cuestan por separado
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La sesión del agente no hace gratuitos los datos ni la entrega; evita confundir un borrador aprobado con un mensaje ya enviado
- Coste: El coste depende del proveedor o la ruta. Usa tu plan Claude o ChatGPT mediante CLI según el proyecto; fuentes pagadas, verificación y correo cuestan por separado
- Equipo: Preparación según la ruta elegida. Python 3.13; Claude Code o Codex CLI autenticado; SMTP y fuentes solo según la prueba
**Repo:** https://github.com/ethanplusai/sellbird

**Instalación** [+]:

```
# 1. Install. Use python3.13, not python3: on macOS bare python3 is 3.9.
python3.13 -m venv .venv && source .venv/bin/activate && pip install -e .
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un borrador de prospección; Evaluar criterios de selección de empresas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Estudia un prospecto ficticio y genera un borrador sin habilitar envíos automáticos
**Qué comprobar:** Puedes revisar evidencias, redacción y costes de la fuente antes de aprobar cualquier envío
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `compai-crm`

## `twenty-main`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=automation,crm,typescript,docker

**Qué es:** CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones.
**Stack:** CRM o entorno self-host; Node y CLI solo para construir apps; modelo si activas AI
**Acceso y costes:**
- API de IA: API de IA opcional. CRM, hosting y AI tienen costes por ruta; las skills de desarrollo usan el agente anfitrión
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. El CLI twenty app init crea una extensión y no todo el servidor CRM; para usar el producto elige su instalación o servicio
- Coste: El coste depende del proveedor o la ruta. CRM, hosting y AI tienen costes por ruta; las skills de desarrollo usan el agente anfitrión
- Equipo: Preparación según la ruta elegida. CRM o entorno self-host; Node y CLI solo para construir apps; modelo si activas AI
**Repo:** https://github.com/twentyhq/twenty

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/twentyhq/twenty/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Modelar un proceso comercial propio; Desarrollar una app sobre un CRM
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un objeto y dos registros ficticios y revisa sus relaciones antes de añadir automatización
**Qué comprobar:** Puedes consultar registros y reconocer la estructura de campos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `n8n`, `evolution-api`, `cal.diy`
