[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Chatbots y asistentes conversacionales

# 🤖 Botpress

> Hub de SDKs, CLI e integraciones para desarrollar y desplegar conexiones en el ecosistema Botpress.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Repositorio de herramientas de desarrollo de Botpress Cloud, la plataforma comercial de chatbots y asistentes con IA de Botpress, con licencia MIT. No contiene el servidor autoalojable: la versión local v12 vive en el repositorio aparte `botpress/v12`, cuyo último lanzamiento visible aquí es de 2023.

## ¿Qué hace?

Reúne las integraciones públicas del Botpress Hub (WhatsApp, Telegram, Messenger, Slack, Teams, HubSpot, Salesforce, Zendesk, Odoo, n8n, Cal.com, Stripe, OpenAI, Anthropic, Groq, Mistral y muchas más), las herramientas de desarrollo (CLI, SDK y cliente de API), bots de ejemplo «como código» y, próximamente, plugins para Botpress Studio. Sirve para crear o modificar integraciones y bots que se ejecutan en Botpress Cloud.

## ¿Cómo lo hace?

Es un monorepo en TypeScript. Se instala la CLI con `npm install -g @botpress/cli` para desarrollar, probar y publicar integraciones en el Hub, o para definir bots con el SDK. Los bots se ejecutan en la nube de Botpress, que requiere cuenta.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Botpress puede llamar a un webhook de Activepieces (o recibir llamadas de su pieza HTTP) para conectar el bot con otros servicios. (combinación por arquitectura) | Cuenta en Botpress y Activepieces accesible por internet; protege el webhook con un secreto. |
| [Odoo](odoo.md) | Integración oficial con Odoo para consultar o registrar datos del ERP/CRM desde el bot. | Odoo con usuario de API; después configura la integración. |
| [cal.diy](cal-diy.md) | Existe una integración oficial con Cal.com; cal.diy es su edición comunitaria, así que la compatibilidad con una instancia propia está [DATO NO VERIFICADO]. | Instancia de cal.diy accesible por internet y token de API antes de configurar la integración. |

**Notas:** La ficha del catálogo debe entenderse como herramientas para Botpress Cloud, no como plataforma autoalojada.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v12.30.9 (2023-06-22) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/botpress/botpress/blob/master/readme.md) · [2](https://github.com/botpress/botpress/tree/master/integrations)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Los paquetes del repositorio son MIT; Botpress Cloud, modelos y canales tienen sus precios y límites |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El repositorio actual es un hub de SDKs e integraciones; clonarlo no instala una plataforma completa auto-hospedada equivalente a Cloud |
| Coste | El coste depende del proveedor o la ruta. Los paquetes del repositorio son MIT; Botpress Cloud, modelos y canales tienen sus precios y límites |
| Equipo | Preparación según la ruta elegida. Node y gestor de paquetes; cuenta Botpress para desplegar una integración; TypeScript |

El repositorio actual es un hub de SDKs e integraciones; clonarlo no instala una plataforma completa auto-hospedada equivalente a Cloud

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node y gestor de paquetes
- cuenta Botpress para desplegar una integración
- TypeScript

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npm install -g @botpress/cli # for npm
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/botpress/botpress/blob/master/readme.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Botpress para mi objetivo y necesito pasos guiados. Lee https://github.com/botpress/botpress/blob/master/readme.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una integración con bp init y revisa su definición antes de desplegarla.

**Qué comprobar:** Puedes identificar eventos, acciones y configuración de la integración.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender el SDK de integraciones Botpress
- Prototipar una conexión para un chatbot alojado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender el SDK de integraciones Botpress; Prototipar una conexión para un chatbot alojado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El repositorio actual es un hub de SDKs e integraciones; clonarlo no instala una plataforma completa auto-hospedada equivalente a Cloud

## Stack y modelos

- **Stack:** Node y gestor de paquetes; cuenta Botpress para desplegar una integración; TypeScript
- **Etiquetas:** `chatbot` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [botpress/botpress](https://github.com/botpress/botpress)
- 🌐 Web: <https://botpress.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/botpress/botpress/blob/master/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
