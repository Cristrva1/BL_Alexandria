[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 tree-sitter

> Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.5k | MIT | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

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

## Qué puedes hacer con él

Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código.

## Por qué destaca

Usos propuestos: Construir un analizador de código; Extraer símbolos para una herramienta de edición.

## Cómo funciona

Es infraestructura de parsing; no contesta por sí sola preguntas sobre arquitectura o intención del código

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Herramientas y binding del lenguaje elegido
- gramática

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ast-grep](ast-grep.md) | 16.6k | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. |
| [Aider](aider.md) | 50.1k | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. |

## Enlaces

- 🐙 GitHub: [tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter)
- 🌐 Web: <https://tree-sitter.github.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tree-sitter/tree-sitter/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
