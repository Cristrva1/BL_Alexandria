[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Presentaciones

# 🖥️ Slidev

> Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 49.5k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Slidev, presentaciones para desarrolladores escritas en Markdown, de Anthony Fu y slidevjs. Licencia MIT. Es madura (~49k estrellas, v53.1.0).

## ¿Qué hace?

Crea diapositivas con Markdown, componentes Vue, resaltado de código, diagramas Mermaid, LaTeX, grabación, modo presentador y exportación a PDF, PPTX o PNG.

## ¿Cómo lo hace?

Requiere Node.js 22.12+ y se inicia con `npm init slidev`. Usa Vite para la recarga instantánea.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Mermaid](mermaid.md) | Diagramas integrados en Markdown. | Escribe bloques mermaid. |
| [Claude Code](claude-code.md) | Generar diapositivas en Markdown. (combinación por arquitectura) | Pide al agente el slides.md. |
| [playwright](playwright.md) | Exportación a PDF o PNG. | Instala playwright-chromium cuando lo pida. |
| [diagram-design](diagram-design.md) | Combinación recíproca: diagram-design lo enlaza como «Incrustar diagramas en presentaciones. (combinación por arquitectura)». | Orden indicado desde diagram-design: Exporta SVG/PNG e insértalos. |

**Notas:** Alternativas (elige una): marp, reveal.js.

Estado en GitHub: activo · último push 2026-11-05 · última versión publicada v53.1.0 (2026-11-05) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/slidevjs/slidev/blob/main/README.md) · [2](https://sli.dev/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. MIT y sin API de IA obligatoria; hosting y recursos externos tienen condiciones independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una herramienta orientada a Markdown y componentes Vue; utilizar un agente para escribir el contenido no la convierte en plugin de ese agente |
| Coste | Sin pago a un modelo en la ruta básica. MIT y sin API de IA obligatoria; hosting y recursos externos tienen condiciones independientes |
| Equipo | Preparación según la ruta elegida. Node; editor de texto; navegador; contenido propio |

Es una herramienta orientada a Markdown y componentes Vue; utilizar un agente para escribir el contenido no la convierte en plugin de ese agente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- editor de texto
- navegador
- contenido propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm init slidev
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/slidevjs/slidev/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Slidev para mi objetivo y necesito pasos guiados. Lee https://github.com/slidevjs/slidev/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea tres diapositivas Markdown y modifica una antes de exportar.

**Qué comprobar:** Puedes comprobar contenido, notas y navegación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una charla técnica
- Explicar un ejemplo de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una charla técnica; Explicar un ejemplo de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una herramienta orientada a Markdown y componentes Vue; utilizar un agente para escribir el contenido no la convierte en plugin de ese agente

## Stack y modelos

- **Stack:** Node; editor de texto; navegador; contenido propio
- **Etiquetas:** `slides` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marp](marp.md) | 12.7k | Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separado. |
| [reveal.js](reveal-js.md) | 72.6k | Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. |

## Enlaces

- 🐙 GitHub: [slidevjs/slidev](https://github.com/slidevjs/slidev)
- 🌐 Web: <https://sli.dev>
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/slidevjs/slidev/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
