[🏠 Inicio](../README.md) › [🎨 Diseño, UI & Frontend](../categorias/09-dise-o-ui-frontend.md) › Skills de diseño para agentes

# 📐 design.md

> Formato para describir una identidad visual a agentes de código con tokens YAML y prosa.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 28.8k | Apache-2.0 | TypeScript | 2026-11-06 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Resuelve la inconsistencia de marca cuando varias personas o agentes tocan la UI.

## Por qué destaca

Propuesta de Google Labs que aporta no solo los valores sino el "por qué" y cómo aplicarlos, algo que un simple archivo de tokens no transmite. Al ser un formato declarativo, funciona con cualquier agente que lea Markdown.

## Cómo funciona

Archivo Markdown/YAML que el agente lee como contexto persistente, combinando tokens de diseño (color, tipografía, espaciado) con guías en prosa sobre cuándo usarlos.

## Instalación rápida

Crear un `design.md` en el repo siguiendo el formato (sin dependencias). Solo necesitas un agente de código que lo cargue como contexto.

## Casos de uso

- Dar al agente un sistema de diseño persistente
- Mantener coherencia de marca entre varios contribuyentes
- Onboarding rápido de estilo para nuevos agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres consistencia de marca con IA y usas agentes para UI | no usas agentes para generar código de UI |

## Stack y modelos

- **Stack:** Markdown/YAML
- **Modelos / API:** Agentes de código (Claude Code, Cursor, etc.).
- **Etiquetas:** `skills` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [impeccable](impeccable.md) | 107k | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. |

## Enlaces

- 🐙 GitHub: [google-labs-code/design.md](https://github.com/google-labs-code/design.md)
- 🌐 Web: <https://stitch.withgoogle.com/docs/design-md/specification>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
