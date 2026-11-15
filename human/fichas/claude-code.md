[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 Claude Code

> Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 156k | — | TypeScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Puede utilizarse con sesión del plan compatible o con API key; no son la misma facturación. |
| Claude Code | Acceso oficial con sesión del plan |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

La sesión oficial del plan y una API key son rutas de autenticación distintas. Elegir una y consultar los límites del plan.

## Qué puedes hacer con él

Lee y edita archivos, ejecuta comandos, hace commits y abre PRs a partir de instrucciones en lenguaje natural. Se extiende con skills, plugins, subagentes, hooks y servidores MCP.

## Por qué destaca

Referencia en agentes de código por su autonomía en tareas largas y su ecosistema de skills y plugins.

## Cómo funciona

Un bucle agéntico con Claude decide qué herramientas usar (leer, editar, bash, MCP) y pide permiso según el modo configurado.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y acceso a Claude Code mediante plan o API, según la ruta elegida.

1. Sigue el instalador oficial para tu sistema; el comando mostrado corresponde a Windows.
2. Ejecuta Claude Code y autentícate con el plan o con la cuenta de API que quieras consumir.
3. Abre un proyecto de prueba y comprueba el método de acceso antes de trabajar con tareas largas.

**Comando de entrada documentado:**

```shell
winget install Anthropic.ClaudeCode
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/anthropics/claude-code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Claude Code para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/claude-code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Implementar funciones completas con tests
- Migrar o refactorizar código grande
- Automatizar tareas con skills y hooks

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el agente de código más capaz para tareas largas en tu repo | necesitas un agente totalmente abierto y multi-modelo; mira `opencode` |

**Limitaciones:** Requiere suscripción o clave de API de Anthropic; el código no es open source.

## Stack y modelos

- **Stack:** TypeScript, Node.js
- **Etiquetas:** `coding-agent` `agents` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |
| [Anthropic Skills](anthropic-skills.md) | 195k | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. |
| [claude-mem](claude-mem.md) | 117k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. |
| [Context7](context7.md) | 64.8k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [Gemini CLI](gemini-cli.md) | 109k | Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. |
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [goose](goose.md) | 56.6k | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-code](https://github.com/anthropics/claude-code)
- 🌐 Web: <https://code.claude.com/docs/en/overview>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/anthropics/claude-code/blob/main/README.md)
- [Fuente 2](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
