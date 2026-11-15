[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ DaVinci Resolve MCP

> Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.1k | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | Consumo del agente que ya utilizas. Necesita DaVinci Resolve instalado y su API de scripting; algunas funciones dependen de la edición de Resolve. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Expone la API oficial de scripting de DaVinci Resolve como herramientas MCP para Claude, Cursor, Codex y otros clientes. Cubre montaje, organización del media pool, render, marcadores, color, Fusion y Fairlight, y añade análisis de medios que nunca modifica los originales. Incluye un panel de control local en el navegador.

## Por qué destaca

Cubre casi toda la API de Resolve, en un modo compacto de 37 herramientas o uno granular de 390, con operaciones protegidas. El instalador configura automáticamente una docena de clientes MCP.

## Cómo funciona

Servidor Python que se conecta a un Resolve abierto por su API de scripting externo y agrupa operaciones por acción para ahorrar contexto. Un servidor Node opcional edita archivos .drp/.drt sin Resolve abierto; ffmpeg y Whisper amplían el análisis.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

[Instrucciones originales de instalación](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DaVinci Resolve MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Pedir a Claude que arme un timeline con clips del media pool
- Automatizar ajustes de render y colas de exportación
- Transcribir clips y escribir marcadores y metadatos en el proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| editas en DaVinci Resolve y quieres que un agente MCP automatice montaje, render o metadatos | no usas Resolve o prefieres montar video por código sin editor; mira `moviepy` o `ffmpeg` |

**Limitaciones:** El scripting externo solo funciona en Resolve Studio (de pago); en la edición gratuita depende de un puente interno que solo está verificado hasta Resolve 21.0.x.

## Stack y modelos

- **Stack:** Python, Node.js, DaVinci Resolve Scripting API, ffmpeg
- **Etiquetas:** `video` `mcp` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [FFmpeg](ffmpeg.md) | 67.3k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |

## Enlaces

- 🐙 GitHub: [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
