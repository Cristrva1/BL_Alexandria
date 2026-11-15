[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 GitHub MCP Server

> Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.5k | MIT | Go | 2026-06-24 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | El coste depende del proveedor o la ruta. Requiere autenticación y permisos de GitHub. La IA que decide las acciones pertenece al cliente MCP. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Conecta asistentes y agentes con la plataforma GitHub: repositorios, issues, pull requests, Actions y seguridad.

## Por qué destaca

Oficial y mantenido por GitHub, con un servidor remoto listo para usar.

## Cómo funciona

Un servidor Go expone herramientas MCP que llaman a la API de GitHub con tu token u OAuth.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

[Instrucciones originales de instalación](https://github.com/github/github-mcp-server/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GitHub MCP Server para mi objetivo y necesito pasos guiados. Lee https://github.com/github/github-mcp-server/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Triage de issues con un agente
- Revisar PRs automáticamente
- Consultar el estado de Actions

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente trabaja con GitHub | usas otra forja como GitLab |

## Stack y modelos

- **Stack:** Go, Docker
- **Etiquetas:** `mcp` `code` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Enlaces

- 🐙 GitHub: [github/github-mcp-server](https://github.com/github/github-mcp-server)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/github/github-mcp-server/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
