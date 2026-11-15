[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🛠️ n8n-skills

> Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.6k | MIT | Shell | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas. La skill no sustituye la instancia de n8n ni las credenciales de los servicios de un workflow.

## Por qué destaca

Ataca un problema concreto y frecuente —el JSON de n8n generado por IA suele fallar— reduciendo bucles de error y timeouts. Su foco narrow la hace más eficaz que prompts genéricos para este caso.

## Cómo funciona

Aportan instrucciones y criterios para trabajar con el formato y las conexiones de n8n.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/czlonkowski/n8n-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar n8n-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/czlonkowski/n8n-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Evitar errores de sintaxis al generar JSON de n8n
- Plantillas de workflows complejos
- Acelerar la creación de flujos con IA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| generas workflows n8n con IA y te cansan los fallos de JSON | no usas n8n |

## Stack y modelos

- **Stack:** `SKILL.md`, Markdown
- **Etiquetas:** `skills` `automation`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [n8n-mcp](n8n-mcp.md) | 23.3k | Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. |

## Enlaces

- 🐙 GitHub: [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills)
- 🌐 Web: <https://www.n8n-skills.com>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/czlonkowski/n8n-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
