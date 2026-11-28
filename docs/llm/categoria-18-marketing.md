# Alexandría para agentes · Email, marketing y notificaciones

Categoría 18 «CRM, ventas y marketing» › subcategoría `marketing`. 7 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=18&sub=marketing · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `postiz-app` | Plataforma para preparar, programar y gestionar publicaciones en redes… | 3 Avanzado | 70 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `open-seo` | Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO… | 3 Avanzado | 68 | MIT (OSI permisiva) | sin grupo |
| `mautic` | Plataforma open-source de marketing automation y segmentación de audiencias… | 3 Avanzado | 64 | GPL-3.0-or-later (OSI copyleft) | sin grupo |
| `novu` | Infraestructura open-source de notificaciones que centraliza la comunicación… | 2 Intermedio | 64 | MIT + licencia Enterprise (enterprise/packages) (open-core) | sin grupo |
| `cloud-mail` | Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y… | 3 Avanzado | 60 | MIT (OSI permisiva) | sin grupo |
| `listmonk` | Gestor self-hosted de newsletters y listas de correo de alto rendimiento… | 2 Intermedio | 58 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `sellbird` | Plataforma de prospección por correo que documenta el uso de sesiones de Claude… | 2 Intermedio | 48 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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
- **Combina con:** `claude-code` [20/terminal], `coolify` [22/infraestructura], `claude-seo` [27/dominio], `cloud-mail`, `marketingskills` [27/dominio]
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
- **Combina con:** `activepieces` [1/motores], `novu`, `postiz-app`, `formbricks` [18/encuestas]
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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-18-marketing.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Email, marketing y notificaciones», lee `docs/alexandria/categoria-18-marketing.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-18-marketing.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
