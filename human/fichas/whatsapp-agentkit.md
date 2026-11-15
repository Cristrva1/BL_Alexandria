[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 🤖 whatsapp-agentkit

> Plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de programar, partiendo de preguntas sobre tu negocio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 567 | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo de APIs o servicios. La plantilla pide una clave de Anthropic para el bot. Usar Claude Code para construirlo no sustituye la autenticación del bot. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Arranca un bot de WhatsApp con IA sin escribir código, a partir de una plantilla guiada.

## Por qué destaca

Baja drásticamente la barrera de entrada al delegar la generación del código en Claude Code, ideal para arranques rápidos y perfiles no técnicos. El resultado es código real que luego puedes editar, no una caja negra.

## Cómo funciona

Un flujo de preguntas conversacionales alimenta a Claude Code, que autogenera el código del bot (Node.js/Python) y la configuración del webhook de WhatsApp. El asistente hace las veces de scaffolder guiado por tus respuestas.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whatsapp-agentkit para mi objetivo y necesito pasos guiados. Lee https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Prototipo de atención al cliente
- Setup de webhook por preguntas conversacionales
- Demo de ventas por WhatsApp en una tarde

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres arrancar sin partir de cero y te vale con lo que Claude Code genere | necesitas control fino del stack o ya tienes el bot hecho |

## Stack y modelos

- **Stack:** Node.js/Python, APIs de WhatsApp
- **Etiquetas:** `agents` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [n8n-mcp](n8n-mcp.md) | 23.3k | Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. |

## Enlaces

- 🐙 GitHub: [Hainrixz/whatsapp-agentkit](https://github.com/Hainrixz/whatsapp-agentkit)
- 🌐 Web: <https://hainrixz.github.io/whatsapp-agentkit/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
