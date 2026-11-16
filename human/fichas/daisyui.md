[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › CSS y estilos

# 🎨 daisyUI

> La librería de componentes más popular para Tailwind CSS, con clases semánticas y temas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.8k | MIT | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de componentes para Tailwind CSS (MIT) de @saadeghi, la más popular de su tipo según el README. Es madura y activa (daisyUI 5, v5.8.1).

## ¿Qué hace?

Añade clases semánticas de componentes (`btn`, `card`, `modal` y otras) sobre Tailwind, para escribir menos clases utilitarias, e incluye un sistema de temas con decenas de temas predefinidos. Es agnóstica del framework: funciona con HTML puro, React, Vue, Svelte y otros, porque es solo CSS.

## ¿Cómo lo hace?

Es un plugin de Tailwind CSS v4: se instala con npm y se activa con `@plugin "daisyui"` en el CSS. No trae JavaScript: el comportamiento interactivo (modales, menús) depende de HTML nativo o de tu propio código.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tailwindcss](tailwindcss.md) | daisyUI es un plugin de Tailwind; sin él no funciona. | Instala Tailwind v4 y añade `@plugin "daisyui"`. |
| [Lucide](lucide.md) | Iconos para los componentes. (combinación por arquitectura) | Instala el paquete de Lucide de tu framework. |
| [flexoki](flexoki.md) | Paleta para crear un tema personalizado de daisyUI. (combinación por arquitectura) | Define un tema propio con los colores de Flexoki. |

**Notas:** Alternativas (elige una): ui.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v5.8.1 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/saadeghi/daisyui/blob/master/README.md) · [2](https://daisyui.com/docs/install/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no requiere IA; plantillas o servicios comerciales relacionados son opcionales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un plugin de estilos y clases de Tailwind; sigue la guía de la versión instalada para configurar el CSS |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no requiere IA; plantillas o servicios comerciales relacionados son opcionales |
| Equipo | Preparación según la ruta elegida. Proyecto con Tailwind compatible; Node y gestor de paquetes |

Es un plugin de estilos y clases de Tailwind; sigue la guía de la versión instalada para configurar el CSS

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto con Tailwind compatible
- Node y gestor de paquetes

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://daisyui.com/docs/install/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar daisyUI para mi objetivo y necesito pasos guiados. Lee https://daisyui.com/docs/install/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade un botón y una tarjeta con un tema y cambia al segundo tema.

**Qué comprobar:** Se actualizan colores sin reescribir cada componente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar una web con clases semánticas
- Añadir temas a un panel sencillo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar una web con clases semánticas; Añadir temas a un panel sencillo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un plugin de estilos y clases de Tailwind; sigue la guía de la versión instalada para configurar el CSS

## Stack y modelos

- **Stack:** Proyecto con Tailwind compatible; Node y gestor de paquetes
- **Etiquetas:** `ui` `design` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ui](ui.md) | 128k | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. |

## Enlaces

- 🐙 GitHub: [saadeghi/daisyui](https://github.com/saadeghi/daisyui)
- 🌐 Web: <https://daisyui.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/saadeghi/daisyui/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
