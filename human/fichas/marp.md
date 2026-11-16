[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Presentaciones

# 🖥️ Marp

> Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.7k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Puntuación de calidad** 47/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Marp, ecosistema para escribir presentaciones en Markdown plano, de marp-team. Licencia MIT. Es maduro (~13k estrellas); este repo es el punto de entrada (web y documentación) a Marpit, Marp Core, Marp CLI y Marp for VS Code.

## ¿Qué hace?

Convierte Markdown en diapositivas con temas y directivas, y exporta a HTML, PDF, PPTX o imágenes.

## ¿Cómo lo hace?

Marp CLI se usa vía npm o npx y Marp for VS Code ofrece previsualización. La exportación a PDF usa un navegador.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Generar Markdown de diapositivas. (combinación por arquitectura) | Pide al agente un .md con directivas Marp. |
| [Mermaid](mermaid.md) | Diagramas. (combinación por arquitectura) | Renderiza a imagen e incrústala. |
| [Pandoc](pandoc.md) | Conversión de documentos a Markdown. (combinación por arquitectura) | Preprocesa el contenido. |

**Notas:** Alternativas (elige una): slidev, reveal.js.

Estado en GitHub: activo · último push 2026-11-07 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/marp-team/marp/blob/main/README.md) · [2](https://marp.app/)</sub>

## Ver similares

Grupo **Presentaciones desde Markdown**: Marp ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Slidev](slidev.md) ⭐ recomendado | 73 | Si buscas esto: presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. |
| 2 | [reveal.js](reveal-js.md) | 59 | Si buscas esto: framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. |
| 3 | **Marp** (esta ficha) | 47 | Si buscas esto: entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separado. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El ecosistema básico no exige API de IA; recursos y distribución tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Este repositorio es la entrada y web del ecosistema; el CLI y extensión están en repos separados y los formatos de exportación no prometen editabilidad nativa equivalente a PPT generado con formas |
| Coste | Sin pago a un modelo en la ruta básica. El ecosistema básico no exige API de IA; recursos y distribución tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Marp CLI o extensión de VS Code; Markdown; contenido propio |

Este repositorio es la entrada y web del ecosistema; el CLI y extensión están en repos separados y los formatos de exportación no prometen editabilidad nativa equivalente a PPT generado con formas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Marp CLI o extensión de VS Code
- Markdown
- contenido propio

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/marp-team/marp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Marp para mi objetivo y necesito pasos guiados. Lee https://github.com/marp-team/marp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige la herramienta Marp CLI o VS Code y exporta tres diapositivas de muestra.

**Qué comprobar:** Puedes comparar Markdown y salida exportada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar slides sencillas
- Versionar una presentación en Git

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar slides sencillas; Versionar una presentación en Git | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Este repositorio es la entrada y web del ecosistema; el CLI y extensión están en repos separados y los formatos de exportación no prometen editabilidad nativa equivalente a PPT generado con formas

## Stack y modelos

- **Stack:** Marp CLI o extensión de VS Code; Markdown; contenido propio
- **Etiquetas:** `slides` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Slidev](slidev.md) | 49.5k | Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. |
| [reveal.js](reveal-js.md) | 72.6k | Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. |

## Enlaces

- 🐙 GitHub: [marp-team/marp](https://github.com/marp-team/marp)
- 🌐 Web: <https://marp.app/>
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/marp-team/marp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
