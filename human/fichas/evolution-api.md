[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 🧬 evolution-api

> API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.1k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

API REST de código abierto para WhatsApp y mensajería multicanal, mantenida por Evolution Foundation, con licencia Apache 2.0 y condiciones adicionales de marca.

## ¿Qué hace?

Crea varias instancias de WhatsApp, envía y recibe mensajes y medios desde tus aplicaciones y reenvía eventos a chatbots, CRM o colas. Admite dos conexiones: Baileys, basada en WhatsApp Web, gratuita pero con limitaciones frente a la oficial, y la WhatsApp Cloud API de Meta, que exige cumplir sus políticas y puede cobrar por mensaje.

## ¿Cómo lo hace?

Servidor Node.js 20+ en TypeScript con Express y Prisma sobre PostgreSQL o MySQL, con Redis recomendado como caché. Autentica con un `apikey` en la cabecera y tokens por instancia, publica eventos por webhooks, WebSocket, RabbitMQ, Kafka, SQS, NATS o Pusher y guarda medios en disco o en S3/MinIO. Integra de forma nativa Typebot, Chatwoot, Dify, OpenAI (transcripción de audio), Flowise y n8n.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [n8n](n8n.md) | Pone la lógica del bot en un flujo visual: recibe el webhook del mensaje, consulta un modelo o un CRM y responde por la API de Evolution. | Independientes; configura el webhook de la instancia hacia n8n después de levantar ambos. |
| [chatwoot](chatwoot.md) | Integración nativa: las conversaciones de WhatsApp llegan a la bandeja de Chatwoot para que las atiendan personas. | Chatwoot primero; después configura la integración Chatwoot en la instancia de Evolution con la URL y las credenciales de tu cuenta. |
| [Typebot](typebot.md) | Integración nativa con gestión de disparadores para flujos conversacionales visuales sin programar. | Typebot primero; luego vincula el bot a la instancia. |
| [dify](dify.md) | Integración nativa para responder con agentes o RAG construidos en Dify. | Dify primero, con su app publicada; luego conéctala a la instancia. |

**Notas:** Alternativas (elige una): whatsapp-web-js, waha, baileys. Evolution y Chatwoot necesitan PostgreSQL y Redis; pueden compartir servidor, pero usa bases de datos separadas (recomendación, no probada).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/evolution-foundation/evolution-api/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La API básica no exige LLM; ruta Meta oficial, hosting y bots AI pueden cobrar; la licencia añade condiciones de marca y notificación |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La conexión WhatsApp Web y Meta Cloud API tienen requisitos distintos; una clave apikey de Evolution no es una clave de modelo |
| Coste | El coste depende del proveedor o la ruta. La API básica no exige LLM; ruta Meta oficial, hosting y bots AI pueden cobrar; la licencia añade condiciones de marca y notificación |
| Equipo | Preparación según la ruta elegida. Docker o Node; PostgreSQL y Redis según ruta; canal y credenciales; cuenta de prueba |

La conexión WhatsApp Web y Meta Cloud API tienen requisitos distintos; una clave apikey de Evolution no es una clave de modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o Node
- PostgreSQL y Redis según ruta
- canal y credenciales
- cuenta de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/evolution-foundation/evolution-api/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar evolution-api para mi objetivo y necesito pasos guiados. Lee https://github.com/evolution-foundation/evolution-api/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura una instancia de ensayo y consulta su estado antes de habilitar webhooks o respuestas.

**Qué comprobar:** Puedes identificar motor, instancia y permisos de acceso.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conectar atención de WhatsApp a una app
- Recibir eventos en una automatización de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conectar atención de WhatsApp a una app; Recibir eventos en una automatización de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La conexión WhatsApp Web y Meta Cloud API tienen requisitos distintos; una clave apikey de Evolution no es una clave de modelo

## Stack y modelos

- **Stack:** Docker o Node; PostgreSQL y Redis según ruta; canal y credenciales; cuenta de prueba
- **Etiquetas:** `automation` `whatsapp` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |

## Enlaces

- 🐙 GitHub: [evolution-foundation/evolution-api](https://github.com/evolution-foundation/evolution-api)
- 🌐 Web: <https://evolutionfoundation.com.br>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/evolution-foundation/evolution-api/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
