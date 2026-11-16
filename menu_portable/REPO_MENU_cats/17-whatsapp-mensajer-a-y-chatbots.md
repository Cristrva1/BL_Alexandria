# 17. WhatsApp, mensajería y chatbots — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `baileys`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=whatsapp,chatbot,typescript

**Qué es:** Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador.
**Stack:** Node y TypeScript compatibles; sesión y almacenamiento de credenciales; cuenta de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita LLM; servidor y componentes AI añadidos tienen costes separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Usa el protocolo WhatsApp Web y no la API oficial; v7 incorpora cambios incompatibles que requieren su guía de migración
- Coste: Sin pago a un modelo en la ruta básica. No necesita LLM; servidor y componentes AI añadidos tienen costes separados
- Equipo: Preparación según la ruta elegida. Node y TypeScript compatibles; sesión y almacenamiento de credenciales; cuenta de prueba
**Repo:** https://github.com/WhiskeySockets/Baileys

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender el flujo multidispositivo; Conectar eventos de una cuenta propia a una app
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta el ejemplo de conexión y observa cambios de estado sin programar envíos
**Qué comprobar:** Puedes reconocer conexión, desconexión y datos de sesión persistidos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `evolution-api`, `n8n`
**Alternativas (elige una):** `whatsapp-web-js`, `waha`

## `botpress`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=chatbot,agents,typescript

**Qué es:** El repositorio actual reúne paquetes e integraciones abiertas y un CLI para crear y desplegar extensiones. Botpress Cloud y sus modelos tienen condiciones de servicio separadas. Clonar este código no instala toda la plataforma alojada.
**Stack:** Node y gestor de paquetes; cuenta Botpress para desplegar una integración; TypeScript
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Los paquetes del repositorio son MIT; Botpress Cloud, modelos y canales tienen sus precios y límites
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El repositorio actual es un hub de SDKs e integraciones; clonarlo no instala una plataforma completa auto-hospedada equivalente a Cloud
- Coste: El coste depende del proveedor o la ruta. Los paquetes del repositorio son MIT; Botpress Cloud, modelos y canales tienen sus precios y límites
- Equipo: Preparación según la ruta elegida. Node y gestor de paquetes; cuenta Botpress para desplegar una integración; TypeScript
**Repo:** https://github.com/botpress/botpress

**Instalación** [+]:

```
npm install -g @botpress/cli # for npm
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender el SDK de integraciones Botpress; Prototipar una conexión para un chatbot alojado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una integración con bp init y revisa su definición antes de desplegarla
**Qué comprobar:** Puedes identificar eventos, acciones y configuración de la integración
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `chatwoot`, `n8n`

## `evolution-api`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=automation,whatsapp,typescript,docker

**Qué es:** API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks.
**Stack:** Docker o Node; PostgreSQL y Redis según ruta; canal y credenciales; cuenta de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. La API básica no exige LLM; ruta Meta oficial, hosting y bots AI pueden cobrar; la licencia añade condiciones de marca y notificación
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La conexión WhatsApp Web y Meta Cloud API tienen requisitos distintos; una clave apikey de Evolution no es una clave de modelo
- Coste: El coste depende del proveedor o la ruta. La API básica no exige LLM; ruta Meta oficial, hosting y bots AI pueden cobrar; la licencia añade condiciones de marca y notificación
- Equipo: Preparación según la ruta elegida. Docker o Node; PostgreSQL y Redis según ruta; canal y credenciales; cuenta de prueba
**Repo:** https://github.com/evolution-foundation/evolution-api

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/evolution-foundation/evolution-api/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar atención de WhatsApp a una app; Recibir eventos en una automatización de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura una instancia de ensayo y consulta su estado antes de habilitar webhooks o respuestas
**Qué comprobar:** Puedes identificar motor, instancia y permisos de acceso
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `whatsapp-web-js`, `waha`

## `fluxer`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=whatsapp,chatbot,typescript

**Qué es:** Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio.
**Stack:** Cliente o servidor elegido; micrófono para voz; cuenta de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La mensajería básica no usa IA; alojamiento y servicios tienen condiciones propias; assets usan licencias distintas del código
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una plataforma comunitaria independiente, no una integración WhatsApp; por eso cambia de subcategoría
- Coste: El coste depende del proveedor o la ruta. La mensajería básica no usa IA; alojamiento y servicios tienen condiciones propias; assets usan licencias distintas del código
- Equipo: Preparación según la ruta elegida. Cliente o servidor elegido; micrófono para voz; cuenta de prueba
**Repo:** https://github.com/fluxerapp/fluxer

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/fluxerapp/fluxer/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar conversación de una comunidad; Probar una interfaz de mensajería y VoIP propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una comunidad de ensayo y comprueba permisos de un canal y una llamada de prueba
**Qué comprobar:** Puedes distinguir miembros, canales y permisos configurados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `open-generative-ai`

## `openwa`
role=platform · exec=local · setup=easy · mcp=True · prov=— · tags=whatsapp,chatbot,typescript

**Qué es:** Gateway autoalojado de WhatsApp con API, panel de sesiones y servidor MCP HTTP opcional, del proyecto rmyndharis/OpenWA.
**Stack:** Docker; cuenta y número propios; configuración de autenticación y persistencia
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El gateway no requiere modelo; hosting y servicios conectados tienen costes propios
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Este proyecto es rmyndharis/OpenWA; MCP HTTP añade herramientas de lectura por defecto y capacidades de escritura se habilitan aparte
- Coste: El coste depende del proveedor o la ruta. El gateway no requiere modelo; hosting y servicios conectados tienen costes propios
- Equipo: Preparación según la ruta elegida. Docker; cuenta y número propios; configuración de autenticación y persistencia
**Repo:** https://github.com/rmyndharis/OpenWA

**Instalación** [+]:

```
# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access (the dashboard is bundled into the API image and served on the same port)
# Dashboard: http://localhost:2785
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una integración de mensajería; Consultar estados desde un agente MCP
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre el dashboard y consulta el estado de una sesión de prueba antes de automatizar mensajes
**Qué comprobar:** Puedes ver sesión, API y permisos del usuario configurado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `evolution-api`

## `typebot`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=chatbot,automation,typescript

**Qué es:** Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más.
**Stack:** Cuenta o despliegue; bloques y canal elegidos; proveedor solo para AI
**Acceso y costes:**
- API de IA: API de IA opcional. Los bloques fijos no necesitan modelo; Cloud, canales y funciones LLM tienen costes propios; el código usa Functional Source License
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es fair-source con condiciones específicas; no se debe presentar toda modalidad como software sin restricciones comerciales
- Coste: El coste depende del proveedor o la ruta. Los bloques fijos no necesitan modelo; Cloud, canales y funciones LLM tienen costes propios; el código usa Functional Source License
- Equipo: Preparación según la ruta elegida. Cuenta o despliegue; bloques y canal elegidos; proveedor solo para AI
**Repo:** https://github.com/baptisteArno/typebot.io

**Instalación** [?]:

```
Seguir la instalación original: https://docs.typebot.io/self-hosting/get-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un formulario conversacional; Probar un flujo de preguntas frecuentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un flujo de dos preguntas con respuestas fijas y comprueba la rama elegida
**Qué comprobar:** El resultado guarda respuestas y recorre el camino esperado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `evolution-api`

## `waha`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=whatsapp,automation,docker

**Qué es:** API REST de WhatsApp en un contenedor Docker, con varios motores y panel web.
**Stack:** Docker; cuenta propia de prueba; configuración de auth y volumen según guía
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El núcleo y las modalidades Plus tienen condiciones distintas; hosting y servicios conectados cuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El contenedor --rm del ejemplo es una prueba temporal; para conservar sesiones sigue persistencia y seguridad de la guía
- Coste: El coste depende del proveedor o la ruta. El núcleo y las modalidades Plus tienen condiciones distintas; hosting y servicios conectados cuestan aparte
- Equipo: Preparación según la ruta elegida. Docker; cuenta propia de prueba; configuración de auth y volumen según guía
**Repo:** https://github.com/devlikeapro/waha

**Instalación** [+]:

```
docker run -it --rm -p 3000:3000/tcp --name waha devlikeapro/waha
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un webhook de mensajería; Evaluar un gateway HTTP para una app propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre el panel del contenedor de ensayo y comprueba estado de sesión y autenticación
**Qué comprobar:** Puedes reconocer qué motor y sesión están configurados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `evolution-api`, `whatsapp-web-js`, `baileys`

## `whatsapp-agentkit`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,automation,python

**Qué es:** Instrucciones y scripts que guían a Claude Code para construir un bot de WhatsApp; el bot resultante necesita sus propios proveedores y credenciales.
**Stack:** Claude Code; Python >=3.11; clave Anthropic; Zernio o Meta Cloud API; negocio ficticio para ensayo
**Acceso y costes:**
- API de IA: API de IA necesaria. Claude Code construye el proyecto; el bot usa su propia clave Anthropic y canal con tarifas o planes separados
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El tiempo anunciado es una estimación del autor y no una instalación garantizada; el plan de Claude Code no paga la API del bot
- Coste: El coste depende del proveedor o la ruta. Claude Code construye el proyecto; el bot usa su propia clave Anthropic y canal con tarifas o planes separados
- Equipo: Preparación según la ruta elegida. Claude Code; Python >=3.11; clave Anthropic; Zernio o Meta Cloud API; negocio ficticio para ensayo
**Repo:** https://github.com/Hainrixz/whatsapp-agentkit

**Instalación** [+]:

```
git clone https://github.com/Hainrixz/whatsapp-agentkit.git
cd whatsapp-agentkit
bash start.sh
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un asistente de preguntas frecuentes; Diseñar una consulta de horarios en un número de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Completa la entrevista con datos ficticios y revisa el código y credenciales requeridas antes de conectar un número
**Qué comprobar:** Puedes explicar cómo entra un mensaje, qué modelo responde y qué servicio lo envía
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `evolution-api`, `n8n-mcp`

## `whatsapp-web-js`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=whatsapp,chatbot,javascript

**Qué es:** Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless.
**Stack:** Node.js; Chrome o Chromium; cuenta y número propios de prueba; sesión WhatsApp Web
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no usa LLM; hosting y funciones AI añadidas cuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Automatiza WhatsApp Web y no es la API oficial Meta; las condiciones y estabilidad de esa sesión son independientes del código abierto
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no usa LLM; hosting y funciones AI añadidas cuestan aparte
- Equipo: Preparación según la ruta elegida. Node.js; Chrome o Chromium; cuenta y número propios de prueba; sesión WhatsApp Web
**Repo:** https://github.com/wwebjs/whatsapp-web.js

**Instalación** [+]:

```
npm install whatsapp-web.js
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un bot de atención en laboratorio; Conectar eventos WhatsApp Web a una app propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inicia el ejemplo y comprueba estado de autenticación antes de habilitar respuestas automáticas
**Qué comprobar:** Puedes distinguir sesión vinculada y eventos recibidos en el entorno de prueba
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`, `chatwoot`
**Alternativas (elige una):** `baileys`, `waha`, `evolution-api`

## `whatsmeow`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=whatsapp,go,golang,whatsapp-web

**Qué es:** Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web.
**Stack:** Go; almacenamiento de sesión; cuenta propia de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere IA; infraestructura y funciones añadidas tienen costes separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Biblioteca de protocolo Web multidispositivo; no es una app final ni la API oficial Meta
- Coste: Sin pago a un modelo en la ruta básica. No requiere IA; infraestructura y funciones añadidas tienen costes separados
- Equipo: Preparación según la ruta elegida. Go; almacenamiento de sesión; cuenta propia de prueba
**Repo:** https://github.com/tulir/whatsmeow

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/tulir/whatsmeow/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una integración de eventos en Go; Estudiar almacenamiento de sesiones WhatsApp Web
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el ejemplo de conexión y comprueba los eventos y la sesión guardada
**Qué comprobar:** Puedes reconocer el estado del cliente multidispositivo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `n8n`
