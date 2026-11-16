[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 📂 jsoncanvas

> Especificación abierta de JSON Canvas para describir nodos y conexiones de un lienzo visual en un archivo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.9k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Especificación abierta JSON Canvas para datos de lienzos infinitos, creada por Obsidian. Licencia MIT. Es estable (~4k estrellas, especificación 1.0) y se actualiza poco.

## ¿Qué hace?

Define un formato `.canvas` legible y fácil de parsear para nodos (texto, archivo, enlace, grupo) y conexiones entre ellos, pensado para longevidad e interoperabilidad. Cualquier app puede implementarlo libremente para importar, exportar o almacenar. El sitio mantiene un listado de apps y herramientas que lo usan.

## ¿Cómo lo hace?

El repo contiene la especificación, el sitio jsoncanvas.org y ejemplos. Para usarlo basta con leer o escribir JSON según la especificación 1.0; Obsidian Canvas lo usa de forma nativa.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [obsidian-skills](obsidian-skills.md) | La skill oficial `json-canvas` enseña a los agentes a crear y editar archivos `.canvas` válidos. | Instala obsidian-skills en el agente y pídele lienzos. |
| [Claude Code](claude-code.md) | Generar mapas, diagramas o tableros como `.canvas` desde un agente. (combinación por arquitectura) | Da al agente la especificación o la skill y abre el resultado en Obsidian. |
| [obsidian-help](obsidian-help.md) | La ayuda oficial de Obsidian documenta Canvas, la implementación de referencia del formato `.canvas` (página `Plugins/Canvas`). | Lee la especificación 1.0 y contrasta el comportamiento en la página de Canvas de la ayuda. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-07-24 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/obsidianmd/jsoncanvas/blob/main/readme.md) · [2](https://jsoncanvas.org/spec/1.0/) · [3](https://obsidian.md/blog/json-canvas/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La especificación no requiere modelo ni servicio; cada aplicación define sus costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un formato, no un editor de canvas listo para instalar |
| Coste | Sin pago a un modelo en la ruta básica. La especificación no requiere modelo ni servicio; cada aplicación define sus costes |
| Equipo | Preparación según la ruta elegida. Editor de texto; aplicación compatible con JSON Canvas |

Es un formato, no un editor de canvas listo para instalar

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Editor de texto
- aplicación compatible con JSON Canvas

1. Lee el esquema y crea un lienzo de dos notas conectadas usando una app compatible.
2. Comprueba: Puedes abrir el archivo y reconocer nodos y conexión en JSON.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/obsidianmd/jsoncanvas/blob/main/readme.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar jsoncanvas para mi objetivo y necesito pasos guiados. Lee https://github.com/obsidianmd/jsoncanvas/blob/main/readme.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee el esquema y crea un lienzo de dos notas conectadas usando una app compatible.

**Qué comprobar:** Puedes abrir el archivo y reconocer nodos y conexión en JSON.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Intercambiar un mapa de ideas
- Estudiar un formato abierto de lienzo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Intercambiar un mapa de ideas; Estudiar un formato abierto de lienzo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un formato, no un editor de canvas listo para instalar

## Stack y modelos

- **Stack:** Editor de texto; aplicación compatible con JSON Canvas
- **Etiquetas:** `notas` `reference` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [obsidianmd/jsoncanvas](https://github.com/obsidianmd/jsoncanvas)
- 🌐 Web: <https://jsoncanvas.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/obsidianmd/jsoncanvas/blob/main/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
