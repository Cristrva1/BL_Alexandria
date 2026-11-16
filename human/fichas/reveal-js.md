[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Presentaciones

# 🖥️ reveal.js

> Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 72.6k | MIT | JavaScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

reveal.js, framework HTML de presentaciones de @hakimel. Licencia MIT. Es veterano y estable (creado en 2011, ~73k estrellas, v6.0.2).

## ¿Qué hace?

Ofrece diapositivas anidadas, soporte de Markdown, Auto-Animate, exportación a PDF, notas del presentador, API JavaScript y plugins.

## ¿Cómo lo hace?

Se usa como paquete npm o clonando el repo; funciona en cualquier navegador. Slides.com es su editor visual comercial, de los mismos autores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Mermaid](mermaid.md) | Diagramas en las diapositivas. (combinación por arquitectura) | Añade un plugin de Mermaid. |
| [GSAP](gsap.md) | Animaciones avanzadas. (combinación por arquitectura) | Úsalo en las diapositivas. |
| [Claude Code](claude-code.md) | Generar HTML de presentaciones. (combinación por arquitectura) | Pide al agente el index.html. |
| [Pandoc](pandoc.md) | Combinación recíproca: Pandoc lo enlaza como «Pandoc genera presentaciones reveal.js desde Markdown». | Orden indicado desde Pandoc: Usa `-t revealjs`; reveal.js puede cargarse desde CDN o una copia local. |

**Notas:** Alternativas (elige una): slidev, marp.

Estado en GitHub: activo · último push 2026-09-30 · última versión publicada 6.0.2 (2026-09-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hakimel/reveal.js/blob/master/README.md) · [2](https://revealjs.com/)</sub>

## Ver similares

Grupo **Presentaciones desde Markdown**: reveal.js ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Slidev](slidev.md) ⭐ recomendado | 73 | Si buscas esto: presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. |
| 2 | **reveal.js** (esta ficha) | 59 | Si buscas esto: framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. |
| 3 | [Marp](marp.md) | 47 | Si buscas esto: entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separado. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El framework MIT es gratuito; curso, hosting y servicios externos son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El curso de pago no es necesario para la biblioteca y no se requiere modelo de IA para renderizar slides |
| Coste | Sin pago a un modelo en la ruta básica. El framework MIT es gratuito; curso, hosting y servicios externos son independientes |
| Equipo | Preparación según la ruta elegida. Node según ruta; HTML; contenido propio; navegador |

El curso de pago no es necesario para la biblioteca y no se requiere modelo de IA para renderizar slides

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node según ruta
- HTML
- contenido propio
- navegador

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://revealjs.com/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar reveal.js para mi objetivo y necesito pasos guiados. Lee https://revealjs.com/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea dos slides y una nota del orador y prueba navegación y presentación.

**Qué comprobar:** Puedes abrir la presentación y ver las notas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una presentación web
- Mostrar un ejemplo interactivo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una presentación web; Mostrar un ejemplo interactivo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El curso de pago no es necesario para la biblioteca y no se requiere modelo de IA para renderizar slides

## Stack y modelos

- **Stack:** Node según ruta; HTML; contenido propio; navegador
- **Etiquetas:** `slides` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Slidev](slidev.md) | 49.5k | Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. |
| [Marp](marp.md) | 12.7k | Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separado. |

## Enlaces

- 🐙 GitHub: [hakimel/reveal.js](https://github.com/hakimel/reveal.js)
- 🌐 Web: <https://revealjs.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hakimel/reveal.js/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
