# Alexandría para agentes · CRM, ERP y soporte al cliente

Categoría 18 «CRM, ventas y marketing» › subcategoría `crm`. 9 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=18&sub=crm · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `twenty-main` | CRM open-source orientado a equipos técnicos, pensado como alternativa moderna… | 3 Avanzado | 75 | AGPL-3.0 + licencia comercial (archivos @license Enterprise) (open-core) | recomendado |
| `erpnext` | ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y… | 3 Avanzado | 74 | GPL-3.0 (OSI copyleft) | alternativa |
| `compai-crm` | CRM de Comp AI diseñado alrededor de agentes que investigan contactos… | 3 Avanzado | 66 | MIT (OSI permisiva) | sin grupo |
| `odoo` | Suite ERP y CRM de código abierto con módulos de ventas, inventario… | 3 Avanzado | 66 | LGPL-3.0 (OSI copyleft) | alternativa |
| `chatwoot` | Plataforma open-source de soporte al cliente que unifica conversaciones de… | 3 Avanzado | 65 | MIT + licencia Enterprise (enterprise/) (open-core) | sin grupo |
| `freescout` | Helpdesk y bandeja de entrada compartida muy ligera, alternativa abierta a Help… | 2 Intermedio | 59 | AGPL-3.0 (OSI copyleft) | recomendado |
| `zammad` | Sistema de helpdesk y tickets autoalojado y omnicanal: correo, chat, teléfono y… | 3 Avanzado | 58 | AGPL-3.0 (OSI copyleft) | alternativa |
| `espocrm` | CRM web ligero y autoalojable para gestionar contactos, cuentas, oportunidades… | 2 Intermedio | 53 | AGPL-3.0 (OSI copyleft) | alternativa |
| `suitecrm` | CRM open source clásico (fork de SugarCRM): contactos, oportunidades, casos y… | 2 Intermedio | 45 | AGPL-3.0 (OSI copyleft) | alternativa |

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-18-crm.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «CRM, ERP y soporte al cliente», lee `docs/alexandria/categoria-18-crm.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-18-crm.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
