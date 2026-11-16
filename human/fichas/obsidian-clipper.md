[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ obsidian-clipper

> Extensión oficial para capturar páginas y fragmentos de la web y guardarlos como notas en Obsidian.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.6k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Obsidian Web Clipper, la extensión oficial de navegador de Obsidian para capturar y subrayar la web. Código MIT; las marcas y recursos de marketing quedan excluidos. Es activa (~6k estrellas, 1.7.1).

## ¿Qué hace?

Guarda páginas web como archivos Markdown duraderos en tu vault, legibles sin conexión. Permite subrayar, usar plantillas con variables y lógica (if/for) y, con el Interpreter, extraer o resumir datos con un modelo de lenguaje que configures. Funciona en Chrome y derivados, Firefox, Edge y Safari (macOS, iOS, iPadOS).

## ¿Cómo lo hace?

Se instala desde la tienda de extensiones de cada navegador. Está escrito en TypeScript y usa Defuddle para extraer el contenido y convertirlo a Markdown. La documentación oficial está en la ayuda de Obsidian.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [defuddle](defuddle.md) | Motor de extracción de contenido y conversión a Markdown que usa el Clipper, según su README. | Viene incluido; úsalo aparte solo si quieres la misma extracción en scripts. |
| [claude-obsidian](claude-obsidian.md) | Capturar fuentes en la carpeta `inbox/` para que el agente las convierta en wiki. (combinación por arquitectura) | Configura una plantilla del Clipper que guarde en `inbox/`. |
| [kepano-obsidian](kepano-obsidian.md) | Guardar los recortes dentro de una estructura de vault ya pensada. (combinación por arquitectura) | Apunta la carpeta de destino del Clipper al vault de plantilla. |
| [obsidian-help](obsidian-help.md) | Combinación recíproca: obsidian-help lo enlaza como «La documentación del Web Clipper vive en la ayuda oficial». | Orden indicado desde obsidian-help: Lee la sección del Web Clipper antes de crear plantillas. |
| [obsidian-minimal](obsidian-minimal.md) | Combinación recíproca: obsidian-minimal lo enlaza como «Lectura cómoda de los artículos capturados. (combinación por arquitectura)». | Orden indicado desde obsidian-minimal: Captura con el Web Clipper y lee las notas con Minimal. |

**Notas:** Sin alternativas declaradas. El Interpreter envía el contenido de la página al proveedor de modelos que configures.

Estado en GitHub: activo · último push 2026-09-22 · última versión publicada 1.7.1 (2026-07-22) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/obsidianmd/obsidian-clipper/blob/main/README.md) · [2](https://help.obsidian.md/web-clipper) · [3](https://help.obsidian.md/web-clipper/interpreter)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El recorte normal no usa LLM; Interpreter puede llamar API o usar Ollama local; sus modelos mantienen costes y recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Guardar notas localmente no hace local una petición Interpreter a un proveedor remoto; Ollama necesita permisos de origen para la extensión |
| Coste | El coste depende del proveedor o la ruta. El recorte normal no usa LLM; Interpreter puede llamar API o usar Ollama local; sus modelos mantienen costes y recursos propios |
| Equipo | Preparación según la ruta elegida. Extensión oficial del navegador; Obsidian; modelo solo para Interpreter |

Guardar notas localmente no hace local una petición Interpreter a un proveedor remoto; Ollama necesita permisos de origen para la extensión

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Extensión oficial del navegador
- Obsidian
- modelo solo para Interpreter

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://help.obsidian.md/web-clipper)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar obsidian-clipper para mi objetivo y necesito pasos guiados. Lee https://help.obsidian.md/web-clipper. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda un artículo público de prueba con título, URL y fragmento y comprueba el Markdown.

**Qué comprobar:** La nota conserva el contenido y la referencia de origen.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Capturar lecturas con una plantilla
- Extraer un resumen opcional con Interpreter

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Capturar lecturas con una plantilla; Extraer un resumen opcional con Interpreter | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Guardar notas localmente no hace local una petición Interpreter a un proveedor remoto; Ollama necesita permisos de origen para la extensión

## Stack y modelos

- **Stack:** Extensión oficial del navegador; Obsidian; modelo solo para Interpreter
- **Etiquetas:** `notas` `app` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [obsidianmd/obsidian-clipper](https://github.com/obsidianmd/obsidian-clipper)
- 🌐 Web: <https://obsidian.md/clipper>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/obsidianmd/obsidian-clipper/blob/main/README.md)
- [Fuente 2](https://obsidian.md/help/web-clipper/interpreter)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
