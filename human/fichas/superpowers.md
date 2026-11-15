[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 💪 superpowers

> Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 318k | MIT | Shell | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

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

Le da a tu agente de código un método de trabajo completo y coherente (planear, probar, revisar), no piezas sueltas.

## Por qué destaca

Ofrece un sistema coherente en lugar de piezas sueltas, lo que da consistencia al flujo de trabajo del agente entre tareas. Sus metaprompts fuerzan la invocación de skills, evitando que el agente las ignore.

## Cómo funciona

Combina skills modulares con metaprompts/instrucciones que el agente lee y encadena para seguir un método paso a paso. Las skills se componen entre sí, de modo que el output de una alimenta la siguiente.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/obra/superpowers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar superpowers para mi objetivo y necesito pasos guiados. Lee https://github.com/obra/superpowers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Dar a tu agente un método consistente
- Estandarizar el flujo de desarrollo
- Reducir variabilidad entre sesiones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres método, no fragmentos sueltos | solo necesitas una skill aislada puntual |

## Stack y modelos

- **Stack:** Markdown/skills
- **Etiquetas:** `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Claude Code](awesome-claude-code.md) | 58k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |
| [agent-toolkit](agent-toolkit.md) | 2.7k | Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agent Skills (Addy Osmani)](agent-skills.md) | 118k | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. |

## Enlaces

- 🐙 GitHub: [obra/superpowers](https://github.com/obra/superpowers)
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/obra/superpowers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
