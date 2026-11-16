[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ AppFlowy

> Espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento propio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 78.9k | AGPL-3.0 | Dart | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Espacio de trabajo con IA, open source y alternativa a Notion, de AppFlowy. Licencia AGPL-3.0. Es maduro y popular (~79k estrellas, 0.15.1) y sigue versionado como 0.x.

## ¿Qué hace?

Ofrece documentos, wikis, bases de datos (tablas, kanban, calendario), proyectos y colaboración en equipo. Incluye funciones de IA (resúmenes, «pregunta a la IA», escritura asistida) con modelos en la nube o, en escritorio, IA local con Ollama. Prioriza el control de los datos: funciona en local y se puede autoalojar el servidor de sincronización.

## ¿Cómo lo hace?

El cliente está hecho con Flutter (Dart) y Rust, y tiene apps para escritorio y móvil. El servidor (AppFlowy-Cloud, repo aparte) se autoaloja con Docker siguiendo la guía oficial. La IA local requiere instalar Ollama y descargar los modelos indicados en la guía.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | IA local en el escritorio de AppFlowy, documentada en su guía de IA local con Ollama. | Instala Ollama, descarga los modelos que pide la guía y actívalo en los ajustes de AppFlowy. |
| [coolify](coolify.md) | Autoalojar el backend de AppFlowy como servicio de un clic (Coolify documenta el servicio AppFlowy). | Instala Coolify, añade el servicio y apunta los clientes a tu URL. |
| [markitdown](markitdown.md) | Convertir documentos existentes a Markdown para importarlos. (combinación por arquitectura) | Convierte con MarkItDown e importa los archivos en AppFlowy. |

**Notas:** Alternativas (elige una): anytype-ts.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 0.15.1 (2026-11-15) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AppFlowy-IO/AppFlowy/blob/main/README.md) · [2](https://appflowy.com/docs/Step-by-step-Self-Hosting-Guide---From-Zero-to-Production) · [3](https://appflowy.com/guide/appflowy-local-ai-ollama) · [4](https://coolify.io/docs/services/appflowy)</sub>

## Ver similares

Grupo **Espacios de trabajo local-first tipo Notion**: AppFlowy ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **AppFlowy** (esta ficha) ⭐ recomendado | 64 | Si buscas esto: espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento propio. |
| 2 | [Anytype Desktop](anytype-ts.md) | 48 | Si buscas esto: cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento personal. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Notas básicas y AI tienen rutas distintas; Cloud, infraestructura y proveedores se cobran según condiciones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Usa el instalador para empezar; la guía from-source es de desarrollo; no se confirma aquí una ruta completa de modelo local |
| Coste | El coste depende del proveedor o la ruta. Notas básicas y AI tienen rutas distintas; Cloud, infraestructura y proveedores se cobran según condiciones |
| Equipo | Preparación según la ruta elegida. Instalador o despliegue elegido; proveedor solo si activas AI |

Usa el instalador para empezar; la guía from-source es de desarrollo; no se confirma aquí una ruta completa de modelo local

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador o despliegue elegido
- proveedor solo si activas AI

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AppFlowy para mi objetivo y necesito pasos guiados. Lee https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una página y una tabla de proyecto antes de activar funciones de IA.

**Qué comprobar:** Puedes editar y recuperar los datos de la página y la tabla.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar un proyecto colaborativo
- Construir una wiki de equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar un proyecto colaborativo; Construir una wiki de equipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Usa el instalador para empezar; la guía from-source es de desarrollo; no se confirma aquí una ruta completa de modelo local

## Stack y modelos

- **Stack:** Instalador o despliegue elegido; proveedor solo si activas AI
- **Etiquetas:** `notas` `app` `dart`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Anytype Desktop](anytype-ts.md) | 9.1k | Cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento personal. |

## Enlaces

- 🐙 GitHub: [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)
- 🌐 Web: <https://appflowy.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AppFlowy-IO/AppFlowy/blob/main/README.md)
- [Fuente 2](https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
