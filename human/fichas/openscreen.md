[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🖥️ OpenScreen

> App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a Screen Studio.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 40k | MIT | TypeScript | 2026-10-17 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

> ⚠️ Archivado en GitHub: ya no recibe cambios.

## Qué es

OpenScreen graba una ventana o la pantalla completa con micrófono y audio del sistema, y después te deja pulir la demo: zooms que siguen al cursor, webcam superpuesta, fondos, anotaciones, recorte y velocidad por tramo. Exporta a MP4 o GIF en varias proporciones. El proyecto original está archivado; su continuación activa es getopenscreen/openscreen.

## Por qué destaca

Cubre lo esencial de Screen Studio gratis y sin marcas de agua, también para uso comercial, y genera subtítulos automáticos en el propio equipo sin subir el audio.

## Cómo funciona

App Electron en TypeScript con render en PixiJS. En macOS y Windows captura con APIs nativas (ScreenCaptureKit, Windows Graphics Capture) y en Linux con la captura del navegador.

## Instalación rápida

Descarga el instalador desde GitHub Releases, o usa `brew install --cask siddharthvaddem/openscreen/openscreen` (macOS) o `winget install SiddharthVaddem.OpenScreen` (Windows).

## Casos de uso

- Grabar demos de producto para X, Reddit o YouTube
- Hacer tutoriales con zoom que sigue al cursor
- Exportar GIFs cortos de una función para la documentación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio | necesitas un proyecto mantenido; usa su continuación getopenscreen/openscreen, o `obs-studio` para grabación y streaming generales |

**Limitaciones:** El repositorio está archivado y sin mantenimiento (el propio autor advierte que no es de calidad de producción); la continuación comunitaria es getopenscreen/openscreen.

## Stack y modelos

- **Stack:** TypeScript, Electron, PixiJS
- **Modelos / API:** No usa LLM; los subtítulos automáticos se generan con un modelo de voz a texto local.
- **Etiquetas:** `video` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LosslessCut](lossless-cut.md) | 45.9k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. |
| [OpenCut](opencut.md) | 98k | Editor de video libre con línea de tiempo, alternativa a CapCut, que funciona en el navegador y procesa en tu equipo. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OBS Studio](obs-studio.md) | 79.3k | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. |

## Enlaces

- 🐙 GitHub: [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
