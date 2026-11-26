# Alexandría para agentes · WhatsApp, mensajería y chatbots

Categoría 17 completa (18 repos, 3 subcategorías). Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=17 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `openwa` | whatsapp | Gateway autoalojado de WhatsApp con API, panel de sesiones y servidor MCP HTTP… | 2 Intermedio | 70 | MIT (OSI permisiva) | sin grupo |
| `whatsapp-web-js` | whatsapp | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un… | 2 Intermedio | 69 | Apache-2.0 (OSI permisiva) | recomendado |
| `baileys` | whatsapp | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin… | 2 Intermedio | 67 | MIT (OSI permisiva) | alternativa |
| `waha` | whatsapp | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. | 1 Básico | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `evolution-api` | whatsapp | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con… | 3 Avanzado | 54 | Apache-2.0 con condiciones adicionales (source-available) | alternativa |
| `whatsmeow` | whatsapp | Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp… | 2 Intermedio | 49 | MPL-2.0 (OSI copyleft) | alternativa |
| `signal-cli` | whatsapp | Interfaz de línea de comandos y API (JSON-RPC y D-Bus) no oficial para… | 2 Intermedio | 47 | GPL-3.0 (OSI copyleft) | sin grupo |
| `whatsapp-agentkit` | whatsapp | Instrucciones y scripts que guían a Claude Code para construir un bot de… | 2 Intermedio | 41 | MIT (OSI permisiva) | sin grupo |
| `discord-js` | chatbots | Módulo Node.js de referencia para interactuar con la API de Discord y crear… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `python-telegram-bot` | chatbots | Biblioteca Python asíncrona de referencia para crear bots de Telegram, con… | 2 Intermedio | 68 | LGPL-3.0 (OSI copyleft) | sin grupo |
| `botpress` | chatbots | Hub de SDKs, CLI e integraciones para desarrollar y desplegar conexiones en el… | 2 Intermedio | 53 | MIT (OSI permisiva) | sin grupo |
| `typebot` | chatbots | Constructor visual de chatbots conversacionales, auto-hospedable, para web… | 2 Intermedio | 53 | FSL-1.1-Apache-2.0 (source-available) | sin grupo |
| `rocket-chat` | comunidades | Plataforma de comunicación autoalojable para equipos y atención al cliente, con… | 2 Intermedio | 75 | MIT + licencia Enterprise (ee/) (open-core) | recomendado |
| `mattermost` | comunidades | Plataforma de colaboración autoalojada y open core, alternativa a Slack: chat… | 2 Intermedio | 71 | AGPL-3.0 / Apache-2.0 (herramientas) + Enterprise (open-core) | alternativa |
| `fluxer` | comunidades | Aplicación de mensajería instantánea y llamadas de voz para comunidades, con… | 2 Intermedio | 70 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `element-web` | comunidades | Cliente web Matrix (Element): chats, salas y cifrado E2E contra un homeserver… | 2 Intermedio | 66 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `zulip` | comunidades | Chat de equipo open source con hilos por tema: combina lo mejor del email y del… | 3 Avanzado | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `synapse` | comunidades | Servidor doméstico de Matrix de referencia, mantenido por Element: chat… | 3 Avanzado | 59 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OpenWA (`openwa`)

- **Repo:** https://github.com/rmyndharis/OpenWA · MIT · nivel 2 · 70/100
- **Qué es:** Gateway de API de WhatsApp de código abierto (MIT) y autoalojado, creado en 2026 y con versiones muy frecuentes. Es un proyecto comunitario no oficial que se conecta a WhatsApp mediante clientes de ingeniería inversa, no mediante la Cloud…
- **Cuándo elegirlo:** Casos: Prototipar una integración de mensajería; Consultar estados desde un agente MCP.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; Docker; cuenta y número propios; configuración de autenticación y persistencia; hardware prerequisites; API de IA: no; Docker; cuenta y número propios; configuración de autenticación y persistencia.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/rmyndharis/OpenWA/blob/main/README.md

  ```bash
  # Clone and start
  git clone https://github.com/rmyndharis/OpenWA.git
  cd OpenWA
  docker compose -f docker-compose.dev.yml up -d

  # Access (the dashboard is bundled into the API image and served on the same port)
  # Dashboard: http://localhost:2785
  # API: http://localhost:2785/api
  # Swagger: http://localhost:2785/api/docs
  ```
- **Primera prueba propuesta (no ejecutada):** Abre el dashboard y consulta el estado de una sesión de prueba antes de automatizar mensajes Éxito: Puedes ver sesión, API y permisos del usuario configurado
- **Combina con:** `chatwoot` [18/crm], `typebot` [17/chatbots], `claude-code` [20/terminal]
- **Riesgos y avisos:** Riesgo de bloqueo: no envíes mensajes en frío a números que nunca te escribieron y usa destinatarios que hayan dado su consentimiento. Este proyecto es rmyndharis/OpenWA; MCP HTTP añade herramientas de lectura por defecto y capacidades de escritura se habilitan aparte.

### whatsapp-web.js (`whatsapp-web-js`)

- **Repo:** https://github.com/wwebjs/whatsapp-web.js · Apache-2.0 · nivel 2 · 69/100 · recomendado en «APIs y librerías no oficiales de WhatsApp»
- **Qué es:** Librería Node.js de código abierto (Apache 2.0) para interactuar con WhatsApp Web y construir una API de WhatsApp propia. Es un proyecto comunitario no oficial, activo desde 2019 y con versiones frecuentes (serie 1.34 en 2026).
- **Cuándo elegirlo:** Casos: Estudiar un bot de atención en laboratorio; Conectar eventos WhatsApp Web a una app propia.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node.js; Chrome o Chromium; cuenta y número propios de prueba; sesión WhatsApp Web; hardware prerequisites; API de IA: no; Node.js; Chrome o Chromium; cuenta y número propios de prueba; sesión WhatsApp Web.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install whatsapp-web.js` — fuente: https://github.com/wwebjs/whatsapp-web.js/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Inicia el ejemplo y comprueba estado de autenticación antes de habilitar respuestas automáticas Éxito: Puedes distinguir sesión vinculada y eventos recibidos en el entorno de prueba
- **Combina con:** `activepieces` [1/motores], `ollama` [8/motores], `chatwoot` [18/crm]
- **Alternativas:** `baileys`, `waha`, `evolution-api`, `whatsmeow`
- **Riesgos y avisos:** Alternativas (elige una): baileys, waha, evolution-api. Es un cliente no oficial: WhatsApp puede restringir números que envían mensajes masivos o no…. Automatiza WhatsApp Web y no es la API oficial Meta; las condiciones y estabilidad de esa sesión son independientes del código abierto.

### Baileys (`baileys`)

- **Repo:** https://github.com/WhiskeySockets/Baileys · MIT · nivel 2 · 67/100 · alternativa en «APIs y librerías no oficiales de WhatsApp»
- **Qué es:** Librería de código abierto (MIT) en TypeScript para interactuar con la API de WhatsApp Web mediante WebSockets, mantenida por la comunidad WhiskeySockets.
- **Cuándo elegirlo:** Casos: Aprender el flujo multidispositivo; Conectar eventos de una cuenta propia a una app.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node y TypeScript compatibles; sesión y almacenamiento de credenciales; cuenta de prueba; hardware prerequisites; API de IA: no; Node y TypeScript compatibles; sesión y almacenamiento de credenciales; cuenta de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el ejemplo de conexión y observa cambios de estado sin programar envíos Éxito: Puedes reconocer conexión, desconexión y datos de sesión persistidos
- **Combina con:** `evolution-api`, `activepieces` [1/motores], `litellm` [23/serving]
- **Alternativas:** `whatsapp-web-js`, `waha`, `evolution-api`, `whatsmeow`
- **Riesgos y avisos:** Alternativas (elige una): whatsapp-web-js, waha. Revisa la guía de migración de la versión 7 antes de actualizar. Usa el protocolo WhatsApp Web y no la API oficial; v7 incorpora cambios incompatibles que requieren su guía de migración.

### WAHA (`waha`)

- **Repo:** https://github.com/devlikeapro/waha · Apache-2.0 · nivel 1 · 62/100 · alternativa en «APIs y librerías no oficiales de WhatsApp»
- **Qué es:** WAHA («WhatsApp HTTP API») es una API REST de WhatsApp que instalas en tu propio servidor, de devlike.pro, con licencia Apache 2.0. Desde la versión 2026.6 las funciones de la antigua edición «Plus» están incluidas en la imagen principal.
- **Cuándo elegirlo:** Casos: Prototipar un webhook de mensajería; Evaluar un gateway HTTP para una app propia.
- **Requisitos:** nivel 1: preparación sencilla; Docker; cuenta propia de prueba; configuración de auth y volumen según guía; hardware prerequisites; API de IA: no; Docker; cuenta propia de prueba; configuración de auth y volumen según guía.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -it --rm -p 3000:3000/tcp --name waha devlikeapro/waha` — fuente: https://github.com/devlikeapro/waha/blob/core/README.md
- **Primera prueba propuesta (no ejecutada):** Abre el panel del contenedor de ensayo y comprueba estado de sesión y autenticación Éxito: Puedes reconocer qué motor y sesión están configurados
- **Combina con:** `activepieces` [1/motores], `chatwoot` [18/crm], `typebot` [17/chatbots]
- **Alternativas:** `whatsapp-web-js`, `baileys`, `evolution-api`, `whatsmeow`
- **Riesgos y avisos:** Alternativas (elige una): evolution-api, whatsapp-web-js, baileys. Es una conexión no oficial: evita mensajes masivos o no solicitados. El contenedor --rm del ejemplo es una prueba temporal; para conservar sesiones sigue persistencia y seguridad de la guía.

### evolution-api (`evolution-api`)

- **Repo:** https://github.com/evolution-foundation/evolution-api · Apache-2.0 con condiciones adicionales · nivel 3 · 54/100 · alternativa en «APIs y librerías no oficiales de WhatsApp»
- **Qué es:** Evolution API, API REST para WhatsApp y mensajería multicanal, mantenida por Evolution Foundation. Licencia Apache-2.0 con condiciones adicionales: conservar el logo y el copyright en los componentes frontend y avisar del uso, incluso en…
- **Cuándo elegirlo:** Casos: Conectar atención de WhatsApp a una app; Recibir eventos en una automatización de prueba.
- **Requisitos:** nivel 3: preparación pesada; Docker o Node; PostgreSQL y Redis según ruta; canal y credenciales; cuenta de prueba; hardware prerequisites; API de IA: opcional; Docker o Node; PostgreSQL y Redis según ruta; canal y credenciales; cuenta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull evoapicloud/evolution-api:latest` — fuente: https://github.com/evolution-foundation/evolution-api/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura una instancia de ensayo y consulta su estado antes de habilitar webhooks o respuestas Éxito: Puedes identificar motor, instancia y permisos de acceso
- **Combina con:** `chatwoot` [18/crm], `typebot` [17/chatbots], `dify` [3/visual], `baileys`, `twenty-main` [18/crm]
- **Alternativas:** `whatsapp-web-js`, `baileys`, `waha`, `whatsmeow`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): whatsapp-web-js, waha. La conexión Baileys usa WhatsApp Web de forma no oficial: riesgo de bloqueo del número y de incumplir los…. La conexión WhatsApp Web y Meta Cloud API tienen requisitos distintos; una clave apikey de Evolution no es una clave de modelo.

### whatsmeow (`whatsmeow`)

- **Repo:** https://github.com/tulir/whatsmeow · MPL-2.0 · nivel 2 · 49/100 · alternativa en «APIs y librerías no oficiales de WhatsApp»
- **Qué es:** Librería de Go para la API multidispositivo de WhatsApp Web, creada por Tulir Asokan (autor de los puentes mautrix) con licencia MPL-2.0. Es un proyecto activo sin versiones etiquetadas; el soporte comunitario se hace en una sala de Matrix…
- **Cuándo elegirlo:** Casos: Construir una integración de eventos en Go; Estudiar almacenamiento de sesiones WhatsApp Web.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Go; almacenamiento de sesión; cuenta propia de prueba; hardware prerequisites; API de IA: no; Go; almacenamiento de sesión; cuenta propia de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/tulir/whatsmeow/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el ejemplo de conexión y comprueba los eventos y la sesión guardada Éxito: Puedes reconocer el estado del cliente multidispositivo
- **Combina con:** `activepieces` [1/motores], `ollama` [8/motores], `chatwoot` [18/crm]
- **Alternativas:** `whatsapp-web-js`, `baileys`, `waha`, `evolution-api`
- **Riesgos y avisos:** Cliente no oficial: no lo uses para mensajes masivos ni no solicitados. Biblioteca de protocolo Web multidispositivo; no es una app final ni la API oficial Meta.

### signal-cli (`signal-cli`)

- **Repo:** https://github.com/AsamK/signal-cli · GPL-3.0 · nivel 2 · 47/100
- **Qué es:** Cliente no oficial de código abierto (GPL-3.0) mantenido por AsamK. Maduro y activo; sigue los cambios del protocolo de Signal.
- **Cuándo elegirlo:** Casos: enviar avisos de un servidor a tu móvil por Signal; conectar un asistente o bot a Signal mediante su API JSON-RPC.
- **Requisitos:** nivel 2: preparación media; Java; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/AsamK/signal-cli/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga la release (JRE 25 o binario nativo), vincula signal-cli como dispositivo secundario y envía un mensaje de prueba a ti mismo. Éxito: El mensaje llega a tu app de Signal.
- **Combina con:** `openclaw` [21/asistentes], `activepieces` [1/motores], `uptime-kuma` [22/infraestructura]
- **Riesgos y avisos:** Hay envoltorios REST de la comunidad (no catalogados) sobre signal-cli.

### whatsapp-agentkit (`whatsapp-agentkit`)

- **Repo:** https://github.com/Hainrixz/whatsapp-agentkit · MIT · nivel 2 · 41/100
- **Qué es:** Kit de código abierto (MIT), escrito en español para builders de Latinoamérica, que usa Claude Code para crear un agente de WhatsApp que atiende a clientes. Es un proyecto pequeño y reciente (2026) sin versiones publicadas.
- **Cuándo elegirlo:** Casos: Preparar un asistente de preguntas frecuentes; Diseñar una consulta de horarios en un número de prueba.
- **Requisitos:** nivel 2: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP), requiere clave de API; Claude Code; Python >=3.11; clave Anthropic; Zernio o Meta Cloud API; negocio ficticio para ensayo; hardware prerequisites; API de IA: sí; Claude Code; Python >=3.11; clave Anthropic; Zernio o Meta Cloud API; negocio ficticio para ensayo.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md

  ```bash
  git clone https://github.com/Hainrixz/whatsapp-agentkit.git
  cd whatsapp-agentkit
  bash start.sh
  ```
- **Primera prueba propuesta (no ejecutada):** Completa la entrevista con datos ficticios y revisa el código y credenciales requeridas antes de conectar un número Éxito: Puedes explicar cómo entra un mensaje, qué modelo responde y qué servicio lo envía
- **Combina con:** `claude-code` [20/terminal], `chatwoot` [18/crm], `coolify` [22/infraestructura]
- **Riesgos y avisos:** Costes: la Cloud API de Meta cobra respuestas de servicio desde el 1 de octubre de 2026 (con 1.000 gratis al mes por número, según el README) y Railway ya no…. El tiempo anunciado es una estimación del autor y no una instalación garantizada; el plan de Claude Code no paga la API del bot.

### discord.js (`discord-js`)

- **Repo:** https://github.com/discordjs/discord.js · Apache-2.0 · nivel 2 · 71/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) mantenida por la comunidad discord.js. Muy madura; sigue las versiones de la API de Discord.
- **Cuándo elegirlo:** Casos: crear un bot de Discord con comandos de barra para tu comunidad; conectar un asistente de IA a un servidor de Discord.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install discord.js` — fuente: https://github.com/discordjs/discord.js/blob/main/apps/guide/content/docs/legacy/preparations/installation.mdx
- **Primera prueba propuesta (no ejecutada):** Instala con `npm install discord.js`, crea una aplicación en el portal de desarrolladores de Discord y ejecuta un bot que responda a un comando. Éxito: El bot aparece en línea y responde al comando en tu servidor de pruebas.
- **Combina con:** `vercel-ai` [3/ts], `ollama` [8/motores], `coolify` [22/infraestructura]
- **Riesgos y avisos:** Respeta los términos de desarrolladores de Discord y los límites de tasa.

### python-telegram-bot (`python-telegram-bot`)

- **Repo:** https://github.com/python-telegram-bot/python-telegram-bot · LGPL-3.0 · nivel 2 · 68/100
- **Qué es:** Biblioteca de código abierto (LGPL-3.0 según su README; la API de GitHub la marca como GPL-3.0) mantenida por voluntarios. Muy madura; sigue de cerca cada versión de la Bot API.
- **Cuándo elegirlo:** Casos: crear un bot de Telegram que responda comandos y envíe avisos; conectar un modelo de lenguaje a un chat de Telegram.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install python-telegram-bot --upgrade` — fuente: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install python-telegram-bot --upgrade`, crea un token con BotFather y ejecuta el ejemplo echobot. Éxito: El bot responde en Telegram repitiendo tus mensajes.
- **Combina con:** `ollama` [8/motores], `langgraph` [3/py], `coolify` [22/infraestructura]
- **Riesgos y avisos:** Para bots con IA ya listos, revisa también openclaw o hermes-agent, que integran Telegram como canal.

### Botpress (`botpress`)

- **Repo:** https://github.com/botpress/botpress · MIT · nivel 2 · 53/100
- **Qué es:** Repositorio de herramientas de desarrollo de Botpress Cloud, la plataforma comercial de chatbots y asistentes con IA de Botpress, con licencia MIT.
- **Cuándo elegirlo:** Casos: Aprender el SDK de integraciones Botpress; Prototipar una conexión para un chatbot alojado.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node y gestor de paquetes; cuenta Botpress para desplegar una integración; TypeScript; hardware prerequisites; API de IA: depends; Node y gestor de paquetes; cuenta Botpress para desplegar una integración; TypeScript.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g @botpress/cli # for npm` — fuente: https://github.com/botpress/botpress/blob/master/readme.md
- **Primera prueba propuesta (no ejecutada):** Genera una integración con bp init y revisa su definición antes de desplegarla Éxito: Puedes identificar eventos, acciones y configuración de la integración
- **Combina con:** `activepieces` [1/motores], `odoo` [18/crm], `cal.diy` [18/reservas]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. La ficha del catálogo debe entenderse como herramientas para Botpress Cloud, no como plataforma autoalojada. El repositorio actual es un hub de SDKs e integraciones; clonarlo no instala una plataforma completa auto-hospedada equivalente a Cloud.

### Typebot (`typebot`)

- **Repo:** https://github.com/baptisteArno/typebot.io · FSL-1.1-Apache-2.0 · nivel 2 · 53/100
- **Qué es:** Constructor de chatbots visual y autoalojable creado por Baptiste Arnaud. Se distribuye bajo Functional Source License 1.1 con conversión futura a Apache 2.0 (FSL-1.1-Apache-2.0), un modelo «Fair Source» con restricciones de uso…
- **Cuándo elegirlo:** Casos: Crear un formulario conversacional; Probar un flujo de preguntas frecuentes.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Cuenta o despliegue; bloques y canal elegidos; proveedor solo para AI; hardware prerequisites; API de IA: opcional; Cuenta o despliegue; bloques y canal elegidos; proveedor solo para AI.
- **Instalación (documentada en la fuente; no ejecutada):** `docker-compose up -d` — fuente: https://github.com/baptisteArno/typebot.io/blob/main/apps/docs/self-hosting/deploy/docker.mdx
- **Primera prueba propuesta (no ejecutada):** Crea un flujo de dos preguntas con respuestas fijas y comprueba la rama elegida Éxito: El resultado guarda respuestas y recorre el camino esperado
- **Combina con:** `evolution-api` [17/whatsapp], `chatwoot` [18/crm], `openwa` [17/whatsapp], `waha` [17/whatsapp], `formbricks` [18/reservas]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Revisa la FSL antes de ofrecer Typebot como servicio a terceros. Es fair-source con condiciones específicas; no se debe presentar toda modalidad como software sin restricciones comerciales.

### Rocket.Chat (`rocket-chat`)

- **Repo:** https://github.com/RocketChat/Rocket.Chat · MIT + licencia Enterprise (ee/) · nivel 2 · 75/100 · recomendado en «Chat de equipo auto-hospedado»
- **Qué es:** Plataforma de comunicación de Rocket.Chat Technologies. El núcleo es MIT y las carpetas ee/ tienen licencia Enterprise propia. Muy madura; usada por grandes organizaciones.
- **Cuándo elegirlo:** Casos: sustituir Slack o Teams por un chat de equipo en tu servidor; atender clientes de varios canales desde una bandeja compartida.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo snap install rocketchat-desktop` — fuente: https://github.com/RocketChat/Rocket.Chat/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Rocket.Chat con Docker Compose siguiendo su guía, crea un espacio de trabajo y un canal. Éxito: Puedes chatear en el canal desde la web y la app móvil.
- **Combina con:** `activepieces` [1/motores], `ollama` [8/motores], `coolify` [22/infraestructura]
- **Alternativas:** `mattermost`, `zulip`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): mattermost.

### Mattermost (`mattermost`)

- **Repo:** https://github.com/mattermost/mattermost · AGPL-3.0 / Apache-2.0 (herramientas) + Enterprise · nivel 2 · 71/100 · alternativa en «Chat de equipo auto-hospedado»
- **Qué es:** Plataforma de colaboración open core de Mattermost, Inc. El código fuente se licencia bajo AGPL-3.0 o licencia comercial; los binarios oficiales, bajo MIT; hay ediciones de pago. Muy madura.
- **Cuándo elegirlo:** Casos: montar un chat de equipo privado en tu infraestructura; integrar alertas de CI o monitorización en canales del equipo.
- **Requisitos:** nivel 2: preparación media; TypeScript; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mattermost/mattermost/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Mattermost con Docker siguiendo la guía oficial, crea un equipo y un canal y añade un webhook entrante. Éxito: Los mensajes enviados al webhook aparecen en el canal.
- **Combina con:** `activepieces` [1/motores], `ollama` [8/motores], `coolify` [22/infraestructura]
- **Alternativas:** `rocket-chat`, `zulip`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): rocket-chat.

### fluxer (`fluxer`)

- **Repo:** https://github.com/fluxerapp/fluxer · AGPL-3.0 · nivel 2 · 70/100
- **Qué es:** Aplicación de mensajería instantánea y llamadas de voz (VoIP) gratuita y de código abierto para amigos, grupos y comunidades, con licencia AGPL-3.0 o posterior.
- **Cuándo elegirlo:** Casos: Organizar conversación de una comunidad; Probar una interfaz de mensajería y VoIP propia.
- **Requisitos:** nivel 2: preparación media; Cliente o servidor elegido; micrófono para voz; cuenta de prueba; hardware prerequisites; API de IA: no; Cliente o servidor elegido; micrófono para voz; cuenta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `flatpak install https://pkgs.fluxer.com/flatpak/fluxer.flatpakref` — fuente: https://github.com/fluxerapp/fluxer/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una comunidad de ensayo y comprueba permisos de un canal y una llamada de prueba Éxito: Puedes distinguir miembros, canales y permisos configurados
- **Combina con:** `activepieces` [1/motores], `ollama` [8/motores], `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La AGPL obliga a publicar tus cambios si ofreces una versión modificada como servicio. Es una plataforma comunitaria independiente, no una integración WhatsApp; por eso cambia de subcategoría.

### Element Web (`element-web`)

- **Repo:** https://github.com/element-hq/element-web · AGPL-3.0 · nivel 2 · 66/100
- **Qué es:** Cliente Matrix AGPL de Element.
- **Cuándo elegirlo:** Casos: UI web delante de Synapse propio; salas E2E para un equipo.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --rm -p 127.0.0.1:80:80 vectorim/element-web` — fuente: https://github.com/element-hq/element-web/blob/develop/docs/install.md
- **Primera prueba propuesta (no ejecutada):** Configura element-web contra tu Synapse de lab según docs Element. Éxito: Inicias sesión en el cliente web.
- **Combina con:** `synapse`, `mattermost`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### Zulip (`zulip`)

- **Repo:** https://github.com/zulip/zulip · Apache-2.0 · nivel 3 · 63/100 · alternativa en «Chat de equipo auto-hospedado»
- **Qué es:** Team chat Apache-2.0 con topic threading.
- **Cuándo elegirlo:** Casos: chat interno con hilos por ticket; comunidad open source autoalojada.
- **Requisitos:** nivel 3: servidor de chat con instalador propio y varios servicios; Python, package.json, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install zulip` — fuente: https://github.com/zulip/zulip/blob/main/api_docs/installation-instructions.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://zulip.readthedocs.io para un install de lab o usa Zulip Cloud de prueba. Éxito: Creas un stream y un topic.
- **Combina con:** `synapse`
- **Alternativas:** `rocket-chat`, `mattermost`

### Synapse (`synapse`)

- **Repo:** https://github.com/element-hq/synapse · AGPL-3.0 · nivel 3 · 59/100
- **Qué es:** Implementación de servidor de Matrix de código abierto (AGPL-3.0, o licencia comercial de Element) mantenida por Element. Muy madura.
- **Cuándo elegirlo:** Casos: alojar tu propio servidor de chat federado para un grupo o comunidad; conectar usuarios con otros servidores Matrix manteniendo tus datos.
- **Requisitos:** nivel 3: preparación pesada; Python, Cargo.toml, pyproject.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/element-hq/synapse/blob/develop/README.rst
- **Primera prueba propuesta (no ejecutada):** Instala Synapse con paquetes o Docker siguiendo la guía oficial, crea un usuario y conéctate con un cliente Matrix. Éxito: Puedes chatear desde el cliente y unirte a salas de otros servidores federados.
- **Combina con:** `grafana` [10/bi], `caddy` [22/infraestructura], `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Para despliegues sencillos, servidores Matrix más ligeros (no catalogados) pueden bastar.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-17.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «WhatsApp, mensajería y chatbots», lee `docs/alexandria/categoria-17.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-17.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
