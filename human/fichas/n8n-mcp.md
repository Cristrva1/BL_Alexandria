[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🔌 n8n-mcp

> Servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n (816 core + 1.029 comunitarios) para ayudar a construir y depurar flujos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 23.2k | MIT | TypeScript | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Resuelve el problema de que un LLM invente parámetros de nodos que no existen y genere workflows rotos.

## Por qué destaca

Reduce drásticamente los errores cuando se pide a una IA que arme un workflow de n8n, al darle acceso fiable a los parámetros reales de cada nodo. Su enfoque de "documentación como herramienta MCP" es un patrón replicable para otras plataformas.

## Cómo funciona

El cliente MCP (Claude, Cursor, Gemini CLI) invoca tools del servidor para consultar nodos, propiedades y ejemplos vía el protocolo MCP; el LLM recibe esquemas exactos en lugar de alucinarlos.

## Instalación rápida

`npx n8n-mcp` y añadirlo a la config del cliente MCP (p. ej. Claude Desktop). Requiere Node.js y, para flujos reales, una instancia n8n accesible.

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
- **Modelos / API:** Claude Desktop/Code, Cursor, Gemini CLI; agnóstico vía MCP.
- **Etiquetas:** `automation` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [n8n-skills](n8n-skills.md) | 6.6k | Conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando errores al generar su JSON. |

## Enlaces

- 🐙 GitHub: [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)
- 🌐 Web: <https://www.n8n-mcp.com/>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
