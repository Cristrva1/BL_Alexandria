[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 ui-ux-pro-max-skill

> Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla".

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 150k | MIT | Python | 2026-06-23 |

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

Resuelve el punto débil habitual del código asistido por IA: la jerarquía visual y el acabado.

## Por qué destaca

Aporta criterio de layout, tipografía y composición además de código, algo que los LLMs por sí solos no manejan bien. Se integra con asistentes populares (Claude Code, Codex, Cursor) vía una CLI propia y skills copiables.

## Cómo funciona

Las skills inyectan guías de diseño (espaciado, jerarquía, motion) en el contexto del asistente, y la CLI `uipro-cli` (Node) orquesta la aplicación de esos criterios sobre el código generado, con reglas concretas para Tailwind/CSS.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ui-ux-pro-max-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Mejorar layouts y jerarquía visual de UIs generadas por IA
- Acabado profesional con Tailwind/CSS
- Iterar diseño sin handoff manual con un diseñador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| generas UI con IA y el resultado se ve genérico o despulido | no trabajas frontend o ya tienes un sistema de diseño impuesto |

## Stack y modelos

- **Stack:** Node.js (uipro-cli), TypeScript/React
- **Etiquetas:** `skills` `design` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [taste-skill](taste-skill.md) | 116k | Skills "anti-slop" para producir frontends premium (layout, tipografía, motion y espaciado) más skills de generación de imagen para crear mood boards de referencia. |
| [impeccable](impeccable.md) | 110k | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. |
| [tailwindcss](tailwindcss.md) | 98.6k | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. |

## Enlaces

- 🐙 GitHub: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- 🌐 Web: <https://www.uupm.cc/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
