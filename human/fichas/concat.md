[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🖥️ Concat

> Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.6k | AGPL-3.0 | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Concat, editor de vídeo libre y multiplataforma, de @jub0t. Licencia AGPL-3.0 o posterior, con licencia comercial disponible. Es reciente (~18k estrellas, v0.2.11).

## ¿Qué hace?

Cubre lo habitual en edición (cortes, pistas, efectos) y añade subtítulos automáticos, texto a voz y recorte de fondo con modelos que se descargan una vez y funcionan sin conexión. Incluye un servidor MCP (`concat --mcp`) y una API JSON-RPC para que agentes y scripts editen.

## ¿Cómo lo hace?

Se descarga desde su web o desde GitHub Releases para macOS, Windows, Linux y Android. Está escrito en Rust y usa FFmpeg (en macOS se instala con `brew install ffmpeg`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Servidor MCP integrado documentado. | Configura `concat --mcp` en el agente. |
| [FFmpeg](ffmpeg.md) | Dependencia para leer y exportar medios. | Instala FFmpeg en el sistema. |
| [yt-dlp](yt-dlp.md) | Editar material descargado. (combinación por arquitectura) | Descarga y abre el archivo en Concat. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.2.11 (2026-11-13) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jub0t/Concat/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La edición y modelos locales no necesitan API; AGPL y licencia comercial para ciertos usos cerrados tienen condiciones distintas |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Está en beta; MCP puede usar la ventana o un proceso separado y sus modos tienen límites distintos al editar el mismo proyecto |
| Coste | El coste depende del proveedor o la ruta. La edición y modelos locales no necesitan API; AGPL y licencia comercial para ciertos usos cerrados tienen condiciones distintas |
| Equipo | Preparación según la ruta elegida. Distribución compatible; clip propio; modelos opcionales descargados; permisos de automatización para MCP |

Está en beta; MCP puede usar la ventana o un proceso separado y sus modos tienen límites distintos al editar el mismo proyecto

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Distribución compatible
- clip propio
- modelos opcionales descargados
- permisos de automatización para MCP

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/jub0t/Concat/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Concat para mi objetivo y necesito pasos guiados. Lee https://github.com/jub0t/Concat/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Recorta una copia de un clip y añade subtítulos locales antes de exportar.

**Qué comprobar:** Puedes revisar texto, puntos de corte y archivo final.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Editar un video sin subir el material
- Automatizar una variante de montaje mediante MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Editar un video sin subir el material; Automatizar una variante de montaje mediante MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Está en beta; MCP puede usar la ventana o un proceso separado y sus modos tienen límites distintos al editar el mismo proyecto

## Stack y modelos

- **Stack:** Distribución compatible; clip propio; modelos opcionales descargados; permisos de automatización para MCP
- **Etiquetas:** `edicion` `app` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jub0t/Concat](https://github.com/jub0t/Concat)
- 🌐 Web: <https://concat.standalones.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jub0t/Concat/blob/main/README.md)
- [Fuente 2](https://github.com/jub0t/Concat/blob/main/docs/MCP.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
