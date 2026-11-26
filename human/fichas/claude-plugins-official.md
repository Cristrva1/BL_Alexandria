[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🔌 Claude Code Plugins Directory

> Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47.3k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Repositorio de Anthropic (Apache 2.0) con sus propios plugins para Claude y el marketplace `claude-plugins-official` de Claude Code. Está en transición: los envíos de terceros ya se hacen en claude.ai/directory/manage.

## ¿Qué hace?

Contiene plugins internos de Anthropic (`/plugins`) y plugins de terceros añadidos antes del cambio, además de los plugins de canal de Anthropic (Discord, iMessage, Telegram) en `/external_plugins`. El `marketplace.json` se irá reduciendo a los plugins propios de Anthropic. El README advierte que Anthropic no controla los servidores MCP ni el software que incluyen los plugins.

## ¿Cómo lo hace?

Se usa desde el sistema de plugins de Claude Code: `/plugin install <nombre>@claude-plugins-official` o `/plugin > Discover`. Las entradas pueden declarar skills de repositorios externos en modo estricto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Marketplace oficial de plugins. | Revisa cada plugin antes de instalarlo, como recomienda el README. |
| [superpowers](superpowers.md) | Se instala desde este marketplace (`superpowers@claude-plugins-official`). | `/plugin install superpowers@claude-plugins-official`. |
| [skills](skills.md) | Las skills de Matt Pocock se instalan desde este marketplace. | `claude plugin install mattpocock-skills@claude-plugins-official`. |
| [Awesome Claude Code](awesome-claude-code.md) | Combinación recíproca: Awesome Claude Code lo enlaza como «Marketplace oficial frente a los recursos comunitarios de la lista (combinación por arquitectura)». | Orden indicado desde Awesome Claude Code: Prioriza lo oficial y revisa lo comunitario. |

**Notas:** Alternativa (elige una): wshobson-agents. Se quitaron anthropic-skills y awesome-claude-code: son catálogos paralelos, no integraciones.

Estado en GitHub: activo · último push 2026-11-14 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anthropics/claude-plugins-official/blob/main/README.md)</sub>

## Ver similares

Grupo **Catálogos de skills y plugins para agentes**: Claude Code Plugins Directory ocupa la posición 2 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) ⭐ recomendado | 68 | Si quieres el catálogo más grande de skills instalables para varios agentes. |
| 2 | **Claude Code Plugins Directory** (esta ficha) | 62 | Si quieres solo plugins publicados por Anthropic. |
| 3 | [Awesome Agent Skills](awesome-agent-skills.md) | 54 | Si quieres skills en formato portable para varios agentes. |
| 4 | [wshobson/agents](wshobson-agents.md) | 51 | Si quieres subagentes y plugins listos para Claude Code por especialidad. |
| 5 | [Awesome Claude Skills](awesome-claude-skills.md) | 48 | Si buscas skills para Claude ordenadas por tema. |
| 6 | [Awesome Claude Code](awesome-claude-code.md) | 48 | Si usas Claude Code y quieres una lista curada de comandos, hooks y flujos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El marketplace no incluye tarifas de todos sus servicios; el agente y cada integración conservan sus costes |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un directorio gestionado por Anthropic; instalar un plugin no implica instalar todos los del repositorio |
| Coste | Consumo del agente que ya utilizas. El marketplace no incluye tarifas de todos sus servicios; el agente y cada integración conservan sus costes |
| Equipo | Preparación según la ruta elegida. Claude Code;  elegir un plugin y revisar sus dependencias |

Es un directorio gestionado por Anthropic; instalar un plugin no implica instalar todos los del repositorio

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- elegir un plugin y revisar sus dependencias

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://code.claude.com/docs/en/plugins)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Claude Code Plugins Directory para mi objetivo y necesito pasos guiados. Lee https://code.claude.com/docs/en/plugins. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Busca un plugin del marketplace e instala solo el que corresponde a tu tarea.

**Qué comprobar:** El plugin figura instalado y puedes consultar sus comandos o skills.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir una herramienta de revisión al flujo de desarrollo
- Conectar un servicio mediante un plugin publicado en el marketplace oficial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir una herramienta de revisión al flujo de desarrollo; Conectar un servicio mediante un plugin publicado en el marketplace oficial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un directorio gestionado por Anthropic; instalar un plugin no implica instalar todos los del repositorio

## Stack y modelos

- **Stack:** Claude Code;  elegir un plugin y revisar sus dependencias
- **Etiquetas:** `skills` `coding-agent` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [wshobson/agents](wshobson-agents.md) | 42.5k | Colección de plugins, agentes y skills con adaptadores documentados para Claude Code, Codex, Antigravity y otros clientes. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- 🌐 Web: <https://code.claude.com/docs/en/plugins>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/claude-plugins-official/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
