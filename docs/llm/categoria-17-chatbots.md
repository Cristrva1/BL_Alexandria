# Alexandría para agentes · Chatbots y asistentes conversacionales

Categoría 17 «WhatsApp, mensajería y chatbots» › subcategoría `chatbots`. 4 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=17&sub=chatbots · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `discord-js` | Módulo Node.js de referencia para interactuar con la API de Discord y crear… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `python-telegram-bot` | Biblioteca Python asíncrona de referencia para crear bots de Telegram, con… | 2 Intermedio | 68 | LGPL-3.0 (OSI copyleft) | sin grupo |
| `botpress` | Hub de SDKs, CLI e integraciones para desarrollar y desplegar conexiones en el… | 2 Intermedio | 53 | MIT (OSI permisiva) | sin grupo |
| `typebot` | Constructor visual de chatbots conversacionales, auto-hospedable, para web… | 2 Intermedio | 53 | FSL-1.1-Apache-2.0 (source-available) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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
- **Combina con:** `evolution-api` [17/whatsapp], `chatwoot` [18/crm], `openwa` [17/whatsapp], `waha` [17/whatsapp], `formbricks` [18/encuestas]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Revisa la FSL antes de ofrecer Typebot como servicio a terceros. Es fair-source con condiciones específicas; no se debe presentar toda modalidad como software sin restricciones comerciales.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-17-chatbots.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Chatbots y asistentes conversacionales», lee `docs/alexandria/categoria-17-chatbots.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-17-chatbots.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
