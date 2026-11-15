[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ DaVinci Resolve MCP

> Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 4k | MIT | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Expone la API oficial de scripting de DaVinci Resolve como herramientas MCP para Claude, Cursor, Codex y otros clientes. Cubre montaje, organización del media pool, render, marcadores, color, Fusion y Fairlight, y añade análisis de medios que nunca modifica los originales. Incluye un panel de control local en el navegador.

## Por qué destaca

Cubre casi toda la API de Resolve, en un modo compacto de 37 herramientas o uno granular de 390, con operaciones protegidas. El instalador configura automáticamente una docena de clientes MCP.

## Cómo funciona

Servidor Python que se conecta a un Resolve abierto por su API de scripting externo y agrupa operaciones por acción para ahorrar contexto. Un servidor Node opcional edita archivos .drp/.drt sin Resolve abierto; ffmpeg y Whisper amplían el análisis.

## Instalación rápida

`npx davinci-resolve-mcp setup` (o `git clone` y `python install.py`). Antes, en Resolve Studio pon Preferences > General > External scripting using en Local.

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
- **Modelos / API:** No llama a ningún LLM: lo usa el cliente MCP que elijas (Claude, Cursor, Codex...). Whisper local opcional para transcribir.
- **Etiquetas:** `video` `mcp` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [FFmpeg](ffmpeg.md) | 66.9k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |
| [whisper](whisper.md) | 112k | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |

## Enlaces

- 🐙 GitHub: [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
