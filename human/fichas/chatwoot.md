[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# 💬 chatwoot

> Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.9k | NOASSERTION | Ruby | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Plataforma de atención al cliente de código abierto (MIT) y autoalojable, alternativa a Intercom o Zendesk.

## ¿Qué hace?

Reúne en una bandeja omnicanal las conversaciones de chat web, email, Facebook, Instagram, Twitter, WhatsApp, Telegram, Line y SMS, con asignación automática, respuestas predefinidas, notas privadas, contactos, campañas, centro de ayuda y reportes con CSAT. Incluye Captain, un agente de IA que responde consultas frecuentes; su disponibilidad en la edición comunitaria es [DATO NO VERIFICADO].

## ¿Cómo lo hace?

Backend en Ruby y frontend en Vue, según los lenguajes del repositorio en GitHub. En Docker se despliega con PostgreSQL, Redis y workers Sidekiq para tareas en segundo plano, y necesita variables de entorno correctas para cada función. Se integra con Slack, Dialogflow, Shopify, Linear y Google Translate y permite incrustar herramientas internas como Dashboard Apps.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [evolution-api](evolution-api.md) | Aporta el canal de WhatsApp mediante la integración nativa que Evolution tiene con Chatwoot. | Chatwoot primero; después configura la integración desde la instancia de Evolution. |
| [n8n](n8n.md) | Automatiza acciones (crear contactos, etiquetar, notificar) llamando a la API de Chatwoot desde nodos HTTP (combinación por arquitectura). | Independientes; crea un token de acceso en Chatwoot y úsalo en n8n. |

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/chatwoot/chatwoot/blob/develop/README.md) · [2](https://www.chatwoot.com/docs/self-hosted/deployment/docker) · [3](https://api.github.com/repos/chatwoot/chatwoot/languages) · [4](https://github.com/evolution-foundation/evolution-api/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Community, Cloud y Enterprise tienen condiciones distintas; canales y funciones AI pueden consumir servicios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El helpdesk no incluye por sí solo la facturación de WhatsApp ni modelos; configura cada integración por separado |
| Coste | El coste depende del proveedor o la ruta. Community, Cloud y Enterprise tienen condiciones distintas; canales y funciones AI pueden consumir servicios |
| Equipo | Preparación según la ruta elegida. Cuenta o servidor; canal de prueba; proveedor solo para funciones AI |

El helpdesk no incluye por sí solo la facturación de WhatsApp ni modelos; configura cada integración por separado

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta o servidor
- canal de prueba
- proveedor solo para funciones AI

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/chatwoot/chatwoot/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar chatwoot para mi objetivo y necesito pasos guiados. Lee https://github.com/chatwoot/chatwoot/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una bandeja de ensayo y recorre una conversación ficticia con etiquetas y asignación.

**Qué comprobar:** Puedes seguir estado, agente asignado e historial de la conversación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar una mesa de soporte
- Comparar atención humana y asistencia AI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar una mesa de soporte; Comparar atención humana y asistencia AI | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El helpdesk no incluye por sí solo la facturación de WhatsApp ni modelos; configura cada integración por separado

## Stack y modelos

- **Stack:** Cuenta o servidor; canal de prueba; proveedor solo para funciones AI
- **Etiquetas:** `automation` `crm` `ruby` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Enlaces

- 🐙 GitHub: [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)
- 🌐 Web: <https://www.chatwoot.com/help-center>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/chatwoot/chatwoot/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
