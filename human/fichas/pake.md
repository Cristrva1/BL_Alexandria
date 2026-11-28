[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🖥️ Pake

> Convierte una página web o una carpeta con tu web estática en una app de escritorio ligera para macOS, Windows o Linux con un solo comando.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 64.1k | GPL-3.0 | Rust | 2026-11-27 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 60/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia y costes:** Pake es GPL-3.0 con una excepción añadida: las apps que generas pueden distribuirse con la licencia que elijas, incluso privativa. Pake y sus versiones modificadas siguen bajo GPL-3.0, y la marca Pake no puede usarse en productos derivados.

## ¿Qué es?

Herramienta de línea de comandos que empaqueta páginas web como apps de escritorio.

## ¿Qué hace?

Crea un instalador para macOS, Windows o Linux que abre una web o tus archivos HTML en una ventana propia.

## ¿Cómo lo hace?

Usa Tauri y el visor web del sistema operativo en lugar de incluir Chromium; por eso los instaladores ocupan poco.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Slidev](slidev.md) | Empaqueta la carpeta que genera slidev build como app para presentar sin navegador. | — |
| [tailwindcss](tailwindcss.md) | Da estilo a la página propia antes de empaquetarla. | — |
| [Excalidraw](excalidraw.md) | Abre la pizarra en una ventana propia, separada de las pestañas del navegador. | — |

Estado en GitHub: activo · último push 2026-11-25 · última versión publicada V3.21.0 (2026-11-23) · licencia declarada GPL-3.0 (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/README.md) · [2](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/LICENSE) · [3](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/LICENSE-EXCEPTION) · [4](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/TRADEMARK.md) · [5](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/docs/cli-usage.md) · [6](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/docs/faq.md) · [7](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/.github/workflows/quality-and-test.yml) · [8](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/.github/workflows/npm-publish.yml) · [9](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/plugins/pake/skills/pake/SKILL.md) · [10](https://github.com/tw93/Pake/releases/tag/V3.21.0) · [11](https://github.com/tw93/Pake/actions/runs/45192308113) · [12](https://github.com/tw93/Pake/actions/runs/45195435888) · [13](https://github.com/tw93/Pake/security/advisories/GHSA-vq4w-55rh-9ff3) · [14](https://github.com/tw93/Pake/security/advisories/GHSA-6c7f-87jf-wg9w) · [15](https://www.npmjs.com/package/pake-cli/v/3.21.0) · [16](https://pake.run/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita clave de API. Al empaquetar una URL descarga el icono del sitio, y la app resultante carga esa web. |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Empaquetar no usa modelos de IA. |
| Coste | Sin pago a un modelo en la ruta básica. CLI GPL-3.0 gratuita. La app gráfica de pake.run cobra a partir de la tercera app y no es necesaria. |
| Equipo | Preparación según la ruta elegida. Node.js 22.12 o posterior, Rust 1.85 o posterior y herramientas de compilación del sistema. La primera compilación descarga dependencias. |

El repositorio incluye un plugin oficial para Claude Code y Codex que enseña al agente a usar la CLI con --json. Pake no usa la suscripción del agente: la CLI compila en tu equipo.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Instala Node.js 22.12 o posterior, Rust 1.85 o posterior y las herramientas de compilación de tu sistema: Xcode Command Line Tools en macOS, Visual Studio Build Tools en Windows o las bibliotecas de WebKitGTK que indica la guía en Linux.
2. Instala la versión revisada con npm install -g pake-cli@3.21.0 y comprueba que pake --version muestra 3.21.0. No uses versiones anteriores a la 3.17.3.
3. Ejecuta la primera prueba con tu archivo hola.html. La primera compilación tarda más porque prepara el entorno. Abre la app generada y comprueba el contenido.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/tw93/Pake/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/tw93/Pake/releases/tag/V3.21.0)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pake para mi objetivo y necesito pasos guiados. Lee https://github.com/tw93/Pake/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea hola.html con un título y un párrafo propios y ejecuta pake ./hola.html --name HolaPake.

**Qué comprobar:** En la carpeta aparece un instalador (.dmg, .msi, .deb o AppImage). Instálalo y abre HolaPake: la ventana muestra tu título y tu párrafo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir una página de inicio propia en una app con icono y ventana propios
- Empaquetar la carpeta dist de una presentación o herramienta web estática para usarla sin abrir el navegador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir una página de inicio propia en una app con icono y ventana propios; Empaquetar la carpeta dist de una presentación o herramienta web estática para usarla sin abrir el navegador | no quieres instalar Node.js, Rust y herramientas de compilación, o necesitas que la app acceda a funciones del sistema más allá de mostrar la web. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Usa la 3.17.3 o posterior, mejor la 3.21.0. Las apps creadas con versiones anteriores dejaban que los scripts de la web llamaran a funciones nativas, y antes de la 3.13.1 podían escribir archivos fuera de la carpeta de descargas. Reconstruye las apps antiguas y empaqueta solo webs en las que confíes. La app gráfica de pake.run es un producto aparte y de pago.

## Stack y modelos

- **Stack:** Rust, Dockerfile, package.json
- **Etiquetas:** `apps de escritorio` `tauri` `empaquetar web` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [tw93/Pake](https://github.com/tw93/Pake)
- 🌐 Web: <https://pake.run>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/README.md)
- [Fuente 2](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/LICENSE)
- [Fuente 3](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/LICENSE-EXCEPTION)
- [Fuente 4](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/TRADEMARK.md)
- [Fuente 5](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/docs/cli-usage.md)
- [Fuente 6](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/docs/faq.md)
- [Fuente 7](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/.github/workflows/quality-and-test.yml)
- [Fuente 8](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/.github/workflows/npm-publish.yml)
- [Fuente 9](https://github.com/tw93/Pake/blob/705f738d0a96832cc34e5922b4648f299336d567/plugins/pake/skills/pake/SKILL.md)
- [Fuente 10](https://github.com/tw93/Pake/releases/tag/V3.21.0)
- [Fuente 11](https://github.com/tw93/Pake/actions/runs/45192308113)
- [Fuente 12](https://github.com/tw93/Pake/actions/runs/45195435888)
- [Fuente 13](https://github.com/tw93/Pake/security/advisories/GHSA-vq4w-55rh-9ff3)
- [Fuente 14](https://github.com/tw93/Pake/security/advisories/GHSA-6c7f-87jf-wg9w)
- [Fuente 15](https://www.npmjs.com/package/pake-cli/v/3.21.0)
- [Fuente 16](https://pake.run/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
