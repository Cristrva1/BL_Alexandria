[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 tree-sitter

> Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.5k | MIT | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Tree-sitter, generador de parsers y librería de parsing incremental. Licencia MIT. Es infraestructura madura (~27k estrellas, v0.27.2) usada por muchos editores y herramientas.

## ¿Qué hace?

Construye un árbol sintáctico concreto de un archivo y lo actualiza eficientemente mientras se edita. Es lo bastante general para cualquier lenguaje, lo bastante rápido para cada pulsación y robusto ante errores de sintaxis. Es la base del resaltado, la navegación y el análisis estructural en editores y herramientas de IA.

## ¿Cómo lo hace?

El runtime está escrito en C puro sin dependencias, con bindings para Rust, Wasm y otros lenguajes. Las gramáticas se generan con la CLI (`tree-sitter generate`), que requiere Node.js para gramáticas en JavaScript.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ast-grep](ast-grep.md) | ast-grep usa Tree-sitter para buscar y reescribir por patrones. | Instala ast-grep; incluye las gramáticas comunes. |
| [Aider](aider.md) | El mapa del repo de Aider se construye con Tree-sitter. | No requiere instalación aparte en Aider. |
| [Repomix](repomix.md) | `repomix --compress` extrae la estructura con Tree-sitter. | Usa la opción `--compress`. |
| [graphify](graphify.md) | Graphify analiza el código con Tree-sitter. | Viene incluido en graphifyy. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.27.2 (2026-11-07) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tree-sitter/tree-sitter/blob/master/README.md) · [2](https://tree-sitter.github.io) · [3](https://aider.chat/docs/repomap.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere IA ni servicios; compilar gramáticas puede necesitar herramientas nativas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es infraestructura de parsing; no contesta por sí sola preguntas sobre arquitectura o intención del código |
| Coste | Sin pago a un modelo en la ruta básica. No requiere IA ni servicios; compilar gramáticas puede necesitar herramientas nativas |
| Equipo | Preparación según la ruta elegida. Herramientas y binding del lenguaje elegido; gramática |

Es infraestructura de parsing; no contesta por sí sola preguntas sobre arquitectura o intención del código

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Herramientas y binding del lenguaje elegido
- gramática

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://tree-sitter.github.io/tree-sitter/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar tree-sitter para mi objetivo y necesito pasos guiados. Lee https://tree-sitter.github.io/tree-sitter/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Analiza un archivo mínimo y observa cómo cambia el árbol tras editar una función.

**Qué comprobar:** El árbol refleja el cambio sin interpretar semánticamente todo el programa.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir un analizador de código
- Extraer símbolos para una herramienta de edición

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir un analizador de código; Extraer símbolos para una herramienta de edición | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es infraestructura de parsing; no contesta por sí sola preguntas sobre arquitectura o intención del código

## Stack y modelos

- **Stack:** Herramientas y binding del lenguaje elegido; gramática
- **Etiquetas:** `code` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter)
- 🌐 Web: <https://tree-sitter.github.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tree-sitter/tree-sitter/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
