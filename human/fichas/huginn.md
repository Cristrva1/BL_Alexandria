[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🤖 huginn

> Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú".

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.5k | MIT | Ruby | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Vigila webs, feeds y APIs y dispara acciones cuando algo cambia, todo alojado por ti y sin depender de terceros.

## Por qué destaca

Proyecto veterano y muy respetado en la comunidad open-source para monitoreo y scraping, valorado por su privacidad y su modelo de agentes encadenables. Su longevidad lo hace una opción estable para flujos de vigilancia.

## Cómo funciona

Define "agents" que hacen polling o reciben webhooks y se conectan entre sí pasando eventos (la salida de uno alimenta al siguiente), sobre un stack Ruby on Rails con base de datos. Cada agent tiene un tipo (trigger, acción, filtro) y se configura por UI o YAML.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/huginn/huginn/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar huginn para mi objetivo y necesito pasos guiados. Lee https://github.com/huginn/huginn/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Vigilar fuentes externas y disparar acciones
- Scraping + reglas de automatización
- Encadenar eventos entre servicios sin SaaS

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| automatizas tareas orientadas a eventos y valoras la privacidad | quieres editor visual moderno o IA nativa (n8n) |

**Limitaciones:** Proyecto veterano con ritmo de mantenimiento lento; sin IA integrada y UI menos pulida que alternativas modernas.

## Stack y modelos

- **Stack:** Ruby on Rails, MySQL/PostgreSQL, self-host
- **Etiquetas:** `automation` `ruby` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [novu](novu.md) | 40.3k | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [Node-RED](node-red.md) | 23.8k | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. |

## Enlaces

- 🐙 GitHub: [huginn/huginn](https://github.com/huginn/huginn)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/huginn/huginn/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
