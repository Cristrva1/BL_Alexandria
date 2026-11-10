[🏠 Inicio](../README.md) › [🎨 Diseño, UI & Frontend](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# 🎨 open-design

> Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 107k | Apache-2.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Resuelve el ir y venir entre prompt, preview y código exportable.

## Por qué destaca

Combina generación por IA con edición visual real y enruta varios modelos en una sola herramienta, algo poco común en editores abiertos. Su arquitectura Tauri (Rust) le da un binario nativo ligero frente a apps puramente web.

## Cómo funciona

App de escritorio en React + Tauri (Rust) que traduce prompts a UI editable y la sincroniza de vuelta, con un enrutador AMR que reparte peticiones entre modelos según la tarea.

## Instalación rápida

Clonar el repo y compilar la app Tauri, o usar los binarios de release según plataforma. Requiere claves API de al menos un proveedor (OpenAI/Anthropic/Google/DeepSeek).

## Casos de uso

- Describir una pantalla y ver cómo la IA la maqueta y anima
- Importar sistemas de diseño (Figma, Tailwind) y iterarlos por voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| generas UI desde texto y quieres edición visual | prefieres editar visualmente sobre tu código existente (plasmic) |

## Stack y modelos

- **Stack:** TypeScript/React, Tauri (Rust)
- **Modelos / API:** GPT-4o, Claude, Gemini, DeepSeek vía AMR.
- **Etiquetas:** `agents` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [tailwindcss](tailwindcss.md) | 98.7k | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. |
| [heroui](heroui.md) | 31.2k | Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Onlook](onlook.md) | 27.2k | Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma. |

## Enlaces

- 🐙 GitHub: [nexu-io/open-design](https://github.com/nexu-io/open-design)
- 🌐 Web: <https://open-design.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
