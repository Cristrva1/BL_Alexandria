[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › CSS y estilos

# 🌬️ tailwindcss

> Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 98.6k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework CSS utility-first (MIT) de Tailwind Labs. Es el estándar de facto en muchos stacks modernos de frontend, muy maduro y activo (v4.3.5).

## ¿Qué hace?

Proporciona clases utilitarias (espaciado, color, tipografía, layout y otras) para construir interfaces directamente en el marcado. Genera solo el CSS que se usa. La v4 configura el tema con CSS (`@theme`), incluye Preflight (un reset basado en modern-normalize) y admite variantes, modo oscuro y plugins.

## ¿Cómo lo hace?

Se instala como plugin de Vite (`npm install tailwindcss @tailwindcss/vite`), mediante PostCSS o con la CLI, y se importa con `@import "tailwindcss"`. Funciona con cualquier framework. La migración de v3 a v4 cambia la configuración, que pasa de `tailwind.config.js` a CSS, así que conviene usar la herramienta de actualización oficial.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ui](ui.md) | shadcn/ui escribe todos sus componentes con Tailwind. | Configura Tailwind primero y luego inicializa shadcn/ui. |
| [daisyUI](daisyui.md) | Plugin de componentes semánticos para Tailwind. | Añade `@plugin "daisyui"` tras configurar Tailwind. |
| [heroui](heroui.md) | Biblioteca de componentes que requiere Tailwind v4. | Configura Tailwind v4 antes de instalar HeroUI. |
| [magicui](magicui.md) | Componentes animados escritos con Tailwind (vía shadcn). | Tailwind y shadcn primero; luego Magic UI. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (18). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Biome](biome.md) · [Chart.js](chart-js.md) · [design.md](design-md.md) · [Figma Context MCP](figma-context-mcp.md) · [flexoki](flexoki.md) · [konva](konva.md) · [Lucide](lucide.md) · [Onlook](onlook.md) · [penpot](penpot.md) · [plasmic](plasmic.md) · [Radix Primitives](radix-primitives.md) · [React Bits](react-bits.md) · [Recharts](recharts.md) · [screenshot-to-code](screenshot-to-code.md) · [Storybook](storybook.md) · [TanStack Query](tanstack-query.md) · [UI SDK (Vercel)](ui-sdk.md) · [ui-ux-pro-max-skill](ui-ux-pro-max-skill.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada v4.3.5 (2026-11-06) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tailwindlabs/tailwindcss/blob/main/README.md) · [2](https://tailwindcss.com/docs/installation/using-vite) · [3](https://tailwindcss.com/docs/preflight)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El framework no usa modelos ni API; productos de pago del ecosistema tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Elige la integración de tu framework; la configuración actual no debe copiarse sin más de tutoriales de Tailwind v3 |
| Coste | Sin pago a un modelo en la ruta básica. El framework no usa modelos ni API; productos de pago del ecosistema tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Proyecto Vite u otra integración elegida; Node |

Elige la integración de tu framework; la configuración actual no debe copiarse sin más de tutoriales de Tailwind v3

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto Vite u otra integración elegida
- Node

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://tailwindcss.com/docs/installation/using-vite)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar tailwindcss para mi objetivo y necesito pasos guiados. Lee https://tailwindcss.com/docs/installation/using-vite. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una tarjeta adaptable y cambia el espaciado con utilidades.

**Qué comprobar:** Puedes comprobar diferencias entre móvil y escritorio.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar un formulario responsive
- Definir colores y espaciado consistentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar un formulario responsive; Definir colores y espaciado consistentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Elige la integración de tu framework; la configuración actual no debe copiarse sin más de tutoriales de Tailwind v3

## Stack y modelos

- **Stack:** Proyecto Vite u otra integración elegida; Node
- **Etiquetas:** `ui` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)
- 🌐 Web: <https://tailwindcss.com/>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tailwindlabs/tailwindcss/blob/main/README.md)
- [Fuente 2](https://tailwindcss.com/docs/installation/using-vite)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
