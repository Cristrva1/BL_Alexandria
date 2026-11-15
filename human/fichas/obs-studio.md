[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ OBS Studio

> App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 79.3k | GPL-2.0 | C | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

OBS Studio captura, compone, codifica, graba y transmite video en Windows, macOS y Linux. Combinas en escenas la pantalla, ventanas, webcam, navegador y archivos multimedia, mezclas el audio con filtros y emites a YouTube, Twitch u otro servicio RTMP, o grabas a disco.

## Por qué destaca

Es el estándar libre para streaming y grabación de pantalla, con codificación por hardware (NVENC, AMF, QuickSync, Apple VT), cámara virtual, plugins y control remoto por WebSocket incluido.

## Cómo funciona

Su núcleo en C/C++ (libobs) compone en GPU las fuentes de cada escena y codifica con x264, FFmpeg o encoders de hardware. Se automatiza con scripts Lua o Python y con el protocolo obs-websocket.

## Instalación rápida

Instalador oficial en obsproject.com; también `brew install --cask obs` (macOS), `winget install OBSProject.OBSStudio` (Windows) o `flatpak install flathub com.obsproject.Studio` (Linux).

## Casos de uso

- Grabar tutoriales y demos de producto con la webcam superpuesta
- Transmitir en directo a YouTube o Twitch con varias escenas
- Grabar clases o reuniones para transcribirlas después

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas | lo que necesitas es montar o recortar el video ya grabado; usa `opencut` o `lossless-cut` |

**Limitaciones:** No es un editor: graba y emite, pero el montaje posterior requiere otra herramienta.

## Stack y modelos

- **Stack:** C, C++, Qt, FFmpeg
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `video` `audio` `ui` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LosslessCut](lossless-cut.md) | 45.9k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. |
| [OpenCut](opencut.md) | 98k | Editor de video libre con línea de tiempo, alternativa a CapCut, que funciona en el navegador y procesa en tu equipo. |
| [faster-whisper](faster-whisper.md) | 26.6k | Reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenScreen](openscreen.md) | 40k | App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a Screen Studio. |

## Enlaces

- 🐙 GitHub: [obsproject/obs-studio](https://github.com/obsproject/obs-studio)
- 🌐 Web: <https://obsproject.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
