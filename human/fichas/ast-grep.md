[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🛡️ ast-grep

> CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.6k | MIT | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

ast-grep (sg), CLI en Rust para búsqueda estructural, lint y reescritura de código, de @HerringtonDarkholme. Licencia MIT. Es activa (~17k estrellas, 0.51.2).

## ¿Qué hace?

Busca código con patrones escritos como código normal, usando `$VAR` como comodín para nodos del AST. Permite crear reglas de lint en YAML y aplicar reescrituras masivas. Soporta muchos lenguajes y tiene un playground online.

## ¿Cómo lo hace?

Se instala con `npm install --global @ast-grep/cli` (Node.js 20+), `pip install ast-grep-cli`, `brew` o `cargo install ast-grep --locked`. Está escrito en Rust sobre Tree-sitter.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tree-sitter](tree-sitter.md) | Usa gramáticas de Tree-sitter. | No requiere instalación aparte. |
| [Claude Code](claude-code.md) | Dar al agente búsquedas y refactorizaciones estructurales. (combinación por arquitectura) | Instala `sg` y permite al agente usarlo. |
| [Aider](aider.md) | Aplicar refactorizaciones masivas deterministas junto a la edición con IA. (combinación por arquitectura) | Usa ast-grep para el cambio mecánico y Aider para el resto. |

**Notas:** Alternativas (elige una): semgrep.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 0.51.2 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ast-grep/ast-grep/blob/main/README.md) · [2](https://ast-grep.github.io)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; solo recursos locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Empieza por búsqueda; revisa el diff de una reescritura antes de aplicarla al proyecto entero |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelo ni API; solo recursos locales |
| Equipo | Preparación según la ruta elegida. Node y npm para esta ruta; archivos de prueba |

Empieza por búsqueda; revisa el diff de una reescritura antes de aplicarla al proyecto entero

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node y npm para esta ruta
- archivos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install --global @ast-grep/cli
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ast-grep/ast-grep/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ast-grep para mi objetivo y necesito pasos guiados. Lee https://github.com/ast-grep/ast-grep/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Busca una llamada por su estructura y revisa los resultados antes de reescribir.

**Qué comprobar:** Encuentras la expresión aunque varíe el espaciado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Migrar llamadas de una API
- Aplicar reglas de lint personalizadas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Migrar llamadas de una API; Aplicar reglas de lint personalizadas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Empieza por búsqueda; revisa el diff de una reescritura antes de aplicarla al proyecto entero

## Stack y modelos

- **Stack:** Node y npm para esta ruta; archivos de prueba
- **Etiquetas:** `code` `security` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Semgrep](semgrep.md) | 17.7k | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. |

## Enlaces

- 🐙 GitHub: [ast-grep/ast-grep](https://github.com/ast-grep/ast-grep)
- 🌐 Web: <https://ast-grep.github.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ast-grep/ast-grep/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
