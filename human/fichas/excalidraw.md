[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# ✏️ Excalidraw

> Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 136k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Pizarra virtual open source (MIT) con estilo dibujado a mano, colaborativa y con cifrado de extremo a extremo. Es muy madura y popular (~136k estrellas, v0.18.1). Tiene una versión comercial, Excalidraw+, con funciones para equipos.

## ¿Qué hace?

Ofrece un lienzo infinito para diagramas, wireframes y bocetos con rectángulos, elipses, rombos, flechas con enlace y etiquetas, dibujo libre y borrador. Incluye modo oscuro, imágenes, bibliotecas de formas, i18n, deshacer y rehacer, y zoom. Exporta a PNG, SVG, portapapeles y a un formato abierto `.excalidraw` (JSON). La app web añade colaboración en tiempo real y cifrado E2E.

## ¿Cómo lo hace?

Se usa en excalidraw.com o se embebe en apps React con `npm install react react-dom @excalidraw/excalidraw`. El componente es personalizable y tiene API. Hay integraciones comunitarias, como una extensión de VS Code. El formato JSON abierto permite que herramientas o agentes generen diagramas programáticamente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Generar o editar diagramas `.excalidraw` (JSON abierto) desde un agente. (combinación por arquitectura) | Pide al agente que escriba el JSON y ábrelo en Excalidraw. |
| [penpot](penpot.md) | Pasar de bocetos rápidos a diseño de alta fidelidad. (combinación por arquitectura) | Boceta en Excalidraw y diseña la versión final en Penpot. |
| [flexoki](flexoki.md) | Paleta coherente para diagramas de documentación. (combinación por arquitectura) | Define los colores personalizados en la paleta del lienzo. |
| [Kroki](kroki.md) | Combinación recíproca: Kroki lo enlaza como «Kroki renderiza Excalidraw con el contenedor complementario `yuzutech/kroki-excalidraw`». | Orden indicado desde Kroki: Despliega Kroki y `kroki-excalidraw`; después envía el JSON a `/excalidraw/svg`. |

**Notas:** Alternativas (elige una): tldraw, mermaid.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.18.1 (2026-04-21) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/excalidraw/excalidraw/blob/master/README.md) · [2](https://docs.excalidraw.com)</sub>

## Ver similares

Grupo **Pizarras y diagramas a mano alzada**: Excalidraw ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Excalidraw** (esta ficha) ⭐ recomendado | 70 | Si buscas esto: pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa. |
| 2 | [tldraw](tldraw.md) | 55 | Si buscas esto: sDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La pizarra básica no requiere IA; productos alojados adicionales pueden tener planes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Para dibujar puedes usar la app web; npm instala el componente para integrarlo en otra aplicación |
| Coste | Sin pago a un modelo en la ruta básica. La pizarra básica no requiere IA; productos alojados adicionales pueden tener planes |
| Equipo | Preparación según la ruta elegida. Navegador para la app; React solo si integras el componente |

Para dibujar puedes usar la app web; npm instala el componente para integrarlo en otra aplicación

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador para la app
- React solo si integras el componente

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/excalidraw/excalidraw/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Excalidraw para mi objetivo y necesito pasos guiados. Lee https://github.com/excalidraw/excalidraw/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Dibuja tres pasos de un proceso y exporta el diagrama como imagen.

**Qué comprobar:** Puedes abrir la imagen y conservar el archivo editable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explicar un flujo a un equipo
- Bocetar una interfaz antes de construirla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explicar un flujo a un equipo; Bocetar una interfaz antes de construirla | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Para dibujar puedes usar la app web; npm instala el componente para integrarlo en otra aplicación

## Stack y modelos

- **Stack:** Navegador para la app; React solo si integras el componente
- **Etiquetas:** `design` `docs` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [tldraw](tldraw.md) | 51.4k | SDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas. |
| [Mermaid](mermaid.md) | 91.1k | Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown. |

## Enlaces

- 🐙 GitHub: [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)
- 🌐 Web: <https://excalidraw.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/excalidraw/excalidraw/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
