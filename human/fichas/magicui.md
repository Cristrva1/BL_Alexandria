[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# ✨ magicui

> Componentes React para componer secciones de página con shadcn y Tailwind, como una cuadrícula Bento o un bloque de video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.3k | MIT | MDX | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de componentes UI animados (MIT) para 'design engineers', de Magic UI. Es popular (~23k estrellas) y activa.

## ¿Qué hace?

Ofrece componentes y efectos visuales (globos, marquesinas, partículas, textos animados, bordes brillantes y otros) para landing pages y webs de producto. Incluye un servidor MCP para que asistentes de IA usen los componentes.

## ¿Cómo lo hace?

Se distribuye como registro de shadcn: `npx shadcn@latest add @magicui/<componente>` copia el código al proyecto. Usa React, TypeScript, Tailwind CSS y Motion para las animaciones. Requiere un proyecto con shadcn/ui inicializado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ui](ui.md) | Base de instalación: Magic UI se añade con la CLI de shadcn. | Ejecuta `npx shadcn@latest init` y luego añade los componentes de Magic UI. |
| [tailwindcss](tailwindcss.md) | Estilos de los componentes. | Se configura con la inicialización de shadcn. |
| [motion](motion.md) | Biblioteca de animación usada por los componentes. | Se instala como dependencia al añadir cada componente. |
| [Claude Code](claude-code.md) | Usar los componentes desde el asistente vía el servidor MCP de Magic UI. | Registra el MCP según magicui.design/docs/mcp. |
| [Anime.js](animejs.md) | Combinación recíproca: Anime.js lo enlaza como «Animaciones extra en componentes de interfaz. (combinación por arquitectura)». | Orden indicado desde Anime.js: Aplica animaciones a componentes. |

**Notas:** Alternativas (elige una): react-bits.

Estado en GitHub: activo · último push 2026-11-13 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/magicuidesign/magicui/blob/main/README.md) · [2](https://magicui.design/docs/installation) · [3](https://magicui.design/docs/mcp) · [4](https://magicui.design/docs/components/bento-grid) · [5](https://pro.magicui.design/license)</sub>

## Ver similares

Grupo **Componentes animados para React**: magicui ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [React Bits](react-bits.md) ⭐ recomendado | 59 | Si buscas esto: la mayor colección open source de componentes React animados e interactivos para webs llamativas. |
| 2 | **magicui** (esta ficha) | 53 | Si buscas esto: componentes React para componer secciones de página con shadcn y Tailwind, como una cuadrícula Bento o un bloque de video. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Los componentes del repositorio son MIT; productos o plantillas comerciales asociados tienen términos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Copiar un componente puede añadir dependencias; verifica qué se incorpora antes de instalar varios efectos |
| Coste | Sin pago a un modelo en la ruta básica. Los componentes del repositorio son MIT; productos o plantillas comerciales asociados tienen términos propios |
| Equipo | Preparación según la ruta elegida. React; dependencias del componente elegido; proyecto de prueba |

Copiar un componente puede añadir dependencias; verifica qué se incorpora antes de instalar varios efectos

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React
- dependencias del componente elegido
- proyecto de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://magicui.design/docs)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar magicui para mi objetivo y necesito pasos guiados. Lee https://magicui.design/docs. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade un componente visual pequeño y comprueba el diseño en móvil y con movimiento reducido.

**Qué comprobar:** El contenido sigue siendo legible y el componente no desborda.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar una sección de landing
- Añadir una interacción de presentación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Quieres componer una sección React con una cuadrícula de funcionalidades, un bloque de video o un registro de componentes bajo MIT. | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El repositorio de componentes publica MIT. Magic UI Pro aplica sus propios términos a sus secciones y plantillas de pago.

## Stack y modelos

- **Stack:** React; dependencias del componente elegido; proyecto de prueba
- **Etiquetas:** `ui`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [React Bits](react-bits.md) | 52k | Efectos de texto, fondos gráficos y componentes interactivos para añadir animaciones puntuales a una interfaz React. |

## Enlaces

- 🐙 GitHub: [magicuidesign/magicui](https://github.com/magicuidesign/magicui)
- 🌐 Web: <https://magicui.design>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/magicuidesign/magicui/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
