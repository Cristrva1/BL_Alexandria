# Alexandría para agentes · CRM, ventas y marketing

Categoría 18 completa (19 repos, 3 subcategorías). Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=18 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `twenty-main` | crm | CRM open-source orientado a equipos técnicos, pensado como alternativa moderna… | 3 Avanzado | 75 | AGPL-3.0 + licencia comercial (archivos @license Enterprise) (open-core) | recomendado |
| `erpnext` | crm | ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y… | 3 Avanzado | 74 | GPL-3.0 (OSI copyleft) | alternativa |
| `compai-crm` | crm | CRM de Comp AI diseñado alrededor de agentes que investigan contactos… | 3 Avanzado | 66 | MIT (OSI permisiva) | sin grupo |
| `odoo` | crm | Suite ERP y CRM de código abierto con módulos de ventas, inventario… | 3 Avanzado | 66 | LGPL-3.0 (OSI copyleft) | alternativa |
| `chatwoot` | crm | Plataforma open-source de soporte al cliente que unifica conversaciones de… | 3 Avanzado | 65 | MIT + licencia Enterprise (enterprise/) (open-core) | sin grupo |
| `freescout` | crm | Helpdesk y bandeja de entrada compartida muy ligera, alternativa abierta a Help… | 2 Intermedio | 59 | AGPL-3.0 (OSI copyleft) | recomendado |
| `zammad` | crm | Sistema de helpdesk y tickets autoalojado y omnicanal: correo, chat, teléfono y… | 3 Avanzado | 58 | AGPL-3.0 (OSI copyleft) | alternativa |
| `espocrm` | crm | CRM web ligero y autoalojable para gestionar contactos, cuentas, oportunidades… | 2 Intermedio | 53 | AGPL-3.0 (OSI copyleft) | alternativa |
| `suitecrm` | crm | CRM open source clásico (fork de SugarCRM): contactos, oportunidades, casos y… | 2 Intermedio | 45 | AGPL-3.0 (OSI copyleft) | alternativa |
| `postiz-app` | marketing | Plataforma para preparar, programar y gestionar publicaciones en redes… | 3 Avanzado | 70 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `open-seo` | marketing | Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO… | 3 Avanzado | 68 | MIT (OSI permisiva) | sin grupo |
| `mautic` | marketing | Plataforma open-source de marketing automation y segmentación de audiencias… | 3 Avanzado | 64 | GPL-3.0-or-later (OSI copyleft) | sin grupo |
| `novu` | marketing | Infraestructura open-source de notificaciones que centraliza la comunicación… | 2 Intermedio | 64 | MIT + licencia Enterprise (enterprise/packages) (open-core) | sin grupo |
| `cloud-mail` | marketing | Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y… | 3 Avanzado | 60 | MIT (OSI permisiva) | sin grupo |
| `listmonk` | marketing | Gestor self-hosted de newsletters y listas de correo de alto rendimiento… | 2 Intermedio | 58 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `sellbird` | marketing | Plataforma de prospección por correo que documenta el uso de sesiones de Claude… | 2 Intermedio | 48 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `cal.diy` | reservas | Edición comunitaria de Cal.com para experimentar con agendas y reservas en una… | 3 Avanzado | 70 | MIT (OSI permisiva) | recomendado |
| `formbricks` | reservas | Encuestas y experience management open source (alternativa a Qualtrics)… | 2 Intermedio | 66 | AGPL-3.0 + licencia Enterprise (ee/) (open-core) | sin grupo |
| `easyappointments` | reservas | Aplicación web autoalojada de reserva de citas: clientes reservan online según… | 2 Intermedio | 47 | GPL-3.0 (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### twenty-main (`twenty-main`)

- **Repo:** https://github.com/twentyhq/twenty · AGPL-3.0 + licencia comercial (archivos @license Enterprise) · nivel 3 · 75/100 · recomendado en «CRM y ERP auto-hospedados»
- **Qué es:** CRM de código abierto pensado para equipos técnicos, de Twenty (twentyhq), que se construye, despliega y versiona como el resto del código. Es muy activo (versión 2.58 en 2026); su licencia no figura como estándar en GitHub y combina…
- **Cuándo elegirlo:** Casos: Modelar un proceso comercial propio; Desarrollar una app sobre un CRM.
- **Requisitos:** nivel 3: preparación pesada; CRM o entorno self-host; Node y CLI solo para construir apps; modelo si activas AI; hardware prerequisites; API de IA: opcional; CRM o entorno self-host; Node y CLI solo para construir apps; modelo si activas AI.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g twenty` — fuente: https://github.com/twentyhq/twenty/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un objeto y dos registros ficticios y revisa sus relaciones antes de añadir automatización Éxito: Puedes consultar registros y reconocer la estructura de campos
- **Combina con:** `claude-code` [20/terminal], `activepieces` [1/motores], `evolution-api` [17/whatsapp], `cal.diy` [18/reservas], `docuseal` [13/pdf]
- **Alternativas:** `erpnext`, `odoo`, `espocrm`, `suitecrm`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). El CLI twenty app init crea una extensión y no todo el servidor CRM; para usar el producto elige su instalación o servicio.

### ERPNext (`erpnext`)

- **Repo:** https://github.com/frappe/erpnext · GPL-3.0 · nivel 3 · 74/100 · alternativa en «CRM y ERP auto-hospedados»
- **Qué es:** Sistema ERP 100 % de código abierto (GPL v3) de Frappe Technologies, construido sobre el Frappe Framework. Es maduro y muy activo (serie v16 en 2026), con hospedaje gestionado opcional en Frappe Cloud.
- **Cuándo elegirlo:** Casos: Evaluar inventario y ventas; Estudiar un ERP con datos de muestra.
- **Requisitos:** nivel 3: preparación pesada, varios servicios con Docker Compose; Docker; servicios Frappe; datos de negocio ficticios; permisos de prueba; hardware prerequisites; API de IA: no; Docker; servicios Frappe; datos de negocio ficticios; permisos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/frappe/erpnext/blob/develop/README.md

  ```sh
  git clone https://github.com/frappe/frappe_docker
  cd frappe_docker
  
  docker compose -f pwd.yml up -d
  ```
- **Primera prueba propuesta (no ejecutada):** Usa la demo Docker y crea un artículo y una oportunidad ficticios antes de configurar una empresa real Éxito: Puedes inspeccionar módulos y flujo de documentos de la demo
- **Combina con:** `activepieces` [1/motores], `metabase` [10/bi], `paperless-ngx` [13/gestion]
- **Alternativas:** `twenty-main`, `odoo`, `espocrm`, `suitecrm`
- **Riesgos y avisos:** Alternativa (elige una): odoo. Pwd.yml es un entorno de evaluación; no equivale a configurar una instalación de producción con respaldos y credenciales propias.

### crm (`compai-crm`)

- **Repo:** https://github.com/trycompai/crm · MIT · nivel 3 · 66/100
- **Qué es:** CRM de código abierto (MIT) «agentic-first» de Comp AI, en el que el agente es el usuario principal y el CRM es donde guarda sus notas. Es reciente y activo (v1.16 en 2026).
- **Cuándo elegirlo:** Casos: Estudiar un CRM con investigación de contactos; Organizar tareas con evidencia de su origen.
- **Requisitos:** nivel 3: preparación pesada, varios servicios con Docker Compose; Bun; PostgreSQL; OAuth Google o Microsoft para login; AI Gateway para agentes fuera de Vercel; hardware prerequisites; API de IA: opcional; Bun; PostgreSQL; OAuth Google o Microsoft para login; AI Gateway para agentes fuera de Vercel.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/trycompai/crm/blob/release/README.md

  ```sh
  git clone https://github.com/trycompai/crm.git && cd crm
  cp .env.example .env          # then fill in the values below
  bun install
  
  docker compose up -d          # Postgres on :5432
  
  bun run db:deploy             # apply migrations
  bun run db:seed               # optional: a believable pipeline to look at
  bun run dev
  ```
- **Primera prueba propuesta (no ejecutada):** Carga datos ficticios y revisa qué fuentes de enriquecimiento y modelo están configurados antes de conectar correo Éxito: Puedes distinguir funciones CRM, lectura de historial y llamadas a proveedores externos
- **Combina con:** `sellbird` [18/marketing], `cal.diy` [18/reservas], `activepieces` [1/motores]
- **Riesgos y avisos:** Las herramientas nuevas o modificadas requieren revisión antes de que el agente pueda usarlas. Pensado para Vercel; en otro proveedor hay que sustituir…. El agente es un despliegue propio; OAuth de correo no sustituye autenticación y presupuesto del modelo; la configuración incluye telemetría desactivable.

### Odoo (`odoo`)

- **Repo:** https://github.com/odoo/odoo · LGPL-3.0 · nivel 3 · 66/100 · alternativa en «CRM y ERP auto-hospedados»
- **Qué es:** Suite de aplicaciones de negocio web de código abierto de Odoo S.A. La edición comunitaria del repositorio se publica bajo LGPL v3 y convive con una edición Enterprise de pago; es un proyecto maduro (desde 2004) con desarrollo diario y…
- **Cuándo elegirlo:** Casos: Evaluar un CRM para un negocio; Estudiar cómo se conectan ventas e inventario.
- **Requisitos:** nivel 3: preparación pesada; Edición y versión elegidas; servidor y PostgreSQL; negocio ficticio; hardware prerequisites; API de IA: opcional; Edición y versión elegidas; servidor y PostgreSQL; negocio ficticio.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://www.odoo.com/documentation/master/administration/install/install.html
- **Primera prueba propuesta (no ejecutada):** Crea un contacto y una oportunidad ficticios y recorre sus etapas sin emitir documentos reales Éxito: Puedes comprobar campos, etapas y permisos del flujo
- **Combina con:** `activepieces` [1/motores], `metabase` [10/bi], `botpress` [17/chatbots]
- **Alternativas:** `twenty-main`, `erpnext`, `espocrm`, `suitecrm`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): erpnext. Algunas apps solo existen en la edición Enterprise. La edición determina módulos y licencia; instalar el repositorio Community no incluye todas las funciones comerciales.

### chatwoot (`chatwoot`)

- **Repo:** https://github.com/chatwoot/chatwoot · MIT + licencia Enterprise (enterprise/) · nivel 3 · 65/100
- **Qué es:** Chatwoot, plataforma de atención al cliente autoalojable y alternativa a Intercom o Zendesk, de Chatwoot Inc. La Community Edition es MIT; el directorio `enterprise/` tiene licencia propia (por eso GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Organizar una mesa de soporte; Comparar atención humana y asistencia AI.
- **Requisitos:** nivel 3: preparación pesada; Cuenta o servidor; canal de prueba; proveedor solo para funciones AI; hardware prerequisites; API de IA: opcional; Cuenta o servidor; canal de prueba; proveedor solo para funciones AI.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/chatwoot/chatwoot/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una bandeja de ensayo y recorre una conversación ficticia con etiquetas y asignación Éxito: Puedes seguir estado, agente asignado e historial de la conversación
- **Combina con:** `evolution-api` [17/whatsapp], `activepieces` [1/motores], `firecrawl` [4/crawlers]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. El equipo desaconseja usar la Community Edition para clones de Chatwoot Cloud o servicios de rebranding. El helpdesk no incluye por sí solo la facturación de WhatsApp ni modelos; configura cada integración por separado.

### FreeScout (`freescout`)

- **Repo:** https://github.com/freescout-help-desk/freescout · AGPL-3.0 · nivel 2 · 59/100 · recomendado en «Help desk y tickets»
- **Qué es:** Helpdesk de código abierto (AGPL-3.0) del proyecto FreeScout, financiado con la venta de módulos. Maduro y activo.
- **Cuándo elegirlo:** Casos: gestionar el correo de soporte de un equipo pequeño en un hosting barato; unificar correo, WhatsApp o Telegram de clientes con módulos.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; PHP, composer.json, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://freescout.net/docker/
- **Primera prueba propuesta (no ejecutada):** Instala FreeScout en un servidor PHP o con su imagen Docker, conecta un buzón de prueba y responde a una conversación. Éxito: El correo aparece como conversación y la respuesta se envía desde FreeScout.
- **Combina con:** `activepieces` [1/motores], `claude-code` [20/terminal], `coolify` [22/infraestructura]
- **Alternativas:** `zammad`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): zammad.

### Zammad (`zammad`)

- **Repo:** https://github.com/zammad/zammad · AGPL-3.0 · nivel 3 · 58/100 · alternativa en «Help desk y tickets»
- **Qué es:** Helpdesk de código abierto (AGPL-3.0) de la Zammad Foundation, con alojamiento y soporte de pago de Zammad GmbH. Muy maduro.
- **Cuándo elegirlo:** Casos: centralizar el soporte por correo y chat de un equipo pequeño; crear una base de conocimiento y métricas de atención.
- **Requisitos:** nivel 3: preparación pesada; Ruby, Dockerfile, Gemfile, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/zammad/zammad/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Zammad con zammad-docker-compose, conecta una cuenta de correo de prueba y responde a un ticket. Éxito: El correo entra como ticket y la respuesta sale desde Zammad.
- **Combina con:** `activepieces` [1/motores], `claude-code` [20/terminal], `coolify` [22/infraestructura]
- **Alternativas:** `freescout`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): freescout. Chatwoot cubre atención por chat y mensajería con otro enfoque.

### EspoCRM (`espocrm`)

- **Repo:** https://github.com/espocrm/espocrm · AGPL-3.0 · nivel 2 · 53/100 · alternativa en «CRM y ERP auto-hospedados»
- **Qué es:** CRM de código abierto (AGPL-3.0) de EspoCRM Inc., con extensiones y soporte de pago. Maduro y activo.
- **Cuándo elegirlo:** Casos: llevar el pipeline de ventas de una pyme en tu servidor; adaptar entidades y campos del CRM a tu proceso sin programar.
- **Requisitos:** nivel 2: preparación media; PHP, composer.json, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/espocrm/espocrm/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala EspoCRM con su imagen Docker o en un servidor PHP, crea una cuenta y una oportunidad. Éxito: La oportunidad aparece en el pipeline con su etapa.
- **Combina con:** `activepieces` [1/motores], `easyappointments` [18/reservas], `coolify` [22/infraestructura]
- **Alternativas:** `twenty-main`, `erpnext`, `odoo`, `suitecrm`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): twenty-main.

### SuiteCRM (`suitecrm`)

- **Repo:** https://github.com/SuiteCRM/SuiteCRM · AGPL-3.0 · nivel 2 · 45/100 · alternativa en «CRM y ERP auto-hospedados»
- **Qué es:** CRM AGPL SuiteCRM Ltd.
- **Cuándo elegirlo:** Casos: CRM interno para un equipo comercial pequeño; portal de casos de soporte.
- **Requisitos:** nivel 2: preparación media; PHP, composer.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/SuiteCRM/SuiteCRM/blob/hotfix/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega SuiteCRM según la guía oficial (LAMP/Docker) y completa el instalador web. Éxito: Escritorio CRM accesible.
- **Combina con:** `chatwoot`, `listmonk` [18/marketing]
- **Alternativas:** `twenty-main`, `erpnext`, `odoo`, `espocrm`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### postiz-app (`postiz-app`)

- **Repo:** https://github.com/gitroomhq/postiz-app · AGPL-3.0 · nivel 3 · 70/100
- **Qué es:** Plataforma de gestión de redes sociales para programar, automatizar y analizar contenido, de gitroomhq. La edición autoalojada es de código abierto (AGPL-3.0) sin funciones limitadas por licencia, y existe Postiz Cloud gestionado.
- **Cuándo elegirlo:** Casos: Organizar un calendario de contenido; Evaluar generación asistida de borradores.
- **Requisitos:** nivel 3: preparación pesada; Cuenta Cloud o self-host con PostgreSQL y Redis; apps de plataforma; modelos solo para AI; hardware prerequisites; API de IA: opcional; Cuenta Cloud o self-host con PostgreSQL y Redis; apps de plataforma; modelos solo para AI.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.postiz.com/quickstart
- **Primera prueba propuesta (no ejecutada):** Prepara una publicación ficticia en borrador y revisa preview, canal y horario sin programarla Éxito: Puedes comprobar contenido y cuenta de destino antes de publicar
- **Combina con:** `activepieces` [1/motores], `claude-code` [20/terminal], `coolify` [22/infraestructura], `humanizer` [27/escritura], `instagram-agent-skill` [27/dominio], `linkedin-agent-skill` [27/dominio]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. MCP y CLI están incluidos por ambas rutas; clonar el código no obtiene automáticamente credenciales aprobadas de cada red.

### open-seo (`open-seo`)

- **Repo:** https://github.com/every-app/open-seo · MIT · nivel 3 · 68/100
- **Qué es:** Herramienta SEO de código abierto (MIT), alternativa a Semrush y Ahrefs, de every-app. Es reciente y activa (v0.1.x en 2026), con versión alojada de pago opcional.
- **Cuándo elegirlo:** Casos: Investigar palabras clave de una web propia; Preparar una revisión técnica SEO.
- **Requisitos:** nivel 3: preparación pesada; Cuenta o despliegue; DataForSEO; cliente MCP opcional; dominio propio de prueba; hardware prerequisites; API de IA: no; Cuenta o despliegue; DataForSEO; cliente MCP opcional; dominio propio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/every-app/open-seo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta una métrica de un dominio propio y revisa origen, fecha y coste de la solicitud Éxito: Puedes identificar qué datos devuelve DataForSEO y qué interpreta el agente
- **Combina con:** `claude-code` [20/terminal], `coolify` [22/infraestructura], `geo-seo-claude` [27/dominio], `claude-seo` [27/dominio], `cloud-mail`, `marketingskills` [27/dominio]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Cada consulta a DataForSEO tiene coste; vigila el gasto en su panel. El plugin Codex agrupa MCP y skills; MCP HTTP también conecta otros clientes; el agente mantiene sus propios límites.

### mautic (`mautic`)

- **Repo:** https://github.com/mautic/mautic · GPL-3.0-or-later · nivel 3 · 64/100
- **Qué es:** Plataforma de automatización de marketing de código abierto, presentada como el mayor proyecto abierto de su tipo y con comunidad mundial. Se distribuye bajo GPL v3 [DATO NO VERIFICADO: GitHub no reconoce la licencia como estándar] y…
- **Cuándo elegirlo:** Casos: Estudiar segmentación de audiencias; Prototipar una secuencia de marketing.
- **Requisitos:** nivel 3: preparación pesada; Servidor y versión compatibles; SMTP; contactos ficticios; colas y tareas según guía; hardware prerequisites; API de IA: no; Servidor y versión compatibles; SMTP; contactos ficticios; colas y tareas según guía.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.mautic.org/
- **Primera prueba propuesta (no ejecutada):** Diseña una campaña de prueba con un contacto ficticio y revisa condiciones y acciones antes de activarla Éxito: Puedes explicar qué evento dispara cada paso del flujo
- **Combina con:** `activepieces` [1/motores], `marketingskills` [27/dominio], `posthog` [10/producto]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Se solapa con listmonk en envío masivo de email; usa uno como canal principal de boletines. Las campañas pueden ejecutar acciones y envíos; una plantilla dibujada no demuestra que cron, colas y entrega estén configurados.

### novu (`novu`)

- **Repo:** https://github.com/novuhq/novu · MIT + licencia Enterprise (enterprise/packages) · nivel 2 · 64/100
- **Qué es:** Infraestructura de comunicación de código abierto para productos y agentes, de Novu. Sigue un modelo «open core»: el núcleo es abierto y la carpeta `enterprise` requiere licencia comercial; publica versiones con frecuencia.
- **Cuándo elegirlo:** Casos: Añadir una bandeja de notificaciones a una app; Coordinar avisos de email y chat.
- **Requisitos:** nivel 2: preparación media; Proyecto de notificaciones; credenciales del canal; destino propio de prueba; hardware prerequisites; API de IA: no; Proyecto de notificaciones; credenciales del canal; destino propio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @novu/react` — fuente: https://docs.novu.co/platform/quickstart/react?utm_source=github&utm_medium=readme&utm_campaign=react-starter-link
- **Primera prueba propuesta (no ejecutada):** Define un evento ficticio y comprueba su preview y entrega en un canal de ensayo Éxito: Puedes rastrear evento, plantilla y estado de entrega
- **Combina con:** `vercel-ai` [3/ts], `langgraph` [3/py], `listmonk`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Novu conecta agentes y productos a canales; no es el agente ni incluye el modelo que toma decisiones.

### cloud-mail (`cloud-mail`)

- **Repo:** https://github.com/maillab/cloud-mail · MIT · nivel 3 · 60/100
- **Qué es:** Plataforma de correo de código abierto (MIT) basada en Cloudflare, del proyecto maillab, que permite crear muchos buzones con un solo dominio. Su documentación principal está en chino, con traducciones al inglés y japonés; publica…
- **Cuándo elegirlo:** Casos: Estudiar correo sobre Workers; Gestionar buzones de un dominio de prueba.
- **Requisitos:** nivel 3: preparación pesada; Cuenta Cloudflare; dominio propio; Workers y almacenamiento de la guía; canal de envío; hardware prerequisites; API de IA: no; Cuenta Cloudflare; dominio propio; Workers y almacenamiento de la guía; canal de envío.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/maillab/cloud-mail/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega un entorno de prueba y comprueba recepción con un buzón propio antes de usar correo real Éxito: Puedes identificar dónde se guarda el mensaje y qué servicio lo entrega
- **Combina con:** `activepieces` [1/motores], `open-seo`, `changedetection` [4/busqueda]
- **Riesgos y avisos:** Depende de servicios de Cloudflare (Workers, D1, KV, R2) y de sus límites de plan. No es una app totalmente local: se apoya en servicios Cloudflare y en la configuración del dominio.

### listmonk (`listmonk`)

- **Repo:** https://github.com/knadh/listmonk · AGPL-3.0 · nivel 2 · 58/100
- **Qué es:** Gestor autoalojado de boletines y listas de correo, de código abierto (AGPLv3), creado por Kailash Nadh en 2018. Se distribuye como un único binario en Go; en noviembre de 2026 su última versión es la v7.0.0-beta.2.
- **Cuándo elegirlo:** Casos: Gestionar una newsletter propia; Evaluar segmentación de una lista de prueba.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker; PostgreSQL; SMTP de ensayo; lista ficticia; hardware prerequisites; API de IA: no; Docker; PostgreSQL; SMTP de ensayo; lista ficticia.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/knadh/listmonk/blob/master/README.md

  ```shell
  # Download the compose file to the current directory.
  curl -LO https://github.com/knadh/listmonk/raw/master/docker-compose.yml
  
  # Run the services in the background.
  docker compose up -d
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una lista de prueba y revisa el preview de una campaña antes de un envío de ensayo propio Éxito: Puedes comprobar plantilla, destinatario y estado del trabajo
- **Combina con:** `activepieces` [1/motores], `novu`, `postiz-app`, `formbricks` [18/reservas]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Necesitas un proveedor SMTP con buena reputación (SPF, DKIM y DMARC configurados). mautic cubre automatización de marketing más amplia y se solapa en email…. No incluye un servicio de entrega de correo gratuito por instalarlo; configura el proveedor y prueba con tu propio destinatario.

### sellbird (`sellbird`)

- **Repo:** https://github.com/ethanplusai/sellbird · AGPL-3.0 · nivel 2 · 48/100
- **Qué es:** Plataforma de prospección («outreach») de código abierto (AGPL-3.0) que funciona con tu plan de Claude o ChatGPT, antes llamada Harvey. Es reciente (v0.4 en 2026) y tiene una versión alojada en acceso anticipado.
- **Cuándo elegirlo:** Casos: Preparar un borrador de prospección; Evaluar criterios de selección de empresas.
- **Requisitos:** nivel 2: preparación media; Python 3.13; Claude Code o Codex CLI autenticado; SMTP y fuentes solo según la prueba; hardware prerequisites; API de IA: no; Python 3.13; Claude Code o Codex CLI autenticado; SMTP y fuentes solo según la prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ethanplusai/sellbird/blob/main/README.md

  ```bash
  # 1. Install. Use python3.13, not python3: on macOS bare python3 is 3.9.
  python3.13 -m venv .venv && source .venv/bin/activate && pip install -e .
  ```
- **Primera prueba propuesta (no ejecutada):** Estudia un prospecto ficticio y genera un borrador sin habilitar envíos automáticos Éxito: Puedes revisar evidencias, redacción y costes de la fuente antes de aprobar cualquier envío
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `compai-crm` [18/crm]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. El email en frío está regulado (por ejemplo GDPR o CAN-SPAM); revisa la normativa de tu país y usa dominios de envío separados. La sesión del agente no hace gratuitos los datos ni la entrega; evita confundir un borrador aprobado con un mensaje ya enviado.

### cal.diy (`cal.diy`)

- **Repo:** https://github.com/calcom/cal.diy · MIT · nivel 3 · 70/100 · recomendado en «Reservas y citas»
- **Qué es:** Plataforma de agendamiento de código abierto y comunitaria: un fork de Cal.com con todo el código Enterprise eliminado, 100 % bajo licencia MIT. Sus autores la recomiendan para uso personal y no productivo, y remiten a Cal.com para usos…
- **Cuándo elegirlo:** Casos: Experimentar con una agenda personal autoalojada; Probar la duración y disponibilidad de distintos tipos de cita.
- **Requisitos:** nivel 3: preparación pesada; Node.js y Yarn según el proyecto;  PostgreSQL;  Docker para el entorno de desarrollo; hardware prerequisites; API de IA: no; Node.js y Yarn según el proyecto; PostgreSQL; Docker para el entorno de desarrollo.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/calcom/cal.diy.git` — fuente: https://github.com/calcom/cal.diy/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un evento personal de prueba y abre su página de reserva Éxito: Puedes elegir una franja disponible y revisar la reserva creada
- **Combina con:** `activepieces` [1/motores], `twenty-main` [18/crm], `botpress` [17/chatbots], `compai-crm` [18/crm], `formbricks`
- **Alternativas:** `easyappointments`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. El autor la recomienda para uso personal y no productivo. Se mueve de motores de workflows a agendas y reservas.

### Formbricks (`formbricks`)

- **Repo:** https://github.com/formbricks/formbricks · AGPL-3.0 + licencia Enterprise (ee/) · nivel 2 · 66/100
- **Qué es:** Formbricks: experiencia/encuestas OS (AGPL núcleo; packages MIT; apps/web/modules/ee con licencia EE).
- **Cuándo elegirlo:** Casos: encuestas NPS in-app en un producto propio; formularios de onboarding autoalojados.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `claude mcp add --transport http formbricks https://app.formbricks.com/api/mcp` — fuente: https://github.com/formbricks/formbricks/blob/main/docs/platform/mcp/setup.mdx
- **Primera prueba propuesta (no ejecutada):** Sigue https://formbricks.com docs para Docker Compose y abre la UI. Éxito: Creas una encuesta de prueba.
- **Combina con:** `cal.diy`, `easyappointments`, `listmonk` [18/marketing], `typebot` [17/chatbots]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Easy!Appointments (`easyappointments`)

- **Repo:** https://github.com/alextselegidis/easyappointments · GPL-3.0 · nivel 2 · 47/100 · alternativa en «Reservas y citas»
- **Qué es:** Sistema de reservas de código abierto (GPL-3.0) creado por Alex Tselegidis. Maduro y activo.
- **Cuándo elegirlo:** Casos: permitir a tus clientes reservar citas en tu web; gestionar la agenda de varios profesionales y servicios.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; PHP, composer.json, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up` — fuente: https://github.com/alextselegidis/easyappointments/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Levanta el entorno Docker Compose del repositorio, crea un servicio y un proveedor y haz una reserva de prueba. Éxito: La cita aparece en el calendario del proveedor.
- **Combina con:** `espocrm` [18/crm], `activepieces` [1/motores], `coolify` [22/infraestructura], `formbricks`
- **Alternativas:** `cal.diy`
- **Riesgos y avisos:** Alternativas (elige una): cal.diy.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-18.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «CRM, ventas y marketing», lee `docs/alexandria/categoria-18.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-18.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
