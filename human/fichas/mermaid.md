[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Diagramas y documentación

# 🗺️ Mermaid

> Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 91.1k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 78/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Mermaid, herramienta para generar diagramas a partir de texto tipo Markdown, de mermaid-js. Licencia MIT. Es madura y muy extendida (~91k estrellas), y tiene soporte nativo en GitHub, Slidev y muchas otras herramientas.

## ¿Qué hace?

Dibuja diagramas de flujo, de secuencia, de clases, de estados, ER, Gantt, mindmaps y más, con un editor en vivo.

## ¿Cómo lo hace?

Se usa con `npm install mermaid` o desde CDN en el navegador; existe mermaid-cli para generar imágenes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Slidev](slidev.md) | Diagramas en presentaciones. | Usa bloques mermaid en Slidev. |
| [Claude Code](claude-code.md) | Los agentes generan diagramas en Mermaid. (combinación por arquitectura) | Pide diagramas en sintaxis Mermaid. |
| [archify](archify.md) | Combinación recíproca: archify lo enlaza como «Diagramas textuales para documentación estática. (combinación por arquitectura)». | Orden indicado desde archify: Usa Mermaid en docs y Archify para explorar. |
| [Marp](marp.md) | Combinación recíproca: Marp lo enlaza como «Diagramas. (combinación por arquitectura)». | Orden indicado desde Marp: Renderiza a imagen e incrústala. |
| [reveal.js](reveal-js.md) | Combinación recíproca: reveal.js lo enlaza como «Diagramas en las diapositivas. (combinación por arquitectura)». | Orden indicado desde reveal.js: Añade un plugin de Mermaid. |
| [draw.io](drawio.md) | Combinación recíproca: draw.io lo enlaza como «draw.io importa diagramas Mermaid y los convierte en diagramas editables». | Orden indicado desde draw.io: Escribe el diagrama en Mermaid; después usa Organizar > Insertar > Avanzado > Mermaid en draw.io. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Kroki](kroki.md)

**Notas:** Alternativas (elige una): excalidraw.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada @mermaid-js/examples@2.1.0 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mermaid-js/mermaid/blob/develop/README.md) · [2](https://mermaid.js.org/)</sub>

## Ver similares

Grupo **Diagramas como código**: Mermaid ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Mermaid** (esta ficha) ⭐ recomendado | 78 | Si buscas esto: genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown. |
| 2 | [D2](d2.md) | 58 | Si buscas esto: lenguaje declarativo de diagramas que convierte texto en diagramas SVG, PNG, PDF o PPTX, con temas, modo boceto y tres motores de layout incluidos. |
| 3 | [PlantUML](plantuml.md) | 55 | Si buscas esto: herramienta clásica que genera diagramas UML y técnicos (secuencia, clases, actividad, Gantt, mapas mentales) a partir de descripciones de texto. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El render básico MIT no necesita API de IA; servicios hospedados o AI son ofertas independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No requiere un LLM para convertir sintaxis a diagramas; un diagrama válido puede representar un proceso equivocado y necesita revisión |
| Coste | Sin pago a un modelo en la ruta básica. El render básico MIT no necesita API de IA; servicios hospedados o AI son ofertas independientes |
| Equipo | Preparación según la ruta elegida. Editor o entorno que renderice Mermaid; texto del proceso |

No requiere un LLM para convertir sintaxis a diagramas; un diagrama válido puede representar un proceso equivocado y necesita revisión

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Editor o entorno que renderice Mermaid
- texto del proceso

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mermaid-js/mermaid/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Mermaid para mi objetivo y necesito pasos guiados. Lee https://github.com/mermaid-js/mermaid/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Escribe un flujo con una decisión y comprueba que sus flechas representan el proceso real.

**Qué comprobar:** Puedes relacionar cada nodo con un paso.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Documentar un proceso
- Preparar un diagrama de secuencia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Documentar un proceso; Preparar un diagrama de secuencia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No requiere un LLM para convertir sintaxis a diagramas; un diagrama válido puede representar un proceso equivocado y necesita revisión

## Stack y modelos

- **Stack:** Editor o entorno que renderice Mermaid; texto del proceso
- **Etiquetas:** `docs` `dataviz` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Excalidraw](excalidraw.md) | 136k | Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa. |
| [D2](d2.md) | 25.8k | Lenguaje declarativo de diagramas que convierte texto en diagramas SVG, PNG, PDF o PPTX, con temas, modo boceto y tres motores de layout incluidos. |
| [PlantUML](plantuml.md) | 13.4k | Herramienta clásica que genera diagramas UML y técnicos (secuencia, clases, actividad, Gantt, mapas mentales) a partir de descripciones de texto. |

## Enlaces

- 🐙 GitHub: [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)
- 🌐 Web: <https://mermaid.ai/open-source/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mermaid-js/mermaid/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
