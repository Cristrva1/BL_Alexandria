[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🛠️ n8n-skills

> Conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando errores al generar su JSON.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 6.6k | MIT | Shell | 2026-10-24 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Enseña a tu agente de código a escribir flujos de n8n en JSON que funcionan a la primera, con menos idas y vueltas de errores.

## Por qué destaca

Ataca un problema concreto y frecuente —el JSON de n8n generado por IA suele fallar— reduciendo bucles de error y timeouts. Su foco narrow la hace más eficaz que prompts genéricos para este caso.

## Cómo funciona

Las skills aportan plantillas y reglas de validación que guían al modelo a producir nodos y conexiones n8n sintácticamente válidos. Cada skill cubre un patrón de workflow (trigger, transformación, integración) con su esquema JSON.

## Instalación rápida

Clona el repo y copia las skills (`SKILL.md`) a tu directorio de skills de Claude Code u otro asistente compatible; sin dependencias.

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
- **Modelos / API:** Claude Code u otro que lea skills.
- **Etiquetas:** `skills` `automation`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [n8n-mcp](n8n-mcp.md) | 23.2k | Servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n (816 core + 1.029 comunitarios) para ayudar a construir y depurar flujos. |

## Enlaces

- 🐙 GitHub: [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills)
- 🌐 Web: <https://www.n8n-skills.com>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
