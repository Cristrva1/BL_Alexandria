[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Anthropic Skills

> Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 195k | — | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Repositorio de Anthropic con skills listas para Claude Code, Claude.ai y la API: creativas, técnicas (pruebas de apps web, creación de servidores MCP) y empresariales, más las skills de docx, pptx, xlsx y PDF que Claude usa para generar archivos. Incluye la especificación del estándar Agent Skills y una plantilla para crear las tuyas.

## Por qué destaca

Es la implementación de referencia del formato SKILL.md, publicada por quien definió el estándar. Las skills de documentos son las que Claude usa en producción, así que sirven de modelo para skills complejas.

## Cómo funciona

Cada skill es una carpeta con un SKILL.md (frontmatter YAML con nombre y descripción, más instrucciones) y a veces scripts. Claude ve la descripción y carga el contenido completo solo cuando la tarea lo pide.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/anthropics/skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Anthropic Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Crear y editar docx, pptx, xlsx y PDF desde Claude Code
- Generar un servidor MCP con la skill mcp-builder
- Escribir tus propias skills partiendo de skill-creator o la plantilla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres skills oficiales de Anthropic o un ejemplo de referencia para escribir las tuyas | buscas volumen o skills de comunidad para varios agentes; mira `awesome-agent-skills` o `antigravity-awesome-skills` |

**Limitaciones:** Son skills de demostración y las de documentos (docx, pdf, pptx, xlsx) son source-available, no open source.

## Stack y modelos

- **Stack:** Markdown, YAML, Python, JavaScript
- **Etiquetas:** `skills` `docs` `pdf` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Claude Code Plugins Directory](claude-plugins-official.md) | 47.3k | Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. |
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |

## Enlaces

- 🐙 GitHub: [anthropics/skills](https://github.com/anthropics/skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/anthropics/skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
