[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# 👥 twenty-main

> CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.9k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

CRM de código abierto pensado para equipos técnicos, de Twenty (twentyhq), que se construye, despliega y versiona como el resto del código. Es muy activo (versión 2.58 en 2026); su licencia no figura como estándar en GitHub y combina código abierto con partes comerciales [DATO NO VERIFICADO: reparto exacto de licencias].

## ¿Qué hace?

Gestiona empresas, personas, oportunidades y tareas con objetos, campos y vistas personalizables. Permite crear «apps» propias con objetos, vistas, agentes y funciones lógicas definidas como código y publicarlas en tu espacio de trabajo. Se usa en la nube de Twenty o autoalojado.

## ¿Cómo lo hace?

Backend NestJS en TypeScript con BullMQ, PostgreSQL y Redis, y frontend en React. Las apps se crean con la CLI (`npm install -g twenty`, `twenty app init`, `twenty app publish`) y el SDK `twenty-sdk`; hay skills oficiales para agentes de código instalables con `npx skills add`. El autoalojamiento se hace con Docker Compose según su documentación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Twenty publica skills oficiales para que un agente de código cree objetos, vistas y lógica de apps del CRM. | Instala la CLI de Twenty y las skills; inicia sesión en tu espacio con `twenty auth login` antes de publicar. |
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `twenty` para usar twenty-main en flujos. | twenty-main en marcha con sus credenciales; después añade la pieza `twenty` en un flujo de Activepieces. |
| [evolution-api](evolution-api.md) | Registrar conversaciones de WhatsApp como actividades del CRM con un flujo de Activepieces (pieza oficial de Twenty y webhook de Evolution API) o un servicio intermedio (combinación por arquitectura). | Evolution API y Activepieces primero; después el flujo que escribe en Twenty. |
| [cal.diy](cal-diy.md) | Crear o actualizar oportunidades cuando alguien reserva una cita (combinación por arquitectura, mediante webhooks y un flujo intermedio). | Configura el webhook de reservas en cal.diy apuntando al flujo que escribe en Twenty. |
| [docuseal](docuseal.md) | Combinación recíproca: docuseal lo enlaza como «Registrar contratos firmados en las oportunidades del CRM (combinación por arquitectura)». | Orden indicado desde docuseal: Usa un flujo intermedio con el webhook de DocuSeal. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada twenty/v2.58.0 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/twentyhq/twenty/blob/main/README.md) · [2](https://docs.twenty.com/developers/self-host/capabilities/docker-compose) · [3](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/twenty)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. CRM, hosting y AI tienen costes por ruta; las skills de desarrollo usan el agente anfitrión |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. El CLI twenty app init crea una extensión y no todo el servidor CRM; para usar el producto elige su instalación o servicio |
| Coste | El coste depende del proveedor o la ruta. CRM, hosting y AI tienen costes por ruta; las skills de desarrollo usan el agente anfitrión |
| Equipo | Preparación según la ruta elegida. CRM o entorno self-host; Node y CLI solo para construir apps; modelo si activas AI |

El CLI twenty app init crea una extensión y no todo el servidor CRM; para usar el producto elige su instalación o servicio

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- CRM o entorno self-host
- Node y CLI solo para construir apps
- modelo si activas AI

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/twentyhq/twenty/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar twenty-main para mi objetivo y necesito pasos guiados. Lee https://github.com/twentyhq/twenty/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un objeto y dos registros ficticios y revisa sus relaciones antes de añadir automatización.

**Qué comprobar:** Puedes consultar registros y reconocer la estructura de campos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Modelar un proceso comercial propio
- Desarrollar una app sobre un CRM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Modelar un proceso comercial propio; Desarrollar una app sobre un CRM | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El CLI twenty app init crea una extensión y no todo el servidor CRM; para usar el producto elige su instalación o servicio

## Stack y modelos

- **Stack:** CRM o entorno self-host; Node y CLI solo para construir apps; modelo si activas AI
- **Etiquetas:** `automation` `crm` `typescript` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [EspoCRM](espocrm.md) | 3.6k | CRM web ligero y autoalojable para gestionar contactos, cuentas, oportunidades y actividades, con API REST y personalización sin código. |
| [SuiteCRM](suitecrm.md) | 5.9k | CRM open source clásico (fork de SugarCRM): contactos, oportunidades, casos y portal en PHP. |
| [Odoo](odoo.md) | 55.8k | Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. |

## Enlaces

- 🐙 GitHub: [twentyhq/twenty](https://github.com/twentyhq/twenty)
- 🌐 Web: <https://twenty.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/twentyhq/twenty/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
