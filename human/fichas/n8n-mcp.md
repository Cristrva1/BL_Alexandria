[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🔌 n8n-mcp

> Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.3k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. El cliente MCP y la instancia de n8n conservan sus propios requisitos de acceso.

## Por qué destaca

Reduce drásticamente los errores cuando se pide a una IA que arme un workflow de n8n, al darle acceso fiable a los parámetros reales de cada nodo. Su enfoque de "documentación como herramienta MCP" es un patrón replicable para otras plataformas.

## Cómo funciona

Expone herramientas de documentación y, con la configuración correspondiente, de gestión de workflows.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP; una instancia de n8n y sus permisos solo si quieres administrarla.

1. Elige el servidor gestionado o la instalación local según el README.
2. Añade su URL o comando a la configuración MCP del cliente.
3. Comprueba una consulta de documentación. Configura por separado la instancia y credenciales de n8n para operaciones sobre workflows.

[Instrucciones originales de instalación](https://github.com/czlonkowski/n8n-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar n8n-mcp para mi objetivo y necesito pasos guiados. Lee https://github.com/czlonkowski/n8n-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Que Claude investigue parámetros del nodo de Gmail para armar un flujo
- Reducir errores al construir workflows
- Onboarding de IA al catálogo de nodos de n8n

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| generas flujos n8n con IA y quieres menos alucinaciones de parámetros | no usas n8n o construyes los flujos a mano |

## Stack y modelos

- **Stack:** Node.js/TypeScript, MCP
- **Etiquetas:** `automation` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [n8n-skills](n8n-skills.md) | 6.6k | Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas. |

## Enlaces

- 🐙 GitHub: [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)
- 🌐 Web: <https://www.n8n-mcp.com/>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/czlonkowski/n8n-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
