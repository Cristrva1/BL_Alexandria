# 1. Automatizar procesos y crear herramientas internas — detalle de repos

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
