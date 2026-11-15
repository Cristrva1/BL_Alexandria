[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# 💬 chatwoot

> Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.9k | NOASSERTION | Ruby | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Reúne WhatsApp, email, web chat y redes en una sola bandeja, con paso a un humano cuando el bot no basta. Alternativa abierta a Intercom o Zendesk.

## Por qué destaca

Es una de las alternativas open-source más populares a Intercom/Zendesk, valorada por centralizar el soporte multicanal con handoff humano y asignación de tickets. Su comunidad activa y su integración con canales la hacen apta para producción.

## Cómo funciona

Centraliza conversaciones por canal en una bandeja con tickets y agentes, sobre un stack Ruby on Rails con PostgreSQL y Redis para tiempo real. Los agentes responden desde un panel unificado y los bots pueden intervenir antes del handoff.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/chatwoot/chatwoot/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar chatwoot para mi objetivo y necesito pasos guiados. Lee https://github.com/chatwoot/chatwoot/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Centralizar WhatsApp/web/correo en un panel
- Tickets y agentes con handoff bot→humano
- Soporte multicanal para una agencia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| das soporte por varios canales y necesitas handoff humano | solo necesitas enviar mensajes salientes (evolution-api) |

**Limitaciones:** Self-host con varios componentes (app, worker, Redis, Postgres); el setup y las actualizaciones corren por tu cuenta.

## Stack y modelos

- **Stack:** Ruby on Rails, Vue.js, PostgreSQL, Redis, Docker
- **Etiquetas:** `automation` `crm` `ruby` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [novu](novu.md) | 40.3k | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. |

## Enlaces

- 🐙 GitHub: [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)
- 🌐 Web: <https://www.chatwoot.com/help-center>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/chatwoot/chatwoot/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
