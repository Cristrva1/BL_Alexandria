[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces](../categorias/09-dise-o-ui-frontend.md) › Skills de diseño para agentes

# ✏️ skills_emil

> Colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.9k | MIT | Markdown | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Resuelve el handoff diseño↔código, no solo la estética final.

## Por qué destaca

Pone el foco en la traducción de diseño a implementación (tokens, consistencia, decisiones compartidas), un ángulo menos cubierto por otras skills de UI que miran solo el resultado visual.

## Cómo funciona

Se entrega como un `SKILL.md` (skill `emil-design-eng`) que el asistente carga para guiar decisiones de diseño-implementación: estructura de componentes, naming, tokens y patrones coherentes entre Figma y código.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/emilkowalski/skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar skills_emil para mi objetivo y necesito pasos guiados. Lee https://github.com/emilkowalski/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Mejorar el handoff diseño↔ingeniería
- Resultados UI más consistentes entre Figma y código
- Alinear naming y tokens en un equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas diseño+dev en equipo y sufres el handoff | buscas componentes listos o trabajas solo |

## Stack y modelos

- **Stack:** Markdown (skills), TypeScript/React
- **Etiquetas:** `skills` `design`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ui-ux-pro-max-skill](ui-ux-pro-max-skill.md) | 150k | Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla". |

## Enlaces

- 🐙 GitHub: [emilkowalski/skills](https://github.com/emilkowalski/skills)
- 🌐 Web: <https://emilkowal.ski/skill>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/emilkowalski/skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
