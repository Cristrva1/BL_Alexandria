[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › CSS y estilos

# 📂 flexoki

> Paleta de color para texto, código e interfaces que puede servir de referencia al definir un sistema visual.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.8k | MIT | CSS | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## ¿Qué es?

Esquema de color (MIT) de @kepano (stephango.com, también autor del tema Minimal de Obsidian) pensado para leer y escribir en pantallas, inspirado en tintas de imprenta y tonos de papel. Versión 2.0.0; último push en marzo de 2026.

## ¿Qué hace?

Define una paleta de colores para prosa, código e interfaces, con variantes claras y oscuras y resaltado de sintaxis. Tiene ports para decenas de aplicaciones y herramientas, la mayoría comunitarios: Alacritty, Chrome, Discord, Emacs, Neovim, Obsidian, VS Code, Vim, terminales y Tailwind, entre otros.

## ¿Cómo lo hace?

Se usa instalando el port de cada aplicación o copiando los valores de color (hex, variables CSS) desde stephango.com/flexoki. El port de Tailwind lo mantiene la comunidad (@bslobodin). No es software, sino una especificación de colores con archivos de tema.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tailwindcss](tailwindcss.md) | Usar la paleta como colores del tema mediante el port de Tailwind listado en el README. | Copia el port y regístralo en `@theme`. |
| [daisyUI](daisyui.md) | Crear un tema daisyUI propio con los colores de Flexoki. (combinación por arquitectura) | Define un tema personalizado con las variables de la paleta. |
| [Excalidraw](excalidraw.md) | Paleta coherente para diagramas y documentación visual. (combinación por arquitectura) | Configura los colores personalizados en Excalidraw. |
| [normalize.css](normalize-css.md) | Combinación recíproca: normalize.css lo enlaza como «Paleta de color sobre una base de estilos normalizada en un sitio de CSS propio. (combinación por arquitectura)». | Orden indicado desde normalize.css: Importa normalize.css y define las variables de color de Flexoki. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-03-07 · última versión publicada 2.0.0 (2025-01-07) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kepano/flexoki/blob/main/README.md) · [2](https://stephango.com/flexoki)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; el proyecto pide atribución al portar la paleta |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una referencia de color y sus ports; no instala una aplicación ni garantiza contraste en cualquier combinación |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelo ni API; el proyecto pide atribución al portar la paleta |
| Equipo | Preparación según la ruta elegida. Navegador o editor con un tema compatible |

Es una referencia de color y sus ports; no instala una aplicación ni garantiza contraste en cualquier combinación

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador o editor con un tema compatible

1. Aplica la paleta a una página de prueba y comprueba contraste de texto y controles.
2. Comprueba: Puedes identificar colores semánticos legibles en claro y oscuro.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/kepano/flexoki/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar flexoki para mi objetivo y necesito pasos guiados. Lee https://github.com/kepano/flexoki/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Aplica la paleta a una página de prueba y comprueba contraste de texto y controles.

**Qué comprobar:** Puedes identificar colores semánticos legibles en claro y oscuro.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Definir una paleta para una app de notas
- Crear un tema de editor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Definir una paleta para una app de notas; Crear un tema de editor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una referencia de color y sus ports; no instala una aplicación ni garantiza contraste en cualquier combinación

## Stack y modelos

- **Stack:** Navegador o editor con un tema compatible
- **Etiquetas:** `estilos` `reference` `css`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [kepano/flexoki](https://github.com/kepano/flexoki)
- 🌐 Web: <https://stephango.com/flexoki>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kepano/flexoki/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
