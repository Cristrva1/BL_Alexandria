[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Escritura y calidad de texto

# 🧑 Humanizer

> Skill que reescribe texto generado por IA para que suene humano, basada en la guía de Wikipedia sobre señales de escritura IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 69.1k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

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

Detecta 26 patrones típicos de la prosa de LLM (contrastes tipo 'no es X, es Y', cierres dramáticos, tríadas forzadas, frases de falsa profundidad, importancia inflada) y reescribe el texto sin cambiar lo que dice. Puede imitar tu estilo si le das una muestra y, sobre un archivo, solo toca la prosa: no el código, los datos ni el frontmatter.

## Por qué destaca

Parte de una fuente pública (la guía 'Signs of AI writing' de los editores de Wikipedia) y muestra su trabajo: primera reescritura, crítica de lo que aún suena artificial y versión final. No añade datos que no estuvieran en el original.

## Cómo funciona

El SKILL.md ordena los patrones por fuerza: los cinco primeros justifican un cambio con una sola aparición y los débiles solo cuentan si se acumulan. El agente marca las señales, redacta, contrasta el borrador con los patrones y las afirmaciones originales y entrega.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/blader/humanizer/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Humanizer para mi objetivo y necesito pasos guiados. Lee https://github.com/blader/humanizer/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Quitar el tono IA de un post o un anuncio de producto
- Reescribir documentación generada sin perder los datos
- Ajustar un borrador a tu propia voz con una muestra

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| publicas textos redactados con IA y quieres que se lean como escritos por una persona | quieres reglas de estilo cortas para pegar en un system prompt, con rúbrica propia; mira `stop-slop` |

**Limitaciones:** Sus patrones y ejemplos están pensados para prosa en inglés, y no busca engañar a los detectores de IA, que siguen marcando la mayoría de sus salidas.

## Stack y modelos

- **Stack:** Markdown, SKILL.md
- **Etiquetas:** `skills` `prompts` `docs`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marketing Skills](marketingskills.md) | 60.4k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stop Slop](stop-slop.md) | 18.9k | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. |

## Enlaces

- 🐙 GitHub: [blader/humanizer](https://github.com/blader/humanizer)
- 🌐 Web: <https://skills.sh/blader/humanizer>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/blader/humanizer/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
