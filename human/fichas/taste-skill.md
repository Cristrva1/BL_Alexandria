[🏠 Inicio](../README.md) › [🎨 Diseño, UI & Frontend](../categorias/09-dise-o-ui-frontend.md) › Skills de diseño para agentes

# 🍷 taste-skill

> Skills "anti-slop" para producir frontends premium (layout, tipografía, motion y espaciado) más skills de generación de imagen para crear mood boards de referencia.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 113k | MIT | JavaScript | 2026-11-08 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Ataca el acabado "de plantilla" que delata a las UIs generadas por IA.

## Por qué destaca

Aporta criterio de diseño además de código, y opcionalmente genera boards visuales (web, mobile, brand) para anclar el estilo antes de programar. Es portable entre asistentes (Codex, Cursor, Claude Code) y de foco estético.

## Cómo funciona

Las skills inyectan guías de gusto visual en el contexto del asistente y, cuando se activan las de imagen, llaman a un generador (ChatGPT Images u otro) para producir boards de referencia que el modelo usa como guía.

## Instalación rápida

Clona el repo y copia las skills a tu directorio de skills (Codex, Cursor o Claude Code); las de imagen requieren un generador disponible y su correspondiente acceso/API.

## Casos de uso

- Subir el gusto de UIs construidas por IA
- Boards de referencia (web/mobile/brand) antes de codificar
- Alinear estética entre diseñador y agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres frontends con gusto y no te basta con UI funcional | ya tienes un design system cerrado o no usas generadores de imagen |

## Stack y modelos

- **Stack:** Markdown/skills
- **Modelos / API:** Codex, Cursor, Claude Code; las skills de imagen usan generadores como ChatGPT Images.
- **Etiquetas:** `skills` `design` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ui-ux-pro-max-skill](ui-ux-pro-max-skill.md) | 148k | Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla". |
| [impeccable](impeccable.md) | 107k | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. |

## Enlaces

- 🐙 GitHub: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- 🌐 Web: <https://tasteskill.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
