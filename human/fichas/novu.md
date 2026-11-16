[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Email, marketing y notificaciones

# 🔔 novu

> Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.3k | MIT + licencia Enterprise (enterprise/packages) | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** MIT + licencia Enterprise (enterprise/packages). Fuente: [LICENSE](https://github.com/novuhq/novu/blob/next/LICENSE-ENTERPRISE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Infraestructura de comunicación de código abierto para productos y agentes, de Novu. Sigue un modelo «open core»: el núcleo es abierto y la carpeta `enterprise` requiere licencia comercial; publica versiones con frecuencia.

## ¿Qué hace?

Envía notificaciones por bandeja in-app, email, SMS, push y chat con una sola API, con flujos, resúmenes («digests») y un componente de bandeja incrustable. Su capa ACI (Agent Communication Infrastructure) conecta cualquier agente que ya tengas (Claude, AI SDK, LangGraph o propio) a Slack, Microsoft Teams, Telegram, WhatsApp, email o una bandeja in-app, normalizando los mensajes entrantes y devolviendo las respuestas con hilos, reacciones y formato por canal.

## ¿Cómo lo hace?

Es un monorepo en TypeScript con API, panel de administración y SDK (incluido `@novu/framework` y componentes para React). Unifica proveedores por canal (por ejemplo SendGrid para email) detrás de un modelo de conversación único. Se usa en Novu Cloud o autoalojado [DATO NO VERIFICADO: requisitos de infraestructura del autoalojamiento, no descritos en el README].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AI SDK (Vercel)](vercel-ai.md) | El README cita el AI SDK entre los agentes que puede conectar a canales como Slack, Teams o email. | Agente con AI SDK funcionando primero; después conecta el canal en Novu y apunta su enrutamiento al agente. |
| [LangGraph](langgraph.md) | Agentes construidos con LangGraph se exponen en Slack, Telegram o email a través de la capa ACI de Novu. | Igual: primero el agente desplegado con un endpoint, luego Novu. |
| [listmonk](listmonk.md) | Novu cubre notificaciones transaccionales e in-app; listmonk, boletines y listas masivas (combinación por arquitectura). | Independientes; usa dominios o subdominios de envío separados para no mezclar reputación. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada @novu/framework@v2.14.0 (2026-09-28) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/novuhq/novu/blob/next/README.md) · [2](https://docs.novu.co/platform/quickstart/react) · [3](https://docs.novu.co/platform/integrations/email/sendgrid)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La infraestructura no necesita un modelo para notificar; proveedores de canal, Cloud y módulos Enterprise tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Novu conecta agentes y productos a canales; no es el agente ni incluye el modelo que toma decisiones |
| Coste | El coste depende del proveedor o la ruta. La infraestructura no necesita un modelo para notificar; proveedores de canal, Cloud y módulos Enterprise tienen costes propios |
| Equipo | Preparación según la ruta elegida. Proyecto de notificaciones; credenciales del canal; destino propio de prueba |

Novu conecta agentes y productos a canales; no es el agente ni incluye el modelo que toma decisiones

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto de notificaciones
- credenciales del canal
- destino propio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install @novu/react
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Install @novu/react»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://docs.novu.co/platform/quickstart/react?utm_source=github&utm_medium=readme&utm_campaign=react-starter-link)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar novu para mi objetivo y necesito pasos guiados. Lee https://docs.novu.co/platform/quickstart/react?utm_source=github&utm_medium=readme&utm_campaign=react-starter-link. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Define un evento ficticio y comprueba su preview y entrega en un canal de ensayo.

**Qué comprobar:** Puedes rastrear evento, plantilla y estado de entrega.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir una bandeja de notificaciones a una app
- Coordinar avisos de email y chat

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir una bandeja de notificaciones a una app; Coordinar avisos de email y chat | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Novu conecta agentes y productos a canales; no es el agente ni incluye el modelo que toma decisiones

## Stack y modelos

- **Stack:** Proyecto de notificaciones; credenciales del canal; destino propio de prueba
- **Etiquetas:** `automation` `email` `typescript`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Enlaces

- 🐙 GitHub: [novuhq/novu](https://github.com/novuhq/novu)
- 🌐 Web: <https://go.novu.co/github>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/novuhq/novu/blob/next/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
