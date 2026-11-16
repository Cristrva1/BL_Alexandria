[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🖥️ Biome

> Formateador y linter en un solo binario para JavaScript, TypeScript, JSX, JSON, CSS, GraphQL y más, usable por CLI y LSP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.1k | Apache-2.0 | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Cadena de herramientas de código abierto (doble licencia MIT o Apache-2.0) mantenida por la comunidad Biome, sucesora de Rome. Muy activa y adoptada en proyectos web.

## ¿Qué hace?

Formatea JavaScript, TypeScript, JSX, JSON, CSS, GraphQL, HTML, Markdown, YAML y SCSS con un 97 % de compatibilidad con Prettier según el proyecto, y analiza con más de 750 reglas que cubren casos de ESLint, typescript-eslint y otras fuentes, con diagnósticos detallados y correcciones automáticas.

## ¿Cómo lo hace?

Escrito en Rust; se instala con npm (`npm install --save-dev --save-exact @biomejs/biome`) u otros gestores, y se usa con `biome format`, `biome lint`, `biome check` y `biome ci`. Tiene extensiones oficiales para editores y servidor LSP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pre-commit](pre-commit.md) | Biome publica hooks oficiales para pre-commit que ejecutan check o format sobre los archivos cambiados. | Instala pre-commit; después añade el repositorio de hooks de Biome. |
| [tailwindcss](tailwindcss.md) | Biome incluye una regla para ordenar clases de utilidad de Tailwind CSS (useSortedClasses, que la próxima versión reubica en opciones propias de Tailwind). | Proyecto con Tailwind; después activa la regla de clases ordenadas en biome.json. |
| [Claude Code](claude-code.md) | Un agente de código puede ejecutar `biome check --write` tras cada cambio para dejar el código formateado y sin avisos (combinación por arquitectura). | Añade Biome al proyecto; después indícale al agente que lo ejecute antes de terminar. |

**Notas:** Algunos plugins de ESLint no tienen equivalente en Biome: revisa las reglas que necesitas antes de migrar.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada @biomejs/biome@2.6.8 (2026-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.md) · [2](https://biomejs.dev/) · [3](https://github.com/biomejs/pre-commit) · [4](https://github.com/biomejs/biome/blob/main/crates/biome_migrate/src/analyzers/tailwind_options.rs)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
npm install --save-dev --save-exact @biomejs/biome
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/biomejs/biome/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Biome para mi objetivo y necesito pasos guiados. Lee https://github.com/biomejs/biome/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala `@biomejs/biome` como dependencia de desarrollo y ejecuta `npx @biomejs/biome check --write`..

**Qué comprobar:** Biome formatea y corrige los archivos y lista los problemas restantes..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- sustituir ESLint y Prettier en un proyecto web por una sola herramienta
- formatear y revisar el código que genera un agente antes de abrir un PR

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: sustituir ESLint y Prettier en un proyecto web por una sola herramienta; formatear y revisar el código que genera un agente antes de abrir un PR | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Rust, Cargo.toml, package.json
- **Etiquetas:** `code` `javascript` `typescript` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [biomejs/biome](https://github.com/biomejs/biome)
- 🌐 Web: <https://biomejs.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/biomejs/biome/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
