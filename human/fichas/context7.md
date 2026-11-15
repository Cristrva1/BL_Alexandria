[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Context7

> Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 64.5k | MIT | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Evita que el modelo invente APIs viejas: busca la documentación vigente de la librería que estás usando y la inyecta en el prompt.

## Por qué destaca

Muy adoptado en agentes de código; reduce errores por APIs obsoletas.

## Cómo funciona

Indexa documentación de miles de proyectos y la sirve por MCP filtrada por librería y versión.

## Instalación rápida

Añade a tu cliente MCP: `npx -y @upstash/context7-mcp` (o el servidor remoto con clave).

## Casos de uso

- Programar con librerías que cambian rápido
- Evitar APIs alucinadas
- Consultar docs sin salir del agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente de código usa librerías que cambian a menudo | trabajas sin conexión a internet |

**Limitaciones:** Depende del servicio en la nube de Upstash.

## Stack y modelos

- **Stack:** TypeScript
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `mcp` `docs` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Cline](cline.md) | 71.5k | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. |
| [OpenCode](opencode.md) | 226k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepWiki Open](deepwiki-open.md) | 18.4k | Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki. |

## Enlaces

- 🐙 GitHub: [upstash/context7](https://github.com/upstash/context7)
- 🌐 Web: <https://context7.com>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
