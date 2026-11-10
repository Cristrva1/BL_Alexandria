[🏠 Inicio](../README.md) › [🎨 Diseño, UI & Frontend](../categorias/09-dise-o-ui-frontend.md) › Skills de diseño para agentes

# 🎨 ui-ux-pro-max-skill

> Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla".

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 148k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Resuelve el punto débil habitual del código asistido por IA: la jerarquía visual y el acabado.

## Por qué destaca

Aporta criterio de layout, tipografía y composición además de código, algo que los LLMs por sí solos no manejan bien. Se integra con asistentes populares (Claude Code, Codex, Cursor) vía una CLI propia y skills copiables.

## Cómo funciona

Las skills inyectan guías de diseño (espaciado, jerarquía, motion) en el contexto del asistente, y la CLI `uipro-cli` (Node) orquesta la aplicación de esos criterios sobre el código generado, con reglas concretas para Tailwind/CSS.

## Instalación rápida

Clona el repo y sigue su README; instala la CLI vía Node (`npx` o instalación local) y copia las skills al directorio de skills de tu asistente. Requiere Node.js y un asistente compatible con skills.

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
- **Modelos / API:** Agnóstico; funciona con cualquier asistente que cargue skills (Claude Code, Codex, Cursor).
- **Etiquetas:** `skills` `design` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [taste-skill](taste-skill.md) | 113k | Skills "anti-slop" para producir frontends premium (layout, tipografía, motion y espaciado) más skills de generación de imagen para crear mood boards de referencia. |
| [impeccable](impeccable.md) | 107k | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. |
| [tailwindcss](tailwindcss.md) | 98.7k | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. |

## Enlaces

- 🐙 GitHub: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- 🌐 Web: <https://www.uupm.cc/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
