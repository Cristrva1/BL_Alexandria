[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 n8n

> Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 211k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

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

Conecta cualquier app con cualquier otra en tu propio servidor, sin pagar una suscripción mensual por cada flujo.

## Por qué destaca

Se ha convertido en un estándar de facto para automatización self-hosted, muy adoptado por su enorme catálogo de nodos y su fuerte integración de IA (LangChain, MCP). Su comunidad y su documentación lo hacen el punto de partida habitual.

## Cómo funciona

Encadena nodos (triggers, transformaciones, integraciones) en un grafo de workflow ejecutado por un runtime Node.js, con nodos de IA basados en LangChain y soporte MCP. Los workflows se exportan como JSON, lo que permite versionarlos.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- n8n Cloud o un entorno para el despliegue propio indicado en su documentación.

1. Elige servicio gestionado o despliegue propio; son instalaciones y costes diferentes.
2. Crea un primer workflow con un disparador y una acción sin IA.
3. Añade un nodo de modelo solo si lo necesitas y configura su proveedor o el backend local correspondiente.

[Instrucciones originales de instalación](https://github.com/n8n-io/n8n/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar n8n para mi objetivo y necesito pasos guiados. Lee https://github.com/n8n-io/n8n/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Extraer leads → enriquecer con IA → notificar
- Pipelines de negocio sin SaaS cerrado
- Workflows versionados como JSON junto al código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el motor central de automatización con máximo catálogo | buscas algo minimalista o sin self-host |

**Limitaciones:** La versión self-host comunitaria tiene límites en ejecuciones y usuarios; algunas funciones avanzadas requieren licencia.

## Stack y modelos

- **Stack:** Node.js, TypeScript, Docker
- **Etiquetas:** `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n-mcp](n8n-mcp.md) | 23.3k | Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. |
| [n8n-skills](n8n-skills.md) | 6.6k | Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas. |
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [activepieces](activepieces.md) | 25.5k | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. |
| [huginn](huginn.md) | 50.5k | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". |
| [Windmill](windmill.md) | 18.6k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Node-RED](node-red.md) | 23.8k | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. |

## Enlaces

- 🐙 GitHub: [n8n-io/n8n](https://github.com/n8n-io/n8n)
- 🌐 Web: <https://n8n.io>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/n8n-io/n8n/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
