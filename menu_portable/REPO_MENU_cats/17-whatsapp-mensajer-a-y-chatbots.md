# 17. WhatsApp, mensajería y chatbots — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

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
