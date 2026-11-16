[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🎬 palmier-pro

> Editor de video para macOS con herramientas de IA y MCP cuyo repositorio conserva código histórico y binarios actuales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.8k | GPL-3.0 | Swift | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Palmier Pro, editor de vídeo para macOS con IA y MCP, de Palmier. El código hasta la v0.7.6 (rama `last-gpl-source`) se publicó con GPLv3; las versiones posteriores son binarios propietarios sin código publicado. Tiene ~15k estrellas (v0.12.1).

## ¿Qué hace?

Combina un editor de línea de tiempo con generación por IA integrada y un agente en la app. Mientras está abierto expone un servidor MCP en `http://127.0.0.1:19789/mcp` para que Claude, Codex o Cursor creen y editen en la línea de tiempo.

## ¿Cómo lo hace?

Requiere macOS 26 (Tahoe) en Apple Silicon. Se conecta con `claude mcp add --transport http palmier-pro …` o `codex mcp add palmier-pro --url …`. El repositorio solo aloja releases binarias y el código GPL histórico.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Conexión MCP documentada. | Abre la app y añade el servidor MCP HTTP. |
| [Codex CLI](codex.md) | Conexión MCP documentada. | Ejecuta `codex mcp add palmier-pro --url …`. |
| [FFmpeg](ffmpeg.md) | Preparar medios antes de importarlos. (combinación por arquitectura) | Convierte los formatos no soportados con FFmpeg. |

**Notas:** Sin alternativas declaradas. Pregunta de pertenencia al catálogo: el producto actual es propietario.

Estado en GitHub: activo · último push 2026-11-02 · última versión publicada v0.12.1 (2026-11-02) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/palmier-io/palmier-pro/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las versiones posteriores a 0.7.6 son binarias propietarias; agente y modelos tienen costes propios según ruta |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. El código GPL histórico no concede automáticamente la licencia de los binarios actuales; MCP local HTTP está documentado para Claude y Codex |
| Coste | El coste depende del proveedor o la ruta. Las versiones posteriores a 0.7.6 son binarias propietarias; agente y modelos tienen costes propios según ruta |
| Equipo | Preparación según la ruta elegida. Apple Silicon; macOS 26; binario y licencia de su versión; cliente opcional |

El código GPL histórico no concede automáticamente la licencia de los binarios actuales; MCP local HTTP está documentado para Claude y Codex

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Apple Silicon
- macOS 26
- binario y licencia de su versión
- cliente opcional

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/palmier-io/palmier-pro/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar palmier-pro para mi objetivo y necesito pasos guiados. Lee https://github.com/palmier-io/palmier-pro/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una copia de un proyecto y consulta su timeline mediante MCP antes de editar.

**Qué comprobar:** El agente identifica pistas y clips del proyecto correcto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar cortes con un agente
- Revisar una secuencia desde herramientas externas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar cortes con un agente; Revisar una secuencia desde herramientas externas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El código GPL histórico no concede automáticamente la licencia de los binarios actuales; MCP local HTTP está documentado para Claude y Codex

## Stack y modelos

- **Stack:** Apple Silicon; macOS 26; binario y licencia de su versión; cliente opcional
- **Etiquetas:** `edicion` `ai-video` `claude` `macos` `mcp` `seedance2` `swift` `video-editor`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro)
- 🌐 Web: <https://palmier.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/palmier-io/palmier-pro/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
