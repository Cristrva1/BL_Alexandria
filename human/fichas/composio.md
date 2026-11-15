[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ Composio

> Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.1k | MIT | TypeScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Da a cualquier agente herramientas listas para Gmail, Slack, GitHub, Notion y cientos más, gestionando OAuth por ti. Funciona con los principales frameworks y por MCP.

## Por qué destaca

Resuelve la parte más tediosa de los agentes: autenticación y herramientas para muchas apps.

## Cómo funciona

Su API expone toolkits con auth gestionada; los SDK los convierten en herramientas para tu framework o en servidores MCP.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install composio
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/ComposioHQ/composio/blob/next/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Composio para mi objetivo y necesito pasos guiados. Lee https://github.com/ComposioHQ/composio/blob/next/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agente que lee y responde correos
- Automatizar tareas en Slack y GitHub
- Herramientas MCP con OAuth

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente necesita actuar en muchas apps SaaS | quieres todo auto-hospedado sin servicio externo |

**Limitaciones:** Depende de su servicio en la nube y tiene planes de pago por uso.

## Stack y modelos

- **Stack:** TypeScript, Python
- **Etiquetas:** `agents` `mcp` `automation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [OpenAI Agents SDK](openai-agents-python.md) | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |
| [Mastra](mastra.md) | 29.5k | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. |

## Enlaces

- 🐙 GitHub: [ComposioHQ/composio](https://github.com/ComposioHQ/composio)
- 🌐 Web: <https://docs.composio.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ComposioHQ/composio/blob/next/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
