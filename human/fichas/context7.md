[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Context7

> Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 64.8k | MIT | TypeScript | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | El coste depende del proveedor o la ruta. El cliente MCP usa su propio modelo. Context7 recomienda una API key y aplica límites o planes al servicio de documentación. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Evita que el modelo invente APIs viejas: busca la documentación vigente de la librería que estás usando y la inyecta en el prompt.

## Por qué destaca

Muy adoptado en agentes de código; reduce errores por APIs obsoletas.

## Cómo funciona

Indexa documentación de miles de proyectos y la sirve por MCP filtrada por librería y versión.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP y el acceso a Context7 que requiera la ruta elegida.

1. Elige el servidor remoto o la configuración documentada para tu cliente.
2. Configura la API key recomendada y comprueba los límites de tu plan si la necesitas.
3. Consulta la documentación de una librería concreta y verifica que la respuesta corresponde a su versión.

[Instrucciones originales de instalación](https://github.com/upstash/context7/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Context7 para mi objetivo y necesito pasos guiados. Lee https://github.com/upstash/context7/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `mcp` `docs` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Cline](cline.md) | 71.6k | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. |
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepWiki Open](deepwiki-open.md) | 18.4k | Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki. |

## Enlaces

- 🐙 GitHub: [upstash/context7](https://github.com/upstash/context7)
- 🌐 Web: <https://context7.com>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/upstash/context7/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
